---
Date Generated: June 08, 2024
Transcription Model: whisper medium 20231117
Length: 4612s
Video Keywords: []
Video Views: 19075
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2022/05/09/196-judea-pearl-on-cause-and-effect/

To say that event A causes event B is to not only make a claim about our actual world, but about other possible worlds — in worlds where A didn’t happen but everything else was the same, B would not have happened. This leads to an obvious difficulty if we want to infer causes from sets of data — we generally only have data about the actual world. Happily, there are ways around this difficulty, and the study of causal relations is of central importance in modern social science and artificial intelligence research. Judea Pearl has been the leader of the “causal revolution,” and we talk about what that means and what questions remain unanswered.

Judea Pearl received a Ph.D. in electrical engineering from the Polytechnic Institute of Brooklyn. He is currently a professor of computer science and statistics and director of the Cognitive Systems Laboratory at UCLA. He is a founding editor of the Journal of Causal Inference. Among his awards are the Lakatos Award in the philosophy of science, The Allen Newell Award from the Association for Computing Machinery, the Benjamin Franklin Medal, the Rumelhart Prize from the Cognitive Science Society, the ACM Turing Award, and the Grenander Prize from the American Mathematical Society. He is the co-author (with Dana MacKenzie) of The Book of Why: The New Science of Cause and Effect.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel: https://www.youtube.com/c/seancarroll

#podcast #ideas #science #philosophy #culture
---

