---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4863s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 11487
Video Rating: None
---

# BI 129 Patryk Laurent: Learning from the Real World
**Brain Inspired:** [March 02, 2022](https://www.youtube.com/watch?v=9ZCGL27-I5I)
*  I think GPT-3 or these large language models, they are expensive toys, I think.
*  They're expensive toys.
*  Fun but maybe not of very much use, in my opinion.
*  There's a very rich amount of encoding and representation and processing in a spiking
*  system that's just not used right now.
*  To what extent can AI research or machine learning research inform us about brains?
*  I think it can really help us understand the challenges and the problems brains face.
*  They help us reflect back on ourselves and, well, what can humans or animals actually
*  do?
*  And why is it so hard for these machines to do it?
*  That is super valuable, in my opinion.
*  This is Brain Inspired.
*  Hey everyone, it's Paul.
*  My guest today is a friend of mine, actually, Patrick LaRonde.
*  I met Patrick in graduate school and always admired his broad perspective and his depth
*  of knowledge on a variety of topics.
*  As you'll hear, that depth of knowledge came from a diverse background and his neuroscience
*  graduate school time was just one stop along what has continued to be a diverse career
*  path that he has taken.
*  I thought it would be interesting just to have him on and probe his broad perspective
*  on neuro-AI.
*  As you'll hear, he's worked on just a variety of projects also in industry.
*  This is more kind of a casual conversation, but we do talk about some of the work that
*  he published with his team using deep learning methods with some neuroscience inspiration
*  to help models better generalize in environments that are constantly changing.
*  So this conversation didn't have a specific focus like most episodes do, and I appreciate
*  Patrick being willing to go down that road with me.
*  And we do jump around plenty.
*  But I hope that you take away some helpful insights.
*  I'll link to Patrick's information and the paper that we discuss in the show notes at
*  brandinspired.co.
*  slash podcast slash 129.
*  Thanks for listening.
*  Enjoy.
*  So I've known you Patrick for I don't know if many is the right word, but since graduate
*  school, what was that 50, 60 years ago?
*  Right about that.
*  I, I figure there are two types of graduate students.
*  Those that come in super green like me.
*  And you know, this is their first time learning some of the, you know, the materials and without
*  a necessarily advantageous background.
*  And then I always admired you because you're the other type of graduate student who seems
*  to already have their act together, who seems like this is step number 12 in their trajectory.
*  Right.
*  Because what I, what I didn't appreciate is how much software development and machine
*  learning background that you had coming into graduate school.
*  And of course you were learning new things.
*  How would you summarize your graduate school and your academic experience from graduate
*  school through postdoc?
*  I know that's a large question, but I know that you also, you faced some challenges along
*  the way as well.
*  As well.
*  Sure.
*  Absolutely.
*  Sure.
*  Yes.
*  I, I think, I think I did come in the door with certain ideas because I had a fairly
*  good undergraduate research experience that started kind of in, kind of in my first year,
*  actually.
*  Well, that's when you got into neural networks or when you started really getting, it was
*  actually back in high school, right?
*  Came across it.
*  High school is when I first started reading about them for some, yeah, you're right.
*  And in high school, I first started reading about them for some science fair project type
*  stuff and some hobby projects.
*  But it was only in undergraduate that I joined a lab that was doing spiking neural networks
*  research to understand hippocampal function.
*  And that came with doing a class on machine learning, essentially.
*  We didn't really use that term as much, but it was the theory of neural networks and application
*  of neural networks to certain kinds of problems.
*  So that was the start of my exposure.
*  And then, right, graduate school, yes, I did also learn a lot there.
*  For example, I had not been exposed to reinforcement learning until graduate school.
*  And so that was, that was cool.
*  So learned more methods and techniques did essentially and learned about ways other,
*  brain regions and how thinking more on the brain scale than on a brain region scale.
*  I think that was a big part of my graduate school experience, right?
*  Your development as a scientist.
*  A lot of development as a scientist, for sure.
*  Learning to enjoy the grant writing process, which fortunately I never ended up submitting
*  many grants and getting rejected, right?
*  Therefore I didn't get all the rejection.
*  So in my mind, writing grants is still a positive experience.
*  This one's going to get a lot of funding.
*  Yeah, that's right.
*  Yeah.
*  So I don't know.
*  I think there are definitely challenges with getting your research program going and doing
*  all the networking and socializing of your ideas.
*  There's a whole other part of the science process that I did not recognize at the time.
*  That is important also for your career development.
*  Of course, had awesome chats with people like you and others and stuff, but there's always
*  more you can do there too, other than just designing hypotheses and evaluating them.
*  There's a lot more to science life than just that.
*  So learning that was really good as well.
*  And then you went on after your postdoc to work for multiple companies.
*  So you were able to use...
*  So first of all, you were always into computers, right?
*  So you were an early Mac.
*  What was the early Mac system that you had that you are fond of?
*  I don't even...
*  Commodore 64, is that a word?
*  Yes, that is a thing.
*  Yeah, that's pre-Mac.
*  The Commodore 64 was my entrée, that's right, into that.
*  And then old IBM machines.
*  Yeah, so from a very young age, I started working with computers.
*  But I think that drove me to learn what else was out there.
*  And I think that's how I got into neural networks and machine learning.
*  It's not just about programming, there's other stuff out there.
*  Yeah, I feel like that was cheating.
*  I feel like people like you who were into computers and programming...
*  I'm trying to get my kids a little...
*  There are some games where it teaches you program, the tenets of programming.
*  They're not very fun though.
*  And I don't even enjoy playing them.
*  So when they ask me to play them, sometimes I pass.
*  What was your first job ever?
*  Do you remember?
*  Of course you remember, like making money.
*  I think my first job ever was...
*  I think it was in high school.
*  Well actually, unofficially, I did have an unofficial job, which was my dad's company,
*  my dad's office where he worked.
*  They had a large number of computers.
*  And so I would often go in and either update them or upgrade their operating system.
*  Or if they needed a little repair, I would do things like this.
*  So that was my unofficial job.
*  But my first official job was actually assembling, making working computers out of broken computers.
*  So here's a room full of broken computers.
*  Can you get all the working parts and assemble functioning computers?
*  That's the best functioning computers you could.
*  So that was my first.
*  To highlight the difference in our backgrounds, my first job unofficially was a little lawn mowing company
*  in our neighborhood growing up.
*  But then my first official job, of course, was bagging groceries.
*  A little different.
*  I was assembling the groceries into the bags.
*  Optimizing their fit in the bags.
*  Yeah, I've noticed that that art is lost on grocery baggers these days.
*  But my point is that you have had this diverse background with software development,
*  getting interested in neural networks, going into neuroscience.
*  Since then, working for various diverse companies with all sorts of different projects.
*  Is that diversity something that someone should strive for?
*  Do you think that it...
*  How do you think it benefited you?
*  I think having the diversity of experience...
*  So I have worked in publishing companies, health care companies, robotics companies,
*  home and consumer electronics companies.
*  And then most recently, my work has been split across real estate finance,
*  another publishing company, and education.
*  And I guess those are the main three sectors.
*  So it is a quite diverse sector.
*  I think what I've taken away from that diversity is how important it is
*  to understand or formulate the problem that needs to be solved.
*  It's really, really important to be able to clearly express what is the problem.
*  That's more of an industry skill, isn't it?
*  That trying to solve problems.
*  It could be.
*  I think it's also relevant for academic and research settings
*  because it's more than formulating the hypothesis,
*  it's understanding what is the system or framework in which that hypothesis is being asked.
*  You can always make a hypothesis, but how is that going to inform you about the problem of, say, understanding X?
*  And I guess we'll talk about the problem of understanding what the brain is doing, for example, or what intelligence is.
*  I think consciousness is even one that I probably don't want to get into.
*  But I think formulating what it is you're talking about or what it is you really want to learn, I think is key.
*  Do you think it's hindered you at all?
*  Because some might look at that track record, that trajectory, and think, well, it's too scattered, it's too all over the place.
*  I totally expect that.
*  And that's something I've encountered throughout my career, even as an undergraduate.
*  I did have that cross interdisciplinary major cognitive science that had just been introduced at my university.
*  And my academic advisor would just sort of stare at me across the desk and be like, why are you taking all these different random classes?
*  So I think if you're going to be interdisciplinary and going to be comfortable with jumping between fields,
*  yeah, you'll benefit from it because you'll get a broader outlook.
*  You'll transfer knowledge across these fields and see solutions that others who've been in that field might not see.
*  I definitely have seen that's definitely happened.
*  At the same time, yeah, I'm sure.
*  I mean, there are people who talk to me and they're like, oh, you actually code.
*  You know, for example, you actually write code.
*  And I'm like, I write a code every day.
*  But they can't fathom it because their view of me is quite different based on what they've seen.
*  I see an idea, for example.
*  Yeah. Aside from others opinions of you, do you think that has hindered you in other ways that that maybe you have not been able to go as deep on some things as you'd like and or focus for longer periods on very specific projects?
*  I'm sorry, I'm asking these things.
*  A large part of the brain inspired audience is actually either thinking about going to grad school and or like retired folks or people who've been working their whole lives and are just have been peripherally interested in this and are getting into it more and thinking about how they could get into it more, etc.
*  Yes.
*  Surely being able to focus deeply on a particular subject exclusively has tremendous value.
*  And actually, that was probably the greatest thing about the PhD program is that you had more or less that ability to focus.
*  And so I really do appreciate that.
*  And you can get lots of deep insights by doing that.
*  But I think you can also get insights from that broader outlook and that cross pollination kind of cross field approach.
*  You can get insights from both.
*  That's what I'm saying.
*  And so what is it?
*  There's a T shaped.
*  Oh, yeah.
*  Yeah.
*  Have you heard this term?
*  Right there.
*  They go very deep in one thing.
*  They're an expert in one thing.
*  And then they have like sort of a broader experience.
*  There are I should people who are just really focused experts.
*  Right.
*  And then I think what has happened to me, you know, just, you know, just circumstance by circumstance, I've become a cone shaped person.
*  Right. I've got several deep areas.
*  That's the that's the thing to aspire to.
*  Right.
*  I feel like that that is a goal.
*  Perhaps, perhaps.
*  I mean, I think that depending on your personality to I shaped could be very, very good for a person to have that exclusive focus.
*  And then you become the person that I come to and say, hey, you know, I know, you know about this.
*  You know, can you help me?
*  Right. So having that mixture is one of the greatest things that's the great thing about working at a company with a good a good crew of talent is that there will have both.
*  You'll have a lot of a lot of I shaped people who love nothing better than to focus on something.
*  And then as long as you know where they are and you know that you can find them, you can leverage them and they can help you.
*  And if you're going to be like me, you're going to have to understand the limits of your own capabilities, knowledge, et cetera.
*  Right. And then.
*  But I do appreciate sometimes just digging in and focusing on something intensely.
*  Is there room for illegible scribbled shape people?
*  Because that's what I think. That's what I when I look in the mirror, that's what I see is just a big scribble.
*  You know, one of well, yes, I think so.
*  I'll tell you what I think that role is.
*  OK, I think it's it's this role.
*  There's there's a researcher named Alan Kay, and he he used he calls himself in some cases the agitator, like chief agitator officer or things like that.
*  It's someone who's going to.
*  Inspire people to to do what they what they should know they should be doing right to do better.
*  And I've met several of these throughout my career.
*  Agitators are are are great, right?
*  They they connect distant dots together for you, help you see the bigger picture.
*  I think I think that's a supremely useful role.
*  So that's my my answer for the scribbly.
*  All right. Well, that's that's a very optimistic answer and one that I think I fall short of, but that's OK.
*  So so like I said, so we've been friends.
*  We weren't tied at the hip in graduate school and or after, but we kind of regularly communicate.
*  One of the nice things, I think, about having well in academia, at least.
*  And I don't know if you could speak to this in industry as well, is that you can know someone pretty well and have known them throughout the years.
*  And yet there's an endless supply of things to learn from that person.
*  So there's like I can always go back to the well with you and find out something new, right?
*  Which is a testament to human intelligence.
*  What does intelligence mean to you?
*  I think. One thing that has struck me is.
*  The intelligence and artificial intelligence, more specifically, a lot of people don't like to define that,
*  so I'm curious if people have refused to answer this on your on your podcast or if you've asked others.
*  I mean, it's usually something about being able to adapt in changing environments.
*  And then there's often a generalization component tagged on.
*  I would exactly say it's very good generalization is what I would consider intelligence.
*  But is that just a synonym or is that a definition? Right.
*  So generalization, what does that mean? Right.
*  What's what is that? That's right. That's what I was going to ask you.
*  What does that mean? Yeah. So so I think it means it means flexibility.
*  It's things that look like creativity or novelty.
*  You might be solving the same problem in an in a intelligent way or you may be solving a new problem.
*  It could be an old problem or a new problem, but you might take a novel approach to it. Right.
*  I think I think how do people measure intelligence?
*  Right. They they do things like test your ability to do analogies.
*  Right. I think an analogy is a form of generalization.
*  Right. You're applying some some features or attributes to to a new condition.
*  Abstraction is another way people measure intelligence. Right.
*  I think analogy, abstraction, prediction, inference, all of those things that we do.
*  Intelligence is the ability that underlies that enables us to do those things. Right.
*  So we can indirectly measure intelligence by someone's ability to do those things.
*  Not to say that someone who can't make inferences or can't do analogies isn't intelligent.
*  I don't want to say that. Right. Like you may have never heard of an analogy,
*  but you may have intelligence, which is the ability to do that if you understood what two colons and a dot here would mean. Right.
*  So so I think that's it. I think intelligence is that ability to generalize.
*  And that leads to a whole bunch of capabilities.
*  Can you articulate how your view of intelligence has changed throughout your career and life?
*  Because, you know, you've also worked on robotics and and, you know,
*  because my my own outlook is sort of, you know, constantly shifting.
*  And I don't think I could articulate how I thought about it 10 years ago.
*  I'm not sure if you can. I'm thinking back to early graduate school reinforcement learning work,
*  where I saw the agents I was training that I was working with.
*  They're training themselves or just to get reward.
*  I saw behaviors that looked really intelligent sometimes. Right.
*  Sort of it looked like they had forethought. It looked like they were right.
*  There were there were things that appeared to be intelligent.
*  And what I say, they actually are intelligent, you know, in that in that context with respect to their environment.
*  Yes, they seemed intelligent. Right. OK. There's caveats.
*  They're caveats. Right. So so maybe intelligence is relative to your environment.
*  I think those were fairly simple.
*  I think what I appreciate now is the sheer amount of computational power
*  and architecture that would be required to make something intelligent with respect to the real world.
*  Right. To make something intelligent with respect to the real world will require a lot of compute power.
*  And I did not really appreciate that. I think back then I thought you could just slap the reinforcement learning on a camera,
*  slap that robot onto a camera and it would just work. Right.
*  And I think I'm now realizing that that's there's going to be a lot more to it than that.
*  Well, you've worked on robotics. So is that what gave you the appreciation that it's beyond slapping the reinforcement learning and the camera on a robot?
*  Yes, I would say quite quite directly.
*  So I would say that that basically spending four years after my postdoc in a robotics company gave me a lot of that appreciation and understanding of how hard of a problem it is to really solve well.
*  But so I know that what you have done is taking your neuroscience knowledge from your years in academia and made the case well and incorporated that knowledge into the robotic systems that you guys were building.
*  And that you think that there are principles from the brain that are important. Right. To incorporate.
*  I know, you know, like, for instance, you've worked on spiking neural networks throughout the years, actually.
*  And yet in a conversation you and I have had previously, you know, you've said that we don't need to use everything in the brain and that there are some core principles that you think that are needed to implement.
*  How many how many core principles are there and how do we actually discover those principles?
*  I think under so I think building brains like building robotic brains, things basically devices that allow robots to navigate the world, successfully interact with it, right.
*  You know, perceive and act.
*  Building brains is a great way to discover those principles and sort of in the Feynman sense of what I cannot build, I cannot understand.
*  Right. Just modeling is ultimately what we're talking about here.
*  Once you try to build those things, even the simplest robot that needs to be autonomous, then you start to think back to what was it about brains that seemed to be interesting, right.
*  That that seemed like they would give them the capabilities to do this.
*  Right. And so I could hear echoes of our professors at Pitt, for example, right.
*  In our program saying things like, you know, one said that Cortex is always predicting what's going to happen next.
*  Right. There was this one thing that just echoed in my mind.
*  And you realize that, OK, that that sense of constantly predicting what happens next could be very valuable as a sort of computational driving force force for things to learn good representations.
*  Right. So I think I think you have to be knowledgeable deeply about the neuroscience of what's going on.
*  And so having done that coursework and having been exposed to what brains seem to be doing is helpful, but also facing the problems and challenges and realizing that, you know, how are we going to design a system that's going to understand the world around it?
*  What we we can't use labels.
*  This isn't a supervised learning problem.
*  And to recognize, well, actually using the future as the label for the present, for example, right, or is a great way to drive the system to, you know, if the system is driven to do that and architected appropriately, you know, it could come up with certain things.
*  So I think you have to have both right.
*  You have to have the neuroscience knowledge and the appreciation for what brains are doing.
*  Should we talk about that?
*  So you just mentioned some of the things that went into a paper that you and other co-authors published six years ago now, I suppose, that used a an unsupervised and supervised learning algorithm.
*  Should we talk about that work just to kind of lay it on the table?
*  We could we could do that.
*  Because it's important to be able to.
*  So what you were just talking about, how you need to predict in an unsupervised way, you guys and you can elaborate more on this.
*  You guys built a system that would essentially predict the next time step.
*  And then you made multiple hierarchical layers and then you could track a green basketball and look at stop signs in various lighting conditions with various challenges visually.
*  But it was a visual system.
*  Do I have is that an accurate description?
*  And then, you know, what was I missing there?
*  That's highly accurate.
*  There were situations where we'd see the visual systems of our robots fail on a very regular basis.
*  And we were using sort of state of the art convolutional networks.
*  We were using other computer vision algorithms like using state of the art stuff.
*  But we would despite, you know, tremendous amounts of training or very clever parameter settings from one day to the next, the system might fail to track an object.
*  And that type of failure was obviously disheartening for a lot of people on the team and stuff.
*  And and but coming up with understanding why that was the case was was key.
*  And so under so the fact that, you know, the color of an object, our brains do tremendous amount of things for us.
*  I don't know if you're familiar with Moravec's paradox.
*  There's this paradox.
*  I thought it was Moravec.
*  Moravec.
*  Yeah, more probably.
*  OK, I don't know.
*  But right.
*  The idea is that it's very easy to make computers do very sophisticated things like chess.
*  Right.
*  But we sort of ignore the things like what a one year old or two year old does.
*  Right.
*  Just being able to see an object on a table.
*  Right.
*  Things like this.
*  And those are those are also amazing things, but we just don't think of them as amazing.
*  We just tend to think, oh, that was a green basket.
*  That was a green basketball.
*  We didn't we didn't realize that we're constantly compensating for ambient lighting and colors and shadows and, you know, blurry effects.
*  And so there's always a there's a lot of adaptation going on, even at that perceptual level.
*  Right.
*  A lot of intelligence, you might say, generalization going on even there.
*  And so we try to capture that using three principles from that we thought were brain inspired principles.
*  Right.
*  This predicting the predicting the future, doing this very compressed representation at every part of the system and having massive feedback.
*  Throughout the system, right.
*  Massive to even the input layers.
*  So.
*  But so the architecture that you guys use is similar to multiple other architectures.
*  First of all, you mentioned convolutional neural networks, but at least in the paper, if I remember correctly, you're using kind of simple three layer, multi layer perceptrons.
*  Right.
*  And then, OK, so there's that component.
*  So you're using this quote unquote simple MLP.
*  But then you are and the job of the final layer, the third layer, is to predict the next time step incoming.
*  Right.
*  But then sort of like an element recurrent neural network, you take output from the middle layer, the hidden layer, which is a smaller layer.
*  So it's compressed actually, which is like an auto encoder.
*  But you take that compressed representation and you feed it back to the earlier layers.
*  So then I'm describing one little unit here, and I know it's more complicated than that.
*  But then you had a bunch of units that comprised kind of a layer and you put lateral connections between those units.
*  And then there were hierarchies, hierarchical levels of these little units, and they're all kind of connected together.
*  So there so it's interesting that you use a lot of different similar architectures like a vanilla recurrent neural network, a vanilla multi layer perceptron.
*  And then what's now known is from principles of what is an auto encoder.
*  Yes, I would actually call them the term we use was future encoders.
*  So the right because that was the key aspect that they had to predict the future.
*  They couldn't just re encode what what was happening now.
*  Right. So the so an auto encoders job is to regenerate the original data.
*  Whereas in this case, the job of the MLP was to predict the next time step in an unsupervised fashion.
*  Right. Right.
*  Yes, it's almost like it's almost self supervised.
*  And the the interesting thing, too, is it might almost be called a heterarchy.
*  I mean, yes, there is a certain order.
*  So it is somewhat hierarchical.
*  But because all of them can communicate with each other, right, all of them are trying to use not just their own past to predict what they what they think would be coming next.
*  They also use their neighboring, their neighboring processing units to try to help them predict.
*  So they essentially become sensitive not just to their own input, but distant input, potentially through multiple connections to to better process.
*  And the why this is important is because if you have a scene and you're tracking and you're looking at an object, it can be very valuable to integrate information across the whole scene to interpret, say the color of that object.
*  Right.
*  So, for example, if there's a tree casting a shadow onto the object, you know, that tree may not even be in your field of view, but you might see the shadow kind of coming across the ground towards that and overlapping with that object.
*  The only hope you have of compensating for the shift in color of that object is to be aware of the shadow over there.
*  Right.
*  And that needs to somehow impinge on the processing.
*  So that was the impetus behind the architecture you've described pretty quite accurately.
*  So this is a little nitpicky and haven't studied the paper that much in depth.
*  But the brain is modular to some degree.
*  Right. It's not just mass action, but the all of the units were kind of connected equally.
*  Right. Everyone got the same vote.
*  It's so then you have this almost homogeneous collection of these units and it seems so.
*  So, of course, the brain is highly, highly recurrent at every place.
*  But then some recurrence probably is stronger than others.
*  Some counts more.
*  And I suppose this is what happens when you train that network that you trained, where some connections, of course, become more important than others.
*  But it seems like so many different inputs could actually overwhelm the system.
*  Did you guys face any problems with it's actually too much recurrent information?
*  So I would say that this is a very fair point.
*  I would say that this architecture that we presented is version one version zero point one.
*  Maybe you call it right.
*  And there was a lot.
*  Why isn't it? Why isn't it like a whole brain, man?
*  No, no, no, no. But I think to your point is very fair.
*  There was a little bit of exploration.
*  This I should say this was a one year project.
*  It was a one year project that was funded by DARPA, after which we had to end it.
*  And so, yeah, so we actually had to get outside funding in order to make this project happen,
*  because it was sort of outside of it was getting out of scope for our own company.
*  So questions about how much recurrence and if there was a there should have been a gradient
*  like a neurodevelopmentally set up gradient of recurrence prior.
*  And would that have helped?
*  You know, quite potentially, I think a lot of exploration needs to be done with this type of architecture.
*  I would say, unfortunately, it's very hard to run this type of model implemented in something like
*  TensorFlow or PyTorch, one of the more common because of the style of its recurrent connections.
*  It's quite challenging to implement.
*  Oh, OK. So that might not just not just because you'd have to hand engineer the different
*  architectures and they just they aren't built in as features in the in Python or TensorFlow.
*  Right. It's not just that the libraries don't contain these, although they probably I think it would be a matter of
*  connecting these units all together would be a bit of a challenge.
*  One one other thing I would say is that despite, you know, us not having tremendous amount of time to fine tune
*  or optimize the architecture, the to get to your point of the training would be setting things up.
*  One thing we did notice was that we had this large sort of data set of video, continuous video, and on which it
*  was trained and we were training it and it just kept improving, always improving.
*  So a lot of a lot of deep networks, they they're they're they kind of saturate.
*  You know, they need more data. They're very data hungry in the sense that they just need more data in order to get
*  any improvements. This architecture didn't face that.
*  The longer we trained it, the better it got.
*  It never was, you know, it never hit an asymptote or never asymptotic.
*  Right. It just kept getting better, which was fascinating to me.
*  We would check it overnight. We'd check it the next day.
*  It was trained for weeks and wouldn't that lead to perfection, though?
*  And but it was still making errors.
*  Right. It still wasn't perfect at predicting its own future, but it just kept getting better with the same data set,
*  which was really I'm not even sure what the implications of that are.
*  Right. Right.
*  Just like you and me, we just keep getting better and better.
*  That's what the implication is.
*  Well, I hadn't thought of this, but was that so I guess you started working on that probably in 2014 or 2015 or something.
*  Right. And these days, it's all about unsupervised learning.
*  You know, when you you hear like Jan LeCun talk about the future is is self-supervised slash unsupervised learning.
*  Were you guys ahead of the curve there?
*  Not that unsupervised learning hasn't always been around, but it just hasn't been as popular because supervised learning was
*  such a success for those few years after 2012.
*  Yeah, I mean, I think we were.
*  Yeah, perhaps we were ahead of the curve.
*  I think it was definitely a different path.
*  We were definitely on a different path from from what most people were on to because of the problems we were facing or the problems we chose.
*  The the fact that we chose to recognize the problem as one of not you need more data.
*  Right. That the majority of the field just said, well, you just need more training data.
*  They're still saying that to some extent today, whereas we realized it's not about more data.
*  It's about having a architecture, right.
*  The algorithm that is suited for the problem you're trying to solve.
*  Right. It has to be suitable.
*  You also this kind of switching topics here, but thinking about modern networks and the continued rise of
*  expansion of these deep learning models, et cetera.
*  I know that you have interest in language, at least you did back in graduate school.
*  What are your thoughts on these recent transformers, these language models?
*  That's not something that we talk about much on the podcast.
*  I have a few kind of episodes kind of geared up to talk about them more.
*  But how do you view?
*  How do you view? Well, I mean, there's I know there's a bunch of different language models,
*  but how do you view like the transformer kinds of models?
*  Transformers to me are very interesting.
*  I view them as a formalism formalization, perhaps is the word of what recurrent networks do.
*  But in a way that makes them suitable for GPU acceleration and more precision, right.
*  They're able to go back and instead of hoping that the recurrent system learns to preserve the
*  meaningful information to make the decision at the end, right.
*  Instead of just hoping that that sort of churning process preserves what you need, the transformer
*  architectures makes it more explicit and says, if you if this information is beneficial for your
*  output at this time, you can actually go and use it.
*  You can retrieve it from that moment in your history, right.
*  And so to me, that's a really clever design and in my hands, using them on a few problems,
*  transformers have been very, very successful.
*  They've worked very well.
*  Of course, I'm using much smaller transformers than these big language models and smaller data
*  sets, but they're a very useful tool.
*  So you use them to create a very, very useful tool.
*  So you use the term formalism to describe what was happening with transformers.
*  And that immediately made me think of the word syntax.
*  But are semantics still missing?
*  And I'm really naive about language models these days, but there's always the problem
*  of meaning and semantics, right.
*  So is it all syntax or are there semantics?
*  Is there meaning in there?
*  Right.
*  So I think GPT-3 or these large language models, they are expensive toys, I think.
*  They're expensive toys.
*  Fun, but maybe not of very much use in my opinion.
*  Use for what?
*  Use for for any.
*  So I think people have been interested in using them in various domains, helping them
*  analyze, summarize text, for example, in a way that's very useful.
*  To analyze, summarize text, for example, right.
*  Things like this.
*  Or using them in the context of a customer service system or an education system for
*  kids or things like this.
*  I think that they don't know what they're talking about, right.
*  And that's why you see, you can always cherry pick great looking examples, but you can
*  also see very bad failures of these things.
*  And it's not that hard to get bad failures.
*  Some people make it a hobby to just show how they fail.
*  Aggravators.
*  Yeah.
*  So I think, yes, what is missing is the intelligence, right.
*  The correct good generalization.
*  And probably the way to do it is, so I used to believe that you could learn language by
*  listening to the radio.
*  You could learn a language by listening to the radio, right.
*  That was the old idea that just by looking at strings of language.
*  Taking it in.
*  Yeah.
*  Taking it in, right.
*  You should be able to figure out what it is.
*  And then eventually I realized, you might not be able to do it until you actually.
*  So suppose the language is a stream about a coffee shop, right.
*  About activity in the coffee shop.
*  There's barista, people ordering things, you're getting served things.
*  Maybe you even have the audio of what's happening.
*  Some stirring sounds, some pouring sounds, right.
*  I think actually to the point, I think stirring sounds and pouring sounds
*  or seeing what's going on is what helps you really be sure of the meaning, right.
*  Until you get that real world input that accompanies the language stream.
*  You might always be a bit unsure about what they're really talking about.
*  Well, I thought you were going to go action that you have to speak, you have to generate.
*  Right.
*  I'm not necessarily ready to jump there yet to say that you would have to.
*  But I would think you could sit in the coffee shop.
*  If you sat on the coffee shop, that's much better than just hearing the language stream
*  about what's going on in the coffee shop.
*  You forgot Sarah McLaughlin playing in the background as well.
*  In the background, exactly.
*  If you're in a coffee shop.
*  That's a little outdated.
*  I've seen her perform twice.
*  Oh, live?
*  I didn't know you're a fan of Sarah McLaughlin.
*  Are you a fan?
*  I actually am a fan.
*  Yeah.
*  It's funny.
*  We can edit that out.
*  That's okay.
*  Through my wife.
*  I learned about her through my wife.
*  Oh, I didn't know she was still going.
*  Anyway, there are people like Chris Manning and others who are analyzing the properties of
*  these language models and finding, for lack of a better term, human-like structure.
*  The question is, are they teaching us anything about our own intelligence?
*  This goes back to your model that we talked about also.
*  Using that AI approach, you can answer it for both.
*  Do transformers and modern language models have anything to teach us about our own intelligence?
*  Great question.
*  I think you could certainly, if you have a model that does something and you look inside and you
*  find certain patterns of activation, perhaps I could say it's likely you will find those patterns
*  in the brain as well.
*  Or there's multiple ways to skin a cat, multiple realizability.
*  Right?
*  It's not to say it is the way that this is solved, but it's a way it may be solved.
*  I think the brain does things in a diverse manner of ways.
*  I don't think there are single mechanisms to achieve something.
*  There are probably multiple mechanisms to achieve something.
*  Perhaps you might look at what a transformer is doing and you might say,
*  I found something in Wernicke's area that's similar or some higher language level area that's
*  similar.
*  I think, is that interesting?
*  Perhaps it is.
*  I guess what's perhaps more interesting is understanding where those models fail
*  and where brains succeed and trying to get insight there.
*  Right?
*  Maybe that's all I can say.
*  You can always look in the model and then see, find something in the brain that's like it.
*  I just don't know how helpful that is.
*  Your question of to what extent can AI research or machine learning research inform us about brains,
*  I think it can really help us understand the challenges and the problems brains face.
*  It can make those very clear.
*  I was going to ask you how you thought thus far how AI has most contributed to helping us understand
*  our own intelligence.
*  Is that your answer that the challenges?
*  That would be my answer.
*  That they help us reflect back on ourselves and, wow, what can humans or animals actually do?
*  Why is it so hard for these machines to do it?
*  Right?
*  That is super valuable in my opinion.
*  Let's reverse that.
*  I've had this recurring thought lately and I know it's not an original thought, but
*  when we think of building AGI or human level intelligence, we often, well, I assume that we
*  often mean a system that doesn't make any mistakes and yet humans, we have so many follies,
*  we're so imperfect.
*  How do you think about that?
*  Well, do you agree with that first of all, because the picture of perfection, right,
*  an AI that's perfect, well, now it's human level.
*  Well, no, because humans are way imperfect, right?
*  So can we use our own follies to help inform AI as well?
*  Yes, probably.
*  I think that's really insightful way to think about it because when we think about AI,
*  when one talks about AGI.
*  Not that we need to.
*  I don't know what that means either, but yeah.
*  Let's say human level performance, right?
*  Like or exceeding human level performance, right?
*  You know, is human level performance the goal or is it just human like performance?
*  That's the goal, right?
*  That's one thing.
*  That's one thing.
*  And I'm thinking of these claims of radiology scanning things, right,
*  where they exceed human level performance, right?
*  They see a tumor, well, where a human can't see a tumor.
*  Is that what you're, were they diagnosed better than a human would?
*  Right, right, exactly, exactly.
*  I think that's really impressive.
*  Of course, there are some humans that will probably be able to do that.
*  And there's the term idiote savante.
*  I don't know if there's a more politically correct term for it now.
*  Probably these days, yeah.
*  There must be something, but there are always people who can do things,
*  they're outliers, right, who can do things amazingly well.
*  And I view a lot of these machine learning systems as kind of maybe
*  becoming like those types of outlier people where you've got some.
*  You probably just drop idiot and just, I think we just say savante now.
*  Maybe, I don't know.
*  Yeah, savante would be like a wise person, you know, someone who's.
*  An idiot savante would be a very specialized person.
*  Very special, right, exactly.
*  Okay.
*  But so.
*  We're going to get in trouble for this.
*  Yeah, I know, we'll have to figure out what to do, but okay.
*  But right, so do we do, does human level performance matter?
*  Does exceeding or approaching human level performance matter?
*  Or do we just want human like performance, right?
*  Where, you know, it may not, it may be prone to error,
*  but it still recovers really well, right?
*  You know, like people make mistakes all the time, but they can recover very quickly.
*  So take the self-driving cars and crashing into a police car with sirens or a fire engine, right?
*  Park fire engine with siren lights going on, right?
*  Humans don't crash into those things, right?
*  So who cares about your level of performance?
*  I think the goal is to get something that makes the kinds of errors, perhaps.
*  Or doesn't, or recovers from the kinds of errors in a way that a human might, right?
*  Yeah, but so the car example is a good example, right?
*  Because the whole point of having self-driving cars is that it would not make the same sort of
*  dumb errors that humans make and contribute to fatalities and the danger of driving, right?
*  So is that, is that, is that it?
*  Is that really?
*  Isn't that one reason?
*  What was the, what would be the other reason?
*  Traffic flow?
*  Right.
*  Maybe traffic flow or, you know, you can just gain a bit of a few hours in your day, right?
*  But we would, but, but we would consider it a failure, right?
*  If self-driving cars came along and we had the same fatality rate
*  as before self-driving cars, wouldn't that be a failure of the AI?
*  I don't know.
*  I don't know.
*  And also I think that if the errors were human-like,
*  maybe that would be, you know, if you get to explainability of AI, right?
*  And people understand why things fail, right?
*  Because, you know, if you're crashing into a, into a parked police car or something like this,
*  like, I think that sends sort of shocks of terror throughout people who are looking at this
*  technology, right?
*  Because it's a failure.
*  They can't understand how that failure happened.
*  So in terms of just trusting the system, now,
*  now, I mean, I'm sure plenty of people trust the system now, right?
*  For self-driving, I would not obviously knowing what I know, I wouldn't do it, but,
*  but I don't know.
*  It's totally a good question.
*  I don't know where people sit on their acceptance of that and what they're expecting.
*  A human level performance sounds great, but is that really what we should be looking for?
*  What would you imagine, and I can tell you kind of what I would imagine,
*  like you would, how would you feel or what would you need to see to think something is,
*  oh, that's real AI?
*  Right.
*  Real AI.
*  Yeah, great.
*  Whatever the whatever the fuck that is, but,
*  but so I'll give you mine.
*  And then, well, there are a couple like criteria, I think, for now, and, you know,
*  ask me next week and I'll have a different answer or no answer.
*  One of the things is, so you mentioned autonomy earlier.
*  One of the things about autonomy is that I am autonomous for myself and I,
*  you know, my care for you, Patrick, is limited, right?
*  And is probably on some level related to how much gain you can provide for me.
*  Right.
*  So no offense taken.
*  No offense.
*  Yeah, that's a thing.
*  So I don't care about you, Patrick, right?
*  So AI has to not like real quote unquote, AI has to not care about us, for one thing.
*  And the other criteria that I've recently been thinking of is,
*  I just don't think that we would be able to understand.
*  So here's a thing.
*  It doesn't care about us.
*  It kind of disregards us unless it really needs us, but I don't know why it would need us.
*  And then the other thing is, I don't think we would be able to understand
*  why it was doing whatever it was doing, let alone understand what it was doing.
*  Does that sound ridiculous?
*  It doesn't.
*  It doesn't sound ridiculous.
*  I think one has to consider what is the imperative for that AI system.
*  Yeah.
*  Right.
*  What is its sort of fundamental design or programming, right?
*  Because there are things, I guess, instincts, you might say,
*  or very low level drives that are in all of us, right?
*  And you could imagine that those drives might not exist in an AI system if,
*  say, the resources it needs are super plentiful, for example, right?
*  It doesn't have to worry about getting energy for itself, let's say.
*  So maybe it doesn't have to worry about that.
*  Maybe it doesn't have to have wars over that energy, things like that, right?
*  Say there's solar power.
*  Let's go.
*  Let's go Matrix, right?
*  Okay.
*  San Diego.
*  That's a very San Diego thing to say.
*  Totally San Diego, right?
*  Yes.
*  So this, again, goes to the fact that artificial intelligence systems don't necessarily,
*  they may not necessarily end up being human-like, right?
*  They might become very specialized.
*  It's just, can they generalize, is the question.
*  Well, can I just interject?
*  Because I think that there are kind of two visions, right?
*  So stemming from the question, well, what do you want AI for?
*  And one vision is that we'll have all these very specialized AI robots doing specialized things,
*  but maybe generalize well.
*  And maybe these two things are related.
*  The other vision is that we're going to build AI to be like the most intelligent thing in
*  the universe, us, and that their intelligence, therefore, will resemble the most intelligent
*  thing in the universe, us.
*  And I guess it depends on what you want the AI for.
*  I tend to think that the former is where we should go, right?
*  Where we're going to have a bunch of specialized things serving our needs, of course.
*  And this is, again, not an original thought.
*  Agreed.
*  I think the first one is probably much more realistic and I think less conceited, right?
*  So obviously.
*  But right, imagine agricultural robots where essentially food needs are satisfied, right?
*  I can tell you from working with robots that they are constantly breaking down.
*  So I think an important part of this for me would be that the robots would have to be
*  intelligent enough to repair themselves, which I think would be a huge measure of
*  intelligence and autonomy, right?
*  Not only can it autonomously navigate, but it can autonomously maintain itself or has
*  a symbiotic relationship with other robots that can do the repairs or something, right?
*  Like, so having robots that can construct and repair themselves would be a huge, huge
*  challenge because of the mechanics, quite literally speaking.
*  But that would lead to that autonomous type intelligence.
*  So I think that's probably where we would want to go in terms of robots that can assist
*  us in doing things or saving time or things like that, right?
*  Hopefully without endangering the lives of people, if that could be avoided.
*  Let's switch gears.
*  So I'm always asking, how can the brain better inform AI?
*  And you've been on both sides of the coin, really, on the, I keep referring to it as
*  industry, but I know that your industry experience was closely related to sort of academic pursuits
*  as well.
*  But anyway, what do you see as that's missing in AI?
*  And it doesn't have to be one thing where you think that neuroscientific research could
*  inform AI?
*  I think that there are a lot of sort of theoretical, there's a lot of neuroscience theory, a lot
*  of theoretical neuroscience concepts that could inform AI.
*  There are things that we know about the brain and what the brain does that have yet to be
*  leveraged.
*  Did you have theoretical ideas in mind or?
*  We could take some examples.
*  So just, for example, let's take the first one, which is spiking networks, right?
*  And why does that matter?
*  Right?
*  Why should spiking be important?
*  Because I think we talked about this a bit last time, right?
*  That people claim it's energy efficient or something.
*  And so that's an important reason to adopt it.
*  But I don't know if that's the most interesting thing about spiking or the most relevant thing.
*  And you can always make circuits energy efficient if you need to.
*  If you think about the most neural networks right now, they use vector representations,
*  right?
*  Vectors where each element maybe represents the average firing rate of a neuron or a set
*  of neurons, right?
*  That's the analogy that people have used for decades now.
*  And a vector has a direction and a magnitude.
*  That's it, pretty much, right?
*  You're pointing somewhere and you have a magnitude of how much you're pointing there.
*  So it's very, I think, impoverished compared to what a spiking code could do, a spiking
*  representation does.
*  So by spiking, I guess I would say it's like asynchronous, it's temporal, it has some
*  ordering to it, it has some percentage population activity, right?
*  All of these things, right?
*  So a spiking pattern can be synchronous, it can be asynchronous, it could be in sequence,
*  it could be randomized, it could be play quickly, it could play slowly.
*  It could play slowly and it could ramp up in its activity level, right?
*  It could still be the same population code, but it might ramp up or ramp down and the
*  rate at which it ramps up, percentage-wise could be...
*  So there's a very rich amount of encoding and representation and processing in a spiking
*  system that's just not used right now, right?
*  And all of these different properties I've talked about, I was just thinking in mind,
*  these are all with respect to a particular percept, let's say, right?
*  So I like to think, was this percept surprising or was it anticipated, right?
*  Does it need to engender action immediately or does it need to engender reserved, non-action,
*  does it require orienting to it to find out more or is it just a prediction of a percept,
*  we don't actually see it, right?
*  Spiking codes could very naturally express all these things and if you look at current networks,
*  right, they don't really have...
*  When you look at errors in a perceptual, in a visual network,
*  these adversarial errors or things like that, I think having that spiking representation to encode
*  uncertainty or...
*  Robustness essentially is...
*  Right, right, exactly.
*  So I think one thing that's missing, but there are other concepts, right?
*  Like sleep, the concept of sleep or...
*  I was going to ask you about this because I've been asked about sleep recently too.
*  Sorry that I interrupted you but I guess the most recent thing that I've seen on sleep
*  trying to incorporate principles from sleep into networks is a spiking neural network where they
*  found that if they injected sinusoidal noise that's supposed to mimic sleep,
*  and I don't know how that is actually supposed to mimic sleep, the headlines were all,
*  AI needs sleep too, but then in this thing it's just sinusoidal noise, right?
*  That helped the network generalize.
*  But then of course the idea of replay has been used multiple times and in fact that's what helped
*  the DeepMind DQN algorithm learn the Atari games and now replay is just ubiquitously used.
*  That's something that happens when we're awake and restful as well.
*  But we don't understand the function of sleep well enough, do we, to start
*  taking inspiration from that and building it in?
*  Right, I mean I think this sinusoidal thing sounds really interesting.
*  I'm going to look into it.
*  I'll send you the link.
*  You know, taking it back to the original wake-sleep algorithm, right?
*  Remember from pre-deep learning, basically there was a forward pass where the recognition
*  weights gets trained and then there's a backwards pass, a generative pass, and it trains like that.
*  That has nothing to do with sleep, right?
*  But it was quote-unquote inspired by sleep.
*  So I think that there are just mis- I think there are clever advertisers
*  who might use the term sleep, but I just think we need to understand a lot more about what's
*  happening during sleep before we start claiming that these are sleep-related
*  algorithms that are being used perhaps.
*  I think that's a very fair point.
*  That's a very fair point.
*  I think there are other concepts that are perhaps a bit better understood, like the prediction over
*  time, like you know prediction and mismatch of prediction.
*  That would be, you know, those are more tangible things that could be implemented,
*  as we did in a little bit of that paper.
*  You know, I think it was definitely not just advertisement there.
*  We were like definitely inspired by that pretty strongly, although it's not a spiking network,
*  as you did note, right?
*  Or the fact that there's- perhaps it's more behavioral than anything else, but the fact that
*  you need to take time to perceive or to act, right?
*  Taking certain types of decisions or actions take a bit more time than others.
*  These types of things, you know, aren't really used either, right?
*  Long-term planning for like to graduate college or something like that,
*  when you're in high school, something like that, right?
*  You know you have to take 50 million steps to get there,
*  but you don't encode all the steps.
*  Is that what you're alluding to?
*  Perhaps, or maybe even shorter term than that, right?
*  Certain even perceptual decisions take a bit of time to answer, right?
*  Whereas a lot of these systems, we show them an image or a frame and we expect them to
*  answer fairly immediately, right?
*  You don't have to do that, right?
*  You can actually run networks so they accumulate information over time and then periodically do
*  an output.
*  You just don't do that very often, right?
*  We tend to...
*  So reframing problems to be less about image perception and more about
*  perceiving things in video and continuous video streams, right?
*  Might make a big difference, but since that's kind of what we do, right?
*  And so it'd be interesting to see if that improves things.
*  I've also wondered a lot about, you know, the fact that we make saccades all over the
*  place when scanning a scene and, you know, as opposed to just taking in the whole image.
*  And, you know, could there be some benefits of that for perception?
*  You know, not to say that we need to mimic humans or animals, right?
*  We don't, but maybe there's benefits that we haven't quite recognized.
*  So, I mean, there are convolutional systems, right?
*  That are designed to look across images and mimic saccades in some way and then kind of
*  piece it together over time.
*  Okay, so let's reverse this.
*  What can we put in the bin to safely ignore?
*  Safely ignore.
*  Astrocytes, can we safely ignore astrocytes?
*  I don't know if we can.
*  I've been in communication with an astrocyte fan who has this idea that
*  astrocytes are really the seat of, like, subjective awareness and really higher
*  cognitive functions, right?
*  But the whole history of neuroscience has said ignore, ignore.
*  So maybe AI should too.
*  Are there other things that I won't pin you down on astrocytes.
*  I'll leave it open if there are things that you think we could safely ignore.
*  It is hard to answer that question, right?
*  It's, I think, right, you always, so a minimalist approach does say, let's try to only
*  use the ingredients or principles, like a small set of them to see what
*  functionality we get out of them, right?
*  The minimal set, right?
*  Minimal set, right?
*  To see what you can get out.
*  And so I think the minimal, that is interesting way to go forward, but I think it's hard to
*  rule out any one of those items, right?
*  So if you're going to take, if you're going to build your model around
*  astrocytes, what else would be relevant and included in that minimal set?
*  Would you have to have, you know, neurotransmitter types, right?
*  What you need to separate out your glutamate from your dopamine.
*  But now you're talking beyond what current AI uses also, right?
*  Because they're just point processes.
*  So like I just had Randy Gallistole on the podcast recently, and he has been arguing
*  for 50 years now that there needs to be some sort of intracellular mechanism for memory,
*  something to read from and write to, right?
*  And of course you have deep learning architectures where there is an external memory, but that's
*  different.
*  So, you know, he didn't say this, but I should have asked him, you know, do you think that
*  in artificial networks, he's not interested in AI at all, but do you think in artificial
*  networks, does that mean that we have to build in a little read, write memory into each unit?
*  You know, if someone came to you with that idea, would you roll your eyes?
*  There are all these things where there are still open questions in neuroscience where
*  you think, well, we don't even have the answer to that.
*  How would we know whether we should build it in, etc.?
*  Right.
*  No, I think pragmatically speaking, you know, if there was a weight and there are some really
*  interesting.
*  So, okay, I must say the LSTM, for example, right?
*  It does have some interesting little internal memory system.
*  There are some more interesting ones that have, well, I would say more powerful, I guess,
*  that have explicit little almost Turing machines, right?
*  Like little read, write memories, and they're kind of linked in with that gradient descent
*  process.
*  So they do learn to move bits of memory.
*  Yeah, when they need to.
*  And so it's certainly a complex thing to add in, but could it help?
*  And if it's valid, it's probably worth exploring, right?
*  What's the computational cost of doing it?
*  Of implementing these things and what's the benefit, right?
*  So just pragmatically speaking, right?
*  If you really care about getting something working and this can demonstrably show it,
*  you know, I think that's good.
*  To your point about transformers earlier, right?
*  If, you know, if the transformer could do what our, you know, our hierarchical, you
*  know, hierarchical system was doing better pragmatically and give our robots better
*  visual capabilities.
*  Absolutely, right?
*  Similarly, you know, we could have gone the other way and said if spiking were somehow
*  better for, you know, we would go in that direction, right?
*  So I was putting that on a spectrum, right?
*  Of transformers being like maybe a bit more removed from biology than that model.
*  And then spiking is closer to biology than that model, right?
*  You know, we sort of just chose to ignore a lot of stuff just for the purpose of getting
*  a minimal design to work with and understand and learn from.
*  Here's another way to ask the question.
*  Do you think all things being equal and not that they ever are, is it more important to
*  think to use inspiration from low level brain processes, you know, like spiking, for instance,
*  or higher level cognitive sciency type behavioral processes, like the way that humans do things
*  and just build it that way, more top down that way, or is it more important to focus
*  on sort of bottom up processes?
*  And you can't cheat and say both.
*  Right.
*  I love asking you these impossible questions.
*  This is why I wanted to have you on too, because it's just fun.
*  Really good.
*  These are really, really good.
*  Maybe.
*  The problem is you're a careful thinker.
*  And so you what you need, you need to be knee jerk like everybody, like many,
*  like the majority, right?
*  And say, this is the way.
*  This is why I guess what if we put it as the low level stuff?
*  So I think human behavior is great.
*  Human error is also great to learn from.
*  Right.
*  How about is using both this way, the low level stuff in, you know, qualified by the behavior.
*  Right.
*  So right.
*  That's both.
*  That's that answer.
*  That's the answer.
*  But it's somewhat of a direction.
*  I'll accept that.
*  Ding.
*  I'll accept it.
*  Yeah.
*  That's okay.
*  Okay.
*  Right.
*  Are there things that you have been thinking about besides sailing recently that you've
*  kind of been struggling to wrap your head around?
*  A problem you'd like to tackle that's just beyond your expertise or domain?
*  I mean, I certainly have been wondering about how to,
*  how I would move that research direction that we started those, you know, six years ago,
*  or whatever, how might move that forward in a good practical way.
*  Right.
*  Something where it's not a massive towering computer sitting next to a tiny robot, right,
*  to make something happen and also to take into account more about, you know, the robot's
*  own actions.
*  So I think there's a whole like research program that would be neat to, to plan out and figure
*  out.
*  I don't really know how it would move forward though, at this point.
*  If someone offered you a faculty position, a full lab, well-funded at an academic institution
*  at this point, would you accept?
*  Would you start your own lab if you'd given the opportunity?
*  Just not sure I would do at an academic institution.
*  But it's easier to do your own research at an academic institution, no?
*  I mean, otherwise you have to convince a funding agency.
*  Well, you have to do that at an academic institution.
*  What about, let's say a team of researchers.
*  Let's say a tenured position, right?
*  Well, that's not fair.
*  That's cheating because it's not a real lab situation.
*  But so you would rather start your own company and work on these things?
*  I think so.
*  I think so.
*  I think there's something important about what I learned and what really drives me is
*  the importance of what you're developing working, right?
*  What matters is that it's working and that it's helpful and beneficial.
*  And I think that if that's what you're working on, yes, it does take more work to get it out there.
*  But I think that's maybe the term academic in colloquial speech, right?
*  If something is academic, it means it doesn't have that utility necessarily.
*  That's how people say, oh, he's very academic, right?
*  But that's maybe where I'm going at, right?
*  So, okay, I guess it doesn't matter if I were in a faculty position or not, right?
*  That doesn't really matter.
*  Unless somehow the faculty position had a huge number of responsibilities
*  that would detract me from doing something right.
*  Yeah, administrative.
*  That might be part of the issue, right?
*  That's why I didn't say if you were offered a chair position or something,
*  because that's a no, isn't it?
*  Probably.
*  That's not core to my interests, right?
*  At this stage, maybe in the future, but that kind of thing isn't core to my interests.
*  Not sure I want to train graduate students either.
*  Because you're autonomous and you don't care about people like me, etc.
*  That's not the case.
*  I'm happy to advise them from afar.
*  For a lot of money so you can solve problems.
*  Sorry, Andrew.
*  I've had great conversations with people that I advise.
*  It's great, actually.
*  Teaching is something I also really appreciate.
*  It's been over Zoom, but having calls with people I know who,
*  maybe they already have their PhD or whatever,
*  but just having conversations and potentially even working on a little project.
*  I do seriously take, I think on our degrees,
*  it says something about the responsibilities as well that came with our degrees or PhDs, right?
*  I think teaching is a big part of those responsibilities.
*  I definitely appreciate being able to do that occasionally, too.
*  Well, it also said, there was also like when we were in graduate school,
*  the slogan was from bench top to bedside, right?
*  That's a very problem solving practical thing that I just shoot away.
*  Yes, yes, yes, from bench top to bedside.
*  Yes, that's what we're doing.
*  That's true.
*  I think it's just about mindset.
*  It's just about mindset.
*  Whatever position, I think you can do it in industry, you can do it in academia,
*  and there are hybrid things that are popping up now, too, which are happening between.
*  Yeah, that's exciting.
*  It's very exciting.
*  So yeah, any place is good as long as you can do what you think is important, right?
*  Given your comb shape, if you had to look back, right, thinking and starting from,
*  I don't know when you consider your beginning, quote unquote, but let's go back.
*  Well, you can choose if you would take a different trajectory,
*  if you would do anything differently in your earlier career, looking back.
*  Right.
*  I don't think I would change anything.
*  I mean, that's certainly the past was not certain.
*  It didn't feel very certain as I was going along the path.
*  But given where I am now looking back, yeah, I wouldn't change anything because I think
*  where I've arrived is a very, it's an interesting point, right?
*  So could I have gotten here faster if I had stayed true to my interests
*  and really pursued them?
*  Possibly.
*  But then you wouldn't have learned nearly as much.
*  If someone stays true just to their interest, doesn't that make them more eye shaped?
*  It might.
*  It might have.
*  And I think that and I think I might not have arrived where I am today if I had forced that.
*  Yeah.
*  So do you feel like you've made because often people give the advice you have to
*  step out of your comfort zone.
*  Do you feel like you've done that over and over or has it been always kind of a small step and
*  you've been kind of comfortable in your role?
*  Or have you made that a point to step out of your comfort zone?
*  And or have you felt like you actually have?
*  Good question.
*  I think I have stepped out of my comfort zone, but with gusto, I think with with interest in that.
*  Right.
*  So you're comfortable because you're interested.
*  You've always seemed comfortable to me in whatever situation you're in.
*  And that's also something that I have admired from afar, I suppose.
*  This is the first time I'm telling you that.
*  I wish I were comfortable in the situations as comfortable as I appear to be.
*  I think, yeah, no, I think there is, yeah, it's.
*  Yes, it's challenging to go into new environments and solve new problems.
*  Right.
*  But I think it's also very, very interesting.
*  And so I guess it's just the outlook of if there's an interesting problem, if you're willing to
*  learn and if you're if you can be comfortable with not knowing all the answers and
*  ideally you're in an environment that's supportive of that, that's the best.
*  That's the best thing, I think, to find that.
*  But it is it is hard to find, I think.
*  But is there anything that you wish you knew earlier on that you felt like if I'd only known
*  this or had this X skill, it would have tenfolded my progress, my rate of progress.
*  This is there's a related question.
*  I know you're thinking and I'm sorry to interrupt your thinking, but a related
*  question I was going to ask you is so you had software development essentially before
*  software development was required in neuroscience.
*  Right.
*  So coding skills, for instance.
*  And, you know, it wasn't required when I started graduate school.
*  I had to learn coding in graduate school.
*  But now it seems it seems to be a requirement.
*  Is is coding slash software development?
*  I know that those are different things, but is that computer side of things
*  the most important thing to the most important skill to have or to learn
*  for what I'm calling neuro AI computational neuroscience, the study of intelligence?
*  Yeah.
*  Possibly.
*  I think it is important to be able to write software.
*  I think it is tremendously helpful, tremendously helpful.
*  I would if someone I guess I would highly recommend learning something other than just Python.
*  If possible, that lab, that lab.
*  No, no, no.
*  Okay.
*  I don't know.
*  After 10 years, I still don't like Python.
*  She's still writing it.
*  And it's just that's the standard now.
*  It's it's terrible.
*  But anyway, I think another thing that would be interesting,
*  if something that would have been beneficial.
*  Well, it's hard to know.
*  Right.
*  So I've always, you know, FPGAs, the sort of developing things on in digital.
*  So there's a way of essentially
*  chips that can be reprogrammed, reprogrammable microchips.
*  And that's the one thing I don't quite have yet.
*  I've done barely the basics on it.
*  And I feel like that would be tremendously helpful to have moving forward.
*  But again, I can't.
*  For robotics?
*  For robotics or for research purposes, for building perceptual systems,
*  understanding how to translate software ideas into hardware
*  is something that but I can't say, you know, having known that would that have changed
*  my path at all.
*  Right.
*  Would that have allowed me to be a 10x, you know, potentially.
*  Right.
*  Actually, I think on Wall Street, traders are using FPGAs to have really fast
*  trading algorithms.
*  Right.
*  So that is a case where they are getting a 10x benefit of that.
*  Could I have somehow gotten a 10x benefit on something?
*  I'm not sure if it would have been anything I had ended up doing or not.
*  Right.
*  But OK, I think one of the most important things for neuro AI, though,
*  is to overcome that introspection bias where like you think that things work a certain way
*  because you think that's how they work in your brains.
*  I think people come up with theories about how their own mind works.
*  And right.
*  So rather than being driven by sort of the scientific research and findings,
*  they're driven by how they think things work.
*  And I think, you know, the reason that things like chess and go and all these
*  video games, right, people view these.
*  Oh, these are human activities or even logic.
*  Right.
*  These are quintessential intelligent human behaviors.
*  Right.
*  And they're not really right.
*  Well, going back to go, going back to good old fashioned symbolic AI, I mean, that was,
*  you know, they would videotape people playing chess and look at the behavior.
*  Right.
*  So that's always been kind of the intuitive introspective.
*  Although I guess that's an attempt to be objective about it, but they're still relying on,
*  you know, this chess is the way to go to.
*  Right.
*  Yeah.
*  So chess is the way to go.
*  Right.
*  It's sort of maybe it's a bit of an ivory tower concept as well.
*  Right.
*  That just, you know, look outside of that for, you know, the real problem.
*  Right.
*  What is the actual problem that we would like to solve?
*  Isn't that the hardest thing to do, though, because we are all as scientists
*  inundated with our own biases and this is a known awful problem.
*  That's what we need to develop AI for is to remind us how biased we are and to
*  generate alternative hypotheses.
*  I think that's key.
*  That's exactly key.
*  Yeah.
*  There's all this concern about bias and AI, but you're right.
*  There's bias.
*  There's, I know, right?
*  So that's the thing we're trying to get rid of in AI, but we,
*  we're perfect and we have bias.
*  So put it in.
*  That's right.
*  What are you doing?
*  We're putting it in.
*  No, that's exactly right.
*  That's it.
*  It should help us by working on these.
*  We should, yeah, it should be very helpful as a exercise and as an end product
*  to build these AI systems.
*  Patrick, this has been super fun for me.
*  You know, usually when I have a guest on, it's the first time I've met them or I've
*  met them, you know, once or twice before.
*  You, I've met multiple times over the years and I look forward to continue meeting you
*  over and over and 10Xing my own knowledge base by asking you questions.
*  It's been really fun.
*  Thanks for coming on.
*  Thanks, Paul.
*  Thanks for having me.
*  Great to chat and looking forward to the next time.
