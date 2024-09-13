---
Date Generated: September 12, 2024
Transcription Model: whisper medium 20231117
Length: 5532s
Video Keywords: []
Video Views: 418
Video Rating: None
Video Description: Show notes:  https://braininspired.co/podcast/193/

Patreon (full episodes and Discord community): 
https://www.patreon.com/braininspired

Apple podcasts: 
https://itunes.apple.com/us/podcast/brain-inspired/id1428880766?mt=2
Spotify: 
https://open.spotify.com/show/2UZj8c8Ap5oc2gh2rJxLLe

The Transmitter is an online publication that aims to deliver useful information, insights and tools to build bridges across neuroscience and advance research. Visit thetransmitter.org to explore the latest neuroscience news and perspectives, written by journalists and scientists. 

Read more about our partnership: https://www.thetransmitter.org/partners/

Check out this story: 
Monkeys build mental maps to navigate new tasks https://www.thetransmitter.org/cognitive-neuroscience/monkeys-build-mental-maps-to-navigate-new-tasks/

Sign up for the “Brain Inspired” email alerts to be notified every time a new “Brain Inspired” episode is released: https://www.thetransmitter.org/newsletters/ 

To explore more neuroscience news and perspectives, visit thetransmitter.org.

Music by: The New Year: 
http://www.thenewyear.net/

Kim Stachenfeld embodies the original core focus of this podcast, the exploration of the intersection between neuroscience and AI, now commonly known as Neuro-AI. That's because she walks both lines. Kim is a Senior Research Scientist at Google DeepMind, the AI company that sprang from neuroscience principles, and also does research at the Center for Theoretical Neuroscience at Columbia University. She's been using her expertise in modeling, and reinforcement learning, and cognitive maps, for example, to help understand brains and to help improve AI. I've been wanting to have her on for a long time to get her broad perspective on AI and neuroscience.
ble learned simulators.

0:00 - Intro
4:31 - Deepmind's original and current vision
9:53 - AI as tools and models
12:53 - Has AI hindered neuroscience?
17:05 - Deepmind vs academic work balance
20:47 - Is industry better suited to understand brains?
24?42 - Trajectory of Deepmind
27:41 - Kim's trajectory
33:35 - Is the brain a ML entity?
36:12 - Hippocampus
44:12 - Reinforcement learning
51:32 - What does neuroscience need more and less of?
1:02:53 - Neuroscience in a weird place?
1:06:41 - How Kim's questions have changed
1:16:31 - Intelligence and LLMs
1:25:34 - Challenges
---

