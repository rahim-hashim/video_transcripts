---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 5306s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 6279
Video Rating: None
---

# BI 064 Galit Shmueli: Explanation vs. Prediction
**Brain Inspired:** [March 28, 2020](https://www.youtube.com/watch?v=IzZrGBIotro)
*  This notion that scientific knowledge is, you know, on a pedestal if you understand how things work,
*  that's what we're trying to achieve. We don't really care about prediction. Prediction is just to utilize it, to make money out of it.
*  I don't agree with that. Nobody says that you have to stick with theories forever.
*  Theory, the whole idea of science is that theories evolve and get better.
*  But forgetting about theories and saying, oh, they're useless.
*  It's kind of cool and, you know, Silicon Valley to say that.
*  And I used to be very, you know, it's very nice and that, but it's not long term thinking and it's not deep thinking.
*  This is Brain Inspired.
*  If you have a machine that can accurately predict something, does that mean that you can explain how the machine works, how the predictions were caused?
*  Likewise, if you can explain how a machine works, does that mean you can use it to make accurate predictions?
*  These are pretty important questions these days in neuroscience and AI because we have these complicated machines called brains.
*  And we use other machines, vastly less complicated, but still complicated, deep learning machines or models,
*  which we use a lot these days to model various brain processes.
*  But if we make a deep learning model that perfectly predicts brain activity, as some studies these days are trending slightly toward,
*  does that mean that we can explain brains, let alone understand them?
*  After my conversation with Uri Hasson last episode about brains as brute force data fitting machines,
*  I started exploring the difference between prediction and explanation and I reached out to Galit Shmueli,
*  my guest today, because Galit has written clearly about the difference between prediction and explanation and their various uses.
*  And I found her because of her 2010 paper about the difference between predictive and explanatory models and predictive and explanatory power.
*  And you can find her giving talks on this topic online as well.
*  Galit is a statistician. I mean, data scientist or no, I mean, statistician.
*  Well, actually, she doesn't care which of those you call her.
*  She is a professor at National Tsinghua University in Taiwan, and she's done a lot of work in data mining for business analytics.
*  And she's written multiple textbooks on the subject, among other things.
*  But she has a broad background in all things statistics.
*  So she's not a neuroscientist and she doesn't work in the AI industry, but she's an expert in modeling, especially as it relates to statistics.
*  And I was curious about what she might think of the prospect of using deep learning to model brains.
*  I did record this a couple of weeks ago, so you'll hear me in the very beginning, you know, being the clueless American ignorant of the coming coronavirus situation.
*  When I spoke with Galit, the start of her semester had been delayed because of Covid.
*  I just checked in with her and she says she's doing well and they are having classes and they're still taking lots of precautions.
*  And she said she's thankful for the super quick and effective response of the government there.
*  Ahem, ahem, hint, hint. And that they are inching closer to normal life.
*  So that's good news.
*  She also mentioned that we both, ironically, probably in retrospect, sound a little too casual about Covid,
*  especially given that our topic is predicting and explaining things during this episode.
*  Anyway, don't worry, I'm not going to do a coronavirus special episode, just like every other podcast it seems.
*  So you're welcome for that. But I do hope that you are well.
*  Oh, and Azat, Esen, Connor and Bruce, thank you for your support on Patreon.
*  I got a little delayed myself creating the first bits of the Brand Inspired course, but it is coming.
*  And you guys and the rest of my Patreon supporters will see those first bits soon with more to come later.
*  Learn more about Galit and her work in the show notes at brandinspired.co.
*  slash podcast slash sixty four, or you can follow her on Twitter.
*  She's at G. Schmueli. I hope your models are working well out there, whether they're predicting or explaining things.
*  All right. Here's Galit.
*  So it's 730 p.m. on a Friday here in Colorado.
*  It is 1030 a.m. Saturday morning there in Taipei.
*  Galit, thanks for being on the show. What's the future like?
*  I guess when you have these black swans like a coronavirus, you stop forecasting very far ahead.
*  I didn't even think about that.
*  That's everywhere around us. Yes.
*  Oh, man. Are you sequestered in your home or what?
*  Well, I think it's, you know, like a lot of things, it's blown a lot more out of what it really is.
*  But our semester starts on Monday, so I'll be more knowledgeable to tell you how crazy things are in a few days.
*  So it has been delayed then.
*  It has been delayed by two weeks. Man.
*  Well, good luck. Wonderful. Longer.
*  Yeah. Longer winter vacation. Who says no to that?
*  That's right. Well, again, thanks for being here.
*  So, you know, this is this is different because you're a professor of business analytics.
*  Is it Xinhua University? Is that am I pronouncing that anywhere near correct?
*  It's Xinhua. You can think of it as a CH. Yeah.
*  So business is not your background.
*  But I know or I understand that you came to it through statistics.
*  And of course, statistics is why I'm speaking with you today.
*  So you've written a bunch of books about time series forecasting, data mining for business analytics, information quality.
*  And I could go on.
*  And from what I understand, your introduction to writing textbooks, you had you had found this software that you wanted to use.
*  But there wasn't a guide for it. You didn't really know how to use it.
*  You didn't have anything to guide you.
*  So you ended up writing the textbook for people to use the software.
*  Is that right? Yeah, that's kind of right.
*  I mean, I was an assistant professor at the time and I inherited a course in kind of advanced statistics that I was converting into a data mining course.
*  It was one of the earliest data mining courses in business schools.
*  And I did not know about data mining much myself.
*  So I was kind of moving in the direction myself.
*  And I needed to teach business students, MBAs and MBAs can't read the computer science books.
*  So there were lots of books, except they were not readable to the audience that I was supposed to be teaching.
*  So, yeah, I ended up teaming up with a couple of people.
*  One person who was created a software that was an add on to Excel, which means the MBAs could work with it.
*  And the other one was also helping with writing cases.
*  And the three of us sat together and wrote the textbook.
*  And the textbook has evolved over the years.
*  We just came out with a Python edition recently.
*  Yeah, you have like 17 editions in different programming languages.
*  Well, yeah, that was based on demand, although I was not always happy with it.
*  But that's kind of how the world moves. Right.
*  I mean, it takes turns and things happen and you have to adapt.
*  So, yeah, that's how things work.
*  I mean, so part of the reason why I do this podcast is I'm a big fan of podcasts.
*  I mean, in general, I was kind of disappointed with the fairly superficial level of scope of science podcasts that existed.
*  You know, they're geared toward the broadest audience possible.
*  But I wanted more depth.
*  So I basically created what I wanted in, you know, creating the show.
*  I'm just kind of wondering, you know, what the process of needing a textbook and so just going out and creating it, you know,
*  what has that taught you about yourself and or just about your kind of work?
*  I guess, you know, it started a little earlier when I when I moved out of.
*  So I studied at the Technion and that's an engineering school in Israel.
*  And then I was in a statistics department at Carnegie Mellon for two years as a visiting assistant professor.
*  But once I moved out of those two places, I moved into business schools.
*  And when you move into a business school, you face this really big, different kind of expectation and both of your students and your colleagues to explain really complicated stuff in simple ways.
*  So a textbook is kind of like that because you have to take really complicated ideas and bring them, simmer them down to really just the essence, the main important things.
*  And those principles are what you need to disseminate or teach or discuss every all the technicalities.
*  I mean, taking layers off of things actually was it's a hard thing to do.
*  But I think for me, it's been one of the best things because you figure out what really matters.
*  Yeah. Yeah. So that's the process.
*  It's the process of writing fiction and non from what I understand.
*  It's just kill your babies is the whole the whole idea.
*  Right. I wouldn't know about writing fiction.
*  I'm terrible. You know, when I have to come up with when my daughter was young and I had to come up with, you know, stories before bed and make them up.
*  That would be like the most terrifying moment, much worse than writing the next chapter in the textbook.
*  So, yeah, I've had my off nights there as well.
*  So, OK, well, let's get into this.
*  So I'm just going to lay out the situation here in and you're not an expert in deep learning or neuroscience or anything.
*  So, you know, I'm really fortunate that you are stepping out of your own ocean of expertise here and joining me on the show.
*  So so we want to understand intelligence.
*  We want to understand how it works.
*  We have these deep learning models that perform cognitive tasks well.
*  So you can have a model perform a task like a categorization task.
*  And it turns out when they're performing the task well, if you set them up the right way, they predict neural data well.
*  Well, but now we're faced with the task of understanding the model to help understand our brains.
*  And the whole goal is to use these models to help us understand our brains that are these models are very loosely based on.
*  So there are there are a lot of different goals in neuroscience and there are a lot of different questions that you can use neural networks to ask, as you know.
*  But an overarching goal is really to understand the nature of the complex processing within the neural circuits that give rise to our minds, our thoughts.
*  You know, we want we want to understand we want insight.
*  We want to feel like we know.
*  And I've actually seen you giving a tutorial on neural networks for the purpose of forecasting financial data, for instance.
*  And and you're there, you're explaining how it works and what you get from the neural network.
*  And then you point to the parameters, which are the connection weights between the units.
*  And you actually say these are not very useful or interpretable.
*  What we care about more is the performance.
*  So it's not your goal in forecasting in that respect to explain, to understand what the you know, what the parameters mean, what the models how how the model is doing its function right.
*  OK, so that's a long preamble.
*  So I apologize. But now deep learning in general has infiltrated a large part of neuroscience.
*  So, you know, whether it's using these neural networks as models of brain networks, like I was just talking about, or using them as tools of analysis.
*  The frequent trope these days is that deep learning is basically just statistics on steroids.
*  And then usually someone says that and then it's followed up by the notion that what we really need is to build causality into the models.
*  So my knowledge of deep learning is really within the neuroscience world and within the A.I. world.
*  And so I have really no have no idea how it's used in the financial sector and in the statistical business analytics world.
*  I mean, has deep learning affected the stats community at all?
*  OK, so I think you have to really separate between industry and academia.
*  Yeah, this is like deep learning, as I think, you know, kind of if you're talking about discrimination and categorizing, it's a totally different story in both places.
*  If you're looking in industry, then obviously it's had some really magnificent successes, you know, in anything from natural language processing, you know, image recognition.
*  Those are proven. I mean, things got better once they started using these models and the data, of course, that they rely on.
*  When you look in academia, I think the story is a little bit different.
*  So I'm talking about you asked me about statisticians.
*  So let me let me also explain that I am probably not a typical statistician in the sense that I don't attend statistics conferences, the main ones.
*  I don't go to those. I'm not part of the mainstream community.
*  The data mining or business school type of statisticians, data scientists, wherever you want to call us, we kind of go to other places.
*  So, for example, I work very closely in in the field of information systems.
*  So I will go to some major information systems conferences that are more around data science.
*  So the more technical ones I publish in those kinds of journals, you know, I will be more integrated with people in marketing and again, information systems,
*  management. So what you're hearing from me about statistics might not be representative if you speak to a mainstream statistician.
*  But what I do see is the following usually in the field of statistics.
*  And I do follow I read journals, I read papers, of course, the majority of statisticians will see something like this and say, that's just a fad.
*  The computer scientists are playing whatever they're doing. We already invented it.
*  It's kind of just a special case of, you know, it's just, you know, nonparametric stuff.
*  A lot of them will say that. But then you have a very small and growing group, actually.
*  Now they're actually much bigger, like people in Stanford who did a lot of work on on studying machine learning from a statistical point of view and actually enlightening a lot of the mystery that the CS people,
*  the computer science people, you know, just said, it works here. It's working. We have no idea why, but it's working.
*  But these statisticians kind of broke it apart and were able to figure out a lot of properties.
*  And there are papers coming out of people like that in that group.
*  So if you search journals and statistics, the top journals, you will find here and there are some papers like that.
*  But that's far from mainstream. OK, so it's even statistics is a very fragmented kind of area.
*  And then what I'm seeing is both in the types of conferences that I go to and also I saw in the in the last joint statistics meeting, the big meeting,
*  they do have something like a workshop dedicated to deep learning because I'm sure a lot of people are curious about what it is.
*  And then they'll bring someone. So I saw for JSM for the statistics meeting, they brought someone from Amazon to come and explain how it works in the big conference that I went to.
*  When was this? Maybe two years ago, they had a faculty who that that was his expertise and he did like a few hours workshop with hands on and stuff like that.
*  So there is interest. People want to know what it is. I don't think that a lot of them are using it.
*  This is not like something that people will go and keep developing it.
*  There's a small niche of people who will, but the majority won't.
*  What I also see is, you know, and I said this is a big divide between academia and and industry is that in order to run these models,
*  you really have to have access to the enormous data sets.
*  But those are everywhere now. Not really. Not really. Not really.
*  The type of data that Google and Amazon and Microsoft have is not what we have in academia, not statisticians.
*  OK, you might be thinking about the computer science people, but also I'll tell you another thing.
*  A lot of the data that's out there that's collected Wild West style by the big companies.
*  We academics are actually not allowed to do it right without going through ethics committees.
*  Yeah, those ethics, they get in the way, don't they?
*  No, they should be there and they should be regulated as well in industry.
*  But I think that's another thing.
*  And the third thing is, you know, statisticians tend to work.
*  Applied statisticians work with other people who have data.
*  They don't go and collect their own data.
*  So maybe if they're working with a neuroscientist, they will have access to your data, but they won't go and collect the data on their own.
*  Usually, if they need to create data, they'll simulate data.
*  That's like the statistician approach to things.
*  And is it did I make a mistake by even saying statistician?
*  Isn't it data scientist now?
*  You know what? You can name me any name.
*  It doesn't matter as long as you're happy to talk to me.
*  You know, years ago when you'd meet new people and say, oh, what do you do?
*  What's your field? It's like statistics.
*  Like, oh, yes, we had this terrible course and statistics.
*  I suffered so much. You're probably so smart.
*  Yeah, you're probably so smart and I don't want to hang out with you.
*  Yes, exactly.
*  So, I mean, I don't really care.
*  But to be very honest with you, I've living in a business school makes you look at things, I think, from a higher like a big picture kind of thing.
*  So it's not so much the nitty gritty of doing things, but it's how do you solve problems with these methods?
*  And that makes you more of, I don't know, a problem solver that's open to lots of different methodologies and looks around for just good tools.
*  It's kind of like an engineering mindset in the sense.
*  Yeah. Well, see, that's there's this divide and it can all be in academia, but there's this divide sort of between A.I. and neuroscience.
*  In that, in A.I. tends to be or can be can afford to be more engineering like in their approach and just build something that works.
*  And if it works, that's great.
*  And it doesn't matter how it works if it accomplishes the task.
*  Whereas in on the neuroscience side, we actually want to understand how and we want an explanation, not just a prediction.
*  And we'll get into this difference between explanation and prediction in a few minutes here.
*  You know, it's interesting you mentioned the word how I think the type of question that you ask is really fundamentally different.
*  And it's it's not so obvious.
*  I mean, for example, because I know nothing much about neuroscience beyond, you know, popular books, there's kind of different kinds of explanation.
*  So when you're saying, yeah, we're trying to understand how you also have other kinds of questions, which is that we're trying to understand why.
*  And then sometimes you have questions, especially in industries, like they just want to know what what causes that or if I do this, what's going to happen?
*  Right. What's going to happen?
*  And then you have the whole world now of deploying these decision making algorithms where people want explainable predictions.
*  It's like, why did it generate this prediction?
*  And all these different questions are actually totally different.
*  And they call for completely different ways of modeling and thinking about the problem.
*  So when you set up the neuroscience context for me and you said we want to understand how things are working, it's still not specific enough for me to be able to say, oh, so this kind of modeling is what you want to do.
*  I'd have to drill down a lot more to get you to give me the type of the narrow question that you want.
*  Yeah. Yeah.
*  Yeah. And I want to keep it as broad as possible because there are so many different types of questions and in different sectors.
*  And there are how and why questions, you know.
*  OK.
*  So yeah. So who knows what we'll actually get to and what kind of progress we'll make here.
*  But well, so I suppose one eventual situation is that we have this model that perfectly predicts brain activity.
*  But we don't understand how the model works.
*  Right. So we can recapitulate brains down to the level of the activity of individual neurons, let's say.
*  But then when we step back and look at it on the whole, it's let's say it's performing some task like it's, you know, turning a screw, a robot turning a screw on a line or putting a car together or something like that.
*  But we don't understand how it's doing it.
*  So we haven't actually.
*  So in that sense, we have made a perfectly predictive model, but we haven't made a model that explains how it is functioning.
*  So I guess what we really want, or at least what I want, is a model that has explanatory power and then beyond that actually is interpretable for me to understand.
*  Yeah, that's the dream, right?
*  That's the dream.
*  So I guess, look, if you're able if you're able to create like an incredible predictive model, I think it has a lot of scientific value.
*  And actually, you know, it's kind of funny.
*  Probably, you know, a lot of people know my explain to explain or predict paper, but it actually has a sister paper that's in a in a different journal and that fewer people know about it because it belongs to it.
*  And that one is in an information system journal called MIS quarterly.
*  And that one is called something like predictive analytics for it's called predictive analytics in information systems research.
*  That's right.
*  Now, you can actually, to be very honest, you can scratch out information systems and just put in predictive analytics in scientific research.
*  But this was kind of geared with examples towards information systems.
*  And what we do there is we talk about how you can use prediction for scientific research improvement.
*  So not just for utility like companies.
*  Right. And what you just gave me an example of is I have this I am able to create this amazing predictive machine.
*  It predicts very well the phenomenon that I'm interested in studying in terms of causality.
*  But I don't know anything about it.
*  What have you just created for yourself?
*  You've created an amazing benchmark.
*  Now, any explanatory models that you have that are competing theories that you have, you can actually see how well they're doing, where they're doing better and where they're doing worse, because you know what the prediction thing, how well that prediction works.
*  How well that prediction optimal system is working.
*  Having this benchmark, I think, is amazing.
*  Can you I can't even imagine if you had something like this and lots of fields, medicine.
*  I mean, think about what it would mean.
*  It would be really useful.
*  That's a that's sort of where we are with in neuroscience.
*  Science there.
*  You know, the most well known example is you set up a deep learning net and compared to any other model, it predicts neuronal activity in the visual cortex in this hierarchical visual system that we know about in brains better than any model that's ever come before it.
*  So we do have that benchmark, which is how the field is progressing.
*  And so other domains are kind of following along in this same vein.
*  Right. And I guess, of course, I mean, the question of causality is a super important one.
*  And I mean, Judea Pearl has finally made enough noise that people are hearing about it in lots of fields.
*  Yeah. But this these questions about, you know, why are things happening and what happens if you start changing and manipulating stuff?
*  Because at the end of the day, those are the you don't just want to know for for not for knowing.
*  Right. You want to know so that you can start controlling.
*  Let's be honest. Everything's about control at the end.
*  We're humans.
*  So in order to control, you really need to be able to know what knobs to turn.
*  And when you turn them, what is going to happen and what will happen if you don't turn them right, the counterfactual questions.
*  So that is going to play an important role.
*  But sticking only with prediction, you know, it's interesting.
*  The explained predict came out in 2010.
*  That's 10 years ago. And the world has so dramatically changed in these 10 years.
*  Back then, industry was not doing any prediction.
*  It was it was it was super rare.
*  It was big data, big data yet. I don't even know.
*  No, there wasn't the word big data. There was no word analytics yet.
*  I mean, business intelligence, I think, was kind of the hot word.
*  So industry was not really doing prediction because, you know, folks in industry were studying statistics and learning how to do T tests.
*  That's kind of the regression models with hypothesis tests.
*  And then finally, data mining started kicking into business.
*  And that's when everything changed.
*  So now all of a sudden, industry is doing massive prediction, massive prediction on everything without caring why or how.
*  Right. They do care about what.
*  So they do a lot of A B tests. Right.
*  It's like, oh, if we change the color of the light button from blue to light blue, is it going to make more money or not?
*  So they care about that. But they don't care about why.
*  And, you know, what are the implications and what's the whole system that's down there?
*  So industry has turned completely 180 degrees.
*  Academia, I think, has been kind of slow to change, but it depends on the field.
*  So I guess in neuroscience, because because the neural nets kind of reminds people of the brain, they feel comfortable with something that has all these nodes and layers.
*  I guess that's why maybe it's I don't know, you know better than me.
*  It's acceptable. It's less acceptable in other places.
*  Although I do see many colleagues now, for example, you go to conferences, you read papers and they will just as a convenience kind of start using image tagging with with neural nets.
*  So instead of before, maybe they had Amazon Mechanical Turkers doing the stuff for them.
*  It's like, OK, now you just ran.
*  We did a little bit and we labeled all the rest using deep neural nets.
*  So people use it as a convenience.
*  It's like, oh, we have a new powerful new button on on on our software.
*  But it's not really at least against social science kind of behavioral scientists.
*  I haven't seen them using it for trying to really mimic the whole system.
*  It's a piece of yeah. Yeah.
*  The few that I should say, I mean, there are efforts, small efforts to try and use deep learning for modeling behavioral data.
*  And I'm not talking about neural.
*  I'm talking about behavior as in well, whether it's online behavior or anything like that.
*  Yeah. OK. Yeah. Yeah. Exactly.
*  Clicking purchasing searching. Yeah.
*  Yeah. A lot of it is online.
*  I mean, because we have data, right.
*  Or companies have data online.
*  And again, I can tell you in academia and in the work that I've seen and I've sat on some PhD dissertations and I'm involved in some collaborations with double E colleagues.
*  The behavioral data is a lot trickier and I don't yet see much promise with results with a deep learning compared to just framing your problems appropriately and getting your data into the right shape and thinking about what makes sense and what doesn't.
*  And then just using models, you know, machine learning models that are more reasonable, simpler and efficient and environmentally more friendly, meaning not consuming enormous amounts of power and software and scientifically open.
*  We know what the algorithms will kind of open because we're always using someone else's software.
*  So, yes, it's OK.
*  OK. Well, so you already mentioned your to explain or predict in the sister paper, the predictive analytics in research paper.
*  So you've given lots of talks about this prediction versus explanation and whether you like it or not, this is sort of made you well known.
*  I don't know. Do you feel well known from it?
*  This is how you get invited to a lot of places, I think.
*  Well, it's kind of interesting. I'm always pretty shocked at where this paper has reached.
*  I get emails, I guess, on a regular basis from fields that I have not even imagined.
*  And it's so interesting to see how they said, oh, wow, you know, we've never thought about this before, but in our field, we typically only do this and that.
*  And people have used this paper to try and write editorials into their field.
*  So it's really, really interesting to see this.
*  And then also what's nice about it is all of a sudden I'll get an email from someone saying, yeah, I read your paper.
*  And there are also this other interesting paper that came out, you know, in 2007.
*  What do you think about this one? I haven't seen that paper. Of course, it's like, oh, thank you very much.
*  Yes. This is really interesting.
*  So I'm also getting introduced to relevant stuff that's happening in other fields where people are beginning to do the explain predict.
*  And I find that very interesting.
*  Yeah, you're right. I give a lot of talks about this because I think it's important because people find it interesting in almost every field, which is kind of shocking.
*  But that's why I wrote that paper.
*  And I think it's definitely not the end.
*  And there's a lot of things that evolved since I wrote that paper that I learned that I'm still learning.
*  I've also started playing with all kinds of crazy stuff since then.
*  Yeah. Yeah.
*  I mean, you know, the fun of once you realize that there's this this this big difference between things you you can you can play on both sides.
*  You can take the machine learning stuff and see what kind of useful things you can do in the causal world with them, which is an interesting, really interesting.
*  So, you know, I have a few interesting papers that I did with colleagues on trying to use mostly trees, which are this amazing tool, amazing tool.
*  Amazing. Yes. But using them for causality, things like identifying Simpson's paradoxes in large databases that would totally change your your your recommendations means the whole causal direction flips when you break down the data by something.
*  Or it's just an amazing tool. So it's kind of taking the machine learning tool and seeing what you can do with it in order to enhance causal work.
*  And then you're playing also the other game, which is kind of really interesting, is taking these models that are only well, they were kind of by design for causal modeling things like structural equation models that are very heavily used in in marketing in behavioral world where they have.
*  It's basically if you know, Judea Pearls, arrows, you know, nodes and arrows, the arrows mean causal stuff.
*  So people in these behavioral fields start from that. And then all their modeling is just geared towards testing causal hypothesis.
*  And then we're taking those models and say, can you actually use them to predict generate predictions?
*  Because if you're going to build any kind of model, you want them to have an ability to generate predictions so that you can even test their relevance and see how they're doing.
*  So it's kind of an interesting thing to play both both sides and see they don't really meet. But it's interesting. You learn different things. You learn different things.
*  Well, so we're on the heels here. I will have just released an episode with Lori Hassan, where which is how I became aware of you from a reference from one of his papers recently that talks about the use of deep learning networks as models in neuroscience.
*  And he came to this realization that in understanding brains and minds, we have this tacit assumption that what the brain is doing is building an explanatory model of the world that it's perceiving.
*  But what deep neural networks do really well is they're not building models. They're just predicting really well.
*  And what he calls direct fitting. So, you know, in modeling, you can underfit if you have like huge bias. Right.
*  And so you're not explaining the data very well. Then you can overfit so that your fit goes through all of the data points and all the noise.
*  And then you give it new data and it can't predict anything. Well, and his idea is that what neural networks are doing and what brains are likely maybe his suggestion is that brains are doing well.
*  His suggestion is that brains are doing the same thing is direct fitting because there's so it's the model our brains and the deep learning networks are over parameterized.
*  So they're able to handle all of this predictive ability and basically directly fit all the data.
*  And then when there's a new data point, they have the capability not to have to use a model that it's generated for the underlying data, but just to by dent of its overparameterization.
*  Interpolate to that new data point and it will fit it. Well, I'm not sure if I explained that well enough.
*  And did you look at that paper that I sent you by chance? I did. I did. And it's a it's a very well written paper, although it's kind of something that I have to think about very deeply.
*  But I mean, there are a few things there that kind of raised interesting questions in my mind. So I think, first of all, it's a very interesting paper. And when a paper kind of makes you think and ask questions that that's already like a good paper for me.
*  Me too.
*  So there are a few things about it. First of all, the notion of overfitting and there's a very nice graphic in that paper showing the under fitting and the overfitting and then the what is it called the exact fitting direct fitting.
*  Yeah. But what struck me there was that the direct fit curve and maybe that's just, you know, not really what's happening. It also kind of goes through all the data points. Yeah. Yeah.
*  So we would call that an overfit as well. Yep. Except that you have some kind of a requirement or a I mean, that's what we do in regularization. Right. So that the the polynomial there was not going up and down as crazy. It was almost like linearly interpolating the points almost.
*  So it was more of like a, you know, a space where you limit it. You say you can't go crazy with your polynomials, but you can still go through the points. If you're doing that, it means that you're assuming that your measurements have no error. There's nothing else. Your points are the points.
*  So where are you allowing for the error? And that kind of the question that that comes to my mind is where is your uncertainty coming from? Is it that different brains will have different points for the same inputs? Or do you not care about different brains because you assume all the brains are the same and they're all functioning in the same way. So there's no variability. So I'm not sure where the variability is coming in, but I'm not seeing it in the direct fit. And again, maybe it's just because I'm focusing too much on that image. Yeah. From what I read, they're just basically saying, let's just regularize.
*  And regularization is, yeah, sure. I mean, we do that all the time. And it's usually very useful when you're building predictive models. It's useful when you're building descriptive model. It's not useful when you're building explanatory models. That's kind of defeating your purpose.
*  That's kind of the point is that is that these are just really great predictive models. And I yeah, those the images that you're referring to, I mean, I think they are schematic because even in individual brains, it's it's known there's a lot of variability within the way that neurons operate. So I imagine that that that those perfect fits with the lots of squiggles is just a schematic to show that it can work ideally like that.
*  Okay. You know, the other thing that it brought to mind, I shouldn't say that right, it brought to mind is at the time when I did a lot of work on online auctions, we were looking at data coming in from an online auction, and we were trying to predict, you know, in real time, if the price is here, what is it going to be at the end of a seven day eBay auction or something. And we had, you know, tons of auctions, and we were trying to fit curves basically to the price. So the price from the start till the end of the auction, where you just have the beginning. And you have examples of the price that you're going to get at the end of the auction.
*  And you have examples of other prices that you had before. And what we did was we basically ended up using a non parametric function. We use this, it's a field called functional data analysis and statistics, which of course is messing up with neuroscience because for you functional data means something else.
*  But functional data analysis is just a field in statistics that uses these. It treats instead of using vectors as objects, you're using anything that you want. It could be any kind of functional. So we ended up using those things and and they're non parametric.
*  So again, you can say they're overparameterized. You could think of splines basically. But we knew that prices and auctions can only go up. They can't go down. The price cannot go down. So we constrained them. So by putting a constraint, we only had a set of these kinds of models.
*  So they're still very flexible. There's so many ways they can capture the data, but they're limited by some domain knowledge that we know about the problem. And I think the same thing, if that's what you want to do, constrain these neural nets by saying, look, but some things we know cannot happen. That's one thing. I think that SunPaper is not doing that. They're saying just regularize it. Let the data control things. So I don't know. I'm not an expert on any of this. It's just my questions that came up to mind.
*  Oh, that's great, though. Well, okay. I mean, like I said, you've given so many talks about this, but let's let's talk about prediction and explanation to be crystal clear here. So these days, so models, if you don't have a model these days, you're not doing science. And in general, I mean, all of this is up in the air. But in general, models are broken down into three types, descriptive, explanatory and predictive. And I had not thought of this, but you have pointed out that statistics is more than just a model.
*  And using descriptive models. So what are descriptive models and why has stats mostly dealt with them?
*  Okay, so descriptive models, they're defined by their goal. Okay, so when we say descriptive, it means that your goal is to represent in some parsimonious useful way a relationship between an output and a bunch of inputs. Okay, that's what I'm trying to do.
*  Correlation wise, okay, I just want to find out, you know, what's the correlation structure between inputs and an output of interest? Why do I want to do that? I have the sample and then I want to test this correlation in a larger population. And that's where statistics basically, I mean, that's one big field of statistics. So there's so many problems that arise little technical problems about how do you generalize from this kind of sample, and you can fit lots of little representations, descriptions, and so on.
*  How do those generalize and what can you say about them? And if you went through a process of variable selection, does that change the way you have to do your inference? They're just endless question. It's a rabbit hole. It's a rabbit hole for a whole field. And that's why there's been so much work on this in statistics. There's so many descriptive models. Even if you think of a histogram, you know, when you're plotting your data, what is it? It's a descriptive model, but it's a model, right? You choose your bins, it's a model. And so you can do that. And so you can do that. And so you can do that. And so you can do that. And so you can do that. And so you can do that. And so you can do that. And so you can do that. And so you can do that. And so you can do that. And so you can do that. And so you can do that. And so you can do that. And so you can
*  you're speaking to it. Yeah, you're speaking right directly to my heart as a neuroscientist. So yeah, the histogram.
*  There you go. So really, the field has been mostly about description. Again, prediction is relatively new, but things are changing. I mean, now there's more things happening with prediction, because it's useful, because it's hot, because there's funding, because there's tools, because whatever.
*  Explaining has been a very rocky thing in statistics. If you explaining and when I say explaining, I'm talking about causal explanation. You know, you change something and what happens to the outcome in statistics, the majority of.
*  Well, let's say this most statisticians will tell you you're only allowed to infer causality if you're running a randomized experiment like a clinical trial. That's the only way you can infer causality. Everything else. Forget it.
*  You know, you can always do experiments. We have all these.
*  Yeah, you can do quasi experiments or observational data, which is kind of similar. And then we have this whole toolkit of really interesting ways to try and tease out causality. It's very interesting. You know, I mean, I have not known about those tools until I'm really ashamed to say this, you know, maybe 10 years ago.
*  And I'm a statistician. They're pretty. I thought they're pretty recent, though. Are they not?
*  No, they've been around for a long time. OK, and I remember and I remember actually when I was when I was at University of Maryland in 2002, a little later than that, I was asked to teach some kind of a course on advanced statistics. And I looked at the topics and it had all these things in there. And I said, I'm going to teach you some advanced statistics.
*  I'm not teaching this, you know, someone else take this course for me. And it was all econ stuff. It was all kind of, but it's actually amazingly interesting and intricate and beautiful. And I think when you're seeing now some of the wars on Twitter or over journals with a lot of people, you know, they're all kind of like, oh, I'm going to teach this.
*  And then there's a rejoinder and then there's a response to the rejoinder and a response to the response. I've seen things like that before. It's when these clashes happen between the stats approach, the econ approach and Judea Pearl's new approach to identifying things.
*  So there's a whole set of thing of toolkits now that are more visible. And I think those are really the explained part of things. And that's not something that was done in statistics, because again, statistics explaining causal explanation was only the world of
*  experiments. And that's a very elaborate world that's geared towards more industrial type of experiments. There's the world of clinical trials, which is a small part of it. There's a much bigger part of the academic statistician body in the world of industrial statistics and quality control that developed lots of methods for how to experiment, how to set it up and you know, how many factors are there to be used to make it work.
*  So the world are so separate, that that's why you don't really get this mix. And until I stepped out of the world of statistics, and I came out of industrial statistics, actually, that was my PhD. So once I stepped out of there, and I moved into a business school, and my colleagues were behavioral people and like all kinds of interesting backgrounds and
*  econometricians. I was looking at them, I had no idea what they were doing. Really, I was shocked. So, so it is sometimes you have the reaction, I'm not teaching that course, take it away for me. But sometimes you just going in there saying, hey, can you tell me why you're doing that? And how are you thinking about this? And for them, it's so natural that they don't understand why you don't understand it. So it takes a long kind of working together and figuring out how to do it. And it's not something that's really simple. And of course, you need to be able to understand the real world of statistics and how to do it. And I think that's really important because you don't have to be trying to figure it out.
*  and trust to start seeing that these are really different things. Everyone's
*  seeing the world in a different way and developing tools to try and answer their
*  questions. And I think that's why when you're talking about neuroscience and
*  you know when it's gonna work better it's like you have to define your
*  questions so specific. What exactly do you want to answer here and then see
*  what kind of tools are available in different fields to answering that.
*  I mean I know if you look into the history of explanation, you know
*  explanation and prediction have had this interesting relationship in the history
*  of philosophy of science at least. You know there and you point out in your
*  talks there's a time when they were considered the same thing, prediction and
*  explanation. And then they split and they've been bouncing around ever since.
*  So how did explanation and prediction come to be appreciated as distinct? I
*  mean this is going back to the late 1940s I know. Actually the philosophy of
*  science is interesting because they were not looking at data at all. What
*  they were looking at was they were looking at logic structure. So if
*  you say something what does it mean? And in the early times, I mean in the
*  40s, there was really like you said there was this understanding that they're the
*  same thing. They have the same logical structure. There's no difference between
*  explanation and prediction. And there's explanation for them again it's a logic
*  structure. There's no data here. We're not talking about data. And then they had
*  all this back and forth debating over journals. You can actually see
*  the papers going on for and for ten years. And then finally you know there's
*  a nice paper by Helmer and Rescher in 1959 where they say it becomes pertinent
*  to investigate the possibilities of predictive procedures, autonomous of
*  those used for explanation. So they finally say you should dedicate some
*  separate space for these two things. Let's just explore them separately. And
*  then again debate debate debate debate debate and there's a really beautiful
*  book in 1969 that came out by Dubin. It's called Theory Building. And again still
*  we're talking about philosophy of science. And this is where the first time
*  he says theories of social and human behavior. Notice that he's talking about
*  social and human behavior. That's I think the most interesting part of it. They
*  address themselves to two distinct goals of science. One is prediction and two is
*  understanding. And he meant explanation is understanding. Yes. Which has come to
*  be those of distinct now too. Yes exactly. And I think the fact that they're
*  recognizing that they're both goals of science is really a tricky part.
*  Because you know I also wrote in my paper and I asked people and I was trying to
*  figure out what is going on here. Why have we not inherited some of this into
*  the world of statistics. And you see that this notion that prediction is just for
*  utility. Oh it's very useful. We can make money out of it. You know we can create a
*  product out of it. But explaining is the science. That notion is very deeply
*  ingrained into lots of minds. And I had I remember I used to have pretty fierce
*  discussions with an econometrician colleague from NYU. And at first he used to
*  tell me no no no no no. If you understand how things work you should be able to
*  predict them. And you can't predict them if you don't understand. And he totally
*  changed his mind by the way in the last 10 years. But this notion that scientific
*  knowledge is you know on a pedestal if you understand how things work. That's
*  what we're trying to achieve. We don't really care about prediction. Prediction
*  is just to utilize it to make money out of it. I don't agree with that. And as I
*  said you know industry is also doing all these A B tests because they're trying
*  to figure out what works what works. They don't necessarily care about the why.
*  Unfortunately that's because it's a broken way. They don't maybe care about
*  the how but they do care about the what. And definitely I think in a lot of
*  fields where we're finally seeing a little bit of progress that you know I
*  think fields that were stuck for a long time. Fields that were using data to
*  advance their theories and we're only doing explaining stuff. They were stuck
*  so hard. Bringing prediction in actually brings some you know some new ways of
*  thought and breaking some old themes that were there and were maybe not
*  supposed to be there. So yeah I think that that has changed a lot. So it starts
*  a long time philosophy of science and what I did it was kind of translated
*  into the world of data and modeling. Yeah. And it wasn't just me you know it was
*  this really enormous effort. When I was on sabbatical in 2008 and 9 it was like
*  a half year here half year there. I gave this talk I don't know how many times it
*  was before I wrote the paper and I gave it all over the world. I mean I gave it
*  except for Africa I think on every continent and I got feedback. Every place
*  I gave it to it was some were statisticians some were non statisticians
*  it was mix of audiences and every place I gave it to I got some interesting part
*  of it that would come from people that said oh you know in our field we find
*  this and I would go and search it up and they would give me some references. So
*  the paper at the end is actually not just my paper. It's a paper that brings
*  together lots of thoughts from people who you know heard about this and
*  discussed with me and gave me inputs and gave me thoughts. And that's I think what
*  makes it so interesting. What made you give a tour giving this talk before you
*  wrote the paper. Well it's kind of interesting. I think the first talk I
*  ever gave on it I probably gave a seminar just like within my department.
*  So you had formed some of some sort of core vague ideas and when that vague it
*  can't be vague if you can even talk but.
*  It's a very good question you know this is like a human memory. I don't remember
*  how it all really. I think I think I think here's how it started. OK I think
*  when I was writing that textbook we started from some notes our co-author
*  Nitin Patel had. He was teaching a course at MIT and in his notes there was a
*  chapter on linear regression and it had a few bullets at the beginning and it had
*  some weird bullets that said something like if you're using the regression for
*  prediction you don't have to do this and that or this doesn't matter. I looked at
*  this and I said what is this. And that was the start of the doubt in my mind. I
*  think that's what started it. But that's my reconstruction. And then I started
*  developing it and developing it and finally I gave like a little informal
*  talks with some thoughts you know some of these things that I knew that you were
*  doing differently this way in that way and why. And I was slowly building it up
*  and I gave a talk at it's called the CIST. It's a workshop of more like the
*  data type of things and information systems. And it was very raw but it won
*  the best paper. And I knew something was there but you know sometimes it's very
*  hard to articulate things. Again you know I don't come out of the humanities. I
*  don't write so well non-technical stuff. And I knew there was something there
*  and I knew that I needed to get more feedback. And I knew that I just touched
*  on something that was like you know something was much bigger was hiding
*  there. And that's why I went on the tour to give talks because every talk that I
*  gave every interaction that I had was like eyes were popping up and I was
*  either getting very antagonistic reactions or very heated. Oh yes exactly
*  yes yes yes this is what we're finding here and there. And I was hearing this
*  from people who I admired and you know were like the icons in their field. I
*  remember going to Arizona State University and Doug Montgomery who's
*  like a huge icon in industrial statistics and in experiments. He said to
*  me yes you know this is why response surface methodology does things that are
*  different from you know design of experiments. And he was enlightening me
*  to things that I knew about but I never connected them to the explain predict. So
*  that's why I did the huge tour. And I think that doing these tours is is
*  extremely useful if you can get good feedback. If you get to the right
*  audiences taking an idea that's that's a little out there and not the standard
*  thing helps you take it in a long way. And since then I've I've tried to do that
*  with all my crazy ideas. Yeah yeah it's a good approach for me. What's better
*  antagonistic feedback or confirmatory feedback? The combination. Yeah okay there
*  you go. Then you know you're on to something. Well done. Well let's let's get back a
*  little bit to just you know prediction versus explanation. So we talked a
*  little bit about the history of explanation and prediction developing
*  into a separate goal, a separate entity than explanation. And this pair of
*  papers that you're referring to 2010-2011 you know they really make the
*  case or they made the case back then really for prediction being a valuable
*  in itself and you talk about different ways in which prediction can function in
*  science. If it's okay can we just walk through a few of those that you know
*  come come to your mind and talk about them? Sure. So I mean first from my own
*  experience of delving a little bit with predictive models in those early days I
*  found that especially as you're moving into fields that are either the field is
*  new or else there's something new happening in the field. For example when
*  I was working on the online auction stuff online auctions were relatively new
*  in the early 2000s you know eBay started in I think 1999 or something.
*  So auctions all of a sudden moved online and everything changed because
*  behaviors online are totally different than in an auction room. And now you're
*  taking all the theories from game theory about auctions and you're saying oh yeah
*  that applies online as well. How do you know that right? So when you're building
*  predictive models you're trying to predict prices or whatever it is you're
*  able sometimes to find out things that the original theories did not think
*  about. Because how do you generate the original theories? How do theories come
*  into place? There's a lot of domain knowledge coming in that people
*  formulate and then over time they finesse it and test it and finesse it and test
*  it. But it gets stuck in a certain structure that you can't totally break.
*  Nothing is gonna give it a big whack unless you build in a predictive model
*  that says hey I can predict so much better than your current theory. So
*  generating new theory is one very useful thing to use predictive models for in a
*  field where there's really nothing much. In the case of the online auction thing
*  was it just you know you take the predictive model from the you know a
*  picture the cowboy hat and the quick talking gentleman the present auction
*  what do you call that? It's just an auction that's just an auction isn't it?
*  Yeah just the ongoing auction. Yeah as opposed to an online auction it would be
*  an offline auction? Oh yeah an offline auction. Okay so you take a predictive
*  model that works well with the offline auction and then and you just slap it on
*  and expect it to work with the online auction but you know it sort
*  of breaks right? And is that so that's how you generate the new theories to
*  determine how it broke? You could do that or you can also in parallel you can
*  develop predictive models on the online auctions and show that they're
*  predicting much better than the other ones. And now you're all of a sudden maybe
*  accounting for you know other stuff that's happening in the online auction
*  that's not part of game theory and say that's actually a very important piece
*  of of how humans are reacting to this thing that's not built into the old
*  theories. I see. So that would be one example. Another really useful thing to
*  do especially in in in social sciences you know where measurement is a serious
*  problem right? I mean we're all building models that are around constructs around
*  these abstractions when we say that something is increasing your
*  satisfaction or your engagement you know what does that mean? You have to
*  measure it somehow. So this this measurement level where you're
*  operationalizing something abstract into something measurable is basically a
*  whole field of psychometrics and it's a really difficult field and I always
*  I'm always shocked at how people think it's so easy to just create a survey and
*  send it out. When I teach my research methods course to the PhD students they
*  somehow have a notion that it's really easy even after my course when I tell
*  them don't do it don't do it and here's why I still get you know we get this all
*  the time but it's really hard to get to design good measures. When you're doing
*  prediction everything is just at the measurement level nobody cares about
*  constructs. So if you're if you have a bunch of different measures that you're
*  considering to use for a construct and some of them predict much better when
*  you put it in your model let's say you want to again let's say satisfaction
*  and you can measure it by a person's self-reported satisfaction level on a
*  scale of 1 to 10 or by their neuro behavior right that you're measuring or
*  by how often they're smiling on the you know on the video or whatever it is you
*  have all these different measures and you find that some of these have much
*  better predictive power it helps you design better measures. So again this is
*  kind of using the predictive predictive theory to try and help you develop
*  measures kind of taking it back into the psychometrics. I mean is this this is
*  related to generating new theories it seems like. Well theories are at the
*  construct level but then you have to somehow move the the theoretical thing
*  into the world of measurement and I think this is this is foreign to people
*  who don't do social science because when you're doing you know I'm guessing
*  neural is like medicine you're just measuring heart rate heart rate is heart
*  not abstracting it as you know health of the heart right. So the minutes you
*  you think in constructs and your theories are at the construct level you
*  have another layer which is measurement. So that's another very useful thing
*  where predictive models come in is developing the measures. We talked about
*  comparing theories so you know there are fields where you have competing theories
*  and they've been there for a long time fighting fighting in communities of
*  researchers saying no this is right no this is right and until you can actually
*  generate predictions sometimes it's very hard because both of them can explain
*  everything. This is this is big in the neuroscience world as well so and this
*  is directly relates. Yes and of course you could do things like improving
*  theory so a very low-hanging kind of thing to do is you know when you're
*  using predictive models and they're more flexible a lot of times it's because
*  they're maybe adding more interaction terms like if you're using trees instead
*  of regression models the tree is kind of looking through all the possible
*  interactions and finding stuff for you and interactions have a very important
*  meaning in theory because if you find that things interact it can mean that
*  one thing is moderating the other thing it can mean that they're both there are
*  different ways to interpret what it means but that can actually add to the
*  theory itself. If you know that a certain mechanism works differently during day
*  and night and the predictive model picked up on the day and night and you
*  never thought about it yourself then that helps you develop your theory. So
*  there's so many things I mean assessing predictability or evaluating how
*  predictable this phenomenon that you're even looking at that's fundamental I
*  mean think about finance if they would be a little more humble and test their
*  models in terms of is it every is it really predictable what you're trying to
*  predict? They don't need to. Exactly so it's either you have your confidence or
*  hubris or you actually evaluate whether it's even predictable because if you
*  look you know I can predict with a small no problem but if you look at the
*  prediction accuracy and you think about the practical meaning of the accuracy
*  it's like not practically meaningful then what's the whole point? What is the
*  whole point? So you have to be honest about the predictability of what you're
*  doing sometimes it doesn't matter but at least just tell me so we know where
*  things are. These are so interesting I mean it's you know as I'm looking at the
*  know I'm thinking like how you know I've got to apply this to the deep learning
*  and neuroscience world and so it's a lot to think about how you know how to apply
*  these different types of uses for prediction so I think this is really
*  useful and I mean you go through these more in-depth in the paper as well so of
*  course I'll you know be pointing people in both papers actually so I'll be
*  pointing to both of those papers you know you talk about different ways I
*  think in the paper you use four different ways that prediction and
*  explanation their difference manifests but I now I think you're up to 15 or 16
*  is that no no no no okay you're right in that you're right in the direction
*  but your quantity okay okay so initially I really kind of map these four aspects
*  and over time actually it pretty quickly started hitting me but it was too late
*  right the paper was out I realized there was a fifth one that was fundamentally a
*  huge difference it doesn't have to be one this fifth dimension doesn't have to
*  be a differentiator but it is and it might change later on but here it is so
*  so let me start from the first four yeah the four that I talk about in the in the
*  paper these are aspects that help you distinguish that are there have
*  different weights in explanation versus in prediction and when I'm saying
*  explanation now I'm the meaning that I am referring to is the causal explanation
*  if X is going to happen then is if X happens is that going to cause why and by
*  different weights you just mean it's not it's not a black and white binary
*  explanation is related to X whereas prediction is related to X yes exactly
*  so for example the first aspect is theory versus data and you can have a
*  whole spectrum of how much you rely on theory versus how much you rely on data
*  when you're doing explanatory work you're relying very heavily on theory you
*  start from theory that's built out of you know domain previous knowledge
*  everything is very theory driven and then you use the data to test your
*  theories right so the data is used as a helper in a sense and if something weird
*  is happening you're gonna say something's weird about the data whereas
*  when you're doing prediction you're a lot more heavy on the data side and you
*  of course you're not just closing your eyes and putting every data that you can
*  into the story but your theories are your theory is brought in in a less
*  formal way it's your domain knowledge is kind of things oh yeah we know that
*  this should be in the model we should measure those and put them in them all
*  but it's less formal so that is one aspect that will make predictive models
*  very different from explanatory models your starting point is just completely
*  different and how much theory and how much data is in there it's a good one
*  to start off with because I think that the data has obviously exploded it's
*  changed a lot in the past ten years you know with the rise of big data so
*  data has maybe taken on a more important role and I don't do you see
*  that as having helped the rise of predictive models in various domains just
*  the availability of data because previously data was kind of scant right
*  so you had to build an explanatory model and you had a few data points to throw
*  in there and see if it can confirm the model or you know helped explain whether
*  the model was correct whereas now we have all this data we can just throw the
*  data at it and see what happens do you see that as being a factor well first
*  of all of course I mean without the data you can't do all the predictive stuff
*  that's going on right now sure so so I'm sure that I absolutely agree that you
*  know having all this data right now is is making prediction possible in ways
*  that was totally not possible before both in terms of the richness of the
*  data and in terms of the amounts of the data and most importantly the fact that
*  the data is now structured in a way in databases in ways that support the
*  analytical work because even you know years and years ago you had telecoms and
*  you had banks they had tons of data but a lot of it was not in a in a place that
*  you could actually use to do to do the analysis on paper well in boxes it was
*  in boxes and even when it was digitized it was it was in silos right you couldn't
*  put things together so so technology has definitely made a big difference in that
*  whether theory is playing less or more again you kind of have to separate what's
*  going on in industry and what's going on in academia the time frames and this the
*  the deadlines and the goals in both places are completely different and not
*  relying on theory is is a very short-term thinking nobody says that you
*  have to stick with theories forever theory the whole idea of science is that
*  theories evolve and get better but forgetting about theories you know like
*  the wired and saying oh they're useless it's kind of a cool and you know Silicon
*  Valley to say that and I used to be very you know it's very nice in there but
*  it's not long-term thinking and it's not deep thinking what's the wired you meant
*  you referenced the wired the wired editor who wrote about the end of the
*  theory oh I didn't know that oh yeah that was a very famous debunking of
*  theory we have so much data now there's no point you don't need theory no need
*  it's actually standing in the way you know so so the reason these arguments
*  come up is because in many times people get fall so much in love with a theory a
*  community of research is so in love with a theory that they can't see beyond
*  their theory and that is a problem but it doesn't mean that theory doesn't have
*  value theory forces you to go slowly to test it out by in lots of ways in lots
*  of scenarios by lots of you know if it's different groups over time and
*  different so you have to have something there if you're just gonna move along
*  with the data and move with the tide sure but I mean as humans we don't really
*  wake up in the morning and just think what's gonna happen in the next minute
*  and not care about the rest we can't really do very well about the rest but
*  we care about the rest so if we care about the rest I think theory has a role to play
*  sounds lovely though to not really have to think about it yes it's easy you can just
*  write your code that's right all right well so good so that's the theory data
*  that's the first one right okay the second one is is is almost obvious it's
*  causation versus association and you have this whole spectrum and again you know
*  you have things that are more strongly causal and a little less and less a
*  how much confidence you have in your causality until you say no you know all I care about is
*  just correlations and predictive models will work just fine as long as correlations are there they
*  don't care about causality sometimes you don't even I mean you don't need the causality it
*  doesn't help you to get better predictions in the short term within the context that you are right
*  so prediction is a very kind of context dependent animal and if that's what you want to do
*  association or your friend so all kinds of things like you know statisticians love really
*  complicated words that are long and hard to spell so multicollinearity is like a curse word
*  in statistics it's where you have a bunch of inputs that are highly correlated and when they're
*  highly correlated it messes up some of the standard errors and whatever and there's like
*  methods to detect them and to remove them this is like you know cancer it's it's serious but if
*  you're trying to do prediction multicollinearity doesn't really matter much if you don't if you
*  don't unless you want to extrapolate beyond your input sphere it doesn't matter so all this extra
*  efforts and whatever they're they're kind of useless it's not really good so the kinds of
*  efforts that you would put into modeling in a predictive model would be different than the type
*  of efforts that you would put in when you're doing causal stuff for example here's a here's a different
*  thing when you're doing causal modeling you care very much because it's causal the inputs have to
*  happen before the outputs in terms of the causal chain you have to be really careful in terms of
*  not putting anything else that influence the inputs into the output right then you get something
*  called reverse causality and again in this is econometricians are amazing at this they're so
*  careful at looking at each variable that they have and thinking carefully whether there's something
*  that could have affected in this way or the other but when you're doing prediction you don't care
*  what you care is that at the time of prediction all those input variables are available if those
*  inputs are available at the time of prediction i couldn't care less how they led to the outcome
*  if something else was causing both of them i do not care so that's why you have this really
*  different set of decisions that you make when you're building a predictive model than a causal one
*  is not there's not one truth it's just utilitarian what do you want to do based on that here's your
*  path here are the things that you have to worry about so that's the causation versus association
*  and it's kind of funny because uh you know um you have this mantra that statisticians always say
*  association is not causation yeah yeah and right they say association is not causation
*  yes well we relation is not causation yes we always yeah relation is not and it's true it one
*  does not infer the other but nobody really ever i mean thinks that in disciplines where they
*  where they're using correlation and making causal statements it's usually because there's a theory
*  that states the causal thing and the correlation is just quantifying it it's interesting i just
*  got an email last night from a medical doctor in the states asking me exactly about this you know
*  i read your paper and i'm just wondering if i'm just trying to to build a descriptive model and
*  i and i i just care about which inputs are correlated with the outputs is it okay to do
*  this and that so you know obviously the answer is always what do you mean is it okay what are
*  you trying to do with this model at the end is it okay what is the final goal the the patient is
*  on the gurney right now what should i yeah is it okay that's you must get those emails all the time
*  i do yeah i do i do i do but again it's very interesting because it lets me see what's
*  happening in a field yeah how people are thinking about it um we wrote this little paper uh i did a
*  collaboration it's a short paper that i did with a physical therapist researcher after we got a
*  request from an editor to write some editorial piece and we went through it we went through it
*  four times four rounds eventually it didn't go anywhere and i said you know what we did such
*  an interesting piece here about using prediction for doctors basically what they can do if you
*  don't know much and whatever i just i just posted it i think on archive ssrn or archive one of them
*  i think on ssrn maybe that's like the social it's the equivalent of the social science because these
*  emails these contacts that i get you know they open they open an important question in a field
*  that stuck on either explanation or prediction and by just giving a little nugget out there
*  of saying here's how to get started with with what you with what you have right now and this
*  little collaboration you know that we did i think those are the important opportunities to actually
*  spread the knowledge so talks are one thing but these emails are or personalized um into fields
*  yeah but that's a lot of emails either way it is it is some of them i can't answer of course yes
*  well okay so we're into the second one right so the third one is um a retrospective to prospective
*  that is almost intuitive once you say that because when you're doing prediction you're
*  usually looking forward not always but you're usually looking forward you're trying to predict
*  something in the future so everything that you're doing in the modeling process has to mimic
*  that thought you kind of have to simulate that moment of deployments where you're going to use
*  the model to predict and every decision that you make will have to be based on do i have the same
*  information that i will have at the time of deployment will things change or not versus
*  when you're doing explanatory or even descriptive modeling you're looking retrospectively you're
*  just trying to find some kind of relationship between the outputs and inputs and you're not
*  necessarily going to project that into the future you're trying to learn some kind of a i don't want
*  to use the very loaded word truth but some kind of a relationship that's useful to you
*  and in that sense because it's retrospective it allows you to do a lot more things that you cannot
*  do in a perspective case for example um you can use information that's known after the output
*  happens so again when i go back to the online auctions example if i wanted to predict the or
*  create a model that captures the relationship between the price and some inputs the number of
*  bidders is a critical input in all game theory you know the more bidders you have the price goes up
*  but if you're looking at an ebay auction you don't know the number of bidders until the auction's
*  closed so i couldn't use number of bidders as an input in a prediction model but i'm allowed to
*  use it as an explanatory because if i'm in the middle of the auction i don't know how many
*  of an individual auction but you could you could predict on average who wants it on average well
*  yeah that's true it's kind of useless for that i suppose yeah you actually just you actually just
*  exactly hit on the fifth dimension i mean we skipped the fourth one but sure the fifth one
*  that i added is exactly this the difference between the average observation and the individual
*  observation so when you're doing prediction and that's just how things are today it doesn't have
*  to be that way prediction is typically done at the individual you're trying to personalize right
*  you're trying to predict what's going to be the outcome for this person or for this transaction
*  or so everything and prediction is geared towards individual prediction you're using your model
*  and you're scoring or you're deploying it to individual observations and then you're
*  accumulating the mistakes and tuning based on that but everything that's done in the descriptive and
*  explanatory world is geared towards the average observation so on average three units increase
*  and blah blah blah will increase you know everything there is about the average because
*  you're trying to learn a story about a population and that's very different it's totally different
*  and now it's as i said i mean this is kind of what's i'm just mapping i'm telling you this is
*  the normative thing of what's going on but it doesn't have to be like that because even when
*  you look inside the prediction world and this is something that i i'm just waiting for this to sort
*  of start breaking out big it's in little pockets you can sometimes when you're doing prediction
*  it's really because the decisions that will happen based on those predictions are individualized
*  so if i'm predicting different outcomes for different people i will treat them in different
*  ways pay personalized treatment but in some cases those predictions are not really going to lead to
*  that they're going to lead to just one policy change yes we're allowing we're going to do a
*  monetary uh i don't know uh let's not say things like that now right let's just change a big policy
*  and this policy is going to affect everyone we're going to quarantine everyone or not quarantine
*  everyone maybe i build a predictive model for that but it will be used in a in an aggregate way
*  right because you do have policy problems like that yeah and and the way you measure the way
*  you measure performance and the way you tweak the models should actually be totally different
*  totally different but right now we have one way of doing things in the world of prediction it's
*  rms e and confusion matrices and recalling yeah so um i mean you know as you're going through these
*  you know i'm just thinking like every one of them so far i'm thinking the deep learning and
*  could could do either of these could go could the goal of a deep learning model could be for either
*  of these cases so you know in this average versus individual case you you can see it we each uh each
*  one of us has an individual model of our brains and it's you know this big network right of
*  artificial neurons all interacting but if we really want to if we honor want to understand
*  how taste works for instance then we wouldn't be modeling individual individual brains for predicting
*  you know how their taste buds would react we would model on average we'd make a model to understand
*  how taste works in general so it's so much to think about just going down this list and thinking how
*  okay you could approach it in this theory way or you could approach it in this data way you could
*  approach it in the retrospective way or the explaining or prospective predicting what the
*  units are going to be doing so i realize i'm just blathering on here but um each one of these it's
*  really interesting to think about how deep learning neural networks can be used in the domain of
*  neuroscience so um so there is one more it's the bias variance uh difference here and that's that's
*  the one that um you know most statisticians and machine learning people get most excited about
*  yeah yeah and typically they think oh yeah yeah that's the difference um so so that's the one
*  that's most um developed theoretically and you know you can write it out you can write out equations
*  and show that um when you're trying to do when you're doing explanation it's all about the bias
*  and you care about the bias and you'll do whatever you can over parameterization is less of a problem
*  because you know you put in an extra thing and it's supposed to be zero it will just be
*  it doesn't bother you but when you're doing prediction that really matters and then the
*  variance also matters so you try in prediction to balance both bias and variance whereas an
*  explanation it's only about the bias in description it's usually also this bias variance together
*  which is kind of interesting um and i think a lot of these uh and again the questions that i'm getting
*  by emails is sometimes is about model selection variable selection you know things like stepwise
*  in regression or lassoes or any kind of regularization where you have many inputs
*  and you're trying to reduce them and in if you look at classic papers in econometrics or people
*  doing econometrics in other fields you'll see for example if they do a regression model they will
*  run the regression model and they'll show you results of the regression model with all the
*  inputs with some of the inputs with a few less they have like what they call like the long
*  regression and then shorter regressions and as a statistician when you look at this and you say
*  what no but they have these things that are statistically insignificant they should remove
*  them this is what they teach us in statistics it's a different approach because um the the
*  inputs that they choose and leave in there maybe they're not statistically significant but they're
*  theoretically supposed to be there so they want to show me that the theory says they're supposed to
*  be here but look at how small they are look at how meaningless they are or whatever so so this idea
*  of bias and variance it's it's you can write it out but there's also a lot of there's also a
*  lot of domain level justification you have to think about it also from a more domain point of
*  view the other thing that comes up with bias variance is using all kinds of regularized
*  methods and that's why you'll see them more being used in predictive places so if you're using the
*  deep learning and it has regularization on and everything and of course it's not interpretable
*  to start with that makes total sense for prediction and for description but it's not
*  going to make any sense for explanation because think about it this way suppose you have these
*  two inputs and both of them are measuring the construct that you really care about but one of
*  them is not measured as well as the other because of your measurement tools or something like that
*  and you're regularizing who's going to get dropped out so you just lost a really important piece of
*  information so for prediction it's good yeah great right for describing you just reduce the bias
*  variance but from your domain point of view you lost something useful and interesting and that's
*  why this this trade-off of how you do variable selection and why some things work better for
*  prediction and not well for explanation is is a different you need a different approach
*  yeah it's so i mean there's just so much to uh so much to consider it's too much to consider really
*  yes i know one way in which it is suggested that artificial neural networks can be used
*  is as in an exploratory uh mode so i mean basically like you know if you don't have a
*  good theory on something you can use your your model as a toy and explore uh throughout and that
*  sounds to me almost like it falls under the predictive modeling uh umbrella i mean do you see
*  exploration itself as a valid modeling goal um i i i think that again you have to sort of tell me
*  what is the what are you going to do with it what do you mean by exploration are you trying to find
*  how certain inputs so correlate with a certain output or what are you trying to do yeah so so i
*  guess in the case of deep learning models there isn't a good theory to begin with so i think that
*  it would be in the service of generating hypotheses right so you you know you run your model you look
*  at the data uh maybe then you take out half the units and run the model and you look at the data
*  and see but but in that regime it's basically acting as a predictive model uh because then
*  you're going to be matching the data that the model generates to the data that you recorded
*  in a brain for instance so why is that not a descriptive goal i mean if if the end goal is to
*  build a theory of prediction then maybe you're predicting but if you're just trying to find what
*  kind of configurations you know have a a good let's say i don't know why you're measuring it low rms
*  ease or whatever yeah then it could be just a descriptive model it doesn't unless you're doing
*  holdout data and you're caring about what's happening when you're training the data on some
*  part you're training your model on some part and how well it works on a different part
*  then it would be about out of sample and about prediction but if you're just trying to build a
*  model that's descriptive and you don't care so much maybe about i don't know a prediction it
*  could be descriptive see i mean uh you mentioned my book uh on information quality and this work
*  that i did with ron kennett started from from from something very naive that's very relevant here as
*  well so information quality the idea of this uh concept that we came up with was that whenever
*  you're doing data analysis there are actually four components going on and they're very tightly
*  coupled and in order to determine how much information is available in a certain data
*  set in order to answer your question which is what an analysis is about right you have data
*  you've got a question you want to answer you want to answer it you have to sort of figure out a
*  bunch of things so the four components that we have in there are you have your goal you have your
*  data you have the set of analysis that are in your world in your case for example you're saying the
*  deep learning methods right and then you have a utility measure your performance measures
*  and in order to tell you whether you know you're going to give me this data set and whether there's
*  any information is there any quality in the information in that data set i need to know
*  all these four things and in order to specify all of these there's like a checklist of questions so
*  when you say i want to explore it's like no you don't want to explore what are you going to do
*  with exploration i'm going to take you down and pin you to the wall until i know what you want to
*  do with this at the end so i don't think the word exploration in itself is a modeling goal i think
*  it's maybe you're describing what you're planning to do but not what is the goal
*  of course yeah okay i can agree with that so i'm going out i'm going outside in taipei
*  and you're telling what's your goal i'm not going to say oh i'm just exploring it's like no i want
*  to find new places or um i want to see people you know or i want to see a place i've not seen
*  before so there needs to be a goal um implicit yeah maybe goal was the the wrong uh terminology
*  to use maybe the means as an end would be a better way to phrase it perhaps i mean okay
*  in a sense this is the way science generally really works anyway when you get down to it is we're all
*  exploring you can talk about your highfalutin theory as much as you want and the way you're
*  going to analyze your data but then on a day-to-day basis often you're just in there and you're getting
*  comfortable with the data because you have to understand the data seeing what you can do and
*  then that helps you form the theory and you know it's all circular of course and feeds into each
*  other totally totally i agree with you and that's a whole uh like a gray shadow area of how we do
*  research we actually spend most of their time uh like getting familiar with the data exploring
*  it for sure but that's usually not i mean try and publish that stuff that's not the publishable stuff
*  right because that's your homework so you're doing all your homework and you get to know the data set
*  and the field really well and actually you're very right i think that many times when i looked at data
*  that's when some weird stuff comes up and you say hold on a second we had no idea you know maybe
*  this whole thing that we were thinking about that's the wrong question to ask we should be
*  asking a totally different question so i think you're right that's what actually happens that's
*  the engine that runs behind the scenes um but i don't think it's stated as such i think that
*  is really the the back end that's the backstage of what we do sure and i that's why also you know
*  data visualization i i think that's like one of the most important things you can do much more
*  than the modeling uh you know you have a deep neural net fine everything but if you kind of
*  get a feel of looking at stuff and then see why things are working um that helps and that's the
*  part that you were saying before about our needs to explain things in a language that we understand
*  or we think we understand we think we understand well we're just about out of time let me ask one
*  more question about prediction and explanation here and so in science there's this sort of
*  glorified loop right that you have a theory you make a model you know uh then you do an experiment
*  you get the data and you test it against the model and then you use that to tweak the model and use
*  that to tweak the theory and then you make a new experiment and on and on and on and i'm wondering
*  if given the difference between prediction and explanation if if uh you see them as
*  accommodating this sort of back and forth so you make this beautiful predictive model and then you
*  generate new hypotheses and then you change your use that to make a better explanatory model
*  and then you can use the explanatory model to make a better predictive model and back and forth is
*  that a feasible way of going about things um i definitely think that's that's um probably the
*  best way to do things i think we're not really there it would be really important to go there i
*  think that's the whole point of the paper you know that i did was in order to do anything scientific
*  you have to have both components if you're lacking one of them you're just stumbling in place um so i
*  think what you described is correct i think that you're starting i don't know where you started
*  depends which field you're in but you're in the loop now and then you're building your theories up
*  and then you're building predictive models and the predictive models are telling you new stuff and
*  you have to update your theories and you keep going back and forth and again this is when we're
*  talking about science development we're not talking about necessarily applications yeah in
*  applications you have also a circular thing but it's a little bit different but if you really
*  want to answer the the how and the and the why not just the what's right the how and the why
*  i think that is the circle and in fact you know if you take it back to the brain which is your
*  favorite organ um i think that's kind of what our brain is doing anyways you know you asked me once
*  about um about how the brain works and i don't know i'm not a neuroscientist i can just tell you
*  what my personal theory is right right now and that is we're we're creating these predictions
*  all the time the the brain is processing what's going on you know whether it's your memory whether
*  it's what's happening around you it's processing and immediately creating these predictions so that
*  you can act in the world can you you can react and you can act and you can interact but immediately
*  the minute you do this unconscious thing which i think is unfortunately it took me a long time
*  to figure out it's unconscious um the moment it happens you also produce an explanation of why
*  post-hoc all the time yeah all the time so we're constantly making up these stories now
*  why we're making up these stories i mean they're theories i guess you can ask different people
*  what happens before and what you know i think it's a loop as well so you've created your story and
*  that story adds to your memory and adds the way you're framing things and affects your predictions
*  and and it just keeps going on so whether science is trying to mimic what the brain is doing because
*  that's what we feel comfortable with we need the explanations we can't live without them
*  it's a good question yeah maybe we're stuck in our own head cycle but we can only produce the way
*  that our brain actually works mechanically anyway right yes maybe it's the time to ask the heavy
*  meditators maybe they can free us out of the scientific of you know circle of death no don't
*  bother the meditators let them meditate it actually works pretty well it's a good thing
*  for a scientist to meditate i can tell you that it gives you a lot of insights as well
*  yeah yeah all right gali well i really appreciate your time i know i've taken you over a minute or
*  two here now but but thank you for the insight thanks for the paper and i wish you continued
*  success moving forward and um hope maybe one day you'll not have to be talking about explain or
*  predict thank you very much i hope that the we'll hear a lot of interesting other podcasts coming
*  from your side and now we'll be talking about explaining and predicting that would be pretty
*  interesting thanks gali okay bye bye brain inspired is a production of me and you you can support the
*  show through patreon for a microscopic two or four dollars per month go to brain inspired dot co and
*  find the red patreon button there your contribution will help sustain and improve the show and
*  prohibit any annoying advertisements like you hear on other shows to get in touch with me email
*  paul at brain inspired dot co the music you hear is by the new year find them at the new year dot
*  net thanks for your support see you next time
*  oh
*  you trust the sky
*  you must like your lies
*  you
