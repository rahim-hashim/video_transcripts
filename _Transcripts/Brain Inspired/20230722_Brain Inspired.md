---
Date Generated: April 19, 2024
Transcription Model: whisper medium 20231117
Length: 5081s
Video Keywords: []
Video Views: 758
Video Rating: None
---

# BI 171 Mike Frank: Early Language and Cognition
**Brain Inspired:** [July 22, 2023](https://www.youtube.com/watch?v=GlyUrHDfDTA)
*  I'm fascinated by language in general, and I always have been.
*  And I focused in on early word learning because it's, you might call it the smallest big thing.
*  The listeners thinking, what was the speaker's goal given that they said this utterance?
*  And then the speaker's thinking, how would I get the listener to figure out my goal?
*  Which utterance should I choose?
*  And of course, that's a recursive formulation.
*  The listener speaking, thinking about speaker, speaker's thinking about listener.
*  Yeah, this kind of question is really controversial in part because there's a lot of ambiguity when somebody asks the question, what is the function of language?
*  So philosophers have a lot to say about distinguishing different kinds of functions, but minimally we can say...
*  This is Brent Inspired.
*  I'm Paul.
*  Welcome, everyone.
*  My guest today is Michael C. Frank, better known as Mike Frank, who runs the language and cognition lab at Stanford.
*  Mike's main interests center on how children learn language, and in particular, he focuses a lot on early word learning and what that tells us about our other cognitive functions like concept formation and social cognition.
*  So we discussed that.
*  We discuss his love for developing open data sets that anyone can use.
*  Mike dances the dance between bottom up data driven approaches in this big data era and traditional experimental approaches and top down theory driven approaches.
*  So we talk about those different approaches and the advantages and disadvantages.
*  We talk about how early language learning in children differs from large language models and large language models in general.
*  We also discuss one of Mike's normative language models called the Rational Speech Act model, or RSA model of language use, which considers the intentions or pragmatics of speakers and listeners in dialogue.
*  And of course, we talk about how his model compares to large language models and a lot of other topics as well.
*  You can support this podcast on Patreon if you value it.
*  That or signing up for my Neuro AI course online are the very best ways to support what I do.
*  So you can go to BrainInspired.co to learn more about those.
*  I'd like to give a special thanks to Yolanda and Kendra, whom I got to meet at the recent Gordon Research Seminar and Conference for iMovements.
*  Thank you both for being patrons for over two years now.
*  So awesome. Yolanda, it's nice to meet you finally.
*  And thank you for the invitation.
*  And Kendra, I enjoyed being squeezed in your car for a few minutes with those other clowns.
*  And great to see lots of old friends and meet new ones as well at the conference.
*  And now here's Mike.
*  Oh, wait, I forgot to mention the show notes for this episode are at BrainInspired.co slash podcast slash 171, where you can learn more about Mike and the excellent science he does.
*  OK, here's Mike.
*  So bluegrass music.
*  Do you play bluegrass?
*  I do. Yeah, I play the mandolin.
*  So I've said this and thought this about jazz and I think and have said the same about bluegrass that it's more about the for the player than the audience.
*  Is that too scathing?
*  Or would you disagree?
*  No, I think that's totally true.
*  I actually didn't.
*  Thank you.
*  I didn't like bluegrass before I started playing it, but I loved the ability to play with other people and to have a language that I could use.
*  So in bluegrass, there are all these rules that mean that you can roll up to a jam and somebody can call a tune you've never heard before.
*  And by the end of three minutes, you know, you all are playing together, singing harmony on the chorus.
*  It's a very, very structured way of interacting, really very much like jazz.
*  And the amazing thing about bluegrass is, you know, you can master those skills with a couple of years of hard practice, whereas jazz really takes a lifetime.
*  Oh, and rock and roll takes two minutes.
*  Well, I was in rock and all through high school and college.
*  I mean, that's definitely my first love in terms of listening to music.
*  But I've grown to love bluegrass because I can just go anywhere in the world and immediately connect with people.
*  I'll see.
*  I appreciate that.
*  And I appreciate like the skills aspect.
*  But from a aesthetics in listening, have you come to enjoy bluegrass?
*  Just can you just sit back?
*  My old friends, they were like, oh, I'm going to play a song.
*  Can you just sit back?
*  My old neighbor, who was a painter and artist, he would always have bluegrass and he played bluegrass, but he would always have it in the background while he was painting.
*  And so can you it must bring you joy now to just consume it as well.
*  Not always.
*  So I remember coming back in a car, very kind of vivid memory of driving through the beautiful marine hills, coming back from my first bluegrass camp.
*  That's actually before I played the mandolin.
*  And I remembered I was just in love.
*  Like I wanted to immerse myself and understand this genre so that I could get this incredible high of playing with people and producing music.
*  And so I put on some really banjo heavy bluegrass, flattened scrubs or something.
*  And I thought, oh, I don't know that I want to listen to this.
*  But look, I love new acoustic music.
*  You know, Tony Rice, David Grisman, this kind of stuff that I'll listen to all day.
*  But there is a certain kind of real banjo forward thing that is not my bag, per se.
*  OK, well, it was a great segue that you mentioned language and enjoying that, you know, that there is a language to communicate with your other bluegrass players.
*  Because we're going to talk a lot about language today.
*  And that is, you know, the main focus of your research.
*  And you can correct me is in how we acquire language and language learning, especially from a very young, I guess, early word learning would be your specialization.
*  Is that right?
*  Yeah, I'm fascinated by language in general.
*  And I always have been and I focused in on early word learning because it's you might call it the smallest big thing.
*  Right. It's a very manageable problem in some sense.
*  Like we have all these wonderful word learning experiments where we can teach a kid a word in the lab and we know they learned that word.
*  But it's also connected to social cognition.
*  It's connected to language structure.
*  It's connected to sound structure and so forth.
*  So it's both a very tiny, well operationalized construct that you can study in a controlled way and also just this incredible universe of possibilities, connections to different aspects of cognition and language.
*  OK, so I was going to ask how your interests and your research focus has changed over the course of your academic career.
*  But you just said that you've always been interested in language.
*  But you come from a Bayesian background as well.
*  And we'll get into your modeling aspect of it as well.
*  But that's why I was curious.
*  Like if it started off with like, oh, is he more of Bayesian or is he more language?
*  Like how you began and that trajectory?
*  You know, it's funny, you know, you have these intuitions about the topic you're studying sometimes, especially when the topic is psychology or cognitive science.
*  And for me, that intuition was something like that language was really critical to thinking and structuring the world.
*  And I remember having these conversations, you know, back in high school, late at night about thinking of language and just thinking about, you know, your thoughts, like one of those kind of late night introspective ideas.
*  And then in college, when somebody assigned me a little bit of Wittgenstein, I read that I thought, yes, this is how it works.
*  We're just deciding on the ways that we communicate and coordinate with one another.
*  And so I became a, you know, roughly a philosophy major.
*  I mean, I was I was a symbolic systems undergraduate, which is actually our cognitive science major.
*  But I was a philosophical foundations concentrator, which meant I was reading Wittgenstein and doing a lot of philosophy of language.
*  And, you know, then I tried to get involved in research and they were like, well, OK, you're doing the research right now.
*  You know, you're thinking about it.
*  And that didn't seem so satisfying.
*  So I ended up going kind of in a more empirical direction.
*  I had some great mentors in psychology who encouraged me to study language with empirical tools from cognitive science and especially developmental tools.
*  But so I was always interested in language and thought and this connection.
*  It was just that the approaches have changed pretty radically over the years.
*  OK, but you're not like a Chomskyian that language is for thought.
*  No, no, I think that language is functionally for communication.
*  And much of my work has been about cashing out what that means and how it might affect interpretation in the moment, as well as a little bit how it might affect the structure of language downstream.
*  OK, yeah, we'll come back to function of language in a minute.
*  But I was going to open with a sort of morose question, which would be, you know, what would your scientific tombstone say if you just vanished from the science community right now?
*  And the reason why I brought this up now is because you said, well, you know, your mentors and your advisors said, well, you're doing the the empirical work right now by using words.
*  And if I understand it correctly, you kind of had a backlash because you wanted to get into like numbers and computational, theoretically driven aspects of understanding how we acquire language.
*  So would your tombstone say something like that?
*  Maybe a little less long winded?
*  Well, there's what I'd want it to say and what it would say.
*  I think I would want it to say something about bringing bigger data sets to bear on fundamental questions about the origins of language and the variation between kids and between languages.
*  That's your more recent interest, correct?
*  Yeah, so there's real continuity in my interest in the sense that I've always wanted to create unified computational theories.
*  It's just that when I started to try to do that, the rubber met the road, I realized there just wasn't enough data about the questions that I was interested in theorizing on.
*  And so in some sense, the questions, the theories, all of those are, you know, relatively older.
*  I'm trying to answer questions that people have been asking for a long time.
*  And the project has been to get the resources, mostly data, but then increasingly the formal models to run over those data and then actually be able to evaluate hypotheses which many people have had.
*  Well, maybe I'll just maybe we'll go ahead and talk about this because I was going to ask about, you know, building these repositories.
*  I know that you ran out of good data for your models and so you needed more data.
*  So, you know, now you're like building essentially like tools and open source tools and you're building these repositories.
*  Like tools and open source tools, publicly available data sets and for people to come use them when they want.
*  How's that going? Like this is a huge focus of your work right now.
*  I know. And I think I saw in one of your talks, you put up the Field of Dreams poster, the If You Build It, They Will Come.
*  And so is that true? If you build great tools, will they come and use them?
*  Well, the contrast that I sometimes make in the talks is between the Field of Dreams model where you just build something and people show up and use it versus something a bit more product and user focused, which is to drive adoption of a tool.
*  You need to really think about what people want and then you need to promote it and build a user base and gradually kind of gain steam in the community.
*  So I don't think we're really at the Field of Dreams level right now.
*  You know, the other alternative, which is maybe another bad way to go, is the Joshua Bell and the Subway model where you're fiddling away, you're doing something amazing.
*  You know, it's world class and nobody stops to look and listen.
*  Right. So we're trying to navigate these things in repository building, tool building, data sharing is really it's a critical challenge right now.
*  But is so you have to promote it.
*  Was that is that high on your list of desires, promotional activities?
*  Well, you know, it's not like we're advertising in the subway.
*  Instead, what we're doing and what I think about when I'm constructing these repositories is not, oh, there should be such a repository, because I think that's the way some people approach it is there should be a thing that does X and we're going to build the tool.
*  I actually go into it with a much more I could call it selfish, but it's a scientific motivation.
*  I want to do this kind of analysis.
*  I think this kind of analysis will answer my question.
*  And so I want to get together the kind of data set that will allow that analysis.
*  And I've learned from experience that if you structure the data in an appropriate way, that analysis will be easier and a hundred other analyses will be easier, too.
*  So I'm going in it thinking, hey, maybe I can get enough data together to get a really clear picture of something that I couldn't see before.
*  So we don't need to spend too much time persevering on this.
*  But, you know, have you like had people come and say, well, actually, I need it structured a slightly different way.
*  Have you had to modify the structures of the data over time?
*  I I've had a couple of really wonderful collaborations across the years with folks who are very technically sophisticated and talented.
*  Mika Brzezinski is one.
*  Stefan Mehlins is another.
*  These are folks that actually came into my lab quite early on when I was getting started.
*  And they've taught me about the open source community and tool design and the set of practices that make it relatively easy to create a kind of an API that is centered around what you might want to do.
*  And so I don't I don't think I'm particularly good at this, but I've at least observed some of those lessons and they've helped with a lot of these projects.
*  And so we have tools that are.
*  Relatively flexible and straightforward for doing a bunch of stuff.
*  And, you know, again, the benefit is that you then can do some fun things that make it easy to scientifically promote these these repositories.
*  So you can do a bunch of visualizations that are fun to play with these interactives that we have on our websites.
*  And then you can do kind of big mega analysis, glomming all the data together and looking at what comes out across countries or across languages or across socio demographic groups.
*  And those are very intuitive and appealing.
*  The analysis that I show people to demonstrate one of our repositories is just about.
*  The female advantage in early word learning.
*  And I don't know how theoretically significant it is from the perspective of understanding the universals of language acquisition, but it totally resonates with anybody who's had a kid or been in a preschool classroom and they see the girls talking up a storm.
*  And it turns out the world around there is a substantial female advantage for toddlers learning language.
*  And I think that's pretty cool and fun.
*  Well, that's kind of the other direction I was going to go instead of the tombstone was to ask about how your approach has changed, because I mean, you've developed the RSA model, which I'm sure we'll talk about, which is a theory.
*  But now we have this big data world and you can do things like visualize just based on different slices of demographics, et cetera.
*  And are you am I right that you're like kind of playing with that data now and taking a more bottom up or data driven approach to develop theories?
*  Or are you using a theoretical approach and playing with the data and meeting in the middle?
*  What's your overview there?
*  Your worldview?
*  Yeah, there's there's a fundamental tension here, which I'm well aware of.
*  And sometimes you look at an individual piece of work and it's like, hey, you're just looking at the data.
*  And then there's another time you look at a different individual piece of work and people are like, this is a terribly simple, simplified, boiled down, tiny little model of like people talking about squares and circles.
*  Why don't you look at the data?
*  I'm like, well, you can't do both at once.
*  So maybe you can, but it takes a lot of work and a lot of development.
*  So there's this beautiful paper by Brown and Hanlon from 1970.
*  This is Roger Brown, one of the founders of the field of language development, who's at Harvard for many years.
*  He had lots of wonderful students and he was always known as just this amazing writer.
*  And it's a paper about whether parents correct kids.
*  It's kind of a classic paper in a small niche of child language development.
*  But at the end, he just starts opining.
*  He starts just talking about stuff.
*  And he says, I think it's the last paragraph.
*  He's like, at this point, I want to express the distaste that experimentalists will have for this fundamentally observational work that I just did here.
*  They're going to think it's totally uncontrolled and doesn't show anything about causality.
*  But I challenge them to model also the distaste that the observationalist is going to have at their little tightly controlled experiment.
*  And really only by putting these two together is the truth going to emerge.
*  And I feel that very strongly.
*  I mean, this tension is just completely evident in my research life because my main teaching contribution at Stanford is to teach an experimental methods course where I hammer home these issues about causal inference and tight experimental control and construct validity.
*  And my current book project is this textbook on experimental methods.
*  And yet I continually find myself developing these large data projects which are completely observational, have no control over causality and so forth.
*  So I really think you have to play both sides of this methodological continuum and try to connect between them.
*  And of course, the connective tissue here is theory, is computational theory.
*  And so if you have big data sets and good experiments, you can try to bridge between those using a well-articulated computational theory.
*  And that's, of course, the end goal for me.
*  But it takes time to get there.
*  Well, a lot of the data that you work with is like survey data from parents making judgments or maybe judgments is too harsh.
*  Observing their own children and estimating when they how many words they learn in a week, things like that.
*  But then you also have some like recorded data, right, which is like transcribed, which is people in their homes and how much children, parents are talking to their children.
*  So it's a lot of like speech data.
*  So the quality of that data, I guess, is always in question somewhat as well, perhaps.
*  That's not my real question, but it was just a quick question.
*  Yeah, the quality of any data about an internal construct should be in question.
*  These are all measures of internal constructs.
*  And so we always have to ask about the reliability and validity of those.
*  And my whole stick for these repositories is that they're domain specific data repositories.
*  They're about individual constructs that people care about.
*  And the kind of basic theory for language development, you know, the one before the kind of pre theoretic theory is like, hey, kids have to hear some stuff in their house.
*  They have to process it. And then they have to have some outcomes.
*  I have to show learning in some way.
*  And so what we do is try to create repositories and data sets around those constructs.
*  And each of them is going to have their weaknesses.
*  So, for example, if we're interested in kids' outcomes, we can and do archive their eye tracking data from in lab experiments.
*  Turns out those eye tracking data, which are direct assessment, are extremely noisy because kids are very noisy.
*  They're, you know, well, they're literally noisy.
*  Their data are noisy as well.
*  They come into the lab and they do a couple of trials and they fuss out and they look at the thing that's more interesting rather than the language matching thing and so forth.
*  So you don't get that much data from direct assessment.
*  So, OK, let's go to parent report.
*  Now, you get a lot more data by asking parents about the kid, but you've got a bunch of biases creeping in.
*  You've got a bunch of worries about the parents not remembering right or being biased because of certain things they think about their kid or about particular kinds of words.
*  So, OK, you go to transcript data and you've got yet another set of issues.
*  So you really have to triangulate across these measures because no individual measure is really revealing the construct.
*  OK, I mean, the reason why I asked is because it's so studying an animal model of something, whether you're doing it observationally or experimentally in tightly controlled experiments or something.
*  You. Well, let me back up.
*  So it's so my thought was like this is a very hard thing to study language acquisition because, A, you're dealing with humans and not nonhuman animals, you know, B, because.
*  Of all those factors that you just listed, however, it seems like you could get and do, I guess, get massive, massive data from it or have the potential to.
*  I mean, you could. I guess you'd have to.
*  Well, you of course know this much better than I like how you would do this, but you could surveil on any given family as long as their privacy was protected.
*  Right. And if 10 percent of all families did that for a year, you'd have way more data than you wanted, probably.
*  OK, just just tacit agreement there.
*  OK, so OK, all this leads me up to the question of.
*  It's an unfair question that having read a bunch of your work and just how many open questions there are.
*  But the big broad question was is like roughly where we are in understanding how humans acquire language.
*  And if that's too big of a question, we could I could reframe it and say like what maybe has been surprising in the past handful of years that has come out of recent research based on these new data.
*  Well, let's let me see if I can take a shot at the bigger question.
*  Do it. Yeah. All right. How far are we?
*  I mean, I'm like, let's start with something that I don't know as much about, which is the eventual visual stream.
*  I'm an outsider to this research, but I just love seeing it.
*  It seems like we've just learned so much in the past 25 years since I first started taking classes as an undergrad.
*  Our understanding of the pathways that get you from basic visual input to a variety of different categories and their recognition,
*  that understanding has just been enhanced so much by the science of the past 25 years.
*  So we've got the human neuroimaging literature, we've got the single unit literature, we've even got some controlled rearing experiments.
*  Then we've got this whole host of new deep learning models that provide pretty good models of general responses across the cortex.
*  There's just there's just this wealth of exciting stuff happening where it feels like from a computational theory perspective,
*  we kind of understand a bit about why it might be organized this way.
*  And then from an actual neuroscience perspective, we see the the organization being measured.
*  And so that's just I think that's just tremendously exciting.
*  Then the question is, what do you do when you've got a case where you can't use the monkey models?
*  Your neuroscience tools don't work very well for the population. That's critical.
*  I mean, new methods are starting to come online and people are starting to figure out how to get awake behaving FMRI recordings with kids.
*  But it's it's really rough.
*  So how do you get the level of precision?
*  How do you get the level of convergence that we would want?
*  So it seems to me that you can't just do the same experiments and just like come up with another clever experimental design.
*  I mean, no question that people make progress and they come up with really clever designs and they do get incremental answers there.
*  But it seems to me that what we need is a bit more in the way of this multi-method synthesis where we come up with framework theories.
*  And people have been doing that since really the very earliest days of some of the neural network models and even before trying to think about what is a feed forward model of the ventral stream look like?
*  How can we, you know, reason about the relation between that and a bunch of different modalities worth of data?
*  So you need a model and then you need to be able to connect between different data sets that have different strengths and weaknesses,
*  including some more naturalistic free form data, right?
*  That's kind of inspirational work on the statistics of natural images and so forth, and including controlled experiments that test individual bits of the proposed theory.
*  So anyway, that's in terms of scientific strategy.
*  So how far along are we with language development?
*  Well, you know, we've got some kind of basic ideas about key principles.
*  But, you know, putting those things together into models that actually learn from data and tell us what things are mattering for the acquisition of kind of a fragment of language,
*  I think we're really a little bit low on synthetic theory there.
*  You know, there are some, I think, quite promising proposals.
*  So I like a lot of the learning accounts that are based in kind of learning individual words and then generalizing constructions from those.
*  Those feel sort of fundamentally right and maybe more so as we look at the progress of language models and we can get to that later.
*  But getting unifying models that connect between that kind of acquisition and a range of empirical phenomena that people have documented has been very hard.
*  We're not there yet.
*  So are there have there been thinking back to the old days of just theorizing without actually quantifying anything, having empirical work?
*  I mean, I guess there are observational studies, but it used to be philosophers would just think about it and make a claim.
*  Right. And then I'm not discounting any of the computational work that's gone on since then.
*  But but have there been surprising new ideas and or results about how we acquire language?
*  Just because there are so many different facets. Right.
*  So there's the developmental facet of when we start acquiring language and how we start acquiring it, how much of it is social, how much are we just absorbing, how much of it is active.
*  So has that story changed?
*  Has the broad I don't know. I don't even know what the story was.
*  And so I don't I don't know how it would have changed over time.
*  Well, I think I should differentiate here between the acquisition of vocabulary, which people have said certain things about.
*  And then when you say vocabulary, sometimes you're saying in the kind of narrow sense of like, hey, did you learn the word for dog?
*  And sometimes people talk about in the broad sense, like when you learn the word justice, are you actually learning something about the concept, the way the world is organized?
*  So there's there's both narrow and broad there.
*  And then the place where a lot of the theoretical action has been is actually in discussing theories of grammar and the mechanisms of word combination and syntactic structure and so forth.
*  So in both of those places, I think there's been real progress.
*  If you go back to kind of first principles, we're talking kind of nativism and empiricism.
*  And those are the kinds of philosophical positions that people articulated without looking at kids or looking at data or doing experiments.
*  So from the empiricist perspective, I think there are some real challenges to the pure associative story about about early word learning and about early grammar learning.
*  And the most effective of those challenges, from my perspective, come from the social world.
*  So as we've understood more how deeply grounded kids are in social interaction with others and how much that motivates them, it's become clear that kids aren't just picking up word world associations.
*  They're learning how to use language to talk to other people and how to make their way through the world.
*  So from that perspective, I think that's a challenge to empiricism.
*  On the nativist perspective, there's been nativist theories where, OK, much of the kind of conceptual and syntactic structure of language is innate.
*  And really what we just need to do is plug in a bunch of kind of individual word forms or something and maybe learn a couple of things from the environment.
*  And then all of that structure is going to come online and tell us what to do.
*  And obviously, that's a caricature. But those kinds of views, I think, have been really challenged both by.
*  Learnability demonstrations that kids can and do learn from the statistical structure of the environment and also by proof of concept from a variety of computational models, clearly the most recent language models,
*  but also many before that showing that actually it is quite possible and sometimes even easy and sometimes even more effective to learn a particular task from the environment than to rely on a fragile set of rules.
*  So anyway, I think that their challenges is a long, very long answer to your question, but I think the challenges to both positions that you might have had as a a priori theorist and that occurred in the philosophical literature.
*  So really beyond, OK, nativist versus empiricist, I think we need to talk about what are the tools the child brings to language learning?
*  How are those grounded in different aspects of cognition, memory, generalization, but also social cognition, also conceptual and perceptual structures?
*  How do those come together? And that's a much richer and more fun story.
*  But all in this messy developmental stage as well, because everything is developing at the same time, like how it just seems impossible to parse all of these things out.
*  Well, yeah, that's why we're learning is such a fun case study is because we're funny.
*  You could have a well, because it's so central, right, because you can have cases where what's critical is the child's own active exploration,
*  what's or what's critical is the perceptual structure of the environment or what's critical is the pragmatics of the social interaction or the syntactic structure.
*  Like you've got all these different information sources or clues to meaning and the child can put them all together really, I think, very flexibly to to reason about language use in the moment.
*  And then word meaning going forward. So this kind of set of interactions is really what makes it fun, because word learning isn't modular.
*  It's the most fundamentally central part of what a kid is doing.
*  But you use the term flexible. Is that the most amazing thing is how flexible our learning is?
*  Like in a stage, in a very young stage where we're cognitively developing, also our language is developing, our social context is developing.
*  We're actually physically growing. You know, we're being embodied in the world in different ways, and that's constantly changing.
*  And is that is nothing critical or should we just be impressed with the flexibility or are there critical things?
*  Well, language learning is very robust against developmental variation.
*  Now, there are certainly cases of developmental disorders that lead to impairments in language.
*  There's no question of that. But across many, many different caregiving environments, across many different, for example, sensory disorders and across many different.
*  Aspects of cognitive diversity, you still see language emerge and its emergence can lead to some variation in timeline.
*  There's potentially variation in content and focus, but you see.
*  The ability to communicate using language and just a dizzying number of circumstances, and that's, I think, fundamentally amazing.
*  So there has to be some flexibility.
*  If somebody says, oh, social learning is literally the only way you can learn language, they say, OK, well, let's talk about cases where the social input is impaired or social motivation is impaired.
*  And you still see language emerge.
*  Somebody says, oh, it's about perceptual mappings where you talk about kind of cases where the sensory modality in question isn't present and the kids are still picking up something about the structure of language.
*  So there's a lot of robustness and flexibility in the system.
*  And if you think about.
*  I would use neural network terminology, but like a loss function that's about communication in some sense,
*  so expressing something to another person, then there's a lot of different ways that you can kind of optimize that loss.
*  There's a lot of different information sources that you can learn about and use, and there's a lot of different sensory.
*  Well, yes, there's just a let me say that a different way.
*  It's likely that if this loss function is really important, that the organism will use almost anything at its disposal information wise, cognitive resource wise to optimize it.
*  OK, yeah, OK. So does that mean what does that say about the relative importance of not importance, but.
*  How impressed should we be with language?
*  You know, we're always impressed with language because it's uniquely human and we're the best thing in the universe.
*  Is language all that all that and more?
*  I have to say, I'm pretty impressed.
*  I think that language is pretty incredible for its ability to allow us to coordinate complex plans with other people,
*  for our ability to its ability to allow us to externalize our thoughts and augment our cognition.
*  And its ability to allow us to structure our cognition around complex concepts that otherwise might not be comprehensible in our thinking.
*  We can tag things with new words and use those as abstractions and kind of reuse them in our mental simulation and in our reasoning.
*  We can structure complex propositions and reason about them internally or in external forms.
*  So I really do think it's amazing.
*  And one of the fundamental exciting things is that I think right, if you're optimizing this communicative loss.
*  On both an evolutionary and a developmental time scale, you actually get something that's not just good for coordinating in the moment,
*  but also actually has all these cognitive benefits in terms of structure, recognition, allowing externalization, allowing persistent plans over time and space and so forth.
*  OK, so I was going to ask you what the function of language is.
*  I know that you have said it's definitely for communication.
*  And I don't know if you're saying that with the background of the debate between whether it's for communication or for thought.
*  But I recently had Nick Enfield on and he's written a book called Nature versus Reality.
*  And his argument is that language is mostly for or the primary function of language is for socially coordinating around social problems,
*  which you just mentioned a few minutes ago.
*  But I guess I don't have to ask you what you think the function of language is.
*  But it just occurs to me, does there need to be a function of language or thinking about my children?
*  They just chatter chatter all day and I don't know what the hell their language is for.
*  I mean, it's like it's for them to practice language.
*  And before that, it was like to get things from me.
*  And I think a large part of language is getting things, getting what you want, which would would fit into that social coordination aspect.
*  But but now they're at a later stage where they're just yammering on all day.
*  You know, and so can language be for different things at different stages of your development?
*  I mean, is there how many functions of their of language are there?
*  Well, what can we say about the function or why not have lots of functions?
*  Yeah, this kind of question is really controversial in part because there's a lot of ambiguity when somebody asks the question, what is the function of language?
*  So. Philosophers have a lot to say about distinguishing different kinds of functions, but minimally we can say.
*  Is there a evolutionary advantage that's granted by a particular behavior set of behaviors that are enabled by language
*  that would lead to language ability being selected for over the past million years, say.
*  Speculating about these kinds of things is difficult.
*  It's hard to find really great evidence, but I think that's probably the root of Enfield's claim that social coordination might confer selective advantage.
*  And on the flip side of that, somebody like Chomsky has asserted that the role in representational thought might be the key grantor of selective advantage.
*  Personally, when you work out the evolutionary story around that, especially Chomsky at times has endorsed a saltatory evolutionary story
*  where there's sort of a small number of key changes evolutionarily that happened relatively recently, 50 to 100,000 years.
*  That story for me doesn't seem like it is as likely or as plausible based on some of the evidence out there, but I'm not a specialist in this.
*  So anyway, that's kind of evolutionary for that is what selective advantage does language confer?
*  But you could also think developmentally, what are the reasons that a child might want to talk?
*  And those are going to vary from child to child often social connectedness, getting what they want, as you mentioned and so forth, seem like motivations for some kids.
*  But for other kids, they seem like there are other expressive motivations.
*  They like to talk to themselves and so forth.
*  So these might be fairly diverse and variable.
*  I know they don't want to just understand what I have to say.
*  I'll leave it at that.
*  I don't know how your parenting experience has been.
*  Well, there's this insight from Michael Tomasello, which is that the fundamental thing that emerges in very early childhood and even infancy is this desire to share.
*  And you see that in many, many children.
*  I have these moments where before language, they started to want to share using that declarative pointing with your index finger.
*  And I just have these pictures of both kids being like this and share their experiences.
*  Yeah, yeah. They want to know that somebody else is seeing the same thing as them.
*  That triadic attention that Tomasello has written about.
*  And I just think that's totally right for a lot of kids that they are doing that kind of sharing.
*  And it appears to be a huge motivator of early language, because if you look at kids earliest vocabulary, we've done this across many languages in the Word Bank book.
*  What you see is that the earliest words are not typically these kind of basic needs words like change my diaper.
*  I need food of this type and so forth.
*  They feature a ton of people and people's names.
*  They like mom and dad and grandma and grandpa and sister, brother and so forth.
*  They feature interesting stuff in their environment and they feature social routines like hi, bye, peekaboo and so forth.
*  So kids try to talk in this, by and large, on average, in this very affiliative way that allows them to relate to the people around them, to share interesting stuff with people around them, as opposed to just meeting their basic needs.
*  So that feels kind of largely fundamental, although, as I said, there are cases of resilience where you don't see as much social motivation and you do see language emerge sometimes on a different time scale.
*  So it's not, you know, that's not. Absolutely necessary, but it is at least in most cases of typical development, a really strong functional driver.
*  So, you know, I mentioned that acquiring language is couched in this crazy, complicated development as well.
*  What is the relationship of understanding development itself, development of the organism to development or acquiring language?
*  I mean, is there do we need to understand development writ large to understand language acquisition or can we just understand language acquisition from a purely psychological perspective?
*  What I don't know that there's one thing that I'd call development writ large.
*  There are lots of different processes of growth and change.
*  Right.
*  And one way of defining this is that language, because it's so central in cognition, because it has all these connections to other aspects of conception and perception, to social interaction, to learning and memory,
*  we do need to get a sense of that connectedness and how it's changing over time.
*  Especially when you're looking at very early word learning, there are these pretty dramatic processes of growth and change that are happening, physical and psychological.
*  And so language does appear to be affected by them.
*  Just to take one example, this comes from work with head-mounted cameras.
*  And we've done a little bit of this work, but there are many pioneers of it, Linda Smith and Chen Yu and Karen Adolph and then others.
*  And when you look at kids around when they're learning their first word, they're also learning to walk.
*  And so their perspective on the world is changing radically.
*  And so what they have access to in terms of what they can see and then also what they can do.
*  Both of those things are changing, so they're starting to pick stuff up and take it over to people and ask about it.
*  They're seeing a lot more of the social world around them just because they're a higher up and look up at their parents as opposed to looking down at the carpet when
*  they're crawling. So yeah, there's a lot of changes there.
*  And that's a place where I think you see pretty strong coupling between the physical changes and the psychological changes.
*  Later on, I think you see those things decouple a little bit.
*  And we've done some kind of large scale research with milestone data showing that early on,
*  language and motor milestones around babbling and around kind of gross motor stuff and even first words seem more correlated.
*  And then they kind of by the end of the second year, certainly, they're kind of decoupled and a kid will make motor progress,
*  but not language progress in a particular month or two of development.
*  So that's all to say that that's just one example of that developmental connectedness and the need to understand a particular piece of development at the critical time.
*  At other times, maybe the critical pieces are around social cognition or around conceptual understanding.
*  So, yeah, there's absolutely these other correlated developmental trends that you really have to think about as you're thinking about what's going on in the context of language learning.
*  Refresh my memory on what the end story was about regarding the dimensionality of development, developmental behavior with respect to language.
*  The idea is that either language processes in stages with your cognitive functions or everything's going in parallel.
*  And I think that you concluded that everything's going in parallel, that we have all these ability cognitive functions integrating with our language and we're acquiring language using these other faculties all in parallel.
*  Is that right?
*  Yeah, this is, I think, actually a cool case where there has been a convergence across different ways of understanding language and language learning.
*  So if you look at a standard linguistics department, you've got your phonology and phonetics, you've got your morphology, lexicon, syntax, semantics, pragmatics.
*  There's this hierarchical ordering of abstractions.
*  And those are the classes you take.
*  And for a long time, people studied individual aspects of acquisition and individual aspects of language representation kind of around that same stratified hierarchy.
*  And I think now that it's pretty clear from a couple of different sources of evidence that that is not how human beings represent language.
*  We don't represent these individual modular components.
*  So on the acquisition end, if you look at variation across individuals, all of these different constructs hang together variationally.
*  So a kid who's good at gesturing and gestures early tends to have a larger vocabulary, they tend to have a larger vocabulary.
*  They tend to be combining words more, they tend to have more word meanings, so forth.
*  So the language system in development is what we call tightly woven.
*  The correlations between these things are very, very high relative to almost any within participant correlation you might see with kids.
*  Then if you look at the neuroscience evidence, and this is worked by folks like Ed Fedorenko,
*  you see that there aren't differentiation between, say, syntax and semantics in the brain.
*  There's no place in the brain that does syntax, but not semantics.
*  And so that really breaks down some of the modularity that's been supposed between those two different ways of looking at language meaning versus the rules of composition.
*  And then finally, from large language models, we see that the models that do best are the ones that learn more or less everything at once.
*  So you feed in a lot of language and they get better at combining words grammatically.
*  They also appear to get better at reasoning tasks, whether that reflects true reasoning.
*  They certainly are gaining some abstractions intermediate to some kinds of predictive reasoning tasks.
*  So earlier efforts that aimed to do something like syntactic parsing without meaning really didn't work that well.
*  And the parses that came out were OK for downstream tasks, but certainly nowhere near the level that a holistically trained model now achieves.
*  So, OK, again, long answer, but you've got data from acquisition, data from the cognitive neuroscience and data from the computational modeling, natural language processing.
*  That all for me converge on saying, hey, this stuff is happening together.
*  It works better when it's together, it's represented in the brain together and it varies together in acquisition.
*  It does not look like these things come apart and are learned sequentially in series.
*  They're happening in parallel in a combined way.
*  Since you mentioned large language models, let's bring them into the conversation, I suppose.
*  Yeah, they're learning everything at once.
*  And I should preface this by saying, like everything that we've been talking about, it's not like, you know, six half year olds, one and a half year olds.
*  They're not learning written language.
*  They're not learning getting vector inputs.
*  They're learning auditory speech.
*  And I don't know how much of a difference that would make in a large language model.
*  But children learn language in a vastly, vastly different way than a large language model, correct?
*  Sure. Yeah, I'm on board with that.
*  Does it matter?
*  Of course. Yeah, it absolutely matters.
*  So what we're seeing with the most massive language models is really something like a proof of concept around certain aspects of learnability.
*  And that can really inform the conversation.
*  But they're not learning from the same data or even the same sensory information sources.
*  And the kinds of data that they're being exposed to are different.
*  Obviously, the architectures are vastly different and the scale of the data is vastly different.
*  So it's worth noting that there's a really big language acquisition literature that made very strong learnability claims under a range of different learning paradigms.
*  They didn't say, hey, it would take a couple billion words to learn syntax.
*  They said syntax is not learnable.
*  And people were saying this in all sorts of major and legitimate high profile ways within the last 20 years.
*  There's a kind of influential series of papers from Parthen Yogi and Martin Nowak and so forth that promoted a bunch of these learnability results,
*  some of them dating back to the 60s, that said syntactic structures are not learnable under certain conditions.
*  And there was a lot of debate about what those conditions were.
*  But now I think everybody agrees that the syntax coming out of large language models is pretty much perfect.
*  And so from the perspective of like a proof of concept that bare string acquisition of language from syntax is possible.
*  Yeah, yeah, we're there.
*  OK, now everybody can backtrack and be like, well, we meant we meant within a couple hundred million words or something.
*  Is that what's happening?
*  Yeah, certainly on Twitter.
*  Nobody was, it's not fair.
*  Some people were very precise about the conditions of acquisition.
*  So in the original Gold's theorem that is cited very widely here, there's a particular adversarial learning context for learning a context free grammar.
*  And the adversarial learning context is I can guarantee that you cannot learn a context free grammar if I hold back key exemplars for an infinite amount of time.
*  I can always hold back key rules and then surprise you with them adversarially and then you will not learn.
*  And that's totally reasonable.
*  So those are precise results that have very limited scope in some sense, because that adversarial learning context is obviously wrong.
*  And then there was a lot of general kind of opining on the subject of learnability, which was not as precise and didn't give clear conditions or amounts of data or constraints on the learning regime.
*  So great. Now we're getting a little more precise.
*  OK, does anybody want to make a learning claim on 100 million words?
*  OK, well, that's starting to be about more of the right scope of data.
*  I'm not sure that anybody is about to draw that line in the sand, given how fast things are moving right now.
*  But yeah, what we can conclude from from learning from 100 million words is probably very different than, you know, three point six trillion in the latest three point six trillion tokens.
*  So more than two trillion words in the latest Google model.
*  Yeah, it is a proof of concept.
*  Yeah, have you learned anything from the way that large language models function and acquire language?
*  I'm not going to say so efficiently, because that's a huge difference between humans and large and models is efficiency.
*  But have you have you has it changed your mind in any way about how children learn and acquire language?
*  Oh, yeah, I think it's an incredibly exciting time.
*  You know, are we. At the full understanding we need of what is happening in transformer models.
*  That are learning from input prediction, no, we don't we don't know, but that's why it's exciting.
*  So. In my kind of formative cognitive science years, I was reading the rules versus statistics debate.
*  I was deeply inspired by stuff like Jen Safran's statistical learning papers with the gasoline and Alyssa Newport,
*  where they were showing again proof of concept that kids could learn from data and then was really affected by this debate between them and Gary Marcus and others on whether particular phenomena could only be captured with symbolic rules and so forth.
*  So the emergence of reasoning related behaviors, just using the kind of most vanilla way of describing it in these large language models,
*  I think is very exciting and suggests that networks without inbuilt symbolic structures can learn to do very highly abstract tasks.
*  And that's really cool. And some of the work that I've done in collaboration with folks like Atticus Geiger and Chris Potts has probed that more deeply and convinced me that.
*  Many people were wrong about the necessity of inbuilt symbolic representations.
*  And so I learned something fundamentally, my mind was changed.
*  I thought there was a good mic of, let's say 2010 when I published a paper on rule learning,
*  I thought that there was probably an inbuilt operator for equality or sameness.
*  At least I couldn't figure out a way to make the model work without one.
*  And, you know, like of 2022, I was at least convinced by the collaborators on the project that you could learn such an operator.
*  And in fact, it would even be causally identical to some tolerance to the symbolic operator.
*  And that that operator could be learned from data in both supervised and unsupervised regimes in a kind of flexible way with the potential for connection to human data.
*  So that really changed my mind. And I think folks who are still kind of saying, oh, but the symbols haven't engaged deeply with the new literature on these models and how they can learn abstractions from data.
*  And that's just so exciting. What a great moment to be in.
*  Would you describe the like learning of symbolic utility as like an emergent property of the large language of the large models?
*  Yeah, yeah, it's clear that there's some abstractions that are being learned and we don't know.
*  I certainly don't know, but I think nobody knows exactly what the granularity of the abstractions are in the largest models,
*  because for one thing, they're commercial artifacts that we can't probe and mess with in the ways that we want to.
*  But even in smaller artifacts, we're just gradually getting the tool set necessary to understand what kinds of things they're representing.
*  But it's clear they're representing something.
*  We'll get to your child with a hat and glasses task in a moment.
*  Well, I'll know. I'll just ask you now. So one of your favorite tasks.
*  And this has to do with pragmatic inference.
*  So what I was going to ask you about is do large language models pragmatically infer.
*  And maybe if you could describe what I'll just ask you that first, if you could describe what pragmatic inference is beforehand,
*  and then I'll ask you on your thoughts like so, you know, the larger question is like,
*  what are large language models missing and are they missing pragmatic inference?
*  Yeah, it's a great question. So pragmatics is broadly speaking, all the stuff about language that's not the literal meaning,
*  it's about the contextual inferences about meaning.
*  So any time you're going beyond the literal meaning of an utterance to infer some kind of extra communicated meaning,
*  you're doing a pragmatic inference.
*  Classic example is something like a classic and I should say also controversial and highly debated example is something like a scalar implicature.
*  So if I say some of the students passed the test, you might infer that some of them didn't.
*  But it's logically consistent. I could say some of the students passed the test.
*  In fact, all of them did. Yeah.
*  Or the you know, the other classic that is not as highly debated, it's kind of clearly pragmatic is when I write the letter of recommendation and I say,
*  you know, dear sir, please accept my student, he has fantastic penmanship and often shows up on time.
*  You infer there's nothing else good that I could have said about the poor guy.
*  These are from Grice. Yeah.
*  Oh, Grice. Yeah, you cite Grice a lot. Would this with the Mitch Hedberg joke work?
*  I used to do drugs. I still do, but I used to, too.
*  So that's why it's funny is because we pragmatically infer that it no longer does.
*  Is that would that count? Oh, absolutely.
*  I love Mitch Hedberg is like the perfect comedian for this kind of stuff because he's got these one liners that are all about assuming you have an alternative in mind.
*  That you might not have had in mind, so I'm going to mangle it, but my favorite Mitch Hedberg was like they should have a sign that says.
*  Escalator now stairs. Thanks for the convenience escalators cannot break.
*  Yeah, yeah, right. I wasn't thinking about that alternative, but now you pointed it out to me.
*  I'm reasoning about it. It's like, oh, yeah, OK. Anyway, so, yes.
*  So pragmatics is all of that going beyond the literal meaning to the communicated meaning.
*  And. There's. You know, there's been a lot of discussion about the extent to which various different model classes start to do that.
*  I remember it just like a funny story. I was at a conference at Google, I don't know, in like 2011 or 2012, something like this.
*  And I was really deep in this pragmatic stuff at the time, and I gave this talk about pragmatic inference, and I was talking to Peter Norvig afterwards.
*  And I was saying, oh, doesn't you know, doesn't Google need to do pragmatics?
*  I think you're just considering other alternatives, and I think we do that.
*  I can't really tell you about the details, but I'm pretty sure we do that.
*  And I was like, oh, yeah, that makes sense. You are a search company considering like which searches go with which targets.
*  So kind of key principle of pragmatics is like what could somebody have said if they had wanted a particular thing?
*  What are other things they could have said and what goals would have been consistent with that?
*  And so in some sense, a lot of different technologies, something as simple as TF-IDF information retrieval and many different search algorithms and so forth, will follow some of those basic principles.
*  And then the question is, like, are they effectively doing that in communicative contexts in the way you would want?
*  And, you know, large language models do get some pragmatic tasks, especially the bigger ones.
*  So there are folks who have been doing the probing game and trying to figure out to what extent they can pass some of these tasks.
*  And they do actually do a few of them fairly well.
*  I don't think they're great, perfect conversational partners, but some of the dialogue training and stuff that folks have done on top of the chat agents actually does encourage a lot of.
*  What seems like inference about the motivations or goals or intentions of the dialogue partner, the human dialogue partner.
*  And that's actually fundamental to pragmatics.
*  So I don't think I used to think again, this is a place where I was wrong.
*  I used to think you had to build in the pragmatics thing to these models.
*  And then when context conditional agents like GPT-3 came along, I was like, oh, actually, they're kind of doing pragmatics in some sense.
*  Maybe it's not the perfect sense, but it's kind of baked in and it's kind of emerging.
*  And that's pretty exciting.
*  I mean, does that tell us more about the impressiveness of the models or that pragmatics is a less difficult problem to solve?
*  I think it maybe tells us that pragmatics might emerge actually as Grice hypothesized from more general.
*  Processes of. Well, he would he would have said kind of collaborative action, maybe.
*  You know, so he was thinking of talking as a form of rational behavior where somebody has a goal and is trying to accomplish it with language.
*  And so when models are trained to complete that goal or to help you achieve that goal in dialogue,
*  maybe there that's a fundamentally Gricean kind of training to train on dialogue and kind of inferring the goals of rational action.
*  And so then when pragmatics falls out, maybe what that tells you is actually that you didn't need it's not that pragmatics is not impressive,
*  but it's that you didn't need specific pragmatic machinery.
*  What you needed is general abstractions related to goals and action and communication or maybe just a huge pile of data about those things.
*  Yeah, well, let's take a side street to rational speech that speech act, because since you mentioned Grice a few times,
*  is that where is that what inspired the Rational Speech Act, the Gricean approach?
*  So it's all about it. It's sort of, you know, it can specifically address pragmatic inference, right?
*  Because it's all about the probability of someone's intended meaning based on your own understanding and your understanding of their understanding.
*  And then you can like recursively what they are not meaning to say.
*  What is the prior over possible meanings of what they're saying?
*  So that is that recursive process? Is that kind of out of Gricean and Bayesian approaches or?
*  Yeah, exactly. You know, we were trying and this was with my collaborator, Noah Goodman.
*  We were trying to figure out what it might mean to infer somebody's intention in context.
*  What are they trying to talk about in context?
*  This actually came out of earlier work where we were collaborating on a model of word learning.
*  And we stuck in this node called the speaker's intended reference.
*  What is the thing they're talking about?
*  And that actually happened to play a big role in the success of our model, because, you know, kind of classic associative models of word learning thought that kind of everything was being talked about a little bit all the time.
*  That's how the associations are formed. Everything's kind of connected a little bit to everything.
*  But that's not true in a social perspective.
*  Actually, people are only talking about one thing at a time or maybe two or maybe none.
*  But there is a particular thing they're typically talking about.
*  So we put in this node called intention and we instantiated in a pretty stripped down, not very social way in that model.
*  And then we started talking about it like, could we flesh this thing out?
*  Could we make it a little bit more interesting in the next version of the model?
*  And of course, that then spawned this whole research program on Rational Speech Act Models, where we lost track of the connection to word learning for maybe about six or eight or ten years.
*  And just we're trying to figure out what it might mean to infer the intention and context based on the language that was used.
*  And so what we fundamentally did was just try to write down Grice's idea about intentional inference in a Bayesian framework.
*  So the listeners thinking, what was the speaker's goal, given that they said this utterance?
*  And then the speakers thinking, how would I get the listener to figure out my goal?
*  Which utterance should I choose?
*  And of course, that's a recursive formulation.
*  The listener speaking about thinking about speaker, speakers thinking about listener.
*  And for us, we then tried to ground that out in what we call the literal listener, which is a listener that is a kind of a notional agent that just reasons about the meanings of words that doesn't think pragmatically.
*  So listener thinks about speaker who's thinking about a kind of dumber listener.
*  And so the regress is an infinite.
*  It kind of grounds out after a couple of levels.
*  Meaning that the dumber listener knows that there that there are only two meanings of the word bat and considers them with some probability each or something.
*  Exactly. Yeah. So if you take this hat and glasses example, this is one of our fun ones that we use in a lot of different studies with kids.
*  There's a face with a hat and a face with a hat and glasses.
*  And you say my friend has glasses.
*  That means have glasses and not a hat.
*  And so that's the that's the most chosen answer, right?
*  That people choose is it's not the person with glasses and a hat.
*  It's the person just with glasses.
*  If you say my friend has glasses, even though they both have glasses.
*  Sorry, I just wanted to spell it out.
*  Yeah, thanks. Thanks. Thanks for making the example explicit.
*  And what we find is that adults will choose the one with just glasses and not a hat, maybe 75 percent or 80 percent of the time.
*  And actually, so will three year olds.
*  And in some studies, even two year olds or older two year olds will be able to do this kind of very simple pragmatics, suggesting that this is really something that is not too hard developmentally, even though this is kind of an unfamiliar new inference.
*  At least in a new context, kids are still able to get this.
*  So. In that kind of example, what RSA says is the listener hears glasses and thinks about glasses with respect to the two potential speaker goals, which of the two faces we're talking about and thinks, oh, well, if the speaker had meant.
*  Hat, I think I had the hat on glasses, they would have said hat and that would have been perfect, but they didn't have access to that if it was just the guy with only glasses.
*  And so they could say glasses now in the real world.
*  They could also say only glasses or the guy on the left or so forth and so on.
*  There's lots of different possible utterances.
*  And so in those early experiments, what we did is really constrain the world and constrain the set of things that a speaker could say and constrain the listeners interpretations and so forth to try to get a very simple reference game that we could make quantitative predictions about.
*  Do LLMs answer that correctly?
*  Have you tested it?
*  You have to input an image, right?
*  Assuming I don't have, I can't keep up with like all the different models and what they what you can input and stuff.
*  So apologies that I don't already know.
*  No, no worries.
*  Yeah, I don't know that anybody has done a multimodal version of this.
*  OK, there are some evaluations on kind of some simple implicate your tasks.
*  And I do think that the more sophisticated models do OK at them.
*  I don't know if anybody's done that exact one.
*  I don't have to look.
*  But yeah, in general, they.
*  I'm not totally up on this, but there have been some some notable successes lately.
*  What's your guess on, you know, so would it easily pass?
*  Yeah, I mean, I think this is not a hard task.
*  And, you know.
*  Yeah, I would be surprised if GPT-4 were not able to do this task.
*  What would you have said four years ago?
*  Three years ago?
*  GPT-3 already made me think that there were a bunch of possibilities for pragmatic
*  inference baked in.
*  So as soon as we started to see, like kind of really task conditional behaviors in
*  prompting that I remember, you know, walking the dish at Stanford with Noah and him
*  saying, you know, it's just all baked in there.
*  Like, try these things.
*  And we played with them.
*  There was a, you know, early demo copy.
*  Oh, yeah, OK.
*  So I think that's a good point.
*  Yeah, because task inference, like the thing that you're doing when you're trying to
*  complete a prompt, that's really very pragmatic.
*  You're like, what does this person want?
*  What are they trying to communicate to me about the task, the underlying task and the
*  kinds of completions they want?
*  So the same abstractions that a model has to learn to do that task well.
*  About goals.
*  And I think that's a really good point.
*  I think that's a really good point.
*  So from the prompts that we see to a kind of abstract set of goals that the user has,
*  that's very much a pragmatic inference, that reverse inference about goals.
*  And so I think, you know, I would have said no and like, yeah, 2018, 2019, probably.
*  And then after that, uncertainty started to go up until it's pretty much at yes.
*  So I think that's a really good point.
*  I think a lot of these, a lot of people, what's the term?
*  Like everything is AI until it becomes solved and then it's not AI anymore.
*  There's some term for it.
*  Like it's a moving goalpost anyway.
*  It's a paradox.
*  But do you think that there's a lot of like people saying, well, it can't do this.
*  So it's no good.
*  And then they build a bigger model and it can do it.
*  And so I think that's a really good point.
*  Well, we have to have some kind of benchmarks and understanding of what capacities we care about.
*  And I'm not so much into the line drawing.
*  You know, there's this old idea of the Rubicon, right?
*  Like, and you know, it's like, you know, it's like, you know, it's like, you know,
*  it's like, you know, it's like, you know, it's like, you know, it's like, you know,
*  right?
*  There's like 19th century philologists saying like, you know, language is the Rubicon between
*  man and beast or something.
*  And I think that that's not a great game to play.
*  Like we've seen that play out in the comparative literature where, you know, somebody says,
*  okay, like, you know, language is that boundary.
*  And then you get a dog that knows a hundred words and like, well, okay, but a hundred words
*  doesn't count.
*  Like somebody trains their dog to do a thousand words.
*  And then does that count?
*  Like, well, okay, there are a lot of self-respecting three-year-olds that maybe are only around
*  that level.
*  So I think it's very tricky to draw the lines, but it's very useful to have some kinds of
*  benchmarks, tasks and tests that you think really do reliably provide evidence of a
*  particular capacity.
*  And so triangulating that, you know, what sorts of representations a model appears to
*  have access to is really very interesting.
*  That's why I always draw my lines in sand at low tide near the water, you know, and
*  it's just really easy to start over.
*  I brought us away from the Rational Speech Act model.
*  And I want to come back to it because I want to try to think about how to think about that
*  model with respect to large language models, because RSA is like a normative model of how
*  we might implement these things.
*  And it's a theory driven model.
*  Whereas a large language model is this kind of associative connectionist, somewhat theory
*  free, although you could say that there's theory in the architecture, et cetera, but
*  almost brute force driven.
*  How do you think about something like the RSA model that you continue to work on versus
*  these large language models?
*  Well, so maybe one way to start is to think about what the goal of a model is in a
*  in a science.
*  And there's lots of very interesting philosophy of science about this.
*  But you might think about like a cognitive model as an artifact that you put in some
*  relation to a target system.
*  And then you reason about the relationship between the artifact and the target system,
*  in part by kind of encoding assumptions about the target system in the design of the artifact.
*  And in part by then having access to a set of strategies that you could probe the behavior
*  of the artifact and look at how that might reflect on certain aspects of its performance.
*  So then you could think, OK, is a large language model a useful scientific model?
*  Well, GPT-4 isn't because we can't poke it in a lot of the ways we want to.
*  We don't know what went into it.
*  We don't know its architecture.
*  So there's a lot of basic guarantees that are not being met by some commercially available
*  large language models.
*  So, OK, how about alpaca or llama or whatever?
*  This is getting closer.
*  We could start to think about using that as a cognitive model for some tasks.
*  And that's, I think, pretty cool and interesting.
*  And we gain access to certain kinds of evaluations that we wouldn't have otherwise by the sheer
*  capacities of the models, which is cool.
*  Right.
*  So they're useful for some things.
*  But we also really don't understand fundamentally a lot of things about the training data, about
*  the representations and so forth.
*  So a model like RSA is probably the extreme end of the simple cognitive model side.
*  Right.
*  This is written down in a couple of equations.
*  Early versions we played with really mostly on paper and pencil.
*  We coded them up in different ways.
*  Eventually, it became important to code them up in larger and more data connectable ways.
*  But that was a lot of the fun of that development process for me, is that you could kind of
*  math out what should happen in particular situations.
*  And so there's a huge amount of transparency about the assumptions and lots of ability
*  to extend and modify and compose with other kinds of reasoning models or other sources
*  of information or other reasoning tasks.
*  So there's a lot of flexibility in the kinds of relations you can learn between that teeny
*  tiny artifact and the cognitive system of interest.
*  So lots of benefits there, in other words.
*  But there are also real major costs because the models aren't that capable.
*  You have to constrict the language and the world and then code them in very specific
*  ways in order to get anything out.
*  So I guess I see them both as different cognitive modeling strategies with the scale being
*  a key variable that controls what you can do.
*  Last thought on this is that one reason that RSA has been useful is in part because of this
*  small scale, which has allowed it to be adopted by many groups that are working on this
*  phenomena.
*  And some of those groups really do the thing that I was talking about paper and pencil
*  wise.
*  And others connect it to larger reasoning issues or even to NLP systems and incorporate
*  those insights.
*  So that kind of simple modularity has been, to the extent that RSA has been successful,
*  that's been part of the success.
*  We'll see in LLMs, it's more the power of the general framework that makes it intuitively
*  appealing to try to use them as cognitive models.
*  But as we're seeing, there's a lot of real scientific challenges that come with it around
*  reproducibility, replicability, around just the scale of resources necessary for training
*  from scratch, which is critical.
*  And even around what are the right probes to better understand what's going on with
*  the models because that's not totally clear yet.
*  So you were on a recent review.
*  You had mentioned the ventral visual stream and how far we've come understanding that.
*  And convolutional neural networks have been a large part of that.
*  And you're on a recent review from the Dan Yehman's group, I believe, and PNAS asked
*  about that.
*  I believe you're on it.
*  Am I right?
*  Yeah.
*  And so you mentioned Ed Fadarenko.
*  She's also been on the podcast.
*  And we talked about her results and others that have correlated the predictive aspect
*  of large language models to the predictive next word prediction of our brains.
*  And that's a predictive aspect.
*  First of all, because I want to ask you about prediction as an explanatory goal of science.
*  But what do you think of that work then?
*  As we were comparing RSA to these large language models and we don't have access and
*  everything that you said about the large language models, what do you think of that
*  avenue of research that is parallel to the ventral visual stream and convolutional neural
*  networks versus our language area, language brain regions and EEG data and stuff is to
*  large language models?
*  Yeah.
*  So first I should just say about this piece of work that you mentioned, this is Cheng Shu
*  Chuang.
*  And he was really interested in unsupervised models of visual learning.
*  I was involved there because I was helping them work with and think about the developmental
*  data they use in that paper, the SACAM corpus.
*  This is a corpus of head mounted videos that we collected from young children.
*  So the upshot of that paper is that you can get some pretty good neural productivity from
*  unsupervised visual learning models.
*  And for me, a real strength of the paper, irrespective of anything that I might have
*  contributed there, I certainly didn't contribute to this, it was the systematicity with which
*  Cheng Shu had gone through this literature.
*  So it's not just, oh, my model wins at neural prediction, but rather unsupervised models
*  that learn in a variety of different related but distinct ways through prediction and recoloring
*  and infilling and so forth, all seem to relate to brain data in really interesting ways.
*  So there's something about this kind of general task.
*  So as a scientific strategy, then it was to understand commonalities and differences
*  between models and use that as a basis for inference.
*  And I think that that's very exciting.
*  So prediction is one, brain prediction is one way to evaluate models.
*  And if you can then look at differences or similarities in prediction accuracy to brain
*  data, or for that matter, to behavior data, which he did a little bit of in that paper,
*  then you have a lever with which to understand how differences between models, differences
*  between artifacts and their assumptions and their architectures might relate to human
*  cognition and behavior.
*  So I guess I see the most stripped down version of the prediction task is just, hey, here's
*  a really high dimensional data structure that I can kind of compare to and use as a benchmark
*  or outcome that goes beyond performance benchmarks like achieving an NLP task and goes beyond
*  the low dimensional behavioral outcome predictions, which often from cognitive science
*  don't have enough data to really differentiate models.
*  There's some counter examples to that.
*  So that's the kind of stripped down version is just like brain score is amazing as a
*  framework, brain score being this comparison of models to brain data and scoring them on
*  their fit to help out brain data.
*  So it's amazing in part just because you bring really high dimensional data to bear on
*  understanding which representational assumptions of the models matter.
*  One of the reasons you've been on my list for a long time, I have a really long list of
*  people that I want to invite on the podcast and you've been there a long time, but I
*  happen to see I had Jeff Bowers on recently, Jeffrey Bowers, and he argued that we need
*  to start testing large language models like psychology tests as we do in psychology, as
*  you do in psychology.
*  And you had a similar sort of, I guess, tweet thread along the same lines.
*  And this was related to the usefulness of using prediction as a proxy for comparing
*  things and for explanation.
*  And one of the things that you warned against, I suppose, is that there's a problem with
*  saying that this particular large language model has this particular cognitive function.
*  It can relationally reason or something like that.
*  So what's the problem with saying that a large language model has a particular cognitive
*  function?
*  Well, so from a measurement perspective, I think all of that tweeting that I was doing
*  was really subtweeting people who are screenshotting language models and saying the model does
*  X or doesn't do X, which is the equivalent of the cognitive scientist taking a video of
*  their kid at the dinner table and they're like, oh, yeah, my kid does relational reasoning.
*  Right.
*  Just look at this.
*  And an anecdote is not a data set.
*  So I was suggesting that the minimal thing that you might want to do in evaluation is
*  follow some psychology best practices like having a control group that is matched, a
*  control condition that is matched in all but the key way to the experimental condition
*  where you actually evaluate a particular test.
*  You also, of course, want to look for data contamination to make sure that your test
*  hasn't been used before in a very similar or even identical form in the literature so
*  that the language model hasn't been trained on it.
*  You might want to use multiple different items of the surface form of the item that you're
*  using doesn't contaminate the task because you might see success in a reasoning task
*  that's instantiated in a particular kind of common item and then a failure in a more general
*  item or a decontextualized version of the reading, reasoning task.
*  So I was really kind of ranting on the topic of experimental methods because that's what
*  I teach and I'm passionate about.
*  And so when you get these screenshots of like model can't do causal reasoning or can do
*  theory of mind or whatever, the truth is often more complicated because these models
*  may vary widely in their behavior based on how you're asking the question, what the
*  materials are and so forth.
*  Just like kids, as it turns out.
*  Meanwhile, you're drawing cartoons of all the psychological approaches along the tweet.
*  So I'll link to that tweet thread in the show notes so people can read the full thing and
*  visualize what you were just saying.
*  I know we only have a few more minutes.
*  What's more fun?
*  Building data repositories and doing open site ensuring that your data is structured
*  well so that it can be shared and so that we can all be good open science practitioners
*  or not worrying about that and asking the questions that you want to ask and doing
*  non-reproducible, perhaps non-reproducible science.
*  What's more fun?
*  What's more fun?
*  There's a version of open science that I worry is like the open science that everybody
*  is pushing for, which is fundamentally boring.
*  It's compliance-based open science.
*  It's yeah, okay, at the end of your research project, you got to fill out all these forums,
*  document your thing, put the link there, upload the thing here.
*  That is kind of boring.
*  It's really important.
*  It's critical.
*  Don't get me wrong, but it's not fun.
*  Compliance is not like the way I want to spend my time and I'm either monitoring
*  compliance or doing compliance work on my own science.
*  But the alternative version is really like I took my research program to be an argument
*  for the idea that if we follow open science principles, not in this compliance-based sense,
*  but in the broader spirit of them, which is to collaborate, to make open, to make accessible
*  our research, we actually enable new discoveries that are more interesting.
*  And that's what's fun is when we get data from labs around the world all working together,
*  sharing their materials, their code, their data openly in service of a particular scientific goal,
*  like the Many Babies Consortium, which is this collaborative network.
*  When we do that, we have a pre-registered hypothesis.
*  We've thought through what we want to do.
*  Hundreds of people around the world have looked at our stimuli and we've often
*  found them wanting in different ways.
*  Then we see something fundamentally new and exciting.
*  So it's that power of openness to fuel collaboration, to fuel the pooling of effort,
*  and to allow us to go beyond what we were doing before, not just to make what we were
*  doing before a little more solid and a little bit more compliant.
*  That I think is fundamentally fun.
*  The fun I have is it's like the kid in the candy store or the Christmas morning.
*  It's opening up the data set that wouldn't have been possible without those principles of openness
*  and sharing and the analysis that wouldn't be possible if we weren't reproducing what others
*  had done and building on it code-wise and data-wise.
*  Okay.
*  Okay.
*  I promised I would let you go right at the hour and I've taken us to the very last minute
*  and few seconds.
*  So Mike, we could have talked a lot more about a lot more things, but I really appreciate
*  your time and I know you're a busy fellow.
*  So thanks for your time.
*  Thank you so much.
*  It's a pleasure.
*  I alone produce Brain Inspired.
*  If you value this podcast, consider supporting it through Patreon to access full versions of
*  all the episodes and to join our Discord community.
*  Or if you want to learn more about the intersection of neuroscience and AI,
*  consider signing up for my online course, Neuro AI, the quest to explain intelligence.
*  Go to braininspired.co to learn more.
*  To get in touch with me, email paul at braininspired.co.
*  You're hearing music by the new year.
*  Find them at the newyear.net.
*  Thank you.
*  Thank you for your support.
*  See you next time.
