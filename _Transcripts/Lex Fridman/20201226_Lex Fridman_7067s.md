---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 7067s
Video Keywords: ['charles isbell and michael littman', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 196104
Video Rating: None
Video Description: Charles Isbell is the Dean of the College of Computing at Georgia Tech. Michael Littman is a computer scientist at Brown University. Please support this podcast by checking out our sponsors:
- Athletic Greens: https://athleticgreens.com/lex and use code LEX to get 1 month of fish oil
- Eight Sleep: https://www.eightsleep.com/lex and use code LEX to get special savings
- MasterClass: https://masterclass.com/lex to get 2 for price of 1
- Cash App: https://cash.app/ and use code LexPodcast to get $10

EPISODE LINKS:
Charles's Twitter: https://twitter.com/isbellHFh
Charles's Website: https://www.cc.gatech.edu/~isbell/
Michael's Twitter: https://twitter.com/mlittmancs
Michael's Website: https://www.littmania.com/
Michael's YouTube: https://www.youtube.com/user/mlittman

PODCAST INFO:
Podcast website: https://lexfridman.com/podcast
Apple Podcasts: https://apple.co/2lwqZIr
Spotify: https://spoti.fi/2nEwCF8
RSS: https://lexfridman.com/feed/podcast/
Full episodes playlist: https://www.youtube.com/playlist?list=PLrAXtmErZgOdP_8GztsuKi9nrraNbKKp4
Clips playlist: https://www.youtube.com/playlist?list=PLrAXtmErZgOeciFP3CBCIEElOJeitOr41

OUTLINE:
0:00 - Introduction
2:27 - Is machine learning just statistics?
6:49 - NeurIPS vs ICML
9:05 - Data is more important than algorithm
14:49 - The role of hardship in education
23:33 - How Charles and Michael met
28:05 - Key to success: never be satisfied
31:23 - Bell Labs
42:50 - Teaching machine learning
53:01 - Westworld and Ex Machina
1:01:00 - Simulation
1:07:49 - The college experience in the times of COVID
1:36:27 - Advice for young people
1:43:19 - How to learn to program
1:54:43 - Friendship

CONNECT:
- Subscribe to this YouTube channel
- Twitter: https://twitter.com/lexfridman
- LinkedIn: https://www.linkedin.com/in/lexfridman
- Facebook: https://www.facebook.com/LexFridmanPage
- Instagram: https://www.instagram.com/lexfridman
- Medium: https://medium.com/@lexfridman
- Support on Patreon: https://www.patreon.com/lexfridman
---

# Charles Isbell and Michael Littman Machine Learning and Education  Lex Fridman Podcast #148
**Lex Fridman:** [December 26, 2020](https://www.youtube.com/watch?v=yzMVEbs8Zz0)
*  The following is a conversation with Charles Isbell and Michael Littman.
*  Charles is the Dean of the College of Computing at Georgia Tech, and Michael is a computer
*  science professor at Brown University.
*  I've spoken with each of them individually on this podcast, and since they are good friends
*  in real life, we all thought it would be fun to have a conversation together.
*  Quick mention of each sponsor, followed by some thoughts related to the episode.
*  Thank you to Athletic Greens, the only one drink that I start every day with to cover
*  all my nutritional bases, 8 Sleep, a mattress that cools itself and gives me yet another
*  reason to enjoy sleep, Masterclass, online courses from some of the most amazing humans
*  in history, and Cash App, the app I use to send money to friends.
*  Please check out these sponsors in the description to get a discount and to support this podcast.
*  As a side note, let me say that having two guests on the podcast is an experiment that
*  I've been meaning to do for a while.
*  In particular, because down the road, I would like to occasionally be a kind of moderator
*  for debates between people that may disagree in some interesting ways.
*  If you have suggestions for who you would like to see debate on this podcast, let me
*  know.
*  As with all experiments of this kind, it is a learning process.
*  Both the video and the audio might need improvement.
*  I realized I think I should probably do three or more cameras next time as opposed to just
*  two, and also try different ways to mount the microphone for the third person.
*  Also, after recording this intro, I'm going to have to go figure out the thumbnail for
*  the video version of the podcast.
*  Since I usually put the guest's head on the thumbnail, and now there's two heads and two
*  names to try to fit into the thumbnail.
*  It's a kind of bin packing problem, which in theoretical computer science happens to
*  be an NP-hard problem.
*  Whatever I come up with, if you have better ideas for the thumbnail, let me know as well.
*  In general, I always welcome ideas how this thing can be improved.
*  If you enjoy it, subscribe on YouTube, review it with Five Stars on Apple Podcast, follow
*  on Spotify, support on Patreon, or connect with me on Twitter at Lex Friedman.
*  And now here's my conversation with Charles Isbell and Michael Litman.
*  You'll probably disagree about this question, but what is your biggest, would you say, disagreement
*  about either something profound and very important or something completely not important at all?
*  I don't think I have any disagreements at all.
*  I'm not sure that's true.
*  We walked into that one, didn't we?
*  So one thing that you sometimes mention is that, and we did this one on air too, as it
*  were, whether or not machine learning is computational statistics.
*  It's not.
*  But it is.
*  Well, it's not.
*  And in particular, and more importantly, it is not just computational statistics.
*  So what's missing in the picture?
*  All the rest of it.
*  What's missing?
*  That which is missing.
*  Oh, well, you can't be wrong now.
*  Well, it's not just the statistics.
*  He doesn't even believe this.
*  We've had this conversation before.
*  If it were just the statistics, then we would be happy with where we are.
*  But it's not just the statistics.
*  That's why it's computational statistics.
*  Or if it were just the computational statistics.
*  I agree that machine learning is not just statistics.
*  It is not just statistics.
*  We can agree on that.
*  Nor is it just computational statistics.
*  It's computational statistics.
*  It is computational.
*  What is the computational and computational statistics?
*  Does this take us into the realm of computing?
*  It does, but I think perhaps the way I can get him to admit that he's wrong is that it's
*  about rules.
*  It's about rules.
*  It's about symbols.
*  It's about all these other things.
*  But statistics is not about rules?
*  I'm going to say statistics is about rules.
*  But it's not just the statistics.
*  It's not just a random variable that you choose and you have a probability.
*  I think you have a narrow view of statistics.
*  Okay, well then what would be the broad view of statistics that would still allow it to
*  be statistics and not say history that would make computational statistics okay?
*  Well, okay.
*  So I had my first sort of research mentor, a guy named Tom Landauer, taught me to do
*  some statistics, right?
*  And I was annoyed all the time because the statistics would say that what I was doing
*  was not statistically significant.
*  And I was like, but, but, but, and basically what he said to me is statistics is how you're
*  going to keep from lying to yourself, which I thought was really deep.
*  It is a way to keep yourself honest in a particular way.
*  I agree with that.
*  Yeah.
*  And so you're trying to find rules.
*  I'm just kind of bringing back to rules.
*  Wait, wait, wait.
*  Could you possibly try to define rules?
*  Even regular statisticians, non-computational statisticians, do spend some of their time
*  evaluating rules, right?
*  Applying statistics to try to understand, does this rule capture this?
*  Does this not capture this?
*  You mean like hypothesis testing kind of thing?
*  Sure.
*  Or like confidence intervals?
*  I think more like hypothesis.
*  I feel like the word statistic literally means like a summary, like a number that summarizes
*  other numbers.
*  Right.
*  So that's why statistics actually applies that idea to things like rules, to understand
*  whether or not a rule is valid.
*  So software engineering statistics?
*  No.
*  Programming languages, statistics?
*  No.
*  Because I think there's a very, it's useful to think about a lot of what AI and machine
*  learning is, or certainly should be, as software engineering, as programming languages.
*  Just if, to put it in language that you might understand, the hyperparameters beyond the
*  problem itself.
*  The hyperparameters is too many syllables for me to understand.
*  The hyperparameters.
*  That's better.
*  That goes around it, right?
*  It's the decisions you choose to make.
*  It's the metrics you choose to use.
*  It's the loss function.
*  So you want to say the practice of machine learning is different than the practice of
*  statistics?
*  Like the things you have to worry about and how you worry about them are different, therefore
*  they're different.
*  Right.
*  At a very little, I mean at the very least.
*  It's that much is true.
*  It doesn't mean that statistics, computational or otherwise, aren't important.
*  I think they are.
*  I mean, I do a lot of that, for example.
*  But I think it goes beyond that.
*  I think that we could think about game theory in terms of statistics, but I don't think
*  it's very as useful to do.
*  I mean, the way I would think about it, or a way I would think about it is this way.
*  Chemistry is just physics.
*  But I don't think it's as useful to think about chemistry as being just physics.
*  It's useful to think about it as chemistry.
*  The level of abstraction really matters here.
*  So I think it is, there are contexts in which it is useful.
*  Yes.
*  I think that way, right?
*  So finding that connection is actually helpful.
*  And I think that's when I emphasize the computational statistics thing.
*  I think I want to befriend statistics and not absorb them.
*  Here's the A way to think about it beyond what I just said, right?
*  So what would you say, and I want you to think back to a conversation we had a very long
*  time ago, what would you say is the difference between, say, the early 2000s, ICML and what
*  we used to call MIPS, NURBS?
*  Is there a difference, particularly on the machine learning that was done there?
*  ICML was around that long.
*  So ICLR is the new conference, newish.
*  Yeah, I guess so.
*  And ICML was around the 2000s.
*  Oh, ICML predates that.
*  I think my most cited ICML paper is from 94.
*  Michael knows this better than me because, of course, he's significantly older than I
*  am.
*  But the point is, what is the difference between ICML and NURBS in the late 90s, early 2000s?
*  I don't know what everyone else's perspective would be, but I had a particular perspective
*  at that time.
*  ICML was more of a computer science place and that NURBS was more of an engineering
*  place, like the kind of math that happened at the two places.
*  As a computer scientist, I felt more comfortable with the ICML math and the NURBS people would
*  say that that's because I'm dumb.
*  And that's such an engineering thing to say.
*  I agree with that part of it, but I do a little differently.
*  We actually had a nice conversation with Tom D. Trigger about this on Twitter just a couple
*  days ago.
*  I put it a little differently, which is that ICML was machine learning done by computer
*  scientists and NURBS was machine learning done by computer scientists trying to impress
*  statisticians.
*  Which was weird because it was the same people, at least by the time I started paying attention,
*  but it just felt very, very different.
*  And I think that that perspective of whether you're trying to impress the statisticians
*  or you're trying to impress the programmers is actually very different and has real impact
*  on what...
*  What you choose to worry about and what kind of outcomes you come to.
*  So I think it really matters.
*  I think computer statistics is a means to an end.
*  It is not an end in some sense.
*  And I think that really matters here in the same way that I don't think computer science
*  is just engineering or just science or just math or whatever.
*  Okay.
*  So I'd have to now agree that now we agree on everything.
*  Yes.
*  Yes.
*  The important thing here is that my opinions may have changed, but not the fact that I'm
*  right I think is what we just came to.
*  Right.
*  And my opinions may have changed and not the fact that I'm wrong.
*  That's right.
*  You lost me.
*  I'm not even...
*  I think I lost myself there too.
*  But anyway, we're back.
*  This happens to us sometimes.
*  We're sorry.
*  How does neural networks change this, just to even linger on this topic, change this
*  idea of statistics, how big of a pie statistics is within the machine learning thing?
*  Because it sounds like hyperparameters and also just the role of data.
*  So I started to use the terminology of software 2.0, which is like the act of programming
*  as a...
*  Like you're a designer in the hyperparameter space of neural networks and you're also the
*  collector and the organizer and the cleaner of the data.
*  And that's part of the programming.
*  So how did...
*  On the NeurIPS versus ICML topic, what's the role of neural networks in redefining the
*  size and the role of machine learning?
*  I can't wait to hear what Michael thinks about this, but I would add one...
*  But you will.
*  But that's true.
*  I will.
*  I'll force myself to.
*  I think there's one other thing I would add to your description, which is the kind of
*  software engineering part is what does it mean to debug, for example.
*  But this is a difference between the kind of computational statistics view of machine
*  learning and the computational view of machine learning, which is I think one is worried
*  about the equation as it were.
*  And by the way, this is not a value judgment.
*  I just think it's about perspective.
*  But the kind of questions you would ask when you start asking yourself what does it mean
*  to program and develop and build the system is a very computer sciency view of the problem.
*  If you get on data science Twitter and econ Twitter, you actually hear this a lot with
*  the economist and the data scientist complaining about the machine learning people.
*  It's just statistics.
*  And I don't know why they don't see this, but they're not even asking the same questions.
*  They're not thinking about it as a kind of programming problem.
*  And I think that that really matters, just asking this question.
*  I actually think it's a little different from programming and hyperparameter space and sort
*  of collecting the data.
*  But I do think that that immersion really matters.
*  So I'll give you a quick example the way I think about this.
*  So I teach machine learning.
*  Michael and I have co-taught a machine learning class, which has now reached, I don't know,
*  a thousand people at least over the last several years or somewhere there's abouts.
*  And my machine learning assignments are of this form.
*  So the first one is something like implement these five algorithms, you know, K and N and
*  S, you know, SVMs and boosting and decision trees and neural networks.
*  And maybe that's it.
*  I can't remember.
*  And when I say implement, I mean, steal the code.
*  I am completely uninterested.
*  You get zero points for getting the thing to work.
*  your time worrying about getting the corner case right of, you know, what happens when
*  you are trying to normalize distances and the points on the thing.
*  And so you divide by zero.
*  I'm not interested in that, right?
*  Steal the code.
*  However, you're going to run those algorithms on two datasets.
*  The datasets have to be interesting.
*  What does it mean to be interesting?
*  Well, a dataset is interesting if it reveals differences between algorithms, which presumably
*  are all the same because they can represent whatever they can represent.
*  And two datasets are interesting together if they show different differences, as it
*  were.
*  And you have to analyze them.
*  You have to justify their interestingness and you have to analyze them in a whole bunch
*  of ways.
*  But all I care about is the data in your analysis, not the programming.
*  And I occasionally end up in these long discussions with students.
*  Well, I don't really, I copy and paste the things that I've said the other 15,000 times
*  it's come up, which is they go, but the only way to learn, really understand is to code
*  them up, which is a very programmer software engineering view of the world.
*  If you don't program it, you don't understand it, which is, by the way, I think is wrong
*  in a very specific way.
*  But it is a way that you come to understand because then you have to wrestle with the
*  algorithm.
*  But the thing about machine learning is it's not just sorting numbers, where in some sense
*  the data doesn't matter.
*  What matters is, well, does the algorithm work on these abstract things, one list, the
*  other?
*  In machine learning, the data matters.
*  It matters more than almost anything.
*  And not everything, but almost anything.
*  And so as a result, you have to live with the data and don't get distracted by the algorithm
*  per se. And I think that that focus on the data and what it can tell you and what question
*  it's actually answering for you as opposed to the question you thought you were asking
*  is a key and important thing about machine learning and is a way that computationalists
*  as opposed to statisticians bring a particular view about how to think about the process.
*  The statisticians, by contrast, bring, I think I'd be willing to say, a better view about
*  the kind of formal math that's behind it and what an actual number ultimately is saying
*  about the data.
*  And those are both important, but they're also different.
*  I didn't really think of it this way is to build intuition about the role of data, the
*  different characteristics of data by having two data sets that are different and they
*  reveal the differences and the differences.
*  That's a really fascinating, that's a really interesting educational approach.
*  The students love it, but not right away.
*  No, they love it.
*  They love it later.
*  Not at the beginning.
*  Not even immediately after.
*  I feel like there's a deep, profound lesson about education there.
*  That you can't listen to students about whether what you're doing is the right or the wrong
*  thing.
*  Well, as a wise, Michael Lippman once said to me about children, which I think applies
*  to teaching, is you have to give them what they need without bending to their will.
*  And students are like that.
*  They have to figure out what they need.
*  You're a curator.
*  Your whole job is to curate and to present because on their own, they're not going to
*  necessarily know where to search.
*  So you're providing pushes in some direction and learn space.
*  And you have to give them what they need in a way that keeps them engaged enough so that
*  they eventually discover what they want and they get the tools they need to go and learn
*  other things off of.
*  What's your view?
*  Let me put on my Russian hat, which believes that life is soft.
*  I like Russian hats, by the way.
*  If you have one, I would like this.
*  Those are ridiculous.
*  Yes.
*  But in a delightful way.
*  But sure.
*  What do you think is the role of we talked about balance a little bit.
*  What do you think is the role of hardship in education?
*  Like I think the biggest things I've learned, like what made me fall in love with math,
*  for example, is by being bad at it until I got good at it.
*  I feel like like struggling with a problem, which increased the level of joy I felt when
*  I finally figured it out.
*  And it always felt with me, with teachers, especially modern discussions of education,
*  how can we make education more fun, more engaging, more all those things?
*  Or from my perspective is like you may be missing the point that education, that life
*  is suffering.
*  Education is supposed to be hard and that actually what increases the joy you feel when
*  you actually learn something.
*  Is that ridiculous?
*  Do you like to see your students suffer?
*  OK, so this may be a point where we differ.
*  I suspect not.
*  I'm going to do go on.
*  Well, what would your answer be?
*  I want to hear you first.
*  OK, well, I was going to not answer the question.
*  You don't want the students to know you enjoy them suffering?
*  No, no, no, no, no, no.
*  I was going to say that there's I think there's a distinction that you can't really tell
*  I was going to say that there's I think there's a distinction that you can make in the kind
*  of suffering.
*  Right.
*  So I think you can be in a mode where you're you're suffering in a hopeless way versus
*  you're suffering in a hopeful way.
*  Right.
*  Where you're like you can see that if you that you still have you can still imagine
*  getting to the end.
*  Right.
*  And as long as people are in that mindset where they're struggling, but it's not a
*  kind of struggling.
*  That's that's productive.
*  I think that's really helpful.
*  But it's struggling like if you break their will, if you leave them hopeless.
*  No, that don't.
*  Sure.
*  Some people are going to whatever lift themselves up by their bootstraps.
*  But like mostly you give up and certainly it takes the joy out of it.
*  And you're not going to spend a lot of time on something that brings you no joy.
*  So it's it's it is a bit of a delicate balance.
*  Right.
*  Right.
*  So I think you can work people in a way that they still believe that there's a way through.
*  Right.
*  So that's a that we strongly agree, actually.
*  So I think well first off, struggling and suffering aren't the same thing.
*  Right.
*  Being poetic.
*  I actually appreciate the poetry.
*  And one of the reasons I appreciate it is that they are often the same thing and often
*  quite different.
*  Right.
*  So you can struggle without suffering.
*  You can certainly suffer suffer pretty easily.
*  You don't still have to struggle to suffer.
*  So I think that you want people to struggle.
*  But that hope matters.
*  So you have to they have to understand that they're going to get through it on the other
*  side.
*  And it's very easy to confuse the two.
*  I actually think Brown University has a very just philosophically has a very different
*  take on the relationship with the students, particularly undergrads from say a place like
*  Georgia Tech, which is which universities better.
*  Well, I have my opinions on that.
*  I mean, remember, Charles said it doesn't matter what the facts are.
*  I'm always right.
*  Is that it doesn't matter.
*  They're different.
*  But clearly, clearly, he went to a school like the school where he is as an undergrad.
*  I went to a school specifically the same school, though it was changed a bit in the in the
*  intervening years.
*  Brown or Georgia Tech?
*  No, I was talking about Georgia Tech.
*  And I went to change.
*  Yeah.
*  And I went to an undergrad place.
*  It's a lot like the place where I work now.
*  And so it does seem like we're more familiar with these models.
*  There's a similarity between Brown and Yale.
*  Yeah.
*  I think that I think they're quite similar.
*  Yeah.
*  And Duke.
*  Duke has some similarities, too.
*  But it's got a little southern drawl.
*  You've kind of worked your you sort of worked at universities that are like the places where
*  you learned.
*  And the same would be true for me.
*  Are you uncomfortable venturing out side the box?
*  Is that what you're saying?
*  Joining out what I'm saying?
*  Yeah, Charles is definitely the only goes to places that have institute in the name.
*  It has worked out that way.
*  Well, academic places anyway.
*  Well, no, I was a visiting scientist at U Penn or visiting visiting something at U Penn.
*  Oh, wow.
*  I just I just understood your joke.
*  Which one?
*  Five minutes later, I like to set the sort of time bomb.
*  The Institute is in the Charles only goes to places that have institute in the name.
*  So I guess Georgia, I forget that Georgia Tech is Georgia Institute of Technology.
*  The number of people who refer to it as Georgia Tech University is large and incredibly irritating.
*  It's one of the few things that genuinely gets under my skin.
*  But like schools like Georgia Tech and MIT have as part of the ethos like there is I
*  want to say there's a there's an abbreviation that someone taught me like IHTFP, something
*  like that.
*  Like there's a there's an expression which is basically I hate being here, which they
*  say so proudly.
*  And that is definitely not the ethos at Brown.
*  Like Brown is there's a little more pampering and empowerment and stuff.
*  And it's not like we're going to crush you and you're going to love it.
*  So yeah, I think there's a I think the ethos are different.
*  That's interesting.
*  Yeah, we had Drowned.
*  Perfect.
*  What's that?
*  In order to graduate from Georgia Tech.
*  This is a true thing.
*  Feel free to look it up.
*  If you lot of schools have this, by the way.
*  No, actually, Georgia Tech was barely the first Brandeis has it had it.
*  I feel like Georgia Tech was the first in a lot of the first in a lot of things.
*  It was the first in a lot of things.
*  I had the first one.
*  I will be mascot.
*  Stop that.
*  First Masters in computer science, actually.
*  Right.
*  Online Masters.
*  Well, that too, but way back in the 60s.
*  NSF grant.
*  Yeah, yeah.
*  You're the first information and computer science masters degree in the country.
*  But the Georgia Tech, it used to be the case that in order to graduate from Georgia Tech,
*  you had to take a Drowned proofing class where effectively they threw you in the water, tied
*  you up.
*  If you didn't drown, you got to graduate.
*  Tied you up?
*  I believe so.
*  No.
*  There were certainly versions of it.
*  But I mean, luckily, they ended it just before I had to graduate because otherwise I would
*  have never graduated.
*  It wasn't going to happen.
*  I want to say 84, 83, someone around then, they ended it.
*  But yeah, you used to have to prove you could tread water for some ridiculous amount of
*  time or you couldn't graduate.
*  Two minutes.
*  No, it was more than two minutes.
*  I bet it was two minutes.
*  Okay, well we'll look at it.
*  And it was in a bathtub.
*  It was in a pool.
*  But it was a real thing.
*  But that idea that push you...
*  Fully clothed.
*  Yeah, fully clothed.
*  I bet it was that and not tied up.
*  Because who needs to learn how to swim when you're tied?
*  Nobody.
*  Who needs to learn to swim when you're actually falling into the water dressed?
*  That's a real thing.
*  I think your facts are getting in the way with a good story.
*  Oh, that's fair.
*  That's fair.
*  I didn't mean to.
*  All right.
*  So they tie you up.
*  Sometimes the narrative matters more.
*  But whatever it was, it was called drown-proofing for a reason.
*  The point of the story, Michael, is that...
*  Struggle.
*  Well, no, but that's good.
*  It does bring it back to struggle.
*  That's a part of what Georgia Tech has always been.
*  And we struggle with that, by the way, about what we want to be, particularly as things
*  go.
*  You sort of...
*  How much can you be pushed without breaking?
*  And you come out of the other end stronger, right?
*  There's this saying we used to have when I was an undergrad there, which was, Georgia
*  Tech, building tomorrow the night before.
*  And it was just kind of idea that, you know, give me something impossible to do and I'll
*  do it in a couple of days because that's what I just spent the last four or five or six
*  years doing.
*  That ethos definitely stuck to you.
*  Having now done a number of projects with you, you definitely will do it the night before.
*  That's not entirely true.
*  There's nothing wrong with waiting until the last minute.
*  The secret is knowing when the last minute is.
*  That's brilliantly put.
*  Yeah.
*  That is a definite Charles statement that I am trying not to embrace.
*  And I appreciate that because you helped move my last minute.
*  That's the social construct where you converge together what the definition of last minute
*  is.
*  We figure that out all together.
*  I'm sure a lot of universities have this, but MIT has MIT time that everyone has always
*  agreed together that there is such a concept and everyone just keeps showing up like 10
*  to 15 to 20, depending on the department, late to everything.
*  So there's a weird drift that happens.
*  It's kind of fascinating.
*  Yeah, we're five minutes.
*  In fact, the classes will say, well, this is no longer true, actually, but it used to
*  be a class was started eight, but actually started eight or five and ends at nine.
*  Actually, it ends at eight fifty five.
*  Everything's five minutes off and nobody expects anything to start until five minutes after
*  the half hour, whatever it is.
*  It still exists.
*  It hurts my head.
*  Well, let's rewind the clock back to the fifties and sixties when you guys met.
*  How did you?
*  I'm just kidding.
*  But what can you tell the story of how you met?
*  So you've like the Internet and the world kind of knows you as as as connected in some
*  ways in terms of education, of teaching the world.
*  That's that's like the public facing thing.
*  But how did you as human beings and as collaborators meet?
*  I think there's two stories.
*  One is how we met and the other is how we got to know each other.
*  I'm not going to say I'm going to say that we came to understand that we had some common
*  something.
*  Yeah, it's funny because on the surface, I think we're we're different in a lot of ways.
*  But there's something.
*  Yeah, I mean, now we just leave each other's.
*  There you go.
*  Afternoon.
*  So I will tell the story of how we met and I'll let Michael tell the story of how we
*  met.
*  OK, all right.
*  So here's how we met.
*  I was already at at that point was AT&T Labs.
*  There's a long, interesting story there.
*  But anyway, I was there and Michael was coming to interview.
*  He was a professor at Duke at the time, but decided for reasons that he wanted to be in
*  New Jersey.
*  And so that would mean Bell Labs AT&T Labs.
*  And we were doing interviews, very much like academic interviews.
*  And so I had to be there.
*  We all had to meet with him afterwards and so on, one on one.
*  But it was obvious to me that he was going to be hired, like no matter what, because
*  everyone loved him.
*  They were just talking about all the great stuff he did.
*  Oh, he did this great thing.
*  And you just won something at AAAI, I think.
*  Or maybe you got 18 papers in AAAI.
*  I got the best paper award at AAAI for the crossword stuff.
*  Right.
*  Exactly.
*  Everyone was going on and on and on about it.
*  Actually, Tinder was saying incredibly nice things about you.
*  Really?
*  Yes.
*  He can be very grumpy.
*  Yes.
*  That's nice to hear.
*  He was grumpily saying very nice things.
*  Oh, that makes sense.
*  That does make sense.
*  So it was going to come.
*  So why was I meeting him?
*  I had something else I had to do.
*  I can't remember what it was.
*  It probably involved comic books.
*  So he remembers meeting me as inconveniencing his afternoon.
*  So he came.
*  So I eventually came to my office.
*  I was in the middle trying to do something.
*  I can't remember what.
*  And he came and he sat down.
*  And for reasons that are purely accidental, despite what Michael thinks, my desk at the
*  time was set up in such a way that had sort of an L shape.
*  And the chair on the outside was always lower than the chair that I was in.
*  And the kind of point was to...
*  The only reason I think that it was on purpose is because you told me it was on purpose.
*  I don't remember that.
*  Anyway, the thing is that it kind of gives...
*  His guest chair was really low so that he could look down at everybody.
*  The idea was just to simply create a nice environment that you were asking for a mortgage
*  and I was going to say no.
*  That was the point.
*  It was a very simple idea here.
*  Anyway, so we sat there and we just talked for a little while.
*  And I think he got the impression that I didn't like him.
*  It wasn't true.
*  I strongly got that impression.
*  The talk was really good and he was full of excitement.
*  The talk, by the way, was terrible.
*  And right after the talk, I said to my host, Michael Kearns, who ultimately was my boss...
*  I'm a huge fan.
*  I'm a friend and a huge fan of Michael, yeah.
*  Yeah, he is a remarkable person.
*  After my talk, I went into the...
*  Irritatingly good at basketball.
*  I went...
*  Racquetball.
*  He's good at everything.
*  No, basketball.
*  No, but basketball, racquetball too.
*  Squash.
*  Squash, squash, not racquetball.
*  Yeah, squash, which is not...
*  Racquetball, yes.
*  Squash, no.
*  And I hope you hear that, Michael.
*  You mean it as a game, not his skill level, because I'm pretty sure he's...
*  All right, there's some competitiveness there.
*  But the point is that it was like the middle of the day, I had full day of interviews.
*  I met with people, but then in the middle of the day, I gave a job talk.
*  And then there was going to be more interviews.
*  But I pulled Michael aside and I said, I think it's in both of our best interests if I just
*  leave now, because that was so bad that it's just be embarrassing if I have to talk to
*  any more people.
*  Like, you look bad for having invited me.
*  It's just...
*  Let's just forget this ever happened.
*  So I don't think the talk went well.
*  That's one of the most Michael Lipman set of sentences I think I've ever heard.
*  He did great, or at least everyone knew he was great, so maybe it didn't matter.
*  I was there.
*  I remember the talk and I remember him being very much the way I remember him now, on any
*  given week.
*  So it was good.
*  And we met and we talked about stuff.
*  He thinks I didn't like him, but...
*  Because he was so grumpy.
*  Must have been the chair thing.
*  The chair thing and the low voice, I think.
*  He obviously...
*  And that slight skeptical look.
*  Yes.
*  I have no idea what you're talking about.
*  Well, I probably didn't have any idea what you were talking about.
*  Anyway, I liked him.
*  He asked me questions.
*  I answered questions.
*  I felt bad about myself.
*  It was a normal day.
*  It was a normal day.
*  And then he left.
*  And then he left.
*  And that's how we met.
*  Can we take a...
*  And then I got hired and I was in the group.
*  Can we take a slight tangent on this topic of...
*  It sounds like maybe you could speak to the bigger picture.
*  It sounds like you're quite self-critical.
*  Who, Charles?
*  No, you.
*  Oh, I think I can do better.
*  I can do better.
*  Try me again.
*  I'll do better.
*  Don't be so self-critical.
*  I won't.
*  I won't.
*  Yeah, that was like a three out of 10 response.
*  So let's try to work it up to five and six.
*  Yeah, I remember Marvin Minsky said on a video interview,
*  something that the key to success in academic research
*  is to hate everything you do.
*  For some reason...
*  I think I followed that because I hate everything he's done.
*  That's a good line.
*  That's a success.
*  Maybe that's a keeper.
*  But do you find that resonates with you at all in how you think about talks and so on?
*  I would say it differently.
*  No, not really.
*  That's such an MIT view of the world.
*  So I remember talking about this when, as a student,
*  you were basically told, I will clean it up for the purposes of the podcast,
*  my work is crap, my work is crap, my work is crap, my work is crap.
*  Then you go to a conference or something,
*  you're like, everybody else's work is crap, everybody else's work is crap,
*  and you feel better and better about it, relatively speaking.
*  And then you sort of keep working on it.
*  I don't hate my work.
*  That resonates with me.
*  Yes, I've never hated my work, but I have been dissatisfied with it.
*  And I think being dissatisfied, being okay with the fact that you've taken a positive step,
*  the derivative's positive, maybe even the second derivative's positive,
*  that's important because that's a part of the hope, right?
*  But you have to...
*  But I haven't gotten there yet.
*  If that's not there, that I haven't gotten there yet,
*  then it's hard to move forward, I think.
*  So I buy that, which is a little different from hating everything that you do.
*  I mean, there's things that I've done that I like better than I like myself.
*  So it's separating me from the work, essentially.
*  So I think I am very critical of myself,
*  but sometimes the work I'm really excited about, and sometimes I think it's kind of good.
*  Does that happen right away?
*  So I found the work that I've liked, that I've done, most of it,
*  I liked it in retrospect more when I was far away from it in time.
*  I have to be fairly excited about it to get done.
*  No, excited at the time, but then happy with the result.
*  But years later, or even a little bit, you know what?
*  That actually turned out to matter.
*  That turned out to matter.
*  Or, oh gosh, it turns out I've been thinking about that.
*  It's actually influenced all the work that I've done since, without realizing it.
*  Boy, that guy was smart.
*  Yeah, that guy had a future.
*  Yeah.
*  He's going places.
*  So yeah, I think there's something to it.
*  I think there's something to the idea you've got to hate what you do,
*  but it's not quite hate, it's just being unsatisfied.
*  And different people motivate themselves differently.
*  I don't happen to motivate myself with self-loathing.
*  I happen to motivate myself with something else.
*  So you're able to sit back and be proud of, in retrospect, of the work you've done.
*  Well, and it's easier when you can connect it with other people,
*  because then you can be proud of them.
*  Proud of the people, yeah.
*  And then the question is...
*  And then you can still safely hate yourself privately.
*  Yeah, that's right.
*  It's win-win, Michael.
*  Or at least win-lose, which is what you're looking for.
*  Oh, wow.
*  There's so many brilliant lines in this.
*  There's levels.
*  So how did you actually meet me?
*  Yeah, Michael.
*  So the way I think about it is...
*  Because we didn't do much research together at HNT.
*  But then we all got laid off.
*  So that was...
*  By the way, sorry to interrupt,
*  but that was one of the most magical places, historically speaking.
*  They did not appreciate what they had.
*  And how do we...
*  I feel like there's a profound lesson in there, too.
*  How do we get it...
*  Like, why was it so magical?
*  Is it just a coincidence of history?
*  Or is there something special about...
*  There were some really good managers
*  and people who really believed in machine learning
*  as this is going to be important.
*  Let's get the people who are thinking about this
*  in creative and insightful ways
*  and put them in one place and stir.
*  Yeah, but even beyond that, right?
*  It was Bell Labs at its heyday.
*  And even when we were there, which I think was past its heyday...
*  And to be clear, he's gotten to be at Bell Labs.
*  I never got to be at Bell Labs.
*  I joined after that.
*  Yeah, I should have been 91 as a grad student.
*  So I was there for a long time.
*  Every summer, except for...
*  So twice I worked for companies that had just stopped being Bell Labs.
*  Bellcore and then AT&T Labs.
*  So Bell Labs was several locations for the research?
*  Or is it what, like, the Jerseys involved somehow?
*  They're all in Jersey.
*  Yeah, they're all over the place.
*  But they were in a couple places in Jersey.
*  Murray Hill was the Bell Labs place.
*  So you had an office at Murray Hill at one point in your career.
*  Yeah, and I played ultimate frisbee on the cricket pitch at Bell Labs at Murray Hill.
*  And then it became AT&T Labs when it split off with Luce during what we call Trivestiture.
*  Are you better than Michael Kornz at ultimate frisbee?
*  Yeah.
*  Oh, yeah.
*  But I think that was not boasting.
*  I think Charles plays a lot of ultimate, and I don't think Michael does.
*  I was, yes, but that wasn't the point.
*  The point is yes.
*  I'm finally better.
*  Oh, yes, yes, sorry.
*  Okay, I have played on a championship-winning ultimate frisbee team, or whatever, ultimate
*  team, with Charles.
*  So I know how good he is.
*  He's really good.
*  How good I was anyway when I was younger.
*  But the thing is...
*  I know how young he was when he was younger.
*  That's true.
*  That is true.
*  So much younger than now.
*  He's older now.
*  Yeah, I'm older.
*  Michael was a much better basketball player than I was.
*  Michael Kornz.
*  Yes, no, not Michael Kornz.
*  Let's be very clear about that.
*  To be clear, I've not played basketball with you.
*  So you don't know how terrible I am, but you have a probably pretty good guess.
*  That you're not as good as Michael Kornz.
*  He's tall and athletic.
*  And he cared about it.
*  He's very athletic.
*  He's very good.
*  And probably competitive.
*  I love hanging out with Michael.
*  Anyway, but we were talking about something else, although I no longer remember what it
*  was.
*  What were we talking about?
*  Oh, Bell Labs.
*  Oh, Bell Labs.
*  But also Labs.
*  So this was kind of cool about what was magical about it.
*  The first thing you have to know is that Bell Labs was an arm of the government, right?
*  Because AT&T was an arm of the government.
*  And every month you paid a little thing on your phone bill, which turned out was a tax
*  for all the research that Bell Labs was doing.
*  They invented transistors and the laser and whatever else.
*  The Big Bang or whatever.
*  The cosmic background radiation.
*  They did all that stuff.
*  They had some amazing stuff with directional microphones, by the way.
*  I got to go in this room where they had all these panels and everything.
*  And we would talk.
*  And he'd move some panels around.
*  And then he'd have me step, two steps to the left.
*  And I couldn't hear a thing he was saying because nothing was bouncing off the walls.
*  And then he would shut it all down and you could hear your heartbeat, which is deeply
*  disturbing to hear your heartbeat.
*  You can feel it.
*  I mean, you can feel it now.
*  There's just so much all this sort of noise around.
*  Anyway, Bell Labs is about pure research.
*  It was a university, in some sense the purest sense of a university, but without students.
*  So it was all the faculty working with one another and students would come in to learn.
*  They would come in for three or four months during the summer and they would go away.
*  But it was just this kind of wonderful experience.
*  I could walk out my door.
*  In fact, I would often have to walk out my door and deal with Rich Sutton and Michael
*  Kerns yelling at each other about whatever it is they were yelling about, the proper
*  way to prove something or another.
*  And I could just do that.
*  And Dave McAllister and Peter Stone and all of these other people, including Satyendra
*  and then eventually Michael.
*  And it was just a place where you could think thoughts.
*  And it was okay because so long as once every 25 years or so somebody invented a transistor,
*  it paid for everything else.
*  You could afford to take the risk.
*  And then when that all went away, it became harder and harder and harder to justify it
*  as far as the folks who were very far away were concerned.
*  And there was such a fast turnaround among mental management on the AT&T side that you
*  never had a chance to really build a relationship.
*  At least people like us didn't have a chance to build a relationship.
*  So when the diaspora happened, it was amazing, right?
*  Everybody left and I think everybody ended up at a great place and made a huge, continued
*  to do really good work with machine learning.
*  But it was a wonderful place.
*  And people will ask me, what's the best job you've ever had?
*  And as a professor, the answer that I would give is, well, probably Bell Labs in some
*  very real sense.
*  And I would never have a job like that again because Bell Labs doesn't exist anymore.
*  And Microsoft Research is great and Google does good stuff and you can pick IBM.
*  You can do whatever you want to.
*  But Bell Labs was magical.
*  It was an important time and it represents a high water mark in basic research in the US.
*  Is there something you could say about the physical proximity and the chance collisions?
*  We live in this time of the pandemic where everyone is maybe trying to see the silver
*  lining and accepting the remote nature of things.
*  Is there one of the things that people like faculty that I talk to miss is the procrastination
*  like the chance to make everything is about meetings that are supposed to be there's
*  not a chance to just talk about comic book or whatever, like go into discussion that's
*  totally pointless.
*  So it's funny you say this because that's how we met.
*  It was exactly that.
*  So I'll let Michael say that.
*  But I'll just add one thing, which is just that research is a social process and it helps
*  to have random social interactions, even if they don't feel social at the time.
*  That's how you get things done.
*  One of the great things about the AI lab when I was there, I don't quite know what it looks
*  like now once they move buildings, but we had entire walls that were whiteboards and
*  people would just get up there and they were just right.
*  And people would walk up and you'd have arguments and you'd explain things to one another.
*  And you got so much out of the freedom to do that.
*  You had to be okay with people challenging every freaking word you said, which I would
*  sometimes find deeply irritating.
*  But most of the time it was quite useful.
*  But the sort of pointlessness and the interaction was in some sense the point, at least for
*  me.
*  Yeah.
*  I mean, I think offline yesterday I mentioned Josh Tannenbaum and he's very much, he's such
*  an inspiration in the child-like way that he pulls you in on any topic.
*  It doesn't even have to be about machine learning or the brain.
*  He'll just pull you into a closest writable surface, which is still, you can find whiteboards
*  and MIT everywhere.
*  And just like basically cancel all meetings and talk for a couple hours about some aimless
*  thing.
*  And it feels like the whole world, the time space continuum kind of warps and that becomes
*  the most important thing.
*  And then it's just, it's definitely something worth missing in this world where everything's
*  remote.
*  There's some magic to the physical presence.
*  Whenever I wonder myself whether MIT really is as great as I remember it, I just go talk
*  to Josh.
*  Yeah.
*  You know, that's funny is there's a few people in this world that carry the best of what
*  particular institutions stand for.
*  Right.
*  And this is Josh.
*  I mean, I don't, I, my guess is he's unaware of this.
*  That's the point.
*  Yeah.
*  The masters are not aware of their mastery.
*  So how did you meet?
*  Yes.
*  But, but first the tangent.
*  No.
*  How did you meet me?
*  So I'm not sure what you were thinking, but my, when it started to dawn on me that maybe
*  we had a longer term bond was after we all got laid off and you had decided at that point
*  that there, that we were, we were still paid.
*  We were given an opportunity to like do job search and kind of make a transition, but
*  it was clear that we were done.
*  And I would go to my office to work and you would go to my office to keep me from working.
*  That was, that was my recollection of it.
*  And then you decided that there was no, really no point in working for the company because
*  the company, our relationship with the company was, was done.
*  Yeah.
*  But remember I felt that way beforehand.
*  It wasn't about the company.
*  It was about the set of people.
*  They're doing really cool things.
*  And it always, always been that way, but we were working on something together.
*  Oh yeah.
*  Yeah.
*  That's right.
*  So at the very end, we all got laid off, but then our boss came to our bosses, boss came
*  to us because our boss was Michael Kearns and he had jumped ship brilliantly, like perfect
*  timing, like things like right before the ship was about to sink.
*  He was like, gotta go.
*  And, and, and landed perfectly because Michael Kearns.
*  Because Michael Kearns.
*  And the, the, and leaving the rest of us to go like, this is fine.
*  And then it was clear that it wasn't fine.
*  And we were all toast.
*  So we had this sort of long period of time, but then our boss figured out, okay, wait,
*  maybe we can save a couple of these people if we can have them do something really useful.
*  And the useful thing was we were going to make a, basically an automated assistant that
*  could help you with your calendar.
*  You could like tell it things and it would, it would respond appropriately.
*  It would just kind of integrate across all sorts of your personal information.
*  And so me and Charles and Peter Stone were this, were set up as the crack team to actually
*  solve this problem.
*  Other people maybe were too theoretical that they thought.
*  And, and, but we could actually get something done.
*  So we sat down to get something done and there wasn't time and it wouldn't have saved us anyway.
*  And so it all kind of went downhill.
*  But the interesting, I think, coda to that is that our boss's boss is a guy named Ron
*  Brockman.
*  And he, when he left AT&T, cause we were all laid off, he went to DARPA, started up a program
*  there that became KALO, which is the program from which Siri sprung, which is a digital
*  assistant that helps you with your calendar and a bunch of other things.
*  It really, you know, in some ways got its start with me and Charles and Peter trying to
*  implement this vision that Ron Brockman had that he ultimately got implemented through his
*  role at DARPA.
*  So when I'm trying to feel less bad about having been laid off from what is possibly the
*  greatest job of all time, I think about, well, we kind of helped birth Siri.
*  That's something.
*  And then he did other things too.
*  But the, we got to spend a lot of time in his office and talk about that.
*  We got to spend a lot of time in my office.
*  Yeah.
*  Yeah.
*  Yeah.
*  And so, so then we went on our merry way.
*  Everyone went to different places.
*  Charles landed at Georgia Tech, which was what he always dreamed he would do.
*  And so that worked out well.
*  I came up with a saying at the time, which is luck favors the Charles.
*  It's kind of like luck favors the prepared.
*  But Charles, like, like he'd wish something and then it would basically happen just the
*  way he wanted.
*  It was, it was inspirational to see things go that way.
*  Things worked out.
*  And we stayed in touch.
*  And then I think it really helped when you were working on, I mean, you'd kept me in
*  the loop for things like threads and the work that you were doing at Georgia Tech.
*  But then when they were starting their online master's program, he knew that I was really
*  excited about MOOCs and online teaching.
*  And he's like, I have a plan.
*  And I'm like, tell me your plan.
*  He's like, I can't tell you the plan yet because they were deep in negotiations between
*  Georgia Tech and Udacity to make this happen.
*  And they didn't want it to leak.
*  So Charles would kept teasing me about it, but wouldn't tell me what was actually going
*  on.
*  And eventually it was announced.
*  And he said, I would like you to teach the machine learning course with me.
*  I'm like, that can't possibly work.
*  But it was a great idea.
*  And it was, it was super fun.
*  It was a lot of work to put together, but it was, it was really great.
*  And was that the first time you thought about, first of all, was it the first time you got
*  seriously into teaching?
*  I mean, you know, I was a professor.
*  I'm trying to get the timing right.
*  This is already, this is already after you jumped to, so like, there's a little bit of
*  jumping around in time.
*  Yeah, sorry about that.
*  There's a pretty big jump in time.
*  So like the MOOCs thing.
*  So Charles got to Georgia Tech and he, I mean, maybe Charles, maybe this is a Charles story.
*  I got to Georgia Tech in 2002.
*  He got to Georgia Tech in 2002.
*  And, but then, and worked on things like revamping the curriculum, the undergraduate curriculum,
*  so that it had some kind of semblance of modular structure, because computer science was at
*  the time moving from a fairly narrow specific set of topics to touching a lot of other parts
*  of intellectual life.
*  And the curriculum was supposed to reflect that.
*  And so Charles played a big role in kind of redesigning that.
*  And then the...
*  And for my, and for my, my labors, I ended up the associate dean.
*  Right.
*  He got to become associate dean of, in charge of educational stuff.
*  This should be a valuable lesson.
*  If you're good at something, they will give you responsibility to do more of that thing.
*  Well, until you...
*  Don't show competence.
*  Don't show competence.
*  If you...
*  Well, you know what they say.
*  No one has responsibility.
*  Here's what they say.
*  Yeah.
*  The reward for good work is more work.
*  Yeah.
*  The reward for bad work is less work.
*  Which, I don't know, depending on what you're trying to do that week, one of those is better
*  than the other.
*  Well, one of the problems with the word work, sorry to interrupt, is that it seems to be
*  an antonym in this particular language.
*  We have the opposite of happiness, but it seems like they're...
*  That's one of the, you know, we talked about balance.
*  It's always like work-life balance.
*  It always rubbed me the wrong way as a terminology.
*  I know it's just words.
*  Right.
*  The opposite of work is play, but ideally work is play.
*  Oh, I can't tell you how much time I'd spend.
*  Certainly, when I was at Bell Labs, except for a few very key moments, as a professor,
*  I would do this too.
*  I would just say, I cannot believe they're paying me to do this.
*  Because it's fun.
*  It's something that I would do for a hobby if I could anyway.
*  So, that sort of worked out.
*  Are you sure you want to be saying that when this is being recorded?
*  As a dean, that is not true at all.
*  I need a raise.
*  Yeah.
*  But I think here with this, even though a lot of time passed, you know, Michael and
*  I talked almost every...
*  Well, we texted almost every day during the period.
*  Charles, at one point, took me...
*  There was the ICML conference.
*  The machine learning conference was in Atlanta.
*  I was the chair, the general chair of the conference.
*  Charles was my publicity chair or something like that or fundraising chair.
*  Fundraising chair.
*  Yeah.
*  But he decided it'd be really funny if he didn't actually show up for the conference
*  in his own home city.
*  So, he didn't.
*  But he did at one point pick me up at the conference in his Tesla and drove me to the
*  Atlanta mall and forced me to buy an iPhone because he didn't like how it was to text
*  with me and thought it would be better for him if I had an iPhone.
*  The text would be somehow smoother.
*  And it was.
*  And it was.
*  And it is.
*  And his life is better.
*  And my life is better.
*  And so, yeah.
*  Charles forced me to get an iPhone so that he could text me more efficiently.
*  I thought that was an interesting moment.
*  It works for me.
*  Anyway, so we kept talking the whole time.
*  And then eventually we did the teaching thing.
*  And it was great.
*  And there's a couple of reasons for that, by the way.
*  One is I really wanted to do something different.
*  Like, you've got this medium here.
*  People claim it can change things.
*  What's a thing that you could do in this medium that you could not do otherwise?
*  Besides edit.
*  I mean, what could you do?
*  And being able to do something with another person was that kind of thing.
*  I mean, you can take turns, but teaching together, having conversations, very hard, right?
*  So that was a cool thing.
*  The second thing, give me an excuse to do more stuff with him.
*  Yeah, I always thought he makes it sound brilliant.
*  And it is, I guess.
*  But at the time, it really felt like I've got a lot to do, Charles is saying.
*  And it would be great if Michael could teach the course and I could just hang out.
*  Yeah, just kind of coast on that.
*  Well, that's what the second class was more like that.
*  Second class was explicit.
*  The first class, it was at least half.
*  So the structure that we came up with.
*  I think you're once again letting the facts get in the way.
*  A good story.
*  I should just let Charles talk.
*  But that's the fact that he saw.
*  So that was kind of true for 7642, which is the reinforcement learning class, because that was really his class.
*  You started with reinforcement learning?
*  No, I did the intro machine learning, 7641, which is supervised learning, unsupervised learning, and reinforcement learning and decision making.
*  And cram all that in there, the kind of assignments that we talked about earlier.
*  And then eventually, about a year later, we did a follow on 7642, which is reinforcement learning and decision making.
*  The first class was based on something I had been teaching at that point for well over a decade.
*  And the second class was based on something Michael had been teaching.
*  Actually, I learned quite a bit teaching that class with him.
*  But he drove most of that.
*  But the first one I drove most of was all my material.
*  Although I had stolen that material originally from slides I found online from Michael, who had originally stolen that material from Michael.
*  I had stolen that material from, I guess, slides he found online probably from Andrew Moore, because the jokes were the same anyway.
*  At least some of the, at least when I found the slides, some of the stuff was there.
*  Is that true?
*  Yes. Every machine learning class taught in the early 2000s stole from Andrew Moore.
*  A particular joke or two?
*  At least the structure.
*  Now I did, and he did actually a lot more with reinforcement learning and such and game theory and those kinds of things.
*  But we all sort of built.
*  You mean in the research world?
*  No, no, no.
*  No, I mean in teaching that class.
*  The coverage was different than what we started.
*  Most people were just doing supervised learning and maybe a little bit of clustering and whatnot.
*  But we took it all the way to machine learning.
*  A lot of it just comes from Tom Mitchell's book.
*  Oh no. Yeah, except, well, half of it comes from Tom Mitchell's book, right?
*  The other half doesn't.
*  This is why it's all readings, right?
*  Because certain things weren't invented when Tom Mitchell wrote this.
*  Yeah, okay, that's true.
*  But it was quite good.
*  But there's a reason for that besides just I wanted to do it.
*  I wanted to do something new and I wanted to do something with him, which is realization, which is despite what you might believe.
*  He's an introvert and I'm an introvert or I'm on the edge of being an introvert anyway.
*  But both of us, I think, enjoy the energy of the crowd, right?
*  There's something about talking to people and bringing them into whatever we find interesting that is empowering, energizing or whatever.
*  And I found the idea of staring alone at a computer screen and then talking off of materials less inspiring than I wanted it to be.
*  And I had in fact done a MOOC for Udacity on algorithms.
*  And it was a week in a dark room talking at the screen, writing on the little pad.
*  And I didn't know this was happening, but they had watched the crew had watched some of the videos while in the middle of this.
*  And they're like, something's wrong.
*  You're sort of shutting down.
*  And I think a lot of it was I'll make jokes and no one would laugh.
*  And I felt like the crowd hated me.
*  Now, of course, there was no crowd.
*  So like it wasn't rational.
*  But it's little each time I tried it and I got no reaction.
*  It just was taking the energy out of my performance, out of my presentation.
*  Such a fantastic metaphor for grad school.
*  Anyway, by working together, we could play off each other and have it.
*  And keep the energy up because you can't let your guard down for a moment with Charles.
*  He'll just he'll just overpower you.
*  I have no idea what you're talking about.
*  But we would work really well together, I thought.
*  And we knew each other.
*  So I knew that we could we could sort of make it work.
*  Plus, I was the associate dean.
*  So they had to do what I told them to do.
*  We had to do that.
*  We had to make it work.
*  And so it worked out very well, I thought.
*  Well enough that we with great power comes great power.
*  That's right.
*  And we became smooth and curly.
*  And that's when we we did the the the overfitting thriller video.
*  Yeah, we took. Yeah, yeah, that's a thing.
*  So what can we just like smooth and curly?
*  Where was that?
*  OK, so that happened.
*  It was completely spontaneous.
*  These are names you go by.
*  Yeah. So it's what the students call us.
*  He was he was lecturing.
*  So the way that we structure the lectures is one of us is the lecturer and one of us is basically the student.
*  And so the he was lecturing on the lecture, prepares all the materials, comes up with the quizzes.
*  And then the student comes in not knowing anything.
*  So it's just like being on campus.
*  And I was doing game theory in particular.
*  Yeah. The Prisoners' Dilemma.
*  Prisoners' Dilemma.
*  And so he needed to set up a little Prisoners' Dilemma grid.
*  So he drew it and I could see what he was drawing.
*  And the Prisoners' Dilemma consists of two players, two parties.
*  So he decided he would make little cartoons of the two of us.
*  And so there was two criminals, right, that were deciding whether or not to rat each other out.
*  One of them he drew as a circle with a smiley face and a kind of goatee thing, smooth head.
*  And the other one with all sorts of curly hair.
*  And he said, this is smooth and curly.
*  I said, smooth and curly? He said, no, no, smooth with a V.
*  It's very important that it have a V.
*  And that's stuck. I actually watched that video.
*  And then the students really took to that.
*  Like they found that relatable.
*  He started singing Smooth Criminal by Michael Jackson.
*  Yeah. And those names stuck.
*  So we now have a video series, an episode, our kind of first actual episode should be coming out today.
*  Smooth and Curly on video where the two of us discuss episodes of Westworld.
*  We watched Westworld and we're like, huh, what does this say about computer science and AI?
*  And we did not watch it. I mean, I know it's on season three or whatever we have.
*  As of this recording, it's on season three.
*  We've watched now two episodes total.
*  Yeah, I think I watched three.
*  What do you think about Westworld?
*  Two episodes in. So I can tell you so far, I'm just guessing what's going to happen next.
*  It seems like bad things are going to happen with the robots uprising.
*  It's a lot of alert.
*  So I have not. I have not. I mean, you know, I vaguely remember a movie existing.
*  So I assume it's related to that.
*  But that was more my time than your time, Charles.
*  That's right. Because you're much older than I.
*  I think the important thing here is that it's narrative, right?
*  It's all about telling a story. That's the whole driving thing.
*  But the idea that they would give these reveries that they would make people, they would remember the awful things that happened.
*  Who could possibly think that was good?
*  I mean, I don't know. I've only seen the first two episodes or maybe the third one.
*  I think I've only seen the first two.
*  You know what it was? You know what the problem is?
*  What?
*  That the robots were actually designed by Hannibal Lecter.
*  That's true. They were.
*  So like, what do you think is going to happen? Bad thing.
*  It's clear that things are happening and characters are being introduced and we don't yet know anything.
*  But still, I was just struck by how it's all driven by narrative and story.
*  And there's all these implied things like programming.
*  The programming interface is talking to them about what's going on in their heads, which is both, I mean, artistically, it's probably useful to film it that way.
*  But think about how it would work in real life. It just seems very creative.
*  But there was, we saw in the second episode, there's a screen. You could see things.
*  They were wearing like, cool glasses.
*  It was quite interesting to just kind of ask this question so far.
*  I mean, I assume it veers off into Never Neverland at some point.
*  So we don't know. We can't answer that question.
*  I'm also a fan of a guy named Alex Garland. He's a director of Ex Machina.
*  And he is the first. I wonder if Kubrick was like this, actually.
*  Is he like studies? What would it take to program an AI system?
*  Like he's curious enough to go into that direction.
*  On the Westworld side, I felt there was more emphasis on the narratives than like actually asking like computer science questions.
*  Like, how would you build this? How would you?
*  How would you debug it? To me, that's the key issue. They were terrible debuggers.
*  Yeah.
*  Well, they said specifically, so we make a change and we put it out in the world.
*  And that's bad because something terrible could happen.
*  Like if you're putting things out in the world and you're not sure whether something terrible is going to happen, your process is probably fine.
*  I just feel like there should have been someone whose sole job it was to walk around and poke his head in and say, what could possibly go wrong just over and over again?
*  I would have loved if there was an I did watch a lot more.
*  I'm not giving anything away. I would have loved it if there was like an episode where like like the new intern is like debugging a new model or something.
*  And like it just keeps failing. And they're like, all right.
*  And then it's more turns into like a episode of Silicon Valley or something like that versus versus like this ominous AI systems that are constantly like threatening the fabric of this world that's been created.
*  Yeah. Yeah. And you know, the other this reminds me of something that I agree that that should be very cool.
*  At least for the small percentage of people who care about debugging systems.
*  But the other thing is debugging the series.
*  It falls into the thing of the sequels. Fear of the debugger.
*  Oh, my gosh.
*  And anyway, so a nightmare show. It's a horror movie.
*  I think that's where we lose people, by the way, early on, is the people who either decide either figure out debugging or think debugging is terrible.
*  This is where we lose people in computer science.
*  This is part of the struggle versus suffering. Right.
*  You get through it and you kind of get the skills of it or you just like this is dumb and this is a dumb way to do anything.
*  And I think that's when we lose people.
*  But well, I'll leave it at that.
*  But I think that I think that there's something really, really neat about framing it that way.
*  But what I don't like about all of these all of these things, and I love text marketing, by the way, the ending was very depressing.
*  One of the things I have to talk to Alex about, he says that the thing that nobody noticed he put in is the at the end.
*  Spoiler alert. The robot turns and looks at the camera and smiles briefly.
*  And to him, he thought that his definition of passing the touring, the general version of the touring test or the consciousness test is smiling for no one.
*  Hmm. Oh, like, like not.
*  Oh, you know, it's like the Chinese room kind of experiment is not always trying to act for others.
*  Right. But just on your own, being able to have a relationship with the actual experience and just like take it in.
*  I don't know. He said like nobody noticed the magic of it.
*  I have this vague feeling that I remember the smile. But now you now you just put the memory in my head.
*  So probably not. But I do think that that's interesting.
*  Although by looking at the camera, you are smiling for the audience, right?
*  You're breaking the fourth wall. It seems I mean, well, that's a that's a limitation of the medium.
*  But I like that idea. But here's the problem I have with all of those movies, all of them is that.
*  But I know why it's this way. And I enjoy those movies and Westworld is it sets up the problem of AI as succeeding and then having something we cannot control.
*  But it's that's not the bad part of AI. The bad part of AI is the stuff we're living through now. Right.
*  It's the using the data to make decisions that are terrible.
*  It's not the intelligence that's going to go out there and surpass us and, you know, take over the world or, you know, lock us into a room to starve to death slowly over multiple days.
*  It's instead the tools that we're building that are allowing us to make the terrible decisions we would have less efficiently made before. Right.
*  You know, computers are very good at making us more efficient, including being more efficient at doing terrible things.
*  And that's the part of the AI we have to worry about.
*  It's not the, you know, true intelligence that we're going to build sometime in the future, probably long after we're around.
*  But, you know, I just I think that whole framing of it sort of misses the point, even though it is inspiring.
*  And I was inspired by those ideas. Right. I got into this in part because I wanted to build something like that.
*  Philosophical questions are interesting to me. But but, you know, that's not where the terror comes from.
*  The terror comes from the everyday. And you can construct situate in the subtlety of the interaction between AI and the human like with the social networks,
*  all the stuff you're doing with interactive artificial intelligence.
*  But, you know, I feel like Cal 9000 came a little bit closer to that when in 2001 Space Odyssey because it felt like a personal assistant.
*  You know, it felt like closer to the AI systems we have today and the real things we might actually encounter,
*  which is over relying on in some fundamental way on our like dumb assistance or on social networks like over offloading too much of us onto,
*  you know, onto things that require Internet and power and so on and thereby becoming powerless as a standalone entity.
*  And then when that thing starts to misbehave in some subtle way, it creates a lot of problems and those problems are dramatized when you're in space because you don't have a way to walk away.
*  Well, as the man said, once you once we started making the decisions for you, it stopped being your world. Right.
*  That's the Matrix, Michael, in case you don't. I didn't. You don't remember.
*  But on the other hand, I could say no, because isn't that what we do with people anyway?
*  You know, this kind of the shared intelligence that is humanity is relying on other people constantly.
*  I mean, we we hyper specialize, right, as individuals. We're still generally intelligent.
*  We make our own decisions in a lot of ways, but we leave most of the stuff to other people and that's perfectly fine.
*  And by the way, everyone doesn't necessarily share our goals.
*  Sometimes they seem to be quite against us.
*  Sometimes we make decisions that others would see as against our own interests, and yet we somehow manage it, manage to survive.
*  I'm not entirely sure why an A.I. would actually make that worse.
*  Or even different, really.
*  You mentioned the Matrix. Do you think we're living in a simulation?
*  It does feel like a thought game more than a real scientific question.
*  Well, I'll tell you why. I think it's an interesting thought experiment.
*  See what you think from a computer science perspective.
*  It's a good experiment of how difficult would it be to create a sufficiently realistic world that us humans would enjoy being in?
*  That that's almost like if we're living in a simulation, then I don't believe that we were put in the simulation.
*  I believe that it's just physics playing out and we came out of that.
*  I don't I don't I don't think so.
*  You think you have to build the universe?
*  I think the universe itself, we can think of that as a simulation.
*  And in fact, what I try sometimes I try to think about to understand what it's like for a computer to start to think about the world.
*  I try to think about the world, things like quantum mechanics, where it doesn't feel very natural to me at all.
*  And it really strikes me as I don't understand this thing that we're living in.
*  It has there's weird things happening in it that don't feel natural to me at all.
*  Now, if you want to call that as the result of a simulator, OK, I'm fine with that.
*  But like I know there's the bugs in the simulation.
*  There's the bugs. I mean, the interesting thing about the simulation is that it might have bugs.
*  I mean, that's the thing that I the bugs for the people in the simulation.
*  They're just that's just reality.
*  Unless you were aware enough to know that there was a bug.
*  But I think back to the matrix.
*  Yeah.
*  I don't think that we live in a in a simulation created for us.
*  OK, I would say that I think that's interesting.
*  I've actually never thought about it that way.
*  I mean, you the way you ask the question, though, is could you create a world that is enough for us humans?
*  It's an interestingly sort of self-referential question because.
*  The beings that created the simulation probably have not created the simulation that's realistic for them.
*  But we're in the simulation, and so it's realistic for us.
*  So we could create a simulation that is fine for the people in the simulation, as it were,
*  that would not necessarily be fine for us as the creators of the simulation.
*  But while you can you can forget, I mean, if when you go to the if you play video games and virtual reality,
*  you can if it was some suspension of disbelief or whatever, it becomes a world.
*  It becomes the world even like in brief moments.
*  You forget that another world exists.
*  I mean, that's what like good stories do.
*  They pull you in.
*  The question is, is it possible to pull, you know, our brains are limited.
*  Is it possible to pull the brain in to where we actually stay in that world longer and longer and longer and longer?
*  And like not only that, but we don't want to leave.
*  And so especially this is the key thing about the developing brain is if we journey into that world early on in life often.
*  How would you even know? Yeah.
*  Yeah. So I but like from a video game design perspective, from a Westworld perspective, it's I think I think it's an important thing
*  for even computer scientists to think about because it's clear that video games are getting much better and virtual reality,
*  although it's been ups and downs, just like artificial intelligence, it feels like virtual reality will be here in a very impressive form.
*  If we were to fast forward 100 years into the future in a way that might change society fundamentally.
*  Like if I were to I'm very limited in predicting the future as all of us are.
*  But if I were to try to predict like in which way I'd be surprised to see the world 100 years from now, it'd be that or impressed.
*  It'd be that we're all no longer living in this physical world that we're all living in a virtual world.
*  You really need to be calculating God by Sawyer.
*  It's a you'll read it in the night. It's a very easy read.
*  But it's assuming you're that kind of reader.
*  But it's a it's a good story.
*  And it's kind of about this, but not in a way that it appears.
*  And I really enjoyed the thought experiment.
*  I think it's pretty sure it's Robert Sawyer.
*  But anyway, he's he's apparently Canadians top science fiction writer, which is why the story mostly takes place in Toronto.
*  But it's a it's a very good it's a very good sort of story that that sort of imagines this very different kind of simulation hypothesis sort of thing from, say, the egg, for example.
*  You know, you know, I'm talking about the short story by the guy who did The Martian, who wrote The Martian.
*  You know, the Martian. Matt Damon.
*  So we had this whole discussion that Michael doesn't doesn't partake in this exercise of reading.
*  He doesn't seem to like it, which seems very strange to me concerning how much he has to read.
*  I read all the time. I used to read 10 books every week when I was when I was in sixth grade or whatever.
*  I was a lot of science fiction, a lot of it, a lot of history that I love to read.
*  But anyway, you should read Calculating God.
*  I think you'll you'll it's very easy read, like I said, and I think you'll enjoy sort of the ideas that it presents.
*  Yeah, I think the thought experiment is quite interesting.
*  One thing I've noticed about people growing up now, I mean, we talk about social media,
*  but video games is a much bigger, bigger and bigger and bigger part of their lives.
*  And the video games have become much more realistic.
*  I think it's possible that the three of us are not maybe the two of you are not familiar exactly with the numbers we're talking about here.
*  The number of people it's bigger than movies. Right.
*  It's it's it's huge. I used to do a lot of the computational narrative stuff.
*  I understand that economists can actually see the impact of video games on the labor market,
*  that there are there there's fewer young men of a certain age participating in like paying jobs than you'd expect.
*  And then they trace it back to video games.
*  I mean, the problem with Star Trek was not warp drive or teleportation.
*  It was the holodeck. Like if you have the holodeck, it's it.
*  That's it. You go in the holodeck. You never come out.
*  I mean, it just never made once I saw that, I thought, OK, well, so this is the end of humanity.
*  Right. They've been in the holodeck because that feels like the singularity, not some AGI or whatever.
*  It's some possibility to go into another world that can be artificially made better than this one.
*  Mm hmm. And slowing it down so you live forever or speeding it up so you appear to live forever or making the decision of when to die.
*  And then most of us will just be old people on the porch yelling at the kids these days in their virtual reality.
*  Mm hmm. But they won't hear us because they've got headphones on.
*  So, I mean, rewinding back to MOOCs, is there lessons that you've speaking to kids these days?
*  There you go. That was a transition.
*  That was fantastic.
*  All right. I'll edit. I'll fix it in post.
*  That's Charles's favorite phrase.
*  Fix it in post?
*  Fix it in post.
*  Fix it in post. We said all when we were recording all the time, whenever the editor didn't like something or whatever, I would say, we'll fix it in post.
*  He hated that. He hated that more than anything.
*  Because it's Charles's way of saying, I'm not going to do it again.
*  You know, you're on your own for this one.
*  But it always got fixed in post.
*  Exactly. So is there something you've learned about?
*  I mean, it's interesting to talk about MOOCs. Is there something you've learned about the process of education, about thinking about the present?
*  I think there's two lines of conversation to be had here is the future of education in general that you've learned about.
*  And more presciently is the education in the times of COVID.
*  The second thing in some ways matters more than the first for at least in my head for the not just because it's happening now, but because I think it's it's reminded us of a lot of things.
*  Coincidentally, today there's an article out by a good friend of mine who's also a professor at Georgia Tech, but more importantly, a writer and editor at the Atlantic.
*  I'm Ian Bogos.
*  And the title is something like Americans Will Sacrifice Anything for the College Experience.
*  And it's about why we went back to college and why people wanted us to go back to college.
*  And it's not, you know, greedy presidents trying to get the last dollar from someone.
*  It's because they want to go to college.
*  And what they're paying for is not the classes.
*  What they're paying for is the college experience.
*  It's not the education. It's being there.
*  I've been saying this for a long time that we continually make this mistake of people want to go back to college as being people want to go back to class.
*  They don't. They want to go back to campus.
*  They want to move away from home. They want to do all those things that people experience.
*  It's a rite of passage.
*  It's a identity, if I can steal some of Ian's words here.
*  And I think that's right.
*  And I think what we've learned through COVID is it has made it the disaggregation was not the disaggregation of the education from the place, the university place,
*  and that you can get the best anywhere you want to.
*  It turns out there's lots of reasons why that is not necessarily true.
*  The disaggregation is having it shoved in our faces that the reason to go, again, that the reason to go to college is not necessarily to learn.
*  It's to have the college experience.
*  And that's very difficult for us to accept, even though we behaved that way, most of us, when we were undergrads.
*  You know, a lot of us didn't go to every single class.
*  We learned and we got it and we look back on it and we're happy we had the learning experience as well, obviously, particularly us, because this is the kind of thing that we do.
*  And my guess is that's true of the vast majority of your audience.
*  But that doesn't mean the I'm standing in front of you telling you this is the thing that people are excited about.
*  And that's why they want to be there, primarily why they want to be there.
*  So to me, that's what COVID has forced us to deal with, even though I think we're still all in deep denial about it and hoping that it'll go back to that.
*  And I think about 85 percent of it will.
*  We'll be able to pretend that that's really the way it is.
*  Again, we'll forget the lessons of this.
*  But technically what will come out of it or technologically what will come out of it is a way of providing a more dispersed experience through online education and these kinds of remote things that we've learned.
*  And we'll have to come up with new ways to engage them in the experience of college, which includes not just the parties or whatever kids do, but the learning part of it so that they actually come out four or five or six years later with having actually having actually learned something.
*  So I think the world will be radically different afterwards.
*  And I think technology will matter for that, just not in the way that the people who were building the technology originally imagined it would be.
*  And I think this would have been true even without COVID, but COVID has accelerated that reality.
*  So it's happening in two or three years or five years as opposed to 10 or 15.
*  That was an amazing answer that I did not understand.
*  So it was passionate and and shots fired.
*  But I don't know. I just didn't know. I'm not trying to criticize it. I think I'm I don't think I'm getting it.
*  So you mentioned disaggregation.
*  So what's that?
*  Well, so, you know, the power, the power of technology that if you go on the West Coast and hang out long enough is all about we're going to disaggregate these things together.
*  The books from the bookstore, you know, that kind of a thing.
*  And then suddenly Amazon controls the universe. Right.
*  And technology is a disruptor. Right.
*  And people have been predicting that for higher education for a long time, but certainly in the age.
*  Is this the sort of idea like students can aggregate on a campus someplace and then take classes over the network anywhere?
*  This is what people thought was going to happen, or at least people claim it was going to happen. Right.
*  That, you know, because my daughter is essentially doing that now.
*  She's on one campus, but learning in a different campus.
*  Sure. And Kobe makes that possible. Right.
*  Kobe makes that legal, but avoidable. Right.
*  But the idea originally was that, you know, you and I were going to create this machine learning class and it was going to be great.
*  And then no one else would be the machine because everyone takes.
*  That was never going to happen. But, you know, something like that.
*  You didn't address that. So why? Why? Why is it that like you?
*  Why? I don't think that will be the thing that happens to the college experience.
*  Maybe I maybe I missed what the college experience was.
*  I thought it was peers like people hanging around a large part of it is peers.
*  Well, it's peers and independence. Yeah.
*  But you can do classes online for all of that.
*  No, no, no, no, no, because we're social people. Right.
*  So you want to be in the same class as that also has to be part of an experience.
*  It's in a context in the context is the university.
*  And by the way, it actually matters that Georgia Tech really is different from Brown.
*  I see. Because then students can choose the kind of experience they think is going to be best for them.
*  OK, I think we're giving too much agency to the students and making an informed decision.
*  OK. But the truth. But yes, they will make choices and they will have different experiences.
*  And some of those choices will be made for them.
*  Some of them will be choices they're making because they think it's this that or the other.
*  I just don't want to say that I don't want to give the idea.
*  Yes, it's certainly not homogenous. Right.
*  I mean, Georgia Tech is different from Brown.
*  Brown is different from pick your favorite state school in Iowa, Iowa State.
*  OK, which I guess is my favorite state school in Iowa.
*  But, you know, these are all different. They have different contexts.
*  And a lot of those contexts are they're about history. Yes.
*  But they're also about the location of where you are.
*  They're about the larger group of people who are around you, whether you're in Athens, Georgia.
*  And you're basically the only thing that's there as a university.
*  You're responsible for all the jobs or whether you're at Georgia State University,
*  which is an urban campus where you're surrounded by, you know, six million people in your campus,
*  where it ends and begins in the city, ends and begins.
*  We don't know. It actually matters whether a small campus or a large campus.
*  I mean, these things matter.
*  Why is it that if you go to Georgia Tech, you're like forever proud of that
*  and you like say that to people at dinner, like bars and whatever.
*  And if you get a degree at an online university somewhere,
*  that's not a thing that comes up at a bar.
*  Well, it's funny you say that.
*  So the students who take our online masters by several measures
*  are more loyal than the students who come on campus, certainly for the master's degree.
*  The reason for that, I think, and you'd have to ask them,
*  but based on my conversations with them, I feel comfortable saying this,
*  is because this didn't exist before.
*  I mean, we talk about this online masters and that it's reaching, you know, 11,000 students
*  and that's an amazing thing and we're admitting everyone we believe who can succeed.
*  We've got a 60% acceptance rate. It's amazing, right?
*  It's also a $6,600 degree. The entire degree costs $6,600 or $7,000,
*  depending on how long you take.
*  A dollar degree as opposed to $46,000, it costs you to come on campus.
*  So that feels, and I can do it while I'm working full time,
*  and I've got a family and a mortgage and all these other things.
*  So it's an opportunity to do something you wanted to do,
*  but you didn't think was possible without giving up two years of your life,
*  as well as all the money and everything else in the life that you had built.
*  So I think we created something that's had an impact,
*  but importantly, we gave a set of people opportunities they otherwise didn't feel they had.
*  So I think people feel very loyal about that.
*  And my biggest piece of evidence for that, besides the surveys,
*  is that we have somewhere north of 80 students, might be 100 at this point,
*  who graduated but come back in TA for this class for basically minimum wage,
*  even though they're working full time, because they believe in having that opportunity.
*  They want to be a part of something.
*  Now, will Generation 3 feel this way?
*  15 years from now, will people have that same sense? I don't know.
*  But right now, they kind of do.
*  And so it's a matter of feeling as if you're a part of something.
*  We're all very tribal.
*  And I think there's something very tribal about being a part of something like that.
*  Being on campus makes that easier.
*  Going through a shared experience makes that easier.
*  It's harder to have that shared experience if you're alone looking at a computer screen.
*  We can create ways to make that true.
*  But is it possible?
*  It is possible.
*  The question is, it still is the intuition to me,
*  and it was at the beginning when I saw something like the online master's program,
*  is that this is going to replace universities.
*  And it won't replace universities.
*  But why?
*  Because it's living in a different part of the ecosystem.
*  The people who are taking it are already adults.
*  They've gone through their undergrad experience.
*  I think their goals have shifted from when they were 17.
*  They have other things that are going.
*  But it does do something really important, something very social and very important.
*  You know this whole thing about, don't build the sidewalks, just leave the grass,
*  and the students or the people will walk, and you put the sidewalks where they create paths.
*  That's interesting, yeah.
*  Their architects apparently believe that's the right way to do things.
*  The metaphor here is that we created this environment.
*  We didn't quite know how to think about the social aspect,
*  but we didn't have time to do all the social engineering.
*  The students did it themselves.
*  They created these groups, like on Google+.
*  There were like 30-something groups created in the first year because somebody had used Google+.
*  They created these groups, and they divided up in ways that made sense.
*  We live in the same state, or we're working on the same things,
*  or we have the same background, or whatever.
*  They created these social things.
*  We sent them T-shirts.
*  We have all these great pictures of students putting on their T-shirts as they travel around the world.
*  I climbed to this mountaintop. I'm putting this T-shirt on.
*  I'm a part of this. They were a part of them.
*  They created the social environment on top of the social network and the social media that existed
*  to create this sense of belonging and being a part of something.
*  They found a way to do it.
*  I think they had other ... It scratched an itch that they had,
*  but they had scratched some of that itch that might have required they be physically in the same place long before.
*  I think, yes, it's possible, and it's more than possible, it's necessary,
*  but I don't think it's going to replace the university as we know it.
*  The university as we know it will change,
*  but there's just a lot of power in the rite of passage going off to yourself.
*  Now, maybe there'll be some other rite of passage that'll happen.
*  That'll drive us somewhere else if possible.
*  The university is such a fascinating mess of things,
*  so just even the faculty position is a fascinating mess.
*  It doesn't make any sense. It stabilized itself,
*  but why are the world-class researchers spending a huge amount of time of their time teaching and service?
*  You're doing three jobs.
*  It turns out it's maybe an accident of history or human evolution. I don't know.
*  It seems like the people who are really good at teaching are often really good at research.
*  There seems to be a parallel there,
*  but it doesn't make any sense that you should be doing that.
*  At the same time, it also doesn't seem to make sense that your place where you party
*  is the same place where you go to learn calculus or whatever.
*  But it's a safe space.
*  Safe space for everything.
*  Yeah, relatively speaking, it's a safe space.
*  Now, by the way, I feel the need very strongly to point out that we are living in a very particular weird bubble.
*  Most people don't go to college.
*  And by the way, the ones who do go to college, they're not 18 years old.
*  They're like 25 or something. I forget the numbers.
*  The places where we've been, where we are,
*  they look like whatever we think the traditional movie version of universities are,
*  but for most people, it's not that way at all.
*  By the way, most people who drop out of college, it's entirely for financial reasons.
*  So we're talking about a particular experience.
*  And so for that set of people, which is very small,
*  but larger than it was a decade or two or three or four, certainly, ago,
*  I don't think that will change.
*  My concern, which I think is kind of implicit in some of these questions,
*  is that somehow we will divide the world up further into the people who get to have this experience
*  and get to have the network and they sort of benefit from it,
*  and everyone else while increasingly requiring that they have more and more credentials
*  in order to get a job as a barista, right?
*  You got to have a master's degree in order to work at Starbucks.
*  We're going to force people to do these things,
*  but they're not going to get to have that experience,
*  and there'll be a small group of people who do who will continue to, you know,
*  positive feedback, et cetera, et cetera, et cetera.
*  I worry a lot about that, which is why for me,
*  and by the way, here's an answer to your question about faculty,
*  which is why to me that you have to focus on access and the mission.
*  I think the reason, whether it's good, bad, or strange, I mean, I agree it's strange,
*  but I think it's useful to have the faculty member, particularly at large R1 universities
*  where we've all had experiences, that you tie what they get to do
*  and with the fundamental mission of the university and let the mission drive.
*  What I hear when I talk to faculty is they love their PhD students
*  because they're reproducing, basically, right?
*  And it lets them do their research and multiply.
*  But they understand that the mission is the undergrads,
*  and so they will do it without complaint, mostly,
*  because it's a part of the mission and why they're here,
*  and they have experiences with it themselves,
*  and it was important to get them where they were going.
*  The people who tend to get squeezed in that, by the way, are the master students, right?
*  Who are neither the PhDs who are like us nor the undergrads
*  we've already bought into the idea that we have to teach, though.
*  That's increasingly changing.
*  Anyway, I think tying that mission in really matters,
*  and it gives you a way to unify people around making it an actual higher calling.
*  Education feels like more of a higher calling to me than even research,
*  because education, you cannot treat it as a hobby if you're going to do it well.
*  But that's the pushback on this whole system,
*  is that education should be a full-time job.
*  And almost like research is a distraction from that.
*  Yes, although I think many of our colleagues would say that research is the job,
*  and education is the distraction.
*  Right, but that's the beautiful dance.
*  It seems to be that tension in itself seems to bring out the best in the faculty.
*  But I will point out two things.
*  One thing I'm going to point out, and the other thing I want Michael to point out,
*  because I think Michael is much closer to the ideal professor in some sense than I am.
*  You're the platonic sense of a professor.
*  I don't know what he meant by that, but he is a dean, so he has a different experience.
*  I'm giving him time to think of the profound thing he's going to say.
*  That's good.
*  But let me point this out, which is that we have lecturers in the College of Computing where I am.
*  There's 10 or 12 of them depending on how you count, as opposed to the 90 or so tenure track faculty.
*  Those 10 lecturers who only teach, well, they don't only teach, they also do service.
*  Some of them do research as well, but primarily they teach.
*  They teach 50%, over 50% of our credit hours, and we teach everybody.
*  So they're doing more than eight times the work of the tenure track faculty,
*  just closer to nine or 10.
*  And that's including our grad courses, right?
*  So they're doing this, they're teaching more, they're touching more than anyone, and they're beloved for it.
*  So we recently had a survey.
*  Everyone does these alumni surveys.
*  You hire someone from the outside to do whatever, and I was really struck by something.
*  You saw all these really cool numbers.
*  I'm not going to talk about it because it's all internal confidential stuff.
*  But one thing I will talk about is there was a single question we asked our alum.
*  These are people who graduated, born in the 30s and 40s, all the way up to people who graduated last week, right?
*  Well, last semester.
*  Okay, good.
*  Time flies.
*  Yeah, time flies.
*  And there was a question.
*  Name a single person who had a strong positive impact on you, something like that.
*  I think it was special impact?
*  Yeah, special impact on you.
*  And then, so they got all the answers from people, and they created a word cloud.
*  It was clear, a word cloud created by people who don't do word clouds for a living
*  because they had one person whose name appeared nine different times, like Philip, Phil, Dr. Phil.
*  But whatever.
*  But they got all this.
*  And I looked at it, and I noticed something really cool.
*  The five people from the College of Computing, I recognized, were in that cloud.
*  And four of them were lecturers, the people who teach.
*  Two of them, relatively modern, both were chairs of our Division of Computing Instruction.
*  One retired, one is going to retire soon.
*  And the other two were lecturers I remembered from the 1980s.
*  Two of those four actually have-
*  By the way, the fifth person was Charles.
*  That's not important.
*  The thing is, I don't tell people that.
*  But the two of those people our teaching awards are named after.
*  Thank you, Michael.
*  Two of those our teaching awards are named after, right?
*  So when you ask students, alumni, people who are now 60, 70 years old even, who touched them?
*  They say the Dean of Students.
*  They say the big teachers who taught the big introductory classes that got me into it.
*  There's a guy named Richard Bark who's on there who's known as a great teacher.
*  The Phil Adler guy who I probably just said his last name wrong.
*  But I know the first name's Phil because it kept showing up over and over again.
*  Adler is what it said.
*  But different people spelled it differently.
*  So he appeared multiple times.
*  Right.
*  So he was a professor in the business school.
*  But when you read about him, I went to read about him because I was curious who he was.
*  It's all about his teaching and the students that he touched, right?
*  So whatever it is that we're doing and we think we're doing that's important
*  or why we think the universities function, the people who go through it,
*  they remember the people who were kind to them, the people who taught them something.
*  And they do remember it.
*  They remember it later.
*  I think that's important.
*  That's what the mission matters.
*  Not to completely lose track of the fundamental problem of how do we replace the party aspect of universities.
*  That's right.
*  Before we go to what makes the platonic professor, do you think,
*  like what in your sense is the role of MOOCs in this whole picture during COVID?
*  Like should we desperately be clamoring to get back on campus?
*  Or is this a stable place to be for a little while?
*  I don't know.
*  I know that the online teaching experience and learning experience has been really rough.
*  I think that people find it to be a struggle in a way that's not a happy, positive struggle.
*  That when you got through it, you just feel like glad that it's over as opposed to I've achieved something.
*  So, you know, I worry about that.
*  But, you know, I worry about just even before this happened, I worry about lecture teaching.
*  How well is that actually really working as far as a way to do education, as a way to inspire people?
*  I mean, all the data that I'm aware of seems to indicate, and this kind of fits, I think, with Charles' story,
*  is that people respond to connection, right?
*  They actually feel, if they feel connected to the person teaching the class, they're more likely to go along with it.
*  They're more able to retain information.
*  They're more motivated to be involved in the class in some way.
*  And that really matters.
*  You mean to the human themselves.
*  Yeah.
*  Can't you do that, actually, perhaps more effectively online?
*  Like you mentioned science communication.
*  So I literally, I think, learned linear algebra from Gilbert Strang by watching MIT OpenCourseWare when I was in direct.
*  And he was a personality.
*  He was a bit like a tiny little...
*  In this tiny little world of math, he's a bit of a rock star, right?
*  So you kind of look up to that person.
*  Can't that replace the in-person education?
*  It can help.
*  I will point out something.
*  I can't share the numbers, but we have surveyed our students, and even though they have feelings about what I would interpret as connection,
*  I like that word, in the different modes of classrooms, there's no difference between how well they think they're learning.
*  For them, the thing that makes them unhappy is the situation they're in.
*  And I think the lack of connection, it's not whether they're learning anything.
*  They seem to think they're learning something anyway, right?
*  In fact, they seem to think they're learning it equally well, presumably because the faculty are putting in,
*  or the instructors, more generally speaking, are putting in the energy and effort to try to make certain that what they've curated can be expressed to them in a useful way.
*  But the connection is missing.
*  And so there's huge differences in what they prefer.
*  And as far as I can tell, what they prefer is more connection, not less.
*  That connection just doesn't have to be physically in a classroom.
*  I mean, look, I used to teach 348 students in a machine learning class on campus.
*  Do you know why?
*  That was the biggest classroom on campus.
*  They're sitting in theater seats.
*  I'm literally on a stage looking down on them and talking to them, right?
*  There's no, I mean, we're not sitting down having a one-on-one conversation,
*  reading each other's body language, trying to communicate and going, we're not doing any of that.
*  So if you're past the third row, it might as well be online anyway, is the kind of thing that people have said.
*  Daphne has actually said some version of this, that online starts on the third row or something like that.
*  And I think that's not, yeah, I like it.
*  I think it captures something important.
*  But people still came, by the way.
*  Even the people who had access to our material would still come to class.
*  I mean, there's a certain element about looking to the person next to you.
*  Yeah.
*  It's just like their presence there, their boredom.
*  And like when the parts are boring and their excitement, when the parts are exciting, like in sharing in that unspoken kind of communication.
*  In part, the connection is with the other people in the room.
*  Watching the circus on TV alone is not really...
*  Have you ever been to a movie theater and been the only one there at a comedy?
*  It's not as funny as when you're in a room full of people all laughing.
*  Well, maybe you need just another person as opposed to many.
*  Maybe there's some kind of...
*  Well, there's different kinds of connection.
*  And there's different kinds of comedy.
*  As we're learning today.
*  I wasn't sure if that was going to land.
*  Just the idea that different jokes...
*  I've now done a little bit of standup.
*  And so different jokes work in different size crowds too.
*  No, it's true.
*  Where sometimes if it's a big enough crowd, then even a really subtle joke can take root someplace and then that cues other people.
*  And it kind of...
*  There's a whole statistics of...
*  I did this terrible thing to my brother.
*  So when I was really young, I decided that my brother was only laughing at sitcoms when I left.
*  He was taking cues from me.
*  So I purposely didn't laugh just to see if I was right.
*  And did you laugh at non-funny things?
*  Yes.
*  You didn't really want to do both sides.
*  I did both sides.
*  And at the end of it, I told him what I did.
*  He was very upset about this.
*  And from that day on...
*  He lost his sense of humor.
*  No, no, no, no.
*  Well, yes.
*  But from that day on, he laughed on his own.
*  He stopped taking cues from me.
*  I see.
*  So I want to say that it was a good thing that I did.
*  Yes, yes.
*  You saved that man's life.
*  Yes, but it was mostly me.
*  But it's true, though.
*  It's true, right?
*  That people...
*  I think you're right.
*  But okay.
*  So where does that get us?
*  That gets us the idea that...
*  I mean, certainly movie theaters are a thing, right?
*  Where people like to be watching together, even though the people on the screen aren't
*  really co-present with the people in the audience.
*  The audience is co-present with themselves.
*  By the way, at that point, it's an open question that's being raised by this, whether movies
*  will no longer be a thing because Netflix's audience is growing.
*  So that's a very parallel question for education.
*  Will movie theaters still be a thing in 2021?
*  No, but I think the argument is that there is a feeling of being in the crowd that isn't
*  replicated by being at home watching it and that there's value in that.
*  And then I think just...
*  But...
*  But...
*  It scales better on the line.
*  But I feel like we're having a conversation about whether concerts will still exist after
*  the invention of the record or the CD or wherever it is, right?
*  They won't.
*  You're right.
*  Concerts are dead.
*  Well, okay.
*  I think the joke is only funny if you say it before now.
*  Right.
*  Yeah, that's true.
*  Like three years ago.
*  It's like, well, no, obviously, concerts are still a big thing.
*  I'll wait to publish this until we have a vaccine.
*  We'll fix it in post.
*  We'll fix it in post.
*  But I think the important thing is...
*  Fix the virus.
*  Concerts changed, right?
*  Concerts changed.
*  First of all, movie theaters weren't this way, right?
*  In the 60s and 70s, they weren't like this.
*  Blockbusters were basically what?
*  Jaws and Star Wars created Blockbusters, right?
*  Before then, there weren't.
*  The whole shared summer experience didn't exist in our lifetimes, right?
*  Certainly, you were well into adulthood by the time this was true, right?
*  So it's just a very different...
*  It's very different.
*  So what we've been experiencing in the last 10 years is not like the majority of human history,
*  but more importantly, concerts, right?
*  Concerts means something different.
*  Most people don't go to concerts anymore.
*  Like there's an age where you care about it.
*  You sort of stop doing it, but you keep listening to music or whatever and da-da-da-da-da-da-da.
*  So I think that's a painful way of saying that it will change.
*  It was not the same thing as it going away.
*  Replace is too strong of a word, but it will change.
*  It has to.
*  I actually like to push back.
*  I wonder because I think you're probably just throwing that your intuition out.
*  I want and it's possible that concerts, more people go to concerts now,
*  but obviously much more people listen to what is dumb than before there was records.
*  It's possible to argue that if you look at the data,
*  that it just expanded the pie of what music listening means.
*  So it's possible that like universities grow in the parallel or the theaters grow,
*  but also more people get to watch movies.
*  More people get to like be educated.
*  I hope that.
*  Yeah.
*  And to the extent that we can grow the pie and have education be not just something you do for four years
*  when you're done with your other education, but it be a more lifelong thing.
*  That would have tremendous benefits, especially as the economy and the world change rapidly.
*  Like people need opportunities to stay abreast of these changes.
*  And so I don't know, I could, I could.
*  It's all part of the ecosystem.
*  It's all to the good.
*  I mean, you know, I'm not going to have an argument about whether we lost fidelity when we went from laser disc to DVDs or record players to CDs.
*  I mean, I'm willing to grant that that is true, but convenience matters.
*  And the ability to do something that you couldn't do otherwise because that convenience matters.
*  And you can tell me I'm only getting 90% of the experience, but I'm getting the experience.
*  I wasn't getting it before or wasn't lasting as long or it wasn't as easy.
*  I mean, this just seems, this just seems straightforward to me.
*  It's going to, it's going to change.
*  It is for the good that more people get access.
*  And it is our job to do two separate things.
*  One, to educate them and make access available.
*  That's our mission.
*  But also for very simple, selfish reasons, we need to figure out how to do it better so that we individually stay in business.
*  We can do both of those things at the same time.
*  They are not in, they may be intention, but they are not mutually exclusive.
*  So you've educated some scary number of people.
*  So you've seen a lot of people succeed, find their path through life.
*  Is there a device that you can give to a young person today about computer science education, about education in general, about life, about whatever the journey that one takes in there, maybe in their teens, in their early 20s, sort of in those underground years, as you try to go through the essential process of success.
*  And you're in the process of partying and not going to classes and yet somehow trying to get a degree.
*  If you get to the point where you're, you're, you're far enough up in the, in the hierarchy of needs that you can actually make decisions like this, then find the thing that you're passionate about and pursue it.
*  And sometimes it's the thing that drives your life and sometimes it's secondary and you'll do other things because you've got to eat, right?
*  You got a family, you got to feed, you got people you have to help or whatever.
*  I understand that and it's not easy for everyone, but always take a moment or two to pursue the things that you love, the things that bring passion and happiness to your life.
*  And if you don't, I know that sounds corny, but I genuinely believe it.
*  And if you don't have such a thing, then you're lying to yourself.
*  You have such a thing.
*  You just have to find it.
*  And it's okay if it takes you a long time to get there.
*  Rodney Dangerfield became a comedian in his 50s, I think.
*  Certainly was in his 20s and lots of people failed for a very long time before getting to where they were going.
*  You know, I try to have hope and it wasn't obvious.
*  I mean, you know, we, you and I talked about the experience that I had a long time ago with, with a particular police officer.
*  Was it my first one?
*  And was it my last one?
*  But, you know, in my view, I wasn't supposed to be here after that and I'm here.
*  So it's all gravy.
*  So you might as well go ahead and grab life as you can because of that.
*  That's that's sort of how I see it while recognizing again, the delusion matters, right?
*  Allow yourself to be deluded.
*  Allow yourself to believe that it's all going to work out.
*  Just don't be so deluded that you you miss the obvious and you're going to be fine.
*  It's going to be there.
*  It's going to be there.
*  It's going to work out.
*  What do you think?
*  I like to say choose your parents wisely because that has a big impact on your life.
*  Yeah, I mean, you know, I mean, there's a whole lot of things that you don't get to pick.
*  And whether you get to have, you know, one kind of life or a different kind of life can depend a lot on things out of your control.
*  But I really do believe in the in the passion excitement thing.
*  I was talking to my mom on the phone the other day and.
*  Essentially, what came out is that computer science is really popular right now.
*  And I get to be a professor teaching something that's very attractive to people.
*  And she was like.
*  Trying to give me some appreciation for how for sightful I was for choosing this line of work as if somehow I knew that this is what was going to happen in 2020.
*  But that's not how it went for me at all.
*  Like I studied computer science because I was just interested.
*  It was just so interesting to me.
*  I didn't think it would be particularly lucrative.
*  Yeah.
*  And I've done everything I can to keep it as un-lucrative as possible.
*  Yeah.
*  Some of my, you know, some of my friends and colleagues have have to have not done that.
*  And I pride myself on my ability to just to remain un-rich.
*  But but but but I do believe that that like I'm glad.
*  I mean, I'm glad that it worked out for me.
*  It could have been like, oh, I would.
*  I was really fascinated by is this particular kind of engraving that nobody cares about.
*  But so I got lucky in the thing that I cared about happened to be a thing that other people eventually cared about.
*  But I don't think I would have had a fun time choosing anything else.
*  Like this was the thing that kept me interested and engaged.
*  Well, one thing that people tell me, especially early undergraduate and the Internet is part of the problem here, is they say they're passionate about so many things.
*  How do I choose a thing, which is an harder thing for me to know what to do with?
*  Is there any?
*  I mean, don't you know?
*  I mean, you know, a long time ago, I walked down a hallway and I took a left turn.
*  Yeah, I could have taken a right turn in my world could be better or it could be worse.
*  I have no idea. I have no way of knowing.
*  Is there anything about this particular hallway that's relevant or you just in general choices?
*  Yeah, you were on the left.
*  It sounds like you regret not taking the right.
*  Oh, no, not at all.
*  You brought it up.
*  Well, because it was a turn.
*  It's a turn there.
*  On the left was Michael Lemmon's office, right?
*  I mean, these sorts of things happen, right?
*  But here's the thing.
*  By the way, it was just a blank wall.
*  It wasn't a huge choice.
*  It would have really hurt.
*  He tried first.
*  But it's true, right?
*  I think about Ron Brockman, right?
*  I went, I took a trip I wasn't supposed to take and I ended up talking to Ron about this and I ended up going down this entire path.
*  That allowed me to, I think, get tenure.
*  But by the way, I decided to say yes to something that didn't make any sense.
*  And I went down this educational path.
*  But it would have been, you know, who knows, right?
*  Maybe if I hadn't done that, I would be a billionaire right now.
*  I'd be Elon Musk.
*  My life could be so much better.
*  My life could also be so much worse.
*  You know, you just got to feel that sometimes you have decisions you're going to make.
*  You cannot know what's going to do.
*  You should think about it, right?
*  Some things are clearly smarter than other things.
*  You got to play the odds a little bit.
*  But in the end, if you've got multiple choices or lots of things you think you might love, go with the thing that you actually love, the thing that jumps out at you and sort of pursue it for a little while.
*  The worst thing that will happen is you took a left turn instead of a right turn and you ended up merely happy.
*  Beautiful.
*  So, so accepting, so taking the step and just accepting, accepting that that don't like question, question, question.
*  Life is long and there's time to actually pursue every once in a while.
*  You have to put on a leather suit and make a thriller video every once in a while.
*  If I ever get the chance again, I'm doing it.
*  Yeah, I was told that you actually danced, but that part was edited out.
*  I don't dance.
*  There was a thing where we did do the zombie thing.
*  We did do the zombie.
*  That wasn't edited out.
*  It just wasn't put into the final thing.
*  I'm quite happy.
*  But there was a reason for that too, right?
*  Like I wasn't wearing something right.
*  There was a reason for that.
*  I can't remember what it was.
*  No, leather suit.
*  Is that what it was?
*  I can't remember.
*  Anyway, the right thing happened.
*  Exactly.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  I'm going to ask you a question.
*  One of the magic things about the internet
*  of the people that write me is
*  I don't know.
*  My answer is different.
*  My daughter is taking AP computer science right now.
*  Hi, Joni.
*  She's amazing and doing amazing things.
*  My son is beginning to get interested
*  and I'm really curious where he takes it.
*  I think his mind actually works very well
*  for this sort of thing and she's doing great.
*  One of the things I have to tell her
*  all the time is, well, I want to make a rhythm game.
*  I want to go
*  for two weeks and then build a rhythm game.
*  Show me how to build a rhythm game.
*  Start small.
*  Learn the building blocks and how to take the time.
*  Have patience. Eventually you'll build a rhythm game.
*  I was in grad school when I suddenly
*  woke up one day over the Royal East
*  and I thought, wait a minute.
*  I'm a computer scientist. I should be able to write Pac-Man
*  in an afternoon. And I did.
*  Not with great graphics. It was actually a very cool game.
*  I had to figure out how the ghost moved and everything
*  and I did it in an afternoon in Pascal
*  on an old Apple IIGS.
*  But if I had started out trying to build Pac-Man,
*  I think it probably would have ended very poorly for me.
*  Luckily back then, there weren't
*  these magical devices we call phones
*  and software everywhere to give me this illusion
*  that I could create something by myself
*  from the basics inside of a weekend like that.
*  I mean, that was a
*  culmination of years and years and years
*  right before I decided I should be able to write this
*  and I could. So, my advice if you're early on
*  is, you've got the internet.
*  There are lots of people there to give you the information.
*  You've got the internet.
*  There are lots of people there to give you the information.
*  Find someone who cares about this.
*  Remember, they've been doing it for a very long time.
*  Take it slow. Learn the little pieces.
*  Get excited about it and then keep the big
*  project you want to build in mind.
*  You'll get there soon enough because, as a wise man
*  once said, life is long.
*  Sometimes it doesn't seem that long, but it is
*  long and you'll have enough
*  time to build it all out.
*  All the information is out there.
*  But start small.
*  Generate Fibonacci numbers.
*  It's not exciting, but it'll get you
*  a better language.
*  Well, there's only one programming language, it's Lisp.
*  But, if you have to pick a programming
*  language, I guess in today's
*  day, what would I do? I guess I'd do
*  Python is basically Lisp, but with
*  better syntax.
*  Blasphemy. Yeah. With C syntax.
*  How about that? So, you're going to argue that C
*  syntax is better than anything?
*  Anyway, I'll go, I'm going to answer
*  Python despite what you said. Tell me, tell your story
*  about somebody's dissertation that had
*  a Lisp program in it. It was so
*  funny. This is Dave's.
*  Dave's dissertation was like, Dave McAllister, who was a
*  professor at MIT for a while, and then he came
*  in our labs.
*  Now he's at Technology,
*  Technical Institute of Chicago. A brilliant guy.
*  Such an interesting guy.
*  Anyway, his thesis,
*  it was a
*  theorem prover, and he decided
*  to have as an appendix
*  his actual code, which of course
*  was all written in Lisp, because of course it was.
*  And like the last 20 pages are just right
*  parentheses.
*  It's wonderful.
*  That's programming right there.
*  Pages of book pages are right parentheses.
*  Anyway, Lisp is the only real language,
*  but I understand that that's not necessarily the place where
*  you start. Python is just fine.
*  Python is good.
*  If you're, you know, of a certain age,
*  if you're really young and trying to figure it out, graphical
*  languages that let you kind of see how the thing works,
*  that's fine too. They're all fine. It almost
*  doesn't matter, but there are people who spend a lot of time
*  thinking about how to build
*  languages that get people in.
*  The question is, are you trying to get in
*  and figure out what it is, or do you already know
*  what you want? And that's why I asked you
*  what stage of life people are in, because if you're different stages
*  of life, you would attack it differently.
*  The answer to that question of which
*  language keeps changing, I mean there's some
*  value to exploring
*  a lot of people
*  write to me about Julia.
*  There's these like more modern languages
*  that keep being invented, Rust
*  and Kotlin.
*  There's stuff that
*  for people who love functional
*  languages like Lisp,
*  apparently there's echoes of that,
*  but much better in the modern
*  languages. And it's worthwhile to
*  especially when you're learning
*  languages, it feels like it's okay to
*  try one that's not like
*  the popular one. Oh yeah, but you know
*  I think you get that way
*  of thinking almost no matter
*  what language. And
*  if you push far enough, like it can be assembly
*  language, but you need to push pretty far
*  before you start to hit the really deep concepts
*  that you would get sooner in other languages.
*  But like, I don't know, computation
*  is kind of computation, is kind of
*  Turing equivalent is kind of computation.
*  And so it matters
*  how you express things, but you have to build out
*  that mental structure in your mind.
*  And I don't think
*  it super matters which language. I mean
*  it matters a little, because some things are just at the wrong
*  level of abstraction. I think assembly's at the wrong
*  level of abstraction for someone coming in new.
*  I think that
*  For someone coming in new. Yes.
*  For frameworks, big frameworks
*  are quite a bit. You know, you've got to
*  get to the point where I want to learn a new language
*  means I just pick up a reference book and I think of a
*  project and I go through it in a weekend.
*  You've got to get there. You're right though,
*  the languages that are designed for that are
*  it almost doesn't matter.
*  Pick the ones that people have built
*  tutorials and infrastructure around to help
*  you get kind of eased into it.
*  Because it's hard. I mean, I did this little experiment once.
*  I was teaching intro to CS
*  in the summer as a favor.
*  Which is, anyway. Pleasant memories.
*  I was teaching intro to CS as a favor.
*  And it was very funny because I'd go in every single time
*  and I would think to myself
*  how am I possibly going to fill up an hour and a half
*  talking about for loops, right?
*  And there wasn't enough time.
*  It took me a while to realize this, right?
*  There are only three things, right? There's reading from a variable,
*  writing to a variable, and conditional branching.
*  Everything else is syntactic sugar.
*  Right? The syntactic sugar matters.
*  But that's it. And when I say that's it,
*  I don't mean it's simple.
*  I mean it's hard. Like, conditional
*  branching, loops, variables.
*  Those are really hard concepts.
*  So you shouldn't be discouraged by this.
*  Here's a simple experiment. I'm going to ask you a question now.
*  You ready?
*  X equals three.
*  Y equals four.
*  What is X?
*  Three. What is Y?
*  Four. Y equals X.
*  No? Oh, it's easy.
*  Y equals X.
*  What is Y?
*  Three. That's right.
*  X equals seven.
*  What is Y?
*  That's one of the trickiest things to get
*  for programmers. That there's a memory
*  and the variables are
*  pointing to a particular thing in memory.
*  And sometimes the languages hide that
*  from you and they bring it closer to the way
*  you think mathematics works.
*  Right. So in fact, Mark Guzdial, who
*  worries about these sorts of things, or used to worry about these
*  sorts of things anyway, had this
*  kind of belief that actually
*  people, when they see these statements,
*  X equals something, Y equals something, Y equals X.
*  That you have now
*  made a mathematical statement
*  that Y and X are the same.
*  Which you can if you just put like an
*  anchor in front of it. Yes, but
*  people, that's not what you're doing. Right?
*  I thought, and
*  I kind of asked the question, and I think I had some evidence
*  for this, it's hardly a study, is that
*  most of the people who didn't know the answer
*  or weren't sure about the answer, they had used
*  spreadsheets.
*  And so it's a name,
*  it's, you know,
*  it's by
*  reference, or by name really. Right?
*  And so depending upon what you think,
*  they are, you get completely different answers.
*  The fact that I could go, or one could
*  go, two thirds of the way through
*  a semester, and people still
*  hadn't figured out in their heads, when you say
*  Y equals X what that meant,
*  tells you it's actually hard.
*  Because all those answers are possible,
*  and in fact, when you said, oh, if you just put an ampersand
*  in front of it, I mean, that doesn't make any sense
*  for an intro class, and of course a lot of languages
*  don't even give you the ability to think about it in terms of ampersand.
*  Do we want to have a 45 minute discussion
*  about the difference between equal, EQ, and
*  equal in Lisp?
*  I know you do.
*  But, you know, you could
*  do that. This is actually really hard stuff.
*  So you shouldn't be, it's not too hard,
*  we all do it, but you shouldn't be discouraged.
*  That's why you should start small,
*  so that you can figure out these things, so you have the right
*  model in your head, so that when you
*  write the language, you can execute it,
*  and build the machine that you want to build.
*  Right? Yeah, the funny thing about programming
*  and those very basic things
*  is the very basics
*  are not often made explicit,
*  which is actually what drives
*  everybody away from basically any
*  discipline, but programming is just another one.
*  Like, even a simpler version of the equal sign
*  that I kind of forget
*  is in mathematics,
*  equals is not assignment.
*  Yeah.
*  Like, I think basically
*  every single programming language with just
*  a few handful of exceptions
*  equals is assignment.
*  You have some other operator for
*  equality.
*  And, you know, even that, like, everyone
*  kind of knows it
*  once you started doing it,
*  but, like, you need to say that explicitly,
*  or you just realize it,
*  like, yourself.
*  Otherwise, you might be stuck
*  for, you said, like, half a semester.
*  You could be stuck for quite a long time.
*  And I think also part
*  of the programming is being
*  okay in that state of
*  confusion for a while.
*  It's to the debugging point.
*  It's like, I just wrote two lines of code.
*  Why doesn't this work?
*  And staring at that for, like, hours.
*  And trying to figure out.
*  And then every once in a while, you just have to
*  restart your computer and everything works again.
*  And then you just
*  kind of stare into the
*  void with the tears slowly
*  rolling down your eye. By the way, the fact
*  that they didn't get this actually had no impact
*  on, I mean, they were still able to
*  do their assignments. Right. Because it turns out
*  their misunderstanding
*  wasn't being revealed to them.
*  By the problem sets we were
*  giving them. Found, actually, yeah.
*  I wrote a
*  program a long time ago, actually
*  for my master's thesis. And
*  in C++, I think. Or C. I guess
*  it was C. And it was all memory
*  management and terrible.
*  And it wouldn't work for
*  a while. And
*  it was some kind of, it was clear to me that it was
*  overwriting memory. And I just couldn't,
*  I was like, look, I got a paper done
*  time for this. So I basically
*  declared a variable at the
*  front in the main that was like
*  400k, just an array.
*  And it worked. Because wherever
*  I was scribbling over memory, it would
*  scribble into that space and it didn't matter.
*  And so I never figured out what the bug was.
*  But I did create something
*  to sort of deal with it. To work around it.
*  And it, you know, that's crazy.
*  That's crazy. It was okay because that's what I wanted.
*  But I knew enough about memory manage
*  to go, you know, management to go, you know,
*  I'm just going to create an empty array here and hope that
*  that deals with the scribbling memory problem.
*  And it did. That takes a long time to figure out.
*  And by the way, the language you first learned probably is
*  garbage collection anyway. So you're not even going to come up
*  across, you're not going to come across that problem.
*  So we talked about the
*  Minsky idea of hating everything
*  you do and hating yourself.
*  So let's end
*  on a question that's going
*  to make both of you very uncomfortable.
*  Which is, what is your,
*  Charles, what's your favorite
*  thing that
*  you're grateful for about
*  Michael? And Michael,
*  what is your favorite thing that you're grateful
*  for about Charles?
*  Well, that answer is actually quite easy.
*  His friendship.
*  He stole the easy answer.
*  I did. Yeah. I can tell you what I hate about Charles.
*  It steals my good answers.
*  The thing I like most about Charles,
*  he sees the world in it in a
*  similar enough but different way
*  that it's sort of like having
*  another life.
*  It's sort of like I get to experience
*  things that I wouldn't otherwise get to experience
*  because I would not naturally gravitate to them
*  that way. And so he just
*  shows me a whole other world.
*  It's awesome. Yeah. The inner
*  product is not zero
*  for sure. It's not quite one.
*  0.7 maybe.
*  Just enough that you can
*  learn.
*  Just enough that you can learn.
*  That's the definition of friendship. The inner product
*  is 0.7. Yeah. I think so. That's
*  the answer to life really. Charles sometimes
*  believes in me when I have not believed
*  in me. He also sometimes works as an outward
*  confidence that he has
*  so much, so much
*  confidence and self
*  I don't know, awareness, comfortableness.
*  Okay. Let's go with that.
*  That I feel better
*  a little bit. If he
*  thinks I'm okay, then maybe I'm not as bad as
*  I think I am. At the end of the
*  day, luck favors the Charles.
*  It's
*  a huge honor to talk with you.
*  Thank you so much for taking this time,
*  wasting your time with me. It was an awesome
*  conversation. You guys are an inspiration to
*  a huge number of people
*  and to me. So, I really enjoyed this.
*  Thanks for talking. I enjoyed it as well. Thank you so much.
*  And by the way, if luck favors the Charles, then it's certainly
*  the case that I've been very lucky to
*  tell you. I'm going to add that part out.
*  Thanks for listening to this conversation with
*  Charles Isbell and Michael Litman.
*  And thank you to our sponsors.
*  Athletic Greens,
*  Super Nutritional Drink,
*  8 Sleep, Self-Cooling
*  Mattress, Master Class
*  Online Courses
*  from some of the most amazing humans in history,
*  and Cash App,
*  the app I use to send money to friends.
*  Please check out the sponsors
*  in the description to get a discount
*  and to support this podcast.
*  If you enjoy this thing,
*  subscribe on YouTube, review it with
*  5 Stars on Apple Podcasts, follow on
*  Spotify, support it on Patreon,
*  connect with me on Twitter,
*  and Lex Friedman.
*  And now, let me leave you with some words from Desmond Tutu.
*  Don't raise your voice.
*  Improve your argument.
*  Thank you for listening,
*  and hope to see you next time.
