---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 5358s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 1300
Video Rating: None
---

# BI 061 Jörn Diedrichsen and Niko Kriegeskorte: Brain Representations
**Brain Inspired:** [February 21, 2020](https://www.youtube.com/watch?v=TMVKl66K2K8)
*  It's not about, I mean we could have easily dug in our ditches and shot at each other
*  and saying like my method is better, my method is better, like scientists usually do.
*  And then there's a kind of rare collaboration like the one that Jörn and I have, which
*  for me has been transformative for my lab, and there's something deeper going on and
*  that is really hard to come by and it's very interesting to think about what's required
*  for that to work out.
*  How things are arranged on the cortical sheet is probably not that important for all the
*  competition.
*  You could argue either way.
*  I think, you know, I mean these things are very replicable and they are true and I think
*  the placement of components in the brain is very important.
*  The key lesson from the journey I think is that...
*  This is Brain Inspired.
*  Hey everyone, thanks for listening.
*  I'm Paul Middlebrooks.
*  So on the one hand, you have brains.
*  One way to think of brains is as a series of encoding and decoding information processing
*  steps.
*  Sensory areas encode incoming signals from the environment, like say you see a friendly
*  acquaintance and he says, dude, I saw the movie Inception.
*  Have you seen it?
*  You're a neuroscientist.
*  You would love it.
*  Is that how dreams really work?
*  This auditory signal gets encoded in some parts of your brain.
*  But then you could say to pass it along to the next part of your brain and ensure that
*  it maintains its representation as the same auditory signal.
*  That encoded information needs to get decoded so the next brain area knows that it has an
*  incoming auditory signal.
*  And on and on, encoding and decoding until there's a final decoding step that results
*  in motor output.
*  In our example, that would be silently turning around and walking away.
*  On the other hand, you have neuroscientists.
*  Neuroscientists have tools to measure brain activity and ask how that information gets
*  represented in brains.
*  And these days we have big brain data.
*  Big data from brains.
*  We measure lots of brain signals from lots of different brain areas in parallel.
*  So where do we begin with that?
*  What's the right level to ask about?
*  Does it matter what parts of the brain a signal comes from?
*  Can we ignore that location information and focus instead on how the brain activity patterns
*  differ among different stimuli?
*  Or when does it make sense to focus on some bit of brain activity in particular and ask
*  whether it can tell you if a person is about to engage you in some awkward situation or not.
*  Jörn Diedrichsen and Nico Kriegskorte, my guests today, have called these different
*  layers these different ways of examining what's represented in brain signals the onion of
*  brain representation.
*  The idea is that as you peel the onion you remove some facet of information that may
*  or may not be relevant to your particular goal of understanding.
*  And that's of course a cursory and insufficient introduction to their review paper that we're
*  talking about which is called peeling the onion of brain representations.
*  So Nico has been on the show before.
*  He's a professor at Columbia and he studies visual perception and how we can use deep
*  learning to better understand how brains visually perceive the world.
*  And Jörn who's new to the show today specializes on the motor side of things.
*  He runs his lab at the University of Western Ontario where he studies the learning and
*  production of coordinated and skilled movements.
*  Jörn and Nico have been collaborating for a few years now on representational models
*  of brain activity.
*  And because of that and because they're joint authors of the paper that we discuss I decided
*  to try having them both on at once which presented a few challenges but I think it
*  turned out well.
*  I enjoyed it.
*  You may remember last episode I had Michael Rescorla on and Michael and I talked about
*  representation in philosophy and in brain and machine computation.
*  And today I got Nico and Jörn's view on representation as well.
*  Then we go on to talk about the onion peeling it and putting it back together and you know
*  we cover plenty of surrounding topics as usual.
*  Patreon supporters I'm working on getting a separate podcast feed going especially for
*  you so I'll announce that when it happens.
*  It'll have extra bits of interviews that I will save just for your personal podcast feed
*  as a way of saying thanks to you.
*  So that will be coming soon.
*  And in the next month or so you'll be getting parts of the neuroscience AI course as it
*  comes out.
*  Bolaagy, Joan, Sebastian, Jan, Jimmy and Michael thank you for your recent support on Patreon.
*  Show notes for this episode are at braininspired.co slash podcast slash 61.
*  60 61 61.
*  Okay here's Jörn and Nico.
*  So I'm reading peeling the onion of brain representations and I'm having this moment
*  where I'm reading the text and the text is referring to one of the images you know and
*  I'm looking at the image I'm looking at the panel in the image and it's not like matching
*  up for me.
*  I'm like having a hard time like understanding how they relate.
*  I keep going back and forth and getting kind of frustrated but then it kind of starts to
*  make sense and I'm starting to kind of get it you know and this kind of goes on and on.
*  I finally convinced myself oh okay yeah now I understand how the figure and text match
*  and I realize finally that I'm actually looking at the wrong figure.
*  You know the scary thing is is I you know halfway convinced myself that I was you know
*  that it all makes sense right and this is this is not a good sign for you know for a
*  scientist for things like confirmation bias and etc in my own practice right.
*  But I also recognize this thing has recurred in my in my life reading papers and you know
*  it's like what the hell is wrong with me so how can I do science if I can't match figures
*  to text you know.
*  Jörn we failed.
*  It's me it's my failure as the as the reader.
*  No your failure is our failure.
*  It actually made complete sense once I matched the text to the correct figure so.
*  Okay good.
*  Jörn welcome to the show and Nico welcome back thanks guys for being here.
*  Good to be here.
*  Good to see you.
*  Good to see you too.
*  Alright so just to kind of start off and we have we all have these hurdles to overcome
*  you know this sort of resistance.
*  Mine obviously is just a general incompetence but you know for fun I thought I might start
*  by asking both of you maybe for an example of some hurdle or some challenge that you
*  might face you know either these days or maybe something that you even overcame earlier in
*  your scientific careers you know in your scientific journey.
*  Jörn you're new I'll start with you.
*  Is there anything that you can think of?
*  I mean I have one thing that that relates very highly to also writing this paper and
*  maybe even the problem you had in matching text to figure is that things can be extremely
*  clear in your brain and in your mind and you kind of think you perfectly understand what
*  what you're talking about but actually the misconception that just saying the words and
*  then expecting other people to know exactly what you mean is a very treacherous trap to
*  fall in.
*  Okay and so what I really learned is that you cannot be clear enough and even if you're
*  the person that you talk to nods and smiles at you and says I perfectly understand what
*  you're saying you cannot be sure that they actually understand really what you say.
*  As the podcast host nods and smiles as he says.
*  So if I have ever learned one thing is that I can work for hours and hours and hours and
*  trying to write something that I think is crystal clear and then when I get the reviewer
*  or comments back they say that I didn't understand it or they completely misunderstand it and
*  they are very sure about that they understand correctly.
*  So if all the for all my trainees is that's the first thing and every trainee falls into
*  the gap they think immediately what they say is understanding because like obviously they
*  experiment and the supervisor knows what they're talking about but actually getting the right
*  words making it very clear making sure that the representations in the other person's
*  brain are actually the representations that you want to be is not a not a very easy feat
*  and that's yeah so I'm still failing on that every day but you know at least I'm
*  warned that that is a big problem.
*  Writing is really hard any type of writing.
*  Why are you even talking?
*  I wouldn't know I wouldn't know about that.
*  In a direct conversation you at least have the option to question and to talk and to
*  make sure that it's coming across.
*  This is a challenge ever going challenge in a podcast format as well which it's weird
*  because I have to I expect a lot from my listeners and it's always hard to strike the right to
*  know where the right balance is and who knows if I strike it right.
*  Some people seem to like it some people you know I get all sorts of comments like it was
*  over my head but I enjoyed it and I think I'm not doing my job you know.
*  Anyway so so Nico how about you are you are you perfect.
*  My life is a series of failures and I constantly feel inadequate and has always been like that
*  and insecure about you know what I understand and what I don't understand.
*  And of course you know I mean as everyone always says we learn from error right.
*  So this is what what drives us to improve things.
*  That's just a sense of how we're we're not quite there yet right.
*  And so it's a good thing but it's definitely extremely uncomfortable.
*  So a lot of my life is spent in in relative discomfort.
*  And when you see people give give talks then that's very misleading because of course when
*  we give a talk or we write a paper that's after years of thinking about this stuff right.
*  And then we leave out all the things that we're not confident about we just say like the
*  little sort of pearls of insight that we've arrived at.
*  And then then we seem very confident and in control.
*  But that's just because we choose to only move in in the small part of this whole space
*  in which we are comfortable and confident.
*  The lowest error of the in the error surface is what we present.
*  There's this meta aspect to this too though you have to sort of be comfortable being
*  uncomfortable and just get used to it.
*  It's a strange thing but useful.
*  Yeah.
*  This reminds me this reminds me of a song I think Fiona Apple.
*  I'm good at being uncomfortable so I can't help changing all the time.
*  I felt like yeah that's nice.
*  That's a good description.
*  That's good.
*  Yeah.
*  It's a I also tell my students that that failing should be fun and you all you need to do
*  in your PhD is to the trick is to really fail very fast.
*  Right.
*  Just not you know try things out fail learn from it and move on.
*  And that's that that iteration is important I think.
*  And then being knowing that that's part of the process that's that's really important.
*  Yeah.
*  The resilience that comes with that.
*  This is all really good stuff.
*  So all right.
*  Very good.
*  I guess none of us are perfect.
*  This shatters my my preconceived notions here.
*  How did your collaboration come about.
*  Did you guys bond over your hatred for neuroanatomical spatial locations or what.
*  How did you guys come together on this recent paper and then you've wrote a couple written
*  a couple before as well.
*  I think we met.
*  How do we meet.
*  I think you contact me because you said oh I read your paper I thought that was interesting.
*  The original.
*  Yeah I remember two things and I don't remember in which order they happened.
*  One was that I reviewed a paper of the very important one that is sort of the basis for our
*  collaboration since which is the paper about pattern component modeling.
*  And I was very inspired by that paper and also all a little bit and I was struggling to
*  follow the math but I could tell that this is an important thing and that it has some elements
*  that are missing from my framework up to that point for analyzing brain activity patterns.
*  So it was really an inspiration and I knew like this guy is onto something and this guy has
*  something that that I need.
*  And you know so that was like one step.
*  And then the other thing was that I think we wanted a little bit maybe maybe then I talked to
*  my graduate student Alex Walter and we wanted to you know play around with your methods and I
*  think we contacted him about the code for some piece of his analysis and he shared that and that
*  began a conversation where in the end my graduate student moved to your lab for an extended
*  period and we started collaborating and we haven't stopped collaborating ever since.
*  Yeah. And then the I mean the from from my perspective was I mean he commented on my paper
*  and and then I realized that yeah I mean the problem is so PCM and representation analysis
*  representation similarity analysis are very related methods and with PCM that might be
*  elegant the math might be compelling but obviously it has a lot of problems in for people to use it
*  to be intuitive and all those things are given in RSA.
*  So there were really a lot of things that are important about statistical development that really
*  RSA had nailed namely intuitive you know the the option to explore the data data visualization and
*  so on and so you know for despite the fact that we had these method developments in my lab we
*  actually used RSA very heavily and you know I think it's it's been a great conversation and what
*  I really value is that that ultimately it's not about I mean we could have easily dug in our
*  ditches and shot at each other and saying that my method is better my method is better like
*  scientists usually do.
*  But the awesome thing I think about the conversation is that that we both I think Nico and I hope I
*  also understand that methods are just tools and and the key thing is like the question is what you
*  answer with them and that's what we feel passionate about and and you know with the tools you just
*  choose the best one and the most appropriate one and and that's I think that's been like the
*  underlying core in our collaborations that I really value.
*  I was going to ask about collaborations next just in general because if you're not an important
*  university unless you tout your interdisciplinary nature and and that everyone you foster
*  collaborations between departments and stuff and and so how important do you think is
*  collaborating versus really digging in your heels and maybe not competing against each other but
*  sort of focusing on your own narrow pathway what's the right balance there.
*  I don't know I think it's a little bit like you know this might be a slightly OK analogy but like
*  bike racing right so bike racing is a sport where you need to you know do your own thing and you
*  need to work hard but you know if you don't work together with other people and form those
*  coalitions within the race and talk and you know get into one common goal then you're never going
*  to succeed.
*  You're leaving out the performance enhancing drugs but OK.
*  So I've skipped those.
*  So I'm talking about clean bike racing.
*  Yeah so and you know if you piss people off and you're an asshole then that's the end of your
*  career usually.
*  Well it doesn't count for all the people but so that's certainly the case.
*  That's also in science.
*  I mean there is an interesting you know sometimes you need to stand up for yourself and say you
*  know this is an idea that I've worked on and here's my work and not you know basically put your
*  light under the shovel and that is unfortunately often what happens with some trainees often female
*  but also for some male trainees it's not natural.
*  The really good and very smart people sometimes don't have the the urge to really go out and
*  bang their drum and there are other people who bang their drum very well but you know fall short
*  in some other departments and you know both of them are skills that you kind of have to have.
*  But in terms of collaborations I mean it's also you know we're spending a lot of time on science
*  and we need to feel passionate about it and that also means in collaboration the personal level is
*  also really important.
*  I mean you really need to get to like the other person right.
*  Yeah.
*  And not just for their skills but also for their opinions and general outlook on life.
*  You have to respect them anyway.
*  I know in the decision making world where I come from people are kind of entrenched in their
*  camps and looking at it from the outside you think that everyone hates each other but in reality
*  everyone's going for this common goal and they do respect each other even if they do you know have
*  plenty of friction between them.
*  But your collaboration between you and Nico is really not fictional at all.
*  Right.
*  Oh I wouldn't say that.
*  So what is something that you guys disagree about besides.
*  What do we not disagree about.
*  We have fundamental disagreements for example about the naming conventions for functions in our new
*  Python toolbox and stuff like that.
*  Important stuff.
*  So you know it is hard.
*  It is hard.
*  I have to say it's very tough.
*  And we're both very stubborn so that doesn't mean things.
*  Yeah he's obstinate he doesn't want to understand.
*  But we also fundamentally disagree about this onion paper.
*  Absolutely.
*  I hope it shows in the writing.
*  No I don't think it does.
*  Should we. Is it too soon to talk about that.
*  Should we get into the details before.
*  Maybe one one thing about collaborations I think there is kind of very qualitatively different
*  modes of collaboration right.
*  There's sort of just positive interactions with other people in the field that can be critical but
*  still lead to something good.
*  Then there's the kind of collaboration where you have something like you build a tool and you share
*  it with others and maybe you give advice or something like that.
*  But it's somewhat asymmetrical.
*  Yeah. And then there is a kind of rare collaboration like the one that you and I have which for me has
*  been transformative for my lab.
*  And there's something deeper going on and that is really hard to come by.
*  And it's very interesting to think about what's required for that to work out.
*  And I think there is has to be so this element of complementarity where there is a common goal.
*  And in our case maybe that has to do with wanting to measure brain activity patterns with
*  massively parallel methods such as functional imaging and cell recordings and then linking these
*  measurements to theories to be able to test theories.
*  But then there is also sort of a complementarity where John works in the motor domain and he's
*  interested in motor cortex and motor control.
*  And when he talks he uses metaphors from biking which I would never come up with.
*  You know I don't know when I see a biking race I see only competition.
*  I wouldn't even notice that there's you know this is a very subtle thing that I'm hearing about for
*  the first time. So it's quite inspiring.
*  You know I'll see I'll watch the next differently the next time I see you know some bikers flash
*  by on TV.
*  So and I am focused on vision and on perception.
*  So that's there's a fundamental complementarity there.
*  And then also in terms of intellectual styles there is a complementarity.
*  Right. So I feel like deeply that John has something where I have shortcomings.
*  Right. So he has some abilities that I feel that's exactly what is sort of missing.
*  What helps me solve my problems.
*  And I just want him to help me solve my problems.
*  And I can also learn a lot.
*  Right. So because I love the things that he's good at and I'm kind of suffering from the fact
*  that I'm not as good at them as he is.
*  But this inspires me a lot.
*  And I I'm also you know I know that I can make progress there.
*  You know I know that it's not a loss.
*  I'm not the last cause.
*  I can always learn more.
*  And you know for me that's that's how it works.
*  Yeah. I can't return the compliment.
*  I mean I feel with other things especially the same way that there are things that I just don't
*  you know Nico you know it's often like it takes all kinds in science.
*  Right. I mean there's you know we can't just say oh I'm I'm not as good as that person.
*  No I'm not as I'm not as famous as Nico Prieckscott.
*  And you can feel that.
*  But ultimately the key thing is you need to know what you are and be proud of it and then
*  respect other people for what they what their strengths are and what they bring to the table.
*  And yeah I mean there's just so much that I've learned from the that is fantastic.
*  Is this collaboration style.
*  Is this the modern version of the Renaissance person I'll say to be politically correct where
*  back in the day there wasn't as much to know.
*  I mean there's still a lot to know but someone could sort of touch a lot of different areas.
*  But now everyone's so specialized that everyone fills each other's holes.
*  You know are the days of the lone researcher gone.
*  I think the days of the lone researcher.
*  Yeah I think if they ever existed if they ever really existed.
*  Yeah if they ever really existed.
*  I mean.
*  I doubt it that they ever really existed.
*  Nobody came up with ideas in vacuum.
*  It's always based on communication.
*  And when you think of people like Newton who worked in his study you know doing his alchemy.
*  Yes and no.
*  But he was embedded in the natural philosophy movement in Britain at that time.
*  And there was a lot of people that discussed and wrote and interacted.
*  And without that community Newton wouldn't be here.
*  So there is a reason why there are hotspots of the high science coming up.
*  And it's not the soul the lone wolf that suddenly comes up with this smashing theory.
*  Although you know history then post-hoc constructs it because we want heroes and single
*  world that do these things.
*  But you know that's never how science was done.
*  But I think you know I mean moving forward I think yes.
*  I mean for me it's been transformational here at Western to have my lab not alone but
*  but also here together with two other PIs and co-supervising and transformational to
*  have Nico as a collaborator and send students back and forth and exchange ideas and so on.
*  I mean those are they change the way you you work and the change the way you think about
*  science and how you all your things.
*  And they also can change the way that that your students interact with each other and
*  get to know science.
*  So Nico you pointed out that you are more concerned with the perception side of things
*  and and Jorn is more concerned with the motor side of things.
*  But but you're both on board with this concept I think that that I love that movement is
*  the primary goal of brains.
*  You know this Daniel Wolpert approach here and you know there's this idea that actually
*  thoughts are sort of modified motor commands that have been internalized throughout
*  evolution and and you know in that sense thought is a sort of proto form of action.
*  So am I right in thinking that you're both on board with this move movement is the goal
*  of brains essentially.
*  And if so is this the lens through which you view all of your brain research whether it's
*  motor or or perception.
*  You need to ask Nico about that one.
*  So I first I first heard this argument from my colleague in Cambridge and now colleague
*  here Daniel Wolpert whom I greatly respect.
*  And when I heard him say that I found it entirely compelling and I still find it quite
*  compelling. But there's also sort of a part of me that wants to question it and argue.
*  And that's because the perception to action cycle is a cycle.
*  Right. So you could also call it the action to perception cycle.
*  It depends how you sort of where you draw the line where you know how you sequentialize it
*  to think about it. We have a focus on the brain and perception is the input and action is
*  the output. But there is an arbitrariness there and there's a very very interesting
*  philosophical question I think.
*  But I think it's sort of too maybe too big for for right now.
*  But I would love to explore this more deeply because it is a deep question.
*  And you could say you know yeah we want to control our actions but just so that we can
*  fulfill our needs and that we can perceive the world.
*  What the ultimate goal is is sort of in the eye of the beholder.
*  Ultimately there might not be any ultimate goal.
*  I think that this idea of movement first is really a little bit out of the minority
*  complex that the community has.
*  I mean if you look at neuroscience you know there's the relation the ratio of vision
*  research to motor research is maybe a to one or something in terms of mass.
*  And that's just vision. That's not even just for all of the session.
*  And so you kind of you know when you see that and you kind of think about would I rather
*  lose my sight or would I rather be quadriplegic.
*  You know it's certainly not an A to one decision clearly here right.
*  So but I think I mean the interesting thing is that it gives you two very different
*  perspectives on representation and how you think about representation.
*  And I think the way that the old representationists have thought about representation
*  is really just on a basically driven by perception right.
*  And when we need to represent these objects in the world of being to have codes that
*  stand for these objects and I think that that idea is not coming as natural when you
*  think about controlling.
*  Right. Right.
*  So I think that's it. That's kind of an interesting tension field.
*  And ultimately whatever theory or whatever concept or framework we have for representation
*  it needs to capture both of those sides.
*  Let's let's go and talk about representation models.
*  So and to kind of start off let's keep kicking around the idea of representation itself
*  for a minute.
*  I just had philosopher Michael Raskurla on which you guys wouldn't have been able to
*  hear hasn't been released yet you know anyway but we went kind of deep on the history
*  and the current landscape of representation in philosophy in particular in philosophy of
*  mind and the philosophy of computation.
*  And what's what's relevant for today is that he distinguishes between something that
*  you're trying to understand namely like the brain and mental computation the mind.
*  And how representation is the right way to understand computation in brains.
*  This is called the representational level in computational field versus something that
*  you're building which you know a computing machine and and how for that all you really
*  need are formal rules and properties.
*  You don't need to understand what will be represented by those rules when you're
*  building the computing machine.
*  And this is called the syntactic level in the computational.
*  Work but but neural networks there's this you know weird in between right because yes
*  we do build them but with as few formal computational rules as possible.
*  I mean there are constraints right.
*  And that so we build them but what we're also trying to understand them as computing
*  systems and in the hopes to better understand our brains and our minds and how our minds
*  compute.
*  I don't know with that in the background sort of how do you you know think of
*  representation in computation in general and its relation to neural activity in
*  particular.
*  And I don't know who might want to jump in.
*  Maybe I would ever so slightly disagree with the idea that computer scientists can do
*  without the concept of representation.
*  I think computer scientists even when they're not working with neural networks but
*  certainly when they are working with neural networks think of the states of the system
*  as representing things like numbers.
*  So in a simple Turing machine you think this is the case.
*  Yeah the memory the memory cells represent things.
*  I think that is already a deeply representational way of envisioning a computer and as
*  for all the computation models that I'm aware of.
*  I feel like that's the case but it's a less problematic way of thinking about
*  representation because these are systems that we build ourselves.
*  So we it's much more crisp in terms of there being a single sort of abstract description
*  level that involves representation that perfectly explains how the system behaves and
*  things become more murky when we use that abstract language of description to understand
*  a natural system like a biological brain.
*  An abstract syntactical type level like non-representational level you mean?
*  No an abstract representational level.
*  So the language that's natural for computer science is also representational and then
*  we want to apply that to the brain.
*  And I think that is well motivated.
*  It's our best shot.
*  But it's also problematic.
*  Yeah I would agree.
*  I mean so I'm not quite sure when somebody says I'm a non-representational view of
*  something. Now you can have a non-representational view of a system itself but what you can't
*  have is a non-representational view of the relationship between a system and the world.
*  So a computational system and the things that it relates to that it computes that it
*  acts in. That relationship between the brain and the world you know that is that is the
*  core definition of representation.
*  How does things that happen in the brain relate to things that happen in the world.
*  So this is your definition of representation.
*  There's nothing right.
*  This is like a super basically umbrella that is in this sense void of meaning.
*  But all I'm saying is is that I'm not quite sure if I understand when people say so if
*  you take a non-representational view of the brain you can only talk about the brain in
*  resting state and look at these fluctuations.
*  That's it. That's a clear non-representational view.
*  But as soon as you talk about how does this neural activity relate to anything that the
*  brain does or sees or experiences or tries to achieve.
*  You're talking about relationship between things that happen in the world and things that
*  happen in the brain and that relationship.
*  That's the philosophical call of the term representation for me.
*  Now. Yeah.
*  Well I was going to say this is intentionality or aboutness.
*  Intentionality aboutness exactly.
*  John Searles intentionality aboutness.
*  So now there are like two radical views I think on this.
*  And I think the paper is trying to kind of get right in between and kind of break up
*  the front lines.
*  So on the one hand I think that what we might call the old representationalists in
*  neuroscience that say like OK here's a neuron I measure it and it clearly represents
*  velocity of the arm or it represents the color of the object or it's a gamboa function.
*  OK. So that basically what happens here is there's a one to one relationship between
*  the information contained in the fighting rate of the neuron and some physical variable
*  that we used to think about the world some feature.
*  Grandmother cell. Yeah.
*  Yes. But also it doesn't have to be it can be distributed code like population vector
*  and motor cortex is a classic.
*  When we say like oh yes there's movement direction and velocity that's a Newtonian
*  concept about how we describe our movement and there's some activity and we just say
*  yeah that's exactly you know there are these cosine tuning functions and we're done.
*  Now that's what we've called the feature fallacy in representational modeling that you
*  think that the way we think about the brain and break it up in physical variables that
*  the neurons encoded in the same way and I'll describe by these features.
*  And I think in the visual cortex that has given rise to Nobel Prize who will be so
*  right now in the motor cortex they had I think you can sum up the motor cortical
*  neurophysiology field for the last 40 years by having really who will increase land
*  and trying to find what is the code in motor cortex and they you know paper after paper
*  is the idea that yeah you know it comes a limit for velocity it comes a little bit for
*  muscles it comes a little bit for something else and there's a lot of mixed selectivity and
*  we don't actually know what's going on.
*  So most papers are like this.
*  And so I think that triggers the other side to say like you know let's throw out the
*  baby with the bath water and not think about representation at all.
*  And it's all a dynamical systems and there's some rules and then now you might call those
*  people that say like I don't want to talk about representation.
*  Now the interesting thing is that if they don't want to talk about representation they
*  can't actually talk about how those dynamical systems relate to things that the brain wants
*  to do like moving down.
*  The dynamical system has to produce the thing right.
*  The state of the dynamical system relates in some lawful way to the things that it needs
*  to produce.
*  OK.
*  Not just what it produced but the internal states you know in a way that relate to things
*  that that are context you know what is the next movement or whatever.
*  And I think you are there is no intellectual distinction no clear intellectual distinction
*  that that shouldn't be called representation.
*  So I call that representation because it's about to relate this or things that have been
*  in the world and things that happen in the brain and studying that relationship I think
*  is very important.
*  So when we study these recurrent networks or you know dynamical systems we can think
*  about attractor points and oscillations and you know beta waves.
*  But ultimately we also need to think about how does the information or the difference
*  in the states relate to the things that the thing wants to do or wants to see or represents.
*  But is that dependent on your interpretation of the system or is it inherent to let's say
*  the dynamical system right.
*  So you know are you adding anything by saying that there is representation or is it
*  inherent to the system.
*  Well yeah.
*  Yeah that's a that's a great question.
*  So.
*  My view is that representation gives us a more abstract language of description on top
*  of dynamical systems.
*  So it's not incomplete to say it's a dynamical system and we can study it as just a dynamical
*  system and never refer to representations.
*  We can do that.
*  But the representational interpretation is powerful in linking what goes on in the brain
*  to the world as you said.
*  And this gives us a functional understanding.
*  Much like in biology we want to understand organisms we want to understand the functions
*  of different parts of their body.
*  What's the function of a hand.
*  Right. And we can come up with all kinds of stories and that is on the one hand somewhat
*  arbitrary. There's the problem of just so stories in these interpretations of how
*  some body of an animal might be adapted to its environment.
*  But it's also clearly a very powerful explanatory concept.
*  Right. And representation to interpret something as a representation is to ascribe a
*  particular function to a pattern of activity in the brain.
*  And the function is to convey particular information about the outside world.
*  And that requires that the information be present there and that it's encoded in a
*  format that can be exploited by the rest of the brain.
*  And it also requires that it actually is exploited by the rest of the brain.
*  Right. These three criteria.
*  So this is a terrible question.
*  But the analogy of a tree falling in the forest when no one is around to hear it just
*  popped into my head. Right.
*  So the tree has the ability to produce sound.
*  It's all there in this really terrible metaphor.
*  So I apologize. But if there's no one there to hear it, then one might say that would
*  one say that the sound still happened.
*  So if there's no one there to interpret that this is a representation, is it a
*  representation if there's no mind to interpret it?
*  And we'll move on. I promise.
*  After this. Yeah, I mean, the answer to that is like it was nobody's around to see the
*  tree falling. Who cares?
*  But there's a model in a forest and it is no.
*  OK, so we'll go with who cares?
*  I mean, this is important.
*  Right. So the tree is still falling.
*  But the pattern of activity that is not read out, that can never even in principle
*  affect behavior in any way, is not a representation.
*  But I mean, to answer your question, like our representation is real or not.
*  Well, nothing is real.
*  Right. I mean, nothing.
*  None of our models dynamic.
*  The brain is also not a dynamical system.
*  Right. At some level of description, a dynamical system is a good analogy
*  or powerful model about how the brain activity might evolve on the short term scale.
*  But it's not a you know, it's not a dynamical system.
*  It is not a system.
*  And likewise, the brain does not have representations.
*  They do not exist.
*  But it's a conceptual tool to understand the relationship of neural activity and
*  things that happen in the world.
*  Nico, you happy with that?
*  Almost, almost.
*  I would say for me, for me, there's slightly more arbitrariness at the level of
*  representational interpretations.
*  So my my conception is a little bit lighter weight.
*  So I've been talking regularly to a philosopher at Bernard College at Columbia,
*  John Morrison, and he has a slightly stronger representational view where he
*  thinks more of an ontological interpretation of representation, where he
*  thinks there are systems that really do have representations and there are other
*  things that really don't have representations.
*  And I'm not comfortable with that.
*  And he gets there by much the same argument that you're on kind of started,
*  although I think he wouldn't pursue it to this consequence, which is that for all
*  the levels equally, it's questionable how exactly they relate to the reality.
*  Right. So it's unclear whether why why we should make weaker claims about this
*  particular level of description that we call representational.
*  But to me, it seems that the arbitrariness that I experience when I try to pull it
*  off and trying to understand how the brain works is at a level where I am closer
*  to Dennett in philosophy, which John tells me is a minority view in philosophy
*  in saying that we take the intentional stance and we describe the system as though
*  it were representational and maybe in some deep sense it is.
*  But there's not only one representational interpretation, and you could apply this
*  language to any system, even to a thermostat, except when the system is very
*  simple, then maybe you have no need for the heavy artillery, the heavy conceptual
*  artillery of representational language to kind of make sense of what the system does.
*  I suppose, Jern, you don't think representation is causally, computationally
*  causal then. And Nico, you probably don't either.
*  You can't do computations with representations, right?
*  Yes, yes, you can.
*  You can only only you can only compute with.
*  Oh, I see, because it's it's embedded in within the structure of the computer.
*  Computation on the on on representations, I would say there's no separation between
*  the symbol and its meaning.
*  These go together.
*  Well, the combination is involved on representations.
*  So once you are at a representational level of description, these representations are
*  causal. You take that representation away.
*  The computation doesn't work anymore.
*  Now, once you are at a level of description below it, meaning you look at the electron
*  flow in in transistors or in spiking potentials and neurons or membrane potentials,
*  then you can choose not to talk about representation and the system still works.
*  So there is non-causal.
*  So it really is really, you know, it's really a confusion about levels of description, I
*  think, here. And the key thing that, you know, is a rather simple idea is that as you
*  move up in the level of description, the concepts that you need to do build causal
*  models become different.
*  And it's a non-trivial relationship between them.
*  And physicists have understood that for a long time.
*  And I think neuroscience is just catching up on that.
*  Yeah, I mean, it's really whether it's causal or not, at many different levels of
*  abstraction, you could have a causal model.
*  Right. And there is not greater causality at lower levels of abstraction.
*  In fact, the dynamical systems perspective is non-causal.
*  Right. So you could even argue it's the other way around.
*  At this higher level of description, where we think about representations causing
*  downstream other representations through computations that transform them, that that
*  is more of a causal interpretation than a dynamical systems description, which is
*  mathematically defined, but not mechanistic in the sense of cause and effect.
*  All right. So I think it's time for us all to take a shot of our liquor.
*  And I think that's actually a good transition to talk about encoding and decoding to get
*  into the onion.
*  Quote of the show so far, by the way, is Jern's, nothing is real.
*  I believe that's a direct quote.
*  That's good. So, so representations and encoding and decoding, the brain has to encode
*  and decode. And so encoding is basically how a stimulus gets translated into neural
*  activity into some, let's say, representation.
*  Whereas decoding, which is so decoding is talked about in two different ways.
*  And the way that you guys use it in the paper, and I think properly, is that decoding in
*  terms of the way the brain's function is translated some encoded neural activity into
*  something useful for downstream neural activity and or motor output or behavior.
*  And brain processing is one big cascade of encoding and decoding until a behavior is
*  produced. So it's this interesting, you don't often think of it, but one area in the
*  brain is has to be an encoder and a decoder in that respect.
*  Do I do I have that picture right?
*  So these are confusing concepts, right?
*  I remember when when I was an undergraduate, we learned about the brain, how signals travel
*  from the senses to different stations in the brain that forever relate.
*  And I was wondering, when do they ever get processed?
*  Right. So clearly, that's a that's a notion that's very limited.
*  The idea of encoding and decoding is one step more sophisticated than that, but still
*  limited. And so the important thing is to see what can that buy us and what are the
*  limits? What it buys us, I think, is a perspective.
*  On what is the transformation from the sensory evidence and the signals at the sensory
*  surface to the activity patterns in the brain?
*  And that is the encoding.
*  And then when we when we take that perspective and we want to say, well, this serves some
*  function, then we have to assume that somehow it's read out and then we view the rest of
*  the brain as the decoder.
*  But of course, where the encoder ends and the decoder begins is in the eye of the
*  beholder. It depends on the region X that we chose to focus on.
*  Right. And if we move on from from X to Y, then the little piece of processing from X
*  to Y that was part of the decoder is now part of the encoder.
*  Right. So that is one thing to keep in mind.
*  And another thing to keep in mind is that the decoder is not the inverse of the
*  encoder. Right. So when we think often we think of encoders and decoders as inverses,
*  but that doesn't make sense because then this begs the question why you don't just copy
*  the input. Why would you and so, you know, we have to think about what is the purpose
*  of the encoding. And there's a number of possible answers.
*  You might want to compress it, for example, for passage through a limited channel like
*  the optic nerve. You might want to transmit it through time.
*  You might want to change the format so that other inferences are computationally close
*  or can be reached in in few steps.
*  Yeah. So, Paul, I think they asked.
*  So I agree with you that you can look at brain processes as encoding and decoding, and
*  that might be a useful perspective. But at least for one half of the onion paper,
*  and this might also underlie your initial confusion, we are talking not about encoding
*  and decoding in terms of what the brain does, is about what we as researchers do.
*  Right. OK, so this is the first onion that you have, and that's the data onion in a way.
*  And this is the one that I feel more most comfortable with because, you know, that's
*  just my view as a statistician on the world and on the things that I'm doing.
*  And there it doesn't matter what the brain does.
*  It's this the thing is like I want to learn something about what things happen in the
*  brain and what's the relationship to things that happen in the world.
*  That's I want to study representations and I can either take an encoding or decoding
*  view. And people do. Right. And this is something that Jack Gallen in his lab has talked
*  a lot about about. You can either say take an encoding view, meaning like we're going
*  to explain brain activity and predict brain activity from the features of the world.
*  All we do is the other way around. We pretend that we don't know what happened in the
*  world and we read out or predict the things that happen in the world from the brain
*  activity. That's a decoding.
*  That's how decoding is mostly used, I think, in the literature.
*  Yeah. And that I think that is still the first perspective that comes to mind when you
*  hear that term. And that's also the one that I think is at least confusing and makes
*  sense. So it's not about what the brain does in this case.
*  It's about how we treat the data that we get and how we try to make inferences.
*  And so there are these different styles.
*  Now, the interesting thing is that it doesn't matter.
*  You can do encoding and decoding models in visual context or area that in your perspective
*  takes information in. You can also do encoding and decoding models in motor cortex,
*  where you think like, oh, why do you do an encoding in motor cortex?
*  Motor cortex doesn't encode anything. That's not the point at all.
*  Right. It's the type of statistical tool we apply to build this relationship.
*  And I think what's nice about the methods or the class of methods that Nico and I have
*  worked on is that it acknowledged this, that this is the subjective directionality that
*  you choose. And there's no end of discussion in the literature about whether you should
*  do encoding or decoding, blah, blah, blah.
*  It's kind of boring from a statistic point of view because ultimately it doesn't matter.
*  Right. It really doesn't matter whether you what you what which direction you do.
*  You're going to get similar results and people are confused.
*  And so our same PCM lie right in the middle.
*  They say it's neither encoding or decoding.
*  What we have is two complex multivariate patterns.
*  We want to find the relationship between them and can we build models of that relationship?
*  And that's what really kind of is the main main thing.
*  So I think the surface discussion should you do, you know, what type of analysis should
*  you run on your data and so on is kind of misled and sometimes that, you know, ultimately,
*  let's just get clear what we're trying to infer here.
*  Well, that's what the representation models do is just tease out the information that
*  is in the activity in the population that's represented.
*  I don't know. Maybe we should step back and.
*  Well, we could either peel the onion, start peeling the onion or talk about what a
*  representation model is first.
*  I'm not sure what the best way is.
*  Maybe maybe we should slightly motivate because, you know, what what this is all about.
*  So really what it's all about is that neuroscience needs to decide how it's going to
*  evaluate computational models.
*  So we're getting these richer and richer measurements of brain activity, tens of
*  thousands of channels is always advancing and humans and animals.
*  And that's wonderful.
*  And it's inspiring.
*  And it gives rise to this vision that we can just measure everything and build it up.
*  But we also need the top down approach where we're building these models.
*  And the models are also getting very big.
*  And now we can simulate many aspects of cognition at scale.
*  So at the complexity of the information processing that's actually going on in the
*  brain to some extent, and some sort of subcategories like vision or certain aspects
*  of motor control and certain aspects of high level tasks.
*  But then as we build these models, we also have to be able to test these models with
*  brain activity data.
*  And this is a problem that is not getting enough attention.
*  And, you know, and I have been thinking about this for a long time.
*  And I think it's great that more people are getting interested in this problem.
*  But there are really fundamental questions there.
*  And these are both fundamental questions of theoretical neuroscience and sort of
*  more methodological questions of, you know, OK, here you've got your your dozen
*  neural network models and you've got your brain activity data set from array
*  recording. So now how do you adjudicate between these models?
*  Right. And it requires some difficult decisions because you have to decide what
*  aspects of these high dimensional measured data do you want to rely on for
*  making that comparison?
*  So you could naively think, well, let's have the models predict the brain
*  activity. Right. But then how are you going to do this?
*  Are you going to predict every single neuron, every single spike?
*  That seems too much of an ask because brains are idiosyncratic.
*  Here we have three brains that at the level at which I'm interested in brain
*  information processing are identical in their functionality.
*  But in terms of their particular neurons, they're all unique.
*  And so we have to abstract from these idiosyncrasies somehow.
*  And then in neuroscience, there's been these long traditions of somewhat
*  separate literatures discarding different portions of the measured information.
*  And the goal of the ONYIN paper was to kind of systematize this range of
*  approaches that exist. It's really kind of a review that brings the range of
*  existing approaches to what to discard and what to focus on when analyzing
*  brain activity and using brain activity measurements to adjudicate among models,
*  you know, to bring that into a framework where we can understand how the
*  approaches relate to each other.
*  I think that one of the most valuable things about this approach and and this
*  is some sort of deficit that we have as humans, I think, because even when they're
*  back when they were single cell, single neuron recordings, maybe a few people
*  thought, hey, maybe one day we'll be able to record two neurons at a time and then
*  gets bigger and bigger and bigger.
*  But what has been lacking is what happens when we get there, when we can record
*  every single neuron at the sub millisecond time scale, what do we do with it?
*  And as humans, we have this tendency to think, well, we'll figure it out when we
*  get there. You know, but so I think that this representational model work and and
*  just conceiving of it as an onion as the whole is really important work.
*  Yeah, I think I mean, for this part of the paper, it's really important.
*  What we wanted to achieve with the paper is that to make explicit, they often
*  implicit decisions that are being made by saying, like, I'm going to analyze my
*  data like this. Right. People usually don't take a justification of why they
*  exactly do decoding or why they make just look at a map, a somatotopic
*  map of S1. Why do they choose to present the data in that way or analyze or think
*  about the data this way? And these are often implicit decisions.
*  And they they have consequences.
*  They have consequences on how the authors think about the paper and influence
*  the way theories are built.
*  So just to give an example, as we all know, neuroscientists love maps.
*  And one of the iconic maps we have in our textbooks is the homunculus in
*  primary motor code. Yeah.
*  Right. The idea that there are these areas that relate in a one to one
*  relationship to body parts.
*  OK. And this is very deeply ingrained in people's brains now, because it's just
*  such a tempting and conducive kind of like you look at the map and you just
*  understand it. So this is kind of what in our way is kind of like this is basically
*  looking at the outer shell of the onion.
*  Right. You know, how things are arranged on the cortex.
*  And now I think that the key the key insight came in like, you know, studying
*  figure representations and one just staring at these maps, knowing that we
*  measure them highly reliably, just looking at that intersubject variability where
*  none of them look like the homunculus.
*  They look all different and they are overlapping and messy.
*  And you can generate data analysis pipelines that give you like you can rescue
*  that somatotopic map and it's there and you can talk about it.
*  But you're missing like, you know, you're missing the main point, right?
*  You're missing the main point that there's some structure there that relates to how
*  we move the hand that has nothing to do with the somatotopic map that you cannot
*  understand when you just map in a winner take all fashion.
*  And so that's kind of the key idea that we need to dig in the onion.
*  And now the question is, OK, if we don't look at maps and we want to analyze
*  population codes in a more general fashion, there are many ways of doing this.
*  And which feature are we are we tossing everything away and just saying, can I
*  decode this physical feature from there?
*  You know, look, do I look at the covariance matrix?
*  Do I do PCA?
*  Do I do more fancy methods?
*  Do I take into account where those neurons are on the cortical sheet at all?
*  These are all decisions.
*  And looking ahead, I think.
*  People will make these decisions and that will influence the way they conclude in
*  their papers and the way they develop their theories.
*  And it's really important to understand that the tools we use shape the way we
*  think. And that's kind of the way that that first
*  the first half of the paper really is targeted at this data analysis process.
*  Starting at the outside of the onion, then should we just start there and peel it?
*  Yep. All right.
*  So the data onion, you mean?
*  The data onion. Yeah.
*  And then we build it to the scientists.
*  Well, we can go either way. I don't know.
*  We have. Well, let's do the data on your first really quick because that's easy.
*  Yeah. There's only one onion.
*  OK, one. I disagree on everything.
*  But, you know, there's there's an onion that you cut and then there's super glue
*  to put it back together. So that's the core of the onion.
*  OK, let's start with the whole onion.
*  All right. So someone's in an fMRI machine and you get data about the homunculus.
*  And when they move their thumb where it lights up and so you have the location
*  and the activity of the cortex and or, you know, you're recording single neurons
*  or, you know, EEG or whatever, you have these massive recording techniques
*  and you're getting location information and activity information.
*  Is that all there is to say about the outside of the onion?
*  Well, yeah, no, I mean, that's the data that goes.
*  That's the whole onion. Yep.
*  Now what do you do with it?
*  And there was one tempting thing to do is just to label each spot on the cortex
*  for which body part it responded most.
*  And you get a homunculus.
*  Kind of a little bit messy, but, you know, it's there.
*  It exists. Right.
*  Now, the tempting thing is that you then stop thinking
*  and vision it would be retina topic mapping and higher up
*  finding the category selective regions in the ventral stream.
*  And the the insight from our own work is that when you do that,
*  it makes people very happy and makes reviewers happy.
*  It makes readers happy. It makes everybody happy.
*  Television programs.
*  It's it's just, you know, you have a map.
*  You understand what the thing is doing.
*  And the treacherous thing here is that you are only looking at the outside of the onion
*  and really how things are arranged on the cortical sheet is probably not that important
*  for all the competition.
*  You could argue either way.
*  I think, you know, I mean, these things are very replicable and they are true.
*  And I think the placement of components in the brain is very important.
*  And all of this literature is going to be a treasure trove
*  in decades to come for building models that take the spatial relationships into account.
*  For example, things that are closer together can interact at shorter latency
*  and with shorter, shorter connections and less metabolic costs.
*  So this is all totally key.
*  However, just mapping it out doesn't mean that you understand the mechanism.
*  Right. You haven't understood how how the information is represented,
*  what format it's represented in and how the computations work.
*  Right. So it's sort of a first step.
*  It's essential, but it's not the whole story.
*  Yeah. You guys don't burn your architectural bridges.
*  I'll be talking to Daniel Bassett in a few days here.
*  So she has something to say about architecture.
*  All right. So then you can take the radical other view and saying,
*  and you know, that's basically in the in the original Haxby paper, that's kind of this one.
*  Let's not think about FFA and and Fusiform phase area and and parry-up-a-cum-pull-place area.
*  Let's just think about the information that we can gather from it.
*  And that's like, you know, basically removing all any information
*  and just using a linear classifier in correlation to decode something.
*  Is there asking just is the information, linearly decodable information in this data?
*  So you could scramble all the neurons in an area and you could decode all the same information.
*  Right. And at a finer scale, actually, it is more more random.
*  So does it matter exactly where those neurons are in the brain to computational function?
*  And this is not just an imaging, but also an electrophysiology as people got into array recordings
*  and looked at populations of neurons.
*  They became interested in not only thinking of the codes as population codes that has a longer history,
*  but also analyzing them multivariately as population codes.
*  And so there's this whole separate literature where you say, let's not care about where these neurons are.
*  Let's care about what information they convey.
*  Yeah. And even, I mean, going one step further, it's not only forget about where they are,
*  also forget about tuning functions of individual neurons because it's only the population now that is important.
*  And not only the population. And this is where I think statistical concepts are really important.
*  When you look at a method like linear decoding or correlation, you can actually it doesn't use the whole data.
*  So there's this concept in statistics that's called the sufficient statistics.
*  So if you get a result, you base it on data.
*  But there's this intermediate point, things that you can compute on the data that is sufficient to get exactly that result.
*  And when you prove what a sufficient statistics is for a certain method, you know exactly what information is discussed.
*  And so this leads then or this leads us then if you just look at linear decoding,
*  the sufficient statistics for linear decoding is the covariance matrix of the data or more generally the second moment matrix of the data.
*  And that's it forgets everything else.
*  So whether it's like the distribution, you know, whether there are special clusters in your population, all of that is discarded.
*  You're only interested in that one statistics that you choose.
*  And so I think thinking about very critically with each method, which parts of the data is actually looking at it looks at all the neurons,
*  it looks at population. But you can actually generate other populations that if you would show these populations to a neurophysiologist,
*  you would immediately say, no, this is not a real neuron recording.
*  Neurons don't look like this. And it would have exactly the same second moment.
*  And the decoding would be exactly the same as the real data.
*  So if you choose to use this tool, you wouldn't be able to distinguish it.
*  But there are features in the data that are just not in this, that can't be captured with this method.
*  And so looking at one feature at a time, can you decode this feature or this feature?
*  That's kind of the feature fallacy that you just, you know, basically look at it.
*  And now, representational similarity analysis and pattern component analysis go one step further in just saying, we're not interested in a specific feature.
*  We don't even know that there are specific features.
*  We don't want to, you know, we don't necessarily want to think about features and what feature, which neurons encodes which feature.
*  But we just got to think about the structure of the neural activity and the structure of the feature space and relate it to each other.
*  And so this is basically now you haven't, you know, you haven't gone further much in terms of, like, you know,
*  finer arguments about the distribution or you're still throwing away the spatial information.
*  But now you're looking at all features in one or possible features you can think about in one go.
*  And that's a much more complete description of that particular view.
*  So this is going from the stimulus response matrix, where we have other stimuli along the vertical and all the responses,
*  all the neurons along the horizontal and an activity in every entry of that matrix to this square matrix that stimuli by stimuli.
*  And this could be the second moment of the stimulus response matrix, or it could be the distance matrix.
*  And these two are actually equivalent. You can compute one from the other.
*  And you can think of this sufficient statistic as characterizing the representational space or the representational geometry.
*  And that's most intuitive to me when I think of the distance matrix, where every point you have for every stimulus,
*  you have a response pattern that's a point in the multivariate response space.
*  And then you have the distances between these points that define the geometry of the ensemble.
*  And that's what's defined by this intermediate level summary statistic that we found particularly useful.
*  Just for clarity, what does a second moment measure?
*  Oh, I mean, in a way, it's the variance covariance matrix of the data.
*  And we say in general, we say second moment because it's not just variance and covariance.
*  So basically, how similar is this pattern? How much does this pattern correlate with this pattern?
*  But we also take into account that one pattern might be much brighter than the other one or much more active.
*  In one condition, the brain is very, very active. In the one condition, the brain isn't very active.
*  If you just take the covariance across neurons and loxals, you would subtract out the mean.
*  So second moment is just a statistical concept for covariance matrix where you didn't subtract out the mean.
*  OK, very good. So we've peeled away one level of the onion.
*  We have these representation models of pattern component modeling, representational similarity analysis.
*  I'm not sure if we've said enough about them.
*  Oh, we're going the other direction, right? So what we did, we looked at the outside of the data on you.
*  We looked at the outside of the data on you and all the way in the center and say, OK, if you only look at one feature,
*  you're just looking at this one kernel and you might not find the center of the onion.
*  Now, the level that we've described and that our research is mostly focused on is using the second moment.
*  And that is already a very rich description of the neural population.
*  And just to be clear, those linear decoders, the center of the onion, there's lots of tiny little bulbs in there, lots of linear decoders.
*  It's not there's no one center like you just.
*  Well, because some people tries to decode velocity and another person tries to decode muscle activity
*  and another person tries to decode precision or talk or snap.
*  And they all can declare victory because they all can decode that particular feature from the thing.
*  And not all of them are just getting one kind of needle in the haystack view of the whole representation.
*  And I think what we're pointing out here in the paper is that if you really want to describe the whole representation
*  in the constraint that you only look at these things that you could read out linearly features,
*  then you need to look and put them all together.
*  And that's what what representation of similarity analysis does for you.
*  Now, we still have thrown and so now we're going out.
*  Now we say, what do we actually peel away to arrive at this level?
*  And in many ways, I still think this level is a very happy medium between peeling away and not peeling too much away.
*  And I think we will keep doing things on this level, but we want to acknowledge that we peel things away.
*  We throw away all the spatial information and it's we and our lab and many other people are looking at the spatial information
*  kind of through the new lens now and saying like, no one does do like maps, but we want to look at we want to acknowledge
*  that the spatial information is very variable across subjects and the exact X, Y, Z location might not be that important.
*  But the relationship between how these things that we can describe as representation models and how they map on the surface, you know, that's something.
*  Do you think of it more as a architecturally as a constraint in a principle of information coding or is it is it part of the information coding itself?
*  Well, it's a product of learning. Right.
*  So there are learning rules in the brain. There is architecture, genetically predetermined architecture.
*  But there is also the learning algorithm that is important in the sense of system.
*  And that learning algorithm learns on some data and it has effects.
*  Now, that learning algorithm isn't spatially blind.
*  It's, you know, nearby neurons have more, you know, more opportunities to communicate.
*  They might build more long term pronunciation with each other.
*  So they ask the things that could be changed, but actually where the learning algorithm follows that gradient, basically, and makes it so.
*  And looking at the when we are at the level of these relatively fine grained activity parents that we look at, maybe within a cortical region,
*  I think they are the product of some learning and some, you know, which is partly a random biological process.
*  But there's some commonalities about how how these look like when you look at them on the cortical surface.
*  It's going to tell us a lot about what they are trying to optimize and what they're trying to do and what computational function they serve.
*  OK, so so rather than thinking about them as constraint, the product of some biological constraints as genetic and some learning rule that was applied to things that the system tried to do when it grew up.
*  How things were learned in what order, at what time, those sorts of environmental considerations.
*  Yeah, exactly. Yeah, yeah. That's interesting.
*  And what the system tried to optimize, what was important for that brain region to do.
*  Right. And I think understanding those things, you know, ultimately, we need to come up with theories that link from the things that the brain wants to do.
*  And one of the hard genetic constraints, but I think the literature on plasticity for people who lost their arm or worn without a hand or are blind tells us that there's a lot of stuff that happens or can happen when the system just, you know, misses one input.
*  Right. And the representations might look very different.
*  And understanding those features are important.
*  This also maps well onto your work on sequential motor activity and how that might get encoded in within a spatial distribution, right?
*  Depending on how you learn it and and different types of sequences, which we, you know, we can't really get into, but it's really interesting stuff.
*  Yeah, it's also relates a lot to work that my colleague, Thomas Marken at UCL does on looking at MUTs.
*  Right. So what happens if you lost that 20 years ago?
*  What happens to these representations?
*  What happens when you never were born with a hand?
*  And so I think that, you know, that this is a really kind of interesting field to look at, but how do these activity maps come about?
*  So now we're not saying it's the exact map that is important, but there is the spatial relationship between these elements that we've identified by analyzing the second moment.
*  That is still important. And coming up with that is, you know, I want to keep an open mind.
*  It might turn out to be really, really informative.
*  It might turn out to be very simple that there's just a smoothness constraint on the cortex and, you know, whatever.
*  And that there isn't really much interesting things going on.
*  But it's clearly a data feature that we haven't looked at and that we might want to feel uncomfortable about discarding.
*  Nico, do you want to respond to that?
*  And also, I just I see that we're two minutes until the half hour.
*  Maybe just to wrap up on my part, that maybe maybe good to to summarize a little bit.
*  So the the whole of the onion is the stimulus response matrix for some little area in the brain that you've recorded from with an array or with functional imaging.
*  And you've got you've presented a number of stimuli and you've got a response for each of your response channels, each of your neurons.
*  And then you also know where these neurons are. Right.
*  And then some some of us, some neuroscientists want to make a map out of that.
*  They want to make a little map of that patch of cortex and show the selectivities.
*  And then others say, well, I'm really interested in computation.
*  I want to see what information is in there.
*  So I am not so interested in this map.
*  So I'm going to throw away the locations matrix and just look at the activity profiles.
*  And then I have some summary of the distribution of activity profiles.
*  And that's the level at which you on has defined representational models and as a probability distribution over activity profiles, which I think is a extremely important concept.
*  And to me, an inspiring concept, because this keeps more information than I want to keep.
*  I want to go one step further or where I say, well, not only do I not care about the exact positions of those neurons, I also don't care about the distribution of activity profiles.
*  I care about the geometry of the representation.
*  And that can be characterized by the second moment or by the distance matrix.
*  And interestingly, this sufficient statistic now gives you under certain assumptions about the noise, for example, let's say it's a Euclidean distance matrix and the noise is isotropic.
*  In that case, this gives you all the information that is encoded about the stimuli in the neural responses.
*  And it gives you additionally information about the format of the code.
*  For example, you can then predict what can be linearly decoded.
*  And you don't need the original stimulus response matrix anymore.
*  You don't need the distribution of activity profiles.
*  You just keep this stimulus by stimulus matrix.
*  And that's been very useful to us in comparing human brains to monkey brains and monkey brains to computational model representations.
*  So that is sort of the one one layer deeper.
*  And then there are other people who have said historically, well, we don't care about all dimensions of the representational geometry.
*  We just want to check, can this particular important variable be decoded?
*  And that's where linear decoding is right.
*  This is people who are interested in asking whether particular information is not only present in the data, but is present in a format that can be linearly decoded.
*  And they're interested in that because they're saying, well, if it can be linearly decoded by us, then it can certainly also be read out by downstream neurons.
*  And then you could go further and you could say, well, maybe we should restrict this more and say it should be decodable from a local set of neurons.
*  And then you have some more restricted definitions of the decodable information.
*  And that's where you get into the core of the onion.
*  And in the end, you're you're back with looking just at a single cell and the selectivity of a single cell.
*  And of course, that was the classical approach in neurophysiology, where you you only had one cell to look at and you tried to understand the selectivity and the tuning properties of a single cell.
*  Or on a good day, you have two cells on one electrode.
*  But that was a good day.
*  OK, then that's a great summary for peeling the under.
*  So let's put it back together and then I guess we'll wrap up pretty quickly.
*  So, yeah. So the classical studies in neurophysiology that looked at selectivity were interested in single neurons.
*  Now, you can ask why. On the one hand, you know, that's a place to start.
*  And, you know, the idea, the idea being you look at one cell at a time and then, you know, once you've looked at 100 billion of them, maybe you understand the brain.
*  But of course, that's a naive thought. And every everyone knew that.
*  And even from studying single cell responses, people understood that the code isn't fundamentally a single cell code, that in order to interpret what these these findings mean, they have to think about the population of neurons and the information encoded in the population.
*  And so the concept of the population code was very strong in theoretical neuroscience before it was strong in the analysis of data.
*  Right. So people started caring about what the information contained in the population and the format at the level of linear decodability, which is not the only biologically plausible concept of decoding or reading out a brain representation.
*  But it's an influential one.
*  It's almost the first easiest, first intuitive way to do it.
*  I would imagine.
*  Yeah.
*  And partly, partly, it's that you have a hammer and then, you know, it looks very tempting to just pound the nail.
*  Yeah. And now you have this better hammer of, you know, measuring lots of cells and you have the linear decoders and you can ask these these more specific questions.
*  But then, of course, you want to say, well, you know, we have these we decode certain dimensions.
*  Why don't we just decode all dimensions?
*  Why don't we just look at all readout dimensions?
*  And that leads you to the representational geometry at the second moment.
*  All within a certain range of brain area and stimuli.
*  Yeah. Yeah.
*  And now. And so so then you add the representational geometry.
*  So you could say, well, maybe we're happy there.
*  Right. I mean, you and I have certainly been happy there.
*  Why would anyone want to add further outer layers to the onion?
*  But there are good reasons.
*  So you could say, well, now all you care about is what's linearly decodable or the representational geometry.
*  But the same representational geometry can be spanned by many different sets of single neurons with different kinds of tuning.
*  And not all of these might be equally easily computed from the stimulus input.
*  So it might not be irrelevant which particular set of a single neuron tuning characteristics spans this representational space.
*  It might be important for understanding the computational function.
*  And that's where we might care again about the particular encoding and look at the whole distribution of encodings.
*  Right. And then if we're at that stage and we can say, well, part of these computations going on is lateral interactions between these neurons.
*  It's a recurrent neural network.
*  These neurons are talking to each other and that informs their tuning and who they can talk to depends on where they are.
*  They can't talk at equal cost to a neuron that's that's far away.
*  So the placement is important.
*  And then we're back with the entire onion.
*  So we're kind of back at maps.
*  But the key the key lesson from the journey, I think, is that the way we look at these maps needs to fundamentally change.
*  And I think that's from a statistical point of view.
*  We don't really have the tools to really analyze those types of maps very well.
*  And that's that's, I think, an interesting frontier.
*  And I was trying to ask questions.
*  It doesn't matter. It doesn't matter at all.
*  Is there something to be learned from where the regularities and that's that's I think is really kind of interesting, interesting things to pursue.
*  And one of the things that you can correct me if I'm wrong, but that I'm not seeing in the onion as a whole at any level, is the actual dynamics, how things change over time, because all of these measurements are made within a window of time and then averaged or whatever.
*  Yeah, I think this is a particular lens that we've applied here, which is very driven by the fact that we both started with FMI, functional magnetic resonance imaging, where you just don't have that information.
*  So it's like having only a single cell.
*  You know, you don't think about populations right away.
*  And in this case, it's just constrained on the measurement technique that at the time scales that we might be interested in, it doesn't deliver reliable information.
*  Now, you know, yes, that is absolutely another dimension.
*  And we can write another onion paper.
*  So it's somewhere some other onion that the temporal information is.
*  We didn't focus on that.
*  You can animate all of these sufficient statistics and look at them as movies, right?
*  You can have the representational distance matrix as a movie or the second moment as a movie, or you could have spatiotemporal patterns and then do the same analyses.
*  So there is some sort of straightforward ways to extend it.
*  But it's also true that there are some fundamental questions that are in some ways analogous to the questions that we focus on in the paper, which is that they're about correspondency between different systems.
*  And our paper focuses on spatial correspondency and how we can overcome the idiosyncrasies and in terms of spatial layout of things at a sort of fine scale.
*  And then when you get into dynamics, there's also the problem of temporal correspondency.
*  How do you integrate over time?
*  How, you know, maybe one participant gets the joke slightly later than another one.
*  And but still fundamentally, their brains are going through the same cognitive process and understanding the movie or the joke.
*  And how can you relate these these two processes to each other?
*  Guys, I think that this is a good, good place to to leave it with the with the onion.
*  And I'll point people to the paper as well.
*  And and I'll make sure that people remember when you're reading the text, look at the right figure and vice versa.
*  It's hard to understand if you don't do that.
*  Maybe just a quick, quick hits here.
*  Do spikes matter? Does spiking matter?
*  I think spiking is absolutely essential for neurons to signal over long distances.
*  And it might also be computationally important, but I don't know about that yet.
*  And it's not on top of my list of detail, biological details to add to the models that we're building.
*  To the neural network.
*  That's that's subjective. So it could be essential.
*  It could be an essential feature.
*  It's pretty likely with high probability that there is exists some level at which spiking isn't important anymore.
*  Which it is not important.
*  It is not important. Right. So so that that I would hold.
*  You know, I think the proof is in the pudding what the what the what the real what the real importance of spiking,
*  whereas this continuous rate codes are.
*  And, you know, I don't know.
*  Finally, what's something that you used to believe that you now think is naive?
*  Oh, lots of things. I forgot them all, I think.
*  You know, this is like, you know, this is what the brain does when you when you believe something that was naive.
*  And then just to maintain yourself worse than maybe you used to believe that something was real.
*  And now you believe nothing is real.
*  No, I don't believe that nothing is real.
*  All right. I got you. I have that quote as well.
*  What about you, Nico?
*  I think when when I started, I thought it was kind of glamorous to try to find out how the brain works, but also impossible.
*  Yeah. And I thought anyone who thinks that it's possible to succeed must be naive.
*  Now, I think, you know, I've kind of lost this confidence that it's impossible.
*  I think, you know, who knows? Maybe we have a shot.
*  That's the directly opposite way most people go into it.
*  You have to start off naive and confident that you can figure it out and then it beats you down over time.
*  Right. Maybe I'm just getting more naive as I get older.
*  Well, the problem is if we figured it out, we're out of a job. Right.
*  So, you know, yeah, it would be a good thing to do.
*  Yeah. Yeah. Slow it down a little bit.
*  I'm not worried. Yeah.
*  Thanks, guys, for being here with me. And I appreciate you both being on.
*  It's been fun.
*  Great. Good to see you, Paul.
*  Good to see you, Nico.
*  Bye, Paul.
*  Bye, Nico. Okay. Talk soon. Bye-bye.
*  Brain Inspired is a production of me and you.
*  You can support the show through Patreon for a microscopic two or four dollars per month.
*  Go to braininspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show and prohibit any annoying
*  advertisements like you hear on other shows.
*  To get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year. Find them at thenewyear.net.
*  Thanks for your support. See you next time.
