---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5514s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 17735
Video Rating: None
---

# BI 106 Jacqueline Gottlieb and Robert Wilson: Deep Curiosity
**Brain Inspired:** [May 27, 2021](https://www.youtube.com/watch?v=8vUFM_g8t-4)
*  Curiosity seems like such an exotic topic, right?
*  So it's the new kid on the block in neuroscience and cognitive psychology.
*  But curiosity is everywhere. I mean, animals do not have the luxury of not being curious.
*  You know, when I've worked with people who are very quantitatively gifted before, engineers, mathematicians,
*  they often don't respect the psychology side, the neuroscience side, and see it as sort of soft.
*  But, you know, these are not fields that just sprung up out of nowhere. They're not naive people.
*  They've been thinking hard about these problems for a long time. And I think it's really important to respect all sides.
*  If we were actually successful in making a robot that actually is as intrinsically motivated as people are,
*  I think that could get out of hand.
*  The AI implementation of it can be quite complicated.
*  But the basic idea and the way I like to think about it is making a decision by mental stimulation.
*  This is Brain Inspired.
*  What is curiosity? How do we have it? How do our brains do it? How do we build it in machines?
*  How is it related to intrinsic motivation, to attention, to the fundamental exploration-exploitation trade-off in reinforcement learning?
*  Is this a record number of questions in a row to start a podcast episode?
*  Hey everybody, it's Paul. And on this episode, I've brought together two people from different technical backgrounds,
*  but whose common purpose overlaps, at least in the desire to understand curiosity.
*  Jacqueline Gottlieb runs her lab at Columbia University, where she comes from a more neuroscience-focused background,
*  trying to understand attention and decision-making, recording neural activity during eye movement tasks, among other things.
*  And Robert Wilson runs his neuroscience of reinforcement learning and decision-making lab at the University of Arizona,
*  where he comes from more of a computational background, I'd say.
*  But they both do a little bit of everything and have vast interests, so those descriptions are way too specific and limiting.
*  We focus our discussion today on the young field of curiosity in neuroscience and AI,
*  but we actually spend a good chunk at first talking about curiosity in the pursuit of career goals.
*  That wasn't my intention, but that's the way it went, and I think it's quite useful.
*  So, you know, how to make progress in the face of the enormity of things to learn in this field.
*  Both Bob and Jackie give some great advice for different time points, different eras in your own vocational journey.
*  But then we move on to a host of topics surrounding the study of curiosity,
*  their work doing things like using eye movements to study cognition,
*  how to think about curiosity relative to overlapping topics like attention, like motivation, directed versus random exploration.
*  We talk about Bob's most recent work using the deep exploration algorithm to account for exploration exploitation,
*  which uses a handful of simulations, essentially, to make decisions.
*  And we end up discussing the promise and peril of curiosity in artificial agents.
*  As usual, this really just scratches the surface of their work,
*  which you should learn more about through the show notes at brandinspired.co.uk
*  slash podcast slash one oh six.
*  If you like the podcast, please do consider supporting it with a couple of dollars per month through Patreon and or tell a friend.
*  That helps as well a lot.
*  Sometimes I think I should rename the podcast to something like great people doing great work,
*  because that is the recurring theme and today's episode fits that to a T.
*  I hope you're well out there and fulfilling your own curiosity.
*  Enjoy. I don't usually do this, but stepping back from the specific research that you're doing these days,
*  how would you describe and Jackie will start with you.
*  How would you describe your central interests in?
*  Well, I guess the study of intelligence, I was going to say neuroscience, but it can be broader than that.
*  What would you how do you describe your central interests?
*  So my central interest is in is how mental activity adjust itself to the needs of decision making.
*  Succinct. So I like to think, you know, yeah, does that make sense?
*  Should I say more? I really like how succinct that was, but you can elaborate, but I thought you were done and I was going to let it go.
*  Go ahead. Well, so usually, I mean, so I think that in the traditional way,
*  the tradition that I was raised in and the most dominant way of thinking in neuroscience,
*  I think is what I think of as a bottom up way.
*  So in other words, we have information just exists there instead of injected into our brains by some external process.
*  And we process it. And in many, many cases, we think of even the processing of information is kind of fixed.
*  And animals have like minimal things.
*  You might spend a little longer reaction time or shorter reaction time, but pretty much what you do, that information is pretty fixed.
*  And what we're interested in is what kind of things you prefer.
*  Like we think like, you know, preference. Do you want something sooner? More sooner, less later, whatever, you know, preferences.
*  So right. So we want to understand what you do with the information given your preferences.
*  But it's always seems to me that there's a huge gap in there because what you do, you process the information in a way.
*  And that processing is not fixed, but you adjust it to the situation so you can put more or less effort into something.
*  You can pay more or less attention. You can try to memorize it more or less carefully.
*  You adjust the degree of precision that you take the information in.
*  And people think about those things, but it seems like to be a different universe.
*  They don't usually think that those mental operations are incentivized.
*  So people who are come from the cognitivist tradition, they talk about a lot of representations, a lot of very fancy mental operations, but they never talk about incentives.
*  Is there a cost involved in those operations? Is there a reward?
*  And I thought that those two ways of thinking have to be put together because otherwise you're going to keep not understanding what's happening.
*  Yeah. Bob, what about you? Would you? How would you describe your central interest or plural interests?
*  Yeah. So I think my sort of central, you know, and it's hard to top Jackie's answer.
*  Do it in three words or less.
*  I don't know how succinct it is. Yeah.
*  But I think my central interest is really, you know, this question of can we describe the human mind and the human brain with math, right?
*  And with models. And, you know, to what extent is that possible?
*  And what can we learn from those, from that approach to doing neuroscience, to doing psychology?
*  So that's, you know, enormously broad, right? Pretty much it captures, you know, everything in psychology and cognitive science.
*  You know, so you've got to be more specific than that.
*  And, you know, the area I've really focused in is on decision making and reinforcement learning, which is a place where, you know, historically, you know, and by historically, I mean, the last 20 years or so, there's been a huge amount of progress made in applying these, you know, mathematical models of behavior and of learning and really finding they can shed light on what's going on, not just at the level of behavior, but at the level of the brain.
*  So that's really where my central interest lies.
*  Jackie, do you agree that the application of mathematical models feels as recent? I mean, he used the word historical, but 20 years is pretty recent.
*  Do you agree that it feels as recent as what I'm interpreting Bob's suggestion to be?
*  Well, it certainly feels recent, but nothing is new. I mean, mathematical psychology has been around for a long time.
*  Reinforcement learning behaviorism has always tried to pin things down in equations.
*  I mean, the thing certainly exploded with the artificial intelligence and data science.
*  And it certainly is. I mean, the enterprise itself, the idea itself is not new.
*  But I do agree that even since when I started in my PhD, theoretical neuroscience wasn't a big deal.
*  Yeah. Right. Yeah. And it just became almost everything recently.
*  And sometimes it's I think it's a balance, a good development, but I think sometimes people overdo it.
*  And the point is that just putting an equation on something is an actual understanding.
*  It's not a substitute for critical thinking. Right.
*  And I think that that's a bit overlooked. Doing a well-controlled experiment is still the most important thing.
*  And knowing exactly how you formulate your questions, your hypotheses and your models.
*  And I completely agree. I mean, we have, you know, I wrote this paper a couple of years ago on the ten simple rules for computational modeling.
*  And rule number one was design a good experiment. It wasn't anything to do with the model. So I completely agree.
*  I also agree that it's the roots of this stuff go back.
*  I mean, even to the 19th century, talking about color vision, there was Maxwell and Helmholtz and those folks sort of writing down mathematical equations to understand color vision.
*  I think that really sort of provided incredible understanding. I mean, that they not only wrote down equations to explain it,
*  they had a qualitative explanation of color blindness. And this all came from very careful experiments, but also thinking about it in a mathematical way.
*  You know, and that, you know, followed through. But, you know, I do think in the last, you know, maybe it's 20 years, maybe it's 30 years, there has been a real explosion.
*  You know, as computing power has gotten better and as neuroscientific experiments have gotten better and we can actually measure the correlates of these things, you know, in ways that we couldn't have imagined not that long ago.
*  And I think it's kind of funny right now what it feels like, even though I'm not in your world and in the thick of things, it feels like right now the math, the AI side is like, God, neuroscience, why are you guys so slow?
*  You know, whereas the neuroscience, you know, was built and, you know, back in the day, Jackie's sticking a single electrode down in there recording one neuron and just flashing a light bulb out in the periphery and saying, look, the neuron increases its activity.
*  I mean, it's come a long way since then. So the pendulum goes back and forth, I suppose.
*  All right, guys. Well, I have, we're going to pause here because I elicited two people that you know to have submitted some questions for you.
*  We're going to start off. This one is, and I want you to both to, you know, address the questions. This one was directed toward Bob here. So I want to play the question and then we'll come back and you can answer it.
*  Hi Bob, it's Sav. I hope all's well and the discussion's going well. I know I always come away super energized after our discussions.
*  My question is, as an Explorer, what advice do you give to an undergraduate or graduate student that is trying to make the most out of their time in school?
*  Do you think it's more beneficial to focus on a narrow scope of questions and methods and kind of really go down the rabbit hole or try to expand the scope of questions and learn new skills and new methods?
*  And I guess personally, which approach did you take when you were in grad school? Thanks.
*  Okay, Bob, let's start with you. You know that guy?
*  Yeah, Sav, I know Sav well. He's a student that he was a lab technician or lab manager.
*  Research assistant, yeah, something like that.
*  Yes, at U of A in Anna Ekstrom's lab and we really tried to recruit him for a PhD, but he left us for Princeton. But no hard feelings, Sav.
*  But yeah, that's a really great question.
*  And I think you mentioned undergraduate and graduate in there.
*  And so, you know, I think the answer is slightly different at each level.
*  I think at the undergraduate level, especially, you really want to just have a diverse set of experiences.
*  I think that's huge. I think, you know, taking as many classes as you can, reading as much as you can, trying to get into a lab, I think that's a huge thing nowadays.
*  At U of A, it's part of the psychological science degree program is you have to do up to three semesters in a lab.
*  And I think that is a very big part. But I think at the undergraduate level, just breadth is really important.
*  You know, I will say more and more that coding skills are increasingly important.
*  I mean, even in my time as assistant professor, you know, which is only like five or six years, the number of students applying, coming in with significant coding backgrounds to a psychology program,
*  you know, not to a computer science program, to a psychology program, the graduate level is just exploded.
*  So I do think, you know, the specific skills of coding and, you know, it's probably Python and R nowadays.
*  But really, any language is better than nothing is a big one at the undergraduate level.
*  See, I had an advisor, I'd had two, actually, I did a rotation in graduate school, you know, over 10 years ago, where all the FMRI analysis was done in Excel.
*  And my most recent advisor when I was a postdoc is just a whiz in Excel. And there's no need to learn anything else.
*  You know, Jackie, are you in Excel? Are you guys both in Excel?
*  No, not anymore. I gave it up for best luck.
*  OK, yeah, sorry for the interruption.
*  Yeah, no, that's and I, you know, I myself am sort of old school in that, you know, I'm more MATLAB trained.
*  That's old school now.
*  It is old school now. You know, I mean, it's powerful and it's useful, but it's old school.
*  And I've actually spent part of the pandemic lockdown teaching myself Python with the Pygame plugin, which is a Pygame module, which is, you know, I've been making these little games for my kids.
*  And it's, you know, a really great way to learn the language.
*  So so I do think that that's a big part, especially at the undergraduate level.
*  At the graduate level, I think you do need a mixture of of breadth. You have to have breadth.
*  I think you have to go to your colloquia, you know, go to all of them.
*  Right. Often you have talks that don't seem that relevant.
*  Maybe that, you know, maybe you're a AI person and there's a talk in social psychology.
*  You should go to those talks because there's often overlap that you've not even realized.
*  You know, I remember going to a social psychology talk once where they talked about people feeling free to take risks in certain situations when they when they have the sort of capacity to do that, like the wealth or the time or whatever it was.
*  And they're talking about it in different languages to how we might talk about it in sort of neuro economic world.
*  But it's the same problem.
*  And, you know, often they often people have different insights and they think about a problem in a way that you might never have done because they're thinking about it at a different level.
*  So I do think it's really important to get that breadth.
*  I do think, though, at the graduate student level, you really need to get the depth as well.
*  And you need to come out as an expert in something, whether that's, you know, if you're in my lab, probably computational modeling, neuroimaging, TMS.
*  You know, what some something that you can go to a potential postdoc and you are you become the X, you know, the subject matter expert in that in that thing.
*  The other thing I would say there is it's really important at that level to, you know, when you're writing papers and there's so much pressure now to publish.
*  It's to really focus on the quality of the work and be and make sure that you are proud of what you've done and you're willing to stand by what you've done.
*  You know, I often feel you have you have kind of an internal smell test, or at least I do.
*  And I think most people do.
*  You know, when something's kind of half baked or not right.
*  And I do think you need to listen to that.
*  And really, I honestly believe that there's there's a lot to be said for putting out work that you're proud of may not necessarily be, you know, the sexiest thing in the world or the most citations, but something that you stand by and you will stand by 10 years later.
*  And, you know, that's how I feel about the work that I did as a as a graduate student.
*  You know, certainly my first computational neuroscience paper, I think, has been cited like five times.
*  But I'm proud of that work and it's solid.
*  You know, I stand by the models and, you know, nobody's interested in the parallel hotfield network.
*  Maybe we can, you know, maybe this podcast will change it.
*  But, you know, it was solid work and I'm proud of it.
*  And I think that is that is important, you know, especially in this area of reproducibility, you know, and all this all these crises associated, you know, with psychology.
*  You want to be able to say, I did good work and I'm proud of that work.
*  You know, maybe nobody cites it.
*  Maybe nobody cares about it.
*  But what they're not going to do is come back 10 years down the line and say this was this was rubbish.
*  So the kind of the overall picture I got there was go in undergraduate with a super high explore rate and over time, reduce that, increase your exploitation and reduce your exploration through your academic career.
*  But never stop.
*  Never stop exploring.
*  Never stop.
*  Sometimes you need to go to Florida and just take in some sun.
*  And that's right.
*  Right.
*  It's more the opposite for us.
*  Maybe go to like Colorado or Maine or something.
*  Right.
*  Get out of the sun.
*  That's right.
*  The snow just melted here.
*  But yeah, Jackie, I saw you nodding your head a lot there.
*  Was there anything to disagree with?
*  No, I agree with everything.
*  But so the explore exploit dilemma is terrible in neuroscience.
*  I was thinking in neuroscience, it's an insane field.
*  And I can see this from the students and postdocs that I have in my lab.
*  And I have a very diverse sponge.
*  But, you know, they're just learning.
*  It's like just so much.
*  Everybody did.
*  I mean, there are thousands of papers.
*  Everybody seems to talk a different language.
*  Right.
*  I mean, not to mention that we have from the molecular level to fMRI and recurrent networks.
*  Even so the scales, but then even the ideas.
*  So, you know, one person talks about memory and the other person talks about responsive vigor.
*  And the other person talks about personality traits.
*  And how can anybody learn this?
*  Right.
*  And I found one way.
*  So sometimes, you know, I mean, my students ask me this.
*  We meet once a week for a journal club.
*  We discuss a paper.
*  They're like, oh, my God.
*  And I remember how I was at that at that stage.
*  I thought I was going crazy.
*  And it truly does take I mean, one advice I would have is to read a lot.
*  And this is what I give advice.
*  I mean, I certainly did read a lot at that stage.
*  And after a while, things start to crystallize in your mind, certain structures and ideas.
*  But one thing that I found is really efficient these days.
*  Whenever you encounter a problem or a topic area, look for the models that people have.
*  And not necessarily the itsy bitsy details that sort of the conceptual models, the classes of models.
*  Right.
*  And if you look for the classes of models that are being used, all of a sudden, the field simplifies itself a lot more.
*  Right.
*  So we have reinforcement learning ideas.
*  We have Bayesian models.
*  Yeah, that's pretty much all there is to it.
*  And those have a couple of fundamental ideas to them.
*  And if you grasp those ideas, you will find that all the papers like you could have thousands of papers, but in fact, they just use a single idea.
*  Right. They're just variations on a theme.
*  If you really understand what are the fundamental ideas and assumptions, if you start to see the ideas,
*  in a field, then it becomes also easier for you to read other papers because, you know, you say, oh, you know, last this paper says X.
*  But last week we said why.
*  And even though the paper last week may have seemed very different, in fact, if you understand where it's coming from, you can connect them and then you can start to think critically.
*  OK, so what is this adding?
*  Is this different?
*  Is it the same?
*  Is it novel?
*  Is it not?
*  I have a lot of a lot to ask about this one first just quickly.
*  Is it OK to take as a let's say graduate student, is it OK to take a whole day off out of the lab to read papers per week or something?
*  When I was a graduate student and even a postdoc, I think I was taking weeks.
*  Well, yeah, that's almost a sabbatical.
*  I had I had I had very nice.
*  OK, I must say.
*  But I disappeared from the lab.
*  But I disappeared from the lab.
*  But honestly, I did.
*  I was not goofing off.
*  And I really felt like I needed to read because otherwise I had no idea what I was doing.
*  And I guess on the flip side is that I was designing my own experiments.
*  I was doing my own data analysis independently.
*  So my advisor really put very little effort into my project.
*  I delivered a project from start to finish.
*  And in exchange for that, I didn't have to be in the lab every day.
*  I could set my own schedule.
*  I mean, talk about intrinsic motivation, though.
*  I mean, this goes back to Sebs question.
*  I mean, there's just you know, there are many different axes of types of students, type of types of academics.
*  Right. And it sounds like you like I did this, too.
*  I really took things into my own hands for better and worse.
*  And, you know, I had a lot of help, but a lot was on me to design and collect data.
*  And I thought at the time and I still think that that was one of the most valuable things that could have happened is just throw them in the lab and figure it out, buddy, you know, that kind of thing.
*  Although, you know, you do miss conceptual things that way.
*  Right. Well, so anyway, we don't have to go down that road.
*  But one of the things I was going to mention when you're saying reading a bunch of papers is there's this magical thing that happens.
*  You know, when you're entering a new field, you read a paper, you have no idea what that paper you read it.
*  You read it and paying as much attention as you can to it and you have no idea what it's about.
*  But then you keep going and going and somehow like magically, you know, you wake up, you unconsciously process one night and wake up and all of a sudden, like you're just the ideas that are familiar and actually conceptually are making sense to you.
*  And just through reading sheer tyranny of will, you know, like by keeping going.
*  I don't know if we're fooling ourselves into thinking we're understanding and not understanding, but somehow just continuing to push forward seems to make concepts sink in across different fields.
*  I have found. Yeah, no, yeah.
*  I was just going to say I totally agree with that.
*  I would add, especially in the sort of theoretical mathy side, if you can.
*  And now even more so even inside even in the experimental side as people share data.
*  If you get into the weeds of this stuff and you implement the models that really, really builds the understanding in a deep way.
*  Even if it's only a simple case, you know, not the full thing that they did in the in the paper.
*  If you're just doing a simple case, often that really solidifies understanding in a very deep way.
*  And that's something that that I did as a graduate student messing around with these, you know, hotfield networks or, you know, divisive normalization networks or, you know, change point models in my case.
*  You know, and it really it builds an understanding in a deep way that that, you know, just sort of skimming things doesn't.
*  So I would advocate for that where you can.
*  You know, you have to pick and choose, right? You can't do that with everything.
*  But if it's something that's sort of in your wheelhouse, there's something to be said for just going deep on on some of these some of these things.
*  And especially some of the early stuff. I remember working through one of Sophie Deneves 1999 papers and it's really easy to implement that network.
*  You know, it's it's, you know, in MATLAB, it's like, you know, five lines of code or ten lines of code.
*  And and there it is. You can get the same results or at least an approximation to what she was getting in this nature neuroscience paper.
*  Is it important? First of all, we get it, Bob. You want to keep mentioning hotfield networks.
*  We're going to get you more citations. OK, but is it important to connect the model to actual data?
*  Whereas it what you're what you're saying is that it's important to run the models and you get a lot out of that.
*  It depends. It depends on the you know, on the on the question.
*  You know, I was looking at this particular line attractor neural network and it made a lot of you know, there was no experimental data to look at.
*  I've done other things where I've I've looked at papers.
*  You know, there was one on prevalence induced concept change a couple of years ago that was a really nice paper and they, you know, shared their data online.
*  And you could just take a look at the data set.
*  And, you know, I messed around with the data set for a week and suddenly got, you know, a much broader understanding not only of that effect, but also of sequential effects in in these sort of judgments, these sequential judgment tasks that they were doing.
*  So I really think you can't do that with everything.
*  You have to pick and choose.
*  But but I do think really getting into the weeds sometimes can give you a deep understanding of something.
*  So, Jackie, I think that you might know this person and I know you from me growing up in academia.
*  I knew you as the lateral intra parietal attention monkey neurophysiology person.
*  Yeah, that's what everybody knows.
*  I movement person is what is what I was.
*  And so and this brings us to the question here.
*  Hi, Jackie. It's Yolanda. I have a question about something you recently said, and that is that I movements are different from other movements because they don't interact with the external world.
*  So I actually have two questions.
*  First, how do you think I movements compare to other active sensors like maybe our hands or some sort of antenna and an insect that sends through interaction with the external world?
*  Do you think I movements are just a fundamentally different sensing organ or are there some similarities that can be drawn?
*  And my second question kind of follows.
*  So if one were to build an artificial active sensing system in a robot, our eye movements, a good model to start with, or is it maybe easier or I don't know more promising to start with an interactive sensor that relies on touch or vibration or something like that?
*  Okay, thank you.
*  Oh, yeah, thank you. This is my favorite favorite questions.
*  Yeah, so I think that I movements are they're not that different.
*  They're similar to some active sensors and a bit different from others.
*  And so what? Definitely, I do say that.
*  And rather than I movements don't interact with the external world, I will say that they do not exert force on the external world.
*  They cannot change the external world except through social interactions.
*  That's a huge like if I look at somebody, I can actually make them do something, even if it's an animal, anything that's cognizant.
*  I can make them do something almost as if I was exerting force physical force.
*  But everything else I cannot do anything to to anything external with an eye movement.
*  And so I cannot survive by just making eye movements with the exception of social interactions, because I cannot I cannot grab a piece of food and eat it.
*  I cannot digest it. I cannot do anything. Right.
*  Okay, so so there's I think there's something fundamental here that in order to survive, you need to exert force on the world in some way.
*  And I think that what we think of as decisions, decision making, we talk about those actions that exert exert force in the world in order to obtain a reward in order to obtain any consequence that you want by acting on the world.
*  That's what we call decisions. So now I movements cannot do that.
*  And so you have to wonder then, you know, then why do we make them and how do we decide which I mean, what is the utility function there?
*  If it's not getting us a reward directly, what is the utility function?
*  The utility function is that it changes our internal state by gathering some by sensing something and changing our beliefs.
*  That's the utility. Now, other sensing movements have the same property.
*  So, for example, if you orient your head, you also usually don't exert force unless you, you know, knock a football with your head.
*  Now, if you touch something, I think that hands are a bit more complicated because they're usually you're both exert force and acquire information.
*  So sensation and external effects are hard to disentangle when a rat whiskers.
*  I don't think they're exert a lot of force on it on much.
*  So whisking, I think it's mostly sensing when monkeys move their pinna movements again.
*  They don't exert force on anything. You just change your internal state.
*  So, but I think I movements are particularly beautiful if you're going to look at active sensing because they do not exert force on the world and because they're so precise.
*  So in animals with phobia, you know exactly what the person is looking at and which is something a luxury that you don't have so much like with audition.
*  You don't know the object that's being attended. It's harder to infer and so on.
*  OK, so then you said if you were to build an active sensor.
*  Well, I mean, I think, yeah, if you if if you want some sort of model of an active sensing organ that's purely for active sensing, then I guess vision is a good place to start.
*  But another thing that you really need in order to build any sort of coherent controller of an active sensor, I think you have to have a good grasp of the internal representation of the information.
*  Be it the internal presentation of visual input or the task that is being done.
*  That is really important, and that is a big challenge that we have in the field because, you know, we can.
*  There have been many studies done. For example, you put people in front of look at a work of art or look at a scene and you can observe very precise what they're looking at.
*  But you still don't understand why they're doing that because you don't understand what their internal representation is, what questions they have, what inferences they're making.
*  So anyway, that's a bigger challenge of understanding any active sensor.
*  Bob, do you have what do you think about eye movements?
*  I mean, think thinking about what Jackie just said about internal representations and your work on orbital frontal cortex and and the task space.
*  Do you think in terms of different effectors like eye movements and or reaching and grasping, et cetera?
*  I guess yes, at one level, but no sort of at an experimental level.
*  So we you know, I think it's very much part of that story.
*  You get the information, visual information from eye movements, and I think it's very much part of the representation of the task or the representation of the task is going to be driving where you look at.
*  Right. I think that's, you know, very famous studies of eye movements, right.
*  Going going way back, you know, depending on the task you give.
*  Yeah, exactly. You know, depending on the task you give, they'll look differently at a picture.
*  And so it's very much part of that in terms of other kinds of active sensing.
*  I think Anne Collins has some nice work on this where she's shown that, you know, depending on how you depending on how you have people make a response,
*  you know, different kind of key mappings on the fingers, people will generate different kind of task representations based on that.
*  And I, you know, I don't want to go too much into the details to, you know, otherwise I'm going to embarrass myself not knowing the full details of Anne's work there.
*  But as I recall, like depending how you set it up with the finger movements, you know, you map different bottoms to different responses, you can generate or have people bias people towards certain task representations versus other task representations.
*  So I think it's all very much a part of the space right of the task spaces.
*  How ultimately are you going to register your response?
*  Is it with a button press? Is it with a more effortful run over to somewhere and do something?
*  Is it with a social interaction or verbal response?
*  You know, all of these things are very much part of that space.
*  But I guess we don't look at those too much in detail in the lab right now.
*  Jackie, before we move on to curiosity, I'm kind of curious what your because you've been in the eye movement business for a long time relative to me, I guess.
*  I'm not implying that you're old or anything.
*  But what is your view on the status of eye movements these days in neuroscience writ large and as a window into understanding the brain and decision making?
*  It seems like eye movements were one of the gold standards sort of back when I was coming up in graduate school.
*  Are they are they still or, you know, has the pendulum sort of swung from them?
*  Yeah, they're not enough.
*  I think I think they're not enough.
*  I think that they're not.
*  So I often say this.
*  So I mean, I say this when I go to an eye movement is a GRC conference that goes on every two years in the summer.
*  And, you know, I mean, I do say this, that if we're going to if we in the eye movement field are going to continue the same way, there's no more for us to go.
*  You know, so I can a model research has really has been a beautiful model system.
*  And really, we we trace the pathway from retinal information coming into visual cortex all the way to these eye movement target selection centers and all the way to the brain stem oculomotor muscles.
*  And and what attracted me back then when I was learning this is how precise this was so simple, rigorous.
*  It was because we're talking about the sensory motor transformation and so on.
*  Okay, but but you know, people just focus if you just talk about the sensory motor loop, we figured out a lot of that.
*  And if you just stick in there, then, you know, it becomes claustrophobic because there's nowhere else to go.
*  And we in our field, I think, forgot about that big question is, you know, the decision of where to look.
*  And it's that stage that couples eye movements with all of cognition and decision making.
*  And so we have this at the front of a right on network, the superior colliculus that these neurons kind of magically select targets.
*  We have to ask, how do they know? How do they select targets?
*  And when you ask that, it opens up to the whole brain is pretty much the whole brain.
*  I think it's a major operation of the whole brain to know, decide what to focus on.
*  What is relevant in my world? It's an astoundingly complex question.
*  It has comes in many flavors. And I think that, you know, ninety nine percent of the brain is devoted to answering that question.
*  So, you know, I hope that that will see more and more studies like this that talk about eye movements and decision making that connect eye movements
*  with the kind of economic ideas that are fairly developed.
*  You know, we're still, you know, so I feel because I'm at the intersection of this field, I somehow am frustrated by both sides.
*  Right. So when I talk about which I see as a source of creative tension, I like to be there where I'm never satisfied about anything because that pushes me to do something about it.
*  When I talk about people who talk about decision making, somehow I am frustrated because they're very disembodied.
*  Right. So you write this equation about reducing uncertainty stuff. Right. And you put uncertainty in equation.
*  Well, I mean, what is that? Reducing uncertainty is a mental operation that has some substrates in your brain, some pathways.
*  It's not just some right. And and and and you orient your sensors. Right.
*  That's the immediate motor manifestation of that drive to reduce uncertainty.
*  And many, many, many decisions model don't take into account the actual sensors.
*  And then I look at a system that studies eye movements. So they have a sensor.
*  But then they focus on the low level stuff and they don't ask, well, how does that reduce uncertainty?
*  Right. And, you know, people in the traditional field, if they talk about reward, let me just put this way.
*  Discussion is not very satisfying. You know, because you just throw out these terms as maybe it's motivation, maybe it's vigor.
*  Maybe it's this. Maybe it's that's like, well, you know, actually, you could do better.
*  It can be if you understood the decision theories, you could actually do better.
*  So, yeah, so I think that we have to bring these things together.
*  I think that we should put courses together where people learn both sides of things.
*  And I think that in the absence of courses, because we professors are very lazy and don't like to teach,
*  I think students should just teach themselves both of these literatures and try to connect them.
*  Well, yeah, they could talk about magic. How are they magically going to know that that's what they need to teach themselves?
*  So, Bob, did you have something to add on to what Jackie said?
*  Not really, except I think that that really sort of reiterates this point of being curious and in graduate school and really exploring different fields and being respectful of other fields.
*  You know, I think this is something, you know, I definitely see, you know, when I've worked with people who are very quantitatively gifted before engineers, mathematicians,
*  they often don't respect the psychology side, the neuroscience side and see it as sort of soft.
*  And, you know, maybe even I had that back in the day, you know, when I come from that side.
*  But, you know, I think we really have to respect it because people, you know, these are not fields that just sprung up out of nowhere.
*  They're not naive people. They've been thinking hard about these problems for a long time.
*  And I think it's really important to respect all sides.
*  You know, and I think the kind of thing that Jackie's talking about here about this disconnect between, you know, us on the sort of decision making mathematical side
*  and then the actual motor movements and the eye movements required to implement these kind of things.
*  I think that's a really big thing. And it's important for us to respect that and understand those differences because I think, like Jackie said, you know,
*  at the sort of interface, that tension is where the interesting stuff is.
*  Thinking about that and thinking about, so Jackie said, you know, she's at the kind of has her toes into dipping her toes into well.
*  Drowning, dipping her whole up to her knees or up to her shoulders into two different fields, you know, and you can have the tension.
*  How many is the right amount of fields to go into? And how important is it to devote yourself?
*  How much of your efforts do you devote yourself to? I mean, I guess this kind of goes back to Seth's question, right?
*  But but just in a projecting forward your career, your legacy, etc. is to the magic number to get this tension?
*  Or is it three or is it what's the magic number?
*  I mean, I guess I would focus on the questions that you're interested in and the questions lead you to the fields, right?
*  I mean, I think if you're interested in curiosity or exploration, you have to be interested in neuroscience.
*  You have to be interested in psychology. You know, there's a there's a tradition going back, you know, at least to the 60s there.
*  But you also have to be interested in, you know, the math side of it.
*  There's there's a tradition on that side as well, going back also to the 50s and 60s.
*  The questions that you're interested in really define what you what you should be paying attention to.
*  Plus a little bit of just randomness as well. You know, I think you do want to, you know, I think you need to be as curious as possible.
*  You know, you're not you know, you should go to your department colloquium when they're on, you know, seeming irrelevant topics.
*  You're not going to do a PhD in those topics, but they give you they give you insight and depth.
*  In a way that you don't get when you really specialize, I think.
*  So, Bob, you're suggesting that we should have a little bit of directed exploration and a little bit of exploration.
*  Is that it? I mean, you want to take over the hosting job of the show here?
*  That's right. I'm sorry. I'll stop. I'll stop.
*  So let's talk curiosity. And, you know, like we've been mentioning, it's just a huge topic and it touches on so many other topics.
*  So we'll get to some and we'll leave 90 percent out probably.
*  But, you know, kind of a main goal is an overarching approach to curiosity through attention and through the exploration exploitation theoretically.
*  And hopefully we'll talk about some of the implementation regarding curiosity.
*  But I guess I'll just start off with I'm not going to ask either of you to define curiosity.
*  But how should we think of curiosity and and why are we as animals, as humans curious?
*  What you know, what does it do for us? Jackie, just randomly, I'll ask you the question.
*  Just that fairly easy question.
*  The super easy question. Well, I mean, you can you can bring you know, you bring up through the lens of your work and et cetera.
*  You know, I know it's it's an unfair, under determined question.
*  Yeah, way under determined. Well, I mean, why are we curious?
*  I mean, you know, it's funny that curiosity seems like such an exotic topic.
*  So it's the new kid on the block in neuroscience and cognitive psychology.
*  And indeed, it hasn't been explored so much as a as a topic.
*  But curiosity is everywhere.
*  I mean, animals do not have the luxury of not being curious.
*  We must interact with the world, the things and the world is way, way, way larger than our brains.
*  I mean, the amount of information that's out there is way larger than we can ever process.
*  And so we must constantly decide which information to throw out and which one to not throw out.
*  It's not even right information is there.
*  So it's not data limited.
*  I often like to say, like, you know, everything's in front of you.
*  How the brain works is right in front of you.
*  How behavior works like you're looking at people, you're interacting with people for like ever in your life.
*  All the information is out there.
*  It's just, you know, it takes us, you know, thousands of years to make some sense and put a little theory about the regularity, right?
*  The pattern that we have to discover.
*  Right. OK, so we have to decide all the time and we do this all the time.
*  I think the smallest things like where do I look and what do I study and what experiment do I do right on different scales?
*  Now, a subset of our activities, we actually know what we're doing.
*  So in so this is maybe the simplest form of exploration.
*  When you engage in some sort of known behavior, like we're talking here, we know the script, we know the schema.
*  We know when we should when what to look at, at what time.
*  We know when to listen and when to say something.
*  So so even here we have to do a mini exploration to find out what's going on at this particular time.
*  But it's the most limited form of exploration that we do.
*  But this set of activities, you know, maybe like sometimes if you live in a modern urban society,
*  you might seem like most of what you do is exploiting things.
*  We created these environments that are structured, they're reward rich.
*  We have food in the supermarket. We have safety. We have shelter.
*  We have so much.
*  All this took humanity thousands of years to learn.
*  Right. I mean, we forget how expensive that those environments are.
*  And and even in these environments, we get hit with, you know, something like COVID.
*  Oh, shit. We have no idea.
*  No idea even what to think about what to look at first, what we're to put our resources, how to investigate this toilet paper.
*  Apparently, toilet paper.
*  And and right. And yeah.
*  And even more serious than if it's possible to be even more serious than that.
*  Right. And so explore.
*  So we don't have the luxury to not explore.
*  We have to explore in small ways and in huge ways.
*  What do you think about that, Bob?
*  You know, adding perhaps, you know, why why we why we exercise curiosity as well.
*  Right.
*  It's a huge question, right.
*  It's, you know, why?
*  But but I do think it's, you know, I think Jackie touches on on a lot of it, right.
*  We can't afford not to gain information about the world if we don't have information.
*  We don't learn anything.
*  We can't do anything.
*  And and so I think a key component of of curiosity is that we have to be able to explore.
*  And so I think a key component of of curiosity is, you know, sort of, yes,
*  driving us to learn things and gain information that may be useful down the line.
*  But the flip side of of having curiosity is not having curiosity.
*  So we're equally on curious about lots of things.
*  You know, you can look at a TV screen filled with static and you're not curious about it,
*  despite it having incredible amounts of information.
*  You know, you look at the sort of sort of pure information theory perspective, you know,
*  there's more information there than there is in the in the video of this podcast.
*  So I think being able to be selective about the kinds of information that we want to pay
*  attention to and that we don't want to pay attention to, we do want to learn from and we don't want to learn from.
*  I think that is a critical role for curiosity.
*  You know, and it really comes from the fact that we need information to be able to make good decisions and function and survive.
*  But there's a cost associated with getting that information, either in terms of time or, you know, even a physical cost.
*  Right. If I want to try and find groundwater, I've got to drill a drill a well in the ground and, you know,
*  see if there's anything there. And there's a cost associated with that.
*  This will come up. The cost issue will come up later when we talk about directed versus random as well.
*  But so, Jackie, you mentioned that curiosity is the new kid on the block in neuroscience.
*  And I guess it's kind of new in AI as well.
*  So in reinforcement learning, you know, the explore exploit dilemma is just as old as reinforcement learning, I suppose.
*  And Bob, you've characterized the explore exploit dilemma as any time our desire for information conflicts with our need for reward.
*  I think of reinforcement learning all about rewards as it being all about rewards.
*  And the way that curiosity is talked about in information seeking is in a way that is what's called non-instrumental,
*  where you're making taking actions that don't immediately you can't immediately tie to a reward,
*  but maybe somewhere far down the line or something that you can.
*  I mean, is that a fair comparison to make?
*  What I'm wondering is like how to how to compare or talk about curiosity relative to exploration within the exploration exploitation dichotomy.
*  Is it fair to say that exploration is about rewards being an instrumental way about moving through the world,
*  whereas curiosity is about figuring out what to pay attention to for possible future rewards?
*  Maybe is that a is that a fair characterization?
*  That's a really great question.
*  I think you I think I think you could make that case.
*  And I think that's that's certainly one way to think about it.
*  I guess I my personal view, which is maybe not not published.
*  And but, you know, I tend to think of curiosity is as more of the of the emotion or even the drive.
*  If you want to use that word, I mean, I think that's a loaded term.
*  And exploration is more the act associated with it.
*  So this is, you know, you can be curious about something but never act on it.
*  Right. But if you act on it, then then you're starting to get into exploratory type behaviors or maybe, you know,
*  maybe it's not a single action, but a sort of meta action like becoming more random, for example, or, you know, trying out things you've not tried before.
*  So I tend to make that distinction.
*  I don't know. I don't think that's sort of necessarily broadly, you know, sort of accepted.
*  And I think the drive language is at least was sort of controversial, I think, back in the day, because the drive, you know,
*  the idea that a drive can be satiated, whereas curiosity maybe can't be satiated.
*  Right. And in some in some circumstances.
*  But I do sort of frame it frame it in those terms.
*  So then curiosity is more like intrinsic motivation.
*  Right. Yes. And that in that framing.
*  And I don't know if Jackie agrees with me or not, actually, on that.
*  But yeah, I think it's more sort of this intrinsic motivation.
*  I think you can frame it. I think you could potentially frame both of them.
*  You know, if you want to get abstract and mathematically, you can frame both of them in a sort of reinforcement learning view of Bellman's equation
*  in the idea there that, you know, you're when you're judging actions and how valuable it is to take actions, you want to consider the immediate reward.
*  But you also want to consider the long term reward as well.
*  And in fact, the whole mathematical difficulty associated with explore exploit dilemma comes in that the long term reward.
*  And, you know, it's an extremely complicated, you know, it's just exponentially difficult problem to solve.
*  But, you know, the feeling one one way of framing curiosity is it's really you're curious about something when whatever instincts you have or whatever sort of neural network that's been trained up to sort of identify times at which you might have future value associated with something.
*  That could be one thing that drives curiosity.
*  And, you know, that's one way of sort of putting it into into this.
*  And then exploration is taking that information, values information and making a choice with it.
*  Jackie, I don't know. Just just in case you.
*  Yeah. Yeah. So I was thinking, how would I I mean, I'm not going to disagree, but how could I add to this?
*  I mean, I think I think time has a lot to do with it.
*  And I think I would think of curiosity as, you know, many of our behaviors are like this, I mean, especially for for people who do things on such long time scales.
*  You need little motives on the way to keep you going.
*  Right. I mean, you know, so it's right.
*  It's farce farce for words or right.
*  Or, you know, so, you know, we all when we go to school, we eventually want to grow up and earn money.
*  Right. But there's so much we have to do until we get there.
*  And so we we need we need things to keep our drive going so we don't get tired on the way.
*  Right. So we need motivators on the way.
*  But also we need constraints on the way, because when you enter kindergarten, you might want to make money.
*  You're sure you want you're very driven to make money when you're 25, but you don't know how to get there.
*  Right. You just don't know how to get there.
*  So you need little reward systems on the way to tell you how to get there.
*  You know, that's your mom and dad.
*  And then you go to school and your teacher says, OK, you do this and then you do that and do that.
*  And you're your friends and everybody.
*  So those are little rewards on the way.
*  Now, this is why I do think that curiosity is one of the important importance of that.
*  We start to talk about it is because it gives us an access to these intrinsic motivations that we haven't talked about.
*  It could be, you know, they could be a very different kind.
*  So reducing uncertainty right now, like, OK, I have a present.
*  What is it? What is it? What is it? Right.
*  That's a very feels like a very sharp peak of emotion that could be immediately satisfied.
*  So that's one kind of drive.
*  Another drive might be sort of a slower learning stuff.
*  So, you know, I personally derive deep satisfaction just from the process of learning something.
*  And I'm somebody who whatever they do, I can be very patient and really put in a lot of labor as long as I feel that I'm learning something, however little.
*  And I think I think some people have that to different extents.
*  I mean, this kind of slow learning process is definitely not for everybody.
*  So I think that's kind of a slightly different motivation.
*  And I think there are other motives there.
*  I mean, the motive for control, the motive for effectance.
*  You know, these are things. So when when I'm going to have a little more time for my lab, I'd like to learn this.
*  And again, this is language from social and effective psychology, which doesn't have that many models and not that many equations.
*  But I think it's super important for us to understand what construct they think are solid in there.
*  And so we can start bringing them in and making them more quantitative.
*  So, yeah. So I think this, you know, yeah, I don't really know if curiosity is if that is against drive theory or for drive theory.
*  These are kind of labels. And I don't know.
*  Yeah. But but but the one thing is we have to make this richer.
*  We have to introduce some more concepts about different kinds of utility and motivation.
*  A handful of episodes ago, I talked with Russ Poldrack about cognitive ontologies.
*  And, you know, now I just question everything. Is curiosity a thing or or is it a hundred things?
*  You know, one of the things one of the things that the literature does is make it is distinguish between curiosity as being a reduction in uncertainty,
*  the drive to reduce uncertainty versus anticipatory utility, which, you know, Jackie, you've written about where you're just wanting to feel good.
*  You do something because it makes you feel good and you're curious that way.
*  So is the notion of curiosity just going to dissolve?
*  And of course, Celeste Kidd and Ben Hayden had a piece a few years ago about, hey, we haven't defined curiosity well, but it doesn't matter.
*  We're still moving forward. I mean, is that?
*  It doesn't. But we don't define anything, anything we care about.
*  We don't define it. I mean, define decision making for me, define attention, define exploration.
*  Well, you define attention. You've defined attention.
*  No, I can't. No, I can't. I mean, yes, right.
*  You know, I just, you know, call it something different.
*  But it's more like, you know, how we measure it, how we operationalize it, how it's posing the question and then making our paradigm a little bit richer.
*  Here's here's how you define attention. Attention.
*  This is a quote from one of your. Oh, no, no, no, I don't think so.
*  No, but we have to operationalize things.
*  I mean, it's not like you're setting laying down the law about what attention is.
*  Right. I don't. You want me to read it?
*  I don't have to read it. No, go ahead.
*  Attention refers to the cognitive mechanisms that accompany active sensing behaviors, identify relevant information and link it to learning and actions.
*  So it's just that. Yeah, it's not simple.
*  And you could tear this apart in many ways. But yes.
*  So so so we all agree that there's that. Well, no one answered my question because so the idea.
*  So curiosity itself, just the word. Right.
*  And I don't want to spend too much time on this because the three of us know that it just doesn't matter.
*  But we have to give a label to something.
*  But, you know, mostly from my own head, like, how do I relate curiosity and exploration?
*  And, you know, what does that mean about is curiosity a thing, you know, or is it a label that refers to a bunch of things?
*  And does that matter?
*  So, you know, when I discovered the value of using this term, and it's funny because I wasn't I wasn't going to because I came from attention.
*  Right. And to me, I said, OK, what I'm interested about attention is how do we seek information?
*  Are there sample information? Right. That's it.
*  And I had this paper that I wrote and they had this this headline was information seeking or something in humans.
*  Oh, my God. This paper was I when I must have sent it to like nine journals.
*  I mean, everything from impact factor of everything from nature, human behavior to impact factor of zero point five.
*  I kid you not. We got rejected from a journal and the editor and the impact factor zero point five because nobody has heard of this term information.
*  So after so after we did all this, I said, God damn it.
*  Yeah, I just got, you know, I said, OK, we're going to change the title marketing and we're going to say curiosity in the title.
*  And we tweak the paper a little bit and we send it back to a high profile journal.
*  I won't mention what it was. Oh, that's so interesting.
*  You immediately went out to review. So I'm like, OK, you know, if that's how people understand how people understand each other, it's another topic for coming up.
*  It's another topic for conversation. But sometimes we do need these keywords.
*  And the value of these words is not so much that we can define them, but they somehow trigger the right amount, the right associations.
*  And they put your reader in kind of the right ballpark. So I guess that's good work that works for for people.
*  So never take it too seriously. You think I should title the episode information seeking with Jackie?
*  Oh, definitely not. Definitely not. OK.
*  Neither should you title it eye movements or.
*  Sukad. I do want to make sure we talk about some science here, because this is a lot of fun to me.
*  But maybe we could jump into Bob deep exploration and then this and then we can kind of come back and talk about attention and so on.
*  So the so exploration is now these days, the concept of exploration is kind of divided into two subsets, which are directed exploration versus random exploration.
*  And maybe we before we talk about your model for how we go about using both of these things, kind of maybe would you mind saying just a bit a bit more about the difference between directed and random and why they exist and et cetera?
*  Yes, I always I always use this cheesy example of going to a restaurant when I'm talking about this explorer exploiter.
*  So you sit down at Italian restaurant. Yes, I know it's always it's always the same.
*  You know, so I'm a real exploiter when it comes to this example.
*  I should I should probably branch out a little bit.
*  Well, to your credit, you actually you're you're metacognitive about this.
*  You're you're aware because I think you make fun of yourself and your own paper about always using the same.
*  That's right. Yes, I got to the point that I couldn't sort of an elephant in the room that I always use the same example in like 10 different papers.
*  So I really had to acknowledge it.
*  It was either acknowledge it or explore some more.
*  So I acknowledged it.
*  But but in this example, you sit down at a restaurant, you've got the the menu and you have the choice between the pizza that you always get and something else, some new item that appears on the menu like this ravioli.
*  And then you can think of the decision here is as a sort of utility maximizing decision.
*  I'm trying to pick the thing I'm going to enjoy the most.
*  You know, but I don't want to enjoy just this meal.
*  I might come back to this restaurant again.
*  And so it might be valuable to explore the the unknown ravioli.
*  And so in this context, you can think of directed exploration as being sort of an explicit bias to the unknown option, giving the unknown option a little piece of extra value that, you know, in the sort of Bellman view corresponds to the value of information or the value of the future
*  expected value I can get from that information.
*  And that's an explicit bias to new things.
*  It might not be a strong enough bias to overcome, you know, wanting to have a really great pizza.
*  If the pizza is really great, I'm going to have to have a very big what we call information bonus to get me to explore.
*  And that's one way I can explore.
*  But another way, you know, and, you know, the more I study this, the more I actually do this at restaurants is if I can't decide, just kind of pick randomly, stick your finger in the in the menu at random toss a coin.
*  And on average, that will get you to try new things.
*  Doesn't always sometimes you'll you know, the coin will land heads and you'll do what you always did.
*  But sometimes it lands tails and you try something new.
*  And, you know, this is this these are general approaches that have come from reinforcement learning, but also the sort of mathematics and statistics and operations research fields where they have all kinds of algorithms for solving the explore exploit dilemma.
*  But these two big classes of information seeking and randomization really come up again and again.
*  And a lot of the different algorithms are just different tweaks on those on those things.
*  But for special kinds of situations, you know, they work better in some situations than other situations.
*  So that's the two kinds of exploration that, you know, we think are going on in human behavior.
*  Yeah, as well as, you know, being useful in AI.
*  And so you recently made a model.
*  It's called deep exploration.
*  Speaking of marketing, I mean, I suppose everything deep these days, everything, everything is deep.
*  And we didn't come up with a term so that the term comes from Ian Osband and Ben Van Roy, who really coined it in the AI world.
*  And I saw this talk from Ben Van Roy in RLDM 2015.
*  I think it's still online.
*  And I was just blown away by it.
*  It was really because there were all these questions that I, you know, all these properties that that we'd measured experimentally about directors and random exploration.
*  And he gave a talk where it was pretty clear that they would just drop out of this of this one model of deep exploration.
*  And the AI implementation of it can be quite complicated.
*  But the basic idea and the way I like to think about it is making a decision by mental simulation and not necessarily just one mental simulation, but certainly not many mental simulation, not infinitely many one, two, three mental simulations.
*  And the idea is very much how you might talk through a decision.
*  You know, well, if I get the pizza, that'll be great, but I won't learn anything.
*  So, you know, maybe I won't do that.
*  Right.
*  Or if I get the pasta, well, what if it's good?
*  Then that's great.
*  I get to keep doing that forever.
*  Or what if it's bad?
*  Well, you know, then maybe I that's another mental simulation.
*  Then maybe I'll switch back to the pizza next time.
*  And I only pay that cost once.
*  And it turns out that if, you know, in this sort of simplified settings and this is, you know, I think it's a very, very simple thing.
*  I mean, this is, you know, gets to things that Jackie was talking about with the limitations of, you know, lab experiments.
*  But in the simplified settings, you can you can write down equations for this and you can show that the kind of this algorithm sort of generates directed and random exploration quite naturally.
*  And they have all the properties that we see in the lab.
*  The longer the time horizon that you're considering, so the further out into the future you're considering, the more directed exploration, the more random exploration you should have.
*  And that turns out not to be a trivial property to get the fact that random and directed exploration both depend on uncertainty.
*  That just drops out of this.
*  And then this sort of really almost prediction.
*  I mean, it's based on some work coming as a fiddling, I think, is that the first author of Valentine Wyatt is the is the last author on it, where they did an Explorer exploit task where they just stopped where they gave people in one condition only partial feedback.
*  That's a classic Explorer exploit case.
*  You only get feedback about what you what you choose.
*  And then another case where you give full feedback.
*  So you get to taste the pizza and the pasta, regardless of what you actually choose.
*  And it actually makes some predictions about how directed and well directed goes away completely in that case.
*  But what you see is randomness and you could almost think of it as random exploration actually should have a rise in dependence, even in that partial feedback case.
*  And that actually comes out experimentally, which is was a really nice prediction of that model.
*  So it's it's a model I'm excited about because it does capture everything that we know in sort of one one model, at least everything we know about these simple settings in one model.
*  You know, it's an open question that, you know, what's not been tested about it yet and it's something that we like to do down the line is, you know, the more explicit testing of are we actually using mental simulations to make our decisions?
*  Right. And that's a very specific mechanistic hypothesis about how these decisions are made.
*  And you would like to find neural correlates of those decisions, those simulations, possibly eye movement correlates of those decisions, those simulations.
*  You know, that's not been done yet. And it's a hard thing to do. But that would be something, you know, we'd be excited to try to.
*  We have to be using simulations.
*  There's I experienced simulations myself when I'm laying down at night to sleep.
*  And I think why am I going over and over and over this one idea with just, you know, with minor variation?
*  I mean, we just have to be. There's no that's what replay is.
*  Right. That's yes, exactly.
*  And these these sort of forward sweeps and hippocampus.
*  Right. I think there's there's there's some interesting there's, you know, and here's again is something where where other fields have considered this as well.
*  There's fields that study deliberation and decision making and these sort of slow mental speaking.
*  Right. You know, literally thought processes and think aloud paradigms.
*  Right. And this is something that, you know, certainly in my world, we've kind of ignored completely.
*  And we sort of think more in terms of these hippocampal sweeps and their fast, fast mental simulations.
*  I think that's probably the case for these simple explorer exploit choices.
*  But when you think about, you know, the kind of choice where you're, you know, should I explore this new job opportunity or not?
*  Those aren't decisions that you make in a moment.
*  These are things that you, you know, you talk through by yourself.
*  Right. You talk through with with a trusted friend or an adviser, you know, and you game out different different things.
*  I mean, I was just actually we're just planning out summer vacation trips.
*  And we've just been I've been chatting with my wife, like for long periods of time about, well, what if we do this week here and this week there?
*  Sort of a very explicit mental simulation, trying to come up with the best the best course of action.
*  And that it you know, at the very highest level, it's a mental simulation, just like a forward sweep.
*  But at the lowest level, it's got a feeling that it might be qualitatively different.
*  That's something that, you know, I think is a really interesting avenue for future work is to try to connect these older ideas, more established ideas about deliberation and these more modern ideas about mental simulation, fast replay, these hippocampal processes.
*  You know, maybe someone's doing it. I don't know anyone who's doing it, but but I think it would be a really interesting, you know, area.
*  Well, the meanwhile, while you're discussing and deliberating with your wife, you're making three to four to five saccades, rapid eye movements, you know, per second.
*  And maybe this is a good time to bring Jackie in.
*  Obviously, this is all about.
*  Yeah, you're the eye movement.
*  And if it's not eye movement, it's at least attention.
*  Attention. Yeah. But but I mean, it crossed my mind that this idea of deep deep exploration where you have just a few you run kind of a small number of simulations, but run them out for a long time.
*  And that's where the deep comes from.
*  And, you know, this is being applied to decisions, right.
*  And, you know, for like a reinforcement learning agent, for instance, moving through the world and taking actions.
*  But it actually could be and I'm sorry, I just thought of this off the top of my head.
*  This could be a mechanism for, you know, to determine what to pay attention to.
*  You know, Jackie, I know you're interested in this as well.
*  And how do we figure out what even to pay attention to to make the active sampling with eye movements or what have you?
*  So I don't know what you think about that.
*  And then I wanted your take on this, this idea of, you know, trying to reconcile this sort of approach to reinforcement learning, you know, with the really fast eye movement, sampling the world really fast and while figuring out what what to pay attention to on that time scale.
*  And just your thoughts on those.
*  So I think, OK, I don't know how to put this together with a deep exploration models, but maybe it feels like there's potential there.
*  But I think this is very much a hierarchical process.
*  So we start with a goal, like a broad goal that we like.
*  We want to go on vacation. Right.
*  And I think that that activates some sort of representation.
*  So I really think what I believe options are kind of becoming activated somehow.
*  And then we, you know, a couple of options capture our imagination.
*  I'm going to go to. Rome or I'm going to go to Paris, Rome or Paris.
*  OK, that'll be really cool. Right.
*  Yeah. And that and that focuses your attention.
*  And then and that drives you actually to ask more questions.
*  Oh, Rome or Paris.
*  I really think people like where the exciting stuff happens in our head is when we narrow down to two options.
*  And yes, I really don't think we can make decisions about more than two.
*  I'll just turn it down to two at a time.
*  OK, but Rome and Rome versus Paris.
*  Now, that is a very, very fruitful place to be because now we have maximal uncertainty.
*  It's 50 50. I love Rome and Paris the same way.
*  Oh, my God. Now I need to resolve that uncertainty.
*  How am I going to do it? OK, well, let's see.
*  Is there a different in price that may totally resolve my uncertainty?
*  If Rome is 10 times more expensive than Paris, I'll go to Paris.
*  What's the weather like? Right.
*  Did Paris just got hit by a hurricane?
*  Well, then I might need to go to Rome.
*  Right. Then that gets me to the, you know, so so then I make that decision.
*  OK, I decided I'm going to go to Rome.
*  OK, great. Now, what am I going to do? How am I going to get there?
*  Oh, how am I going to get there? OK, is it Delta or United?
*  OK, again, binary decision.
*  All right. Why am I going to learn about Delta and United?
*  Then we go Google them and see what I'm learning. Right.
*  So so this is how I mean, I think things go.
*  So absolutely. I think that imagination and these mental simulations
*  fuel our curiosity and also provide motivation to keep thinking about it.
*  And that's super important.
*  I don't see how we can make these long term decisions without without that.
*  And so, OK, so here's the thing.
*  So actually, this is a little bit like an experiment we're doing now.
*  So I'm trying to get to the principle.
*  So we say that curiosity and information seeking is an attempt to reduce uncertainty.
*  But before we reduce it, we have to select the source of uncertainty.
*  Right. Even the question is not given to us.
*  Like we have 10 million questions.
*  So the first thing we have to do is choose the question you want to address.
*  Choose your uncertainty.
*  And I think that these and where does this the question where do the questions come from?
*  They come from our mental representations that we reawaken,
*  which is like this imagination and playing scenarios in our heads.
*  But, yeah, so I think these mental simulations are absolutely super important part for attention and for curiosity.
*  Where's the room in eye movement and sampling the world through eye movements?
*  Is there is there a connection there at all to that can be made?
*  Well, I think so. But it's but it's tricky. Right.
*  So because eye movements, you know, first of all, eye movements are going to be driven by visual input.
*  So you've got to put somebody in a dark room and have them think about something.
*  You've got to set up the right conditions to discover this. Right.
*  And I'm sure that it can be done.
*  So first of all, you have to lay things out things out spatially because eye movements tell you by where they are directed.
*  Right. So if you have two alternatives that are organized spatially and you can get people to imagine those alternatives,
*  I kind of bet you that you can discover this.
*  But in many cases, our imagination is non spatial.
*  So it's really not clear what eye movements will tell you.
*  It's not that eye movements are not involved.
*  It's just that you don't know how to interpret them in relation to somebody's internal model because you don't know what that model is.
*  Yeah. Yeah. And I do think there is stuff to mental life beyond eye movements.
*  Say that again. I'm sorry. Beyond eye movements.
*  Beyond eye movements. Yes. Yes. I don't know if I repeat it.
*  No, I just I mean, I became interested in, you know, trying to connect those two things because I'm from the eye movement world, too.
*  And it's just the time scale of I mean, because like you were saying from the very beginning, Jackie, the the eye movement world is still pretty tied into sensory and motor and kind of low level things.
*  And and a broad swath of what we do is way beyond that.
*  I mean, that's what we're all interested in is the the magical cognitive processing happen happening somewhere in our brain and for these longer term things.
*  So I suppose we're coming up on toward the end here and we need to talk a little bit about AI and then I have kind of a closing question as well.
*  So I'm not, you know, gosh, we just never get to everything that I want to get to.
*  But the question does AI need curiosity? Do we want curious AI agents?
*  Yes, I think is the answer.
*  And I think we do. I think there are I mean, you know, he and Osmond is now at DeepMind itself.
*  So and applying deep exploration and I think other algorithms as well to to help train AI faster.
*  Right. I think that's the goal.
*  And people like Pierre Vooday, right, who's done a lot of work with Jackie, has sort of, you know, very much made a well, maybe not his whole career, but certainly a big part of his career is adding curiosity to to learning algorithms and robots and other kind of situations and getting things to learn faster.
*  And I think you're always going to need, you know, sort of good exploration and curiosity whenever you have a situation where data has any kind of cost to it.
*  And you're sort of limited in time in some way.
*  And the world changes, right. If the world is changing, your AI may need to be continually learning.
*  Right. If you're serving up ads on Facebook, right, you want to serve up the ads that people are going to click on.
*  So you want to exploit. But you need to find out if maybe a different ad works better with this kind of person.
*  You know, and you want example is, you know, ads for masks, right?
*  Like, you know, 18 months ago, an ad for a surgical mask is not something I'd have been interested in.
*  But, you know, six months, six months later, you know, it was something I was very interested in.
*  And, you know, you want an algorithm that can pick up on that, but not just that.
*  Right. The other weird stuff that's come out of the pandemic, like people want to know about shirts, but they don't want pants.
*  Right. Like, because they're on Zoom.
*  So, you know, so these these are things that you want.
*  You want your AI to pick up on and you want to pick up on it quickly.
*  And so, yeah, having something that's curious that that is exploring at the right amount, right.
*  If it's if it's learning on the job, you've got to exploit as well.
*  Right. So I think there's a real a real benefit to that.
*  And I think we do want curious. I think there are some cases where, you know, the problem is simple enough.
*  The data are cheap enough that you just throw all the data at the algorithm and you train it and it's done.
*  You know, like cat versus dog, right. Like, you know, pictures of cats, pictures of dogs.
*  I don't think that's a problem that needs, you know, clever exploration.
*  But these much more complicated problems controlling robots, you know, serving up ads in a changing environment.
*  I think that's something where exploration and curiosity really comes into their own.
*  I would say that I'm not somebody who's scared of technology by any means, but actually.
*  Succeeding to make a truly curious robot, I think it's something that could be very scary.
*  If we actually succeeded.
*  Now, luckily, I think we're very far from succeeding to do this.
*  But if we were actually successful in making a robot that actually is as intrinsically motivated as people are, I think that could get out of hand.
*  And so I think about this, this famous phrase from Vladimir Nabokov, who was a Russian writer, his author of Lolita.
*  But he famously said something.
*  He said that curiosity is the purest form of insubordination because a curious agent invents their own goals.
*  They invent their own goals. There's no other way of saying it.
*  Right. If you if you and it's related to this process of recalling your memories, asking a question, finding a source of uncertainty, resolving it, that becomes your goal.
*  Then it then that leads you to some other question, to some other question, some other question.
*  You are autonomous. You do your own thing.
*  So you can see, I think we could maybe lose control of these machines and they're smarter and have a lot more computational power, faster and much bigger memories than we do.
*  The only thing they don't have is autonomy right now.
*  Now, if we give them curiosity, we give them autonomy.
*  I don't know.
*  Yeah, but you're talking about curiosity as as encompassing both what Bob was talking about the drive, but also the actuation, the what Bob was talking about the exploration.
*  Yeah, the physically. Yeah, because there are, you know, like Deepak Pathak has made intrinsically curious RL agents that, you know, they get rewarded for actually making errors.
*  Right. So that's how they their rewards are through the largest prediction errors.
*  And that's how they solve Mario and Super Mario Brothers and other games like that.
*  But that's that's funny that it's curiosity. Curiosity is your your kryptonite regarding when the AI will take over is when they become curious.
*  And by the way, I think they're rewarding things for for errors.
*  I don't think that's going to work because in a big open ended environment, there are actually a lot of nonsense activities one can do.
*  And so they will get trapped in nonsense.
*  But if you have a more powerful algorithm that actually rewards something for finding structure for discovering structure, that is the big prize.
*  And I don't think we know how to make that happen right now.
*  How to define structure. Right. If we ever figure out how to do that, that would be a very powerful thing.
*  Bob, isn't this where directed exploration and simulations come in?
*  It could be right. And I think that's one of the exciting things about things like deep exploration is the basic idea is is mental simulation on top of some structure that you already have or some, you know,
*  that sort of respects your model of the environment. And yes, you know, you can start to simulate.
*  Well, what how would that change my model of the environment if I did something and I got an unexpected outcome?
*  And so I think that is one of the things I'm excited about with deep exploration is potentially it can be applied to these much more complicated problems
*  than the kind of things we've traditionally done in the lab, which are very simplified gambling tests.
*  Last question, guys, and this is just kind of a fun one. So I'm trying a new question here.
*  But and Bob, I guess we'll start with you.
*  What trait do you wish that you had more of as a as a research scientist?
*  And you can say I want to expand my food horizons if you want to go beyond it.
*  No, I'm just kidding. That's a really great question.
*  That's a really great question. Yeah, that one trait that I would improve.
*  Wow. I mean, you know, I'm not sure.
*  I mean, if I had a superpower, it would probably be that I didn't need to sleep.
*  That would be a good one. Yeah. Yeah.
*  But one thing that I think is, you know, it's difficult, I think, for a lot of scientists is just sort of is the social side of it.
*  Being able to network and chat with people at conferences and, you know, and sound intellectual and but interesting and fun.
*  You know, I feel like you can always be better in that.
*  And, you know, I think if I had to pick a, you know, trait that I would, you know, if I could surgically enhance, I think that would probably be the one.
*  Because I do think you get a huge amount out of talking to people.
*  You know, I think you really do. You get you get ideas and you get ideas and you generate ideas that you would never generated on your own.
*  I think there's a lot of that. All right, Jackie, you've had time to think now.
*  What trait do you wish you had more of as a research scientist?
*  I'm perfect.
*  And on that note.
*  I can't wait for the emails.
*  No, I mean, exactly. I think I kind of agree with Bob.
*  I mean, first of all, I'd like this sleeping is really a pain.
*  It takes up a lot of time.
*  But you consolidate, you simulate through the night and you consolidate and make these these new ideas.
*  I just wish it would happen faster.
*  Do you guys ever wake up with a problem solved?
*  I never have gone to bed thinking hard about a problem and wake up, woken up.
*  It feels like it feels like you solved it.
*  But then like 10 minutes later, it's like, oh, no, what, what, what?
*  Then you forget it.
*  I mean, I've definitely I've definitely had sort of like moments of insight at unusual times, never sleeping.
*  But, you know, I remember coming up with the Horizon task walking down a street in Princeton.
*  Yeah, it's cool.
*  And the memory of when when and where stays with you.
*  Yeah, I can tell you exactly where the Horizon task originated from.
*  Like, you know, there's a there's a space I should mark on Google Maps.
*  You know, there's another one I was lying down in bed with my kids trying to get them to sleep.
*  And, you know, I sort of figured out how I was going to approach this other problem, but never like woken up and be like,
*  oh, yeah, that's that's the solution.
*  You know, like Paul McCartney with late yesterday.
*  That's right. Yeah.
*  Yeah, I wish that wasn't a problem, though.
*  That just came to him.
*  And when he didn't go to sleep thinking the problem is to write the best song I can.
*  Although I guess that's always the problem.
*  So, so yours is the same as the just.
*  Yeah, sleep and also so yeah, social.
*  Yeah. So I have it been now I'm more social.
*  When I was younger, I wasn't I really did.
*  When I started my career, when I started my lab, I really didn't get up much.
*  So part of it was just I was overwhelmed.
*  So I had two little kids and I had to run this lab.
*  And I was also very yeah, I'm a bit I have hard time delegating.
*  I think I tend to do stuff by myself and want to do it.
*  And particularly because I really care about the details.
*  And sometimes I think I'm overly obsessive about the details.
*  I feel like I feel like, oh, my God, because sometimes the devil is in the details.
*  There we go. So so I do.
*  Right. We got to it. We dug down.
*  We got to your you got to write more. Yeah.
*  I need to delegate more. I need to delegate more.
*  Yes. Yes. Thank you guys so much.
*  This has been a lot of fun. I appreciate the time spending with me here.
*  Thank you so much. Thank you.
*  I really enjoyed it.
*  Great.
*  The music you hear is by the New Year.
*  Find them at the new year dot net.
*  Thank you for your support. See you next time.
*  Where are you?
