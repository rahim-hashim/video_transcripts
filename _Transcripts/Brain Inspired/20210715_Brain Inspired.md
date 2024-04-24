---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4530s
Video Keywords: ['Education', 'Science', 'Technology']
Video Views: 24440
Video Rating: None
---

# BI NMA 02: Dynamical Systems Panel
**Brain Inspired:** [July 15, 2021](https://www.youtube.com/watch?v=s5ztJRdGI3w)
*  Trying to understand the brain as it is a fully formed thing is somewhat of a very incomplete
*  picture because it grew that way and the plan for which it grew that way also grew that
*  way over a much longer timeframe.
*  And so those are really important constraints in my mind for how we understand it as a whole.
*  I like the fact that I'm fitting RNNs to biological data, but I don't actually believe that the
*  brain is making little analog continuous signals or not.
*  They're making actual spikes with all of this rich biophysics underneath it.
*  I worry sometimes that our classic ideas about neural network training are missing a lot
*  of really cool stuff that biology can do that may implement totally different kinds of learning
*  that operate on much lower time scales or that change excitability in interesting ways.
*  This is Brain Inspired.
*  Hello, it's Paul.
*  This is the second panel discussion about the topics at Neuromatch Academy 2021.
*  Today we're talking about the scientific experiences and perspectives about dynamical systems
*  coming on the heels of the lectures and tutorials on linear systems, real neurons, and dynamic networks.
*  With me today is Adrienne Fairhall at the University of Washington, Seattle,
*  Bing Brunton also at the University of Washington, Seattle,
*  and our old friend Kanaka Rajan at Mount Sinai in New York.
*  And you'll learn more about them in a moment.
*  Among other things, we all agree that talk of doctrines should be banished from neuroscience.
*  It's the only part of the show where we're all passionately talking over each other for 10 seconds or so.
*  I link to their labs and information in the show notes at braininspired.co.uk
*  Enjoy.
*  I thought maybe what we could do is go around and you guys could each introduce yourself,
*  say what you do, you know, very high level.
*  But I thought maybe it'd be fun to ask you.
*  So if you ask a musician what his or her favorite work is,
*  it's never the same as what is their most popular work, what they're best known for.
*  So I thought in addition to talking about something that talking about what you do,
*  you could reveal something that you feel most proud of that might be maybe it is the expected thing that you might be most proud of.
*  But what do you consider your best idea or body of work or feat or event, et cetera?
*  Adrienne, perhaps we could just start with you.
*  So go for it.
*  Sure. So I'm Adrienne Fairhall.
*  I'm Adrienne Fairhall. I'm a professor at the University of Washington.
*  My background is in physics.
*  So I came through statistical physics and was really inspired to get into neuroscience via working on dynamical systems.
*  I started out in plasma physics, actually, and then went to turbulence and then only started neuroscience in my postdoc years.
*  So I am a computational neuroscientist.
*  So I do work on many different systems.
*  And I think the way I like to think about that common theme of our work is really very central to this topic,
*  which is trying to apply dynamical systems ideas to understand coding.
*  We sort of came into neuroscience thinking about neurons as encoding information.
*  And from the beginning, I've always been very interested in how the picture that we have of neuronal representation really arises from the fact that neurons are physical systems that undergo transformations that are governed by dynamics.
*  So I guess the piece of work that I love maybe most, I have done a lot of work on adaptive coding, and I really am fond of that too.
*  But I really particularly love this way that we were able to describe the dynamics of single neurons that have these long time scales of adaptation.
*  When I saw that happening in the fly visual system, in collaboration with Bill Bialik, we realized that that might be able to be described as fractional differentiation.
*  And that turned out to really be a very good model.
*  So the way that the neural firing rate transforms the envelope of a time varying noise stimulus matches very well with the idea that it's taking a fractional derivative of that noise envelope.
*  And that matches really well and explains a lot of kind of weird looking behavior in the fly visual system, and then also turns out to be not a bad model for cortical neurons.
*  So I love that. And I think it's really kind of unexpected finding that's weirdly transferred from one system to another.
*  I should have added what I should make you guys also say is what you think other people would guess that you would say that you're most proud of.
*  Do you have an answer for that, Adrienne?
*  It's probably our nature paper, you know, 2001, which is a paper I really still love to write that way.
*  We showed this very neat adaptation of a neural input output curve to the standard deviation of the input and that your neurons are able to dynamically adapt their dynamic range to sort of almost instantaneously match the dynamic range of the input.
*  So we're doing sort of efficient coding, but continuously and on the fly.
*  So that's my.
*  It's got to be the high profile.
*  We will know.
*  Yeah.
*  Great. Thank you. Bing, maybe we should move on to you.
*  What are you most proud of and what do you do and what would other people say is your best known or best work, let's say?
*  Yeah, Paul. So I've been thinking about that.
*  So so so like Adrian, I'm a computational neuroscientist at the University of Washington, but I think I arrived at doing kind of similar type work and dynamical system from a pretty different path.
*  I started out as a biology major as an undergraduate, and I did it in part because I knew I loved biology, but it also meant that I could take as much physics and math as I wanted.
*  And and that was where I actually got to dynamical systems.
*  So I took my first in emphasis in class with Jerry Marsden, and it totally changed my entire life.
*  From then on, I realized that this was basically everything that I actually cared about, because life is is the study of things that change and the dynamical system is the mathematics of things that change.
*  And so I wanted to do that.
*  And up until that time, I had been my research had mostly been in molecular biophysics, working with microorganisms.
*  And it wasn't until my my first year in graduate school where I randomly heard a talk from Carlos Brody, who became my my graduate PhD advisor.
*  And it was all about dynamical systems.
*  And afterwards, I went up and talked to him and said, this is this is this is awesome.
*  Like, I need I need to be in your lab because this is the this is the type of math that I wanted to do.
*  And I knew very little about neuroscience at that point because I've been a different type of biologist, but kind of joined the lab, built some stuff and learned a bunch.
*  And so so I feel like I kind of came in from this field.
*  So Asian talked about she came in the field from from physics.
*  And I think that's what came in actually from from from biology, even though we arrived at largely overlapping research interests.
*  So, yeah, so so I think I think the the the work that I'm probably people still know me for is is my is the work I did with Carlos.
*  I think at the time, one of the first sets of papers that established rodents as a viable system for studying decision making and cognitive processes.
*  And so I had developed a task for for studying decision making using rodents where the information coming in was uncertain and it was was really variable, along with a of actually dynamical systems.
*  Framework for modeling this behavior.
*  And so since then, I've I've really been drifting kind of more towards I've been more drawn towards naturalistic behaviors.
*  And so a lot of what my lab works on now is using tools from dynamical systems to understand the newer computations underlying behaviors that are unstructured and long term and sometimes have multi scale dynamics.
*  And and using these analytic tools to connect not only the neural activity, but connecting it with kinematics and other behavior measures.
*  And so that's what I really love doing now.
*  And I think it's really hard for me to pick a favorite project because we work on so many different things.
*  So this projects in my lab now focusing on everything between insects.
*  Now we have a couple projects on rodents, nonhuman primates, and we have a large project on on on human clinical data as well.
*  And so so everything everything from from from insects to humans is my favorite.
*  So I would say that there's one one technique that is a that is a kind of a vectorized generalization of a very simple linear model, as we have talked about in linear systems day that we've been working on called dynamic mode decomposition.
*  We've used it for a variety of systems.
*  It's I think I think the success of this method, which also came from physics from fluid physics, is is an example of the unreasonable effectiveness of linear models.
*  It is at its core a very linear, a very simple set of assumptions.
*  And it almost doesn't make sense that it should well work as well as it does.
*  But it does. And so we go with it.
*  I feel like everyone is from physics now.
*  So hearing that you're from biology was kind of an interesting diversion, although it was biophysics and it was kind of sounded pretty physics heavy in your biological background.
*  So you weren't stamp collecting, as they say, perhaps.
*  No, I've always loved math and physics and and computer science.
*  But I think I knew from from earlier on in my training that I wanted to study biology.
*  Connika, you've always despised math and physics, right?
*  Well, I'm a giant stereotype.
*  So I come at it from an engineering perspective.
*  So hi, I'm going to go.
*  I am an assistant professor in the Friedman Brain Institute and the Department of Neuroscience at Mount Sinai in New York.
*  Like like my brilliant colleagues here, I'm also a computational neuroscientist.
*  I run a small lab here.
*  And I had my undergraduate degree was in biochemical engineering and biotechnology.
*  And then I studied physics for a while, then essentially lapsed out of physical sciences fields and self identify as a biologist now.
*  So I'm not an engineer.
*  I don't want to build the smartest AI that does the most effective state of the art, whatever.
*  I want to build the machines that with all their bumps and warts can help us understand the biological brain in air quotes or the biological nervous system that given the constraints that biology has put on the fact that neurons fire at a certain timescale or their synaptic dynamics, then what is the system capable of doing and why it does so?
*  And so there's the dreaded mechanism work.
*  So that's what my lab is devoted to doing.
*  So in keeping with the theme of last week, I can tell you about the stuff that I'm the best known for and the stuff that I am secretly the most proud of.
*  So the secret pride, so that stuff that I'm actually most known for is the fact that I build these recurrent neural network models and train them to match the dynamics from real experimental data.
*  So I've done this in a variety of nervous systems from larval zebrafish, mice and macaques and recently with the human systems.
*  So that's sort of the body of work that I'm the most commonly associated with.
*  And yes, I'm super proud of it and all that.
*  But I think in taking a page from Adrian's book, I too am secretly proud of an early piece of work that I did.
*  And I hesitate to say this out loud, but it had very little to do with actual biology.
*  It had these idealized randomly connected model neurons.
*  And in that particular randomly connected recurrent neural network model, I wanted to ask how networks in the brain or in the biological system reconcile subtle inputs with all this rich ongoing activity that they have going on.
*  So, you know, we have all of these rich internal states and dynamics.
*  And in the old days, they would just model the biological brain or the nervous system like a light bulb, right?
*  You flicked on the switch and something happened, but if you flicked it off, nothing happened.
*  But that's clearly not how nervous systems work.
*  There's a lot of spontaneous activity that is in some sense almost as rich as stimulus evoked responses.
*  So how do brains then reconcile sensitivity to subtle inputs and why aren't we hallucinating the whole time?
*  So that's the biological spirit of the question.
*  But we just essentially did a mean field calculation in this idealized random network scenario.
*  And it's a calculation that I'm kind of secretly the most proud of.
*  I wonder if that's a trend that people are most proud of some of their earliest work because often that's the most hard fought as well coming in and not understanding as much and having to work harder just to make anything work or make sense of anything.
*  That's right. I mean, it was also for me the first spark of something having clicked, right?
*  I don't want to, you know, say, oh, scientific discovery and big pooh-wah words, but it was the closest I've experienced that for the first time was when, you know, things just kind of worked that one day.
*  And the feeling I had on the insight.
*  Anything partly also to give credit to our people in our labs that once you have a lab, a lot of the great ideas are coming in concert between you and the people in the lab.
*  Whereas when you're, you know, during your postdoc work, your early faculty work, it's all you.
*  And I think that's partly why I think we feel so connected to that work.
*  Since you mentioned, there's about a thousand questions I want to ask, but maybe I'll start with this.
*  Considering the different roles that you have once you are running a lab versus when you're starting out, how you feel like the nature of your questions have changed over time?
*  Sort of the trajectory of your thinking, you know, have they become more narrow, broader?
*  I know many of you work across many different animal species and how just how you approach the questions that you're interested in.
*  Is there an easy way for you to characterize how that's changed over the course of your careers?
*  It's a great question.
*  And I think that part of what makes you a PI, right, is that you have a certain flavor of questions you like to ask in a certain approach to the way you ask them.
*  But at the same time, we have been living in a decade or two where techniques and machine learning has sort of changed hugely.
*  And so that requires us to continually, you know, sort of shift the way the way we're approaching problems.
*  And for me, that that is really an intimately tied up with with people coming into the lab, you know, who are often because of mirror match and other other experiences, much more deeply trained in in some of the new techniques than I am.
*  And so I'm sort of steering the ship of sort of trying to provide the questions and the taste maybe to to what kinds of things are interesting to ask.
*  And and you go to some extent, hoping that my students are really, really most knowledgeable down in the weeds on some of some of the newer approaches.
*  So you're like the neuromodulator to their smaller network dynamics.
*  I see that totally resonates with me what Adrian just said, the metaphor being the modulator.
*  I definitely have benefited tremendously from students and postdocs in my lab who have a lot of expertise that I definitely do not have.
*  And I'll definitely confess that there have been many papers we've written where I can't tell you the details.
*  Right. Like, I trust that they've been done correctly.
*  We've had people working together on it, but I personally cannot explain to you all the guts of all the derivations.
*  And to some extent, it was just the process of coming to terms with that.
*  That's that's kind of OK in some circumstances.
*  And that's what we have collaborators for.
*  And I feel like increasingly I feel like my role is as a most like a project manager.
*  Like, I figure out what are the problems that should be that should be asked.
*  What are the good questions to ask an overcomplete set?
*  I asked too many questions as I show up to questions, actual to meetings.
*  I ask a lot of questions. Most of them get answered and that's OK.
*  And then and then I figure out, OK, so what's what's the team of people that we need to get to to to attack this using whatever tools are necessary?
*  So do we need to get do we need to hire an electrophysiologist who is an expert in this particular system?
*  Do we need a statistical machine learning person who specializes in this technique, whatever it is, right?
*  And then find the resources, the human resources and also the the computing resources, the experimental resources, whatever it is, and put the team together and just hope that hope that they gel and hope that something really wonderful happens.
*  And so so I think I when it doesn't work, I can't I take the I take blame when it when it works.
*  And wonderfully, I take very little of the credit.
*  It's it's the team working together.
*  I feel like I have very little to add to this this amazing picture that Adrian and Bing have have painted.
*  I so personally, I think I've also been so, yeah, you know, there's like a research proposal that I came to Sinai to start my lab with.
*  Right. There was this mental picture. It starts with a chalk talk.
*  You make yourself a research program. Maybe even your first grant is based on these ideas that think you want to execute on.
*  And then, you know, some of them do go in that direction.
*  But then there were these amazing pivots that, you know, I must confess, I resisted initially.
*  And those pivots are, yes, as painted by Adrian and Bing in their in their picture, driven by the people in that have come to work alongside me in the lab.
*  But also because of experimental colleagues kind of nudging the ship in in in different directions.
*  So, you know, usually we're spark an interesting problem occurs when, you know, you've made somebody has made an experimental observation and you go, oh, gee, I wonder why that is.
*  And then you build up a model and then we talk to the experimentalist who basically tells you in about, you know, five or six months that it takes them to do an experiment optimistically and say, you're completely wrong.
*  And this is completely mad. This is not how any of this works at all.
*  So then very soon you've you know, you have to rewire your model, build a whole other architecture, different framework and a different way of looking at it.
*  And so, you know, I have had projects that have gone in unexpected directions because of of talking to experimentalists alongside my team.
*  And so, you know, an example of that is, you know, working on maladaptive states.
*  So, you know, anyone that knows my work knows that I've worked on essentially I'm a basic scientist, right.
*  I've worked on mechanisms of learning, remembering and deciding in essentially healthy animal models.
*  But, you know, I'm at I'm at a medical school where, you know, translational research is incredibly valued and clinical people as well as experimentalists are, you know, hemorrhaging data in different experiments from animal models of various neuropsychiatric diseases.
*  About which we actually know very, very little. So, yes, there's computational psychiatry as a field, but computational neuroscience itself has not traditionally focused very much on disease mechanisms.
*  So my initial instinct was to say, well, we'll just look at error trial data, right.
*  The ways that animals grew up may have something to do with maladaptive states turns out no, completely, completely wrong.
*  So we threw out a whole bunch of our models because turns out just adding noise to networks doesn't exactly disease make.
*  I could have asked somebody, but, you know, that's how one learns. So, you know, an example.
*  I really love the role that the students and postdocs have to in both bringing new ideas and in in sort of dragging you in your directions.
*  One of my my first rotation students, he was super keen and he's just great. Barry Walker, if some of you might know him.
*  He came to study his rotation over the summer because he was so keen to get going.
*  And I gave him a project connected with the work we'd done analyzing the Hodgkin-Huxley neuron.
*  And so had an idea about how he could extend their model to have kind of multiple time scales of adaptation.
*  And he went away about two weeks later, came back and said, yeah, I tried it doesn't really work, but I saw this great talk, you know, as at Stanford about this technique IMAP.
*  And I think, you know, there's this nonlinear dimensionality reduction technique that I think could be a really interesting way to look at the system.
*  And so often running with that very pressing, actually, because that's exactly what we are using kind of routinely now to analyze all kinds of nonlinear data.
*  So that's the kind of way that that experiences like like this course or a random seminars can help help our students introduce new things into the research program.
*  In that case, it sounds like it was kind of a horizontal direction move, right? Because it was kind of a technique.
*  But often are these getting dragged into different directions helplessly and happily, I suppose?
*  Yeah, that happens to. Yeah, well, sure. Yeah.
*  Yeah, that ends and whatnot. But, you know, over the course of your research career, do you ask more and more narrow questions into the nuances or bigger and bigger questions?
*  Or is it just does it run the gamut in my life?
*  Definitely runs the gamut. You know, so an example of a new new direction that a student brought me into, you know, she she was very interested in development.
*  And I'm terrified of development. Everything's changed. We love change.
*  There's a lot of change. And I really, you know, I hadn't ever done any any real reading into that, but she was fascinated by it.
*  So she went off to Woods Hole. She had been she'd come from cognitive sciences, so didn't really have deep experimental training.
*  She went off to Neurosystems and Behavior or Neurobiology at Woods Hole, learned how to get into a lab, started a new collaboration with someone else, you know, with Bill Moody and in the Biology Department, started working on on a whole new system.
*  We then had three or so papers about that. We've I stand to write grants with Bill Moody and other students kind of come through that that research direction that I would never have initiated without without Rebecca.
*  So it always does seem to come back to the answer to many questions asked these days about what is the right level to study things at?
*  What is the right system to use? The answer is always it depends on your question.
*  So in Neuromatch, one of the things students learn is single neuron activity and modeling dendrites as part of a single neuron and focusing at the single neuron level.
*  And then and then the the dynamical systems approach is like zoomed way out to a larger level.
*  And and I kind of want to get this back to the question of the single neuron doctrine versus population doctrine versus what is the right doctrine we should all be following?
*  And what do we need to be paying more attention to?
*  Because these days, especially with deep learning, it's the poor, lonely single neuron doesn't seem to have a role anymore.
*  It doesn't matter when you get into those cognitive things or does it?
*  What do you guys think?
*  Oh, gosh, what a great question.
*  I'd love to have to ask that we just dropped the word doctrine.
*  I want to get rid of it too.
*  That's why I want to be a doctor there.
*  Can we abolish it, please?
*  Yeah, right.
*  We're done here.
*  No, I never I mean, Kahal's picture about the single neuron was was an idea, right?
*  That their neuron was was a complete information processing unit, which is fine.
*  There was never a claim that that was that everything was built around coding properties of single neurons, rather that they are units of computation that obviously are built into networks.
*  We know that that's always been clear, right?
*  From every drawing that's ever been made of another system.
*  And so I think that it's been fascinating to me how much can be done without worrying about the single neuron.
*  A lot of our work has been zooming in on the details of biophysics using dynamical systems, actually, you know, to make the link between how underlying nonlinear dynamical processes can translate into coding models.
*  And the single neuron is a great, you know, building ground for that because you know everything, right?
*  You know, all the you have the complete conductance based system from which you can start.
*  Whereas when you're working with a biological neural network, at least there's many parameters that you don't know and much higher dimensional.
*  But if one wants to sort of systematically understand how a nonlinear physical system leads to something that looks like a coding model, then the single neuron is a wonderful kind of sandbox for that.
*  And so I, you know, what I think our work on that has shown and that of many, many others is that single neurons are capable of a very interesting, but not infinite, you know, range of computations at the individual neuron level.
*  And I believe that that matters, right? And so, of course, it's possible to and, you know, as Kanaka's work has really beautifully shown, it's possible to show that you can get the firing rates from a particular neuron by a model that works at, you know, at a somewhat more abstracted level, right?
*  You build a network that has you kind of make up the properties of the network and yet you can train all the parameters to do, you know, reproduce the activity of a single neuron.
*  In real life, that's not actually what's going on. Individual neurons are transforming their inputs with very particular rules that depend on the underlying ion channel distributions.
*  And as we learn more about single neuron cell types, right, those rules do vary across different brain areas, across cortex under, you know, four different cell types.
*  That has to matter. It is possible to build models that don't care about that because they're very high dimensional, right? So they can kind of sweep all that under the rug.
*  What I think is important about those rules, one is that we may, it may allow neural systems to do complex computations with fewer units, right, that you have all of this interesting molecular machinery under the hood.
*  And so you turn every neuron into a complex computational element. So maybe, you know, maybe that that makes it simpler in some ways because you have these rich elements.
*  The other piece of that that I think we have to care about is that these are the properties that we can manipulate with drugs or with genetic manipulation.
*  These are the knobs that we have is to influence the way different ion channels work, the way they interact with different kinds of molecules.
*  And so if we're ever going to be able to take our high level models and translate them into treatments or understanding of how drugs interact with the brain, we're going to have to understand those knobs.
*  That's my doctor.
*  I think you did extremely well, Adrian, as usual. I honestly think that, I mean, she, Adrian kind of captured everything that I would have wanted to say on this. I think it's a taste in problems thing, right?
*  I think there's a little bit of our tendency as people with physical sciences backgrounds to look for this one unifying theory that ties everything with a bow.
*  I think that approach may have its misleading. Honestly, what is going to happen is we'll have a bunch of integrative series and models and some collective understanding will emerge from it.
*  And pieces of those theories will include biophysics and all of the richness of individual neurons. And some of them will include much more abstract models, depending on your taste in problems.
*  That would be my take.
*  Do you have hope or optimism, though? So I think that's perfectly fine to have a patchwork of different levels. And often people kind of zone in on one level when they have one question, they think about one level to answer their question at that given level.
*  And maybe you can verbally relate it to some other things. But do you have any optimism that there might be some sort of integrative, I want to say hierarchical structure or principles by which we can have a more holistic across level appreciation of these systems?
*  Or do they really need to be independent levels that we just have to be happy with?
*  I have optimism. I don't know if it's based on anything.
*  I'm optimistic as well.
*  I think I think Adrian brought up about development earlier and I think that's actually a really interesting clue for me. I am like Adrian, I have almost no training in actual developmental biology and I'm also terrified by it.
*  But but I have this feeling that is super duper important because that's what, along with evolution development is what differentiates biological systems from physical systems fundamentally.
*  And so trying to understand the brain as it is a fully formed thing is somewhat of a very incomplete picture because it grew that way.
*  And the plan for which it grew out that way also grew that way over a much longer time frame.
*  And so those are really important constraints in my mind for how we understand it as a whole because you can't have a network of neurons that is incapable of getting to the state it is when it actually does work in the adult animal.
*  And then we're ignoring neurodegeneration as Conica mentioned earlier, right, which is very important part of understanding the system as well.
*  So I don't I don't have a solution, but I think I'm kind of optimistic that that once we can look at the system, not as a as a fully baked thing that works and does a thing that's well characterized.
*  But think about how it got there. Maybe maybe that's a kind of a sideways sideways approach to that question that may be fruitful.
*  I don't know. I think I think there's a definitely a couple of our colleagues are doing really, really cool work in the computational neuroscience of developing nervous systems.
*  And I'm really quite hopeful that that more people will go into that field.
*  Yeah, I mean, development is such a hard problem. I mean, I'm super I mean, I said, I mean, you both kind of confessed to feeling a little bit of a terror to it, right?
*  It's like, oh, my God, everything is changing, right? The hardware is changing, software is changing.
*  Yeah, it was hard enough as it is and is still changing. Right.
*  We're such a long time scale that what do you even do? Right.
*  And the task that the that the network is supposed to be doing is also changing wildly the whole time.
*  But I think it's it's a holy grail problem that the two of you are working on. So so it's kind of amazing.
*  I mean, my attempt at working on something that is longitudinal is looking at learning trajectories.
*  So, you know, take a fully fledged adult animal.
*  And what does it look like when it's naively placed on in the task for the first time and over the process of shaping starts to look a lot like this expert animal.
*  So what happens then? Can we look at state space representations or can we look at behavioral changes over these weeks that it takes animals to learn a task and tell me if, you know, I don't know, a mouse learned in Seattle or a mouse learned in New York.
*  Are those trajectories are different, but the final state of this animal having done the task are identical in both scenarios.
*  So how do you build models that can distinguish these learning trajectories?
*  It's a topic that's of interest to me, but it's nowhere as complex, I imagine, as the development problem that that you two are.
*  I think the question of learning is a really interesting one that comes back to to post questions about the interface between single neurons and networks.
*  I've always been intrigued by a sort of throwaway line at the end of the Bliss and Lomo LTP paper where there's, well, we've characterized this synaptic plus a zero, but there are all kinds of other ways for neurons to be plastic.
*  You can express different numbers of ion channels.
*  And, you know, there's beautiful work by Sascha Gluck and others that show that excitability properties of neurons can change dynamically over time.
*  And of course, homeostasis, you know, lovely work by Gina Trigiano and others.
*  And so I worry sometimes that our classic ideas about about neural network training are missing a lot of really cool stuff that biology can do that, that, you know, may implement totally different kinds of learning roles that operate on much lower timescales or that change
*  excitability in interesting ways. Right. So, you know, not just raise or lower threshold that would be that you could equally map onto a synaptic weight change.
*  And so there there feels like, you know, there are good reasons to keep paying attention to the single neuron level and the cool molecular dynamics of single neurons, because we may, we may realize that there's a whole richness there that we're, you know, neglecting at the moment.
*  I feel like it's I could start an entirely new podcast for hundreds of episodes called throwaway lines, just about lines that were that crop up again X amount of years later that were in some paper that people take as rule.
*  But but then show a very different side of it. Here's a here's a throwaway question.
*  How many years back should we look in the literature to find great ideas that weren't ready for their that were ahead of their time that are now ready to be used from a let's say a computation of the number of neurons that are in the brain.
*  Let's say a computational nurse, you know, different people in different fields have different answers to this question.
*  I mean, didn't one of you just cite Golgi in your talk like work a hall, I think somebody said, go home.
*  I often have started a few talks lately with with a quote about, you know, basically, you know, neurons firing firing in a synchronous way, making those two neural groups being connected and ask people to guess where that came from.
*  And they say, well, you must be happy. In fact, it was William James from the 1890s. Right. So if my husband's been doing a lot of research lately into touring and others.
*  There are so many insightful ideas buried in 1950s papers in the Colick of Pits.
*  These guys really had thought through a huge number of things that we were still rediscovering.
*  So, you know, I don't know whether the most efficient way is to read all the literature and look for interesting things.
*  You know, I think we all do need and people feel bad about this, but I think it's true.
*  We kind of need to discover things for ourselves.
*  I think you most deeply understand something when you figure it out yourself and then, OK, it's often very disappointing to realize that this idea is out there already.
*  You've been scooped or whatever.
*  But that doesn't obviate the value of realizing it uniquely and coming to it through a path of understanding it that you've built up yourself.
*  And so I think the idea of being scooped is just not something we should we should be so distressed about.
*  You've got a you now have a starting point that's a very different basis for discovering new things than if you just read the line in a paper and copied it.
*  I would like to add to that by saying that perhaps we should also be talking to people in maybe related fields or unexpectedly related fields.
*  And, you know, this is, you know, I've had a very sort of traditional, you know, route in science, right?
*  You just wed yourself to the science track. If you were I was raised in India and that's just how it went.
*  So I've never had occasion to study, you know, philosophy of mind, for example, cognitive neuroscience.
*  But in my recent experience, I would say maybe like a year and a half dating back only a year and a half.
*  I figured that this whole bodies of work where they've thought about these deep and to some of you, this may be obvious that they've thought about these deep questions way before we had the technical ability to even think about measuring them.
*  So I think the controversial statement is that philosophers and artists have probably seen farther than we can or have years ago, decades ago.
*  So it's probably diversity of approaches, talking to people from other fields that has that has been like, oh, my God, this brilliant idea wasn't exactly, you know, it was already said by somebody else way back when.
*  But all of that takes a lot of time and effort and people don't have time.
*  I mean, Neuromatch Academy, I know, is intense for people.
*  And this goes back to the idea of being driven by questions and what Adrienne just said about needing to do the work yourself to really get a grasp on things and know have a viewpoint where you can then use that to pivot and think about things in different ways.
*  And it's would you agree that to get so all the work that people are doing in Neuromatch right now, Neuromatch Academy, that's the thing that's worth it is the actual doing it yourself and maybe not feeling like you're progressing, but it's probably the most worthwhile way you can do it.
*  I agree with that.
*  I agree with that. You know, I think that this is why we do courses. This is, you know, you could just download the thing right from your your your model from someone else's paper. And that's a great way to do it.
*  But going through a real course, a real school where you kind of build it up from from the ground up, right, I think is is just very valuable to going forward.
*  Obviously, we're in a, you know, we're in a golden era where so much is now available online. People are so great about sharing their tools and their models and their methods.
*  And that is accelerating science, but just once in a while, maybe at this early phase to to take that deep dive and to build up your background.
*  You know, when when people we have a lot, you know, I teach a lot of summer classes and and we try to make them accessible both to people coming from physics who need to understand.
*  So what's the state of the art in neuroscience and how can I apply these tools in neuroscience, but also people who who came through biology and really want to quickly catch up on the mathematics and the physics that they need.
*  And the regret that we often hear right from from biology people is that they didn't take more math and more physics early on in their career.
*  And it's not because, you know, they need to remember the formula for the quadratic equation or whatever.
*  It's because that practice of just working through problems is what you get in physics.
*  It's not any one thing. It's not a formula or a rule.
*  It's it's the training in studying at the beginning of a problem and working all the way through it that that that background gives you.
*  And so that's that's the hard thing to catch up on.
*  But I think an intense experience like a summer school is kind of the best way you can you can do it.
*  It's like doing an immersion course in language or something like that.
*  You kind of get that accelerated trajectory through it.
*  I agree with everything Adrian said, and I think a related point that I've been thinking about is also the value of the value of repetition,
*  which is another thing that you would get from a more traditional quantitative education as you might get in physics and engineering.
*  So, for example, I I've been teaching for many years a class for undergraduates, which, among other things, I teach them the principal component analysis.
*  So so I teach them what it is.
*  And then I tell them now that you know what it is, you're going to start seeing it everywhere, like literally everywhere.
*  You may not have heard it before, but now that you know what it is, it's going to pop up everywhere.
*  And it's true. Right. So some of it for me is just that that that fluency with talking through the quantitative stuff, the computational stuff,
*  doing enough of it yourself that you then start seeing connections other places.
*  I think the wonderful point that Conica made earlier about talking to people who are in related fields and kind of adjacent fields, I think I completely agree with that.
*  But I think some of the difficulty that I've had in talking to other people in different fields is often just the language,
*  because they may have had a very brilliant idea that it's totally exactly what I've been working on.
*  But we're speaking a different dialect and I just don't understand what they're saying until we can kind of meet somewhere in the middle.
*  And I think I think that's also one thing that I at least I try to be valuable in collaborations of that kind, because I do have, I don't know, kind of a diverse set of training and experiences
*  that even though I am not often or very rarely the often the expert on the thing we're actually doing, I can speak all of the various languages, kind of bring people together.
*  I can tell my experimental colleague, you know, the thing that you want to do is actually called this technical term.
*  And I can go to my mathematician colleagues and say, OK, here is the thing that the biologists really want to do.
*  And I can I can I can write it down for you as an optimization function.
*  Like, can you solve that problem? Yeah, I can totally do that.
*  But the two of them may not have gotten to that point by themselves or at least not as quickly.
*  And so so having some fluency with both, I think is quite valuable and it just takes it takes repetition, takes doing yourself.
*  And I think being a, you know, the world's leading expert on that very specific thing is is great, but not not necessary for for making progress forward, especially as we go forward in neuroscience, where often often there's large teams of people working on it.
*  So not no one individual needs to be a deep, deep expert on every single part of the thing.
*  We can all agree that no one knows what the hell developmental biologists are talking about, right?
*  Their language is just not a it's not understandable.
*  That's the problem, maybe there's words.
*  There's a lot of words.
*  They use words. Yeah.
*  Maybe we can go back to another thing that Adrian mentioned earlier, talking about the potential importance of details at the single neuron level.
*  So it seems to me the trend.
*  Yes, ecologically valid behaviors has become more popular and more important.
*  And there are plenty of models, you know, that are trying to use some of the computations at the at the single neuron level like apical dendrites versus basal dendrites to incorporate those incorporate those into artificial networks.
*  But I would say on the whole, the trend is the importance of biological processes has really gone by the wayside has really decreased over time.
*  Do you agree with that within the computational neuroscience and it's become very computational, very non biological, very stale in in most other ways?
*  Would you agree with that?
*  And would you think that the trend is should be that way?
*  Or Conoco, go ahead.
*  You're just shaking your head.
*  You can just start talking.
*  I don't think I agree.
*  I think that, you know, I think we're actually going the other way.
*  So, you know, we're in this era where we're where experimental colleagues are recording more and more from nervous systems.
*  And we can certainly argue about whether more is necessarily better.
*  But, you know, we have access due to explosive neuro technological developments to larger and larger portions of the nervous system during behaviors in some case, and the ability to record and manipulate at the same time and so forth.
*  Right. So when that first sort of set off, theorists, at least speaking for myself, felt a little bit like we were on a back front, right.
*  Like we were on a back foot.
*  We were building these sort of abstract models at a time when it was valuable, but they couldn't actually be tested because, you know, who's going to record from all of this to know.
*  Now we know, right.
*  There's a lot of structure in these networks in the in the in the even in the very small nervous systems where you can have, you know, highly sampled data samples.
*  Data sets. They're very highly structured. There's very little that actually looks completely random.
*  So, you know, the work that I said that I was kind of secretly the most proud of is actually the thing that is wildly unrealistic.
*  So in some sense, now everybody is pushing for more biological features, even, you know, landmark papers on, you know, the visual architecture must be hierarchical.
*  Therefore, it is a pure, you know, convent or pure deep network.
*  Even those papers have now augmented their findings with, you know, feedback projections with different kinds of cell types with a tighter link to biology.
*  So I don't particularly agree that we're going away from it.
*  Yeah, I feel like Paul is talking about a, you know, more a trend in the community of who's getting, you know, talks and giving talks and getting podcasted and whatever.
*  There definitely has been, I think, a swing towards a style of doing computational neuroscience, which is fitting, fitting RNNs.
*  And that's it's it's a very cool tool and it's very of the moment and it's doing all kinds of great stuff.
*  And they don't think we should, you know, I don't want to critique that either.
*  I think it's a really important piece of our library of possibilities of how to how to go ahead with neuroscience.
*  I think at the same time, there are many people who remain aware and care right about about the role of single neuron properties and want to put them in.
*  And eventually those things will come together.
*  I think that they're that the biophysicists haven't gone away.
*  We haven't forgotten about that.
*  And if anything, it's more that we don't quite yet know how to do it well.
*  And I think that really comes back to the point you raised earlier, Paul, about, you know, how do we do this kind of multi-level modeling?
*  I think we're still struggling for good tools to do that well.
*  And, you know, we we have all this amazing new data from the Allen Institute where they're characterizing single cell, you know, physiological properties.
*  Now we can see where those single cells are in circuits.
*  Now it kind of now the well, you know, the shit is hitting the fan in terms of us having to actually make use of that data.
*  And I think there's a kind of oh, my husband sometimes puts it as, you know, well, you know, the dog caught the car.
*  Now we have to handle it.
*  And I think that is the challenge of the next era is bringing together what everyone said we needed, right?
*  Characterization of a single cell probably what do they all do?
*  Where are they in the neural network?
*  What are the connectivity rules with on the other hand, which are which are very elegant, you know, methods to just fit, you know, train a neural network.
*  You don't even have to take into account any of that.
*  And then you have someone like Kanika who's really kind of at that interface where you could just train your network.
*  But actually, what if you constrain it with some with some real recordings and that we have to keep going along that route?
*  You know, can we now constrain constrain cell types and what you ask how that helps or hinders our ability to fit those models?
*  And so I think one of the downsides, of course, of that is that it gets more and more sort of details.
*  And, you know, when you start to give those talks, people, the eyes kind of glaze over.
*  And so it's it's less easy to sound bite or to or to even do.
*  You know, it's it's a lot becomes a lot more murky exactly how to how to use that information.
*  I think we are hoping, waiting for some cool method or way of thinking about it that lets us do that elegantly and in a way that that doesn't feel like just a slog of parameter, you know, fitting, which maybe that is the way it is.
*  Maybe that is the answer. But those of us coming from physics and other other fields hold out the belief that there is some beautiful way to capture to capture all those those effects and those influences that is straightforward to talk about and not not just an exercise in Brazilian parameters.
*  I mean, a related question to that is, is the actual processes of of life, right?
*  Life is not important to cognition. That's another problem.
*  So metabolic processes unimportant to cognition.
*  All they do is to make the brain more efficient and have been evolutionarily carved to make our brains run on 20 watts.
*  But they're not important for cognition, right?
*  I mean, that's another part of the question is, it's all it used to be all spikes.
*  Now it's all population dynamics.
*  Do we really, you know, thinking about the the multi-level integration is life anywhere in this?
*  So, you know, the NIH has a whole set of I mean, they have a whole entire working group, whole fields of research devoted to, I mean, broadly called multiscale modeling.
*  And they do look at physiological processes and their interface with with with neuronal dynamics as we know it.
*  So, you know, in the spirit of what you're trying to get, I think, at is that we have to have some skepticism in our favorite tools.
*  Right. I mean, you know, I do, you know, I like the fact that I'm fitting RNNs to biological data, but I don't actually believe that, you know, the brain is making, you know, little analog continuous signals or not.
*  They're making actual spikes with all of this rich biophysics underneath it when different cells have different, you know, they have types.
*  Our best idea for a neural modulator is a very slow sine wave.
*  So I think we got to, you know, have a little skepticism.
*  But there are, you know, there's a whole meeting on glial dynamics every few years.
*  I'm old enough to know that every few years there's a cycle.
*  Everybody seems to be super keen on glial.
*  They make an appearance everywhere and then it goes away.
*  Those guys, they're going to go down swinging.
*  They're going to really.
*  Right. And then we forget about them for a while and then they come in.
*  I recently found out that they're chorionic cells on the inside lining of the ventricles in the brain that are, you know, responsible for controlling neural dynamics.
*  Vascular is linked very heavily with dynamics, specifically dopaminergic terminals and so forth.
*  So there's a whole other level.
*  Right. You asked about biophysics and properties of single cells.
*  But at the physiological systems level, there are whole other fields of research that try to get at the two at the link between normal.
*  Yeah, I think that's kind of silly to say that cognition has nothing to do with life.
*  And it's maybe a bit unpopular.
*  But sometimes I like to I like to say that the brain doesn't actually do anything except control muscles.
*  There's no output, really.
*  Sorry, you say you said it's silly to say that cognition has does have something or does not have something to do.
*  I just I don't see how you can possibly dissociate the two dissociate because if you think about why we even have a nervous system in the first place, it's to control our bodies in the real physical world.
*  And also, right. And we're also thinking things we're reading, for example, without a motor output.
*  Right. Like even your internal processes where I get like I know I talked to my cognitive science colleagues and sometimes they get mad at me.
*  But I say it anyway.
*  Like the fact that we have long term memory, the fact that we can we have our internal monologue, we make decisions, we can imagine the futures and plan for the future, stuff like that.
*  Although that is because the size of our bodies and the duration of our lives, let's say a number of decades and how we are like a meter tall lives over a couple of decades.
*  Like in order to function that way in the real world, you have to be able to plan for the future.
*  If you were a plankton size, we wouldn't have a nervous system and plankton don't have sophisticated nervous systems like we do.
*  What about hydro size?
*  Well, I don't know. Let's ask Adrian.
*  They don't seem to have a lot of memory.
*  It's been very elusive to find any kind of learning in Hydra.
*  And so they control their body, but they live in the present.
*  They're a nerve net though. I'm sorry.
*  I love Hydra. I wanted to learn more about it.
*  Yeah, it's just I think part of this is why in my lab's work, we've been drawn more to, for lack of a better term, more tractable systems where we can actually kind of access every part of the system from the sensory inputs to the neural computations and back out to the motor outputs and have a notion of what the biophysical feedback is.
*  Like that entire loop that is life, the thing that I actually do every day.
*  I take sensory inputs, I make some decisions, I do some stuff that has an impact on the world and comes back to me.
*  That whole thing, right?
*  Rather than studying each part of it by itself, trying to put it together.
*  And that's really, really difficult over the over the time scales of minutes, hours, days.
*  But it is possible for relatively accessible sensor motor loops.
*  And so we've done, we've been kind of slowly going in that direction for the reason that I find that personally intellectually satisfying to think about the whole thing as a closed loop system.
*  And parts of it are really detailed biophysics, right?
*  And parts of it are not, where we don't really know what kind of models fit the data.
*  And so we just fit the data however we can.
*  These are more phenomenological models.
*  And so I think there may be an intermediary of these models is just a hodgepodge of phenomenological models that are glued together with biophysical models.
*  And we're just doing the best we can.
*  But with the idea that the whole thing actually is interactive, right?
*  This is an agent and it actually interacts with the world.
*  And so explaining each piece of it by itself, that's very great.
*  I definitely take advantage of a lot of that work.
*  But I find it really satisfying to try to put the whole thing together.
*  Given the popularity of manifolds these days in dynamical systems theories to describe populations of neurons and what they're doing on a lower dimensional scale,
*  do you think that we will eventually be using some sort of law like terms to describe thoughts as we creep closer and closer into cognition?
*  I know Bing only has thoughts about movement and thinking and projecting movements, apparently.
*  But I can see you're thinking and talking with their hands.
*  I'm not denying anything.
*  Okay. All right.
*  Let's back off. Let's back off.
*  No, but you know, do we need because physics, the celebration in physics has been laws and describing things in laws mostly.
*  Although I know that's changing.
*  But do you think that we're headed in that direction or is that even a goal to head in in complex systems?
*  Do we need law like terms and ways of describing thoughts?
*  See, I don't like this either.
*  Sorry. I'm going to be a Debbie Downer on this question, too.
*  I think this word should also go the way of doctrine and dogma.
*  Okay, so I'm going to quote Kaelbling from MIT, Leslie Kaelbling.
*  They said biology is gnarly.
*  And I think I agree with that.
*  I don't think they're I mean, yes, the pursuit of a law is fine and all, but it's sort of like the pursuit of understanding consciousness.
*  It's to me that, you know, there isn't going to be one because biology is gnarly.
*  It isn't it isn't describable, I think, by by any closed loop formula, because even in the smallest nervous system that you can sample as completely as possible, there are many redundant pathways.
*  It might be optimized for a certain behavior, but the roots by which it is optimized are manifold with a different use of the word.
*  Nice.
*  I guess I'm a little confused by the question because the idea of manifolds is just one way of expressing low dimensionality or you know, and that that has to be true.
*  We have billions of neurons, we do a relatively small number of things with them.
*  And so at some level, there has to be a reduction of dimensionality between the activity space of billions of neurons and cognition or behavior.
*  And so, you know, manifolds are one one aspect of that, right?
*  There may be there is some well structured, you know, space in which one can one can see that, but it's going to be infinitely interleaved right there.
*  You change something about the task. It's a slightly different manifold.
*  So what is the most convenient way to think about how low dimensional representation and you know, that's that's a great question.
*  And, you know, what I don't know if that would constitute a law, it just constitutes a better parameterization of the thing that we're studying, which is its neural activity.
*  And so I I'm all for that, right? I think it's a very it's the most appropriate thing we can try to do in neuroscience is to reduce our observations into some space in which we can start to see what the dynamics are doing and what they mean.
*  And that's that's our goal, whether that means that there's a law.
*  I don't think that that's necessary or even even important in a way.
*  Against against doctrines and against laws, I'm seeing the formation of a nice review paper coming.
*  So, you know, this whole week is about like dynamics.
*  Our dynamics is time appreciated enough enough in neuroscience, because this goes back to my I know I'm harping on this, but this computational approach like a Turing machine doesn't doesn't give a damn about time, for instance, right?
*  And it just goes from state to state.
*  And when we talk about states, when we talk about computations and but this recent stretch has been all about time.
*  Do we do we think about time and incorporate it enough into our thinking?
*  We do. And I think that the original way that that some of the field came out kind of swinging against neural coding and everything's different now because we're talking about dynamical systems.
*  Kind of neglected that the fact that your visual neuroscience has been fully aware of time, all not all along if you go all the way back to human these all they neglected time but a spatial temporal receptive fields right is a kernel that has a time dimension.
*  And so I, and so you can take a dynamical system you can re express it in terms of its greens function and then you have its its integral over time.
*  And so I, I've been you, which you can think about as a temporal receptive field and that's certainly from the beginning of my life in neuroscience, I felt like that was the approach I was taught by will be like and others and so it was always a surprise to me that that was framed as such a paradigm shift I feel like we've kind of known that all along.
*  It doesn't mean that everyone is fully on board with that with the issue of time but but I do feel like it's it's deeply rooted in approaches for the last 30 years.
*  Yeah, I would agree with that. I mean cognition is dynamic right things change over time. How could we possibly not. I mean I think we get ourselves in trouble when we take our models super super seriously.
*  That's a little antithetical to the end the whole NeuroMatch Academy.
*  I know I know I know I'm like you know if I write a paper and then I say you know a RNN model of you know pick favorite behavior.
*  But if I say, this is the unifying theory of cognition in the brain, that's, that starts to smell a lot like a lot to me and you know that it's I know I know I'm kind of tying to have your questions together, but it.
*  It goes back to this thing time is a fundamental fundamental piece of, of behaviors and neural processing.
*  I do hope it's not antithetical to to do a match Academy because one thing that we should all understand is that whatever method we're using right now is not the be all and end all you know you can try something you get somewhere, it'll work, but there are going to be other methods that come along that are going to be better so never take your method.
*  There, you know, there's so many great people out there, advancing these tools all the time you know with the help of amazing statisticians that so we're at a we're at a moment in time with respect to to the tools that we're using that will evolve further over time as we figure out better ways to do it and so.
*  And I hope that that's the way that people have always been taught in school, right that that you need to know the the math of how to build tools but the tools themselves are constantly moving their analogies to some extent for me right these models we build their representations and their analogies and their metaphors what for what we're trying to understanding in biological reality.
*  Sometimes I think back to her I heard this this the streamer that that because the most modern technology we have in our in our world are computers and so it's it's and the brain is kind of like you know the most inscrutable of all organs in her bodies and so we make this analogy that all the brain works like computer right and so I often have a lot of.
*  Friends who especially who haven't studied biology much trying to pin me down like well so what is the hardware of the brain and what is the software the brain they must understand in terms of this computer analogy.
*  And I have to explain to them well it's not exactly like that right like that analogy doesn't actually apply if you take it too literally.
*  And then and then back before computers when seam engines was a was the most advanced technology that that we had people had the steam engine allergy of the brains it was all nomatics and and and see you and you know pressure and hydraulics going going from these tools that are inside your brain and so I don't know I don't know what the next one is going to be maybe when when humanity comes up with a with a more advanced technology than computers so that will become I don't know maybe quantum computing I know a lot of people like talking about that I have no opinion on the matter but.
*  It's not a lot of people but.
*  There's non zero people who talks about it but in any case I'm just wondering right looks I don't I can't predict the future technology and I'm wondering by the time that technology.
*  It becomes popular whether we will update our analogy of the brain as well because we still will will not have completely understood it by that point.
*  All right guys I have one more question for you and then we can and then if you have final thoughts we can wrap up if I were back at the beginning of my training I would study or work on blank more and blank less being you have the scrunchiest face right now let's start with you really really thinking about this.
*  I'm scratching my face is actually really difficult.
*  I can give you the stock answer.
*  Blair bail flee Adrian to rescue this particular train also.
*  I am what's a drink and a say with what with what I studied I think you know I started in non-linear dynamical systems you know and and let during my undergraduate to write my undergraduate thesis I reduced a you know height parameter.
*  Dynamical system onto a manifold can you believe and we're ahead of my time right so that that was all incredibly useful then statistical physics was also incredibly useful what I wish I'd taken more seriously in my life.
*  I think the general criticism of the way physics is taught is statistics I took one statistics course in my undergrad I was bored to death they treat they taught it just as you know here's the T test here's the R test they never.
*  Yeah I did cryptic crosswords instead and you know showed up to the test and it was fine and so yeah I would love to learn statistics properly there was one course at the Vizon where I did my my graduate work on some advanced data analysis or just data and we'll leave it advanced just data analysis which was sort of enlightening but.
*  We have courses now at UW and once that Bing teachers when they think it's teachers on on how did I not learn about the PCA in my physics training with that's amazing right and so I would have loved to do statistics properly in my in my training and I think that that sets you up very well for.
*  And I think that that sets you up very well for be able to use machine learning tools you know fluently and to integrate them with a physics way of thinking that's because that's really what I would like to think that my work does so I'd love to have a deeper deeper training in that in that area.
*  I wish there were sabbaticals during grad school right like a year off when you can go do something that is not related to your main thing I would like to have gone back in time and sold my advisor on that particular scheme that I'm going to go off to see me place where let's say Adrian is and learn something completely different.
*  And if if that were the case I would have wanted to learn something about you know, you know, stuff like ecology development, the natural world mathematical ecology has some gorgeous models, including things that walk a lot like our ducks and quack a lot like our ducks, the tools are very very similar.
*  And so that's what I would have liked to do more of.
*  It's funny because that was that was my my entry actually into this with mathematical ecology.
*  I high school I heard a talk from Bob May at this International Science School that I attended as an 11th grader and that that excited me and then I got into chaos because of that.
*  Oh, somehow Adrian's been doing it right the whole time, her entire life.
*  Just had so much luck.
*  I think I have a better answer now having listened to Connika and Adrian's answers.
*  I have very few regrets. I really I really like all the things that I've done and the path which I've taken to doing what I'm doing now. And I think, I think the one thing that I wish I had better training in like actual formal training is actually I have two different answers that are in a totally different direction.
*  One of them is scientific computing. So so not just the mathematics, but the actual implementation.
*  Of course, this is a fast evolving field right like every six months a new the cool new tool comes out and you have to keep up. But there's some foundations there I feel like I never I never quite had the formal training in it.
*  I had just been kind of trying my best to pick it up as I go along and feel always like a little bit behind.
*  Yeah, so I wish I had taken more courses than that. And then on the opposite end, I wish I were better trained. I think Connika mentioned the same thing in developmental and evolutionary biology.
*  Because it's such a foundational thing about trying to study life. And, you know, because, like I mentioned earlier, I think life is not a computer life is life, right.
*  And knowing the evolutionary history of life, the such richness of observations that people have from those fields and I've only recently begun to appreciate it because I happen to sit in an integrative biology department.
*  I have all these colleagues who are paleontologists and developmental biologists. I hear them talk.
*  It's like, oh, why did I, how come I never learned about this? Why did I not know about this? I want to do that. Right.
*  My secret dream is that my confession as a biologist is that I've never done a single hour of field work in my entire life.
*  My ideal field work is that I take my laptop to a coffee shop. That's my field work. And so I've been hinting at all my colleagues that the next time they go out somewhere to collect specimens or something, I don't even care what it is. They need to take me along.
*  You should come and collect hydro with us at Woods Hole.
*  I would love to.
*  That's good.
*  I'm probably competent to do that, hopefully.
*  This is we've covered a lot of ground actually. This has been a lot of fun.
*  Do you guys have any? Did we? Did I leave anything out that you were hoping to talk about or or that you feel might be words of wisdom to those students who are listening and, you know, after this conversation might be even feeling even more overwhelmed because their list just got a lot longer about what they need to learn, etc.
*  I would I would like to pass along a piece of advice that I received from my undergrad research advisor, Grant Jensen.
*  So at the time I was having this conversation with him because I was considering going to grad school. I hadn't even applied yet.
*  And I was like, oh, what do I do? Do I really want to do this? Right.
*  And he told me that that in one's life, one should strive for for for three things.
*  You should pick something that you're good at.
*  You should pick something that that's interesting and you should pick something that's important for the world and that most people succeed in getting approximately two out of three.
*  But if you can find something that's three out of three, then that's what you should do.
*  So I tried to take his advice seriously and I've also tried to pass the advice along, because I think it's a really good way of not be overwhelmed.
*  Right. Because not everyone has to do everything.
*  What's interesting to you is not what's interesting to everyone else.
*  What you're good at is not what everyone else is good at.
*  And even what you consider to be important for the world, that is a matter of taste.
*  What you what you like. But I think that's that's been a piece of advice has come back to my life over and over.
*  And I just want to pass it along to what are you a two or three?
*  On a good day, I think I'm somewhere between a two and a three.
*  OK, yeah, didn't know we could do fractions.
*  I guess the thing I would like to say to mitigate the overwhelmingness, which I understand completely, is that you shouldn't feel starting that you need to know everything and you can do everything.
*  You know, that's certainly not the way my career has gone.
*  You have to do a couple of things and built on those both by, you know, opportunistic.
*  Once you realize that your question is taking you in a certain direction, you learn what you need to know kind of around that thing.
*  And, of course, as everyone has has has emphasized, you collaborate and you get great colleagues and even great students and great postdocs that can help to augment your your own background.
*  And so I think and even the point that you raised about how much of the literature should we go back to?
*  Obviously, you can't have read all the you know, it's why we have Grace Lindsay, right?
*  To surprise that literature for us and and give us a path through it.
*  And so I I feel like the main thing is to deeply engage yourself in a question and a problem that excites you have tools that you know where you can make some initial progress.
*  And then as you go, you can bring in all kinds of other things as you see them, you'll be open and aware and you're a lifelong learner, right?
*  That you need to continue to to keep developing your toolbox and your, you know, your set of mental analogies, let's say.
*  So, you know, that idea that you kind of need to be super highly trained in all areas before you can even make progress is almost the wrong way, because sometimes I think you can know too much.
*  If you know everything, you can talk yourself out.
*  You know, one of the most brilliant guys in my in my graduate school group just continually talked himself out of doing anything because he could kind of see five steps ahead and see where it would go aground and sort of know that's not going to work.
*  That's not going to work.
*  And, you know, I think if you if you're like that, if you're oh, well, maybe someone did something like that already.
*  You are you may not just bound into the problem and try something and then, you know, that's the only way you'll you'll do original work is to really deeply engage and do so anonymously quote one of my mentors.
*  So don't read do.
*  I wouldn't go that far, but you know, that's something there's something to it.
*  Very good.
*  Conor, could you have any parting thoughts?
*  Oh, well, I want to talk to Bing and Adrienne more.
*  I think what they said, I want to, you know, really kind of I don't have anything else to add to that.
*  Thank you, guys.
*  This has been really enjoyable.
*  I think it's been a really worthwhile conversation for people.
*  So thanks.
*  Thanks, love, for having us.
*  Thanks, Paul.
*  Bye bye.
*  Thanks, Paul.
*  Brain inspired is a production of me and you.
*  I don't do advertisements.
*  You can support the show through Patreon for a trifling amount and get access to the full versions of all the episodes.
*  Plus bonus episodes that focus more on the cultural side but still have science.
*  Go to brain inspired dot co and find the red Patreon button there to get in touch with me.
*  Email Paul at brain inspired dot co.
*  The music you hear is by the New Year.
*  Find them at the new year dot net.
*  Thank you for your support.
*  See you next time.
*  Bye.
