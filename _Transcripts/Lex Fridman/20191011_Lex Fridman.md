---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 8671s
Video Keywords: []
Video Views: 63813
Video Rating: None
Video Description: 
---

# David Ferrucci IBM Watson, Jeopardy & Deep Conversations with AI  Lex Fridman Podcast #44
**Lex Fridman:** [October 11, 2019](https://www.youtube.com/watch?v=Whtt2H5_isM)
*  The following is a conversation with David Ferrucci.
*  He led the team that built Watson,
*  the IBM question answering system
*  that beat the top humans in the world
*  at the game of Jeopardy.
*  For spending a couple hours with David,
*  I saw a genuine passion,
*  not only for abstract understanding of intelligence,
*  but for engineering it to solve real world problems
*  under real world deadlines and resource constraints.
*  Where science meets engineering
*  is where brilliant, simple ingenuity emerges.
*  People who work at joining it too
*  have a lot of wisdom earned through failures
*  and eventual success.
*  David is also the founder, CEO,
*  and chief scientist of Elemental Cognition,
*  a company working to engineer AI systems
*  that understand the world the way people do.
*  This is the Artificial Intelligence Podcast.
*  If you enjoy it, subscribe on YouTube,
*  give it five stars on iTunes,
*  support it on Patreon,
*  or simply connect with me on Twitter.
*  Alex Friedman, spelled F-R-I-D-M-A-N.
*  And now, here's my conversation with David Ferrucci.
*  Your undergrad was in biology
*  with an eye toward medical school
*  before you went on for the PhD in computer science.
*  So let me ask you an easy question.
*  What is the difference between
*  biological systems and computer systems?
*  In your, when you sit back,
*  look at the stars and think philosophically.
*  I often wonder whether or not
*  there is a substantive difference.
*  I mean, I think the thing that got me into
*  computer science and into artificial intelligence
*  was exactly this presupposition that
*  if we can get machines to think,
*  or I should say this question,
*  this philosophical question,
*  if we can get machines to think,
*  to understand, to process information the way we do,
*  so if we can describe a procedure, describe a process,
*  even if that process were the intelligence process itself,
*  then what would be the difference?
*  So from a philosophical standpoint,
*  I'm not sure I'm convinced that there is.
*  I mean, you can go in the direction of spirituality,
*  you can go in the direction of the soul,
*  but in terms of what we can experience
*  from an intellectual and physical perspective,
*  I'm not sure there is.
*  Clearly there are implement,
*  there are different implementations,
*  but if you were to say,
*  is a biological information processing system
*  fundamentally more capable than one we might be able
*  to build out of silicon or some other substrate,
*  I don't know that there is.
*  How distant do you think is the biological implementation?
*  So fundamentally they may have the same capabilities,
*  but is it really a far mystery
*  where a huge number of breakthroughs are needed
*  to be able to understand it,
*  or is it something that, for the most part,
*  in the important aspects,
*  echoes of the same kind of characteristics?
*  Yeah, that's interesting.
*  I mean, so your question presupposes
*  that there's this goal to recreate
*  what we perceive as biological intelligence.
*  I'm not sure that's how I would state the goal.
*  I mean, I think that studying-
*  What is the goal?
*  Good, so I think there are a few goals.
*  I think that understanding the human brain
*  and how it works is important for us
*  to be able to diagnose and treat issues
*  for us to understand our own strengths and weaknesses,
*  both intellectual, psychological, and physical.
*  So neuroscience and understanding the brain
*  from that perspective, there's a clear goal there.
*  From the perspective of saying,
*  I wanna mimic human intelligence,
*  that one's a little bit more interesting.
*  Human intelligence certainly has a lot of things we envy.
*  It's also got a lot of problems too.
*  So I think we're capable of sort of stepping back
*  and saying, what do we want out of an intelligence?
*  How do we wanna communicate with that intelligence?
*  How do we want it to behave?
*  How do we want it to perform?
*  Now, of course, it's somewhat of an interesting argument
*  because I'm sitting here as a human
*  with a biological brain,
*  and I'm critiquing the strengths and weaknesses
*  of human intelligence and saying that we have
*  the capacity to step back and say,
*  what is intelligence and what do we really want out of it?
*  And that in and of itself suggests that
*  human intelligence is something quite enviable,
*  that it can introspect that way.
*  And the flaws, you mentioned the flaws.
*  The humans have flaws.
*  Yeah, I mean, I think that flaws that human intelligence has
*  is extremely prejudicial and biased
*  in the way it draws many inferences.
*  Do you think those are, sorry to interrupt,
*  do you think those are features or are those bugs?
*  Do you think the prejudice, the forgetfulness, the fear,
*  what other flaws?
*  List them all.
*  What, love?
*  Maybe that's a flaw.
*  You think those are all things that can be,
*  get in the weight of intelligence
*  or the essential components of intelligence?
*  Well, again, if you go back and you define intelligence
*  as being able to sort of accurately, precisely,
*  rigorously reason, develop answers
*  and justify those answers in an objective way,
*  yeah, then human intelligence has these flaws
*  in that it tends to be more influenced
*  by some of the things you said.
*  And it's largely an inductive process,
*  meaning it takes past data,
*  uses that to predict the future.
*  Very advantageous in some cases,
*  but fundamentally biased and prejudicial in other cases,
*  because it's gonna be strongly influenced by its prior,
*  is whether they're right or wrong
*  from some objective reasoning perspective,
*  you're gonna favor them because those are the decisions
*  or those are the paths that succeeded in the past.
*  And I think that mode of intelligence makes a lot of sense
*  for when your primary goal is to act quickly
*  and survive and make fast decisions.
*  And I think those create problems
*  when you wanna think more deeply
*  and make more objective and reasoned decisions.
*  Of course, humans capable of doing both.
*  They do sort of one more naturally than they do the other,
*  but they're capable of doing both.
*  You're saying they do the one that responds quickly
*  more naturally.
*  Right.
*  Because that's the thing we kind of need
*  to not be eaten by the predators in the world.
*  For example, but then we've learned
*  to reason through logic, we've developed science,
*  we've trained people to do that.
*  I think that's harder for the individual to do.
*  I think it requires training and teaching.
*  I think we are, the human mind certainly is capable of it,
*  but we find it more difficult.
*  And then there are other weaknesses, if you will,
*  as you mentioned earlier, just memory capacity
*  and how many chains of inference can you actually go through
*  without losing your way?
*  So just focus.
*  So the way you think about intelligence,
*  and we're really sort of floating
*  in this philosophical space,
*  but I think you're the perfect person to talk about this
*  because we'll get to Jeopardy and beyond.
*  That's like an incredible,
*  one of the most incredible accomplishments in AI,
*  in the history of AI,
*  but hence the philosophical discussion.
*  So let me ask, you've kind of alluded to it,
*  but let me ask again, what is intelligence
*  underlying the discussions we'll have
*  with Jeopardy and beyond?
*  How do you think about intelligence?
*  Is it a sufficiently complicated problem,
*  being able to reason your way through solving that problem?
*  Is that kind of how you think about
*  what it means to be intelligent?
*  So I think of intelligence primarily two ways.
*  One is the ability to predict.
*  So in other words, if I have a problem,
*  can I predict what's gonna happen next,
*  whether it's to predict the answer of a question
*  or to say, look, I'm looking at all the market dynamics
*  and I'm gonna tell you what's gonna happen next,
*  or you're in a room and somebody walks in
*  and you're gonna predict what they're gonna do next
*  or what they're gonna say next.
*  In a highly dynamic environment full of uncertainty,
*  be able to predict.
*  The more variables, the more complex,
*  the more possibilities, the more complex.
*  But can I take a small amount of prior data
*  and learn the pattern and then predict
*  what's gonna happen next accurately and consistently?
*  That's certainly a form of intelligence.
*  What do you need for that, by the way?
*  You need to have an understanding
*  of the way the world works
*  in order to be able to unroll it into the future, right?
*  What do you think is needed to predict?
*  Depends what you mean by understanding.
*  I need to be able to find that function.
*  This is very much what deep learning does,
*  machine learning does, is if you give me enough prior data
*  and you tell me what the output variable is that matters,
*  I'm gonna sit there and be able to predict it.
*  And if I can predict it accurately
*  so that I can get it right more often than not, I'm smart.
*  If I can do that with less data and less training time,
*  I'm even smarter.
*  If I can figure out what's even worth predicting,
*  I'm smarter, meaning I'm figuring out
*  what path is gonna get me toward a goal.
*  What about picking a goal?
*  Sorry to interrupt again.
*  Well, that's interesting about picking a goal,
*  sort of an interesting thing.
*  I think that's where you bring in,
*  what do you pre-program to do?
*  We talk about humans and humans are pre-programmed to survive.
*  So sort of their primary driving goal,
*  what do they have to do to do that?
*  And that can be very complex, right?
*  So it's not just figuring out that you need to run away
*  from the ferocious tiger,
*  but we survive in a social context as an example.
*  So understanding the subtleties of social dynamics
*  becomes something that's important for surviving,
*  finding a mate, reproducing, right?
*  So we're continually challenged with complex sets
*  of variables, complex constraints, rules of conduct,
*  rules, if you will, or patterns,
*  and we learn how to find the functions
*  and predict the things, in other words,
*  represent those patterns efficiently
*  and be able to predict what's gonna happen.
*  And that's a form of intelligence.
*  That doesn't really require anything specific
*  other than the ability to find that function
*  and predict that right answer.
*  It's certainly a form of intelligence.
*  But then when we say, well, do we understand each other?
*  In other words, would you perceive me as intelligent
*  beyond that ability to predict?
*  So now I can predict, but I can't really articulate
*  how I'm going through that process,
*  what my underlying theory is for predicting.
*  And I can't get you to understand what I'm doing
*  so that you can follow,
*  you can figure out how to do this yourself
*  if you did not have, for example,
*  the right pattern-managing machinery that I did.
*  And now we potentially have this breakdown
*  where in effect, I'm intelligent,
*  but I'm sort of an alien intelligence relative to you.
*  You're intelligent, but nobody knows about it.
*  Well, I can see the output.
*  So you're saying, let's sort of separate the two things.
*  One is you explaining why you were able
*  to predict the future.
*  And the second is me being able to,
*  impressing me that you're intelligent,
*  me being able to know that you successfully predicted
*  the future.
*  Do you think that's?
*  Well, it's not impressing you that I'm intelligent.
*  In other words, you may be convinced
*  that I'm intelligent in some form.
*  So how, what would convince you?
*  Because of my ability to predict.
*  So I would look at the metrics.
*  When you pan, I'd say, wow, you're right more times
*  than I am.
*  You're doing something interesting.
*  That's a form of intelligence.
*  But then what happens is if I say, how are you doing that?
*  And you can't communicate with me
*  and you can't describe that to me.
*  Now I may label you a savant.
*  I may say, well, you're doing something weird
*  and it's just not very interesting to me
*  because you and I can't really communicate.
*  And so now, so this is interesting, right?
*  Because now this is, you're in this weird place
*  where for you to be recognized as intelligent
*  the way I'm intelligent, then you and I sort of have
*  to be able to communicate.
*  And then my, we start to understand each other
*  and then my respect and my appreciation,
*  my ability to relate to you starts to change.
*  So now you're not an alien intelligence anymore.
*  You're a human intelligence now
*  because you and I can communicate.
*  And so I think when we look at animals, for example,
*  animals can do things we can't quite comprehend.
*  We don't quite know how they do them,
*  but they can't really communicate with us.
*  They can't put what they're going through in our terms.
*  And so we think of them as sort of, well,
*  they're these alien intelligences
*  and they're not really worth necessarily what we're worth.
*  We don't treat them the same way as a result of that.
*  But it's hard because who knows what's going on.
*  So just a quick elaboration on that,
*  explaining that you're intelligent,
*  explaining the reasoning that went into the prediction
*  is not some kind of mathematical proof.
*  If we look at humans, look at political debates
*  and discourse on Twitter, it's mostly just telling stories.
*  So your task is, sorry, your task is not to tell
*  an accurate depiction of how you reason,
*  but to tell a story, real or not,
*  that convinces me that there was a mechanism
*  by which you are right.
*  Well, ultimately, that's what a proof is.
*  I mean, even a mathematical proof is that
*  because ultimately the other mathematicians
*  have to be convinced by your proof.
*  Otherwise, in fact, there have been several proofs out there
*  where mathematicians would study for a long time
*  before they were convinced
*  that it actually proved anything.
*  You never know if it proved anything
*  until the community of mathematicians decided that it did.
*  So I mean, but it's a real thing.
*  And that's sort of the point,
*  is that ultimately this notion of understanding us,
*  understanding something, is ultimately a social concept.
*  In other words, I have to convince enough people
*  that I did this in a reasonable way.
*  I did this in a way that other people can understand
*  and replicate and that it makes sense to them.
*  So human intelligence is bound together in that way.
*  We're bound up in that sense.
*  We sort of never really get away with it
*  until we can sort of convince others
*  that our thinking process makes sense.
*  Did you think the general question of intelligence
*  is then also a social construct?
*  So if we ask questions
*  of an artificial intelligence system,
*  is this system intelligent?
*  The answer will ultimately be a socially constructed concept.
*  I think, so I think, I'm making two statements.
*  I'm saying we can try to define intelligence
*  in a super objective way that says here's this data.
*  I wanna predict this type of thing, learn this function,
*  and then if you get it right,
*  often enough we consider you intelligent.
*  But that's more like a savant.
*  I think it is.
*  It doesn't mean it's not useful.
*  It could be incredibly useful.
*  It could be solving a problem we can't otherwise solve
*  and can solve it more reliably than we can.
*  But then there's this notion of
*  can humans take responsibility
*  for the decision that you're making?
*  Can we make those decisions ourselves?
*  Can we relate to the process that you're going through?
*  And now you as an agent,
*  whether you're a machine or another human frankly,
*  are now obliged to make me understand
*  how it is that you're arriving at that answer
*  and allow me, me or the obviously community
*  or judge of people to decide whether or not
*  that makes sense.
*  And by the way, that happens with the humans as well.
*  You're sitting down with your staff, for example,
*  and you ask for suggestions about what to do next.
*  And someone says, oh, I think you should buy,
*  and I think you should buy this much,
*  or have a salad or whatever it is.
*  Or I think you should launch the product today or tomorrow
*  or launch this product versus that product,
*  whatever the decision may be.
*  And you ask why, and the person says,
*  I just have a good feeling about it.
*  And you're not very satisfied.
*  Now, that person could be, you might say,
*  well, you've been right before,
*  but I'm gonna put the company on the line.
*  Can you explain to me why I should believe this?
*  Right.
*  And that explanation may have nothing to do with the truth.
*  You just, the ultimate-
*  It's gotta convince the other person.
*  It's still be wrong.
*  It's still be wrong.
*  It's just gotta be convincing.
*  But it's ultimately gotta be convincing.
*  And that's why I'm saying, we're bound together.
*  Our intelligences are bound together in that sense.
*  We have to understand each other.
*  And if, for example, you're giving me an explanation,
*  I mean, this is a very important point, right?
*  You're giving me an explanation,
*  and I'm not good,
*  and then I'm not good at reasoning well,
*  and being objective, and following logical paths
*  and consistent paths, and I'm not good at measuring
*  and sort of computing probabilities across those paths.
*  What happens is, collectively,
*  we're not gonna do well.
*  How hard is that problem?
*  The second one.
*  So I think we'll talk quite a bit about the first
*  on a specific objective metric benchmark performing well.
*  But being able to explain the steps, the reasoning,
*  how hard is that problem?
*  I think that's very hard.
*  I mean, I think that that's,
*  well, it's hard for humans.
*  The thing that's hard for humans, as you know,
*  may not necessarily be hard for computers and vice versa.
*  So, sorry, so how hard is that problem for computers?
*  I think it's hard for computers.
*  And the reason why I related to,
*  or saying that it's also hard for humans
*  is because I think when we step back
*  and we say we wanna design computers to do that,
*  one of the things we have to recognize is,
*  we're not sure how to do it well.
*  I'm not sure we have a recipe for that.
*  And even if you wanted to learn it,
*  it's not clear exactly what data we use
*  and what judgments we use to learn that well.
*  And so what I mean by that is,
*  if you look at the entire enterprise of science,
*  science is supposed to be at about objective reason
*  and reason, right?
*  So we think about,
*  she who's the most intelligent person
*  or group of people in the world,
*  do we think about the savants
*  who can close their eyes and give you a number,
*  we think about the think tanks
*  or the scientists or the philosophers
*  who kind of work through the details
*  and write the papers
*  and come up with the thoughtful logical proves
*  and use the scientific method.
*  And I think it's the latter.
*  And my point is that,
*  how do you train someone to do that?
*  And that's what I mean by it's hard.
*  What's the process of training people to do that?
*  Well, that's a hard process.
*  We work as a society,
*  we work pretty hard to get other people
*  to understand our thinking
*  and to convince them of things.
*  Now we could persuade them,
*  obviously we talked about this,
*  like human flaws or weaknesses,
*  we can persuade them through emotional means.
*  But to get them to understand and connect to
*  and follow a logical argument is difficult.
*  We try it, we do it as scientists,
*  we try to do it as journalists,
*  we try to do it as even artists in many forms,
*  as writers, as teachers.
*  We go through a fairly significant training process
*  to do that.
*  And then we could ask, well, why is that so hard?
*  But it's hard.
*  And for humans, it takes a lot of work.
*  And when we step back and say,
*  well, how do we get a machine to do that?
*  It's a vexing question.
*  How would you begin to try to solve that?
*  And maybe just a quick pause
*  because there's an optimistic notion
*  in the things you're describing,
*  which is being able to explain something through reason.
*  But if you look at algorithms that recommend things
*  that we look at next,
*  whether it's Facebook, Google,
*  advertisement-based companies,
*  their goal is to convince you to buy things
*  based on anything.
*  So that could be reason,
*  because the best of advertisement
*  is showing you things that you really do need
*  and explain why you need it.
*  But it could also be through emotional manipulation.
*  The algorithm that describes why a certain reason,
*  a certain decision was made,
*  how hard is it to do it through emotional manipulation?
*  And why is that a good or a bad thing?
*  So you've kind of focused on reason, logic,
*  really showing in a clear way why something is good.
*  One, is that even a thing that us humans do?
*  And two, how do you think of the difference
*  in the reasoning aspect and the emotional manipulation?
*  So you call it emotional manipulation,
*  but more objectively is essentially saying,
*  there are certain features of things
*  that seem to attract your attention,
*  I mean, to kind of give you more of that stuff.
*  And manipulation is a bad word.
*  Yeah, I'm not saying it's right or wrong.
*  It works to get your attention
*  and it works to get you to buy stuff.
*  And when you think about algorithms
*  that look at the patterns of features
*  that you seem to be spending your money on
*  and say, I'm gonna give you something
*  with a similar pattern,
*  so I'm gonna learn that function
*  because the objective is to get you to click on it
*  or get you to buy it or whatever it is.
*  I don't know, I mean, it is what it is.
*  I mean, that's what the algorithm does.
*  You can argue whether it's good or bad.
*  It depends what your goal is.
*  I guess this seems to be very useful for convincing,
*  for telling a story.
*  For convincing humans, it's good
*  because again, this goes back to what is the human behavior like?
*  How does the human brain respond to things?
*  I think there's a more optimistic view of that too,
*  which is that if you're searching
*  for certain kinds of things,
*  you've already reasoned that you need them.
*  And these algorithms are saying, look, that's up to you
*  to reason whether you need something or not.
*  That's your job.
*  You may have an unhealthy addiction to this stuff
*  or you may have a reasoned and thoughtful,
*  explanation for why it's important to you.
*  And the algorithms are saying, hey, that's like whatever.
*  Like that's your problem.
*  All I know is you're buying stuff like that.
*  You're interested in stuff like that.
*  Could be a bad reason, could be a good reason.
*  That's up to you.
*  I'm gonna show you more of that stuff.
*  And I think that it's not good or bad.
*  It's not reasoned or not reasoned.
*  The algorithm is doing what it does,
*  which is saying, you seem to be interested in this.
*  I'm gonna show you more of that stuff.
*  And I think we're seeing this not just in buying stuff,
*  but even in social media, you're reading this kind of stuff.
*  I'm not judging on whether it's good or bad.
*  I'm not reasoning at all.
*  I'm just saying, I'm gonna show you other stuff
*  with similar features.
*  And that's it.
*  And I wash my hands from it and I say,
*  that's all that's going on.
*  People are so harsh on AI systems.
*  So one, the bar of performance is extremely high.
*  And yet we also ask them to, in the case of social media,
*  to help find the better angels of our nature
*  and help make a better society.
*  What do you think about the role of AI there?
*  I agree with you.
*  That's the interesting dichotomy, right?
*  Because on one hand, we're sitting there
*  and we're sort of doing the easy part,
*  which is finding the patterns.
*  We're not building, the system's not building a theory
*  that is consumable and understandable by other humans
*  that can be explained and justified.
*  And so on one hand to say, oh, AI is doing this.
*  Why isn't doing this other thing?
*  Well, this other thing's a lot harder.
*  And it's interesting to think about why it's harder.
*  And because you're interpreting the data
*  in the context of prior models.
*  In other words, understandings of what's important
*  in the world, what's not important.
*  What are all the other abstract features
*  that drive our decision-making?
*  What's sensible, what's not sensible, what's good,
*  what's bad, what's moral, what's valuable, what isn't.
*  Where is that stuff?
*  No one's applying the interpretation.
*  So when I see you clicking on a bunch of stuff
*  and I look at these simple features, the raw features,
*  the features that are there in the data,
*  like what words are being used,
*  or how long the material is,
*  or other very superficial features,
*  what colors are being used in the material.
*  Like, I don't know why you're clicking
*  on this stuff you're clicking.
*  Or if it's products, what the price is,
*  or what the categories, and stuff like that.
*  And I just feed you more of the same stuff.
*  That's very different than kind of getting in there
*  and saying, what does this mean?
*  The stuff you're reading, like why are you reading it?
*  What assumptions are you bringing to the table?
*  Are those assumptions sensible?
*  Does the material make any sense?
*  Does it lead you to thoughtful, good conclusions?
*  Again, there's interpretation and judgment involved
*  in that process that isn't really happening in the AI today.
*  That's harder.
*  Because you have to start getting at the meaning
*  of the stuff, of the content.
*  You have to get at how humans interpret the content
*  relative to their value system and deeper thought processes.
*  So that's what meaning means is not just some kind of
*  deep, timeless, semantic thing that the statement represents,
*  but also how a large number of people
*  are likely to interpret.
*  So it's again, even meaning is a social construct.
*  So you have to try to predict how most people
*  would understand this kind of statement.
*  Yeah, meaning is often relative.
*  But meaning implies that the connections
*  go beneath the surface of the artifacts.
*  If I show you a painting, it's a bunch of colors on a canvas,
*  what does it mean to you?
*  And it may mean different things to different people
*  because of their different experiences.
*  It may mean something even different
*  to the artist who painted it.
*  As we try to get more rigorous with our communication,
*  we try to really nail down that meaning.
*  So we go from abstract art to precise mathematics,
*  precise engineering drawings and things like that.
*  We're really trying to say, I wanna narrow that space
*  of possible interpretations,
*  because the precision of the communication
*  ends up becoming more and more important.
*  And so that means that I have to specify,
*  and I think that's why this becomes really hard.
*  Because if I'm just showing you an artifact
*  and you're looking at it superficially,
*  whether it's a bunch of words on a page,
*  or whether it's brushstrokes on a canvas
*  or pixels on a photograph, you can sit there
*  and you can interpret lots of different ways
*  at many, many different levels.
*  But when I wanna align our understanding of that,
*  I have to specify a lot more stuff
*  that's actually not directly in the artifact.
*  Now I have to say, well, how are you interpreting
*  this image and that image?
*  And what about the colors and what do they mean to you?
*  What perspective are you bringing to the table?
*  What are your prior experiences with those artifacts?
*  What are your fundamental assumptions and values?
*  What is your ability to kind of reason,
*  to chain together logical implications
*  as you're sitting there and saying,
*  well, if this is the case, then I would conclude this.
*  And if that's the case, then I would conclude that.
*  So your reasoning processes and how they work,
*  your prior models and what they are,
*  your values and your assumptions,
*  all those things now come together into the interpretation.
*  Getting in sync of that is hard.
*  And yet humans are able to intuit some of that
*  without any pre-
*  Because they have the shared experience.
*  And we're not talking about two people
*  having a shared experience.
*  No.
*  As a society.
*  That's correct.
*  We have the shared experience and we have similar brains.
*  So we tend to, in other words,
*  part of our shared experience is our shared local experience.
*  Like we may live in the same culture,
*  we may live in the same society,
*  and therefore we have similar educations.
*  We have similar, what we like to call prior models
*  about the word prior experiences.
*  And we use that as a, think of it as a wide collection
*  of interrelated variables,
*  and they're all bound to similar things.
*  And so we take that as our background
*  and we start interpreting things similarly.
*  But as humans, we have a lot of shared experience.
*  We do have similar brains, similar goals,
*  similar emotions under similar circumstances
*  because we're both humans.
*  So now one of the early questions you asked,
*  how is biological and computer information systems
*  fundamentally different?
*  Well, one is humans come with a lot of pre-programmed stuff,
*  a ton of program stuff,
*  and they're able to communicate because they have a lot of,
*  because they share that stuff.
*  Do you think that shared knowledge,
*  if we can maybe escape the hardware question,
*  how much is encoded in the hardware,
*  just the shared knowledge in the software,
*  the history, the many centuries of wars and so on
*  that came to today, that shared knowledge,
*  how hard is it to encode?
*  Do you have a hope?
*  Can you speak to how hard is it to encode that knowledge
*  systematically in a way that could be used by a computer?
*  So I think it is possible to learn to, for a machine,
*  to program a machine to acquire that knowledge
*  with a similar foundation, in other words,
*  a similar interpretive foundation
*  for processing that knowledge.
*  What do you mean by that?
*  So in other words, we view the world in a particular way.
*  So in other words, we have a, if you will,
*  as humans, we have a framework
*  for interpreting the world around us.
*  So we have multiple frameworks
*  for interpreting the world around us.
*  But if you're interpreting, for example,
*  social political interactions,
*  you're thinking about whether there's people,
*  there's collections and groups of people, they have goals,
*  goals largely built around survival and quality of life.
*  There are fundamental economics around scarcity of resources.
*  And when humans come and start interpreting
*  a situation like that, because you brought up
*  like historical events,
*  they start interpreting situations like that.
*  They apply a lot of this fundamental framework
*  for interpreting that.
*  Well, who are the people?
*  What were their goals?
*  What resources did they have?
*  How much power or influence did they have over the other?
*  Like this fundamental substrate, if you will,
*  for interpreting and reasoning about that.
*  So I think it is possible to imbue a computer
*  with that stuff that humans take for granted
*  when they go and sit down and try to interpret things.
*  And then with that foundation, they acquire,
*  they start acquiring the details,
*  the specifics in a given situation,
*  are then able to interpret it with regard to that framework.
*  And then given that interpretation, they can do what?
*  They can predict.
*  But not only can they predict,
*  they can predict now with an explanation
*  that can be given in those terms,
*  in the terms of that underlying framework
*  that most humans share.
*  Now you could find humans that come
*  and interpret events very differently than other humans
*  because they're like using a different framework.
*  The movie Matrix comes to mind where they decided
*  humans were really just batteries,
*  and that's how they interpreted the value of humans
*  as a source of electrical energy.
*  But I think that for the most part,
*  we have a way of interpreting the events
*  or these social events around us
*  because we have this shared framework.
*  It comes from, again, the fact that we're similar beings
*  that have similar goals, similar emotions,
*  and we can make sense out of these.
*  These frameworks make sense to us.
*  So how much knowledge is there, do you think?
*  So you said it's possible.
*  Well, there's a tremendous amount of detailed knowledge
*  in the world.
*  You can imagine effectively infinite number
*  of unique situations and unique configurations
*  of these things.
*  But the knowledge that you need,
*  what I refer to as the frameworks,
*  for interpreting them, I don't think.
*  I think those are finite.
*  You think the frameworks are more important
*  than the bulk of the knowledge.
*  So like, framing.
*  Yeah, because what the frameworks do
*  is they give you now the ability to interpret and reason,
*  and to interpret and reason,
*  to interpret and reason over the specifics
*  in ways that other humans would understand.
*  What about the specifics?
*  Well, you acquire the specifics by reading
*  and by talking to other people.
*  So I'm mostly actually just even,
*  if we can focus on even the beginning,
*  the common sense stuff,
*  the stuff that doesn't even require reading,
*  or it almost requires playing around with the world
*  or something.
*  Just being able to sort of manipulate objects,
*  drink water and so on, all of that.
*  Every time we try to do that kind of thing
*  in robotics or AI, it seems to be like an onion.
*  You seem to realize how much knowledge
*  is really required to perform
*  even some of these basic tasks.
*  Do you have that sense as well?
*  If so, how do we get all those details?
*  Are they written down somewhere?
*  Do they have to be learned through experience?
*  So I think if you're talking about the physics,
*  the basic physics around us, for example,
*  acquiring information about acquiring how that works.
*  Yeah, I think there's a combination of things going on.
*  I think there is fundamental pattern matching,
*  like what we were talking about before.
*  You see enough examples, enough data about something,
*  you just start assuming that.
*  And with similar input,
*  I'm gonna predict similar outputs.
*  You can't necessarily explain it at all.
*  You may learn very quickly that when you let something go,
*  it falls to the ground.
*  But you can't necessarily explain that.
*  But that's such a deep idea,
*  that if you let something go, like the idea of gravity.
*  I mean, people are letting things go
*  and counting on them falling well
*  before they understood gravity.
*  But that seems to be, that's exactly what I mean,
*  before you take a physics class
*  or study anything about Newton,
*  just the idea that stuff falls to the ground
*  and then you be able to generalize
*  that all kinds of stuff falls to the ground.
*  It just seems like a non, without encoding it,
*  like hard coding it in,
*  it seems like a difficult thing to pick up.
*  It seems like you have to have a lot of different knowledge
*  to be able to integrate that into the framework,
*  sort of into everything else.
*  So both know that stuff falls to the ground
*  and start to reason about social political discourse.
*  So both like the very basic
*  and the high level reasoning decision making.
*  I guess my question is how hard is this problem?
*  Sorry to linger on it because again,
*  and we'll get to it for sure,
*  Watson with Jeopardy did is take on a problem
*  that's much more constrained
*  but has the same hugeness of scale,
*  at least from the outsider's perspective.
*  So I'm asking the general life question
*  of to be able to be an intelligent being
*  and reasoning in the world about both gravity and politics,
*  how hard is that problem?
*  So I think it's solvable.
*  Okay, now beautiful.
*  So what about time travel?
*  Okay, I'm not talking.
*  I'm just saying.
*  Not as convinced.
*  Not as convinced yet, okay.
*  No, I think it is.
*  I think it is solvable.
*  I mean, I think that it's a,
*  first of all, it's about getting machines to learn.
*  Learning is fundamental.
*  And I think we're already in a place
*  that we understand, for example,
*  how machines can learn in various ways.
*  Right now, our learning stuff is sort of primitive
*  in that we haven't sort of taught machines
*  to learn the frameworks.
*  We don't communicate our frameworks
*  because of how shared they are.
*  In some cases, we do,
*  but we don't annotate, if you will,
*  all the data in the world with the frameworks
*  that are inherent or underlying our understanding.
*  Instead, we just operate with the data.
*  So if we wanna be able to reason over the data
*  in similar terms in the common frameworks,
*  we need to be able to teach the computer,
*  or at least we need to program the computer to acquire,
*  to have access to and acquire,
*  learn the frameworks as well,
*  and connect the frameworks to the data.
*  I think this can be done.
*  I think we can start, I think, machine learning,
*  for example, with enough examples,
*  we can start to learn these basic dynamics.
*  Will they relate the necessary to gravity,
*  not unless they can also acquire those theories as well
*  and put the experiential knowledge
*  and connect it back to the theoretical knowledge.
*  I think if we think in terms of these class of architectures
*  that are designed to both learn the specifics,
*  find the patterns, but also acquire the frameworks
*  if we think in terms of robust architectures like this,
*  I think there is a path toward getting there.
*  In terms of encoding architectures like that,
*  do you think systems that are able to do this
*  will look like neural networks or representing,
*  if you look back to the 80s and 90s with the expert systems,
*  so more like graphs, systems that are based in logic,
*  able to contain a large amount of knowledge
*  where the challenge was the automated acquisition
*  of that knowledge.
*  I guess the question is, when you collect both the frameworks
*  and the knowledge from the data,
*  what do you think that thing will look like?
*  Yeah, so I mean, I think asking the question
*  they look like neural networks is a bit of a red herring.
*  I mean, I think that they will certainly do inductive
*  or pattern match based reasoning.
*  And I've already experimented with architectures
*  that combine both that use machine learning
*  and neural networks to learn certain classes of knowledge,
*  in other words, to find repeated patterns
*  in order for it to make good inductive guesses,
*  but then ultimately to try to take those learnings
*  and marry them, in other words, connect them to frameworks
*  so that it can then reason over that
*  in terms other humans understand.
*  So for example, at Elemental Cognition, we do both.
*  We have architectures that do both, but both those things,
*  but also have a learning method
*  for acquiring the frameworks themselves and saying,
*  look, ultimately I need to take this data.
*  I need to interpret it in the form of these frameworks
*  so they can reason over it.
*  So there is a fundamental knowledge representation
*  like what you're saying, like these graphs of logic,
*  if you will.
*  There are also neural networks
*  that acquire certain class of information.
*  Then they then align them with these frameworks,
*  but there's also a mechanism
*  to acquire the frameworks themselves.
*  Yeah, so it seems like the idea of frameworks
*  requires some kind of collaboration with humans.
*  Absolutely.
*  So do you think of that collaboration as direct?
*  And let's be clear, only for the express purpose
*  that you're designing an intelligence
*  that can ultimately communicate with humans
*  in the terms of frameworks that help them understand things.
*  Right, so to be really clear,
*  you can independently create a machine learning system
*  and intelligence that I might call an alien intelligence
*  that does a better job than you with some things,
*  but can't explain the framework to you.
*  That doesn't mean it might be better than you at the thing.
*  It might be that you cannot comprehend the framework
*  that it may have created for itself
*  that is inexplicable to you.
*  That's a reality.
*  But you're more interested in a case where you can.
*  I am, yeah.
*  My sort of approach to AI is because
*  I've set the goal for myself.
*  I want machines to be able to ultimately communicate
*  understanding with humans.
*  I want to be able to acquire and communicate,
*  acquire knowledge from humans
*  and communicate knowledge to humans.
*  They should be using what inductive
*  machine learning techniques are good at,
*  which is to observe patterns of data,
*  whether it be in language or whether it be in images
*  or videos or whatever,
*  to acquire these patterns,
*  to induce the generalizations from those patterns,
*  but then ultimately work with humans to connect them
*  to frameworks, interpretations if you will,
*  that ultimately make sense to humans.
*  Of course, the machine is gonna have the strength
*  that it has, the richer and longer memory,
*  it has the more rigorous reasoning abilities,
*  the deeper reasoning abilities,
*  so it'll be an interesting complimentary relationship
*  between the human and the machine.
*  Do you think that ultimately needs explainability
*  like a machine?
*  So if we look, we study, for example,
*  Tesla autopilot a lot, where humans,
*  I don't know if you've driven the vehicle
*  or are aware of what it is.
*  So basically the human and machine are working together there
*  and the human is responsible for their own life
*  to monitor the system and the system fails every few miles.
*  And so there's hundreds, there's millions of those failures
*  a day and so that's like a moment of interaction.
*  Do you see?
*  Yeah, that's exactly right.
*  That's a moment of interaction where the machine
*  has learned some stuff, it has a failure,
*  somehow the failure's communicated,
*  the human is now filling in the mistake, if you will,
*  or maybe correcting or doing something
*  that is more successful in that case,
*  the computer takes that learning.
*  So I believe that the collaboration
*  between human and machine,
*  I mean that's sort of a primitive example
*  of sort of a more, another example is where
*  the machine's literally talking to you and saying,
*  look, I'm reading this thing.
*  I know that the next word might be this or that,
*  but I don't really understand why.
*  I have my guess, can you help me understand
*  the framework that supports this
*  and then can kind of acquire that,
*  take that and reason about it and reuse it.
*  The next time it's reading to try to understand something,
*  not unlike a human student might do.
*  I mean I remember when my daughter was in first grade
*  and she had a reading assignment about electricity
*  and somewhere in the text it says,
*  and electricity is produced by water flowing over turbines
*  or something like that.
*  And then there's a question that says,
*  well how is electricity created?
*  And so my daughter comes to me and says,
*  I mean I could, created and produced
*  are kind of synonyms in this case,
*  so I can go back to the text and I can copy
*  by water flowing over turbines,
*  but I have no idea what that means.
*  Like I don't know how to interpret water flowing
*  over turbines and what electricity even is.
*  I mean I can get the answer right by matching the text,
*  but I don't have any framework for understanding
*  what this means at all.
*  And framework really is, I mean it's a set of,
*  not to be mathematical, but axioms of ideas
*  that you bring to the table in interpreting stuff
*  and then you build those up somehow.
*  You build them up with the expectation
*  that there's a shared understanding of what they are.
*  Sure, it's the social, the us humans.
*  Do you have a sense that humans on earth in general
*  share a set of, like how many frameworks are there?
*  I mean it depends on how you bound them, right?
*  So in other words, how big or small,
*  like their individual scope.
*  But there's lots and there are new ones.
*  I think the way I think about it is kind of in a layer.
*  I think of the architectures being layered in that.
*  There's a small set of primitives
*  that allow you the foundation to build frameworks
*  and then there may be many frameworks,
*  but you have the ability to acquire them.
*  And then you have the ability to reuse them.
*  I mean one of the most compelling ways of thinking about this
*  is a reasoning by analogy where I can say,
*  oh wow, I've learned something very similar.
*  I never heard of this game soccer,
*  but if it's like basketball in the sense
*  that the goal's like the hoop
*  and I have to get the ball in the hoop
*  and I have guards and I have this and I have that,
*  like where are the similarities and where are the differences?
*  And I have a foundation now
*  for interpreting this new information.
*  And then different groups,
*  like the millennials will have a framework
*  and then the Democrats and Republicans.
*  Millennials, nobody wants that framework.
*  Well, I mean I think.
*  Nobody understands it.
*  Right, I mean you're talking about political and social ways
*  of interpreting the world around them.
*  And I think these frameworks
*  are still largely, largely similar.
*  I think they differ in maybe
*  what some fundamental assumptions and values are.
*  Now, from a reasoning perspective,
*  like the ability to process the framework
*  might not be that different.
*  The implications of different fundamental values
*  or fundamental assumptions in those frameworks
*  may reach very different conclusions.
*  So from a social perspective,
*  the conclusions may be very different.
*  From an intelligence perspective,
*  I just followed where my assumptions took me.
*  Yeah, the process itself will look similar,
*  but that's a fascinating idea
*  that frameworks really help carve
*  how a statement will be interpreted.
*  I mean, having a Democrat and a Republican framework
*  and then read the exact same statement
*  and the conclusions that you derive
*  will be totally different.
*  From an AI perspective, it's fascinating.
*  What we would want out of the AI
*  is to be able to tell you that this perspective,
*  one perspective, one set of assumptions
*  is gonna lead you here,
*  another set of assumptions is gonna lead you there.
*  And in fact, to help people reason and say,
*  oh, I see where our differences lie.
*  I have this fundamental belief about that.
*  I have this fundamental belief about that.
*  Yeah, that's quite brilliant.
*  From my perspective, NLP, there's this idea
*  that there's one way to really understand a statement,
*  but there probably isn't.
*  There's probably an infinite number of ways
*  to understand a statement, depending on the framework.
*  There's lots of different interpretations.
*  And the broader the content, the richer it is.
*  And so you and I can have very different experiences
*  with the same text, obviously.
*  And if we're committed to understanding each other,
*  we start, and that's the other important point,
*  if we're committed to understanding each other,
*  we start decomposing and breaking down our interpretation
*  to its more and more primitive components
*  until we get to that point where we say,
*  oh, I see why we disagree.
*  And we try to understand how fundamental
*  that disagreement really is.
*  But that requires a commitment
*  to breaking down that interpretation
*  in terms of that framework in a logical way.
*  Otherwise, and this is why I think of AI
*  as really complementing and helping human intelligence
*  to overcome some of its biases and its predisposition
*  to be persuaded by more shallow reasoning
*  in the sense that we get over this idea,
*  well, I'm right because I'm Republican,
*  or I'm right because I'm Democratic,
*  and someone labeled this as a Democratic point of view,
*  or it has the following keywords in it.
*  And if the machine can help us break that argument down
*  and say, wait a second, what do you really think
*  about this, right?
*  So essentially, holding us accountable
*  to doing more critical thinking.
*  I'm gonna have to sit and think about that as fast.
*  I love that.
*  I think that's really empowering use of AI
*  for the public discourse that's completely
*  disintegrating currently as we learn how to do it
*  on social media.
*  That's right.
*  So one of the greatest accomplishments
*  in the history of AI is Watson competing
*  in the game of Jeopardy against humans.
*  And you were a lead in that, a critical part of that.
*  Let's start at the very basics.
*  What is the game of Jeopardy?
*  The game for us humans, human versus human.
*  Right, so it's to take a question and answer it.
*  The game of Jeopardy.
*  It's just the opposite.
*  Actually, well, no, but it's not, right?
*  It's really not.
*  It's really to get a question and answer,
*  but it's what we call a factoid question.
*  So this notion of like, it really relates to some fact
*  that few people would argue whether the facts are true
*  or not.
*  In fact, most people wouldn't.
*  Jeopardy kind of counts on the idea that these statements
*  have factual answers.
*  And the idea is to, first of all, determine whether or not
*  you know the answer, which is sort of an interesting twist.
*  So first of all, understand the question.
*  You have to understand the question.
*  What is it asking?
*  And that's a good point because the questions
*  are not asked directly, right?
*  They're all like, the way the questions are asked
*  is non-linear.
*  It's like, it's a little bit witty.
*  It's a little bit playful sometimes.
*  It's a little bit tricky.
*  Yeah, they're asked in exactly numerous witty,
*  tricky ways.
*  Exactly what they're asking is not obvious.
*  It takes inexperienced humans a while to go,
*  what is it even asking?
*  And it's sort of an interesting realization that you have
*  when somebody says, oh, what's the,
*  Jeopardy is a question answering show.
*  And then he's like, oh, like I know a lot.
*  And then you read it and you're still trying to process
*  the question and the champions have answered and moved on.
*  There are three questions ahead by the time you figured out
*  what the question even meant.
*  So there's definitely an ability there to just parse out
*  what the question even is.
*  So that was certainly challenging.
*  It's interesting historically though,
*  if you look back at the Jeopardy games much earlier,
*  like 60s, 70s, that kind of thing,
*  the questions were much more direct.
*  They weren't quite like that.
*  They got sort of more and more interesting.
*  The way they asked them that sort of got more
*  and more interesting and subtle and nuanced and humorous
*  and witty over time, which really required the human
*  to kind of make the right connections
*  in figuring out what the question was even asking.
*  So yeah, you have to figure out the questions even asking.
*  Then you have to determine whether or not
*  you think you know the answer.
*  And because you have to buzz in really quickly,
*  you sort of have to make that determination
*  as quickly as you possibly can.
*  Otherwise you lose the opportunity to buzz in.
*  You may even before you really know if you know the answer.
*  I think a lot of humans will assume they'll look at,
*  they'll look at it, they process it very superficially.
*  In other words, what's the topic?
*  What are some keywords?
*  And just say, do I know this area or not?
*  Before they actually know the answer,
*  then they'll buzz in and think about it.
*  So it's interesting what humans do.
*  Now some people who know all things,
*  like Ken Jennings or something,
*  or the more recent big Jeopardy player,
*  I mean, they'll just buzz in.
*  They'll just assume they know all of Jeopardy
*  and they'll just buzz in.
*  Watson, interestingly, didn't even come close
*  to knowing all of Jeopardy.
*  Watson really-
*  Even at the peak, even at the-
*  Yeah, so for example, I mean,
*  we had this thing called recall,
*  which is like how many, of all the Jeopardy questions,
*  how many could we even find the right answer for anywhere?
*  Could we come up with, if we had a big body of knowledge,
*  something in the order of several terabytes?
*  I mean, from a web scale, it was actually very small.
*  But from a book scale,
*  I was talking about millions of books, right?
*  So they're calling it millions of books,
*  encyclopedias, dictionaries, books.
*  So it's still a ton of information.
*  And for, I think it was only 85%
*  was the answer anywhere to be found.
*  So you're already down at that level
*  just to get started, right?
*  So, and so it was important to get a very quick sense of,
*  do you think you know the right answer to this question?
*  So we had to compute that confidence
*  as quickly as we possibly could.
*  So in effect, we had to answer it
*  and at least spend some time essentially answering it
*  and then judging the confidence that we,
*  that our answer was right.
*  And then deciding whether or not
*  we were confident enough to buzz in.
*  And that would depend on what else was going on in the game.
*  Because there was a risk.
*  So like if you're really in a situation
*  where I have to take a guess,
*  I have very little to lose,
*  then you'll buzz in with less confidence.
*  So that was accounted for the financial standings
*  of the different competitors.
*  Correct.
*  How much of the game was left?
*  How much time was left?
*  Where you were in the standing, things like that.
*  How many hundreds of milliseconds
*  that we're talking about here?
*  Do you have a sense of what is,
*  like if, what's the target?
*  So, I mean, we targeted answering
*  in under three seconds.
*  And...
*  Buzzing in, so the decision to buzz in
*  and then the actual answering,
*  are those two different stages?
*  Yeah, they were two different things.
*  In fact, we had multiple stages,
*  whereas like we would say,
*  let's estimate our confidence,
*  which was sort of a shallow answering process.
*  And then ultimately decide to buzz in.
*  And then we may take another second or something
*  to kind of go in there and do that.
*  But by and large, we were saying like,
*  we can't play the game.
*  We can't even compete if we can't, on average,
*  answer these questions in around three seconds or less.
*  So you stepped in, so there's this,
*  there's these three humans playing a game
*  and you stepped in with the idea that IBM Watson
*  would be one of, replace one of the humans
*  and compete against two.
*  Can you tell the story of Watson taking on this game?
*  Sure.
*  It seems exceptionally difficult.
*  Yeah, so the story was that it was coming up,
*  I think to the 10 year anniversary of Big Blue,
*  not Big Blue.
*  Deep Blue.
*  IBM wanted to do sort of another kind of really,
*  fun challenge, public challenge,
*  that can bring attention to IBM research
*  and the kind of the cool stuff that we were doing.
*  I had been working in AI at IBM for some time.
*  I had a team doing what's called open domain,
*  factoid question answering,
*  which is, we're not gonna tell you what the questions are,
*  we're not even gonna tell you what they're about.
*  Can you go off and get accurate answers to these questions?
*  And it was an area of AI research that I was involved in.
*  And so it was a very specific passion of mine.
*  Language understanding had always been a passion of mine.
*  One sort of narrow slice on whether or not
*  you could do anything with language
*  was this notion of open domain,
*  meaning I could ask anything about anything.
*  Factoid, meaning it essentially had an answer
*  and being able to do that accurately and quickly.
*  So that was a research area that my team had already been in.
*  And so completely independently,
*  several IBM executives, like, what are we gonna do?
*  What's the next cool thing to do?
*  And Ken Jennings was on his winning streak.
*  This was like, whatever it was, 2004, I think,
*  was on his winning streak.
*  And someone thought, hey, that'll be really cool
*  if the computer can play Jeopardy.
*  And so this was like in 2004,
*  they were shopping this thing around.
*  And everyone was telling the research execs, no way.
*  Like, this is crazy.
*  And we had some pretty senior people in the field
*  and they're saying, no, this is crazy.
*  And they'll come across my desk and I was like,
*  but that's kind of what I'm really interested in doing.
*  And, but there was such this prevailing sense of,
*  this is nuts, we're not gonna risk IBM's reputation on this,
*  we're just not doing it.
*  And this happened in 2004, it happened in 2005.
*  At the end of 2006, it was coming around again.
*  And I was coming off of a,
*  I was doing the open domain question answering stuff,
*  but I was coming off a couple other projects.
*  I had a lot more time to put into this.
*  And I argued that it could be done.
*  And I argued it would be crazy not to do this.
*  Can I, you can be honest at this point.
*  So even though you argued for it,
*  what's the confidence that you had yourself privately
*  that this could be done?
*  Was, we just told the story,
*  how you tell stories to convince others.
*  How confident were you?
*  What was your estimation of the problem at that time?
*  So I thought it was possible.
*  And a lot of people thought it was impossible.
*  I thought it was possible.
*  A reason why I thought it was possible
*  was because I did some brief experimentation.
*  I knew a lot about how we were approaching open domain,
*  factoid question answering,
*  I've been doing it for some years.
*  I looked at the Jeopardy stuff.
*  I said, this is gonna be hard
*  for a lot of the points that we mentioned earlier,
*  hard to interpret the question,
*  hard to do it quickly enough,
*  hard to compute an accurate confidence.
*  None of this stuff had been done well enough before.
*  But a lot of the technologies we're building
*  were the kinds of technologies that should work.
*  But more to the point, what was driving me was
*  I was in IBM research.
*  I was a senior leader in IBM research.
*  And this is the kind of stuff we were supposed to do.
*  In other words, we were basically supposed to do.
*  This is the moonshot.
*  This is the-
*  We were supposed to take things and say,
*  this is an active research area.
*  It's our obligation to kind of,
*  if we have the opportunity to push it to the limits.
*  And if it doesn't work to understand more deeply
*  why we can't do it.
*  And so I was very committed to that notion saying,
*  folks, this is what we do.
*  It's crazy not to do this.
*  This is an active research area.
*  We've been in this for years.
*  Why wouldn't we take this grand challenge
*  and push it as hard as we can?
*  At the very least, we'd be able to come out and say,
*  here's why this problem is way hard.
*  Here's what we tried and here's how we failed.
*  So I was very driven as a scientist from that perspective.
*  And then I also argued,
*  based on what we did a feasibility study,
*  a why I thought it was hard but possible.
*  And I showed examples of where it succeeded,
*  where it failed, why it failed.
*  And sort of a high level architectural approach
*  for why we should do it.
*  But for the most part, at that point,
*  the execs really were just looking for someone crazy enough
*  to say yes, because for several years at that point,
*  everyone had said no, I'm not willing to risk my reputation
*  and my career on this thing.
*  Clearly you did not have such fears.
*  Okay. I did not.
*  So you dived right in and yet, for what I understand,
*  it was performing very poorly in the beginning.
*  So what were the initial approaches and why did they fail?
*  Well, there were lots of hard aspects to it.
*  I mean, one of the reasons why prior approaches
*  that we had worked on in the past failed
*  was because the questions were difficult to interpret.
*  Like what are you even asking for, right?
*  Very often, like if the question was very direct,
*  what city, or what, even then it could be tricky,
*  but what city or what person,
*  often when it would name it very clearly,
*  you would know that.
*  And if there were just a small set of them,
*  in other words, we're gonna ask about these five types.
*  It's gonna be an answer and the answer will be
*  a city in this state or a city in this country.
*  The answer will be a person of this type, right?
*  Like an actor or whatever it is.
*  But it turns out that in Jeopardy,
*  there were like tens of thousands of these things
*  and it was a very, very long tail,
*  meaning it just went on and on.
*  And so even if you focused on trying to encode the types
*  at the very top, like there's five that were the most,
*  let's say five of the most frequent,
*  you still cover a very small percentage of the data.
*  So you couldn't take that approach of saying,
*  I'm just going to try to collect facts
*  about these five or 10 types or 20 types
*  or 50 types or whatever.
*  So that was like one of the first things,
*  like what do you do about that?
*  And so we came up with an approach toward that
*  and the approach looked promising
*  and we continued to improve our ability
*  to handle that problem throughout the project.
*  The other issue was that right from the outside,
*  I said, we're not going to,
*  I committed to doing this in three to five years.
*  So we did it in four, so I got lucky.
*  But one of the things that that,
*  putting that like stake in the ground was,
*  and I knew how hard the language understanding problem was,
*  I said, we're not going to actually understand language
*  to solve this problem.
*  We are not going to interpret the question
*  and the domain of knowledge that the question refers to
*  in reason over that to answer these questions.
*  Obviously we're not going to be doing that.
*  At the same time, simple search wasn't good enough
*  to confidently answer with a single correct answer.
*  First off, that's brilliant.
*  That's such a great mix of innovation
*  and practical engineering, three, four, eight.
*  So you're not trying to solve the general NLU problem.
*  You're saying, let's solve this in any way possible.
*  Oh yeah, no, I was committed to saying,
*  look, we're just solving the open domain
*  question answering problem.
*  We're using Jeopardy as a driver for that.
*  Hard enough, big benchmark, exactly.
*  And now we're-
*  How do we do it?
*  We can just like whatever, like just figure out what works
*  because I want to be able to go back
*  to the academic science community and say,
*  here's what we tried, here's what worked,
*  here's what didn't work.
*  I don't want to go in and say,
*  oh, I only have one technology, I have a hammer,
*  I'm only going to use this.
*  I'm going to do whatever it takes.
*  I'm like, I'm going to think out of the box
*  and do whatever it takes.
*  One, and I also, there was another thing I believed.
*  I believed that the fundamental NLP technologies
*  and machine learning technologies would be adequate.
*  And this was an issue of how do we enhance them?
*  How do we integrate them?
*  How do we advance them?
*  So I had one researcher who came to me
*  who had been working on question answering
*  with me for a very long time,
*  who had said, we're going to need Maxwell's equations
*  for question answering.
*  And I said, if we need some fundamental formula
*  that breaks new ground in how we understand language,
*  we're screwed.
*  We're not going to get there from here.
*  I am not counting, my assumption is I'm not counting
*  on some brand new invention.
*  What I'm counting on is the ability to take everything
*  that has done before to figure out an architecture
*  on how to integrate it well and then see where it breaks
*  and make the necessary advances we need to make
*  until this thing works.
*  Push it hard to see where it breaks and then patch it up.
*  I mean, that's how people change the world.
*  I mean, that's the Elon Musk approach with rockets,
*  SpaceX, that's the Henry Ford and so on.
*  I love it.
*  And I happen to be, and in this case, I happen to be right,
*  but like we didn't know, but you kind of have to put
*  a stake in it.
*  How are you going to run the project?
*  So yeah, and backtracking to search.
*  So if you were to do, what's the brute force solution?
*  What would you search over?
*  So you have a question.
*  How would you search the possible space of answers?
*  Look, web search has come a long way even since then.
*  But at the time, first of all, I mean, there are a couple
*  of other constraints around the problem, which is interesting.
*  So you couldn't go out to the web.
*  You couldn't search the internet.
*  In other words, the AI experiment was we want
*  a self-contained device.
*  If the device is as big as a room, fine,
*  it's as big as a room, but we want a self-contained
*  device, you're not going out to the internet.
*  You don't have a lifeline to anything.
*  So it had to kind of fit in a shoe box, if you will,
*  or at least size of a few refrigerators,
*  whatever it might be.
*  But also you couldn't just get out there.
*  You couldn't go off network, right, to kind of go.
*  So there was that limitation.
*  But then we did, but the basic thing was go do a web search.
*  Problem was, even when we went and did a web search,
*  I don't remember exactly the numbers, but someone
*  in the order of 65% of the time, the answer would be
*  somewhere in the top 10 or 20 documents.
*  So first of all, that's not even good enough
*  to play Jeopardy.
*  In other words, even if you could perfectly pull the answer
*  out of the top 20 documents, top 10 documents,
*  whatever it was, which we didn't know how to do,
*  but even if you could do that, and you knew it was right,
*  and you had enough confidence in it, right,
*  so you'd have to pull out the right answer,
*  you'd have to have confidence it was the right answer.
*  And then you'd have to do that fast enough
*  to now go buzz in, and you'd still only get 65% of them
*  right, which doesn't even put you in the winner circle.
*  Winner circle, you have to be up over 70,
*  and you have to do it really quickly.
*  But now the problem is, well, even if I had somewhere
*  in the top 10 documents, how do I figure out where
*  in the top 10 documents that answer is,
*  and how do I compute a confidence
*  of all the possible candidates, so it's not like
*  I go in knowing the right answer and have to pick it.
*  I don't know the right answer.
*  I have a bunch of documents, somewhere in there
*  is the right answer, how do I, as a machine,
*  go out and figure out which one's right,
*  and then how do I score it?
*  So, and now how do I deal with the fact
*  that I can't actually go out to the web?
*  First of all, if you pause on that, just think about it.
*  If you could go to the web, do you think that problem
*  is solvable, if you just pause on it,
*  just thinking even beyond jeopardy?
*  Do you think the problem of reading text
*  defined where the answer is?
*  We solved that in some definition of solved,
*  given the jeopardy challenge.
*  But how did you do it for jeopardy?
*  So how do you take a body of work on a particular topic
*  and extract the key pieces of information?
*  So now, forgetting about the huge volumes
*  that are on the web, right, so now we have to figure out,
*  we did a lot of source research, in other words,
*  what body of knowledge is gonna be small enough,
*  but broad enough to answer jeopardy?
*  And we ultimately did find the body of knowledge
*  that did that, I mean, it included Wikipedia
*  and a bunch of other stuff.
*  So like encyclopedia type of stuff,
*  I don't know if you can speak to it.
*  Encyclopedia, dictionaries, different types
*  of semantic resources, like WordNet
*  and other types of semantic resources like that,
*  as well as some web crawls, in other words,
*  where we went out and took that content
*  and then expanded it based on statistically producing seeds,
*  using those seeds for other searches,
*  and then expanding that.
*  So using these expansion techniques,
*  we went out and had found enough content
*  that we're like, okay, this is good.
*  And even up until the end, we had a thread of research
*  that was always trying to figure out
*  what content could we efficiently include.
*  I mean, there's a lot of popular,
*  what is the church lady?
*  Well, I think was one of the, like, what,
*  where do you, I guess that's probably an encyclopedia.
*  So I guess like Beatles and something.
*  But then we would take that stuff
*  and we would go out and we would expand.
*  In other words, we go find other content
*  that wasn't in the core resources and expand it.
*  The amount of content grew it by an order of magnitude,
*  but still, again, from a web scale perspective,
*  this is very small amount of content.
*  It's very select.
*  We then took all that content,
*  we pre-analyzed the crap out of it,
*  meaning we parsed it, broke it down
*  into all its individual words,
*  and then we did semantic,
*  static and semantic parses on it,
*  had computer algorithms that annotated it,
*  and we index that in a very rich and very fast index.
*  So we have a relatively huge amount of,
*  let's say the equivalent of, for the sake of argument,
*  two to five million bucks.
*  We've now analyzed all that,
*  blowing up its size even more,
*  because now we have all this metadata,
*  and then we richly indexed all of that,
*  by the way, in a giant in-memory cache.
*  So Watson did not go to disk.
*  So the infrastructure component there,
*  if you could just speak to it, how tough,
*  I mean, I know 2000, maybe this is 2008, nine,
*  that's kind of a long time ago.
*  Right.
*  How hard is it to use multiple machines?
*  How hard is the infrastructure component,
*  the hardware component?
*  So we used IBM hardware.
*  We had something like, I forget exactly,
*  but close to 3000 cores, completely connected.
*  So we had a switch where every CPU
*  was connected to every other CPU.
*  And they were sharing memory in some kind of way.
*  Kind of clever.
*  Shared memory, right?
*  And all this data was pre-analyzed
*  and put into a very fast indexing structure
*  that was all in memory.
*  And then we took that question,
*  we would analyze the question,
*  so all the content was now pre-analyzed.
*  So if I went and tried to find a piece of content,
*  it would come back with all the metadata
*  that we had pre-computed.
*  How do you shove that question?
*  How do you connect the big stuff,
*  the big knowledge base with the metadata
*  and that's indexed to the simple little witty
*  confusing question?
*  Right.
*  So therein lies the Watson architecture, right?
*  So we would take the question,
*  we would analyze the question,
*  so which means that we would parse it
*  and interpret it a bunch of different ways.
*  We'd try to figure out what is it asking about,
*  so we had multiple strategies to kind of determine
*  what was it asking for.
*  That might be represented as a simple string,
*  a character string,
*  or something we would connect back
*  to different semantic types
*  that were from existing resources.
*  So anyway, the bottom line is we would do
*  a bunch of analysis in the question.
*  And question analysis had to finish,
*  it had to finish fast.
*  So we'd do the question analysis
*  because then from the question analysis,
*  we would now produce searches.
*  And we had built, using open source search engines,
*  we modified them.
*  We had a number of different search engines we would use
*  that had different characteristics.
*  We went in there and engineered
*  and modified those search engines,
*  ultimately to now take our question analysis,
*  produce multiple queries based on different interpretations
*  of the question,
*  and fire out a whole bunch of searches in parallel.
*  And they would come back with passages.
*  So these were passage search algorithms,
*  they would come back with passages.
*  And so now let's say you had a thousand passages.
*  Now for each passage, you parallelize again.
*  So you went out and you parallelized the search,
*  each search would now come back
*  with a whole bunch of passages.
*  Maybe you had a total of a thousand
*  or five thousand, whatever, passages.
*  For each passage now, you'd go and figure out
*  whether or not there was a candidate,
*  we'd call it candidate answer in there.
*  So you had a whole bunch of other algorithms
*  that would find candidate answers,
*  possible answers to the question.
*  And so you had candidate answer,
*  called candidate answer generators,
*  a whole bunch of those.
*  So for every one of these components,
*  the team was constantly doing research,
*  coming up better ways to generate search queries
*  from the questions, better ways to analyze the question,
*  better ways to generate candidates.
*  And speed, so better is accuracy and speed.
*  Correct, so right, speed and accuracy,
*  for the most part were separated.
*  We handled that sort of in separate ways.
*  Like I focus purely on accuracy and then accuracy,
*  are we ultimately getting more questions
*  and producing more accurate confidences?
*  And then a whole other team that was constantly
*  analyzing the workflow to find the bottlenecks,
*  and then figuring out how to both parallelize
*  and drive the algorithm speed.
*  But anyway, so now think of it like,
*  you have this big fan out now, right?
*  Because you had multiple queries,
*  now you have thousands of candidate answers.
*  For each candidate answer, you're gonna score it.
*  So you're gonna use all the data that built up.
*  You're gonna use the question analysis,
*  you're gonna use how the query was generated,
*  you're gonna use the passage itself,
*  and you're gonna use the candidate answer
*  that was generated, and you're gonna score that.
*  So now we have a group of researchers
*  coming up with scorers.
*  There are hundreds of different scorers.
*  So now you're getting a fan out again
*  from however many candidate answers you have
*  to all the different scorers.
*  So if you have 200 different scorers
*  and you have a thousand candidates,
*  now you have 200,000 scores.
*  And so now you gotta figure out,
*  how do I now rank these answers
*  based on the scores that came back?
*  And I wanna rank them based on the likelihood
*  that they're a correct answer to the question.
*  So every scorer was its own research project.
*  What do you mean by scorer?
*  So is that the annotation process
*  of basically a human being saying that this answer
*  has a quality of?
*  Think of it, if you wanna think of it,
*  what you're doing, if you wanna think about
*  what a human would be doing,
*  human would be looking at a possible answer.
*  They'd be reading the, Emily Dickinson,
*  they'd be reading the passage in which that occurred.
*  They'd be looking at the question,
*  and they'd be making a decision of how likely it is
*  that Emily Dickinson, given this evidence in this passage,
*  is the right answer to that question.
*  Got it.
*  So that's the annotation task.
*  That's the annotation process.
*  That's the scoring task.
*  But scoring implies zero to one continuous.
*  That's right, you give it a zero to one score.
*  So it's not a binary.
*  No, you give it a score.
*  Give it a zero to, yeah, exactly.
*  So it's like humans give different scores
*  so that you have to somehow normalize
*  and all that kind of stuff
*  that deal with all that complexity.
*  Depends on what your strategy is.
*  We both, we-
*  Could be relative to.
*  It could be.
*  We actually looked at the raw scores as well,
*  standardized scores,
*  because humans are not involved in this.
*  Humans are not involved.
*  Sorry, so I'm misunderstanding the process here.
*  There's these passages.
*  Where is the ground truth coming from?
*  Ground truth is only the answers to the questions.
*  So it's end to end.
*  It's end to end.
*  So we all, so I was always driving end to end performance.
*  It was a very interesting,
*  a very interesting engineering approach,
*  and ultimately scientific and research approach
*  were always driving end to end.
*  Now, that's not to say we wouldn't make hypotheses
*  that individual component performance
*  was related in some way to end to end performance.
*  Of course we would,
*  because people would have to build individual components.
*  But ultimately, to get your component
*  integrated into the system,
*  you had to show impact on end to end performance,
*  question answering performance.
*  There's many very smart people working on this,
*  and they're basically trying to sell their ideas
*  as a component that should be part of the system.
*  That's right.
*  And they would do research on their component,
*  and they would say things like,
*  I'm gonna improve this as a candidate generator,
*  or I'm gonna improve this as a question score,
*  or as a passage score,
*  I'm gonna improve this,
*  or as a parser,
*  and I can improve it by 2% on its component metric,
*  like a better parse, or a better candidate,
*  or a better type estimation, whatever it is.
*  And then I would say,
*  I need to understand how the improvement
*  on that component metric
*  is gonna affect the end to end performance.
*  If you can't estimate that,
*  and can't do experiments that demonstrate that,
*  it doesn't get in.
*  That's like the best run AI project I've ever heard.
*  That's awesome.
*  Okay, what breakthrough would you say,
*  like I'm sure there's a lot of day to day breakthroughs,
*  but was there like a breakthrough
*  that really helped improve performance?
*  Like where people began to believe?
*  Or is it just a gradual process?
*  Well, I think it was a gradual process,
*  but one of the things that I think gave people confidence
*  that we can get there was that,
*  as we follow this procedure of different ideas,
*  build different components,
*  plug them into the architecture,
*  run the system, see how we do,
*  do the error analysis,
*  start off new research projects to improve things.
*  And the very important idea that
*  the individual component work
*  did not have to deeply understand
*  everything that was going on with every other component.
*  And this is where we leverage machine learning
*  in a very important way.
*  So while individual components
*  could be statistically driven machine learning components,
*  some of them were heuristic,
*  some of them were machine learning components,
*  the system as a whole combined all the scores
*  using machine learning.
*  This was critical because that way you can divide and conquer.
*  So you can say, okay, you work on your candidate generator,
*  or you work on this approach to answer scoring,
*  you work on this approach to type scoring,
*  you work on this approach to passage search
*  or to passage selection and so forth.
*  But when you just plug it in
*  and we had enough training data to say,
*  now we can train and figure out
*  how do we weigh all the scores relative to each other
*  based on predicting the outcome,
*  which is right or wrong on Jeopardy.
*  And we had enough training data to do that.
*  So this enabled people to work independently
*  and to let the machine learning do the integration.
*  Beautiful, so yeah, the machine learning
*  is doing the fusion,
*  and then it's a human orchestrated ensemble
*  of different approaches.
*  That's great.
*  Still impressively, you were able to get it done
*  in a few years.
*  That's not obvious to me that it's doable
*  if I just put myself in that mindset.
*  But when you look back at the Jeopardy challenge,
*  again, when you're looking up at the stars,
*  what are you most proud of?
*  Just looking back at those days.
*  I'm most proud of my commitment
*  and my team's commitment to be true to the science,
*  to not be afraid to fail.
*  That's beautiful because there's so much pressure,
*  because it is a public event, it is a public show,
*  that you were dedicated to the idea.
*  That's right.
*  Do you think it was a success?
*  In the eyes of the world, it was a success.
*  By your, I'm sure, exceptionally high standards,
*  is there something you regret you would do differently?
*  It was a success.
*  It was a success for our goal.
*  Our goal was to build the most advanced
*  open domain question answering system.
*  We went back to the old problems
*  that we used to try to solve,
*  and we did dramatically better on all of them,
*  as well as we beat Jeopardy.
*  So we won at Jeopardy.
*  So it was a success.
*  I worry that the world would not understand it as a success
*  because it came down to only one game,
*  and I knew statistically speaking,
*  this can be a huge technical success,
*  and we could still lose that one game,
*  and that's a whole nother theme of the journey.
*  But it was a success.
*  It was not a success in natural language understanding,
*  but that was not the goal.
*  Yeah, that was, but I would argue,
*  I understand what you're saying in terms of the science,
*  but I would argue that the inspiration of it, right,
*  the, not a success in terms of solving
*  natural language understanding.
*  It was a success of being an inspiration
*  to future challenges.
*  Absolutely.
*  That drive future efforts.
*  What's the difference between how human being
*  compete in Jeopardy and how Watson does it
*  that's important in terms of intelligence?
*  Yeah, so that actually came up
*  very early on in the project also.
*  In fact, I had people who wanted to be on the project
*  who were early on who sort of approached me
*  once I committed to do it,
*  that wanted to think about how humans do it,
*  and they were, from a cognition perspective,
*  like human cognition and how that should play.
*  And I would not take them on the project
*  because another assumption or another stake
*  I put in the ground was,
*  I don't really care how humans do this.
*  At least in the context of this project.
*  I need to build, in the context of this project,
*  in NLU and in building an AI that understands how,
*  it needs to ultimately communicate with humans,
*  I very much care.
*  So it wasn't that I didn't care in general.
*  In fact, as an AI scientist, I care a lot about that.
*  But I'm also a practical engineer,
*  and I committed to getting this thing done.
*  And I wasn't gonna get distracted.
*  I had to kind of say, like, if I'm gonna get this done,
*  I'm gonna chart this path.
*  And if this path says, we're gonna engineer a machine
*  that's gonna get this thing done,
*  and we know what search and NLP can do,
*  we have to build on that foundation.
*  If I come in and take a different approach
*  and start wondering about how the human mind
*  might or might not do this,
*  I'm not gonna get there from here in the time frame.
*  I think that's a great way to lead the team.
*  But now that it's done, and then one, when you look back,
*  analyze what's the difference, actually, between.
*  Right, so I was a little bit surprised, actually,
*  to discover over time, as this would come up
*  from time to time, and we'd reflect on it,
*  and talking to Ken Jennings a little bit
*  and hearing Ken Jennings talk about how he answered questions,
*  that it might have been closer to the way humans
*  answer questions than I might have imagined previously.
*  Because humans are probably in the game of Jeopardy
*  at the level of Ken Jennings,
*  probably also cheating their way to winning, right?
*  Not cheating, but shallow.
*  They're doing the fastest possible.
*  They're doing shallow analysis.
*  So they are very quickly analyzing the question
*  and coming up with some key vectors or cues, if you will,
*  and they're taking those cues,
*  and they're very quickly going through
*  their library of stuff, not deeply reasoning
*  about what's going on, and then sort of,
*  lots of different, like what we call these scores,
*  would kind of score that in a very shallow way,
*  and then say, oh, boom, that's what it is.
*  And so it's interesting, as we reflected on that,
*  so we may be doing something that's not too far off
*  from the way humans do it,
*  but we certainly didn't approach it by saying,
*  how would a human do this?
*  Now, in elemental cognition, like the project I'm leading now,
*  we ask those questions all the time,
*  because ultimately, we're trying to do something
*  that is to make the intelligence of the machine
*  and the intelligence of the human very compatible.
*  Well, compatible in the sense
*  they can communicate with one another,
*  and they can reason with this shared understanding.
*  So how they think about things and how they build answers,
*  how they build explanations,
*  becomes a very important question to consider.
*  So what's the difference between this open domain,
*  but cold, constructed question answering of Jeopardy,
*  and more something that requires understanding
*  for shared communication with humans and machines?
*  Yeah, well, this goes back to the interpretation
*  of what we were talking about before.
*  Framework.
*  Jeopardy, the system's not trying to interpret the question,
*  and it's not interpreting the content that's reasoning,
*  with regard to any particular framework.
*  I mean, it is parsing it, and parsing the content,
*  and using grammatical cues and stuff like that.
*  So if you think of grammar as a human framework,
*  in some sense, it has that.
*  But when you get into the richer semantic frameworks,
*  what are people, how do they think, what motivates them,
*  what are the events that are occurring,
*  and why are they occurring,
*  and what causes what else to happen,
*  and where are things in time and space?
*  And like when you start thinking about how humans formulate
*  and structure the knowledge that they acquire in their head,
*  it wasn't doing any of that.
*  What do you think are the essential challenges
*  of free-flowing communication, free-flowing dialogue,
*  versus question answering, even with a framework,
*  with the interpretation, dialogue?
*  Yep.
*  Do you see free-flowing dialogue
*  as fundamentally more difficult than question answering,
*  even with shared interpretation?
*  So dialogue is important in a number of different ways.
*  So first of all, when I think about the machine that,
*  when I think about a machine that understands language
*  and ultimately can reason in an objective way,
*  that can take the information that it perceives
*  through language or other means
*  and connect it back to these frameworks,
*  reason and explain itself,
*  that system ultimately needs to be able to talk to humans,
*  or it needs to be able to interact with humans.
*  So in some sense, it needs to dialogue.
*  That doesn't mean that it,
*  sometimes people talk about dialogue and they think,
*  how do humans talk to each other in a casual conversation?
*  And you can mimic casual conversations.
*  We're not trying to mimic casual conversations.
*  We're really trying to produce a machine
*  whose goal is to help you think
*  and help you reason about your answers and explain why.
*  So instead of talking to your friend down the street
*  about having a small talk conversation
*  with your friend down the street,
*  this is more about you would be communicating
*  to the computer on Star Trek,
*  where what do you wanna think about?
*  What do you wanna reason about?
*  I'm gonna tell you the information I have,
*  I'm gonna have to summarize it,
*  I'm gonna ask you questions,
*  you're gonna answer those questions,
*  I'm gonna go back and forth with you,
*  I'm gonna figure out what your mental model is,
*  I'm gonna now relate that to the information I have
*  and present it to you in a way that you can understand it
*  and we can ask follow-up questions.
*  So it's that type of dialogue that you wanna construct.
*  It's more structured, it's more goal-oriented,
*  but it needs to be fluid.
*  It has to be engaging and fluid.
*  It has to be productive and not distracting.
*  So there has to be a model of,
*  in other words, the machine has to have a model
*  of how humans think through things and discuss them.
*  So basically a productive, rich conversation,
*  unlike this podcast.
*  I'd like to think it's more similar to this podcast.
*  I was just joking.
*  I'll ask you about humor as well, actually.
*  But what's the hardest part of that?
*  Because it seems we're quite far away
*  as a community from that still, to be able to,
*  so one is having a shared understanding.
*  That's, I think, a lot of the stuff you said
*  with frameworks is quite brilliant.
*  But just creating a smooth discourse.
*  It feels clunky right now.
*  Which aspects of this whole problem that you specified
*  of having a productive conversation is the hardest?
*  And that where, or maybe any aspect of it
*  you can comment on because it's so shrouded in mystery.
*  So I think to do this, you kind of have to be creative
*  in the following sense.
*  If I were to do this as purely a machine learning approach
*  and someone said, learn how to have a good,
*  fluent, structured knowledge acquisition conversation,
*  I'd go out and say, okay, I have to collect a bunch
*  of data of people doing that.
*  People reasoning well, having a good structured conversation
*  that both acquires knowledge efficiently
*  as well as produces answers and explanations
*  as part of the process.
*  And you struggle.
*  I don't know.
*  To collect the data.
*  To collect the data because I don't know
*  how much data is like that.
*  Okay, well, okay, this one, there's a humorous commenter
*  on the lack of rational discourse.
*  But also, even if it's out there, say it was out there,
*  how do you actually annotate, like,
*  how do you collect successful examples?
*  Right, so I think any problem like this
*  where you don't have enough data
*  to represent the phenomenon you want to learn,
*  in other words, you want, if you have enough data,
*  you could potentially learn the pattern.
*  In an example like this, it's hard to do.
*  This is sort of a human sort of thing to do.
*  What recently came out at IBM was the Debater Project,
*  sort of interesting, right?
*  Because now you do have these structured dialogues,
*  these debate things where they did use machine learning
*  techniques to generate these debates.
*  Dialogues are a little bit tougher, in my opinion,
*  than generating a structured argument
*  where you have lots of other structured arguments like this.
*  You could potentially annotate that data
*  and you could say this is a good response,
*  this is a bad response in a particular domain.
*  Here, I have to be responsive and I have to be opportunistic
*  with regard to what is the human saying.
*  So I'm goal-oriented in saying I want to solve the problem,
*  I want to acquire the knowledge necessary,
*  but I also have to be opportunistic and responsive
*  to what the human is saying.
*  So I think that it's not clear that we could just train
*  on the body of data to do this, but we could bootstrap it.
*  In other words, we can be creative and we could say,
*  what do we think, what do we think the structure
*  of a good dialogue is that does this well?
*  And we can start to create that.
*  If we can create that more programmatically,
*  at least to get this process started,
*  and I can create a tool that now engages humans effectively,
*  I could start both, I could start generating data,
*  I could start the human learning process
*  and I can update my machine,
*  but I could also start the automatic learning process
*  as well, but I have to understand
*  what features to even learn over.
*  So I have to bootstrap the process a little bit first.
*  And that's a creative design task
*  that I could then use as input
*  into a more automatic learning task.
*  Some creativity and yeah, and bootstrapping.
*  What elements of a conversation do you think
*  you would like to see?
*  So one of the benchmarks for me is humor, right?
*  That seems to be one of the hardest.
*  And to me, the biggest contrast is sort of Watson.
*  So one of the greatest sketches,
*  comedy sketches of all time, right,
*  is the SNL celebrity Jeopardy,
*  with Alex Trebek and Sean Connery
*  and Burt Reynolds and so on,
*  with Sean Connery commentating
*  on Alex Trebek's mother a lot.
*  So, and I think all of them are in the negative,
*  pointless wise.
*  So they're clearly all losing
*  in terms of the game of Jeopardy,
*  but they're winning in terms of comedy.
*  So what do you think about humor in this whole interaction
*  in the dialogue that's productive?
*  Or even just whatever, what humor represents to me is,
*  the same idea that you're saying about framework,
*  because humor only exists
*  within a particular human framework.
*  So what do you think about humor?
*  What do you think about things like humor
*  that connect to the kind of creativity
*  you mentioned that's needed?
*  I think there's a couple of things going on there.
*  So I sort of feel like,
*  and I might be too optimistic this way,
*  but I think that there are,
*  we did a little bit about with this,
*  with puns in Jeopardy.
*  We literally sat down and said,
*  how do puns work?
*  And it's like wordplay,
*  and you could formalize these things.
*  So I think there's a lot aspects of humor
*  that you could formalize.
*  You could also learn humor.
*  You could just say, what do people laugh at?
*  And if you have enough, again,
*  if you have enough data to represent the phenomenon,
*  you might be able to weigh the features
*  and figure out what humans find funny
*  and what they don't find funny.
*  The machine might not be able to explain
*  why the human is funny.
*  Why it's funny.
*  Unless we sit back and think about that more formally.
*  Again, I think you do a combination of both.
*  And I'm always a big proponent of that.
*  I think robust architectures and approaches
*  are always a little bit combination of us reflecting
*  and being creative about how things are structured,
*  how to formalize them,
*  and then taking advantage of large data
*  and doing learning and figuring out
*  how to combine these two approaches.
*  I think there's another aspect to humor though,
*  which goes to the idea that I feel like I can relate
*  to the person telling the story.
*  And I think that's an interesting theme
*  in the whole AI theme, which is,
*  do I feel differently when I know it's a robot?
*  And when I imagine that the robot is not conscious
*  the way I'm conscious,
*  when I imagine the robot does not actually
*  have the experiences that I experience,
*  do I find it funny?
*  Or do, because it's not as related,
*  but I don't imagine that the person's relating it to it
*  the way I relate to it.
*  I think this also, you see this in the arts
*  and in entertainment where sometimes you have savants
*  who are remarkable at a thing,
*  whether it's sculpture, it's music or whatever,
*  but the people who get the most attention
*  are the people who can evoke a similar emotional response
*  who can get you to emote, right, about the way they are.
*  In other words, who can basically make the connection
*  from the artifact, from the music
*  or the painting or the sculpture, to the emotion
*  and get you to share that emotion with them.
*  And that's when it becomes compelling.
*  So they're communicating at a whole different level.
*  They're just not communicating the artifact.
*  They're communicating their emotional response
*  to the artifact.
*  And then you feel like, oh wow,
*  I can relate to that person, I can connect to that person.
*  So I think humor has that aspect as well.
*  So the idea that you can connect to that person,
*  that person being the critical thing,
*  but we're also able to anthropomorphize objects pretty,
*  robots and AI systems pretty well.
*  So we're almost looking to make them human.
*  Maybe from your experience with Watson,
*  maybe you can comment on, did you consider that as part,
*  well, obviously the problem of jeopardy
*  doesn't require anthropomorphization, but nevertheless.
*  Well, there was some interest in doing that
*  and that's another thing I didn't wanna do
*  because I didn't wanna distract
*  from the actual scientific task.
*  But you're absolutely right.
*  I mean, humans do anthropomorphize
*  and without necessarily a lot of work,
*  I mean, just put some eyes in a couple of eyebrow movements
*  and you're getting humans to react emotionally.
*  And I think you can do that.
*  So I didn't mean to suggest that that connection
*  cannot be mimicked.
*  I think that connection can be mimicked
*  and can produce that emotional response.
*  I just wonder though, if you're told what's really going on,
*  if you know that the machine is not conscious,
*  not having the same richness of emotional reactions
*  and understanding that doesn't really share
*  the understanding, but it's essentially
*  just moving its eyebrow or drooping its eyes
*  or making them bigger, whatever it's doing,
*  this getting the emotional response,
*  will you still feel it?
*  Interesting, I think you probably would for a while.
*  And then when it becomes more important
*  that there's a deeper understanding,
*  it may run flat, but I don't know.
*  I'm not sure.
*  I'm pretty confident that majority of the world,
*  even if you tell them how it works.
*  It won't matter.
*  Well, it will not matter,
*  especially if the machine herself says
*  that she is conscious.
*  That's very possible.
*  So you, the scientist that made the machine is saying
*  that this is how the algorithm works.
*  Everybody will just assume you're lying
*  and that there's a conscious being there.
*  So you're deep into the science fiction genre now,
*  but yeah, I know.
*  I don't think it's, it's actually psychology.
*  I think it's not science fiction.
*  I think it's reality.
*  I think it's a really powerful one
*  that we'll have to be exploring in the next few decades.
*  Exactly.
*  It's a very interesting element of intelligence.
*  So what do you think, we've talked about social constructs
*  of intelligences and frameworks
*  and the way humans kind of interpret information.
*  What do you think is a good test of intelligence
*  in your view?
*  So there's the Alan Turing with the Turing test.
*  Watson accomplished something very impressive with Jeopardy.
*  What do you think is a test
*  that would impress the heck out of you
*  that you saw that a computer could do?
*  They would say this is crossing a kind of threshold
*  that gives me pause in a good way.
*  My expectations for AI are generally high.
*  What does high look like by the way?
*  So not the threshold, test is a threshold.
*  What do you think is the destination?
*  What do you think is the ceiling?
*  I think machines will, in many measures,
*  will be better than us, will become more effective.
*  In other words, better predictors about a lot of things
*  than ultimately we can do.
*  I think where they're gonna struggle
*  is what we talked about before,
*  which is relating to communicating with
*  and understanding humans in deeper ways.
*  And so I think that's a key point.
*  We can create the super parrot.
*  What I mean by the super parrot is, given enough data,
*  a machine can mimic your emotional response,
*  can even generate language that will sound smart
*  and what someone else might say under similar circumstances.
*  Like I would just pause on that.
*  Like that's the super parrot, right?
*  So given similar circumstances,
*  moves its faces in similar ways,
*  changes its tone of voice in similar ways,
*  produces strings of language that would similar
*  that a human might say,
*  not necessarily being able to produce
*  a logical interpretation or understanding
*  that would ultimately satisfy a critical interrogation
*  or a critical understanding.
*  I think you just described me in a nutshell.
*  So I think philosophically speaking,
*  you could argue that that's all we're doing
*  as human beings, to where superparrots.
*  I was gonna say, it's very possible,
*  humans do behave that way too.
*  And so upon deeper probing and deeper interrogation,
*  you may find out that there isn't a shared understanding
*  because I think humans do both.
*  Like humans are statistical language model machines
*  and they are capable reasoners.
*  You know, they're both.
*  And you don't know which is going on, right?
*  So, and I think it's an interesting problem.
*  We talked earlier about like where we are
*  in our social and political landscape.
*  Can you distinguish someone who can string
*  words together and sound like they know
*  what they're talking about from someone who actually does?
*  Can you do that without dialogue,
*  without interrogative or probing dialogue?
*  So it's interesting because humans are really good
*  in their own mind, justifying or explaining what they hear
*  because they project their understanding onto yours.
*  So you could say you could put together a string of words
*  and someone will sit there and interpret it
*  in a way that's extremely biased
*  to the way they wanna interpret it.
*  They wanna assume that you're an idiot
*  and they'll interpret it one way.
*  They will assume you're a genius
*  and they'll interpret it another way that suits their needs.
*  So this is tricky business.
*  So I think to answer your question,
*  as AI gets better and better, better and better mimic,
*  we create the super parrots,
*  we're challenged just as we are with,
*  we're challenged with humans.
*  Do you really know what you're talking about?
*  Do you have a meaningful interpretation,
*  a powerful framework that you could reason over
*  and justify your answers,
*  justify your predictions and your beliefs,
*  why you think they make sense?
*  Can you convince me what the implications are?
*  Can you, so can you reason intelligently
*  and make me believe that those,
*  the implications of your prediction and so forth?
*  So what happens is it becomes reflective.
*  My standard for judging your intelligence
*  depends a lot on mine.
*  But you're saying there should be a large group of people
*  with a certain standard of intelligence
*  that would be convinced by this particular AI system.
*  Then it would pass.
*  There should be, but I think one of the,
*  depending on the content,
*  one of the problems we have there
*  is that if that large community of people
*  are not judging it with regard to a rigorous standard
*  of objective logic and reason, you still have a problem.
*  Masses of people can be persuaded.
*  The millennials, yeah.
*  To turn their brains off.
*  Right, okay.
*  Sorry.
*  By the way, I have nothing against the money.
*  No, I don't, I'm just,
*  so you're a part of one of the great benchmarks,
*  challenges of AI history.
*  What do you think about AlphaZero,
*  OpenAI 5, AlphaStar accomplishments on video games recently,
*  which are also, I think, at least in the case of Go,
*  with AlphaGo and AlphaZero playing Go
*  was a monumental accomplishment as well.
*  What are your thoughts about that challenge?
*  I think it was a giant landmark for AI.
*  I think it was phenomenal.
*  I mean, as one of those other things
*  nobody thought like solving Go was gonna be easy,
*  particularly because it's, again,
*  it's hard for, particularly hard for humans,
*  hard for humans to learn, hard for humans to excel at.
*  And so it was another measure of intelligence.
*  It's very cool.
*  I mean, it's very interesting what they did.
*  And I loved how they solved the data problem,
*  which again, they bootstrapped it
*  and got the machine to play itself
*  to generate enough data to learn from.
*  I think that was brilliant.
*  I think that was great.
*  And of course, the result speaks for itself.
*  I think it makes us think about,
*  again, it is, okay, what's intelligence?
*  What aspects of intelligence are important?
*  Can the Go machine help me make me a better Go player?
*  Is it an alien intelligence?
*  Am I even capable of, like again,
*  if we put in very simple terms, it found the function.
*  It found the Go function.
*  Can I even comprehend the Go function?
*  Can I talk about the Go function?
*  Can I conceptualize the Go function
*  like whatever it might be?
*  So one of the interesting ideas of that system
*  is that it plays against itself, right?
*  But there's no human in the loop there.
*  So like you're saying, it could have by itself
*  created an alien intelligence.
*  How?
*  Toward a goal, imagine you're sentencing,
*  you're judging, you're sentencing people
*  or you're setting policy or you're making medical decisions.
*  And you can't explain, you can't get anybody
*  to understand what you're doing or why.
*  So it's an interesting dilemma for the applications of AI.
*  Do we hold AI to this accountability that says,
*  humans have to be able to take responsibility
*  for the decision?
*  In other words, can you explain why you would do the thing?
*  Will you get up and speak to other humans
*  and convince them that this was a smart decision?
*  Is the AI enabling you to do that?
*  Can you get behind the logic that was made there?
*  Do you think, sorry to link on this point
*  because it's a fascinating one, it's a great goal for AI.
*  Do you think it's achievable in many cases?
*  Or okay, there's two possible worlds
*  that we have in the future.
*  One is where AI systems do like medical diagnosis
*  or things like that or drive a car
*  without ever explaining to you why it fails when it does.
*  That's one possible world and we're okay with it.
*  Or the other where we are not okay with it
*  and we really hold back the technology
*  from getting too good before it's able to explain.
*  Which of those worlds are more likely, do you think,
*  and which are concerning to you or not?
*  I think the reality is it's gonna be a mix.
*  I'm not sure I have a problem with that.
*  I think there are tasks that are perfectly fine
*  with machines show a certain level of performance
*  and that level of performance is already better
*  than humans.
*  So for example, I don't know that I take driverless cars.
*  If driverless cars learn how to be more effective drivers
*  than humans but can't explain what they're doing,
*  but bottom line, statistically speaking,
*  they're 10 times safer than humans,
*  I don't know that I care.
*  I think when we have these edge cases,
*  when something bad happens and we wanna decide
*  who's liable for that thing and who made that mistake
*  and what do we do about that?
*  And I think those edge cases are interesting cases.
*  And now do we go to designers of the AI
*  and the AI says, I don't know, that's what it learned to do
*  and it says, well, you didn't train it properly.
*  You were negligent in the training data
*  that you gave that machine.
*  Like how do we drive down the real life?
*  So I think those are interesting questions.
*  So the optimization problem there, sorry,
*  is to create an ad system that's able to explain
*  the lawyers away.
*  There you go.
*  I think it's gonna be interesting.
*  I mean, I think this is where technology
*  and social discourse are gonna get deeply intertwined
*  and how we start thinking about problems,
*  decisions and problems like that.
*  I think in other cases, it becomes more obvious where
*  why did you decide to give that person a longer sentence
*  or deny them parole?
*  Again, policy decisions or why did you pick that treatment?
*  Like that treatment ended up killing that guy.
*  Like why was that a reasonable choice to make?
*  And people are gonna demand explanations.
*  Now there's a reality though here.
*  And the reality is that it's not,
*  I'm not sure humans are making reasonable choices
*  when they do these things.
*  They are using statistical hunches, biases
*  or even systematically using statistical averages
*  to make calls.
*  I mean, this is what happened to my dad
*  and if you saw the talk I gave about that.
*  But they decided that my father was brain dead.
*  He had went into cardiac arrest
*  and it took a long time for the ambulance to get there
*  and he was not resuscitated right away and so forth.
*  And they came and they told me he was brain dead
*  and why was he brain dead?
*  Because essentially they gave me
*  a purely statistical argument.
*  Under these conditions with these four features,
*  98% chance he's brain dead.
*  I said, but can you just tell me,
*  not inductively but deductively,
*  go there and tell me his brain's not functioning
*  is the way for you to do that.
*  And the protocol in response was,
*  no, this is how we make this decision.
*  I said, this is inadequate for me.
*  I understand the statistics and I don't know how,
*  there's a 2% chance he's still alive.
*  Like I just don't know the specifics.
*  I need the specifics of this case
*  and I want the deductive logical argument
*  about why you actually know he's brain dead.
*  So I wouldn't sign that do not resuscitate.
*  And I don't know, it was like they went through
*  lots of procedures, it was a big long story.
*  But the bottom, fascinating story by the way,
*  but how I reasoned and how the doctors reasoned
*  through this whole process.
*  But I don't know, somewhere around 24 hours later
*  or something he was sitting up in bed
*  with zero brain damage.
*  I mean what lessons do you draw from that story,
*  that experience?
*  That the data that's being used
*  to make statistical inferences
*  doesn't adequately reflect the phenomenon.
*  So in other words, you're getting shit wrong,
*  I'm sorry, you're getting stuff wrong
*  because your model is not robust enough
*  and you might be better off not using
*  statistical inference and statistical averages
*  in certain cases when you know the model's insufficient
*  and that you should be reasoning about the specific case
*  more logically and more deductively.
*  And hold yourself responsible,
*  hold yourself accountable to doing that.
*  And perhaps AI has a role to say the exact thing
*  we just said, which is perhaps this is a case
*  you should think for yourself.
*  You should reason deductively.
*  So it's hard because it's hard to know that.
*  You know, you'd have to go back
*  and you'd have to have enough data to essentially say,
*  and this goes back to how do we,
*  this goes back to the case of how do we decide
*  whether the AI is good enough to do a particular task?
*  And regardless of whether or not it produces an explanation.
*  So, and what standard do we hold, right, for that?
*  So, you know, if you look at,
*  you look more broadly, for example,
*  my father as a medical case,
*  the medical system ultimately helped him a lot
*  throughout his life.
*  Without it, he probably would have died much sooner.
*  So overall, it sort of, you know, worked for him
*  in sort of a net-net kind of way.
*  Actually, I don't know that that's fair.
*  But maybe not in that particular case, but overall,
*  like the medical system overall does more good than bad.
*  Yeah, the medical system overall, you know,
*  was doing more good than bad.
*  Now, there's another argument that suggests
*  that that wasn't the case, but for the sake of argument,
*  let's say like that's, let's say a net positive.
*  And I think you have to sit there and there
*  and take that into consideration.
*  Now you look at a particular use case,
*  like for example, making this decision.
*  Have you done enough studies to know
*  how good that prediction really is?
*  Right.
*  And have you done enough studies to compare it
*  to say, well, what if we dug in in a more direct,
*  you know, let's get the evidence,
*  let's do the deductive thing and not use statistics here,
*  how often would that have done better?
*  Right, so you have to do the studies
*  to know how good the AI actually is.
*  And it's complicated because it depends
*  how fast you have to make the decision.
*  So if you have to make the decision super fast,
*  you have no choice.
*  Right.
*  If you have more time, right,
*  but if you're ready to pull the plug,
*  and this is a lot of the argument that I had with the doctor,
*  I said, what's he gonna do if you do it my way?
*  What's gonna happen to him in that room if you do it my way?
*  Well, he's gonna die anyway, so let's do it my way then.
*  I mean, it raises questions for our society
*  to struggle with, as is the case with your father,
*  but also when things like race and gender
*  start coming into play, when certain,
*  when judgments are made based on things
*  that are complicated in our society,
*  at least in the discourse, and it starts, you know,
*  I think I'm safe to say that most of the violent crimes
*  are committed by males.
*  So if you discriminate based, you know,
*  it's male versus female saying that if it's a male,
*  more likely to commit the crime.
*  So this is one of my very positive and optimistic views
*  of why the study of artificial intelligence,
*  the process of thinking and reasoning logically
*  and statistically, and how to combine them,
*  is so important for the discourse today,
*  because it's causing a, regardless of what,
*  what state AI devices are or not,
*  it's causing this dialogue to happen.
*  This is one of the most important dialogues that,
*  in my view, the human species can have right now,
*  which is how to think well,
*  how to reason well, how to understand our own
*  cognitive biases and what to do about them.
*  That has gotta be one of the most important things
*  that we as a species can be doing, honestly.
*  We've created an incredibly complex society.
*  We've created amazing abilities to amplify noise
*  faster than we can amplify signal.
*  We are challenged.
*  We are deeply, deeply challenged.
*  We have, you know, big segments of the population
*  getting hit with enormous amounts of information.
*  Do they know how to do critical thinking?
*  Do they know how to objectively reason?
*  Do they understand what they are doing,
*  nevermind what their AI is doing?
*  This is such an important dialogue to be having.
*  And, you know, we are fundamentally,
*  our thinking can be and easily becomes fundamentally biased.
*  And there are statistics, and we shouldn't blind ourselves,
*  we shouldn't discard statistical inference,
*  but we should understand the nature of statistical inference.
*  As a society, as, you know,
*  we decide to reject statistical inference
*  to favor understanding and deciding on the individual.
*  Yes.
*  We consciously make that choice.
*  So even if the statistics said,
*  even if the statistics said,
*  males are more likely to be violent criminals,
*  we still take each person as an individual,
*  and we treat them based on the logic
*  and the knowledge of that situation,
*  we purposefully and intentionally
*  reject the statistical inference.
*  We do that out of respect for the individual.
*  For the individual, yeah,
*  and that requires reasoning and thinking.
*  Looking forward, what grand challenges
*  would you like to see in the future?
*  Because the Jeopardy challenge, you know,
*  captivated the world.
*  AlphaGo, AlphaZero, captivated the world.
*  Deep Blue, certainly beating Kasparov.
*  Gary's bitterness aside, captivated the world.
*  What do you think, do you have ideas
*  for next grand challenges,
*  for future challenges of that ilk?
*  You know, look, I mean, I think there are lots
*  of really great ideas for grand challenges.
*  I'm particularly focused on one right now,
*  which is, can you demonstrate that they understand,
*  that they could read and understand,
*  that they can acquire these frameworks
*  and communicate, you know, reason and communicate
*  with humans.
*  So it is kind of like the Turing test,
*  but it's a little bit more demanding than a Turing test.
*  It's not enough to convince me that you might be human
*  because you can parrot a conversation.
*  I think, you know, the standard is a little bit higher,
*  is for example, can you, you know, the standard is higher.
*  And I think one of the challenges
*  of devising this grand challenge is that we're not sure
*  what intelligence is.
*  We're not sure how to determine whether or not
*  two people actually understand each other
*  and in what depth they understand it.
*  They, you know, in what, to what depth
*  they understand each other.
*  So the challenge becomes something along the lines of,
*  can you satisfy me that we have a shared understanding?
*  So if I were to probe and probe and you probe me,
*  can machines really act like thought partners
*  where they can satisfy me that they,
*  that we have a shared, our understanding is shared enough
*  that we can collaborate and produce answers together
*  and that they can help me explain
*  and justify those answers.
*  So maybe here's an idea.
*  So we'll have AI system run for president
*  and convince- That's too easy.
*  I'm sorry, go ahead.
*  Well, no, you have to convince the voters
*  that they should vote.
*  So like, I guess what does winning look like?
*  Again, that's why I think this is such a challenge
*  because we go back to the emotional persuasion.
*  We go back to, you know, now we're checking off an aspect
*  of human cognition that is in many ways weak or flawed,
*  right, we're so easily manipulated.
*  Our minds are drawn for often the wrong reasons, right?
*  Not the reasons that ultimately mattered to us,
*  but the reasons that can easily persuade us.
*  I think we can be persuaded to believe one thing or another
*  for reasons that ultimately don't serve us well
*  in the longterm.
*  And a good benchmark should not play with those elements
*  of emotional manipulation.
*  I don't think so.
*  And I think that's where we have to set the higher standard
*  for ourselves of what, you know, what does it mean?
*  This goes back to rationality
*  and it goes back to objective thinking.
*  And can you produce, can you acquire information
*  and produce reasoned arguments?
*  And to those reasons, arguments pass a certain amount
*  of time in the master.
*  And is it, and can you acquire new knowledge?
*  You know, can you, can you, for example,
*  can you reasonable, I have acquired new knowledge,
*  can you identify where it's consistent or contradictory
*  with other things you've learned?
*  And can you explain that to me
*  and get me to understand that?
*  So I think another way to think about it perhaps
*  is can a machine teach you?
*  Can it help you?
*  Oh, that's a really nice, nice way to put it.
*  Can it help you understand?
*  Can it help you understand something
*  that you didn't really understand before?
*  Oh, that's a beautiful way to put it.
*  Where it's, you know, it's taking you,
*  so you're not, you know, again, it's almost like,
*  can it teach you?
*  Can it help you learn?
*  And in an arbitrary space,
*  so it can open those domain spaces.
*  So can you tell the machine,
*  and again, this borrows from some science fiction,
*  so it's like, can you tell the machine,
*  can you tell the machine,
*  borrows from some science fiction,
*  but can you go off and learn about this topic
*  that I'd like to understand better?
*  And then work with me to help me understand it.
*  That's quite brilliant.
*  Well, the machine that passes that kind of test,
*  do you think it would need to have self-awareness
*  or even consciousness?
*  What do you think about consciousness
*  and the importance of it,
*  maybe in relation to having a body,
*  having a presence, an entity?
*  Do you think that's important?
*  You know, people used to ask me if Watson was conscious,
*  and I used to think,
*  and I used to think, he's conscious of what, exactly?
*  I mean, I think, you know,
*  maybe it depends what it is that you're conscious of.
*  I mean, like, so, you know, did it, if you, you know,
*  it's certainly easy for it to answer questions about,
*  it would be trivial to program it,
*  to answer questions about whether or not
*  it was playing Jeopardy.
*  I mean, it could certainly answer questions
*  that would imply that it was aware of things.
*  Exactly, what does it mean to be aware
*  and what does it mean to be conscious of it?
*  It's sort of interesting.
*  I mean, I think that we differ from one another
*  based on what we're conscious of.
*  But wait, wait a minute, yes, for sure.
*  There's degrees of consciousness and there's so,
*  in terms of- Well, and there's just areas.
*  Like, it's not just degrees.
*  It's like, what are you aware of?
*  Like, what are you not aware of?
*  But nevertheless, there's a very subjective element
*  to our experience.
*  Let me even not talk about consciousness.
*  Let me talk about another, to me,
*  really interesting topic of mortality, fear of mortality.
*  Watson, as far as I could tell,
*  did not have a fear of death.
*  Certainly not.
*  Most humans do.
*  Wasn't conscious of death.
*  It wasn't, yeah.
*  So there's an element of finiteness to our existence
*  that I think, like you mentioned, survival,
*  that adds to the whole thing.
*  I mean, consciousness is tied up with that,
*  that we are a thing.
*  It's a subjective thing that ends.
*  And that seems to add a color and flavor to our motivations
*  in a way that seems to be fundamentally important
*  for intelligence, or at least the kind of human intelligence.
*  Well, I think for generating goals.
*  Again, I think you could have
*  you could have an intelligence capability
*  and a capability to learn, a capability to predict.
*  But I think without,
*  I mean, again, you get a fear,
*  but essentially without the goal to survive.
*  So you think you can just encode that
*  without having to really-
*  I think you can encode that.
*  I mean, you can create a robot now,
*  and you could say, you know,
*  plug it in and say, protect your power source,
*  you know, and give it some capabilities,
*  and it'll sit there and operate
*  to try to protect its power source and survive.
*  I mean, so I don't know that that's philosophically
*  a hard thing to demonstrate.
*  It sounds like a fairly easy thing to demonstrate
*  that you can give it that goal.
*  Will it come up with that goal by itself?
*  I think you have to program that goal in.
*  But there's something, because I think,
*  as we touched on, intelligence is kind of
*  like a social construct.
*  The fact that a robot will be protecting its power source
*  would add depth and grounding to its intelligence
*  in terms of us being able to respect it.
*  I mean, ultimately, it boils down to us
*  acknowledging that it's intelligent.
*  And the fact that it can die,
*  I think, is an important part of that.
*  The interesting thing to reflect on
*  is how trivial that would be.
*  And I don't think if you knew how trivial that was,
*  you would associate that with being intelligence.
*  I mean, I literally put in a statement of code
*  that says you have the following actions you can take.
*  You give it a bunch of actions.
*  Maybe you mount a laser gun on it,
*  or you give it the ability to scream or screech or whatever.
*  And you say if you see your power source threatened
*  and you could program that in,
*  and you're gonna take these actions to protect it.
*  You could teach it, train it on a bunch of things.
*  And now you're gonna look at that and you say,
*  well, that's intelligence
*  because it's protecting its power source.
*  Maybe, but that's again this human bias that says
*  the thing I identify, my intelligence and my conscious
*  so fundamentally with the desire,
*  or at least the behaviors associated
*  with the desire to survive,
*  that if I see another thing doing that,
*  I'm going to assume it's intelligent.
*  What timeline year will society have something
*  that you would be comfortable calling
*  an artificial general intelligence system?
*  What's your intuition?
*  Nobody can predict the future,
*  certainly not the next few months or 20 years away,
*  but what's your intuition?
*  How far away are we?
*  It's hard to make these predictions.
*  I mean, I would be guessing.
*  And there's so many different variables,
*  including just how much we want to invest in it
*  and how important we think it is,
*  what kind of investment we're willing to make in it,
*  what kind of talent we end up bringing to the table,
*  the incentive structure, all these things.
*  So I think it is possible to do this sort of thing.
*  I think it's, I think trying to sort of
*  ignore many of the variables and things like that.
*  Is it a 10 year thing?
*  Is it a 23 year?
*  Probably closer to a 20 year thing, I guess.
*  But not several hundred years.
*  No, I don't think it's several hundred years.
*  I don't think it's several hundred years.
*  But again, so much depends on how committed we are
*  to investing and incentivizing this type of work.
*  And it's sort of interesting.
*  Like I don't think it's obvious
*  how incentivized we are.
*  I think from a task perspective,
*  if we see business opportunities
*  to take this technique or that technique
*  to solve that problem, I think that's the main driver
*  for many of these things.
*  From a general intelligence,
*  it's kind of an interesting question.
*  Are we really motivated to do that?
*  And like we just struggled ourselves right now
*  to even define what it is.
*  So it's hard to incentivize
*  when we don't even know what it is
*  we're incentivized to create.
*  And if you said mimic a human intelligence,
*  I just think there are so many challenges
*  with the significance and meaning of that
*  that there's not a clear directive.
*  There's no clear directive to do precisely that thing.
*  So assistance in larger and larger number of tasks.
*  So being able to, a system that's particularly able
*  to operate by microwave and making a grilled cheese sandwich.
*  I don't even know how to make one of those.
*  And then the same system would be doing the vacuum cleaning
*  and then the same system would be teaching
*  my kids that I don't have math.
*  I think that when you get into a general intelligence
*  for learning physical tasks,
*  and again, I wanna go back to your body questions.
*  I think your body question was interesting,
*  but you wanna go back to learning the abilities
*  to physical tasks.
*  You might have, we might get,
*  I imagine in that timeframe,
*  we will get better and better
*  at learning these kinds of tasks,
*  whether it's mowing your lawn or driving your car
*  or whatever it is.
*  I think we will get better and better at that
*  where it's learning how to make predictions
*  over large bodies of data.
*  I think we're gonna continue
*  to get better and better at that.
*  And machines will outpace humans
*  in a variety of those things.
*  The underlying mechanisms for doing that may be the same,
*  meaning that maybe these are deep nets,
*  there's infrastructure to train them,
*  reusable components to get them to do different classes
*  of tasks, and we get better and better
*  at building these kinds of machines.
*  You could argue that the general learning infrastructure
*  in there is a form of a general type of intelligence.
*  I think what starts getting harder is this notion of,
*  can we effectively communicate and understand
*  and build that shared understanding
*  because of the layers of interpretation
*  that are required to do that,
*  and the need for the machine to be engaged with humans
*  at that level in a continuous basis.
*  So how do you get the machine in the game?
*  How do you get the machine in the intellectual game?
*  Yeah, and to solve AGI,
*  you probably have to solve that problem.
*  You have to get the machine,
*  so it's a little bit of a bootstrap.
*  Can we get the machine engaged in the intellectual,
*  calling it a game, but in the intellectual dialogue
*  with the humans?
*  Are the humans sufficiently in intellectual dialogue
*  with each other to generate enough data in this context?
*  And how do you bootstrap that?
*  Because every one of those conversations,
*  every one of those conversations,
*  those intelligent interactions require so much prior knowledge
*  that it's a challenge to bootstrap it.
*  So the question is, and how committed,
*  so I think that's possible, but when I go back to,
*  are we incentivized to do that?
*  I know we're incentivized to do the former.
*  Are we incentivized to do the latter significantly enough?
*  Do people understand what the latter really is well enough?
*  Part of the elemental cognition mission
*  is to try to articulate that better and better
*  through demonstrations and through trying to craft
*  these grand challenges and get people to say,
*  look, this is a class of intelligence.
*  This is a class of AI.
*  Do we want this?
*  What is the potential of this?
*  What's the business potential?
*  What's the societal potential to that?
*  And to build up that incentive system around that.
*  Yeah, I think if people don't understand yet,
*  I think they will.
*  I think there's a huge business potential here.
*  So it's exciting that you're working on it.
*  We kind of skipped over it,
*  but I'm a huge fan of physical presence of things.
*  Do you think Watson had a body?
*  Do you think having a body adds to the interactive element
*  between the AI system and a human
*  or just in general to intelligence?
*  So I think going back to that shared understanding,
*  humans are very connected to their bodies.
*  I mean, one of the reasons, one of the challenges
*  in getting an AI to kind of be a compatible
*  human intelligence is that our physical bodies
*  are generating a lot of features that make up the input.
*  So in other words, where our bodies are,
*  are the tool we use to affect output,
*  but they also generate a lot of input for our brains.
*  So we generate emotion, we generate all these feelings,
*  we generate all these signals that machines don't have.
*  So machines don't have this as the input data.
*  And they don't have the feedback that says,
*  okay, I've gotten this emotion or I've gotten this idea.
*  I now want to process it and then I can,
*  it then affects me as a physical being
*  and then I can play that out.
*  In other words, I could realize the implications of that,
*  the implications again on my mind-body complex.
*  I then process that and the implications again,
*  our internal features are generated.
*  I learn from them, they have an effect
*  on my mind-body complex.
*  So it's interesting when we think,
*  do we want a human intelligence?
*  Well, if we want a human compatible intelligence,
*  probably the best thing to do is to have
*  embedded in a human body.
*  Just to clarify, and both concepts are beautiful,
*  is humanoid robots, so robots that look like humans is one,
*  or did you mean actually sort of what Elon Musk
*  is working with Neuralink,
*  really embedding intelligence systems
*  to ride along human bodies?
*  No, I mean riding along is different.
*  I meant like if you want to create an intelligence
*  that is human compatible,
*  meaning that it can learn and develop
*  a shared understanding of the world around it,
*  you have to give it a lot of the same substrate.
*  Part of that substrate is the idea that it generates
*  these kinds of internal features,
*  like sort of emotional stuff, it has similar senses,
*  it has to do a lot of the same things with those same senses.
*  So I think if you want that, again,
*  I don't know that you want that.
*  That's not my specific goal.
*  I think that's a fascinating scientific goal.
*  I think it has all kinds of other implications.
*  That's sort of not the goal.
*  I think of it as I create intellectual thought partners
*  for humans, that kind of intelligence.
*  I know there are other companies that are creating
*  physical thought partners,
*  physical partners for humans,
*  but that's kind of not where I'm at.
*  But the important point is that a big part of what we process
*  is that physical experience of the world around us.
*  On the point of thought partners,
*  what role does an emotional connection,
*  or forgive me, love, have to play in that thought partnership?
*  Is that something you're interested in,
*  put another way, sort of having a deep connection
*  beyond intellectual?
*  With the AI?
*  Yeah, with the AI, between human and AI.
*  Is that something that gets in the way of the rational discourse?
*  Is that something that's useful?
*  I worry about biases, obviously.
*  So in other words, if you develop an emotional relationship
*  with a machine, all of a sudden you start,
*  are more likely to believe what it's saying,
*  even if it doesn't make any sense.
*  So I worry about that.
*  But at the same time, I think the opportunity to use machines
*  to provide human companionship is actually not crazy.
*  And intellectual and social companionship is not a crazy idea.
*  Do you have concerns, as a few people do,
*  Elon Musk, Sam Harris, about long-term existential threats of AI,
*  and perhaps short-term threats of AI?
*  We talked about bias, we talked about different misuses,
*  but do you have concerns about thought partners,
*  systems that are able to help us make decisions together with humans,
*  somehow having a significant negative impact on society in the long term?
*  I think there are things to worry about.
*  I think giving machines too much leverage is a problem.
*  And what I mean by leverage is too much control over things that can hurt us.
*  Whether it's socially, psychologically, intellectually, or physically.
*  And if you give the machines too much control, I think that's a concern.
*  Forget about the AI.
*  Just once you give them too much control, human bad actors can hack them
*  and produce havoc.
*  So that's a problem.
*  And you can imagine hackers taking over the driverless car network
*  and creating all kinds of havoc.
*  But you could also imagine, given the ease at which humans could be persuaded
*  one way or the other, and now we have algorithms that can easily take control
*  over that and amplify noise and move people one direction or another.
*  I mean, humans do that to other humans all the time.
*  And we have marketing campaigns, we have political campaigns
*  that take advantage of our emotions or our fears.
*  And this is done all the time.
*  But with machines, machines are like giant megaphones, right?
*  We can amplify this in orders of magnitude and fine tune its control.
*  So we can tailor the message.
*  We can now very rapidly and efficiently tailor the message to the audience
*  taking advantage of their biases and amplifying them and using them
*  to persuade them in one direction or another in ways that are not fair,
*  not logical.
*  Not objective, not meaningful.
*  And machines empower that.
*  So that's what I mean by leverage.
*  It's not new, but wow, it's powerful because machines can do it more effectively,
*  more quickly, and we see that already going on in social media and other places.
*  That's scary.
*  And that's why I'm, I'm, I'm not going to be able to do that.
*  That's why I go back to saying one of the most important public dialogues
*  we could be having is about the nature of intelligence
*  and the nature of inference and logic and reason and rationality
*  and us understanding our own biases, us understanding our own cognitive biases
*  and how they work and then how machines work
*  and how do we use them to complement it basically so that in the end
*  we have a stronger overall system.
*  That's just incredibly important.
*  I don't think most people understand that.
*  So like telling your kids or telling your students,
*  this goes back to the cognition.
*  Here's how your brain works.
*  Here's how easy it is to trick your brain.
*  There are fundamental cognitive, you should appreciate
*  the different types of thinking and how they work
*  and what you're prone to and what do you prefer
*  and under what conditions does this make sense versus that makes sense.
*  And then say, here's what AI can do.
*  Here's how it can make this worse and here's how it can make this better.
*  And that's where the AI has a role is to reveal that trade-off.
*  So if you imagine a system that is able to beyond any definition
*  of the Turing test, the benchmark, really an AGI system as a thought partner
*  that you one day will create, what question, what topic of discussion
*  if you get to pick one, would you have with that system?
*  What would you ask and you get to find out the truth together?
*  So you threw me a little bit with finding the truth at the end,
*  but because the truth is a whole other topic.
*  But I think the beauty of it, I think what excites me is the beauty of it is
*  if I really have that system, I don't have to pick.
*  So in other words, I can go to and say, this is what I want to do.
*  I can say, this is what I care about today.
*  And that's what we mean by it, like this general capability.
*  Go out, read this stuff in the next three milliseconds,
*  and I want to talk to you about it.
*  I want to draw analogies.
*  I want to understand how this affects this decision or that decision.
*  What if this were true? What if that were true?
*  What knowledge should I be aware of that could impact my decision?
*  Here's what I'm thinking is the main implication.
*  Can you prove that out? Can you give me the evidence that supports that?
*  Can you give me evidence that supports this other thing?
*  Boy, would that be incredible. Would that be just incredible?
*  Just a long discourse.
*  Just to be part of whether it's a medical diagnosis
*  or whether it's the various treatment options or whether it's a legal case
*  or whether it's a social problem that people are discussing.
*  Be part of the dialogue, one that holds itself and us accountable
*  to reasons and objective dialogue.
*  I get goosebumps talking about it.
*  It's like, this is what I want.
*  So when you create it, please come back on the podcast
*  and we can have a discussion together and make it even longer.
*  This is a record for the longest conversation ever.
*  It was an honor. It was a pleasure, David.
*  Thank you so much for that.
*  Thanks so much. A lot of fun.