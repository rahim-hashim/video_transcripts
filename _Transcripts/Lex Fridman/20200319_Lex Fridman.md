---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 5913s
Video Keywords: ['anca dragan', 'berkeley', 'robotics', 'hri', 'human-robot interaction', 'waymo', 'tesla', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 68591
Video Rating: None
Video Description: Anca Dragan is a professor at Berkeley, working on human-robot interaction -- algorithms that look beyond the robot's function in isolation, and generate robot behavior that accounts for interaction and coordination with human beings.

This episode is presented by Cash App. Download it & use code "LexPodcast":
Cash App (App Store): https://apple.co/2sPrUHe
Cash App (Google Play): https://bit.ly/2MlvP5w

PODCAST INFO:
Podcast website:
https://lexfridman.com/podcast
Apple Podcasts:
https://apple.co/2lwqZIr
Spotify:
https://spoti.fi/2nEwCF8
RSS:
https://lexfridman.com/feed/podcast/
Full episodes playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist:
https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

EPISODE LINKS:
Anca's Twitter: https://twitter.com/ancadianadragan
Anca's Website: https://people.eecs.berkeley.edu/~anca/

OUTLINE:
0:00 - Introduction
2:26 - Interest in robotics
5:32 - Computer science
7:32 - Favorite robot
13:25 - How difficult is human-robot interaction?
32:01 - HRI application domains
34:24 - Optimizing the beliefs of humans
45:59 - Difficulty of driving when humans are involved
1:05:02 - Semi-autonomous driving
1:10:39 - How do we specify good rewards?
1:17:30 - Leaked information from human behavior
1:21:59 - Three laws of robotics
1:26:31 - Book recommendation
1:29:02 - If a doctor gave you 5 years to live...
1:32:48 - Small act of kindness
1:34:31 - Meaning of life

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Anca Dragan Human-Robot Interaction and Reward Engineering  Lex Fridman Podcast #81
**Lex Fridman:** [March 19, 2020](https://www.youtube.com/watch?v=iOCfIFBBpVY)
*  The following is a conversation with Anca Jogan, a professor at Berkeley working on human-robot
*  interaction, algorithms that look beyond the robot's function in isolation and generate
*  robot behavior that accounts for interaction and coordination with human beings. She also
*  consults at Waymo, the autonomous vehicle company, but in this conversation she is 100%
*  wearing her Berkeley hat. She is one of the most brilliant and fun roboticists in the world to
*  talk with. I had a tough and crazy day leading up to this conversation, so I was a bit tired,
*  even more so than usual. But almost immediately as she walked in, her energy, passion, and excitement
*  for human-robot interaction was contagious. So I had a lot of fun and really enjoyed this conversation.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  review it with 5 stars on Apple Podcasts, support it on Patreon, or simply connect with me on
*  Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. As usual, I'll do one or two minutes of ads now
*  and never any ads in the middle that can break the flow of the conversation.
*  I hope that works for you and doesn't hurt the listening experience.
*  This show is presented by Cash App, the number one finance app in the App Store. When you get it,
*  use code LEXPODCAST. Cash App lets you send money to friends, buy bitcoin, and invest in the stock
*  market with as little as $1. Since Cash App does fractional share trading, let me mention that the
*  order execution algorithm that works behind the scenes to create the abstraction of fractional
*  orders is an algorithmic marvel. So big props to the Cash App engineers for solving a hard problem
*  that in the end provides an easy interface that takes a step up to the next layer of abstraction
*  over the stock market, making trading more accessible for new investors and diversification
*  much easier. So again, if you get Cash App from the App Store or Google Play and use the code
*  LEXPODCAST, you get $10 and Cash App will also donate $10 to First, an organization that is
*  helping to advance robotics and STEM education for young people around the world. And now,
*  here's my conversation with Enka Drogon. When did you first fall in love with robotics?
*  I think it was a very gradual process and it was somewhat accidental actually because I first
*  started getting into programming when I was a kid and then into math and then into computer science
*  was the thing I was going to do. And then in college, I got into AI and then I applied to the
*  robotics institute at Carnegie Mellon. And I was coming from this little school in Germany that
*  nobody had heard of, but I had spent an exchange semester at Carnegie Mellon. So I had letters
*  from Carnegie Mellon. So that was the only, you know, MIT said no, Berkeley said no, Stanford said
*  that was the only place I got into. So I went there to the robotics institute and I thought that
*  robotics is a really cool way to actually apply the stuff that I knew and love like optimization.
*  So that's how I got into robotics. I have a better story how I got into cars, which is I, you know,
*  I used to do mostly manipulation in my PhD, but now I do kind of a bit of everything application
*  wise, including cars. And I got into cars because I was here in Berkeley
*  while I was a PhD student still for RSS 2014, Peter Beale organized it. And he arranged for,
*  it was Google at the time to give us rides and self-driving cars. And I was in a robot and it was
*  just making decision after decision, the right call. And it was so amazing. So it was a whole
*  different experience, right? Just, I mean, manipulation is so hard. You can't do anything.
*  And there it was. Was it the most magical robot you've ever met? So like for me to
*  meet Google self-driving car for the first time was like a transformative moment.
*  Like I had two moments like that, that and spot mini. I don't know if you met spot mini for
*  Boston Dynamics. I felt like I fell in love or something like it, because I thought I know how
*  a spot mini works, right? It's just, I mean, there's nothing truly special. It's great
*  engineering work, but the anthropomorphism that went on into my brain, that could came to life,
*  like a head, a little arm and it like, and looked at me. He, she looked at me. You know, I don't
*  know, there's a magical connection there. And it made me realize, wow, robots can be so much more
*  than things that manipulate objects. They can be things that have a human connection. Do you have,
*  was the self-driving car at the moment, like, was there a robot that truly sort of inspired you?
*  That was, I remember that experience very viscerally, riding in that car and being just
*  wowed. I, I had the, they gave us a sticker that said I rode in a self-driving car and it had this
*  cute little firefly on it. And, or logo or something. Oh, that was like the smaller one,
*  like the firefly. Yeah. Yeah. The really cute one. Yeah. And, and I put it on my laptop and I had
*  that for years until I finally changed my laptop out. And you know. What about if we walk back,
*  you mentioned optimization, like what beautiful ideas inspired you in math, computer science
*  early on, like why get into this field? It seems like a cold and boring field of math. Like what
*  was exciting to you about it? The thing is I liked math from very early on from
*  fifth grade is when I got into the math Olympiad and all of that. Oh, you competed too. Yeah. This
*  Romania is like our national sport. You gotta understand. So I got into that fairly early and,
*  and it was a little, maybe too just theory with no kind of, I didn't kind of had a,
*  didn't really have a goal. And other than understanding, which was cool. I always like
*  learning and understanding, but there was no, okay, what am I applying this understanding to?
*  And so I think that's how I got into more heavily into computer science. Cause it was,
*  it was kind of math meets something you can do tangibly in the world. Do you remember like the
*  first program you've written? Okay. The first program I've written with, I kind of do it was
*  in cube basic in fourth grade. And it was drawing like a circle. Yeah. That was, I don't know how
*  to do that anymore, but in fourth grade, that's the first thing that they taught me. It was like,
*  you could take a special, I wouldn't say it was an extra, it was in the sense an extra curricular.
*  So you could sign up for, you know, dance or music or programming. And I did the programming
*  thing and my mom was like, what? Why? Did you compete in programming? Like these days,
*  Romania probably that's like a big thing. There's a program and competition. Was that,
*  did that touch you at all? I did a little bit of the computer science Olympian, but not, not as
*  seriously as I did the math Olympian. So it was programming. Yeah. It's basically, here's a hard
*  math problem. Solve it with a computer is kind of the deal. Yeah. It's more like algorithm.
*  Exactly. It's always algorithmic. So I get, you kind of mentioned the Google self-driving car, but
*  outside of that, Oh, what's like, who or what is your favorite robot? Real or fictional that
*  like captivated your imagination throughout. I mean, I guess you kind of alluded to the Google
*  self drive. The firefly was a magical moment, but is there something else? It was on the firefly.
*  It was, I think that was the Lexus by the way. This was back, back then. But yeah. So good question.
*  I, okay. My favorite fictional robot is Wally and I love how amazingly expressive it is. I'm
*  personally thinks a little bit about expressive motion kinds of things you were saying with,
*  you can do this and it's a head and it's the manipulator and what does it all mean?
*  Um, I like to think about that stuff. I love Pixar. I love animation. I love Wally has
*  two big eyes, I think, or no, yeah, it has these, um, these cameras and they move.
*  So yeah, that's it's a, you know, it goes, and then it's super cute. It's yeah, it's, you know,
*  the way it moves is just so expressive. The timing of that motion, the, what it's doing with its arms
*  and what it's doing with these lenses is amazing. And so, um, I've, I've really liked that from the
*  start. And then on top of that, sometimes I shared this, it's a personal story. I share it with people
*  or when I teach about AI or whatnot. Um, my, uh, husband proposed to me by building a Wally
*  and he actuated it. So it's seven degrees of freedom, including the lens thing.
*  And it kind of came in and it had the, he made it have like a, you know, the belly box opening thing.
*  So it just did that. And then it spewed out this, uh, box made out of Legos that open slowly and
*  then bam. Yeah. Yeah. It was, uh, it was quite, quite, it set a bar. It could be like the most
*  impressive thing I've ever heard. Okay. That was special connection to Wally. Long story short,
*  I like Wally cause I like animation and I like robots and I like, uh, you know, the fact that
*  this was, we still have this robot to this day. What, uh, how hard is that problem? Do you think
*  of the expressivity of robots? Like the, with the Boston dynamics, I've never talked to those folks
*  about this particular element. I've talked to them a lot, but it seems to be like almost an accidental
*  side effect for them that they weren't, I don't know if they're faking it. They weren't trying to
*  Okay. They do say that the gripper on it was not intended to be a face.
*  I don't know if that's a honest statement, but I think they're legit. And so do we automatically
*  just anthropomorphize any sub anything we can see about a robot. So like the question is how hard is
*  it to create a Wally type robot that connects so deeply with us humans? What do you think?
*  It's really hard, right? So, um, it depends on what setting. So if you want to
*  do it in this very particular narrow setting where it does only one thing and it's expressive,
*  then you can get an animator, you know, can have Pixar on call, come in, design some trajectories.
*  There was a, Anki had a robot called Cosmo where they put in some of these animations.
*  That part is easy, right? The hard part is doing it not via these kind of handcrafted
*  behaviors, but doing it generally autonomously. Like I want robots. I don't work on just to
*  clarify. I don't, I used to work a lot on this. I don't work on that quite as much these days,
*  but, but have the notion of having robots that, you know, when they pick something up and put it
*  in a place, they can do that with various forms of style, or you can say, well, this robot is,
*  you know, succeeding at this task and it's confident versus it's hesitant versus, you know, maybe it's
*  happy or it's, you know, disappointed about something, some failure that it had, or I think
*  that when robots move, they can communicate so much about internal states or perceived internal
*  states that they have. And I think that's really useful and an element that we'll want in the
*  future because I was reading this article about how kids are, kids are being rude to Alexa
*  because they can be rude to it and it doesn't really get angry, right? It doesn't reply in
*  any way. It just says the same thing. So I think there's, at least for that, for the, for the
*  correct development of children, it's important that these things, you kind of react differently.
*  I also think, you know, you walk in your home and you have a personal robot and if you're really
*  pissed, presumably the robot should kind of behave slightly differently than when you're
*  super happy and excited. But it's really hard because it's, I don't know, you know, the way I
*  would think about it and the way I thought about it when it came to expressing goals or intentions
*  for robots, it's, well, what's really happening is that instead of doing robotics where you have
*  your state and you have your action space and you have your space, the reward function to try and
*  optimize, now you kind of have to expand the notion of state to include this human internal
*  state. What is the person actually perceiving? What do they think about the robots? Something
*  more or rather, and then you have to optimize in that system. And so that means you have to
*  understand how your motion, your actions end up sort of influencing the observer's kind of
*  perception of you. And it's very hard to write math about that. Right. So when you start to think
*  about incorporating the human into the state model, I apologize for the philosophical question,
*  but how complicated are human beings do you think? Like can they be reduced to
*  kind of almost like an object that moves and maybe has some basic intents? Or is there something,
*  do we have to model things like mood and general aggressiveness and time? I mean,
*  all these kinds of human qualities are like game theoretic qualities. Like what's your sense?
*  How complicated is how hard is the problem of human robot interaction?
*  Yeah. Should we talk about what the problem of human robot interaction is?
*  Yeah. This is what is human robot and then talk about how that, yeah. So, and by the way,
*  I'm going to talk about this very particular view of human robot interaction, right? Which is not
*  so much on the social side or on the side of how do you have a good conversation with the robot?
*  What should the robot's appearance be? It turns out that if you make robots taller versus shorter,
*  this has an effect on how people act with them. So I'm not talking about that, but I'm talking
*  about this very kind of narrow thing, which is you take, if you want to take a task that a robot can
*  do in isolation in a lab out there in the world, but in isolation, and now you're asking what does
*  it mean for the robot to be able to do this task for presumably what its actually end goal is,
*  which is to help some person. That ends up changing the problem in two ways. The first
*  way it changes the problem is that the robot is no longer the single agent acting. That you have
*  humans who also take actions in that same space. Cars navigate around people, robots around an
*  office, navigate around the people in that office. If I send the robot to over there in the cafeteria
*  to get me a coffee, then there's probably other people reaching for stuff in the same space.
*  And so now you have your robot and you're in charge of the actions that the robot is taking.
*  Then you have these people who are also making decisions and taking actions in that same space.
*  Even if the robot knows what it should do and all of that, just coexisting with these people,
*  getting the actions to mesh well together, that's the problem number one.
*  Then there's problem number two, which goes back to this notion of if I'm a programmer,
*  I can specify some objective for the robot to go off and optimize and specify the task.
*  But if I put the robot in your home, presumably you might have your own opinions about,
*  well, okay, I want my house clean, but how do I want it cleaned? And how should robot move? How
*  close to me it should come? And all of that. And so I think those are the two differences that you
*  have. You're acting around people and what you should be optimizing for should satisfy the
*  preferences of that end user, not of your programmer who programmed you.
*  And the preferences thing is tricky. So figuring out those preferences, be able to interactively
*  adjust to understand what the human is doing. So really it boils down to understand the humans in
*  order to interact with them and in order to please them. Right. So why is this hard?
*  Yeah. Why is understanding humans hard? So I think there's two tasks about understanding humans that
*  in my mind are very, very similar, but not everyone agrees. So there is the task of being
*  able to just anticipate what people will do. We all know that cars need to do this. Right. We all
*  know that, well, if I navigate around some people, the robot has to get some notion of, okay, where
*  is this person going to be? So that's kind of the prediction side. And then there's what you are
*  saying, satisfying the preferences. Right. So adapting to the person's preferences, knowing what
*  to optimize for, which is more this inference side, this, what does this person want? What is
*  their intent? What are their preferences? And to me, those kind of go together because I think that
*  at the very least, if you can understand, if you can look at human behavior and understand what it
*  is that they want, then that's sort of the key enabler to being able to anticipate what they'll
*  do in the future. Because I think that, you know, we're not arbitrary. We make these decisions that
*  we make, we act in the way we do because we're trying to achieve certain things. And so I think
*  that's the relationship between them. Now, how complicated do these models need to be in order
*  to be able to understand what people want? So we've gotten a long way in robotics with something
*  called inverse reinforcement learning, which is the notion of someone acts demonstrates what,
*  how they want the thing done. What is an inverse reinforcement learning? You just briefly said it.
*  Right. So it's the problem of take human behavior and infer reward function from this. So figure
*  out what it is that that behavior is optimal with respect to. And it's a great way to think about
*  learning human preferences in the sense of, you know, you have a car and the person can drive it
*  and then you can say, well, okay, I can actually learn what the person is optimizing for. I can
*  learn their driving style or you can, you can have people demonstrate how they want the house clean.
*  And then you can say, okay, this is, this is, I'm getting the trade-offs that they're,
*  that they're making. I'm getting the preferences that they want out of this.
*  And so we've been successful in robotics somewhat with this. And it's based on a very simple model
*  of human behavior. It was remarkably simple, which is that human behavior is optimal with respect to
*  whatever it is that people want. Right. So you make that assumption and now you can kind of
*  inverse through. That's why it's called inverse. Well, really optimal control, but, but also
*  inverse reinforcement learning. So this is based on utility maximization in economics. Back in the
*  forties von Neumann-Morgenstein were like, okay, people are making choices by maximizing utility.
*  Go. And then in the late fifties, we had Luce and Shepherd come in and say,
*  people are a little bit noisy and approximate in that process. So they might choose something kind
*  of stochastically with probability proportional to how much utility something has. There's a bit of
*  noise in there. This has translated into robotics and something that we call Boltzmann rationality.
*  So it's a kind of an evolution of inverse reinforcement learning that accounts for,
*  for human noise. And we've had some success with that too, for these tasks where it turns out people
*  act noisily enough that you can't just do vanilla, the vanilla version. Ah, you can account for noise
*  and still infer what, what they seem to want based on this. Then now we're hitting tasks where that's
*  no, not enough. And what's, what are examples of basic tasks? So imagine you're trying to control
*  some robot that's, that's fairly complicated. You're trying to control the robot arm because
*  maybe you're a patient with a motor impairment and you have this wheelchair mounted arm and you're
*  trying to control it around. Or one task that we've looked at with Sergey is, and our students did,
*  is a lunar lander. So I don't know if you know this Atari game, it's called lunar lander.
*  It's really hard. People really suck at landing the thing. Mostly they just crash it left and right.
*  Okay. So this is the kind of task we imagine you're trying to provide some assistance
*  to a person operating such, such a robot where you want the kind of the autonomy to kick in,
*  figure out what it is that you're trying to do and help you do it. It's really hard to do that for
*  say lunar lander because people are all over the place. And so they seem much more noisy than really
*  irrational. That's an example of a task where these models are kind of failing us. And it's
*  not surprising because so we, you know, we talked about the forties utility late fifties, sort of,
*  noisy. Then the seventies came and behavioral economics started being a thing where people are
*  like, no, no, no, no, no. People are not rational. People are messy and emotional and irrational
*  and have all sorts of heuristics that might be domain specific. And they're just, they're just a
*  mess. So, so what do you, so what does my robot do to understand what you want? And it's a very,
*  it's very, that's why it's complicated. It's, you know, for the most part we get away with pretty
*  simple models until we don't. And then the question is, what do you do then? And I've had days when I
*  wanted to pack my bags and go home and switch jobs because it's just, it feels really daunting
*  to make sense of human behavior enough that you can reliably understand what people want,
*  especially as, you know, robot capabilities will continue to get developed. You'll get these
*  systems that are more and more capable of all sorts of things. And then you really want to make
*  sure that you're telling them the right thing to do. What is that thing? Well, read it in human
*  behavior. So if I just sat here quietly and tried to understand something about you by listening to
*  you talk, it would be harder than if I got to say something and ask you and, and interacting control.
*  Can you, can the robot help its understanding of the humor by influencing it, influencing
*  the behavior by actually acting? Yeah, absolutely. So one of the things that's been exciting to me
*  lately is this notion that when you try to, that, that, that when you try to think of the robotics
*  problem as, okay, I have a robot and it needs to optimize for whatever it is that a person wants
*  it to optimize as opposed to maybe what a programmer said. That problem we think of as a human
*  robot collaboration problem in which both agents get to act in which the robot knows less than the
*  human because the human actually has access to, you know, at least implicitly to what it is that
*  they want. They can't write it down, but they can, they can talk about it. They can give all sorts
*  of signals. They can demonstrate and, and, but the robot doesn't need to sit there and passively
*  observe human behavior and try to make sense of it. The robot can act too. And so there's these
*  information gathering actions that the robot can take to sort of solicit responses that are actually
*  informative. So for instance, this is not for the purpose of assisting people, but with kind of back
*  to coordinating with people in cars and all of that. One thing that Dorsa did was, so we were
*  looking at cars being able to navigate around people and you might not know exactly the driving
*  style of a particular individual that's next to you, but you want to change lanes in front of them.
*  Navigating around other humans inside cars. Yeah. Good, good clarification question. So
*  if you have an autonomous car and it's trying to navigate the road around human driven vehicles,
*  similar things, ideas apply to pedestrians as well, but let's just take human driven vehicles.
*  So now you're trying to change a lane. Well, you could be trying to infer the driving style
*  of this person next to you. You'd like to know if they're in particular, if they're sort of aggressive
*  or defensive, if they're going to let you kind of go in or if they're going to not. And, you know,
*  and it's very difficult to just, you know, when, if you think that if you want to head your bets and
*  say, ah, maybe they're actually pretty aggressive, I shouldn't try this. You kind of end up driving
*  next to them and driving next to them, right? And then you, you don't know because you're not actually
*  getting the observations that you get the way someone drives when they're next to you.
*  And they just need to go straight. It's kind of the same regardless of their aggressive or defensive.
*  And so you need to enable the robot to reason about how it might actually be able to
*  gather information by changing the actions that it's taking. And then the robot comes up with these
*  cool things where it kind of nudges towards you and then sees if you're going to slow down or not.
*  Then if you slow down, it sort of updates its model of you and says, okay, you're more on the
*  defensive side. So now I can actually. That's a fascinating dance. That's so, that's so cool
*  that you could use your own actions to gather information. That's a, that feels like an
*  totally open, exciting new world of robotics. I mean, how many people are even thinking about
*  that kind of thing? A handful of us. It's rare because it's, it's actually leveraging human.
*  I mean, most roboticists I've talked to a lot of colleagues and so on are kind of being honest,
*  kind of afraid of humans. Because they're messy and complicated. Right. I understand.
*  Going back to what we were talking about earlier, right now we're kind of in this dilemma of, okay,
*  there are tasks that we can just assume people are approximately rational for and we can figure out
*  what they want. We can figure out their goals. We can figure out their driving styles, whatever.
*  Cool. There are these tasks that we can't. So what do we do? Right. Do we pack our bags and go home?
*  And this one, I've had a little bit of hope recently. And I'm kind of doubting myself because
*  what do I know that, you know, 50 years of behavioral economics hasn't figured out? But maybe
*  it's not really in contradiction with what, with the way that field is headed. But basically one
*  thing that we've been thinking about is instead of kind of giving up and saying people are too
*  crazy and irrational for us to make sense of them, maybe we can give them a bit the benefit
*  of the doubt. And maybe we can think of them as actually being relatively rational, but just under
*  different assumptions about the world, about how the world works, about, you know, they don't have,
*  when we think about rationality, implicit assumption is, oh, they're rational under
*  all the same assumptions and constraints as the robot. Right. What if this is the state of the
*  world? That's what they know. This is the transition function. That's what they know.
*  This is the horizon. That's what they know. But maybe, maybe the kind of this difference,
*  the way, the reason they can seem a little messy and hectic, especially to robots,
*  is that perhaps they just make different assumptions or have different beliefs.
*  So I mean, that's another fascinating idea that this kind of anecdotal desire to say that humans
*  are irrational, perhaps grounded in behavioral economics, is that we just don't understand the
*  constraints and the rewards under which they operate. And so our goal shouldn't be to throw
*  our hands up and say they're irrational. It's to say, let's try to understand what are the constraints,
*  what it is that they must be assuming that makes this behavior make sense.
*  Good life lesson, right? Good life lesson. That's true. It's just outside of robotics.
*  That's just good to, that's communicating with humans. That's just a good, assume that you just
*  don't, sort of empathy, right? It's a, this is maybe there's something you're missing and you,
*  and it's, you know, it especially happens to robots because they're kind of dumb and they don't know
*  things. And oftentimes people are sort of supra-rational and that they actually know a lot of things that
*  robots don't. Sometimes like with the lunar lander, the robot, you know, knows much more.
*  So it turns out that if you try to say, look, maybe people are operating this thing, but
*  assuming a much more simplified physics model, because they don't get the complexity of this
*  kind of craft or the robot arm with seven degrees of freedom with these inertias and whatever.
*  So maybe they have this intuitive physics model, which is not, you know, this notion of intuitive
*  physics is something that you studied actually in cognitive science was like Josh Dennenbaum,
*  Tom Griffith's work on this stuff. And, and what we found is that you can actually try to figure out
*  what, what physics model kind of best explains human actions. And then you can use that to sort
*  of correct what it is that they're commanding the craft to do. So they might, you know, be sending
*  the craft somewhere, but instead of executing that action, you can sort of take a step back and
*  say, according to their intuitive, if the world worked according to their intuitive physics model,
*  where do they think that the craft is going? Where are they trying to send it to?
*  And then you can use the real physics, right? The inverse of that to actually figure out what
*  you should do so that you do that instead of where they were actually sending you in the real world.
*  And I kid you not, at work people land the damn thing in, you know, in between the two flags and,
*  and, and all that. So it's not conclusive in any way, but I'd say it's evidence that,
*  yeah, maybe we're kind of underestimating humans in some ways when we're giving up and saying,
*  yeah, they're just crazy noisy. So then you, you, then you try to explicitly try to model the kind
*  of a worldview that they have. That they have. That's right. That's right. And it's not too,
*  I mean, there's things in behavioral economics too, that, that, that for instance, have touched upon
*  the planning horizon. So there's this idea that, there's bounded rationality essentially,
*  and the idea that, well, maybe we work under computational constraints. And I think kind of
*  our view recently has been take the Bellman update in AI and just break it in all sorts of ways by
*  saying state, no, no, no, the person doesn't get to see the real state. Maybe they're estimating
*  somehow transition function. No, no, no, no, no. Even the actual reward evaluation,
*  maybe they're still learning about what it is that they want. Like, like, you know,
*  when you watch Netflix and you know, you have all the things and then you have to pick something.
*  Imagine that, you know, the, the, the AI system interpreted that choice as this is the thing you
*  prefer to see. How are you going to know? You're still trying to figure out what you like, what you
*  don't like, et cetera. So I think it's important to also account for that. So it's not irrationality
*  present doing the right thing under the things that they know. Yeah, that's brilliant. You mentioned
*  recommender systems. What kind of, and we were talking about human robot interaction, what kind
*  of problem spaces are you thinking about? So is it, um, robots like wheeled robots with autonomous
*  vehicles? Is it, uh, object manipulation? Like when you think about human robot interaction in
*  your mind and maybe, uh, I'm sure you can speak for the entire community of human robot interaction
*  for like, what are the problems of interest here is, and does it, um, you know, I, I kind of think of,
*  um, open domain dialogue as human robot interaction. And that happens not in the
*  physical space, but it could just happen in, in the virtual space. So where's, where's the
*  boundaries of this field for you when you're thinking about the things we've been talking
*  about? Yeah. So I, um, I try to find kind of underlying, I don't know what to even call them.
*  I get, try to work on, you know, I might call what I do the kind of working on the foundations
*  of algorithmic human robot interaction and trying to make contributions there. Um, and,
*  and it's important to me that whatever we do is actually somewhat domain agnostic when it comes
*  to, is it about, you know, autonomous cars or is it about quadrotors or is it about, is it sort of
*  the same underlying principles apply? Of course, when you're trying to get a particular domain to
*  work, you usually have to do some extra work to adapt that to that particular domain. But these
*  things that we were talking about around, well, you know, how do you model humans? It turns out
*  that a lot of systems need to benefit from a better understanding of how human behavior relates
*  to what people want and need to predict human behavior, physical robots of all sorts and,
*  and beyond that. And so I used to do manipulation. I used to be, you know, picking up stuff and then
*  it was picking up stuff with people around. And now it's sort of very broad when it comes to the
*  application level, but in a sense, very focused on, okay, how does the problem need to change?
*  How do the algorithms need to change when we're not doing a robot by itself, you know, emptying
*  the dishwasher, but we're stepping outside of that. Oh, I thought that popped into my head just now.
*  On the game theoretic side, I think you said this really interesting idea of using actions to gain
*  more information. But if we think of sort of game theory, the humans that are interacting with you,
*  with you, the robot, I'm thinking the identity of the robot. Yeah, I did that all the time. Yeah.
*  They also have a world model of view and you can manipulate that. I mean, if we look at autonomous
*  vehicles, people have a certain viewpoint. You said with the kids, people see Alexa in a certain way.
*  Is there some value in trying to also optimize how people see you as a robot?
*  Or is that a little too far away from the specifics of what we can solve right now?
*  So, both, right? So, it's really interesting. And we've seen a little bit of progress on this
*  problem, on pieces of this problem. So, you can, again, it kind of comes down to how complicated
*  the human model needs to be. But in one piece of work that we were looking at, we just said,
*  okay, there's these parameters that are internal to the robot and what the robot is about to do
*  or maybe what objective or driving style the robot has or something like that. And what we're
*  going to do is we're going to set up a system where part of the state is the person's belief
*  over those parameters. And now when the robot acts, that the person gets new evidence about
*  this robot internal state. And so, they're updating their mental model of the robot, right? So, if they
*  see a card that sort of cuts someone off, like, oh, that's an aggressive card, they know more, right?
*  If they see sort of a robot head towards a particular door, they're like, oh, yeah, the
*  robot's trying to get to that door. So, this thing that we have to do with humans to try to
*  understand their goals and intentions, humans are inevitably going to do that to robots. And then
*  that raises this interesting question that you asked, which is, can we do something about that?
*  This is going to happen inevitably, but we can sort of be more confusing or less confusing to
*  people. And it turns out you can optimize for being more informative and less confusing if you
*  have an understanding of how your actions are being interpreted by the human, how they're using
*  these actions to update their belief. And honestly, all we did is just Bayes' rule. Basically, okay,
*  the person has a belief, they see an action, they make some assumptions about how the robot generates
*  its actions, presumably as being rational, because robots are rational, it's reasonable to assume
*  that about them. And then they incorporate that new piece of evidence, in the Bayesian sense,
*  in their belief, and they obtain a posterior. And now the robot is trying to figure out what
*  actions to take, such that it steers the person's belief to put as much probability mass as possible
*  on the correct parameters. So, that's kind of a mathematical
*  formalization of that. But my worry, and I don't know if you want to go there with me, but I talk
*  about this quite a bit. The kids talking to Alexa disrespectfully worries me. I worry in general
*  about human nature. Like I said, I grew up in Soviet Union, World War II, I'm a Jew too, so with
*  the Holocaust and everything. I just worry about how we humans sometimes treat the other, the group
*  that we call the other, whatever it is. The human history, the group that's the other has been
*  changed faces. But it seems like the robot will be the other, the next the other. And
*  one thing is, it feels to me that robots don't get no respect.
*  They get shoved around.
*  Shoved around. And is there one, at the shallow level, for better experience, it seems that robots
*  need to talk back a little bit. Like my intuition says, I mean, most companies from Roomba,
*  autonomous vehicle companies might not be so happy with the idea that a robot has a little bit of an
*  attitude. But I feel, it feels to me that that's necessary to create a compelling experience. Like
*  we humans don't seem to respect anything that doesn't give us some attitude. Or like a mix
*  of mystery and attitude and anger that threatens us subtly, maybe passive aggressively. I don't,
*  it seems like we humans need that. What are your, is there something, you have thoughts on this?
*  I'll give you two thoughts on this. One is, we respond to someone being assertive,
*  but we also respond to someone being vulnerable. So I think robots, my first thought is that robots
*  get shoved around and bullied a lot because they're sort of tempting and they're sort of showing off
*  or they appear to be showing off. And so I think going back to these things we were talking about
*  in the beginning of making robots a little more expressive, a little bit more like,
*  that wasn't cool to do and now I'm bummed. I think that can actually help because people
*  can't help but anthropomorphize and respond to that. Even that though, the emotion being
*  communicated is not in any way a real thing. And people know that it's not a real thing because
*  they know it's just a machine. We're still interpreting, we watch there's this
*  famous psychology experiment with little triangles and dots on a screen and a triangle is chasing the
*  square and you get really angry at the darn triangle because why is it not leaving the
*  square alone? So that's, yeah, we can't help. So that was the first thought.
*  The vulnerability is really interesting. I think of being pushing back,
*  being assertive as the only mechanism of getting, of forming a connection of getting respect,
*  but perhaps vulnerability. Perhaps there's other mechanisms that are less threatening.
*  Yeah. Well, I think a little bit, yes, but then this other thing that we can think about is,
*  it goes back to what you were saying, that interaction is really game theoretic.
*  Right? So the moment you're taking actions in a space, the humans are taking actions in that same
*  space, but you have your own objective, which is, you're a car, you need to get your passenger to
*  the destination. And then the human nearby has their own objective, which somewhat overlaps with
*  you, but not entirely. You're not interested in getting into an accident with each other,
*  but you have different destinations and you want to get home faster and they want to get home faster.
*  And that's a general sum game at that point. And so I think that's what,
*  treating it as such is kind of a way we can step outside of this kind of mode that where you try
*  to anticipate what people do and you don't realize you have any influence over it, while still
*  protecting yourself because you're understanding that people also understand that they can influence
*  you. And it's just kind of back and forth. There's this negotiation, which is really,
*  really talking about different equilibria of a game. The very basic way to solve coordination
*  is to just make predictions about what people will do and then stay out of their way.
*  And that's hard for the reasons we talked about, which is how you have to understand
*  people's intentions implicitly, explicitly, who knows, but somehow you have to get enough
*  of an understanding of that. We want to anticipate what happens next. And so that's challenging,
*  but then it's further challenged by the fact that people change what they do based on what you do
*  because they don't plan in isolation either. So when you see cars trying to merge on a highway
*  and not succeeding, one of the reasons this can be is because they look at traffic that keeps coming,
*  they predict what these people are planning on doing, which is to just keep going,
*  and then they stay out of the way because there's no feasible plan. Any plan would actually
*  intersect with one of these other people. So that's bad. So you get stuck there.
*  So now if you start thinking about it as no, no, no, actually these people change what they do
*  depending on what the car does. If the car actually tries to inch itself forward, they might actually
*  slow down and let the car in. And now taking advantage of that, well, that's kind of the next
*  level. We call this this underactuated system idea where it's kind of underactuated system robotics,
*  but you influence these other degrees of freedom, but you don't get to decide what they do.
*  I've somewhere seen you mention the human element in this picture as underactuated. So you understand
*  underactuated robotics is that you can't fully control the system. You can't go in arbitrary
*  directions in the configuration space. Under your control. Yeah, it's a very simple way of
*  underactuation where basically there's literally these degrees of freedom that you can control
*  and these degrees of freedom that you can't, but you influence them. And I think that's the important
*  part is that they don't do whatever, regardless of what you do, that what you do influences what
*  they end up doing. I just also like the poetry of calling human-robot interaction an underactuated
*  robotics problem. And you also mentioned sort of nudging. It seems that there, I don't know,
*  I think about this a lot in the case of pedestrians. I've collected hundreds of hours of videos. I like
*  to just watch pedestrians and it seems that it's a funny hobby. Yeah, it's weird because I learn a
*  lot. I learned a lot about myself, about our human behavior from watching pedestrians, watching
*  people in their environment. Basically crossing the street is like you're putting your life on the
*  line, you know, I don't know, tens of millions of time in America every day is people are just like
*  playing this weird game of chicken when they cross the street, especially when there's some
*  ambiguity about the right of way that has to do either with the rules of the road or with the general
*  personality of the intersection based on the time of day and so on. And this nudging idea,
*  it seems that people don't even nudge, they just aggressively make a decision.
*  There's a runner that gave me this advice. I sometimes run in the street, not in the street,
*  on the sidewalk and he said that if you don't make eye contact with people when you're running,
*  they will all move out of your way. It's called civil inattention. Civil inattention, that's a
*  thing. Oh wow, I need to look this up, but it works. What is that? My sense was if you communicate
*  like confidence in your actions that you're unlikely to deviate from the action that you're
*  following, that's a really powerful signal to others that they need to plan around your actions
*  as opposed to nudging where you're sort of hesitantly, the hesitation might communicate
*  that you're still in the dance and the game that they can influence with their own actions.
*  I've recently had a conversation with Jim Keller, who's sort of this
*  legendary chip architect, but he also led the autopilot team for a while. And his intuition
*  that driving is fundamentally still like a ballistics problem. You can ignore the human
*  element that is just not hitting things and you can kind of learn the right dynamics required to
*  do the merger and all those kinds of things. And then my sense is, and I don't know if I can
*  provide sort of definitive proof of this, but my sense is like an order of magnitude are more
*  of magnitude or more difficult when humans are involved. Like it's not simply object
*  collision avoidance problem. Where does your intuition, of course, nobody knows the right
*  answer here, but where does your intuition fall on the difficulty, fundamental difficulty
*  of the driving problem when humans are involved? Yeah. Good question. I have many opinions on this.
*  Yes. Imagine downtown San Francisco. Yeah. Yeah. It's crazy, busy, everything. Okay. Now take all
*  the humans out. No pedestrians, no human driven vehicles, no cyclists, no people on little
*  electric scooters zipping around, nothing. I think we're done. I think driving at that point
*  is done. We're done. There's nothing really that still needs to be solved about that.
*  Let's pause there. I think I agree with you. And I think a lot of people that will hear
*  agree with that, but we need to sort of internalize that idea. So what's the problem there? Because we
*  might not quite yet be done with that. Because a lot of people kind of focus on the perception
*  problem. A lot of people kind of map autonomous driving into how close are we to solving,
*  being able to detect all the, you know, the drivable area, the objects in the scene.
*  Do you see that as a, how hard is that problem? So your intuition there behind your statement was
*  we might have not solved it yet, but we're close to solving basically the perception problem.
*  I think the perception problem, I mean, and by the way, a bunch of years ago, this would not have
*  been true. And a lot of issues in the space were coming from the fact that, oh, we don't really,
*  you know, we don't know what's where. But I think it's fairly safe to say that at this point,
*  although you could always improve on things and all of that, you can drive through downtown San
*  Francisco if there are no people around. There's no really perception issues standing in your way
*  there. I think perception is hard, but yeah, we've made a lot of progress on the perception.
*  And I had to undermine the difficulty of the problem. I think everything about robotics is
*  really difficult, of course. I think the planning problem, the control problem, all very difficult,
*  but I think what makes it really- Yeah. It might be, I mean, you know, and I picked
*  downtown San Francisco, adapting to, well, now it's snowing, now it's no longer snowing,
*  now it's slippery in this way, now it's the dynamics part, I could imagine being
*  still somewhat challenging. But- No, the thing that I think worries us,
*  and our intuition is not good there, is the perception problem at the edge cases.
*  Sort of downtown San Francisco, the nice thing, it's not actually, it may not be a good example
*  because- Because you know what you're getting from, well, there's like crazy construction
*  zones and all that. Yeah, but the thing is you're traveling at slow speeds, so it doesn't feel
*  dangerous. To me, what feels dangerous is highway speeds when everything is, to us humans, super
*  clear. Yeah. I'm assuming lidar here, by the way. I think it's kind of irresponsible to not use lidar.
*  That's just my personal opinion. I mean, depending on your use case, but I think, like, you know,
*  if you have the opportunity to use lidar, in a lot of cases you might not.
*  Good. Your intuition makes more sense now. So you don't think vision-
*  I really just don't know enough to say, well, vision alone, what's like, there's a lot of,
*  how many cameras do you have? Is that how you're using them? I don't know. There's all sorts of
*  details. I imagine there's stuff that's really hard to actually see, how do you deal with
*  glare, exactly what you were saying, stuff that people would see that you don't. I think I have,
*  more of my intuition comes from systems that can actually use lidar as well.
*  Yeah, and until we know for sure it makes sense to be using lidar. That's kind of the safety
*  focus. But then there's sort of the, I also sympathize with the Elon Musk statement of
*  lidar is a crutch. It's a fun notion to think that the things that work today is a crutch
*  for the invention of the things that will work tomorrow, right? Like it, it's kind of true
*  in the sense that if, you know, we want to stick to the comforts, you see this in academic and
*  research settings all the time, the things that work force you to not explore outside,
*  think outside the box. I mean, that happens all the time. The problem is in safety critical
*  systems, you kind of want to stick with the things that work. So it's, it's an interesting
*  and difficult trade off in the, in the, in the case of real world sort of safety critical robotic
*  systems. But so your intuition is just to clarify how, I mean, how hard is this human element?
*  For like, how hard is driving when this human element is involved? Are we
*  years, decades away from solving it? But perhaps actually the year isn't the thing I'm asking. It
*  doesn't matter what the timeline is, but do you think we're, how many breakthroughs are we away
*  from in solving the human-robot interaction problem to get this, to get this right?
*  I think it, in a sense, it really depends. I think that, you know, we were talking about how,
*  well, look, it's really hard because Anticipation of what people do is hard. And on top of that,
*  playing the game is hard. But I think we sort of have the fundamental, some of the fundamental
*  understanding for that. And then you already see that these systems are being deployed in the real
*  world, you know, even, even driverless. Like there's, I think now a few companies that don't
*  have a driver in the car in some small areas. I got a chance to, I went to Phoenix and I,
*  I shot a video with Waymo and he needed to get that video out. People have been giving me slack,
*  but there's incredible engineering work being done there. And it's one of those other seminal
*  moments for me in my life to be able to, it sounds silly, but to be able to drive without a,
*  without a ride, sorry, without a driver in the seat. I mean, that was an incredible robotics.
*  I was driven by a robot without being able to take over, without being able to
*  take the steering wheel. That's a magical, that's a magical moment. So in that regard,
*  in those domains, at least for like Waymo, they're, they're, they're solving that human.
*  There's, I mean, they were, they were going, I mean, it felt fast because you're like freaking
*  out at first. That was, this is my first experience, but it's going like the speed limit, right? 30,
*  40, whatever it is. And there's humans and it deals with them quite well. It detects them and
*  negotiates the intersections, the left turns and all that. So at least in those domains,
*  it's solving them. The open question for me is like, how quickly can we expand?
*  You know, that's the, you know, outside of the weather conditions, all those kinds of things,
*  how quickly can we expand to like cities like San Francisco? Yeah. And I wouldn't say that it's
*  just, you know, now it's just pure engineering and it's probably the, I mean, and by the way,
*  I'm speaking kind of very generally here as hypothesizing, but I, I think that,
*  that there are successes and yet no one is everywhere out there. So that seems to suggest
*  that things can be expanded and can be scaled and we know how to do a lot of things, but there's
*  still probably, you know, new algorithms or modified algorithms that, that you still need
*  to put in there as you, as you learn more and more about new challenges that get, you get faced
*  with. How much of this problem do you think can be learned through end to end? Is it the success of
*  machine learning and reinforcement learning? How much of it can be learned from sort of data from
*  scratch and how much, which most of the success of autonomous vehicle systems have a lot of heuristics
*  and rule-based stuff on top, like human expertise in, in injected forced into the system to make it
*  work. What's your, what's your sense? How much, what's the, what will be the role of learning
*  in the near term? I think, I, I think on the one hand that learning is inevitable here, right?
*  I think on the other hand, that when people characterize the problem as it's a bunch of
*  rules that some people wrote down versus it's an end to end RL system or imitation learning,
*  then maybe there's kind of something missing from maybe that's, that's more. So for instance,
*  I think a very, very useful tool in this sort of problem, both in how to generate the cars behavior
*  and robots in general, and how to model human beings is actually planning search optimization,
*  right? So robotics is a consequential decision making problem. And when, when a robot can
*  figure out on its own how to achieve its goal without hitting stuff and all that stuff,
*  right? All the good stuff for motion planning one-on-one, I think of that as very much AI,
*  not this is some rule or something. There's nothing rule based around that, right? It's just
*  you're, you're searching through a space and figuring out, or you're optimizing through a
*  space and figure out what seems to be the right thing to do. And I think it's hard to just do that
*  because you need to learn models of the world. And I think it's hard to just do the learning part
*  where you don't, you know, you don't bother with any of that because then you're saying, well,
*  I could do imitation, but then when I go off distribution, I'm really screwed. Or you can say,
*  I can do reinforcement learning, which adds a lot of robustness, but then you have to
*  do either reinforcement learning in the real world, which sounds a little challenging,
*  or that trial and error, you know, or you have to do reinforcement learning in simulation.
*  And then that means, well, guess what? You need to model things, at least to, to model people,
*  model the world enough that you, you know, whatever policy you get of that is like actually fine to
*  roll out in the world and do some additional learning there. So.
*  Do you think simulation, by the way, just a quick tangent has a role in the human
*  robot interaction space. Like, is it useful? It seems like humans, everything we've been talking
*  about are difficult to model and simulate. Do you think simulation has a role in this space?
*  I do. I think so because you can take models and train with them ahead of time. For instance,
*  you can. But the models are to interrupt the models are sort of human constructed or learned.
*  I think they have to be a combination because if you get some human data and then you say,
*  this is going to be my model of the person, what are for simulation and training or for
*  just deployment time. And that's what I'm planning with as my model of how people work.
*  Regardless, if you take some data and you don't assume anything else and you just say, okay,
*  this is, this is some data that I've collected. Let me fit a policy to help people work based on
*  that. What does to happen is you collected some data and some distribution, and then now your,
*  your robot sort of computes a best response to that. Right. It's sort of like, what should I do
*  if this is how people work? And easily goes off of distribution where that model that you've built
*  of the human completely sucks because out of distribution, you have no idea. Right. There's,
*  if you think of all the possible policies and then you take only the ones that are consistent with
*  the human data that you've observed, that still leads a lot of, a lot of things could happen
*  outside of that distribution where you're confident and you know what's going on.
*  By the way, that's, I mean, I've gotten used to this terminology of out of a distribution,
*  but it's such a machine learning terminology because it kind of assumes. So distribution
*  is referring to the, the data that you've seen. The set of states that you encounter.
*  They've encountered so far at training time. But it kind of also implies that there's a nice
*  like statistical model that represents that data. So out of distribution feels like, I don't know,
*  it, it, it raises to me philosophical questions of how we humans reason out of distribution,
*  reason about things that are completely we haven't seen before. And so, and what we're
*  talking about here is how do we reason about what other people do in, you know, situations where we
*  haven't seen them and somehow we just magically navigate that. I, you know, I can anticipate what
*  will happen in situations that are even novel in many ways. And I have a pretty good intuition for,
*  I don't always get it right, but you know, and I might be a little uncertain and so on.
*  I think it's, it's this, that if you just rely on data, you know, you, there's, there's just too
*  many possibilities, too many policies out there that fit the data. And by the way, it's not just
*  state, it's really kind of history of state because to really be able to anticipate what the
*  person will do, it kind of depends on what they've been doing so far, because that's the information
*  you need to kind of at least implicitly sort of say, ah, this is the kind of person that this is,
*  this is probably what they're trying to do. So anyway, it's like you're trying to map history
*  of states to actions. There's many mappings. And history meaning like the last few seconds
*  or the last few minutes or the last few months. Who knows, who knows how much you need, right?
*  In terms of if your state is really like the positions of everything or whatnot and velocities,
*  who knows how much you need? And then, and then there's this, there's so many mappings. And so
*  now you're talking about how do you regularize that space? What priors do you impose? Or what's
*  the inductive bias? So, you know, there's all very related things to think about it. Basically,
*  what are assumptions that we should be making such that these models actually generalize outside of
*  the data that we've seen. And now you're talking about, well, I don't know, what can you assume?
*  Maybe you can assume that people like actually have intentions and that's what drives their actions.
*  Maybe that's, you know, the right thing to do when you haven't seen data very nearby that tells you
*  otherwise. I don't know. It's a very open question. Do you think so that one of the dreams of
*  artificial intelligence was to solve common sense reasoning, whatever the heck that means,
*  do you think something like common sense reasoning has to be solved in part to be able to solve this
*  dance of human robot interaction, the driving space or human robot interaction in general?
*  You have to be able to reason about these kinds of common sense concepts of physics, of,
*  you know, all the things we've been talking about humans, I don't even know how to express them with
*  words, but the basics of human behavior, a fear of death. So like, to me, it's really important to
*  encode in some kind of sense, maybe not, maybe it's implicit, but it feels that it's important to
*  explicitly encode the fear of death that people don't want to die because it seems silly, but like
*  it seems silly, but like that, the game of chicken that involves with the pedestrian crossing the
*  street is playing with the idea of mortality. Like we really don't want to die. It's not just like a
*  negative reward. I don't know. It just feels like all these human concepts have to be encoded.
*  Do you share that sense or is this a lot simpler than I'm making out to be? I think it might be
*  simpler and I'm the person who likes to complicate it. I think it might be simpler than that.
*  Because it turns out, for instance, if you say model people in the very,
*  I'll call it traditional, I don't know if it's fair to look at it as a traditional way, but
*  calling people as, okay, they're irrational somehow, the utilitarian perspective. Well,
*  in that, once you say that, you automatically capture that they have an incentive to keep on
*  being. Stuart likes to say, you can't fetch the coffee if you're dead. Stuart Russell, by the way.
*  That's a good line. So when you're sort of treating agents as having these objectives,
*  these incentives, humans or artificial, you're kind of implicitly modeling that they'd like to
*  stick around so that they can accomplish those goals. So I think in a sense, maybe that's what
*  draws me so much to the rationality framework, even though it's so broken. It's been such a useful
*  perspective. And like we were talking about earlier, what's the alternative? I give up and go home or
*  I just use complete black boxes, but then I don't know what to assume out of distribution. I come
*  back to this. It's been a very fruitful way to think about the problem and a very
*  more positive way, right? It's just people aren't just crazy. Maybe they make more sense than we
*  think. But I think we also have to somehow be ready for it to be wrong, be able to detect when
*  these assumptions aren't holding, be all of that stuff. Let me ask sort of another small side of
*  this that we've been talking about the pure autonomous driving problem, but there's also
*  relatively successful systems already deployed out there in what you may call like level two
*  autonomy or semi-autonomous vehicles, whether that's Tesla, autopilot, work quite a bit with
*  Cadillac Super Guru system, which has a driver facing camera that detects your state. There's
*  a bunch of basically lane centering systems. What's your sense about this kind of way of
*  dealing with the human robot interaction problem by having a really dumb robot
*  and relying on the human to help the robot out to keep them both alive?
*  Is that from the research perspective, how difficult is that problem? And from a practical
*  deployment perspective, is that a fruitful way to approach this human robot interaction problem?
*  I think what we have to be careful about there is to not make it seems like some of these systems,
*  not all, are making this underlying assumption that if, so I'm a driver and I'm now really not
*  driving but supervising and my job is to intervene, right? And so we have to be careful with this
*  assumption that if I'm supervising, I will be just as safe as when I'm driving. Like that I will,
*  if I wouldn't get into some kind of accident if I'm driving, I will be able to avoid that accident
*  when I'm supervising too. And I think I'm concerned about this assumption from a few perspectives.
*  So from a technical perspective, it's that when you let something kind of take control and do its
*  thing, and it depends on what that thing is, obviously, and how much it's taking control and
*  how, what things are you trusting it to do. But if you let it do its thing and take control,
*  it will go to what we might call off policy from the person's perspective state. So states that the
*  person wouldn't actually find themselves in if they were the ones driving. And the assumption
*  that the person functions just as well there as they function in the states that they would
*  normally encounter is a little questionable. Now, another part is the kind of the human factor side
*  of this, which is that I don't know about you, but I think I definitely feel like I'm experiencing
*  things very differently when I'm actively engaged in the task versus when I'm a passive observer.
*  Even if I try to stay engaged, right, it's very different than when I'm actually actively making
*  decisions. And you see this in life in general, like you see students who are actively trying to
*  come up with the answer, learn the thing better than when they're passively told the answer.
*  I think that's somewhat related. And I think people have studied this in human factors for
*  airplanes. And I think it's actually fairly established that these two are not the same.
*  So on that point, because I've gotten a huge amount of heat on this and I stand by it.
*  Okay. Because I know the human factors community well.
*  And the work here is really strong and there's many decades of work showing exactly what you're
*  saying. Nevertheless, I've been continuously surprised that much of the predictions of that
*  work has been wrong in what I've seen. So what we have to do, I still agree with everything you said,
*  but we have to be a little bit more open-minded. So I'll tell you, there's a few surprising things
*  that super, like everything you said to the word is actually exactly correct, but it doesn't say
*  what you didn't say is that these systems are, you said you can't assume a bunch of things,
*  but we don't know if these systems are fundamentally unsafe. That's still unknown.
*  There's a lot of interesting things like I'm surprised by the fact, not the fact,
*  what seems to be anecdotally from large data collection that we've done, but also from just
*  talking to a lot of people when in the supervisory role of semi-autonomous systems that are
*  sufficiently dumb, at least, which is the, that might be a key element is the systems have to be
*  dumb. The people are actually more energized as observers. So they're actually better,
*  they're better at observing the situation. So there might be cases in systems, if you get
*  the interaction right, where you, as a supervisor, will do a better job with the system together.
*  I agree. I think that is actually really possible. I guess mainly I'm pointing out that if you
*  do it naively, you're implicitly assuming something, that assumption might actually
*  really be wrong. But I do think that if you explicitly think about
*  what the agent should do such that the person still stays engaged,
*  so that you essentially empower the person to more than they could, that's really the goal.
*  You still have a driver, so you want to empower them to be so much better than they would be
*  by themselves. And that's different. It's a very different mindset than I want them to basically
*  not drive. But be ready to sort of take over. So one of the interesting things we've been talking
*  about is the rewards, that they seem to be fundamental to the way robots behave. So broadly
*  speaking, we've been talking about utility functions, but could you comment on how do we
*  approach the design of reward functions? How do we come up with good reward functions?
*  Really good question, because the answer is we don't. I used to think about how, well,
*  it's actually really hard to specify rewards for interaction because it's really supposed to be
*  what the people want, and then you really, you know, we talked about how you have to customize
*  what you want to do to the end user. But I kind of realized that even if you take the interactive
*  component away, it's still really hard to design reward functions. So what do I mean by that? I
*  mean, if we assume this sort of AI paradigm in which there's an agent and his job is to optimize
*  some objective, some reward, utility, loss, whatever cost. If you write it out, maybe it's
*  a set depending on the situation or whatever it is. If you write it out and then you deploy the agent,
*  you'd want to make sure that whatever you specified incentivizes the behavior you want
*  from the agent in any situation that the agent will be faced with. Right? So I do motion planning
*  on my robot arm. I specify some cost function like, you know, this is how far away you should
*  try to stay. So much about stay away from people and this is how much it matters to be able to be
*  efficient and blah, blah, blah. Right? I need to make sure that whatever I specified those constraints
*  or trade-offs or whatever they are, that when the robot goes and solves that problem in every new
*  situation, that behavior is the behavior that I want to see. And what I've been finding is
*  that we have no idea how to do that. Basically, what I can do is I can sample, I can think of
*  some situations that I think are representative of what the robot will face and I can tune and add
*  and tune some reward function until the optimal behavior is what I want on those situations,
*  which first of all is super frustrating because, you know, through the miracle of AI, we've taken,
*  we don't have to specify rules for behavior anymore. Right? The, who were saying before,
*  the robot comes up with the right thing to do. You plug in the situation, it optimizes,
*  bring that situation, it optimizes, but you have to spend still a lot of time on actually defining
*  what it is that that criterion should be, making sure you didn't forget about 50 bazillion things
*  that are important and how they all should be combining together to tell the robot what's good
*  and what's bad and how good and how bad. And so I think this is a lesson that, I don't know, kind of,
*  I guess I close my eyes to it for a while because I've been, you know, tuning cost functions for 10
*  years now. But it really strikes me that, yeah, we've moved the tuning and the, like, designing of
*  features or whatever from the behavior side into the reward side. And yes, I agree that there's way
*  less of it, but it still seems really hard to anticipate any possible situation and make sure
*  you specify a reward function that when optimized will work well in every possible situation.
*  So you're kind of referring to unintended consequences or just in general, any kind of
*  suboptimal behavior that emerges outside of the things you said, out of distribution.
*  Suboptimal behavior that is, you know, actually optimal. I mean, this, I guess the idea of
*  unintended consequences, you know, it's optimal respect to what you specified, but it's not what
*  you want. And there's a difference between those. But that's not fundamentally a robotics problem,
*  right? That's a human problem. So like- That's the thing. Right? So there's this thing called
*  Goodheart's Law, which is you set a metric for an organization and the moment it becomes
*  on target that people actually optimize for, it's no longer a good metric.
*  What's it called? That's a good heart's law. So the moment you specify a metric,
*  it stops doing its job. Yeah, it stops doing its job. So there's, yeah, there's such a thing as
*  optimizing for things and, you know, failing to think ahead of time of all the possible things
*  that might be important. And so that's interesting because, sorry, I work a lot on reward learning
*  from the perspective of customizing to the end user, but it really seems like it's not just
*  the interaction with the end user that's a problem of the human and the robot collaborating
*  so that the robot can do what the human wants, right? This kind of back and forth, the robot
*  probing, the person being informative, all of that stuff might be actually just as applicable
*  to this kind of maybe new form of human robot interaction, which is the interaction between
*  the robot and the expert programmer, roboticist, designer in charge of actually specifying
*  what the heck the robot should do, specifying the task for the robot. That's so cool, like
*  collaborating on the reward design. Right, collaborating on the reward design. And so what
*  does it mean, right? When we think about the problem, not as someone specifies all of your
*  job is to optimize and we start thinking about you're in this interaction and this collaboration.
*  And the first thing that comes up is when the person specifies a reward, it's not, you know,
*  Gosp, it's not like the letter of the law. It's not the definition of the reward function you
*  should be optimizing because they're doing their best, but they're not some magic perfect oracle.
*  And the sooner we start understanding that, I think the sooner we'll get to more robust
*  robots that function better in different situations. And then you have kind of say,
*  okay, well, it's almost like robots are over learning, over putting too much weight on the
*  reward specified by definition. And maybe leaving a lot of other information on the table. Like what
*  are other things we could do to actually communicate to the robot about what we want them to do besides
*  attempting to specify a reward function? Yeah, you have this awesome, again, I love the poetry of
*  leaked information. You mentioned humans leak information about what they want, you know,
*  leak reward signal for the robot. So how do we detect these leaks?
*  What is that? Yeah, what are these leaks?
*  By the way, just, I don't know, those words recently saw it, read it, I don't know where from you.
*  And it's going to stick with me for a while for some reason, because it's not explicitly expressed.
*  It kind of leaks indirectly from our behavior. From what we do. Yeah, absolutely. So I think
*  maybe some surprising bits, right? So we were talking before about, I'm a robot arm, it needs
*  to move around people, carry stuff, put stuff away, all of that. And now imagine that, you know,
*  the robot has some initial objective that the programmer gave it, so they can do all these
*  things functional, it's capable of doing that. And now I noticed that it's doing something and
*  maybe it's coming too close to me. Right? And maybe I'm the designer, maybe I'm the end user,
*  and this robot is now in my home. And I push it away. So I push away because, you know,
*  it's a reaction to what the robot is currently doing. And this is what we call physical human
*  robot interaction. And now there's a lot of interesting work on how the heck do you respond
*  to physical human robot interaction? What should the robot do if such an event occurs? And there's
*  different schools of thought. Well, you can sort of treat it the control theoretic way and say,
*  this is a disturbance that you must reject. You can sort of treat it more heuristically and say,
*  I'm going to go into some gravity compensation modes so that I'm easily maneuverable around,
*  or I'm going to go in the direction that the person pushed me. And to us,
*  part of realization has been that that is signal that communicates about the reward. Because if
*  my robot was moving in an optimal way and I intervened, that means that I disagree with
*  its notion of optimality. Whatever it thinks is optimal is not actually optimal. And sort of
*  optimization problems aside, that means that the cost function, the reward function is incorrect,
*  or at least is not what I want it to be. How difficult is that signal to
*  to interpret and make actionable? Because this connects to our autonomous vehicle discussion,
*  whether in the semi-autonomous vehicle or autonomous vehicle, when the safety driver
*  disengages the car. But they could have disengaged it for a million reasons.
*  Yeah. Yeah. So that's true. Again, it comes back to, can you structure a little bit your
*  assumptions about how human behavior relates to what they want? And you know, you can't,
*  one thing that we've done is literally just treated this external torque that they applied
*  as, you know, when you take that and you add it with what the torque the robot was already applying,
*  that overall action is probably relatively optimal in respect to whatever it is that the person wants.
*  And then that gives you information about what it is that they want. So you can learn that people
*  want you to stay further away from them. Now, you're right that there might be many things that
*  explain just that one signal and that you might need much more data than that for the person to
*  be able to shape your reward function over time. You can also do this info gathering stuff that
*  we were talking about. Not that we've done that in that context, just to clarify, but it's definitely
*  something we thought about where you can have the robot start acting in a way, like if there are a
*  bunch of different explanations, right? It moves in a way where it sees if you correct it in some
*  other way or not, and then kind of actually plans its motion so that it can disambiguate and collect
*  information about what you want. Anyway, so that's one way that's got a sort of leaked
*  information, maybe even more subtle leaked information is if I just press the E stop,
*  right? I just I'm doing it out of panic because the robot is about to do something bad.
*  There's again information there, right? Okay, the robot should definitely stop, but it should also
*  figure out that whatever it was about to do was not good. And in fact, it was so not good that
*  stopping and remaining stop for a while was a better trajectory for it than whatever it is
*  that it was about to do. And that again is information about what are my preferences?
*  What do I want? Speaking of East stops, what are your expert opinions on the three laws of
*  robotics from Isaac Asimov that don't harm humans, obey orders, protect yourself? I mean,
*  it's such a silly notion, but I speak to so many people these days, just regular folks, just,
*  I don't know, my parents and so on about robotics. And they kind of operate in that space of,
*  you know, imagining our future with robots and thinking, what are the ethical,
*  how do we get that dance, right? I know the three laws might be a silly notion, but do you think
*  about like what universal reward functions that might be that we should enforce on the robots of
*  the future or is that a little too far out? Or is the mechanism that you just described,
*  there shouldn't be three laws, it should be constantly adjusting kind of thing.
*  I think it should constantly be adjusting. I think the issue with the laws is I don't even,
*  there are words and I have to write math and have to translate them into math. What does it mean?
*  What does harm mean? What is... Obey.
*  It's not math. Obey what? Right? Because we just talked about how you try to say what you want,
*  but you don't always get it right. And you want these machines to do what you want,
*  not necessarily exactly what you're literally, so you don't want them to take you literally. You want
*  to take what you say and interpret it in context. And that's what we do with the specified rewards.
*  We don't take them literally anymore from the designer. We, not we as a community, we as,
*  some members of my group, and some of our collaborators like Peter Beal and Stuart Russell,
*  we sort of say, okay, the designer specified this thing, but I'm going to interpret it not as this
*  is the universal reward function that I shall always optimize always and forever, but as this is
*  good evidence about what the person wants. And I should interpret that evidence in the context
*  of these situations that it was specified for. Because ultimately that's what the designer
*  thought about. That's what they had in mind. And really them specifying reward function that works
*  for me in all these situations is really kind of telling me that whatever behavior that incentivizes
*  must be good behavior respect to the thing that I should actually be optimizing for. And so now the
*  robot kind of has uncertainty about what it is that it should be, what its reward function is.
*  And then there's all these additional signals we've been finding that it can kind of continually
*  learn from and adapt its understanding of what people want. Every time the person corrects it,
*  maybe they demonstrate, maybe they stop, hopefully not. One really, really crazy one
*  is the environment itself. Like our world, you observe our world and the state of it,
*  and it's not that you're seeing behavior and you're saying, oh, people are making decisions
*  that are rational, blah, blah, blah. But our world is something that we've been acting with
*  according to our preferences. So I have this example where the robot walks into my home
*  and my shoes are laid down on the floor kind of in a line. It took effort to do that. So even though
*  the robot doesn't see me doing this, actually aligning the shoes, it should still be able to
*  figure out that I want the shoes aligned because there's no way for them to have magically
*  instantiated themselves in that way. Someone must have actually taken the time to do that.
*  So it must be important. So the environment actually tells the environment information,
*  at least information. I mean, the environment is the way it is because humans somehow manipulated
*  it. So you have to kind of reverse engineer the narrative that happened to create the
*  environment as it is, and that leaks the preference information.
*  Yeah. And you have to be careful because people don't have the bandwidth to do everything. So
*  just because my house is messy doesn't mean that I want it to be messy. But that just because I
*  didn't put the effort into that, I put the effort into something else. So the robot should figure
*  out, well, that's something else was more important, but it doesn't mean that the house being messy is
*  not. So it's a little subtle, but yeah, we really think of it, the state itself is kind of like a
*  choice that people implicitly made about how they want their world.
*  What book or books, technical or fiction or philosophical, had a, when you look back,
*  life had a big impact, maybe it was a turning point, was inspiring in some way. Maybe we're
*  talking about some silly book that nobody in their right mind would want to read. Or maybe it's a book
*  that you would recommend to others to read. Or maybe those could be two different recommendations
*  of books that could be useful for people on their journey.
*  When I was in, it's kind of a personal story. When I was in 12th grade, I got my hands on a
*  PDF copy in Romania of Russell Norvig, AI Modern Approach. I didn't know anything about AI at that
*  point. I had watched the movie, The Matrix, was my exposure.
*  So I started going through this thing and you were asking in the beginning,
*  it's math and it's algorithms, what's interesting. It was so captivating, this notion that you could
*  just have a goal and figure out your way through a messy, complicated situation.
*  What sequence of decisions you should make to autonomously achieve that goal. That was so cool.
*  I'm biased, but that's a cool book to look at.
*  You can convert the process of intelligence and mechanize it. I had the same experience. I was
*  really interested in psychiatry and trying to understand human behavior. Then AI Modern
*  Approach is like, wait, you can just reduce it all to-
*  So you can write math about human behavior. I think that stuck with me because a lot of what
*  we do in my lab is write math about human behavior, combine it with data and learning,
*  put it all together, give it to robots to plan with and hope that instead of writing rules for
*  the robots, writing heuristics, designing behavior, they can actually autonomously come
*  up with the right thing to do around people. That's our signature move. We wrote some math and then
*  instead of hand crafting this and that and that, the robot figuring stuff out and isn't that cool.
*  I think that is the same enthusiasm that I got from the robot figuring out how to reach that
*  goal in that graph. Isn't that cool? So apologize for the romanticized questions,
*  and the silly ones. If a doctor gave you five years to live,
*  sort of emphasizing the finiteness of our existence, what would you try to accomplish?
*  It's like my biggest nightmare, by the way. I really like living. I really don't like the idea
*  of being told that I'm going to die. Sorry to link on that for a second. Do you meditate or ponder on
*  your mortality or on our human, the fact that this thing ends? It seems to be a fundamental
*  feature. Do you think of it as a feature or a bug too? You said you don't like the idea of dying,
*  but if I were to give you a choice of living forever, you're not allowed to die.
*  Now I'll say that I want to live forever, but I watch this show, it's very silly, it's called
*  The Good Place, and they reflect a lot on this. The moral of the story is that you have to make
*  the afterlife be finite too, because otherwise people just kind of just like wallow. It's like,
*  whatever, fly around. So I think the finiteness helps, but yeah, it's just, I'm not a religious
*  person. I don't think that there's something after, and so I think it just ends and you stop
*  existing. And I really like existing. It's such a great privilege to exist that, yeah,
*  it's just, I think that's the scary part. I still think that we like existing so much
*  because it ends. And that's so sad. It's so sad to me every time. I find almost everything about
*  this life beautiful. The silliest, most mundane things are just beautiful. And I think I'm
*  cognizant of the fact that I find it beautiful because it ends. And it's so, I don't know,
*  I don't know how to feel about that. I also feel like there's a lesson in there for robotics
*  and AI that is not like, the finiteness of things seems to be a fundamental nature of human
*  existence. I think some people sort of accuse me of just being Russian and melancholic and
*  romantic or something, but that seems to be a fundamental nature of our existence that should
*  be incorporated in our reward functions. But anyway, if you were speaking of reward functions,
*  if you only had five years, what would you try to accomplish? This is the thing. I'm thinking about
*  this question and have a pretty joyous moment because I don't know that I would change much.
*  Oh, that's a beautiful thing.
*  I'm trying to make some contributions to how we understand human AI interaction. I don't think
*  I would change that. Maybe I'll take more trips to the Caribbean or something, but I tried to
*  solve that already from time to time. So yeah, I mean, I try to do the things that bring me joy.
*  And thinking about these things bring me joy is the Mary Kondo thing. Don't do stuff that
*  doesn't spark joy. For the most part, I do things that spark joy. Maybe I'll do less service in the
*  department or something. I'm not dealing with admissions anymore. But no, I mean, I think I
*  have amazing colleagues and amazing students and amazing family and friends and kind of spending
*  time and some balance with all of them is what I do. And that's what I'm doing already. So I
*  don't know that I would really change anything. So on the spirit of positiveness, what small act
*  of kindness, if one pops the mind, were you once shown that you will never forget?
*  When I was in high school, my friends, my classmates did some tutoring. We were gearing up
*  for our baccalaureate exam and they did some tutoring on, well, some on math, some on whatever.
*  I was comfortable enough with some of those subjects, but physics was something that I
*  hadn't focused on in a while. And so they were all working with this one teacher. And I started
*  working with that teacher. Her name is Nicole Bacchano. And she was the one who kind of opened
*  up this whole world for me because she sort of told me that I should take the SATs and apply to
*  go to college abroad and do better on my English and all of that. And when it came to, well,
*  financially, I couldn't, my parents couldn't really afford to do all these things. She started
*  tutoring me on physics for free. And on top of that, sitting down with me to kind of train me for
*  SATs and all that jazz that she had experience with.
*  Wow. And obviously that has taken you to be here today. Also one of the world experts in robotics.
*  It's funny, those little...
*  Yeah, people do these small or large jobs of kindness.
*  For no reason, really. Just out of...
*  Wanting to support someone.
*  Yeah. So we talked a ton about reward functions. Let me talk about the reward functions.
*  The most ridiculous big question. What is the meaning of life? What's the reward function
*  under which we humans operate? Like what, maybe to your life, maybe broader to human
*  life in general, what do you think...
*  What gives life fulfillment, purpose, happiness, meaning?
*  You can't even ask that question with a straight face. That's how ridiculous this is.
*  I can't. I can't.
*  Okay. So, you know...
*  You're gonna try to answer it anyway, aren't you?
*  So, I was in a planetarium once.
*  Yes.
*  And, you know, they show you the thing and then they zoom out and zoom out and this whole like
*  your respect of dust kind of thing. I think I was conceptualizing that we're kind of, you know,
*  what are humans? We're just on this little planet, whatever. We don't matter much in the
*  grand scheme of things. And then my mind got really blown because they talked about this
*  multiverse theory where they kind of zoomed out and were like, this is our universe. And then
*  there's a bazillion other ones and it just stays popped in and out of existence. So,
*  our whole thing that we can't even fathom how big it is was like a blimp that went in and out.
*  And at that point I was like, okay, I'm done. This is not... There is no meaning.
*  And clearly what we should be doing is try to impact whatever local thing we can impact,
*  our communities, leave a little bit behind there, our friends, our family, our local communities,
*  and just try to be there for other humans because I just... Everything beyond that seems ridiculous.
*  I mean, are you like... How do you make sense of these multiverses? Like, are you inspired
*  by the immensity of it? Is it amazing to you or is it almost paralyzing in the mystery of it?
*  It's frustrating. I'm frustrated by my inability to comprehend. It just feels very frustrating.
*  There's some stuff that we should time, blah, blah, blah, that we should really be understanding.
*  And I definitely don't understand it, but the amazing physicists of the world have a much better
*  understanding than me, but it's still in the grand scheme of things. So, it's very frustrating. It
*  feels like our brains don't have some fundamental capacity yet, well, yet or ever. I don't know.
*  One of the dreams of artificial intelligence is to create systems that will
*  expand our cognitive capacity in order to understand, build the theory of everything
*  with the physics and understand what the heck these multiverses are. So, I think there's no
*  better way to end it than talking about the meaning of life and the fundamental nature
*  of the universe and multiverses. And the multiverse.
*  So, Anka, it's a huge honor. One of my favorite conversations I've had. I really
*  appreciate your time. Thank you for talking today.
*  Thank you for coming. Come back again.
*  I'm going to leave you with some words from Isaac Asimov.
*  Your assumptions are your windows on the world. Scrub them off every once in a while,
*  or the light won't come in. Thank you for listening and hope to see you next time.