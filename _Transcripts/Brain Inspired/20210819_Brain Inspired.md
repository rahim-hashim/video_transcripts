---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4833s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 11631
Video Rating: None
---

# BI NMA 06: Advancing Neuro Deep Learning Panel
**Brain Inspired:** [August 19, 2021](https://www.youtube.com/watch?v=e5G_ltg3fFw)
*  When we do brain imaging, we're measuring the artifacts of the algorithm.
*  We're measuring the intermediate stages that the algorithm outputs in order to do its next
*  step.
*  We can see the states that are happening, but we don't have trouble seeing the actual
*  operations.
*  I think if we could do that well in humans, we would have some sense of what people's
*  algorithm is.
*  There is an infinite number of algorithms that we can come up with.
*  I think that we should think in terms of learning principles and just develop as many algorithms
*  as needed until we have something that captures a lot.
*  I don't think reinforcement learning or even learning in general is necessarily what our
*  brains were built to do or is all that they do.
*  I think learning itself is a continuous concept.
*  We should take a more broad approach than just to say, you know, we need to understand
*  learning only in terms of the kinds of algorithms that can encompass learning.
*  This is Brain Inspired.
*  Is a riverbed alive?
*  That's one of the questions that we tackle here in this last panel discussion in the
*  Neuromatch deep learning series.
*  This week in Neuromatch, it was all about advanced methods, unsupervised and self-supervised
*  learning, reinforcement learning, and continual learning slash causality.
*  We don't talk about causality at all.
*  We actually have a pretty broad meandering discussion.
*  With me today is Alana Fish from the University of Alberta, Jane Wong from DeepMind who's
*  been on the show before, and Ida Momenejad who's now at Microsoft who's also been on
*  the podcast before.
*  Some of what we do talk about is language and representations, what separates humans
*  from the rest of the animal kingdom and bacteria and rocks and rivers and AI.
*  We talk a little bit about meta-learning and continual learning more broadly.
*  What meaning is and lots of other things.
*  Like I said, it was a broad discussion.
*  So you can go to the show notes to learn more about the panelists at braininspired.co slash
*  podcast slash NMA dash six.
*  For those of you in Neuromatch, I hope you enjoy your experiences in Neuromatch.
*  And actually, just as I'm recording this, which is right after we had the discussion,
*  Ida emailed me and asked if I could add, if it's not too late, that she thinks the internet
*  as a whole is closer to life than a river bed is.
*  There's a little nugget to put in your pocket for later in the discussion, but I'm done
*  recording the intro, so I can't wait for Jane to respond via email.
*  This was a fun conversation to round out these panel discussions.
*  Enjoy.
*  Alana, before you introduce yourself, I have to ask you a question.
*  So you worked at Google in Pittsburgh, correct?
*  While you were working there, did you ever do any of the in-house yoga classes that were
*  offered?
*  I know you guys probably had a lot of offered ping pong and stuff like that.
*  Let me think.
*  So I was in their, well, what was technically their second office on CMU campus.
*  Yeah.
*  So my wife taught yoga at all of their Pittsburgh campuses.
*  And I thought, oh, I wonder, because you were working there around the same time I was in
*  graduate school and she was teaching yoga.
*  So I was wondering if she had taught yoga.
*  I feel like yes, but God, that was a long time ago.
*  I was there 2007 to 2009.
*  So yeah, I believe she was, I'll have to ask her, but it was, it's funny because she taught
*  yoga all around and at Google specifically, a bunch of engineers, she said that it was
*  so funny because you guys, I'm going to say, were so like compliant that at one point she
*  was just, she got a foot cramp and she started like moving her foot around.
*  And then everyone in the room started moving their foot around as if that was the yoga
*  move.
*  That's engineers.
*  Yeah.
*  Instruction following.
*  Definitely.
*  It was a good time for her.
*  So hi, Olana.
*  So Ida and Jane have both been on the podcast before you have not.
*  So welcome.
*  And why don't you, who the heck are you?
*  What do you do?
*  I'm Olana Fish.
*  I'm a professor at the University of Alberta.
*  I'm also a fellow at the Alberta Machine Intelligence Institute.
*  And in my work, I like to think that we compare representations.
*  So we look at how computer models represent the world, including using vision and language.
*  We look at the internal representations and we compare those to human representations
*  in the brain and ask how using brain imaging, we ask how those representations are similar,
*  how they're different than how they change.
*  So I want to go around right after you guys introduced yourselves also, and I'd love for
*  you to say what you think might have been your first really good question that you asked
*  at any point in your career or pre-career, who knows?
*  And then I'd like you to talk about maybe something that is that's a question right
*  now that you feel like is just beyond your grasp.
*  Okay, so I have a young son, he's two and a half.
*  So I have to say that we all ask excellent questions as we're young as young ins.
*  And one of the really good ones is why?
*  Just like over and over again, why?
*  But in grad school, I had this idea that maybe language models and the brain were actually
*  representing the same thing and we could improve computer models of language using brain imaging
*  data. And so in 2014, I published a paper showing that that actually did work.
*  And I've actually recently expanded upon it again.
*  So that's sort of what I would say was my big aha moment, that it's actually all the
*  same brains, computer models, all the same thing, because it's all living sort of living
*  in the same world.
*  Something that's just outside of my grasp.
*  So I would like to take that idea a little bit further so we can measure how people do
*  things using brain imaging data.
*  And so I would like to use that idea to improve computer models of language in the areas
*  that they are just failing right now, like common sense reasoning, sort of implications
*  and inference and dialogue.
*  All these things are just natural to us.
*  We do them all the time.
*  And that even thinking computer models just fall apart.
*  And I feel like is like where is that link between what the people are doing with their
*  brains and what computer models are not doing?
*  How can we find that connection?
*  Well, we'll come back to the question of meaning in a little bit as well, which is related.
*  Very good.
*  Jane, you want to go next?
*  And who are you?
*  What do you do?
*  And what was an early, maybe an early good question, maybe your first good question.
*  And then what do you not know right now that you wish you knew?
*  OK, hi, I'm Jane Wong.
*  I'm a research scientist at DeepMind on the neuroscience team.
*  And I've been working there about six years now.
*  I can't believe it's been six years.
*  And I was a neuroscientist slash, I guess, kind of physicist before that.
*  I actually did my PhD in applied physics where I applied the applied physics, I guess,
*  to computational neuroscience and was essentially creating these dynamic systems or
*  modeling systems of the brain in a very abstract sense, not in any kind of biologically
*  detailed way necessarily.
*  And then in my postdoc, I entered more into the cognitive neuroscience realm of dealing
*  with actual real brain systems and humans and doing neuroimaging and cognitive modeling
*  and all that stuff.
*  Let me look to kind of just I'm going to jump in and interrupt you.
*  So if you had to do it again, would you switch the order of anything or was that a was
*  that a good order?
*  I think that was a good order.
*  I'm pretty happy with that order.
*  I might have jumped more into programming at an earlier stage, because I do think that
*  programming is something that I could have used the whole way through.
*  Just been a lot more comfortable with the engineering side of it.
*  But no, physics really gives you a good way of asking questions.
*  It gives you a good toolbox, I think, to be able to reason about new problems.
*  So like the physicist, like the archetypal sort of problem that you have in physics is
*  a spherical cow.
*  You always reduce everything to a spherical cow.
*  You reduce it to a problem that you already know how to solve, no matter how ridiculous
*  the reduction is.
*  And so that's always been my approach, I think, to to research since then.
*  I think that's really formed the way that I that I ask questions.
*  But yeah, so one one question that I think I asked why I asked this before I even really
*  understood what kind of a question it was.
*  It was during my postdoc and I was talking with one of my advisors about what was I
*  interested in, like what kind of just question about the brain that I want to figure out.
*  And and I just kind of formulated this without even really thinking too much about it.
*  But I was like, well, I want to know how does what we know already impact what we can
*  know or what we will know in the future?
*  And just a phrase like that, it sounds just incredibly naive and very simplistic.
*  But. But, you know, I've been working on meta learning, meta reinforcement learning for
*  years now, and it wasn't until maybe a couple of years back that I thought back to that
*  conversation. I was like, oh, wow, that's actually exactly what I wound up working on,
*  which is how do the things that we have already experienced and know really shape the way
*  that we approach new problems and and the way that we learn in the future?
*  So I mean, I still haven't gotten an answer to that question necessarily.
*  But, you know, that's before you go on again, I'm just going to keep interrupting.
*  So that's really great that you remember, however, you know, maybe loose or vague.
*  The memory is that you remember you had that question.
*  So, Alana, you were the CNBC in Pittsburgh and I have just been asked to do the alumni
*  lecture, the CNBC alumni lecture, which is a big mistake on their part.
*  But one of the things that they want me to do is answer some of the questions that I
*  ask on the podcast, these vague things and one of these questions like what did you
*  used to think that you now think is naive and stuff like that?
*  And I'm like, I don't know my own answer to these questions.
*  That's why I ask them.
*  You know, I think it's such an interesting like that is research, right?
*  Like we keep returning to these questions over and over again with new lenses.
*  Right. And I think that so many of the questions we end up answering are the ones that we
*  asked long ago before we had the tools to answer them.
*  Right. I think that's actually really insightful.
*  OK. But but like Jane just said, those are the ones that seem to never truly get answered,
*  perhaps. I don't know. Maybe that's is that what you do.
*  You also sometimes look back on your answers and realize like you answered the question.
*  It wasn't what you thought the answer would be.
*  And it didn't take the same shape you thought it would.
*  Like you had something in mind.
*  You answered the question and you realized you answered it before you knew that was still
*  the same question you were asking.
*  Yeah.
*  Well, I feel like, you know, in the beginning, we asked questions that are really grandiose.
*  They're the things that drive us, you know, and they have to be grandiose to be motivating.
*  The more naive, the more grandiose, perhaps.
*  Yeah. Yeah. But then once you finally figure out how do you go about answering this question
*  and you make it concrete, you make it doable, then you're might have answered a very small
*  part of it. So I can answer something about neural network.
*  How do neural networks meta learn in a specific set of environments?
*  And what does that look like in a very narrow sense?
*  So, yeah, I can I can answer that question.
*  But, you know, the larger question still drives me, I think, in a lot of different ways.
*  Well, so so the next thing that you need to tell us then is so you started off with the
*  with the grandiose question that that was a good question.
*  And now you're grappling with many things, I presume.
*  What's one of those things?
*  And and how specific and how non-naive is it now?
*  Right. I think I'm still quite naive and maybe grandiose in my question asking, because
*  maybe it's just because I don't know as much about this topic.
*  But, yeah, one thing that I've been really interested in is thinking about how much of
*  human intelligence is really cultural.
*  It's due to the social factors that bind us.
*  It's due to the fact that we have literature and education and we raise our kids in a very
*  social way with language and with through imitation.
*  And kids are sort of primed to to to learn in that fashion.
*  If you if you raise a child in isolation, then they wind up having all sorts of
*  developmental issues.
*  So so, yeah, I think that that's a lot more people are starting to think about things
*  like this as well. And even in the realm of A.I., which I think is really exciting.
*  So I do think it is still quite a grandiose question because you have to not only answer
*  how much of intelligence is cultural, but what is intelligence?
*  How do you define human intelligence?
*  And maybe this is why I started to think about this in the first place is a lot of what I do is I
*  compare human intelligence or animal intelligence against artificial intelligence that you
*  know, you've trained this model and a lot of in a lot of ways, I feel like maybe the
*  comparison is a bit unfair because if you're comparing a human, they kind of come in with all
*  of these pre-programmed in bits of knowledge that are cultural and are social.
*  And they're told things by the the evaluator, by the, you know, whatever the researcher
*  that's conducting the experiment.
*  And so the machines don't have the same benefit of that.
*  Ida, how was the gig last night?
*  Oh, it actually was great.
*  It was by the beach, so it was wonderful.
*  What instrument or instruments did you play?
*  I played the melodica, the guitar and I sang.
*  Oh, I didn't know that you're a singer.
*  And I looked at it.
*  So what gig was this?
*  Oh, it's just it's our other life.
*  It's it's your musical career.
*  Right. Oh, wow.
*  I had no idea. This is not going to be in the file.
*  Do you want me to edit it out?
*  I can. I just thought it's fun.
*  It's fun for people to hear.
*  Yeah. OK. Yeah.
*  So I make music on my free time and sometimes I perform it.
*  And so Ida has seen me frequently in the past month or so.
*  So she was on the podcast.
*  And then we recently did a discussion panel for deep learning and dopamine
*  for the online dopamine conference.
*  And in fact, we did that like a month ago, but it's going to air
*  in a couple of weeks through the podcast.
*  So the time is a little reversed.
*  So Ida, who are you?
*  What do you do and questions?
*  Only if I know.
*  So I'm a research, I'm a senior researcher at Microsoft Research in New York City.
*  I work on reinforcement learning.
*  I particularly work on I build algorithms that learn to build models
*  of the world, representations of the world, and then test those algorithms
*  in brains and behavior from fMRI to electrophysiology.
*  And something that I'm very interested in and I've worked on for the past,
*  I don't know, 15 years or something, is how the ways in which representations
*  and memory is structured in the brain corresponds to how we would remember
*  to do things in the future or we would predict or plan or imagine things.
*  So the relationship between executive function, which is planning,
*  which is multitasking and transfer learning, etc.
*  to memory and representation learning.
*  So that's something that has driven my work for a very long time.
*  And I continue to work on that.
*  And now I get to sort of focus on it a little bit more computationally than the past.
*  But I'm still obviously doing experiments both with behavior
*  and still collaborating on neuroscience data if I'm not collecting it myself.
*  Yeah. Oh, another direction of my research
*  that I really love is one where I study how
*  the structure of groups of people talking to each other shapes their memory.
*  So how the graph structure of a number of people talking to each other
*  and the order in which the edges or the conversations on this graph happen
*  shapes whether they converge or diverge more.
*  And yeah, so that's a very exciting part of my work
*  that usually I don't mention in talks or unless there's a different audience for that.
*  And so I have a review coming out in
*  philosophical transactions of the Royal Society called Collective Minds,
*  which is about this one, because this is something that has been on my mind
*  since very early on as well.
*  So now I think I should mention it.
*  Yeah. So I just want to interrupt again, but go.
*  Let's go through your questions.
*  What was the best a good early question that you had and what are you struggling
*  to think about now? OK, great. Great.
*  That was a great question from you to ask.
*  I really enjoyed hearing what Alona and also Jane thought about
*  had to say about that.
*  I think so my background is I started with computer science
*  and I was actually coding when I was a teenager
*  and won some sort of competitions like that,
*  which was a good starting point for me to feel the sense of algorithmic possibilities.
*  And then I got very interested in philosophy since I was like,
*  I don't know, 16 or something.
*  And at some point I decided I'm going to do my master's in philosophy of science.
*  While I was doing my master's in philosophy of science,
*  the thing that I was very interested in was free will and like
*  like a million other people on Earth.
*  But something that the thing that came to my mind back then was that
*  I was more interested in long term agency and not free will in the metaphysical sense.
*  And I thought that we waste a lot of time thinking about the metaphysics.
*  But actually, the more interesting question is, how are we capable of long term agency,
*  especially in the face of uncertainty and so many things that change?
*  What's long term agency? Is that planning?
*  Maybe, maybe it is a little planning, but not exactly only planning.
*  So consider the fact that you can order something,
*  a flight, and then you can take that flight next year.
*  That is an ability for long term agency that you are not.
*  Your brain is not the only thing that's responsible for that kind of long term agency.
*  Or imagine that you promise me that next month you're going to send me
*  the audio file for this, let's say, for instance, you're going to send me
*  the higher quality on-cut audio file of this recording.
*  That is it's not it is planning, but it's also something else.
*  It's the fact that you are going to remember this is a perspective memory thing.
*  There is a social contract of the promise that you have made.
*  There's a number of other components in it.
*  And if you're a person that manages to always sort of deliver on the at the right time,
*  then you become a responsible agent.
*  Then I would consider you someone that within this particular domain
*  has proper long term agency. Right.
*  Or consider the fact that you probably don't have catastrophic
*  forgetting with regard to tying your shoes.
*  Because of the fact that you're learning something new on a podcast,
*  you're not going to forget that how to tie your shoes or how to cook food
*  or how to, you know, set up your audio system.
*  That tells me that you have also another kind of long term agency
*  that's consistent with a kind of continual continual learning
*  that doesn't erase what you've learned before when you learn new things.
*  So that's another part of your long term agency.
*  So as you can see in the things that I said, I had both things
*  that are within a given algorithm, but I also had things
*  that rely on social structures that somebody is embedded within.
*  For instance, the plane that you're taking next year depends
*  whether there is not another pandemic, that there is no war in the location
*  you're going to, that, you know, there is not an environmental catastrophe,
*  that that airport is entirely burned down.
*  You know, there are so many things happening. Right.
*  So it's uncertain. It's not exactly certain.
*  And your long term agency, to some extent,
*  depends on how our social structures are resilient
*  towards the uncertainty of the world and how sustainable they are.
*  And so when I was in my
*  sort of my first graduate degree, which was in philosophy of science,
*  and I was thinking about how long term agency,
*  how can I think about long term agency?
*  I think that was the initial trigger.
*  And you will see that everything I do now is related to that.
*  The question I had was how this long term agency is mediated,
*  but because it's very special in humans.
*  I was interested in what kind of structures and functions in human brains
*  mediates them on the one hand.
*  And second, what kind of social interdependent
*  structures are necessary to enable them?
*  And as you can see, the first part of it relates to my work that I did
*  in how the prefrontal cortex might enable this kind of multitasking,
*  perspective memory, analogical reasoning, all the kinds of nice things
*  that my favorite region of the brain, brahmin area 10,
*  which is anterior prefrontal cortex right behind your forehead.
*  And then and also, obviously, it turns out that
*  we have the this is the largest site to architectonic area
*  of the human prefrontal cortex, and it's the region in which we have
*  the biggest difference with other nonhuman primates.
*  And then on the other hand, the work I've done on how graph structures
*  of social interactions lead to our memories converging or diverging
*  leads to the second part of that question that our long term agency
*  to a large extent depends on our ability on our social structures,
*  how our social structures basically augment or sustain our long term agency.
*  And the first one and the second one, as you see, both of them
*  are related to the notion of memory.
*  And so I think that both executive function and a lot of our social structures
*  have very deep connections to memory.
*  And it's not just about brains, but it's also how our social structures are organized.
*  And so, as you can see, like that question that I started with
*  during my master's degree in philosophy of science really drove everything
*  that I did later on in science. And I still do.
*  And that's the reason I moved to computational neuroscience to a large extent.
*  So it's interesting.
*  So, you know, what Jane said, you know, becoming more interested in the social
*  aspects as she learned more.
*  That's kind of the way I feel, too, although I'm resistant to be dragged
*  into the social aspects of things.
*  But you just because I want to stay on the brain, damn it.
*  You know, but of course, there's it's all connected.
*  But but you but you so the social aspect started
*  you thinking about memory and structure and representations.
*  And that's that was the trigger that set off the rest of your career.
*  The social aspect started when I was thinking about long term agency
*  and this idea that what we really mean by free will is that we can do things
*  further into the is that we have agency and that when, you know, it
*  so it's funny because some people seem to think free will means acting randomly.
*  If that was the case, then, you know, particle random gas particles
*  might have free will.
*  But actually, the ability to be able to have agencies further down in time,
*  that's the thing that requires a real kind of agency.
*  And I'm not so that's why I moved away from the word
*  or from the compound word free will, which has a lot of, I think,
*  confusion attached to it in incompatibilitists and also in
*  people who associated with being random or spontaneous,
*  as opposed to actually being able to deliver a year from now.
*  And so I focus more on that long term agency.
*  So that long term agency was the philosophical idea that I was interested in
*  coming from a background from a country where it was difficult to maintain it
*  because social structures were opposing it.
*  But seeing how people's
*  smart algorithms would overcome it and make somehow make it work. Right.
*  So all of those things are very much tied to that era.
*  When I was trying to figure it out, figure it out philosophically.
*  It was very tied to questions I had asked since I was a child.
*  But it was very much what drove me to figure out, OK, the field
*  I need to go to to answer all these questions is cognitive
*  and computational neuroscience.
*  So I can ask questions about social effects on agency about
*  or specifically, it's not just social interactions or social structures.
*  So I wanted graphs like I loved graphs since I was very young.
*  Just like anything that has to do with graphs and how representations
*  in the brain would mediate it and how there's particular structures
*  of the human brain that makes it possible in a way that it's not possible
*  as far as we've seen in our evolutionary cousins
*  or the species that we know.
*  What's before we move on, because I have a thousand questions.
*  What what's something that's just out of your reach right now?
*  Something that I would die to want to answer.
*  No, I wouldn't want to advocate that.
*  I said that metaphorically.
*  We get it. Yeah.
*  Something that I would really love to answer is so.
*  There are, of course, different kinds of meta learning.
*  One thing I'm very interested in is how algorithms are meta
*  learned throughout evolution, so not just certain parameters, but algorithms.
*  And second, how the human prefrontal cortex makes it possible to
*  to sort of to learn and drive
*  it with many, many different algorithms, more possibilities of algorithms
*  than are, again, our evolutionary cousins.
*  So I think something that's very interesting is algorithms are limited.
*  The further earlier in evolutionary time we are,
*  algorithms are of a given organism are more limited.
*  A given organism can have one or two algorithms very early on,
*  and then it grows and there is more that they can do.
*  But there are limits for many species, obviously for humans, too.
*  But in a very meaningful way, we are capable of running
*  so many different algorithms that I agree with those people
*  who say that human nature is not fixed, but it's defined socially
*  and together with the algorithms that we agree with.
*  We agree upon to a large extent, obviously not 100 percent.
*  But I think Franz de Waal made this point very compellingly,
*  comparing chimps, bonobos and humans, suggesting that humans
*  can override their algorithms or determine their algorithms
*  and behave like different kinds of
*  nature, so to speak, quote unquote.
*  So I think that the idea.
*  So those two things like how how different kind of architectures
*  capable of different algorithms evolve, but more importantly,
*  how the human prefrontal cortex enables many different algorithms
*  within the same. And can we build algorithms like that?
*  That's are capable of flexibly just sorry.
*  Can we build architectures like that?
*  That's are capable of just flexibly hosting many different algorithms,
*  for lack of a better word.
*  Jane, the prefrontal cortex is just an LSTM that that enacts
*  all of these different algorithms in its dynamics, right?
*  Can you just answer this for Ida and then satisfy her curiosity?
*  You know, I was just thinking it's very interesting that the
*  our just out of reach questions seem to to match what we have each done.
*  So we should probably have a lot more conversations about these things.
*  Absolutely. Yeah.
*  Yeah. I mean, well, I wouldn't necessarily say that the prefrontal cortex
*  is just an LSTM that even though maybe maybe you'd be forgiven
*  for thinking that that's what we're saying in our paper.
*  But yeah, I mean, I was on Ida's
*  the wonderful learning salon to talk about these kinds of things
*  not too long ago as well.
*  And I, you know, been thinking a little bit also about meta learning
*  in evolution and how these, you know,
*  how you can have these very long scale learning loops
*  that emerge and that gave rise to our ability to have a brain
*  that can can learn across our entire lifetimes.
*  I mean, at some point, some kind of mechanism must have kicked in
*  that allowed it to bootstrap itself to be able to give rise to this kind
*  of flexible learning that nonetheless persists.
*  And we continue to learn throughout throughout the course of our lives.
*  What about I also go ahead. Sorry.
*  Well, I mean, I would say I also wouldn't say that I know the answers
*  to these questions, and I also think that, you know, I share Ida's
*  desire to know much more about these things.
*  I think that it's very much an untapped area.
*  Am I right to think of meta learning as an algorithm itself?
*  So that just interrupt me.
*  But, you know, so Ida's question was about
*  the sort of explosion of algorithmic capacity and the meta
*  algorithmic learning.
*  I don't know what you would call it.
*  But is that something that lands with you?
*  And because I think of meta learning and multitask learning and all,
*  you know, all the lifelong learning approaches as different algorithms
*  to do lifelong learning.
*  But I guess what Ida was asking, and you should clarify, I suppose,
*  Ida, is whether there's an there's a way to
*  exponentiate algorithms themselves and have them meta learn.
*  I guess one thing that I wanted to highlight in that question
*  that I think about a great deal, to be honest, is what are the principles,
*  learning principles of architectures that can host many different algorithms
*  and not just the driving force of a particular algorithm,
*  not just meta learning of a particular parameter in an algorithm,
*  but the learning principles or meta learning principles for architectures
*  that can host many different algorithms without mixing them up,
*  without catastrophic forgetting, without like, you know, the dog forgetting
*  that it's a dog and thinking it's an eagle, you know,
*  for lack of a better analogy.
*  So, yeah, so that's that's what I had in mind.
*  So it seems like humans are capable of a lot more.
*  Maybe I'm optimistic about human capacities,
*  but we can just imagine like as a as a as a parent, as a partner,
*  as a friend, as a child of somebody, as a as a as a colleague of somebody,
*  as someone who's a customer to get coffee, as someone who's just crossing some
*  border during covid.
*  We take so many different, very detailed roles very quickly and very flexibly.
*  And in each of them, not only do we have different algorithms,
*  it's almost we are different selves.
*  And obviously, that's another thing.
*  I hope like when I get older, I think I hope I get old enough
*  to at some point start like writing about the self and this different.
*  You got to have a bunch of cats to do that, I think.
*  There you go. Cats who think they're eagles.
*  But but then
*  we do that a lot and very fast within the same day, within moments.
*  We switch these roles like, you know, you switch the role
*  from being a parent in the pandemic to just turn on the camera
*  and you turn into a teacher or you're at an important board meeting
*  or somebody's a judge or, you know, so this ability to this flexibly
*  adapt, adopt many different algorithms and switch between them
*  without forgetting to breathe or like, you know, forgetting to how to talk
*  or forgetting your other languages if you speak multiple languages in different meetings.
*  I think that ability is very interesting.
*  And I mean, it's definitely not necessary for survival.
*  So that doesn't seem to be the end goal.
*  So if you just set the end goal of some systems to survive bacteria,
*  some bacteria colonies can survive millions of years.
*  Like it's unclear. It's excessive almost.
*  There is something, you know, maybe it is towards like we are like the increase of
*  we are in our kind of,
*  you know, the new architecture is increasing entropy by allowing
*  too many different algorithms.
*  And that's how we're participating in the expansion of the universe.
*  But it's definitely not parsimonious.
*  And that's something I think about a great deal.
*  We are not parsimonious entities.
*  Our evolution is not parsimonious.
*  There's something.
*  And I want to understand what is that learning principle
*  or something else that we haven't maybe yet addressed,
*  which is not just the simplest solution to my self-surviving
*  and my offspring surviving.
*  But there's maybe maybe it is connected to the next question
*  that you have already sent us in a list of questions.
*  I don't know what that is. I've thrown them out, basically.
*  So you had this question about meaning.
*  And I think about that's a great deal, whether at some point are
*  due to our social structures and language of everything,
*  we created some other kind of collective organisms.
*  And they are now the ones who are trying to move forward.
*  And it's not individual fitness
*  or the survival of individuals anymore in our species.
*  Something else is going on.
*  So I'd love to talk about it more.
*  I don't want to. And I'd love to hear what Jane and also
*  Alana have to say about this. But.
*  Do we want to go down the meaning road right now?
*  Or I was going to ask about humans specifically.
*  I'm open to go down any road you guys want to go down.
*  No, humans first. Why not?
*  Well, OK, because Alana, you study language and vision,
*  but I'm going to focus on the language aspect of it.
*  And language is supposed to be the fancy human thing that we do.
*  And so, you know, so AGI, right?
*  Artificial general intelligence is supposed to one way to look at it
*  as human like A.I. and that that is a goal of A.I.
*  is to do human like things.
*  And what I was just talking about is the
*  part of what she was just talking about.
*  Thinking about the these higher.
*  You know, long term agency and these higher cognitive functions
*  that humans seem to excel at specifically relative
*  to the rest of the animal kingdom, et cetera.
*  OK, so more of X paradox, right?
*  That's the idea that the things that seem hard,
*  reasoning, chess, go, those are the easy things to do.
*  However, the things that seem easy, walking,
*  catching yourself when you fall, et cetera,
*  those are things that are hard to do in A.I.,
*  but easy for all animals to do. Right.
*  But are these OK, so my question is, is
*  my question is, what's more impressive in humans
*  if we're going to stick to humans here for a moment, language
*  or this long term agency, this higher level
*  ability that Ida was waxing poetic about?
*  Yeah, I'm not sure that the second could exist without the first.
*  Do you think like I think language is the thing that helps us to create
*  the agency that helps us to build the society that allows us
*  to have the long term agency that we enjoy today?
*  I'm not sure that means that one is more important than the other,
*  but I just think one is sort of dependent on the other.
*  I agree. But aren't we finding out with the language models
*  that language isn't all that hard?
*  Oh, geez, is that what you think we're finding out?
*  That's what that's what.
*  Well, so I know that just like there are adversarial examples in vision
*  and we haven't solved vision, et cetera, and they fail in different ways
*  than humans fail.
*  But the just the ability to string together sentences
*  that you could interpret having some meaning.
*  And I guess we can bring meaning back into this.
*  It seems and you could use, you know, like you're saying,
*  you compare vision and language, and there are a lot of similarities
*  between them.
*  So that might lead one to believe that there aren't that many differences
*  algorithmically, computationally between how we process language
*  and how we process vision.
*  It's you know, that's that's why I'm asking you guys.
*  Well, so I guess my comment.
*  So I've in my work found a lot of overlap in computer models,
*  the vision and computer models of language.
*  But really, I mean, when I'm talking about I'm talking about like
*  this single word concepts.
*  So like CNN's representation for a ball is more similar to a,
*  I don't know, a bat than a car or something like that.
*  And the same thing is true in computer models of language.
*  So that's true.
*  But then I think when you get beyond the even like you were saying,
*  like they generate these sentences that you may be able to interpret.
*  I believe that's true.
*  But I also believe that part of that has to do with the creativity
*  of the human mind.
*  So we see a single sentence and we can think of an interpretation of it.
*  But I think many of us have had the experience of interacting.
*  Well, many some of us computer scientists have had the experience
*  of interacting with a language agent like GPT-2 or whatever,
*  and finding that it very quickly runs into a wall.
*  Right. And it's actually not as coherent as you might have thought it was.
*  I think there's still a lot left to be done there.
*  I don't think we're anywhere near having language solved at the global scale,
*  possibly at the at the local scale.
*  We can generate the next word in a sentence, given some context.
*  And that next word might be reasonable.
*  But trying to have a back and forth language generation,
*  like a dialogue system is still pretty far from optimal.
*  I was just going to say, I agree with everything that Alana said.
*  And I think that, you know, just to add that there's a difference
*  between language and communication.
*  I think that these generative language models are really good at essentially babbling
*  and they're good at pretending, I think, to be to be communicating something.
*  But can you really communicate if you have if you're not goal oriented,
*  if you don't have any kind of reason to be saying these things,
*  you're just saying it to sound like,
*  you know, whatever data set that you train these models on.
*  Because the loss function is completely wrong, right?
*  The loss function is completely off base.
*  It's like generate the next word in the sentence.
*  That's not what people are doing, right?
*  People are doing something much higher, much more goal oriented.
*  Are they are they, though?
*  Aren't you right now? Aren't you trying to get interesting and provocative things
*  right now in podcasts? Isn't that what you're doing?
*  Yeah, but I but there's some random number generator in me also
*  that is sort of producing what's coming out of my mouth.
*  So, I mean, because the people are not very good at randomness, just to be clear.
*  So I grant you that.
*  But, you know, one of the things like that you're interested in, Alana, is,
*  you know, figuring out how how to
*  build language models that understand meaning.
*  Right. And OK, so we can get back to meaning.
*  And I don't know that we understand in the way that we
*  believe language models should, quote unquote, understand.
*  My particular understanding is fleeting and shallow.
*  And I barely scrape by.
*  And I don't know that I have this.
*  I guess it would be a benchmark of whatever we're trying to build,
*  of understanding and meaning.
*  And so maybe I just don't understand it.
*  I think I think if we measured your brain activity as you experience the world,
*  we would find that you do understand it.
*  And we would find that there are differences between what your brain is doing
*  and what what our computer models are doing.
*  Yeah, I would hope so.
*  So I like to think of like so the brain when we do brain imaging,
*  we're we're measuring the artifacts of the algorithm.
*  We're measuring like the intermediate stages that the algorithm
*  sort of outputs in order to do its next step.
*  It's like the ticker tape in a turning machine.
*  Right. Like we can see the states that are happening,
*  but we don't have trouble seeing the actual operations.
*  I think if we could do that well in humans, we would have some sense of what people
*  what people's algorithm is.
*  We might be able to trace back to the actual steps you're doing.
*  So even if you're not really able to write down why you came to whatever conclusion
*  you came to, why you decided to say the next sentence, if we were able to see
*  sort of the mid steps in between you understanding what I had said
*  and you deciding what you were going to say, you might be able to trace it
*  ourselves, even if you can't recall it.
*  Do you think like do you think that maybe I'm misunderstanding you?
*  Is that what you were getting at, that you have this?
*  You're not able to explain your own reason for doing something.
*  Well, that's
*  somewhat adjacent to what I was saying.
*  However, I was going to ask Ida anyway, so this is related.
*  So Ida, you know, you've studied successor representations
*  and there are all these different algorithms for learning the structure,
*  learning a representation, learning the structure of a cognitive map and so on.
*  But is it possible that, you know, the that these algorithms aren't discrete?
*  So this is what I'm getting at, Alana, by
*  maybe maybe it isn't discrete in the algorithm in my own brain.
*  Maybe there are so many damn neurons.
*  There are so many different algorithms that are mixed and matched.
*  I could almost invent one with my random number generator,
*  invent an algorithm that learns a representation and have some confidence
*  that I could find a correlation of that in the brain.
*  And I don't know, Ida, if you have thoughts on that, like if we really probe the brain,
*  do you think that the algorithms are discrete or that it's really
*  very graded in terms of how the brain is actually computing these things?
*  Sorry, I'm getting heavy.
*  I don't know if and I'm trying to I think I'm failing to connect
*  what you're saying to the current discussion, but let me try to try to understand it.
*  There is what a neuron does.
*  And there is what
*  there is a space space that we infer based on the activity
*  of populations of neurons and their connection to behavior.
*  Usually when we think about representations that are abstract
*  or representations in general, even when they're discrete,
*  at least the ones that I study are within that state space.
*  And even when it comes to place cells and place fields,
*  the that the successor representations, the closest thing it can do to the cellular level,
*  it's about place fields, which can be, which has a particular principle of it.
*  And that even is a relational
*  concept that's relating particular neural activity to behavior.
*  And so some of the states, states, spaces that we are talking about
*  have discrete representations and some of them have more continuous representations.
*  And some neurons seem to be firing.
*  Most neurons seem to be seem to be firing in a kind of a continuous way.
*  But some of them are some things are sensitive to particular thresholds.
*  So it's almost a little bit more close to not being continuous.
*  But I don't work at the level of cellular neuroscience to say anything about that.
*  That's completely outside of any realm of expertise for me.
*  I work at the computational algorithmic, whatever level that
*  Marians and anti-Marians would like to call that is not the lowest sort of
*  implementation at the complete cellular molecular level.
*  But what I would say is that the state spaces that are inferred
*  using math, using neural firing, using behavior could have
*  continuous and non-continuous representations.
*  Does that answer your question?
*  Yeah, a little bit.
*  I guess I'm thinking in terms of so the big success story with reinforcement
*  learning in neuroscience and in AI is model free temporal difference learning.
*  And then we've advanced and there's model based learning.
*  And then there are those two compete.
*  And now we have now we're working on a model based learning.
*  And then there are those two compete.
*  And now we have now we're getting there are more and
*  more and more different algorithms that we are building.
*  So the successor representation is an in between kind of thing.
*  But maybe there are how many different reinforcement learning algorithms
*  is our brain running is another way to ask.
*  So let me answer that question by saying that TD learning temporal difference
*  learning is also used to learn representations in the successor representation.
*  It would also be used if you don't know the model of the world and
*  you're learning in the model base, you're learning the states by learning state,
*  state association, state action, state association.
*  So it's not that temporal difference learning.
*  We saw it, it was just model free and we are throwing it away.
*  No, it's a learning principle that can underlie different kinds of learning
*  algorithms.
*  Now, if you only believed that only model free and model based learning existed,
*  then you would have to believe that the brain does both.
*  But you can have other kinds of algorithms that look like that algorithm
*  could address both of those kinds of behavior.
*  Just to connect this to maybe this is what you meant by the last question that
*  you asked, there are continuous versions of deep successor representations as well.
*  So it's not it doesn't necessarily just need things to be tabular.
*  So this tabular versus kind of rich continuous environments,
*  there are algorithms for both.
*  I personally like to focus on the tabular first and then go towards deep and
*  because I'm more interested in like basic algorithm,
*  algorithms that you can test on behavior and then go towards the deep ones.
*  So there is an infinite number of algorithms that we can come up with,
*  virtually infinite number of algorithms that use very similar adjacent learning
*  principles that might address a series of behavior,
*  but not other things or a subset of behaviors or a subset of combination of
*  neuroscience findings and behavior.
*  So to think about giving a number and saying magic number eight.
*  Come on, I'm probing you. You got to give a number.
*  Seven minus plus two or things like that, or three or two or one or,
*  you know, 42 or whatever your favorite sort of way to answer these kinds of
*  questions is or dual systems. Everybody loves dual system.
*  And then the third way.
*  And then there's a lot of ways that one could do this.
*  But what I'm trying to highlight is that.
*  Although we are those of us who are trained in the Middle Eastern
*  slash European culture of thought are very into dualisms,
*  but it doesn't mean that that's necessary.
*  The algorithms that we would find that there is two and when there is a three,
*  oh, no chaos.
*  I think that we should think in terms of learning principles
*  and just develop as many algorithms as needed until we have something
*  that captures a lot.
*  And I think I'm on the side of all the algorithms that we have.
*  Eventually, there will be a better algorithm that captures more things.
*  And my goal is just to make sure that I refute my own algorithms
*  or improve them during my own lifetime.
*  And somebody else will do something else.
*  So I don't think that I personally don't think that you will find
*  the exact model for your model base in the brain.
*  I think that these are these could fit in some situations, but not others.
*  And we are just trying to improve the algorithms based on similar
*  learning principles that all of them use just with small differences here or there.
*  Some of these differences, however, make a huge difference like model
*  three versus SR slash model based huge difference, because it just doesn't
*  care about states, representations or interactions of states.
*  SR and model based, they get much closer because they actually care
*  about the representation of states in absence of rewards.
*  There is learning happening even without rewards, which means
*  this is the first algorithms first or at least minimum
*  RL algorithms that can learn something like latent learning.
*  That said, if you go in the deep RL domain,
*  there are some things that they call deep RL that is model free,
*  but it's not really model free because it has so many layers that is actually
*  learning some things about the states in the middle of those layers.
*  So I think there is some care that should be taken into account
*  when we call those models because they're not really model free,
*  especially when they have many layers that are learning different kind
*  of representations to reach to that point.
*  So I think there is nuance in the term.
*  In the terms, there is qualitative differences, at least in the tabular
*  domain between model free and SR and model based classes of algorithms.
*  But there are also similar learning principles underlying all of them,
*  such as temporal difference learning.
*  And I don't mean just temporal difference learning of rewards, as in model free,
*  but temporal difference learnings of the successor states or temporal
*  difference learnings, learning of transition structures.
*  So, Jane, Ida says the answer seven.
*  Do you agree with that?
*  I did not.
*  I'm wondering if you have just from a meta learning perspective and
*  continual learning perspective, if you have thoughts on top of that?
*  I guess. I mean, one thing I was thinking when you first asked this question,
*  you were saying, you know, how many RL algorithms does our brain hold?
*  I think that was a question.
*  But I guess I don't think that reinforcement learning or even learning
*  in general is necessarily what our brains were built to do or is like all
*  that they do.
*  And I think learning itself is a continuous concept and that we should
*  take a more broad approach than just to say, you know, algorithms or we want
*  to learn about, we need to understand learning only in terms of the kinds of
*  algorithms that we have.
*  I think that there is basically as a consequence of us being embodied in the
*  universe and us needing to persist, there are various adaptations that
*  different organisms take in response to the challenges to those to be able to
*  persist, essentially.
*  And so I think learning is a very important part of learning.
*  So I think it's all just in pursuit of something else.
*  Right.
*  And I think CD learning might be a nice way simple way to encapsulate the
*  concept of growing an ecosystem and we can expand our culture.
*  Maybe we only have it within the organisation of learning, but grows
*  it within it.
*  So that we can have that community support instead of just a self provide
*  simple way to encapsulate the way that organisms tend to do this, where we have some sort of target,
*  we have some optimal point that we want to get to, and then we can get to it via these tiny
*  adjustments towards that optimum. But I think that that's all just a, it's part of a larger,
*  more like generic system, like dynamic system that we're just a part of. So I'm getting a little bit
*  philosophical and abstract, I guess, right here. But I just been inspiring me to.
*  Oh, wait, wait, I'm going to disagree with you there, though, because I feel like some of the
*  things that you said might be contradicting each other. It's one thing to say the capacity for
*  learning didn't, was not the ultimate purpose of life or how life adapted, but learning, especially
*  expansion of brain architectures that can learn better is, did become one of the, let's say, auxiliary
*  sort of things that emerged. So it's not that we're saying that nobody's saying learning is
*  the ultimate goal of the brain. But it is one of the principal things that it does. It's a sub goal
*  towards something else. Maybe it's in, I think it's no longer just individual survival, hopefully.
*  So hopefully it's going to retrace it towards ecological survival as opposed to ecological suicide.
*  But I guess I just, I don't mean that, I mean, certainly the learning is what the brain does.
*  But I guess I don't see it as being distinct categorically from other kinds of adaptation
*  that maybe you wouldn't consider like brain, like to be a brain. You know, like you can
*  think maybe on one end of the spectrum, a riverbank is learning the water that flows over it. And
*  erosion is then going to be the result of that. You know, plants to a certain extent to learn as
*  well. And they adapt. Okay, so I was saying at one end of the spectrum, so like, I wouldn't
*  necessarily say that a riverbank is learning, but it is adapting in a sense. And I think that that's
*  just one extreme of a continuum at which the other end is the human brain.
*  I think I can see your physicist intuitions.
*  But both philosophically and cognitive scientifically speaking, I would disagree that
*  erosion or I wouldn't, I'm not as interested in a frame that considers erosion the same as,
*  let's say, mushrooms that learn a particular path, because the actual structure of changing
*  yourself is different from the dynamics of things that happen to be in each other's way
*  and influence one another, I think. And so it might depend on how I think life is something that
*  it makes a difference for me, things that are living versus not. And I guess this goes back
*  to 19th century discussions of the importance of life. But I think that for me, things that learn
*  are living things, unless they are AI. So then we can discuss whether AI is a living thing or not,
*  or like, whether artificial learning is learning or not. How different is it from a riverbed? How
*  different is AI from a riverbed? Because it's, you know, silicon is extracted at the end of the day,
*  it's extracted minerals. But I think that the ways in which I agree with you, where I do agree
*  with you, is that there is definitely a continuum between, let's say, mushrooms and organisms that
*  learn collectively, and, you know, learning that we think about in terms of learning in the brain.
*  I mean, to be fair, TD learning seems to be what happens almost in, you know, even
*  sort of very early forms of life that basically move towards the gradient of, move randomly,
*  but as soon as they perceive food, move towards increasing gradient of food. That's already,
*  like, you know, I mean, it's not learning, but it's already using something that has to do with
*  temporal difference comparisons, right? In decision making. I feel like I need a definition
*  of learning versus adaptation. Oh, geez. Yeah. So do you guys know the Constructal Law in physics?
*  The what? The Constructal Law. It's actually a physical law. I think it was like 15 years ago,
*  but it's all about, he uses riverbeds as an example of, it's all about life being a flow
*  process. And, you know, it goes back to heat wanting to flow well, and riverbeds wanting
*  to flow well, and our cognition wanting to flow well, and it ties it all into basically,
*  whatever takes the fastest path to flowing well. People can look it up, I suppose. Sorry,
*  I interrupted Alana. But the riverbed example reminded me of the Constructal Law in physics.
*  So I'll send you guys a link. I totally can see that many physicists would see it and many kind of,
*  I would say poets would see it the same way. I think that the side of me that's, there is a
*  side of me that can't, that likes this idea of thinking about cognitive flow in the same way as
*  a riverbed, etc. But at the same time, I do think when we are specifically talking about learning,
*  and let's say TD learning, there are living beings that don't have a brain that seem to show similar
*  principles, but I wouldn't consider what happens in a riverbed to be able to relate to it. So I do
*  think there's something special in certain forms of learning that's specific to, or certain, at
*  least mechanisms of learning that's specific to living things. I'd like to hear what Alana was
*  going to say. You wanted a definition of learning, right? Yeah, I mean, I guess I just feel like
*  following a chemical gradient, or even evolving to follow a chemical gradient, I just feel like
*  it doesn't satisfy me as a kind of learning. Like it was evolving to move either, yeah, evolving to
*  move randomly until you hit the chemical gradient, then following it. That evolution is not some kind
*  of learning. And then the next phase of the evolution is, you know, they develop eyes,
*  for instance, or they develop. That's the next stage. And then I think it's interesting to think
*  about what's the place where you hit learning? I mean, does learning have to be something overt?
*  Because evolution is just a random walk in genetic space, right? I mean, not entirely random,
*  because some of them, the ones that do, many of them die outside, at the end of the day,
*  it's not that random. I guess the steps are random, although the success is not. You're right.
*  Yeah, so it's a random search. The mutations are random. Yeah, but the function determines.
*  Okay, yes. We did have a session at the learnings along with Sam Gershman, which regarded learning
*  in the single cells. So there are some people who think learning can happen at the single cell level.
*  And Alana, I don't know, like, how much I don't know how further down in the sort of the
*  cellular level you have worked, but I haven't worked at the single cell level myself.
*  So anything that I would say on that would be based on what I've read and what I've heard.
*  But I think there is, and we did have this discussion to whether this is learning or not.
*  So it seems like some people, especially people who don't work at the cellular level, don't like
*  to call this learning. But do you think that a virus can learn? Yes. It's true.
*  What's that? Do you think COVID has learned?
*  Yeah, I just was listening to this podcast. Well, actually, anyway, they were talking about,
*  like, oh, the flu is like this cunning virus that's figured out. And somebody said, no,
*  the flu is a clumsy virus. The flu has tried every damn thing. And the only thing that's left is the
*  one that works. It's not smart. Right. And so is it learning? It's just sort of fumbling towards
*  the right answer. Isn't that how we learn also? We have to try.
*  Yeah, I know. I was thinking like, what's the difference? Like, don't you try a million things?
*  Literally, right now, I'm out loud trying a million things and seeing which ones of them work.
*  There's this concept of a goal, right? That it's like goal driven. And that if maybe you
*  would consider a riverbed or a single cell organism that doesn't necessarily have a goal,
*  they just sort of have a consequence to. I don't equate riverbed with single cell
*  organism. I think there is a huge difference. Well, how do you define that then? Why does a
*  single cell organism have a goal, but a riverbed does not have a goal? What do you think life is?
*  Do you think a riverbed is alive? Are rocks alive? Are rocks alive? Do you need to be alive to learn?
*  Unless you're talking about an ecosystem, it seems like you're not talking about an ecosystem. You're
*  only talking about the rocks and the water flowing on the rocks. I am talking about a system. I'm
*  talking about the entire, the water. No, I don't mean a physical system. I mean an ecosystem in
*  which there is life and there is a sustaining life. So that's different. There is a difference
*  between just water and rocks and an ecosystem where there is other, you know, there is actual
*  life forms. Well, I mean, but at our fundamental level, we are just a set of differential
*  equations, right? That we can program at a fine enough level. We can program any organism.
*  I don't agree. Do you think we can program rocks?
*  I'm talking about a dynamic system, right? A riverbed is a dynamic system.
*  Okay. So I'm asking you if you think there is a difference. I understand that this perspective
*  could see anything as a dynamical systems. And I think on some level we can see all of them as
*  dynamical systems. I'm asking if you think there is a difference between a living thing and a non-
*  living thing. Yes, I think so. I don't think a rock is living. So do you think a single cell is
*  living? I mean, I guess according to the biological definition of living, yes. But I mean, you know,
*  what if you ask me, like if I consider that the earth is living or if I consider...
*  The earth is an ecosystem. It's not just... Do you consider ecosystems to be alive?
*  Yes. I'm not the only person either. They breathe. They, you know, they have like cycles. They have
*  certain things that sustain them. You and I, each of us is an ecosystem. In fact, we are...
*  There are so many bacteria living in and around and on us that are sustaining us entirely. And if
*  that ecosystem of other species that are living within us gets messed up, we get messed up.
*  So the earth is in some way similar. Any ecosystem is a living thing. But it's different from
*  just rock and water or two physical objects that are hitting each other.
*  Well, but you can take any physical system and complexify it enough and you can zoom back out to
*  a large enough level that it can look living. It can just, you know, take any kind of complex
*  system. I mean, you look at... You're saying all complex systems are living?
*  I think they, from a certain perspective, they can be. Yeah.
*  So internet is living?
*  I think definitely the internet is living.
*  So do you think the internet is the same as a single cell, the same notion of life?
*  No, no. I think, I mean, so by your definition, you consider the entire earth to be living,
*  any ecosystem to be living, but that doesn't necessarily check all the boxes for biological
*  life, which is they have to reproduce, right? Or they have to... I think that there are
*  different ways that you can consider things to be living.
*  Ecosystems do reproduce and do sustain themselves. They do have seasons, they do change, they do,
*  you know...
*  I don't think the earth has reproduced itself yet. And if it does, we should really,
*  you know, find out other earth because we're in trouble.
*  Well, with the multiverse, I suppose.
*  We're reproducing earth, but the ecosystem is not the rock that is the planet with a heated core.
*  That's the one that it seems like what we are destroying is actually the ecosystem on top of it,
*  which if you do reforestation, that's actually like replenishing it. So it does get replenished.
*  If a seed drops or a particular number of seeds drop, another forest emerges. That's what I mean
*  by ecosystem, not their heated rock or like cooled on the surface and heated at the core rock.
*  That is not what I meant by reproduction. I'm not suggesting that planets reproduce
*  as in they either duplicate or they have... I don't know, they mate and create a new planet
*  that's between the two. I certainly love that story. I would love to see a book that's a
*  science fiction about that. That's very cool. But that is definitely not what I was suggesting.
*  In a similar way, though, I can see the internet as being self replenishing.
*  Right.
*  Because of the humans that are connected to it. If you mean the internet as in the system of
*  computers plus the humans that connects them, that's a different... That definitely is a different
*  kind of entity because there are humans attached to it. They are alive. So as soon as you consider
*  them, it's a different story. So anything that has something living within it is alive, but then you
*  need to define what it means to be alive for the entities that are inside the thing that you're
*  calling alive. Yeah, biological.
*  Yeah, but I just... I mean, I feel like it's...
*  I really think this is not a confusing thing at all, to be honest with you. It's very clear to me
*  that a bedrock in a river and a cell are not alive in the same way. And the notion of learning that
*  we can apply to a cell and anything that's multiple cells is different from the notion of
*  the way that a bedrock might change its shape because water flew over it for a million years.
*  That's something that I think it's not... For me, it's not a continuous thing. It's clear.
*  But I agree with you that if one wants to take the perspective of dynamical systems,
*  that might be... If you just want to look at it from that perspective and not from the perspective
*  of what at least we mean so far by the notion of learning, there are continuance. If you want to
*  see whether you can get inspired by the dynamical systems that you developed to study the bedrock
*  and then use those dynamical systems and equations to study learning, I can totally understand that.
*  Different story though, I think. Sorry, this took longer than I thought it would.
*  Yeah, this was a little bit of a tangent. I regret my riverbed example.
*  I'm sorry about nitpicking on that example.
*  Well, we have five minutes left. Should we bring it back down to earth? No pun intended.
*  Yes, please.
*  I have a lot of different questions. Do we want to end up talking about cognitive maps and are
*  thinking about whether we have that right? Do we want to talk about the balance of unsupervised,
*  self-supervised, reinforcement learning and supervised learning in the brain?
*  Or actually, maybe we should talk about meaning and whether meaning is just a relation between
*  concepts and or whether we need grounding, like what meaning is, because that's what you're
*  interested in figuring out with language models, if I'm correct. What is meaning, Alana? What
*  is meaning? How do we get meaning? We'll end on an easy one.
*  Yeah, I don't know. I think there's lots of facets to that that are hard to untangle, but
*  there's certainly something that's emerging in our computer models of language that seems to be
*  getting closer to meaning. But it is interesting to think about that our computer models have no
*  concept of what the real world is. And so they say cat, but they don't really understand cat
*  in a grounded way. Is that necessary to understand the world? I mean, I kind of feel like it is,
*  especially for some kinds of common sense reasoning. I'm not sure we can get the whole way
*  with the kind of text that we are using right now to train our models. Although I did hear one
*  interesting thing sort of proposed by someone that if we had the right kind of textual data,
*  we might have enough that if we had, it might be enough to if we had the right kind of text data,
*  not just any old random internet data. So if we had people in dialogue, that might be closer to
*  what we need in order to get grounding, because it might be more about the world rather than just
*  sort of adjacent to the world. Can you elaborate briefly what grounding entails?
*  So grounding is understanding the connection between a representation that lives in our brain
*  or representation that lives on a computer and the real world, right? Like what is cat?
*  Cat is a thing in the real world. And what, how would I know if I saw a cat? How would I know
*  if I heard a cat? What's the, what's the connection? At least that's what it is to me.
*  I think grounding is probably one of the biggest things that these language models are missing
*  in that they are not, I mean, the train on text generated by humans that are grounded,
*  that are living in the world and are talking about things that are grounded.
*  But the language models themselves are not grounded because they are sort of adjusting,
*  you know, just data from all different sources and they don't like care where it's coming from
*  or how it's grounded. And so I think maybe that's the distinction in my mind.
*  I think maybe based on that distinction, I'll just say that even if there was a meaning at some
*  point that these, we could ascribe to this language models understanding, it's not the same meaning
*  that we understand. It's a different thing based on the objectives that they were provided,
*  of what kind of tasks they were trying to solve. It's not the same meaning that we use language for.
*  And so I think that's an important distinction too, because of the same things that Alana was
*  saying that, and also Jane was saying that we have these goals and that's why we're using these
*  languages to communicate. But the reason that that model is using language is because of some
*  objective function that was defined for it. It's not the same goals. It's not the same motivation
*  for communication. It's not the same thing to sort of sustain a life, et cetera. So I think that
*  I think that in this way that they are, even if at some point we manage to magically just like,
*  move a wand and then they're going to have meaning, it's not going to be the same meaning we have.
*  I want to say one thing there that like, it's interesting to me that two models, let's just say
*  computer models can have very different goals and end up with representational spaces that are
*  actually pretty similar. So I do agree that without similar goals, their representations will never be
*  the same, but it's interesting to me that we actually don't have to have the same goals to
*  have very similar representations. Right. I wasn't talking about representations, but understanding.
*  So I was saying that the objectives that humans have and the objectives that the language models
*  have are so different that even if they had some notion of understanding, it's not going to be the
*  same understanding that we have, let's say of the word cat or dog, unless they start to interact with
*  it in a human way as well, which they are not. So I don't think that the distinction between
*  objectives in a language model and the objectives of language in a human, I don't think that
*  distinction is close enough that we would either have similar understanding or that similar
*  representation unless it's on a very kind of broad notion of representation. But I wasn't
*  talking about representations, but understanding or meaning.
*  So I love where this conversation went. I have no idea how useful it is, but let's end on a very
*  practical notion and then I promise we'll wrap up. Alana, most people go through academia, they do
*  the graduate work, they do postdoc, they get faculty and or go on to industry. You kind of
*  did that backwards by starting at Google and then going into academia. Is that a recommended path?
*  What do you think maybe benefited you and or you might have been missing and do you recommend that
*  to other perspective humans? I think every computer model should work at Google.
*  So working at Google was fantastic and I was like a hundred times a programmer I was when I left
*  then compared to when I started. So I think that benefited me a lot when I got to grad school
*  because pumping out code was no problem at all and I learned a huge amount there.
*  If it kind of fast tracked your faculty position as well, you went faster I think than most.
*  Skipping the postdoc isn't completely unheard of. Maybe in the computational world it is in the
*  experimental world. It's sort of because of places like DeepMind and Microsoft there's a strong pull
*  for people to go to industry and so you can go straight to faculty from a PhD.
*  So that was good for Google. Also I got a down payment for a house by working at Google.
*  I also highly recommend that. Although I was living in Pittsburgh as you know and Pittsburgh
*  is a buying house in Pittsburgh is pretty easy. I mean I think it was the right decision for me.
*  It also really helped me to solidify my goals and made me realize that it matters to me why
*  I'm solving the problems I'm solving. I loved working at Google because the problems we solved
*  were challenging and they were extremely technical but the reason why we were solving them to me
*  wasn't the sort of thing that got me up on Monday morning excited. You know what I mean?
*  But if you're the kind of person who just loves solving technical problems for solving technical
*  problems then it's a fantastic place. Where I was would have been a fantastic place. But I wanted
*  to solve a problem and be sort of passionate about that problem.
*  Ida and Jane you're both half in academia now, half in industry I suppose. Do you have any
*  reflections on that or perspective to close out?
*  My perspective? Well I mean I consider my job to be mostly really similar to academic.
*  I wouldn't say that I would really even know what it would work. It would be like to work in a more
*  industrial or commercial technical setting. Because I'm not working on production level code or
*  creating any kind of products or anything. I do mostly research and write papers and give talks
*  and do fun things like this. I always get a lot of questions about career paths and things like
*  that. I guess if you're going to be in industry or doing industry research but you might want
*  to go back to academia it is important to continue to publish. I don't think it would be a problem
*  for me to try and look for faculty positions right now if I wanted to leave the industry research
*  type of position. I don't know if it would be harder if I didn't do any research
*  type of thing. Didn't have any research output for a few years and then going back.
*  I don't know that a lot of people go that way. I think a lot of it sounded like you went to grad
*  school. That is a more standard way of becoming a research professor.
*  Aida, I know we're late. Do you have any additional comment to wrap up?
*  Just say for me the objective was to be able to do my research. I did have academic offers and
*  this offer from Microsoft Research and other offers. What I chose was the one that would
*  enable me to do the research that I wanted to do. For anyone who might want to try
*  pursuing research outside academia, I would just say that there are many different paths.
*  Industry research does not equate coding at all. In fact, we have some computer science grad
*  students who finished their PhD and they say that they wrote barely 100 lines of code because they
*  use math to prove things. In fact, there are people at Microsoft Research who spend most
*  of their time proving that particular algorithms would converge as opposed to writing any code.
*  Then they collaborate with someone who is comfortable coding and they would provide
*  maybe the deep learning part. Not every industry research requires to be related to product. This
*  is something that Jane mentioned as well. If you want to connect to products, you can, but that's
*  extra. You don't need to. It's not necessarily required. Like Jane was saying, I'm also completely
*  focused on research and mentoring and doing exactly what I would do in academia other than
*  internships are shorter, the students are better paid, so they're in a better mood maybe.
*  The only thing that I guess I would miss a little bit is I actually enjoy teaching and having the
*  same student for five years and being responsible for them as opposed to having them for short,
*  stellar internships is a different kind of responsibility for the growth of another.
*  I do sense the inclination in myself towards that. I think at some point I might either go back to
*  academia or take on more of these kind of co-advising roles and some forms of teaching that I do, but
*  maybe do more of that. Other than that, if someone doesn't like those parts, if that's not something
*  that they like, there's really room for doing very good high-level research in industry.
*  Go back to academia as soon as you get that down payment for the house. I think that's wise.
*  I was not in a research position at Google. I was a software engineer.
*  Right.
*  We did do a little machine learning, but it was totally for production.
*  Yeah, that's why I was asking you to begin with. Guys, this has been a fun meandering down the
*  river bed. I think this is a really good way to close out the Neuromatch panels here, so thanks
*  for being with me. I appreciate it.
*  Thanks, it was fun.
*  Thank you.
*  Yeah, it was fun.
*  To get in touch with me, email paul at brandinspired.co. The music you hear is by The New Year.
*  Find them at thenewyear.net. Thank you for your support. See you next time.
