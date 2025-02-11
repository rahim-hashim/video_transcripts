---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 4721s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 493
Video Rating: None
---

# BI 038 Máté Lengyel: Probabilistic Perception and Learning
**Brain Inspired:** [June 19, 2019](https://www.youtube.com/watch?v=7YiHCAVV57A)
*  I can't say with complete confidence that AI is going to come up against a really hard
*  wall unless they really listen to us neuroscientists.
*  I can't make that kind of statement.
*  I think intellectually, I think it's going to be exciting even for them if they keep
*  kind of learning about the brain.
*  But whether it's going to be absolutely necessary for what they are trying to achieve, I don't
*  know.
*  Maybe not.
*  I think it's very much a wild west where everybody is riding around with their favorite theories
*  and the things that they think are the most important things, myself included, to work
*  on and understand that there is very, very little consensus still.
*  Welcome, everyone.
*  This is Paul Middlebrooks.
*  Or at least in all probability, it's Paul Middlebrooks.
*  I mean, given that you've heard my voice before, you're probably not too uncertain.
*  But if I talk like this, you may be more uncertain.
*  You may learn that most likely it is me just using a voice that I could use, but you're
*  glad that I don't.
*  Anyway, how does your brain represent a model of things that you perceive and learn and
*  the uncertainty about those things?
*  This is one of the questions that Mate Lengel asks himself every few minutes or so.
*  Mate is a computational neuroscientist at the University of Cambridge, and he's a senior
*  research fellow with the Central European University, interested in that and other related
*  questions, and he is my guest today.
*  He invented the famous McCulloch-Pitts model of a neuron.
*  Well, you'll hear more about that in a minute anyway.
*  During the show, we discuss things like what is a probabilistic internal model?
*  How might our brains represent probability distributions, which are useful for implementing
*  Bayes' rule and why Bayes' rule is important to implement?
*  What makes a theory worth pursuing experimentally?
*  The difference between the deep learning version of machine learning, as we normally think
*  of it, and the probabilistic model approach to machine learning, which is Mate's domain.
*  We talk about famous Hungarians and a lot more.
*  Mate is delivering a keynote address at the Cognitive Computational Neuroscience Conference,
*  so we talk about that a bit.
*  It looks awesome.
*  I hope you're going.
*  You can find links to the conference and everything that we discussed today at braininspired.co.
*  Okay, here in all likelihood is Mate Lingiao.
*  Mate, let me, hang on, let me just pull up my prior here.
*  Yeah, it's looking good.
*  It's looking like my prior suggests that this is going to be a good conversation and we're
*  both going to enjoy ourselves.
*  I'm going to collect evidence while we talk and then I'll have to check my posterior
*  when we're done here and see if we're still good.
*  Has anyone ever used that joke introducing you?
*  No, partly because I haven't given too many interviews, but yeah, but no.
*  Oh, thank God.
*  I was hoping that I would be original in that sense.
*  Mate, welcome to the podcast.
*  Thanks for being here.
*  Thank you very much.
*  It's a pleasure to be here.
*  So you are a part of the computational and biological learning lab at the University
*  of Cambridge and that larger group has subgroups within it which fall into either sort of the
*  biological learning side or the machine learning side and you head up the computational learning
*  and memory group of those subgroups.
*  Now, I could use a lot of words to describe what you do, but you would be better at it.
*  So in a nutshell, how would you describe what you do?
*  I'm a computational neuroscientist or a theoretical neuroscientist, which means I'm using mathematical
*  models to understand the brain.
*  So I don't do experiments myself.
*  I build theories that are kind of putting it into mathematical form and I collaborate
*  with experimental neuroscientists to test those theories.
*  In the experimental world, a lot of people, so I worked with non-human primates, with
*  monkeys and you'd often hear about monkey envy, right, with people who work with sort
*  of other mammals or other animal models and stuff.
*  I feel like it may be just my personal outlook, but I have theorist envy, I think, coming
*  from the experimental world.
*  Yeah, I think there's a lot of mutual envy in both directions and there are people who
*  go from one side to another.
*  I've always stuck to theory, I guess, because I know that I would be really crap at doing
*  experiments and I really enjoy doing theory.
*  So your first love, if I understand correctly, is mathematics.
*  You can correct me if I'm wrong, but you decided not to go into pure math and instead you decided
*  to invent the field of mathematical models of the brain.
*  Is that right?
*  I'm impressed by the amount of background check you've done.
*  It's my job, man.
*  That's really impressive.
*  Yeah, that's true.
*  When I went to high school, I went to a high school that had a special kind of mathematics
*  curriculum in Budapest and Hungary has a kind of traditionally strong kind of educational
*  system in mathematics and this was one of the top schools for that.
*  So I did a lot of math between the age of 14 and 18.
*  And so by the end of it, it was clear to me that I could do it, but I was not going to
*  become a mathematician.
*  But I also discovered that I really enjoyed kind of trying to construct mathematical models
*  for how different things in the world worked.
*  And in particular, I got fascinated by how the brain worked.
*  So I figured that the most exciting thing I could do would be to build mathematical
*  models of the brain, even though I wasn't aware of the time that such a field already
*  existed.
*  This is a case of parallel evolution, essentially.
*  It is.
*  I mean, I reinvented the McCullough and Pitts model, which is like the most first mathematical
*  models of how neurons might work.
*  I just ran some code to simulate something that I thought would be a reasonable model
*  of a neural network.
*  And later, years later, I learned that that was actually the McCullough-Pitts model.
*  But yeah, so with all the arrogance of an 18-year-old, at that point when I was finishing
*  high school, I decided that fine, I knew everything that there was to know about mass.
*  So it was time to learn about the brain if I wanted to do this.
*  So I went to biology, to do biology at university, which is a huge mistake because, you know,
*  a huge amount of biology has nothing to do with the brain.
*  And I was really not interested in a lot of that.
*  And plus, the kind of the way they, at least at the time they were training biologists
*  in Hungary, where I was still doing my undergraduate, was very unlike the way I preferred kind of
*  learning about stuff, which was much more kind of a mathematician's way of learning
*  about things like understanding rather than rote learning, you know, and driving things
*  from principles rather than just accepting facts.
*  So that wasn't an ideal fit for me.
*  But in the end, I just stuck with it and got on with it until through the end, essentially.
*  Oh, wow. Congratulations, I guess.
*  At least you didn't go into the medical field, you know.
*  No, no, I could have made the worst mistake.
*  That's right. Yeah.
*  But so there was never there was never a doubt in my mind that I would be that I would be
*  working on mathematical models.
*  So I never never occurred to me that I would be doing experiments even though I was in this biology.
*  Yeah. So 300 eye rolls later, you finally got through it and you can take it precisely.
*  So so Hungary has I mean, you're Hungarian, right?
*  That's right. Yeah.
*  So Hungary has this like sort of long celebrated lineage of mathematicians and quantitatively
*  minded people.
*  Is John von Neumann like the most well known, do you think the most celebrated of that in that line?
*  I mean, it would be hard to pick one.
*  I guess, you know, there are a few really well known ones.
*  There's the person after whom the the Mathematics Institute of the Hungarian Academy of Sciences is named Rényi,
*  who was a famous mathematician.
*  And then ever since, you know, even the current president of the Hungarian Academy of Scientists is a is a very famous
*  mathematician, Lovasz.
*  Before that, there was, of course, Poul Erdos of Erdos number fame.
*  Yes. And the list really goes on.
*  So there's yeah, there's been a there's been a strong tradition of mathematicians, but certainly von Neumann is
*  certainly one of the most famous ones and probably probably the best known internationally, I would say, very well deservedly, obviously.
*  I'm American. And as you know, as an American, I'm completely ignorant of the rest of the world.
*  So unfortunately, but but is it a is it a point of pride in Hungary to to go down that line?
*  I don't know. I mean, it's hard to generalize about Hungarians and their odd bunch.
*  They can be proud of a lot of things which which I would personally not be very proud of sometimes.
*  Now you have to name one name one of those things.
*  I'm going to I'm going to take a hard pass.
*  Exactly. But the but yeah, I mean, Hungarians like to pride themselves in general.
*  I don't know how much the general population knows about the unique status of mass, but in general, they like to pride themselves as having a lot of really smart scientists.
*  They tend to forget the fact that they drove a lot of those people outside, you know, out of the country, and they're doing it as we speak right now as well.
*  So this is not just a principle of nothing earned easy is worth knowing or you know, that whatever that principle is.
*  No, it's it's it's it's much more grim than that.
*  Yeah. So so I guess, yeah.
*  So my theory we're going to be talking about multiple things here today.
*  One of the things we're going to be talking about is the cognitive computational neuroscience conference where you're going to be giving a keynote address in just a couple of months here.
*  So just in conferences in general, so people talk about their scientific moments that they've had.
*  Is there like a moment from a conference that you can remember that you could that sort of has influenced you in a rather deep way that you can remember?
*  Yeah, I mean, there's always almost always moments at conferences that that I that I feel that this is the reason why I'm in the field to have these kind of moments.
*  The last one, actually, Nathaniel Dole is going to be another keynote speaker.
*  I think he his episode will have aired just before yours.
*  Great. Fantastic. So, you know, this just happens to be one of the last examples of this.
*  That's why I'm going to give you this. But he spoke at a workshop at the last computational and systems neuroscience conference in Lisbon this year.
*  And he was discussing his way of trying to interpret some rather kind of interesting, but somewhat confusing data from a colleague's lab about how dopamine might or might not represent prediction errors, which would be the kind of the classical theoretical account.
*  And actually, this colleague of him, Ileana Witten from Princeton, presented some of these results at the main meeting.
*  And I, you know, while I was listening to her talk, I had this thought that maybe this is not all that much in conflict with what we think with what we know about prediction errors.
*  And then later at the workshop, Nathaniel gave this talk about how he's kind of analyzing and looking at Ileana's data.
*  And he exactly did the things that, you know, that were in a very vague way, kind of in my mind.
*  And it just caused this aha moment that, oh, yeah, this is this is the way to think about it.
*  And, you know, it's not it's probably not going to change the world.
*  Although I think it's really cool with the experimental results and Nathaniel's way of thinking about it.
*  So I don't know how much is going to change the world.
*  Maybe it will, maybe it won't.
*  Maybe it's it's a small step for mankind, but it was definitely a big step for me just in terms of bringing that moment.
*  And that's that's really what I most enjoy in science in general, either through my own research or through someone else's research.
*  I don't really mind and I don't really care as long as it as it brings me that aha moment.
*  That's that's what I mean for here.
*  Oh, man, that's awesome. I actually just got goosebumps a little bit.
*  Seriously, on my arms, just thinking about it, you know, because I'm out of it.
*  I haven't had that in a while. I have to live vicariously through you guys now.
*  So that's interesting that it was Nathaniel Daw because, you know, I spoke with him and of course, he's not Hungarian.
*  And so he's not that intelligent. But we managed to get through the the interview somehow.
*  So so you work on a lot of things.
*  You also collaborate with people like Daniel Wolpert.
*  You've worked on active sensing, which is making movements to gather sensory information to perform some behavior better.
*  And I understand you'll be talking at CCN about probabilistic internal models during your keynote.
*  And we will dive into more detail later.
*  But really broadly, what are probabilistic internal models and what aspects of them will you be talking about?
*  Internal models are these representations that we use to summarize essentially our knowledge of how the brain of sorry, of how the world works.
*  And then we can use these internal models to to make predictions and therefore kind of adapt our choices, our movements and our decisions better.
*  So we can use these internal models to, for example, to to simulate what's going to happen depending on our actions.
*  Or we can use these internal models to make inferences about quantities that we can't directly observe, which would be relevant for us to make decisions.
*  So that's that's what internal models are.
*  And then the qualifier probabilistic means that the mathematical language that we use to describe the operation of these internal models is that of probability theory,
*  because the so-called normative argument is that that is the way it should be,
*  that the best way to use a model of the world to to perform inferences is to acknowledge that you can never be sure about your inferences and therefore to represent your uncertainty about those inferences.
*  And then the correct calculus to compute with uncertainties is given by the laws of probability.
*  And indeed, there is evidence that our brains, including animal other animals, do take into account all sorts of uncertainties that we have and at least approximately apply the rules of probability.
*  I live in the United States and I just realized that our president probably does not use these probability distributions, any uncertainty in any communication.
*  I'm sure I'm sure he does, if not at other times than when he is reaching to grasp a glass of water or maybe more like a can of coke.
*  He does unknowingly.
*  So we're doing this most of the time without even being aware of this.
*  Or when he or when his visual system interprets the world, that's also happening.
*  Now, whether in kind of conscious decision making he is doing this or not, that's that's an all different matter.
*  Yeah, let's not go down that road.
*  There's a lot of interesting literature, by the way, there's a lot of interesting literature on the pathologies of decision making and the pathologies of, you know, and how they might be related to kind of pathologies of these kind of probabilistic internal models.
*  So that might say something about your president.
*  We'll leave it at that for now, then.
*  OK, what do you think?
*  So, you know, within this realm of internal probabilistic internal model models, what is the most critical or intriguing question to you right now?
*  I guess in some sense, the million dollar question there is how does the brain do it?
*  And we know what? How can we how can we trace it down to the actual recordable and observable behavior of neurons and neural circuits and put our fingers onto it and say that?
*  Ah, so this is how it's happening in the brain.
*  This is how probability distributions at least approximately get kind of represented and manipulated in just the right way in the brain.
*  Is an approximate is a key word there, you think?
*  Yes, it is a key word. Yes, absolutely.
*  I mean, there is no I don't think anybody in their right mind would claim that the brain does exact probabilistic inference just because it's so it's so widely intractable that that's that's really a nonstarter.
*  So the real the question is what kind of approximation the brain uses to do this and how can we identify that in neural responses?
*  This is an interesting question for AI.
*  Hopefully we'll get to later in just doing doing this sort of thing in machines.
*  But so you're a theorist.
*  So far, I don't know how many times I've asked this, but it's 100% rate of a certain answer to this question I'm about to ask you.
*  And I'm imagining you're going to answer the same.
*  So I'm wondering what you think that we need more of right now to to get to this.
*  Do we need more theory or better theory or more data, more experiments, more better models, something else?
*  OK, so now you made me nervous that maybe I'll be the only one who doesn't know the right answer.
*  OK, we need both.
*  That's not the yeah, sure.
*  We need we need more and better of everything.
*  That's true. Yeah, yeah.
*  So, right. I think I think there has been incredible progress on the experimental end of things that we are starting to be able to record from an incredible number of neurons simultaneously with incredible precision.
*  That's on like that's on the technology end of things.
*  It's not necessarily the experimental side, I suppose.
*  Yeah, OK, fine. If that's what you mean.
*  OK, well, but so I think we I think there hasn't been necessarily so many kind of unequivocal breakthroughs at the theory end.
*  And in particular, we need just a better integration of the two.
*  Yeah. To really kind of make theories that produce testable predictions and then do the experiments.
*  The test those predictions about things that we really care about.
*  I may just be talking from the silo of my own show here because I talked to a lot of theorists and that might just be a product of the people I'm talking to.
*  But it seems like there are so many theories right now.
*  And I'm wondering if we've swung actually too far in the theory direction.
*  So, like, for instance, I don't want to spend weeks trying to understand someone's theory that ultimately will be a dead end.
*  Right. And so like what what is your criteria, for instance, for deciding whether a theory has merit to then design an experiment to really test?
*  Right. Like what keeps you reading a paper about someone's theory, for instance?
*  So there's very different kinds of theories.
*  Right. So in general, I keep reading on a paper if I feel that they are solving that they are solving a problem.
*  That I think is relevant and that I can't think of the solution of, you know, of the top of my head that, you know, that I feel like, oh, yeah, it's it's a relevant and the challenging question.
*  And so and then, you know, if it's a slightly different question, but, you know, if I want to convince other people that, for example, my theory that they should be interested in my theory, then then I also want to show that there is some
*  experimental data that it really makes contact with and at least kind of preliminary, even if the, you know, the ideal data set doesn't exist yet, that you can kind of do preliminary checks of the theory with existing data sets and it passes those checks.
*  So just very pragmatically, the way I collaborate with experimentalists is very often that kind of I start from a very kind of theoretical standpoint.
*  I identify a question which I think is relevant and interesting.
*  I develop a theory about it and then I start making predictions.
*  But before I ask my colleagues to do experiments for me, I do the best I can to show that existing data that the theory kind of makes contact with and is confirmed by existing data sets.
*  And only once I pass that hurdle, I feel like I should be in the position of asking for new experiments, for example.
*  So do you approach problems then through what lens do you approach problems through sort of just this really computational lens or like a normative lens starting with you see a behavior and you think about a normative issue or or an evolutionary, etc.
*  Yeah, I don't I don't really think about evolution explicitly, although I guess in some sense, all normative theories, maybe implicitly kind of make reference to evolution.
*  But the but yeah, I mean, most most of my work, I kind of build normative theories.
*  So I identify a computational problem that the brain needs to solve and which I think is challenging.
*  And then I kind of try to derive at least approximately optimal solutions to that problem.
*  And then I try to show that the way different bits of the brain work is very kind of analogous to those approximately optimal solutions.
*  And sometimes it's at the level of single neurons or synapses, and sometimes it's at the level of behavior.
*  These kind of problems, you know, sometimes these problems are how to pass information around in a reliable way in neural networks when the neurons have to communicate by spikes, which is kind of an which creates an information bottleneck between them.
*  So that's kind of that's a kind of a computational challenge that needs to be solved at kind of at the single cell or single sign of style.
*  And then but then there is questions of, you know, how do you gather information from the environment, which which you were referring to, where you really want to look at behavior?
*  And then, of course, the in the ideal case, we can connect these different levels eventually.
*  I don't really know how much crosstalk there is, like within your larger group at the University of Cambridge, but like I said at the beginning, you guys are kind of broadly divided into machine learning and biological learning sides.
*  How in your mind and in your experience, how can fields like cognitive science and neuroscience, computational neuroscience and the machine learning side, artificial intelligence side sort of on the pure machine learning, artificial intelligence side.
*  How can these fields work best together?
*  Yeah, I mean, I very much grew up in this, you know, when I did my postdoc that was in the Gatsby computational neuroscience unit, which is kind of one of the pioneers, if not the pioneering place for combining machine learning and computational neuroscience.
*  And, you know, part of the reason why I came here to Cambridge, because there was a group being formed here at the time that had the same premise that we want to combine these.
*  It's a great group. It looks like a great group, by the way.
*  And it's a fantastic and it's been a fantastic group.
*  Absolutely. And so, so there's different ways of combining strengths.
*  You can actually have collaborative projects.
*  And we have had examples of that when, you know, when, you know, people from the machine learning side of CBL and some people, some of us from the more biological learning and of CBL collaborated on a specific project.
*  But also just the way we organize life at CBL, which is not coincidentally very much like we, you know, life was organized at the Gatsby.
*  Several of us were at the Gatsby at some point so that we have joined meetings several times a week when we mix people and we have talks when these talks need to speak to all of CBL, both about our own research and about kind of anything.
*  There are talks when we talk about our own research and there are so-called T-talks when we talk about something that we found kind of scientifically interesting, but not very directly related to our own research.
*  And all of these need to be delivered in a way that they're accessible to the whole of CBL.
*  Like a common language or?
*  Yeah. So there is a common language and there is a common appreciation.
*  I think that's what's really important and that, you know, the faculty members of CBL are really talking to each other and really have a lot of appreciation for each other's work.
*  I think that's what's important to kind of keep exposing our groups to both sides of things.
*  So I think the best way for these fields at large to collaborate is to train people who really know about both these fields and really care about both.
*  I think that's the best investment we can make.
*  It's a lot to learn as a just a learner.
*  Yes, but learning is fun.
*  Yes, it is. But it takes time.
*  Hey, take a few deep breaths now.
*  Jorge Chang, hot damn I'm grateful for your benevolence in supporting the show through Patreon.
*  Find out how to do that for Chump Change.
*  If you find the show valuable, go to braininspired.co to do that.
*  I do have projects in the works that supporters of the show will have early and either free or super cheap access to when they're ready.
*  OK, back to the show.
*  Let's let's go deeper into your work on probabilistic internal models.
*  So you have published a sort of a series of papers in which this work builds, and I'm not actually sure which is the best place to point people just to dip their toe in.
*  If it's specifically about our own work, then somewhat paradoxically, maybe the best place to start is a review paper that we wrote back in 2010.
*  Oh, OK.
*  Which actually proceeded.
*  So we ended up writing papers in the wrong order.
*  So we first wrote the review paper for the things that we published years later.
*  That's awesome. Yeah.
*  Yeah. So we published.
*  So really, we should have done it in the opposite order.
*  But we first published the review paper back in 2010.
*  It was a TICS paper with me as the last author.
*  And then and then we kind of started publishing the actual result papers.
*  So maybe even today, in some sense, you know, so the 2010 paper in many ways precedes the work that we have done since.
*  Maybe they could read the 2010 paper and then just jump into the archive.
*  Your recent papers, like your paper in archive, for instance, and then and then jump around.
*  Who knows? I guess you don't do things in order.
*  So it doesn't really matter.
*  OK, so you work on these probabilistic machine learning or AI algorithms and you contrast that with sort of vanilla deep learning algorithms these days.
*  And I know that these two types of AI systems or models are not mutually exclusive per se,
*  but they there are still differences in them and that you favor this probabilistic machine learning side.
*  I'm wondering if you could just say a few words about the differences between what we think of when we think of deep nets and the probabilistic machine learning approach,
*  maybe with some examples of how one one would be better than the other, for instance, in certain situations.
*  Yeah, I mean, the the main difference is that the the focus in kind of in the probabilistic modeling field is on defining these
*  internal models and then internal models that we think the brain might be in the business of kind of implementing and how uncertainty is represented in these internal models
*  with regard to quantities of interest.
*  Whereas deep learning is really kind of a bunch of algorithms that work spectacularly and there is not necessarily much thought given to, first of all,
*  how uncertainty is represented.
*  And indeed, some of these systems can fail just as they can succeed very spectacularly.
*  They can also fail under some circumstances spectacularly.
*  And in fact, they can they can fail with high confidence.
*  Well, so just to be concrete, like most deep learning nets, the way that uncertainty is represented is just in the last layer, as in the probability that a certain category is the right answer.
*  Yeah, so yeah. So that's classical in the way you train these these these networks.
*  That's right. And so and so what I was referring to concretely is that you can you can engineer particular inputs to these networks on which they will fail.
*  They will widely misclassify those inputs and moreover, they will misclassify them with very high confidence.
*  Yeah. So they are not even aware that there's something going on there.
*  So the emphasis there is on is on algorithms, whereas the the the emphasis in the probabilistic world is more on models.
*  So really kind of in Mars terms, if I can use these terms.
*  Sure. Yeah, we talk about more plenty on the show.
*  So a lot of the probabilistic kind of modeling work is at at the computational level.
*  And, you know, deep networks are very much on the algorithmic level.
*  And, you know, a big question there, I think, is, you know, what's the actual computation?
*  And also just pragmatic, just practically, they are really good at kind of supervised learning.
*  And and in the case when there is lots of data around, we don't know yet how to make them really work well when the data when data is less, when you're doing supervised learning and so forth.
*  So there's various classically probabilistic methods have been quite good in kind of doing unsupervised learning.
*  And, you know, in conditions when there's not a lot of data, a more real world kind of condition.
*  Well, in many ways, it is a it is a more real world condition.
*  Yes. So I think there is there is strengths in both.
*  And in fact, you know, I I'd like to think about, you know, a lot of what's happening in deep learning is essentially developing approximate inference algorithms for kind of probabilistic internal models, if you like.
*  So I think that that can potentially be a really rich area of investigation, kind of trying to kind of work out these relationships.
*  And because, you know, at the end of the day, the brain is a big, huge, big, deep network, neural network with a lot of recurrency.
*  So there's no question that in as much as the brain is in the business of computing with probabilistic internal models, it is actually using neural networks to do that.
*  So I think it's a completely legitimate question to ask how, you know, how can we use the neural networks to to implement some of the computations that one needs to do with probabilistic internal models and how can we interpret already existing neural networks as essentially doing that?
*  Superficially, one of the attractive things about deep neural networks is that these units are inspired by neurons.
*  And so it looks brain like because these units are connected and have whatever synaptic strengths, weights between them.
*  And that's not something that probabilistic internal models really has going for it at the superficial level.
*  So it's an attractive thing to look at the diagram of a deep net, right.
*  And think, oh, it looks like a brain.
*  So from your vantage point, is that a, you know, is that a hurdle to get over?
*  So you're like, oh, it's, you know, that, OK, it looks like a brain.
*  And of course, these units aren't anything like neurons.
*  I mean, they are in the very, very limiting cases.
*  Right. So then you kind of have this hurdle to get over from to convince people that maybe the probabilistic internal machine learning models are the way to go.
*  Why would they be the way to go when we have neurons right here and it looks like the brain?
*  Yeah, absolutely, absolutely.
*  And I mean, look, a lot of the kind of the probabilistic modeling literature didn't even try to address what's happening at the level of neurons.
*  Because, as I said, it's a lot of it was is more about computation and behavior correspondingly.
*  So, you know, they didn't need to worry about it.
*  And indeed, when you want to know how those probabilistic computations are implemented in the brain, that's as far as I'm concerned, one big open question.
*  And I think there's a lot to learn from the recent successes of deep neural networks.
*  They can do amazing stuff. So maybe they can even they can even implement probabilistic internal models.
*  We just need to figure out how they do that.
*  So I don't I mean, look, if you want to talk about neurons, then then you need to get serious.
*  So in that case, I mean, some of the some of the things we have started doing, I'm very careful.
*  My research, my approach to to this is I'm usually quite I usually at least try to be quite careful and kind of address questions at the level of detail, which is absolutely necessary.
*  So if we are interested in how probability distributions are represented in neural activities, that might be an interesting question on its own.
*  And for that, you need to make predictions about about just that.
*  Neural responses, how you how you expect neural responses to vary under different conditions with different stimuli, with different expectations and so forth and so on.
*  But for that, you don't need to necessarily think about circuit mechanisms like what's actually happening, how should individual neurons integrate their inputs?
*  You really just want to make predictions at that point about the phenomenological behavior of neurons, but not the circuit mechanisms that bring about that.
*  Right. But that's you want to think about circuit mechanisms.
*  Right. And just to make the analogy clear, kind of the way people, for example, use deep neural networks is that all of this happens at once.
*  They have a circuit mechanism, so to speak.
*  They have just as you said, they have neurons that have synapses in them and all that.
*  And then they also have neural responses that they can relate to what's happening in the brain.
*  Right. They have they can show that look, I get receptive fields that look like the ones in the ventral visual stream and so forth.
*  So my approach is in some sense is much more kind of cautious and piecemeal, if you like.
*  So I first want to establish that we are thinking about the right representations.
*  And once we have those representations, then start thinking about the actual neural circuit mechanisms.
*  But I guess that's when my biologist of bringing kind of comes out and say that, OK, but if you really want to think about circuit mechanisms, let's get serious about it.
*  Then I start caring about things that a lot of the network stuff doesn't care about, like separation between excitatory and inhibitor cells, like recurrent connections, like neurons not having saturating fighting rates in the physiological regime and a lot of this stuff.
*  So at that point, I get more serious, I guess.
*  But I don't only ever get there if I kind of cleared some of the hurdles that come before that, at least for me.
*  So you're saying when you're equating seriousness with mechanistic level, I suppose, at the implementation level.
*  No, I think you need to be serious about you need to decide what it is that you are making a prediction about, and then you need to get serious about that.
*  So if you want to if you want to make predictions and claims about neural representations, then you don't necessarily need to make claims about your circuit mechanisms.
*  And that's fine. And then get serious about that.
*  Get serious about testing predictions about that.
*  Try to test those predictions under as wide conditions as possible and so forth and so on.
*  But if you really if you really want to say something about circuit mechanisms, then be serious about that.
*  And don't say that I'll have some tan age and I'll rely on my neurons being having saturated fighting rates half of the time, because that's that's not how the cortex works.
*  Really, come on.
*  That's not how the cortex works. Come on.
*  So you actually covered a lot of ground there, and I have questions related to a lot of that stuff.
*  One of the critical questions that you've asked is how are probability distributions encoded in the responses of neural populations?
*  So, you know, at the risk of repeating yourself, why probability distributions?
*  And, you know, maybe you can say a few words about what's important to know about the probability approach if we're going to get into a little bit more of the details here.
*  Yeah, so. So you want to have at least a crude representation of uncertainty about pretty much anything that you compute fundamentally because you always have to fuse information between different sources,
*  either from different sensory modalities or between previous experiences laid down in memory and your current input or different processing streams in general.
*  All the time we need to fuse information from different sources.
*  And the best way to fuse information from different sources, if you fuse in a way that you know your associated uncertainty about each of your inputs so that your output takes into account each of your inputs to a degree that is commensurate with the associated uncertainties.
*  So that's that's kind of that's kind of the starting point.
*  That's that's a very generic kind of law, if you like, of information processing systems that if you are fusing information from different sources, you better know the associated uncertainties if you if you want to fuse them optimally.
*  And that's a really very generic argument that can be kind of that can be applied to many different situations that are relevant for the brain.
*  And that's mathematically pure.
*  And at the level of behavior at the level of single neurons, really kind of quite widely.
*  And so if that's if that's the case, then and we believe that the brain is somehow trying to achieve that, at least approximately, then the question is, OK, so how does the brain, whenever it computes something, how does the brain represent the uncertainty associated with that thing that it has just computed?
*  And so that's that's what a lot of my research is about is trying to account that.
*  So why is Bayes theorem so important to consider?
*  You know, why is it such a strong candidate or so attractive as a basis for brain computations?
*  Well, because it's one of the two laws of probability theory.
*  And so there aren't many more out there.
*  You know, when I use when I teach, I usually say this, that there is really only two laws in probability theory, the law of summation and the law of multiplication.
*  Which together form Bayes?
*  But yeah, I mean, these rule in some sense uses both.
*  But really, it's it's mostly has it has to do with the law of multiplication that, you know, the probably the joint probability of two events is the probability of one event times the probability of the other event given this first event.
*  And that when you rearrange that, you get essentially Bayes rule.
*  So that's that's just that.
*  And yeah, so that's that's why Bayes rule.
*  Another way of putting it is that is that Bayes rule allows a system to do the most amazing thing, which is which is, by the way, I think how statistics should be taught in general statistics is usually taught as like the most boring subject with a big book of recipes about how to do t-test and whatnot.
*  But really, statistics and within that, a particular Bayes rule allows us to reason about things that we can't observe based on things that we can observe.
*  And that's amazing, right?
*  You make some observations and then based on those observations, you have a principled, rigorous mathematical way to reason about things that you can never observe.
*  I mean, that's just that's just the most amazing thing one can do.
*  It's beautiful. And it makes sense a lot of sense to me mathematically.
*  The way that you just stated that is really can land home very easily.
*  I consider myself to have a pretty strong mathematical background, not super high level.
*  You know, I took differential equations and something beyond that.
*  I can't remember now, but that was a while ago.
*  But, you know, talking with I had Federico Turkheimer on the show and he made the point that his students, he doesn't think that Bayes happens in the brain, essentially.
*  And this is really watered down because people have such a hard time even understanding Bayes rule.
*  And internally, I sort of chuckled because, yeah, like it's sort of like.
*  Every time I approach Bayes rule, I have I have to reset myself.
*  Look at the equations. Think about what the likelihood means.
*  Think about what the different, you know, given X or X, given Y.
*  And I have to reorient myself every time. And even then, it's like a fleeting understanding.
*  Why is it so hard for us to understand Bayes rule?
*  So I think there's two questions in there. So, first of all, yeah, I mean, I fully appreciate it.
*  It's hard for me to say why is it so hard.
*  It reminds me when people ask me better Hungarian is a difficult language.
*  And my answer to that is not to me, to me, you know, when I discovered Bayes rule for myself
*  and the whole idea of Bayesian inference, it was actually one of perhaps one of the biggest aha moments
*  that it just felt so natural and it felt like, yeah, of course, this is how this is the right way to think about these mathematical problems.
*  So to me, it's very natural. And to a lot of people, it's very natural.
*  And but I also know and very much appreciate that to a lot of people, it's not at all natural at all.
*  And I think, you know, it's just, you know, practice, I guess, makes perfect.
*  You know, if you work through a couple of examples that helps with kind of the I guess the bigger scientific question is that
*  so if it's so hard for us, there's no way that's happening in the brain.
*  But I've always found that an old argument, right?
*  We can we can throw, you know, people have, you know, people have been able to throw objects at each other and at animals
*  with incredible precision for millennia before, you know, Newton discovered the laws of mechanics.
*  So just because you can't like consciously access these rules and compute with them with pen and paper,
*  that doesn't mean that our brains aren't doing it in some way.
*  Right. Sure. Our brains have obviously been very well adapted to the basic laws of mechanics.
*  And we can, you know, we can make very good use of that.
*  Some better than others. Yeah. Some better than others.
*  But still. So, yeah. So I don't think I don't feel that is a particularly strong argument, I guess.
*  No, no, I'm not arguing that at all. I just I thought it was an interesting take.
*  But also, look, I mean, there is, as we know, there is a very there is a very strong and and and very fruitful tradition in psychology and economics that shows how all the fallacies and and wrongdoings that we commit when we try to manipulate probabilities in our hands.
*  Some Nobel prizes have been awarded for that. Yeah, we're terrible at it. Quite rightly so.
*  But again, you know, a lot of the times it is the case that that we can, you know, our brain can do stuff that we can't do, you know, somewhat kind of loosely stating it that, you know, when you sit down and think about it, you can't do something that, you know, then the same question is posed to you in the right in the ecologically appropriate way.
*  You can do it without thinking. Yeah, right. So, you know, most of us, including myself, you know, can't can't solve optimal control problems.
*  Our brain, our brains can solve them with quite amazing efficiency.
*  A lot of the times, you know, when we are reaching for a glass of water, here it is. Yeah.
*  Just as I was referring to this, you know, with respect to your president.
*  So, yeah, I mean, so our brains can solve all these kind of things that, you know, when we need to think about them, then we find really difficult.
*  But that, I think, is a is a very different question.
*  Sorry for that aside there, but I appreciate you going down that road with me for a second.
*  So, you know, back to the brain, I suppose, and the probability approach.
*  So these probability distributions give rise to a lot of noise, essentially, and which is a part of our brain response.
*  Brain activity is noise. So is this neural variability or noise, if you will?
*  Is it a feature of the brain or is it a bug? You know, does it serve a function?
*  Yeah. So, first of all, just because a system computes with with probability distributions, that doesn't mean that the system must be noisy.
*  Our computer, you know, we can we can compute with probability distributions on our computers that, you know, to a large extent, for all intents and purposes are noiseless.
*  And when you compute, when you solve a mathematical problem with pen and paper, with probability distributions, you know, you write down equations, kind of symbols without noise being there.
*  So just because you're computing performing probabilistic competitions, that doesn't necessarily imply that you need to be noisy.
*  And in fact, there have been a number of proposals for how the brain might represent probability distributions that do not require that the brain be variable.
*  So whether variability is really noise or that is nuisance or whether it's actually useful or so it's a bug or a feature, I guess that's how you phrase it.
*  I think for most of the time, it's a bug.
*  And, you know, if I have to make an evolutionary argument, my argument would be that probably originally it's noise.
*  But then as it so happens so often in evolution, you know, we try to make the best use of stuff that we are given.
*  So the way I see it and the kind of theories that my group develops is that they actually make good use of this variability for representing probability distributions.
*  And the way I personally think about it is that noise was probably already there and the brain somehow learned to make good use of that of that variability in order to represent uncertainty.
*  But that's just one one proposal out there.
*  Yeah. Well, you use like a sampling approach to test this.
*  You want to just speak a little bit about how perceptual uncertainty is related to neural variability?
*  Yeah. So the idea is, I think it's quite simple.
*  You know, classical theories of, say, vision or perception assume that neural activities represent one particular thing about the world.
*  Grandmothers, right?
*  Well, grandmothers or but even if you don't have a grandmother cell, you know, even if you are in the primary visual cortex, they represent the orientation of a line segment somewhere in your visual field.
*  Yeah. And sampling is essentially, you know, a rather simple minded extension of this idea.
*  And it essentially says that, no, the brain doesn't just represent one thing.
*  It tries to represent many possible things because it doesn't know exactly what's the orientation of that line segment out there in the world.
*  And it doesn't know exactly, I don't know whether it's whether it's a house with two windows or three windows that you see on a foggy day, for example.
*  And so it kind of switches between these different things.
*  It for a while, it represents one thing and then it represents another thing.
*  And then it represents a third thing.
*  And then it maybe it comes back and represents the first thing again.
*  So over time, it represents kind of different proposals for what might be out there in the world.
*  And it does so such that the frequency with which it visits these different possible interpretations is actually the posterior probabilities that an ideal Bayesian observer would infer for those possible interpretations of the world.
*  So it uses this kind of switching between different interpretations to to represent its uncertainty and to essentially say that I don't know what it is, but it's probably this thing.
*  And that's why I'm spending most of my time representing this particular interpretation.
*  But it could be this other thing or this this this third thing.
*  And so I'm also going to spend some time representing those those other things.
*  So it's representing uncertainty and at the same time gathering evidence for the posterior.
*  OK, so that's a different question.
*  Whether you are so evidence gathering or evidence integration is a whole lot of kind of kind of what that's a different algorithm.
*  That's a different computation.
*  But even even if the input doesn't change in principle for the same fixed input, you would want to represent the probability distribution, the Bayesian posterior over possible interpretations of that one fixed input.
*  And so the idea here is that the brain represents that posterior distribution by kind of walking through these different possible interpretations over time, even while the input is remains the same fixed thing.
*  Oh, I see. So you there's a there's a lot more we could actually talk about here.
*  And we don't want to go too deep, but you've developed models to to test a lot of these ideas and you've tested them in in data.
*  Like you've said, that wasn't necessarily designed experimentally for your purposes, but you have found these these data to to use.
*  So maybe could you just give us an account of the models that you've used and the data you've tested them with?
*  Yes. So so essentially, based on what I just told you, a research program follows from this idea quite naturally, which is the following.
*  Step one, think of an internal model that a particular area of the brain you think might be in the business of performing inference under.
*  Right. So if you are in, say, the primary visual cortex, as we are for most of the time, for most of the work we do, think of a probabilistic internal model that you think the primary visual cortex might be implementing.
*  OK, then for any particular so in our case, this would be kind of probabilistic models of natural images.
*  Right. So models that have some so-called latent variables, these are these unobserved quantities and kind of have probabilistic relationships between how they think those latent variables relate to the observable variables, which are the actual pixels in an image.
*  Right. So they assume that there's a particular probabilistic relationship between these things, the pixels in the image and these latent variables that which could be, for example, the intensities of different line oriented differently oriented line segments and things like that.
*  And does the model need to know the all of the different possible latent variables to consider since there could be an infinity?
*  Right. Yeah, that could be.
*  But but you can make educated guesses.
*  OK, at least first, I mean, there's a long history here.
*  There's a bug that we can build on, starting from things like the famous sparse coding model and things like that.
*  And so think of a probabilistic internal model that you think in our case, say, the primary visual cortex is in the business of implementing and then provide it with inputs that would be used as as inputs during an experimental, you know, in an experimental scenario.
*  Then given these inputs, you can compute what the inference what this probabilistic internal model would be inferring about the unobserved quantities, the latent variables given these inputs.
*  Right. So for each input, you have a big posterior distribution over these latent variables.
*  And so now you can say that fine, so I can go and look at experimental data because my sampling theory says that these posterior distributions over latent variables should be represented in neural activity in a very direct way.
*  Such that the wider these posterior distributions are, the bigger their variance, the bigger the variability of neural responses should be.
*  Because there's essentially a one to one correspondence between uncertainty and neural variability under this under this sampling hypothesis.
*  And so I can go and look at experimental data when indeed these different kind of inputs have been presented to animals while neurons in their primary visual cortices were recorded.
*  And I can ask, does the kind of modulation of neural variability happen in V1 that I expect based on my sampling based representation of uncertainty?
*  Yeah.
*  And the beauty of that is to a large extent, once you decided what this probabilistic internal model is going to be, which to a large degree only depends on the statistics of the inputs that you think that brain area is processing.
*  So kind of natural image statistics, for example, to a large degree, the probabilistic internal model that you're going to use and the details of that are decided by those things like natural image statistics.
*  And not anything about how the brain works per se.
*  And so you can almost make a kind of a parameter free prediction about what should happen in the brain with this idea that, you know, neural variability in the brain is going to represent uncertainty, posterior uncertainty under these probabilistic internal models.
*  So that's to me, that's an exciting approach that allows you to make really kind of strong predictions about neural observable phenomena.
*  How widespread do you think that these sorts of computations are in our brains? Right? Is this like a very general because we're talking about visual cortex and this is sort of the, you know, what the majority of neuroscience deals with essentially, and a lot of the data, you know, comes out of visual labs and stuff.
*  So, I mean, is this a principle that's just can be broadly applied to lots of different cognitive functions in the same way?
*  Yeah, so I think the basic principle in principle can be applied very generally, but there is specific challenges in different domains that are non-trivial with regard to this proposal.
*  So one challenge that is actually also quite generic, but it becomes more acute in some domains than in some others is what do you do with dynamically changing stimuli?
*  Or when the thing that you're trying to infer is itself dynamically changing because now there's a problem because you are already using time to represent a static probability distribution.
*  But now the distribution that you want to represent itself is changing dynamically.
*  So you would need to kind of to have two arrows of time here.
*  And so it's not clear how to use the same single time that we have to do both things, to kind of collect more samples from a distribution while also tracking how the distribution is changing.
*  And so that, for example, I think is quite a big open question.
*  But these are, I think, quite general computations and they can be applied all the way to decision making.
*  There is very interesting theoretical proposals from machine learning.
*  So this is yet another instance where we can learn a lot from machine learning potentially about how you can rephrase decision making as a central probabilistic inference and how there is a duality between control, sequential decision making,
*  and planning in particular and inference.
*  So you can use probabilistic inference to to solve challenging kind of planning problems as well.
*  And if that is the case, one thing that we are looking into right now in the lab, and we are not even the first to look at this, but we are probably the first to kind of combine this with a sampling based representation of uncertainty is how to use this to understand how planning might be happening in the brain.
*  Hmm.
*  Seems like a lot of people at CCN are talking about maybe talking about planning and and inference, so that it's maybe a common sort of theme.
*  And is this also related to the variability in decision making that's been shown to sort of reduce over time and collapse in just before decision?
*  So there's high variability and then the very via Fano factor variability reduces over time and then there's just a decision made.
*  Does it have any links to that?
*  Yes, it could.
*  It could.
*  I mean, we haven't in principle, it could.
*  We haven't really worked out these theories.
*  I think it's just early days.
*  It's early.
*  Yeah.
*  But but but these are but these are exactly the kind of data that that we will be looking at very closely and trying to relate to to our theories.
*  What's the what's the current goings on right now in the lab?
*  What are you guys working on right now?
*  That's there's a couple of things that we are working on, but maybe most directly relevant to what we've been just talking about.
*  We now really feel that we are in the position of trying to go down to circuit level mechanisms again in the context of V1 to be conservative.
*  But the and really kind of be serious about circuit mechanisms and ask, OK, so how might actual neural circuits in the primary visual cortex give rise to these representations that kind of give you samples from distributions?
*  Let's see how you feel doing real neuroscience, man.
*  No, I'm just kidding.
*  Exactly.
*  Yeah, yeah, yeah.
*  I'm actually quite excited about this.
*  I bet it brings together a lot of things that I'm that I'm quite passionately interested in, you know, like some of the details of how neurons and neural circuits work all the way up to this kind of relatively high level abstract concepts of progress.
*  It is.
*  I mean, it's interesting because reading all your material, you know, you really go down the rabbit hole, you really get sucked into it.
*  And then and then talking to you now and you kind of come out and think, oh, my God, it is early days.
*  So it's just so much interesting stuff going on.
*  So continue luck with with your research there.
*  Thank you. Thank you very much.
*  Let's go with an intermission quote today.
*  The fact that in science, we have to be content with an incomplete picture of the physical universe is not due to the nature of the universe itself, but rather to us.
*  So it will be Albert Einstein in the preface to Max Planck's book, Where is Science Going?
*  So you sort of alluded to this.
*  How do you think, for instance, there's a lot of these things that are going on in the world.
*  So you sort of alluded to this.
*  How do you think, for instance, artificial intelligence is most lacking with respect to incorporating what we know about neuroscience knowledge?
*  And this can be at the computational level as well.
*  Yeah, I don't. I'm I'm usually quite cautious about preaching, you know, about how AI should learn more about neuroscience.
*  I'm not sure they have to.
*  I think, you know, they were, you know, they've already taken inspiration and that's great.
*  Better going forward.
*  They must.
*  I'm not convinced.
*  I think, you know, it could be interesting, but I can't I can't say with complete confidence that, you know, AI is going to come up against a really hard wall unless they really listen to us neuroscientists.
*  I can't I can't make that kind of statement.
*  I think, you know, intellectually, I think it's going to be exciting even for them if they keep kind of learning about the brain.
*  But whether it's going to be absolutely necessary for what they are trying to achieve, I don't know.
*  Maybe not. Yeah.
*  I guess what what a lot of AI researchers realize is that even though now we have these amazing expert systems that very often use deep neural networks to what they want to do.
*  You know, even these systems kind of lack the flexibility and the versatility of biological systems.
*  And I guess that's kind of a challenge if you like at the definitely at the computational and probably also at the algorithmic level.
*  And then at the implementation level, I think there is some interesting questions there, which is these cutting edge systems right now.
*  If you really want to make them competitive with with humans, they just take up a lot of energy.
*  If you actually look at the you know, the number of watts that the supercomputers, you know, consume and and you know, our brain is famous of not consuming all that much energy.
*  Especially mine.
*  More than a light bulb.
*  And so I think if you want to deploy these, you know, really powerful AI systems in a way, you know, in in on autonomous agents with with kind of limited energy capacity, then maybe there are there will be some
*  implementational tricks that we can learn from the brain about how to how to do all this amazing competition in an energy efficient way.
*  And that's not something that that that a lot of AI people are thinking about right now.
*  You're thinking like neuromorphic computing, advancing and helping.
*  Yeah, yeah, yeah.
*  Yeah, but but I'm not I'm not sure that even the neuromorph.
*  Yeah. So I mean, I don't think we know for sure what aspects of of the neural hardware are going to be critical.
*  So just trying to mimic things.
*  I don't think we know for sure that we are trying to mimic with, you know, with the current neuromorphic systems, we are trying to mimic the really important things.
*  Why don't we try to mimic the fact that there are vesicles, you know, maybe that's important.
*  And we don't know yet.
*  Yeah, we'll see. But I think that that's an exciting bunch of questions there.
*  Yeah. Well, circling back to what we were talking about at the very beginning of the show, the idea of these probability distributions, right.
*  So it's intractable to consider all possibilities.
*  It's an intractable copy computationally for our brains because we want we have to conserve energy.
*  And yes, I believe as well that energy efficiency will become that's a limiting factor that will face eventually with AI systems.
*  However, we will be able to use orders of magnitude more energy than the human brain.
*  So it's not like we're going to be limited to the wattage of a human brain.
*  So maybe. Well, we could.
*  It just would make might take more time or more resources.
*  Right. We would have no water left on the planet or something.
*  Right. So so in like a Bayesian thinking like Bayesian right for an AI system to consider all the probability distributions.
*  Why would it matter? Why wouldn't they be able to consider a much wider range of possibilities and always make closer approximations?
*  I don't know to the point of infinitely closer to the solution.
*  Right. So we approximate our brains approximate and we eventually have to act.
*  I mean, do you see the limiting factor being much closer to human brains?
*  Like how much of a problem do you think this will be like?
*  Like why wouldn't an AI system be able to just make better choices using perfect Bayesian statistics?
*  So intractability comes in in different forms.
*  Right. So so exact Bayesian inference is intractable and not only computational complexity.
*  So like theoretical definitions of complexity don't necessarily relate directly to to physical resources such as energy.
*  But you can try to make a relation there.
*  But also, I mean, you you were kind of alluding to this in the way you ask your question.
*  And I think that's very important that that even if you have infinite amounts of energy, you might have you know,
*  you might have limited amounts of time to make a decision, in which case you you might want to just cut things short and don't wait until you've approximated everything to do infinite precision.
*  And so what those constraints are, I think, are going to depend on the particular situation.
*  And in particularly in future AI systems, what will be the really limiting constraints?
*  We don't know. But I guess we know better what to do with with with limited time,
*  because that's that's something that that is even in the abstract algorithmic world is quite directly related to to notions of computational complexity that that people care a lot about in AI.
*  Whereas the amount of physical energy that you have is probably is probably not so obviously related to notions of complexity that come up in theoretical in theories of computation that most AI people would know and care about.
*  So that's that's why I said that these these constraints might might might become more relevant for the underlying.
*  But you might be right. And it might be that we will, you know, we will just develop new energy sources such that we never need to be concerned about, you know, limited energy, for example, for our agents, even if they are kind of mobile and can't be connected to constant energy supply all the time.
*  We don't know. Maybe we will discover cold fusion next year. And then, you know, all these problems will be solved.
*  You should just go ahead and write the review paper on it and then it will happen.
*  That's right. Yeah.
*  What do you think about from the other side? How do you think neuroscience? What do you think neuroscience can learn? Or what's most relevant? Something right now that would be really relevant that neuroscience could learn from AI?
*  I think there's I mean, I think there at least I personally I see much more clearly all the things that that neuroscience have or has already learned from from AI and all the things that that it still can learn.
*  I mean, just the just the way so there's the kind of the theory side of things when when you can learn about how to mathematically formulate problems, how to how to build kind of mathematical theories about issues of computation and things like that.
*  But also now, you know, AI is just giving us a lot of algorithms that work amazingly. And so there are, you know, there should be a huge source of inspiration for neuroscientists.
*  But also they just give us very practical algorithms for a lot of data analysis problems that we need to solve in in your sense.
*  So we can certainly learn those things.
*  And in terms of what's I think to me, again, this is my very kind of personal view.
*  I think there's a lot of interesting stuff going on in in machine learning where people are really trying to get a better theoretical understanding of why deep networks work.
*  Right. That that is very much very much an open question.
*  Why why can they generalize in such powerful ways when they really ought to be terribly overfitting, for example.
*  Right. And then and why do they fail then suddenly so miserably just as we talked about earlier, suddenly in some other conditions.
*  So right now, a lot of it, you know, and people in the field themselves say it's not like I'm as an outsider, I'm kind of diminishing their their great achievements.
*  But, you know, people in the field themselves will will admit that, you know, a lot of it right now is somewhat of a black art and it works and it thrives on all the amazing things that that that you can do just in practical terms.
*  But but there is a lot of I think there is a lot of dissatisfaction in the field that we just we just that the theoretical understanding of what's really going on is kind of lagging behind.
*  And I think there's going to be a lot of interesting things coming up in that domain where people are really going to build a better theoretical understanding of why these systems work and why and when they don't.
*  And I think we as neuroscientists will also have a lot to learn from that.
*  So we should really keep you know, stay tuned.
*  Well, a hundred years from now, when people are writing reviews and historical articles about about us these days, what are they going to write about in this little era of neuroscience and AI?
*  How are they going to view it?
*  Oh, I think they will.
*  So I guess I have a pretty strong opinion on that.
*  I think they will view it as as the wild west.
*  Oh, still.
*  Still.
*  Yeah.
*  I mean, yes, very much in terms of just in terms of the of the social dynamics of neuroscience.
*  Yeah.
*  Today, I think it's very much a wild west where everybody is riding around with their favorite theories and you know, the things that they think are the most important things, myself included, to work on and understand that there is very, very little.
*  Consensus still.
*  So it's we're just, you know, it's just a very mature field in many ways.
*  And so I think that's how it's going to be seen.
*  It's going to be seen as the dawn of of a proper science, but which is not a proper science yet in many ways.
*  So the wild west has good and bad connotations.
*  Do you think it favors the good connotation or the bad?
*  Because a lot of creativity.
*  It's both.
*  Yeah, there's a lot of creativity, but there's a lot of.
*  Unnecessary blood as well.
*  And a lot of mavericks and a lot of mavericks as well.
*  Yeah.
*  OK, good.
*  So you're a young scientist.
*  But if you were, I think I don't know if I can't is young anymore.
*  You may not feel young.
*  I'll take it as a compliment.
*  Yeah.
*  But if you did start over, what would you do different?
*  How would you proceed?
*  I would probably not stop learning math.
*  Wow, really?
*  In high school.
*  Oh, yeah.
*  So I would.
*  Yeah, I would make sure that I take an undergraduate course where I, you know, where I'm taught
*  much more formal theory than what I was taught in during my biology undergrad.
*  And is that what you would advise like a graduate student or something to do as well?
*  Yeah.
*  Yeah.
*  Do as much quantitative training as early on in your career as possible.
*  It seems like you've done a really good job of exploiting your strengths, right?
*  You're capitalizing on your strengths with this sort of quantitative background, even
*  though you just said you would even have even more.
*  But what do you think the right balance is in your field between exploiting your strengths
*  versus improving on your weaknesses?
*  I really don't feel I'm in a position of giving advice to anyone.
*  I think it varies widely between individuals.
*  I personally have always enjoyed learning new stuff.
*  So, you know, a lot of so even though, as I said, during my undergrad and even PhD,
*  I didn't learn an awful lot of new theory.
*  Then during my postdoc, I actually made the effort and learned essentially as much as
*  I should have learned during the years preceding that.
*  So I think there's I guess the lesson and something that I, you know, that I experience
*  up to this day is that there is it's never too late to learn new things.
*  And it's a lot of fun.
*  It's just a lot of fun.
*  You know, again, going back to those moments, I don't care even if it's textbook material.
*  If for me it's something new, then it's great.
*  I don't need to be the first person to understand something or think about something as long
*  for me.
*  This is the first.
*  You don't care that you invented mathematical models of the brain.
*  Yeah.
*  So just getting back to the conference real quickly, is there anything in particular you
*  want to take that you have in mind that you'd like to be able to take from CCN?
*  Yeah, I'm really looking forward to a lot of the talk.
*  I mean, you know, the program is not up yet.
*  All I can see are the or at least I couldn't find it, but I can see the invited speakers
*  and I'm really looking forward to their talks because I know that all of them are amazing
*  people.
*  And so I'm actually really excited about all the things that I'm going to learn from
*  them for sure.
*  And then I'm sure there's going to be kind of contributed talks and posters that will
*  be also very exciting.
*  But those I don't know about yet, but the invited speakers, I at least know the names
*  of, so I can make some inferences there.
*  Like even Tim Behrens, I mean, he's going to be there.
*  You could skip his, right?
*  Yeah, maybe not Tim.
*  He's really a boring guy.
*  So maybe.
*  Okay, fine.
*  Okay, good.
*  Thanks for that.
*  What's a what's a special talent that you have that not many people know about?
*  Theater.
*  Attending theater or performing theater?
*  About directing theater in particular.
*  Directing theater.
*  Oh, I had a theater group which I directed during my PhD.
*  Oh, gosh.
*  You will have to have you on my other improv podcast.
*  So no, I'm just kidding.
*  Okay, finally, what's something that you used to believe that you consider naive now?
*  I believed that what makes you the most important thing that makes you a great scientist is
*  being smart.
*  And I think that's naive.
*  And that was it to it.
*  That was the thing.
*  And if you were smart, you could be a great scientist.
*  If you were not super smart, you could not be a great scientist.
*  How's that changed now?
*  I consider that there's a lot of other things.
*  There's other things that you need to be successful in science, which is not necessarily
*  the same thing as being a great scientist.
*  Yes.
*  But even to be a great scientist, you need other things than just being smart, perhaps
*  with the exception of really pure things like mathematics.
*  But in your sense, things are different.
*  So you just need a lot of skills other than just being smart.
*  Okay, hang on.
*  Let me pull this up real quick.
*  Oh, holy hell, my posterior looks great, man.
*  Thank you for your time here today.
*  I collected so much evidence.
*  It's so much improved.
*  Happy to have contributed to your posterior.
*  Yeah.
*  And I'm not talking about my anatomy.
*  I'm talking about my probability distribution here.
*  Yeah.
*  Thanks, Matei.
*  This has been fun.
*  I appreciate it.
*  Cheers.
*  I really enjoyed it.
*  Thanks very much.
*  Brain Inspired is a production of me and you.
*  You can support the show through Patreon for a microscopic two or four dollars per month.
*  Go to braininspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying advertisements
*  like you hear on other shows.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thanks for your support.
*  See you next time.
*  Bye.
