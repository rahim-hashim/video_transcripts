---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4397s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 1826
Video Rating: None
---

# BI 083 Jane Wang: Evolving Altruism in AI
**Brain Inspired:** [September 05, 2020](https://www.youtube.com/watch?v=63kBRoq4X7s)
*  Keeping in mind that the point of neuroscience is not to engineer something is important.
*  And that allows us to sort of identify what aspects of it are important.
*  I think it will continue to be important though because the brain continues to be sort of the only example
*  of this kind of general intelligence that we want to construct in AI.
*  Most likely the most exciting kinds of AGI that we're going to come up with is going to be tightly interconnected with humans
*  and is sort of going to be interwoven throughout our society.
*  And so we'll need to have a good understanding of what induces cooperative behavior.
*  There's always challenges. There's always sort of internal conflicts between our altruistic impulses
*  and also acting in our own self-interests.
*  This is Brain Inspired.
*  Hey guys, it's Paul.
*  Who do you think would win in an altruism competition between you and an AI agent?
*  If that AI agent was created by Jane Wong and her team at DeepMind, you would have some stiff competition.
*  Today my guest is Jane Wong from DeepMind, and that is one thing that she's been working on lately.
*  We talk about her multi-agent reinforcement learning work to explore how cooperation can emerge from
*  interacting reinforcement learning agents, which will become more important as AI becomes even more ubiquitous
*  than it is now and has to work well with us and with other AI agents.
*  It's also a potential way for us to learn about our own altruistic potential and how we might better reach that potential.
*  The altruism or cooperation work is actually the last topic that we discuss.
*  To get there, we review the meta-reinforcement learning framework she helped develop,
*  where a recurrent neural network's weights were slowly trained on a set of tasks,
*  such that the recurrent network could then by itself learn other related tasks without any more synaptic weight changes.
*  And there's a story there about how these processes map pretty well onto what we know
*  about how dopamine and the prefrontal cortex operate in brains.
*  And before any of that, we discuss at length her experience working at DeepMind,
*  having come from an academic background in cognitive science, complexity science, and neuroscience.
*  And we focus a lot on the relationship and exchange between neuroscience and AI,
*  since Jane has plenty of insight about both sides.
*  Show notes at braininspired.co.uk slash podcast slash 83.
*  If you value this podcast and you want to support it and hear the full versions of all the episodes
*  and occasional separate bonus episodes, you can do that for next to nothing through Patreon.
*  Go to braininspired.co.uk and click the red Patreon button there.
*  My thanks to Jane for a very enjoyable discussion.
*  These are exciting times in the study of and in the engineering of intelligence.
*  Thank you for listening.
*  Was it over a year ago that I'd asked you to come on?
*  Yes. And yeah, I'm really glad that we were finally able to connect on this.
*  I was going back through your recent episodes and I noticed that like almost all of your,
*  the people that you've had on are people that I really like love their work.
*  I really love to follow their work and the scientists that I really respect.
*  And so it just kind of feels like it's all the kinds of topics that I'm most interested in.
*  So I'm really happy to be able to come on.
*  Well, I mean, you fit right in, of course.
*  But it was funny because you seemed surprised that I reached out again.
*  You thought I'd maybe forgotten about you or something.
*  But no, not me.
*  Oh, well, I'm very happy that you did.
*  Anyway, it's good to have you on.
*  And we're here today. Of course, we're going to solve intelligence.
*  Isn't that DeepMind's mantra still?
*  Yes, it is.
*  Technically, our mission is to solve intelligence and then use it to solve everything else.
*  And of course, that last bit is quite overloaded.
*  But I think it's very important.
*  Well, you had a, I guess, brief career in academia, right?
*  And then transitioned to DeepMind.
*  So you've been on, of course, DeepMind is not really not academia.
*  You wouldn't call DeepMind industry.
*  But I want to talk just for a few minutes about what the experience of transitioning was like and what DeepMind is like relative to academia.
*  So what was your experience?
*  I mean, you say you say brief, but it doesn't feel like academia was very brief for me because if you think about it,
*  I've really been in some form of academic environment for like 20 plus years at the point.
*  So I did a postdoc before going to DeepMind.
*  That's you know, in 20 years, that's going to look pretty brief, I think.
*  I guess so. Yeah.
*  I guess maybe relative, relatively speaking, it's a bit brief.
*  I think one of the main things that's, you know, one of my main experiences about transitioning to industry from academia was at first just kind of being unsure and a bit scared about what it was going to be like.
*  Just leaving academia is quite a daunting thing when the whole time that I did my PhD, my postdoc, it's sort of all that I know.
*  And sort of the whole point of being there was kind of to drive you towards getting it like a faculty position.
*  Yeah. Well, let's let's pause just for a second.
*  So people know you have a background in complexity and in physics and that kind of led you into the neuroscience work.
*  Right. Is that was that the it's the yeah, I've had a pretty circuitous path to get to where I'm at.
*  I think everybody says that Jane, everybody says that.
*  OK, it's probably true.
*  It's not. Yeah. Yeah. Maybe it's not that securitas.
*  But I started out in physics.
*  So I did my PhD in applied physics where I was more doing computational neuroscience.
*  So simulation simulating complex dynamic networks, which are supposed to mimic like memory consolidation and memory interaction within the brain.
*  And so from that, you know, I also worked a bit in complex systems, in graph theory, more on the dynamical systems side.
*  Yeah. So but I didn't get into cognitive neuroscience until my postdoc.
*  Oh, OK. But you were working with.
*  Well, I'd have to look at your CV again and your publication record.
*  I thought you did a little bit of neuroscience work also in graduate school, no matter.
*  Well, it was I would say it was I would call it computational neuroscience.
*  It was, you know, setting up like neural like spiking neural network models.
*  So but it wasn't that experimental.
*  I did a bit of experiment with like cell cultures and things like that.
*  So I want to change this notion of what people think of when they when you when one says neuroscience.
*  When I hear neuroscience, I don't think experiment.
*  I think of all of it. I think of the theory and the experimentation, the modeling to meet computational cognitive.
*  It's all neuroscience to me. And I don't know why it's not that way for everyone else as well.
*  Yeah, it is kind of weird. I think once you get into the field, people love to put labels on things and say, oh, that's not neuroscience.
*  That's cognitive science or that's psychology or that's right.
*  But I'm sure like, yeah, from the outside, it all just looks the same.
*  So, I mean, I I definitely did work in neuroscience in in grad school, but I say it's a completely different kind of neuroscience.
*  So I wasn't super I was I wouldn't say I was an expert on sort of the brain regions and more of the cognitive aspects.
*  Like, like I had very specific knowledge about hippocampus and how to model it.
*  And that was sort of my experience of it.
*  And then in my postdoc, I got a much broader sort of perspective about neuroscience and cognitive science and doing human experimentation, which I mean, maybe this is a bit of a tangent.
*  But to me, I feel like the cognitive science is a bit closer to A.I.
*  Than more of the maybe like electrophysiological type experiments.
*  Yeah, yeah, I want to talk about this, too, in terms of like Mars levels and things, because I think that when people think of neuroscience, they also think of Mars implementation level as if neuroscience maps directly onto the implementation level.
*  And, you know, what you're saying is that cognitive science would be more like the algorithmic and computational levels of analysis.
*  But I don't know, maybe this is a fault of mine. I see them all as spanning everything.
*  When I think of neuroscience, I don't just think of recording single neurons, you know, so maybe that that's a fault of mine.
*  I wouldn't I mean, I think everybody could interpret it the way that they that they prefer.
*  I think it's more just a matter of scale and also maybe the the thing that you're saying.
*  So in cognitive science and more like related to psychology, you're kind of studying the the cognitive function itself.
*  You're trying to study, you know, what do people what are people actually doing in this particular situation?
*  What are they actually learning?
*  Whereas if you are moving more to like molecular neurobiology or things like that, you're looking at the mechanisms.
*  And so it's kind of like a slight difference in terms of the thing that you're studying and your motivation.
*  And I think for me, AI is more about the cognitive function itself rather than the implementation, at least with regard to neuroscience.
*  Yes, I can see that.
*  I just think that one should always have the big picture, you know, across level in mind.
*  Right. Well, you're it's good to keep the context in mind.
*  Yeah. Yeah. Why are we doing this? Yeah, for sure.
*  So anyway, so then you had this background and you went and you know, you did a postdoc.
*  Yeah, I did. So I performed psychological experiments with humans looking at learning and decision making and memory and also doing neuroimaging.
*  So with fMRI and EEG and also a bit of work with transcranial magnetic stimulation, which is a kind of noninvasive stimulation that you can do with with humans.
*  Have you ever been stimulated? I have. Yes, of course.
*  I hear it's like a like a rubber band pop. It depends on the kind of stimulation protocol.
*  But what was I say? Like we're all involved in each other's experiments.
*  So, of course, other researchers in the lab and like in their experiments in their mind.
*  So, yeah, I've had TMS done plenty of times.
*  It's so I was doing repetitive stimulation for the most part.
*  And in that case, you know, you're stimulating at maybe like 10 or 20 hertz per second.
*  So it's kind of a little bit of a buzzing.
*  And if you do that long enough, it can start to hurt.
*  But just if you just do a single pop, it just it doesn't hurt at all.
*  And that can do crazy things like move your thumb or like maybe even move your entire arm.
*  Does it have you? Have you had the experience?
*  Well, first of all, we should just briefly say what what TMS actually is.
*  So you're actually there's a thing that's sitting out just outside of your head.
*  And there's a magnetic pulse that's that you can use to like target very specific locations in the brain and stimulate neural activity or ablate neural activity.
*  I don't know what the most recent. Yeah, exactly.
*  Yeah. So depending on the kind of protocol that you're using, you can either do inhibition or excitation.
*  And you're essentially just like inducing electrical activity in a very focal part of the cortical surface of your brain.
*  And yeah, and you can find all sorts of effects from affecting people's judgments to affecting memory to, you know, maybe you can also even induce like visual effects if you do it in, you know, occipital cortex.
*  So, yeah, it's really interesting.
*  And it's a it's a hugely kind of growing and exciting field of study right now.
*  Did you feel like so did you have a thumb twitch? What was your experience?
*  Did you did it elicit behavior in you when you did it?
*  Well, so the thumb twitching is actually what we do to try and get a motor threshold because it turns out for every single person, depending on, you know, just the thickness of your skull or other biological aspects, you will have a different.
*  Laziness. Yeah.
*  Yeah, maybe. Yeah, yeah.
*  Just, you know, every person is different.
*  So so I'm going to have a different sort of threshold at which my my thumb is going to react, for instance.
*  So we sort of use that to calibrate the amount of induction or like, you know, energy that we want to be putting in.
*  And then we use that and then we put it over a part of your your brain that we are interested in studying.
*  So for us, it was to try and induce like memory formation or to enhance memory, just like associated memory.
*  And so and you can also do things like try or look at the effects on functional connectivity, which is what I did, because we understand that, you know, you have these different kinds of networks like functional, functional brain connections in the brain where different regions of your brain are sort of functionally connected to each other, meaning that they're sort of seem to be interacting if you analyze the activity.
*  So you can we can detect changes in in that network as a result of doing stimulation.
*  Oh, that's cool. But anyway, OK, so you're a veritable neuroscientist at that point.
*  And then DeepMind steals you away. But you were you were starting to say that you were a little wary of leaving academia.
*  Yeah, I mean, I think the main thing that sort of gets like drilled into you in academia is that like if you leave, you'll never never be able to go back.
*  You know, like there's kind of this like weird culture where it seems like if you leave, then, oh, you've just given up or something.
*  And then like you'll never be able to come back. And so it feels like you're closing the door.
*  But I that wasn't my experience at all.
*  I feel like maybe it's just because it's the kind of place that I went.
*  But but DeepMind is I would say it's like 75 percent research environments.
*  Yeah. So I publish now like more than I ever did.
*  I'm able to be fully in the academic world and to keep up to date on whatever kind of literature that I'm interested in.
*  I mean, I guess the kind of research that I'm doing is definitely different.
*  I'm not doing so much of the experimental neuroscience side of it, although we do have a lot of collaborations with academic labs.
*  So we, you know, we can publish on that kind of stuff or like work with people that are doing those kinds of experiments.
*  And a lot of those are coming out as well from our from our team.
*  So you haven't you haven't really worked in the industry then.
*  I don't know, because DeepMind is this weird in between kind of place.
*  And so I don't know if it's even fair to ask you what it's like outside of academia, because it's like you're halfway outside or something.
*  I don't know how would you characterize it? Yeah, I think that's right.
*  Yeah, you know, our sort of model is more like Bell Labs, I think.
*  Yeah, we try to like model it after those kinds of like research institutes that are like primary research institutes.
*  And I say the main differences to academia are essentially that we don't have to worry about funding and grants, which is amazing.
*  I never really enjoy that part of it.
*  And we can also collaborate much more readily, I think.
*  So we don't have this notion of sort of like individual labs and, you know, that work very closely within themselves and then like kind of sometimes collaborate with other labs.
*  But it has to be sort of set up and they can take a while for us.
*  You know, I can reach out to somebody else on a different team and just start work on a project just, you know, immediately.
*  And there are so many people that do different things at DeepMind that it's really easy to sort of reach across fields or like across like or to find somebody else with a different field of expertise that can help me do something.
*  So that's almost like in some cases it can be a difficulty to kind of just stop forming new collaborations.
*  Because at some point I feel like I have too many things on my plate and I need to sort of like narrow down and just say, OK, no, I got to I got to like focus here.
*  Decadent. Yeah, exactly.
*  What's the general atmosphere like? Everybody happy? DeepMind? Is everyone optimistic?
*  And or and we'll come back to this in a little bit when we talk about the progress of AI.
*  But relative to an academic lab, let's say, and we all have only had experience with a few different labs.
*  So, you know, we have a small in to say, can some labs or have very different character and flavor than other labs?
*  But does it feel looser? Does it feel more businesslike than an academic lab or about the same?
*  I imagine it's about the same. The only way I can describe is it feels like it moves faster.
*  But I don't know if I'm conflating that with just like the fact that I've switched from neuroscience to AI because it could be that.
*  Yes. Yeah, I just move fast everywhere.
*  I can't imagine what it's like to be a grad student in AI right now and to have to submit to conferences every few months.
*  It just seems like, yeah, it seems so intense.
*  But it does feel like it moves faster.
*  Papers can, you know, projects can be done and out in a few months as opposed to, you know, before I'd work on something for a couple of years.
*  There still are those kinds of projects at DeepMind that, you know, are large scale and we want to do right.
*  And so we'll work on them for a while. And, you know, they'll be like a like a large piece of work, you know, like AlphaGo.
*  And that came out. A lot of people worked on that for a long time.
*  But the rewards, I mean, you work a lot of reinforcement learning and the rewards come much quicker in AI than in neuroscience.
*  Oh, I don't know what you mean by rewards.
*  Well, if your project can be done in a month or two months relative to a year or two years.
*  So there's a longer delay in neuroscience between when you begin and when you are, quote unquote, rewarded with a publication or, you know, whatever.
*  I guess, yeah, that's true. And in fact, in AI, you can just sort of release your work on archive.
*  You don't even need to work, wait for the whole five cycles of review, like submitting to different journals and things like that, which we've all gone through.
*  Yeah, that's happening in neuroscience now, too. And I don't know if maybe AI has led the way there.
*  But so it sounds like the transition was fine. You had slight reservations, but I'm sure you're glad you did.
*  Oh, yeah, yeah. No regrets whatsoever on that front.
*  So, you know, science is this beautiful thing, but it's also frustrating in that the more you learn, the more you understand how little you actually know how much more there is to learn, essentially.
*  I'm wondering, you know, how your experience in neuroscience and now in AI has changed your perspectives on on either neuroscience and or AI.
*  You already talked about how nice it is that AI goes faster, which, yeah, I just was jealous of even when I was still in neuroscience.
*  Well, I'm not going to make a value judgment about that. I don't know if it's nicer or not nicer.
*  You know, it's just faster. Sometimes I miss like being able to spend, you know, five months on one paper and just like think very thoroughly about it.
*  But has it changed your, you know, when you do you do you have less reverence, more reverence for the brain, for instance, things like that?
*  So I'm definitely much more informed about AI machine learning than I was a few years ago.
*  And I think having that kind of background allows me to see neuroscience in a new light because you can sort of compare the two.
*  In particular, the the goals and motivations of AI are almost like the opposite of what they are in neuroscience.
*  Maybe not the opposite, but it's coming at it from a different perspective.
*  So in AI, the point of it is to try and figure out how can I engineer a system such that I can create learning that's, you know, either human like or something that can do superhuman kind of cognition like, you know, Placo or something.
*  Whereas with neuroscience, you're you're taking a system that already can do that, you know, human level intelligence or like even animal level intelligence.
*  And you're trying to figure out you're trying to dissect it down and see, like, well, what is that system?
*  You're trying to characterize that system. So there's sort of like two sides of the same coin to me.
*  And it's very interesting for me to think about it like that, because then that can tell you much more.
*  You know, what can I take away from neuroscience research for AI? What should I take away from neuroscience research?
*  And what are the limitations and what I can take away?
*  So, yeah, so I think that that's, you know, allows me to, I guess, form like manage my expectations of what what you can take away from neuroscience.
*  I think a lot of, you know, AI researchers that I've spoken to and have talked to over the years maybe expects like they're a little bit disappointed that neuroscience just doesn't like give them an answer about like, well, how do you how do you program this particular aspect of cognition?
*  Right.
*  You know, why can't we just take like what we know in neuroscience and just sort of like implement it?
*  Well, the reason is that it's not neuroscience isn't trying to engineer anything.
*  All it can do is sort of tell you this is how one system did it or or not even that.
*  You know, like it's such a it's such a hard thing to to dissect down because there are so many levels that you can figure out a neural system at.
*  You know, you can talk about the cellular level, you can talk about the the neuronal level, talk about the biological level, you can talk about the the functional level, like functionally, what what is it trying to do?
*  And so you have to not only manage your expectations, but also identify the right level that you want to be taking these these lessons from.
*  So I don't think it particularly helps you to be looking at, you know, action potentials and specifically how signals are transducted from neuron to neuron.
*  If you're trying to set up an like an AI system.
*  Well, part of the problem is we don't even know yet what is actually important.
*  Right. You know, for for a given cognitive function, like what is the right level to even examine it?
*  And something that I have come to appreciate more and more the older I get is how young neuroscience still is.
*  I mean, it doesn't seem like it is, but relative to something like physics, neuroscience is really new.
*  And I mean, it's just interesting.
*  You know, when I started in neuroscience, looking at the classic papers, right, recording single units and just characterizing a single neurons activity, you know, and it had been around already for a little while.
*  But it was incredibly young at that point still.
*  And it really still is. So neuroscience is slower, inherently slower than AI cycles goes on, you know, slower cycles.
*  And so at this point, like right now, is neuroscience informative for AI still or has AI just in mass said, all right, we can't wait for neuroscience.
*  We've got to move forward because, you know, obviously, AI is beneficial to neuroscience.
*  Well, you know, people might not like neuroscientists might not think that that's quite so obvious.
*  Well, as I just meant as a tool, but but as theory generators, as theory generation, I think it's pretty well accepted, at least that there are interesting ideas coming out of AI.
*  Maybe not that it's so helpful yet.
*  Yeah. So well, actually, I have a lot of thoughts on that, on that that maybe we can get into later.
*  But in terms of the, I guess, the speed of neuroscience and and how, you know, useful it can be for AI, I think it's got to move at its own pace.
*  I think that keeping in mind that the point of neuroscience is not to engineer something is important.
*  And that allows us to sort of identify like, well, what aspects of it are important.
*  I think it will continue to be important, though, because the brain continues to be sort of what like the only example of this kind of general intelligence that we're that we want to construct in AI.
*  And I think that we can continue to learn from it and we can continue to always take lessons from it.
*  And I'm really grateful that there are people out there that are willing to continue to do experiments on it on the brain.
*  And like, to me, they're sort of doing all the hard work and I can just sort of reap the rewards and the lessons that they learn for my work.
*  AI is where it is today.
*  Deep learning is because of neural networks, which are made up of artificial neurons, units which, you know, emulate the way, you know, really, really crudely emulate the way that brains are connected and function really crudely.
*  But so that that basis was already there.
*  And it's interesting to me to think about how much we still have yet to learn about how brains operate and how they collectively give rise to higher cognitive functions and whether there'll be some discovery, some advance that will then really impactfully inform AI.
*  And I don't know how when that will be.
*  But it feels like it's really ramping up.
*  So I don't know what you know, what is your sense of that?
*  I think that it's so some pretty fascinating kind of areas of advancements in like the cognitive science side and the neuroscience side is being able to essentially quantify like how humans can most efficiently learn about task structure, learn about decision making.
*  So things like Bayesian inference or hierarchical Bayesian learning, there are like these kinds of accounts that are starting to be constructed that show that humans will perform optimal inference under sort of like bounded rationality or different kinds of like resource constraints that allow them to sort of act most optimally in the situations that we most naturally find ourselves.
*  And so I think that kind of work is to me like most related to the kinds of things we might want to think about in AI.
*  And that's incidentally also related to meta learning, which is my favorite topic in AI is thinking about, you know, well, how can we set up these systems such that they can learn for themselves these like optimal like close to Bayes optimal ways of performing inference, given a particularly
*  structured set of environments that it can be encountered with or particular set of tasks. So, yeah, so I think I think that there's definitely parallels in the way that we can think about human information processing and cognition, and the ways that we might want to structure our artificial intelligence agents.
*  Would you say as you continue your career that you take less and less inspiration from neuroscience or more and more? Or is it just kind of a rotating cycle?
*  Sorry to harp on this. It's just, to me, it's, I mean, that's what the show is about is like, you know, the balance between AI and neuroscience. And so I'm trying to dig down.
*  It's definitely a very interesting question. It is one that I tend to get more often than not, I feel like. I definitely want to continue to be abreast of the latest developments in neuroscience. But I'm quite selective about the kinds of things that I pay attention to.
*  And I think that we're we're now actually getting to a point where we can start seeing more of an interactive, like bi directional flow between AI and neuroscience, like the more and more people that are sort of at the intersection. And because of that, I think we're going to start to get more work coming out that that's going to be relevant for both fields. And to me, that's very exciting. So I mentioned a bit earlier about like talking about this feedback from AI to neuroscience.
*  Where you can think about. So one exciting thing that you can do is you can take you can take it like a an RRL sort of setup that you have or an agent that is learning on on a particular set of tasks that you constructed.
*  And you can then analyze it and see, well, what kinds of things has it learned? What are the sort of like biases, inductive biases that it's picked up from the environments? And then from that you can infer you can say something about the task requirements that you've presented the agent with.
*  And then you can then imagine taking an animal and then training that animal on the same set of tasks and then seeing, well, does it have the same biases that agents have? Can it perform to the same level? Can it learn the same kinds of structure that an agent can learn?
*  Or does it have a lot of its already like sort of preset priors that it's going into this task with? And I think that this is something that isn't as well has been studied as much in neuroscience and with animals is thinking about what kinds of priors and inductive biases already exist.
*  You know, a lot of laboratory like task paradigms make the assumption that an animal just sort of like comes in knowing nothing or like with the uniform prior.
*  And then it'll just and then you train it sort of up to ceiling and then you you you like analyze the neural activity or something like that.
*  Well, that's kind of what the most vanilla neural networks connection ism used to assume as well by not structuring it. That's changed with CNN's and these more structured networks, which, you know, I don't know why I'm saying that because you know all about that.
*  Well, yeah, I mean, networks also come come with these biases as well. Yeah, CNN is a kind of an inductive bias. You build in biases all throughout by your choice of architecture and your learning algorithm and so forth.
*  But the thing is with AIs that we know that with animals, we don't know what kinds of biases are already existing. We know that there tend to be certain things like they tend to maybe think of color as more of a of an irrelevance factor.
*  And so I think that's one thing that having done work in AI, that's one thing that I've taken away from from doing that kind of work that I think can be applied to neuroscience.
*  You might get docked for depending on how you answer this, but there's lots of talk these days about deep learning hitting a coming to a standstill, reaching its limits. Right. And I'm wondering, you know, do you think so? Or again, maybe we can go off the record so you won't get docked and pay. But I imagine I know what your answer is going to be. What do you think?
*  I don't think so. I mean, I think that there's a danger in getting too wrapped up in any one approach or to jumping on like the bandwagon of, you know, deep learning or like this particular method of training. And we could just sort of continue to throw more and more data at it.
*  But I think that the field of AI, you know, just even beyond deep learning is is so rich and that there are still so many unexplored regions, areas of research that we haven't even tapped that. Yeah, I think that we're, you know, we're at a position where we have so much data, we have so much compute that I think at any moment we can just go back and look at it.
*  And at any moment we can have a really amazing sort of new algorithm that pops up and it shows us that it sort of opens up an entire new way of thinking about about deep learning and AI.
*  I mean, you know, recently there's been a lot of a lot of excitement around like GPT-3, the stuff coming out of OpenAI, these large scale language models that are just, you know, they have tons of parameters, they have tons of data, and it's just amazing the kinds of of, you know, like structure that they've learned and the kinds of things that you can get them to do the proper prompt.
*  And so a lot of people are now sort of thinking about, well, how do we how do we characterize the limits of that? How do we characterize the kinds of representations that they've learned? And how do we sort of leverage that towards building bigger things and better models?
*  So I think we're going to continue to see these kinds of things where like these little breakthroughs can help us to to bootstrap and to get to, you know, even better things.
*  Well, it sounds like you might actually get a bonus. I thought you might get dock pay, but maybe someone listens to this. I give you a bonus. All right. Well, I've almost taken you an hour now just talking about the deep mind.
*  And but I appreciate you going down that road with me. So let's talk about what was the next big thing. And then you published it. And then we're going to talk about some meta reinforcement learning.
*  And then we'll talk about some more of your recent work. So I talked about meta learning and meta reinforcement learning when I had Matt Botvinnik on the show long time ago, your colleague.
*  And but this is work that you headed up as well. And you just I didn't realize that meta learning is like your favorite topic. So it's good that I'm going to ask you about it, I suppose.
*  But maybe we can recap just the story of meta reinforcement learning as it pertains to as it maps on to the prefrontal cortex and the corticobasal ganglia thalamic loops and how yeah, maybe you could just like summarize what you guys found because that'll lead into this more recent work as well.
*  Yeah, so I mean, this work is actually kind of a series of two papers, I would say, as we had a paper that was presented at COGSI a couple years before that learning to reinforcement learn, which is essentially is looking at meta learning from a reinforcement learning context.
*  So the idea of meta learning is that you have these multiple nested scales of learning and that you can have sort of like an outer loop of learning, which is tuning an inner loop of learning.
*  So essentially, you can learn the learning algorithm that in the inner loop can sort of perform more quickly or like adapt more quickly to new situations.
*  And we call it, you know, meta reinforcement learning because both sort of learning loops are using reinforcement learning.
*  In particular, we use a deep neural network, a deep RL agent, which is learning through, you know, just like policy gradient methods to optimize for reward over the course of an episode.
*  And every episode, you can sample like a new task with different task parameters.
*  And over the course of seeing enough of these episodes, the inner loop is sort of able to quickly adapt.
*  So the sort of the simplest example that we gave in our paper is bandit is a two arm bandit.
*  So a bandit task is sort of like the the most the smallest unit of a reinforcement learning problem that you can have, which is still interesting because it's just a single step sort of trial where you're asked to choose a task.
*  You choose from one of two arms.
*  It's just like imagine like you're in a you're at a in Vegas in front of two slot machines.
*  You have to pick one to to pull.
*  But but each arm has some fixed but unknown probability of giving you a reward.
*  And you have to just sort of over the course of, say, a hundred of these trials, figure out which one is the better one to pull.
*  And but you need to sample both of them because you don't know what the probabilities are because they're hidden from you.
*  And so you need to like sort of take your your past history of observations and then from that figure out, you know, how can I best do perform sort of exploration versus exploitation to get the most amount of reward over the course of this episode of my like set of experiences with with this one parameter set.
*  With the one bandit machine, right?
*  Yeah. And so, you know, it turns out that through just using a just a deep RL agent that has, you know, just a recurrent memory.
*  So the recurrence is quite important because it needs to be able to integrate information over time.
*  So this past history of what it's seen and what it's done and so forth and the kinds of rewards that it's gotten, all that's really important.
*  You guys use an LSTM for that, right?
*  Yeah, yeah, an LSTM. And from that, it can then map onto an appropriate policy to tell it, you know, well, I should be now I should pull arm A, now I should pull arm B.
*  And then it turns out that you can actually take the system and it can learn to do something that looks close to Bayes optimal.
*  So if I can just define this is why we use a bandit at first is because these sort of Bayes optimal solutions already exist.
*  And so you can compare against them. So these called like these Gittin's indices.
*  And so, yeah, over the course of sort of many training episodes, you can you can get an algorithm.
*  You can learn a policy that can perform sort of close to these Bayes optimal solutions.
*  And it turns out that also if you apply it to even like to harder tasks distribution to harder tasks that maybe are not just a single step bandit, but are some sort of MDP or some sort of task where you need to first gain information and then exploit it.
*  So if you so these kinds of tasks sort of can have arbitrary structure.
*  So whatever kind of structure that that you want your your task distribution to have the like meta RL agent will eventually be able to learn that and eventually be able to leverage that in order to perform really well within the span of an episode.
*  But you haven't really talked about because you have to present, you know, multiple different tasks to this network for it to be able to meta learn essentially.
*  But those tasks have to have some similar structure among them. So there is that constraint.
*  Yes. Yeah. And this is related to kind of the free like there's no free lunch theorem.
*  Right. So there is a theorem that's essentially saying that, you know,
*  A given algorithm is never going to be better than another one if you're sort of testing on all possible problems.
*  So the key is that you need to have some kind of structure in the problems.
*  And if your algorithm sort of can pick up on the biases that match that that particular structure that exists in your problems, then you're going to do better than than another given sort of solution.
*  So that's the whole key to meta learning is that you're able to pick up on these inductive biases and these priors.
*  You can learn them as opposed to, for instance, you can you can, you know, handcraft them in.
*  You can build them in, which is the case with more sort of like Bayesian solutions.
*  So I can I can define a Bayesian solution, which is going to perform optimally on this particular task.
*  But then but then I need to do that for every single kind of task.
*  Whereas, you know, meta learning like meta RL is sort of like a general purpose method for you to say, I have I have a task distribution.
*  I'm just going to try and learn that structure and then I don't need to sort of like define it by hand.
*  Yeah. So the relationship of this to to like neuroscience aspect of it, which is in that the Nature Neuroscience paper that that we published in 2018 is that it turns out that you can find signatures of this in the brain as well.
*  So we had a series of I believe it was like five or six neuroscience experiments that are just taken directly from from the neuroscience literature.
*  They've already been published and we can look at the behavior and the the sort of like neural activity of animals that were trained and also humans that were trained in these tasks.
*  And we can train our algorithm, our meta RL agents on those same tasks.
*  And turns out that we can find sort of like similar signatures in our meta RL agents that exists in humans or in animals, the same kinds of behaviors as well.
*  And to me, the magic in the story, because I actually still kind of struggle to think about this is, you know, you have the slow outer loop training the faster inner loop.
*  And then at some point you turn off the training, you turn off the weight updates.
*  So then you just have this recurrent network and learning can still take place in the recurrent network in the dynamics of the recurrent network without the weights being updated.
*  And it's like magic because so there so then there are two things that are driving the learning in the dynamics.
*  There's the rewards still coming in from doing the tasks and there's the internal hidden state history that can just get shifted around in conjunction with incoming rewards to alter its behavior.
*  And that seems like magic to me.
*  Yeah, I mean, it's it's it's magic, but it's also very, very smart for for evolution and biology to have like come across.
*  Right. Because a lot of times you have things that change in the moment.
*  You have sort of, you know, constantly like new observations that you sort of need to adapt to.
*  And yeah, the thing about this work is that that we're able to sort of point to prefrontal cortex as being the place where sort of this fast inner loop of adaptation is happening.
*  We can like find signatures of this, be able to adapt to sort of changing context or changing incoming rewards and observations.
*  And that's what allows us to sort of within minutes be able to adapt to a new situation.
*  Whereas, you know, we know that sort of synaptic plasticity and things that that require maybe like protein synthesis or like long term plasticity.
*  These are things that happen on the time scale of much longer.
*  Yeah. So this is the more outer loop adaptation or learning process that we think sort of like is mediated by maybe dopamine and by like synaptic weight changes in like basal ganglia and things like that.
*  Yeah. So it's nice that that we can sort of in a rough sense, I wouldn't say that we have an exact sort of mapping to the brain.
*  But it's nice that we can sort of see the same sort of a system in a biological system that we find in an RL agent, in a meta RL agent, that sort of like naturally emerges if you have these ingredients set up, if you have like a task distribution that has structure in it.
*  If you have recurrence, if you have this sort of like model free form of reward based learning and that you just like sort of get the meta RL to to emerge from that.
*  Yeah, it's really cool.
*  And those two papers that you were just talking about that we were just talking about are among a few others that are highlighted in this recent review that you guys have written about deep reinforcement learning and deep meta reinforcement learning is one part of that.
*  Story. And so I'll point to that review as I'll point to both the papers that we just talked about and this recent review about deep reinforcement learning.
*  And so we don't need to talk about deep reinforcement learning, but that's like that's the big rage right now, I suppose.
*  And a lot of what you guys are working on. But are you because I want to make sure we get to your newer work here.
*  But are you still working on the meta reinforcement learning PFC dopamine story? Is there more coming or is that is that now a thing of the past?
*  Well, I mean, I wouldn't say it's a thing of the past. So I'm still I'm still working on on meta learning.
*  Yeah, it's it's not like I'm done with it. You know, I'm still quite interested.
*  Yeah. So I guess the one of the things that we're interested in is trying to test some of the the hypotheses that were made in the original paper to see if you can.
*  That's the the ultimate test of a good hypothesis or theories that you can you can test it at some point and confirm or deny it.
*  So there's you know, we're interested in looking at how we can do that.
*  I think one one challenge to try and and do that in particular is that what turns out that I mentioned earlier as well.
*  But in neuroscience, there's not as much work that's being done in looking at the learning process itself.
*  So a lot of times if you have an animal and you're and you have a particular task paradigm, usually you train the animal first to ceiling like like the perfect performance or some kind of like, you know,
*  steady state performance and then you start doing neural recordings.
*  Most people don't do neural recordings during. And so that's sort of one challenge and trying to like falsify this theory.
*  But in general, it's also just interesting to think about the kinds of like so I've been reached out to a lot by neuroscientists that are curious as to, you know, well, what can I do with this?
*  You know, like, how can I incorporate the the learnings from this into into my work?
*  And, you know, how can I what kind of lessons can I take away and how in particular, how can you sort of like close that that loop back from AI to to neuroscience?
*  And you tell them you can't because you're too slow, right?
*  No, no, no, no, no, I, I, I encourage them to to maybe.
*  Yeah, to think about looking at the in particular that learning process itself and to look at, you know, what are the signatures of meta learning as opposed to just sort of learning in that inner loop?
*  And can we identify those? Can we look at some an animal that is at the beginning of learning and compare that to an animal that's at the end of learning?
*  When I say learning, I mean, sort of, I guess, training where if you train an animal that can take months.
*  And so, you know, I think it'd be really interesting to look at what's happening at the beginning of training an animal where I'm sure it's not at that point is probably just exploring.
*  You know, it's not not really like doing much that's of quote unquote interests, maybe from the task paradigms perspective.
*  But I think that it probably is quite interesting if you look at it from a meta learning perspective, because this is the this is what meta learning is doing is that you sort of like you need to construct that inner loop.
*  Yeah, it is interesting when I was in my graduate school and for my postdoc, I had trained monkeys.
*  But in particular, in graduate school, I trained them on a meta cognition task.
*  So they had to keep track of their decisions and then make a bet whether they think they made the decision right or wrong.
*  And that's really hard to train in a monkey.
*  You know, it took months.
*  And and so, you know, you you'd spend those months without recording any neurons.
*  And then finally, you'd get them all trained up and then you'd stick the electrodes in and record the neurons.
*  And we even published like a little learning behavioral learning graph over time.
*  But yeah, it's it'd be super interesting to have neural recordings and come up with a story about about.
*  I mean, in this case, it wouldn't have been meta learning, but come up with a story about the progress of that training regimen.
*  That's a lot of work, too. And I can imagine it'd be messy and not an easy story to tell, perhaps.
*  Yeah. And I can totally sympathize with with neuroscientists that, you know, that they don't want to do that because it is so messy.
*  Like, how do you even analyze that? And also recording for that long, you know, chronically over months, that that's also just its own special challenge.
*  Oh, yeah, yeah. Less so these days. It's getting better and better.
*  All right. We have that much time left. So I really want to talk about altruism.
*  And, you know, this isn't even your most recent work.
*  I could like reach into a hat and pull out any of your publications that we could have talked about.
*  But I know this was interesting to me. So the title of the paper is evolving intrinsic motivations for altruistic behavior.
*  Why is altruism important? I should back up.
*  So this is part of multi-agent reinforcement learning that's pretty big these days in multi-agent game playing and multi-agent,
*  meaning multiple AI agents that have to work together to play a game, perform a task.
*  And but that doesn't necessarily so that means they have to cooperate.
*  But altruism is well, to my understanding, and maybe you maybe have a different understanding than I do.
*  Altruism isn't just about cooperation. So we'll talk about the importance of evolving the cooperative or altruistic behavior.
*  But I'm just wondering, you know, why altruism is important. I'm not sure that humans are terribly altruistic anyway.
*  The why I got interested in it. Yeah.
*  Well, this is sort of my first foray into like multi-agent RL.
*  But I've always been just interested in how how actors can sort of learn to coordinate behavior to accomplish sort of something bigger.
*  And how in particular how can nominally sort of self-interested actors such as RL agents,
*  how can they come to coordinate to be able to perform altruistic actions and things that are sort of good for the whole for everybody.
*  Altruism is, to me, you know, a very important part of human intelligence
*  and an important part of why we are as successful as a species as we are,
*  is because we are able to sort of act for the betterment of everybody as opposed to just ourselves.
*  You know, humans are intrinsically social in nature.
*  I don't know this. I don't know if COVID stands that passes that test.
*  I mean, I didn't say we're perfect at it, but I think it's one of the reasons why we got to the level that we're at.
*  And of course, there's always challenges.
*  There's always sort of internal conflicts between our altruistic impulses and also acting in our own self-interests.
*  But that's also the interests that, you know, that's the source of my fascination with it,
*  because we do have these two sort of competing instincts.
*  And how is it that we got to the point where we were able to come together and build a society and to build all that we have built and to be able to act?
*  Yeah, I think a lot of people are, or at least they want to be altruistic and to act for the betterment of others and aren't just sort of in it for themselves.
*  Living in London, you're losing your American roots, I can tell.
*  I don't know. I mean, it's yeah, I think maybe we spent, or at least I spent too much time on Reddit and Twitter and just getting too bombed out by all the bad actors out there.
*  But I think in general people will try to be good.
*  Okay, all right. Well, so you took a different approach because previous multi-agent reinforcement learning approaches, they have like hand engineered the altruism into the agents, right?
*  Into the way that the agents behave. But you decided to evolve it. So tell me about that. Why was it important to evolve it?
*  And yeah, we'll go from there.
*  Yeah, so I mentioned before that there is this kind of this puzzle as to how altruistic behavior even came about.
*  Because if you think about, yeah, from an evolutionary perspective, why is it that we should act in altruistically or for the betterment of somebody else if it doesn't benefit myself, if it doesn't allow me to sort of reproduce or to pass on my genes?
*  And so there's been a lot of different research into this and suggestions as to how it might happen.
*  You can, you know, some people are like there's been suggestions that this notion of reciprocity that you do something for somebody else with the assumption that then they will do something for you.
*  Or there's also like kinship selection or even the fact that, you know, if you are in a closely knit group and you act sort of altruistically just within that group, then overall your group will tend to out compete out of the other groups that don't do that.
*  And, you know, eventually, you know, you will your group as a whole will benefit from that.
*  So I should preface this by maybe like explaining what is the actual dilemma that we're even trying to solve.
*  So, you know, at DeepMind we always work in games.
*  And so we came up with a game for our agents to play that sort of for us typifies this idea of a dilemma between acting in your own self-interest and for the benefit of everybody.
*  So these are called intertemporal social dilemmas.
*  And these are just generalizations of of like Matrix games, which like the most famous example would be like the prisoners dilemma and prisoners dilemma for people who who haven't heard of it is essentially just like this example of where you imagine that two criminals have been caught and they're being interrogated in two different rooms.
*  There's no evidence there's very little evidence to sort of convict either one of them.
*  And so the cops really want like want a confession in order to be able to convict.
*  And each of them had their own sort of decision points to make where they can either choose to cooperate or to defect.
*  If they cooperate, meaning that they stay silent, they don't sort of rat the other person out.
*  Then if they both do that, then they sort of both will benefit in the long run.
*  Or like they'll serve sort of a minimal amount of a sentence.
*  Short sentence. Yeah.
*  But if they rat the other person out.
*  Sorry, if prisoner A defects, but prisoner B cooperates, then prisoner A would go free and then prisoner B would have like the maximum sentence.
*  But if they both defects, then they both will serve sort of a medium amount of sentence.
*  So if you're acting rationally, you actually would always defect because depending on whether or not the other person cooperates or defects, it's always better for you to defect.
*  But then if both of you defect, then you're both worse off than if both of you cooperated.
*  So this is just sort of setups to where if you just act just strictly in your own best interest, then everybody is worse off.
*  And so the intertemporal social dilemma essentially generalizes that to multiple time steps.
*  So these matrix payout games is always just a single decision that you make.
*  Choose to cooperate or to defect.
*  Intertemporal social dilemmas sort of are just like these grid world games where the agents can choose to sort of walk around and they can collect apples or they can choose to, for instance, clean a river and contribute to the public good and things like that.
*  So they take multiple time steps to sort of do.
*  And then they also have this notion of that there's this tension between acting in your own self-interest in the short term.
*  So if I collect this apple, then it's sort of I get a lot of reward in the short term.
*  But in the long term, it's worse off for everybody because I have I have now depleted our source of apples.
*  And so this is the tragedy of the commons.
*  Or if everybody sort of raids the common good, then it's just going to be gone for everybody forever.
*  And this kind of problem seems a little bit maybe contrived, but it actually typifies a lot of real world problems that we're facing now, such as climate change, where a lot of people are sort of unable to act in the long term interest of everybody.
*  Because on the short term, we want to be able to continue sort of using as much resources as we want.
*  We would want to be able to have short term rewards, even though in the long term we know that it's going to be worse off for everybody.
*  So we know that this is a kind of an issue that I guess humans already are not very good at solving.
*  And so that's for me.
*  Yeah, go ahead.
*  Yeah, well, so that's one of the motivations for for for me to study this in these kind of multi agent RL settings.
*  The most important point is that you have these sort of two different time scales because you have these two different time scales.
*  It actually is a pretty perfect setting for meta learning because meta learning sort of naturally has these like multiple time scales of learning.
*  And this is where evolution comes in, because evolution can be thought of as sort of the ultimate meta learner in my mind.
*  It operates on a very slow time scale.
*  But within, say, a single lifetime, an organism learn like it has a lot of different learning strategies that has presumably been evolved or been sort of instilled in developmentally.
*  And so this is why the decision was made to address the evolution of altruistic behavior using evolution.
*  And the way that we do it is we essentially are evolving like social signals that can be passed from one agent to another.
*  So we have essentially a we would call a reward network, which constructs the intrinsic reward that an agent can derive from social signals that are given by other agents.
*  For this first work, we for the social signals, we just used sort of the observable external rewards that other agents are getting, like the number of apples that they're picking and so forth.
*  But you can think of it as like I can observe other agents being happy or sad.
*  Like, are they smiling? Are they not smiling? Are they getting reward?
*  Yeah, yeah. And they're social because they're sort of like passed between agent to agent.
*  And so if I can evolve over this kind of signal and subject to certain constraints, such that we all sort of need to be playing by the same rules, we all need to be valuing these social signals the same way.
*  Then it turns out that we can solve these intertemporal social dilemmas and we can get the evolution of altruistic behaviors, such as agents that refrain from collecting too many apples so that there's going to be more in the long term or agents that will perform a public good action, such as cleaning a river so that more apples will grow for everybody.
*  So it's interesting the idea of creating and evolving agents that behave in some sort of optimally altruistic manner.
*  It's interesting that they could far outstrip our own ability to do that.
*  I mean, is that the goal?
*  You know, because I mean, well, there's so there are two things.
*  One, it's just we could use what you're learning about how to create artificial agents.
*  We could use that to sort of shape policy, right? And in our own behaviors.
*  But the other issue, and I don't know what's more important to you, is that in the future when AI is, you know, just all I mean, it's already all around us.
*  But when we have these multi-agents, AI is interacting with each other while they're going to need to be constructed and constrained in such a manner as to be able to cooperate.
*  Yeah, I mean, so I think that this work can address sort of both of those aspects because, yeah, you can imagine a field of work where you take these artificial sort of RL agents
*  and you try and figure out what kind of system or what kinds of like intrinsic rewards can you give them such that then they're more likely to cooperate or they're more likely to sort of coordinate with each other.
*  And then you can try and see if maybe that would sort of generalize to the way that humans act or behave and see if you can sort of induce more cooperative behaviors.
*  But similarly, it's also true that, you know, I don't think we can get away from the fact that humans are going to always be having to interact with AI agents.
*  I don't think that any AI agent that we come up with is just going to be this monolithic sort of separate entity that will not need to be interacted with at all.
*  I think that, you know, most likely the most exciting kinds of AGI that we're going to come out come up with is going to be tightly interconnected with humans and is sort of going to be interwoven throughout our society.
*  And so we'll need to have a good understanding of what induces cooperative behavior and what kinds of learning mechanisms or what kinds of like loss functions are going to be most important for us to get the behavior that we value.
*  And that allows us to get like ethical behavior from both these agents and from ourselves.
*  So the main takeaway is that having these evolved reward networks, which are sort of the important thing is that it's the same reward network that every agent plays with.
*  So if they're playing together, we call it like playing together.
*  But if we put together five agents into one of these environments, then they all need to have the same reward network.
*  And then if we allow evolution of these reward networks over the course of many sort of interactions between these different agents, then you start to see cooperative behavior emerge.
*  And then depending on the task, depending on if it's a public goods game or if it's a like a tragedy of the commons kind of game, then you get these different reward networks that are useful for these different situations because they're different kinds of tasks.
*  So this is kind of the power of evolving and letting it sort of like meta learn in a sense what should be the correct sort of set of rules.
*  So to me, I can I can broadly sort of interpret these reward networks as being the rules of play.
*  So if I'm going to be engaging with a group of other agents or people, then we all need to sort of agree beforehand.
*  These are sort of how we want to be interacting.
*  These are the rules.
*  And if they're a good set of rules, then it will allow us to sort of get good behavior out of everybody.
*  How many different algorithms are out there or in our heads for different situations?
*  Well, I mean, infinite, right?
*  Like, anytime you come into a different situation, I think you're always like sort of negotiating the rules of engagement.
*  And maybe like just through communication, you can sort of like implicitly agree on how we should be interacting with each other.
*  Every like social network that you that you go on like Twitter and Reddit and like they all come up come with their own sort of set of rules for how you interact with each other and so forth.
*  So I think it's really interesting to think about these kinds of things to different systems that people can interact with each other under and it induces different kinds of behavior.
*  Why do I hate Reddit so much? Why can I not get in?
*  Everyone tells me I need to do I need to be more into Reddit and I get nothing from it.
*  I don't understand why anyone uses it.
*  I like that. I think it's I think it's super fascinating.
*  And also Twitter, like the kinds of information that you can get from it.
*  I mean, maybe maybe you just need to follow different subreddits.
*  I don't know. I'm trying.
*  But I get next to nothing from Twitter as well.
*  I just don't want to. This is too long of a side.
*  But I can see why it'd be useful to people.
*  I will say I think we are just that we're very embryonic in terms of our understanding what kinds of social networks are most useful for communication.
*  And, you know, I think right now a lot of social networks are built to sort of generate advertisement revenue or to generate like increase engagement.
*  Most like first of all.
*  So I don't think that they're necessarily built to incentivize good communication.
*  And that's probably why a lot of times you would find them like sort of upsetting or like or that they're very distracting because they're not right now, I guess, built to do that.
*  And I think that it is important for us to think hard about what kinds of systems would allow us to engage best with each other and to come up with ways to I don't know.
*  Better coordinate and to form like useful collective action and to coordinate with each other in altruistic ways and so forth.
*  Yeah. I mean, yeah. So I definitely think that there's a lot of work to to be done on this front.
*  Yeah, agreed. Well, I know I've already taken you over time here and we had planned because I know that you're interested in A.I. ethics and we plan to talk a little bit about that.
*  But instead, I'm going to have to I'll email you in a couple of weeks and then you can say you're too busy and then I'll wait another year and then I'll email you again.
*  And maybe you can come back home because we really never talk about ethics on the show.
*  And I know that's like a big topic of interest publicly as well.
*  For now, my last question, random patron supporter question here.
*  What's one before we before I let you go, what's one book that you would recommend people read?
*  And it could be that that's been important to you or that it doesn't have to be even a science book.
*  Yeah, one book that I read recently that is related to A.I. quite liked is called Human Compatible by Stuart Russell,
*  which is essentially asking the question of how can we ensure that an advanced artificial intelligence is going to be able to well align with human values and to be safe to interact with?
*  Oh, another another book that I read, which I think I think is very good, is Algorithms to Live By.
*  They're making they're making a second part and interviewing a bunch of people because success with the audio version of that one.
*  I had Tom on the show, so I can recommend that as well.
*  Yes, yeah, that one's definitely one of my my favorite recent books.
*  So thanks, Jane. It's been a long time coming.
*  I really appreciate you coming on the show and continued fortune at DeepMind.
*  Thank you very much. Yeah.
*  And I look forward to coming back in a year and a half.
*  Good.
*  I hope you enjoyed this video.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
*  I hope you enjoyed it.
