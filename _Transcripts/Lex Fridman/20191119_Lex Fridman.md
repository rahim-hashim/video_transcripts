---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 6535s
Video Keywords: []
Video Views: 47713
Video Rating: None
Video Description: 
---

# Michael Kearns Algorithmic Fairness, Privacy & Ethics  Lex Fridman Podcast #50
**Lex Fridman:** [November 19, 2019](https://www.youtube.com/watch?v=AzdxbzHtjgs)
*  The following is a conversation with Michael Kearns.
*  He's a professor at the University of Pennsylvania
*  and a co-author of the new book, Ethical Algorithm,
*  that is the focus of much of this conversation.
*  It includes algorithmic fairness, bias, privacy,
*  and ethics in general.
*  But that is just one of many fields
*  that Michael is a world-class researcher in,
*  some of which we touch on quickly,
*  including learning theory
*  or the theoretical foundation of machine learning,
*  game theory, quantitative finance,
*  computational social science, and much more.
*  But on a personal note, when I was an undergrad,
*  early on, I worked with Michael
*  on an algorithmic trading project
*  and competition that he led.
*  That's when I first fell in love
*  with algorithmic game theory.
*  While most of my research life
*  has been in machine learning and human-robot interaction,
*  the systematic way that game theory
*  reveals the beautiful structure in our competitive
*  and cooperating world of humans
*  has been a continued inspiration to me.
*  So for that and other things,
*  I'm deeply thankful to Michael
*  and really enjoyed having this conversation
*  again in person after so many years.
*  This is the Artificial Intelligence Podcast.
*  If you enjoy it, subscribe on YouTube,
*  give it five stars on Apple Podcasts,
*  support on Patreon, or simply connect with me on Twitter,
*  at Lex Friedman, spelled F-R-I-D-M-A-N.
*  This episode is supported by an amazing podcast
*  called Pessimists Archive.
*  Jason, the host of the show, reached out to me
*  looking to support this podcast,
*  and so I listened to it to check it out.
*  And by listened, I mean I went through it
*  Netflix-binge style, at least five episodes in a row.
*  It's now one of my favorite podcasts,
*  and I think it should be one of the top podcasts
*  in the world, frankly.
*  It's a history show about why people resist new things.
*  Each episode looks at a moment in history
*  when something new was introduced,
*  something that today we think of as commonplace,
*  like recorded music, umbrellas, bicycles,
*  cars, chess, coffee, the elevator.
*  And the show explores why it freaked everyone out.
*  The latest episode on mirrors and vanity
*  still stays with me as I think about vanity
*  in the modern day of the Twitter world.
*  That's the fascinating thing about the show,
*  is that stuff that happened long ago,
*  especially in terms of our fear of new things,
*  repeats itself in the modern day,
*  and so has many lessons for us to think about
*  in terms of human psychology
*  and the role of technology in our society.
*  Anyway, you should subscribe and listen to Pessimist Archive.
*  I highly recommend it.
*  And now, here's my conversation with Michael Kearns.
*  You mentioned reading Fear and Loathing in Las Vegas
*  in high school, and having a more,
*  or a bit more of a literary mind.
*  So what books, non-technical, non-computer science,
*  would you say had the biggest impact on your life,
*  either intellectually or emotionally?
*  You've dug deep into my history, I see.
*  Went deep.
*  Yeah, I think, well, my favorite novel
*  is Infinite Jest by David Foster Wallace,
*  which actually, coincidentally, much of it takes place
*  in the halls of buildings right around us here at MIT.
*  So that certainly had a big influence on me.
*  And as you noticed, when I was in high school,
*  I actually even started college as an English major,
*  so was very influenced by that genre of journalism
*  at the time, and thought I wanted to be a writer,
*  and then realized that an English major teaches you to read,
*  but it doesn't teach you how to write,
*  and then I became interested in math
*  and computer science instead.
*  Well, in your new book, Ethical Algorithm,
*  you kinda sneak up from an algorithmic perspective
*  on these deep, profound philosophical questions
*  of fairness, of privacy.
*  In thinking about these topics,
*  how often do you return to that literary mind
*  that you had?
*  Yeah, I'd like to claim there was a deeper connection,
*  but I think both Aaron and I kind of came at these topics
*  first and foremost from a technical angle.
*  I mean, I kind of consider myself primarily
*  an originally a machine learning researcher,
*  and I think as we just watched, like the rest of the society,
*  the field technically advance,
*  and then quickly on the heels of that,
*  kind of the buzzkill of all of the anti-social behavior
*  by algorithms, just kind of realized
*  there was an opportunity for us to do something about it
*  from a research perspective.
*  More to the point in your question,
*  I mean, I do have an uncle who is literally
*  a moral philosopher, and so in the early days
*  of our technical work on fairness topics,
*  I would occasionally run ideas behind him.
*  So I mean, I remember an early email I sent to him
*  in which I said like, oh, here's a specific definition
*  of algorithmic fairness that we think is some sort of
*  variant of Rawlsian fairness.
*  What do you think?
*  And I thought I was asking a yes or no question,
*  and I got back to your kind of classical philosophers
*  responding, well, it depends.
*  If you look at it this way, then you might conclude this.
*  And that's when I realized that there was a real
*  kind of rift between the ways philosophers and others
*  had thought about things like fairness
*  from sort of a humanitarian perspective,
*  and the way that you needed to think about it
*  as a computer scientist if you were going to
*  kind of implement actual algorithmic solutions.
*  But I would say the algorithmic solutions
*  take care of some of the low-hanging fruit.
*  The problem is a lot of algorithms,
*  when they don't consider fairness,
*  they are just terribly unfair.
*  And when they don't consider privacy,
*  they're terribly, they violate privacy.
*  Sort of the algorithmic approach fixes big problems.
*  But there is still, when you start pushing
*  into the gray area, that's when you start getting
*  into this philosophy of what it means to be fair,
*  starting from Plato, what is justice kind of questions.
*  Yeah, I think that's right.
*  And I mean, I would even not go as far as you went to say
*  that sort of the algorithmic work in these areas
*  is solving the biggest problems.
*  And we discuss in the book the fact that really we are,
*  there's a sense in which we're kind of looking
*  where the light is in that, for example,
*  if police are racist in who they decide to stop and frisk,
*  and that goes into the data,
*  there's sort of no undoing that downstream
*  by kind of clever algorithmic methods.
*  And I think especially in fairness,
*  I mean, I think less so in privacy
*  where we feel like the community kind of really
*  has settled on the right definition,
*  which is differential privacy.
*  If you just look at the algorithmic fairness
*  literature already, you can see it's gonna be
*  much more of a mess.
*  And you've got these theorems saying,
*  here are three entirely reasonable,
*  desirable notions of fairness,
*  and here's a proof that you cannot simultaneously
*  have all three of them.
*  So I think we know that algorithmic fairness
*  compared to algorithmic privacy
*  is gonna be kind of a harder problem.
*  And it will have to revisit, I think,
*  things that have been thought about
*  by many generations of scholars before us.
*  So it's very early days for fairness, I think.
*  So before we get into the details
*  of differential privacy and then the fairness side,
*  let me linger on the philosophy a bit.
*  Do you think most people are fundamentally good?
*  Or do most of us have both the capacity
*  for good and evil within us?
*  I mean, I'm an optimist.
*  I tend to think that most people are good
*  and want to do right, and that deviations from that
*  are kind of usually due to circumstance,
*  not to do to people being bad at heart.
*  With people with power,
*  are people at the heads of governments,
*  people at the heads of companies,
*  people at the heads of maybe, so financial power markets,
*  do you think the distribution there is also,
*  most people are good and have good intent?
*  Yeah, I do.
*  I mean, my statement wasn't qualified
*  to people not in positions of power.
*  I mean, I think what happens in a lot of the cliche
*  about absolute power corrupts absolutely.
*  I mean, I think even short of that,
*  having spent a lot of time on Wall Street
*  and also in arenas very, very different
*  from Wall Street like academia,
*  one of the things I think I've benefited from
*  by moving between two very different worlds
*  is you become aware that these worlds
*  kind of develop their own social norms,
*  and they develop their own rationales for behavior,
*  for instance, that might look unusual to outsiders,
*  but when you're in that world,
*  it doesn't feel unusual at all.
*  And I think this is true of a lot of professional cultures,
*  for instance, and so then you're,
*  maybe slippery slope is too strong of a word,
*  but you're in some world where you're mainly
*  around other people with the same kind of viewpoints
*  and training and worldview as you.
*  And I think that's more of a source of abuses of power
*  than sort of there being good people and evil people,
*  and that somehow the evil people
*  are the ones that somehow rise to power.
*  That's really interesting.
*  So it's the within the social norms constructed
*  by that particular group of people,
*  you're all trying to do good,
*  but because as a group, you might drift into something
*  that for the broader population,
*  it does not align with the values of society.
*  That's the word.
*  Yeah, I mean, or not that you drift,
*  but even the things that don't make sense
*  to the outside world don't seem unusual to you.
*  So it's not sort of like a good or a bad thing,
*  but like so for instance, in the world of finance,
*  there's a lot of complicated types of activity
*  that if you are not immersed in that world,
*  you cannot see why the purpose of that activity
*  exists at all.
*  It just seems like completely useless
*  and people just like pushing money around.
*  And when you're in that world,
*  and you learn more, your view does become more nuanced.
*  You realize, okay, there is actually a function
*  to this activity.
*  And in some cases, you would conclude that actually,
*  if magically we could eradicate this activity tomorrow,
*  it would come back because it actually is
*  serving some useful purpose.
*  It's just a useful purpose that's very difficult
*  for outsiders to see.
*  And so I think lots of professional work environments
*  or cultures, as I might put it,
*  kind of have these social norms
*  that don't make sense to the outside world.
*  Academia is the same, right?
*  I mean, lots of people look at academia and say,
*  what the hell are all of you people doing?
*  Why are you paid so much?
*  In some cases, the taxpayer expenses to do, you know, to-
*  Publish papers that nobody reads.
*  But when you're in that world,
*  you come to see the value for it,
*  but even though you might not be able to explain it
*  to the person in the street.
*  Right, and in the case of the financial sector,
*  tools like credit might not make sense to people.
*  Like it's a good example of something
*  that does seem to pop up and be useful,
*  or just the power of markets and just in general, capitalism.
*  Yeah, in finance, I think the primary example
*  I would give is leverage, right?
*  So being allowed to borrow,
*  to sort of use 10 times as much money
*  as you've actually borrowed, right?
*  So that's an example of something
*  that before I had any experience in financial markets,
*  I might've looked at and said,
*  well, what is the purpose of that?
*  That just seems very dangerous.
*  And it is dangerous and it has proven dangerous.
*  But, you know, if the fact of the matter is that,
*  you know, sort of on some particular time scale,
*  you are holding positions that are, you know,
*  very unlikely to, you know, lose, you know,
*  they're like your value at risk,
*  your variance is like one or 5%.
*  Then it kind of makes sense that you would be allowed
*  to use a little bit more than you have,
*  because you have, you know, some confidence
*  that you're not going to lose it all in a single day.
*  Now, of course, when that happens,
*  we've seen what happens, you know, not too long ago.
*  But the idea that it serves no useful economic purpose
*  under any circumstances is definitely not true.
*  We'll return to the other side of the coast, Silicon Valley,
*  and the problems there as we talk about privacy,
*  as we talk about fairness.
*  At the high level, and I'll ask some sort of basic questions
*  with a hope to get at the fundamental nature of reality.
*  But from a very high level, what is an ethical algorithm?
*  So I can say that an algorithm has a running time
*  of using big O notation, N log N.
*  I can say that a machine learning algorithm
*  classified cat versus dog with 97% accuracy.
*  Do you think there will one day be a way to measure
*  sort of in the same compelling way as the big O notation
*  this algorithm is 97% ethical?
*  First of all, let me riff for a second
*  on your specific N log N examples.
*  So because early in the book,
*  when we're just kind of trying to describe algorithms period,
*  we say like, okay, you know, what's an example
*  of an algorithm or an algorithmic problem?
*  First of all, like it's sorting, right?
*  You have a bunch of index cards with numbers on them
*  and you want to sort them.
*  And we describe, you know, an algorithm
*  that sweeps all the way through,
*  finds the smallest number, puts it at the front
*  then sweeps through again, finds the second smallest number.
*  So we make the point that this is an algorithm
*  and it's also a bad algorithm in the sense that,
*  you know, it's quadratic rather than N log N,
*  which we know is kind of optimal for sorting.
*  And we make the point that sort of like, you know,
*  so even within the confines
*  of a very precisely specified problem,
*  there might be many, many different algorithms
*  for the same problem with different properties.
*  Like some might be faster in terms of running time,
*  some might use less memory, some might have, you know,
*  better distributed implementations.
*  And so the point is, is that already we're used to,
*  you know, in computer science,
*  thinking about trade-offs between different types
*  of quantities and resources,
*  and there being, you know, better and worse algorithms.
*  And our book is about that part of algorithmic ethics
*  that we know how to kind of put on that same kind
*  of quantitative footing right now.
*  So, you know, just to say something
*  that our book is not about,
*  our book is not about kind of broad,
*  fuzzy notions of fairness.
*  It's about very specific notions of fairness.
*  There's more than one of them.
*  There are tensions between them, right?
*  But if you pick one of them,
*  you can do something akin to saying
*  that this algorithm is 97% ethical.
*  You can say, for instance, the, you know,
*  for this lending model, the false rejection rate
*  on black people and white people is within 3%, right?
*  So we might call that a 97% ethical algorithm
*  and a 100% ethical algorithm would mean
*  that that difference is 0%.
*  In that case, fairness is specified
*  when two groups, however they're defined, are given to you.
*  That's right.
*  So the, and then you can sort of mathematically
*  start describing the algorithm.
*  But nevertheless, the part where the two groups
*  are given to you, unlike running time, you know,
*  we don't, in computer science, talk about
*  how fast an algorithm feels like when it runs.
*  True.
*  We measure it and ethical starts getting into feelings.
*  So for example, an algorithm runs, you know,
*  if it runs in the background,
*  it doesn't disturb the performance of my system.
*  It'll feel nice.
*  I'll be okay with it.
*  But if it overloads the system, it'll feel unpleasant.
*  So in that same way, ethics,
*  there's a feeling of how socially acceptable it is.
*  How does it represent the moral standards
*  of our society today?
*  So in that sense, and sorry to linger on that,
*  first of high, low philosophical questions,
*  do you have a sense we'll be able to measure
*  how ethical an algorithm is?
*  First of all, I didn't, certainly didn't mean
*  to give the impression that you can kind of measure,
*  you know, memory speed trade-offs, you know,
*  and that there's a complete, you know,
*  mapping from that onto kind of fairness, for instance,
*  or ethics and accuracy, for example.
*  In the type of fairness definitions
*  that are largely the objects of study today
*  and starting to be deployed,
*  you as the user of the definitions,
*  you need to make some hard decisions
*  before you even get to the point
*  of designing fair algorithms.
*  One of them, for instance, is deciding
*  who it is that you're worried about protecting,
*  who you're worried about being harmed by, for instance,
*  some notion of discrimination or unfairness.
*  And then you need to also decide what constitutes harm.
*  So for instance, in a lending application,
*  maybe you decide that, you know,
*  falsely rejecting a credit-worthy individual,
*  you know, sort of a false negative,
*  is the real harm and that false positives,
*  i.e. people that are not credit-worthy
*  or are not gonna repay your loan, that get a loan,
*  you might think of them as lucky.
*  And so that's not a harm, although it's not clear
*  that if you don't have the means to repay a loan,
*  that being given a loan is not also a harm.
*  So, you know, the literature is sort of so far
*  quite limited in that you sort of need to say,
*  who do you wanna protect
*  and what would constitute harm to that group?
*  And when you ask questions like,
*  will algorithms feel ethical,
*  one way in which they won't,
*  under the definitions that I'm describing,
*  is if, you know, if you are an individual
*  who is falsely denied a loan, incorrectly denied a loan,
*  all of these definitions basically say like,
*  well, you know, your compensation is the knowledge
*  that we are also falsely denying loans to other people,
*  you know, in other groups
*  at the same rate that we're doing it to you.
*  And, you know, and so there is actually this interesting,
*  even technical tension in the field right now
*  between these sort of group notions of fairness
*  and notions of fairness
*  that might actually feel like real fairness to individuals,
*  right, they might really feel like
*  their particular interests are being protected
*  or thought about by the algorithm rather than just,
*  you know, the groups that they happen to be members of.
*  Is there parallels to the big O notation
*  of worst case analysis?
*  So, is it important to,
*  looking at the worst violation of fairness
*  for an individual, is it important to minimize
*  that one individual, so like worst case analysis?
*  Is that something you think about or?
*  I mean, I think we're not even at the point
*  where we can sensibly think about that.
*  So first of all, you know, we're talking here
*  both about fairness applied at the group level,
*  which is a relatively weak thing,
*  but it's better than nothing.
*  And also the more ambitious thing
*  of trying to give some individual promises,
*  but even that doesn't incorporate,
*  I think something that you're hinting at here
*  is what I might call subjective fairness, right?
*  So a lot of the definitions, I mean,
*  all of the definitions in the algorithmic fairness literature
*  are what I would kind of call received wisdom definitions.
*  It's sort of, you know, somebody like me sits around
*  and thinks like, okay, you know,
*  I think here's a technical definition of fairness
*  that I think people should want
*  or that they should think of as some notion of fairness,
*  maybe not the only one, maybe not the best one,
*  maybe not the last one.
*  But we really actually don't know
*  from a subjective standpoint,
*  like what people really think is fair.
*  There's, you know, we just started doing a little bit
*  of work in our group at actually doing
*  kind of human subject experiments in which we, you know,
*  ask people about, you know,
*  we ask them questions about fairness, we survey them,
*  we, you know, we show them pairs of individuals
*  in let's say a criminal recidivism prediction setting,
*  and we ask them, do you think these two individuals
*  should be treated the same as a matter of fairness?
*  And to my knowledge, there's not a large literature
*  in which ordinary people are asked about, you know,
*  they have sort of notions of their subjective fairness
*  elicited from them.
*  It's mainly, you know, kind of scholars
*  who think about fairness,
*  kind of making up their own definitions.
*  And I think this needs to change actually
*  for many social norms, not just for fairness, right?
*  So there's a lot of discussion these days
*  in the AI community about interpretable AI
*  or understandable AI.
*  And as far as I can tell,
*  everybody agrees that deep learning,
*  or at least the outputs of deep learning
*  are not very understandable.
*  And people might agree that sparse linear models
*  with integer coefficients are more understandable.
*  But nobody's really asked people, you know,
*  there's very little literature on, you know,
*  sort of showing people models and asking them,
*  do they understand what the model is doing?
*  And I think that in all of these topics,
*  as these fields mature,
*  we need to start doing more behavioral work.
*  Yeah, which is, so one of my deep passions is psychology.
*  And I always thought computer scientists
*  will be the best future psychologists.
*  In a sense that data is,
*  especially in this modern world,
*  the data is a really powerful way to understand
*  and study human behavior.
*  And you've explored that with your game theory side
*  of work as well.
*  Yeah, I'd like to think that what you say is true
*  about computer scientists and psychology
*  from my own limited wandering into human subject experiments,
*  we have a great deal to learn.
*  Not just computer science,
*  but AI and machine learning more specifically,
*  I kind of think of as imperialist research communities
*  in that, you know, kind of like physicists
*  in an earlier generation,
*  computer scientists kind of don't think
*  of any scientific topic as off limits to them.
*  They will like freely wander into areas
*  that others have been thinking about for decades or longer.
*  And, you know, we usually tend to embarrass ourselves
*  in those efforts for some amount of time.
*  Like, you know, I think reinforcement learning
*  is a good example, right?
*  So a lot of the early work in reinforcement learning,
*  I have complete sympathy for the control theorists
*  that looked at this and said like, okay,
*  you are reinventing stuff that we've known
*  since like the 40s, right?
*  But, you know, in my view, eventually,
*  this sort of, you know, computer scientists
*  have made significant contributions to that field,
*  even though we kind of embarrassed ourselves
*  for the first decade.
*  So I think if computer scientists
*  are gonna start engaging in kind of psychology,
*  human subjects type of research,
*  we should expect to be embarrassing ourselves
*  for a good 10 years or so,
*  and then hope that it turns out as well as, you know,
*  some other areas that we've waded into.
*  So you kind of mentioned this,
*  just to linger on the idea of an ethical algorithm,
*  an idea of groups, sort of group thinking
*  and individual thinking, and we're struggling that.
*  One of the amazing things about algorithms
*  and your book and just this field of study
*  is it gets us to ask, like, forcing machines,
*  converting these ideas into algorithms
*  is forcing us to ask questions of ourselves
*  as a human civilization.
*  So there's a lot of people now in public discourse
*  doing sort of group thinking,
*  thinking like there's particular sets of groups
*  that we don't want to discriminate against and so on,
*  and then there's individuals,
*  sort of in the individual life stories,
*  the struggles they went through and so on.
*  Now, like, in philosophy, it's easier to do group thinking
*  because you don't, it's very hard to think about individuals.
*  There's so much variability,
*  but with data, you can start to actually say,
*  you know, what group thinking is too crude?
*  You're actually doing more discrimination by thinking
*  in terms of groups and individuals.
*  Can you linger on that kind of idea
*  of group versus individual in ethics?
*  And is it good to continue thinking
*  in terms of groups in algorithms?
*  So let me start by answering a very good,
*  high-level question with a slightly
*  narrow technical response,
*  which is these group definitions of fairness,
*  like here's a few groups, like different racial groups,
*  maybe gender groups, maybe age, what have you.
*  And let's make sure that, you know,
*  for none of these groups do we, you know,
*  have a false negative rate,
*  which is much higher than any other one of these groups.
*  Okay, so these are kind of classic group
*  aggregate notions of fairness.
*  And, you know, but at the end of the day,
*  an individual you can think of as a combination
*  of all of their attributes, right?
*  They're a member of a racial group,
*  they have a gender, they have an age, you know,
*  and many other demographic properties
*  that are not biological, but that, you know,
*  are still very strong determinants of outcome
*  and personality and the like.
*  So one, I think, useful spectrum is to sort of think
*  about that array between the group
*  and the specific individual,
*  and to realize that in some ways,
*  asking for fairness at the individual level
*  is to sort of ask for group fairness simultaneously
*  for all possible combinations of groups.
*  So in particular, so in particular, you know,
*  if I build a predictive model
*  that meets some definition of fairness by race,
*  by gender, by age, by what have you,
*  marginally, to get it slightly technical,
*  sort of independently, I shouldn't expect that model
*  to not discriminate against disabled Hispanic women
*  over age 55, making less than $50,000 a year annually,
*  even though I might have protected
*  each one of those attributes marginally.
*  So the optimization, actually,
*  that's a fascinating way to put it.
*  So you're just optimizing,
*  the one way to achieve the optimizing fairness
*  for individuals is just to add more and more definitions
*  of groups that each individual belongs to.
*  So, you know, at the end of the day,
*  we could think of all of ourselves as groups of size one,
*  because eventually there's some attribute
*  that separates you from me
*  and from everybody else in the world, okay?
*  And so it is possible to put, you know,
*  these incredibly coarse ways of thinking about fairness
*  and these very, very individualistic specific ways
*  on a common scale.
*  And, you know, one of the things we've worked on
*  from a research perspective is, you know,
*  so we sort of know how to, you know, in relative terms,
*  we know how to provide fairness guarantees
*  at the coarsest end of the scale.
*  We don't know how to provide kind of sensible, tractable,
*  realistic fairness guarantees at the individual level,
*  but maybe we could start creeping towards that
*  by dealing with more, you know, refined subgroups.
*  I mean, we gave a name to this phenomenon
*  where, you know, you protect,
*  you enforce some definition of fairness
*  for a bunch of marginal attributes or features,
*  but then you find yourself
*  discriminating against a combination of them.
*  We call that fairness gerrymandering,
*  because like political gerrymandering, you know,
*  you're giving some guarantee at the aggregate level,
*  but that when you kind of look in a more granular way
*  at what's going on, you realize that you're achieving
*  that aggregate guarantee by sort of favoring some groups
*  and discriminating against other ones.
*  And so there are, you know, it's early days,
*  but there are algorithmic approaches
*  that let you start creeping towards that,
*  you know, individual end of the spectrum.
*  Does there need to be human input in the form of weighing
*  the value of the importance of each kind of group?
*  So for example, is it like, so gender, say,
*  crudely speaking, male and female,
*  and then different races,
*  are we as humans supposed to put value
*  on saying gender is 0.6 and race is 0.4,
*  in terms of, in the big optimization of achieving fairness?
*  Is that kind of what humans are supposed to do here?
*  I mean, of course, you know, I don't need to tell you
*  that, of course, technically one could incorporate
*  such weights if you wanted to
*  into a definition of fairness.
*  You know, fairness is an interesting topic
*  in that having worked in the book being about
*  both fairness, privacy, and many other social norms,
*  fairness, of course, is a much, much more loaded topic.
*  So privacy, I mean, people want privacy,
*  people don't like violations of privacy,
*  violations of privacy cause damage, angst,
*  and bad publicity for the companies
*  that are victims of them.
*  But sort of everybody agrees,
*  more data privacy would be better than less data privacy.
*  And you don't have these, somehow the discussions
*  of fairness don't become politicized
*  along other dimensions like race, and about gender,
*  and you know, whether we, and you know,
*  you quickly find yourselves kind of revisiting topics
*  that have been kind of unresolved forever,
*  like affirmative action, right?
*  Sort of, you know, like why are you protecting,
*  some people will say, why are you protecting
*  this particular racial group?
*  And others will say, well, we need to do that
*  as a matter of retribution, other people will say
*  it's a matter of economic opportunity,
*  and I don't know which of, you know,
*  whether any of these are the right answers,
*  but you sort of, fairness is sort of special,
*  in that as soon as you start talking about it,
*  you inevitably have to participate in debates
*  about fair to whom, at what expense to who else.
*  I mean, even in criminal justice, right?
*  You know, where people talk about fairness
*  in criminal sentencing, or you know,
*  predicting failures to appear,
*  or making parole decisions or the like,
*  they will, you know, they'll point out that,
*  well, these definitions of fairness
*  are all about fairness for the criminals,
*  and what about fairness for the victims, right?
*  Well, so when I basically say something like, well,
*  the false incarceration rate for black people
*  and white people needs to be roughly the same,
*  you know, there's no mention of potential victims
*  of criminals in such a fairness definition.
*  And that's the realm of public discourse.
*  I should actually recommend,
*  I just listened to people listening,
*  Intelligence Squares Debates, US edition,
*  just had a debate, they have this structure
*  where you have old Oxford style,
*  or whatever they're called, debates,
*  and it was two versus two,
*  and they talked about affirmative action,
*  and it was incredibly interesting that it's still,
*  that there's really good points
*  on every side of this issue,
*  which is fascinating to listen to.
*  Yeah, yeah, I agree.
*  And so it's interesting to be a researcher trying to do,
*  for the most part, technical algorithmic work,
*  but Aaron and I both quickly learned you cannot do that
*  and then go out and talk about it
*  and expect people to take it seriously
*  if you're unwilling to engage in these broader debates
*  that are entirely extra algorithmic, right?
*  They're not about, you know, algorithms
*  and making algorithms better,
*  as you said, sort of like,
*  what should society be protecting in the first place?
*  When you discuss the fairness,
*  an algorithm that achieves fairness,
*  whether in the constraints and the objective function,
*  there's an immediate kind of analysis you can perform,
*  which is saying, if you care about fairness in gender,
*  this is the amount that you have to pay for it
*  in terms of the performance of the system.
*  Is there a role for statements like that
*  in a table in a paper,
*  or do you wanna really not touch that?
*  No, we wanna touch that and we do touch it.
*  So, I mean, just again,
*  to make sure I'm not promising your viewers
*  more than we know how to provide.
*  But if you pick a definition of fairness,
*  like I'm worried about gender discrimination,
*  and you pick a notion of harm,
*  like false rejection for a loan, for example,
*  and you give me a model,
*  I can definitely, first of all, go audit that model.
*  It's easy for me to go from data to kind of say like,
*  okay, your false rejection rate on women
*  is this much higher than it is on men, okay?
*  But once you also put the fairness
*  into your objective function,
*  I mean, I think the table that you're talking about
*  is what we would call the Pareto curve, right?
*  You can literally trace out,
*  and we give examples of such plots
*  on real data sets in the book,
*  you have two axes.
*  On the X axis is your error,
*  on the Y axis is unfairness by whatever,
*  if it's like the disparity between false rejection rates
*  between two groups.
*  And your algorithm now has a knob that basically says,
*  how strongly do I want to enforce fairness?
*  And the less unfair,
*  if the two axes are error and unfairness,
*  we'd like to be at zero, zero.
*  We'd like zero error and zero unfair unfairness
*  simultaneously.
*  Anybody who works in machine learning
*  knows that you're generally not going to get
*  to zero error period
*  without any fairness constraint whatsoever.
*  So that's not gonna happen.
*  But in general, you'll get this,
*  you'll get some kind of convex curve
*  that specifies the numerical trade-off you face.
*  If I wanna go from 17% error down to 16% error,
*  what will be the increase in unfairness
*  that I've experienced as a result of that?
*  And so this curve specifies the kind of undominated models.
*  Models that are off that curve
*  can be strictly improved in one or both dimensions.
*  You can either make the error better
*  or the unfairness better or both.
*  And I think our view is that not only are these objects,
*  these Pareto curves, efficient frontiers,
*  as you might call them,
*  not only are they valuable scientific objects,
*  I actually think that they in the near term
*  might need to be the interface between researchers
*  working in the field and stakeholders in given problems.
*  So you could really imagine telling a criminal jurisdiction
*  look, if you're concerned about racial fairness,
*  but you're also concerned about accuracy,
*  you want to release on parole people
*  that are not going to recommit a violent crime
*  and you don't wanna release the ones who are.
*  So that's accuracy.
*  But if you also care about the mistakes you make
*  not being disproportionately on one racial group or another,
*  you can show this curve.
*  I'm hoping that in the near future,
*  it'll be possible to explain these curves
*  to non-technical people
*  that are the ones that have to make the decision,
*  where do we wanna be on this curve?
*  Like what are the relative merits or value
*  of having lower error versus lower unfairness?
*  That's not something computer scientists
*  should be deciding for society, right?
*  That the people in the field, so to speak,
*  the policy makers, the regulators,
*  that's who should be making these decisions.
*  But I think and hope that they can be made to understand
*  that these trade-offs generally exist
*  and that you need to pick a point
*  and ignoring the trade-off,
*  you're implicitly picking a point anyway, right?
*  You just don't know it and you're not admitting it.
*  Just to linger on the point of trade-offs,
*  I think that's a really important thing to sort of think about.
*  So you think when we start to optimize for fairness,
*  there's almost always in most system going to be trade-offs.
*  What's the trade-off between, just to clarify,
*  there've been some sort of technical terms thrown around,
*  but a perfectly fair world,
*  why will somebody be upset about that?
*  The specific trade-off I talked about
*  just in order to make things very concrete
*  was between numerical error
*  and some numerical measure of unfairness.
*  What is numerical error in the case of...
*  Just like say predictive error,
*  like the probability or frequency
*  with which you release somebody on parole
*  who then goes on to recommit a violent crime
*  or keep incarcerated somebody
*  who would not have recommitted a violent crime.
*  So in the case of awarding somebody parole
*  or giving somebody parole or letting them out on parole,
*  you don't want them to recommit a crime.
*  So it's your system failed in prediction
*  if they happen to do a crime.
*  Okay, so that's one axis.
*  And what's the fairness axis?
*  And so then the fairness axis might be
*  the difference between racial groups
*  in the kind of false positive predictions,
*  namely people that I kept incarcerated
*  predicting that they would recommit a violent crime
*  when in fact they wouldn't have.
*  Right, and the unfairness of that, just to linger it,
*  and allow me to in eloquently to try to
*  sort of describe why that's unfair,
*  why unfairness is there.
*  The unfairness you wanna get rid of is
*  that in the judge's mind,
*  the bias of having being brought up to society,
*  the slight racial bias, the racism that exists in the society,
*  you wanna remove that from the system.
*  Another way that's been debated is sort of equality
*  of opportunity versus equality of outcome.
*  And there's a weird dance there
*  that's really difficult to get right.
*  And we don't, the affirmative action is exploring that space.
*  Right, and then this also quickly bleeds into questions
*  like well, maybe if one group really does recommit crimes
*  at a higher rate, the reason for that is that
*  at some earlier point in the pipeline
*  or earlier in their lives,
*  they didn't receive the same resources
*  that the other group did.
*  Right.
*  And so there's always in kind of fairness discussions,
*  the possibility that the real injustice came earlier,
*  earlier in this individual's life,
*  earlier in this group's history, et cetera, et cetera.
*  And so a lot of the fairness discussion is almost,
*  the goal is for it to be a corrective mechanism
*  to account for the injustice earlier in life.
*  By some definitions of fairness
*  or some theories of fairness, yeah.
*  Others would say like, look,
*  it's not to correct that injustice,
*  it's just to kind of level the playing field right now
*  and not incarcerate, falsely incarcerate
*  more people of one group than another group.
*  But I mean, I think just, it might be helpful
*  just to demystify a little bit about
*  the many ways in which bias or unfairness
*  can come into algorithms,
*  especially in the machine learning era, right?
*  And I think many of your viewers
*  have probably heard these examples before,
*  but let's say I'm building a face recognition system, right?
*  And so I'm kind of gathering lots of images of faces
*  and trying to train the system to recognize new faces
*  of those individuals from training on,
*  training set of those faces of individuals.
*  And it shouldn't surprise anybody
*  or certainly not anybody in the field of machine learning
*  if my training data set was primarily white males
*  and I'm training the model to maximize the overall accuracy
*  on my training data set,
*  that the model can reduce its error most
*  by getting things right on the white males
*  that constitute the majority of the data set,
*  even if that means that on other groups,
*  they will be less accurate, okay?
*  Now, there's a bunch of ways
*  you could think about addressing this.
*  One is to deliberately put into the objective
*  of the algorithm not to optimize the error
*  at the expense of this discrimination.
*  And then you're kind of back in the land
*  of these kind of two-dimensional numerical trade-offs.
*  A valid counter argument is to say like,
*  well, no, you don't have to,
*  there's no, the notion of the tension
*  between error and accuracy here is a false one.
*  You could instead just go out
*  and get much more data on these other groups
*  that are in the minority and equalize your data set,
*  or you could train a separate model on those subgroups
*  and have multiple models.
*  The point I think we would,
*  we've tried to make in the book
*  is that those things have cost too, right?
*  Going out and gathering more data on groups
*  that are relatively rare compared to your plurality
*  or majority group that,
*  it may not cost you in the accuracy of the model,
*  but it's gonna cost the company developing this model
*  more money to develop that.
*  And it also costs more money
*  to build separate predictive models
*  and to implement and deploy them.
*  So even if you can find a way to avoid the tension
*  between error and accuracy in training a model,
*  you might push the cost somewhere else,
*  like money, like development time,
*  research time and the like.
*  There are fundamentally difficult
*  philosophical questions in fairness.
*  And we live in a very divisive political climate,
*  outraged culture.
*  There is alt-right folks on 4chan trolls.
*  There is social justice warriors on Twitter.
*  There is very divisive, outraged folks
*  on all sides of every kind of system.
*  How do you, how do we as engineers
*  build ethical algorithms in such divisive culture?
*  Do you think they could be disjoint?
*  The human has to inject your values
*  and then you can optimize over those values.
*  But in our times when you start
*  actually applying these systems,
*  things get a little bit challenging for the public discourse.
*  How do you think we can proceed?
*  Yeah, I mean, for the most part in the book,
*  a point that we try to take some pains to make
*  is that we don't view ourselves or people like us
*  as being in the position of deciding for society
*  what the right social norms are,
*  what the right definitions of fairness are.
*  Our main point is to just show that if society
*  or the relevant stakeholders in a particular domain
*  can come to agreement on those sorts of things,
*  there's a way of encoding that into algorithms
*  in many cases, not in all cases.
*  One other misconception that hopefully we definitely dispel
*  is sometimes when people read the title of the book
*  and I think not unnaturally fear that what we're suggesting
*  is that the algorithms themselves should decide
*  what those social norms are and develop their own notions
*  of fairness and privacy or ethics.
*  And we're definitely not suggesting that.
*  The title of the book is Ethical Algorithm, by the way.
*  And I didn't think of that interpretation of the title.
*  That's interesting.
*  Yeah, yeah.
*  I mean, especially these days where people are concerned
*  about the robots becoming our overlords,
*  the idea that the robots would also sort of develop
*  their own social norms is just one step away from that.
*  But I do think, obviously, despite disclaimer
*  that people like us shouldn't be making
*  those decisions for society, we are kind of living
*  in a world where in many ways computer scientists
*  have made some decisions that have fundamentally changed
*  the nature of our society and democracy
*  and sort of civil discourse and deliberation
*  in ways that I think most people generally feel
*  are bad these days, right?
*  But they had to make, so if we look at people
*  at the heads of companies and so on,
*  they had to make those decisions, right?
*  There has to be decisions.
*  So there's two options.
*  Either you kind of put your head in the sand
*  and don't think about these things
*  and just let the algorithm do what it does,
*  or you make decisions about what you value
*  over injecting moral values into the algorithm.
*  Look, I never mean to be an apologist for the tech industry,
*  but I think it's a little bit too far
*  to sort of say that explicit decisions
*  were made about these things.
*  So let's, for instance, take social media platforms, right?
*  So like many inventions in technology and computer science,
*  a lot of these platforms that we now use regularly
*  kind of started as curiosities, right?
*  I remember when things like Facebook came out
*  and its predecessors like Friendster,
*  which nobody even remembers now,
*  people really wonder like,
*  why would anybody want to spend time doing that?
*  You know, even the web when it first came out,
*  when it wasn't populated with much content
*  and it was largely kind of hobbyists building their own
*  kind of ramshackle websites,
*  a lot of people looked at this and said,
*  well, what is the purpose of this thing?
*  Why is this interesting?
*  Who would want to do this?
*  And so even things like Facebook and Twitter,
*  yes, technical decisions were made by engineers,
*  by scientists, by executives
*  in the design of those platforms.
*  But, you know, I don't think 10 years ago,
*  anyone anticipated that those platforms, for instance,
*  might kind of acquire undue influence
*  on political discourse or on the outcomes of elections.
*  And I think the scrutiny that these companies are getting now
*  is entirely appropriate,
*  but I think it's a little too harsh
*  to kind of look at history and sort of say like,
*  oh, you should have been able to anticipate
*  that this would happen with your platform.
*  And in the sort of gaming chapter of the book,
*  one of the points we're making is that,
*  you know, these platforms, right,
*  they don't operate in isolation.
*  So unlike the other topics we're discussing
*  like fairness and privacy,
*  like those are really cases where algorithms can operate
*  on your data and make decisions about you
*  and you're not even aware of it, okay?
*  Things like Facebook and Twitter, these are systems, right?
*  These are social systems and their evolution,
*  even their technical evolution
*  because machine learning is involved,
*  is driven in no small part by the behavior
*  of the users themselves and how the users decide
*  to adopt them and how to use them.
*  And so, you know, I'm kind of like,
*  who really knew that, you know, until we saw it happen,
*  who knew that these things might be able
*  to influence the outcome of elections?
*  Who knew that, you know, they might polarize
*  political discourse because of the ability to, you know,
*  decide who you interact with on the platform
*  and also with the platform naturally using machine learning
*  to optimize for your own interests
*  that they would further isolate us from each other
*  and, you know, like feed us all basically just the stuff
*  that we already agreed with.
*  And so I think, you know, we've come to that outcome,
*  I think, largely, but I think it's something
*  that we all learned together, including the companies,
*  as these things happen.
*  Now you asked like, well, are there algorithmic remedies
*  to these kinds of things?
*  And again, these are big problems
*  that are not gonna be solved with, you know,
*  somebody going in and changing a few lines of code
*  somewhere in a social media platform.
*  But I do think in many ways,
*  there are definitely ways of making things better.
*  I mean, like an obvious recommendation
*  that we make at some point in the book is like, look, you know,
*  to the extent that we think that machine learning applied
*  for personalization purposes in things like newsfeed,
*  you know, or other platforms has led to polarization
*  and intolerance of opposing viewpoints.
*  As you know, right, these algorithms have models, right?
*  And they kind of place people in some kind of metric space
*  and they place content in that space
*  and they sort of know the extent to which I have an affinity
*  for a particular type of content.
*  And by the same token, they also probably have,
*  that same model probably gives you a good idea
*  of the stuff I'm likely to violently disagree with
*  or be offended by, okay?
*  So, you know, in this case,
*  there really is some knob you could tune that says like,
*  instead of showing people only what they like
*  and what they want, let's show them some stuff
*  that we think that they don't like,
*  or that's a little bit further away.
*  And you can even imagine users being able to control this,
*  you know, just like everybody gets a slider
*  and that slider says like, you know,
*  how much stuff do you want to see that's kind of, you know,
*  you might disagree with,
*  or is at least further from your interests?
*  It's almost like an exploration button.
*  So just get your intuition.
*  Do you think engagement,
*  so like you staying on the platform,
*  you staying engaged,
*  do you think fairness, ideas of fairness won't emerge?
*  Like how bad is it to just optimize for engagement?
*  Do you think we'll run into big trouble
*  if we're just optimizing for how much you love the platform?
*  Well, I mean, optimizing for engagement
*  kind of got us where we are.
*  So do you one, have faith that it's possible to do better
*  and two, if it is, how do we do better?
*  I mean, it's definitely possible to do different, right?
*  And again, you know, it's not as if I think
*  that doing something different than optimizing for engagement
*  won't cost these companies in real ways,
*  including revenue and profitability potentially.
*  In the short term at least.
*  Yeah, in the short term, right.
*  And again, you know, if I worked at these companies,
*  I'm sure that it would have seemed like
*  the most natural thing in the world also
*  to want to optimize engagement, right?
*  And that's good for users in some sense.
*  You want them to be, you know, vested in the platform
*  and enjoying it and finding it useful,
*  interesting and or productive.
*  But, you know, my point is,
*  is that the idea that there's,
*  that it's sort of out of their hands, as you said,
*  that there's nothing to do about it.
*  Never say never, but that strikes me as implausible
*  as a machine learning person, right?
*  I mean, these companies are driven by machine learning
*  and this optimization of engagement
*  is essentially driven by machine learning, right?
*  It's driven by not just machine learning,
*  but, you know, very, very large scale A, B experimentation
*  where you kind of tweak some element of the user interface
*  or tweak some component of an algorithm
*  or tweak some component or feature
*  of your click through prediction model.
*  And my point is, is that anytime you know
*  how to optimize for something, you know, by def,
*  almost by definition, that solution tells you
*  how not to optimize for it or to do something different.
*  Engagement can be measured.
*  So sort of optimizing for sort of minimizing divisiveness
*  or maximizing intellectual growth over the lifetime
*  of a human being are very difficult to measure.
*  That's right.
*  So I'm not claiming that doing something different
*  will immediately make it apparent
*  that this is a good thing for society.
*  And in particular, I mean, I think one way of thinking
*  about where we are on some of these social media platforms
*  is that, you know, it kind of feels a bit like
*  we're in a bad equilibrium, right?
*  That these systems are helping us all kind of optimize
*  something myopically and selfishly for ourselves.
*  And of course, from an individual standpoint
*  at any given moment, like why would I wanna see things
*  in my newsfeed that I found irrelevant, offensive,
*  or you know, or the like, okay?
*  But, you know, maybe by all of us, you know,
*  having these platforms myopically optimized
*  in our interests, we have reached a collective outcome
*  as a society that we're unhappy with in different ways,
*  let's say with respect to things like, you know,
*  political discourse and tolerance of opposing viewpoints.
*  And if Mark Zuckerberg gave you a call and said,
*  I'm thinking of taking a sabbatical,
*  could you run Facebook for me for six months?
*  What would you, how?
*  I think no thanks would be my first response,
*  but there are many aspects of being the head
*  of the entire company that are kind of entirely exogenous
*  to many of the things that we're discussing here.
*  Yes.
*  And so I don't really think I would need to be CEO
*  of Facebook to kind of implement the, you know,
*  more limited set of solutions that I might imagine.
*  But I think one concrete thing they could do
*  is they could experiment with letting people who chose to
*  to see more stuff in their newsfeed that is not entirely
*  kind of chosen to optimize for their particular interests,
*  beliefs, et cetera.
*  So the kind of thing is, so I could speak to YouTube,
*  but I think Facebook probably does something similar
*  is they're quite effective at automatically finding
*  what sorts of groups you belong to,
*  not based on race or gender or so on,
*  but based on the kind of stuff you enjoy watching
*  in the case of YouTube.
*  Sort of, it's a difficult thing for Facebook or YouTube
*  to then say, well, you know what?
*  We're gonna show you something
*  from a very different cluster.
*  Even though we believe algorithmically,
*  you're unlikely to enjoy that thing.
*  Sort of, that's a weird jump to make.
*  There has to be a human, like at the very top
*  of that system that says, well,
*  that will be long-term healthy for you.
*  That's more than an algorithmic decision.
*  Or that same person could say
*  that'll be long-term healthy for the platform.
*  The platform.
*  Or for the platform's influence on society
*  outside of the platform.
*  And it's easy for me to sit here and say these things,
*  but conceptually, I do not think that these are kind of
*  totally, or they shouldn't be kind of completely alien ideas.
*  You could try things like this,
*  and it wouldn't be, we wouldn't have to invent
*  entirely new science to do it,
*  because if we're all already embedded in some metric space
*  and there's a notion of distance between you and me
*  and every piece of content, then we know exactly,
*  the same model that dictates how to make me really happy
*  also tells how to make me as unhappy as possible as well.
*  The focus in your book and algorithmic fairness research
*  today in general is on machine learning,
*  like we said, is data.
*  And just even though the entire AI field right now
*  is captivated with machine learning, with deep learning,
*  do you think ideas in symbolic AI
*  or totally other kinds of approaches
*  are interesting, useful in this space,
*  have some promising ideas in terms of fairness?
*  I haven't thought about that question specifically
*  in the context of fairness.
*  I definitely would agree with that statement in the large.
*  I mean, I am one of many machine learning researchers
*  who do believe that the great successes
*  that have been shown in machine learning recently
*  are great successes,
*  but they're on a pretty narrow set of tasks.
*  I mean, I don't think we're kind of notably closer
*  to general artificial intelligence now
*  than we were when I started my career.
*  There's been progress.
*  And I do think that we are kind of as a community
*  maybe looking a bit where the light is,
*  but the light is shining pretty bright there right now
*  and we're finding a lot of stuff.
*  So I don't wanna argue with the progress that's been made
*  in areas like deep learning, for example.
*  This touches another sort of related thing
*  that you've mentioned and that people might misinterpret
*  from the title of your book, ethical algorithm.
*  Is it possible for the algorithm
*  to automate some of those decisions?
*  Sort of higher level decisions of what kind of.
*  Like what should be fair.
*  What should be fair.
*  The more you know about a field,
*  the more aware you are of its limitations.
*  And so I'm pretty leery of sort of trying,
*  you know, there's so much we don't all,
*  we already don't know in fairness,
*  even when we're the ones picking the fairness definitions
*  and, you know, comparing alternatives
*  and thinking about the tensions
*  between different definitions.
*  But the idea of kind of letting the algorithm
*  start exploring as well.
*  I definitely think, you know,
*  this is a much narrower statement.
*  I definitely think that kind of algorithmic auditing
*  for different types of unfairness, right?
*  So like in this gerrymandering example,
*  where I might want to prevent not just discrimination
*  against very broad categories,
*  but against combinations of broad categories.
*  You know, you quickly get to a point
*  where there's a lot of categories.
*  There's a lot of combinations of end features.
*  And, you know, you can use algorithmic techniques
*  to sort of try to find the subgroups
*  on which you're discriminating the most
*  and try to fix that.
*  That's actually kind of the form of one of the algorithms
*  we developed for this fairness gerrymandering problem.
*  But I'm, you know, partly because of our technology,
*  you know, sort of our scientific ignorance
*  on these topics right now.
*  And also partly just because these topics
*  are so loaded emotionally for people
*  that I just don't see the value.
*  I mean, again, never say never,
*  but I just don't think we're at a moment
*  where it's a great time for computer scientists
*  to be rolling out the idea like, hey, you know,
*  not only have we kind of figured fairness out,
*  but, you know, we think the algorithm
*  should start deciding what's fair
*  or giving input on that decision.
*  I just don't, it's like the cost benefit analysis
*  to the field of kind of going there right now
*  just doesn't seem worth it to me.
*  That said, I should say that I think computer scientists
*  should be more philosophically,
*  like should enrich their thinking
*  about these kinds of things.
*  I think it's been too often used as an excuse
*  for roboticists working on autonomous vehicles, for example,
*  to not think about the human factor or psychology or safety.
*  In the same way, like computer scientists and algorithms
*  that have been sort of using it as an excuse.
*  And I think it's time for basically everybody
*  to become computer scientists.
*  I was about to agree with everything you said
*  except that last point.
*  I think that the other way of looking at it
*  is that I think computer scientists, you know,
*  and many of us are,
*  but we need to wade out into the world more, right?
*  I mean, just the influence that computer science
*  and therefore computer scientists
*  have had on society at large,
*  just like has exponentially magnified
*  in the last 10 or 20 years or so.
*  And, you know, before when we were just tinkering around
*  amongst ourselves and it didn't matter that much,
*  there was no need for sort of computer scientists
*  to be citizens of the world more broadly.
*  And I think those days need to be over very, very fast.
*  And I'm not saying everybody needs to do it,
*  but to me, like the right way of doing it
*  is to not to sort of think that everybody else
*  is gonna become a computer scientist,
*  but, you know, I think, you know,
*  people are becoming more sophisticated
*  about computer science, even laypeople.
*  You know, I think one of the reasons
*  we decided to write this book is we thought 10 years ago,
*  I wouldn't have tried this just because I just didn't think
*  that sort of people's awareness of algorithms
*  and machine learning, you know,
*  the general population would have been high.
*  And I mean, you would have had to first, you know,
*  write one of the many books,
*  kind of just explicating that topic to a lay audience first.
*  Now I think we're at the point where like lots of people
*  without any technical training at all,
*  know enough about algorithms and machine learning
*  that you can start getting to these nuances
*  of things like ethical algorithms.
*  I think we agree that there needs to be much more mixing,
*  but I think a lot of the onus of that mixing
*  needs to be on the computer science community.
*  Yeah, so just to linger on the disagreement,
*  because I do disagree with you on the point that I think
*  if you're a biologist, if you're a chemist,
*  if you're an MBA business person,
*  all of those things you can, like if you learned a program,
*  and not only program, if you learn to do machine learning,
*  if you learn to do data science,
*  you immediately become much more powerful
*  in the kinds of things you can do.
*  And therefore, literature, like library sciences,
*  like so you were speaking, I think,
*  deaf, I think it holds true what you're saying
*  for the next few years, but long-term,
*  if you're interested, to me,
*  if you're interested in philosophy,
*  you should learn a program,
*  because then you can scrape data
*  and study what people are thinking about on Twitter,
*  and then start making philosophical conclusions
*  about the meaning of life.
*  I just feel like the access to data,
*  the digitization of whatever problem you're trying to solve,
*  it fundamentally changes what it means
*  to be a computer scientist.
*  Being a computer scientist in 20, 30 years
*  will go back to being Donald Knuth-style
*  theoretical computer science,
*  and everybody would be doing basically,
*  exploring the kinds of ideas that you explore in your book.
*  It won't be a computer science major.
*  Yeah, I mean, I don't think I disagree,
*  but I think that that trend of more and more people
*  and more and more disciplines adopting ideas
*  from computer science, learning how to code,
*  I think that that trend seems firmly underway.
*  I mean, like an interesting,
*  digressive question along these lines is,
*  maybe in 50 years,
*  there won't be computer science departments anymore,
*  because the field will just sort of be ambient
*  in all of the different disciplines,
*  and people will look back,
*  and having a computer science department
*  will look like having an electricity department
*  or something.
*  It's like, everybody uses this, it's just out there.
*  I mean, I do think there will always be
*  that kind of Knuth-style core to it,
*  but it's not an implausible path
*  that we kind of get to the point
*  where the academic discipline of computer science
*  becomes somewhat marginalized
*  because of its very success in kind of infiltrating
*  all of science and society and the humanities, et cetera.
*  What is differential privacy,
*  or more broadly, algorithmic privacy?
*  Algorithmic privacy more broadly is just the study
*  or the notion of privacy definitions
*  or norms being encoded inside of algorithms.
*  And so, I think we count among this body of work,
*  just the literature and practice
*  of things like data anonymization,
*  which we kind of at the beginning
*  of our discussion of privacy, say like,
*  okay, this is sort of a notion of algorithmic privacy.
*  It kind of tells you something to go do with data,
*  but our view is that it's,
*  and I think this is now quite widespread,
*  that it's, despite the fact that those notions
*  of anonymization, kind of redacting and coarsening,
*  are the most widely adopted technical solutions
*  for data privacy, they are like deeply fundamentally flawed.
*  And so, to your first question,
*  what is differential privacy?
*  Differential privacy seems to be a much,
*  much better notion of privacy that kind of avoids
*  a lot of the weaknesses of anonymization notions
*  while still letting us do useful stuff with data.
*  What's anonymization of data?
*  So by anonymization, I'm kind of referring to techniques
*  like I have a database, the rows of that database
*  are let's say individual people's medical records, okay?
*  And I wanna let people use that data,
*  maybe I wanna let researchers access that data
*  to build predictive models for some disease,
*  but I'm worried that that will leak sensitive information
*  about specific people's medical records.
*  So anonymization broadly refers to the set of techniques
*  where I say like, okay, I'm first gonna like,
*  I'm gonna delete the column with people's names.
*  I'm going to not put, so that would be like a redaction,
*  right, I'm just redacting that information.
*  I am going to take ages and I'm not gonna like say
*  your exact age, I'm gonna say whether you're,
*  zero to 10, 10 to 20, 20 to 30.
*  I might put the first three digits of your zip code,
*  but not the last two, et cetera, et cetera.
*  And so the idea is that through some series of operations
*  like this on the data, I anonymize it.
*  Another term of art that's used is removing
*  personally identifiable information.
*  And this is basically the most common way
*  of providing data privacy, but that's in a way
*  that still lets people access some variant form of the data.
*  So at a slightly broader picture, as you talk about,
*  what does anonymization mean when you have
*  multiple databases, like with a Netflix prize
*  and you can start combining stuff together?
*  So this is exactly the problem with these notions, right?
*  Is that notions of anonymization, removing personally
*  identifiable information, the kind of fundamental
*  conceptual flaw is that these definitions kind of pretend
*  as if the data set in question is the only data set
*  that exists in the world or that ever will exist
*  in the future, and of course, things like the Netflix prize
*  and many, many other examples since the Netflix prize,
*  I think that was one of the earliest ones though,
*  you can re-identify people that were anonymized
*  in the data set by taking that anonymized data set
*  and combining it with other allegedly anonymized data sets
*  and maybe publicly available information about you.
*  For people who don't know, the Netflix prize
*  was being publicly released as data.
*  So the names from those rows were removed,
*  but what was released is the preference or the ratings
*  of what movies you like and you don't like,
*  and from that combined with other things,
*  I think foreign posts and so on,
*  you can start to figure out the names.
*  In that case, it was specifically
*  the internet movie database.
*  The active data.
*  Where lots of Netflix users publicly rate
*  their movie preferences, and so the anonymized data
*  in Netflix, it's just this phenomenon I think
*  that we've all come to realize in the last decade or so
*  is that just knowing a few apparently irrelevant,
*  innocuous things about you can often act as a fingerprint.
*  Like if I know what rating you gave to these 10 movies
*  and the date on which you entered these movies,
*  this is almost like a fingerprint for you
*  is in the sea of all Netflix users.
*  There was just another paper on this in Science or Nature
*  about a month ago that kind of 18 attributes.
*  I mean, my favorite example of this was actually
*  from a paper from several years ago now
*  where it was shown that just from your likes on Facebook,
*  just from the things on which you clicked
*  on the thumbs up button on the platform,
*  not using any information, demographic information,
*  nothing about who your friends are,
*  just knowing the content that you had liked
*  was enough to in the aggregate accurately predict things
*  like sexual orientation, drug and alcohol use,
*  whether you were the child of divorced parents.
*  So we live in this era where even the apparently
*  irrelevant data that we offer about ourselves
*  on public platforms and forums,
*  often unbeknownst to us, more or less acts as signature
*  or fingerprint and that if you can kind of do a join
*  between that kind of data and allegedly anonymized data,
*  you have real trouble.
*  So is there hope for any kind of privacy in a world
*  where a few likes can identify you?
*  So there is differential privacy.
*  What is differential privacy?
*  So differential privacy basically is an alternate,
*  much stronger notion of privacy
*  than these anonymization ideas.
*  And it's a technical definition,
*  but the spirit of it is we compare to alternate worlds.
*  So let's suppose I'm a researcher
*  and I wanna do, there's a database of medical records
*  and one of them is yours.
*  And I want to use that database of medical records
*  to build a predictive model for some disease.
*  So based on people's symptoms and test results and the like,
*  I wanna build a model predicting the probability
*  that people have disease.
*  So this is the type of scientific research
*  that we would like to be allowed to continue.
*  And in differential privacy,
*  you ask a very particular counterfactual question.
*  We basically compare two alternatives.
*  One is when I build this model
*  on the database of medical records,
*  including your medical record.
*  And the other one is where I do the same exercise
*  with the same database
*  with just your medical record removed.
*  So basically, it's two databases,
*  one with N records in it
*  and one with N minus one records in it.
*  The N minus one records are the same
*  and the only one that's missing in the second case
*  is your medical record.
*  So differential privacy basically says that any harms
*  that might come to you from the analysis
*  in which your data was included
*  are essentially nearly identical to the harms
*  that would have come to you
*  if the same analysis had been done
*  without your medical record included.
*  So in other words, this doesn't say that bad things
*  cannot happen to you as a result of data analysis.
*  It just says that these bad things
*  were going to happen to you already
*  even if your data wasn't included.
*  And to give a very concrete example,
*  like we discussed at some length,
*  the study in the 50s that was done
*  that established the link between smoking and lung cancer.
*  And we make the point that like,
*  well, if your data was used in that analysis
*  and the world kind of knew that you were a smoker
*  because there was no stigma associated with smoking
*  before those findings,
*  real harm might have come to you as a result of that study
*  that your data was included in.
*  In particular, your insurer now might have
*  a higher posterior belief that you might have lung cancer
*  and raise your premium.
*  So you've suffered economic damage.
*  But the point is that if the same analysis has been done
*  without, with all the other N minus one medical records
*  and just yours missing, the outcome would have been the same.
*  Your data wasn't idiosyncratically in crucial
*  to establishing the link between smoking and lung cancer
*  because the link between smoking and lung cancer
*  is like a fact about the world that can be discovered
*  with any sufficiently large database of medical records.
*  But that's a very low value of harm.
*  Yeah, so that's showing that very little harm is done.
*  Great, but how, what is the mechanism
*  of differential privacy?
*  So that's the kind of beautiful statement of it.
*  Well, what's the mechanism by which privacy is preserved?
*  Yeah, so it's basically by adding noise to computations.
*  Right, so the basic idea is that
*  every differentially private algorithm, first of all,
*  or every good differentially private algorithm,
*  every useful one is a probabilistic algorithm.
*  So it doesn't, on a given input,
*  if you gave the algorithm the same input multiple times,
*  it would give different outputs each time
*  from some distribution.
*  And the way you achieve differential privacy algorithmically
*  is by kind of carefully and tastefully adding noise
*  to a computation in the right places.
*  And to give a very concrete example,
*  if I wanna compute the average of a set of numbers,
*  the non-private way of doing that is to take those numbers
*  and average them and release a numerically precise value
*  for the average.
*  In differential privacy, you wouldn't do that.
*  You would first compute that average
*  to numerical precisions,
*  and then you'd add some noise to it.
*  You'd add some kind of zero mean,
*  you know, Gaussian or exponential noise to it,
*  so that the actual value you output
*  is not the exact mean, but it'll be close to the mean.
*  But it'll be close, the noise that you add
*  will sort of prove that nobody can kind of reverse engineer
*  any particular value that went into the average.
*  So noise is the savior.
*  How many algorithms can be aided by adding noise?
*  Yeah, so I'm a relatively recent member
*  of the differential privacy community.
*  My co-author Aaron Roth is, you know,
*  really one of the founders of the field
*  and has done a great deal of work,
*  and I've learned a tremendous amount working with him on it.
*  It's a pretty grown-up field already.
*  Yeah, but now it's pretty mature.
*  But I must admit, the first time I saw the definition
*  of differential privacy, my reaction was like,
*  wow, that is a clever definition,
*  and it's really making very strong promises.
*  And my, you know, I first saw the definition
*  in much earlier days, and my first reaction was like,
*  well, my worry about this definition would be
*  that it's a great definition of privacy,
*  but that it'll be so restrictive
*  that we won't really be able to use it.
*  Like, you know, we won't be able to compute many things
*  in a differentially private way.
*  So that's one of the great successes of the field, I think,
*  is in showing that the opposite is true,
*  and that, you know, most things that we know how to compute
*  absent any privacy considerations can be computed
*  in a differentially private way.
*  So for example, pretty much all of statistics
*  in machine learning can be done differentially privately.
*  So pick your favorite machine learning algorithm,
*  back propagation and neural networks, you know,
*  CART for decision trees, support vector machines,
*  boosting, you name it, as well as classic hypothesis testing
*  and the like in statistics.
*  None of those algorithms are differentially private
*  in their original form.
*  All of them have modifications that add noise
*  to the computation in different places, in different ways
*  that achieve differential privacy.
*  So this really means that to the extent that, you know,
*  we've become a, you know, a scientific community
*  very dependent on the use of machine learning
*  and statistical modeling and data analysis,
*  we really do have a path to kind of provide
*  privacy guarantees to those methods.
*  And so we can still, you know, enjoy the benefits
*  of kind of the data science era while providing, you know,
*  rather robust privacy guarantees to individuals.
*  So perhaps a slightly crazy question,
*  but if we take the ideas of differential privacy
*  and take it to the nature of truth
*  that's being explored currently,
*  so what's your most favorite and least favorite food?
*  Not a real foodie, so I'm a big fan of spaghetti.
*  Spaghetti? Yeah.
*  And what do you really don't like?
*  I really don't like cauliflower.
*  Wow, I love cauliflower.
*  Okay, but is one way to protect your preference for spaghetti
*  by having an information campaign, bloggers and so on,
*  of bots saying that you like cauliflower?
*  So like this kind of, the same kind of noise ideas.
*  I mean, if you think of in our politics today,
*  there's this idea of Russia hacking our elections.
*  What's meant there, I believe,
*  is bots spreading different kinds of information.
*  Is that a kind of privacy or is that too much of a stretch?
*  No, it's not a stretch.
*  I've not seen those ideas, you know,
*  that is not a technique that to my knowledge
*  will provide differential privacy.
*  But to give an example, like one very specific example
*  about what you're discussing is,
*  there was a very interesting project at NYU,
*  I think led by Helen Nissenbaum there,
*  in which they basically built a browser plugin
*  that tried to essentially obfuscate your Google searches.
*  So to the extent that you're worried
*  that Google is using your searches to build, you know,
*  predictive models about you to decide what ads to show you,
*  which they might very reasonably want to do,
*  but if you object to that,
*  they built this widget you could plug in,
*  and basically whenever you put in a query into Google,
*  it would send that query to Google,
*  but in the background all of the time from your browser,
*  it would just be sending this torrent
*  of irrelevant queries to the search engine.
*  So, you know, it's like a weed and chaff thing.
*  So, you know, out of every thousand queries,
*  let's say that Google was receiving from your browser,
*  one of them was one that you put in,
*  but the other 999 were not.
*  Okay, so it's the same kind of idea,
*  kind of, you know, privacy by obfuscation.
*  So I think that's an interesting idea.
*  Doesn't give you differential privacy.
*  It's also, I was actually talking to somebody
*  at one of the large tech companies recently
*  about the fact that, you know,
*  just this kind of thing that there are some times
*  when the response to my data
*  needs to be very specific to my data, right?
*  Like I type mountain biking into Google,
*  I want results on mountain biking,
*  and I really want Google to know
*  that I typed in mountain biking.
*  I don't want noise added to that.
*  And so I think there's sort of maybe
*  even interesting technical questions
*  around notions of privacy that are appropriate
*  where, you know, it's not that my data
*  is part of some aggregate like medical records
*  and that we're trying to discover important correlations
*  and facts about the world at large,
*  but rather, you know, there's a service
*  that I really want to, you know,
*  pay attention to my specific data,
*  yet I still want some kind of privacy guarantee.
*  And I think these kind of obfuscation ideas
*  are sort of one way of getting at that,
*  but maybe there are others as well.
*  So where do you think we'll land
*  in this algorithm driven society in terms of privacy?
*  So sort of China, like Kai-Fu Lee describes,
*  you know, it's collecting a lot of data on its citizens,
*  but in the best form, it's actually able to provide
*  a lot of sort of protect human rights
*  and provide a lot of amazing services.
*  And in its worst forms,
*  it can violate those human rights and limit services.
*  So where do you think we'll land?
*  So algorithms are powerful when they use data.
*  So as a society, do you think we'll give over more data?
*  Is it possible to protect the privacy of that data?
*  So I'm optimistic about the possibility of, you know,
*  balancing the desire for individual privacy
*  and individual control of privacy
*  with kind of societally and commercially
*  beneficial uses of data,
*  not unrelated to differential privacy
*  or suggestions that say like,
*  well, individuals should have control of their data.
*  They should be able to limit the uses of that data.
*  They should even, you know, there's fledgling discussions
*  going on in research circles about allowing people
*  selective use of their data and being compensated for it.
*  And then you get to sort of very interesting
*  economic questions like pricing, right?
*  And one interesting idea is that maybe differential privacy
*  would also be a conceptual framework
*  in which you could talk about the relative value
*  of different people's data,
*  like, you know, to demystify this a little bit.
*  If I'm trying to build a predictive model
*  for some rare disease,
*  and I'm gonna use machine learning to do it,
*  it's easy to get negative examples
*  because the disease is rare, right?
*  But I really want to have lots of people with the disease
*  in my data set, okay?
*  And so somehow those people's data
*  with respect to this application
*  is much more valuable to me
*  than just like the background population.
*  And so maybe they should be compensated more for it.
*  And so, you know, I think these are kind of very,
*  very fledgling conceptual questions
*  that maybe we'll have kind of technical thought on them
*  sometime in the coming years.
*  But I do think we'll, you know,
*  to kind of get more directly answer your question,
*  I think I'm optimistic at this point from what I've seen
*  that we will land at some, you know,
*  better compromise than we're at right now,
*  where again, you know, privacy guarantees
*  are few, far between and weak,
*  and users have very, very little control.
*  And I'm optimistic that we'll land in something
*  that, you know, provides better privacy overall
*  and more individual control of data and privacy.
*  But, you know, I think to get there,
*  it's again, just like fairness,
*  it's not gonna be enough to propose algorithmic solutions,
*  there's gonna have to be a whole kind of regulatory,
*  legal process that prods companies and other parties
*  to kind of adopt solutions.
*  And I think you've mentioned the word control a lot,
*  and I think giving people control,
*  that's something that people don't quite have
*  in a lot of these algorithms,
*  and that's a really interesting idea,
*  of giving them control.
*  Some of that is actually literally
*  an interface design question, sort of just enabling,
*  because I think it's good for everybody
*  to give users control.
*  It's almost not a trade-off,
*  except that you have to hire people
*  that are good at interface design.
*  Yeah, I mean, the other thing that has to be said, right,
*  is that, you know, it's a cliche,
*  but, you know, we, as the users of many systems,
*  platforms, and apps, you know, we are the product.
*  We are not the customer.
*  The customer are advertisers, and our data is the product.
*  Okay, so it's one thing to kind of suggest
*  more individual control of data and privacy and uses,
*  but this, you know, if this happens in sufficient degree,
*  it will upend the entire economic model
*  that has supported the internet to date,
*  and so some other economic model will have to be,
*  you know, will have to replace it.
*  So the idea of markets, you mentioned,
*  by exposing the economic model to the people,
*  they will then become a market.
*  They could be participants in it.
*  Participants in it.
*  And, you know, this is not a weird idea, right,
*  because there are markets for data already.
*  It's just that consumers are not participants in them.
*  There's like, you know, there's sort of, you know,
*  publishers and content providers on one side
*  that have inventory, and then they're advertisers
*  on the others, and, you know, you know,
*  Google and Facebook are running, you know,
*  they're pretty much their entire revenue stream
*  is by running two-sided markets between those parties, right?
*  And so it's not a crazy idea
*  that there would be like a three-sided market,
*  or that, you know, that on one side of the market
*  or the other, we would have proxies
*  representing our interests.
*  It's not, you know, it's not a crazy idea,
*  but it would, it's not a crazy technical idea,
*  but it would have pretty extreme economic consequences.
*  Speaking of markets, a lot of fascinating aspects
*  of this world arise not from individual humans,
*  but from the interaction of human beings.
*  You've done a lot of work in game theory.
*  First, can you say what is game theory,
*  and how does it help us model and study things?
*  Yeah, game theory, of course,
*  let us give credit where it's due.
*  They don't, you know, comes from the economist
*  first and foremost, but as I've mentioned before,
*  like, you know, computer scientists never hesitate
*  to wander into other people's turf,
*  and so there is now this 20-year-old field
*  called algorithmic game theory.
*  But, you know, game theory, first and foremost,
*  is a mathematical framework for reasoning
*  about collective outcomes
*  in systems of interacting individuals.
*  Yeah.
*  You know, so you need at least two people
*  to get started in game theory,
*  and many people are probably familiar
*  with Prisoner's Dilemma as kind of a classic example
*  of game theory and a classic example
*  where everybody looking out
*  for their own individual interests
*  leads to a collective outcome
*  that's kind of worse for everybody
*  than what might be possible if they cooperated, for example.
*  But cooperation is not an equilibrium
*  in Prisoner's Dilemma.
*  And so my work in the field of algorithmic game theory
*  more generally in these areas
*  kind of looks at settings
*  in which the number of actors
*  is potentially extraordinarily large,
*  and their incentives might be quite complicated
*  and kind of hard to model directly,
*  but you still want kind of algorithmic ways
*  of kind of predicting what will happen
*  or influencing what will happen
*  in the design of platforms.
*  So what to you is the most beautiful idea
*  that you've encountered in game theory?
*  There's a lot of them.
*  I'm a big fan of the field.
*  I mean, you know, I mean, technical answers to that,
*  of course, would include Nash's work
*  just establishing that there's a competitive equilibrium
*  under very, very general circumstances,
*  which in many ways kind of put the field
*  on a firm conceptual footing,
*  because if you don't have equilibrium,
*  it's kind of hard to ever reason about what might happen
*  since there's just no stability.
*  So just the idea that stability can emerge
*  when there's multiple people.
*  Not that it will necessarily emerge,
*  just that it's possible, right?
*  Like the existence of equilibrium doesn't mean
*  that sort of natural iterative behavior
*  will necessarily lead to it.
*  In the real world, yes.
*  Maybe answering a slightly less personally
*  than you asked the question,
*  I think within the field of algorithmic game theory,
*  perhaps the single most important
*  kind of technical contribution that's been made
*  is the realization between close connections
*  between machine learning and game theory,
*  and in particular between game theory
*  and the branch of machine learning
*  that's known as no-regret learning.
*  And this sort of provides a very general framework
*  in which a bunch of players interacting
*  in a game or a system,
*  each one kind of doing something
*  that's in their self-interest
*  will actually kind of reach an equilibrium
*  and actually reach an equilibrium
*  in a pretty, a rather short amount of steps.
*  So you kind of mentioned acting greedily
*  can somehow end up pretty good for everybody.
*  Or pretty bad.
*  Or pretty bad.
*  It will end up stable.
*  Yeah, right.
*  And stability or equilibrium by itself
*  is not necessarily either a good thing or a bad thing.
*  So what's the connection between machine learning
*  and the ideas of people?
*  Well, I mean, I think we kind of talked about these ideas
*  already in kind of a non-technical way,
*  which is maybe the more interesting way
*  of understanding them first.
*  Which is, we have many systems, platforms,
*  and apps these days that work really hard to use our data
*  and the data of everybody else on the platform
*  to selfishly optimize on behalf of each user.
*  So let me give, I think, the cleanest example,
*  which is just driving apps, navigation apps,
*  like Google Maps and Waze,
*  where miraculously compared to when I was growing up,
*  at least, the objective would be the same
*  when you wanted to drive from point A to point B,
*  spend the least time driving.
*  Not necessarily minimize the distance,
*  but minimize the time, right?
*  And when I was growing up,
*  the only resources you had to do that
*  were like maps in the car,
*  which literally just told you what roads were available.
*  And then you might have like half-hourly traffic reports,
*  just about the major freeways, but not about side roads.
*  So you were pretty much on your own.
*  And now we've got these apps, you pull it out and you say,
*  I wanna go from point A to point B.
*  And in response kind of to what everybody else is doing,
*  if you like what all the other players in this game
*  are doing right now,
*  here's the route that minimizes your driving time.
*  So it is really kind of computing a selfish best response
*  for each of us in response to what all of the rest of us
*  are doing at any given moment.
*  And so, I think it's quite fair to think of these apps
*  as driving or nudging us all towards the competitive
*  or Nash equilibrium of that game.
*  Now you might ask like, well, that sounds great.
*  Why is that a bad thing?
*  Well, it's known both in theory
*  and with some limited studies from actual like traffic data
*  that all of us being in this competitive equilibrium
*  might cause our collective driving time to be higher,
*  maybe significantly higher
*  than it would be under other solutions.
*  And then you have to talk about
*  what those other solutions might be
*  and what the algorithms to implement them are,
*  which we do discuss in the kind of game theory chapter
*  of the book.
*  But similarly, on social media platforms or on Amazon,
*  all these algorithms that are essentially trying
*  to optimize our behalf, they're driving us
*  in a colloquial sense towards some kind
*  of competitive equilibrium.
*  And one of the most important lessons of game theory
*  is that just because we're at equilibrium
*  doesn't mean that there's not a solution
*  in which some or maybe even all of us might be better off.
*  And then the connection to machine learning, of course,
*  is that in all these platforms I've mentioned,
*  the optimization that they're doing on our behalf
*  is driven by machine learning,
*  predicting where the traffic will be,
*  predicting what products I'm gonna like,
*  predicting what would make me happy in my newsfeed.
*  Now, in terms of the stability and the promise of that,
*  I have to ask just out of curiosity,
*  how stable are these mechanisms that you,
*  game theory is just, the economists came up with,
*  and we all know that economists don't live
*  in the real world, just kidding.
*  Do you think when we look at the fact
*  that we haven't blown ourselves up
*  from a game theoretic concept of mutually shared destruction,
*  what are the odds that we destroy ourselves
*  with nuclear weapons, as one example
*  of a stable game theoretic system?
*  Just to prime your viewers a little bit,
*  I mean, I think you're referring to the fact
*  that game theory was taken quite seriously
*  back in the 60s as a tool for reasoning about
*  kind of Soviet, US nuclear armament,
*  disarmative, detente, things like that.
*  I'll be honest, as huge of a fan as I am of game theory
*  and its kind of rich history, it still surprises me
*  that you had people at the Rand Corporation
*  back in those days kind of drawing up two by two tables
*  and one, the row player is the US
*  and the column player is Russia,
*  and that they were taking seriously.
*  I'm sure if I was there, maybe it wouldn't have seemed
*  as naive as it does at the time.
*  It seems to have worked, which is why it seems naive.
*  Well, we're still here.
*  We're still here in that sense.
*  Yeah, even though I kind of laugh at those efforts,
*  they were more sensible then than they would be now,
*  because there were sort of only two nuclear powers
*  at the time, and you didn't have to worry
*  about deterring new entrants
*  and who was developing the capacity.
*  It's definitely a game with more players now
*  and more potential entrants.
*  I'm not in general somebody who advocates using
*  kind of simple mathematical models
*  when the stakes are as high as things like that
*  and the complexities are very political and social,
*  but we are still here.
*  So you've worn many hats, one of which,
*  the one that first caused me to become a big fan
*  of your work many years ago is algorithmic trading.
*  So I have to just ask a question about this
*  because you have so much fascinating work there.
*  In the 21st century, what role do you think algorithms have
*  in the space of trading, investment,
*  in the financial sector?
*  Yeah, it's a good question.
*  I mean, in the time I've spent on Wall Street and in finance,
*  I've seen a clear progression,
*  and I think it's a progression that kind of models
*  the use of algorithms and automation
*  more generally in society,
*  which is the things that kind of get taken over
*  by the algos first are sort of the things
*  that computers are obviously better at than people, right?
*  So first of all, there needed to be this era of automation
*  where just financial exchanges became largely electronic,
*  which then enabled the possibility of trading
*  becoming more algorithmic because once the exchanges
*  are electronic, an algorithm can submit an order
*  through an API just as well as a human can do at a monitor.
*  Can do it really quickly, can read all the data.
*  Yeah, and so I think the places where algorithmic trading
*  have had the greatest inroads and had the first inroads
*  were in kind of execution problems,
*  kind of optimized execution problems.
*  So what I mean by that is at a large brokerage firm,
*  for example, one of the lines of business might be
*  on behalf of large institutional clients taking
*  what we might consider difficult trades.
*  So it's not like a mom and pop investor saying,
*  I wanna buy a hundred shares of Microsoft.
*  It's a large hedge fund saying,
*  I want to buy a very, very large stake in Apple,
*  and I wanna do it over the span of a day.
*  And it's such a large volume that if you're not clever
*  about how you break that trade up, not just over time,
*  but over perhaps multiple different electronic exchanges
*  that all let you trade Apple on their platform,
*  you will push prices around in a way
*  that hurts your execution.
*  So this is an optimization problem.
*  This is a control problem, right?
*  And so machines are better.
*  We know how to design algorithms that are better
*  at that kind of thing than a person is going to be able
*  to do because we can take volumes of historical
*  and real-time data to kind of optimize the schedule
*  with which we trade.
*  And similarly, high-frequency trading,
*  which is closely related,
*  but not the same as optimized execution,
*  where you're just trying to spot very, very temporary
*  mispricings between exchanges or within an asset itself,
*  or just predict directional movement of a stock
*  because of the kind of very, very low-level granular buying
*  and selling data in the exchange.
*  Machines are good at this kind of stuff.
*  It's kind of like the mechanics of trading.
*  What about the, can machines do long-terms of prediction?
*  Yeah, so I think we are in an era where clearly
*  there have been some very successful quant hedge funds
*  that are in what we would traditionally call
*  still in the stat arb regime.
*  So, you know, stat arb referring to statistical arbitrage,
*  but for the purposes of this conversation,
*  what it really means is making directional predictions
*  in asset price movement or returns.
*  Your prediction about that directional movement is good for,
*  you know, you have a view that it's valid for some period
*  of time between a few seconds and a few days,
*  and that's the amount of time that you're going to kind of get
*  into the position, hold it, and then hopefully be right
*  about the directional movement and, you know, buy low
*  and sell high as the cliche goes.
*  So that is a, you know, kind of a sweet spot, I think,
*  for quant trading and investing right now
*  and has been for some time.
*  When you really get to kind of more Warren Buffett-style
*  time scales, right, like, you know, my cartoon of Warren
*  Buffett is that, you know, Warren Buffett sits and thinks
*  what the long-term value of Apple really should be,
*  and he doesn't even look at what Apple's doing today.
*  He just decides, you know, you know, I think that this is what
*  its long-term value is, and it's far from that right now,
*  and so I'm going to buy some Apple or, you know,
*  short some Apple, and I'm going to sit on that
*  for 10 or 20 years, okay?
*  So when you're at that kind of time scale or even more
*  than just a few days, all kinds of other sources of risk
*  and information, you know, so now you're talking about
*  holding things through recessions and economic cycles.
*  Wars can break out.
*  So there you have to understand the human nature
*  at a level that. Yeah, and you need to just be able
*  to ingest many, many more sources of data
*  that are on wildly different time scales, right?
*  So if I'm an HFT, I'm a high-frequency trader,
*  like I don't, I really, my main source of data
*  is just the data from the exchanges themselves
*  about the activity in the exchanges, right?
*  And maybe I need to pay, you know, I need to keep an eye
*  on the news, right, because, you know,
*  that can cause sudden, you know, the, you know,
*  CEO gets caught in a scandal or, you know,
*  gets run over by a bus or something
*  that can cause very sudden changes.
*  But, you know, I don't need to understand economic cycles.
*  I don't need to understand recessions.
*  I don't need to worry about the political situation
*  or war breaking out in this part of the world,
*  because, you know, all I need to know is,
*  as long as that's not gonna happen
*  in the next 500 milliseconds, then, you know, my model's good.
*  When you get to these longer time scales,
*  you really have to worry about that kind of stuff.
*  And people in the machine learning community
*  are starting to think about this.
*  We held a, we jointly sponsored a workshop at Penn
*  with the Federal Reserve Bank of Philadelphia
*  a little more than a year ago on, you know,
*  I think the title was something like
*  Machine Learning for Macroeconomic Prediction.
*  You know, macroeconomic referring specifically
*  to these longer time scales.
*  And, you know, it was an interesting conference,
*  but it, you know, it left me with greater confidence
*  that we have a long way to go to, you know.
*  And so I think that people that, you know,
*  in the grand scheme of things, you know,
*  if somebody asked me like, well,
*  whose job on Wall Street is safe from the bots?
*  I think people that are at that longer, you know,
*  the time scale and have that appetite
*  for all the risks involved in long-term investing
*  and that really need kind of,
*  not just algorithms that can optimize from data,
*  but they need views on stuff.
*  They need views on the political landscape,
*  economic cycles and the like.
*  And I think, you know, they're pretty safe for a while,
*  as far as I can tell.
*  But Warren Buffett's job is safe for a little while.
*  Yeah, I'm not seeing, you know,
*  a robo Warren Buffett anytime soon.
*  Should give him comfort.
*  Last question.
*  If you could go back to,
*  if there's a day in your life you could relive
*  because it made you truly happy,
*  maybe outside family.
*  Yeah, otherwise we'd be out here.
*  What day would it be?
*  What, can you look back, you remember just being,
*  profoundly transformed in some way or blissful?
*  I'll answer a slightly different question,
*  which is like, what's a day in my life or my career
*  that was kind of a watershed moment?
*  I went straight from undergrad to doctoral studies.
*  And, you know, that's not at all atypical.
*  And I'm also from an academic family.
*  Like my dad was a professor,
*  my uncle on his side is a professor.
*  Both my grandfathers were professors.
*  All kinds of majors too, philosophy, I saw.
*  Yeah, kind of all over the map, yeah.
*  And I was a grad student here just up the river at Harvard
*  and then came to study with Les Valiant,
*  which was a wonderful experience.
*  But, you know, I remember my first year of graduate school,
*  I was generally pretty unhappy.
*  And I was unhappy because, you know,
*  at Berkeley as an undergraduate, you know,
*  yeah, I studied a lot of math and computer science,
*  but it was a huge school, first of all.
*  And I took a lot of other courses, as we discussed.
*  I started as an English major and took history courses
*  and art history classes and had friends, you know,
*  that did all kinds of different things.
*  And, you know, Harvard's a much smaller institution
*  than Berkeley and its computer science department,
*  especially at that time,
*  was a much smaller place than it is now.
*  And I suddenly just felt very, you know,
*  like I'd gone from this very big world
*  to this highly specialized world.
*  And now all of the classes I was taking
*  were computer science classes.
*  And I was only in classes with math
*  and computer science people.
*  And so I was, you know, I thought often
*  in that first year of grad school
*  about whether I really wanted to stick with it or not.
*  And, you know, I thought like, oh,
*  I could, you know, stop with a master's,
*  I could go back to the Bay Area and to California.
*  And, you know, this was in one of the early periods
*  where there was, you know, like,
*  you could definitely get a relatively good job,
*  paying job at one of the tech companies back,
*  you know, that were the big tech companies back then.
*  And so I distinctly remember like kind of a late spring day
*  when I was kind of, you know, sitting in Boston Common
*  and kind of really just kind of chewing over
*  what I wanted to do with my life.
*  And then I realized like, okay, you know,
*  and I think this is where my academic background
*  helped me a great deal.
*  I sort of realized, you know,
*  yeah, you're not having a great time right now.
*  This feels really narrowing,
*  but you know that you're here for research eventually
*  and to do something original and to try to, you know,
*  carve out a career where you kind of, you know,
*  choose what you want to think about, you know,
*  and have a great deal of independence.
*  And so, you know, at that point,
*  I really didn't have any real research experience yet.
*  I mean, it was trying to think about some problems
*  with very little success,
*  but I knew that like I hadn't really tried to do the thing
*  that I knew I'd come to do.
*  And so I thought, you know,
*  I'm gonna stick through it for the summer.
*  And, you know, and that was very formative
*  because I went from kind of contemplating quitting
*  to, you know, a year later,
*  it being very clear to me I was gonna finish
*  because I still had a ways to go,
*  but I kind of started doing research.
*  It was going well.
*  It was really interesting.
*  And it was sort of a complete transformation.
*  You know, and it's just that transition
*  that I think every doctoral student makes at some point,
*  which is to sort of go from being like a student
*  of what's been done before to doing, you know,
*  your own thing and figure out what makes you interested
*  in what your strengths and weaknesses are as a researcher.
*  And once, you know, I kind of made that decision
*  on that particular day at that particular moment
*  in Boston Common, you know, I'm glad I made that decision.
*  And also just accepting the painful nature of that journey.
*  Exactly, exactly.
*  And in that moment said, I'm gonna stick it out.
*  Yeah, I'm gonna stick around for a while.
*  Well, Michael, I've looked off to your work for a long time.
*  It's really nice to talk to you.
*  Thank you so much for joining.
*  It's great to get back in touch with you too
*  and see how great you're doing as well.
*  Thank you. Thanks a lot.
*  Appreciate it. Thanks, Michael.
