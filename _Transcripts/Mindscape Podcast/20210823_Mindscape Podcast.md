---
Date Generated: June 08, 2024
Transcription Model: whisper medium 20231117
Length: 5745s
Video Keywords: []
Video Views: 12043
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2021/08/23/161-w-brian-arthur-on-complexity-economics/

Economies in the modern world are incredibly complex systems. But when we sit down to think about them in quantitative ways, it’s natural to keep things simple at first. We look for reliable relations between small numbers of variables, seek equilibrium configurations, and so forth. But those approaches don’t always work in complex systems, and sometimes we have to use methods that are specifically adapted to the challenges of complexity. That’s the perspective of W. Brian Arthur, a pioneer in the field of complexity economics, according to which economies are typically not in equilibrium, not made of homogeneous agents, and are being constantly updated. We talk about the basic ideas of complexity economics, how it differs from more standard approaches, and what it teaches us about the operation of real economies.

W. Brian Arthur received his Ph.D. in operations research from the University of California, Berkeley. He is currently an External Faculty Member at the Santa Fe Institute, IBM Faculty Fellow, and Visiting Researcher in the Intelligent Systems Lab at PARC. He was formerly the Morrison Professor of Economics and Population Studies and Professor of Biology at Stanford. He is known for developing the theory of increasing returns in economics. Among his awards are a Guggenheim Fellowship, the Schumpeter Prize in economics, and the Lagrange Prize for complexity.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel:  @Sean Carroll  

#podcast #ideas #science #philosophy #culture
---

