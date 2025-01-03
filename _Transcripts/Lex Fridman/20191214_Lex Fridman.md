---
Date Generated: November 01, 2024
Transcription Model: whisper medium 20231117
Length: 6357s
Video Keywords: []
Video Views: 57240
Video Rating: None
Video Description: 
---

# Rohit Prasad Amazon Alexa and Conversational AI  Lex Fridman Podcast #57
**Lex Fridman:** [December 14, 2019](https://www.youtube.com/watch?v=Ad89JYS-uZM)
*  The following is a conversation with Rohit Prasad.
*  He's the vice president and head scientist of Amazon Alexa
*  and one of its original creators.
*  The Alexa team embodies some of the most challenging,
*  incredible, impactful and inspiring work
*  that is done in AI today.
*  The team has to both solve problems
*  at the cutting edge of natural language processing
*  and provide a trustworthy, secure and enjoyable experience
*  to millions of people.
*  This is where state of the art methods
*  in computer science meet the challenges
*  of real world engineering.
*  In many ways, Alexa and the other voice assistants
*  are the voices of artificial intelligence
*  to millions of people and an introduction to AI
*  for people who have only encountered it in science fiction.
*  This is an important and exciting opportunity.
*  So the work that Rohit and the Alexa team are doing
*  is an inspiration to me and to many researchers
*  and engineers in the AI community.
*  This is the artificial intelligence podcast.
*  If you enjoy it, subscribe on YouTube,
*  give five stars on Apple podcast,
*  support it on Patreon or simply connect with me on Twitter,
*  Alex Friedman, spelled F-R-I-D-M-A-N.
*  If you leave a review on Apple podcast especially,
*  but also cast box or comment on YouTube,
*  consider mentioning topics, people, ideas, questions,
*  quotes and science, tech or philosophy
*  that you find interesting
*  and I'll read them on this podcast.
*  I won't call out names, but I love comments
*  with kindness and thoughtfulness in them,
*  so I thought I'd share them.
*  Someone on YouTube highlighted a quote
*  from the conversation with Ray Dalio,
*  where he said that you have to appreciate
*  all the different ways that people can be AI players.
*  This connected with me too.
*  On teams of engineers, it's easy to think
*  that raw productivity is the measure of excellence,
*  but there are others.
*  I've worked with people who brought a smile to my face
*  every time I got to work in the morning.
*  Their contribution to the team is immeasurable.
*  I recently started doing podcast ads
*  at the end of the introduction.
*  I'll do one or two minutes after introducing the episode
*  and never any ads in the middle
*  that break the flow of the conversation.
*  I hope that works for you.
*  It doesn't hurt the listening experience.
*  This show is presented by Cash App,
*  the number one finance app in the app store.
*  I personally use Cash App to send money to friends,
*  but you can also use it to buy, sell
*  and deposit Bitcoin in just seconds.
*  Cash App also has a new investing feature.
*  You can buy fractions of a stock, say $1 worth,
*  no matter what the stock price is.
*  Brokerage services are provided by Cash App Investing,
*  a subsidiary of Square and member SIPC.
*  I'm excited to be working with Cash App
*  to support one of my favorite organizations called FIRST,
*  best known for their FIRST Robotics and Lego competitions.
*  They educate and inspire hundreds of thousands of students
*  in over 110 countries
*  and have a perfect rating on Charity Navigator,
*  which means that donated money is used
*  to maximum effectiveness.
*  When you get Cash App from the app store Google Play
*  and use code LexPodcast, you'll get $10
*  and Cash App will also donate $10 to FIRST,
*  which again is an organization
*  that I've personally seen inspire girls and boys
*  to dream of engineering a better world.
*  This podcast is also supported by ZipRecruiter.
*  Hiring great people is hard
*  and to me is one of the most important elements
*  of a successful mission-driven team.
*  I've been fortunate to be a part of
*  and lead several great engineering teams.
*  The hiring I've done in the past
*  was mostly through tools we built ourselves,
*  but reinventing the wheel was painful.
*  ZipRecruiter is a tool that's already available for you.
*  It seeks to make hiring simple, fast, and smart.
*  For example, Codable co-founder Gretchen Huebner
*  used ZipRecruiter to find a new game artist
*  to join our education tech company.
*  By using ZipRecruiter's screening questions
*  to filter candidates,
*  Gretchen found it easier to focus on the best candidates
*  and finally hiring the perfect person for the role
*  in less than two weeks from start to finish.
*  ZipRecruiter, the smartest way to hire.
*  See why ZipRecruiter is effective
*  for businesses of all sizes by signing up,
*  as I did for free at ziprecruiter.com slash Lex Pod
*  that's ziprecruiter.com slash Lex Pod.
*  And now here's my conversation with Rohit Prasad.
*  In the movie Her, I'm not sure if you ever seen it,
*  human falls in love with the voice of an AI system.
*  Let's start at the highest philosophical level
*  before we get to deep learning and some of the fun things.
*  Do you think this, what the movie Her shows
*  is within our reach?
*  I think not specifically about Her,
*  but I think what we are seeing is a massive increase
*  in adoption of AI assistance or AI
*  in all parts of our social fabric.
*  And I think it's what I do believe
*  is that the utility these AIs provide,
*  some of the functionalities that are shown
*  within the movie within reach.
*  So some of the functionality
*  in terms of the interactive elements,
*  but in terms of the deep connection
*  that's purely voice-based,
*  do you think such a close connection is possible
*  with voice alone?
*  It's been a while since I saw Her,
*  but I would say in terms of the,
*  in terms of interactions which are both human-like
*  and in these AI assistance,
*  you have to value what is also superhuman.
*  We as humans can be in only one place.
*  AI assistance can be in multiple places at the same time.
*  One with you on your mobile device,
*  one at your home, one at work.
*  So you have to respect these superhuman capabilities too.
*  Plus as humans, we have certain attributes
*  we're very good at, very good at reasoning.
*  AI assistance not yet there,
*  but in the realm of AI assistance,
*  what they're great at is computation, memory,
*  it's infinite and pure.
*  These are the attributes you have to start respecting.
*  So I think the comparison with human-like
*  versus the other aspect, which is also superhuman,
*  has to be taken into consideration.
*  So I think we need to elevate the discussion
*  to not just human-like.
*  So there's certainly elements we just mentioned.
*  Alex is everywhere, computation speaking.
*  So this is a much bigger infrastructure
*  than just the thing that sits there in the room with you.
*  But it certainly feels to us, mere humans,
*  that there's just another little creature there
*  when you're interacting with it.
*  You're not interacting with the entirety
*  of the infrastructure, you're interacting with the device.
*  The feeling is, okay, sure, we anthropomorphize things,
*  but that feeling is still there.
*  So what do you think we, as humans,
*  the purity of the interaction with a smart assistant,
*  what do you think we look for in that interaction?
*  I think in the certain interactions,
*  I think will be very much where it does feel like a human
*  because it has a persona of its own.
*  And in certain ones, it wouldn't be.
*  So I think a simple example to think of it
*  is if you're walking through the house
*  and you just wanna turn on your lights on and off
*  and you're issuing a command,
*  that's not very much like a human-like interaction.
*  And that's where the AI shouldn't come back
*  and have a conversation with you.
*  It should simply complete that command.
*  So I think the blend of, we have to think about
*  this is not human-human alone.
*  It is a human-machine interaction
*  and certain aspects of humans are needed
*  and certain aspects in situations demand it
*  to be like a machine.
*  So I told you, it's gonna be philosophical in parts.
*  What's the difference between human and machine
*  in that interaction?
*  When we interact two humans, especially those are friends
*  and loved ones versus you and a machine
*  that you also are close with.
*  I think you have to think about the roles the AI plays.
*  And it differs from different customer to customer,
*  different situation to situation.
*  Especially I can speak from a Lexus perspective.
*  It is a companion, a friend at times, an assistant,
*  and an advisor down the line.
*  So I think most AIs will have this kind of attributes
*  and it will be very situational in nature.
*  So where is the boundary?
*  I think the boundary depends on exact context
*  in which you're interacting with the AI.
*  So the depth and the richness
*  of natural language conversation is been,
*  by Alan Turing, been used to try to define
*  what it means to be intelligent.
*  There's a lot of criticism of that kind of test,
*  but what do you think is a good test of intelligence
*  in your view in the context of the Turing test?
*  And Alexa, with the Alexa Prize, this whole realm,
*  do you think about this human intelligence,
*  what it means to define it,
*  what it means to reach that level?
*  I do think the ability to converse
*  is a sign of an ultimate intelligence.
*  I think that there's no question about it.
*  So if you think about all aspects of humans,
*  there are sensors we have,
*  and those are basically a data collection mechanism.
*  And based on that, we make some decisions
*  with our sensory brains, right?
*  And from that perspective, I think there are elements
*  we have to talk about how we sense the world,
*  and then how we act based on what we sense.
*  Those elements clearly machines have,
*  but then there's the other aspects of computation
*  that is way better.
*  I also mentioned about memory again,
*  in terms of being near infinite,
*  depending on the storage capacity you have,
*  and the retrieval can be extremely fast and pure
*  in terms of like, there's no ambiguity of
*  who did I see when, right?
*  I mean, machines can remember that quite well.
*  So again, on a philosophical level,
*  I do subscribe to the fact that to be able to converse,
*  and as part of that, to be able to reason
*  based on the world knowledge you've acquired
*  and the sensory knowledge that is there
*  is definitely very much the essence of intelligence.
*  But intelligence can go beyond human level intelligence
*  based on what machines are getting capable of.
*  So what do you think, maybe stepping outside of Alexa
*  broadly as an AI field,
*  what do you think is a good test of intelligence?
*  Put it another way, outside of Alexa,
*  because so much of Alexa as a product
*  is an experience for the customer.
*  On the research side, what would impress the heck out of you
*  if you saw, you know, what is the test where you said,
*  wow, this thing is now starting to encroach
*  into the realm of what we loosely think
*  of as human intelligence?
*  So, well, we think of it as AGI
*  and human intelligence altogether, right?
*  So in some sense, and I think we are quite far from that.
*  I think an unbiased view I have
*  is that the Alexa's intelligence capability is a great test.
*  I think of it as, there are many other proof points,
*  like self-driving cars, game playing like Go or chess.
*  Let's take those two as an example.
*  Clearly requires a lot of data-driven learning
*  and intelligence, but it's not as hard a problem
*  as conversing with, as an AI is with humans
*  to accomplish certain tasks or open domain chat,
*  as you mentioned, Alexa Prize.
*  In those settings, the key differences
*  that the end goal is not defined, unlike game playing.
*  You also do not know exactly what state you are in
*  in a particular goal completion scenario.
*  In certain sense, sometimes you can, if it's a simple goal,
*  but if you're even certain examples, like planning a weekend
*  or you can imagine how many things change along the way.
*  You look for weather, you may change your mind
*  and you change the destination,
*  or you want to catch a particular event
*  and then you decide, no, I want this other event
*  I want to go to.
*  So these dimensions of how many different steps
*  are possible when you're conversing as a human
*  with a machine makes it an extremely daunting problem.
*  And I think it is the ultimate test for intelligence.
*  And don't you think that natural language is enough
*  to prove that conversation, just pure conversation?
*  From a scientific standpoint,
*  natural language is a great test, but I would go beyond,
*  I don't want to limit it to as natural language
*  as simply understanding an intent or parsing for entities
*  and so forth.
*  We are really talking about dialogue.
*  Dialogue.
*  So I would say human machine dialogue
*  is definitely one of the best tests of intelligence.
*  So can you briefly speak to the Alexa Prize
*  for people who are not familiar with it
*  and also just maybe where things stand
*  and what have you learned and what's surprising?
*  What have you seen that's surprising
*  from this incredible competition?
*  Absolutely, it's a very exciting competition.
*  Alexa Prize is essentially a grand challenge
*  in conversational artificial intelligence
*  where we threw the gauntlet to the universities
*  who do active research in the field to say,
*  can you build what we call a social bot
*  that can converse with you coherently
*  and engagingly for 20 minutes?
*  That is an extremely hard challenge,
*  talking to someone who you're meeting for the first time
*  or even if you've met them quite often
*  to speak at 20 minutes on any topic
*  and evolving nature of topics is super hard.
*  We have completed two successful years of the competition.
*  First was one with the University of Washington,
*  second the University of California.
*  We are in our third instance,
*  we have an extremely strong team of 10 cohorts
*  and the third instance of the Alexa Prize is underway now
*  and we are seeing a constant evolution.
*  First year was definitely a learning.
*  It was a lot of things to be put together.
*  We had to build a lot of infrastructure
*  to enable these universities
*  to be able to build magical experiences
*  and do high quality research.
*  Just a few quick questions, sorry for the interruption.
*  What does failure look like in the 20 minute session?
*  So what does it mean to fail
*  not to reach the 20 minute mark?
*  Oh, awesome question.
*  So there are one, first of all,
*  I forgot to mention one more detail.
*  It's not just 20 minutes,
*  but the quality of the conversation too that matters.
*  And the beauty of this competition
*  before I answer that question on what failure means
*  is first that you actually converse with millions
*  and millions of customers as the social bots.
*  So during the judging phases, there are multiple phases.
*  Before we get to the finals,
*  which is a very controlled judging in a situation
*  where we bring in judges and we have interactors
*  who interact with these social bots,
*  that is a much more controlled setting.
*  But till the point we get to the finals,
*  all the judging is essentially by the customers of Alexa.
*  And there you basically rate on a simple question
*  how good your experience was.
*  So that's where we are not testing
*  for a 20 minute boundary being crossed
*  because you do want it to be very much like
*  a clear cut winner be chosen
*  and it's an absolute bar.
*  So did you really break that 20 minute barrier
*  is why we have to test it in a more controlled setting
*  with actors, essentially interactors,
*  and see how the conversation goes.
*  So this is why it's a subtle difference
*  between how it's being tested in the field
*  with real customers versus in the lab to award the prize.
*  So on the latter one, what it means is that essentially
*  there are three judges and two of them have to say
*  this conversation has stalled essentially.
*  Got it and the judges are human experts.
*  Judges are human experts.
*  Okay, great.
*  So this is in the third year.
*  So what's been the evolution?
*  How far, so the DARPA challenge in the first year,
*  the autonomous vehicles, nobody finished in the second year,
*  a few more finished in the desert.
*  So how far along in this, I would say,
*  much harder challenge are we?
*  This challenge has come a long way to the extent that
*  we're definitely not close to the 20 minute barrier
*  being with coherence and engaging conversation.
*  I think we are still five to 10 years away
*  in that horizon to complete that.
*  But the progress is immense.
*  Like what you're finding is the accuracy
*  and what kind of responses these social bots generate
*  is getting better and better.
*  What's even amazing to see that
*  now there's humor coming in, the bots are quite...
*  Awesome.
*  You're talking about ultimate science of intelligence.
*  I think humor is a very high bar
*  in terms of what it takes to create humor.
*  And I don't mean just being goofy,
*  I really mean good sense of humor
*  is also a sign of intelligence in my mind
*  and something very hard to do.
*  So these social bots are now exploring
*  not only what we think of natural language abilities,
*  but also personality attributes
*  and aspects of when to inject an appropriate joke,
*  when you don't know the domain,
*  how you come back with something more intelligible
*  so that you can continue the conversation.
*  If you and I are talking about AI
*  and we are domain experts, we can speak to it.
*  But if you suddenly switch a topic to that I don't know of,
*  how do I change the conversation?
*  So you're starting to notice these elements as well.
*  And that's coming from partly by the nature
*  of the 20 minute challenge
*  that people are getting quite clever
*  on how to really converse
*  and essentially mask some of the understanding defects
*  if they exist.
*  So some of this, this is not Alexa the product,
*  this is somewhat for fun,
*  for research, for innovation and so on.
*  I have a question, sort of in this modern era,
*  there's a lot of, if you look at Twitter and Facebook
*  and so on, there's discourse, public discourse going on.
*  And some things that are a little bit too edgy,
*  people get blocked and so on.
*  I'm just out of curiosity.
*  Are people in this context pushing the limits?
*  Is anyone using the F word?
*  Is anyone sort of pushing back, sort of,
*  arguing, I guess I should say,
*  as part of the dialogue to really draw people in?
*  First of all, let me just back up a bit
*  in terms of why we are doing this, right?
*  So you said it's fun.
*  I think fun is more part of the engaging part for customers.
*  It is one of the most used skills as well
*  in our skill store.
*  But that apart, the real goal was essentially
*  what was happening is with a lot of AI research
*  moving to industry, we felt that academia
*  has the risk of not being able to have the same resources
*  at disposal that we have, which is lots of data,
*  massive computing power, and a clear ways to test
*  these AI advances with real customer benefits.
*  So we brought all these three together in the Lexaprize.
*  That's why it's one of my favorite projects in Amazon.
*  And with that, the secondary effect is yes,
*  it has become engaging for our customers as well.
*  We're not there in terms of where we want it to be, right?
*  But it's a huge progress.
*  But coming back to your question on
*  how do the conversations evolve?
*  Yes, there is some natural attributes of what you said
*  in terms of argument and some amount of swearing.
*  The way we take care of that is that there is
*  a sensitive filter we have built that sees-
*  Keywords and so on.
*  It's more than keywords, a little more in terms of,
*  of course there's keyword base too,
*  but there's more in terms of, these words can be
*  very contextual as you can see, and also the topic
*  can be something that you don't want a conversation
*  to happen because this is a communal device as well.
*  A lot of people use these devices.
*  So we have put a lot of guardrails for the conversation
*  to be more useful for advancing AI and not so much
*  of these other issues you attributed
*  what's happening in the AI field as well.
*  Right, so this is actually a serious opportunity.
*  I didn't use the right word fun.
*  I think it's an open opportunity to do some,
*  some of the best innovation in conversational agents
*  in the world.
*  Absolutely.
*  Why just universities?
*  Why just universities?
*  Because as I said, I really felt-
*  Young minds.
*  Young minds, it's also to, if you think about
*  the other aspect of where the whole industry is moving
*  with AI, there's a dearth of talent in,
*  given the demands.
*  So you do want universities to have a clear place
*  where they can invent and research and not fall behind
*  with that they can't motivate students.
*  Imagine all grad students left to industry like us
*  or faculty members, which has happened too.
*  So this is a way that if you're so passionate
*  about the field where you feel industry and academia
*  need to work well, this is a great example
*  and a great way for universities to participate.
*  So what do you think it takes to build a system
*  that wins the Alexa Prize?
*  I think you have to start focusing on aspects of reasoning
*  that it is, there are still more lookups of what intents
*  customers asking for and responding to those
*  rather than really reasoning about the elements
*  of the conversation.
*  For instance, if you have, if you're playing,
*  if the conversation is about games
*  and it's about a recent sports event,
*  there's so much context involved
*  and you have to understand the entities
*  that are being mentioned so that the conversation
*  is coherent rather than you suddenly just switch
*  to knowing some fact about a sports entity
*  and you're just relaying that rather than understanding
*  the true context of the game.
*  Like if you just said, I learned this fun fact
*  about Tom Brady rather than really say how he played
*  the game the previous night,
*  then the conversation is not really that intelligent.
*  So you have to go to more reasoning elements
*  of understanding the context of the dialogue
*  and giving more appropriate responses,
*  which tells you that we are still quite far
*  because a lot of times it's more facts being looked up
*  and something that's close enough as an answer,
*  but not really the answer.
*  So that is where the research needs to go more
*  in actual true understanding and reasoning.
*  And that's why I feel it's a great way to do it
*  because you have an engaged set of users working
*  to help these AI advances happen in this case.
*  You mentioned customers there quite a bit
*  and there's a skill.
*  What is the experience for the user that's helping?
*  So just to clarify, this isn't, as far as I understand,
*  the Alexa, so this skill is a standalone
*  for the Alexa Prize.
*  I mean, it's focused on the Alexa Prize.
*  It's not you ordering certain things on Amazon.com
*  or checking the weather or playing Spotify.
*  It's a separate skill.
*  And so you're focused on helping that,
*  I don't know, how do customers think of it?
*  Are they having fun?
*  Are they helping teach the system?
*  What's the experience like?
*  I think it's both actually.
*  And let me tell you how you invoke this skill.
*  So all you have to say, Alexa, let's chat.
*  And then the first time you say, Alexa, let's chat,
*  it comes back with a clear message
*  that you're interacting with one of those social bots.
*  And there's a clear, so you know exactly how you interact.
*  And that is why it's very transparent.
*  You are being asked to help.
*  And we have a lot of mechanisms where as the,
*  we are in the first phase of feedback phase then,
*  you send a lot of emails to our customers
*  and then they know that the team needs a lot of interactions
*  with the accuracy of the system.
*  So we know we have a lot of customers
*  who really want to help these university bots
*  and they're conversing with that.
*  And some are just having fun
*  with just saying, Alexa, let's chat.
*  And also some adversarial behavior
*  to see whether how much do you understand as a social bot.
*  So I think we have a good, healthy mix
*  of all three situations.
*  So what is the, if we talk about solving
*  the Alexa challenge, the Alexa prize,
*  what's the data set of really engaging,
*  pleasant conversations look like?
*  Because if we think of this as a supervised learning problem,
*  I don't know if it has to be,
*  but if it does, maybe you can comment on that.
*  Do you think there needs to be a data set
*  of what it means to be an engaging, successful,
*  fulfilling conversation?
*  I think that's part of the research question here.
*  This is, I think we at least got the first spot right,
*  which is have a way for universities to build
*  and test in a real world setting.
*  Now you're asking in terms of the next phase of questions,
*  which we are still, we're also asking by the way,
*  what does success look like from a optimization function?
*  That's what you're asking in terms of,
*  we as researchers are used to having a great corpus
*  of annotated data and then making,
*  then sort of tune our algorithms on those, right?
*  And fortunately and unfortunately,
*  in this world of Alexa prize,
*  that is not the way we are going after it.
*  So you have to focus more on learning based on live feedback.
*  That is another element that's unique,
*  where just not to, I started with giving you
*  how you ingress and experience this capability
*  as a customer.
*  What happens when you're done?
*  They ask you a simple question on a scale of one to five,
*  how likely are you to interact with this social bot again?
*  That is a good feedback
*  and customers can also leave more open-ended feedback.
*  And I think partly that to me
*  is one part of the question you're asking,
*  which I'm saying is a mental model shift that
*  as researchers also, you have to change your mindset
*  that this is not a DARPA evaluation or NSF funded study
*  and you have a nice corpus.
*  This is where it's real world.
*  You have real data.
*  The scale is amazing.
*  That's a beautiful thing.
*  And then the customer, the user can
*  quit the conversation at any time.
*  Exactly, the user can.
*  That is also a signal for how good you were at that point.
*  So, and then on a scale of one to five, one to three,
*  do they say how likely are you or is it just a binary?
*  How likely? One to five.
*  One to five.
*  Wow, okay.
*  That's such a beautifully constructed challenge.
*  Okay.
*  You said the only way to make a smart assistant
*  really smart is to give it eyes and let it explore the world.
*  I'm not sure it might have been taken out of context,
*  but can you comment on that?
*  Can you elaborate on that idea?
*  Is that I personally also find that idea super exciting
*  from a social robotics, personal robotics perspective.
*  Yeah, a lot of things do get taken out of context.
*  This particular one was just as philosophical discussion
*  we were having on terms of what does intelligence look like.
*  And the context was in terms of learning,
*  I think just we said we as humans are empowered
*  with many different sensory abilities.
*  I do believe that eyes are an important aspect of it
*  in terms of if you think about how we as humans learn,
*  it is quite complex and it's also not unimodal
*  that you are fed a ton of text or audio
*  and you just learn that way.
*  No, you learn by experience, you learn by seeing,
*  you're taught by humans
*  and we are very efficient in how we learn.
*  Machines on the contrary are very inefficient
*  on how they learn, especially these AIs.
*  I think the next wave of research is going to be
*  with less data, not just less human,
*  not just with less labeled data,
*  but also with a lot of weak supervision
*  and where you can increase the learning rate.
*  I don't mean less data in terms of not having
*  a lot of data to learn from
*  that we are generating so much data,
*  but it is more about from a aspect of how fast can you learn.
*  So improving the quality of the data
*  that's the quality of data and the learning process.
*  I think more on the learning process.
*  I think we have to, we as humans learn
*  with a lot of noisy data, right?
*  And I think that's the part that I don't think should change.
*  What should change is how we learn, right?
*  So if you look at, you mentioned supervised learning,
*  we have making transformative shifts
*  from moving to more unsupervised, more weak supervision.
*  Those are the key aspects of how to learn.
*  And I think in that setting, I hope you agree with me
*  that having other senses is very crucial
*  in terms of how you learn.
*  So absolutely, from a machine learning perspective,
*  which I hope we get a chance to talk to a few aspects
*  that are fascinating there, but to stick on the point
*  of sort of a body, you know, embodiment.
*  So Alexa has a body,
*  it has a very minimalistic, beautiful interface,
*  or there's a ring and so on.
*  I mean, I'm not sure of all the flavors
*  of the devices that Alexa lives on,
*  but there's a minimalistic basic interface.
*  And nevertheless, we humans, so I have a Roomba,
*  I have all kinds of robots all over everywhere.
*  So what do you think Alexa of the future looks like
*  if it begins to shift what his body looks like?
*  Maybe beyond Alexa, what do you think
*  are the different devices in the home
*  as they start to embody their intelligence more and more?
*  What do you think that looks like?
*  Philosophically, a future, what do you think that looks like?
*  I think let's look at what's happening today.
*  You mentioned, I think, our devices as an Amazon devices,
*  but I also wanted to point out,
*  Alexa is already integrated a lot of third-party devices,
*  which also come in lots of forms and shapes,
*  some in robots, right?
*  Some in microwaves, some in appliances
*  that you use in everyday life.
*  So I think it's not just the shape Alexa takes
*  in terms of form factors,
*  but it's also where all it's available.
*  And it's getting in cars,
*  it's getting in different appliances in homes,
*  even toothbrushes, right?
*  So I think you have to think about it
*  as not a physical assistant.
*  It will be in some embodiment, as you said,
*  we already have these nice devices,
*  but I think it's also important to think of it
*  it is a virtual assistant.
*  It is superhuman in the sense that it is
*  in multiple places at the same time.
*  So I think the actual embodiment in some sense,
*  to me doesn't matter.
*  I think you have to think of it as not as human-like
*  and more of what its capabilities are
*  that derive a lot of benefit for customers
*  and how there are different ways to delight customers
*  and different experiences.
*  And I think I'm a big fan of it not being just human-like,
*  it should be human-like in certain situations.
*  Alexa Price Social Bot in terms of conversation
*  is a great way to look at it,
*  but there are other scenarios where human-like
*  I think is underselling the abilities of this AI.
*  So if I could trivialize what we're talking about.
*  So if you look at the way Steve Jobs thought
*  about the interaction with the device that Apple produced,
*  there was an extreme focus on controlling the experience
*  by making sure there's only this Apple produced devices.
*  You see the voice of Alexa taking all kinds of forms
*  depending on what the customers want.
*  And that means it could be anywhere from the microwave
*  to a vacuum cleaner to the home and so on.
*  The voice is the essential element of the interaction.
*  I think voice is an essence.
*  It's not all, but it's a key aspect.
*  I think to your question in terms of,
*  you should be able to recognize Alexa.
*  And that's a huge problem.
*  I think in terms of a huge scientific problem,
*  I should say, like what are the traits?
*  What makes it look like Alexa,
*  especially in different settings,
*  and especially if it's primarily voice what it is.
*  But Alexa is not just voice either, right?
*  I mean, we have devices with a screen.
*  Now you're seeing just other behaviors of Alexa.
*  So I think we are in very early stages of what that means.
*  And this will be an important topic for the following years.
*  But I do believe that being able to recognize
*  and tell when it's Alexa versus it's not
*  is going to be important from an Alexa perspective.
*  I'm not speaking for the entire AI community,
*  but I think attribution.
*  And as we go into more of understanding who did what,
*  that identity of the AI is crucial in the coming world.
*  I think from the broad AI community perspective,
*  that's also a fascinating problem.
*  So basically, if I close my eyes and listen to the voice,
*  what would it take for me to recognize that this is Alexa?
*  Exactly.
*  Or at least the Alexa that I've come to know
*  from my personal experience in my home
*  through my interactions, that kind of thing.
*  Yeah, and the Alexa here in the US is very different
*  than the Alexa in UK and the Alexa in India,
*  even though they are all speaking English
*  or the Australian version.
*  So again, so now think about when you go
*  into a different culture, a different community,
*  but you travel there, what do you recognize Alexa?
*  I think these are super hard questions actually.
*  So there's a team that works on personality.
*  So if we talk about those different flavors
*  of what it means culturally speaking, India, UK, US,
*  what does it mean to add?
*  So the problem that we just stated, which is fascinating,
*  how do we make it purely recognizable that it's Alexa?
*  Assuming that the qualities of the voice
*  are not sufficient.
*  It's also the content of what is being said.
*  How do we do that?
*  How does the personality come into play?
*  What's that research gonna look like?
*  I mean, it's such a fascinating.
*  It's a bit of some very fascinating folks
*  who from both the UX background and human factors
*  are looking at these aspects and these exact questions.
*  But I'll definitely say it's not just how it sounds,
*  the choice of words, the tone, not just, I mean,
*  the voice identity of it, but the tone matters,
*  the speed matters, how you speak, how you enunciate words,
*  what choice of words are you using, how terse are you,
*  or how lengthy in your explanations you are.
*  All of these are factors.
*  And you also, you mentioned something crucial
*  that you may have personalized Alexa to some extent
*  in your homes or in the devices you are interacting with.
*  So you as your individual, how you prefer Alexa sounds
*  can be different than how I prefer.
*  And we may, and the amount of customizability
*  you want to give is also a key debate we always have.
*  But I do want to point out it's more than the voice actor
*  that recorded and it sounds like that actor.
*  It is more about the choices of words,
*  the attributes of tonality, the volume,
*  in terms of how you raise your pitch and so forth.
*  All of that matters.
*  This is such a fascinating problem
*  from a product perspective.
*  I could see those debates just happening inside
*  of the Alexa team of how much personalization
*  do you do for the specific customer?
*  Because you're taking a risk if you over personalize.
*  Because you don't, if you create a personality
*  for a million people, you can test that better,
*  you can create a rich, fulfilling experience
*  that will do well.
*  But if the more you personalize it,
*  the less you can test it, the less you can know
*  that it's a great experience.
*  So how much personalization, what's the right balance?
*  I think the right balance depends on the customer.
*  Give them the control.
*  So I'll say, I think the more control you give customers,
*  the better it is for everyone.
*  And I'll give you some key personalization features.
*  I think we have a feature called Remember This,
*  which is where you can tell Alexa to remember something.
*  There you have an explicit sort of controlling
*  customer's hand because they have to say,
*  Alexa, remember X, Y, Z.
*  What kind of things would that be used for?
*  So you can like you.
*  For song titles or something.
*  I have stored my tire specs for my car.
*  Because it's so hard to go and find and see what it is,
*  right when you're having some issues.
*  I store my mileage plan numbers
*  for all the frequent flyer ones,
*  where I'm sometimes just looking at it and it's not handy.
*  So those are my own personal choices I've made
*  for Alexa to remember something on my behalf.
*  So again, I think the choice was be explicit
*  about how you provide that to a customer as a control.
*  So I think these are the aspects of what you do.
*  Like think about where we can use
*  speaker recognition capabilities that it's,
*  if you taught Alexa that you are Lex
*  and this person in your household is person two,
*  then you can personalize the experiences.
*  Again, these are very in the CX customer experience patterns
*  are very clear about and transparent
*  when a personalization action is happening.
*  And then you have other ways like you go through
*  explicit control right now through your app
*  that your multiple service providers, let's say for music,
*  which one is your preferred one?
*  So when you say play Sting,
*  depend on your whether you have preferred Spotify
*  or Apple music that the decision is made
*  where to play it from.
*  So what's Alexa's backstory from her perspective?
*  I remember just asking as probably a lot of us are
*  just the basic questions about love and so on of Alexa,
*  just to see what the answer would be.
*  Just as it feels like there's a little bit of a back,
*  like there's a feels like there's a little bit
*  of personality, but not too much.
*  Is Alexa have a metaphysical presence
*  in this human universe we live in
*  or is it something more ambiguous?
*  Is there a past?
*  Is there a birth?
*  Is there a family kind of idea,
*  even for joking purposes and so on?
*  I think, well, it does tell you if I think you,
*  I should double check this,
*  but if you said when were you born,
*  I think we do respond.
*  I need to double check that,
*  but I'm pretty positive about it.
*  I think you do it
*  because I think I've tested that.
*  But that's like how I was born in your brand of champagne
*  and whatever the year kind of thing.
*  So on terms of the metaphysical, I think it's early.
*  Does it have the historic knowledge about herself
*  to be able to do that?
*  Maybe, have we crossed that boundary?
*  Not yet, right?
*  In terms of being, thank you.
*  Have we thought about it quite a bit,
*  but I wouldn't say that we have come to a clear decision
*  in terms of what it should look like.
*  But you can imagine though,
*  and I bring this back to the Alexa Prize Social Bot One,
*  there you will start seeing some of that.
*  These bots have their identity,
*  and in terms of that, you may find,
*  this is such a great research topic
*  that some academia team may think of these problems
*  and start solving them too.
*  So let me ask a question.
*  It's kind of difficult, I think,
*  but it feels, and fascinating to me,
*  because I'm fascinated with psychology,
*  it feels that the more personality you have,
*  the more dangerous it is in terms of
*  a customer perspective, a product,
*  if you want to create a product that's useful.
*  By dangerous, I mean creating an experience that upsets me.
*  And so how do you get that right?
*  Because if you look at the relationships,
*  maybe I'm just a screwed up Russian,
*  but if you look at the human to human relationships,
*  some of our deepest relationships have fights,
*  have tension, have the push and pull,
*  have a little flavor in them.
*  Do you want to have such flavor
*  in an interaction with Alexa?
*  How do you think about that?
*  So there's one other common thing that you didn't say,
*  but we think of it as paramount
*  for any deep relationship, that's trust.
*  Trust, yeah.
*  I think if you trust every attribute you said,
*  a fight, some tension, is all healthy,
*  but what is sort of unnegotiable in this instance is trust.
*  And I think the bar to earn customer trust for AI
*  is very high, in some sense, more than a human.
*  It's not just about personal information or your data,
*  it's also about your actions on a daily basis.
*  How trustworthy are you in terms of consistency,
*  in terms of how accurate are you in understanding me?
*  Like if you're talking to a person on the phone,
*  if you have a problem with your,
*  let's say your internet or something,
*  if the person's not understanding,
*  you lose trust right away.
*  You don't want to talk to that person.
*  That whole example gets amplified by a factor of 10,
*  because when you're a human interacting with an AI,
*  you have a certain expectation.
*  Either you expect it to be very intelligent
*  and then you get upset, why is it behaving this way?
*  Or you expect it to be not so intelligent
*  and when it surprises you, you're like,
*  really, you're trying to be too smart?
*  So I think we grapple with these hard questions as well,
*  but I think the key is actions need to be trustworthy
*  from these AIs, not just about data protection,
*  your personal information production,
*  but also from how accurately it accomplishes all commands
*  or all interactions.
*  Well, it's tough to hear because trust,
*  you're absolutely right,
*  but trust is such a high bar with AI systems
*  because people, and I see this
*  because I work with autonomous vehicles,
*  I mean, the bar that's placed on AI system
*  is unreasonably high.
*  Yeah, that is going to be, I agree with you,
*  and I think of it as a challenge
*  and it also keeps my job.
*  Right?
*  So from that perspective, I totally,
*  I think of it at both sides,
*  as a customer and as a researcher.
*  I think as a researcher, yes,
*  occasionally it will frustrate me
*  that why is the bar so high for these AIs?
*  And as a customer, then I say,
*  absolutely it has to be that high.
*  Right?
*  So I think that's the trade-off we have to balance,
*  but doesn't change the fundamentals
*  that trust has to be earned.
*  And the question then becomes is,
*  are we holding the AIs to a different bar
*  in accuracy and mistakes than we hold humans?
*  That's gonna be a great societal questions
*  for years to come, I think, for us.
*  Well, one of the questions that we grapple
*  with as a society now that I think about a lot,
*  I think a lot of people in the AI think about a lot,
*  and Alexis taking on head on is privacy.
*  Is the reality is us giving over data
*  to any AI system can be used to enrich our lives
*  in profound ways.
*  So if basically any product that does anything awesome
*  for you, the more data it has,
*  the more awesome things it can do.
*  And yet, on the other side,
*  people imagine the worst case possible scenario
*  of what can you possibly do with that data.
*  People, it goes down to trust, as you said before.
*  There's a fundamental distrust
*  in certain groups of governments and so on,
*  depending on the government, depending on who is in power,
*  depending on all these kinds of factors.
*  And so here's Alex in the middle of all of it,
*  in the home, trying to do good things for the customers.
*  So how do you think about privacy in this context,
*  the smart assistance in the home?
*  How do you maintain, how do you earn trust?
*  Absolutely, so as you said, trust is the key here.
*  So you start with trust, and then privacy
*  is a key aspect of it.
*  It has to be designed from very beginning about that.
*  And we believe in two fundamental principles.
*  One is transparency, and second is control.
*  By transparency, I mean when we build
*  what is now called smart speaker or the first Echo,
*  we were quite judicious about making these right trade-offs
*  on customers' behalf, that it is pretty clear
*  when the audio is being sent to cloud.
*  The light ring comes on when it has heard you say
*  the word wake word, and then the streaming happens.
*  So when the light ring comes up,
*  we also had, we put a physical mute button on it,
*  just so if you didn't want it to be listening,
*  even for the wake word, then you turn the power button,
*  the mute button on, and that disables the microphones.
*  That's just the first decision
*  on essentially transparency and control.
*  Over then, even when we launched,
*  we gave the control in the hands of the customers
*  that you can go and look at any of your individual utterances
*  that is recorded and delete them any time.
*  And we have cut true to that promise, right?
*  So, and that is super, again, a great instance
*  of showing how you have the control.
*  Then we made it even easier.
*  You can say, Alexa, delete what I said today.
*  So that is now making it even just more control
*  in your hands with what's most convenient
*  about this technology is voice.
*  You delete it with your voice now.
*  So these are the types of decisions we continually make.
*  We just recently launched this feature called,
*  what we think of it as if you wanted humans
*  not to review your data,
*  because you've mentioned supervised learning, right?
*  So in supervised learning,
*  humans have to give some annotation.
*  And that also is now a feature where you can,
*  essentially, if you've selected that flag,
*  your data will not be reviewed by a human.
*  So these are the types of controls
*  that we have to constantly offer with customers.
*  So why do you think it bothers people so much that,
*  so everything you just said is really powerful.
*  So the control, the ability to delete,
*  because we collect, we have studies here running at MIT
*  that collects huge amounts of data,
*  and people consent and so on.
*  The ability to delete that data is really empowering,
*  and almost nobody ever asked to delete it,
*  but the ability to have that control is really powerful.
*  But still, there's these popular anecdotes,
*  anecdotal evidence that people say,
*  they like to tell that them and a friend
*  were talking about something, I don't know,
*  sweaters for cats, and all of a sudden,
*  they'll have advertisements for cat sweaters on Amazon.
*  That's a popular anecdote,
*  as if something is always listening.
*  Can you explain that anecdote,
*  that experience that people have?
*  What's the psychology of that?
*  What's that experience?
*  And can you, you've answered it,
*  but let me just ask, is Alexa listening?
*  No, Alexa listens only for the wake word on the device.
*  And the wake word is?
*  The words like Alexa, Amazon, Echo,
*  but you only choose one at a time.
*  So you choose one,
*  and it listens only for that on our devices.
*  So that's first.
*  From a listening perspective,
*  we have to be very clear that it's just the wake word.
*  So you said, why is there this anxiety, if you may?
*  It's because there's a lot of confusion
*  about what it really listens to.
*  And I think it's partly on us to keep educating
*  our customers and the general media more,
*  in terms of what really happens,
*  and we've done a lot of it.
*  And our pages on information are clear,
*  but still people have to have more,
*  there's always a hunger for information and clarity.
*  And we'll constantly look at how best to communicate.
*  If you go back and read everything,
*  yes, it states exactly that.
*  And then people could still question it.
*  And I think that's absolutely okay to question.
*  What we have to make sure is that we are,
*  because our fundamental philosophy is customer first,
*  customer obsession is our leadership principle.
*  If you put, as researchers,
*  I put myself in the shoes of the customer,
*  and all decisions in Amazon are made with that,
*  and trust has to be earned,
*  and we have to keep earning the trust
*  of our customers in this setting.
*  And to your other point on like,
*  is there something showing up based on your conversations?
*  No, I think the answer is like you,
*  lot of times when those experiences happen,
*  you have to also know that, okay,
*  it may be a winter season,
*  people are looking for sweaters, right?
*  And it shows up on your amazon.com because it is popular.
*  So there are many of these,
*  you mentioned that personality or personalization,
*  turns out we are not that unique either.
*  Yeah.
*  So those things we as humans start thinking,
*  oh, must be because something was heard,
*  and that's why this other thing showed up.
*  The answer is no, probably it is just the season
*  for sweaters.
*  I'm not gonna ask you this question,
*  because it's just because you're also,
*  because people have so much paranoia,
*  but for my, let me just say from my perspective,
*  I hope there's a day when the customer can ask Alexa
*  to listen all the time, to improve the experience,
*  because I personally don't see the negative,
*  because if you have the control and if you have the trust,
*  there's no reason why I shouldn't be listening
*  all the time to the conversations to learn more about you,
*  because ultimately, as long as you have control and trust,
*  every data you provide to the device,
*  that the device wants, is going to be useful.
*  To me, as a machine learning person,
*  I think it worries me how sensitive people are
*  about their data relative to how empowering it could be
*  for the devices around them,
*  enriching it could be for their own life
*  to improve the product.
*  So I just, it's something I think about sort of a lot,
*  how do we make that devices, obviously,
*  Alexa thinks about it a lot as well.
*  I don't know if you wanna comment on that sort of,
*  let me ask it in the form of a question.
*  Have you seen an evolution in the way people think about
*  their private data in the previous several years?
*  So as we as a society get more and more comfortable
*  to the benefits we get by sharing more data?
*  First, let me answer that part,
*  and then I'll wanna go back to the other aspect
*  you were mentioning.
*  So as a society, on a general,
*  we are getting more comfortable as a society.
*  It doesn't mean that everyone is,
*  and I think we have to respect that.
*  I don't think one size fits all
*  is always gonna be the answer for all, right?
*  By definition.
*  So I think that's something to keep in mind in these.
*  Going back to your on what more magical experiences
*  can be launched in these kinds of AI settings.
*  I think again, if you give the control,
*  we, it's possible certain parts of it.
*  So we have a feature called follow up mode
*  where you, if you turn it on,
*  and Alexa after you've spoken to it,
*  will open the mics again,
*  thinking you will answer something again.
*  Like if you're adding lists to your shopping item,
*  so right, or a shopping list or to do list,
*  you're not done.
*  You wanna keep, so in that setting,
*  it's awesome that it opens the mic for you to say,
*  eggs and milk and then bread, right?
*  So these are the kind of things which you can empower.
*  So, and then another feature we have,
*  which is called Alexa guard.
*  I said, it only listens for the wake word, all right?
*  But if you have, let's say you're going to say,
*  Alexa, you leave your home and you want Alexa
*  to listen for a couple of sound events,
*  like smoke alarm going off or someone breaking your glass.
*  Right, so it's like just to keep your peace of mind.
*  So you can say Alexa on guard or I'm away or,
*  and then it can be listening for these sound events.
*  And then when you're home, you come out of that mode, right?
*  So this is another one where you again gave controls
*  in the hands of the user or the customer
*  and to enable some experience that is high utility
*  and maybe even more delightful in the certain settings
*  like follow up mode and so forth.
*  Again, this general principle is the same,
*  control in the hands of the customer.
*  So I know we kind of started with a lot of philosophy,
*  a lot of interesting topics
*  and we're just jumping all over the place,
*  but really some of the fascinating things
*  that the Alexa team and Amazon is doing
*  is in the algorithm side, the data side,
*  the technology, the deep learning, machine learning
*  and so on.
*  So can you give a brief history of Alexa
*  from the perspective of just innovation,
*  the algorithms, the data of how it was born,
*  how it came to be, how it has grown, where it is today?
*  Yeah, it starts with, in Amazon,
*  everything starts with the customer.
*  And we have a process called working backwards.
*  Alexa and more specifically than the product Echo,
*  there was a working backwards document essentially
*  that reflected what it would be,
*  started with a very simple vision statement for instance,
*  that morphed into a full-fledged document
*  along the way it changed into what all it can do.
*  But the inspiration was the Star Trek computer.
*  So when you think of it that way,
*  everything is possible, but when you launch a product,
*  you have to start with some place.
*  And when I joined, the product was already in conception
*  and we started working on the far-field speech recognition
*  because that was the first thing to solve.
*  By that we mean that you should be able to speak
*  to the device from a distance.
*  And in those days that wasn't a common practice.
*  And even in the previous research world I was in
*  was considered to unsolvable problem then
*  in terms of whether you can converse from a length.
*  And here I'm still talking about the first part
*  of the problem where you say, get the attention
*  of the device as in by saying what we call the wake word,
*  which means the word Alexa has to be detected
*  with a very high accuracy because it is a very common word.
*  It has sound units that map with words like I like you
*  or Alec, Alex, right?
*  It's an undoubtedly hard problem to detect
*  the right mentions of Alexa's address to the device
*  versus I like Alexa.
*  You have to pick up that signal when there's a lot of noise.
*  Not only noise, but a lot of conversation in the house.
*  You remember on the device you're simply listening
*  for the wake word Alexa.
*  And there's a lot of words being spoken in the house.
*  How do you know it's Alexa and directed at Alexa?
*  Because I could say, I love my Alexa, I hate my Alexa.
*  I want Alexa to do this.
*  And in all these three sentences I said, Alexa,
*  I didn't want it to wake up.
*  So, and-
*  Can I just pause on that second?
*  What would be your device that I should probably
*  in the introduction of this conversation give to people
*  in terms of them turning off their Alexa device
*  if they're listening to this podcast conversation out loud?
*  Like what's the probability that an Alexa device
*  will go off because we mentioned Alexa like a million times.
*  So it will, we have done a lot of different things
*  where we can figure out that there is the device,
*  the speech is coming from a human versus over the air.
*  Also, I mean, in terms of like, also it is,
*  think about ads or, so we have also launched a technology
*  for watermarking kind of approaches
*  in terms of filtering it out.
*  But yes, if this kind of a podcast is happening,
*  it's possible your device will wake up a few times.
*  It's an unsolved problem, but it is definitely
*  something we care very much about.
*  But the idea is you want to detect Alexa-
*  Meant for the device.
*  First of all, just even hearing Alexa versus a like,
*  something, I mean, that's a fascinating part.
*  So that was the first relief.
*  That's the first one.
*  The world's best detector of Alexa.
*  The world's best wake word detector
*  in a far field setting, not like something
*  where the phone is sitting on the table.
*  This is like people have devices 40 feet away
*  like in my house or 20 feet away
*  and you still get an answer.
*  So that was the first part.
*  The next is, okay, you're speaking to the device.
*  Of course you're gonna issue many different requests.
*  Some may be simple, some may be extremely hard,
*  but it's a large vocabulary
*  speech recognition problem essentially,
*  where the audio is now not coming onto your phone
*  or a handheld mic like this or a close talking mic,
*  but it's from 20 feet away
*  where if you're in a busy household,
*  your son may be listening to music,
*  your daughter may be running around with something
*  and asking your mom something and so forth.
*  So this is like a common household setting
*  where the words you're speaking to Alexa
*  need to be recognized with very high accuracy.
*  Now we're still just in the recognition problem.
*  You haven't yet come to the understanding one.
*  And if I pause them, sorry, once again,
*  what year was this?
*  Is this before neural networks began to start
*  to seriously prove themselves in the audio space?
*  Yeah, this is around, so I joined in 2013 in April.
*  So the early research in neural networks coming back
*  and showing some promising results
*  in speech recognition space had started happening,
*  but it was very early.
*  But we just now build on that
*  on the very first thing we did when I joined the team
*  and remember it was a very much of a startup environment,
*  which is great about Amazon.
*  And we doubled on deep learning right away.
*  And we knew we'll have to improve accuracy fast.
*  And because of that, we worked on and the scale of data,
*  once you have a device like this, if it is successful,
*  will improve big time.
*  You'll suddenly have large volumes of data to learn from
*  to make the customer experience better.
*  So how do you scale deep learning?
*  So we did one of the first works
*  in training with distributed GPUs
*  and where the training time was linear
*  in terms of the amount of data.
*  So that was quite important work
*  where it was algorithmic improvements
*  as well as a lot of engineering improvements
*  to be able to train on thousands and thousands of speech.
*  And that was an important factor.
*  So if you asked me like back in 2013 and 2014,
*  when we launched Echo,
*  the combination of large scale data, deep learning progress,
*  near infinite GPUs we had available on AWS even then,
*  all came together for us to be able to
*  solve the far field speech recognition
*  to the extent it could be useful to the customers.
*  It's still not solved.
*  Like, I mean, it's not that we are perfect
*  at recognizing speech, but we are great at it
*  in terms of the settings that are in homes, right?
*  So, and that was important even in the early stages.
*  So first of all, just even,
*  I'm trying to look back at that time.
*  If I remember correctly,
*  it seems like the task will be pretty daunting.
*  So like, so we kind of take it for granted
*  that it works now?
*  Yes, you're right.
*  So let me like how, first of all, you mentioned startup.
*  I wasn't familiar how big the team was.
*  I kind of, because I know there's a lot of
*  really smart people working on it.
*  So now it's a very, very large team.
*  How big was the team?
*  How likely were you to fail in the eyes of everyone else?
*  And ourselves?
*  And yourself?
*  So like what?
*  I'll give you a very interesting anecdote on that.
*  When I joined the team, the speech recognition team
*  was six people.
*  My first meeting, and we had hired a few more people,
*  it was 10 people.
*  Nine out of 10 people thought it can't be done.
*  Who was the one?
*  The one was me.
*  And actually I should say, and one was semi-optimistic.
*  Yeah.
*  And eight were trying to convince,
*  let's go to the management and say,
*  let's not work on this problem.
*  Let's work on some other problem,
*  like either telephony speech for customer service calls
*  and so forth.
*  But this was the kind of belief you must have.
*  And I had experience with far-field speech recognition,
*  and my eyes lit up when I saw a problem like that saying,
*  okay, we have been in speech recognition,
*  always looking for that killer app.
*  And this was a killer use case to bring something
*  delightful in the hands of customers.
*  So you mentioned the way you kind of think of it
*  in the product way in the future,
*  you have a press release and an FAQ
*  and you think backwards.
*  Did you have, did the team have the echo in mind?
*  So this far-field speech recognition,
*  actually putting a thing in the home that works,
*  that it's able to interact with,
*  was that the press release?
*  What was the-
*  Very close, I would say, in terms of the,
*  as I said, the vision was starter computer, right?
*  Or the inspiration.
*  And from there, I can't divulge all the exact specifications,
*  but one of the first things that was magical on Alexa
*  was music.
*  It brought me back to music because my taste is still in
*  when I was in undergrad.
*  So I still listen to those songs and I,
*  it was too hard for me to be a music fan with a phone, right?
*  So I, and I don't, I hate things in my ear.
*  So from that perspective, it was quite hard.
*  And music was part of the,
*  at least the documents I've seen, right?
*  So from that perspective, I think, yes,
*  in terms of how far are we from the original vision?
*  I can't reveal that, but that's why I have done a fun
*  at work because every day we go in and thinking like,
*  these are the new set of challenges to solve.
*  Yeah, it's a great way to do great engineering
*  as you think of the, the press release.
*  I like that idea, actually.
*  Maybe we'll talk about it a bit later,
*  but it's just a super nice way to have focus.
*  I'll tell you this, you're a scientist
*  and a lot of my scientists have adopted that.
*  They have now, they love it as a process
*  because it was very, as scientists,
*  you're trained to write great papers,
*  but they are all after you've done the research
*  or you're proven and your PhD dissertation proposal
*  is something that comes closest or a DARPA proposal
*  or a NSF proposal is the closest that comes
*  to a press release.
*  But that process is now ingrained in our scientists,
*  which is like delightful for me to see.
*  You write the paper first and then make it happen.
*  That's right.
*  In fact, that's not-
*  State of the art results.
*  Or you leave the results section open
*  where you have a thesis about here's what I expect, right?
*  And here's what it will change.
*  Right?
*  So I think it is a great thing.
*  It works for researchers as well.
*  Yeah.
*  So far field recognition.
*  Yeah.
*  What was the big leap?
*  What were the breakthroughs
*  and what was that journey like to today?
*  Yeah, I think the, as you said first,
*  there was a lot of skepticism
*  on whether far field speech recognition will ever work
*  to be good enough, right?
*  And what we first did was got a lot of training data
*  in a far field setting.
*  And that was extremely hard to get
*  because none of it existed.
*  So how do you collect data in far field setup, right?
*  With no customer base at the start.
*  With no customer base, right?
*  So that was first innovation.
*  And once we had that, the next thing was,
*  okay, if you have the data,
*  first of all, we didn't talk about
*  what would magical mean in this kind of a setting?
*  What is good enough for customers, right?
*  That's always, since you've never done this before,
*  what would be magical?
*  So it wasn't just a research problem.
*  You had to put some, in terms of accuracy
*  and customer experience features,
*  some stakes on the ground saying,
*  here's where I think it should get to.
*  So you established a bar,
*  and then how do you measure progress
*  to where it's given you have no customer right now?
*  So from that perspective, we went,
*  so first was the data without customers.
*  Second was doubling down on deep learning
*  as a way to learn.
*  And I can just tell you that the combination of the two
*  generates by a factor of five.
*  From where we were when I started to,
*  within six months of having that data,
*  at that point, I got the conviction that this will work.
*  Right?
*  So, because that was magical
*  in terms of when it started working.
*  And-
*  That reached the magic bar.
*  That came close to the magical bar.
*  To the bar, right?
*  That we felt would be where people will use it.
*  That was critical.
*  Because you really have one chance at this.
*  If we had launched in November 2014 is when we launched,
*  if it was below the bar,
*  I don't think this category exists
*  if you don't meet the bar.
*  Yeah, and just having looked at voice-based interactions,
*  like in the car, earlier systems,
*  it's a source of huge frustration for people.
*  In fact, we use voice-based interaction
*  for collecting data on subjects to measure frustration.
*  So, as a training set for computer vision,
*  for face data,
*  so we can get a data set of frustrated people.
*  That's the best way to get frustrated people
*  is having them interact with a voice-based system in the car.
*  So, that bar, I imagine, is pretty high.
*  Was very high, and we talked about how, also,
*  errors are perceived from AIs versus errors by humans.
*  But we are not done with the problems that ended up,
*  we had to solve to get it to launch.
*  So, do you want the next one?
*  Yeah, the next one.
*  So, the next one was what I think of as
*  multi-domain natural language understanding.
*  It's very, I wouldn't say easy,
*  but it is, during those days,
*  solving it, understanding in one domain, a narrow domain,
*  was doable, but for these multiple domains,
*  like music, like information,
*  other kinds of household productivity, alarms, timers,
*  even though it wasn't as big as it is
*  in terms of the number of skills Alexa has
*  and the confusion space has grown by
*  three orders of magnitude,
*  it was still daunting even those days.
*  Again, no customer base yet.
*  Again, no customer base.
*  So, now you're looking at meaning understanding
*  and intent understanding and taking actions
*  on behalf of customers based on their requests.
*  And that is the next hard problem,
*  even if you have gotten the words recognized,
*  how do you make sense of them?
*  In those days, there was still a lot of emphasis
*  on rule-based systems for writing grammar patterns
*  to understand the intent,
*  but we had a statistical first approach even then,
*  where for our language understanding,
*  we had, even those starting days,
*  an entity recognizer and an intent classifier,
*  which was all trained statistically.
*  In fact, we had to build the deterministic matching
*  as a follow-up to fix bugs
*  that statistical models have, right?
*  So, it was just a different mindset
*  where we focused on data-driven statistical understanding.
*  When's in the end if you have a huge data set?
*  Yes, it is contingent on that.
*  And that's why it came back to how do you get the data?
*  Before customers, the fact that this is why data
*  becomes crucial to get to the point
*  that you have the understanding system built up.
*  And notice that, we were talking about human-machine dialogue
*  and even those early days,
*  even it was very much transactional,
*  do one thing, one short utterances in great way.
*  There was a lot of debate on how much should Alexa talk back
*  in terms of if it misunderstood you,
*  or you said play songs by the stones,
*  and let's say it doesn't know early days,
*  knowledge can be sparse, who are the stones, right?
*  It's the rolling stones, right?
*  So, and you don't want the match to be
*  Stone Temple Pilots or Rolling Stones, right?
*  So, you don't know which one it is.
*  So, these kind of other signals to,
*  and out there we had great assets, right?
*  From Amazon in terms of...
*  UX, like what is it?
*  What kind of, yeah, how do you solve that problem?
*  In terms of what we think of it
*  as an entity resolution problem, right?
*  Because which one is it, right?
*  I mean, even if you figured out the stones as an entity,
*  you have to resolve it to whether it's the stones
*  or the Stone Temple Pilots or some other stones.
*  Maybe I misunderstood, is the resolution
*  the job of the algorithm, or is the job of UX
*  communicating with the human to help the resolution?
*  Well, there is both, right?
*  It is, you want 90% or high 90s to be done
*  without any further questioning or UX, right?
*  So, but that it's absolutely okay,
*  just like as humans, we ask the question,
*  I didn't understand you, Lex.
*  It's fine for a Lex at occasion
*  and say, I did not understand you, right?
*  And that's an important way to learn.
*  And I'll talk about where we have come
*  with more self-learning with these kinds of feedback signals.
*  But in those days, just solving the ability
*  of understanding the intent and resolving to an action,
*  where action could be play a particular artist
*  or a particular song was super hard.
*  Again, the bar was high as we were talking about, right?
*  So while we launched it in sort of 13 big domains,
*  I would say, in terms of, or we think of it as 13,
*  the big skills we had, like music is a massive one
*  when we launched it, and now we have 90,000 plus skills
*  on Alexa.
*  So what are the big skills?
*  Can you just go over them?
*  Because the only thing I use it for
*  is music, weather, and shopping.
*  So we think of it as music information, right?
*  So weather is a part of information, right?
*  So when we launched, we didn't have smart home,
*  but within, by smart home, I mean,
*  you connect your smart devices,
*  you control them with voice.
*  If you haven't done it, it's worth,
*  it will change your life.
*  Like turning on the lights and so on.
*  Yeah, turning on your light to anything that's connected
*  and has a, it's just that.
*  What's your favorite smart device for you?
*  My light.
*  Light.
*  And now you have the smart plug with,
*  and you don't, we also have this echo plug, which is-
*  Oh yeah, you can plug in anything.
*  You can plug anything, and now you can turn
*  that one on and off.
*  I use this conversation motivation
*  and get one and something.
*  The garage door, you can check your status
*  of the garage door and things like,
*  and we have gone, make Alexa more and more proactive,
*  where it even has hunches now that,
*  or looks hunches like you left your light on.
*  Let's say you've gone to your bed
*  and you left the garage light on.
*  So it will help you out in these settings, right?
*  That's smart devices.
*  Information smart devices, you said music.
*  So I don't remember everything we had,
*  but alarms, timers were the big ones.
*  That was, the timers were very popular right away.
*  Music also, you could play, song, artist, album, everything.
*  So that was a clear win in terms of the customer experience.
*  So that's, again, this is language understanding.
*  Now things have evolved, right?
*  So where we want Alexa definitely to be more accurate,
*  competent, trustworthy,
*  based on how well it does these core things.
*  But we have evolved in many different dimensions.
*  First is what I think of it as being more conversational
*  for high utility, not just for chat, right?
*  And there at Remars this year, which is our AI conference,
*  we launched what is called Alexa Conversations.
*  That is providing the ability for developers
*  to author multi-turn experiences on Alexa
*  with no code essentially,
*  where in terms of the dialogue code.
*  Initially it was like, all these IVR systems,
*  you have to fully author,
*  if the customer says this, do that, right?
*  So the whole dialogue flow is hand authored.
*  And with Alexa Conversations,
*  the way it is that you just provide a sample interaction data
*  with your service or an API,
*  let's say your atom tickets that provides a service
*  buying movie tickets.
*  You provide a few examples of how your customers
*  will interact with your APIs.
*  And then the dialogue flow is automatically constructed
*  using a recurrent neural network trained on that data.
*  So that simplifies the developer experience.
*  We just launched our preview for the developers
*  to try this capability out.
*  And then the second part of it,
*  which shows even increased utility for customers,
*  is you and I, when we interact with Alexa or any customer,
*  as I'm coming back to our initial part of the conversation,
*  the goal is often unclear or unknown to the AI.
*  If I say, Alexa, what movies are playing nearby?
*  Am I trying to just buy movie tickets?
*  Am I actually even,
*  do you think I'm looking for just movies for curiosity,
*  whether the Avengers is still in theater or when is it?
*  Maybe it's gone and maybe it will come on my Mistletoe.
*  So I may watch it on Prime, which happened to me.
*  So from that perspective now,
*  you're looking into what is my goal?
*  And let's say I now complete the movie ticket purchase.
*  Maybe I would like to get dinner nearby.
*  So what is really the goal here?
*  Is it night out or is it movies?
*  As in just go watch a movie?
*  The answer is, we don't know.
*  So can Alexa now, figure we have the intelligence
*  that I think this meta goal is really night out
*  or at least say to the customer,
*  when you have completed the purchase of movie tickets
*  from Atom tickets or Fandango or Picure, anyone,
*  then the next thing is,
*  do you want to get an Uber to the theater?
*  Or do you want to book a restaurant next to it?
*  And then not ask the same information over and over again,
*  what time, how many people in your party, right?
*  So this is where you shift the cognitive burden
*  from the customer to the AI,
*  where it's thinking of what is your,
*  it anticipates your goal
*  and takes the next best action to complete it.
*  Now that's the machine learning problem.
*  But essentially the way we saw this first instance,
*  and we have a long way to go to make it scale
*  to everything possible in the world,
*  but at least for this situation,
*  it is from at every instance,
*  Alexa is making the determination
*  whether it should stick with the experience
*  with Atom tickets or offer you,
*  based on what you say,
*  whether either you have completed the interaction
*  or you said, no, get me an Uber now.
*  So it will shift context into another experience or skill
*  or another service.
*  So that's a dynamic decision-making.
*  That's making Alexa, you can say more conversational
*  for the benefit of the customer,
*  rather than simply complete transactions,
*  which are well thought through.
*  You as a customer has fully specified
*  what you want to be accomplished.
*  It's accomplishing that.
*  So it's kind of as,
*  we do this with pedestrians, right?
*  Intent modeling is predicting
*  what your possible goals are,
*  and what's the most likely goal,
*  and then switching that depending on the things you say.
*  So my question is there,
*  it seems maybe it's a dumb question,
*  but it would help a lot if Alexa remembered me,
*  what I said previously.
*  Right.
*  Is it trying to use some memory for the customer?
*  Yeah, it is using a lot of memory within that.
*  So right now, not so much in terms of,
*  okay, which restaurant do you prefer, right?
*  That is a more long-term memory,
*  but within the short-term memory within the session,
*  it is remembering how many people did you,
*  so if you said buy four tickets,
*  now it has made an implicit assumption
*  that you are gonna have,
*  you need at least four seats at a restaurant, right?
*  So these are the kind of contexts it's preserving
*  between these skills, but within that session.
*  But you're asking the right question
*  in terms of for it to be more and more useful,
*  it has to have more long-term memory,
*  and that's also an open question.
*  Again, these are still early days.
*  So for me, I mean, everybody's different,
*  but yeah, I'm definitely not representative
*  of the general population in the sense
*  that I do the same thing every day.
*  Like I eat the same, I do everything the same thing.
*  Wear the same thing clearly, this or the black shirt.
*  So it's frustrating when Alexa doesn't get what I'm saying
*  because I have to correct her every time
*  in the exact same way.
*  This has to do with certain songs.
*  She doesn't know certain weird songs I like.
*  And doesn't know, I've complained to Spotify about this,
*  talked to the head of RID at Spotify,
*  it's Stairway to Heaven.
*  I have to correct it every time.
*  It doesn't play Led Zeppelin correctly.
*  It plays cover of Stairway to Heaven.
*  You should send me your, next time it fails,
*  feel free to send it to me, we'll take care of it.
*  Okay, well.
*  Because Led Zeppelin is one of my favorite.
*  It's awesome.
*  It works for me, so I'm shocked it doesn't work for you.
*  This is an official bug report.
*  I'll make it public, I'll make everybody retweet it.
*  We're gonna fix the Stairway to Heaven problem.
*  Anyway, but the point is,
*  I'm pretty boring and do the same things,
*  but I'm sure most people do the same set of things.
*  Do you see Alexa sort of utilizing that in the future
*  for improving the experience?
*  Yes, and not only utilizing, it's already doing some of it.
*  We call it, where Alexa is becoming more self-learning.
*  So Alexa is now auto-correcting millions and millions
*  of utterances in the US
*  without any human supervision involved.
*  The way it does it is, let's take an example
*  of a particular song didn't work for you.
*  What do you do next?
*  You either, it played the wrong song,
*  and you said, Alexa, no, that's not the song I want,
*  or you say, Alexa, play that, you try it again.
*  And that is a signal to Alexa
*  that she may have done something wrong.
*  And from that perspective, we can learn
*  if there's that failure pattern or that action
*  of song A was played when song B was requested.
*  And it's very common with station names,
*  because play NPR, you can have NB confused as an M,
*  and then you, for a certain accent like mine,
*  people confuse my N and M all the time.
*  Because I have an Indian accent,
*  they're confusable to humans.
*  It is for Alexa too.
*  And in that part, but it starts auto-correcting,
*  and we collect, we correct a lot of these automatically
*  without a human looking at the failures.
*  So one of the things that's for me missing in Alexa,
*  I don't know if I'm a representative customer,
*  but every time I correct it,
*  it would be nice to know that that made a difference.
*  You know what I mean?
*  Like the sort of like, I heard you.
*  Like sort of-
*  Some acknowledgement of that.
*  We work a lot with Tesla, we study Autopilot and so on.
*  And a large amount of the customers
*  that use Tesla Autopilot,
*  they feel like they're always teaching the system.
*  They're almost excited by the possibility
*  that they're teaching.
*  I don't know if Alexa customers generally think of it
*  as they're teaching to improve the system.
*  And that's a really powerful thing.
*  I would say it's a spectrum.
*  Some customers do think that way,
*  and some would be annoyed by Alexa acknowledging that.
*  So there's, again, no one,
*  while there are certain patterns,
*  not everyone is the same in this way.
*  But we believe that, again, customers helping Alexa
*  is a tenet for us in terms of improving it.
*  And more self-learning is by, again,
*  this is like fully unsupervised, right?
*  There is no human in the loop and no labeling happening.
*  And based on your actions as a customer,
*  Alexa becomes smarter.
*  Again, it's early days,
*  but I think this whole area of teachable AI
*  is gonna get bigger and bigger in the whole space,
*  especially in the AI assistant space.
*  So that's the second part where,
*  I mentioned more conversational,
*  this is more self-learning.
*  The third is more natural.
*  And the way I think of more natural
*  is we talked about how Alexa sounds.
*  And we have done a lot of advances in our text-to-speech
*  by using, again, neural network technology
*  for it to sound very human-like.
*  From the individual texture of the sound
*  to the timing, the tone, everything.
*  Everything, I would think, in terms of,
*  there's a lot of controls in each of the places for how,
*  I mean, the speed of the voice, the prosthetic patterns,
*  the actual smoothness of how it sounds.
*  All of those are factored in.
*  We do a ton of listening tests to make sure it works that.
*  But naturalness, how it sounds should be very natural.
*  How it understands requests is also very important.
*  And in terms of, we have 95,000 skills,
*  and if we have, imagine that,
*  in many of these skills, you have to remember the skill name.
*  And say, Alexa, ask the tied skill to tell me X.
*  Now, if you have to remember the skill name,
*  that means the discovery and the interaction is unnatural.
*  And we are trying to solve that by what we think of as,
*  again, you don't have to have the app metaphor here.
*  These are not individual apps, right?
*  Even though they're, so you're not sort of opening one
*  at a time and interacting.
*  It should be seamless because it's voice.
*  And when it's voice, you have to be able to understand
*  these requests, independent of the specificity,
*  like a skill name.
*  And to do that, what we have done is, again,
*  built a deep learning-based capability
*  where we shortlist a bunch of skills when you say,
*  Alexa, get me a car, and then we figure it out.
*  Okay, it's meant for an Uber skill versus a Lyft,
*  or based on your preferences.
*  And then you can rank the responses from the skill
*  and then choose the best response for the customer.
*  So that's on the more natural,
*  other examples of more natural is like,
*  we were talking about lists, for instance,
*  and you don't wanna say, Alexa, add milk,
*  Alexa, add eggs, Alexa, add cookies.
*  No, Alexa, add cookies, milk, and eggs,
*  and that in one shot, right?
*  So that works, that helps with the naturalness.
*  We talked about memory.
*  Like if you said, you can say, Alexa, remember,
*  I have to go to mom's house,
*  or you may have entered a calendar event
*  through your calendar that's linked to Alexa.
*  You don't wanna remember whether it's in my calendar,
*  or did I tell you to remember something
*  or some other reminder, right?
*  So you have to now, independent of how customers
*  create these events, it should just say,
*  Alexa, when do I have to go to mom's house?
*  And it tells you when you have to go to mom's house.
*  That's a fascinating problem.
*  Who's that problem on?
*  So there's people who create skills.
*  Who's tasked with integrating all of that knowledge
*  together so the skills become seamless?
*  Is it the creators of the skills,
*  or is it an infrastructure that Alexa provides problem?
*  It's both.
*  I think the large problem in terms of making sure
*  your skill quality is high, that has to be done
*  by our tools, because it's just,
*  so these skills, just to put the context,
*  they are built through Alexa's SkillSkip,
*  which is a self-serve way of building
*  an experience on Alexa.
*  This is like any developer in the world
*  could go to Alexa's SkillSkit
*  and build an experience on Alexa.
*  Like if you're a dominoes, you can build a domino skills.
*  For instance, that does pizza ordering.
*  When you have authored that, you do want to now,
*  if people say Alexa open dominoes,
*  or Alexa ask dominoes to get a particular type of pizza,
*  that will work, but the discovery is hard.
*  You can't just say, Alexa, get me a pizza,
*  and then Alexa figures out what to do.
*  That latter part is definitely our responsibility
*  in terms of when the request is not fully specific,
*  how do you figure out what's the best skill
*  or a service that can fulfill the customer's request?
*  And it can keep evolving.
*  Imagine going to the situation I said,
*  which was the night out planning,
*  that the goal could be more than that individual request
*  that came up.
*  A pizza ordering could mean a night in,
*  where you're having an event with your kids
*  in your house, and you're,
*  so this is welcome to the world of conversational AI.
*  This is super exciting,
*  because it's not the academic problem of NLP,
*  of natural English processing, understanding, dialogue.
*  This is like real world.
*  And the stakes are high in a sense
*  that customers get frustrated quickly,
*  people get frustrated quickly,
*  so you have to get it right.
*  You have to get that interaction right.
*  So it's, I love it.
*  But so from that perspective,
*  what are the challenges today?
*  What are the problems that really need to be solved
*  in the next few years?
*  What's the focus?
*  I think first and foremost, as I mentioned that,
*  to get the basics right is still true.
*  Basically, even the one-shot requests,
*  which we think of as transactional requests,
*  needs to work magically.
*  No question about that.
*  If it doesn't turn your light on and off,
*  you'll be super frustrated.
*  Even if I can complete the night out for you
*  and not do that, that is unacceptable as a customer, right?
*  So that, you have to get the foundational understanding
*  going very well.
*  The second aspect, when I said more conversational,
*  as you imagine, is more about reasoning.
*  It is really about figuring out what the latent goal is
*  of the customer based on what I have the information now
*  and the history.
*  What's the next best thing to do?
*  So that's a complete reasoning and decision-making problem,
*  just like your self-driving car,
*  but the goal is still more finite.
*  Here, it evolves.
*  Your environment is super hard in self-driving
*  and the cost of a mistake is huge.
*  But there are certain similarities,
*  but if you think about how many decisions Alexa is making
*  or evaluating at any given time,
*  it's a huge hypothesis space.
*  And we're only talked about so far
*  about what I think of reactive decision
*  in terms of you asked for something
*  and Alexa is reacting to it.
*  If you bring the proactive part,
*  which is Alexa having hunches,
*  so any given instance, then it's really a decision
*  at any given point based on the information,
*  Alexa has to determine what's the best thing it needs to do.
*  So these are the ultimate AI problem
*  about decisions based on the information you have.
*  Do you think, just from my perspective,
*  I work a lot with sensing of the human face.
*  Do you think they'll,
*  and we touched this topic a little bit earlier,
*  but do you think it'll be a day soon
*  when Alexa can also look at you
*  to help improve the quality of the hunch it has,
*  or at least detect frustration,
*  or improve the quality of its perception
*  of what you're trying to do?
*  I mean, let me again bring back to what it already does.
*  We talked about how based on you barge in over Alexa,
*  clearly it's a very high probability
*  it must have done something wrong.
*  That's why you barged in.
*  The next extension of whether frustration
*  is a signal or not, of course, is a natural thought
*  in terms of how that should be in a signal to it.
*  You can get that from voice.
*  You can get it from voice, but it's very hard.
*  Like, I mean, frustration as a signal,
*  historically, if you think about emotions of different kinds,
*  there's a whole field of affective computing,
*  something that MIT has also done a lot of research in,
*  is super hard.
*  And you're now talking about a far-field device,
*  as in you're talking to a distance, noisy environment,
*  and in that environment,
*  it needs to have a good sense for your emotions.
*  This is a very, very hard problem.
*  Very hard problem, but you haven't shied away
*  from hard problems.
*  Well, so deep learning has been at the core
*  of a lot of this technology.
*  Are you optimistic about the current deep learning approaches
*  to solving the hardest aspects of what we're talking about?
*  Or do you think there will come a time
*  where new ideas need to, if you look at reasoning,
*  so OpenAI, DeepMind, a lot of folks are now starting
*  to work in reasoning,
*  trying to see how we can make neural networks reason.
*  Do you see that new approaches need to be invented
*  to take the next big leap?
*  Absolutely, I think there has to be a lot more investment,
*  and I think in many different ways.
*  And there are these, I would say,
*  nuggets of research forming in a good way,
*  like learning with less data,
*  or zero-shot learning, one-shot learning.
*  And the active learning stuff you've talked about
*  is incredible stuff.
*  Transfer learning is also super critical,
*  especially when you're thinking about applying knowledge
*  from one task to another or one language to another.
*  It's really ripe.
*  So these are great pieces.
*  Deep learning has been useful too,
*  and now we are sort of marrying deep learning
*  with transfer learning and active learning.
*  Of course, that's more straightforward
*  in terms of applying deep learning
*  in an active learning setup.
*  But I do think in terms of now looking
*  into more reasoning-based approaches is going to be key
*  for our next wave of the technology.
*  But there is a good news.
*  The good news is that I think
*  for keeping on to delight customers,
*  that a lot of it can be done by prediction tasks.
*  And so we haven't exhausted that.
*  So we don't need to give up
*  on the deep learning approaches for that.
*  So that's just, I wanted to sort of point that out.
*  Creating a rich, fulfilling, amazing experience
*  that makes Amazon a lot of money,
*  and a lot of everybody a lot of money,
*  because it does awesome things, deep learning is enough.
*  The point-
*  I don't think, I wouldn't say deep learning is enough.
*  I think for the purposes of Alexa,
*  accomplish the task for customers,
*  I'm saying there are still a lot of things we can do
*  with prediction-based approaches that do not reason.
*  I'm not saying that, and we haven't exhausted those,
*  but for the kind of high utility experiences
*  that I'm personally passionate about
*  of what Alexa needs to do, reasoning has to be solved.
*  To the same extent as you can think of
*  natural language understanding and speech recognition,
*  to the extent of understanding intents
*  has been how accurate it has become.
*  But reasoning, we have very, very early days.
*  Let me ask that another way.
*  How hard of a problem do you think that is?
*  Hardest of them.
*  I would say hardest of them, because again,
*  the hypothesis space is really, really large.
*  And when you go back in time, like you were saying,
*  I want Alexa to remember more things,
*  that once you go beyond a session of interaction,
*  which is by session, I mean a time span, which is today,
*  to versus remembering which restaurant I like,
*  and then when I'm planning a night out to say,
*  do you wanna go to the same restaurant?
*  Now you're up the stakes big time.
*  And this is where the reasoning dimension
*  also goes way, way bigger.
*  So you think the space,
*  we'll be elaborating that a little bit,
*  just philosophically speaking,
*  do you think when you reason about trying to model
*  what the goal of a person is
*  in the context of interacting with Alexa,
*  you think that space is huge?
*  It's huge, absolutely huge.
*  Do you think, so like another sort of devil's advocate
*  would be that we human beings are really simple
*  and we all want like just a small set of things?
*  So do you think it's possible,
*  because we're not talking about
*  a fulfilling general conversation,
*  perhaps actually the Alexa Prize is a little bit more about
*  after that.
*  Creating a customer, like there's so many
*  of the interactions, it feels like are clustered
*  in groups that don't require general reasoning.
*  I think, yeah, you're right in terms of the head
*  of the distribution of all the possible things
*  customers may wanna accomplish.
*  But the tail is long and it's diverse, right?
*  So from that-
*  There's many long tails.
*  So from that perspective,
*  I think you have to solve that problem,
*  otherwise, and everyone's very different.
*  Like, I mean, we see this already
*  in terms of the skills, right?
*  I mean, if you're an avid surfer, which I am not, right?
*  But somebody is asking Alexa about surfing conditions,
*  right?
*  And there's a skill that is there for them to get to, right?
*  That tells you that the tail is massive.
*  Like in terms of like what kind of skills people have created,
*  it's humongous in terms of it,
*  and which means there are these diverse needs.
*  And when you start looking at the combinations of these,
*  even if you're at pairs of skills and 90,000 choose two,
*  it's still a big combination.
*  So I'm saying there's a huge to-do here now.
*  And I think customers are wonderfully frustrated with things
*  and they have to keep getting to do better things for them.
*  And they're not known to be super patient.
*  So you have to-
*  Do it fast.
*  You have to do it fast.
*  So you've mentioned the idea of a press release
*  that research and development,
*  Amazon Alexa and Amazon in general,
*  you kind of think of what the future product will look like
*  and you kind of make it happen.
*  You work backwards.
*  So can you draft for me,
*  you probably already have one,
*  but can you make up one for 10, 20, 30, 40 years out
*  that you see the Alexa team putting out
*  just in broad strokes, something that you dream about?
*  I think let's start with the five years first.
*  And I'll get to the 40 years too hard to think.
*  Because I'm pretty sure you have a real five year one.
*  I didn't want to, but yeah, in broad strokes,
*  let's start with five years.
*  I think the five year is where,
*  I mean, I think of in these spaces, it's hard,
*  especially if you're in thick of things
*  to think beyond the five year space
*  because a lot of things change.
*  I mean, if you asked me five years back,
*  will Alexa will be here?
*  I think it has surpassed my imagination of that time.
*  So I think from the next five years perspective,
*  from a AI perspective, what we're gonna see
*  is that notion which you said goal oriented dialogues
*  and open domain like Alexa Prize,
*  I think that bridge is gonna get closed.
*  They won't be different.
*  And I'll give you why that's the case.
*  You mentioned shopping.
*  How do you shop?
*  Do you shop in one shot?
*  Sure, your double A batteries, paper towels, yes.
*  How long does it take for you to buy a camera?
*  You do ton of research, then you make a decision.
*  So is that a goal oriented dialogue
*  when somebody says, Alexa, find me a camera?
*  Is it simply inquisitiveness?
*  So even in the something that you think of it as shopping,
*  which you said you yourself use a lot of,
*  if you go beyond where it's reorders or items
*  where you sort of are not brand conscious and so forth.
*  That was just in shopping.
*  Just to comment quickly,
*  I've never bought anything through Alexa
*  that I haven't bought before on Amazon on the desktop
*  after I clicked in a bunch of, read a bunch of reviews,
*  that kind of stuff.
*  So it's repurchase.
*  So now you think in, even for something that you felt like
*  is a finite goal, I think the space is huge
*  because even products, the attributes are many,
*  and you wanna look at reviews, some on Amazon,
*  some outside, some you wanna look at what CNET is saying
*  or another consumer forum is saying
*  about even a product, for instance.
*  So that's just shopping where you could argue
*  the ultimate goal is sort of known.
*  And we haven't talked about, Alexa,
*  what's the weather in Cape Cod this weekend?
*  So why am I asking that weather question?
*  So I think of it as how do you complete goals
*  with minimum steps for our customers?
*  And when you think of it that way,
*  the distinction between goal-oriented and conversations
*  for open domain say goes away.
*  I may wanna know what happened in the presidential debate.
*  And is it, I'm seeking just information
*  and I'm looking at who's winning the debates.
*  So these are all quite hard problems.
*  So even the five-year horizon problem,
*  I'm like, I sure hope we'll solve these.
*  And you're optimistic, because that's a hard problem.
*  Which part?
*  The reasoning enough to be able to help explore
*  complex goals that are beyond something simplistic.
*  That feels like it could be, well, five years is a nice.
*  Is a nice bar for them, right?
*  I think you will, it's a nice ambition.
*  And do we have press releases for that?
*  Absolutely, can I tell you what specifically
*  the roadmap will be?
*  No, right?
*  And what, and will we solve all of it
*  in the five-year space?
*  No, this is, we will work on this forever, actually.
*  This is the hardest of the AI problems.
*  And I don't see that being solved even in a 40-year horizon
*  because even if you limit to the human intelligence,
*  we know we are quite far from that.
*  In fact, every aspect of our sensing to neural processing
*  to how brain stores information and how it processes it,
*  we don't yet know how to represent knowledge.
*  So we are still in those early stages.
*  So I wanted to start, that's why at the five-year,
*  because the five-year success would look like that
*  in solving these complex goals.
*  And the 40-year would be where it's just natural
*  to talk to these in terms of more of these complex goals.
*  Right now, we've already come to the point
*  where these transactions you mentioned
*  of asking for weather or reordering something
*  or listening to your favorite tune,
*  it's natural for you to ask Alexa.
*  It's now unnatural to pick up your phone, right?
*  And that I think is the first five-year transformation.
*  The next five-year transformation would be,
*  okay, I can plan my weekend with Alexa
*  or I can plan my next meal with Alexa
*  or my next night out with seamless effort.
*  So just to pause and look back at the big picture of it all,
*  you're part of a large team that's creating a system
*  that's in the home, that's not human,
*  that gets to interact with human beings.
*  So we human beings, we these descendants of apes,
*  have created an artificial intelligence system
*  to have conversations.
*  I mean, that to me,
*  the two most transformative robots of this century,
*  I think, will be autonomous vehicles,
*  but they're a little bit transformative
*  in a more boring way.
*  It's like a tool.
*  I think conversational agents in the home
*  is like an experience.
*  How does that make you feel
*  that you're at the center of creating that?
*  Do you sit back in awe sometimes?
*  What is your feeling about the whole mess of it?
*  Can you even believe that we're able
*  to create something like this?
*  I think it's a privilege.
*  I'm so fortunate where I ended up.
*  And it's been a long journey.
*  I've been in this space for a long time in Cambridge
*  and it's so heartwarming to see the kind of adoption
*  conversational agents are having now.
*  Five years back, it was almost like,
*  should I move out of this?
*  Because we are unable to find this killer application
*  that customers would love
*  that would not simply be a good to have thing
*  in research labs.
*  And it's so fulfilling to see it make a difference
*  to millions and billions of people worldwide.
*  The good thing is that it's still very early.
*  So I have another 20 years of job security
*  doing what I love.
*  So I think from that perspective,
*  I tell every researcher that joins
*  or every member of my team,
*  that this is a unique privilege.
*  And I would say not just launching Alexa in 2014,
*  which was first of its kind.
*  Along the way we have,
*  when we launched Alexa skills kit,
*  it became democratizing AI.
*  Before that, there was no good evidence
*  of an SDK for speech and language.
*  Now we are coming to this
*  where you and I are having this conversation
*  where I'm not saying,
*  oh Lex, planning a night out with an AI agent,
*  impossible.
*  I'm saying it's in the realm of possibility.
*  And not only possibility, we'll be launching this.
*  So some elements of that,
*  it will keep getting better.
*  We know that is a universal truth.
*  Once you have these kinds of agents out there being used,
*  they get better for your customers.
*  And I think that's where,
*  I think the amount of research topics we are throwing out
*  at our budding researchers
*  is just gonna be exponentially hard.
*  And the great thing is you can now
*  get immense satisfaction by having customers use it,
*  not just a paper and NeurIPS or another conference.
*  I think everyone, myself included,
*  are deeply excited about that feature.
*  So I don't think there's a better place to end.
*  Rohit, thank you so much for talking to us.
*  This was fun.
*  Thank you, same here.
*  Thanks for listening to this conversation
*  with Rohit Prasad.
*  And thank you to our presenting sponsor, Cash App.
*  Download it, use code LexPodcast,
*  you'll get $10 and $10 will go to FIRST,
*  a STEM education nonprofit
*  that inspires hundreds of thousands of young minds
*  to learn and to dream of engineering our future.
*  If you enjoy this podcast, subscribe on YouTube,
*  give it five stars on Apple Podcast,
*  support it on Patreon, or connect with me on Twitter.
*  And now let me leave you with some words of wisdom
*  from the great Alan Turing.
*  Sometimes it is the people no one can imagine anything of
*  who do the things no one can imagine.
*  Thank you for listening and hope to see you next time.