# BI 193 Kim Stachenfeld Enhancing Neuroscience and AI
**Brain Inspired:** [September 10, 2024](https://www.youtube.com/watch?v=vqNyi5ODw20)
*  Not only is neuroscience inspired AI not really like super what's going on, like science inspired
*  AI is just like still happening and in lots of different areas, but it's...
*  What neural networks do is they have several stages of processing and at each one it's a
*  re-representation of their input. So this question of what information they represented each layer,
*  the neural network gets to figure that out on its own. It's not like you fix it the way we did,
*  but the question of what it does choose to represent has a big effect on what it can do downstream.
*  Neuroscience just has this tremendous like variety and diversity and like eccentricity
*  and stuff and I just love that. This is Brain Inspired powered by the transmitter. Hey everyone,
*  it's Paul. You may have just caught that Brain Inspired is now powered by the transmitter.
*  That's right, I'm excited to announce a major milestone here. Brain Inspired is now a proud
*  partner of the transmitter. So for those of you who haven't heard of it, the transmitter is an
*  online publication that provides information, insights, and tools to help neuroscientists at
*  all career stages stay current and build connections. It's funded by the Simons Foundation, but
*  it is editorially independent. I'm delighted to join their team. So what does this mean?
*  Well, Brain Inspired will stay the same, but I'll be contributing to and collaborating on
*  various new projects in line with the transmitter's mission to spread the word about neuroscience.
*  In fact, you can find this and future episodes on their website, the transmitter.org, where you can
*  also easily sign up for email alerts every time a new Brain Inspired episode is released. Actually,
*  if you visit their newsletter page, which I'll link to in the show notes, you can customize what
*  kinds of neuroscience news and topics and columns that you'll receive in your inbox. And trust me,
*  there's a wide variety of options there. Moving forward, I'll also point to stories that grab my
*  attention. For example, recently I read a summary of a compelling study from Merida Jazieri's lab
*  about how monkeys' brains build mental cognitive maps and use those maps to imagine things that
*  they've never seen. I'll link to that in the show notes as well. So this is really an exciting new
*  partnership between Brain Inspired and the transmitter, and I'm grateful for their support.
*  All right, now today's episode. Kim Stechenfeld embodies the original core focus of this podcast,
*  the exploration of the intersection between neuroscience and AI, now commonly known as
*  neuro-AI. That is because Kim walks both lines. She's a senior research scientist at Google DeepMind,
*  the AI company that's sprang from neuroscience principles, and she also does research at the
*  Center for Theoretical Neuroscience at Columbia University. She has been using her expertise in
*  modeling and reinforcement learning and cognitive maps, for example, to help understand brains and
*  to help improve AI. So I've been wanting to have her on for a long time to get her broad perspective
*  on AI and neuroscience. One of the things that we discuss is the relative roles of industry and
*  academia in pursuing various objectives related to understanding and building cognitive entities.
*  She has studied the hippocampus in her research on reinforcement learning and cognitive maps.
*  So we discuss what the heck the hippocampus does since it seems to be implicated in so many
*  functions and how she thinks of reinforcement learning these days. Most recently, Kim at DeepMind
*  has focused on more practical engineering questions using deep learning models to predict things like
*  chaotic turbulent flows and even to help design things like bridges and airplanes.
*  We don't get into the specifics of that work, so I will link to it in the show notes,
*  but given that I just spoke with Damien Kelty-Steven, who thinks of brains partially
*  as turbulent cascades, Kim and I discuss how her work on modeling turbulence has shaped her
*  thoughts about brains. Okay, so that was a lot, I know, but you can find all the details in the
*  show notes at braininspired.co.uk, slash podcast slash 193. Again, thank you to the transmitter.
*  This is really exciting for me. And thank you to my Patreon supporters for your continued support.
*  Okay, here's Kim. So I moderated a panel that you were on at CoSign,
*  a few, what was it, a month ago, two months ago. I can't keep track of time.
*  And it struck me, you even mentioned at one point that you were saying something in service,
*  not just to be defensive, I think was the quote. And it was about DeepMind and how,
*  so the original mission of DeepMind was to use what we know about the brains to make better AI.
*  And that has sort of gone off the board, right? Because these days, it's just scaling up is the
*  is what AI is all about these days. What I wanted to ask you is, is it fair to say that DeepMind
*  failed? Okay, all right. I don't think so. I mean, I guess so the, I'm not sure. Okay, yeah,
*  I guess there's a couple things. I mean, one, the original characterization of DeepMind's mission,
*  it was like, it was something a bit more circumspect than that. It was like, solve intelligence,
*  here are lots of different directions that we think might be viable. Neuroscience is one
*  direction that that DeepMind had that maybe it was like unique and that other groups didn't.
*  I think one, the neuroscience research projects were always pretty careful to
*  to pick projects that were in a particular like, zone of impact so that it could be like useful
*  to neuroscience and say something useful about neuroscience and had the possibility to say
*  something useful or relevant to machine learning. So the kinds of questions that we focused on
*  were things that we thought had some application to a particular open problem in machine learning,
*  continual learning, robotics, learning rules and optimization in general, structured credit
*  assignment. We kind of picked things that we wanted to learn something about the brain and
*  were also like open problems in machine learning. The other thing is that the other like thing that
*  the neuroscientists did at DeepMind. This is all past tense I've noticing. Go ahead.
*  I mean, a lot has changed in the last year of like machine learning. So the neuroscience team
*  has also like shifted their focus quite a bit or the neuro lab. The other thing is that like
*  neuroscientists at DeepMind were like as Matt Bavenick who headed the neuro team for a long time
*  put it were like bilingual. So they would work on machine learning problems, publish machine
*  learning, NeurIPS papers, also work on neuroscience problems. And part of the benefit of this was
*  thought to be like a more like intellectual or abstract exchange. Like if you're trained in
*  neuroscience, you just have kind of different ways of thinking about problems. And so like a
*  lot of cool stuff came out of the neuroscience team that had really like very little to do with
*  neuroscience. Like a lot of the stuff with graph neural networks and using them for simulation,
*  that was a project I worked on for a while. Pretty tenuous connection to anything to do
*  with neuroscience. But like it was a pure machine learning project. There was a lot of stuff with
*  like concept learning too that was a big focus of the neuroscience team, not directly like paired
*  with a neuroscience investigation project, but just like something that neuroscientists tend to
*  think about. As you mentioned, this is like pretty past tense. And I think the neuroscientists at
*  DeepMind, we've kind of largely been pivoting for a couple reasons. One is that there were in this
*  like as I said in the as I said in that panel, like we're the whole field of machine learning
*  is like very much in a scale up mode right now. It's like build it bigger, build it better,
*  and just like add more data, add more TPUs and try to generate it for longer. Like this is very much
*  the mode. And this is for some good reasons. There's like two papers that I think really like
*  encapsulate this nicely. One was a paper from OpenAI. Now those the guys who wrote it are
*  anthropic, but he was on scaling laws and transformers. And they basically showed you
*  make the model bigger, you add more data, you add more compute, the model will get better
*  predictably. So if you are like looking for a place to turn money into good machine learning
*  models, that's a really reliable knob to turn. Like that's the kind of that's the kind of signal
*  you want. The other paper was a paper from DeepMind showing that emergent properties
*  start becoming apparent as you scale up a model. So this is almost like the opposite. Rather than
*  just like as you add more compute, the model will get better. This will be like as you add more
*  compute, the model doesn't get better until suddenly it does. It's different. Yeah. Yeah,
*  it starts doing different things. Some abilities that used to not have now emerge. So basically
*  like in both ways that are predictable and not predictable. As you add more compute, the model
*  seem to get as you add more compute, more scale, the model seem to get better. So it seems like
*  I mean, it is I'm a researcher. I'm not an engineer. So, you know, well, not my
*  specialty. Well, you majored in chemical engineering, right? That's true. But that
*  doesn't actually come up that much in my day to day. Right. But yeah, I guess this is just to say
*  like I can see why we're in a period that is more about more like that where engineering and
*  increasing scale are having a moment rather than like let's investigate new methods. Let's try to
*  like search broadly and find inspiration from different areas of science and make interdisciplinary
*  connections. Like not only is neuroscience inspired AI not really like super what's going
*  on like science inspired AI is just like still happening and in lots of different areas. But
*  there's a lot to be gained from scale right now. There's a lot to be gained just for making things
*  better. So it's just not really like the pendulum has swung a bit. Oh, no, we the pendulum again.
*  This came up in the panel as well. I made one of these comments like I stopped everything. I was
*  like the pendulum metaphor because it makes it feel like it's coming back. Yeah. The good
*  news for neuroscience though is there's just there's a lot to be done there. Like the I think that's
*  the other thing is there's just like a lot of good opportunities for applying data. Like this is a
*  this is a moment for data driven methods as a tool. But they're tools, right? They're not
*  necessarily models of the system. And I know like people like Jim DeCarlo and
*  you know, David Zasillo, there's a lot of people using them as models. But
*  yeah, but what I'm hearing you say is that it's it's all tools. I think they're both. I think
*  they're really both. And you can like kind of interpolate in between. So like one one aspect
*  is to just use them for tools. Say like here's a method for getting patterns out of data that's
*  complicated and hard to understand. The brain and behavior is filled with complicated data that's
*  hard to understand. If we train models, maybe we can predict it well. Maybe we can summarize it
*  well. Maybe we can like decompose it into some form that is a little bit more that from which
*  humans can grok patterns. That's like one opportunity is just try to summarize. And
*  that's having a moment. Like there's a lot of methods that people have been working with,
*  like Mackenzie Mathis has like awesome work just like summarizing behavior. Ben Zalevsky, like
*  that summarizing behavior is would be like that's that's on the tool side. And it's really like
*  expands what you can do. But I think on the models of the brain side, it's also pretty useful
*  because even if a model if you train a model to do something, there's many ways you can structure
*  it. And they they kind of trade off interpretability and messiness in a nice way. Like for instance,
*  if you train the same big messy black box model with different optimization algorithms,
*  you get different representational properties that emerge. If you have different objectives on
*  a deep neural network, you can say something systematic about what's happening inside of the
*  representations. And this forces us to think a little bit more about like, what features are
*  happening? What kinds of cognitive operations are happening implicitly in a big messy deep neural
*  network? Like rather than structuring something is like, this is the module that does search,
*  and this is the module that does reinforcement learning. If you're like, we trained a big model
*  to do all sorts of stuff, and we're still looking for those cognitive functions, but we're trying to
*  pull them out of implicit operations rather than structuring them deliberately. I think it's
*  probably a useful perspective and still counts as like model driven research. It's just that like,
*  the specific variable that we're modulating is really is related through a messier system.
*  So this is something that like that, that we've been thinking about a lot is like, if we're
*  thinking about how to use neural networks to comprise models of the brain, there are certain
*  problems that only arise when you have a neural network system, or there's certain ways that you
*  can combine structure and expressiveness and get in this sweet spot where you are getting something
*  out of the neural network, but also not completely foregoing any ability to say something structured.
*  Mm-hmm. One of the things, and I'm not going to just focus on the panel that I moderated, but
*  I was revisiting it. And one of the things I asked was whether any of the panelists thought that AI
*  has actually hurt neuroscience in any way, and then no one answered. And then you were kind enough to,
*  you sort of, you couched it in a different answer that someone else asked a question,
*  and you were kind enough to at least address the question that I asked. And you mentioned
*  something about biological plausibility or non-plausibility biologically.
*  And I think that's interesting because, and I want you to expand on that a little bit because I
*  thought one of the lessons here, and this goes to what you were just talking about, was that
*  biological plausibility doesn't matter. And so it was odd to hear you say that non-biological,
*  biological non-plausibility, non-biological plausibility, whatever it was, that that was
*  in some way how AI has maybe dampened neuroscience or hurt it. Am I making sense?
*  It's funny because I was like, I'm like, my research is not like a paragon of biological
*  plausibility like that. I know. Well, I know. Yeah. And we'll talk, because turbulence.
*  Yeah. Yeah. I mean, I think the, I guess, I don't know. I mean, I think that there is a
*  level of abstraction that models bring. Yeah, I say I think, but I guess this is a common
*  framing principle when thinking about model-driven neuroscience is like, all models are wrong, some
*  models are useful. And exactly what you're trying to say about the system is, and whether or not
*  your claims are justified depends on the level of abstraction you're using. So for instance,
*  if I say like, this effect appears to be driven by the statistics of data, and I think that it is
*  indifferent to which particular learning algorithm you used, then I can say, well, we used a
*  biologically implausible one because we wanted to get the system actually working at the level
*  where it could reason about these kinds of statistics. We couldn't do that with a biologically
*  plausible one. So we did it that way. Somebody could say like, well, I don't agree with your
*  claim that this is irrelevant to the biological implementation details. Like that could make a
*  really huge difference. And then I would have like said something really misleading. And I think the
*  reason that occurred to me in that panel is because that's just like what I worry about a lot is I
*  focus on a particular level of abstraction and have tried to say things that are justified at
*  that level about how the statistics are having an effect, what kinds of computations are supported
*  by different kinds of representations in a kind of specific implementation agnostic way. But those
*  details could really like trickle up and matter. And then I would be saying things that are wrong,
*  which of course nobody wants to do. So I think that that's kind of the, I don't think that it's
*  like, I don't know, for instance, that we have been critically led astray by that. That wasn't
*  necessarily my instinct, but it would be, that's the risk is that like you work at this level
*  and you were led astray because it didn't obey some constraints, which turn out to really make
*  a big difference. I will say though that like there's two levels of biological constraints
*  at some level. There's the implementation details, but then there's the behavioral level.
*  And one thing is the models that relax the behavioral constraints, the advantage of them
*  is that they have an easier time getting this behavioral level, or at least that's ideally the
*  justifying case to use them. So it's not always totally fair to say they're like biologically
*  unrealistic because they are pinning to one aspect that you know the biological system is doing,
*  which is doing a good job at some naturalistic behavior. So I'm not like the first to make that
*  point, but I think that is like they kind of it's almost like they pin to different levels of
*  biological plausibility and no model gets both of them rather than saying like we don't care about
*  the biology at all. So you're like, I don't know if are you half Columbia, half deep mind? What is
*  the fraction? So I am officially, yeah, basically I'm there one day. I'm at Columbia one day a week
*  officially. I sometimes go up on Fridays too because Google is hybrid, but I'm usually there
*  Mondays. And yeah, my official appointment is adjunct associate professor. So it has like a
*  lot of asterisks next to the professor. But yeah, I mean, I'm up there some fraction of the time and
*  then I'm at deep mind the rest of the time. So I do a little academic stuff, a little industry stuff.
*  But the reason why I'm why I asked that is because I'm curious,
*  A, what's more fun? And B, how much time do you spend these days thinking about neuroscience
*  versus applications like modeling turbulence and design? Yeah, I mean, they're both tremendously
*  fun. That's like a boring answer. But they, yeah, they're both really fun. They're fun in different
*  ways. I do the Columbia stuff, at least the way I have it structured because I'm part time is more
*  advising on projects. That's, that's fun because there's like, there can be tremendous variety.
*  There's because you can work on more stuff when it's students or postdocs who are driving the
*  projects. Those projects also tend to mostly be more neuroscience focused, or theory focused.
*  There'll be some of the projects are more, how does the brain do this? Or here's a neural network,
*  it's doing something kind of like the brain. Does that actually compare? Some are more actually
*  analyzing data that's come out of other labs. And some one in particular is more, it's kind of a
*  machine learning project, but it's a more theoretical and conceptual one. In general, like the kinds of
*  stuff that is maybe a bit easier to do in academia, not just possible to do in either place,
*  but but actually easier in academia is things that are with smaller models and that are maybe a
*  little bit more conceptual. Because Google just like toy like toy problems. Yeah, kind of toy,
*  yeah, I think. Yeah, exactly. Things that are a bit more toy or don't at least don't require you
*  to train a gigantic model. You can do stuff with gigantic models that somebody else trained, but
*  like, you don't want to necessarily be in the business of training a huge model. That's not
*  easier to do in academia, at least. The kinds of projects that are fun to do at Google are largely
*  things that benefit more from from scale that have some kind of, like you can use a really big
*  model, you can train a big model to do a different thing. You can really experiment with some of the
*  more conceptual stuff at large scales. This is coming up in the context of I've been working
*  recently on some projects with with memory with retrieval augmented generation. And there are some
*  neuroscience versions of this, you know, we think about hippocampal contributions to learning
*  all the time is like, what what is memory adding to a process? How and and maybe making hypotheses
*  about when you should see different kinds of hippocampal activity, different kinds, different
*  levels of activity, different styles of activity. That's a neuroscience question. And you can often
*  ask that with somewhat toy models, you can get abstract versions of that problem that you can
*  look at in similar systems. Whereas at DeepMind, you can play around with like a large language
*  model retrieving from Wikipedia. And that's not impossible to look at in academia, but it's harder.
*  And it's there's infrastructure and it's, it's, it's nice to be able to play around with the same
*  kind of concepts, but at a scale where it's naturalistic and complex. I remember I was
*  riding in the car with my father, I think I was in graduate school actually for neuroscience, and
*  he asked me or suggested that perhaps industry is better suited to quote unquote, he didn't use the
*  the term solve intelligence, but you know, to understand brains and stuff. I mean, what,
*  how, what is your perspective on this? And I think he made a very good point. Of course,
*  it hurt a little bit because I was in graduate school. But, but you know, he was like an IBM guy
*  and and I think he made a pretty good point. And I'm curious where you fall on that. Should
*  industry just solve neuro? I that's funny. I would be curious to ask you more about what your dad's
*  like, pros and cons were for academia and industry. Well, okay, I can tell you real quick.
*  That I mean, basically just that we academics are like super slow. And you know, there isn't like a
*  bottom line to get done, right? Because it's an endless search, right? So in industry, there's a
*  thing that you are setting out to accomplish. And I think that's part of it. And academics are just
*  slow. Yeah, I mean, academics, I guess, like, researchers in general are pretty motivated.
*  So I think the like, if it's moving, I think it's more like an industry. Because it's not like,
*  you know, people are pulling longer hours in industry because they're getting paid more.
*  No, and they're happier. They go home earlier and they're happier, it seems.
*  I think the I think the difference is like the because of this sort of like, goal collapse in a
*  way. There are like, like that there's a that there's a financial bottom line or that there's
*  like an incentive that sort of aligning people, you get more people working on the same thing,
*  and you have things that are broken into projects. I basically think industry. Yeah, I mean, I'm not
*  an economist. So whatever take this with some grain of salt. But my sense of it is that industry,
*  if there's a if industry is well poised to work on a problem, if a problem does align with the goals
*  of a company, it's great to have it to have that happen. Like there is an alignment of people who
*  are getting funding, and they're going to work on the problem. And they'll break it down into parts
*  that that that will like, be followed up on tightly with different kinds of like, progress
*  management criteria. Like, I think a lot of those things work really well. The question is, of
*  course, just like, is there an alignment of objectives? I think basically when there is,
*  then it's great to have the problem pursued in industry. If there isn't like some problems are
*  really in some sense, there isn't necessarily there's not an obvious financial motive to
*  understand how the brain works, except in so much as you could design pharmaceuticals to help it or
*  base technology on it or something. It's these very sideways scant views of it. So I think the
*  benefit of academia is like, it you have, you have more, like smaller groups of independent
*  researchers all trying their own thing. It's not like a bunch of people are going to lock in and
*  run in the same direction with with quite as much ease. But you but the goal that people have is
*  just the actual can be the same goal as understanding the brain, it doesn't kind of have to align in
*  these sideways ways. So I think that's sort of the the pros and cons, like when industry does it,
*  awesome, we should be delighted. We shouldn't like, you know, I don't I don't worry like,
*  Oh, no, if industry does it, how will academia compete? I'm like, Oh, there's still plenty of
*  things to do that aren't necessarily on the path to making better technology or better pharmaceuticals.
*  And we, and we really, I we don't have, I think, an alternative to academic research to moving in
*  those directions. Well, I wish I wish my dad was around to see the course that deep mind has taken,
*  just to circle it back, because incentives change when companies get bought and pivot is a euphemism
*  that we can use, right. And then all of a sudden, you're not trying to solve intelligence, you're
*  scaling up and, and I mean, I don't know how deep mind works. But, but I'm curious what he would
*  actually think about the trajectory of deep mind. Yeah, I mean, this is what people have said this,
*  for, oh, I mean, this, I guess, was what happened with Bell Labs, right, as they did basic research
*  for a while. And then, you know, there was some reorganization, they kind of pivoted,
*  deep mind still does a ton of basic research, but the, the nature of it, and they do a ton of
*  things that are just like the goal of them is to contribute a high impact scientific result,
*  always has been. Yeah, yeah. And I think that has not like that hasn't stopped being true,
*  or like stopped being a big part of the way that they like brand themselves, we brand ourselves.
*  And I think that the, that is something that makes it a little bit that that adds a little
*  bit more complexity to the story about like, what can industry do? What can academia do,
*  then just like profit motive alignment, because that is very, it's not, it's not profit irrelevant,
*  like doing good, doing things that are positive contributions to the world are good for a company
*  to do their the company does benefit from that. It's not just like if you can product make a
*  product out of it, then it's beneficial to your company. And otherwise it isn't. So it does make
*  it really, it makes it a little bit more complicated. But the, but and yeah, I think deep mind still
*  kind of does do a lot of these things. But you, you, you do have to like, appreciate that a
*  company has different goals. I mean, funding can be fickle in its ways, too. It's not like anyone is
*  totally immune to this. But yeah, it definitely everyone kind of warns about industry research,
*  like as things about the company change, the research will change too. And that's true of
*  grants. And that's true as well. But the time scale is potentially shorter. And universities
*  have been around for a long time. Would you rather have a beer with an academic or an industry
*  person? Oh, it depends. There's huge variability. Come on, you can't wiggle out of that one. Of
*  course. No, I, yeah, I've had I've had excellent beers with industry and academic people.
*  I don't know. One thing I really like about neuroscience departments is that there is a
*  lot of variety and discipline. Like when I was in graduate school, my roommate, Diana Liao, she
*  studied marmoset, how like marmosets talk to each other. That was really cool. None of my colleagues
*  at DeepMind study how marmosets talk to each other. That's like neuroscience just has this
*  tremendous like variety and diversity and like eccentricity and stuff. And I just love that.
*  So that is a point in favor of having a beer with not least neuroscientists. But it kind of gets away
*  from the more controversial question I think you wanted me to answer, which is like, who's objectively
*  more interesting? Yes, let's be objective about it. So I'm curious, you know,
*  I don't know how your interests have changed, but I know that your projects have changed over time.
*  Right. So you've I alluded to some of the work that you've done modeling simulations for turbulence,
*  for design, are those things that you pick? Are they mandated? How have your interests and you're
*  still doing lots of, you know, interesting cognitive map, reinforcement learning,
*  neuroscience stuff. But how would you characterize your own shifting interests?
*  Yeah, I think the so when I was, what I started off working on in graduate school was like
*  computational models of hippocampal contributions to learning. So basically,
*  Oh, you were right into hippocampus immediately.
*  That's what you. Yeah, that was I think that was actually built on like a rotation project I did
*  with Matt Bob and Sam Gershman. So really like right off the bat. So in the kinds of
*  computational models I was working on then that we were working on for that project
*  were things that more had to do with tabular reinforcement learning and linear algebra,
*  which is to say like, they were models where we could set up the math analytically and like compute
*  exactly what we were doing. And we weren't training neural networks to do stuff.
*  We the motivation was neural network. It was like that we want to understand how a certain
*  representation in the brain supports the downstream computation that's happening. So if you
*  represent the world that you're there's different choices you have for how you're going to represent
*  your experience and the way you represent it will support different kinds of computations down the
*  line. For instance, like a kind of simple example would be if you want to tell the difference,
*  if you have a downstream task that requires you to tell the difference between different colors,
*  you need to have a representation that is not grayscale that has color in it.
*  So our work with the hippocampus was about like how representations in hippocampus seem to account
*  for what's going to happen next that they form representations such that different states that
*  are going to the same place end up with similar representations. And if you group things by what
*  outcome they predict, that makes it easier to do certain computations down the line,
*  computations that implicitly need to know something about what's going to happen next.
*  So it was kind of a neural networky motivation because what neural networks do is they have
*  several stages of processing and at each one it's a re-representation of their input. So this
*  question of what information they represented each layer, the neural network gets to figure that out
*  on its own. It's not like you fix it the way we did, but the question of what it does choose to
*  represent has a big effect on what it can do downstream. So the motivation was this like
*  representation learning question, but the method wasn't. After I graduated, I was at DeepMind.
*  I wanted to do something with neural networks. I wanted to learn what those were all about.
*  Also, I had these kind of concepts that I feel like I was working on in certain ways that were
*  tractable and let you really chew them up and understand every aspect of them. But I wanted to
*  see what would happen if we stuck neural networks on them and made them work that way. So at that
*  point, I- Wait, wait, wait. I'm sorry to interrupt you, but what percentage of neuroscientists do
*  you think had that same thought? Like, well, we have this thing, now I just want to stick a
*  neural network on it and see what happens. I bet a lot. I'm not sure. Yeah. I mean,
*  people, it's definitely an aesthetic preference and I think some trial and error is required to see
*  if you like it or not. I definitely have talked to some researchers who say they, sometimes they work,
*  do some work with neural networks, some works without and say they just prefer working with
*  them because they feel like it's working at scale and some say they like working without it
*  because they feel like they don't know what's going on and they want to cut into science to
*  think about stuff and empirically observing is often what you're- I mean, there's exceptions to
*  this, but a lot of neural network research becomes a little bit empirical and observational.
*  So yeah, I think a lot. Also, I think it's just a great- It's a very good skill to learn. So I
*  think a lot of people just want to play with a neural network because it makes them feel safer
*  in their long-term prospects, which is very logical. I certainly felt that way at DeepMind.
*  I was like, a lot of people, a lot more people doing neural networks here than linear algebra.
*  Like, it's time- Oh, interesting. Yeah. Oh, sorry, I interrupted your-
*  No, no, no, not at all. It's a great question. Yeah. So I mean, it was kind of the closest path
*  to looking at the same kinds of principles we were thinking about, like how the brain represents
*  relations between things, how the brain makes predictions about what's coming next, was to work
*  on Pete Battaglia's group where they were using graph neural networks, which are a neural network
*  architecture that reasons about relations between things and using them to make predictions about
*  how a physical system will unfold. So basically, if you have a physical system with a bunch of
*  interacting entities, like things bumping into each other or fluid particles bouncing into each
*  other, that's a relational system. Interactions between those particles determine what's going to
*  happen. It's also a predictive problem. You're trying to see what's going to happen next.
*  So that's how I got there. It was sort of like the kind of nearest neighbor research manifestation
*  of these relational and predictive ideas, but in a machine learning form, in a machine learning
*  application. So do you view the brain as a machine learning entity? Broadly speaking,
*  I mean, I guess at some literal level, I guess I view the brain as a learning entity and not a
*  machine, I guess by definition. But machine learning, I think, is kind of the extent to which the brain
*  is a thing that learns stuff. Machines that learn stuff are a good batch of machine-related
*  analogies for that, if that makes sense. Yeah, yeah. Sure. I'll accept that.
*  Basically, yeah. I think machine learning is a really great batch of tools for thinking about
*  how learning works. And yeah, I think there's just so many concepts in common between
*  understanding how machine learning works, understanding how the brain works, building
*  better machine learning models, understanding why different brains are the way they are.
*  But you see the brain as a learning entity. Yeah.
*  Primarily. Yeah. I mean, that's at least the aspect that I study and find most interesting.
*  I think the whole nature versus nurture, I don't have a super creative opinion on that. But I
*  guess the extent to which the brain is a learning thing is probably the extent to which machine
*  learning is a good batch of models for it. Okay. Yeah.
*  So yeah, you have worked a lot on the hippocampus. And there was a guest speaker that came. I'm at
*  Carnegie Mellon University, and there's a guest speaker that I had lunch with. And he does work
*  with hippocampus stuff. And I realized, maybe I hadn't thought of it before, but the hippocampus
*  has been sort of the darling of neuroscience now since place cells probably, right? Since
*  that became popular. Would you say that's right? Yeah, I would. I mean, I was around back then,
*  but I definitely got that sense. I was warned when I started hippocampus stuff, people were like,
*  it's a crowded field. Good luck in there. Oh, really? Yeah.
*  I thought visual neuroscience was a crowded field, but I guess hippocampus took it.
*  Yeah. I mean, hippocampus is crowded. Vision is crowded. RL is crowded. I don't know. A
*  lot of the good stuff. Oh, yeah. These days, RL, do you feel that it's crowded? Because
*  I'm tired of seeing algorithms, new algorithms. I'm like, oh, I got to learn another one.
*  I work on hippocampal contributions to RL. So I guess there's some part of me that just
*  thinks objectively RL and hippocampus are the most interesting and could never be too crowded.
*  But yeah, I mean, they're definitely real popular.
*  What does hippocampus do? What does hippocampus do? It seems to help with memory, maybe some kind
*  of structure learning. You're good. You're good at wiggling out of questions like this.
*  Okay. But you know, I mean, so there's the learning aspect.
*  I'm not trying to. I'm just also trying not to say things that are wrong.
*  Well, yeah. When you're someone like me, you get used to that real quickly. And I'm fine being
*  wrong. But you know, I mean, it's memory, it's learning, it's spatial cognition, it's a cognitive
*  map. Is it all of these things? I mean, do we need to say hippocampus does function X?
*  Yeah, I mean, it's definitely it does a lot of it. It seems like it is implicated in a large
*  number of things. And yeah, I think there's people joke like, people make fun of hippocampus
*  researchers and say that they think that the cortex is just to keep the hippocampus warm.
*  I haven't heard that one. That's pretty good.
*  Yeah, I mean, you know, it's, it's obviously not doing like everything in the world. I think,
*  I mean, there seems like hippocampus is unique in certain ways that do justify its supposed
*  ubiquity. Like it gets projections from all over the brain, it seems like it's processing lots of
*  different kinds of information. So it's not going to be specialized on like a particular sensory
*  modality. It seems like there are some things about it that are different from other areas,
*  like in particular, like it seems like it's capable of really rapid learning. I think the
*  complementary learning systems idea makes a kind of specific but non specific prediction about
*  hippocampus. Let me just say what that complementary learning systems is real quick. So the idea is
*  that you learn quickly and rapidly in the hippocampus, and then it sort of transfers over
*  time. And what is the word I'm looking for consolidates, right? Is that right? Yeah,
*  in the cortex over time. So hippocampus keeps sending this learned information to cortex and
*  cortex over time consolidates the information. So there are two kind of learning systems. Did
*  I say that right? Yeah, that's I mean, at least. Yeah, that's that's by that's why I take the and
*  that kind of that decomposition of roles is leaves a lot of stuff for hippocampus to do it's saying
*  like what it's specialized in is is rapid acquisition and memory for specifics. And that
*  should relate to all these other things like rapidly learning about spatial environments and
*  where things are stored in them. rapidly acquiring new episodic memories, remembering, preserving
*  specific aspects of memories from which you don't want to generalize. Like maybe you are the classic
*  example is like the difference between where you usually park your car would be more a cortex job
*  and where you parked your car today would be a more hippocampus job. It's something specific,
*  you might change this over time, but you don't want to forget that information. It's useful to
*  preserve the and then also like this, the ability to form new memories should interact with the
*  statistical memories you formed the the kind of like structural memories you formed in a pretty
*  deep way because the a new thing you want to learn is maybe a reconfiguration of old statistics.
*  It's if I today put a coffee cup on on a bench, I have a concept of bench, I have a concept of
*  coffee cup, those are probably statistically learned properties, but the specific conjunction of them
*  is something that's like, that's new. So the that hippocampus is rapid learning should interface
*  with slower learning isn't necessarily a contradiction, but it does make it easier to
*  to just kind of have this explosion of roles where hippocampus is doing all of these things
*  when actually we should really be thinking about it more in terms of how hippocampus is
*  interfacing with other areas that are all partially doing these things.
*  I feel like so what you know you mentioned reinforcement learning, you've done a lot of
*  work in reinforcement learning and I mentioned the idea of cognitive maps a moment ago
*  and you know I mentioned how hippocampus has been the darling and all of these things are wrapped
*  together right and since then there's just been an explosion of algorithms reinforcement learning.
*  You've worked with successor representation learning etc. Model based, model free.
*  What is your perspective? I mean it's out of control isn't it?
*  I think it's nice. I think that the yeah it would be
*  it'd be good to get everyone on the same page I guess. What does that mean?
*  You want model comparison. I guess this is something that you want to see like what one
*  model does that another model doesn't do necessarily. So I think a lot of the yeah so maybe
*  a risk of like proliferation of different models is if you aren't comparing the models on the same
*  data or if you aren't comparing models at all you're just saying look this model captures this
*  picture that's in the paper this other model captures this other picture that was in a paper
*  and you don't necessarily compare them all together. So one thing that people are doing
*  this with hippocampus a little bit there's some toolboxes that people have been developing.
*  I know Rat in a Box is one of them and then by Tom George at UCL. Clementine Domine has one that
*  I'm blanking on the name of but that's also at UCL. I mean basically these things that are trying
*  to take lots of models and make try to make the same predictions of them. Brain score is a nice
*  example of this in the visual world and there's like there's issues with making things too score
*  based and too benchmark based but it has benefits that like all people are talking about the same
*  data and not just saying like this model captures this one aspect this other model captures this
*  other aspect assuming that the brain could just put both together and have it work just as well
*  or not necessarily arbitrating when the models are mutually exclusive. That yeah I mean that's
*  just an important thing to have. On the other hand I think like good yeah I mean I almost see
*  that massive proliferation as a success of the RL account rather than a warning that if you make
*  a model that's somewhat right that's doing kind of a simplistic RL thing then a bunch of other
*  models will come that make that do more nuanced versions of that or more particular versions of
*  that. A multiplexed RL, distributional RL, action prediction error, regularized RL like you know
*  all these kinds of things that add nuance to the picture. If the original RL thing was totally
*  wrong this would be a really bad use of effort but if the original RL thing is a bit right but
*  not capturing everything that's kind of worked pretty well. It's like you have a sort of
*  coarse simpler picture and that got you into the vicinity where people can bubble around making
*  different models and seeing which aspects you can capture and then try to consolidate them.
*  I think I remember you saying in one of your talks maybe I don't remember exactly the way you
*  phrased it but you used to think that reinforcement learning or at least like model-free reinforcement
*  learning was like hey you did something good but now you think it's like oh this is the
*  worst way to how did you phrase it? I don't know what you're talking about.
*  So I use an example when I'm giving RL lectures on what makes reinforcement learning different
*  from other types of learning and it's commonly cruel. I think cruel is the word. I used the
*  word cruel. I think reinforcement learning is a little bit cruel. I think of it as almost very
*  passive aggressive and the example I have of this is if you were taking a, if you were trying
*  to learn biology, one way you might try to learn biology is read a lot of textbooks and try to find
*  patterns and link things across different bits of the text and group all of the things that have to
*  do with the mitochondria and recognize like I don't know causal structures from mitochondria
*  producing energy to enzymes that use that energy to build stuff or whatever. Like you try to
*  identify structure and that's what unsupervised learning is all about is it's a large and kind of
*  amorphous field and it's all about trying to learn patterns and structure. Supervised learning is
*  much more limited in its scope. That is the setting where you have a, there exists a correct answer,
*  there's a right answer and you are trying to find that answer. You can set it up as classification
*  problems or regression problems. You have a picture of something, a human labeled it, a picture of a
*  dog and you are trying to train a network to say this is a dog. If it didn't get, if it guessed that
*  it was a cat, the answer it gets is no, this was a dog. It doesn't just get like an answer like
*  10 points or six points or minus 11 points without any context for how many points are possible or
*  whether there was like more points available with some other answer. That latter one is what
*  reinforcement learning does is learn biology by taking tests and then just getting like a score
*  of 34 and not knowing if it was out of 34 or 8 million or if, you know, exactly which answers
*  you got wrong and which answers you got right. It's just kind of a, it's a very like restrained
*  signal. So it's nice for setting up the problem of autonomous learning. If you can learn from signals
*  like that, then you are pretty good at figuring stuff out on your own. You don't need the
*  handholding of supervised learning. But it I think also highlights the challenges of it. Like you,
*  the credit assignment problem is really hard. You have to figure out which things contributed
*  to your points and which things didn't. The exploration problem is really hard. You have
*  to figure out how many points were available to you where you'd have taken different options.
*  So yeah, I think of reinforcement learning as somewhat cruel rather than this like, oh,
*  you did a good job. You get a treat, which I think I used to conceptualize it as a very like
*  gentle warm way to nurture an agent. So why do we, why do we, why do our brains employ
*  such cruel, passive aggressive algorithms? Well, it's very, it's very flexible. So you can,
*  you can learn lots of different types of things. And it's much more autonomous. Like you, you don't
*  need information to be labeled for you. If you don't have, if you don't have labeled information,
*  you don't really have a choice. So the other thing is like, there's a lot of ways,
*  there's ways to make reinforcement learning easier. And a lot of the research that I've
*  worked on has been about how, how to do that, how hippocampus might specifically help by doing that
*  by, by, by combining unsupervised learning with reinforcement learning, basically by
*  learning some structure so that you can strain the reinforcement learning problem to a narrower
*  set of possibilities or give it some hints about what kinds of, what kinds of things might be
*  driving the number of points. Basically read a textbook and then take a test and see how many
*  points you get rather than just taking the test and hoping that like a billion tests will eventually
*  teach you biology. Where, where is model based reinforcement learning these days? My sense is
*  that, so I travel in, you know, particular bubbles, right? Like we all do, but my sense is that
*  the tide turned to everything is model based reinforcement learning at the pendulum, let's
*  say. And that pendulum has kind of swung back and said, well, maybe very little is like, you actually
*  don't need model based to do a lot of these things. And so maybe we're sort of overstepping our bounds
*  in thinking of everything as model based. Is that accurate at all? Well, it's interesting. I mean,
*  a lot of the huge tide in machine learning recently has been this, the, the, the, the rise
*  of self-supervised learning to the, to the extent that it's, it's, it's sidelined reinforcement
*  learning to a large degree. I think there used to be a lot more appetite for like, let's try to learn
*  as much as we can with reinforcement learning and we'll rely on self-supervised learning when we need
*  a bit of a crutch. Now self-supervised or unsupervised learning, they mean really similar things. Basically,
*  it turns out that gets you very, very far. Like if you just train a model to do next step prediction,
*  you're like on, on words, that's how language models are trained. You're very close to being
*  able to not just predict the next word, but make the next word be something that you actually want
*  it to be. And so I think that is actually very, it's a little bit different from some ways of
*  conceptualizing model-based learning, but it's very similar to others. It's basically like you're
*  using a predictive model to start off the process and then you coax it to do exactly what you want,
*  which is very much the, I think, key concept of model-based learning. Most model-based
*  reinforcement learning, or at least like most that I was kind of familiar with, or the cartoon I had
*  in my mind of model-based reinforcement learning is tree search. So you have a model that can do,
*  simulate different things, you simulate different outcomes, and you see what happens, and then you
*  pick the action that leads to the best possible things. But model-based reinforcement learning
*  can be structured in other ways too. It could be, for instance, like learning concepts about the
*  world, learning some model of like these things are all the same and are going to behave the same
*  way. And then when you learn about their value with model-free reinforcement learning, you've
*  done some sort of vaguely model-based organization of them that supports it.
*  That's sort of what the successor representation does it more that way, that you represent things
*  in terms of the predictive structure and then the model-free reinforcement learning that happens on
*  top of that automatically takes into account some features that a model-based model would have
*  told it about. Yeah, there's other ways that people kind of use these self-supervised models
*  in conjunction with reinforcement learning. So it's a little bit of a different take,
*  but I think it's still the same concepts shuffled around in a different way.
*  Shifting gears, I was going to ask you, I was going to sort of segue into cognitive maps. I'm
*  not sure. Yeah, I'll just shift gears actually and ask you, and one of the questions that I sent you
*  was what do you think neuroscience needs more and less of? I mean, forgive me, someone who works at
*  DeepMind, right, in industry, I think has a unique perspective perhaps on these things. And so I'm
*  genuinely curious from your perspective if you think that you have a perspective that might be
*  unique relative to a normal academic like myself, right? Can you see neuroscience sort of from the
*  outside? I know you're still inside it also, but you're also outside it. And do you have a take on
*  this? Yeah, it's funny. I really struggled with that question. It's an unfair question.
*  I feel like it's a very fair question. I mean, at some level, every part of picking a research
*  problem is trying to figure out what the neuroscience world needs more of that you are equipped to do.
*  The, yeah, I mean, and I also, I guess the kinds of things that I wrote down that I tried to
*  brainstorm about this were- Wow, you put effort into it. I put effort into this,
*  which is extra embarrassing because I don't know if I have a brain. Oh, I'm so thankful for it.
*  Yeah, I mean, I think that the thing that I thought maybe like I might have a bit of a,
*  like some unique insight on or that like the DeepMind perspective relates to
*  is the extent to which we can build pretty sophisticated models of really complicated
*  processes. Like the basic revolution in machine learning recently or the thing that we have
*  increasingly been showing our ability to do is that we can learn really complicated functions.
*  With enough data, the sky's kind of the limit to like how complicated a thing you can learn.
*  So learning predictive models is definitely something we can do. I think there's a lot of
*  appetite for this, for building predictive models of neural data, of behavior, building foundation
*  models that integrate lots of different data. And the question that arises from this is like,
*  what do we do with that? If we distill a black box system into another black box system,
*  what do we do? Was that useful? What is that useful for? And I think like even on its own,
*  that is a useful thing to know how much systematicity there might be in the data,
*  how much is predictable, how much a model changes when you add new data, what kind of counts as
*  surprising based on the data you've had at the time. So like even these kind of black box
*  predictive models, I think could be really useful. There's some other ways I think that we can make
*  them more useful if we combine the deep learning model with a model that has a little bit more
*  structure, a little bit more interpretability. This has been a really big theme for the
*  NeuroLab at DeepMind recently. Folks like Maria Eckstein and Kevin Miller have done some nice work
*  on this recently. And I've been thinking a little bit about how to relate the learned physics
*  dynamic stuff to this if we were to apply the same kind of techniques to biological data.
*  And I think basically like while the revolution in machine learning was very much about building
*  good predictive models, we haven't done quite as much work on building predictive models that are
*  also constrained to be interpretable or constrained to interface with existing models that we've built
*  that we know how to say structured things about. But that's not really something that's
*  fundamentally ruled out. I don't think we have to consider these models 100% black box. And I think
*  thinking about how to combine really complex models with some structure, either by including
*  it as an architectural prior that you know something about or interfacing the model with
*  knowledge or interfacing the large black box model with some prior that takes into account
*  structure that could be hypothesized. I think that that's a really useful direction for
*  neuroscientists to be thinking about, particularly neuroscientists who have an interest in building
*  large scale models and access to doing that. So trying to come up with something that's in between
*  super complex predictive, we're just going to build it all and pretend that that was enough
*  just to imitate the system. And this more like we only care about exactly what we can build in a very
*  tractable way. If we can interface between those levels, I think that would be really powerful.
*  And it would also open up the ability to compare models to data in a much richer way. If we can say
*  this is the behavior that should be happening at the level of this video of an animal, because we've
*  combined the model with something that actually generates low level behavior, that would be a much
*  stricter way of comparing to neural data and behavioral data than it would be to just say
*  this shows on average an increase or we see this gross statistical effect on average, but it's not
*  capturing every specific eccentricity of the behavior. So yeah, I think the integration
*  between structure and data is the big thing. Okay. So is it fair to give the crude summary
*  that neuroscience needs more interpretability on top of the big models?
*  Yeah, broadly speaking, or maybe that the dichotomy between interpretability and data driven is maybe a
*  little... It's too Tarsha dichotomy. We shouldn't be fighting if we want models that are predictive
*  or if we want models that are interpretable. We all want both and we should just try to see
*  think of this more as a Pareto frontier and that has a more complex trade-off.
*  What about... Did you take any notes on the question what neuroscience needs less of?
*  I hope you didn't work too hard on these things, by the way.
*  I just jotted down some notes. I wrote specifically, I don't know if I really have an opinion on that.
*  Honestly, I couldn't think of anything creative here. Yeah, I don't know. I think
*  one thing I notice in my own research is that when I am targeting a journal paper versus a
*  NeurIPS paper, I have a different... It is easier to do something a little bit bite-size or more
*  incremental or I don't know. With a NeurIPS or with a...
*  NeurIPS. Yeah. It's easier to be like, we capture this one thing, trust me, it's wrong. Whereas,
*  when I'm thinking about writing journal articles, it's like we really need to convince people
*  broadly in a really different way. The goal of a journal paper, I think is to...
*  Tell a story. Yeah. Tell a story and talk to... I feel like it's much more about talking to
*  neuroscientists and saying, I think this is right. Do you believe me? Or I think this has something
*  to offer. Can I convince you that that's true? Whereas with... I wouldn't say we need less NeurIPS
*  papers, but I think if we just started only doing NeurIPS papers and not writing in that
*  more journalistic style, it might be a bit of a loss. On the other hand, the general review
*  process is way overbearing and unnecessary and I don't hold for-profit journals and everything
*  about open reviews I have a lot of respect for. There's pros and cons to both models,
*  but I think that specific aspect of writing with an idea of impacting the field rather than writing
*  with the idea of scoring a win and getting a NeurIPS paper in is probably more scientifically
*  minded. But there's something nice about the honesty of the, let's say the NeurIPS, we'll just
*  call it the NeurIPS method, right? Because you don't have to change the world. You can just
*  do something that's incremental. You don't have to claim that you're solving something that no one
*  has ever... There's just a lot of over claiming in the storytelling in journal papers. When I think
*  about writing a journal paper, I think, all right, how can I trick them into thinking that my stuff
*  is important, right? That's funny. I might just have such a different model of journal reviewers
*  versus... Because I think that NeurIPS papers over... I think of them as the worst for the over
*  claiming. Oh, really? You know what? Maybe it's just safer to say that they over claim in different
*  ways. I think the thing I find frustrating about... And I think that's actually probably pretty
*  accurate. There's an incentive to over claim about how broadly your model captures results
*  in a neuroscience paper. There's an attempt to over claim about how novel your method is
*  with a machine learning paper. So a lot of... I think the most frustrating thing about machine
*  learning papers is that there's just this incentive towards what I call a categorical geometry.
*  You want to say, here, we made a model. It is completely different from all of the other
*  models. It is itself just... There's no frame of reference in other models. It's a unique point
*  on the landscape. It's new and we made it. And it's a new method and it's innovative and it's novel.
*  I promise you, the method is new. We compare to other models, which themselves are their own
*  little points on the landscape. And our model does better than them. And you're not really looking
*  like, well, does your model have the same thing as this other model at some level and a different
*  thing at this other level? How is this similar to other stuff? In other fields, like I assume
*  math, but I'm not a mathematician and I like neuroscience. I think you get more points for
*  being integrative. You get more impact if you can say how things relate to other things rather than
*  just saying, this is maximally unrelated to other things. And so I think that makes it really
*  extra work to understand principles about what's working and what isn't working in machine learning.
*  S2 So you would rather have a beer with a neuroscientist than a machine learning
*  industry researcher. S2 You didn't ask that. You asked academic or industry.
*  S2 I know, but I'm changing the question. But it sounds like-
*  S2 I'm not gonna have that one either. But yeah, I mean, I definitely just, well, the thing is,
*  at some level, okay, at some level, I'd rather have a beer with a machine learning person,
*  because the only way to really figure out how a model is related to another model is to have a
*  beer with them, because it's not gonna be in the paper. S2 Oh, wow. A little backhanded
*  compliment, perhaps. S2 Yeah, I'm not sure. But yeah, no, I think that they're both super
*  interesting fields. If I could have picked a single one, I would have done it. But yeah,
*  I think it is true that the kind of behind the scenes talking does fill in a lot with machine
*  learning papers, because you kind of learn how they thought of the idea in the first place.
*  This is true of neuroscience at some level, though. You talk to people and they're like,
*  yeah, this data we feel really sure about. This data was technically significant, but we feel a
*  little shakier about it. There's always a lot to be learned from actually talking to people.
*  S2 Neuroscience feels like it's in a- So in one respect, it's in an awesome place,
*  because we have more compute, more data, more models, more everything. But it's also,
*  it feels like we don't quite yet know what to do with all of the stuff. And there's a lot of
*  exploratory work. What I'm doing right now, it's like, well, we're going to throw all the tools at
*  it that are around, because we don't really know what to do with the data. Does that ring true to
*  you? Yeah, that does ring true to me. Okay. What does that mean? How do we get beyond a weird spot,
*  just a bunch of brilliant people that make the right advances? I mean, I think of it,
*  I think of it, at the very least, I think that's a feature of neuroscience that's useful for
*  recruitment, because it makes it an exciting time to be in neuroscience. You're not just like,
*  figuring out, you're not just like kind of answering specific questions, you're figuring
*  out what are the right questions to ask and what's the right way to describe them.
*  Yeah, that's the hard stuff. Yeah, yeah, that's-
*  And the fun stuff. Yeah. And a lot of people don't like that. They're like, I feel like I spent
*  five years doing a PhD, and I have no idea if the, even the question I answered will be relevant
*  years, let alone the specific answer to it. And I think that, yeah, that's a personality difference,
*  I guess, about risk profiles and what kinds of thoughts you want to have. But I think the fact
*  that it's philosophical is that at some level, we're not really sure how to even be saying things
*  is really interesting. And yeah, I mean, the aspect of the black box machine learning
*  predictive models versus more structured models is a really nice example of that. Is that a
*  philosophical choice about which direction to go? Are there ways to combine the best of both? What
*  would that look like? That kind of just, maybe there's more structured ways to do it. Maybe
*  there is a right yes or no answer. At some level, it feels like it's a bit of an empirical question.
*  Try different stuff and see what works. And what works is itself a really hard thing to evaluate.
*  What are you going for? If you're just going for prediction, then of course the models that just do
*  prediction are going to win. If you're going for insight, that is pretty hard to optimize for. And
*  it's really hard to take gradients through it. So yeah, I think there's a lot of exactly how to
*  operationalize what it means to understand something and make progress on a question. Have a model that
*  makes progress is really tricky. The RL model, as you mentioned, we have this RL model and then
*  there was an explosion of things. You could argue that that was a win for the model in that it opened
*  up a lot more research. And on a longer time scale, I guess we'll know if that research
*  was useful or not. But I'm not sure how we'll actually be able to use that to restructure the
*  models we're asking. Yeah. You just made me realize that it happens too frequently on my commute
*  to work, like on the train. I'll just be sitting there and then I'll think, oh God, what is my
*  question? Because that's the important thing, right? It's like to have the good
*  questions. And I was like, oh, do I have a question? Oh no. Yeah, no, I don't know. I mean,
*  I feel that way. I feel that way a lot. I put off for a really long time writing my bio for my
*  Columbia page. In fact, I think I still have not written my bio for my Columbia page because I was
*  like, oh my God, a one summary sentence of my research. That sounds like a job for tomorrow,
*  that is really hard. Well, how have your, this is again, a very difficult question, I'm sure, but
*  can you articulate how your questions have changed the nature of your questions,
*  if not the content of the questions over the course of your career? Yeah, I think one big one,
*  so I think I originally was kind of motivated. One of the things that shaped some aspect of
*  my research trajectory was in college, I took this philosophy course with Dan Dennett that was on AI,
*  it was called Language in Mind. And one of the thought experiments he raised was this idea of a
*  robot firefighter and what it would take to design a robot firefighter. And he kind of just jotted
*  down all of these competing things that the robot would have to figure out how to reason about at
*  the same time. It would have to figure out how to search a building, whether to make these
*  complicated decisions about whether it should be looking for people or if it should be taking the
*  people it found out of the building, like these high level goal questions, while at the same time
*  also like putting one robot foot in front of the other and actually moving in a direction.
*  We end up parsing this or like triaging this hierarchy of decisions and that allows us to
*  function in the world and there's like some kind of organization to behavior and finding it
*  is an interesting problem, is kind of the way to study the brain. And a lot of the projects I
*  thought about and things I worked on relied on these explicit hierarchies, like how do you,
*  like what should the high level and the low level be? I think one thing I have-
*  Wait, wait, so what you're saying is you came into it because of that or you were influenced by that
*  into thinking in terms of hierarchies? Is that what you're-
*  Yeah.
*  Okay.
*  Yeah. Yeah. That's a pithier way of putting it. Yeah. I was very thinking explicitly about
*  hierarchies. And I think one thing I sort of moved on was exactly like when and where to think about
*  hierarchies being useful or necessary, that a lot of times if you train a model that is really,
*  that is a big model that is trained to do something like next step prediction,
*  it can do some of those things implicitly. You don't necessarily need to hard code those things
*  or like the places you thought you would need to hard code them, you don't necessarily. It turned
*  out like I felt like I had all these projects where I was like, this obviously will need hierarchy.
*  And then it was like, well, actually just a neural network doing kind of simple stuff
*  or trained in a simple way is a pretty tough baseline to beat. So it's not necessarily like
*  that hierarchy isn't useful. I think it just often is emergent or kind of implicit in the system.
*  And I think a lot of the ways I shifted to thinking about hierarchy were instead of just thinking
*  about how to put it into a system, which I still do and I think is still useful in certain settings
*  for like getting better generalization stuff. It's not like that's not useful. But thinking about
*  when it's useful, I took for granted that it was obviously useful a lot of the time. And now I think
*  of it as something that you need to think a lot more carefully about when the data tells you enough
*  to generalize, when you actually need hierarchy to reason more efficiently or to make a broader
*  inference. The other thing is I kind of shifted to thinking like, well, how does this hierarchy,
*  if this what appears to be a hierarchical ability is emergent, how can we understand how that is
*  unfolding in a neural network? Like really shifting to it as an evaluation rather than a method.
*  If the behavior is happening, can we understand it? So I think thinking a little bit more
*  like how things, yeah, thinking more implicitly about how structure and generalization emerges
*  was maybe a little bit of a soft trend in my research. Has modern AI shifted the way that
*  you've thought about that as well? I know that you're impressed with large language models,
*  foundation models. I've heard you say that, but of course everybody is, right? But I think I
*  remember you saying that that has sort of shifted the way that you think about intelligence or
*  brains perhaps. Yeah, I mean, I think they're, I mean, I'm definitely, yeah, I think large
*  language models are good. That's not the world's hottest take. The fact that they can get as far as
*  they can with next step prediction is pretty fantastic to me. It reminds me of, maybe it
*  should have been more predictable because it reminds me of this thing that was observed a
*  really long time ago with HM that supposedly if you just kind of had a conversation with him,
*  he didn't seem that, oh, sorry, I should say, yeah, for people-
*  I was going to do it. That's okay. You want me to do it? HM was the most famous
*  patient in history in the neuroscience world because he, I don't know how he lost his
*  hippocampus. Was it a stroke? No, it was surgery. They took it out.
*  Oh, that's right. Epilepsy, they removed it. They removed a large swath of his hippocampus
*  and some surrounding tissue as well. And he had all these, he had retrograde amnesia. Is
*  that what it's called? Yeah. So he couldn't remember anything moving forward.
*  Yeah. Enterograde? I don't remember. He had amnesia.
*  I should definitely know this. It was the one where he could remember stuff before the surgery,
*  like a few days before the surgery, but he couldn't form new memories.
*  Neither of us know what it's called. That's embarrassing, isn't it?
*  Yeah. We have both of our hippocampi as far as I know.
*  I know. We also have computers in front of us too.
*  I know. I'm worried your listeners will hear me typing if I look it up.
*  Let's just fix this. Let's fix this immediately here. Surgically, enterograde.
*  Cool. Okay. I'm glad we checked. All fixed.
*  Enterograde, I totally suspected. Yeah. So he had both of his hippocampi surgically removed
*  and a little bit of OFC too, I think, and lost the ability to form new episodic memories. Basically,
*  he lost the ability to form most memories besides slowly acquired complex motor control tasks.
*  But supposedly, if you had a conversation with him, he didn't seem that different. You would
*  think that it would be the ability to form new memories would manifest pretty immediately in a
*  conversation. Instead, it would be like if you were just having a conversation with him about
*  the weather, what was going on, or something that didn't require accessing old memories,
*  he would sound pretty normal. It was really specifically tasks that require
*  things we think of as hippocampal functions where the deficits would show up.
*  Why is that surprising to you though?
*  The reason it is... I mean, maybe it shouldn't be surprising. I guess I just think that memory
*  informs so much of our ability to have conversations. When you're talking about
*  new things, it feels like you're searching your memory for the thing to say next. If you
*  say something that reminds me of something that I heard, and then we talk about that for a while,
*  it feels like a process where you keep diving and scooping up memories and sticking them into the
*  conversation. Maybe his conversations were a little bit boring or something and didn't do that,
*  or maybe... I don't know. That's, I guess, harder to write a paper about. But I think the reason I
*  found it surprising is just because it feels like memory informs what you're going to say next in a
*  very recognizable way. Maybe that's just the wrong instinct, but it seems like actually you
*  can continue in a conversation saying pretty complex things without obviously seeming that
*  different unless you're asked pretty specific questions. That's, I think, how I now interpret
*  retroactively this surprise about predictive models that they're going to do a pretty good job
*  predicting what's going to happen next in a sentence. Only on really specific questions
*  about factuality or things that specifically go against the statistics of your experience,
*  specific reasoning questions, will you see something that's obviously wrong. You can get
*  pretty far on just next step prediction. That, I think, is maybe a neuroscience thing that should
*  have made something not surprising, that was surprising to be not surprising by historical
*  context. So you think it's all about prediction? I think prediction can get you really far. I
*  kind of think, yeah, I think prediction can get you really far. Yeah, it's hard to rule out other
*  things. There's certainly things that are not just prediction, I think. Especially in hippocampus,
*  we had a model of how hippocampus represents predictive structure. There's a lot of retrospective
*  structure that it represents too. If you came from different places but are going the same place
*  next, hippocampus will be different based on where you came from. It represents information about
*  your past as well. Keeping information around about the past and the future seems like it's
*  important. But yeah, I think prediction can get you really far. Do you think you have a better
*  understanding of now as opposed to, I don't know, whatever, five, six years ago, of what intelligence
*  is? I think I have a worse understanding than I did. Really? Yeah, I guess I feel like this,
*  I kind of had in mind, yeah, I guess I thought of it as something maybe a little bit more
*  structured. Now I'm maybe less sure. I guess maybe a large enough neural network trained on
*  complex enough data, the fact that it could eventually imitate something that looks basically
*  like language comprehension maybe shouldn't have been surprising because we just know that neural
*  networks are universal function approximators. They can get any function, even a really complicated
*  one. I think I probably had different intuitions based on just nothing in particular but my own
*  intuitions about what would be required to make that work efficiently and what we would have
*  capacity for. I think I kind of maybe felt like more structure would be required to make as much
*  progress as has been made. What do you mean structure? What, like, I'm trying to... Yeah,
*  I mean like explicit decompositions. Like, this is a category, this is another category, their
*  operation is constrained in some explicit way. Yeah, I think that I might have felt like, I think
*  I had an instinct for us needing some aspect of that. Yeah, I mean, I think one thing that's
*  really interesting about transformers as the model that is currently reigning supreme is they
*  are a very, they're very beautiful architecture. Like, they have this deep symmetry built into them
*  that processes sequences in a really different way from how people previously thought sequences
*  should be processed efficiently, which is to say they just look at everything in their recent
*  context. And instead of saying things that happened a long time ago are going to get
*  processed differently from the model, they're going to have been processed more times because
*  you have to keep applying a recurrent neural network that keeps updating itself based on new
*  information. You just say like, we're just going to have all of the information we have in recent
*  history and we're going to label it by its position in the sequence. But every point in that sequence,
*  every entity in that sequence is going to go through exactly the same processing pipeline.
*  You're going to have the same weights that look at every token in that sequence. And only the label
*  on that token that tells you where in the sequence it is, tells you information about the sequential
*  structure. So you could basically scramble up the sequence and as long as you kept the labels the
*  same, the model would do the exact same thing. And that I think is really cool. It's a really
*  fundamentally relational structure. It's at a very low level. It's saying like, we're going to let
*  we're going to process all relationships between entities in our sequence with the same kind of
*  general purpose relational operation. And you can tell us if you are nearby in a sequence or far
*  away in a sequence, you can tell us what features you have. And as layers of processing happen,
*  you can update these tokens with whatever the model has kind of processed about them, but it's
*  still doing the same relational mechanism. It has a deep connection to these models,
*  graph nets that we work with a lot for physics that fundamentally represent predictions about
*  a system in terms of relations between its entities. So I think there's been a lot of work on
*  relational reasoning as a powerful mechanism for computation. And I kind of hypothesize,
*  although not entirely sure how I would test this, that that operation is really
*  a powerful one that is partly giving the model some kind of computational object that it can
*  implicitly sort of arrange relational operations into. But what does that does that tell us anything
*  about brains? Sorry, this is a naive question, but, you know, we don't get labeled sequence
*  information with it through our senses, right? So is it? Well, the brain might go out of its way
*  to label them. So that's that's I think one hypothesis that's related to cognitive maps,
*  which you mentioned, I think one, one, the hypothesis about place cells and time cells
*  and hippocampus is that they are they're learning to label incoming information with a spatiotemporal
*  tag, which then could could be like a useful attribute to have on some kind of information.
*  If you want to index it by space and time, that could be really useful. I think one thing that's
*  useful about transformers is they, they they structure sequence prediction, they structure
*  memory as like an attention as a problem of attending over your past. I think that's a cool
*  way to think about how you might use memories rather than just like recalling the thing that
*  is the most similar to your current situation, loading that into memory and then reasoning
*  accordingly. It's a much more flexible and directed process. It's saying like, you can choose
*  which things in your past you're going to attend to and and and use to inform your current
*  decision. It's really like a more it's kind of a more flexible take on on something like temporal
*  context model where you have like the where you are in a sequence informs how you label and retrieve
*  entities that you remember. But instead of having like a just an exponentially decaying factor, you
*  have a weight on it that you can learn something that you can like more flexibly modulate to relate
*  your past to your present. So I think this model class is useful for expressing questions in that
*  form. Like, when how could we attend to our memories in a way that's a little bit like,
*  like that we now know how to train but is a little bit different and richer than what previous models
*  are doing while still relating to those models. There's a lot of questions about biological
*  plausibility, but that's true for all the neural networks that we currently reason about.
*  The with with trans. Who cares? Who cares about biological plausibility, though? Really? I mean,
*  if it's if it's working, it's working, right? Yeah, I guess if it's, I mean, it depends if it's
*  working to do to like explain how the brain works, or if it's working to Yeah, to be good at
*  that's a different question. Right, right. Yeah. If it's explaining stuff, you couldn't explain
*  otherwise. Like, I think that kind of that kind of counts as working. But yeah, I guess the key
*  biological implausibility of transformers is like, how would you keep all those tokens around?
*  Yeah, yeah, I don't. I know that. I don't keep. I'm almost I'm close to a gym. In that respect.
*  I don't have. Yeah, I'm not exceptional for my memory either.
*  How long are transformers going to be the thing? I don't know. State space models are are getting
*  getting some attention. I think they they're also they have a property in common with transformers,
*  which is that they train you can make them you can train them really efficiently on by like
*  parallelizing over hardware. So I think the key kind of innovation with transformers was like,
*  yes, in some sense, it's less efficient, because you're just representing all of your memory,
*  rather than like, we representing it in the way an LSTM does with a shared batch of parameters.
*  However, you can, you can parallelize the operations that you're training a matrix on. So
*  even though you have way more parameters, you can efficiently train them on way more data. So it's
*  actually like, kind of nice. And state space models to I think have a they're a rearrangement
*  of RNNs that allow parallelization to happen a lot more easily. They just like, at least my Yeah,
*  that's that's essentially my understanding. So I think the architectures that lend themselves to
*  parallelization will that that that's a really big advantage if you've got lots of data and lots of
*  hardware. I don't know if they'll be the I don't know how long they'll be the chosen model. I mean,
*  once they training a big model is really expensive. So once you train a big model,
*  there's a real switch cost. Oh, yeah. That's not stopping anyone. Yeah, I guess there's a lot of
*  money in it. Yeah, I think that's the that's that's the thing is there's a there's a lot of money in
*  getting a good one. And there's, but it's really expensive to train a big one. So I think the
*  proof the the burden of proof to say like, you should switch your model, or you, you know,
*  or you should train a second model just to see if it's as good as a little guy. But like, yeah,
*  definitely. There's a lot of upsides. So there's, there's, there's, if you've, if you're a big tech
*  company, and you've got money to burn on really good AI, there's probably incentives to do it.
*  All right, Kim, I won't keep you too much longer. I have basically two more questions to ask you.
*  One is, is there something that is like, you are currently struggling with just beyond your reach?
*  Is there something that that is as gnawing at you? I mean, definitely, if we the relationship
*  between predictive models and structured models, that's that's gnawing at me. I feel like there's
*  opportunities there. But I, so I'm kind of like, yeah, I guess something that really annoys you and
*  something that's like good research motivation has a lot of overlap. But that feels like there
*  should be something there. And I find that really exciting. Yeah, I think that that's probably been
*  the major thing that is like gnawing at me at the interface of neuroscience and AI.
*  I mentioned your work on turbulence a few times, and it struck me actually. So
*  I just had someone on who thinks of the brain as a kind of system of cascade turbulence.
*  And so he like uses multifractality and principles from turbulence to think of our cognition. And I
*  thought, well, here's a stupid question I could ask Kim, that did your work on the learn simulators
*  for turbulence? Did that shape at all? How you think about brain processing? Yeah, I'm so glad
*  you asked that also is a thing that is gnawing at me. So one is this idea that we should be able to
*  use the same kind of models that we train to capture physics systems, should also be able to
*  capture biological systems too and neural data and where that's a good model and where that can show
*  us stuff is also just something that's been gnawing at me. And it's the same kind of question. It's
*  like, if we build a predictive model with this predictive, with this kind of structure built into
*  it, when is that structure the right fit for different kinds of problems in neuroscience and
*  also in biology? I think like one kind of one structure that's built into like the graph nets
*  and the convolution nets that we used for fluid modeling is that they have this repetition.
*  Just the way convolutional neural networks, what they do is they learn about a little patch of an
*  image and then they repeat that pattern, that filter for extracting features everywhere in the
*  image. And if, for instance, you learn something that's kind of an eyeball detector, then it'll
*  go through your image and wherever there's something that looks kind of eye-like, it'll pass that on
*  to the next layer of processing. Graph neural networks do the same kind of thing, but instead
*  of looking at patches of an image, they look at patches of a network, like a little neighborhood,
*  and then extract rules about like, maybe if there's a bunch of particles that are crashing into each
*  other in that window, they learn that there's going to be a collision, kinds of feature
*  extractions like that. And this seems like a really cool model for fitting data in the brain. If you
*  want to say like, what is a, if you want to kind of try to fit a model of how the brain's connective
*  structure is giving rise to different computations, or how like the structure of different brain areas
*  relates to different dynamics, this seems like it could be a useful model to apply. The main kind
*  of risk of it is that the way that they share and repeat their pattern, understanding when that isn't
*  or is a good fit for neural data is kind of complicated, because the brain isn't actually
*  constrained to literally repeat itself at every point. However, a model that does repeat itself
*  can be a useful way for saying we're going to say take the same kind of model and apply it to
*  different motifs across the brain and say like, and try to capture within the same model
*  why, like different circuits that happen to be arising in different ways. Basically say we're
*  going to take a model that reasons about local graph structures in general, and then says which
*  one applies here, or can reason about what would happen if you like set up the graph structure in
*  a different way, because it's learning general principles about the local structure rather than
*  like letting every part of the brain learn its own eccentric structure. The idea of like learning
*  a general model of connectivity and then trying to apply it everywhere and make the data tell you
*  how it needs to differentiate itself in order for the model to make the right predictions
*  seems like it could be really powerful. I don't know if that made complete sense, but that is
*  something that has been wrong with me. Well, I was thinking that's the like cortical columns
*  fit that right. Yeah, exactly. Cortical columns are, yeah, and I think one of the things these
*  models do really nicely is you can train them on a small system and then generalize to a large system.
*  So you can train the models on like a small window of fluid interactions and then generalize it to
*  a much larger one because you're just learning these little local operations and you can arrange
*  them into different global patterns without breaking anything, without taking a lot of
*  distribution. So it's scale-free in that respect. Yeah, exactly. And that's like this ability to
*  train on something simple but still work on something complicated or like scale to something
*  complicated is like the hypothesized property of these cortical columns that you find a structure
*  that like a little of them is good and more of them is better. It's really like a scaling property
*  that people hope transformers have or shown that transformers have. So I think that would be a
*  really cool thing to capture. Yeah, if any of your listeners want to talk about that. Yeah,
*  that was inspiring. That's a great place to end it, Kim. Thank you so much for taking time out
*  of your busy schedule. It's great to hear that you're having fun doing what you're doing and
*  so I wish you continued fun and keep producing great work. So thank you. Thank you. This was
*  really fun. Brain Inspired is powered by The Transmitter, an online publication that aims
*  to deliver useful information, insights, and tools to build bridges across neuroscience and
*  advanced research. Visit thetransmitter.org to explore the latest neuroscience news and
*  perspectives written by journalists and scientists. If you value Brain Inspired,
*  support it through Patreon to access full length episodes, join our Discord community,
*  and even influence why invite to the podcast. Go to braininspired.co to learn more. You're
*  hearing music by the New Year. Find them at the newyear.net. Thank you for your support.
*  See you next time.