# Mindscape 161 | W. Brian Arthur on Complexity Economics
**Mindscape Podcast:** [August 23, 2021](https://www.youtube.com/watch?v=0rGPZ-JbcIc)
*  Hello everyone, welcome to the Mindscape Podcast. I'm your host, Sean Carroll.
*  Longtime listeners will know that one of my areas of interest is complex systems,
*  the study of complexity, the kind of thing that the Santa Fe Institute does and was founded to do.
*  And if there is any system we can imagine that you would characterize as complex,
*  it would be an economy, right? Economy of a large industrialized country. There are a lot
*  of moving parts related to each other in different ways. It seems as if a priori,
*  economics and complexity theory would go hand in hand. But in fact, when you actually sit down
*  to do economics, just like when you sit down to do any other science, you look for simplifications,
*  right? You look for things you don't need to pay attention to, simple versions of the problem that
*  you can really get a lot of insight into. And in economics, this takes a lot of different forms.
*  We assume that the different people in an economy are more or less rational, that they have complete
*  information, that they're more or less all the same kind of people. And most of all,
*  that the economy is basically in equilibrium, right? Think of supply and demand. Given a certain
*  supply curve and a certain demand curve, the price will adjust to a certain point relatively
*  rapidly and then you'll be in equilibrium. So complex systems research is all about things
*  where you cannot assume that all the parts are the same. You cannot treat things as if they were in
*  equilibrium. You can imagine that different parts of the system have different amounts of information
*  and so forth. So this opens the idea that economics is actually not taking full advantage of the
*  insights gained from complex systems research. And we should study something called complexity
*  economics. That's what we're going to talk about today with W. Brian Arthur, who's one of the
*  founders of this field. Now, I should say, you know, Brian is not a quirky outsider. He was a
*  professor at Stanford for a long time, the youngest person ever to be given an endowed chair at
*  Stanford. But he's one of the founders of this field of complexity economics, dating back to the
*  time when the Santa Fe Institute was founded in the 1980s. He invented several of the foundational
*  puzzles and methods in this field. And he thinks that to this day, the economics profession as a
*  whole hasn't quite taken on the lessons of complexity theory. We're still largely in a
*  certain neoclassical paradigm that treats the world as a much simpler, much less dynamic thing
*  than it really is. So this is a fun conversation, both for the economic insights, but also for,
*  you know, the way of thinking that you become imbued with when you start thinking about the
*  world as a complex system, getting rid of simplifications that simplify over much,
*  thinking of the different layers of the world interacting with each other, thinking about the
*  evolution and the dynamical aspects of the problem as built in rather than things that we can try to
*  ignore, right? Real economies have crashes and bubbles, and you can predict the probability of
*  different things. But if you just look at the equilibrium, you'll never find that kind of
*  behavior. So it'll be useful for anyone interested in society, economics, science, or complexity,
*  which I hope is everyone out there listening to this podcast. So let's go.
*  Brian Arthur, welcome to the Mindscape Podcast.
*  Yeah, hi.
*  So I wanted to start actually, we had Neil Johnson on the podcast about a year ago. I don't know if
*  you know Neil, but he's another complexity person, and he told us about the alpha role problem.
*  Right.
*  But I'm going to presume that maybe, you know, people have forgotten what it is. And I think
*  that you're at least one of if not the originator of the alpha role problem. And it's a nice setup
*  for what we're going to be talking about here. So why don't you remind us what that is all about?
*  Okay. I usually like to flex a few muscles before I jump in here. Anyway, yeah, I am the original,
*  uh, I guess I cooked up the alpha role problem sometime in the, uh, in the early 90s.
*  Alpha roles a bar in Canyon Road in Santa Fe. And on Thursday nights, they used to have Irish music
*  and I would show up. It's a pretty cramped place. And so it began to occur to me, should I go to
*  alpha role this Thursday or not? And I realized that a lot of other people would think that too.
*  So if you start to look at that as a logical problem, say of a hundred people thinking
*  independently, maybe I'll go to alpha role tonight. But if there's more than let's say 60 there,
*  it's going to be awful crowded and smoky and horrible. Um, I don't want to go. If I think
*  there'd be less than 60, I will go. And I realized that posed a kind of strange logical problem
*  for forecasting. Uh, economics is very fond of forecasting and we call it expectations.
*  Uh, if everybody had the same forecasters sitting on their desks, say a little plastic device and
*  it forecasted that 74 people would go this Thursday, then nobody would go.
*  If it said that thinks 15 will go, everybody would go. So it was a strange situation
*  where, um, whatever people jointly forecasted would be negated. If many people think, uh,
*  if everybody thinks many people will go and nobody will go, if they think few will go,
*  everybody will go. So forecasts are automatically negated and it's a kind of, uh, liar's paradox
*  for economics. I posed the problem. I came up with my own solution to it, which was to throw
*  overboard any attempt to be deductive. That wasn't working very well. Uh, there's,
*  you can't really come up with a solution that everybody shares. So I began to think,
*  and this was with the inspiration of John Holland. He wasn't part of this problem,
*  but he certainly inspired my answer. What if everybody had their own, uh, collection of
*  forecasts? So I might've maybe 15, 20 different ways to forecast and a guy down the street might
*  have a similar, uh, number, but different forecasts. So you have a whole ecology of forecasts
*  and how would that work? Each, um, I could track which forecasting methods worked well for me.
*  Uh, think of people doing this on the stock market, which they pretty much do all the time.
*  I could see what didn't work, throw those overboard and gradually find what does work.
*  And so I programmed this to see what would happen. Lo and behold, forecasts came out,
*  forecasting methods formed a little ecology because whether my method is reasonably accurate
*  or not depends on everybody else's method that I'm in there with. And so it was my strategy or my
*  forecasts, uh, trying to survive in a little ecology or a sea of other people's forecasts.
*  The whole thing settled down to about 60. There was a lot of chaotic noise around that.
*  And it was a weird thing. Physicists got this right away. And my good friend at the time,
*  Perry Bach, uh, took this problem, faxed it to all his physics friends. And suddenly the problem
*  became famous in physics. The economists didn't quite know what to make of it. They kind of
*  walked around it and looked at it and said, you know, uh, their usual solution was to say
*  everybody's identical, uh, by assumption. Let's, uh, say therefore they have identical methods
*  for forecasting. But as I said, that doesn't work in this problem. What does work is an inductive
*  approach. Uh, I think maybe, uh, these possibilities for forecasting might work. Somebody else might
*  think other possibilities work and the solution never quite settles down because as, uh, people
*  keep trying these and different people show up as a result, um, the situation keeps changing. So it
*  never quite settles, but it is attracted into this comfort zone of about 60 simply because if
*  a lot of people are forecasting high numbers, uh, for quite a while, uh, those forecasts won't be
*  validated. Uh, they won't show up. If people are forecasting low numbers for a long time, um,
*  they'll all show up and, and high forecasts would be validated. So, so there's a kind of tendency
*  to the middle. I can see why complexity is arising in this, right? You're allowing the different
*  agents to use different set of strategies and there's some obvious notion of complexity there.
*  What, one of the interesting things about it though, is you use this to illustrate an issue
*  in economics and, but there's no mention of money or prices or goods or anything like that. So it
*  lets, it makes me wonder, you know, how are you even defining the word economics, which presumably
*  is the easy word in this phrase, complexity economics.
*  I wish. Yeah. Uh, what I, I think of the economy as the set of ongoing arrangements we make,
*  I throw in the word ongoing because this keeps changing. It's the arrangements and actions we
*  make, uh, to, uh, try to fulfill our needs. So you could say it's a market, it's got goods,
*  it's got prices, but what I just said is much more general. It could be barter. It could be
*  Robinson Cruz, who living alone. It's, uh, it's how we organize yourselves to fill,
*  to try to fulfill our needs. And that often might mean we might have a need to hear Irish music
*  Thursday night. And so this is very much economists immediately recognize what I just said as a,
*  an economic problem. There's incentives to do something, but the space in which you're
*  trying to do it is, is a function of what other people are, or the way other people are trying to
*  solve the same problem. So the essence of economics, I think is not, um,
*  the essence of economics is not markets and prices and things being produced in a real economy.
*  That's very important, but the essence of economics is trying to make decisions
*  in a situation where other people are trying to make decisions as well. And for me, that's very
*  much complexity. Uh, I'll give you an example of that, that I think is totally trivial. Uh,
*  you might be on a freeway here in California. Uh, let's say the traffic's quite dense for some
*  reason, a lot of cars packed in. I'm trying to make decisions about my speed and the lane I'm using
*  based upon the traffic, but the traffic consists of other people trying to make decisions.
*  Independently in different cars, uh, in the traffic. And if you look at that formally,
*  uh, I sometimes use this as an example. And I once shocked audiences. I said, if you think about that
*  formally, there's no such thing as traffic. Traffic doesn't exist. Cars exist. The local
*  cars surrounding you, we tend to call traffic, but it doesn't quite exist. So it's basically
*  individuals trying to make decisions in a situation where other individuals are trying
*  to make decisions. I got a lovely comment after saying that one time, uh, uh, God, I would not
*  like to be in a car of Arthur's drive. He doesn't believe in traffic. No, but I like that. Actually,
*  this is great. I've already learned something because that's the best definition of economics
*  I've ever heard that we have desires, right? We have goals, we have incentives, and there's a bunch
*  of agents with different ones and they're sort of jostling up against each other. And how do they
*  organize that? How do they make things happen? So to hopefully everyone's mutual benefit, I suppose.
*  Oh, well, uh, to be very Western about it, we would say, or to be very economist about it,
*  we'd say to our own benefit and hopefully, hopefully that spreads out and benefits other
*  people. But at the center of economics, at least the center of what's interesting in economics is
*  individuals. We call them agents, sometimes players, sometimes investors, sometimes
*  consumers and so on. Individuals trying to make decisions in a situation. I would call it an
*  ecology of other people trying to make decisions, maybe in the same milieu, the same situation.
*  And that's what's interesting because people's behavior is not predictable. It's not like
*  ions and this is maybe not the right jargon. Ions in the spin glass, apparently are a lot more
*  predictable than human beings. Donating money to help people is a wonderful and selfless act,
*  but how can you feel confident that your donations are improving the most lives?
*  You could do weeks of research to find charities that are out there, what programs they run,
*  how effective they are, or you could visit givewell.org. There you'll get a short vetted
*  list of the best charities they found at saving or improving lives the most per dollar. Every time
*  I go to the webpage at givewell.org, I end up donating because their causes are so good and so
*  compelling, whether it's fighting malaria, giving vaccinations, deworming, vitamins, or just straight
*  small amounts of cash to people in poverty to help them get out of it. If you've never donated to
*  GiveWell's Recommended Charities before, you can have your donation matched up to $1,000 before the
*  end of August or as long as matching funds last. To claim your match, go to givewell.org and pick
*  podcast and Sean Carroll's Mindscape at checkout. Make sure they know that you heard about GiveWell
*  from Mindscape to get your donation matched. I do like this because it casts economics in a
*  light where the complexity aspects of it are right there front and center. And I guess therefore,
*  the audience which might not be trained in ordinary economics, let's contrast this.
*  There's sort of the standard neoclassical economic picture, which you contrast with
*  the complexity economics picture. And I think that you try to make the argument that standard
*  economics is a subset of complexity economics, right? Complexity economics is not a subset of
*  classical. It's that complexity economics is letting a lot more freedom into the way we think
*  about things. Yes, I think standard economics, it's called neoclassical economics. We've had
*  this for the last 150 years or so, albeit in different forms. And the way economics is done,
*  let me back up a bit. Around the 1870s, it began to seem a good idea to many economists in England,
*  actually, Germany and Austria, largely France to in Europe, to think that they could use algebra
*  and calculus to really look more formally and more rigorously at problems and economics.
*  And that meant the price of doing that, I think that was successful. And we've it's lasted for
*  quite a long time and will still continue, no doubt. But the price of doing that was to like in
*  physics, which was emulating to quite some degree, you had to make certain assumptions.
*  And the assumptions that economists came up with to solve problems in different settings in economics
*  was to assume individual players that were very often identical. So that were rational, meaning
*  they could solve any logical problem, or they could optimize in any setting. So they were supposed to,
*  by assumption, be super bright, that they're well informed, they knew that everybody else was just
*  like them. They knew everybody else's preferences. And sometimes you could say, well, they're a bit
*  blurred, but they know the probabilities of how other people would react and so on. So they're
*  well informed. And then the whole thing is supposed to happen at equilibrium. So let me
*  give my version of that. And what you're interested in in economics is how individual behavior
*  leads to an overall outcome. And of course, an overall outcome would feed back to individual
*  behavior, just like the cars and traffic. So how do the individual agents together act so that some
*  overall outcome may be in the market forms. And we want to look at situations that are in balance,
*  are consistent, just to keep the mathematics simple. So let's look for a solution in which
*  everybody's identical. They're all hyper rational, they're solving an optimization problem,
*  maybe under constraints. And you're looking for an outcome that causes the individuals not to
*  need to or want to change. So it's a bit like saying, and forgive me here for being
*  slightly mean about this, but it's a bit like asking how do butterflies fly? And okay, well,
*  we'll figure that out by core forming them and nailing them to a board and examining the wings.
*  I think that that's rather extreme to say, but we're looking at consistency in standard economics,
*  what behaviors consistent with the outcome it mutually creates. And in complexity economics,
*  the whole idea is to drop those assumptions, or at least things didn't come out that way.
*  That's not the way it started. But now amounts to saying, what if individuals differ? What if they're
*  not hyper rational? What if they're not well informed? And what if they're just reacting
*  to the outcome and the outcome never settles down and they keep reacting at infinite item?
*  And what would economics look like? So it's not that anybody said we're looking to have a more
*  general economics. But if you start to say we'll do away with the assumptions, it is more general.
*  It's like in mathematics, you can say, well, we're not quite sure we want to include
*  Euclid's fifth axiom here. So let's drop that and have a non Euclidean geometry. And let's examine
*  that. And I don't want to make complexity sound any more difficult or highfalutin than it is. But
*  it's essentially looking at economics under more realistic conditions. And what you find is the
*  economy, or the system you're looking at starts to look much less ordered, and perfect and mechanical,
*  and much more like changing ecology, where things change and may never settle down.
*  You know, it's funny, because there clearly is some level of parallelism with physics. Number one,
*  you mentioned the 1870s as the beginning of the mathematization of economics. And to my mind,
*  when you say 1870s, I'm thinking the beginning of statistical mechanics and Boltzmann and Maxwell
*  and thinking of thermodynamics coming out of all these motions of atoms and using similar techniques,
*  but also the idea of equilibrium versus non equilibrium. Like to my chagrin, most
*  thermodynamics and statistical mechanics over the history of physics has also been in this equilibrium
*  context, where you sort of imagine that everything quickly reaches a more or less steady state and
*  you can study things then it's only in the last 15 or 20 years that we've really made
*  important progress in non equilibrium statistical mechanics. Right. It's not a coincidence.
*  At all. One of the founders of the field in those days, Alfred Marshall, really important economist
*  at Cambridge, England, was very highly trained in mathematical physics. I think he was second
*  Wrangler in physics the year he graduated. So and subsequently between 1870, roughly and 1900s,
*  economists did study statistical mechanics. They were studying people like Boltzmann and others
*  who had brought in this point of view. And I wouldn't say they lifted it wholesale,
*  but they thought this was probably similarly a very good approach. What I'm finding at the moment is
*  that people sometimes say to me, you know, aren't you trying to shoehorn economics into
*  a new approach called complexity? And I say, no, not at all.
*  We, there is a whole movement in sciences away from looking at things totally mechanistically
*  in some sort of Newtonian framework or some kind of statistical mechanics framework
*  at equilibrium and looking at questions of how solutions form over time, not how they persist
*  over time, which may not at all give you equilibrium, in fact, almost by definition, it wouldn't.
*  And so we're looking more at formation. We're looking at how things form, be they species or
*  be they whatever galaxies or larger complexes in the universe. How do things change over time?
*  Will they ever settle down? And so in some way, it's not surprising that that emphasis in
*  formation is also coming into the social sciences, economics in particular. And I think that it's
*  inevitable. One of the questions I've been asking myself is why have we switched from looking at
*  order, equilibrium, perfection, like perfect rationality? Why have we switched from that
*  in general? And I think that certainly with the rise of molecular biology and genomics,
*  proteomics and other aspects of biology, we see much more complex or complicated in this case.
*  We see more complicated structures that may never settle down. Those structures
*  evolve and change and reform depending on what is already there. So they don't settle down
*  necessarily. Even at the molecular level or at a more meta zoological level, they don't settle down.
*  We're starting to see cosmology, I think, much more that way. And also I would say computer science
*  has come in. And since the 1950s, 60s, we're now much more aware that if you take a method
*  and computation, a la Turing, now we call them an algorithm. Your average algorithm doesn't necessarily
*  as a dynamic system, how something works out in a well codified series of rules or steps.
*  That's an algorithm that doesn't necessarily settle down at all. In fact, I like the work of
*  Stephen Wolfram, who shows a very, very simple systems, cellular automata, in general, don't
*  settle into anything you can easily predict. The highly ordered and simple ones are the exceptions.
*  So overall, science is starting to see order and perfection and equilibrium more as fortuitous
*  exceptions. And thank God there is some order. And it's looking to formation and accepting that
*  change is constant. In fact, we don't have to rule it out precisely because we have computation. And
*  we can start to track this sort of thing. Don't have to reduce it to algebra on a few sheets of
*  paper. So science is changing. Economics, I think, is following or will follow the zeitgeist and
*  change itself. So as an observer who is not at all an expert in economics, I'm wondering if we
*  conjured up here, a establishmentarian neoclassical economist, would they agree with this idea that
*  these represent shifts away from the neoclassical paradigm? I mean, I know that at least in the
*  realm of allowing agents to not be perfectly rational, isn't that something where economists
*  have sort of caught on to that already? Yeah, the answer to this, I think, is a bit complicated. But
*  you could have two answers. One is, you know, nothing new here. Move on. The other answer is,
*  yeah, there's a definite shift in the way we're looking at things. So let me speak for both sides.
*  I think in the standard neoclassical economics with these very stringent conditions that are
*  there mostly to allow us to mathematize economics problems and look at them analytically,
*  which is something I would certainly cheer on. That sort of economics, yeah, it's been able to
*  relax one condition here and one condition there, and you're kind of holding on to the rest. So
*  let's assume, for example, that people are not quite perfectly informed, but we're still
*  dealing, however, with probabilities and we'll still allow equilibrium and so on. So economics,
*  I would say, in that regard, yes, has relaxed stringent conditions here and then possibly
*  somewhere else and looked at the strangeness or interesting things that happen. So I'm not saying
*  any of this is completely new. Things I think in science are rarely completely new. But yeah,
*  but I think that's to go back to sort of Thomas Kuhn version of things. Yeah, if you want to hold
*  on to the older way of looking at things, you can hang on to the cliff edge by your fingertips and
*  say, well, you just relaxed two conditions here. It's still neoclassical. I don't know. It's like
*  saying how many conditions do you need to relax before you're doing economics a different way.
*  That's fair. I just wanted to sort of let the audience know that there would be the occasional
*  neoclassical economist who would raise their hackles a little bit. But the point is, who cares?
*  Who cares what the label is? What matters is what we're doing scientifically. I wouldn't set up the
*  question saying what would a neoclassical economist make of this? You could say what I was around
*  in academia in Stanford when molecular biology was coming in big time in the 70s, actually in
*  the 80s. And people were, it was supposed to be revolutionizing this and revolutionizing that. And
*  the people doing molecular biology were very happy with discovering new things. And the
*  more standard folks were really annoyed that funding and so on was going to this new version
*  of the field. What I'd like to see is all types, a wider approach to economics. It doesn't say
*  any different set of assumptions or relaxing an assumption is a travesty and should not be
*  published and should not be allowed. I've got a different way of looking at things than sort
*  of saying what would the old guard make of this? In fact, standard neoclassical economists
*  don't pay much heed to non-standard ideas. That's in my experience. They've had to because
*  there's been a wonderful development in economics where behavioral economics has come along saying,
*  okay, we accept people aren't infinitely smart. What do they do in reality? And that's now accepted.
*  And then we're saying equally that it's not that agents or people in the economy are all alike,
*  there might be multiple firms doing slightly different things. And we can allow them to have
*  well specified strategies that may differ. And so you get something like game theory.
*  And eventually after 40, 50 years, that was accepted in economics. What I find or actually
*  colleague of mine, Rob Axtell has found it takes 40 to 50 years for a new version of economics to
*  come in game theory or behavioral economics, possibly this form of economics, complexity
*  economics. It takes several decades before people get comfortable textbooks have to change and
*  editors have to loosen their thinking a bit. So I think it's a matter of time before this version
*  of economics, which is saying what if you have more realistic conditions that people aren't
*  solving perfectly well defined problems, that there's an awful lot of what economists call
*  fundamental uncertainty, you just don't know how to forecast fundamentally in the L for all problem.
*  What you're trying to do is to explore to cope, to come up with new strategies.
*  And therefore things may always change. So this is that way of thinking is new in economics.
*  It was not that new 200 years ago, people did think in these terms, but they couldn't
*  mathematize it. Yeah. And what has happened, I believe in what's driving this change,
*  you could say it's a bunch of people at the Santa Fe Institute.
*  And what's really driving the change is that in the early 1980s, we all got computers, we got what
*  we then called desktop workstations. Yeah. And that meant that we could set up models, be they in
*  physics or in cellular automata or traffic formation, or indeed in economics, where we
*  could write the rules differently and relax some of these incredibly tight constraints and still
*  track what happens. And when we track what happens, we find things that are much more realistic.
*  So my commentary in all of this is that from my observation of science, the history of science,
*  in particular history of technology and economics, whole fields tend to change
*  when they use different instruments. A classic example is 1610 Galileo
*  develops his own telescope points at Jupiter. Apparently, Jupiter was going retrograde
*  at the moment, astrology and astronomy overlap to some degree. And lo and behold,
*  the better resolution meant that Galileo could see some fixed stars nobody had seen behind Jupiter.
*  And as he looked on the success of nights, he thought he could measure Jupiter's
*  transition against these fixed stars. But amazingly, the stars were not so fixed.
*  Not so fixed. And after about five nights, he sort of says, holy schmolly, I don't know what he would
*  I don't know what he would have said in 1610. Mama mia, whatever. Oh my god.
*  These are moons around Jupiter. So classically, when new instruments, new methods come into
*  science, there's a shift in what can be seen. And so when standard mathematics comes into economics
*  big time in the 1870s and on, you could see things more exactly more rigorously with
*  algebra and calculus just as you could in physical systems. But now we have computation.
*  And computation is extraordinarily important in molecular biology, in
*  genomics, in astronomy, in physics itself, in mathematics increasingly, and now in economics.
*  It's changing what we can see, we can look at more complicated systems, we can relax assumptions.
*  And this is showing us a new world. And it's showing us a different world in a world that's
*  looking far more ecological and far more biological and far more realistic, if you ask me.
*  And any field that's done that, there's a lot of skepticism. You know, Galileo, I wasn't there at
*  the time, but Galileo, I believe, invited luminaries up to the top of his house in evenings to look at
*  the moons of Jupiter. Many of them didn't have decent eyesight, couldn't see it. Young people
*  could see it. Some accepted Galileo was right. But many said, Look, this isn't real astronomy.
*  Real astronomy is seeing something with your own eyes. How do I know that these little specks
*  aren't part of your instrument? And we all get motes in our eyes. So, you know, give me a break.
*  You really haven't discovered anything new here. So I think this is what's happening in economics
*  is a mixture of with these new methods with computation in particular. Wow, look at this,
*  look at that. And on the other side, well, you know, come on.
*  If you're trying to get smarter, you want to read and listen to the best possible sources.
*  But if you're building a company, you want to hire the best possible people. And to do that,
*  Indeed is the source to use. When hiring gets hard, Indeed is the job site that makes it
*  incredibly simple. You can attract, interview and hire all on the website. And you don't just hope
*  your perfect candidates will find you. Indeed's hiring tools will help you cut through the noise
*  to hire faster and smarter. Indeed Instant Match provides a list of quality candidates whose
*  resumes are on Indeed the moment you post a sponsored job. And with Indeed assessments,
*  you choose from 135 skills tests to help make sure you're finding applications from people with the
*  skills you need. So get started right now with a $75 sponsored job credit to upgrade your job post
*  at indeed.com slash mindscape. That's a $75 job credit at indeed.com slash mindscape. Indeed.com
*  slash mindscape offer valid through September 30 terms and conditions apply.
*  Let me let me just dig in a little bit more to this non equilibrium aspect of things. I mean,
*  on the one hand, it wasn't crazy for neoclassical economists to focus on the equilibrium case,
*  just like it wasn't crazy for Maxwell and Boltzmann to focus on equilibrium thermodynamics,
*  right? I mean, there are things that are more or less in equilibrium for a while, but there is in
*  some case in the real world, in some sense, there's a competition of time scales, right?
*  You know, in physical systems, things equilibrate when the microscopic processes are going on much
*  faster than the sort of big macroscopic constraints that fix them. And presumably, an economy has many
*  different time scales, many different layers of organization going on, and they're all sort of
*  talking to each other. And so sometimes that equilibrium assumption or the conditions under
*  which that's a good way of thinking about things break down. I mean, can we say anything in general
*  about when that happens? Has complexity economics taught us something about that?
*  I would say so. I think you're absolutely right, by the way, I'm not saying that complexity economics,
*  the way it's done, applies to everything in the economy. There are many parts of the economy,
*  say oil markets, for example, that reach equilibrium possibly after a day and a half,
*  you know, something happens with OPEC. And then within half a day, markets have equilibrated,
*  and there's a new price formed, and people have adjusted to that. So certainly, in shorter time
*  scales, equilibrium is warranted. And I also think that if you're teaching economics, it's a really
*  wonderful benchmark. There's a lot of deep thinking behind equilibrium and economics.
*  It's people's behaviour is somehow in equilibrium or consistent with the incentives that are posed
*  by the outcome. And I think that's a wonderful insight. And it takes a year or two when you
*  learn economics before that fully gets onto your skin. On the other hand, I think there are
*  there are short term and long term situations that are not subject to equilibrium.
*  I'm trained as an engineer originally and a mathematician, and I wrote a book,
*  in fact, spent many years looking at the evolution of technology. And at first, I might have said,
*  well, new methods come along in steelmaking. Maybe once every decade or two,
*  Bessemer process arrives whenever 1875 or thereabouts, the open hearth process or
*  other processes, Thomas process, these arrive. And in between, you could say there's equilibrium.
*  But when I started to get into it, I realised that new technologies think of computational
*  technologies don't change in bursts. That's what we were trained to think from an equilibrium
*  point of view. They change. If I may use the term fractally, technologies are made out of other
*  technologies that are made out of yet other technologies. And all these are changing all
*  the time. So even the digital technologies or the computer technologies are morphing and changing.
*  The cloud becomes available or really good photonic transmission becomes available in the
*  early 90s. Suddenly we've satellites and fibre optic cable all over the place. And so
*  for technologies themselves, for the structure of the economy, it's changing at all levels all
*  the time. Now, we could sort of freeze frame it and say, OK, you know, let's stop it here.
*  It might be a very old system like whatever fishing for lobsters and lobster pots haven't
*  changed. But in realistic parts of the economy, I'm standing here in Silicon Valley, Xerox Park,
*  and things change here by the month or by the week. And new things come along at all levels,
*  not just at an overall level. It's not just that we got Erbium doped photonic amplifiers in 1987.
*  All sorts of small changes, incremental and almost fractal, used metaphorically,
*  are coming in all the time. So the economy is always changing. And that changes the social
*  structure that when automobiles came along, we got the suburbs. People could drive out of
*  cities easily, daily. Social structures change. History itself changes. What we can do changes.
*  We can now fly across the Pacific or the Atlantic in just a matter of hours. Social arrangements
*  change. Economic possibilities change. And all of that, if you look at equilibrium,
*  has to be either frozen or ruled out of the picture. So the observation I would make on all
*  of that is that economics, equilibrium economics, is wonderful at looking at the logic of markets
*  and incentives and what economists call questions of allocation. How many widgets,
*  how many grand pianos are produced versus how many computer screens are produced?
*  Economics is wonderful at these questions of allocation of time or effort or allocation of
*  budgets. And we've had 150 years of mathematizing that. Questions of where new technologies come
*  from, how they form, how that reforms the economy, how that forms history itself. Once we got textile
*  machinery and steam engines, history in some sense changed. And so those questions can't be
*  and haven't been looked at formally simply because they're not equilibrium questions.
*  And as I understand it, one of the sales pitches for complexity economics is that it gives us a
*  better understanding of bubbles and crashes because these are inherently out of equilibrium
*  phenomena. I mean, what kind of understanding does it give us? Is it not, is it we're able to predict
*  that they will happen or can these methods of reasoning actually help us predict when
*  these dramatic phase transitions occur? I think it's more, and this would also apply in physics,
*  I think it's more of the former. We can predict that certain things will happen. We can't usually
*  predict when they'll happen. To go back to my traffic example, if cars are very dense on a
*  highway and they're moving along, but quite dense then if some small anomaly happens along the way,
*  a dog runs out or somebody spills coffee over themselves, then some car might slow down,
*  that might slow down the ones behind and suddenly there's a slowdown or a jam starts to form.
*  Now, complexity will show us in general that that's possible. You can theorize about it very often
*  with equations. It's not all computation and you can do the statistics on it, but just like
*  anything statistical, you can't predict exactly when it will happen. So it's like you might know
*  a pandemic is possible and likely to happen say in 2015, but you don't know exactly when it will hit
*  and how it will start. Same in economics. Along those lines, this is not really a question,
*  but let me make a comment then you can re-comment on it. The idea that there are fluctuations is a
*  pretty common one. Probably many people have heard, at least they listen to me a lot, that if you have
*  a box of gas and you just wait long enough, eventually all the atoms or the molecules in
*  the gas will fluctuate into one corner of the box or something like that. But in those kinds of
*  situations where there's this huge disparity between the molecular scale and the macroscopic
*  scale, those fluctuations are really, really rare. They're very, very unlikely. We don't need to worry
*  about that happening in the room where we're breathing the air. But in these economic or
*  social situations where you have a multiplicity of scales and something interesting happening at
*  every scale, that's exactly when fluctuations become just inevitable part of your everyday life.
*  Is that a fair way of thinking about it? Yes, I think so. In fact, the research that brought me
*  into thinking about the economy as a complex system is very much looking at systems that had
*  positive feedback. We call them increasing returns in economics as opposed to diminishing returns.
*  Under standard economics, we very often assume diminishing returns. If oil gets too pricey
*  in the world market, then we will use maybe local natural gas or we will switch into
*  hydroelectric over some time and there's a balance reached. But if there's increasing returns or
*  positive feedbacks, say if in 1990 or 2001, there's small firms competing in the
*  search engine business, Alta Vista and a small company called Google and so on. If one of those
*  gets ahead, then other people latch on to that. It's a bit like a language. If there's no reason
*  that English, which was spoken in the 1700s, 1500s should now be a world language. But if
*  something gets ahead, it often pays you to go along with the system that gets ahead.
*  So if something gets ahead by chance, it'll grow and the economy is full of such systems
*  and small events in cases like that. I think in physics, you call those nucleations or something.
*  So these small events get magnified and form new structures. It's certainly true that
*  high technology, advanced technology works that way. If enough people are using, say,
*  PayPal platform to pay off their friends or bills, then somebody else coming along,
*  a friend of mine would want to adopt PayPal versus some other competitor and suddenly
*  PayPal balloons and dominates the market. Economists, before we started to look at
*  such questions formally, economists would say, yeah, there are multiple outcomes, but you know,
*  what can you do? There isn't a solution we can agree on. Now with this new way of looking at
*  things, and I think this would be true in physics, you just say, oh, there's multiple, whatever you
*  call them, metastable states, there's multiple possible outcomes, and those lock in for a while.
*  And then after a while, you go to something else, because some new structure comes along.
*  And so in that sense, there are lots of phenomena that are that make sense in this different form
*  of economics, because we're allowing positive feedbacks, not just negative ones, we're allowing
*  formation. And we can, and we can examine those actually, not necessarily computationally, we can
*  use nonlinear stochastic methods, or stochastic process theory to look at things like that.
*  It makes me wonder about the, you know, one of the very common ideas in complex systems is the idea
*  that there's something happening at all scales, there are power laws in the structure of the
*  system, and so forth. Is this too much of a leap? Or does this have something to say about the almost
*  inevitable nature of inequality in a society? Like, will it be the case that as long as economies
*  are complex, that there will be really, really rich people and really, really poor people because
*  there's structure at all scales? Yeah, again, inequality is a fairly complicated question.
*  There are many answers anyone, any good economist could give you. I would say,
*  here I would go back to looking at positive feedbacks that if one class of people gets ahead,
*  and they rig the system to some degree politically, I'm not saying there's any great conspiracies,
*  but if some class gets ahead, then they can educate their children better, get them off to
*  a better start. And so, it's anomalies and inequalities, and even if you started off with
*  everything equal in some perfect society, come about in the Soviet system changing into what's
*  now Russia in the early 90s, it didn't take very long for a fairly flat and reasonably even
*  distribution, I should say reasonably of wealth and income to turn into what amounted to an
*  oligopoly and very uneven set of distributions. So, I think that there are inevitably positive
*  feedbacks that make it difficult to have reasonable equality all over the place,
*  but that doesn't mean we shouldn't try. Fair enough. Okay, I just had to get that out there
*  because I've been wondering about that myself. But in happier news, let's switch back to this idea that
*  part of the toolkit in complexity economics is that agents are different. They have different
*  information, they have different strategies and so forth, and that's actually a feature in some sense.
*  It allows the economy to evolve in ways that wouldn't be possible if everyone moved in lockstep.
*  And I love the example that you show in one of your papers, which we'll link to in the show notes,
*  of this prisoner's dilemma tournament. The prisoner's dilemma is this famous game theory
*  problem and there's this idea that you have different algorithms for approaching it and they
*  compete against each other. But surprisingly to me, I don't know how long I've made it this far in
*  my life without understanding this, but at least in the example you showed, there wasn't an equilibrium
*  reached. It wasn't that there was a winner and eventually you found it. It's that if you just
*  keep running the tournament, different strategies seem to win at different times.
*  Yes, I love that example. It's actually due to a Swedish physicist called Christian Lindgren
*  working around 1990. So this is not particularly new. He did a lovely piece of work imagining that
*  there was a prisoner's dilemma tournament. You don't need to understand much about
*  prisoner's dilemma. Just think of it as a collection of strategies that may differ. Let's say
*  there's a hundred different strategies possible and they compete against each other one on one
*  repeatedly at random. If a strategy does well, it can replicate, it can reproduce itself. If it
*  continually does badly, there's a kind of trap door and it falls out and isn't seen again.
*  What Lindgren did I think was brilliant. Lovely, lovely work. He not only set up this computerized
*  prisoner's dilemma tournament, but he allowed that strategies, given strategies, say you might be
*  playing tit for tat consistently, strategies could mutate. He had a way of coding so that
*  a strategy could mutate into some neighboring strategy. Then he did something that I thought
*  was profoundly interesting. He said, not only can they mutate, but they can randomly deepen.
*  So normally I'm playing this prisoner's dilemma against similar strategies that are a bit different
*  and I'm looking back, say one move and suddenly I'm faced with a strategy that's deepened.
*  It's mutated. It can look two moves back, two of its own moves and two of my moves and it's playing
*  me a hundred times. So this sort of history is good because you can start to figure out what the
*  other person's strategy is going to be and act accordingly. So what Lindgren had done was to
*  not just have mutation of strategies, but deepening the strategies could notice more
*  and get smarter. Then he sets all this thing up and his computer hits the return button
*  and allows the strategies to interact and play each other. He starts from just four simple
*  strategies that can look back one move and lo and behold tit for tat starts to dominate and
*  some other thing, anti-tit for tat details don't matter, but certain strategies do quite well.
*  What fascinates me about Lindgren's experiment is that you could stop it at any stage and say,
*  oh the solution's been reached. So after maybe 10,000, 20,000 such tournaments with these four
*  strategies, one of them dominates, replicates and you can say, oh that's the solution. This is the
*  best strategy, but then some strategy deepens and it enters randomly and suddenly everything
*  gets complicated. System goes wild, that strategy may or may not take over, but other similar
*  strategies deepen and the whole thing gets far more complicated and goes wild for a while.
*  It's almost like a stock market that hasn't settled this enormous amount of variation
*  and then things settle down again and then at some future period things might deepen again
*  and so on. You're tempted to say that strategies at each time you would stop the whole experiment,
*  which might have taken days on some computer in Sweden, you're tempted to stop and say a solution
*  has been reached, but a solution I believe is never quite reached because you can always deepen
*  further and further and further and get more and more information, more and more smartness.
*  What this tells me, it's a bit like saying technology keeps changing. You might think,
*  well we've got ships that will transport people in the 1940s, 50s across the Atlantic and
*  suddenly the Boeing 707 comes along and the game changes and then many such aircraft come along
*  What fascinated me about Lindgren's experiment was that the strategies, wherever you looked at,
*  formed an ecology. Strategies appeared that were mutually fed off each other. Strategy A supports
*  Strategy K, which also supports Strategy A and that dominates for a while. Strategies that are
*  parasitic appear. They only work if they can exploit some other strategy, but then that might
*  die out so they die out. Strategies, there are times of great volatility where you see an enormous
*  amount of change and times of quiescence where everything looks terribly stable.
*  As I looked at this, he's got a graph of the outcome over a quarter of a million trials or
*  such tournaments, one leading to the next. When I looked at the graph, I thought, oh my God,
*  this reminds me very much of paleobiology. You have so many species of dinosaurs. This one depends
*  on that one. They depend on dinosaurs that maybe are grazing, which depend on something else.
*  There are many food webs and there's mutualism. There's competition. There's periods of enormous
*  change, periods of quiescence. The whole thing looked biological, yet it was coming out of an
*  extremely simple, well-defined system. For me, it was kind of a shocker and a wake-up call.
*  It was done in 1990. It's a very early version of what we now call agent-based model.
*  Agents would be the strategies themselves.
*  We're all trying to get in shape and eat right, and Freshly is here to help. Their delicious
*  meals are designed by nutritionists and cooked by chefs, making it easier to eat better. Freshly
*  offers chef-made, nutrient-packed, delicious meals delivered fresh to your door with no
*  cooking required. We all know that grocery shopping and cooking can be a pain, especially
*  right now. With Freshly, you don't have to. Your meals arrive cooked and fresh every week,
*  so you keep your fridge stocked and skip the trip to the store. Best of all, ordering is easy. You
*  visit Freshly.com and choose from over 30 delicious, satisfying, better-for-you meals,
*  like steak peppercorns, sausage-baked penne, or their chicken pesto bowl. Your meals are
*  always delivered fresh, never frozen, and are ready to eat and enjoy in just three minutes.
*  Right now, Freshly is offering our listeners $40 off your first two orders when you go to
*  Freshly.com slash Mindscape. So stop stressing about dinner. Go to Freshly.com slash Mindscape
*  for $40 off your first two orders. That's Freshly.com slash Mindscape. Get $40 off your first two orders.
*  The parallel with evolution is very, very clear and very, very provocative in some way. And it
*  makes me think back again to this timescale question. Even if there were a single best
*  strategy for the prisoner's dilemma, you can imagine that the space of possible strategies
*  is so large, just like the space of possible genomes for a population of species is so large,
*  that who cares if there is a best one? You'll never find it. What you can do is just spend a long,
*  long, long time getting better and better, depending on what your environment is.
*  Yeah. And if you might be a very, very smart strategy and be faced suddenly,
*  maybe artificially by simple strategies, maybe a meteorite hits the computer or something
*  at the tertiary Cretaceous boundary, something changes and then you'll get a different system,
*  growing up a different system entirely. So I think the biological metaverse is very good.
*  And I would say in that case, simple, very simple setups, which just consist of
*  given strategies at the start and some rules for how they might mutate or change or deepen
*  can give you not just complicated outcomes, but ones that appear biological or zoological.
*  And for me, that is a more organic way to look at the economy. Yeah, there's an architect wrote
*  a book in the 1960s, Robert Venturi, very well known about complexity in architecture. Now,
*  he didn't mean complex systems or scientific. He was looking more at really a reaction to the
*  simplicity of the Bauhaus people, the order that they wanted to bring in a look Corbusier and others.
*  And he was rebelling against that. And he used this term that I like or two phrases to sum it
*  all up. He said, in architecture recently, this isn't a perfect quote, we have been subject to
*  prim dreams of pure order. And I think that that was true. And that came out of a kind of
*  possibly that came out of an enlightenment view of what Newton had really done. He showed that
*  something quite complicated, certainly in the solar system was actually pure order. If you could start
*  with four equations, inverse law of gravity and all and get something where the complications
*  suddenly became ordered. And we began to think in the 1700s that science is like that should be like
*  that. And we got these prim dreams of pure order. What Venturi was on about and I love this, he said,
*  we need to allow for things that are contradictory, things that may even look out of place,
*  things that look more organic and biological, I can't remember the exact words here.
*  And what we want is to allow for messy vitality. And so what we're finding, and certainly this is
*  my point of view, we're finding that the world is a lovely mixture of pure order and things changing,
*  and things changing in a way that might never repeat. And I like the phrase messy vitality for
*  that. So I'm cheering economics on if it's getting out of just purity of pure order and
*  equilibrium and perfection, and entering a time, a phase of looking at the economy as vital,
*  alive, changing, changing its structure all the time, with equilibrium being part of the mix,
*  but not dominating. So this is an economics of what I would call messy vitality.
*  One of the things that I really was struck by in your article that I read was the idea that not
*  only by starting with these agents that we can allow to have different strategies, not only do
*  we learn how the economy gets put together, the collective behavior gets put together,
*  but we learn about how agents reason, right? We try out different things and we realize,
*  oh, that's what they were thinking all along. We never even knew that.
*  Well, there's a lovely move in economics that I mentioned, a little behavioral economics,
*  and it's basically showing, let me back up on that. In the standard way of thinking,
*  if you think that perfect rationality, that all agents are in or facing well defined problems
*  and solving those perfectly rationally optimizing and so on, then any deviation from that appears to
*  be stupidity. Rationality is bounded. They're just not that smart. The way I would see it is otherwise
*  and say that agents in the economy, the players just simply most of the time don't know what their
*  rivals will be doing. They don't know what to do. It's a bit like a year ago, a year and a half ago
*  in March 2020, we had a new thing. We had a pandemic and we didn't know how it would work out,
*  how infectious it was, what strategies, what mutations were possible and so on.
*  In the economy, most of the time, we don't know. There's what economists call fundamental
*  uncertainty. You can't even put decent probabilities on outcomes. You don't know what,
*  this is true in Silicon Valley. You might be entering some space. We're going to dominate
*  the space of driverless convoys of vehicles in Los Angeles or something. There might be 10
*  different companies trying to do that, but you don't know what the technologies are for the others
*  or the resources or the regulations or the insurance procedures and so on. You don't know.
*  This is where standard economics would come to a halt and say, okay, problem isn't well defined.
*  Therefore, optimal behavior is not well defined. Therefore, rationality isn't well defined.
*  In this case, I remember one very prominent economist telling me that he recognized that
*  was very much part of the world and he had a Nobel Prize in economics. He threw up his hands and he
*  says, I get it. He said, I believe the world's like that, but what can you do?
*  It was in Santa Fe that we started to think this was in 1988 when we started this program I was in
*  charge of and the economy is an evolving complex system that we began to think, yeah, people do
*  make moves in ill-defined problems. They try different options. They cook up different
*  beliefs. They explore different strategies. They explore different means of forecasting.
*  What if we allowed them to do this, at least on a computer, what would come out? I must say we were
*  very heavily influenced by the ideas of John Holland, who was one of the pioneers of how do
*  you teach computers to play a decent game of checkers and then chess all the way down now to
*  go and alpha go zero, et cetera. There's a lineage of thinking and basically saying,
*  okay, we can try this, try that and learn what works, but other agents are learning too.
*  So the situation keeps changing and there's no point at which you say you've optimized because
*  the situation will change as other people make new discoveries. Yeah, it seems to me that the
*  lesson from the more recent experimentations with alpha go, alpha zero, et cetera, is just don't try
*  to teach them at all. Let the algorithms learn. They're much better at it than we are at teaching
*  them. Am I correct? Do I remember correctly that somewhere you mentioned that there was a kind of
*  a phase transition as a function of how much experimentation you allowed the algorithms to do?
*  If they were only allowed to do a little bit, they never found a better solution, but if you let all
*  the algorithms experiment a lot, a whole bunch of new things could happen.
*  Yes, and we started to look at financial markets at the problem of asset pricing,
*  what you'd call a theory of the stock market. And we cooked up, there was a neoclassical solution
*  to that and it says if all investors were identical and operated with a single company,
*  single stock, and that stock gave you varying random earnings, what prices would develop to
*  reflect those random earnings? What would the stock be worth stock price? How would it move over
*  time? Looks quite realistic. It's beautiful work done by Robert Lucas in the late 1970s.
*  That became a kind of standard in economics. What we did was to say, well, hang on. This was in Santa
*  Fe. We are going to set up a stock market in the computer. This was in 1988 and the investors will
*  be artificially intelligent computer programs. They will work by testing out forecasts and
*  making bets and figuring out what's working, but they're all doing this and they're all mutually
*  presumably getting smarter, at least more experienced. We'll allow them to do that
*  exploring of new ideas, new strategies, all different, of course, among different players.
*  We'll allow them to do that at a certain rate. So what I would call a twiddle parameter,
*  physicists do this routinely, I notice. We call it lambda. If lambda was low, meaning they didn't
*  explore very often, then you were attracted. The whole system then is like a bunch of stars,
*  all these different strategies start to be attracted towards Robert Lucas's standard outcome.
*  The market settles down and it's almost as if there's a gravitational attraction
*  towards this so-called rational expectations equilibrium, the neoclassical solution.
*  We saw that and the computer output showed that and I was terribly disappointed. I thought
*  something more interesting would happen when we turned the parameter up so they could explore
*  a bit more often and indeed into a realistic mode of exploring because we had data on how humans
*  change their minds and so on. We found that there was phase transition.
*  Suddenly the standard theory, by the way, shows that there can be no such thing as a market
*  psychology. Why? Because all agents are identical. There's actually no trading because the one agent
*  wants to sell. All other agents are the same and they want to sell and there's no buyers so the
*  price adjusts until people are indifferent. There's no technical trading. You can't look at past
*  history and predict in any way. There's no bubbles and crashes. When we turned our knob
*  up a little bit and allowed people to explore more realistically often,
*  suddenly all those phenomena appeared. There was a market psychology,
*  trivially. Technical trading appeared and it wasn't because people were using these strategies to say
*  I'm optimizing. They found that worked in a market where other artificial agents were doing
*  the same thing. We got all these emergent strategies and lo and behold, these are phenomena
*  that real markets show. We were looking for, can we find a problem where our apparatus, our methodology
*  and complex systems comes up with something that's in the real world but standard
*  neoclassical economics can't see. Suddenly our little telescope, it was on a Mac Plus on my desk,
*  was able to show moons of Jupiter that were actually there. I'm exaggerating here but for
*  me it was a breakthrough moment. We were showing actual phenomena that are statistically present
*  in real markets. I remember I'd gone back to Stanford then. I used to call the guy in charge
*  of this in Santa Fe every two or three days and I'd say what's the market doing today? He says,
*  oh, it's highly volatile at the moment. Somebody's discovered new strategy and everybody else has to
*  adjust or nothing's happening. It's quiet. It began to feel like a real market. There's now been a
*  lot of work done on this and I think those findings hold that complexity economics can actually see
*  realistic phenomena, bubbles and crashes, periods of high volatility and periods of
*  quiescence that you see in real markets. For me that was a breakthrough moment. It was remarkable.
*  Okay, I have two more questions and I'm just giving you a warning because they're easy questions to
*  ask but they're very broad so I'm going to let you choose in what detail to answer them.
*  The first one is, is there a worry that this computational approach like you just described
*  where you have this simulation running that somehow if that's the right tool for this question,
*  then we'll never be able to get an understanding at the deeper level that we could get with an
*  explicitly equation analytic based way of thinking about things. We can study different systems on a
*  system by system basis but it's harder to find the general laws. Is that a true worry?
*  I think it's, I wouldn't call it a worry but it's definitely a concern. I don't want to say
*  computation is the answer to everything. A great deal of the early work we did on what's now called
*  complex systems in economics was equation based and I'm very much a trained user of
*  nonlinear stochastic process theory so we did an awful lot of that but definitely computation is
*  here and it's here to stay. What I would say is that when you set up an equation based system,
*  you're basically setting up how individual agents usually behave. You're well defining that.
*  There's many assumptions you're making and you can follow the logic via mathematical deduction
*  from line to line to see how some outcome is formed and the outcome itself you can analyze
*  analytically as well. It's all there in equation form but it seems clear to me that you're not
*  doing anything terribly different when you compute. You usually start off with a lot of equations
*  in the algorithm you set up. You design your algorithm. The equations might differ because
*  each agent maybe differs. There's a lot of exploration and discovery and mutations and
*  finding new things just as there would be in AlphaGo zero. You're not starting your
*  agents off with supposed insights. You're just starting them from zero and watching them get
*  smart. Is this kind of a hodgepodge? Is that just sort of we can compute
*  and then I can twiddle the assumptions and get something different out. I would say
*  maybe in the wrong hands things can go like that but I think if you're doing rigorous honest science,
*  you're tracking your assumptions versus what it shows you and you're doing that rigorously
*  just as you were in Christian Lindgren's setup or on the L for all problem,
*  you're watching how things come out. You have a record, a detailed record step by step
*  of how that came out. You can make arguments. Greg Chaitin does this that computational
*  descriptions are every bit as theoretical as equation based descriptions. That's a side
*  observation. I like it and I've always admired his work. This comes out of algorithmic information
*  theory and that's an aside but what you can do is once you see something, oh my god our agents are
*  getting into little bubbles and crashes. We are seeing periods of high volatility and low
*  volatility. Then you can go back and find deeper explanations, qualitative ones and test those out,
*  isolate the phenomenon in question. So again if you said we have equilibrium of flow traffic
*  and we're not seeing anything but the equilibrium and we can see how the traffic forms
*  so on. Yeah but with a computational system that's open to new behaviors you might see
*  traffic jams forming. Once you see traffic jams forming you can slow that down and ask
*  how that forms. You can refine the models, you can make toy models of that, you can reduce that into
*  simple equations often. You see this I believe again and again in physics where some anomaly
*  appears and then there's a theory. The anomaly might appear experimentally or it might appear
*  computationally or it might be at the level of cosmology or it might be at the level of
*  particle physics but you see something happening in your experiment and computers are performing
*  experiments and then you try to isolate it. You look back through your data, how did that form?
*  Right. So I'm not too worried I think that there's an awful lot of very bad mathematics
*  in every field and there's rigorous and beautiful mathematics. Similarly there could be a lot of bad
*  simulation but there could be beautifully formed and beautifully studied and beautifully analyzed
*  simulation. I'm not against standard mathematics that's nearly all my training. What I'm I think
*  it can sit alongside computation. We used to have geometry in the 1600s that was mathematics and
*  algebra was spurned and scoffed at by Kepler and even by Newton until quite late in his
*  career and now we have then algebra came in and suddenly by 1750s that was kosher and
*  then we began to think that science meant reducing things to mathematics and mathematics was algebra.
*  I would say there's a different form of mathematics could be rigorous,
*  algorithmic mathematics and we can study that as people like Wolfram have done or Greg Chaitin
*  and we can look at the reasons certain anomalies or outcomes are not even anomalies,
*  certain outcomes can occur. It's very much like the controversy and the four color problem
*  that might have been the 70s or early 80s. The four color problem if you recall in
*  mathematics was solved by computation. Standard mathematicians said oh my god
*  this isn't mathematics where's the reasoning and so on. The computational people say well we've
*  settled the problem and it was as if the astronomers in 1610 many of them were saying
*  astronomy means looking closely at the heavens maybe with good instruments but not with these
*  newfangled telescopes. So computer people were saying the computer gives you a new instrument,
*  a new telescope and I'm on the side of not thoughtless computation. I just think we have
*  a new instrument, computation or algorithmic mathematics. We should treat it very carefully,
*  very rigorously and we should know what we're doing and it stands alongside earlier forms of
*  mathematics as valid as ever but it's allowing us to see more deeply, allowing us to see new things.
*  Yeah I mean that sounds perfectly fair and then the last question which is maybe implicit a little
*  bit in things you've already said but the obvious one is what are the policy implications of this
*  way of thinking? I mean do you have a way of summarizing for people who are out there pulling
*  levers on our economy how thinking about complexity is going to help them out?
*  Well if you, yes I would say that what you can think of is something that economists now routinely
*  call policy labs. You can take for example, just excuse me, to give a recent example
*  of we are faced with a pandemic and as recently as maybe three, four months ago we were wondering if
*  different types of vaccines come along, who should they be distributed to and why?
*  So standard economics or standard decision thinking would make that somewhat difficult to solve
*  in a conventional way, not totally difficult, set up equations and so on but what people were
*  able to do was to put questions like that on a computer and if it was done carefully you could
*  get good answers. You're basically setting up what John Holland would have called a flight
*  simulator for the mind. You were saying okay the obvious thing would be to give vaccines to old
*  people and they want, you know if the vaccines are effective they won't die but that was just
*  obvious. A more subtle approach would be to say let's give vaccines to younger people, the ones
*  who are out partying, drinking in bars and so on and that might cut the transmission way down so
*  eventually old people will benefit. Of course you want a combination of both but what we can
*  do for policy is to set up detailed models possibly computationally in an experimental lab
*  and really start to understand the system, vary this, vary that until you get really good intuition,
*  learn what you can from the real world and make your models accurate. I want to add one other
*  thing about policy that fascinated me. If you assume any outcome is at equilibrium
*  that implies that there's no group of people, no agents who can game the system or exploit it to
*  their advantage and why if they could in an equilibrium economics they would already have
*  done that and so the system wouldn't be at equilibrium if someone can come in and make
*  a change or would want to make a change. If we relax this equilibrium assumption we might say
*  something like oh Russia's going to make capital markets free in the years 1990.
*  You could assume it's going to find a conventional equilibrium quickly but we could also
*  make the assumption there might be coteries of players, small groups who exploit the system to
*  their own advantage which is exactly what happened and you can see this again and again so I think
*  with this if you drop the idea of equilibrium then you're open to the view that systems can
*  be exploited or gamed and we're always surprised when that happens under this new way of thinking
*  we shouldn't be surprised. In fact we can possibly anticipate how that might happen.
*  It's a bit like saying the US Navy has a very good code encryption system. It's wonderful and it's
*  not going to be broken and that would be the equilibrium standard. We could also say
*  we have a new encryption system for the US Navy. We're going to invite people to try to break
*  and I think that's a very different outlook and when you assume equilibrium you're basically
*  assuming the system. Nobody can beat the system and that's patently untrue. It's a good lesson.
*  It's a good lesson that I think we're getting over a few of our recent podcast episodes here that
*  we need to complexify our worldview and the way that we think about things and that's true whether
*  we're in policy or just trying to be abstractly thinking about how the world works. So you pushed
*  us in that direction very effectively. Thanks so much Brian Arthur for being on the Mindscape podcast.
*  And I am delighted and thank you as well, Sean.