# Mindscape 196 | Judea Pearl on Cause and Effect
**Mindscape Podcast:** [May 09, 2022](https://www.youtube.com/watch?v=9VsTpsD_dP0)
*  Hello everyone and welcome to the Blindscape Podcast. I'm your host, Sean Carroll. As we go
*  through life, one of the things that we're inevitably going to do all the time is to assign
*  credit or blame for things that happen in the world, either to people or to other events that
*  are happening, right? We have effects, things that happen, and we have the causes for those effects,
*  the reasons why those things happen. This idea of a structure of reality based on causes and effects
*  and their relationships is perfectly obvious, right? I mean, it's something that is completely
*  evident to us ever since we were little kids. The ancients talked about it. Aristotle famously
*  kind of organized a whole categorization of causes and different kinds of causes and their effects.
*  But like many such ideas, when you think about it a little bit more deeply, it becomes tricky. What
*  exactly is going on? If I say I got sick because of a virus, what do I really mean? I mean, there's a
*  simple answer, which is if it weren't for the virus, I wouldn't have gotten sick, right? The
*  virus weren't there. But you try to implement that in some systematic way, and what you find is it's
*  much trickier than that. For example, what if you had gotten the virus, but you were also vaccinated,
*  so therefore you were protected against it? Or what if you didn't get the virus, but you got
*  something else, so you got sick anyway? Furthermore, that kind of reasoning isn't limited to just the
*  virus, right? I mean, Darwin's theory of evolution is responsible for viruses in the first place,
*  in some sense. So did you get sick because of Darwin's theory of evolution? Did you get sick
*  because space-time is four-dimensional, without which maybe there wouldn't be such thing as
*  viruses? It's hard to pin down exactly what's going on. And this difficulty is not just for
*  physicists or philosophers or other kinds of scientists. It's becoming increasingly important
*  in artificial intelligence research, because computers don't have this immediate, obvious
*  feeling that there are causes and effects in the world like human beings do. So we really do need
*  to get at the guts of what's going on when we talk about causes and effects. And modern scientists
*  and philosophers and mathematicians and computer scientists have done this. No one has been more
*  influential than today's guest, Judea Pearl. He's done foundational research on understanding what
*  is meant by causes and effects, and he's written about it. He has a popular book from a few years
*  ago, 2018, with Dana McKenzie called The Book of Why, the New Science of Cause and Effects.
*  You can read about it there, but you can also get it here on this podcast. We're going to talk about
*  exactly this set of questions. Just to give you a little bit of a hint, the idea is we think about
*  probabilities of things happening. And even if there's definite things that happen, even if it's
*  not about randomness, maybe you don't know what's happening, right? So for a statistician, if you say
*  there are people, a set of things called people, and some of those people drink alcohol and some
*  teetotals, some don't drink alcohol. So what that will mean is there's a fraction of the people
*  who drink, and that's saying that the probability that a randomly selected person will drink is a
*  known quantity. So there's a probability involved even if everything is perfectly deterministic.
*  And then also for people, there's a probability that they own a cat or own a dog or have no pets
*  at all, or both or whatever. And then you can ask questions about, well, okay, given that, you drink
*  or you don't drink, what is more likely? Do you own a cat, a dog, or no pet at all? And then you can say,
*  what causes what? Are people who drink more likely to own pets? Or if you own a cat, does that force
*  you to drink? That's the kind of question that this new science of causality is designed to answer.
*  I'm not going to give away all the ways that it happens, but again, crucially important for
*  computer science and artificial intelligence. Also for areas like medicine, you want to know
*  what medical intervention is giving some effect in the patients. For politics or economics,
*  what policy changes lead to what effects? This idea of cause and effect and getting it right
*  pervades how we think about the world. As a physicist, of course, there's a whole other
*  dialogue to have about the fact that in Newton's laws of motion, there are no causes and effects.
*  How do you recover them at the macroscopic level? We get into that a little bit and
*  many more interesting ideas. Let's go. Judea Pearl, welcome to the Mindscape Podcast.
*  Glad to be here.
*  Causality is one of my favorite topics to think about, both as a human being and as an academic
*  researcher. This is going to be a great thrill for me to talk to the world's master. Let's try to get
*  on the table how the typical person out there should think about causality. We're both right
*  now in Los Angeles as we're recording this. We'll hear people say things like, I was late
*  because there was a traffic jam on the 405, attributing to the fact that they're late a
*  cause, namely there's a traffic jam on the 405. I guess the first question is, does that make sense?
*  Are these good ways of thinking? Is that causal language?
*  That's the best way because that's the way people talk. To distinguish my profession or my hobby
*  from yours, I'm interested in capturing the way people think and not the way nature is constructed.
*  This is because I am in the circle of AI people and we have a certain mission. We want to capture
*  how you and I think so that the robot can communicate with that in a natural way,
*  regardless of how the molecules move. I think it's a great fact that AI helps us understand
*  not only the world but how we think because we take so many things for granted and the computers
*  don't. Absolutely and that is a real test. That's why I'm accused many times that I didn't pay
*  attention to the great philosophers, to what Kant said and Hegel and Aristotle.
*  They didn't have the pressure to build a robot that behaved like us and they didn't have a
*  metaphor of thinking. That's important. Explain more what you mean by that, the metaphor of thinking.
*  Well, the cart had a metaphor. We have gears in our mind and they turn and that's what makes us
*  deduce one thing from another. Why? He needed to have a metaphor because he was familiar with gears.
*  He wasn't familiar with neurons. He wasn't familiar with even logic circuits.
*  He had only one metaphor for a deductive machine or at least a machine that has output based on
*  input and that was the gears system that Archimedes maybe invented. So he put it together. Once you
*  have a laboratory or a playground, you have to have a playground for your own ideas. So you can
*  take them apart and try different combinations. Philosophers did not have a playground for ideas
*  about thinking and we have. We have. The computers are forcing us. We have and that is why I don't
*  think I can learn much from philosophers. Good. Perfectly fair. Now I will mention Aristotle once
*  and not because I learn a lot from his theories of causation, but because he did sort of try to
*  divide up different kinds of causes. I think he went too far into things that we don't even
*  call causes, but let me just distinguish between the kind of thing I said, I was late because
*  there's a traffic jam, versus something like why is the sky blue? Well, it's blue because short
*  wavelengths of light scatter off of air preferentially, but that's not an event,
*  right? I mean the traffic jam is an event in space-time. The properties of the air are properties
*  that are more or less permanent. Are those the same kind of cause-effect relationships from your
*  point of view or do you distinguish between those? We distinguish between them. One is called the
*  actual cause and I think philosopher called it the token. Okay. Token versus, I forgot the
*  other one. Type. One is based on variable and the other one is based on event. Right. If I say
*  I was late because of the traffic jam, I'm talking about one specific event
*  in one specific time and one individual, that's me, and one situation. Okay. That's token and this
*  one event caused another one. The contrast to that is variable-based causation. Like I said,
*  careless driving cause accidents, which means it's in the variable driving type,
*  which has many values depending on how you drive and tends to cause a higher risk of accidents.
*  The philosopher used the example of drinking hemlock cause death or Socrates died because he
*  drank this hemlock. That's singular. Singular versus token. Okay. That's how they use it.
*  Right. Okay. We have different names for them and we have different algorithms for identifying
*  each one. Good. Do you think that causality is something that is fundamental in nature
*  or is it something that is helpful to be human beings to describe what's going on in nature?
*  Is it more emergent or is it built in to the fabric of reality?
*  There's nothing. There's no cause and effect in physics, as you know it, because all the
*  equations of physics are symmetrical in time. They are built around algebra. Algebra is tied
*  to a connective called equality and equality is symmetric. If F is equal to MA, then A is equal to
*  F over M. Physics doesn't distinguish between the two. However, as an emergent property,
*  we perceive certain things as directional. We say that the rooster crow does not cause the sunrise,
*  but the other way around, even though it occurs earlier and is highly correlated.
*  I will be forced sometimes to ask questions that I think I know the answer to just because
*  it will help the audience along. Don't be surprised.
*  No, no, no. I like those because it gives me a chance to repeat myself.
*  That's good. We'll both be doing that. Okay.
*  I like this distinction that you're drawing and I just want to emphasize how very profound it is.
*  There was this giant revolution with Newton and Descartes and Galileo in constructing mathematical
*  theories of physics. You're right. The most commonly appearing symbol in a mathematical
*  equation, set of mathematical equations, is the equal sign. There's no arrow on it.
*  In some sense, you're doing something absolutely audacious, or at least going back to a previous
*  time when these audacious things were commonplace, when you're saying, I want to know not just equal
*  signs but arrows. Which is the cause and which is the effect?
*  Yeah, correct. I'm glad that you share with me the astonishment about what Galileo did.
*  He chose algebra and said, nature speaks algebra, which wasn't clear at the time.
*  And it enabled him to do so many things that weren't done before, just 50 years after the
*  invention of algebra by Vieta and others. Okay. I think students today should appreciate this
*  revolution and take analogy now that draw parallel to what civil rights did. Civil rights is a
*  geneticist in 1920 that got sick and tired of working with equations and said, it doesn't
*  represent what I want. I want to have an assignment operator. I put an arrow. He didn't think about
*  assignment, but me and computer science know that there is a difference between assignment
*  and equality. I take the content of register A and assign it to be the content of register B.
*  It's a different operator, which is asymmetric. He was the first to put a symbol for it. The symbol
*  was an arrow and he built these path diagrams, which everybody attacked him for that. But at
*  least he said it represents what he wants. Right. That's why I admire him for having the audacity
*  to put a new symbol for something that he understood is needed.
*  I'm trying to understand. All right. We're done with the questions that I think I know the answers
*  to. Now we're already moving on to questions I don't know the answers to. What is the relationship
*  of this new way of thinking? Which again, it's an old way of thinking, right? Aristotle would have
*  been perfectly happy with these arrows, but we sort of got rid of them and we're bringing them back.
*  What is the relationship between this and the idea of counterfactuals or possible worlds? I mean,
*  a very simple minded guess as to what causes are is that A causes B if, had A not happened,
*  B would not have happened. Already you're talking about a whole different universe where different
*  things happen. Right. That was the glitch of Hume. He used almost this term, had A not happened,
*  B would not have happened. Yeah. What the relation is that we have a calculus of counterfactual.
*  Very simple, which means we take path diagram the way that
*  civil rights put them on and we can define what a counterfactual is for every two variables of
*  events. We can assign truth value to every counterfactual you can think of based on
*  the path diagram. So we have a calculus. Plus we have an understanding of what you need to build
*  those path diagrams. And it's built on one relationship. Listen to. Everything is built
*  on knowledge. You have to combine data with knowledge. So somebody has to build those path
*  diagrams. What do you need to think of when you decide whether to put an arrow or not to put an
*  arrow between A and B? That is the question. What comes to your mind? And the only primitive we need
*  is the primitive of listens to. Okay. The barometer deflection listens to the atmospheric pressure.
*  The rooster listens to the glare in the sky. Okay. That's the only relationship. It's a very
*  primitive one and it's a very natural one because I believe this is the most rudimentary. You cannot
*  ask for more rudimentary and simple relationship for a scientist or for a robot to think about.
*  The barometer example is a very good one. We think that the barometer is telling us the
*  atmospheric pressure. And if all we had was the data, if all we knew was what the pressure was
*  and what the barometer reading was, we're back in Galileo land and there's an equal sign and there's
*  no arrow going either way. And what you're saying is there's something extra that that is missing.
*  It's not just a correlation. There is a clear fact of the matter that the pressure is causing
*  the barometer, not the other way around. And that's all we would like to understand.
*  Yeah. And we only come aware of it when we have to program on a stupid robot.
*  Because the stupid robot, if it looks for the equation, will try to move the barometer
*  and hope to see us to prevent the rain tomorrow. Okay.
*  Right. Good. And let me also just give the audience a visual here because you and I have
*  in mind these diagrams you've already referred to, Sewell Wright's diagrams, and you and your
*  collaborators have built these into a wonderful tool. So these diagrams represent what? Let me
*  let you say what they are. The collection of judgment about who listens to whom.
*  I'll put an arrow between the barometer and the atmospheric pressure if I think the barometer
*  listens to the atmospheric pressure. And I would not put an arrow there if I think that the
*  barometer, between the barometer deflection and the price of beans in China tomorrow.
*  Okay. Even though there could be
*  indirect connection between the two. Good. So we have in mind a bunch of
*  facts or a bunch of things in the world that could take on different values, right? The barometer
*  could have different readings, the pressure could be different. Because of variables.
*  Yeah, variables. Right. Good. But it's a man-made, you know, variable is a man-made entity.
*  And then we put all of these variables in circles and we draw arrows connecting ones where we think
*  that one thing listens to another thing. Okay. And I do have one philosophy question about
*  the counterfactuals. We want to say, you know, if A hadn't happened, then B wouldn't happen.
*  If all, I mean, all the robot knows is the world. All it knows is the data, right? I mean,
*  what gives us the license to talk about what would have happened in a different world where all we
*  have is what did happen in our world? Okay. Assuming that you are willing to make
*  assumptions in the form of who listens to whom. When you feed the robot this collection of
*  assumptions in terms of a path diagram, and that's enough. From now on, the robot can reason
*  counterfactually because all the knowledge about counterfactual is contained in that diagram.
*  So the game is to use things we observe about the world to construct this kind of diagram,
*  telling us what listens to what, and then we can deduce what would happen counterfactually.
*  Absolutely. That's the whole point. Yeah. Good. So this is a parsimonious representation
*  of counterfactuals, of superexponentially large number of counterfactuals. Sure. Sure. Yeah. And
*  that's something, by the way, if you compare it to what philosophers did in about closest world
*  semantics, like David Lewis, right? He had the idea that A is counterfactually related to B.
*  If B is true in all the worlds which are closest to A, something like that, right? So as a
*  philosopher, he didn't care about computer representation or mental representation.
*  How would you ever write down, how does the mind represent all the infinite relationship between
*  who is closer, which world is closer to which world given another world, okay? This is enormously
*  large set. But we computer science cannot deal with superexponential storage. We must,
*  two things, first of all, as psychologists, we must agree that we have to face the problem of
*  representation. If you have a theory and the theory does not allow for parsimonious representation,
*  screw up the theory. It cannot work in our mind, right? And the other consideration is practical.
*  We cannot feed the robot superexponentially large memory.
*  That's a very good point. And I guess as a physicist slash philosopher, I'm guilty of
*  thinking like Lewis sometimes and just letting ourselves imagine arbitrarily complicated
*  different situations. But you're making the point that if what we care about is teaching a robot,
*  our understanding had better be simple in the sense that there's only a tiny number of rules
*  and choices that need to be implemented to say something about what happens next.
*  And something else to enforce it is the fact that we form a consensus. We human beings,
*  society, we do form a consensus about counterfactual. How is that possible? If each of one had a
*  different notion of which world is closest to which, we wouldn't form a consensus.
*  Yeah. And it makes me wonder, okay, so why can we do that? I mean, much like why can we talk a
*  language of causality at all if it's not to be found in physics? And I think that ultimately physics
*  is where our description of the world bottoms out. Are there special features of physics
*  that allow us to talk about these ideas at the higher emergent levels?
*  I'm not sure I understand what the question is. Yes, we have to ask why do we, what is it about
*  the mechanism and the motion of the molecules that makes us believe that the barometer is a
*  result of the atmospheric debate and not the other way around? Now, Simon has said, in Herbert Simon,
*  right, he had some conjectures about it. He said, it's probably consideration of power,
*  okay, energy. The sun doesn't care about the rooster. And because of the enormous difference
*  in mass, in energy involved here. So we rather give the sun the power of influencing the rooster
*  and not the other way around. We have all kinds of time progression is also important, right?
*  So both time and energy and mass gives us the clues about directionality.
*  Good, good. Okay, that is very helpful. But now let's roll up our sleeves a little bit and get
*  into the nitty gritty of how this works. So we have a diagram, we imagine a diagram between all
*  sorts of different variables and what listens to what, but just because B listens to A doesn't
*  necessarily mean that A is the cause of what's happening in B. It's more subtle than that, right?
*  Well, yeah, because B is listening to many other things. Some of them are influenced by A
*  negatively. So yeah, it's a combination of listening, which for which we have algorithm
*  that unpack them and give you answers to questions on three level of the reasoning hierarchy.
*  And that is the organization in which I like to think is the ability to answer questions of a
*  certain type. So sorry, what are the three levels of the reasoning hierarchy? That sounds important.
*  I thought everybody knows by today. Okay. Well, they should all buy your book,
*  but let's assume they haven't yet. Okay, the lowest level is statistics. I hope you don't have
*  many statisticians among your audience because they get so extremely insulted when you put them
*  on the lowest level. I know. Yeah. It's just, you look at one event, then you infer the likelihood
*  another one or cares, we look here or head up here. That's better. Sure. But it's still
*  the association between events. This is correlation. This is statistics. This is by the way,
*  also machine learning. Unfortunately, or at least 99% of machine learning. So this is what we get
*  on the lowest level. For that, we don't even need a diagram. We can do that. Actually, we need it
*  for parsimonious representation of conditional probabilities. We need a diagram too, but it's a
*  purely probabilistic diagram. We call it Bayesian network in my language. So that's the level one.
*  Level two is action. What if I do that? And the reason it's totally different than the first one,
*  because you're talking about changing the probability space. You're talking about the
*  new environment. Things have changed in the world. Okay. I don't wait for the sprinkler to be turned
*  on. I apply my muscle and make sure that the sprinkler is on. Looking at the sprinkler,
*  it says the sprinkler is on. I can infer it must be summer. But if I turn the sprinkler on,
*  I can no longer infer it must be summer. Okay. So that is a simple example of why it changes the
*  world. So the world of intervention, this is something that we can learn from randomized
*  experiments. And that was the greatness of Fisher, Ronald Fisher, to introduce
*  randomized experiment into statistics. Statistics before Fisher was all about correlation.
*  And that changed the practice of statistics, not the philosophy, because Fisher refused to talk
*  counterfactuals. So he couldn't prove that his randomized experiment give you what you really
*  want. What the farmer really wanted in his station in the agricultural environment there in England
*  was to know whether to plant use fertilizer A or fertilizer B and what will be the yield
*  if I do one or the other. The father did not care about randomization.
*  But Fisher convinced the community that if you randomize, you get rid of all the other factors.
*  Okay. And what you have is an answer to the farmer. He couldn't prove it. Neiman could prove it.
*  Neiman at the time, but Fisher locked horns with Neiman and he refused to use his notation. So
*  without the language of mathematics, he was able to convince the community that randomized
*  experiments give you answers to your question, which fertilizer should they use? Good. Now we
*  are going to a third level and this is counterfactual or understanding or explanation,
*  unit level, retrospection and imagination. It's the highest level of reasoning that I can think of.
*  Perhaps I'm missing fourth level. But this is what we mean by explanation. Why things happen
*  the way? Was it the aspirin that removed my headache or other factors? As you mentioned,
*  it's event-based. It has to do with individually. In a particular situation, one event happened
*  and another one happened was the first one, the cause of the other one. And that is not even in,
*  you cannot answer that in a randomized experiment. Right. So I guess the understanding,
*  I'm getting confused between the second level of action and the third level of counterfactuals.
*  Why aren't counterfactuals in the second level? I mean, the action is if we did this,
*  what would happen? Yeah. In the future, right. There's no contradiction. Good. There's no
*  contradiction about me going to take an aspirin now. I want to know if my headache will go away.
*  Okay. But if I say I did take the aspirin, my headache did go away. What if I didn't? Now I have
*  a contradiction between what was actually observed, event that occurred and one that I hypothesized.
*  What if I didn't take aspirin? Good. So now I do understand. So the second level is moving forward
*  in time. If I do this, what will happen next? Whereas the third level lets us go, had I not
*  done something, how would things be different? It's undoing events that took place. Good. Okay.
*  Let's look at one of the classic examples, which is always used in these discussions, which is,
*  does smoking cause cancer? Right. This was, we know the answer, but back in the 60s,
*  there was a debate and one of the ideas was that there were, there might be something else, some
*  genetic effect or something like that that could cause cancer. And the question is, how can you tell?
*  And the answer is you can't. Unless you make some, no, you can't unless you make experiment.
*  Sure. You could, but it's unethical and probably practically impossible to force a guy to smoke
*  two packs a day, even though he's not inclined to do that.
*  Okay.
*  Probably bad. Yeah.
*  Yeah. So it's hard to do, although conceptually it's doable, but it's hard. I cannot answer the
*  question without randomized experiment, but at least we have one technique to answer it.
*  I randomized experiment. Yeah. Yeah. You said, okay, good. At the time,
*  given that we cannot run the randomized experiment, the answer it developed into a fierce
*  discussion or controversy, an argument between the pro tobacco and anti-tobacco, the camps.
*  And Fisher was a heavy smoker. He argued for, he argued that you cannot rule out the possibility
*  that there is a genetic factor that makes people crave for nicotine and puts you into a cancer
*  risk. And indeed we cannot rule it out except we can bring to bear some knowledge about plausibility
*  in the world. And the way it was resolved by thinking how strong should that
*  um, tobacco gene be in order to account for the observation, it turned out it had to be quite
*  strong. It had to have a strength that the, um, the presence or non-presence of that gene would
*  make you eight times more likely to smoke than not smoke. Okay. And that was just implausible
*  on the basis of what? Yeah. The whole legal battle there was resolved by appealing to plausibility.
*  Wow. Okay. Yeah. But let's, let's put aside, uh, ethics and human beings and what we're allowed
*  to do and things like that. And just wonder intellectually about this question, because
*  it's just a paradigm for other kinds of questions. I mean, the two possibilities are smoking causes
*  cancer or some genetic factor causes both smoking and cancer. And if I understand the move, uh,
*  that you and your collaborators want to make, it's to say the difference is that if we force you to
*  smoke, you will probably get cancer and therefore it doesn't matter. The difference is shown in the
*  model very nicely. You have a model and the difference will be in predicting the effect
*  of action. If I force you to smoke, I can predict the likelihood of cancer. If I force you to evade
*  smoking, to refrain from smoking, then I can predict the likelihood of cancer under that
*  circumstances. Okay. So it's a, um, uh, however, there's another element here. If you believe in,
*  if you bring to bear knowledge in the form of a diagram, then I can do more than that. And I can
*  say, perhaps you should adjust for, um, gender or just for family history or just for, um,
*  addiction in the family. Okay. To prevent that kind of thing. And so the diagram also tells you
*  what factors you must adjust for in order to get an answer without experiment. So now we are talking
*  about replacing the experiments, which many times cannot be done by a piece of knowledge.
*  The diagram, a diagram contains a piece of knowledge, which is the collection of who listens
*  to whom. Okay. And, uh, it tells you now what factors it should adjust for if you want to get
*  the answer. Replacing the randomized experiment. Good. And at the level of this new calculus that
*  you want to talk about rather than just equal signs, we have arrows now. Um, you, you invented
*  an operation in this world of diagrams called the do operator that sort of implements this idea.
*  So tell us what a do operator is as a D O as in I'm going to do it.
*  It is very simple. The operator that simulate on the diagram, what an action will be in the
*  real world. For instance, if I want to say, I turn the sprinkler on, but you can simulate on the
*  diagram. Previous right now, the sprinkler is enslaved to the climate, to the season,
*  because I connected it to automatic, uh, controller. If I do with sprinkler on, I
*  subject the sprinkler to a new master. That's my muscle. And I dislodge it from the influence
*  of all previous influences. I can also, I can do it on a diagram. I remove the arrows from
*  its previous masters and I subject it to the new master, which is my muscle on a diagram.
*  And I set the value of the sprinkler to on a bullion one being, I have a new diagram.
*  I can solve it. And that the do operator is simple simulation of action.
*  I remember when, uh, Simon de Deo, I don't know if you know Simon, but he was a previous guest
*  on the podcast and, uh, he mentioned in conversation that something that he wanted to do was like, uh,
*  an implementation of Judea Pearl's do operator. And I had never heard of this concept before,
*  but instantly I was, I, I had the impression this was something very, very, very important.
*  So I ran out and learned about it. And it's clear that this is going to be crucial to how we're
*  thinking about, uh, artificial intelligence and, and complicated science questions going forward.
*  I'm very happy with the operator. Yeah. But it's so simple. It's so simple. That's good. That's not
*  bad. Only statisticians get irritated by the do operator. You know why? Because they realize
*  that they should have invented it 500 years before Pearl and they didn't. Well, it's simple
*  in implementation, but there is some, there's something subtle here. Let me just sort of
*  say it in my own words to see if I'm right. Uh, you know, another example is exactly the same
*  structure as, as what you've been saying, but my favorite example is windshield wipers on cars being
*  on and people having their umbrellas up, right? In the data, whenever people have their umbrellas up,
*  the windshield wipers are going on cars and when they're not, they're not. Uh, and so there's a
*  correlation there in the data and this is why you say the statisticians, you know, this is what
*  they do. They go, look, there's a correlation, but what you're saying is you can implement in your
*  diagram, do umbrella. So walk outside on a sunny day and put up your umbrella and see if all the
*  windshield wipers start moving on cars and they don't. And that's the sort of physical implementation
*  of what, of what you can do in a Bayesian diagram. But this will not convince a statistician.
*  I'll tell you why. Because the dual operator doesn't exist in probability theory. Okay.
*  Yeah. Okay. So it's not an operator and probably where does, where does it exist on the diagram
*  and where does the diagram come from? It's a piece of knowledge that is brought to where outside the
*  data. Exactly. No, I think that's what statisticians resist. We don't want any opinion.
*  Well, that was a, that was the manifesto of the
*  Royal Statistical Society in 1833. Okay. We are not going to publish anything which has to do with
*  opinion. Data, data and only data. Right. Yes. But it's not a matter of opinion. I mean, so I think
*  I'm totally on your side here. But it is not in the data either. Right. It's, it's counterfactual
*  data. It's the question if I walk outside and put on my umbrella, what would happen? And so you need
*  to go, like you say, beyond the data, but you can by doing experiments. Right. That's one way is by
*  doing experiment. But as far as the windshield wipers, yes, you can do it by experiment. Right.
*  It's a better example than smoking for that reason. We don't have to hurt anybody
*  by making them smoke. Yeah. So the station will be happy with it. Do experiment. And how,
*  explain a little bit how this helps us tackle classic conundrums of causality, like
*  the firing squad, right? You know, when you have a firing squad where there's 10 people shooting
*  at a death penalty victim, and one bullet hits first, and you say that causes the person to die.
*  But if your definition of cause was had that not happened, the effect wouldn't have happened.
*  That's wrong, because the next bullet would have would have come and hit them. Right. So
*  how does this help us understand cases like that? That is a difference between
*  necessary cause and sufficient cause. So we can compute how sufficient was rifleman, rifleman A
*  bullet as opposed to rifleman 12 bullet. And that's why we put the squad there. So no one
*  could be blamed as an individual. Blame is a necessary cause. We are saying if it wasn't for
*  your bullet, the guy would be alive. So the responsibility is divided here equally, not even
*  equally. I think if you compute it, including all kinds of noises, for instance, you're kind of
*  happy trigger guys, and things like that, the probability will be minimal for each rifleman
*  as a responsible necessary cause for that, for the death. But at least we have a calculus to
*  compute it. That's right. The degree to which your bullet was a necessary cause for the death.
*  And vice now we can also talk about sufficient cause and compute that and the combination of
*  two plays a role in responsibility. It's still not part of standard court procedure to compute
*  the necessary not yet not yet. But I think when we are advancing now with causal AI,
*  I think the legal profession will listen to us. Because they are dealing with now with very
*  critical issue of fairness to what the what degree the algorithm was unfair to gender to women,
*  or to minority groups in the request for loans and so forth. Okay, so the idea of responsibility
*  and sufficient and necessary cause play a very critical role. They will have to listen
*  to those philosophical definitions. I call it computer science definition.
*  Yes, and listen to them and implement them in some procedure they already did because
*  according to the court of law, the but for is is a standard criterion. You don't pay compensation
*  unless unless you apply the but for criteria. This is the the victim would be alive but for
*  the actions of the defendant. And is that sorry, is that compatible with your definition of causality
*  or do you think? Okay, but for is no but for has no meaning in the colloquial conversations among
*  lawyers. Unless you put it in a firm scientific basis. Okay, good. And the algorithm is is a
*  definition of but for it's a necessary cause, a degree to which the action of the defendant
*  is necessary for the death of the victim. And it has to be greater than 50% according to the
*  court of law before the guy is declared guilty or before he's forced to pay compensation.
*  Okay, so let me just try to summarize because I think that we didn't quite
*  end up with the definition of causality yet and maybe there isn't one but I think it
*  No, no, no, I like it because I like the fact that we didn't conclude that because it has different
*  shades for you have direct cause indirect cause necessary cause sufficient cause necessary and
*  sufficient where they come in all kinds you want to quantify all those. So I'm glad we didn't come
*  up with a single one. Well, it's not a single one. But there is an insight which I think is crucial
*  and you've said it but I just want to say it again because you know, sometimes we say lots of things
*  and it's hard to take away the message that at least I have this idea that you know, you have this
*  Bayesian network this graph of all the probabilities of all these things that can happen and then all
*  these arrows from one thing to another if if one thing listens to it, I like that formulation.
*  And then there's this extra statement that you need to go a little bit beyond the data you have
*  to say if I put a do on one of the variables and just force it to do something without propagating
*  backward in the graph right without saying why it's doing that I'm just forcing it to do it I'm
*  going outside and putting up my umbrella turning on my sprinkler if doing that causes if that leads
*  to some effect down the chain then that action is a cause of those effects. Yes. Correct. Yeah. Good.
*  And and one of the and again you said this again but I just want to sort of rub it in because it
*  is so profound for the purposes of learning and robots and AI. It's a lesson that the data
*  or a comprehensive set of data might not be enough. You have to go play. You have to do
*  some experiments to really learn why things are happening. And that's why you find toddler
*  and babies are constantly playing around in the crib and they are not pacified and they are
*  restless until they get the state of understanding why this toy makes noise and this toy doesn't
*  make noise. Okay. And that is why this restlessness is the craving for establishing the diagram.
*  So babies in the crib they're doing. I'm serious about it. Yeah. Baby in the crib
*  are thriving to construct a causal diagram for the crib world. I like that. I'm just going to sit in
*  silence and contemplate that because they don't know it but that's what they're doing just like
*  Euclid didn't know. No, no, no. I'm sorry. They are born with a craving. Okay. Okay.
*  That is I'm serious about it which means it explains why babies remain restless
*  regardless if you reward them for the right action or not. They are reward neutral and they
*  have this curiosity to find out how things work regardless of the payoff as opposed to monkeys and
*  other animals which are driven by reward and not by curiosity. Okay. So this raises a whole bunch
*  of questions about at what point in evolution did we become motivated to just learn the causal
*  network rather than just get rewards? Yeah. I leave it to anthropology and I leave it but I
*  pose to them the question in more concrete terms. At what point in evolution did this transition occur
*  or what kind of computational facilities we must acquire to enable us to do that kind of things?
*  I believe it was the invention of the counterfactual and if you read the first chapter of
*  the book of why is the Harari hypothesis that the artist was able to take to construct things that
*  have no physical reality. It could not happen in the physical reality like the lion man,
*  the head of a person with a body, sorry, the body of a person with the head of a lion.
*  Put them together. This ability to construct things which do not exist in reality but exist
*  in one's imagination that was the key cognitive transition or cognitive evolution that enables the
*  homo sapiens to dominate the planet. So I will mention something that maybe you have not heard
*  much earlier in evolution but it wouldn't be doing what you say. It's the first step toward
*  doing what you say. Malcolm MacIver who's a neuroscientist at Northwestern was a previous
*  guest on the show and he studies fish climbing onto land for the first time. Okay. And he makes
*  the claim that if you're underwater you're swimming along at meters per second but you can only see
*  meters in front of you and all of the evolutionary optimization is to react instantly to whatever you
*  see. But when you're on land now you can see forever. Now you can see to the horizon and
*  there's a new modality that opens up namely seeing something far away and contemplating different
*  hypothetical responses to it. You have time to do that and he makes predictions on the basis of this
*  theory about the development of brains and bones and sensory organs in the fish that they climb on.
*  I get it. I don't know if it's true or not. I don't have the qualifications but in some sense
*  that'll be the birth of imagination. But it's only imagination like within the template of what you
*  already know is possible. But you could see how evolution would in the long term develop that up
*  into something much more creative. Yeah I can see that. I haven't heard about this experiment.
*  Interesting. I'm surprised that fish can see outside the water on land. Well in fact as soon as they
*  start peeking up onto land their eyes move. They evolve so their eyes like you know become frog
*  like right and you know peek up above their head instead of being on the side so they can see better.
*  Interesting. It is. It is. Okay good. So babies constructing Bayesian networks. But again I want
*  to I want to sort of re-ask a question that came in at the very beginning but now we're more
*  sophisticated so we can ask it again. When we're drawing these arrows we do it on the basis of data
*  even though it's supposed to be something that says more than the data are telling us ideally.
*  All we have is the data that we have to construct them. How objective is that? How can we write down
*  a methodology for saying here's a bunch of data therefore here are the arrows you should draw?
*  Or is that completely coming in from our judgment or something like that?
*  The easy answer completely comes from our judgment. However our judgment has also evolved.
*  And general contains condensation, compilation of ideas, tradition,
*  knowledge that came to us by social evolution as well as by biological evolution.
*  So our judgment is also based on stream of data that took billions of years
*  to evolve or to impact us. So indeed the controversy in data science is whether we should
*  build an Einstein from an amoeba by simulating the stream of data that our ancestor had from the time
*  there were amoebas until they became Einstein. Which essentially what data science is today,
*  let's learn everything from data because that's all we have. Or the alternative is we are already
*  ahead. Our ancestors worked for us and have compiled a bunch of knowledge that we call
*  plausible, plausibility. Who listens to whom? We have already compiled and we know that the
*  sun does not listen to the rooster. Let's use it. Both sides have arguments on their sides
*  because after all everything we know originally came from sense data. But the question is can we
*  afford to wait zillions of years to replicate it? Will we ever replicate it the way we evolved?
*  Because the knowledge that we have is subject to incidents such as meteor rains and
*  something we cannot duplicate. Anyhow that's a philosophical question
*  and I'm for using compiled knowledge that we already have. Also the argument is like that.
*  Suppose you are successful in discovering the causal graph from pure data. By the way there is
*  a bunch of activity called causal discovery which is based also on the idea of what should the graph
*  look like in order to be compatible with the data. Let's rule out all the incompatible. I'm leaving
*  it on the side now. It's quite a picked up momentum in the past few years. But aside from
*  even if you are successful to learn the causal graph from data you have to learn it, how to use
*  it. That's why it's important to keep it in mind to know how to use it and to remember that you have
*  to communicate with the human being, the end user, who is enslaved to this structure. So you have to
*  be compatible with the way the human being has structured his or her causal graph in order to
*  build trust between the computer and the user. No I like that because I think that in a lot of
*  philosophy of science for example people pretend that we should aspire to be some objective
*  receiver of data and develop hypotheses. But in fact we carry around with us models of the world
*  from the start. The manifest image or whatever you want to call it. I think we under emphasize
*  the importance of that built-in starting point in reasoning. Absolutely. As I say in one of my
*  chapter the physicists write equations but they talk cause effect in the cafeteria.
*  Very true. Speaking of which I do want to talk about physics a little bit because
*  here's how I say it sometimes. The question that you and your friends are trying to ask is
*  does smoking cause cancer or is there some other variable that causes both smoking and cancer?
*  You're not trying to answer the question does cancer cause smoking. You've decided ahead of
*  time that cancer doesn't cause smoking because like you said it's heavier or whatever. We know
*  from the structure of the world that it's plausible that cancer listens to smoking and it's
*  implausible the other way around. I want to derive that though on the basis of the laws of physics
*  and in particular like you said that might be too ambitious as a general rule but I do want to
*  derive the fact that the causes come before the effects in time. I want to derive the fact that
*  the arrows have to point toward the future. Are you optimistic that that is something that can be
*  derived on the basis of our physical understanding of the world or do you think it's going to have to
*  be taken for granted? You want to derive the time directionality from causes. Today normally we
*  think about that causes must be constrained by the flow of time, by temporal precedence.
*  No sorry I think I misspoke. I want to derive the fact that causes precede effects from the arrow of
*  time but by the arrow of time I mean the increase of entropy since the big bang to today. That is
*  the definition of time? That's the arrow of time. The arrow of time is an increase of entropy?
*  Yes that's right. I cannot help you. Okay good. I don't know but it's a nice challenge.
*  I can maybe if you convince me it's worth doing I'll be happy to immerse myself in that question.
*  I need to write a paper here. I'm halfway done. Yeah but I'm not there. Good. I mean I know that
*  temporal precedence constrains the direction of cause and effect but it's not sufficient.
*  It's not sufficient. Right. Well as we saw for instance in the in the Rostov flow that it comes
*  before the sunrise but still we say it's not the cause. That's right. That's right. No that I
*  completely agree with. I'll just add one more claim that you can think about whether or not
*  you think it's relevant or not which is the following. That if I know the state of the world
*  macroscopically right now. So what I mean by that is I don't know where every atom is etc. But I know
*  where the people are where the planets are. I can use or even better if I have a probability
*  distribution over the macroscopic state of the world. I claim that from that plus the laws of
*  physics I can predict the probability distribution in the future. I can just use the laws of physics
*  to move forward in time. But from that and the laws of physics I can't retrodict the paths
*  all by themselves. I need an extra assumption which is the low entropy boundary condition
*  near the big bang. And I think that's what's going to break the symmetry between going forward and
*  going backward. That ability to predict the correct probability distribution of the world
*  just based on current macroscopic probability data.
*  Okay why do we go to microscopic where we cannot think to will.
*  Talking about molecules and there are already zillions of them. Let's talk about something
*  which is simpler. Let's talk about the billiard table. And you have this nice triangle
*  of the balls sitting there. And what you call this leading ball that bounces.
*  What's the name? The cue ball. The cue ball comes. It hits the triangle.
*  Everybody disperse and hits the walls of the table. Now we run it backward.
*  Take a movie. We run it backward. Can you tell with the bare eye whether you run the movie
*  forward or backward? Yes. By what? You see there's no entropy here. Well that is the
*  initial. F is equal to ma for every billiard ball. True but you chose to begin with a low
*  entropy configuration in the triangle. Yeah. Why is the triangle lower entropy than the state of
*  the balls a second later where each one of them bounces? Why is it low entropy? Well you have.
*  I don't think it's. It is. It's just coarse graining. No it's just the fact that you have a name
*  for the nicely arranged balls when they are in triangle and you don't have a name for the state
*  a minute later. Just a matter of a name. No I think it's actually. Which is subjective.
*  I think there is something objective about the measure on the space of ways to be in the triangle
*  versus scattered around the. Just because it's simpler. Yeah. But if I remember my thermodynamic
*  correctly it is not a progression from an ordered state to a disorder but the natural escape from
*  a real narrow region in phase space to a wider region. Exactly yes that's right. Okay okay.
*  So it's the order is a subjective perception. We have a name to the triangle. We don't have a name
*  for the state to this state of the balls a minute later. We don't have it. It's just
*  we have to keep on saying ball number one is it has momentum 23 and so on. It doesn't have a single
*  name. So we are biased by our language. I don't think it is just our language. I think that it's
*  there is something about how we observe the system that lets us coarse grain in some ways
*  and not others. When we say all the cream is separated from all the coffee in a cup of coffee
*  is low entropy versus when they're all mixed together it's high entropy. That's because we
*  can see the difference pretty immediately. You see we are biased immediately yes.
*  Okay anyway this is my responsibility to work further on this. I just wondered if you
*  had any strong opinions about it from the start. But I want to get back to the this idea that human
*  beings have this baked in manifest image because this is really where it becomes important for the
*  AI right. I mean the robots don't have any pre-existing image of the world. I just had
*  Gary Marcus on the podcast. He was the one who connected us here and Gary has been very strongly
*  arguing that there is a roadblock to deep learning being too successful if it just does correlations
*  between different things in the world. You need some structure. You need some common sense.
*  I'm betting that you agree and causality is going to be part of that common sense. But how do we do
*  it? How do we actually teach the robot how the arrows go between all the parts of our little network?
*  Okay let me first answer. I agree. Not only I agree but I have to supplement it by saying
*  that it is not an opinion. It's a theorem. It's a theorem that here is a limit. There are certain
*  tasks you cannot do if you don't have this set of assumptions. Okay so it is mathematical constraints
*  on the ability of robots to do certain tasks. Okay now we go to how do we get this
*  model of the world into the robot. If you have the time you can just
*  feed it with a diagram plus equip it with the techniques to enrich the diagram. Enrich the
*  diagram by thinking conjecturally what experiments do I have to conduct in the future
*  in order to answer a certain question. What additional variables I wish I could purchase
*  so that I can observe them and enrich the diagram. So this is what we mean by automatic
*  scientist. A scientist that can design the next experiment because it answers a question which
*  currently cannot be answered on the basis of the existing diagram. So the diagram must be
*  vulnerable to number one refutation from the data and number two to enrichment. So that is a blue
*  sky idea of automated scientists which I could elaborate on but it's all built on the force of
*  curiosity. We strive to obtain a state of deep understanding and deep understanding is having
*  the ability to answer questions in all three levels of the hierarchy that gives us a sense of
*  being in control and having an understanding of a domain of crossing the street of playing games
*  and so on. I don't have any fish in this pan or whatever the metaphor is here, dogs in this fight,
*  but I'm betting that the reaction to that philosophy from a lot of people who are working
*  in contemporary deep learning is no that's not what we do. We just let the computer learn
*  everything it can, do all the thought experiments it can do, collect all the data it can and the
*  computer will figure out what the patterns are. For that we have a theorem saying impossible.
*  Is that someone's name attached to that theorem or whose theorem is that?
*  That's the causal hierarchy. It's a ladder of causation. You cannot go from level i to level
*  i plus one unless you have information or assumptions on level i plus one or higher.
*  Okay good, but I do get the impression and again correct me if I'm wrong that this perspective is
*  sort of a plucky minority in the field. It has not swept the consensus view.
*  It has not swept the machine learning people or the deep learning people.
*  It's the same way that it took 20 years to sweep the
*  statistical society until they accepted the operator.
*  But okay. Even that is still resistant. I still have an island of resistance there.
*  You'll win. I think you'll win that one. I can safely predict.
*  I know I'm gonna win.
*  But okay, I mean even if we're on board, even if we're on the train, it does sound hard.
*  It's really unfair for me to fight against this huge industry called machine learning.
*  Because I know that I have mathematicians on my side and they don't have this certainty.
*  So I think it's unfair. I'm gonna win.
*  You're gonna win. That's okay. It's okay to know you're gonna win ahead of time.
*  There are worse positions to be in. But even if you're going to win, it still leaves us with
*  hard problems about what to tell the computer. I mean, what is the diagram? What are the causal
*  relationships that matter? Or even what's the stuff out there in the universe? Do you tell it
*  that there are tables and chairs and people and cars rather than letting it learn that?
*  How advanced is that program of sort of formalizing
*  our common sense intuition about the causal structure of the world?
*  I have neglected to talk about object-property relationship. I've been very narrowed in what
*  I'm doing. I'm narrow-minded. So I only dealt with cause-effect relationship. I've neglected
*  many other things which come into bear in natural language, in vision, interpretation, and so on.
*  But I think what we have learned in the causal corner can be a role model for other areas.
*  We are now working with propositional calculus. We have to go to expand into predicate calculus,
*  all kinds of things that need to be done. And it will be done eventually. We have to teach the
*  robots about objects and properties relationship, chairs and tables and their functions.
*  I haven't done anything in this area except what we do.
*  I mean, when you say that, just to be clear, because I think that some people might hear you
*  say we need to teach the robot about object-property relations, and they'll say, well, sure. But the
*  important part of that phrase is we need to teach as opposed to let it figure it out.
*  We can't wait for it to figure it out.
*  Some things we need to teach others, we can let the robot figure it out. At least in my corner,
*  I have a theorem which tells us what you must teach and what you can let the robot figure out
*  by itself. I don't have those theorems applied to natural language and vision.
*  Okay. And then I guess the final thing I just wanted to touch on, which you've already brought
*  up, but is very exciting but also confusing to me, is the whole set of applications to
*  the social sciences and even to law or moral philosophy. I mean, when we talk about right and
*  wrong, blame and responsibility, punishment and reward, we're always assuming some causal
*  structure. You are responsible for this happening. Do you expect that more sophisticated, nuanced idea
*  of how cause and effect structures work is going to have an effect downstream on how we think about
*  these puzzles? Yes, I have some expectations, some excitements. I can see how we can build
*  social intelligence on top of environment intelligence. So far, I was talking about
*  a robot learning about managing a domain or understanding a domain, a disease domain, and so on.
*  But now we can build on top of that the idea that robots can have a model of another robot
*  or of itself. If it has a blueprint of its own software, then it can reason about
*  what made me do what I did. And then you can program compassion of that and say,
*  I understand why you did what you did, because you're like me. If I were in your situation,
*  I would do the same thing. But are you aware of this and this? So all this relationship, awareness,
*  compassion, I understand you, trust me, all this relationship involves a robot having a model of
*  another robot. And once we have it, we're going to have a nice conversation with our apprentice
*  robot. Are you optimistic that artificial intelligence will reach human levels of
*  intelligence at some point? I'm absolutely sure. How can one be absolutely sure on the basis of
*  conjecture? Only on the basis that I don't see any impediments. But is it a sooner rather than
*  later kind of question? Is this something we need to contemplate? I refuse to answer that.
*  I don't have any imagination that other people have. Okay. I'm with you. That's the problem.
*  I don't have it.
*  So you say that, but what you really mean is you have too much imagination,
*  because you can imagine many different possible things. It's hard to tell which is going to be
*  true, right? Correct. Yeah, correct. And then, okay, I'll just close with sort of a statement
*  that you can reflect on if you want. But as we were having this conversation, I realized the
*  following weird thing. I write books. I write books for sort of broad audiences on physics and
*  other things. And over and over again, in all of my books, I always start with the following idea,
*  whether or not I like it or not. It helps to start with the idea that there was Aristotle,
*  who imputed natures and goals to objects in the world, right? Fire wants to rise up,
*  rocks want to fall down. It was a teleological view. And causes and effects were front and
*  center. He had this taxonomy of cause effect relationships. And I say, we got rid of all that.
*  Galileo and Newton came along and we replaced this. This happens because of that language
*  with a language of patterns, right? The equal sign in your mathematical representation.
*  And that's been very helpful. All of modern physics is this sort of,
*  it doesn't have any direction of time. There's no direction of causality. It's just,
*  this is happening and this is happening and this is happening. But of course, like you say,
*  in the cafeteria, all we physicists talk about causes and effects all the time. And so it is
*  crucially important to me to recover, to understand how to recover our ordinary, everyday understanding
*  of causality and goals and teleology in a way that is compatible with that underlying
*  view of fundamental physics. And so I guess all I'm saying is I'm glad to see you're doing it.
*  I'm not sure that I'm capable of undertaking this major monumental goal that you mentioned.
*  Okay. But I am having fun just capturing the way we think, the you and I think. And I have
*  a tremendous satisfaction from seeing myself replicated, amplified on a computer. And I get
*  a better understanding of myself. Well, why I had this intuition? Oh, because so and so.
*  I have a playground for myself. I mean, maybe this is a paradigm. Maybe we should all have
*  gigantic, huge aspirational goals and work to make progress on them in little tiny pieces,
*  step by step. I agree with you. All right. That's like a wonderful lesson for us all
*  and a good place to stop. So today, Pearl, thanks so much for being on the Winescape podcast.
*  Thank you, Sean. It's great having me having you having me on your show.
*  All right.
*  you
