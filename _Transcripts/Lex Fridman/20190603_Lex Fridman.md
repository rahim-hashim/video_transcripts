---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 4258s
Video Keywords: []
Video Views: 37309
Video Rating: None
---

# Rajat Monga: TensorFlow | Lex Fridman Podcast #22
**Lex Fridman:** [June 03, 2019](https://www.youtube.com/watch?v=NERNE4UThHU)
*  The following is a conversation with Rajat Manga.
*  He's an engineer and director at Google, leading the TensorFlow team.
*  TensorFlow is an open source library at the center of much of the work going on in the world in deep
*  learning, both the cutting edge research and the large scale application of learning-based approaches.
*  But it's quickly becoming much more than a software library.
*  It's now an ecosystem of tools for the deployment of machine learning in the cloud,
*  on the phone, in the browser, on both generic and specialized hardware.
*  TPU, GPU, and so on.
*  Plus, there's a big emphasis on growing a passionate community of developers.
*  Rajat, Jeff Dean, and a large team of engineers at Google Brain are working to define the future
*  of machine learning with TensorFlow 2.0, which is now in alpha.
*  I think the decision to open source TensorFlow is a definitive moment in the tech industry.
*  It showed that open innovation can be successful and inspire many companies to open source their
*  code to publish and in general engage in the open exchange of ideas.
*  This conversation is part of the Artificial Intelligence podcast.
*  If you enjoy it, subscribe on YouTube, iTunes, or simply connect with me on Twitter
*  at Lex Friedman, spelled F-R-I-D.
*  And now here's my conversation with Rajat Manga.
*  You were involved with Google Brain since its start in 2011 with Jeff Dean.
*  It started with this belief, the proprietary machine learning library,
*  and turned into TensorFlow 2014, the open source library.
*  So what were the early days of Google Brain like?
*  What were the goals, the missions?
*  How do you even proceed forward when there's so much possibilities before you?
*  It was interesting back then, when I started or when you were even just talking about it.
*  The idea of deep learning was interesting and intriguing in some ways.
*  It hadn't yet taken off, but it held some promise.
*  It had shown some very promising and early results.
*  I think that the idea where Andrew and Jeff had started was,
*  what if we can take this, what people are doing in research,
*  and scale it to what Google has in terms of the compute power,
*  and also put that kind of data together, what does it mean?
*  And so far the results have been, if you scale the compute, scale the data,
*  it does better, and would that work?
*  And so that was the first year or two, can we prove that out?
*  And with this belief, when we started the first year, we got some early wins,
*  which is always great.
*  What were the wins like?
*  What were the wins where you were, there's some problems to this, this is going to be good?
*  I think there are two early wins where one was speech,
*  that we collaborated very closely with the speech research team,
*  who was also getting interested in this.
*  And the other one was on images where we, you know, the cat paper, as we call it,
*  that was covered by a lot of folks.
*  And the birth of Google Brain was around neural networks.
*  That was, so it was deep learning from the very beginning.
*  That was the whole mission.
*  So what would, in terms of scale, what was the sort of,
*  sort of dream of what this could become?
*  Were there echoes of this open source TensorFlow community that might be brought in?
*  Was there a sense of TPUs?
*  Was there a sense of like machine learning is not going to be at the core of the entire company,
*  is going to grow into that direction?
*  Yeah, I think so that was interesting.
*  And like, if I think back to 2012 or 2011, and first was, can we scale it in the year or so,
*  we had started scaling it to hundreds and thousands of machines.
*  In fact, we had some runs even going to 10,000 machines.
*  And all of those shows great promise.
*  In terms of machine learning at Google,
*  the good thing was Google has been doing machine learning for a long time.
*  Deep learning was new.
*  But as we scale this up, we showed that yes, that was possible.
*  And it was going to impact lots of things.
*  Like we started seeing real products wanting to use this.
*  Again, speech was the first.
*  There were image things that photos came out of and then many other products as well.
*  So that was exciting.
*  As we went into with that a couple of years, externally also academia started to,
*  there was lots of push on, okay, deep learning is interesting,
*  we should be doing more and so on.
*  And so by 2014, we were looking at, okay, this is a big thing.
*  It's going to grow.
*  And not just internally, externally as well.
*  Yes, maybe Google's ahead of where everybody is.
*  But there's a lot to do.
*  So a lot of this stuff to make sense and come together.
*  So the decision to open source, I was just chatting with Chris Glattner about this.
*  The decision to go open source with TensorFlow,
*  I would say for me personally, it seems to be one of the big seminal moments
*  in all of software engineering ever.
*  I think that's when a large company like Google decides to take a large project
*  that many lawyers might argue has a lot of IP.
*  Just decide to go open source with it.
*  And then so doing lead the entire world and saying, you know what, open innovation
*  is a pretty powerful thing and it's okay to do.
*  That was, I mean, that's an incredible moment in time.
*  So do you remember those discussions happening?
*  Whether open source should be happening?
*  What was that like?
*  I would say, I think, so the initial idea came from Jeff,
*  who was a big proponent of this.
*  I think it came off of two big things.
*  One was research-wise, we were a research group.
*  We were putting all our research out there.
*  We were building on all this research and we wanted to push the state of the art forward.
*  And part of that was to share the research.
*  That's how I think deep learning and machine learning has really grown so fast.
*  So the next step was, okay, now would software help with that?
*  And it seemed like they were existing a few libraries out there,
*  Tiano being one, Torch being another, and a few others.
*  But they were all done by academia and so the level was significantly different.
*  The other one was from a software perspective,
*  Google had done lots of software that we used internally, you know, and we published papers.
*  Often there was an open source project that came out of that,
*  that somebody else picked up that paper and implemented and they were very successful.
*  Back then it was like, okay, there's Hadoop, which has come off of tech that we've built.
*  We know the tech we've built is way better for a number of different reasons.
*  We've invested a lot of effort in that.
*  And turns out we have Google Cloud and we are now not really providing our tech,
*  but we are saying, okay, we have Bigtable, which is the original thing.
*  We're going to now provide HBase APIs on top of that, which isn't as good,
*  but that's what everybody's used to.
*  So there's like, can we make something that is better and really just provide,
*  helps the community in lots of ways, but also helps push the right, a good standard forward.
*  So how does cloud fit into that?
*  There's a TensorFlow open source library and how does the fact that you can
*  use so many of the resources that Google provides and the cloud fit into that strategy?
*  So TensorFlow itself is open and you can use it anywhere, right?
*  And we want to make sure that continues to be the case.
*  On Google Cloud, we do make sure that there's lots of integrations with everything else.
*  And we want to make sure that it works really, really well there.
*  So you're leading the TensorFlow effort.
*  Can you tell me the history and the timeline of TensorFlow project
*  in terms of major design decisions?
*  The open source decision, but really what to include and not.
*  There's this incredible ecosystem that I'd like to talk about.
*  There's all these parts, but if you just some sample moments
*  that defined what TensorFlow eventually became through its,
*  I don't know if you were allowed to say history when it's just,
*  but in deep learning everything moves so fast in just a few years is already history.
*  Yes.
*  Yes. So looking back, we were building TensorFlow.
*  I guess we open sourced it in 2015, November 2015.
*  We started on it in summer of 2014, I guess.
*  And somewhere like three to six late 2014, by then we had decided that,
*  okay, there's a high likelihood we'll open source it.
*  So we started thinking about that and making sure we're heading down that path.
*  At that point, by that point we had seen a few,
*  lots of different use cases at Google.
*  So there were things like, okay, yes, we want to run in at large scale in the data center.
*  Yes, we need to support different kinds of hardware.
*  We had GPUs at that point.
*  We had our first TPU at that point was about to come out roughly around that time.
*  So the design sort of included those.
*  We had started to push on mobile.
*  So we were running models on mobile.
*  At that point, people were customizing code.
*  So we wanted to make sure TensorFlow could support that as well.
*  So that sort of became part of that overall design.
*  When you say mobile, you mean like pretty complicated algorithms running on the phone?
*  That's correct.
*  So when you have a model that you deploy on the phone and run it there.
*  At that time, there was ideas of running machine learning on the phone.
*  That's correct.
*  We already had a couple of products that were doing that by then.
*  In those cases, we had basically customized handcrafted code
*  or some internal libraries that we're using.
*  I was actually at Google during this time in a parallel universe,
*  but we were using Theano and Cafe.
*  Was there some degree to which you were balancing,
*  trying to see what Cafe was offering people,
*  trying to see what Theano was offering
*  that you want to make sure you're delivering on?
*  Whatever that is, perhaps the Python part of things.
*  Maybe did that influence any design decisions?
*  Totally.
*  So when we built this belief and some of that was in parallel
*  with some of these libraries coming up, Theano itself is older.
*  But we were building this belief focused on our internal thing
*  because our systems were very different.
*  By the time we got to this, we looked at a number of libraries
*  that were out there.
*  Theano, there were folks in the group who had experience with Torch, with Lua.
*  There were folks here who had seen Cafe.
*  I mean, actually, Yang Jing was here as well.
*  There's what other libraries?
*  I think we looked at a number of things.
*  Might even have looked at Jane Eyre back then.
*  I'm trying to remember if it was there.
*  In fact, we did discuss ideas around, okay, should we have a graph or not?
*  So putting all these together was definitely,
*  there were key decisions that we wanted.
*  We had seen limitations in our prior disbelief things.
*  A few of them were just in terms of research was moving so fast.
*  We wanted the flexibility.
*  The hardware was changing fast.
*  We expected to change that so that those probably were two things.
*  I think the flexibility in terms of being able to express all kinds of crazy things
*  was definitely a big one then.
*  So what the graph decisions?
*  So now with moving towards TensorFlow 2.0, there's more, by default, it'll be eager execution.
*  So sort of hiding the graph a little bit because it's less intuitive in terms of
*  the way people develop and so on.
*  What was that discussion like in terms of using graphs?
*  It's kind of the theano way.
*  Does it seem the obvious choice?
*  So I think where it came from was our disbelief had a graph-like thing as well.
*  It wasn't a general graph.
*  It was more like a straight line thing.
*  More like what you might think of Cafe, I guess, in that sense.
*  But the graph was, and we always cared about the production stuff.
*  Even with disbelief, we were deploying a whole bunch of stuff in production.
*  So the graph did come from that when we thought of, okay, should we do that in Python?
*  And we experimented with some ideas where it looked a lot simpler to use,
*  but not having a graph meant, okay, how do you deploy now?
*  So that was probably what filtered the balance for us.
*  And eventually we ended up with a graph.
*  And I guess the question there is, did you, I mean,
*  so production seems to be the really good thing to focus on.
*  But did you even anticipate the other side of it where there could be,
*  what is it?
*  What are the numbers?
*  Something crazy.
*  41 million downloads.
*  I mean, was that even like a possibility in your mind that it would be as popular as it became?
*  So I think we did see a need for this a lot from the research perspective
*  and early days of deep learning in some ways.
*  41 million?
*  No, I don't think I imagined this number then.
*  It seemed like there's a potential future where lots more people would be doing this
*  and how do we enable that?
*  I would say this kind of growth, I probably started seeing somewhat after the open sourcing,
*  where it was like, okay, deep learning is actually growing.
*  We're faster for a lot of different reasons.
*  And we are in just the right place to push on that and leverage that
*  and deliver on lots of things that people want.
*  So what changed once you open source?
*  Like how, you know, this incredible amount of attention from a global population of developers,
*  how did the projects start changing?
*  I don't even actually remember during those times.
*  I know looking now, there's really good documentation.
*  There's an ecosystem of tools.
*  There's a community blog, there's a YouTube channel now, right?
*  It's very community driven.
*  Back then, I guess 0.1 version.
*  Is that the version?
*  I think we called it 0.6 or 5, something like that.
*  I forget what that is.
*  What changed leading into 1.0?
*  It's interesting.
*  I think we've gone through a few things there.
*  When we started out, when we first came out, people loved the documentation we have
*  because it was just a huge step up from everything else
*  because all of those were academic projects, people doing, you know,
*  would don't think about documentation.
*  I think what that changed was instead of deep learning being a research thing,
*  some people who were just developers could now suddenly take this out
*  and do some interesting things with it, right?
*  Who had no clue what machine learning was before then.
*  And that, I think, really changed how things started to scale up in some ways.
*  And pushed on it.
*  Over the next few months, as we looked at, you know, how do we stabilize things?
*  As we look at not just researchers, now we want stability.
*  People want to deploy things.
*  That's how we started planning for 1.0.
*  And there are certain needs for that perspective.
*  And so again, documentation comes up, designs, more kinds of things to put that together.
*  And so that was exciting to get that to a stage where
*  more and more enterprises wanted to buy in and really get behind that.
*  And I think post 1.0 and, you know, with the next few releases,
*  that enterprise adoption also started to take off.
*  I would say between the initial release and 1.0, it was, okay, researchers, of course.
*  Then a lot of hobbies and early interest people excited about this
*  who started to get on board.
*  And then over the 1.x thing, lots of enterprises.
*  I imagine anything that's below 1.0 gets pressure to be enterprise problem or something that's stable.
*  Exactly.
*  And do you have a sense now that TensorFlow is safe?
*  It feels like deep learning in general is extremely dynamic field.
*  So much is changing.
*  Do you have a, and TensorFlow has been growing incredibly.
*  Do you have a sense of stability at the helm of this?
*  I mean, I know you're in the midst of it, but.
*  Yeah, it's, I think in the midst of it, it's often easy to forget what an enterprise wants
*  and what some of the people on that side want.
*  There are still people running models that are three years old, four years old.
*  So Inception is still used by tons of people.
*  Even ResNet-50 is what, a couple of years old now or more.
*  But there are tons of people who use that and they're fine.
*  They don't need the last couple of bits of performance or quality.
*  They want some stability in things that just work.
*  And so there is value in providing that with that kind of stability and in making it really simpler
*  because that allows a lot more people to access it.
*  And then there's the research crowd which wants, okay,
*  they want to do these crazy things exactly like you're saying, right?
*  Not just deep learning in the straight up models that used to be there.
*  They want RNNs and even RNNs are maybe old.
*  They are transformers now and now it needs to combine with RL and GANs and so on.
*  So there's definitely that area that, like the boundary that's shifting and pushing the state of the art.
*  But I think there's more and more of the past that's much more stable.
*  And even stuff that was two, three years old is very, very usable by lots of people.
*  So that part makes it a little easier.
*  So I imagine maybe you can correct me if I'm wrong.
*  One of the biggest use cases is essentially taking something like ResNet-50 and doing some kind of
*  transfer learning on a very particular problem that you have.
*  It's basically probably what majority of the world does.
*  And you want to make that as easy as possible.
*  So I would say for the hobbyist perspective, that's the most common case, right?
*  In fact, the apps on phones and stuff that you'll see, the early ones, that's the most common case.
*  I would say there are a couple of reasons for that.
*  One is that everybody talks about that.
*  It looks great on slides.
*  Yeah.
*  That's a big presentation.
*  Yeah, exactly.
*  What enterprises want is that is part of it, but that's not the big thing.
*  Enterprises really have data that they want to make predictions on.
*  This is often what they used to do with the people who were doing ML was just regression models,
*  linear regression, logistic regression, linear models.
*  Or maybe gradient booster trees and so on.
*  Some of them still benefit from deep learning, but they want that,
*  that's the bread and butter, like the structured data and so on.
*  So depending on the audience you look at, they're a little bit different.
*  And they just have, I mean, the best of enterprise
*  probably just has a very large data set or deep learning can probably shine.
*  That's correct.
*  That's right.
*  And then I think the other pieces that they want, again, with 2.0 or the developer summit
*  we put together is the whole TensorFlow extended piece, which is the entire pipeline.
*  They care about stability across doing their entire thing.
*  They want simplicity across the entire thing.
*  I don't need to just train a model.
*  I need to do that every day again, over and over again.
*  I wonder to which degree you have a role in, I don't know.
*  So I teach a course on deep learning.
*  I have people like lawyers come up to me and say, you know, say when is machine learning
*  going to enter legal, the legal realm?
*  The same thing in all kinds of disciplines, immigration, insurance.
*  Often when I see what it boils down to is these companies are often a little bit old school
*  in the way they organize the data.
*  So the data is just not ready yet.
*  It's not digitized.
*  Do you also find yourself being in the role of an evangelist for like,
*  let's get, organize your data folks and then you'll get the big benefit of TensorFlow.
*  Do you get those, have those conversations?
*  Yeah.
*  Yeah.
*  I get all kinds of questions there from, okay, what can I, what do I need to make this work?
*  Right.
*  Do we really need deep learning?
*  I mean, there are all these things.
*  I already use this linear model.
*  Why would this help?
*  I don't have enough data, let's say, you know, or I want to use machine learning,
*  but I have no clue where to start.
*  So it really is back to all the way to the experts who are very specific things.
*  So it's interesting.
*  Is there a good answer?
*  It boils down to oftentimes digitizing data.
*  So whatever you want automated, whatever data you want to make prediction based on,
*  you have to make sure that it's in an organized form.
*  Like within the TensorFlow ecosystem, there's now you're providing more and more data sets
*  and more and more pre-trained models.
*  Are you finding yourself also the organizer of data sets?
*  Yes.
*  I think with TensorFlow data sets that we just released,
*  that's definitely come up where people want these data sets.
*  Can we organize them and can we make that easier?
*  So that's definitely one important thing.
*  The other related thing I would say is I often tell people, you know what?
*  Don't think of the most fanciest thing that the newest model that you see.
*  Make something very basic work and then you can improve it.
*  There's just lots of things you can do with it.
*  Yeah, start with the basics.
*  One of the big things that makes TensorFlow even more accessible
*  was the appearance whenever that happened of Keras,
*  the Keras standard sort of outside of TensorFlow.
*  I think it was Keras on top of Tiano at first only,
*  and then Keras became on top of TensorFlow.
*  Do you know when Keras chose to also add TensorFlow as a backend,
*  who was the...
*  Was it just the community that drove that initially?
*  Do you know if there was discussions, conversations?
*  Yeah, so Francois started the Keras project before he was at Google.
*  And the first thing was Tiano.
*  I don't remember if that was after TensorFlow was created or way before.
*  And then at some point, when TensorFlow started becoming popular,
*  there were enough similarities that he decided to create this interface
*  and put TensorFlow as a backend.
*  I believe that might still have been before he joined Google.
*  So we weren't really talking about that.
*  He decided on his own and thought that was interesting and relevant to the community.
*  In fact, I didn't find out about him being at Google until a few years ago.
*  A few months after he was here, he was working on some research ideas
*  and doing Keras and his nights and weekends project and stuff.
*  Oh, interesting.
*  So he wasn't like part of the TensorFlow.
*  He didn't join initially.
*  He joined research and he was doing some amazing research.
*  He has some papers on that and research.
*  He's a great researcher as well.
*  And at some point we realized, oh, he's doing this good stuff.
*  People seem to like the API and he's right here.
*  So we talked to him and he said, okay, why don't I come over to your team
*  and work with you for a quarter and let's make that integration happen?
*  And we talked to his manager and he said, sure, my quarter's fine.
*  And that quarter's been something like two years now.
*  So he's fully on this.
*  So Keras got integrated into TensorFlow in a deep way.
*  And now with TensorFlow 2.0, Keras is the recommended way for a beginner to interact
*  with TensorFlow, which makes that initial transfer learning or the basic use cases,
*  even for enterprise, super simple.
*  Right?
*  That's correct.
*  That's right.
*  So what was that decision like?
*  That seems like it's a bold decision as well.
*  We did spend a lot of time thinking about that one.
*  We had a bunch of APIs, some built by us.
*  There was a parallel layers API that we were building.
*  And when we decided to do Keras in parallel, so there were like, okay,
*  two things that we are looking at.
*  And the first thing we was trying to do is just have them look similar,
*  like be as integrated as possible, share all of that stuff.
*  There were also like three other APIs that others had built over time
*  because we didn't have a standard one.
*  But one of the messages that we kept hearing from the community,
*  okay, which one do we use?
*  And they kept seeing like, okay, here's a model in this one,
*  and here's a model in this one, which should I pick?
*  So that's sort of like, okay, we had to address that straight on with 2.0.
*  The whole idea was we need to simplify.
*  We had to pick one.
*  Based on where we were, we were like, okay, let's see what are the people like?
*  And Keras was clear.
*  What are the people like?
*  And Keras was clearly one that lots of people loved.
*  There were lots of great things about it.
*  So we settled on that.
*  Organically, that's kind of the best way to do it, which it was great.
*  It was surprising, nevertheless, to sort of bring in and outside.
*  I mean, there was a feeling like Keras might be almost like a competitor
*  in a certain kind of a two-tensor flow.
*  And in a sense, it became an empowering element of TensorFlow.
*  That's right.
*  Yeah, it's interesting how you can put two things together, which can align.
*  In this case, I think Francois, the team, and a bunch of us have chatted,
*  and I think we all want to see the same kind of things.
*  We all care about making it easier for the huge set of developers out there,
*  and that makes a difference.
*  So Python has Guido Van Rossum, who until recently held the position of
*  benevolent dictator for life.
*  Right.
*  So does a huge successful open source project like TensorFlow need
*  one person who makes a final decision?
*  So you've did a pretty successful TensorFlow Dev Summit just now,
*  last couple of days.
*  There's clearly a lot of different new features being incorporated
*  in an amazing ecosystem and so on.
*  How are those design decisions made?
*  Is there a BDFL in TensorFlow, or is it more distributed and organic?
*  I think it's somewhat different, I would say.
*  I've always been involved in the key design directions,
*  but there are lots of things that are distributed where there are a number of people,
*  Martin Rick being one who has really driven a lot of our open source stuff,
*  a lot of the APIs, and there are a number of other people who've been
*  pushed and been responsible for different parts of it.
*  We do have regular design reviews.
*  Over the last year, we've really spent a lot of time opening up to the community
*  and adding transparency.
*  We're setting more processes in place, so RFCs, special interest groups,
*  really grow that community and scale that.
*  I think the kind of scale that ecosystem is in,
*  I don't think we could scale with having me as the lone point of decision maker.
*  I got it.
*  So yeah, the growth of that ecosystem.
*  Maybe you can talk about it a little bit.
*  First of all, when I started with André Carpathy when he first did ComNet.js,
*  the fact that you can train in your own network in the browsers,
*  in JavaScript was incredible.
*  So now TensorFlow.js is really making that a serious, a legit thing,
*  a way to operate whether it's in the back end or the front end.
*  Then there's the TensorFlow Extended, like you mentioned.
*  There's TensorFlow Lite for mobile.
*  And all of it, as far as I can tell, it's really converging towards
*  being able to save models in the same kind of way.
*  You can move around, you can train on the desktop,
*  and then move it to mobile and so on.
*  There's that cohesiveness.
*  So can you maybe give me, whatever I missed,
*  a bigger overview of the mission of the ecosystem that's trying to be built
*  and where is it moving forward?
*  Yeah.
*  So in short, the way I like to think of this is
*  our goals to enable machine learning.
*  And in a couple of ways.
*  One is we have lots of exciting things going on in ML today.
*  We started with deep learning, but we now support a bunch of other algorithms too.
*  So one is to, on the research side, keep pushing on the state of the art.
*  How do we enable researchers to build the next amazing thing?
*  So BERT came out recently.
*  It's great that people are able to do new kinds of research.
*  There are lots of amazing research that happens across the world.
*  So that's one direction.
*  The other is, how do you take that across all the people outside
*  who want to take that research and do some great things with it and integrate it
*  to build real products, to have a real impact on people?
*  And so if that's the other axis in some ways.
*  At a high level, one way I think about it is
*  there are a crazy number of computer devices across the world.
*  And we often used to think of ML and training and all of this as,
*  okay, something you do either in the workstation or the data center or cloud.
*  But we see things running on the phones.
*  We see things running on really tiny chips.
*  And we had some demos at the developer summit.
*  And so the way I think about this ecosystem is,
*  how do we help get machine learning on every device that has a compute capability?
*  And that continues to grow.
*  And so in some ways, this ecosystem has looked at various aspects of that
*  and grown over time to cover more of those.
*  And we continue to push the boundaries.
*  In some areas, we've built more tooling and things around that to help you.
*  I mean, the first tool we started was TensorBoard.
*  You wanted to learn just the training piece,
*  the effects for TensorFlow Extended to really do your entire ML pipelines
*  if you care about all that production stuff.
*  But then going to the edge, going to different kinds of things.
*  And it's not just us now.
*  We are a place where there are lots of libraries being built on top.
*  So there are some for research, maybe things like TensorFlow Agents
*  or TensorFlow Probability that started as research things,
*  or for researchers for focusing on certain kinds of algorithms.
*  But they're also being deployed or used by production folks.
*  And some have come from within Google,
*  just teams across Google who wanted to build these things.
*  Others have come from just the community.
*  There are different pieces that different parts of the community care about.
*  And I see our goal as enabling even that.
*  It's not we cannot and won't build every single thing.
*  That just doesn't make sense.
*  But if we can enable others to build the things that they care about,
*  and there's a broader community that cares about that,
*  and we can help encourage that, and that's great.
*  That really helps the entire ecosystem, not just those.
*  One of the big things about 2.0 that we're pushing on is,
*  OK, we have so many different pieces.
*  How do we help make all of them work well together?
*  So there are a few key pieces there that we're pushing on,
*  one being the core format in there and how we share the models themselves
*  through, say, Model and TensorFlow Hub and so on.
*  And a few of the pieces that we really put this together.
*  I was very skeptical about the way that we're doing this.
*  I was very skeptical that that's, you know, when TensorFlow.js came out,
*  it didn't seem or deep learning JS.
*  It seems like technically very difficult project.
*  As a standalone, it's not as difficult,
*  but as a thing that integrates into the ecosystem, it seems very difficult.
*  So, I mean, there's a lot of aspects of this you're making look easy,
*  but on the technical side, how many challenges have to be overcome here?
*  A lot.
*  And still have to be.
*  That's the question here, too.
*  There are lots of steps to it.
*  I mean, we've iterated over the last few years, so there's a lot we've learned.
*  Often when things come together well, things look easy.
*  That's exactly the point.
*  It should be easy for the end user, but there are lots of things that go behind that.
*  If I think about still challenges ahead, there are,
*  we have a lot more devices coming on board, for example, from the hardware perspective.
*  How do we make it really easy for these vendors to integrate with something like TensorFlow?
*  There's a lot of compiler stuff that others are working on.
*  There are things we can do in terms of our APIs and so on that we can do.
*  As we, TensorFlow started as a very monolithic system,
*  and to some extent it still is.
*  There are lots of tools around it, but the core is still pretty large and monolithic.
*  One of the key challenges for us to scale that out is how do we break that apart with
*  clearer interfaces?
*  In some ways, it's software engineering 101, but for a system that's now four years old,
*  I guess, or more, and that's still rapidly evolving and that we're not seeing that
*  still rapidly evolving and that we're not slowing down with, it's hard to change and
*  modify and really break apart.
*  It's sort of like, as people say, changing the engine with a car running or fixing
*  the interface, that's exactly what we're trying to do.
*  There's a challenge here because the downside of so many people being excited about TensorFlow
*  and becoming to rely on it in many of their applications is that you're kind of responsible,
*  it's the technical debt.
*  You're responsible for previous versions to some degree still working.
*  When you're trying to innovate, it's probably easier to just start from scratch every few months.
*  Absolutely.
*  Do you feel the pain of that?
*  2.0 does break some back compatibility, but not too much.
*  It seems like the conversion is pretty straightforward.
*  Do you think that's still important given how quickly deep learning is changing?
*  Can you just...
*  The things that you've learned, can you just start over or is there pressure to not?
*  It's a tricky balance.
*  So if it was just a researcher writing a paper who a year later will not look at that code again,
*  sure, it doesn't matter.
*  There are a lot of production systems that rely on TensorFlow, both at Google and across the world.
*  People worry about this.
*  I mean, these systems run for a long time.
*  So it is important to keep that compatibility and so on.
*  And yes, it does come with a huge cost.
*  We have to think about a lot of things as we do new things and make new changes.
*  I think it's a trade off, right?
*  You can, you might slow certain kinds of things down, but the overall value you're bringing
*  because of that is much bigger because it's not just about breaking the person yesterday.
*  It's also about telling the person tomorrow that, you know what, this is how we do things.
*  We're not going to break you when you come on board because there are lots of new people
*  who are also going to come on board.
*  One way I like to think about this, and I always push the team to think about as well,
*  when you want to do new things, you want to start with a clean slate,
*  design with a clean slate in mind.
*  And then we'll figure out how to make sure all the other things work.
*  And yes, we do make compromises occasionally, but unless you design with the clean slate
*  and not worry about that, you'll never get to a good place.
*  That's brilliant.
*  So even if you're responsible in the idea stage, when you're thinking of new,
*  just put all that behind you.
*  Okay.
*  That's really, really well put.
*  So I have to ask this because a lot of students, developers ask me
*  how I feel about PyTorch versus TensorFlow.
*  So I've recently completely switched my research group to TensorFlow.
*  I wish everybody would just use the same thing.
*  And TensorFlow is as close to that, I believe, as we have.
*  But do you enjoy competition?
*  So TensorFlow is leading in many ways,
*  many dimensions in terms of the ecosystem, in terms of the number of users,
*  momentum, power, production level, so on.
*  But a lot of researchers are now also using PyTorch.
*  Do you enjoy that kind of competition or do you just ignore it and focus on
*  making TensorFlow the best that it can be?
*  So just like research or anything people are doing right,
*  it's great to get different kinds of ideas.
*  And when we started with TensorFlow, like I was saying earlier,
*  it was very important for us to also have production in mind.
*  We didn't want just research, right?
*  And that's why we chose certain things.
*  Now PyTorch came along and said, you know what?
*  I only care about research.
*  This is what I'm trying to do.
*  What's the best thing I can do for this?
*  And it started iterating and said, okay, I don't need to worry about graphs.
*  Let me just run things.
*  I don't care if it's not as fast as it can be, but let me just make this part easy.
*  And there are things you can learn from that, right?
*  They again had the benefit of seeing what had come before,
*  but also exploring certain different kinds of spaces.
*  And they had some good things there, building on say things like JNR and so on before that.
*  So competition is definitely interesting.
*  It made us, this is an area that we had thought about, like I said, way early on.
*  Over time we had revisited this a couple of times, should we add this again?
*  At some point we said, you know what?
*  Here's, it seems like this can be done well.
*  So let's try it again.
*  And that's how we started pushing on eager execution.
*  How do we combine those two together?
*  Which has finally come very well together in 2.0,
*  but it took us a while to get all the things together and so on.
*  So let me ask, put another way.
*  I think eager execution is a really powerful thing, those added things.
*  You think it wouldn't have been, you know, Muhammad Ali versus Frazier, right?
*  You think it wouldn't have been added as quickly if PyTorch wasn't there?
*  It might have taken longer.
*  Longer?
*  Yeah.
*  It was, I mean, we had tried some variants of that before,
*  so I'm sure it would have happened, but it might have taken longer.
*  I'm grateful that TensorFlow responded the way they did.
*  It's doing some incredible work last couple of years.
*  What other things that we didn't talk about?
*  Are you looking forward in 2.0?
*  It comes to mind.
*  So we talk about some of the ecosystem stuff,
*  making it easily accessible through Keras, eager execution.
*  Is there other things that we missed?
*  Yeah.
*  So I would say one is just where 2.0 is,
*  and, you know, with all the things that we've talked about.
*  I think as we think beyond that,
*  there are lots of other things that it enables us to do
*  and that we're excited about.
*  So what it says is,
*  we've cleaned up the surface for what the users want.
*  What it also allows us to do a whole bunch of stuff
*  behind the scenes once we are ready with 2.0.
*  So, for example, in TensorFlow with graphs
*  and all the things you could do,
*  you could always get a lot of good performance
*  if you spent the time to tune it.
*  And we've clearly shown that lots of people do that.
*  And we've also done a lot of things
*  with 2.0 with these APIs where we can give you
*  a lot of performance just with whatever you do.
*  Because we see it's much cleaner,
*  we know most people are going to do things this way.
*  We can really optimize for that
*  and get a lot of those things out of the box.
*  And it really allows us, both for single machine
*  and distributed and so on,
*  to really explore other spaces behind the scenes
*  after 2.0 in the future versions as well.
*  So right now the team is really excited about that.
*  Over time, I think we'll see that.
*  The other piece that I was talking about
*  in terms of just restructuring the monolithic thing
*  into more pieces and making it more modular,
*  I think that's going to be really important
*  for a lot of the other people in the ecosystem,
*  other organizations and so on
*  that wanted to build things.
*  Can you elaborate a little bit what you mean
*  by making TensorFlow ecosystem more modular?
*  The way it's organized today is there's one,
*  there are lots of repositories
*  in the TensorFlow organization at GitHub.
*  The core one where we have TensorFlow,
*  it has the execution engine,
*  it has the key backends for CPUs and GPUs,
*  it has the work to do distributed stuff.
*  All of these just work together
*  in a single library or binary.
*  There's no way to split them apart easily.
*  There are some interfaces, but they're not very clean.
*  In a perfect world, you would have clean interfaces where,
*  okay, I want to run it on my fancy cluster
*  with some custom networking,
*  just implement this into that.
*  We kind of support that, but it's hard for people today.
*  I think as we are starting to see more interesting things
*  in some of these spaces,
*  having that clean separation will really start to help.
*  And again, going to the large size of the ecosystem
*  and the different groups involved there,
*  enabling people to evolve
*  and push on things more independently
*  just allows it to scale better.
*  And by people, you mean individual developers and?
*  And organizations.
*  And organizations?
*  That's right.
*  So the hope is that everybody sort of major,
*  I don't know, Pepsi or something uses,
*  like major corporations go to TensorFlow
*  to this kind of...
*  If you look at enterprises like Pepsi or these,
*  I mean, a lot of them are already using TensorFlow.
*  They are not the ones that do the development
*  or changes in the core.
*  Some of them do, but a lot of them don't.
*  I mean, they touch small pieces.
*  There are lots of these, some of them being,
*  let's say hardware vendors who are building their custom hardware
*  and they want their own pieces.
*  Or some of them being bigger companies, say IBM.
*  I mean, they're involved in some of our special interest groups
*  and they see a lot of users who want certain things
*  and they want to optimize for that.
*  It's folks like that often.
*  Autonomous vehicle companies, perhaps.
*  Exactly. Yes.
*  So yeah, like I mentioned,
*  TensorFlow has been downloaded 41 million times,
*  50,000 commits, almost 10,000 pull requests,
*  and 1,800 contributors.
*  So I'm not sure if you can explain it,
*  but what does it take to build a community like that?
*  In retrospect, what do you think,
*  what is the critical thing that allowed for this growth to happen
*  and how does that growth continue?
*  Yeah. Yeah, that's an interesting question.
*  I wish I had all the answers there, I guess,
*  so we could replicate it.
*  I think there are a number of things that need to come together.
*  Right? One, just like any new thing,
*  it is about there's a sweet spot of timing,
*  what's needed, does it grow with what's needed.
*  So in this case, for example,
*  TensorFlow is not just grown because it was a good tool,
*  it's also grown with the growth of deep learning itself.
*  So those factors come into play.
*  Other than that, though, I think just hearing,
*  listening to the community, what they need,
*  being open to, like in terms of external contributions,
*  we've spent a lot of time in making sure
*  we can accept those contributions well,
*  we can help the contributors in adding those,
*  putting the right process in place,
*  getting the right kind of community, welcoming them and so on.
*  Like over the last year, we've really pushed on transparency,
*  that's important for an open source project.
*  People want to know where things are going
*  and we're like, okay, here's a process for you can do that,
*  here are our CS and so on.
*  So thinking through, there are lots of community aspects
*  that come into that you can really work on.
*  As a small project, it's maybe easy to do
*  because there's like two developers and you can do those.
*  As you grow, putting more of these processes in place,
*  thinking about the documentation,
*  thinking about what do developers care about,
*  what kind of tools would they want to use,
*  all of these come into play, I think.
*  BOWEN So one of the big things, I think,
*  that feeds the TensorFlow Fire is people building something
*  on TensorFlow and implement a particular architecture
*  that does something cool and useful
*  and they put that on GitHub.
*  And so it just feeds this growth.
*  Do you have a sense that with 2.0 and 1.0
*  that there may be a little bit of a partitioning
*  like there is with Python 2 and 3,
*  that there'll be a code base in the older versions of TensorFlow
*  that will not be as compatible easily
*  or are you pretty confident that this kind of conversion
*  is pretty natural and easy to do?
*  DR. KANAYASHWARAN So we're definitely working hard
*  to make that very easy to do.
*  There's lots of tooling that we talked about
*  at the Developer Summit this week
*  and we continue to invest in that tooling.
*  When you think of these significant version changes,
*  that's always a risk and we are really pushing hard
*  to make that transition very, very smooth.
*  I think at some level people want to move
*  and they see the value in the new thing.
*  They don't want to move just because it's a new thing.
*  And some people do, but most people want a really good thing.
*  And I think over the next few months
*  as people start to see the value,
*  we'll definitely see that shift happening.
*  So I'm pretty excited and confident
*  that we will see people moving.
*  As you said earlier, this field is also moving rapidly
*  so that'll help because we can do more things
*  and all the new things will clearly happen in 2.x.
*  So people will have lots of good reasons to move.
*  DR. KANAYASHWARAN So what do you think
*  TensorFlow 3.0 looks like?
*  Are things happening so crazily
*  that even at the end of this year
*  it seems impossible to plan for?
*  Or is it possible to plan for the next five years?
*  DR. KANAYASHWARAN I think it's tricky.
*  There are some things that we can expect
*  in terms of, okay, change.
*  Yes, change is going to happen.
*  Are there some things going to stick around
*  and some things not going to stick around?
*  I would say the basics of deep learning,
*  say convolution models or the basic kind of things,
*  they'll probably be around in some form still in five years.
*  Will RL and GAN stay?
*  Very likely based on where they are.
*  Will we have new things?
*  Probably, but those are hard to predict.
*  Directionally, some things that we can see
*  and things that we're starting to do
*  with some of our projects right now
*  is just 2.0 combining eager execution in graphs
*  where we're starting to make it more like
*  just your natural programming language.
*  You're not trying to program something else.
*  Similarly, with Swift for TensorFlow,
*  we're taking that approach.
*  Can you do something round up?
*  So some of those ideas seem like,
*  that's the right direction.
*  In five years, we expect to see more in that area.
*  Other things we don't know is,
*  will hardware accelerators be the same?
*  Will we be able to train with four bits instead of 32 bits?
*  I think the TPU side of things is exploring that.
*  TPU is already on version three.
*  It seems that the evolution of TPU and TensorFlow
*  are sort of, they're co-evolving almost
*  in terms of both are learning from each other
*  and from the community and from the applications
*  where the biggest benefit is achieved.
*  That's right.
*  You've been trying to sort of with eager with Keras
*  to make TensorFlow as accessible and easy to use as possible.
*  What do you think for beginners
*  is the biggest thing they struggle with?
*  Have you encountered that
*  or is basically what Keras is solving is that eager,
*  like we talked about?
*  Yeah, for some of them, like you said,
*  beginners want to just be able to take some image model.
*  They don't care if it's Inception or ResNet or something else
*  and do some training or transfer learning
*  on their kind of model.
*  Being able to make that easy is important.
*  So in some ways, if you do that by providing them
*  simple models with say in hub or so on,
*  they don't care about what's inside that box,
*  but they want to be able to use it.
*  So we're pushing on, I think, different levels.
*  If you look at just a component that you get,
*  which has the layers already smushed in,
*  the beginners probably just want that.
*  Then the next step is, okay, look at building layers with Keras.
*  If you go out to research,
*  then they are probably writing custom layers themselves
*  or doing their own loops.
*  So there's a whole spectrum there.
*  And then providing the pre-trained models
*  seems to really decrease the time from you trying to start.
*  You could basically in a colab notebook achieve what you need.
*  So I'm basically answering my own question
*  because I think what TensorFlow delivered on recently
*  is trivial for beginners.
*  So I was just wondering if there was
*  other pain points you tried to ease,
*  but I'm not sure there would be.
*  No, those are probably the big ones.
*  I mean, I see high schoolers doing a whole bunch of things now,
*  which is pretty amazing.
*  It's both amazing and terrifying.
*  Yes.
*  In a sense that when they grow up,
*  it's some incredible ideas will be coming from them.
*  So there's certainly a technical aspect to your work,
*  but you also have a management aspect to your role with TensorFlow
*  leading the project, a large number of developers and people.
*  So what do you look for in a good team?
*  What do you think?
*  Google has been at the forefront of exploring
*  what it takes to build a good team.
*  And TensorFlow is one of the most cutting edge technologies
*  in the world.
*  So in this context, what do you think makes for a good team?
*  It's definitely something I think a fair bit about.
*  I think in terms of the team being able to deliver something well,
*  one of the things that's important is a cohesion across the team.
*  So being able to execute together in doing things,
*  it's not an end like at this scale,
*  an individual engineer can only do so much.
*  There's a lot more that they can do together,
*  even though we have some amazing superstars across Google and in the team.
*  But there's often the way I see it is the product of what the team generates
*  is way larger than the whole or the individual put together.
*  And so how do we have all of them work together,
*  the culture of the team itself?
*  Hiring good people is important.
*  But part of that is it's not just that,
*  okay, we hire a bunch of smart people and throw them together
*  and let them do things.
*  It's also people have to care about what they're building.
*  People have to be motivated for the right kind of things.
*  That's often an important factor.
*  And finally, how do you put that together with
*  somewhat unified vision of where we want to go?
*  So are we all looking in the same direction or are we just going all over?
*  And sometimes it's a mix.
*  Google's a very bottom-up organization in some sense,
*  also research even more so.
*  And that's how we started.
*  But as we've become this larger product and ecosystem,
*  I think it's also important to combine that well with a mix of,
*  okay, here's the direction we want to go in.
*  There is exploration we'll do around that,
*  but let's keep staying in that direction, not just all over the place.
*  And is there a way you monitor the health of the team?
*  Is there a way you know you did a good job, the team is good?
*  I mean, you're saying nice things, but it's sometimes difficult to determine
*  how aligned.
*  Because it's not binary.
*  There's tensions and complexities and so on.
*  And the other element of this is the mention of superstars.
*  There's so much, even at Google,
*  such a large percentage of work is done by individual superstars too.
*  And sometimes those superstars can be against the dynamic of a team
*  and those tensions.
*  I'm sure TensorFlow might be a little bit easier
*  because the mission of the project is so beautiful.
*  You're at the cutting edge, so it's exciting.
*  But have you struggled with that?
*  Has there been challenges?
*  There are always people challenges in different kinds of ways.
*  That said, I think we've been,
*  what's good about getting people who care and have the same kind of culture,
*  and that's Google in general to a large extent.
*  But also, like you said, given that the project has had so many exciting things to do,
*  there's been room for lots of people to do different kinds of things and grow,
*  which does make the problem a bit easier, I guess.
*  And it allows people, depending on what they're doing,
*  if there's room around them, then that's fine.
*  But yes, we do care about whether a superstar or not,
*  they need to work well with the team across Google.
*  That's interesting to hear.
*  So it's like superstar or not, the productivity broadly is about the team.
*  Yeah.
*  They might add a lot of value, but if they're hurting the team, then that's a problem.
*  So in hiring engineers, it's so interesting, right?
*  The hiring process, what do you look for?
*  How do you determine a good developer or a good member of a team
*  from just a few minutes or hours together?
*  So again, no magic answers, I'm sure.
*  Yeah. Google has a hiring process that we've refined over the last 20 years, I guess,
*  and that you've probably heard and seen a lot about.
*  So we do work with the same hiring process and that's really helped.
*  For me in particular, I would say, in addition to the core technical skills,
*  what does matter is their motivation in what they want to do.
*  Because if that doesn't align well with where we want to go,
*  that's not going to lead to long-term success for either them or the team.
*  And I think that becomes more important the more senior the person is,
*  but it's important at every level.
*  Like even the junior most engineer, if they're not motivated to do well at what they're trying to do,
*  however smart they are, it's going to be hard for them to succeed.
*  Does the Google hiring process touch on that passion?
*  So like trying to determine...
*  Because I think as far as I understand, maybe you can speak to it,
*  that the Google hiring process sort of helps...
*  The initial determines the skill set there,
*  is your puzzle solving ability, problem solving ability good?
*  But I'm not sure, but it seems that determining whether the person is like fire inside them
*  that burns to do anything really doesn't really matter.
*  It's just some cool stuff, I'm going to do it.
*  Is that something that ultimately ends up when they have a conversation with you
*  or once it gets closer to the team?
*  So one of the things we do have as part of the process is just a culture fit,
*  like part of the interview process itself, in addition to just the technical skills.
*  And each engineer or whoever the interviewer is,
*  is supposed to rate the person on the culture and the culture fit with Google and so on.
*  So that is definitely part of the process.
*  Now, there are various kinds of projects and different kinds of things.
*  So there might be variants into the kind of culture you want there and so on.
*  And yes, that does vary.
*  So for example, TensorFlow has always been a fast moving project,
*  and we want people who are comfortable with that.
*  But at the same time now, for example,
*  we are at a place where we are also very full-fledged product,
*  and we want to make sure things that work really, really work.
*  You can't cut corners all the time.
*  So balancing that out and finding the people who are the right fit for those is important.
*  And I think those kind of things do vary a bit across projects and teams
*  and product areas across Google.
*  And so you'll see some differences there in the final checklist.
*  But a lot of the core culture, it comes along with just the engineering excellence and so on.
*  What is the hardest part of your job?
*  I'll take your pick, I guess.
*  It's fun, I would say.
*  Hard, yes.
*  I mean, lots of things at different times.
*  I think that does vary.
*  So let me clarify that difficult things are fun when you solve them, right?
*  It's fun in that sense.
*  I think the key to a successful thing across the board,
*  and in this case, it's a large ecosystem now, but you want a small product,
*  is striking that fine balance across different aspects of it.
*  Sometimes it's how fast do you go versus how perfect it is.
*  Sometimes it's how do you involve this huge community?
*  Who do you involve?
*  Or do you decide, okay, now is not a good time to involve them
*  because it's not the right fit?
*  Sometimes it's saying no to certain kinds of things.
*  Those are often the hard decisions.
*  Some of them you make quickly because you don't have the time.
*  Some of them you get time to think about them, but they're always hard.
*  So when both choices are pretty good, those decisions.
*  What about deadlines?
*  Do you find TensorFlow to be driven by deadlines to a degree that a product might?
*  Or is there still a balance to where it's less deadline?
*  You had the Dev Summit that came together incredibly.
*  Looked like there's a lot of moving pieces and so on.
*  Did that deadline make people rise to the occasion releasing TensorFlow 2.0 alpha?
*  I'm sure that was done last minute as well.
*  I mean, up to the last point.
*  Again, it's one of those things that you need to strike the good balance.
*  There's some value that deadlines bring that does bring a sense of urgency to get
*  the right things together.
*  Instead of getting the perfect thing out, you need something that's good and works well.
*  And the team definitely did a great job in putting that together.
*  So I was very amazed and excited by everything how that came together.
*  That said, across the year, we try not to put artificial deadlines.
*  We focus on key things that are important.
*  Figure out how much of it's important.
*  And we are developing in the open, internally and externally, everything's available to
*  everybody.
*  So you can pick and look at where things are.
*  We do releases at a regular cadence.
*  So fine if something doesn't necessarily end up this month, it'll end up in the next
*  release in the month or two.
*  And that's okay.
*  But we want to keep moving as fast as we can in these different areas.
*  Because we can iterate and improve on things.
*  Sometimes it's okay to put things out that aren't fully ready.
*  We'll make sure it's clear that, okay, this is experimental.
*  But it's out there if you want to try and give feedback.
*  That's very, very useful.
*  I think that quick cycle and quick iteration is important.
*  That's what we often focus on rather than here's a deadline where you get everything else.
*  It's 2.0.
*  Is there pressure to make that stable?
*  Or like, for example, WordPress 5.0 just came out.
*  And there was no pressure to...
*  It was a lot of build updates that delivered way too late.
*  And they said, okay, well, but we're going to release a lot of updates really quickly
*  to improve it.
*  Do you see TensorFlow 2.0 in that same kind of way?
*  Or is there this pressure to once it hits 2.0, once you get to the release candidate
*  and then you get to the final, that's going to be the stable thing?
*  So it's going to be stable in just like when NodeX was where every API that's there
*  is going to remain and work.
*  It doesn't mean we can't change things under the covers.
*  It doesn't mean we can't add things.
*  So there's still a lot more for us to do and we continue to have more releases.
*  So in that sense, there's still...
*  I don't think we'll be done in like two months when we release this.
*  I don't know if you can say, but is there...
*  There's not external deadlines for TensorFlow 2.0, but is there internal deadlines,
*  the artificial or otherwise, that you're trying to set for yourself?
*  Or is it whenever it's ready?
*  So we want it to be a great product.
*  And that's a big important piece for us.
*  TensorFlow is already out there.
*  We have 41 million downloads for 1.x.
*  So it's not like we have to have this...
*  It's pretty good.
*  Yeah, exactly.
*  So it's not like...
*  All a lot of the features that we've really polishing and putting them together are there.
*  We don't have to rush that just because.
*  So in that sense, we want to get it right and really focus on that.
*  That said, we have said that we are looking to get this out in the next few months,
*  in the next quarter, and as far as possible, we'll definitely try to make that happen.
*  Yeah, my favorite line was, spring is a relative concept.
*  I love it.
*  Yes.
*  Spoken like a true developer.
*  So something I'm really interested in, in your previous line of work is,
*  before TensorFlow, you let a team at Google on search ads.
*  I think this is a very interesting topic on every level,
*  on a technical level, because at their best, ads connect people to the things they want and need.
*  And at their worst, they're just these things that annoy the heck out of you
*  to the point of ruining the entire user experience of whatever you're actually doing.
*  So they have a bad rep, I guess.
*  And on the other end, so that this connecting users to the thing they need and want
*  is a beautiful opportunity for machine learning to shine.
*  Like huge amounts of data that's personalized, and you kind of map to the thing they
*  actually want, won't get annoyed.
*  So what have you learned from this Google that's leading the world in this aspect?
*  What have you learned from that experience?
*  And what do you think is the future of ads?
*  Take you back to the...
*  Yes, it's been a while, but I totally agree with what you said.
*  I think the search ads, the way it was always looked at, and I believe it still is, is
*  it's an extension of what search is trying to do.
*  The goal is to make the information and make the world's information accessible.
*  With ads, it's not just information, but it may be products or other things that people care about.
*  And so it's really important for them to align with what the users need.
*  And in search ads, there's a minimum quality level before that ad would be shown.
*  If you don't have an ad that hits that quality, but it will not be shown even if we have it.
*  Okay, maybe we lose some money there.
*  That's fine.
*  That is really, really important.
*  And I think that that is something I really liked about being there.
*  Advertising is a key part.
*  As a model, it's been around for ages.
*  It's not a new model.
*  It's been adapted to the web and became a core part of search and many other search engines
*  across the world.
*  Like I said, there are aspects of ads that are annoying and I go to a website and
*  if it just keeps popping an ad in my face not to let me read, that's going to be annoying clearly.
*  So I hope we can strike that balance between showing a good ad where it's valuable to the
*  user and provides the monetization to the service.
*  And this might be search, this might be a website, all of these.
*  They do need the monetization for them to provide that service.
*  But if it's done in a good balance between showing just some random stuff that's distracting
*  versus showing something that's actually valuable.
*  So do you see it moving forward as to continue being a model that funds businesses like Google?
*  That's a significant revenue stream.
*  That's one of the most exciting things but also limiting things in the internet is nobody wants
*  to pay for anything.
*  Advertisements again coupled at their best are actually really useful and not annoying.
*  Do you see that continuing and growing and improving or is there more Netflix type models
*  where you have to start to pay for content?
*  I think it's a mix.
*  I think it's going to take a long while for everything to be paid on the internet if at all.
*  Probably not.
*  I think there's always going to be things that are monetized with things like ads.
*  But over the last few years, I would say we've definitely seen that transition
*  towards more paid services across the web and people are willing to pay for them because they
*  do see the value.
*  Netflix is a great example.
*  We have YouTube doing things.
*  People pay for the apps they buy.
*  More people I find are willing to pay for newspaper content,
*  for the good news websites across the web.
*  That was in the case a few years ago I would say.
*  I just see that change in myself as well and just lots of people around me.
*  So definitely hopeful that we'll transition to that mixed model where maybe you get to
*  try something out for free, maybe with ads, but then there's a more clear revenue model
*  that sort of helps go beyond that.
*  So speaking of revenue, how is it that a person can use the TPU and a Google collab for free?
*  So what's the...
*  I guess the question is, what's the future of TensorFlow in terms of empowering, say,
*  a class of 300 students?
*  And I'm asked by MIT what is going to be the future of them being able to do their homework
*  in TensorFlow?
*  Where are they going to train these networks?
*  What's that future look like with TPUs, with cloud services and so on?
*  I think a number of things there.
*  Any TensorFlow open source, you can run it wherever.
*  You can run it on your desktop and your desktops always keep getting more powerful,
*  so maybe you can do more.
*  My phone is like, I don't know how many times more powerful than my first desktop.
*  You probably train it on your phone though.
*  You probably train it on your phone though.
*  So in that sense, the power you have in your hands is a lot more.
*  Clouds are actually very interesting from, say, students or courses perspective because
*  they make it very easy to get started.
*  I mean, Collab, the great thing about it is go to a website and it just works.
*  No installation needed, nothing to...
*  You're just there and things are working.
*  That's really the power of cloud as well.
*  And so I do expect that to grow.
*  Again, Collab is a free service.
*  It's great to get started, to play with things, to explore things.
*  That said, with free, you can only get so much.
*  So just like we were talking about, free versus great.
*  Yeah, subscription.
*  There are services you can pay for and get a lot more.
*  Great.
*  So if I'm a complete beginner interested in machine learning and TensorFlow,
*  what should I do?
*  Probably start with going to our website and playing there.
*  So just go to TensorFlow.org and start clicking on things.
*  Yep. Check our tutorials and guides.
*  There's stuff you can just click there and go to a Collab and do things.
*  No installation needed.
*  You can get started right there.
*  Okay. Awesome.
*  Rajit, thank you so much for talking today.
*  Thank you, Lex.
*  Fun.
*  It was great.
