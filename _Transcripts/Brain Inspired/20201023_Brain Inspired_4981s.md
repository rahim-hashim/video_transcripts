---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4981s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 16221
Video Rating: None
---

# BI 087 Dileep George: Cloning for Cognitive Maps
**Brain Inspired:** [October 23, 2020](https://www.youtube.com/watch?v=2oA_U5x62m8)
*  Is it harder than you thought? Is it more fun than you thought?
*  It's definitely harder than I thought. So, it's basically saying if you knew it was this hard, you would never get into it.
*  Thinking about space as your sequence is something that takes a little bit of practice. That's what I realized.
*  Because when you think about modeling space, people naturally think about grids.
*  People have done a lot of clever experiments about the brain.
*  And that's often a lesson that is missed in machine learning, I think.
*  Blank, blank, blank, blank, something. Blank, blank, blank, blank, something. That's the way it is.
*  When the waiter hands you your bill, should you pay or should you let your date pay?
*  I say if your date is Dalip George, co-founder of the AGI robotics company Vicarious, you let him pay.
*  Yeah, that sounds right.
*  Hey everyone, this is Paul Middlebrooks, and today I have Dalip George back on the show.
*  He was on two years ago, and at that point we talked about his graphical probabilistic models that could do visual inference to do things like solve captures.
*  On this episode, we get an update on Vicarious. We chat about his experience in general running an AI startup.
*  And then we talk about some of his latest modeling work that explains how our hippocampus takes in sequences of events and turns those sequences into cognitive maps that we can then use to simulate or model the world and run that model to decide what actions to take.
*  In particular, we focus on the idea in his model that the hippocampus could use clones or duplicates of concepts so that when we're in a given situation that might call for a variety of different actions, we know which action to take.
*  We can use the current context to decide what to do.
*  You'll also hear from Brad Love back from episode 70, which was about concept learning in the hippocampus, whom I corralled into asking Dalip a few questions.
*  So thanks, Brad, for the questions.
*  You can find Dalip on Twitter at Dalip Learning, and in the show notes, I point to the relevant stuff, brandinspired.co.uk, podcast, slash 87.
*  If you value this podcast and you want to support it and hear the full versions of all the episodes and occasional separate bonus episodes, you can do that for next to nothing through Patreon.
*  Go to brandinspired.co and click the red Patreon button there.
*  Here is our conversation.
*  I have some things to play.
*  So, Dalip, welcome back to Brain Inspired.
*  Happy second anniversary.
*  Actually, I pulled up the last episode and it's been almost two years to the date since we last spoke.
*  Oh, that is great.
*  Thank you.
*  Thanks for remembering the anniversary.
*  That's great.
*  I feel good about that.
*  And thanks for having me back again.
*  So I thought, well, I treat our anniversary, Dalip, like I treat my wedding anniversaries, unfortunately, so I didn't send you flowers.
*  Yeah, where are the flowers?
*  Paul, where are the flowers?
*  How could you forget?
*  Actually, I use my wife as an assistant here on the show.
*  So I'm going to start off the show ridiculously by playing a very brief segment from the last episode as we closed out our last conversation.
*  If you're okay with that.
*  Yes.
*  OK, so hang on.
*  Let me get my assistant.
*  Hey, Catherine.
*  OK, thank you.
*  OK, you ready?
*  Previously on Brain Inspired.
*  Dalip, what can we expect from Vicarious in the next year or two?
*  Well, one, definitely products.
*  One thing very rewarding for us would be when our products start getting used in the real world and seeing something being used.
*  That is very rewarding.
*  So that is one thing.
*  And we are working on some cool ideas related to how high level concepts can be learned.
*  And also we hope to see some of the things that we kind of champion in terms of data efficiency, cost of generating models and using insights from the brain in a deep way being taken up by the broader community.
*  OK, so that's a we have like a two year assessment now.
*  So what do you think?
*  How have you done?
*  How's it been going?
*  That's great.
*  I think it's been great.
*  I think it's been great.
*  And hearing to me reminded me why I never listen to myself.
*  Oh, my gosh.
*  Imagine I have to do it every time I edit every episode.
*  Yeah, so it's a weird feeling.
*  So I think I think we did all of those things that I mentioned in the podcast two years back.
*  So one, our robots are working in the field.
*  They're getting deployed and the deployments are accelerating.
*  So that is very cool to see.
*  And it is very rewarding to see robots doing work in the field.
*  And as we speak, they are picking and packing objects and in multiple locations.
*  Are you selling them yet or are they functioning?
*  But are you are they product?
*  Oh, yeah, yeah, yeah.
*  We are selling them.
*  We are aggressively selling them.
*  No, not not just.
*  No, we are we are going up to the market and we are growing.
*  And yeah, so the number of deployments are growing.
*  We have a good sizeable sales team now.
*  Yeah, so it's a very exciting time because one, there is a need for automation now.
*  And there is a recognition from all the players in the field that, OK, this is robots can do these things now, which they couldn't do before.
*  Yeah, so overall, it's a very exciting time at VKDS.
*  Yeah, I guess the last time we talked, you guys probably had a handful of employees, but now you're up to 100.
*  Yeah, we are now 120.
*  Wow. Yeah, that's great, man. Congratulations.
*  Thank you. Thank you.
*  It must be so satisfying to grow.
*  I mean, I want to start off talking about the vicarious a little bit.
*  But but there are the other two things that you mentioned in the last episode, which was developing this high level conceptual model,
*  which is a large part of what we're going to talk about today.
*  So that was great.
*  Yes. So that particular one was in relation to a project that we have been working on at that time.
*  How do you learn concepts, higher level concepts, higher level concepts would be, for example, simple ones would be, OK, two objects are touching.
*  One is above the other.
*  The glass is half full.
*  Those kinds of things.
*  What does touching mean?
*  What does above mean?
*  What is left, right?
*  You know, in a line, in a circle.
*  How are all these things learned and represented?
*  That was the question that we were after.
*  And so we did have a good project on that and we had good success on that.
*  So we had a paper in Science Robotics about that.
*  It is called Cognitive Programs.
*  You know, that's what we call it.
*  And the main idea there is that concepts are learned as programs.
*  And concepts are learned as programs on a very, very special kind of computer.
*  So this is a computer that we call Visual Cognitive Computer.
*  And all the pieces that we developed earlier, the RCN visual hierarchy, the schema networks for dynamics, all of those pieces are part of this computer.
*  Because you need to learn programs that can imagine visual concepts and manipulate them in the working memory.
*  So all these pieces come together and then you learn programs on this cognitive computer.
*  And that's how concepts are represented.
*  And so this paper was published in Science Robotics.
*  And it was pretty cool because you can now convey an idea to robots using pictures.
*  So you can say, you know, just like IKEA assembly diagrams, you can say, picture A, picture B.
*  What happened between A and B? Do that in the real world.
*  So you have to understand what happened as a concept in the picture and then transfer that to the real world and do the task there.
*  So that's how that were the demonstrations that were part of the paper.
*  And so that was that was actually pretty cool.
*  Yeah, it's great.
*  Interesting.
*  And I guess the third thing before we get moving here on today's episode is that hoping that there is more brain like implementation in AI systems.
*  And I don't know.
*  Do you think that that has come to fruition?
*  I mean, I know you have.
*  At least I'm see.
*  Of course, there is this one track of AI development, which is, OK, let's take existing models or new versions of them and just scale them up.
*  Scaling up transformers to get GPT-3 or making larger and larger continents, etc.
*  So those are successful tracks and those will still continue.
*  But I think in the community, there is a realization that that is that's not enough.
*  You want you need models with more structure, more causal models.
*  Feedback is important.
*  Recurrent connections are important.
*  Explaining a way and passing a scene.
*  All of those are important ideas.
*  There is recognition in the community about that.
*  So I think that part is also happening.
*  I won't be able to say, OK, just taken over the field.
*  But I would say it is it is maybe 20 percent of the people now recognize that as important.
*  There's some influential.
*  OK, there's some influence going on there.
*  Do you think that brain inspired AI is overhyped in AI?
*  Oh, this hype thing.
*  I know it's very hard to get a handle over it.
*  I think I think sometimes it is misused.
*  That's I would I would say.
*  That's well put. Yeah, go ahead.
*  So you can sprinkle inspiration, biological inspiration pretty easily on anything.
*  I had I had a joke.
*  I don't know. Maybe I told this joke last time to you know, if you if you have a convent and if you if you put a different nonlinearity at the lower most level, now you can you can call it the thalamus layer.
*  You know, so it is very easy to sprinkle that kind of biological inspiration on things.
*  But so so I think that happens quite often, misusing the biological inspiration just as a sales point, because people are fascinated about how the brain works and you can use that fascination to, you know, bring attention to your work.
*  Nothing particularly wrong with it.
*  But still, we what we are doing is definitely not that level of bio inspiration.
*  We we definitely dig very deep into into neuroscience and to see what are the principles that we can learn from neuroscience.
*  So so it's it's a I don't like calling it bio inspired anymore.
*  I don't know. You had to feel it almost looks like we had to find some other word.
*  Yeah, yeah. Because inspiration is cheap.
*  Well, that's right. And that leads can it can lead to overhyping.
*  Right. And yeah, and we've talked about the phrase biological plausibility.
*  And some people really don't like that phrase these days, but it's used as a selling point.
*  Got it. But do you think that the AI community does take seriously the notion that there are things to be learned by brain research and emulating brain processes?
*  Or is that still I mean, is that growing or is it still it doesn't seem to have grown at all.
*  It seems like it's still very much a really low priority.
*  I would say some subsection definitely cares about using brain as an inspiration and learning principles from the brain.
*  I don't know how deep they go into, but at least I can say that their interest is genuine and they care about that.
*  Rather than just post quote sprinkling of bio inspiration, they do care.
*  But I would say, yeah, you can.
*  The reason is that you still can make good amount of progress in deep neural networks and machine learning without having to worry about biology because of the practical applications.
*  Those things will continue.
*  So it won't be a giant fraction of the ML field or deep learning field that will be interested in learning from biology because many practical applications do not need that.
*  In fact, it can be it can be hindering if you want to, for example, find a way to model point cloud data.
*  You know, because it's a completely different sensory input.
*  That's not what humans deal with.
*  You don't. Yeah, so there can be so many different ways in which machine learning models can be applied.
*  Only a small fraction of it is relevant for biological inspiration thinking.
*  And a lot of other applications do not need to think about neuroscience at all.
*  And that is fine. And that will continue.
*  Yeah. Well, when you started Vicarious with Scott Phoenix, it was you and Scott Phoenix who started the company, right?
*  Correct. The mission was to develop artificial general intelligence and along the way develop awesome products based on the research that that you are doing.
*  So you have this sort of shorter term and intermediary term goals of developing products based on the very longer term goal of AGI.
*  Correct. Well, so how's it going?
*  You know, does it feel like high competition these days in the robotics space?
*  Or is there just so much different, wonderful projects to do that it's really not doesn't feel competitive?
*  It seems like it would feel competitive. Everyone has a startup.
*  AI wants to have a startup. AI company, perhaps.
*  Well, there are definitely many startups in the robotics space.
*  But in many of the projects that we have been working on, we haven't had any competition.
*  So that could be because one, we have some some unique selling points which others don't have yet.
*  So we do things that others can't do.
*  So that's one. And we are much more data efficient.
*  Those kinds of things come into play there.
*  You know, being able to deal with high changeover situations where the thing that the task changes quite frequently.
*  Those are the situations that we are going after.
*  And so so that gives us an edge in terms of what our systems can do.
*  And second, I think it is also true that the space is very big and fragmented.
*  It is not like, OK, one company can just go and attack all of that market at the same time.
*  So so I think both both things come into play.
*  But so so maybe you can just describe your robots and how they function just really briefly, you know, to find a thing, pick it up, move it across, put it in a box.
*  And that's a very simplistic way of saying it. But maybe you can describe it a little bit better.
*  Yeah, so we have multiple product lines here and they all work together.
*  So the kind of problems our robots solve are kitting, packaging, pilotizing and sorting.
*  And, you know, there will be more such applications.
*  But these are the four things we currently focus on.
*  So these are all manipulating objects.
*  Yes, three and manipulating objects.
*  So it is it is not just picking objects.
*  It is being able to pick and manipulate objects and also assembly.
*  So we also do some assembly tasks which are on the manufacturing line.
*  So all of these, you know, as you mentioned, involve picking up objects, being able to orient them correctly and, you know, putting them in the right place.
*  And sounds very simple.
*  You know, a five year old can do it very easily, but it's an extremely hard problem to do it reliably and at speed required for an assembly line.
*  And what we do is we typically go into a warehouse or an assembly line and look at, OK, this is a line that requires 15 people now.
*  And we basically redesign that line to be a combination of robots and people.
*  And now we basically say, OK, now we can accomplish that same task which is done on that assembly line using six robots and three people or something like that.
*  And so that makes it much more efficient to do the task.
*  It becomes from the warehouse or manufacturing line point of view, their labor supply becomes much more predictable.
*  And that's that's a big, big problem that they have.
*  It's the availability of a predictable labor.
*  Most people, you know, these these kinds of work is quite repetitive.
*  People do not want to do that task. So they come in, they stay for a few days and they leave.
*  And so being able to do those tasks, the availability of labor, which they can turn on and off as they need, that's something they appreciate a lot.
*  And so I would say that's that's the biggest service that we are providing.
*  I know that the the research that you do feeds into the products that you make and vice versa.
*  You know, how much time do you spend? And I know everyone has different roles in the company, but maybe you personally, you know, how much time do you spend thinking and working on the product side and making something practical application wise versus thinking about the larger picture of how the hell to get to AGI?
*  So this this varies. So this depends on what is important to the company at that time point.
*  So I would say in the in the last six, eight months, I've been more than 80 percent on product and no good.
*  No product and sales. So it's not I've been doing enterprise sales in the beginning of this year.
*  So that's that's what I was focused on in the beginning of the year.
*  Then I would say shifted to a mix of sales and product related improvements in the middle of the year.
*  And now I think we are at a point where I can kind of switch back to research for for a few months and then we'll see.
*  So it's a kind of time waiting. And how much time are you spending on the AGI comics these days?
*  Very little. That's when I when I get really angry or frustrated about something.
*  That's great. I mean, that must be a really nice diversion.
*  You know, it just has a very offbeat question.
*  How important is humor to you in all of this and just attacking your world?
*  Because you have a good sense of humor and it shows you do you draw them?
*  These comics you make and you post to Twitter and stuff. Are they hand drawn on like a tablet?
*  Yes, yes. Yeah. Yeah. And so, yeah, you make jokes about recent developments toward AGI and the foibles of the follies of many of our attempts and things of that nature.
*  So those are fun. That must feel good to be a relief as a pressure release or something.
*  Correct. Yeah, I think if we take these things too seriously, if you can't laugh about things, then yeah, it is.
*  There's no point. So, yeah, I think this is also something I learned from Donna Dibinsky.
*  She was the CEO at Numenta. She ran Palm. Basically, she is one of the most fun people I've known.
*  So you can be in a leadership position in a company and even take it IPO and have great success and still have great humor.
*  And even in the leadership meetings there, it used to be fun. So you would crack jokes.
*  You would, of course, have 10 situations, but you would still crack jokes and just be lighthearted about the problems.
*  So I find that to be a very good approach. It's not always like that. There are serious problems often, but still you can laugh at it.
*  I mean, it's also just a nice way to scratch your artistic itch. I mean, I often consider myself half artist anyway.
*  That sounds so ridiculously pompous, but because the scientist is an artist in some sense.
*  And so you are exercising your artistic, your artistry, I suppose.
*  But then creating those comics is a very direct and, I don't know, satisfying, seemingly satisfying.
*  Yeah, I don't know who even reads it. I have fun creating it and my wife enjoys it. And sometimes my kids can also understand it.
*  Yeah, as they get older, they can understand it. Yeah.
*  So going back to like when you guys started Vicarious and you have this long term goal of creating AGI, but you realize you do need to create products along the way.
*  How do you know what the right product is to create? Right. So how do you know?
*  How did you come to the conclusion that these robots, I guess, the robotic arms for now? Right.
*  Yeah. And how did you know that that's that's the right market fit, etc.
*  It's an iterative process. So you have to kind of based on prior knowledge and based on the match to the problem.
*  So, you know, we have considered different problems before robotics was a good fit for AGI or AGI milestone because, you know, we want our AGI.
*  We have a different take on general intelligence compared to many other other groups working on this one.
*  So, for example, we don't believe that you can just scale up a language model and get to AGI.
*  So for us, being able to interact with the world, having, you know, being able to understand the physics of the world, being able to simulate that physics in your mind
*  and recalling those things at the right moment with the right, you know, appropriate prompt.
*  Those are all part of building AGI. I don't know whether I used this example in the in your previous podcast.
*  It's OK. It was two years ago.
*  If it did me out, if that is the case.
*  I always give this example when I talk about why vision is important and perception is important and why sensory motor interactions are important.
*  If I tell you a sentence, John pounded a nail on the wall.
*  And if I then ask you a question, was the nail vertical or horizontal?
*  So this is, you know, this is purely natural language in the in the way the question is posed.
*  But the way humans solve it is by actually imagining that scene.
*  They imagine the scene of John holding a hammer and pounding a nail on the wall.
*  And they read out that answer from that simulation.
*  Right. Of course, you can solve it with a lot of data in that particular setting.
*  But there are so many different variations of this problem that I can ask.
*  And being able to solve that, you need to be able to access the knowledge that you have stored in your perceptual and motor systems and be able to query that with language.
*  So that's the way we think about it.
*  And in that way, robotics felt like a natural fit because of course it is embodied.
*  And you are starting with perception and manipulation as the building blocks and being able to connect from perception to concepts and then finally to language.
*  That's the path that we want to take. And that's the path that we have been pretty much following.
*  And of course, the first part of that, what gets productized there is the basic manipulation ability and basic picking and packing ability without any concept understanding.
*  But as our AGI stack gets more and more sophisticated, then you can think of being able to give an instruction to a robot as simply as, okay, pick up the red objects and put it in the blue box.
*  Or make the assembly like this. Right now we have to program those things.
*  So once robots start understanding concepts, we will be able to tell them those tasks in a more direct way.
*  So that's the path that we want to go on. And so that's why we chose robotics as the domain.
*  Now, which products that you want to build in that domain, that we always find out by talking to customers.
*  In fact, it's a sales team that tells you what products that you need to build.
*  Because they find out from the customers that we don't need drones yet.
*  Right. And what are the specifications of the product?
*  So what are the important pieces? Because you can always build a product that does something very, very well, but does not match the requirements of what is needed in the field.
*  So that feedback loop of the sales team talking to the customers and feeding that into the product team, that is an important thing that you have to establish early on in the company.
*  Is there something, first of all, I want to ask, is it easy for you to tell when someone has a really bad AI startup idea these days?
*  Oh, you know, that's very hard.
*  You must get pitched a lot of ideas like, hey, Dileep, I've got this great idea for an AI startup, you know, right?
*  Yes, people do come and brainstorm about ideas.
*  But it's usually the way people look at it is even if you start with a bad idea, you can change on the way.
*  So usually, you know, when VCs look at startups or pitches, it's not just the idea.
*  It's also the people that they look at. It's a team that they're willing to act on it.
*  And yeah, right. And so there are so many startups that started with the wrong idea.
*  But, you know, based on what they observed, they changed and became phenomenally successful.
*  So there is, yeah, it's OK.
*  It's great if you have the right idea from the very beginning and go about it and you hit success. Great.
*  Happens very, very rarely.
*  Often it happens that you start out on the wrong foot, but you change as you go and you learn with feedback from the world.
*  And it's usually that that grit that VCs are looking for when they look.
*  So it's not just the idea. It's also the team and how people can change and how resilient are they?
*  Those are the kinds of things I would look for.
*  Has there been anything that has sort of surprised you along the way in terms of is it harder than you thought?
*  Is it more fun than you thought running a startup and being involved?
*  Because you just, you know, like I don't like sales, but that's a necessary part.
*  And you just spent 80 percent of your time on, you know, the sales aspect of it.
*  And maybe you love sales. There are people who do, you know.
*  Is there something that is surprising that would be a gem of nugget of information for people?
*  It's definitely harder than I thought.
*  So basically saying if you knew it was this hard, you would never get into it.
*  So in that way, not knowing it was hard was good.
*  So, yeah, so it's definitely way harder than I thought.
*  Running startups is extremely challenging.
*  So there are all kinds of problems that happen every day.
*  And as you grow, there are, you know, of course, you have more resources to handle problems too.
*  But, you know, so it's keeping a level head through that time is sometimes tough.
*  The different roles, I enjoy playing those different roles in some ways.
*  And I have never. So this is something I find.
*  I never complained about work.
*  Whether it is, you know, fixing a bug, you know, way deep down in the assembly code or whether it is writing papers or anything.
*  I've always enjoyed whatever would be the kind of work.
*  So because once you get into the, you know, into the problem, there is something interesting there, you know, some fascinating aspect of the problem.
*  So I never get into this thing of saying, oh, that is beneath me or, you know, why do I need to write production quality code?
*  I will write only MATLAB or those those kinds of things.
*  Each of those problems teach you something.
*  So and I genuinely enjoyed tackling that aspect of that problem that time.
*  So and similarly sales.
*  I really enjoyed working on sales as a problem to tackle.
*  It's a problem to optimize, to figure out how to do it best as well.
*  Exactly. That's a great perspective to have.
*  Still, I wouldn't want 80 percent of my time to put into it.
*  I think. I don't know.
*  So I have a joke there.
*  All the your experience of publishing papers in journals.
*  You know, Tim, so the uncertainty, the arbitrary delays, editors just vanishing, arbitrary review comments.
*  All of this prepare you for a unique job.
*  Enterprise sales. Oh, nice.
*  I believe that. Yeah. Yeah.
*  Interesting. And that's those are unpleasant things, actually, along the way.
*  Many of them are, you know, the publishing. Right.
*  OK, so all right.
*  Let's get back into a little bit of science here by way of vicarious still in robotics.
*  When you give talks, you define intelligence as the ability to model the world and to act on the world.
*  And you make just like you were talking about before about the robots and their capability now versus what they'll need in the future.
*  So there are two questions.
*  Well, and you make this distinction between old brain and new brain and old brain, old brain being this sort of stimulus to response mapper that you play this lovely video of a frog reaching its tongue out to squash flies on an iPhone.
*  And then that's your finger. It bites. Right.
*  Well, not mine.
*  That's not yours. OK.
*  It's some YouTube video. Yeah.
*  Oh, it's a YouTube video. I thought you actually made that anyway.
*  Yeah. And that's an example of old brain kind of mindlessly mapping the stimuli of the flies onto the response, the action of jumping and trying to tongue down the flies.
*  Whereas the new brain you see as more of the cortical, the neocortex and the capabilities that the neocortex brought in with especially with mammals and the expansion in mammals and and now humans because we're the best.
*  And so what you're building here, the goal is to build new brain into these robots.
*  Do first of all, do we know enough about old brain yet?
*  Because old brain is pretty impressive already. Right.
*  Do we know enough about old brain or will learning more about old brain still inform AI?
*  So my take on that is learning about new brain will be easier than learning about old brain.
*  OK. So the reason being the old brain circuits are too clever and each of them can be very highly optimized for each, you know, the particular niche they are in.
*  And it's an amalgamation of all those circuits and reverse engineering.
*  And reverse engineering, those can be really hard because you can, you know, you have to think of it as, you know, somebody somebody very clever wrote a piece of code.
*  And now you have to reverse engineer that.
*  And it is very written close to the metal.
*  Like they are using some esoteric property of the hardware to accomplish a task.
*  And, you know, over millions of years, these have become really intricate circuits.
*  Whereas the new one is more more general purpose.
*  And it's more like Python code if you want to take an analysis.
*  And so it will be easier to and so rather than being idiosyncratic and being tuned to a particular problem, it's more of a general architecture from which you can hope to learn general principles in a much more easier fashion compared to reverse engineering the old brain circuits.
*  So I would say we don't know a lot about the old brain and probably we won't because it is much easier to reverse engineer the neocortex.
*  I mean, does that matter though?
*  Then I mean, essentially we can have these lower level stimulus response mapping functions in AI without learning anything about old brain, perhaps.
*  Correct. Correct.
*  So you can you can train, you know, when you want a particular function, you can, of course, train a deep neural network with lots of data, or you can use combination of deep neural networks and evolutionary algorithms to come up with a circuit for that function.
*  And we don't necessarily need to reverse engineer old brain circuits to accomplish those application specific circuits.
*  Okay, so back to the robots. Right now they're in old brain mode and you you hard code the new brain like features right that that they're implementing.
*  Well, it's it's definitely not in the old brain world in the sense that, you know, we do have a perception system, which is based on, you know, more.
*  So for example, RCN is deployed in the robots. So, so that is more like a new brain. And also the robots plan.
*  They are not they are not just doing reactive motions. They plan.
*  So that that is more like a new brain. But there are, of course, reactive components in their motion, etc. And so I would say it has both old brain and new brain component.
*  Okay, so you so you're building in I mean, I know that this is not a hard line distinction. It's more of a way to sort of conceptualize the different systems and and you consider like deep learning old brain type of process. Right.
*  I mean, that's a story I say, right. Yeah, of course. You have to be very specific or else you'll get in trouble. Right.
*  Correct. I have to I have to be very specific to say it is current deep learning. It is.
*  It is it is the, you know, feed forward neural networks that you have been training.
*  And but once you put more structure into the network, once you have the current connections, once you have feedback, once you start using graphical model concepts like graph neural networks.
*  So then then we are talking about different, you know, so I have to be very, very specific. I have to say it is not deep learning will always be like that.
*  No, that's that would because I don't know exactly where the where the field is going.
*  But many of the current circuits and many of the current ways in which we are applying things definitely look like the old brain system because it is a stimulus response system.
*  We are we are not training world models in deep neural networks. We are training to answer a particular query.
*  We are, you know, we basically give a set of inputs and say here is the target function and we gradient descent on to answer that target function.
*  So in that way, it is definitely very much like old brain.
*  And what we want to do instead is here is a bunch of data, model it, model the world, which is underlying that data.
*  And then we should be able to ask queries, adjust the test time without having to train specifically for that query.
*  And that would be more a new brain like. But we don't we don't do that.
*  That kind of thing much in current deep learning.
*  But but it is trending towards that that thing. But, you know, definitely not the the widely applied models are not like that.
*  They are trained for a particular query. That's good.
*  You have to be really careful or else you'll end up in a long conversation on Twitter where everyone misunderstands each other and is uncharitable to each other's ideas.
*  And it never ends. So, yeah, you have to be very specific.
*  That's right. All right. Let's talk some modeling, some cognitive cognitive maps.
*  So cognitive maps is this is this is the I don't know.
*  It just seems so prevalent these days in it's like the the Holy Grail.
*  It seems to be the Holy Grail right now of figuring out.
*  I don't know. I just see there's a lot of people working on cognitive maps and the navigation story, everything like that within that realm has seemed seems to have exploded.
*  Yeah. Anyway, there's this question of how we form cognitive maps and and the structure of the representations that those cognitive maps use to do things like navigate and plan and form abstractions and concepts and model model the world essentially.
*  So you guys recently released this paper learning cognitive maps as structured graphs for vicarious evaluation.
*  So one issue in forming the representations that a cognitive map can use.
*  And this is a very specific issue that the paper addresses is that you can be in seemingly the same situation, but it calls for a different reaction.
*  So for a terrible example, you know, when I'm younger growing up in what I don't know, high school, something like that.
*  And there's a there's a girl and she got a popular good looking guy comes and talks to her and she thinks, oh, it's really sweet.
*  And then five minutes later, an unpopular and maybe not as good looking guy comes and says the exact same thing to her.
*  And she says, oh, that's creepy. Right.
*  So these are the exact same situation, but she has a different reaction and goes about her business differently.
*  A lovely social example of this idea.
*  And you guys use this never happened to me.
*  So, you know, I wouldn't be.
*  Yeah. Oh, gosh.
*  Am I getting too revealing here?
*  Yeah. I was never either of those guys because I couldn't talk to the girl.
*  You know. Yeah.
*  But anyway, that's a terrible example.
*  And the way that you guys go about solving that kind of problem where you have the same situation perceptually and or socially or whatever, you know, whatever space you're navigating in your cognitive map.
*  But you need to react to them differently.
*  And on the other hand, you can have completely different situations, but you need to they call for the same action to come about.
*  And there is it's a problem to know how or a challenge to know how the brain would implement that solution.
*  Yeah. The idea is a different context call for different reactions.
*  And you guys do this through cloning and merging.
*  And so that's that's what I'll give you the floor now to get it.
*  Yeah. Yeah.
*  So the core problem is how do you learn mental maps from purely sequential experience?
*  So you are you are experiencing the world purely, you know, temporarily.
*  You know, it's it's one instant at a time.
*  Observations come in.
*  But from these observations, you are able to make maps which are 2D, 3D space, some arbitrary space or in conceptual space.
*  And the trouble is that, you know, trouble is exactly what you pointed out.
*  These these observations are aliased or degenerate.
*  The same observations can map to completely different settings.
*  The same input observation can be coming from many different contexts.
*  So how do you take these observations and learn the latent context in that?
*  And what what is the substrate for representing those latent context?
*  And so and then how do you pull out the relevant context when when an observation comes in and how do you handle uncertainty in all these settings?
*  Those are those are the core problems.
*  And that's what we tackle in the paper. Yeah.
*  And what you guys use is a clone structured cognitive graph, a graphical probabilistic model.
*  Is it a graphical probabilistic model or is it a sequence probabilistic model?
*  Both. It is a probabilistic graphical model and it is modeling sequences.
*  So it is it's definitely both.
*  I would say, yeah, so it being a probabilistic graphical model is important in this setting because that's what allows it to one,
*  handle uncertainty in the inputs and also do the planning as a natural property of the model.
*  Like planning is not something you have to think about separately from the model.
*  If you have the model, you can use message passing in that model to plan.
*  So you can, for example, imagine a goal state.
*  You can you want to say, I want to be in that goal state and I am in the current state here.
*  And how do I get to the goal state?
*  You can basically just send messages forward and backward.
*  And the model can then figure out, OK, these are the steps I need to take to go to the goal state.
*  So that is all part of the model.
*  So you don't need to think about planning as a separate thing from the model.
*  So graphical probabilistic models are almost like am I thinking of them because because my familiarity with them is also much less than I'm familiar with, like artificial neural networks.
*  But the way I kind of think of them and please correct me is that every node is so in an artificial neural network, every node is like a quote unquote neuron or unit.
*  Right. And then but every node in a graphical model is stands for a higher level concept.
*  So can almost be thought of as a of a less granular version or almost a little network in itself.
*  And then these networks are connected and represent the probabilities of some assertion or whatever the node stands for being true.
*  How active it is, is a probability for how true that assertion might be.
*  Is that correct?
*  That's correct. So, yeah, so each node, you can think of it as representing a concept and a concept can be as simple as OK, is a pixel being on or is an edge being on.
*  Then the edges between those nodes are representing the relations between these concepts.
*  If a pixel is on here, is a pixel in the neighborhood likely to be on.
*  And similarly, is there a latent higher level feature that explains the, you know, from which these two pixels are generated?
*  So they are they are both generated by a longer line being present.
*  And that line is a higher level feature.
*  So it's a network of concepts like that.
*  And what people might be missing if you're not familiar with probabilistic models is that even though these connections look like the edges look like the ones we draw in a neural network, each edge is bidirectional.
*  So it is not it is not the influence is not just one way.
*  So in a neural network, when we draw the neural network, yeah, the messages propagate or the activations propagate in a unidirectional way.
*  Whereas in a graphical model, the influence is bidirectional.
*  Each edge has a bidirectional influence.
*  So when you when you translate that graphical model to actually be implemented like neurons, then each node will be represented by a set of neurons because there has to be messages going in both directions.
*  And so that's something people who are not familiar with graphical models sometimes miss.
*  And I would say being able to abstract out that relationship between concepts as a knowledge network and then being able to treat inference on that in a coherent way is one of the strengths of graphical models.
*  In neural networks, you are dealing with purely inference all the time.
*  There is no knowledge representation.
*  So I mean, that's is it right to say that something inherent then in the graphical models is that there's more assumptions built in more structure or bias related to cognitive function built in as opposed to the tabula rasa type style of a deep neural network.
*  I would say more it is easier to put in those assumptions in a more rigorous way in the probabilistic graphical model because when you specify the assumptions, you know what you're talking about.
*  It's easy to put that in.
*  In deep neural networks, you are putting in assumptions.
*  You can put in assumptions in deep neural networks in a more indirect way.
*  There will be some structural assumptions you make about the neural network that you put in.
*  So many other things can affect it.
*  So it is not just the things that you put in, the kind of data that you show, then the training dynamics, all of those things can affect what the assumption actually meant.
*  So what you put in thinking that this is what you want to have need not be the reason why the network produces an output.
*  Whereas in graphical models, it's much more controllable.
*  Okay, so let's talk about cloning and merging because the solution that you guys came up with to learning these representations, these cognitive maps and accounting for different contexts and being able to traverse the map differently in different contexts,
*  a solution that you came up with is to essentially clone some nodes, some graphical nodes and or merge them.
*  Maybe you can explain. And I don't know if it'll help because you guys perform about 100 different tasks to show the robustness and the capabilities of these graphical networks.
*  I don't know if it would help to talk about one of some of the tasks or maybe one of your favorite example of what task it performed to talk about how the cloning works.
*  Yeah, yeah. So yeah, I can take a step back.
*  When I used to read hippocampus literature earlier, I used to be very, very confused because there are so many different phenomena and there are so many different cells.
*  There are place cells, there are splitter cells, there are time cells, there are landmark cells, boundary vector cells.
*  There are all these kinds of phenomena recorded in the hippocampus. And once I get into reading that, you realize how wide the field is.
*  So I never used to think too much about hippocampus before. It's a memory system.
*  That was the same way. Yeah, that's ridiculous.
*  Yeah, that's the way I thought. Oh yeah, you can, you know, there's a cortex and it's storing pointers from the cortex and recalling them as needed.
*  That's the way I used to think about hippocampus. And then I happened to read, I think this was around the time of death of Eichenbaum.
*  That's when I started reading some of his papers. And then I found that, oh, the kinds of pictures that he has drawn in the paper, he has some very, very vivid pictures of how a rat would interpret a field of objects.
*  And, you know, those had many similarities with a sequence model that we have been working on. That was, you know, we did not start that model for modeling the hippocampus.
*  Are you talking about the HTM work?
*  Correct. Correct. It was related to the previous sequence model that I had done at Numenta. But we found a different way to learn that. And so that was much more effective.
*  And so when I started reading these hippocampus papers, I started seeing that, okay, these pictures look similar to the concepts that we are playing around with.
*  And then I read one paper that was the killer. This was from Gyuri Buzaki's lab. It put it so emphatically, basically saying that hippocampus is a sequence learner.
*  And it's just sequencing contentless pointers. So it's not, it's ordinal sequencing. There is no, it's just as unrelated things as A and B and C, being able to sequence them, ordinal sequences.
*  And he put it so emphatically in that paper that that's when I started taking this seriously, saying, okay, maybe we should think about this sequence learning idea that we have and see whether that would be a good explanation for the different phenomena that we see in the hippocampus.
*  And then once we started looking at it, then it was pretty interesting. We did many of some experiments that we were not doing before.
*  One example of an experiment is a rat takes a random walk in a room. And the only distinct observations in that room are in the boundary.
*  So at the edges of the room, of course, the rat gets different sensations. Maybe it touches the wall or it sees the boundary of the room. But in the middle of the room, the sensations are exactly the same.
*  You know, it's just seeing blank, blank, blank, blank. And then, and the rat is just walking randomly in this room. There is no, because it doesn't know what the room is.
*  You know, if you place it in the room, it's just walking randomly, it's just getting sensations and the sensations are blank, blank, blank, blank, something blank, blank, blank, blank, something.
*  That's the way it is. And then you feed that sequence into our model and it can learn the actual layout of the room and come up with a graph saying, okay, it actually looks like the room.
*  And it is able to learn that because it is able to take all these different blanks it sees in the middle of the room and put it in different contexts.
*  And all those different blanks are from different contexts because they are at different distances from the boundary.
*  And it is able to automatically figure that out and put that into different contexts in the model. And this is what we call cloning in the model.
*  You know, you take the same sensory observation and copy them into different higher level states.
*  They are all tied to the same observation, but they are differentiated by the context that are flowing into them.
*  And this cloning idea, it turns out, comes from a reasonably well-known compression algorithm, text compression algorithm from the 1980s.
*  And it's called dynamic Markov compression. And it was used in that setting.
*  But then we found a much better way to train that model. That particular model was just using splitting as a way to train the model.
*  But we found a much better way to train that model. And that's what led to the cognitive maps paper.
*  I think this is probably a good place to...
*  Okay, yeah, I think so. So I had, I didn't tell you who I had, a previous guest record themselves asking a question of you, of this particular work.
*  And actually, so it's Brad Love. And he recorded two questions because he's an inquisitive guy.
*  So with your permission, I'd love to just play his, we'll do them one by one, play his questions and then you can address them however you'd like.
*  But maybe like after the question, you can kind of unpack it and then answer it. Sound okay?
*  Yeah, sounds good.
*  All right, here's the first one.
*  Hi, Paul. Hi, Dalit. This is really exciting work. There are analogies here to what's going on in concept learning.
*  For example, Mike Mack finds in his 2016 PNS paper that the same stimuli or percepts give rise to different similarity structures in the hippocampus when different concepts are learned, which seems analogous to the path dependence or notion of context in your work.
*  Working with this analogy, I have some questions.
*  In concept learning, there's not a fixed set of representational units. Instead, the problem dictates the complexity of representation.
*  For example, surprising errors can result in recruiting new representations. Likewise, in Beijing clustering models, there are notions like the Chinese restaurant process, to initially processes, other kinds of infinite mixture models.
*  Instead, you have a fixed number of contexts or clones. Why did you make this choice? Is this a hard limit theoretical commitment like a capacity limit?
*  Or is it an implementational decision?
*  It seems the number of clones should vary depending on the problem. Like a highway would need many clones with everyone going somewhere different, whereas a neighborhood street ending in a cul-de-sac would need very few clones.
*  I see you have a merge redundant clones and again wonder whether this is a theoretical or practical choice.
*  Okay, that's a long question, but you got the gist?
*  Yeah, so the question boils down to, you know, different problems will require different number of clones.
*  I should have prefaced this by saying I had Brad on the show before and we talked about his sustained model of learning concepts via his clustering models of learning concepts in hippocampus.
*  I have read that paper, yes, and I think we do cite them in the paper. So yeah, I definitely learned a lot from that paper.
*  I haven't probably read the paper. The other paper, the P&S paper Brad mentioned, I have to go and read that.
*  But the question stands, so in his clustering methods, you can basically make new clusters at will, right?
*  And so this is in contrast to your cloning method where you have a set number of clones.
*  Yeah, so what we figured out and this is just one version of the algorithms that we published.
*  We have other versions cooking to various levels of maturity.
*  So in all the problems that we dealt with in that paper, you could just over allocate the clones.
*  So you can just allocate the clones to some large capacity and the learning algorithm would figure out the right amount of clones to use.
*  So there was not much harm just over allocating the number of clones and a lot of the capacity will just remain unused
*  because the learning algorithm itself has some regularization in it.
*  So we do have some kind of Dirichlet-like smoothing in the model so that it kind of decides how much of the capacity to use and how much to leave unused.
*  And yes, we want to have future versions of this one to be able to even generate clones as it goes,
*  maybe motivated by the neurogenesis in the hippocampus.
*  And we have played around with that, but none of those were needed for the problems that we tackle in the paper.
*  So we just wanted to add the right amount of bells and whistles to get the basic version of the model out.
*  These other versions are in the works.
*  But what is interesting is that you can just over allocate.
*  And so if you just under allocate, it will still work, but it will be like the model will over generalize if you under allocate the number of clones.
*  But if you over allocate, it doesn't overfit.
*  It still has some regularization built into the learning algorithm that it just leaves the other capacity unused.
*  And we have played with Dirichlet priors to make it much more rigorous in formulation,
*  but we just chose not to put that into this first version of the paper.
*  I mean, you mentioned Yuri Buzaki earlier and having a set number of clones harkens to his notion that basically what we have in the brain anyway
*  is a pre-allocated empty dictionary waiting to be filled and its capacity, essentially, like you just said, will never be used.
*  If you create enough clones or in the brain, if you have enough trajectories, you can store essentially an infinite amount of sequences.
*  And I don't know if you see the similarities there.
*  Yeah, correct. So that's the setting that we want to be in.
*  You over allocate the number of clones.
*  And then when you learn, initially, it might be using all the clones,
*  but then you consolidate it such that now the clones are free for learning something new.
*  And it's almost like it's the pressure of learning something new that forces consolidation on the old clones.
*  So when the new thing comes in, the older learning compresses further and consolidates further.
*  And that's ideally the setting that we want to be in.
*  So we have another version of this algorithm.
*  We had a short paper in CCN where you can rapidly learn the sequences and then compress them as gradually as new sequences come in.
*  So basically in the current paper we are reading, the learning is still batch.
*  We are taking all the sequences and playing them repeatedly to the model.
*  But you can learn incrementally as sequences come in.
*  So that's another version of algorithm that we are working on.
*  And that's the setting that we want to be in.
*  Basically, over allocate the clones and learn incrementally.
*  And it should figure out how to use the clones appropriately as more data comes in.
*  I mean, it does seem to overlap actually with Brad's work on the clustering.
*  They don't seem mutually exclusive.
*  Correct. Correct.
*  In fact, that clustering algorithm should fit.
*  So we explicitly took each observation as an atomic thing.
*  Each observation is atomic and then we are learning sequences of these atomic things.
*  But each observation can have components to it.
*  And that's where the clustering algorithm comes in.
*  So that fits along with our model below that saying,
*  okay, each observation has multiple components to it.
*  And there is a clustering that happening purely in that observation space
*  without using the temporal context.
*  Okay. He has one more question. Are you ready for it?
*  Yes.
*  Okay.
*  The second question concerns how goals and rewards shape representations in your model.
*  Your model seems to effectively compress the trips through the space.
*  In concept learning, rather than a straightforward compression,
*  the assignment of stimuli to categories shapes how all stimuli are represented in the hippocampus.
*  Analogously, reward signals can alter place and grid cell activity.
*  How would these signals enter into your model to shape the learned or inferred representations?
*  Thank you.
*  And I'm really excited for this episode to come out and wish you success with this exciting work.
*  All right. There you go.
*  Yeah. Thank you.
*  This is great that you are getting these questions up front. That is so cool.
*  Oh, yeah. It's kind of fun. I don't know how well it's working out.
*  But I told Brad I thought it'd be fun if he also prerecorded his responses to your responses.
*  And then I tried to pick them out really quickly based on your responses.
*  And that would be just a fun mess.
*  That is cool. Yeah.
*  So in the current model, the reward signals are just treated as sensory signals.
*  We have an experiment based on a real hippocampus experiment where the lab is running laps.
*  And at the end of the fourth lap, it gets a reward.
*  But that reward at the end of the fourth lap in our case is just a different observation.
*  And so in that way, it affects the learning because it's a different observation.
*  So since it is getting a different observation at the end of the fourth lap compared to any other laps,
*  it affects what representation it learns.
*  So it's an indirect, just converting reward to observation kind of thing.
*  We do want to see whether there are more reward related representations, but we haven't tackled that yet.
*  So right now, no, it's just treated just like an observation.
*  And observations affect learning. That's the way it affects learning currently.
*  Well, all right. Thanks, Brad, for the questions. And thanks to Leap for answering them.
*  I appreciate you going back and talking about the inspiration from the hippocampus
*  and how the model is addressing hippocampal function.
*  Do you think it's worthwhile for you to go through just an example of one of the tasks it performs?
*  You were just talking about the lap task, for instance.
*  I just don't want to give short shrift to all of the various different things that it does.
*  So I thought maybe you could pick one of your favorites or something and just describe it.
*  So this is my current favorite. It is not in the paper, but I can still explain it.
*  So, you know, there are all these phenomena which were thought of as space related.
*  So one example is this idea of boundary vector cells.
*  So the experiment, the experiments in the rat is the rats are exposed to a room.
*  They learn in a particular room. And now you in that room, you form their form place fields.
*  So you now take the place field in some corresponding to some location, you know,
*  X equal to two, Y equal to three, something like that.
*  And now enlarge the room, you know, let the let the rats run in an enlarged room.
*  Now you can ask the question, how does the place field of that neuron,
*  which is representing two, three location, two, three.
*  Now, how does that change? All right.
*  Does everything get scaled as you enlarge it or is it adding on to the space?
*  Elongating the room. So think of it as, you know, the room was five by five before.
*  And now the room is five by ten. So it is elongating on one dimension.
*  But there's not like some sort of pattern within the room that gets scaled up or something.
*  No, it's in such that the room is empty in the middle. Right.
*  So it's just, you know, so if it's a uniform carpet, it just gets extended.
*  So the boundaries move further out. Right. That's the experimental setting.
*  So now this and the observation is that the place feels split.
*  So it will it will form two.
*  It will become bimodal and it will now respond highly in two locations.
*  In between those two locations, it will have weak response. So this is the observation.
*  These are so-called splitter cells. I'm sorry to interrupt.
*  Oh, no, this is not a splitter cell. This is the boundary vector cell.
*  OK. And the reason is that this phenomenon explained using boundaries and vector coding.
*  So, you know, you can think of this as, you know, this looks like a purely spatial phenomenon.
*  You have to think about Euclidean space and vectors in the Euclidean space, etc.
*  And what is fascinating is that we can we can explain this without that.
*  We can, you know, it's just take our model, do the pure sequence learning that happens in the model.
*  And, you know, when you learn it in one room with, you know, the walls and the blank middle, it will learn place fields.
*  But now when you expand the room, it will split exactly like what is predicted, you know, what came from the experiments, you know.
*  So it will become bi-model. But now, you know, it is not using any of the space concepts.
*  It's not using, you know, special boundary cells or special vector cells in the model.
*  It is coming naturally out of pure sequence learning.
*  And thinking about space as pure sequence is something that takes a little bit of practice.
*  That's what I realized, because when you think about modeling space, people naturally think about grids,
*  you know, naturally think about a Markov random field with one node associated with each location.
*  That's the way people think about modeling space.
*  But what is counterintuitive is that the space can be modeled purely as sequence.
*  And many of the hippocampal phenomena that we see are arising out of modeling space as a sequence.
*  So examples are, you know, as I said, boundary vector cells.
*  And there are similar examples using landmark vector cells.
*  So when you learn using a set of landmarks and then you move the landmark in the test setting, how does the place field change?
*  You know, that's called the landmark vector cell.
*  But again, in our model, the same thing happens, but it's the same mechanism.
*  No different mechanism needs to be postulated.
*  And then the idea of splitter cells.
*  This is where the rat is not taking a random walk.
*  The rat is moving on, you know, so there is a shared path.
*  Think of like an H maze.
*  The rat starts from one, the left arm of the maze and goes to the left arm and then on the top.
*  And the rat starts from the lower right arm and goes to the top right arm.
*  During that traversal, it is passing through the middle of the H.
*  So wait, so it starts on the left and goes to the right and starts on the right and goes to the left.
*  Sorry, this is a horizontal H, OK?
*  Oh, OK. Yeah, sorry.
*  Sorry.
*  It's an audio podcast.
*  Just draw it for me.
*  Let me repeat that.
*  Let me call it an I maze.
*  So not an H maze, an I maze.
*  OK.
*  So it's a capital letter I.
*  And, you know, so you have the lower limb and the upper limb.
*  And so the rat takes two routes through this maze.
*  So one, it starts from the lower left and goes to the upper left.
*  And then the rat can start from the lower right and go to the upper right.
*  And in these two routes, the midsection is overlapping.
*  So they are getting the same observations when they are passing through the midsection.
*  But it turns out that the rat learns different, you know,
*  so they learn different set of cells in that middle path.
*  And these cells are called the splitter cells because it's the same observation.
*  But the rat responds, you know, depending on where the starting point was.
*  If it started from the left, only some subset of these cells will be active.
*  If it started from the right, only another subset of the cells are active.
*  So those are called the splitter cells.
*  And again, that in our model is just different clones for different contexts
*  because starting from the left or starting from the right are different contexts.
*  Yeah, based on the different sequences that the rat has to.
*  Exactly. Exactly.
*  So it's purely, you know, purely sequence learning explains that.
*  And similarly, a very related phenomena and is very recent work from Chen Sun.
*  He's the first order.
*  So this is with the lab running task where the rat runs four laps.
*  At the end of the fourth lap, there is a reward.
*  And what he's showing is that so he calls it their lab calls this even specific representation.
*  So you can you when you look at the hippocampal responses,
*  you see one set of neurons responding according to which lap it is in.
*  Although all the labs are getting the same observation, you know, lab one.
*  Number one is the same as lab number two.
*  But you see one set of neurons responding to which lap it is in.
*  So you'll see, OK, this set of neurons are highly active in the first lap.
*  Another set of neurons are highly active in the second lap.
*  But you also see that the same set of neurons that were highly active in the first lap are also partially active in the second lap.
*  And similarly, so you see that hippocampal trace and you get the almost identical hippocampal trace out of our model.
*  Because what happens is that when the model runs in this, you know, is exposed to these sequences,
*  it will learn different clones for these different four laps.
*  Although it's the same observation.
*  And then the other clones during inference, the other clones will be partially active.
*  That's a property of the model that the correct clone will be, you know, the strongest active.
*  But the other clones will be partially active because it's a probabilistic model and there is a bit of smoothing in it.
*  And that is the right behavior from the model.
*  So it was fascinating to see that this is the hippocampal recording.
*  When I showed, you know, there are in the company, there are people who do not read neuroscience literature.
*  They see neuroscience literature only through me. They are pure machine learning people.
*  So when I showed that figure from Chen Sun's paper and they're like, this is an actual recording?
*  That was the question.
*  Because we knew that that almost exact same thing will happen in our model.
*  So it was so surprising for them to see that, oh, you can actually record from hippocampus to this level of detail and have traces which almost matches the model.
*  Yeah, that's impressive. That's really awesome.
*  Summing it all up, how do you how would you describe your thoughts on what the hippocampus does?
*  Pure sequence learning.
*  I mean, is that it? Is it pure sequence learning? Is that is that in a nutshell?
*  Yeah, that's I like that simplifying, unifying view that, you know, grid cells, you know, I'll come to grid cells in a while.
*  But if you take the grid cells out of the picture, grid cells are not in hippocampus as I understand grid cells are in MEC or something.
*  I'm not even familiar with all that.
*  The whole anatomy of cortex.
*  Yeah.
*  So if you just look at hippocampus and ignore the grid cells, I think it is pure sequence learning.
*  And I like that simplifying view from Yuri and many others, you know, just makes it easier to deal with.
*  And of course, pure sequence learning, but with the clustering in, you know, the spatial clustering in between so that so that the inputs can be clustered and sequenced.
*  So I would put hippocampus definitely in that and all the sequence learning is, of course, associated with consolidation, planning, all of those things come naturally with that sequence learning.
*  Right. So so all of them will be put in that bucket.
*  Now, grid cells, I think are one hack that brain has figured out to be able to model space where, you know, to tile space from, you know, so based on path integration signals, you can tile space so that even if the observations are blank from the visual system, you can still have something which is from the path integration signal.
*  That's the way I think about grid cells. But of course, these two things interact with each other. Right.
*  So the grid cells influence place cells and place cells influence grid cells.
*  So when you see them working together, you will, of course, see some influence of the place cells on the grid cells, because it's, you know, it's a bidirectional influence.
*  So we do hope to fit grid cells into the picture at some point, but that's not something we are actively working on.
*  Okay, man. So we there's another exciting piece of work that you have that we're not going to have time to go into.
*  But it is basically modeling the cortical microcircuit.
*  The canonical cortical microcircuits using back to your going back to your RCN models that you've been developing.
*  We talked about last time that solved the captures and that I don't know if you that was sort of the media story about what those did, I suppose.
*  Right. Correct. Yeah.
*  And I guess I'm missing a couple of things.
*  So anyway, the paper is called a detailed mathematical theory of thalamic and cortical microcircuits based on inference in a generative vision model.
*  And the generative vision model are the is based on the RCN networks.
*  And so I'm going to have to have you back on the show to talk about the generative vision model.
*  So this is the elusive canonical cortical microcircuit that this is another area where there's a lot of work these days.
*  So this is what what that work is addressing.
*  And we can go deeper on that next time you're back.
*  What are your AI colleagues who don't care about neuroscience?
*  What do they think about you working on the vision model?
*  What are your AI colleagues who don't care about neuroscience?
*  What do they think about you working on having an account of the thalamus and what it's doing versus your neuroscience colleagues?
*  And of course, we care and we think, oh, this is important.
*  But do your AI colleagues think, Dilip, like, what are you doing?
*  Who cares?
*  Well, some of them have started caring because it is fascinating.
*  And so because one of my closest collaborators is Miguel.
*  He's I would say pure machine learning person.
*  He doesn't read the biology papers, but he reads biology papers vicariously through me.
*  And but he's definitely fascinated by it, that you can actually find connections to the brain.
*  And for example, the remark about that hippocampal traces was by him that, oh, wow, this is to this level, you can go into the brain.
*  Because what often machine learning people might miss is that people have done a lot of clever experiments about the brain.
*  And if you go with the go with the right lens to interpret those experiments and, you know,
*  and go with the right attitude to see, can I find reusable principles from all these things?
*  You can. And that's often some lesson that is missed in machine learning, I think.
*  But since we have many of these machine learning people work in close collaboration with people who are on neuroscience and people who are on both sides.
*  Yeah, they can appreciate that a lot more.
*  I want to ask about the importance of learning the neural implementations and the constraints within the brain
*  and how that informs your algorithmic thinking and your computational level thinking and, you know,
*  whether it's important or or do the constraints in the brain really just play a confirmatory role to say,
*  OK, we have all these great algorithms and look, OK, yes, you can do it in brains because you must be able to do it in brains.
*  And this is how you can do it. I confirm that the algorithm can happen in brains.
*  Like what is the in your own thinking process? How do these different levels interact?
*  It's definitely bidirectional. It is not just confirmatory.
*  You know, many of our representational choices in our algorithmic model and the computational model was informed by reading neuroscience literature.
*  And in fact, there were times when we were stuck. OK, this this one seems to be a hard problem.
*  And without some information from neuroscience, there is a large field of models to be explored in on some of those things, for example,
*  how border ownership might be represented in a hierarchy. We were actually stuck for a while.
*  What got us unstuck was reading some papers from Wanderheide,
*  who has studied border ownership responses and proto objects in the in the brain.
*  So for us, at least, you know, maybe we have figured out some mechanism of reading neuroscience papers that look for specific questions.
*  And because of that, it has been very fruitful for us that neuroscience gives very actionable insights into building models.
*  I mean, I mean, obviously you have computational level processes in mind when you're thinking when you're exploring the implementation level type stuff and even algorithms.
*  But but is it fair to say that they're all mutually informative?
*  Yeah, they are. I think of, you know, so we think of these as three corners of a triangle.
*  So there is neurophysiology, neuroanatomy. All of those experiments is one corner of one one corner.
*  And another corner is properties of the real world data, you know, real world benchmarks, all of those things.
*  And the third one is just computational algorithms, you know, things that we know about graphical models, neural networks, properties of algorithms.
*  So all these three pieces are mutual constraints.
*  And the brain is the way it is because of some properties of the world. And those properties can be exploited in our algorithms.
*  So when you can when we go look at the brain for insights, we want to find this triangle.
*  We want to see what are the all three pieces of the puzzle.
*  And that's when we consider that as OK, that is a that is a real insight that we can use.
*  And you know that that that's a promising track of progress then. Is that is that the deal?
*  Yeah. OK. Finally, to leap. And I want to have you on.
*  We'll have you on again before two years. Yes, that would be great.
*  But if you're thinking of someone, you know, imagining someone in a laboratory in a neuroscience laboratory, let's say, or a computer.
*  Any I say neuroscience with the broad swath of natural intelligence laboratories and labs out there.
*  And they're thinking about they either have a great AI startup idea or they're thinking about going into industry
*  and whether they're thinking about starting their own startup or maybe going to work for a startup startup.
*  Do you have any advice for them that maybe you see recurring that you wish people who applied for your company applied for Vicarious you wish they had more of or less of or or something like that?
*  Yeah, I would say definitely get very good at coding and learn to enjoy coding and building things.
*  So that that I would say is definitely a one thing to.
*  And if you are looking to start a company, find a great co-founder, that would be another another advice I can I can give because having a great co-founder can make things a lot smoother.
*  Did you get lucky with Scott Phoenix or was it? Yes. Yes. OK.
*  How do you find what you're saying is get lucky? Right.
*  Yes. Oh, that's general advice for everything.
*  A lot of it is luck. Well, sure. Yeah. Yeah.
*  OK. Well, we are lucky to have graced your presence again, to leap.
*  So thanks for coming on the show again. And we'll talk soon again.
*  So I appreciate it. Thanks for thanks a lot for having me.
*  And I hope I will come back again before two years.
*  Brain Inspired is a production of me and you.
*  I don't do advertisements.
*  You can support the show through Patreon for a trifling amount and get access to the full versions of all the episodes, plus bonus episodes that focus more on the cultural side, but still have science.
*  Go to braininspired.co and find the red Patreon button there.
*  To get in touch with me, email Paul at braininspired.co.
*  The music you hear is by The New Year. Find them at thenewyear.net.
*  Thank you for your support. See you next time.
*  The New Year.
