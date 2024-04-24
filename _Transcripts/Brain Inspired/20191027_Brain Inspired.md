---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 5302s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 2504
Video Rating: None
---

# BI 051 Jess Hamrick: Mental Simulation and Construction
**Brain Inspired:** [October 27, 2019](https://www.youtube.com/watch?v=DhyWJrMBR4o)
*  We're interested in the general idea of construction,
*  which isn't necessarily about blocks,
*  but it's more about the ability to take pieces and put them
*  together and create something new out of that.
*  That's something that we as humans seem to
*  do a lot throughout our history.
*  Well, does it do it this way or does it do it that way?
*  Is the answer always yes to both?
*  Yes.
*  It always is, isn't it?
*  I think so. There's so much interesting stuff
*  that people come at from very different perspectives.
*  And even if that perspective is super, super different,
*  that it can be a really valuable thing to go and read about that
*  and then try to take those insights.
*  This is Brain Inspired.
*  Hey, everyone. I'm Paul Middlebrooks.
*  In 1961, Heinrich Ernst, under the advisorship of Claude Shannon,
*  developed a robot of sorts called MH1,
*  a computer-operated mechanical hand.
*  This thing was a robot hand that had tactile sensors,
*  not a vision system, but a tactile sensory system,
*  and it could put blocks into boxes.
*  So a human would put a block somewhere on a table
*  and a box somewhere on the table.
*  And MH1 would search for the block, pick it up,
*  then search for the box and put the block in the box.
*  As just one early example, of course.
*  Fast forward almost 60 years now,
*  and getting robots to do things with blocks is still a hard problem,
*  as you may recall when I spoke with Raya Hadsel during episode 45.
*  Well, today my guest is Jessica, or Jess Hamrick.
*  These days, Jess is a research scientist at, wait for it,
*  DeepMind, like everyone else, it seems.
*  And she has a background in computational cognitive science,
*  among other things.
*  On the episode today, we focus on two main topics.
*  We talk about physical construction,
*  that is her work using graph neural networks
*  with deep reinforcement learning
*  to create agents that build structures
*  in a simulated blocks and glue kind of world
*  to solve some tasks that she and her colleagues created.
*  This is the first time on the show,
*  I believe, that we've talked about graph neural networks,
*  which are not new, but as Jess and I talk about,
*  are getting more popular in AI these days.
*  And we go on to talk about her work in mental simulation
*  and how model-based reinforcement learning
*  is a promising way to model mental simulation.
*  We talk about some of the proposed ways
*  that humans mentally simulate,
*  or represent mental simulation, which is not settled yet.
*  And we talk about how machines might go about doing it.
*  In the show notes, I link to the papers that we talk about,
*  which I recommend to learn more about both of these topics.
*  Those are at braininspired.co
*  slash podcast slash 51.
*  You can learn more about Jess,
*  like her work on the Jupiter project
*  and her open source advocacy.
*  By following her on Twitter, she is at jhamrick,
*  or visiting her website, jesshamrick.com.
*  Just a reminder, I made a page on the Brain Inspired website
*  where you can enter your email
*  if you'd like me to keep you posted
*  about the little neuroscience AI course that I'm developing.
*  I say little, it's probably gonna be big.
*  You can do that at braininspired.co slash course,
*  where I've also added a brief and extremely rough video
*  explaining a little bit more about the course.
*  If you are a Patreon supporter, or if you become one,
*  like the obvious geniuses, Ingrid, Piet, and Hal,
*  did recently, thank you guys,
*  then you'll have access to a lot of what I create anyway,
*  as I will use you mercilessly
*  as beta testers and guinea pigs.
*  Okay, even though I couldn't convince her
*  that cognitive science should not be its own separate field,
*  I trust that you will enjoy learning from Jess Hamrick.
*  Jess, thank you for joining me on the show here today.
*  Thank you, Paul.
*  It's really great to be on the podcast.
*  Thank you so much for inviting me.
*  So I'm noticing, and we were on Skype,
*  I'm noticing you're not wearing
*  a construction helmet right now.
*  How do you decide when you're giving talks
*  whether to wear the construction helmet?
*  I suppose it probably has something to do
*  with what you're speaking about.
*  Yeah, so I guess you're referring to the talk
*  that I gave at ICML a couple months ago,
*  where, yeah, I was presenting on one of our recent projects
*  where we've been looking at agents that can stack blocks.
*  And so we sort of like, we're referring to that project
*  internally as like the construction project,
*  because we wanna have agents that can construct things.
*  And so that sort of became a bit of a thing
*  that we were construction workers
*  and working on this construction project.
*  And so at some point, Pete actually,
*  who's one of the other, Peter Battaglia,
*  one of the other people on the paper,
*  decided to buy a bunch of construction hats.
*  So we had them around the office
*  and I was like, oh, I'm gonna take this to ICML
*  and wear it during my talk,
*  because I thought it would be fun.
*  How did that go?
*  So, okay, how do you muster the gall to do that?
*  And I guess that's a relaxed setting perhaps.
*  And then, well, first, just how did you decide
*  that that's what you're gonna do?
*  And how did it go over is my second question.
*  I guess it was just, it seemed like a natural thing to do
*  because we had the hats and it was sort of like,
*  this joke that we had.
*  And it was pretty natural to try to do that, I guess.
*  But yeah, it actually went over really well.
*  I think the talk was probably a lot more memorable
*  as a result of that.
*  I had lots of people come up to me afterwards
*  and be like, hey, you were the one wearing the hat.
*  Or where's your hat?
*  Why aren't you wearing it now?
*  Did you quiz them after?
*  Hey, do you remember what I even talked about or what?
*  No, I didn't.
*  Maybe I should have.
*  It's a good idea.
*  But I think that that's sort of,
*  just learning more about you,
*  I think that it seems obvious
*  that you're a really good teacher.
*  And I think that's a really good mechanism
*  to help people learn having that prop.
*  Having things that sort of catch people's attention
*  and make them, I guess,
*  even if they didn't necessarily remember that much
*  about the talk itself,
*  I had a lot of people who came to the poster afterwards
*  who came because they remembered the hat.
*  Or they saw us wearing the hat at the poster
*  and then were like, oh yeah, that talk was interesting.
*  Let me go by the poster and learn a little bit more.
*  So I think it really engages people more
*  and helps them remember a little bit further.
*  Like, either this is something that is interesting,
*  I wanna follow up with it further,
*  or catches their attention more at the time.
*  That's great.
*  I mean, salesmanship actually works well
*  with communicating effectively, I think.
*  So that's a good way to do it.
*  Well, we're gonna talk about construction
*  and your work in that realm here today.
*  We'll talk mental simulation.
*  But before we dive into that,
*  so you have a background in,
*  I mean, kind of a broad array of things,
*  but psychology and computer science and engineering.
*  And of course, you're at DeepMind now
*  using all sorts of methods to answer AI questions.
*  But when you consider your place in all this,
*  where do you consider yourself sort of on the scale
*  between artificial intelligence and brain
*  and neuroscience and cognitive?
*  I hate to throw cognitive science in there
*  because I don't really,
*  I feel like cognitive science should be just lumped into AI.
*  I know that it has origins dating back to wanting to.
*  But I'm gonna say, where do you fall in the spectrum
*  between AI and neuroscience, just to make it simple?
*  I see myself as really being really quite right at the middle.
*  I mean, so even my whole background,
*  so I started out studying computer science
*  and with an emphasis on AI when I was an undergrad.
*  And actually, the earliest research that I did
*  was in a robotics lab.
*  And so I've always sort of been interested in
*  how can we build things that are intelligent?
*  And then I got interested in the human mind
*  and how people think.
*  And I was like, oh, this seems like
*  it's a really good angle to understand
*  artificial intelligence more.
*  And so that's how I got into psychology
*  and why I went to grad school in psychology.
*  And then so I sort of went off in that direction
*  for a while, but towards the end,
*  I came back again towards AI
*  and I started doing some work
*  with human robot collaboration.
*  I did an internship at DeepMind
*  and then ended up back here full-time.
*  So really, I guess my whole path
*  has really been kind of wiggling back and forth
*  between those two ends of things.
*  Sometimes doing more on the human mind side of things
*  and sometimes doing more on the artificial side of things,
*  but really being interested in both all the time.
*  Smack dab in the middle.
*  That's great that you're on the show then.
*  That's a perfect fit for the show.
*  Do I have to include cognitive science as a separate thing
*  or can I lump it in with AI?
*  Or should I lump it in with neuroscience?
*  What do I do with cognitive science?
*  No, I think cognitive science is definitely a separate thing.
*  Well, it's an overlapping thing.
*  I mean, I guess, well, the origins of cognitive science
*  really have it being like the intersection
*  between a whole bunch of different fields,
*  so neuroscience, AI, philosophy, anthropology,
*  so on and so forth.
*  And so I think nowadays,
*  I think if you go to the cognitive science conference,
*  you'll still find a lot of those different areas there
*  that the emphasis is more on the psychology side of things.
*  So it's kind of like, I think it's sort of morphed
*  into a little bit more of like,
*  it's like cognitive psychology,
*  but in particular with the emphasis
*  on either like computational modeling
*  or the idea that the mind can be studied
*  using like computational ideas,
*  like that it is a computational process itself,
*  which distinguishes it from a lot of other psychology.
*  But I would definitely say it's distinct
*  from both neuroscience and AI in and of itself.
*  See, I, and I know this isn't fair,
*  but I lump psychology into neuroscience.
*  I mean, you have to have some sort of buckets
*  that you put these things in.
*  And I'm just like, do I have to change the damn tagline
*  of my podcast to include psychology and cognitive science?
*  No, I'm just gonna keep two buckets
*  and lump everything into those.
*  I'm trying to anyway.
*  Congratulations on your first last author paper.
*  Oh, thanks.
*  So this is a paper called
*  Structured Agents for Physical Construction.
*  How does it feel to, how did that feel?
*  It felt really good.
*  It was really exciting to kind of be like,
*  like after grad school, working mostly like
*  by myself on projects and with my advisor, obviously.
*  And I had a few collaborations as well,
*  but I feel like in grad school,
*  I was often working a little bit like more on my own
*  and driving things myself.
*  And so having this paper was sort of more like,
*  I'm driving it, but more at the level of like,
*  here's like the important questions we should ask.
*  And then also still doing a lot of the hands-on work myself,
*  but then really getting to collaborate on that
*  with a bunch of other people.
*  And that was really fun and really exciting.
*  And it was really satisfying to see it come out.
*  And yeah, I was really happy
*  with how the project turned out.
*  Do you like that role of the driver versus the,
*  I know you're still doing hands-on things,
*  but you're sort of directing, I suppose, right?
*  In that role.
*  Do you prefer that role
*  or do you like the technician sort of role more?
*  I like both.
*  I'm never happy with doing just like one thing
*  or filling just one role.
*  I know, from your record, I know, yeah.
*  Yeah.
*  So I think it's really satisfying to kind of think more
*  at a high level of like, okay, like here's a problem
*  that people haven't really focused on
*  and we should really try to solve this problem.
*  And what would the solution to that look like?
*  And trying to gather suggestions and ideas
*  from the people that you're collaborating with
*  and work them out into a particular direction to follow.
*  But it's also really satisfying
*  to actually be the one to go in and make that happen.
*  Yeah.
*  So yeah, I think I really like both.
*  Cool.
*  Okay, well, so we're gonna talk about that work
*  in just a little bit here.
*  And I mean, who knows what order
*  we'll actually talk about these things.
*  So, but I also wanna ask,
*  so every time I talk to someone,
*  I have this sort of long list
*  of these broad general questions
*  and I never can get to all of them
*  because I'm always running out of time.
*  So I wanna just start with one that is always on my list
*  that I haven't been able to ask.
*  As I'm talking to people, I kind of like cross things out
*  or push them down.
*  And this one always gets pushed down,
*  but I wonder if I can just ask it up front here.
*  The question is, what is a unit of meaningful progress
*  in AI and in neuroscience and just to you personally?
*  Because in the AI world,
*  you're like trying to solve things, right?
*  Accomplish the task or whatever.
*  And that's kind of,
*  I won't feed you, I won't lead you in any directions.
*  Does that question make sense
*  and do you have answers to it?
*  Well, I guess a follow up question in response would be
*  what is the time scale at which you're referring to
*  when you talk about meaningful units?
*  Because I think that the answer is really different
*  if you're talking about the time scale of a few years
*  versus 10 years or 20 years.
*  Well, I wanna let you just answer it
*  because the word meaningful, right,
*  is also just up for grabs in what it really means.
*  I mean, to be sort of pessimistic in academia,
*  a unit of meaningful progress is a paper
*  or a grant published.
*  And I don't know how meaningful that really is.
*  And I know in the AI world,
*  especially DeepMind, you guys publish all your stuff too.
*  But I would say a more meaningful unit of progress
*  would be like figuring out
*  how this particular model instantiation
*  solves the task relative to another task
*  or building a new type of model or something like that.
*  So. Yeah.
*  Well, I guess I see there as being, I guess,
*  two, I mean, there's sort of like two types of progress,
*  maybe one is kind of more of like a task focused progress
*  and one is more of a methods focused progress.
*  So I think like we can certainly make
*  like very meaningful progress on the task dimension
*  at least this is I guess more maybe on the AI side of things,
*  but saying like, can we get an agent to do X?
*  Like, can we get an agent to play StarCraft
*  or can we get an agent to play Go?
*  Not just play, but beat the world champions.
*  Yeah, for example.
*  And I think that those are very meaningful units of progress
*  because you take a problem that people consider
*  to be very challenging and you show it's possible to do this.
*  Now, you can pick out the solution and say,
*  well, is this really the way we want to do it?
*  What about the computational cost
*  or like any of these other considerations?
*  But at least you sort of established we can do this.
*  And I think that that is a useful thing
*  to be able to establish.
*  But then I think on the method side,
*  it's also super valuable if you can say,
*  okay, here's an existing problem,
*  we already know we can solve it,
*  but here we're gonna come up with a new way of solving it
*  that like we hadn't considered before.
*  And I mean, there's many ways
*  you could potentially try to do that,
*  I guess, to make it meaningful
*  as opposed to just like an incremental thing,
*  it would have to be kind of like coming at it
*  from a completely different angle,
*  or maybe like solving a different,
*  maybe if you came up with a method
*  that could solve like a different subset of problems,
*  as opposed to like, you know, you have one method
*  which can solve a particular class of problems,
*  a different method which can solve another class of problems
*  and then something come up with something new
*  that sort of unifies those or whatever
*  would be also a very nice meaningful unit.
*  I think that those are more, I guess, like short-term things.
*  In the long-term, meaningful progress
*  maybe has something to do a little bit more with like,
*  what are the sorts of like general abilities
*  that we would expect like AI agents to be exhibiting.
*  So, you know, I guess, you know, we can kind of, I guess,
*  say we have AI that can do pretty well
*  in like closed simulated environments
*  that are like fully observable and deterministic.
*  That's like, you know, that class of problems
*  like we can do pretty well on.
*  And so if you could say, have another class of problems,
*  which is like equally broad,
*  that, you know, we could be pretty confident,
*  like we can solve would be like another,
*  I think, meaningful unit of progress.
*  So, okay, all of those answers
*  were on the AI side of things.
*  Yeah, yeah, yeah.
*  Well, that's why I'm kind of asking
*  is because it's a little fuzzier on the neuroscience.
*  I think it's a little more definitive on the AI side,
*  what, you know, these measures that you could say
*  are progress, many of which you just named off, yeah.
*  Yeah, so I think, I mean, one thing to me
*  that I see as being progress on like the neuroscience
*  and cognitive science side of things
*  is being able to explain behavior
*  at increasingly more complex,
*  or yeah, being able to explain
*  increasingly more complex behavior.
*  So one thing we really like to do
*  in the behavioral sciences is have these like really nice,
*  well-controlled experiments where, you know,
*  you know exactly like everything that's going on,
*  you can do exactly the manipulations you want to do.
*  And then we can usually explain behavior pretty well
*  under those settings, but it means that we're also limited
*  to very like limited types of behavior.
*  And so I think being able to explain,
*  or maybe explain is too strong a word, but like-
*  I was about to say explanation is its own conundrum, yeah.
*  Like if we can predict behavior that's like
*  in much more complex and like ecologically valid settings.
*  So say if you could predict like, you know,
*  the exact like motor movement someone's going to make
*  in a particular setting, or if you could, you know,
*  predict like maybe how people will play, you know,
*  these more like, you know, very like say open-ended video
*  games or something like that.
*  I think that sort of thing would be a meaningful unit
*  of progress because, you know, even though we might honestly
*  have the explanation to go along with the behavior,
*  we at least have like a starting point that we can then try
*  to dissect and get at that.
*  But I think as long as we stay sort of focused
*  on these very well-controlled things,
*  we might get like little insights about, you know,
*  particular aspects of behavior, but we don't really know
*  like how that gets instantiated and in sort of these larger
*  more complex contexts.
*  And particularly if we're interested in like
*  the intersection of AI and neuroscience and cognitive
*  science, I think, you know, we want AI that's able to act
*  also in these like scaled up ecologically valid settings.
*  And so understanding how human behavior works
*  in those settings is going to be a really important aspect
*  to go along with that too.
*  Yeah. Yeah.
*  I mean, when talking with a lot of people on the AI side
*  of things, it's all, it's often about solving problems,
*  right? So there's a problem, there's a finish line
*  and you solve the problem by, you know, making the version
*  that beats a chess player at chess, you know,
*  and things like that.
*  And so that's a very measurable quantity.
*  And it just struck me, I think just out of jealousy being
*  coming from the neuroscience side of, you know,
*  just doing the daily work, like what's the goal here?
*  The goal is to sort, well, besides curing diseases,
*  because that's very meaningful progress.
*  But then it's to understand, understand how the brain
*  is doing the task, right?
*  For instance, or just understanding what the task is,
*  what's actually being done.
*  And that's such a fuzzy, unsatisfying way to try
*  to measure something.
*  So from coming from the neuroscience side in my own head,
*  if the goal is to understand intelligence, let's say,
*  and we could unify the AI and academia, neuroscience,
*  cognitive science world, that those are fuzzier goals.
*  So that's why I'm curious what people have in mind,
*  you know, just as a unit of measure of meaningful progress.
*  So yeah.
*  Yeah.
*  I appreciate everything that you said as well.
*  So thanks.
*  Yeah.
*  Well, yeah.
*  I guess one thing just to follow up on that is like,
*  I think especially coming from the academic tradition
*  in cognitive science, like I did by PhD in,
*  which is like this idea of doing like
*  computational level modeling and rational analysis.
*  The idea there is actually, in a way, is very similar
*  to the approach that's taken in AI.
*  It's like in AI, we say, okay, here's a problem,
*  we want to get our agent to solve it.
*  What sort of like, you know, constraints,
*  meaning like the architecture or the reward function
*  or whatever, do we need to like apply here
*  in order to get the agent to like solve this problem?
*  Yeah.
*  And in cognitive science, or in this computational level
*  modeling and rational analysis,
*  it's kind of a very similar sort of thing.
*  It's like, okay, here, humans are doing some behavior
*  in this context and like, what are the sort of constraints
*  that we think that they're optimizing for?
*  And so the question is, I mean, you know,
*  in one case, we're trying to infer what the constraints are
*  that people are optimizing for,
*  in the other case, we're trying to like set the constraints
*  just so we can get the behavior that's desired,
*  but they're kind of very similar questions in a way.
*  And so there's some, I think there's some parallels there
*  where like, if you can make progress on one,
*  you can maybe make progress on the other too.
*  And you feel, just personally, you feel like
*  you're making progress, meaningful progress when,
*  you know, when you're, for instance,
*  like mental simulation and construction,
*  these feel meaningful to you.
*  And I'm not trying to like bait you or anything.
*  I think so.
*  I mean, certainly my more recent work, I think,
*  has more to say about AI than about neuroscience
*  and psychology, though I think that there are
*  like interesting connections there
*  that could be explored further.
*  But I think on the AI side of things,
*  with the work that I've been doing, like on construction,
*  I think, I guess like the class of problems
*  that people are focused on, they tend to be,
*  like at least on the RL side of things,
*  tends to be things like games or things like
*  continuous control are kind of like the two main like
*  pillars in RL, I guess, that you see a lot.
*  And there's not a lot in RL that looks at tasks
*  that are a little bit more like things that like
*  kids might do or like, you know,
*  like simplified behaviors that humans might actually exhibit.
*  So not to say that our block stacking agents are like,
*  literally, you know, they're not doing the same stuff
*  that humans do, but it's more similar to maybe
*  the types of things that you might do as a kid,
*  because, you know, kids love to stack blocks or whatever.
*  So it has kind of a different flavor to it
*  than I think a lot of the other types of RL tasks.
*  And I mean, that's actually like one of the things
*  that we found is that sort of like the state of the art
*  canonical RL agents don't actually work that well
*  on these tasks because they have
*  this different flavor to them.
*  Right, okay.
*  All right, thank you for playing along.
*  Okay, so Jess.
*  Yeah.
*  As AI progresses, it seems to me that we're basically,
*  you know, digging deeper into the bag
*  of intelligent behaviors and making machines
*  that can do like some version of those behaviors
*  like you were just describing.
*  Things like image classification,
*  you could describe that as a behavior too.
*  Done, machine learning, machine translation, done.
*  But I've been, so I've been reading about like
*  the early days of AI when symbolic, good old fashioned AI,
*  I'm making air quotes, was born.
*  And it seems like the systems that they were making
*  were inspired either by really scant knowledge of psychology
*  or like their own sort of intuitions about how we think.
*  Yeah.
*  And so we've learned a lot since then,
*  but there is still an infinity essentially
*  to learn about how we think.
*  So I've had people on the show that, you know,
*  they're using deep learning and they consider
*  what they do more psychology actually,
*  because you know, they make these little tasks, right?
*  And then they see if their deep learning nets
*  and such can do the task.
*  But anyway, they consider it more psychology
*  than neuroscience that they're comparing these things to
*  because they're trying to teach machines
*  to do tasks like humans do.
*  And then they're looking at the representations
*  in the artificial networks and seeing how they map on
*  to know, map onto what we know about brains
*  and how the brain works.
*  But these days, I mean, trying to keep up with just
*  the rush of things coming at us,
*  but it's like every day I hear someone talk about
*  like some particular scenario,
*  very specific scenario about cognition.
*  Like, you know, they'll say something like, you know,
*  remembering how to ride a bike, right?
*  You know, after 10 years, let's say, 10 years elapsed
*  and we still know how to ride a bike
*  because of procedural memory or like,
*  or they'll say, you know, like, well, humans can,
*  can just be walking down the street
*  and they were working on a problem they're trying to solve.
*  And then boom, a dream that they had a month ago
*  pops into their head and helps them solve the problem.
*  And they say, well, humans can just do that, right?
*  But machines can't do that yet.
*  We need to figure out how to do that in machines.
*  So I'm kind of wondering, like,
*  are we still playing the same game as in the early days,
*  you know, using these behaviors and maybe having ill-formed
*  or incomplete, at least psychological notions
*  about how these things actually work
*  to build machines that do these things.
*  So that was really long-winded question, I suppose.
*  Yeah, so, well, I guess I think that there's two things.
*  So I don't know if there's necessarily like anything wrong
*  with like using our intuitions to guide scientific progress.
*  Like, well, that's what we do every,
*  we have to use intuitions.
*  Everyone does that.
*  All scientists do that.
*  Not even, you know, scientists that are working on AI, right?
*  So, so I don't necessarily think that there's a problem
*  in and of itself to do that.
*  I do sort of take, take issue with when people do that,
*  but then they say, oh, we know this about humans
*  and therefore, like that's why we're motivating this approach.
*  I don't think you should motivate an approach in AI
*  from human psychology, unless like that's actually
*  like a well-documented thing in human psychology.
*  But yeah, I think that there's like, when that happens,
*  I think it could be a bit of a problem actually,
*  because then maybe people who don't know so much
*  about psychology go and say like, oh, look,
*  like lots of people are basing their, you know,
*  approaches in psychology,
*  but these approaches are like too rigid or whatever.
*  Like if you look back at like, you know, good old fashioned AI,
*  and then they have the wrong idea about like,
*  what can psychology provide for AI?
*  But I think if you look at broadly at like the whole literature
*  of like particular subfields in psychology,
*  there are very important things that you can say about AI.
*  So, I mean, maybe these things are kind of obvious,
*  but I think that they like bear repeating things like,
*  that objects are an important like psychological construct
*  that we like, objects are so fundamental to cognition.
*  And yet like in most of our AI agents, we say, okay,
*  we'll just hope that objects kind of like appear
*  in the representations, you know.
*  But from my point of view, I think, I mean,
*  if we know it's so important psychologically for humans,
*  why not give agents the capacity
*  to represent objects in some way?
*  That doesn't mean you have to tell the agent
*  exactly what an object is, you just want to give it
*  some bias towards the idea that objects are a thing
*  that they could use to reason about the world.
*  So I think that that's where like psychology
*  and neuroscience can potentially really help to inform AI
*  is more in terms of saying like,
*  here's this very important thing in psychology.
*  You know, there's like decades of literature on these ideas.
*  It seems given that there's so much research on this,
*  and it seems to be such an important part of cognition
*  that like that should be a thing in AI too.
*  Yeah, but it's not building in a specific thing,
*  it's building in like a general capacity.
*  Yeah, and I think that that's maybe what differentiates it
*  from like approaches in good old fashioned AI
*  where people did actually say, oh, look, humans do this thing,
*  let's like build in this very specific behavior.
*  And I don't think that that's necessarily
*  the right thing to do.
*  I mean, it is interesting though, like even the,
*  we'll talk about the graph networks in a little bit,
*  even that I'm reading it and I think that is almost like,
*  almost like heuristics in some way, you know,
*  back when they built heuristics just to figure out
*  what the best path through a search tree was, you know,
*  and think, you know, the best way to approach
*  a search tree and stuff.
*  So yeah, so, you know, then I think, well, is it,
*  are we swinging back toward this symbolic AI?
*  But I like the way that you phrased that,
*  that it's not building the thing into it,
*  it's building a capacity to allow things that we know
*  that occur on psychological levels
*  to happen more readily, essentially.
*  Yeah, I mean, I always think of it as just being kind of like,
*  there's a spectrum on like, you know,
*  how much inductive bias you have in your system.
*  Good old fashioned AI was like,
*  it was like all inductive bias.
*  100%, yeah, yeah.
*  Yeah, it's like the system literally like, it cannot like,
*  there's no outside input that causes the system
*  to really like act differently.
*  It's all just like hard coded rules
*  and like that's exactly specified by the programmer.
*  And then sort of the like more like these big like end to end
*  neural network architectures, they have maybe like less,
*  like hard coded inductive bias in them.
*  They still have inductive bias in them.
*  They're not, I don't buy the whole like
*  learning from scratch thing.
*  Cause I think they still do have inductive bias
*  in terms of like the architecture that you choose
*  and like what training data you give it
*  and how long you train it for and you know,
*  which optimizer you use, all of these sorts of things
*  are things that will influence the result.
*  But they maybe have like, you know,
*  the inductive bias that they have is much more,
*  I guess like domain general in that it's, you know,
*  it's not specific to a particular problem
*  that you care about.
*  But, and then, then you can have stuff
*  that's sort of in the middle where you say, okay,
*  you know, things like a graph network,
*  which basically makes the inherent assumption
*  that the world is composed of entities
*  and relationships between those entities.
*  That's sort of like getting at this idea of like that,
*  you know, building the idea of an object into the system.
*  It's not saying, you know, oh,
*  here's how you perform on a particular task,
*  but it's also saying, it's also making the assumption
*  that there are these things that we care about.
*  And that, you know, that maybe wouldn't work well in,
*  if you try to like throw it at a problem
*  where there aren't, you know, discrete entities,
*  maybe everything really is like wishy continuous,
*  you know, stuff, then maybe you really don't want
*  to use a graph network.
*  But, you know, if you want agents that are able to act
*  in the world that we live in, like this world is very,
*  does have a lot of structure and is very discrete
*  in a lot of ways.
*  And so it seems like it's useful to be able
*  to identify like where along that continuum
*  you care about drawing the line and then focus there.
*  Well, Jess, you've screwed up my structure,
*  speaking of structure of the show here.
*  Sorry.
*  You got me all turned around, but all backwards,
*  but that's great.
*  Let's put on our hard hats and talk about construction
*  and graph networks, shall we?
*  Okay, yeah.
*  So this is like your most recent work
*  and it's the last author paper
*  that I alluded to essentially.
*  And you're basically teaching AI agents
*  to build with blocks, essentially like kids do.
*  I know that you backed off from,
*  it's not really the way kids are doing, of course.
*  But basically you made a set of building blocks tasks
*  and tested a bunch of different types of models
*  to see which one performed best.
*  And you found that graph neural networks
*  that use reinforcement learning,
*  a la model-based planning,
*  which is like part of the mental simulation stuff
*  that we'll talk about in a little bit,
*  beat out the other approaches that you tested.
*  So I'm not kidding when I say this,
*  on my way into this little tiny studio
*  that I'm recording in,
*  I literally had to kind of climb over
*  and step over the fort that my kids built in the living room
*  and did not clean up yet, like their father told them to.
*  So yeah.
*  So what is construction in this context here?
*  Well, so we're sort of interested
*  in the general idea of construction,
*  which isn't necessarily about blocks,
*  but it's more about the ability to take pieces
*  and put them together and create something new out of that.
*  And that's something that we as humans
*  seem to do a lot throughout our history.
*  We figure out how to build shelter from the elements
*  and now in the last century or so,
*  we've built even much more complex things
*  like skyscrapers and space stations.
*  And we love to figure out new ways to innovate
*  and construct things that allow us to do new things
*  in the world that we couldn't do before.
*  So that's kind of the idea behind construction.
*  That's the grand view at least
*  that we would like to aim towards.
*  So what we did in this project was really just
*  a very tiny baby step towards that,
*  which is to say, okay, where does,
*  what sort of more simple construction behaviors
*  do we observe?
*  Well, kids love to play with blocks,
*  so let's do something with blocks.
*  And it was actually something that,
*  block towers are a domain that I've worked a lot with
*  for a long time, basically since the beginning
*  of my research career.
*  One of my earliest research projects
*  was also looking at towers of blocks, but in humans,
*  and looking to see how people make predictions
*  about how those towers of blocks fall over,
*  what directions they fall in.
*  And so this is sort of the next iteration of that.
*  But now instead of looking at humans, we're looking at AI,
*  and instead of just making predictions
*  about what's going to happen,
*  we're looking at actually producing
*  those construction behaviors
*  and actually building the towers up.
*  So the goal in the tasks is to,
*  there's like a few different objectives.
*  They all involve like picking up blocks
*  and putting them in the scene.
*  There's some obstacles in the scene
*  that you have to stack around.
*  So you can't, if any of the blocks like touch an obstacle,
*  then the game is over basically.
*  And you're equipped with a glue stick as well.
*  Yes, so you can choose to make blocks sticky,
*  in which case, I actually think of it more as like,
*  you're dipping them in a pot of glue rather than.
*  Pardon me, okay.
*  Yeah, rather than a glue stick.
*  Only just because like if anything sticks to it
*  and any part of it, then.
*  It's all sticky.
*  It's all sticky.
*  What about a glue stick that you have to cover
*  the entire block with vigorously?
*  How about that?
*  Yeah, that's fine.
*  Okay, thank you.
*  But yeah, so you can make some blocks sticky,
*  and then they'll stick to everything,
*  and so you can't like break those bonds.
*  And then there's various tasks.
*  So like one task, for example,
*  is you see like the silhouette of a tower,
*  and you have to place the blocks into that silhouette
*  to like sort of reconstruct the tower.
*  And it's not just as simple as like placing blocks
*  exactly where they need to go.
*  You also need to decide like which blocks
*  should I make sticky,
*  because the tower might not actually be physically stable
*  without the sticky blocks.
*  And then in the task, it actually,
*  there's a cost incurred to using the glue, right?
*  Yeah, so you can think of that as basically like,
*  the glue is expensive or it's a limited resource
*  or something along those lines
*  that you wanna try to limit the amount of glue
*  that you're using.
*  It's also kind of like an interesting parameter to tweak
*  just from like the experimental design point of view,
*  because if you allow glue to be,
*  or sticky blocks to be free,
*  then the easiest thing is just to make all the blocks sticky
*  because you don't have to research about physics
*  in that case.
*  But you didn't have to consider world economies
*  to do this though, did you?
*  No. The supply of glue,
*  supply and demand curves, yeah.
*  Yeah, luckily our glue is simulated,
*  so it doesn't actually incur cost on the economics of glue.
*  But yeah, so that's like one example.
*  But then we have other tasks like stack the blocks
*  to reach like a point in the sky,
*  just while avoiding the obstacles.
*  So that's kind of, it's almost actually more like
*  a navigation task where you have to figure out
*  where to place the blocks just to like weave in
*  and out of the obstacles to get the stack
*  to a particular point.
*  And then we have another task,
*  which is more of like building shelters.
*  So you want to stack the blocks
*  so that they cover the obstacles from above.
*  So you can imagine like if it were to rain,
*  then the obstacles would stay dry in the rain.
*  And so these are like three different tasks
*  that kind of have, you know, they're different objectives,
*  but they're all sort of in the same simulated environment.
*  So it allowed us to explore sort of a range of behaviors.
*  And then, so you could say, okay,
*  how should we train an agent to do this?
*  Well, like the typical response
*  in deep reinforcement learning would be,
*  take an image of the scene and then give it to a CNN
*  and then have the CNN say a coordinate, for example,
*  of where you should place one of the blocks into the scene.
*  Right.
*  So that's like, that's one option.
*  You could say, oh, but like, you know,
*  Josh, you were just talking about how objects are important.
*  So maybe, you know, you should have
*  an object-based representation.
*  So then maybe the next like sort of standard answer
*  would be, okay, well, you take an RNN
*  and you allow it to process each of the objects
*  in the scene one by one.
*  And then you have it at the same, you know,
*  the same as a CNN, you output like a coordinate
*  of like where you want to place a block.
*  And these would kind of be the default ways to approach this
*  given our current, the standard library
*  of deep learning tools, I suppose.
*  Exactly, yeah.
*  It's sort of like, yeah, the natural,
*  like here's your components.
*  Like how would you assemble them to solve this problem?
*  That's sort of like the natural answer.
*  But it turns out like when we tried to implement those agents
*  and train them on this task,
*  they didn't actually do very well.
*  The CNN actually worked okay.
*  Well, it actually depended on the task.
*  Sometimes the CNN did a little bit better.
*  Sometimes the RNN did a little bit better.
*  But neither of them really did that well.
*  So someone said, screw it, let's go back to symbolic AI
*  and use graph networks.
*  Is that what happened?
*  Sort of.
*  No, I mean, yeah.
*  Yeah, not exactly like that.
*  But I mean, the motivation was kind of like,
*  the CNN doesn't really like directly parse objects.
*  And the RNN has this problem where the order
*  that you give the objects will have a big effect
*  on the answer that it gives.
*  So really what you want is something that can reason
*  about all of the objects as discrete separate entities,
*  but not where there's like this effect
*  of like how the order in which you parse them.
*  And so a graph network has these properties.
*  So a graph network is a neural network
*  that operates over graphs,
*  where the graph is a collection of nodes and edges.
*  So in the context of the construction tasks,
*  maybe each object in the scene corresponds
*  to a node in the graph.
*  In our particular case, we chose just to put edges
*  between all the nodes in the graph.
*  And then they have each of those edges and nodes
*  is associated with a vector or a tensor.
*  So that might, in the input that might correspond
*  to the object properties like position, size, type,
*  these sorts of things.
*  So then the graph network processes that graph
*  and it gives you a new graph with the same structure,
*  but like new activations on the edges
*  and the nodes of the graph.
*  And the way that it does that is by basically performing
*  these pairwise computations between all the pairs of nodes
*  that are connected.
*  And so in this way, it doesn't matter the order
*  that you give the nodes in
*  because it does the same computations all over the graph,
*  the same sort of local pairwise computations.
*  And like one time step essentially,
*  or one, I guess that'd be one cycle,
*  one cycle of what would you call it?
*  So we usually call them message passing steps.
*  Okay.
*  Yeah, so one message passing step is like one application
*  of the graph network.
*  It's called message passing because,
*  well, there was an earlier paper called
*  message passing neural networks
*  that they basically formula.
*  It's a particular type of graph neural network
*  that the nodes compute messages
*  and then they pass those messages along the edges
*  of the graph to the other nodes.
*  And then you can pass additional messages.
*  I see.
*  Yeah.
*  So I know this is not symbolic AI,
*  but I was literally just reading about semantic networks
*  from like Marvin Minsky days in the 1960s
*  and when they were trying to figure out language.
*  And like basically a semantic network worked on,
*  they had nodes where they're basically
*  these symbolic structures at the nodes
*  that had little properties, little lists of lists, right?
*  Was like a symbolic structure.
*  And then there are associative links between the nodes
*  that you could perform analysis on.
*  And she was like, oh, that's a graph network.
*  And I know that they don't map perfectly on,
*  but it does kind of harken back to that same way
*  of representing the data,
*  which is just an interesting parallel to me.
*  Yeah, I think that there's a lot of like connections
*  with like graph networks
*  and things that were previously explored.
*  I guess in the same way that,
*  deep learning is really just like the evolution
*  of a lot of stuff that have previously been explored
*  back in those days too.
*  Shockingly, things build upon each other.
*  Yes, as we advance.
*  But these graph networks aren't new.
*  I mean, they're new to me.
*  And now I have, now there's a whole new suite
*  of things I have to learn.
*  Thanks a lot, Jess.
*  Apologies.
*  Because they're kind of exploding now, right now, right?
*  Yeah, so graph networks have been around.
*  So like some of the earliest work
*  with like neural networks on graph happened
*  in like the early mid 2000s, like 2005 or so.
*  This is like work by Marco Gori and Scarcelli and others.
*  And they were looking at neural networks
*  that operate on graphs.
*  The formalism was actually not too different
*  than what it is today.
*  They were motivated by various like actual graph problems.
*  Like so either like graph theoretic problems
*  or questions about like networks.
*  So like doing things like predicting page rank
*  or various graph problems.
*  There was also some early stuff looked at problems
*  in chemistry, molecular chemistry.
*  So say if you have a molecule,
*  you can represent the molecule as a graph
*  and then you can predict like properties of that molecule
*  and these sorts of problems.
*  And then it didn't, yeah, graph neural networks
*  didn't really have, get like too much attention for a while.
*  And then they started picking up a little bit more attention
*  and people got interested in things like,
*  there's like a variant of graph neural networks
*  called graph convolutional networks,
*  which is kind of like a generalization
*  of regular convolutional networks, but on graphs.
*  But you can kind of see them as all being
*  like in the same family of things.
*  Yeah, so they sort of have been picking up steam
*  looking at these sort of like graph centered problems.
*  But I think one of the reasons why we're very excited
*  about them is because we see them as really applying well
*  to the types of like psychological constructs
*  that we think are important.
*  Again, like going back to the question of like,
*  entities and relations, and that has all sorts of,
*  connections in like things like reasoning about analogy,
*  like one of the most famous theories
*  in analogical reasoning is a structure mapping theory,
*  which says that people have these graphs
*  that represent a concept and they have another graph
*  which represents another concept.
*  And then you find the connections between those graphs
*  and that is how you do analogical reasoning.
*  And there's also older work or other work that looks at,
*  various psychological representations
*  as being graph structures.
*  So things like how we represent like taxonomic structure
*  or how we represent even like color,
*  you can see as being like a chain, right?
*  Yeah.
*  Like if you discretize it, then it's a chain.
*  No, it's a really natural way to,
*  it actually feels good to think of things
*  like in this, in the graph way.
*  Like it feels very natural.
*  And so in your blocks world, how do the,
*  how do the tasks, how do the entities map onto graphs
*  in the construction of blocks world?
*  Right, so the nodes in the graph correspond
*  to the objects in the scene.
*  So an object then has properties like its position,
*  its size, its type, you know, if you were in,
*  it doesn't really matter like depends on what
*  particular domain you're in.
*  Could be like density or something.
*  Yeah, like you could also do color, anything like that.
*  And in our case, like color and density don't matter,
*  but you could represent that.
*  And then, so those are the nodes,
*  then the edges can represent the relationships
*  between those things.
*  So in our case, we're looking at, you know,
*  can the neural network kind of learn
*  what are the important relationships?
*  But you could, you know, for example, say,
*  we're gonna connect blocks that are in contact
*  with each other to represent like the contact relation.
*  Or you could say, actually a prior paper that we had
*  before the main construction paper,
*  which I presented at COGSci last summer,
*  was it was looking at a related task called
*  the gluing task where you have a tower of blocks
*  and you have to choose pairs of blocks to glue together.
*  So it's kind of a different notion of sticky blocks
*  than in the construction paper.
*  But, and in that case, there you can represent
*  on the edges, whether that edge has glue or not,
*  like whether those pairs of blocks are glued together.
*  So the edges are very flexible and sort of can represent
*  any types of relations that you might care about.
*  But you hard code that in, right?
*  I mean, you have to make a decision
*  about what they're gonna represent.
*  Yeah, so that, I mean, one of the sort of big questions
*  that a lot of people are working on,
*  and I think we're starting to see some progress
*  in this area is, yeah, basically figuring out automatically
*  what things, like what is the structure of the graph
*  that you should care about?
*  And like what things should go into the nodes
*  and what things should go into the edges?
*  Because ideally, like, I mean,
*  you would start from like sensory perception.
*  You start from an image or something and then say,
*  okay, let me extract the graph structure from this
*  and then do my processing on the graph structure.
*  And then, you know, I get the output at the end.
*  In the construction of work, we were starting directly
*  from the graph structure to begin with.
*  But yeah, I think if you were to like hook it up to,
*  you know, like an unsupervised, like object segmentation
*  sort of system, you would have basically
*  the same sort of behavior.
*  Yeah, so that's the way that the scene
*  is represented as a graph.
*  And then when you do like computation with that graph,
*  you can basically choose then any sort of like function
*  you want as a result of that.
*  So you can have functions on the edges of the graph.
*  You can have functions on the nodes of the graph
*  or like you could have a function
*  as like a global property of the graph.
*  So you could say like, let me predict like whether
*  the whole tower of blocks is stable or unstable, right?
*  That would be like a global prediction that you could make.
*  Or let me predict, yeah, like in the gluing task,
*  let me predict like which edge should be glued
*  so that the tower remains stable.
*  Or in the construction task, we also were actually
*  producing actions on the edges of the graph,
*  which corresponded to relative actions
*  of which block should I place on another block.
*  So it's a, I think like this way of like specifying
*  structured actions on the different things
*  that might be in a graph is a really like powerful language
*  for building agents that are more expressive
*  than your typical RL agents.
*  Cause your typical RL agents are like,
*  you know, you can like,
*  you either have like a small set of actions,
*  like move up, left, right, down maybe,
*  or like, or maybe they're like, you know,
*  something very low level like motor controls,
*  or torques or whatever.
*  Or maybe they're like, you know, you're controlling a cursor
*  so you can move the cursor around and like, you know,
*  point and click or whatever.
*  But these are kind of all very like,
*  they're useful action representations to start with
*  because they are the actual like actions
*  that you get to take on the world.
*  But you can sort of decompose it a little bit
*  in the same way you can decompose like,
*  there's like perception and then there's reasoning.
*  And like, obviously the two are, you know,
*  the interface between the two matters a lot,
*  but you can kind of study each of them
*  a little bit in isolation.
*  I think you can do the same thing
*  with action representations too.
*  So you have like the actual like true action
*  that you take in the world,
*  but then there's the way that you,
*  and then there's maybe the way
*  that you can structure the actions
*  in a more like say relational way,
*  and then translate that into the actual actions
*  you take in the world.
*  So in the case of the block stacking,
*  just to make it more concrete,
*  because it's a little bit like,
*  it's a little bit high level,
*  is if we're gonna place a block,
*  I wouldn't say, you know, pick up this block
*  and place it at like position like 3.2, 6.7, 5.4.
*  Like what does that even mean?
*  Like no one knows, right?
*  I would say I'm gonna put this block on,
*  like I'm gonna pick up the red block
*  and I'm gonna put it on top of the green block, right?
*  And so that's a much more structured way
*  of specifying the thing that I'm trying to accomplish.
*  And even though like my motor system does have to translate
*  that concept of like, you know, red block on green block
*  into like a specific coordinate to bring it to,
*  that's delegated to a different part of cognition.
*  And so I think it's interesting to explore like, okay,
*  what are these more structured ways
*  that we can think about performing actions onto the world?
*  And so this was sort of one way of exploring that
*  and that was basically the action representations
*  that we had was pick up a block
*  and put it on top of another block.
*  Since we're talking about the concrete examples
*  of the blocks, then what did you find?
*  Yeah, so I mentioned earlier, you know,
*  we tried these other agents like the CNN and the RNN
*  and stuff, they didn't work that well.
*  But when you do both, so the graph networks,
*  there was sort of two choices that we had to make
*  and both of these were important.
*  So the first choice was the actual like structure
*  of the problem as a graph itself.
*  So you can take in the input scene,
*  structure it as a graph, you know,
*  run your graph network over that.
*  But then you could just like predict a single
*  like global action to take, which would be like,
*  put the block at this coordinate.
*  So that's like, it's a structured representation,
*  but an unstructured action.
*  You can also choose to make the actions themselves
*  structured so you can then have the structured graph
*  representation, which then supports structured actions
*  like relative actions, like place a block
*  on top of another block.
*  And so we found that the graph structured representation
*  was actually like less important than having
*  the structured actions.
*  Having the structured actions was really the important part.
*  But even if you give like more like structured relative
*  actions to these other agents, like CNNs and RNNs,
*  then they, I mean, that helps their performance too,
*  but it's like really the combination of like
*  the structured actions and the structured representations
*  together in conjunction that gives you the ability
*  to train agents that can do really well at this task.
*  And so we saw that our agents were basically,
*  on some of the tasks, they basically completely solved it.
*  And other tasks, they're very close to ceiling performance,
*  not quite, but almost.
*  So like in the silhouette task,
*  which is the one I mentioned where you see the silhouette
*  of the tower and you have to fill it in with the blocks.
*  That one, the agents are completely able to solve.
*  Which one do they have problems with?
*  Is it the one where they cover the obstacles?
*  Yeah, that's the one that was the hardest task for them.
*  So it's hard for a number of reasons.
*  So one reason why it's hard is it's sparser reward.
*  So you have to like place multiple blocks
*  in order to actually cover it.
*  And then you don't get any reward until you,
*  or any of the obstacles.
*  It's also very, you have to be very careful
*  in where you place the objects,
*  because if you collide with any of the obstacles,
*  then the game is over.
*  So, and you don't get to, you know, retry.
*  So I think this would actually be a very hard task
*  for humans to do too, if you didn't give them
*  an on you button, I think people would be pretty bad at this.
*  But it's also hard because, you know,
*  there's multiple obstacles you have to cover
*  and in order to cover all of them,
*  you really have to like compose the blocks
*  into like multiple structures.
*  So you can't just like, you know, cover this one
*  and then cover this one and cover this one independently.
*  You have to sort of cover them in a compositional way.
*  And so we saw our agents come up
*  with some pretty cool solutions.
*  Like they decided to build these like,
*  these T or umbrella structures.
*  So there were three sizes of blocks,
*  like little square ones,
*  and then like two longer rectangular ones.
*  So they would stack up the little square ones
*  and then like place a long one at the top.
*  And then they would like maybe do the same thing
*  on the other side of the obstacle,
*  and then place another long one like right in the middle.
*  So they build this like big arch all the way around it.
*  The glue is infinitely strong.
*  So in this task actually, the glue was very, very expensive.
*  And so the agents didn't really use it
*  in this particular task.
*  So this is all like their reasoning about the physics
*  of this in order to keep it stable.
*  So they're building arches.
*  Yep, they're building arches.
*  Yeah, that's cool.
*  That was one of the things we really hoped to see
*  when we started the project.
*  We were like, can we get agents to build arches?
*  And because that seems like, I mean, that was,
*  I mean, obviously these aren't real arches, you know,
*  it was a feat of human engineering to figure out
*  how to curve them and like place the keystone or whatever.
*  But we were like, okay, like a simple version of that,
*  that still seems like it would be a nice like illustration
*  of that the agent knows something about construction
*  as if it can build arches and it can.
*  What's next, flying buttresses?
*  Probably that's a bit far off.
*  Okay.
*  But I think, I mean, I would like to see the agents
*  continuing to do, you know, harder versions of these scenes.
*  So in these tasks, like the largest scenes that we had
*  had like 40 to 50 objects in them.
*  But I mean, humans like construct things
*  with many more parts to them.
*  And part of the reason we're able to do that
*  is with, you know, using things like abstractions,
*  like we build this part and then we build this part
*  and then we can compose those and like larger parts together.
*  So I'd like to see agents being able to solve even larger
*  and more difficult scenes.
*  I think exploring like other types of physics
*  would also be super interesting.
*  So, you know, here this is like really just like statically
*  placed objects that can maybe fall over,
*  but you know, you could consider like other sorts
*  of moving objects or like, you know, even like maybe
*  deformables or liquids or these sorts of things
*  would be interesting to have agents that build in a way
*  that also has to be aware of these other different types
*  of dynamics.
*  Well, there's like so much more to talk about here.
*  And, you know, there's a really nice basically survey review
*  that you're a co-author on with, is it Peter Bataldia?
*  Oh, yeah, yeah.
*  Yeah, all about the graph networks.
*  Yes.
*  So I'll link to that paper and of course,
*  the construction paper.
*  So I kind of want to move on just in the interest of time,
*  but do you think, first of all,
*  are you all in on graph networks?
*  Yes.
*  And do you think when you now you're approaching a problem,
*  do you think how could I implement this in a graph network?
*  Is that your sort of your first mode
*  of approaching something?
*  Yeah, I mean, I don't think a graph network
*  is always necessarily the right idea,
*  but I sort of I treat it as like another tool
*  that's in the toolbox, just like,
*  one of the things that we, you know,
*  we tried to like argue for in the review paper
*  was that in deep learning,
*  we have these sort of standard, you know,
*  deep learning components like RNNs and CNNs and MLPs
*  and why not have graph network as another sort of standard
*  tool in the toolbox?
*  Some problems will just call for that
*  and that then you should use it in those cases.
*  So I sort of consider it as like one of the many possibilities
*  that I could use when approaching a problem.
*  But one of the advantages, if I remember correctly,
*  if I'm reading it right, is that a graph network
*  can kind of encompass all of the properties
*  of each of those other types of networks, right?
*  And handle the tasks that are,
*  you would traditionally use those networks for,
*  a graph network can kind of handle all of them.
*  Am I wrong?
*  Well, so in some sense, yes,
*  but I think practically speaking, no.
*  So, well, so I would say like MLPs
*  are actually quite different from-
*  Multilayer perceptron is what you mean by MLPs.
*  Oh, yeah.
*  Yeah, and multilayer perceptron is actually,
*  like a graph network uses,
*  usually uses multilayer perceptrons inside of it.
*  So I think, you know, multilayer perceptrons
*  still like make a lot of sense if like your input data
*  is like literally just a vector that has a fixed size
*  and you want a vector as output that's a fixed size
*  and you don't know anything in particular
*  about like the structure of that data.
*  And that's basically like the assumption
*  that we're making inside the graph networks themselves
*  is that for the nodes and the edges, like their attributes,
*  we're not assuming any particular structure
*  in those representations.
*  And so we're gonna process them with MLPs.
*  Yeah, okay.
*  But then you can kind of see like RNNs
*  as like maybe a particular type of graph network
*  because it's a sequence.
*  But you know, the way that they've been developed,
*  I think there's a lot of very different architectural choices
*  or like smaller architectural choices
*  that make these models actually like quite different
*  from one another.
*  So like even though it's sort of maybe at like a high level,
*  you might be able to use the same language to describe them.
*  I would sort of like treat them practically
*  as different things.
*  Okay, so here's an unfair question.
*  How do you map graph networks onto brains?
*  That is a bit of an unfair question
*  because I didn't do my PhD in neuroscience.
*  Well, okay, so a bit of the real question, I suppose,
*  is is there, I mean, so deep learning networks,
*  everyone says that's how cortex works,
*  which is gonna be wrong.
*  But so there is kind of this mapping onto like,
*  well, okay, a deep network and the hierarchy
*  in a deep network can map onto hierarchies
*  in different brain regions as you process an image,
*  for instance, up to the image object recognition.
*  So there's some at least similarity
*  between the structure of like some types
*  of hierarchical convolutional neural networks and brains.
*  So I guess the question is,
*  do you think at all in terms of is this brain like at all,
*  or is this even, I guess,
*  do you think more on the psychological level
*  and is this how the processing works at a psychological level
*  or do brains even come into the picture?
*  Yeah, I think more about it at the psychological level,
*  like we know psychologically speaking,
*  that people think relationally
*  and like we were talking about earlier,
*  like graphs play an important role.
*  But yeah, just because my background
*  is not really in neuroscience, I don't really.
*  That doesn't mean you can't claim things about the brain,
*  everyone else does, come on.
*  Well, I try to not claim too much about things
*  that I don't know too much about.
*  But so I wouldn't wanna make any strong claims
*  about how graph networks might be instantiated neurally.
*  I mean, it wouldn't surprise me
*  if perhaps you could find like relational structures
*  in the brain too.
*  And I mean, certainly like the brain is,
*  you can represent it as a connective graph,
*  at least loosely speaking.
*  So perhaps there's something interesting there.
*  But yeah, I don't wanna speculate too much about that
*  because I don't know so much about it.
*  I was trying to trap you there, okay.
*  Sorry.
*  So just a transition here
*  because I really wanna talk about this mental simulation
*  review that you've written.
*  So everything that we've been talking about with your work
*  has been physical construction.
*  You mentioned something at the very beginning that it,
*  or maybe I just inferred this from what you were saying,
*  that it doesn't necessarily need to apply
*  to physical construction,
*  that it could apply to abstract concepts as well
*  and using the constructing new ideas
*  from other abstract concepts.
*  Yeah.
*  So maybe this is a good time
*  to talk about mental simulation then.
*  So you wrote a great little review
*  of how mental simulation could be carried out
*  in the deep learning regime.
*  It's called analogs of mental simulation in deep learning
*  in current opinion of behavioral sciences.
*  I highly recommend it.
*  And the figures are really well done.
*  Like I said, it shows, I think that this really,
*  your teaching ability really comes through
*  in just how well the figures are put together
*  and how well it's communicated.
*  So.
*  Oh, thank you.
*  I appreciate that.
*  Yeah, yeah, of course.
*  Okay, so mental simulation you define as constructing,
*  there's that word again, mental models
*  to imagine what will happen or what could be.
*  And of course we do a lot of mental simulation as humans.
*  So what are some behaviors
*  that do and don't require mental simulation?
*  Well, it's a bit of a thorny question to answer just,
*  because if you know anything about the history
*  of mental simulation in psychology,
*  you'll know that it's fraught with debates
*  about what exactly is mental simulation.
*  So it sort of depends a little bit on who you ask.
*  But yeah, I mean, my definition is basically the one
*  that you just gave, which is that it's the ability
*  to make predictions about either future states of the world
*  or alternate states of the world.
*  So like the way that the world could be.
*  And there's an additional component to it,
*  which I didn't get so much into the review article
*  because just because of space constraints,
*  but that there's a notion of which it can also,
*  is something that can be kind of applied iteratively.
*  So mental simulation is like,
*  you can imagine what would happen if I like, say,
*  like throw this ball at a window and then you could say,
*  okay, well, I can imagine maybe the window will break
*  and whoever's house it is is gonna be upset with me.
*  And then I can say, okay, what's gonna happen after that?
*  Well, maybe they'll like, try to like,
*  get me to repair the window or pay for it or whatever.
*  You can keep doing this.
*  You can say, okay, what will happen after that?
*  And after that, and after that.
*  So you run it again, yeah.
*  And eventually you have one where you become
*  really good friends with a person's window,
*  breaking the person who broke their window, yeah.
*  Yeah, exactly.
*  And that's sort of in contrast to,
*  there's other types of thought,
*  which are heuristic judgments might fall into this.
*  So it doesn't necessarily have to use the word heuristic,
*  just anything that may give you a prediction,
*  but can't necessarily be applied iteratively in this way.
*  So, for example, in some of the previous work
*  that I mentioned earlier, where we were looking at,
*  how people make predictions of where blocks will fall
*  and stuff, we found that if we asked them to make
*  a prediction very far in the future,
*  like how far out are the blocks going to fall,
*  as opposed to just saying, will the blocks fall or not?
*  People didn't seem to be using mental simulation so much
*  in those cases, they were using just the heuristic of,
*  if the tower is taller, then the blocks will fall further.
*  And that gives you a pretty good prediction,
*  but it doesn't tell you anything else about it.
*  If I just say, okay, it's tall,
*  so the blocks are gonna fall far.
*  But then I can't say, okay, then let me apply that again.
*  It's like a no-op, right?
*  It doesn't give you any additional information beyond that.
*  So that's kind of the distinction that I like to make.
*  Okay.
*  So, okay, so one challenge with mental simulation
*  is that we don't even know how to represent it.
*  We don't know how humans do it, really.
*  Yeah. And like you're saying,
*  there's this fraught, I guess,
*  historical debate on how humans do it.
*  So, I don't know, if we can, let's just start with
*  natural human-animal mental simulation.
*  So, the examples that you use in the paper
*  are mental imagery, like rotating objects in your mind
*  is kind of the classic one.
*  You also talk about learning by thinking,
*  which is an example of that would be
*  simulating practicing the piano in your head,
*  and then the next day, you're actually better
*  at the piano piece that you're simulating.
*  So it sort of improves your skills just by simulating it.
*  And then the third example is the control of simulation,
*  which you've done research on,
*  and that is whether to even simulate
*  or whether or not to simulate,
*  like the example that you're just describing.
*  So I'd like to use one of these
*  to sort of tie into the work in AI.
*  Is mental imagery the easiest
*  or do you want to talk about the meta control?
*  Well, I guess it sort of depends on which aspect of AI
*  you want to talk about,
*  because I see the meta control is very closely tied
*  to the questions surrounding planning
*  and things like mental imagery are more tied to
*  what are the representations that we use to learn
*  for the world.
*  Well, let me ask about, okay,
*  so you talked about the different,
*  sort of the debate on how these things
*  are represented in our minds.
*  You want to just talk about a few of the examples
*  in the case of mental imagery then?
*  Sure.
*  So the classic debates of mental imagery,
*  sort of the work on mental imagery sort of started with
*  the rotating of these 3D objects
*  with the work of Shepard and Metzler from the 70s.
*  Tetris-like 3D objects.
*  Yeah, exactly.
*  And sort of the conclusion from those experiments was
*  the way, so the actual experiment there is
*  you see these two images
*  of these tetris 3D-like objects,
*  you have to decide is it the same object in each image
*  or are they different objects?
*  And they're either the same
*  and that they differ by rotation or they're different
*  in that one is like a mirror image object of the other.
*  And the conclusion from the experiments is that people
*  mentally imagine the objects rotating
*  in order to compare them, the same or not.
*  And so this sort of kicked off this whole literature
*  of work on mental imagery of looking at like,
*  okay, tell people to imagine that they're looking at a map
*  and that they're looking at the house.
*  So you get people to memorize a map and you say like,
*  okay, you're looking at the house.
*  Now imagine that you are looking at the lake
*  and you see the amount of time it takes people to say,
*  okay, I'm now looking at the lake is different,
*  depending on how far away the lake is from the house.
*  Or like you can say, okay, imagine like
*  that you're looking at this image,
*  but it's like, it's really up close.
*  And then you can say, okay, imagine that you like zoom
*  away from that image.
*  These are all sort of these like manipulations
*  of these images that people have done experiments on.
*  And a lot of this is the work of like Stephen Cossland
*  and others.
*  So Cossland's take on the results of these experiments
*  is that people are doing mental simulation
*  actually on something that is image like.
*  So it might not necessarily be exactly an image,
*  but it's like a 2D spatial array,
*  it has image like properties and spatial.
*  But then there's sort of like another view
*  of this phenomena, which is that,
*  so this is like primarily the view positive by pollution,
*  saying that actually the computations
*  that people are performing are symbolic in nature
*  and this like sense of the mental imagery that we have
*  is just epiphenomenal.
*  It's just sort of like, it's a side effect
*  of the actual thing that's happening,
*  but it doesn't actually have any causal influence on it.
*  Interesting.
*  And so those are sort of the two main theories.
*  And this debate's like, they started in the 80s
*  and I mean, I don't think they've actually
*  technically been resolved.
*  They just kind of moved on, yeah.
*  Yeah, I think most people in the literature
*  tend to accept Cossland's view of things,
*  but yeah, there's not ever been any official resolution
*  to the debate.
*  The 2D map essentially.
*  The 2D spatial, yeah.
*  And that's because I think Cossland did a lot of also like,
*  so the earlier stuff was all behavioral experiments
*  and then he went on to do a lot of neuroscience experiments
*  with fMRI too, showing that there's a lot
*  of shared activation with actual perception
*  and visual imagery.
*  And so I think that convinced a lot of people.
*  Beyond the thought experiments, I suppose.
*  Yeah, yeah.
*  So my feeling on these whole debates are that they're,
*  I think that there's some like,
*  okay, so let me talk a little bit about
*  the review article now because I think
*  if you come at these sorts of questions,
*  so you sort of take this whole debate
*  and put it aside for a moment and you say like,
*  okay, let's think about like,
*  what is just like mental imagery in general?
*  So if we say, you know, like mental simulation
*  is this idea that of making like predictions
*  about like future states or alternate states.
*  And then you say, okay, what is that?
*  Like, what does that look like in the context of AI?
*  Then you end up in the realm of like model-based RL,
*  basically.
*  So this is like the bulk of what the paper is about
*  is how you map these mental simulation
*  within the reinforcement learning world.
*  Yeah.
*  So I'll say, I think that by looking at how AI views this,
*  it tells us something maybe about the debates
*  that people have been having in mental imagery.
*  So we'll come back to that in just a moment
*  after I described like what it is in AI.
*  Okay, so model-based RL, the idea is, or planning,
*  I mean, they're technically separate,
*  but they're similar.
*  Okay.
*  So we can treat them as the same for now.
*  Same thing, for this show, same thing, yeah.
*  So model-based RL is the idea
*  that you have a model of the world
*  and that's a function that it takes in a state of the world
*  and it gives you, maybe it also takes an action
*  that you might apply to the world
*  and it gives you another state of the world.
*  So that might be if I have a block
*  and so the state of the world is like the block
*  is on the table, it's at a particular location on the table
*  and then the action is like lift,
*  then the resulting state of the world would be now
*  like the block is in my hand
*  and it's above the table or something.
*  Right.
*  So that model of the world just gives you the predictions
*  of what's going to happen next
*  and then you can use those models
*  in the context of actual decision-making and acting
*  by using them inside a planning loop.
*  So you can say, okay, let me try it,
*  let me use my model of the world to predict
*  what would happen if I take different actions
*  and I can pick the best action as a result of that.
*  So you run the simulation.
*  Exactly, you imagine.
*  But then if you actually look at the whole literature,
*  there's lots of different choices that people make
*  for how to actually come up with these models of the world.
*  So for example, one approach that some people have taken
*  is to say, okay, you get your images from your robot camera
*  and you just learn to predict the next image.
*  And so you don't worry about anything
*  about the underlying representation,
*  you're just trying to predict the pixels
*  of what's gonna happen next.
*  But then there's other approaches that say,
*  no, we wanna actually have a more structured,
*  latent representation.
*  And so they say, okay, we're going to first encode the image
*  as some high dimensional hidden vector
*  and then we'll make predictions on that vector
*  rather than on the image directly.
*  So that's still more of an unstructured way
*  of predicting the future, but it's more structured
*  in that you're at least assuming there's some
*  lower dimensional latent representation
*  than the image itself.
*  It's still high dimensional,
*  but lower dimensional than the image, I guess.
*  Predicting the hidden state, sort of.
*  Predicting the hidden state, exactly.
*  But then you could also then say,
*  okay, let's assume more forms of structure
*  on that hidden state than just a tensor.
*  So you could say, okay, well, what if that hidden state
*  is a graph and then you could maybe learn the forward model
*  using a graph network.
*  Or maybe if you know something about what is the process
*  that you're trying to model,
*  if you know it's physical dynamics,
*  maybe you say, okay, I'm gonna assume my latent state is...
*  So if you know, for example, that you're trying to predict
*  the motion of one object, but you don't know things
*  like it's mass or whatever, then you could say,
*  my latent state is the position and the velocity
*  and the mass and I have to make predictions
*  about how that changes over time.
*  So you can sort of, again, go on the spectrum
*  of more or less structured on the internal state
*  or the hidden state in ways that either look more symbolic
*  or more kind of distributed representations.
*  And then if you don't have the hidden state at all,
*  you're at something which feels much more spatial.
*  And so now if you take this back
*  to the mental imagery debates, it kind of seems almost like,
*  maybe when people argue for having a spatial representation
*  of mental imagery, what they're talking about is
*  actually making predictions at this image level.
*  And when you're talking about having mental simulation
*  be about propositional representations,
*  you're actually making predictions at a latent space,
*  which is more symbolically structured.
*  But it also reveals something else,
*  which is that you don't necessarily have to have
*  one or the other, right?
*  You could say like, you can make predictions
*  in the hidden state using symbolic representations,
*  but they convert them back to images
*  and then use that as a way of gauging,
*  are my predictions good or not?
*  Because you can say it does look like the thing
*  that should be happening
*  or it doesn't look like the thing should be happening.
*  So it's kind of like, it sort of,
*  it provides a very interesting perspective
*  onto that whole debate, I think, by sort of grounding it
*  in what are the actual computations that are happening.
*  Is the answer to, does it do it this way
*  or does it do it that way?
*  Is the answer always yes to both?
*  Yes.
*  It always is, isn't it?
*  I think so.
*  Yeah, I mean, I think a lot of times,
*  like with these debates,
*  people care about different aspects to the question.
*  And so it's usually people are not asking about
*  like this specific thing, is it X or Y?
*  They're asking, you have this like larger question
*  and like, here's one aspect of it on one side
*  and another aspect of it on the other side.
*  And like someone's talking about how one part of it works
*  and the other person talking about
*  how the other part of it works.
*  And so they might both be right
*  because they're both different aspects of the same problem.
*  This is one of the reasons why I really like
*  computational modeling in general,
*  just because I feel like it forces you
*  to really make concrete
*  what is the thing that you're talking about.
*  So if you say like,
*  the computations that are happening are image-based,
*  then you have to actually like write down
*  the computations that are image-based
*  and show how that, you know,
*  gives you the result that you care about.
*  And actually to be fair, Coslin did do this.
*  He has like a, I think like the early 90s
*  has like a computational model,
*  which looks actually quite a lot like, you know,
*  transformations that you might apply directly to an image.
*  So.
*  I mean, you've been talking about it
*  in terms of these two kind of different,
*  these two different debated theories
*  about how we represent mental imagery.
*  But then there's a third also that has,
*  it's called the inactive that has to do with
*  coupling the imagery to actions strongly, essentially.
*  Yeah.
*  So this was actually like,
*  it was a while before I discovered
*  the inactive theory of mental simulation.
*  Like I went and read all these debates
*  and during the whole thing,
*  I kind of, I was like,
*  what about like the actions that people take?
*  Like, doesn't that matter?
*  And then I finally like eventually stumbled
*  upon the inactive theory and I was like,
*  oh yeah, this is like, here's people talking about this.
*  Because it's not just about the fact like, you know,
*  mental simulation isn't just like making predictions
*  about the world.
*  Like the reason why we make predictions
*  is so we can act better.
*  Yeah.
*  Like that's the point of it.
*  And so if you're not talking about that,
*  then you know, you're missing like the reason why,
*  you're missing something important about like,
*  like a reason why we might have
*  particular types of representations
*  or the reason why we might have different structures
*  in our computations is might be because of like the actions
*  that we're trying to produce.
*  And so, you know, the inactive theory actually looks,
*  I think a lot more like model-based RL.
*  It uses more like the computational versions
*  of like inactive theories tend to use older sorts
*  of techniques like Kalman filters and stuff to explain
*  the way the actions are produced.
*  And so they apply a little bit more to like, I guess,
*  like low level motor control types of things.
*  But I think, you know, using sort of like
*  the general framework of like ideas and model-based RL,
*  either ranging from the low level motor control side
*  to like higher level theories of cognition,
*  I think is like a really promising way to sort of unify
*  all of these different competing views.
*  So, okay.
*  We're running out of time here, so I have to move on.
*  So again, one of the things that we didn't talk about
*  in this article is, you know,
*  you talk about a partially observed Markov decision process
*  as the basis for all these things and how it ties it in.
*  And so I recommend this article that you wrote,
*  even just as a really overview
*  of reinforcement learning based methods,
*  because it's so clearly explained.
*  So again, just, I mean, thanks for writing it.
*  And it's exciting thinking about the possibilities
*  and it makes a lot of sense to use these methods
*  for mental simulation.
*  So carry on the good work.
*  Thanks.
*  So are you doing Jupiter work these days?
*  You've done a lot of work in the realm of Jupiter notebooks.
*  Yes, I am still doing that.
*  You are, okay.
*  Yes.
*  So when I was in grad school,
*  I started this one project
*  that's part of the Jupiter ecosystem called EnvyGrader,
*  which is, it's a tool for creating assignments
*  in Jupiter notebooks and then like doing the grading
*  and also like it's then morphed into something
*  that also handles all like the file distribution
*  and all of these things that surround like having graded
*  assignments in the notebook.
*  And so I still continue to maintain that project.
*  We actually just, I just made a release of the next release
*  of that EnvyGrader version 0.6 this weekend.
*  This is essentially volunteer work, right?
*  Yes, yeah.
*  That's so great, yeah.
*  Yeah, I really enjoy doing it.
*  It's nice to, I feel like contribute to open source projects
*  like and have something that can then be used by everyone
*  and shared by everyone.
*  So it's really satisfying to me
*  to work on these sorts of things.
*  Yeah, I mean, that's a passion of yours
*  that we can't get too much into with the open source.
*  I know that you have a longstanding passion for that.
*  You don't keep your blog up these days though, however.
*  No, it's too many things to do.
*  It's too many things to do, yeah.
*  What's something that you wish you knew going into,
*  let's say undergrad or graduate school?
*  That's a good question.
*  I think that one thing I wish I had known,
*  I keep having to remind myself of this,
*  is that there's so much interesting stuff
*  that people come at from very different perspectives.
*  Even if that perspective is super, super different,
*  that it can be a really valuable thing to go
*  and read about that and then try to take those insights.
*  So I feel like with graph networks
*  as a little bit of an example of this.
*  I wasn't really doing anything with graph theory.
*  These are methods that come out of people
*  who are working more on graph theory types of things.
*  But it turns out to be something that's very general purpose
*  and very useful for the types of problems that I care about.
*  And so I think the same thing with RL.
*  I wish I had started working on RL
*  much earlier in grad school, but I was kind of like,
*  oh, it's like this AI thing.
*  I knew a little bit about it.
*  I took a class in RL when I was in undergrad,
*  but I somehow just didn't really come to appreciate
*  that it was useful.
*  And so I wish I had known to just revisit concepts
*  that might seem not that relevant.
*  I'm coming to terms with the fact that I think that you never
*  appreciate anything first pass, second pass, third pass.
*  You have to actually almost be an expert in something
*  before you appreciate it.
*  And so it's like you have to revisit these concepts
*  over and over and over to then realize,
*  oh, this is important for this various other reason.
*  I don't know if I'm just a really slow learner
*  or if that's just a universal rule.
*  I think it might be a bit of a universal rule.
*  But I think one thing that can help, I think,
*  is to talk to people who are experts
*  and really passionate in those areas.
*  Because it's like you go and you read, I don't know,
*  at least for me, if I go and I read a textbook or a paper
*  or even a blog post on something
*  that I'm not really that familiar with,
*  and that doesn't seem that immediately relevant,
*  I'm like, oh, okay, that seems interesting, I guess,
*  but it's not really that relevant to me.
*  But then if I go and talk to a person
*  who's an expert in that and they're really excited
*  about what they're working on, and then we talk,
*  and then the connections start to come out from that,
*  I think.
*  And that can be really motivating in a good way to do it,
*  even if you don't really know that much about that area.
*  Yeah, I guess one way to think of it is that
*  when you become more, when you become more of an expert
*  in a given area, then all of a sudden,
*  things in other areas look different
*  and you can use them in different ways.
*  You realize you can. Yeah, yeah.
*  How would you, I mean, this is not an easy question,
*  how would you advise someone in undergraduate
*  that's interested in the interface of AI and let's say,
*  we'll just call it natural intelligence.
*  How would you advise them to proceed?
*  What should they do with their formal education
*  versus their self education, for example?
*  Yeah, I think the answer now might look
*  a little bit different from when I was an undergrad,
*  which makes it harder to answer.
*  Yes, it's hard, yeah.
*  Yeah, I think it's very important to stay abreast
*  of both fields, but also I think I would caution
*  not to try to be too in the middle.
*  So at the very beginning of this,
*  we're talking about how I'm kind of right
*  in the middle of both fields, but really-
*  Don't do what I did, yeah.
*  Well, no, but it's more of like an average.
*  I would say on average, you should be in the middle,
*  but spend some time being an expert in something
*  in neuroscience or cognitive science
*  and know that area really well,
*  and then go and spend some time learning about something
*  on the AI side and know that really well.
*  That will give you expertise in both areas,
*  and people then can respect the work
*  that you're doing in both areas,
*  and you'll see the connections between them.
*  But I think trying to do something squarely,
*  always at the middle, is probably really hard
*  because you don't get full expertise in either area.
*  And I think also then it's just a bit distracting
*  because there's so much stuff to have to know about
*  on either side.
*  But if you could just say, I'm gonna ignore everything
*  on the AI side for now and just focus on the problems
*  that are relevant to human cognition,
*  or I'm gonna ignore everything on the human cognition side
*  and just care about the problems that are relevant to AI,
*  I think that's the easier to become an expertise
*  or gather expertise in both areas that way.
*  I really like that.
*  Do you think you should do them in serial or in parallel?
*  I guess you have to do it serially, sort of.
*  Yeah, I probably serially, or at least with a,
*  if you do it, I mean, it's definitely possible
*  to have more than one project going on at a time,
*  but I would say probably the majority of your time
*  should be spent on one side versus the other,
*  with maybe a little bit on the other side.
*  I like that, and then you average out right in the middle,
*  just like you.
*  Yeah, exactly.
*  What's one trait of our intelligence or cognition
*  that you think will be really hard to build into AI,
*  general AI or AI?
*  I could spend a long time talking about that one, actually.
*  But I think, so simply is to say,
*  strong generalization outside the training set.
*  I think there's something very unique about human cognition
*  where we can think of ideas that are just so far-fetched
*  and far removed from anything
*  that we have actually experienced.
*  We can say, oh, what would it be like if we went to the moon?
*  How is it that we came up with that sort of idea?
*  That's not something an AI can come up with,
*  because it's...
*  Yet.
*  Yet.
*  Hopefully, eventually, it could come up
*  with those sorts of ideas,
*  but we just are able to transport
*  ourselves mentally into these completely different worlds
*  than the ones that we actually inhabit.
*  And that seems to be a really powerful part of cognition
*  that AI really struggles with at the moment.
*  And I think it'll take us a long time until we get there.
*  How do you think we'll view deep learning
*  in the history of AI,
*  let's say 30 years from now or something?
*  I hope that we will view it more favorably
*  than people tend to view, I guess, good old-fashioned AI.
*  Let me rephrase that,
*  because I actually have a pretty favorable view
*  of good old-fashioned AI.
*  I think it was actually an incredibly useful stepping stone
*  to get to where we are now.
*  And even today, a lot of our fancy methods,
*  like AlphaGo, for example,
*  use methods from good old-fashioned AI.
*  And so I hope in 30 years,
*  it'll be something similar where we'll have
*  a new class of methods that we're using,
*  but we wouldn't have been able to get there
*  without all of the innovations
*  that we're making right now in deep learning.
*  So the most, maybe five years ago,
*  everyone's like, oh, deep learning, it's the thing.
*  But now people are like,
*  oh, whoa, deep learning is not gonna get us there.
*  And we need extra stuff to compositionality
*  and causality and things like this
*  that deep learning won't get us to.
*  So that's kind of why I'm wondering
*  how important of a stepping stone
*  we're gonna imagine it was.
*  Well, I think having the ability to learn,
*  basically, I see deep learning as being a method
*  for acquiring a function approximator,
*  and that's a very, very useful capacity just in general.
*  So I think we're still gonna need to be able
*  to have function approximators in the future.
*  And so I assume we'll probably still be using something
*  that looks a lot like deep learning.
*  I don't know, maybe someone will figure out
*  how to do evolutionary algorithms for everything
*  or something, and then it won't be quite deep learning
*  anymore, but.
*  No, the deep learning people will say,
*  oh, that's just part of deep learning now.
*  Everything's deep learning now.
*  Because it's like a catch-all term.
*  Deep learning is like, I guess,
*  like all of learning basically at the moment.
*  Yeah, yeah.
*  Moving the goalposts.
*  Okay, finally, Jess, do you think that AI
*  will help us understand our subjective awareness?
*  Oh, that's, I have no idea.
*  All right, we will end it there.
*  Okay.
*  I know you're really busy, so I really appreciate
*  all the time, and keep up the great writing
*  and keep up the great work, and so thanks, Jess.
*  Oh, thank you very much for having me.
*  This was really nice to talk to you
*  and to be on the podcast.
*  Brain Inspired is a production of me and you.
*  You can support the show through Patreon
*  for a microscopic two or $4 per month.
*  Go to braininspired.co and find the red Patreon button there.
*  Your contribution will help sustain and improve the show
*  and prohibit any annoying advertisements
*  like you hear on other shows.
*  And if you're interested in learning more about Brain Inspired,
*  and prohibit any annoying advertisements
*  like you hear on other shows,
*  to get in touch with me, email paul at braininspired.co.
*  The music you hear is by The New Year.
*  Find them at thenewyear.net.
*  Thanks for your support.
*  See you next time.
*  ["The New Year"]
*  Mayday, mayday
*  We've left all hating
*  Searching the coffers
*  For empty offers
*  I don't know why
*  You trust the sky
*  You must like your lies from blue eyes
