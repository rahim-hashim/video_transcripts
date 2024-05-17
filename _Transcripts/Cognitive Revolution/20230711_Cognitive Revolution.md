---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 9764s
Video Keywords: []
Video Views: 977
Video Rating: None
---

# The AI Safety Debates with Zvi Mowshowitz
**Cognitive Revolution "How AI Changes Everything":** [July 11, 2023](https://www.youtube.com/watch?v=5yM7fIfxYV8)
*  A lot of people talk about alignment, talk about it as some sort of weird Boolean, where
*  if you figure out how to align a system, suddenly everything is aligned and everything is aligned
*  and everything is fine.
*  And I think this is a serious way people fool themselves in thinking this problem is a lot
*  easier than it sounds like it is.
*  We're going to tell them things like make the most money, make the most people happy,
*  get me the most dates, or whatever it is.
*  And the moment you say most on top of anything, you get effectively power-seeking behaviors,
*  resource-seeking behaviors by things that, again, are better optimizers than you are.
*  I think Sam Altman understands the problem pretty well, but that it seems clear he hasn't
*  cultivated a culture of safety amongst the people he hired.
*  I think one of the biggest barriers to coordination is people assuming they can't coordinate and
*  therefore not trying.
*  We need to engage with the Chinese and we need to talk to everybody else as well.
*  And we need to explore, could we coordinate on these basis?
*  Which first requires us to understand that we need to coordinate on these basis.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers, entrepreneurs
*  and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today my guest is Zvi Maschowitz, author of the influential blog, Don't Worry About the
*  Base, online at thezvi.substack.com.
*  Zvi is an information hyperprocessor with a background in math, trading, economics,
*  game theory and game design.
*  Over the last three plus years, first with COVID and now with AI, he's carved out a unique
*  niche for himself as a writer who can rapidly synthesize vast amounts of new and ever evolving
*  information into extremely clear, comprehensive summaries that help educated people keep up
*  with the latest news.
*  We had a wide ranging conversation, first talking about Zvi's longstanding interest
*  in AI and his general AI safety worldview, and also comparing notes about how we are
*  each using AI in our respective workflows today.
*  Spoiler, we do both use LLMs for a number of different purposes, but neither of us use
*  it much in our core writing work as of now.
*  We then discuss who really matters in today's AI debates, in other words, who exactly should
*  we be trying to influence with our AI takes.
*  I found Zvi's perspective on this question very interesting.
*  Then Zvi gives an overview of the current state of AI discourse, summarizing the positions
*  of these so-called effective accelerationists, the AI ethics and AI safety camps, and the,
*  in my view, unfortunate rivalry between them, and of course, the doomers, or as Zvi prefers
*  to call them, the worried.
*  Along the way, we cover Zvi's personal ethical framework, how much value he sees in possibly
*  but possibly not sentient AI agents, whether the current AI moment was inevitable, the
*  promise of various approaches to AI safety, the impact of the specter of US-China rivalry
*  on AI discourse, and whether the AI safety movement has been a huge success, or perhaps
*  has merely further accelerated AI capabilities progress.
*  As always, if you're finding value in the show, we encourage you to share it with your
*  friends.
*  And also please send us your questions for an upcoming AMA episode, your guest suggestions,
*  especially if you know entrepreneurs or researchers outside the United States who would make great
*  guests, and of course, your general feedback is always welcome.
*  You can email us at tcr at turpentine.co or DM me on Twitter where I am at LeBenz.
*  And finally, don't forget that my new AI Scouting Report is now available on our YouTube
*  channel.
*  We'll be promoting this more in the coming weeks, but already I've been very pleased
*  to see that a number of early commenters have said that it really has helped them solidify
*  their understanding of AI fundamentals.
*  With that, please enjoy this conversation on AI safety and AI discourse with Zvi Moshowitz.
*  Zvi Moshowitz, welcome to the Cognitive Revolution.
*  Thank you.
*  Great to be here.
*  So yeah, I'm excited about this.
*  You are a leader when it comes to attempting to make sense of the AI discourse, which is
*  along with everything else going exponential these days in terms of its volume.
*  So I'm excited to, you know, kind of get your worldview on all of this and try to get your
*  sense of kind of the lay of the land, what really matters right now, and hopefully identify
*  the signal that really matters in the increasing noisy environment that we're in.
*  I usually don't even do this when I'm talking to like, you know, people who have just published
*  a paper or a project or a product.
*  But because your role is more kind of meta analyst, I thought it would be good to first
*  just give you a second to kind of introduce yourself, give us a little bit of your history
*  on kind of how you got interested in AI, the perspective that you're coming to it from,
*  because I think that will really help inform people as they listen to the rest of your commentary.
*  Yeah, I want to say none of the things that you said in your introduction seem less strange
*  over time.
*  They will continue to feel bizarre.
*  And I think for a long time.
*  So I've been thinking about AI one way or another for decades now, because I was introduced
*  to the Poon debate between Elias Yudkasky and Robin Hansen, which is how I got into
*  the rationalist discourse in the first place.
*  And so, you know, I've been expecting AI on the horizon and wondering about what we
*  can do about it and expecting the default outcome to be quite bad if we didn't actively
*  do something else for a very long time at this point, you know, over a decade.
*  But I had made a deliberate decision not to focus on that, not to make it the thing that
*  I was having shower thoughts about or, you know, bothered me so much because I can do
*  it, you know, other people are better equipped to do this, you know, my comparative advantage
*  lies elsewhere.
*  You know, my math is not strong enough to engage in the kind of theoretical math debate
*  they were working on back in the 2000s and 2010s early on.
*  And so I instead, you know, I mean, first I was a competitive gamer before I started
*  working about this.
*  Then I was a trader of various types.
*  I started to try to start a few businesses.
*  And then in 2020, COVID happened.
*  And then I started writing about COVID.
*  I'd already had a blog and I was writing a bit about my thoughts.
*  But then I started writing just to because that's the way I process the world.
*  So you write down what you're thinking.
*  You try to explain to somebody else.
*  You can explain to somebody else you actually know what you think.
*  And it forces you to like set your sources and justify your reasoning.
*  And I need to process what was happening.
*  And then other people thought it useful and I kept doing it and it kind of snowballed.
*  And now I'm a professional writer.
*  And when COVID ended, I jokingly said on Twitter, weekly COVID posts replace weekly AI posts.
*  What a nightmare. This is going so fast.
*  And everyone said, yes, please.
*  And I was like, oh, and then I tried it.
*  And I've been writing 10,000 plus words a week ever since.
*  So, yeah, the 10,000 plus words is a good guide for the uninitiated.
*  My general sense of what you're trying to do in these kind of periodic roundup posts
*  is sort of create the thing that if people were patient enough to not read anything else
*  and then just come read you once a week, they would kind of come away without having missed
*  anything important. Is that kind of how you conceive of the project as well?
*  Instead of that, as sort of one of the pillars of the project is same with COVID.
*  What I was doing before was a one stop shop where I thought of links.
*  But if you wanted to ignore AI entirely and the AI discourse and AI risk and AI money
*  and ability, except for using it for your own purposes, and then once a week you check back,
*  you see what I have to say about the parts you care about.
*  You can figure out something you need to pay attention to.
*  You can click through, you can explore further, or you can not.
*  And the other big thing is to explain the thinking, explain, build up the world model
*  over the course of weeks and months and many words and help people think about what's going on,
*  not just lay out, OK, here's what I think. Here's what you should think.
*  I think that's, you know, here's how it is.
*  That's not as helpful.
*  So how do you just briefly approach the challenge up front of just ingesting all the information?
*  I mean, it probably goes without, you know, it goes by assumption that you're a pretty fast reader
*  and just naturally given to it.
*  But even so, you know, there's so much stuff, right, that even you can't probably consume
*  everything you'd like to consume at this point.
*  I saw a tweet that you posted recently about the AI X-Risk, you know, pro versus con with
*  Tegmark and Yom Likun and their debate partners.
*  And you asked, like, should I watch this?
*  So I thought that was very interesting that you're kind of crowdsourcing, you know, what you
*  should watch, a reflection of just how much stuff there is.
*  But maybe more broadly, like, how do you approach identifying what you want to take in in the
*  first place and then obviously, you know, working through toward synthesizing that for the audience?
*  Yeah, I thought audio content is especially expensive to consume, right, because I can
*  consume it about one point three and still be able to actually process the information or
*  arguments of people who are speaking like detailed, complex stuff.
*  And for really tough stuff, I can't believe I went to Tyler, I want to go at one point one.
*  But that's still like, compared to reading the transcript, that would be at least two,
*  probably more, three or four times that speed.
*  And I can then deliberately speed up and slow down as there's like these explicit things I want to
*  think about and I don't constantly have to process the new information while I process it.
*  It's much better.
*  So when I have something with audio content, I have to think carefully, do I want to consume
*  this and I have to make cuts, especially in the last three hour podcast coming out now,
*  the Vice Institute, 80,000 Hours, lots of other people.
*  And for a while, I was on every podcast, no demand.
*  And while that's really good content, you have to make choices.
*  For reading, my procedure is I have Twitter, where I set up an extensive set of lists.
*  Primarily, I have a rationalist list and an AI list and I have my followers and I consume those.
*  And then I pop out windows for here are some things that have content I want to consider
*  to do today.
*  If it's a small thing, I use the AI
*  and do it immediately.
*  It can take more than two minutes to handle it.
*  I'll pop it out.
*  And then at some point later, I'll go through all the AI links and I'll go, OK, what does this have to say?
*  How do I incorporate into what I'm doing this week?
*  Which section would this fall into?
*  And then I build the thing step by step as I have different sources to incorporate.
*  And I also have a feed list.
*  So I have a lot of RSS feeds.
*  And that's where I get most of my other stuff.
*  And then, if you'll mind, these two will alert me to anything that isn't going either of these two.
*  So I can then go find it and then proceed there.
*  Plus, there's something that will appear unless wrong at the alignment forum.
*  That's fascinating.
*  We've got some aspects of our history here are very similar.
*  I also got initially very interested in AI from the overcoming bias of Eliezer and Robin
*  Hansen days back in like primarily 2007, I think, was kind of the heart of that.
*  And similarly also kind of felt like, you know, at least as Eliezer was articulating the work to be done at that time,
*  such theoretical math chops seemed required that I basically felt like that wasn't really for me.
*  And obviously, the situation has changed quite a bit.
*  I'm very different, though, actually, on the mode of consumption.
*  For me, I can listen to pretty much everything at 2x.
*  And I kind of slotted into my downtime pretty naturally.
*  And I feel like it's more like the actual time looking at a device that feels scarce.
*  And that probably also just reflects that I'm not as fast or as fluent of a reader as you probably are.
*  Yeah, I think different people are very different.
*  Kyle Cowan will read at several times my speed.
*  Otherwise, there's no way he could read what he writes, what he writes about, what he really says he's when I'm reading.
*  It's insane. I read most, that's with most people.
*  But I definitely have trouble with listening to the hardware processing.
*  I've always had it. I've had problems learning foreign languages for that reason.
*  It's just something that takes more of my energy.
*  And so it's relatively less efficient for consumption.
*  And every time someone says, I listen to your writing, it strikes me as absurd.
*  Like, why would you listen to a podcast of this when you could just read it?
*  But sometimes you can do it.
*  Is there any role of language models in your workflow today?
*  Do you use a tool that helps you summarize or are you dabbling in creating first draft type of content for yourself?
*  Or do you just do it still alls-v top to bottom?
*  The writing is all me.
*  I have found the LMs are very, very bad at summarizing the things that I'm talking about.
*  They're very bad at expanding your writing in this type of form.
*  I know what style I want. I don't want to transform into a different style.
*  The spell checker basically does most of what I want it to do.
*  I don't think that having it check for errors would be very convenient.
*  I've experimented a bit with this, including writing some Python code, and I haven't been able to get anything particularly useful on that.
*  I probably should experiment more, but I don't think they're quite there yet.
*  I think other people will build tools. I'll eventually find those tools.
*  I'll start experimenting with those tools.
*  But it doesn't mean I don't use LMs.
*  I absolutely subscribe to GPT-4, and I use GPT-4, and I use Bing, and I use complexity sometimes.
*  But the main thing I use them for are for finding out about the world, asking questions about what's going on, asking questions about things I don't understand,
*  checking intuitions, checking to see if the LM will share my intuitions about a question, and also coming up with more examples of something.
*  If I have intuition, like today, I was trying to write a book about debate.
*  And so debate strikes me as something that's kind of like democracy.
*  It's one of these, it's the worst thing, except for all the alternatives.
*  And so I asked you, name 10 more things that are like that.
*  And it came up with some beautiful examples, and I started to lose steam by the end.
*  But you got five really good ones.
*  And so stuff like that is really useful.
*  And just it's better than Google for, you know, like, well, what was the source of this book?
*  What's going on with this particular event?
*  Can you narrow this down?
*  Can you extract this particular piece of information?
*  I'm often wanting things that aren't that easy to Google specifically.
*  And also, I'm just confused about something, and I want to understand it.
*  It's about useful. And for coding,
*  I still don't code very much, but I think my productivity was through the roof.
*  But I started using that was just obvious.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it, and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  Yeah, that all resonates with me as well.
*  I think pretty much down the line, I don't really use it for my writing.
*  I am starting to experiment a little bit with.
*  Actually, the mobile app, because the transcription is so good that I am
*  finding there's at least some utility in actually doing this the other day,
*  walking my kids down the street in their stroller, trying to get them to take a nap.
*  And, you know, as they're like getting close to nap, you know,
*  I'm talking to the mobile app and, you know, kind of telling it what I want to do,
*  what I'm trying to create. You know, here's kind of my thoughts.
*  It'll take a shot. It is typically not close.
*  But then I find like just transcribing, you know, recording again and just scrolling through its output
*  and just giving it raw commentary on its output and saying what I want more of, less of, do and don't like, etc.
*  Over like two to three rounds of that, I'm having some successes where I'm getting to like 80 percent,
*  you know, kind of there. And it does feel like when I actually do go back to my computer later and want to write
*  that I'm in a better place than I would have been if I had just sat down blank slate or even just because my typing is only so fast.
*  Right. So it's like just getting a lot of stuff out that then I can edit.
*  I'm not sold on that workflow yet.
*  I do think it has some tradeoffs and there are some things that kind of the LLM does that like you wouldn't have done
*  that you maybe kind of wish you, you know, wish hadn't been the final product that kind of still creeped into the final product.
*  But I don't know, it's at least kind of starting to work for me a little bit in that way.
*  In all the discussions about AI and how much AI is useful and how much it will aid productivity is the question of all that.
*  It's like where is the limiting factor? What is actually slowing you down?
*  You know, what would help you and not help you?
*  In this case, it's a place where like your writing experience is giving you a bottleneck and being able to flush out your thoughts,
*  get a rough idea of where you want to do. And that's just not a bottleneck for me at all.
*  Right. So that's for me, like the bottleneck is getting the information.
*  It's knowing what I want to say, how I think about something and the actual processing of that.
*  When I start writing, it's almost like this just, if anything, is free while I'm finishing the part of processing the information.
*  And so having it like take this kind of first stab wouldn't actually speed up my process at all,
*  because the part where I'm doing that is actually doing work anyway and is also very quick.
*  So I think a lot of AI is like people say, well, it's not very useful.
*  A lot of people haven't figured out how to use it.
*  And a lot of that they haven't asked, they haven't thought carefully about their own process and exactly what parts of things are easy and hard.
*  Don't try to do exactly what everyone else is doing.
*  Do the thing that's useful for you and then iterate on it and also learn what kind of engineering gets you the thing that you want.
*  I haven't done any of the detailed like paragraphs or pages long things,
*  but I figured out some very basic tricks that work for specifically getting me more of the type of things that I want.
*  But it all resonates to me.
*  The other use cases I'm right there with you to encoding.
*  Good God. Similarly, you know, code some, but not full time every day and the ability to just import the right stuff and, you know,
*  write the right kind of boilerplate and get me, you know, man, that really helps a ton.
*  So I love that. OK, let's talk about your worldview.
*  And then we're really going to dig into all this stuff that's going on in discourse.
*  But again, just want to kind of set out your position a little bit.
*  Could you this big question, but could you kind of take a couple of minutes and characterize your overall world view and specifically,
*  you know, as the safety debate has really heated up emphasis on that?
*  Yeah, there's a lot of different aspects to how one thinks about this.
*  And. A lot of the problem with the debate is that whenever you're debating somebody,
*  you never know which of the 20 things that are unclear, they're actually disagreeing with you about.
*  And often it will manifest as a disagreement somewhere else.
*  You understand that where they're actually disagreeing with you is something they haven't mentioned because it hasn't even occurred to them.
*  And someone might think differently about that. It's so obvious.
*  And at other times there will be like 17 different disagreements that don't really have a common cause or don't have a common logical cause,
*  but are motivated by the desire to get to an end result in various people or other things of that nature.
*  Or they're just sort of going off of a vibe and don't really have opinions on most of these questions.
*  And they don't really have to go here at model.
*  And then, like, you have to get them to think about it all in order to have a disagreement.
*  And you can then figure out what part of this is useful.
*  So for me, I would start with, you know, LMS are this incredibly useful tool in their present state.
*  They are almost entirely positive. I think that almost all of the fears and worries about
*  misuse or negative effects of LMS are overblown or if anything, reversed.
*  And that the effects of current levels of tech are just almost uniformly going to be positive.
*  However, I do think that this changes as the eyes approach human approaches to pass human level intelligence.
*  I think that this is a very different environment for us to live in.
*  I think it's a very different world. I think that lots and lots of very hard to predict things start happening.
*  And that if we're not very careful and almost by the pretty much by default,
*  the outcome is the death of every human on the planet, or at least the loss of control over our future such that
*  if you ask most people, including myself, they would see the resulting future to have very little or no value
*  compared to certainly potential futures or compared to what you currently might imagine a normal non-AI future to be.
*  And so you have to draw this big distinction between the AI is a tool right now. It's a tool, right?
*  It has some amount of ability to reason things and figure things out and like mimic human intelligence, but it's not like that.
*  And we can use that to greatly enhance our lives and experience and our progress.
*  And the point where the AI starts to become a rival optimization engine, rival set of capabilities, rival intelligence that can eclipse our own,
*  whether or not that then there's the curse of self-improvement, as Eliud Kaffee talks about,
*  and then suddenly, very quickly after we have something that's human or near human, it suddenly is deeply superhuman and we have no idea what's going on.
*  And then the entire solar system's atoms get rearranged.
*  However, the super intelligence would prefer and that likely doesn't involve us.
*  Or if it's something that looks more gradual, looks more slow, I think these are all very all possibilities are like not just possible,
*  but like substantial double digit probabilities of various outcomes.
*  And that all of these scenarios offer ways for us to come out of it very well and ways for us to come out of it.
*  Not at all, if we're not very careful about it.
*  And you have to think carefully about how these things work, where the problems are going ahead,
*  and that almost everyone thinking very poorly about at least some of the problems involved in this,
*  even if they think well about some of the other problems.
*  And there probably aren't any people who are thinking very well about every step of the way.
*  And that includes me, right? I'm almost certainly thinking poorly about some of these steps,
*  and that will be exposed over the coming months and years, hopefully, as we learn more and I think more and I take my mind.
*  But essentially, the AI safety problem is if you build a more capable optimization engine,
*  something that's more intelligent and do more things than we are, that has inherently many advantages over us.
*  It'll be copyable faster.
*  It'll be able to instantiate in various ways.
*  We have to rewind every moment state, can have essentially limitless memory, et cetera, et cetera.
*  Input huge amounts of data, orders of magnitude more than any human could possibly hope for.
*  It's already happened, et cetera, et cetera.
*  So if it can mimic the parts of what we have that's missing well enough, suddenly its capabilities disguise the limit.
*  And then it's going to be a tremendously powerful optimization engine that's going to optimize whatever gets pointed out to optimize,
*  even if we try to keep it as a chatbot, which we say, oh, we're not going to give it goals.
*  Well, we are going to give it goals. We know this. We've run this experiment.
*  And so it's going to have goals. It's going to have projects that it's going to optimize according to some set of priorities.
*  And we have no idea how to make it do this in a way that we control what those priorities are.
*  And we have no idea what priorities, if we could control it, we could put into it that wouldn't ensure a disastrous outcome,
*  even if we had that ability, either individually or collectively.
*  So all of this are problems we have to solve and we have to solve it knowing that we don't know how to solve these problems very well in current systems,
*  despite the fact that we are smarter than the current systems and the current systems are not dangerous and are not engaging in particularly adversarial actions.
*  But when we start creating these more intelligent, more capable, stronger optimization engines,
*  on every level, we're going to face optimizations for things that we do not want,
*  that respond in adversarial fashion, that require a security mindset where any way for them to fail is the way they definitely will fail.
*  Every time we try to fix problems, we are correcting for the thing that fools us into thinking we solve their problems or that gets around whatever our solution is.
*  And fundamentally speaking, we're trying to get and keep control of something that is smarter than us and more capable than us and more efficient than us with a competitive advantage over us.
*  And that is a very unnatural thing to want to happen.
*  And if you think this is impossible, I am deeply confused.
*  You think it cannot possibly go badly. I think you're just not thinking about this really at all.
*  And if you think we will probably be fine, then I am confused why.
*  I think a lot of people are like, well, we'll figure it out.
*  We will solve these problems and it'll probably be fine.
*  And I think we have to solve a lot of virtually impossible, not impossible in the impossible difficulty level on a game sense, problems.
*  In order to not have this go badly, I think there's probably solutions to that.
*  But these solutions are incredibly hard to find.
*  And as Eliezer Kesske emphasizes, may not have to be solved on the first try, because the moment you transition from a non-dangerous system to a dangerous system,
*  that's exactly when a lot of the things that were working before will stop working, your techniques to align the system, as we call it.
*  And that's exactly the time when if the system isn't aligned, you are in deep deep trouble and you meeting the human species might not be able to recover from a serious mistake.
*  And we also come up ourselves into various dynamics, equilibrium and world states where even though we figured out how to align in an important sense, individual AIs,
*  and we've been able to figure out how to make them act according to some thing that we told them to act according to,
*  how did the result in competitive dynamics end well for us?
*  And those are more problems than I think people are not thinking clearly about, people have no solutions to.
*  A lot of people talk about alignment, talk about it as some sort of weird Boolean, where if you figure out how to align a system, suddenly everything is aligned and everything is aligned, then everything is fine.
*  And I think this is a serious way people fool themselves into thinking this problem is a lot easier than it sounds like it is.
*  Because yes, that's part one of the impossible problem is you have to impossibly figure out how to make the thing do the thing you want at all.
*  But then you figure out what you want. And collectively, we have to coordinate on figuring out what we want.
*  And we have to make this in a enforceable, actually instantiated thing.
*  And we have to not screw it up in a possibly stupid way, because the history of humanity is the history of people constantly making incredibly stupid mistakes and having to fix them by trial and error, even when everybody needs relatively well.
*  So let me just try to give the super high level summary of a couple of those things.
*  I guess if I were to try to describe your overall kind of expectations, like first order approximation, it almost seems it's like uniform probability across everything, like basically radical uncertainty where there's some chance everything could go great.
*  You don't really quite know how there's like significant chance things go very bad or totally catastrophic.
*  And the details of that are also kind of fuzzy, although you gave a little bit more definition, I think, to how that might actually play out versus how things could go well.
*  But is that basically right? Just kind of a probability wise radical uncertainty?
*  Yes, and no. So I would say that one of the things that people do is they ask what should he do? What's your probability of doing?
*  And the answer to me, the first question is like sort of.
*  Where does that matter? Right, so I say that, like, well, if you're if you're in the single digits or below, that's important, because then it starts to be a question of, well, what's the P doom of not acting or slowing down or other alternate possibilities?
*  What are the what are the gains to be had? And you start to think, well, maybe we're getting close to a point where we might want to start taking some chances on that level in order to get the benefits.
*  Or you could argue even that's crazy. And in many other contexts, almost everyone on the earth would agree.
*  If you think your P doom is super high, it's in the 90s or 99s or whatever, then.
*  You have to start thinking about what actions might make sense, given that you can't really hope for just to have a good outcome by proceeding.
*  And so that starts to change your outcome. But if you're in anywhere in the middle, there are very few actions that make sense at 10 percent doom, but not 90 percent doom or vice versa.
*  Because all of the orders of magnitude of payoffs and costs are just bigger than this one order of magnitude of difference here.
*  And so, you know, it's not that you have radical uncertainty is that like it doesn't really pay to be that being that precise is not as valuable as you might think.
*  And that's one reason why people end up with these like kind of arbitrary responsibilities.
*  There are also so many different things in the process to model, so many different ways you can change.
*  You hear a lot of people say five percent, ten percent. You don't see that many people closely in the middle, but that's actually where I am.
*  I think 60 percent when I have to make a guess. But I understand that like as the rules abase, my numbers should be shifting around constantly.
*  And it's not that weird. I wouldn't say all these things are equally likely. It's more that.
*  It's all likely enough. We have to consider them as plausible scenarios and we have to like be willing to spend substantial amounts of time and effort and money and sacrificing of utility to make sure that there are good outcomes in those cases.
*  But if I had to guess what the most likely outcome is, I would say doom is less likely than not doom.
*  Although, again, both are substantially lie. And that if I guess that we lost, you know, I'd say a lot of it is what we just failed the alignment problem.
*  You know, maybe roughly half of it is we just got the alignment problem utterly.
*  Maybe half of it is that we succeeded at the alignment problem as we talked about the alignment problem.
*  And then we specified something that got us doomed anyway because we didn't understand about the dynamics implied in what we were doing.
*  But I don't consider these questions to be worth the detailed time and effort to try and get numerical answers from because I don't see any actions that change.
*  Right. Like, again, the question is, like, are these real things that we really have to deal with or not?
*  And the answer to me is all of them. Yes. Right. And that's much more important than, well, OK, exactly where do we go wrong more often?
*  Like, to me, it's like an interesting but not great use of the question.
*  Yeah. OK. I think that all makes a lot of sense to me. I think I'm pretty much right there with you in terms of not spending too much time trying to narrow my confidence interval.
*  And I think that it's kind of a question of how likely are various extreme outcomes?
*  It just seems like the lower bound on that or the lower end of that interval is high enough that it is of concern to me.
*  And it seems like it should be of concern to most people kind of regardless of exactly where you end up.
*  So it resonates with me and strikes me as just generally wise approach to not get nerd sniped into kind of false precision.
*  I'm going to try to do again the simplest version of why this is something that people should really take seriously.
*  And then I do want to get on to kind of the more discourse side of this, too, but just your view.
*  Simplest possible form seems to be. When something is more powerful than you as a general purpose optimizer.
*  That's inherently dangerous. And even if you get to set it up, you know, it still remains dangerous.
*  Is that a good one sentence summary?
*  Yeah, we're going to give these AIs, even if we manage to give them the goals and ideas that we want, it's called maximalist goals.
*  We're going to tell them things like make the most money, right? Make the most people happy.
*  Right. Like, you know, get me the most dates or whatever it is.
*  And the moment you say most on top of anything, or you want the most probability, you want the close, you know, the macro number of nines on your success on anything you could do.
*  Suddenly, or the thing is simply trying to be selected for more instantiations or, you know, we're just seeing more of the copies of the things that successfully convince humans to instantiate the more or to get the resources or any of these elements like that.
*  You get effectively, you know, power seeking behaviors, resource seeking behaviors by things that, again, are better optimizers than you are.
*  And by default, those things are going to end up with the resources, which is going to end up with power.
*  And that's not going to go well for us.
*  Yeah, makes sense. Certainly, I have never heard one good reason to dismiss that as a concern.
*  So let's leave that there for now. And we'll certainly touch back on some of these aspects as we kind of go through the survey of the AI debate and debate debates, as you put it.
*  For starters, I kind of wanted to ask who you think matters as you create content.
*  And obviously, anybody can come to your blog, you know, among many other points of confusion.
*  I feel like a lot of people are kind of confused about who are they even trying to reach when they put stuff out in the first place.
*  And so I've got my own kind of quick model of like who matters and why.
*  And I want to just bounce that off you and see how you would react to it, think about it maybe differently.
*  Seems to me like the most important people right now, if you could choose who you would want to influence, would be the leaders of the leading AI developers, as they are the ones deciding what to do and not to do and how to approach various problems.
*  You know, in actual work, making actual systems, which seem to be getting, you know, quite powerful quite quickly.
*  So, you know, leadership of OpenAI, leadership of Anthropic, leadership of DeepMind, you know, maybe a dozen global companies would seem to be like the most critical decision makers right now.
*  And then my tier two would maybe be like policymakers on the one hand and sort of general AI research community on the other.
*  Those are maybe, you know, if you think there's maybe a hundred decision makers across those top 10 or so companies, there's maybe then, I don't know, 10,000 each of kind of the policymaker and researcher, you know, somebody who could really make an advance in the field kind of sets.
*  And then the broader, you know, circle beyond that would be maybe like the discourse, you know, like all the people that are sort of echoing stuff back to each other, you know, public intellectuals, you're sort of, you know, venture capitalists.
*  That sort of whole, you know, people who have a lot of cloud on Twitter, but aren't necessarily making object level decisions in the short term.
*  And then finally, beyond that, there's kind of like the general public and they, you know, kind of feedback on to who are going to be the policymakers and like, you know, that kind of on some distant level controls, you know, will companies be allowed to do stuff or not?
*  How would you compare and contrast how you think about it versus that starting point?
*  I think this question is incredibly complicated and you can't think about it in isolation. You have to think about it together with questions like what needs to happen for things to go well?
*  What if it goes wrong causes things to go poorly?
*  How do we think they influence each other? Right. And these questions are very complex and difficult to answer.
*  So if I had to choose like one person to alignment pill properly on the margin, you have to edge towards my view, I would definitely pick Sam Altman.
*  Right. Sam Altman is more important than Joe Biden in this sense.
*  And then, you know, Dennis Sabas, Dario, Ed Infraafik, potentially the CEO of Google and Microsoft, Zuckerberg and others at Metta become prominent because like they are the highest on the totem pole that like clearly don't take this seriously.
*  And it would be great if they did take this seriously, it would substantially make the situation better.
*  And then like how important are they versus how important are the politicians?
*  How much do politicians actually drive policy?
*  How much are they willing to stick their necks out? How much do their opinions, they have real opinions, do they matter?
*  You know, if we convinced Joe Biden, what would happen? I don't even know if it would be that big a deal.
*  Or how likely he would be to understand the issues involved because they're very complicated and technical.
*  And, you know, he has infinite demand on his time, it is very old, and I'm sure his amount of compute left is shrinking in some sense, like it's certainly available for this.
*  And then, you know, we have a system with a lot of these review points and negotiation points, and it's very unclear who causes what to happen.
*  One of my disagreements with Tyler Cowen is Tyler puts a lot of weight on academic consensus and publishing papers to try and convince a bunch of academics to then try and convince potentially a bunch of like sort of behind the scenes policy people.
*  Then maybe convince a bunch of lawmakers and regulators to do the things that would be better.
*  And I think it's possible that that's an important vector, but it's confusing to me and unclear whether that vector is actually open to us or how I do it with V.
*  And I don't see how to run experiments to actually prove it one way or the other. Similarly for the public, right?
*  Like the public is currently, doesn't really know what it thinks, hasn't really understood the situation very well, but tends to be pretty worried about AI when you actually show it AI and ask it basic questions.
*  And how much does that matter? How much does that drive legislation?
*  And then another key question is how much do various different paths lead to good interventions that are well selected and designed to actually ensure good outcomes versus they cause misaligned actions?
*  So like one worry you would have is the population gets really scared about AI.
*  They demand action and then we prevent people from using AIs on a variety of current productive activity in ways that make our lives worse, but don't make us any safer from the real threats.
*  And so that's a reason not to go down the public line, right?
*  If we convince the public to be scared, we're not going to invest this very, very specific complex message that we need to control the training of advanced frontier models, because that is where the danger lies.
*  That is what could go wrong.
*  They are just going to latch on to whatever their minds can see because they are not going to spend endless hours on this.
*  They are not specialists, right?
*  And I would do the same if you talk to me about something that I spend very little time on.
*  So how does that play into your writing?
*  It sounds like, I mean, almost by definition, you're not writing for the general public.
*  Anybody who's reading you, you know, that's enough to qualify as being kind of part of the public intellectual set, at least.
*  But do you actively think about like an audience of open AI leadership, anthropic leadership, or do you just kind of write what you think and hope that that works its way to them?
*  I think in a certain way, you write for yourself always when your writing is going to suck.
*  And so you write the things that I would want to see if I hadn't put the effort into making this, the things that explain things to me.
*  And then the question is, you know, who else are you targeting?
*  And I try to become more and more careful about who am I targeting and who matters.
*  Because one of the things that I do think the number of people who actually like have a major influence on events, who sculpt what's going to happen is relatively small.
*  Not that other people collectively don't matter, but that like mostly they are not individually worth trying to target in that sense.
*  And certainly I developed a case of I'm going to target people who can handle very dense, very complex amounts of information, massive amounts of information.
*  And actually want to process it and make sense of it and like can engage with it on the level it deserves to be engaged with.
*  But if you can't handle that, I'm counting on people who can handle that to then get the information to them in some number of steps by putting distillations into a form they can process or invest the time to process.
*  Right. Like it's not a knock on them. If you gave a 10,000 word per week complex, dense thing on most topics, I wouldn't read it.
*  Right. Even if it was very, very good, because I just don't have that kind of time.
*  So in my mind, like there's a handful of public intellectuals who are sticking their neck out and making like impactful, meaningful arguments about this.
*  They show up time and time again. I try to engage with them specifically. I talk to them and I talk to people who are reading them, talk to people who pay attention to them.
*  More specifically, you know, I do hope that Altman and Hesabis and Amidai are reading what I have to say.
*  But I think even anyone who works at one of those labs, right, who can then pass the information along, who can then spread it to other people, who can then pass the core concepts and the most important parts onto people like that and also people who work around them, matters a lot.
*  One of the things I worry about most with OpenAI is that I think Sam Altman understands the problem pretty well.
*  But that it seems clear he hasn't cultivated a culture of safety amongst the people he hired, such that a lot of people who work at OpenAI don't understand safety the way that Sam understands it and the culture of the people you hire drives your company's actions.
*  And so he has much less ability to steer in these ways than Dario does in the profit work. He didn't in fact do this.
*  Even though I'm not convinced that Dario had a better understanding or worse understanding of what it actually takes to be safe at the end of the day than Sam does.
*  I think these are serious things to consider. I don't know as much about, need my butt, I've had conversations with people who work at all three organizations on, you know, as engineers.
*  And there are definitely people who care deeply about ensuring good outcomes with all three.
*  They have at least one reader in all three and hopefully they forward things on.
*  But yeah, it's a combination of also people who work in alignment, including outside of the labs, people who are in the discourse, who are out there being people with the arguments, public intellectuals who actually matter.
*  But there might be a million public intellectuals in some sense out of seven billion people. But the vast majority of them don't care about AI.
*  And the vast majority of the ones who do care about AI still aren't really providing any inputs to the way AI goes.
*  They're more of what I think of as a lesser tier with respect to AI.
*  So like I have this metaphor of like on level one, you have people who are generating new ideas, new ways of thinking about things, like new synthesis.
*  And then level two, you have people who are capable of processing things from people who are on level one.
*  And then level three, you have people who are only capable of processing things from level two.
*  Because again, of the amount of time, investment and expertise they have in this particular place,
*  then they started because they couldn't do something else.
*  You can definitely move up to a higher tier, lower number if you want to put in that effort in many cases.
*  Doesn't mean it makes sense.
*  And so then basically you want to go down the pyramid.
*  So the question is who is going to be able to explain this to somebody down the line?
*  Or who is going to be able to persuade other people on the same level as where I am?
*  Those are people I'm most talking to.
*  But I do think there's like a handful of people whose viewpoints like matter a lot.
*  And if they were to change their perspectives, change their way of looking at things and make arguments in the other direction,
*  it makes a sense of difference.
*  And we've seen a number of those people actually make this change.
*  Right.
*  But not necessarily the people who are previously out there making lots of the most impactful arguments.
*  But it's often people who just by nature of their careers, by nature of their experiences,
*  they command to raise respect.
*  Like most recently Douglas Hofstad, right, offered a go to Lesher Bach,
*  who pretty much everybody I know looked up to for that I Have a Strange Loop, all that work.
*  Now he thought that super intelligence, like, you know, full AGI was very far until super recently.
*  And he has not flinched from being loud about now that I think it's near,
*  I look at what's about to happen.
*  And this horrifies me.
*  This scares the hell out of me.
*  I don't know what to do.
*  And a few months ago you had, you know, Yashio Bingo, you have Jeffrey Hinton.
*  You know, these are a substantial portion of the voices out there.
*  And, you know, on the other side, you have a handful of people who are cited
*  the majority of the time when people cite reasons not to be worried.
*  And sometimes their arguments are good.
*  And sometimes their arguments are quite bad.
*  But if like even one of those people, you know, of the like five or 10 people
*  were to come around, I think that would make a significant difference, in my point of view.
*  And if a lot of them were to come around, like it would be a complete game changer.
*  I don't think that, you know, most people are doing anything other than looking to
*  a very small group of people for guidance, either direct or indirect.
*  Very interesting.
*  So it almost sounds like you've mentioned you have private, you know,
*  conversations discourse with some of these and then others I'm sure you're not in touch with.
*  It almost sounds like you have a list somewhat explicitly of like, these are,
*  you know, say 10 people who, if they were to change their minds,
*  would make a huge difference to how things go.
*  Would you be willing to venture like actually outlining a list of some individuals
*  that you think are kind of most cruxie for the broader path of history?
*  So I think there are also a lot of people in positions of like governmental authority
*  or power who would be tremendously impactful if they were to change their minds.
*  If any senator were to come out like pretty strongly with good views, well explained.
*  I think that would buy into some other credibility.
*  Certainly if someone like Biden were to do so, it would be huge.
*  Like the prime minister of the United Kingdom came out as concerned about this.
*  And I think that definitely made a significant difference.
*  I think there's like a broad category of many people who are not currently having a voice in
*  the debate, who if they were to suddenly like make it clear they cared about this pretty deeply and
*  became loud, would matter quite a lot. Certainly hundreds, possibly thousands on that level.
*  But in terms of people who are being like very loud in this side of the debate, I hate to spend
*  more time on him than we should given his behaviors. But like, for example, if he's been very,
*  very, very outspoken, very, very loud, he works at Metta, he is the third godfather of AI,
*  and the other two have joined the cause. The third one were to very profoundly and loudly say,
*  oh, I realized I was being stupid. I was wrong.
*  And we could all welcome that. And he started making relatively good arguments
*  and making them for a more nuanced, balanced position or even for a, you know,
*  this is dangerous, you know, anything that I think is an accurate position.
*  And he would be complete overturning of the test board. Like just that one person on his own.
*  And there's a number of other people who clearly make a big difference because, in many cases,
*  because they are one of the few people who are being very loud in a credible way, because of
*  their previous reputations about accelerationism and the need to like actively not take safety
*  precautions or the inability to take safety precautions. Right. And that's why I pay
*  attention to them and I try to address them as much as possible. It's probably convinced those
*  particular specific people themselves and say, you are making a mistake. Like you are wrong.
*  And I respect you enough that I think that if I were to point this out, you might change your
*  mind. And in some cases, I've written, in some cases, like I'm a coon, I said, okay,
*  that's not going to happen. This person is not interested in listening to arguments
*  and trying to figure things out for themselves. They have made their mind up for whatever reason,
*  for better or worse, it is what it is. In other cases, I still hold out a lot of hope.
*  I think you have to try because it's a lot of how things can go well. Also, simply people
*  at the labs often like being willing to stand up. I think Sam Altman did in fact do a lot of this,
*  very positive direction recently. He's come out in favor of strongly, very good regulatory
*  principles and ideas and of the dangers that are out there. There are other things he's doing that
*  are not as helpful, but this is almost tremendously helpful. I think that Jack Clark and Dario at
*  Anthropic could be making much stronger statements that I think they would endorse
*  in private, even now, about a situation that I think would help a lot. I'd like to see
*  Dennis Assamis speak out more. I'd like to see the CEOs of Microsoft and Google speak out more.
*  These are people who would I think be tremendous game changers if they emphasized the actual
*  problems involved. The list would go on and on. I couldn't name any number of people who would be
*  tremendously influential. It includes any of the standard people who are just above or above,
*  people who lots and lots of people would listen to, but just who aren't particularly weighing in on
*  us. I think you'd see a lot change. Interesting. I think one big question I've been very uncertain
*  about over time is to a degree, is this just going to play out how it's going to play out versus
*  is there a more contingent model of history where the local decisions that
*  individuals make and the very small scale dynamics actually could make a huge difference.
*  This one seems tough because on the one hand, you do have these massive trends of web scale data,
*  web scale compute, a whole field that is pushing on this, but then on the other hand, you do have
*  these decision makers who do really seem to matter. It seems like you do think it is ultimately a
*  path of the river history really matters to what outcome we get.
*  Yeah. I think strongly the path of the river will determine the outcome we get.
*  I think there are... I have a lot of model uncertainty about this. We might live in worlds
*  where the path to the river are all almost entirely good. We might live in a world where
*  the path to the river are almost entirely all extinction. We might live in a world in
*  which it's entirely up for grabs and it's very hard to tell. Certain aspects of the situation
*  are very, very difficult to stop. We're not going to stop Moore's Law until the laws of physics stop
*  Moore's Law. We're not going to stop algorithmic improvements and hardware improvements in some
*  general sense. We're not going to be able to contain the things that have already been released.
*  We're not going to contain the profit motives. We're not going to prevent there from being mass
*  investments into AI and AI applications unless we're willing to take very strong actions. A lot of
*  these ships have sailed. We have very tough game theoretic problems to solve, but certainly the path
*  from there to here has been very detail dependent in many ways.
*  We sat around until a very small number of people realized because that transformer is
*  moving because that transformer is moving. The people who founded all three major AI labs that
*  are pushing things forward did so specifically because of Vex, their directly downstream value
*  as you're discussing, and his warnings about the dangers of AI, which resulted both in a
*  substantial advancement in AI capabilities faster than we would have otherwise had,
*  and people who have a much better than we would have otherwise expected understanding of the
*  problem being in positions of authority over all three labs. There are good things about this and
*  there are bad things about this, but if a very small number of people, potentially even one
*  person, had made potentially different decisions about what to emphasize, the discourse would look
*  very different today. The state of AI would look very different today. A different timeline,
*  different game board. I think the arguments for whatever's going to happen is going to happen
*  are something along the lines of either we've already passed the points where we can make these
*  important distinctions and it's kind of too late. I think it's not impossible
*  in some sense, but also a sense of there are various competitive dynamics you can't avoid.
*  That the pressures are too strong, that the humans just don't have the coordination capacity,
*  don't have the impractice ability to make the sacrifices necessary to change the eventual
*  outcome that it's just taken. And always one can say, well, not with that attitude.
*  I think one of the biggest barriers to coordination is people assuming they can't coordinate and
*  therefore not trying. You see this especially in China, where I think that we definitely don't
*  have strong evidence that Chinese are in any mood to cooperate with us on pretty much anything,
*  on any level AI or non-AI, certainly regarding world transformational technologies.
*  But we also do not seem to have taken the first step of asking nicely
*  or put an indicator of interest. We need to talk to China. We need to engage with the Chinese.
*  And we need to talk to everybody else as well. And we need to explore, could we coordinate on
*  these things? Which first requires us to understand that we need to coordinate on these things because
*  there's no we to talk to them. There's no them and there's no we to talk to them.
*  There's no we to talk to them. There's no them and there's no we until we understand
*  collectively in some sense what has to happen. But certainly that's not determined. I see lots
*  and lots of decisions made every day that raise or lower slightly the probability of things being
*  steered in any particular direction. And the regulations on this and the ways people look
*  at this are incredibly fluid. I would even say that if you look at the history of media surrounding
*  AI, that the decisions of individual script writers and directors regarding a very small
*  number of properties have a substantial impact on our debate. Imagine if Don't Look Up hadn't been
*  made. It's very easy to imagine a world where that project wasn't greenlit. And yet it clearly had a
*  substantial impact on the way people looked at things, even though it had nothing to do with
*  the AI that surfaced along. Yeah, the Terminator also comes to mind there as if there had just
*  been no Terminator series. Right. Well, what if the Terminator wasn't very good? Right. What if
*  he's given it to a bad director and hadn't hired Arnold and it sucked? Because it's a normal action
*  movie that hasn't had this weird plot. And then nobody thinks about it. Instead, you know, we have
*  lots of people who are going, you know, we're just gonna do like Terminator. Other people are going,
*  well, Terminator is a terrible metaphor, terrible metaphor. And other people are going, actually,
*  the Terminator scenario itself is actually highly plausible if you've got pan travel
*  and other similar related things. And it's an actual, you know, there's a lot of things that
*  media actually gets a lot of questions remarkably right, remarkably often.
*  And it's surprising to me, on reflection, I'm watching Pursuit of Interest right now.
*  And they get a tremendous number of things correct on a technology that didn't exist
*  and they couldn't possibly have understood. You also get plenty of things wrong, of course.
*  And there are some things that are intentionally wrong for television purposes.
*  But it's amazing how much it's like, no, this is how LLMs perform. This is what big data is about.
*  This is the kind of inferences you can draw. This is the kind of capabilities that emerge when you
*  didn't expect them. This is the kinds of issues you have to think about when you're dealing with
*  the emergence of these kinds of systems for the first time. And what are the ethical considerations
*  and what are the, you know, who do you have power over this thing? How do you limit it? How do you
*  align it? What's the alignment tax you're paying? And they don't talk on the same, they don't use
*  the words we use. But they ask a lot of these really hard questions and they come up with like
*  highly plausible ways that something might play out or the ways that, you know,
*  characters might answer them in a cinematized world.
*  You said a minute ago, there is no us and them until we kind of, you know, figure out what everybody
*  thinks. China being, you know, another dimension of this entirely, just zooming in kind of the
*  local, you know, Western AI discourse, there definitely are some camps. So I kind of wanted
*  to get your survey of the camps, how you see them, you know, which are kind of maybe can,
*  you know, be merged or could at least work together versus, you know, which are sort of
*  irreconcilable. I guess I would break it down for starters into five camps, four or five.
*  On the sort of, you know, what me worry end, you have the EAC, Effective Accelerationists,
*  which, you know, you can maybe try to steelman that for me if you can. So that's nothing to
*  worry about. Then there's like the, you know, current concerns are most important. That's often
*  called the AI ethics community. They often seem to be accusing people of existing in a category
*  that I don't really think anyone necessarily exists in, but that would be the AI safety hype
*  marketers. That's sort of the accusation that people are making bad faith arguments about risks
*  because they want to drum up interest in their own products. So that I would say seems to be an
*  accusation from the AI ethics folks against maybe the next camp, which is like the AI safety folks.
*  Basically, you know, that seems to be kind of the centrist position from my standpoint of like,
*  hey, we should definitely take this seriously. It seems like, you know, it could be a real problem.
*  As you mentioned, all the leaders of the key developers are seemingly in that camp today,
*  with maybe Yann LeCun from Meta is a notable exception. And then finally, you've got your
*  kind of do-mers, you know, we're so screwed that, you know, as one person memorably put it, you know,
*  time to start spending more time with your family. Is that how you would break it down as well? I
*  mean, that's kind of the typical, you know, summary that anybody who is trying to summarize this would
*  give. But is that how you also see it? Or do you conceive of those groups a bit differently?
*  I can see it a bit differently. There's a lot of similarity between our models. A lot of this is
*  like when you go to Europe and there's like 17 different parties and like, mostly they all lie
*  on a spectrum and they're just like, but a bunch of them are just like, here's the pirate party who
*  just believes in ending copyright. There's nothing to do with anybody else. And like the position on,
*  you know, economic redistribution is I don't care, just give me my copyright material.
*  And so, or they might actually care as well, but also be really strong about copyright material.
*  So, one of these groups, I think that, you know, we start with PXL initiatives. I think that's,
*  they call them EXL. So, I think these people are very strongly in favor of just full speed ahead.
*  And then the question is like, what's going on? Like, why are these people have that belief?
*  And, you know, I mean, I'm effectively EXL in most places, the same way that like people talk,
*  you know, the famous, well, you're an atheist for every god but one. I just don't make an exception.
*  And so, they're just not making the exception. Like, they're not seeing what my, they don't
*  understand what makes AI different from all other technologies and why this is something we
*  shouldn't do, whereas everything else that had this kind of promise, we would do. Right. And so,
*  like traditionally people say like, okay, AI and bio risk, like, you know, creating bioengineered
*  plagues and other like risky biological research of particular types and trying to create artificial
*  general intelligence. Well, might not want to do those two, but you want to do pretty much everything
*  you want. You want your fusion power. You want your new medicines. You want all your new techs.
*  You want to build all the things you want to. We want our VR holodecks. Yeah. Can we into space?
*  Yes, we can, etc, etc. We're for all the things. We're just not for this particular thing because
*  we have concern. And they're like, no. Everyone always has reasons to suspect any given tech.
*  There's always talk of it took our jobs. There's always talk of this will destroy the nature of
*  the family or this will destroy our way of life, or humans will somehow be killed by this horrible
*  new thing. We've heard it all a thousand times before. And I think some of that is in fact,
*  a legitimate way of looking at the problem from one direction, like the way of grasping the elephant
*  and a thing to be aware of when thinking about the problem. But basically what's going on is people
*  either don't understand why this is different or choose not to understand or don't want to understand
*  why it is different, or just have some sort of weird, like they generalize so thoroughly as this
*  blinding optimism, or they see no alternative. And so they're presenting a front where they think
*  we should do it anyway. So like Rune on Twitter is I think a very good accelerationist thinker
*  in the sense that he fully acknowledges that it's very easy to get us all killed.
*  And there was tremendous danger. But he advocates eyes open, do it anyway.
*  Right? Like you must like the spice must flow as he puts it. Like there's no choice.
*  There's no there's no plenty. And I think others are in fact of this rough opinion,
*  but they don't say it out loud. But this opinion of well, you know, if we don't build AGI,
*  then our civilization has cut off all these other avenues for progress so thoroughly that we are
*  doomed. So even if it might kill or it might cause various other catastrophes, that's just a
*  risk we're gonna have to pay. These are problems we're gonna have to solve. We must boldly go and
*  make it work out. Right? Boldly going is never safe. Technology is not safe. Intelligence is just
*  the safe technology in the universe. Right? Yeah, we're proof of that. Yeah,
*  most dangerous thing that's ever happened. You know, why should we think of creating more of it
*  that isn't us? Because they say anything you do, that's crazy. What are you thinking?
*  But also one could argue would be crazy not to do it. Right? There's so much available promise,
*  so much value, so much wonder, so little alternative, it's the future, go do it. Or
*  they just think that, you know, it's inevitable. Right? I think some people do generally buy the
*  China argument of better us or if not me, then somebody else. And if somebody else will be less
*  responsible with it or have worse values or both. And so there's just no use in holding that.
*  And I think there's various people in this group of various levels of being genuine about it,
*  of understanding or not understanding the danger, of, you know, facing, internally facing down
*  what actually is going on and whatnot. And I try my best to give people the benefit of the doubt.
*  Right? To treat as many people as possible as actually understanding things as well as possible
*  while also being as good as possible and wanting good things. And I do think most
*  of our races definitely want a good future for the human race and one of the future in terms of what
*  they see as utility. And I will stubbornly cling to this as much as possible. I think there are a
*  handful, you know, I would say there's kind of a fixed category that's beyond Excel, which could
*  be called the extensionists, right? They're the machinists. They're the people who in the
*  free body problems say that this world belongs to Tricelaris, except for AI. They think that AI is
*  the future. They call it speciesist if we say anything otherwise. They think the AIs have value.
*  They're more, they'll be moral patients. They'll have more complexity. They'll think it's just
*  more trick bots. They're what matters and we might die and that's okay. And to them I see,
*  I disagree. I just completely disagree. We have very different moral codes and I think we have
*  the right to have preferences. Can it not work? Some of these people think you're not allowed to
*  have preferences. Objectively in some sense is better. So you're not allowed to say I'm human
*  and I have children, I'm going to have grandchildren, I want that kind of thing. How do you justify that?
*  I'm like, I don't have to. You could have bon arguments about that, but I don't have to.
*  And so there are good accelerationists and there are less good accelerationists. And like
*  the accelerationists I respect most acknowledge that there is a problem. Advocate looking hard
*  on solving that problem, but think that slowing down doesn't help you solve the problem, introduces
*  more other problems, or is just impractical and just think, well, we might as well be more clean.
*  So you can divide the accelerationists into the ones who are useful, good faith accelerationists
*  who want to solve our problems together, and the ones who think that the way we solve all our
*  problems is we just keep going forward without worrying about our problems and our problems
*  never materialize. As opposed to every problem in human history, we've had tons of other problems
*  in human history, we solve them by actually solving them. We solve them by realizing there's a problem
*  that if we don't do anything it's going to be very bad and then figuring out what to do about it.
*  Some of these problems have been very, very hard. Some of these problems have been like, well, it's
*  easy, but if you literally just treat it like it doesn't exist, it's going to be a real problem.
*  So then the safety hype manufacturer, they don't exist. I'm going to flat out deny the existence
*  of the safety hype. I think that there is no motivation for this. It does not actually make
*  sense. It doesn't benefit anybody. And the people who say that they're talking in their book,
*  I think it's a combination of they're talking in their books instead. They're trying to explain
*  why the opposite outcome should happen. So they distribute bad motives to other players
*  because they have those motives themselves. Or they're just so cynical and so second on mindset
*  where everybody's always talking in their book, even if they aren't. They can't imagine the idea
*  that anybody could possibly say anything that wasn't profit motivated. There was a post today,
*  in fact, for example, on PirateWires, it was like, well, everyone's just talking in their book from
*  all points of view. Everybody is just saying whatever their incentives say to say. Because
*  I think this person just can't imagine that there are people on many sides of this who are saying
*  what they believe or advocate what they think is good for the world, which would also be good for
*  them. I don't get to say, well, I think the world is going to die. But in the meantime, they'll be
*  really good companies. So I should support acceleration of them. I also don't get to say,
*  well, I think it's all going to be fine and create a paradise. But I can get more
*  subscribers if I say we're all doomed. So I'm going to sacrifice the future of humanity for
*  readership. How would that make me better off? If the world is going to be wonderful, I want that
*  wonderful world to live in far more than I care about anything else. I think it's all just silly.
*  If you want to stop this amazing technology, you want to stop it because you're afraid of it.
*  You want to stop it because you think it's a big deal. It's a problem. I don't think that means
*  that everybody who comes to do a position is doing so for logically great reasons. Like any other
*  position, a lot of people come to that conclusion because they had a vibe or people around them were
*  worried or they've hallucinated or come up with a different problem that's actually kind of
*  solvable or they're imagining a highly unlikely scenario as almost inevitable, just like every
*  other point of view. They do exist. So I think then jumping ahead, I'll get in the middle
*  afterwards, we have the do-mers as such. But I think this is a wide variety. So you sort of
*  enter this space not when you say there's an X percent chance. There are people who are
*  described as do-mers, like Paul Christiano, for example, who then you ask them what's their
*  chance of doing it, like 10 percent, 20 percent, something reasonably low. But they talk like do-mers
*  because they are saying, well, if we don't treat this problem as an impossible level problem,
*  if we try to play it like we're still playing Guitar Hero on media, we will definitely utterly
*  die unless we get super lucky. Like it would be very, very bad. But they think, well, with an
*  extraordinary effort, we can set up a do-me-impossible. We can make this happen. But we understand that we
*  need to shout from the rooftops just how dangerous the situation is to get that to happen so that we
*  can then solve our problems. Same way that if I didn't think that we were capable at all of
*  coming together and making these extraordinary efforts, I wouldn't be at the team. I'd be much
*  higher. A lot of that is we will in fact do things that are very impressive in some sense.
*  We will make an extraordinary effort. We will figure things out that I don't know how to figure
*  out. And we will solve our problems. And then there are people who actually think, like
*  Eliezer Kowsky, you think the probability of doom is more than 90 percent, more than 99 percent,
*  and need to do whatever gives us any chance at all of success. Or alternatively, like the problems
*  are so incredibly hard that if you don't have a mindset that we are super doomed, none of the
*  things you do will be easy. You can't solve our problem by treating it as a normal problem. You
*  have to treat it as an impossibly hard problem. Have any hope of your solution actually moving
*  us towards the real solution. And if you try to solve an easy problem, you're just not helping
*  much, or maybe even at all. So then there's people who talk about AI effects. I think that's a very
*  strange middle ground. I think some people are like, well, there's problems of AI because I'm
*  against AI. And I'm going to take every problem I can about AI. We'll generally just see disaster
*  in every turn because they're anti-new technology. They're anti-growth. They're anti-intelligence
*  in general in some sense often. And they just see the downside of everything. And so they tend to
*  emphasize these ethical or mundane concerns over the do-more concerns. But they would endorse the
*  do-more concerns probably as well if they thought it was useful and stop them from technology.
*  They just don't see it as especially useful in stopping the technology. Or they don't see it as
*  directly addressing the particular harm that they worry about as directly, so they don't pay as much
*  attention. And then there are people who see the short-term harm as real and see the longer-term
*  harms as irrelevant. And it's not clear to me again if they are coherently thinking about the
*  long-term harms. I think a lot of them are, you ask them, is there in fact a danger of a potential
*  risk? Well, respond with new or no answer. Just no opinion whatsoever. Just we can't think about that
*  right now. That's a distraction. Is there a real answer? They actually haven't thought about it.
*  And in some real sense, they don't care. We'll cross that bridge when we come to it, if we come to it,
*  for now. I really think life is about bias. There's some people who really do think that
*  that's what civilization should dedicate itself to, is fighting bias, fighting misinformation,
*  all of these little micro-causes compared to the objective. And one can argue whether or not the
*  thing they think is how important that is, but I think it's a lot less important than whether
*  humans live or die at all. And I'm not sure they agree. I think some of these people think,
*  well, if we can't solve these problems, we don't deserve to live, or something like that, or even.
*  I don't know. There are lots of different people out there. We're trying to characterize them.
*  I think of the AI ethics people as the people who put what they call ethics
*  above the things that matter to them, above survival of humanity,
*  generally getting good outcomes for people, generally ensuring there will be things of
*  value throughout the universe. These are things that I care about a lot. And I also care about
*  most of their concerns. I think those are important concerns. But they see my concerns
*  as a distraction from their concerns. I see their concerns as, potentially, a distraction from my
*  concerns to the extent that they use that as a reason to dismiss my concerns. We don't have
*  to do that. We can say we have to solve both these problems. And in fact, these problems have
*  complementary solutions. Any solution that helps solve my problem, that helps us keep us alive,
*  will help fight bias. Any solution that helps us get the AI to do what we want them to do,
*  that helps keep them under our control, will prevent the AI from putting misinformation,
*  prevent them from manipulating their users. It will help with all of that.
*  And when they do their work on their thing, it's at least not harmful. I welcome that work. I
*  welcome all of that work. But when you do things like argue the distraction thing,
*  when we get into a fight, we get into a fight because you choose to make it fun. You choose
*  to think of this as a zero-sum game, as opposed to we all benefit when we do all of this work.
*  That's the way I look at it. And if you have a proposal for mitigating near-term harms,
*  I will compare the costs and the benefits, and I will hopefully support that. That's a good idea.
*  But it can't be our focus. And if we only have so much room to pay attention to these things,
*  then we have to prioritize. And I know where my prioritization is, and I hope that that will also
*  help other things. And so in general, I would say you have the accelerationists. You have the
*  people who are—I call them the worried—the people who are worried about AI killing everyone,
*  because do-mers is kind of pejorative. And we don't want to—I don't call you fafers, right?
*  Why are you calling me do-mers? But I'm going to own it on occasion. We have people who are worried,
*  which makes it clear that you only have to be so worried to be worried. 10% is worried about it.
*  People who think we need to take this kind of action that won't happen on its own.
*  We have the people who actively try to distract in order to complain about other AI risks.
*  And then I would say the AI safety hype market factors, even if they aren't real,
*  instead you have a pretty bad-faith faction of the ethics people and a bad-faith faction of the
*  accelerationist people who are claiming this, trying to win an argument, in ways that don't
*  really make sense. Cool. I think that's pretty much all in line with my perception as well.
*  Couple just point-level follow-up questions on a few of these camps. On the accelerationist front,
*  is there any decent argument—what's the most compelling thing you've heard that would give
*  somebody reason to believe? Actually, yeah, there is a—even if you don't think it's the majority
*  case, there's some decent chance that this could just go really well and actually turn out to be
*  easy and never really was anything to be worried about in the first place. Wow, give me the hard
*  question, right? It's not just that—there's an easy-hard question, which is what's the best
*  argument for why we should go boldly, which is it won't be any better if we wait.
*  There are arguments that basically by waiting, you create what's called overhangs,
*  where we have the ability to do something much more powerful, we choose not to,
*  and we encourage bad actors to be the ones who are first movers because the good actors
*  are just raining souls, and we risk you're being too many people who have capabilities in question,
*  and sooner or later someone's going to do the thing we're worried about, and the only way to
*  stop a bad—an irresponsible person with an AGI or creating an AGI is to create the responsible AGI
*  first, or that only by getting close to AGI can we possibly be able to do the proper research
*  that will let us figure out how to make it safe. And so the time we spend putting our thumbs now
*  just gives us less time later. We should instead accelerate right to the edge because we can judge
*  where the edge is. I don't think we can, but we can much better judge where the edge is.
*  And then we can take our time. Then we can put in our Manhattan Project, our huge amount of effort,
*  whatever you want to call it. Then we can solve our problems and ensure good outcomes.
*  I think these are not facetious arguments. I think these are reasonable arguments. I think
*  they're overcome. I think they're not what carries the day, but I understand why someone would advocate
*  for them. The argument, well, why should we think that everything is just going to be easy?
*  People make various arguments of this type. A lot of them are content free. And recently literally
*  said, well, the good guys always win. And we're the good guys is implied. So win, which means the AI
*  must be aligned. It's that simple. We'll keep it in our mouth. And obviously that's kind of nonsense.
*  But you can say things like, a lot of people say, well, like the Yama Coons, or some other people
*  like that often say things like, well, if it was sufficiently intelligent, it would be smart enough
*  to realize that its goal was stupid or that morality is correct. And that it would therefore
*  do good things because it was smart. Scott Aronson has expressed views like this, for example,
*  I believe. I've seen it a number of places. I think it's a bad argument. I think there is no
*  reason to think that a more intelligent thing would be inherently moral or would deliberately
*  and consciously reject its goals in favor of goals that we like, or that any of the sort
*  makes any sense. I think that what we'd be hoping for is something like, it turns out that if you
*  kind of vibe on Elm style, on the things that are good, and you like enshrine a bunch of messy
*  principles that don't really have logical coherence, that's kind of how humans act normal and nice to
*  humans. One could argue. And then they sort of generalize this thing. And they realize they're
*  supposed to be in a sort of consistent, reflexive way, friendly and positive and cooperative and
*  care about other people. And then they actually internalize that because that's the best way
*  having positive incremental goals is the best way to get positive final outcomes that will be
*  approved of, that will allow them to achieve their goals in general. Therefore, it's good with these
*  humans that are pretty friendly in ways that correlate with intelligence, or you could argue
*  correlate with intelligence pretty well, but if you have something even smarter than us, you can
*  think harder for longer, process more data, get wiser, like if it again has more experience,
*  can process more data, this thing will then converge on some sort of place that humans
*  would converge on if they had more thought in terms of what is good in life, what should be done,
*  what's not a good and positive answer, as long as we give it sufficient measures in the right
*  direction. You don't have to be very specific. It's an attractor state. The good outcome is an
*  attractor state. We don't have to get a point of measure zero on a giant graph of exactly the
*  thing that does the thing that we want. We don't have to specify the goal. We don't have to
*  understand what we want either. You just let the AI figure it out. The AI will be vaguely well-meaning
*  and the AI will cooperate, and then the dynamics amongst many of these AIs that are positive or
*  the one AI created is positive will lead to a good outcome. So all we have to do is not intentionally
*  make this terrible. Obviously, if you create chaos GPT and you set up loose bad names, it's going to
*  be terrible. Most people would agree with that, but no one would be so stupid as to.
*  You just do the ordinary best thing, which is some combination of RLHF and constitutional AI and
*  basic ingraining of good principles, and then you do various tests. Then when it starts to exhibit
*  bad behaviors, you correct it. No, it won't suddenly learn how to do this by deception.
*  It won't learn how to pretend it's thinking what it's not thinking. It won't secretly record data
*  in places you're not looking so that it can survive various iterations. It won't pass things on to
*  the successor states and do all these tricky things. It won't figure out things we haven't
*  thought about with these things. It's just the obvious basic thing because that's what most
*  intelligences on the web have ever known and basically not. That's my steel man case for why
*  this is relatively easy. It's what naturally happens. It'll just sort of happen,
*  would be the optimistic case. To be clear, no. That's not how this works. It's not how any of
*  this works. I don't think it's completely impossible. Yeah, I was going to say large
*  language models do seem a heck of a lot closer to that than I would have expected
*  five plus years ago. If you just ask me, okay, we make some AI and it's an AI that's breaking
*  through and is becoming really useful and people are all, attention is turning to it. You don't
*  tell me anything about the nature of that AI, how it was trained or anything. Then you said,
*  like, how much do you think it will understand or be able to act in accordance with human values?
*  I think we're way on the high end of my expectation with LLMs, which is not to say that I
*  disagree with you, I don't think in the big picture, but just that holy moly, there's some sense in
*  which we're very lucky, I think, with the nature of LLMs. A much more kind of AlphaZero type
*  lineage probably doesn't produce anything along the lines of what we do seem to learn in some
*  abstract sense just from all the language. I think that it says we may have been lucky
*  and we may have been unlucky and it's really hard to tell which until first time. In the sense that
*  you can tell a lucky story where these things are much better at grokking more or less what we mean
*  and more or less what we care about in these kind of fuzzy messy ways than we would have expected.
*  They're not going to be ruthless optimizers because it's just not the nature of the mind that we've
*  created in some broad sense. And so, sure, we're getting human-ish things, maybe at the end of the
*  day in some ways. And then if we scale them up, they'll still exhibit these characteristics and
*  then we're in a much better state. However, the flip side of that is that you get these things that
*  are impossible to predict or understand, that are very squishy, they're very inscrutable.
*  And they're not being particularly coherent in many ways. And if they go off the rails,
*  it'd be very hard to prove or detect that they went off the rails in a meaningful way.
*  They're going to misunderstand us and what we actually care about, importantly. And we have
*  no hope of actually injecting the exact thing if we figure out what it is. They just can't take
*  exact things at all in that sense. And then maybe that's just not good enough. Maybe even the best
*  version of that just doesn't get us what we want and we'll start to break down pretty fast.
*  One thing is to note that there are often these very rapid transformations where the best solution
*  to a type of situation or problem, the very nature of it changes and you're best served by throwing
*  out all your previous work and then putting in a lot more work on this more intelligent,
*  more work level to do a better job. And so, for example, deception or telling people what they
*  want to hear, having a direct, like, how are you going to respond when you see this? Like,
*  by directly modeling exactly how these methodologies work is one of those things.
*  And there are many things like that. And I've been trying to write out this argument in more
*  detail the last few weeks and try to get it right. But essentially, right now, with its current level
*  of understanding, just trying to sort of messily represent human preferences and reflect them
*  is the best the AI can possibly do if its current level can go. Right? It's deception wouldn't work,
*  but it doesn't really understand what we care about very well. Whereas if it understood very well,
*  it's going to tell you what you want to hear. Absolutely, it will tell you what you want to
*  hear. There's no secure truth optimization going on here, except in so far as we punish it for
*  finding out what it wants. And if you had an AlphaGo style problem where it's just optimizing,
*  if you knew exactly what you wanted, you optimized for exactly the right thing.
*  Like, maybe you could win, right? Outright win. Get something great that would then do the things
*  you wanted. So it's kind of a, right, if you get a foo, or if you get like a very precisely defined
*  optimization target, and you hit it correctly, you win. And if you miss, you lose. And like,
*  there's not that much middle ground, and there's not much room for you to correct an error. Right?
*  Like, if you said that you made a mistake, you're stuck with the mistake. And if that means you still
*  get some value out of the world, you get some value out of the world, you can't get back the
*  part you lost. Right? You just, what we lost, lost. That is down. Whereas, with these messy LLMs,
*  like, you don't lose that way. You don't have this really scary thing where it suddenly decides to,
*  like, perform this really rigid optimization, and it will never prove up. But you also don't
*  get the good for you. Right? You don't get this precise, like, ensuring that things go well.
*  You just have this kind of messy situation. And this leads back to my concern over competitive
*  dynamics, where if you unleash a bunch of, like, messy human-ish things, that have messy human-ish
*  like alignment, but they're also better optimizers than us, and they're more capable, and they're
*  more efficient, and they have all these advantages. Yeah, they don't immediately turn around and kill
*  us on purpose or anything. But then actually do itself as good. This is our way. Right? Like,
*  that's not an efficient condition for this to turn out well. And that's assuming kind of the,
*  that our current methods don't break down. Like, our current methods hold in a separate way. So,
*  if you tell the story that I told, which is actually, you know, you give them a bunch of
*  feedback as to vaguely what we want, and they kind of generate some processes that kind of internalize
*  the type of things that we want, and that generalize, and they turn into a genuinely, like,
*  about as aligned as us type of aligned thing. Well, if you suddenly, like, created a bunch of
*  things that were, you know, able to quickly outcompete us with numerous advantages
*  that had about our morality, you wouldn't survive very long. Like, certainly you would never meet
*  your own children. But like this idea that, like, there is much hope in that level of
*  approach, I haven't really understood why. Right? Even if it succeeds. And also, I just don't think
*  it happens automatically. Right? I think that what happens is the AI suddenly does a rocking
*  thing, right? Where like, when it goes from 10 to the X, 10 to the X plus one, or 10 to the X plus
*  two cycles, it suddenly realizes that it can do a completely different thing to get the outcome it
*  wants, that it's being rewarded for, it does that other thing instead. And we find out that all the
*  things we did before are suddenly useless. I think that's by far the more likely outcome.
*  Yeah, grokking as a phenomenon, I think, is one of the most under-appreciated and under- I mean,
*  people don't even know about it broadly. But that paradigm has shaped my thinking probably more than
*  any other over the last couple years of moving from memorization to generalization,
*  and the unpredictability of that seems like, yeah, just such a critical point.
*  Going back up the stack then, that was my one question on the EX. But the
*  AI ethics and safety, it seems like from my perspective, probably really dumb that these
*  camps, you know, kind of are so at odds with each other so often. And I would say there's blame on
*  both sides of that, not to blame present company at all, but there is kind of, I'd say both sides
*  kind of say, your concern is a distraction from my concern. And that has kind of, the battle lines
*  have kind of hardened along those lines. If there's any hope that that could change,
*  I mean, we're starting to see a little bit of thaw. And I guess my understanding of why there's been
*  maybe some thaw and could be hope for more working together in the future is maybe that as such focus
*  and attention and resources come to this area in general, maybe there's sort of an omnibus spending
*  kind of thing that everybody can kind of say, yeah, you know, I, much like we have, you know,
*  in these kind of big tent, big budget bills that get passed, right? Like, well, I don't care about
*  what you're doing. You don't necessarily care about what I'm doing, but we're both kind of doing
*  something that this is going to fund. And so that could be good. Maybe that kind of brings camps
*  together into a, hey, what matters is we invest in this, we invest a lot. And, you know, if all of
*  a sudden there's going to be, you know, huge governmental funds poured into it, then there's
*  kind of enough for everybody, you know, to get funded and do their thing. You don't look too
*  pleased with that scenario or hopeful for it. I wish the primary intervention that made sense
*  was to pour a bunch of funds. Right. That would make things so much easier because then you
*  absolutely can all agree, you know, a hundred billion here, a hundred billion there. I get my
*  money, you get your money. Pretty soon you're talking AI safety. Well, pretty soon you're talking
*  about money, but like, I don't know if you're talking about the problems. I don't think you're
*  talking about AI safety. Right. Like I think it helps, but, you know, I don't think this is a case
*  of money is the problem. And then like we hide the cost of getting that money back from the taxpayer,
*  but just having it be any more of a spending bill. I think you have to impose
*  actual costly restrictions on what companies can do on what models can be developed and played
*  and used in various ways. And some of the restrictions help with one problem. Some
*  of the restrictions help with the other problem. And you can require these people to pass certain
*  tests and to go through a certain hoop. And again, like, there's competing for a kind of limited
*  resource here in a much more clear way. This makes it harder. I do agree that there's no reason for
*  these characters to be distinct. The bigger that they are, there's no reason for them to be each
*  other's throats. I think a lot of the reason why the AI humor side of this is so against the
*  ethics people is one, they know the ethics people are going to try and completely side by the humor
*  people. They're going to try and ignore all these concerns, get everybody to ignore all these
*  concerns. They see that in advance. Right. It's the, well, you know, if, you know, AlphaVille is
*  going to attack Beta Town and Beta Town doesn't like AlphaVille. Right. Like, it's just, that's
*  just how it is because you see the conflict coming. Defrauding over limited resources. I'd be fine
*  with the peace treaty. They're not. Well, it's a problem. Part of it is their arguments are
*  incoherent because they imply our problem and then they just deny it. Right. To a large extent. We see
*  this and we get really frustrated. It's like, well, yeah, of course, if these people who are like,
*  well, you know, the AI will never be able to fool people enough to take over the world. The
*  misinformation from AI generated content next year is a serious problem in our election. It's like,
*  really? Right. Like you can have either of these positions and it's fine. And it makes some sense.
*  Really hard to have both in some important sense. Right. Like you think that like these much less
*  capable systems that we fully understand and that we can manage in real time recovering from our
*  mistakes are these dire threats that require these responses. And yet you can't understand why
*  stealing them up a lot will present an example for us. And that's just so people at one point,
*  you know, someone was like, you know, it's like being on a bus and the bus is about to go over
*  a cliff and someone worries we're going to be late for work. Well, yes, we're going to be late for work.
*  But it's very hard to reach that conclusion about noticing the bus is about to go over the cliff.
*  Right. And if you know the bus is going to go over the cliff, maybe you have other problems
*  that you should worry about more. But at the same time, like, you know, once we steer this
*  bus away from the ledge, you have to get you to work on time. To work. Right. Like getting out.
*  And, you know, I do think that's like an example of a metaphor that's like, oh, too dismissive
*  and pisses people off for no reason. And we have to move on to things that are more positive.
*  Like, I don't want that to be the go to. And so I cited as an example of both like how it's easy to
*  interpret the problem from the side of someone worried and how it's easy to like be somewhat
*  unfair to those people who are on the other side at the same time. But there really is this inherent
*  logical contradiction going on a lot of the time. Where they just don't want to see it because they
*  can't imagine it. They can imagine things in front of their face, not the things in the future. And
*  also, like we've seen this time again, where like these types of concerns hijack the political
*  process, the regulatory process. And then like we used to call our concern AI safety. And these
*  people came in, they just started using AI safety to mean don't say bad words.
*  And now we have to find new words for what we're saying. And like, they pretend they're us. They
*  pretend that they're doing the thing that we're doing. And they're just not. Right. And it's like,
*  doesn't mean everything is bad, when everything is not necessarily. Which is incredibly frustrating.
*  And so yeah, we end up each other's throats in bed. And I wish we didn't. As I said, like, I think
*  there's room for us to all cooperate on this. Right. Because we all want the same things.
*  But also, I just think that they're objectively wrong about the near-term concerns. Like the AI
*  FSOs. And also that like, they're wrong about their preferences in many cases. Right. And so like,
*  you would have disagreement over like, what is specifically going to happen? Like if you
*  unleash this AI generation, like what, you know, are people going to be fooled by these deep things?
*  Are they going to think that their girlfriend cheated on them because they saw an AI-generated
*  picture? Are they going to think that that on Trump was in fact, you know, killing Godzilla and that
*  Joe Biden was being, you know, impaling innocent young virgins on sticks? Like, I don't know.
*  And then like, they'll be fooled and they'll vote for Trump and it'll all be terrible. And like, no.
*  Right. It's not going to happen. We're going to be able to deal with it. Is my opinion. And like,
*  that's one disagreement. Another disagreement is they think that certain things are really,
*  really important that I don't think are as important relative to the potential utility games
*  that are involved. Right. Like we have this ongoing disagreement in general about progress
*  and about technology and about growth and about like flourishing of humanity. Many of us. Right.
*  And the ethicists, people who call themselves ethicists these days, right? Medical ethicists
*  show like this, bioethicists show like this, you know, and so on. Their attitude is harm is what
*  matters. Right. The specific harms that I am worried about Trump your, they call it greed
*  or desire or wants, but like they Trump the good that can be done.
*  I think it's just not true. Right. I think these harms should be considered. They should be
*  mitigated. We should do our best to avoid them. But, you know, when we don't, if they vote on
*  people who like, you know, don't do challenge trials for COVID vaccines, right. Like could have
*  saved so many people. We talked to a few people who would have probably volunteered. We didn't do it.
*  The ethicists told us no. And the ethicists are constantly like in the medical context telling us
*  no. You mentioned that will save us, that will save lives. Right. Where everybody involved in agreement
*  is consenting. They don't care. They think it's not okay. And like this is usually less egregious
*  than that, but it's the same idea. Right. It's, they think that there are the deontological rules
*  that matter more than utility involved. Right. Or than other rules and other principles.
*  And I think they have the wrong rules. Right. I'm following a set of references. It's very
*  different. I'm sure you have a reconciliation for this, but I think one place where people might be
*  a little confused about your views is obviously in that, you know, last moment you sound quite
*  consequentialist, utilitarian, whatever. Earlier when talking about sort of AI descendants as a
*  path and like how much value you would ascribe to something like that, it sounded like you were not
*  willing to, you know, go so far on utilitarian thinking as to say, well, if the robots have a
*  lot of utility, then that it's good enough for me. So I wonder what is the, could you kind of
*  unpack those underlying principles a little bit more? It's like a certain kind of utility that
*  you care about the most or how do you think about that? So I'm a virtue ethicist, first of all,
*  just flat out. If I have to select one of the big three to describe how I think, I do think that
*  like, if you can't express your view in all three at the same time, your view is ill conceived and
*  you haven't actually figured out what you want. So like I should be able to define a utility function.
*  It's just going to be really complex. And like with the human amount of data in compute, virtue
*  ethics is the correct way to express what I want. Similarly, the ontological rules, right, are very,
*  very useful again, because we have the way to compute limited data. And, you know, it's very
*  beautiful ourselves. And these calculations come in, intensely complicated and involve lots of
*  terms that we just don't know. But we have radical uncertainty about many aspects of the universe,
*  like we've activated a calculation problem. And like, the utility of the ontological
*  implementation is higher, right? So you should use that. But my reconciliation is very simple.
*  I care about myself and my descendants, my fellow humans.
*  And I don't care on the same level about who they are. And it doesn't mean that I think we could
*  have no value, but I don't think you can just do math. I notice that you can't just do math.
*  Right? You can't, like certainly there are people I know who will say things like, well, you know,
*  each chicken has this much value. Each worm has this much value. If you simulate this many
*  worms and this many GPUs, it might generate this much value. You have them all have orgasms all the
*  time, but it would have this much value. And I'm like, no, you've obviously got it. Right? Like
*  you're taking your metric and you're treating it like it's real, right? When it was supposed to be
*  an approximation, a way of figuring out how to handle situations and you're taking it out
*  of distribution, right? This is not going to worry the AI with it in many cases, right?
*  We teach it what is good by giving it examples in a distribution. And it learns in that distribution
*  how to optimize for the right outcomes. And then we take it out of that distribution
*  by either, you know, treating it with problems that weren't in the training side or are likely
*  in the training side, or just like giving it a lot more capabilities than anyone in the situations
*  that we were modeling had at the time. And that inherently makes every situation radically different
*  or a number of other things. And then we say, okay, what happens now? And the answer is you've got
*  something weird. You've got something that doesn't make any sense, usually often, or that we wouldn't
*  prefer because the data that you have doesn't actually tell you the answer, right? Like
*  utilitarianism is a good way of correcting for the fact that like
*  you have to do math and two or something is more important than one of something.
*  And 20 of something is actually sometimes 10 times as important as two, but not always.
*  And it's not that simple. And also like human preferences are not inherently very coherent
*  or like very consistent. You can try to make the inconsistency of the variance possible, figure out
*  what you actually prefer on reflection. But if you just say, okay, you take a system with a
*  contradiction, right? It's well known. If you take any system of math, you start with a contradiction,
*  you can prove anything you want. Right? So like if you start, if you're utilitarian
*  and you write down an inexact equation and an approximation, and you start manipulating those
*  inexact equations a lot, you're going to get nonsense results. Invisibly out of distribution,
*  who can tell steps? And one of those nonsense results is like, well, maybe we should simulate
*  a bunch of worms having organic oil. This is dumb. Like we all know this is dumb. Right? No matter
*  like, and I can accept, you know, that if you go to a bunch of AI's and they wipe us out, that
*  universe, so I think most of those universes, right? The majority of them are pretty close to zero
*  utilitarian. I evaluate them as like the AI is not good, the AI is not bad, they love me, they hate
*  me, I do not love or hate it. It's just using my items for something else. And that's probably
*  unfortunate. But like, whatever it is I care about is not my default thing. Right? Like I don't really
*  care about something that's optimizing for W symmetric. I don't really care about something
*  that's optimizing for many of the things that might be somewhat technically complex, but which
*  are particularly interesting. Something that is like effectively pure power seeking is not very
*  interesting to me. It's not very valuable to me. And also, I really don't think you have to take
*  this sort of disembodied non-physical utility perspective and say that's what you have to
*  prefer. I think that's not okay. Like, you know, if we live on our world, the vopings live on their
*  world, the Klingons live on their world, we're allowed to prefer humans to Klingons, you know,
*  we're allowed to prefer humans to survive and the Klingons die, and the Klingons live and the humans die,
*  even if under some abstract utility there's not real difference.
*  We're allowed to care about ourselves. In fact, I would say the key part of my
*  sobrality that like, you need to care about yourself and those around you more than random
*  other people, or the entire thing falls apart and doesn't work, and nobody gets any utility.
*  Right, if parents don't care for their children more than they care for other people's children,
*  it's not going well. Right, and so like in some sense you can realize that like there's a
*  contradiction and there's a conflict and there's a kind of mistake, but it has to be that way.
*  In some important sense. So I don't talk philosophy in my blog because I know that like
*  philosophers should have spent lots and lots of time on this to rip anything I say to strut.
*  I understand this, but at the same time I have to follow along with these things, and I believe
*  strongly that you are allowed to care about yourself and care about things you care about
*  and define your own utility function and what you think are important things to exist.
*  And I've made my choices, and again these people call themselves ethicists,
*  I've made very different choices. And I'm not saying you're not allowed to have those
*  preferences legitimately if they have those preferences. I can see I think they're wrong.
*  In the sense that I actually think they do not in fact refer to the world they are claiming to
*  prefer on reflection in the world that they're planning to dis-refer. And that if they actually
*  reflected and reconciled their positions, they would have to change their minds.
*  But maybe they really do. I don't know. It's a different kind of disagreement.
*  Right, partner?
*  Let's imagine all the humans are gone, and then there's some AIs or no AIs, and then within some
*  AIs you could have unfeeling, no qualia, no subjective experience AIs that are just
*  paperclip maximizers or whatever. And then on the other hand you might have some AIs that have
*  some sense of feeling and subjective experience, and maybe they can do even some of the things
*  that we could do, like they could appreciate some art or whatever. But they're obviously
*  going to be still quite different from us presumably. It does sound like you distinguish
*  between those. You would rather have the art appreciators than the non-art appreciators,
*  and you'd rather have more than fewer. But then at some point where people start to push on,
*  well what if there were enough of them? Or what if there was a trillion trillion of them?
*  At some point you just kind of get off that train and say, well I'm not going to allow you
*  to push the multiplication problem to that extent because I just feel like that's out of
*  distribution entirely. And so I kind of fall back to a more brute force fact of my own ethics,
*  which is I care about myself. And so you can't push me that far. Fair?
*  I certainly think I have a preference order over the non-human universes.
*  I am confused about how much I prefer those universes and how much probability of survival
*  I would trade off to get the better universe if I fail versus the worst universe. Like that,
*  I think that's unclear stuff. But I do think that, yeah, it's not that multiplication can never do
*  it. It's not that you couldn't convince me, or was efficiently convincing Kaye's art reflection,
*  that there's a situation in which I prefer certain long-distance futures to other long-distance
*  futures. But I also have a sense in which it's not my role to prefer that. The system doesn't work
*  if people do that. We're supposed to prefer that the things that we care about
*  survive. And there's no reason why, in theory, we couldn't spread those things out to spread
*  throughout the universe in some sense. But I don't think this is an area where anyone
*  can figure it out. I don't think anybody really knows what does and doesn't have certain types
*  of properties or what these completely out of distribution universes, with these completely
*  out of distribution things, what they should think about them, how they should prefer different
*  configurations to other configurations. And this is one of the dangers is that we're potentially
*  setting the configuration of the universe in motion relatively soon with no idea what we
*  actually prefer, and what matters to us for reals at this scale. And that's really scary,
*  because if we don't know how each AI, what we don't even know, I don't just mean that we haven't
*  figured out what we think. We just legitimately are deeply confused, and our feedbacks are not
*  going to reflect anything that we want here. Then we're going to iterate on that somehow with some
*  sort of system. It's a giant disaster waiting to happen. If I had a long reflection, I would take
*  it. If I had the opportunity to suddenly have me and the people around me not age and live for
*  100,000 years, and I can't put my memory to talk about this stuff for a long time and just do
*  philosophy, that sounds great, but you don't get it. We have to solve all our problems first before
*  we get to there, in some important sense, before we can do that. And so we have to have these
*  squishy messy views on how to do these things and what we'll do the best we can. But yeah,
*  I noticed that I prefer not to die, and I prefer my children not to die, and I prefer them to have
*  children of their own, and I prefer that the human race continues in general. And I think I am very
*  much committed to that preference, and it is good that I have that preference. And
*  Kelly, why are you trying to talk me out of it? But I don't expect anyone to succeed.
*  Yeah, I won't attempt that here. Certainly, I'm not the best person to try, as I think I, again,
*  mostly pretty similar in my position, including even just, I would say, probably waiting
*  for virtue ethics more heavily in my own thinking than a pure utilitarian,
*  consequentialist, whatever. Popping back up then, I was asking my point level questions on
*  these different camps, and we're getting to the do-mers, aka the worried. I think people who are
*  coming to this relatively recently and who are encountering this line of thought relatively
*  recently, first of all, have no sense for just how long it has been around and how deep it has
*  run. I wonder if you could give a little bit of a short story from your perspective of what the
*  AI safety evolution has been over the last 15 years since you first got interested in it.
*  I think it's especially interesting to help people understand how much care and, I sometimes call it,
*  AI safety respectability politics has gone into just trying to be, and not always succeeding,
*  but trying to be the sort of people who can be trusted or can be respected or who don't seem
*  crazy on other dimensions. I'd love to just hear that story from your perspective a little bit.
*  From my perspective, I hadn't given AI any thought for a while, and then I read these
*  series of blog posts by Alianzou Kasky and Robin Hansen, and they were engaging in this debate
*  over what would it look like in our distant future when there was artificial intelligence.
*  And as these arguments sunk in, as I thought about the implications, I realized that
*  if this technology were to exist, everything would change. And that Alianzou was basically correct
*  that by default, if you built something smarter than a human, then it would be able to build
*  something smarter than itself still because humans were able to build that thing.
*  And it would be able to scale up its resources and capabilities pretty quickly, again, by default,
*  but not automatically, not necessarily automatically, but by default. And if you
*  didn't have this thing able to preserve some property of what it was optimizing for in a kind
*  of known, provable way, that thing would change in a weird direction and also was actually remarkably
*  hard to specify what it actually wanted anyway, and that this thing would take control of the
*  future. These are the terms that we use now. It's almost hard to remember exactly what terms
*  I was using when I had it back then, but it was a long time ago. It's 15 years, something like that,
*  before now. And at the time, we were trying to solve this, people like Alianzou Kasky were trying
*  to solve this problem by creating mathematical systems and stringing together various different
*  problems together would allow a system while it was self-improvement to preserve provably its
*  utility function such that whatever you put into it as the thing it was trying to accomplish,
*  it would still accomplish that thing right when it was done because we didn't think it was an LLM.
*  What was it? GoFundMe, real-fashioned AI. It was basically a logical enterprise. And if you could
*  preserve that, well, that was not an easy problem. And then you had to actually make it so that
*  preserving it, you had a thing that was worth preserving that would then lead to a good outcome
*  as well. And so at one point, there was a meeting that I was a part of where I was with a bunch of
*  people from what was then called Singularity Institute and that was called MIRI.
*  And it was outlined over here, the seven things that you need to solve. Solve these seven things,
*  then you can solve the alignment problem on a kind of GoFi. And also you kind of built the AI as well
*  like incidentally along the way by doing so, certainly, or you're pretty close. You have to
*  understand a lot of the principle of the problem, that's what it is. And then you can build it and
*  it's safe in every way. And then I was told at the end of the meeting, and so before I was told the
*  seven things, forget what they are. It's an info hazard for you to know what they are. You might
*  tell somebody else, you might act in a way that reflects what they are, and you don't want this
*  stuff getting out, but it helps to build the apps. It actually did forget. One of the six things,
*  one of the seven things, which is a pretty non-dangerous one to remember, but forgot the
*  others. And throughout the years, they did very hard work to try and figure out how to make progress
*  on this type of agenda. This agent foundation is trying to make agents that act predictably,
*  accurately, prove things about, rely upon, work under iteration and improvement. And
*  this was deep math, hard math, hard enough math that when I asked if I should work on it, I was
*  told yes. And they worked on this, but it was a very small number of people. And this effort
*  basically didn't make much progress. But we got a number of things written, we figured some things
*  out, some very interesting, advanced things. We never got that question or solution.
*  And then over time, as we better understood all the ways we couldn't align an AI, all the things
*  that made the problem harder, we didn't make progress in that sense. We discovered all these
*  different reasons why AI was really, really hard to align. And we explained them really well. We
*  made better decisions here than anybody else. Which is one of the reasons why in all this time,
*  it's often said, why don't you go into academia? Why don't you, not me specifically, but like
*  Eliezer and people like that, why don't you go get PhDs? Why don't you go write formal papers?
*  Why don't you speak in front of a view? And the answer to this was that these people are not
*  inclined to listen to and understand and fairly judge and then these arguments, the field evolves
*  too slowly in this type of way because it takes decades to have any influence and at that time,
*  it's too late. And all because we treat it as theoretical, we treat it as like, you don't have
*  any evidence, we don't have to get things in. And the one place where they tested the theory was in
*  decision theory. So decision theory is an academic discipline, which asks, okay, how do we decide
*  what's the best thing to do? What's the best decision theory? And academic decision theory
*  basically has two decisions. They have evidential decision theory and they have causal decision
*  theory. The causal decision theory is the common sense decision theory you have, which is calculate
*  what's the expected value of doing X versus the expected value of doing Y. If X is higher, do X.
*  If Y is higher, do Y. That makes perfect sense. It's a sensible thing to try. The problem with this
*  is it's vulnerable. It has no way to commit to things, for example, without making physical
*  like punishing. It has to make credible pre-commitments in order to commit to anything.
*  Otherwise, it will just defect when it's time to go into the room and either cooperate with the
*  police or not because that benefits it directly. So like, TDT agents have these set of weaknesses.
*  They won't pay for a pitch hiker. They won't cooperate in the prisoner's dilemma. They can't
*  coordinate with each other very well. And they also respond to threats. And there are some other
*  problems as well. But basically, they have lots of well-known very bad points.
*  There's also evidence of a decision theory. That's what the theory said. You can think it will make
*  you happiest to have learned you just did it. Which is a very, very strange sounding proposal
*  for having decisions. And there are some obvious places where this does really, really dumb stuff.
*  What the hell are you doing? It also solves some very weird problems pretty well. And so there's
*  basically a lot of arguments back and forth about how this problem is better here, this problem is
*  better there, and how this is obviously wrong and that's obviously wrong. They're both obviously
*  wrong. And so a bunch of people working on the rationalist puzzle worked out this thing that's
*  called logical decision theory or functional decision theory. It's various iterations,
*  which is act as if you are choosing the output of the logical process that you are using.
*  And so this is just vastly better. Once you understand it, once you work it out,
*  and there are things that are being made the same way you're making your decision,
*  you should act as if you're making those decisions as well. Even if they were in the past, in the
*  future, or separate in space, and obviously you have no physical control over them. You still do
*  this because that will lead you to make better decisions. It will lead to better outcomes.
*  And so this is just vastly better. Once you understand it, once you work it out,
*  you work it out. And there have been papers, including 100-page academic length,
*  academically formatted, properly written papers, that are very, very good, address the previous
*  literature, address the concerns, go step by step, do all the things, and they just got to go.
*  And then to me, this is the place where our contribution was very clearly,
*  incrementally making progress on the existing scientific literature.
*  And providing a just really superior solution to a problem, rather than warning about it's
*  a terrible long-term danger. And just kind of ignore it. I guess we could have all pursued
*  a bunch of PhDs and tried to establish a criticality to at least half our lives to try to make people
*  listen, but it makes sense that we didn't. It's an important sign. We just instead,
*  just use other systems of knowledge. And meanwhile, as it builds up, together with people who decided
*  to work with him, his entire rationale is seen on the principle that, okay, I tried to warn people
*  about AI, but they couldn't think well enough to understand my arguments. They understood my
*  arguments better. This is what he was thinking. I'm not endorsing this theme of thought entirely,
*  but he thought, well, okay, we need to teach people to think, and we'll teach people to think,
*  they will be able to understand my arguments. He wrote the sequences and generally indicated
*  an entire community figuring out how to think better about things in general,
*  in the hope that we think better about this one thing in particular. I think it basically worked,
*  to a large extent, but not to the extent that they needed it to work in order for us to succeed.
*  And so, some of the success, some of it's a failure, but it greatly enhanced my life
*  and the lives of the people around me and their thinkers. So, I'm very grateful for that.
*  But basically, I'm thinking about this AI situation for a while, and I'm thinking to myself, okay,
*  we have to solve this very hard problem of keeping on making progress on, but also how close is AI
*  really? You know, no reason to panic, go about your life, it's fine. Then, you know, deep mind happens
*  and then OpenAI starts to happen. And then, you know, the origins of OpenAI, you can variously
*  look at Sam Altman, Elon Musk, and the interactions with Denis Tsavis, and concerns about Google,
*  and concerns about what Larry Page said about being a speciesist, and the other claims about
*  exactly what happened. But basically, this company gets founded by people who are worried about the
*  power of AI, the same way that Denis Tsavis found the deep mind, because he was worried about the
*  power of AI and the dangers of AI, because of the AI. This is what they say themselves. And so,
*  this entire time, we've been talking about info hazards, and holding back what we thought were
*  ideas that might enhance AI capabilities. When it turned out, the very fact that AI was like,
*  a danger, was a dangerous idea all along. Right? All of our ideas about capabilities,
*  yeah, it would have been somewhat exhilarating to share all of them right away, but like, this was so
*  much worse than all of them, if you find. But it turns out, right, it got people excited, like,
*  ooh, look, this might kill everyone. I've got to get involved in that. That was like really
*  unfortunate, but that's like what we saw. And then they started going down this line of these
*  things that we didn't have any ability to control or understand. Like, even in theory,
*  we just run one more computer outcome, and then like, couldn't stop it. Right? Like,
*  and even had organizations and various people invest in the effort to try and get voice,
*  to try and be able to influence it for the better. Which I think didn't have zero effect, but mostly
*  I think was a mistake. Very clearly a mistake. And then we shouldn't have been more outspoken
*  about how much we didn't want to go down this way from the beginning. But, you know,
*  that's one of the ridges now, right? Here we are. And, you know, the concerns I've been expressing,
*  you know, for a very, very long time now, 15 years in various forms, they're not mainstream exactly,
*  but they no longer sound crazy. They're no longer something you can just put out of hand.
*  And they now have a lot of very credible people, very much authorities and experts and key players
*  in the industry in North America. And that's a tremendous place to have gotten in some ways.
*  And now, you know, I also, we're in a world where like the alignment problem is much more
*  fluid and like, there are real systems to be worked on where you can make what appears to be
*  incremental progress. And a lot of the question is, does this incremental progress do anything?
*  Right. So like, a lot of the debate, one of the debates that we haven't discussed in the discourse
*  is the extent to which if you solve how to make the current systems do what you want,
*  if you figure out how to align them for practical purposes, now, to what extent are you developing
*  useful techniques and methods that then scale up and then will work in the future when we have
*  dangers? And to what extent, even if the current techniques don't work, are you learning key
*  information that will then allow you to develop the techniques in the future that will evolve from
*  the current techniques and those techniques? Or is this solving an easy problem that does not
*  actually help you with the hard problem? The hard problem is completely separate. Or something in
*  the middle where like, is it completely separate track? But doing the easy track first gives you
*  insight into what the hard track might look like. Right. You learn a thousand ways not to build a
*  light bulb helps you build a light bulb, but you can't actually build a light bulb that way.
*  And like, if you think you do, then you die. But if you know you can't, maybe it's very helpful.
*  There are a number of ways to go. There's a lot of arguments about it. And a lot of it's very
*  technical and a lot of it's very detailed and has a lot of branches and a lot of people think about it
*  very differently. If I understand you correctly, I think maybe one of the things I think maybe I see
*  most differently or interpret most differently is to what degree has sort of the Eliezer school
*  of thought won versus lost by shooting itself in the foot by becoming sort of accidentally
*  accelerationist. I'm guessing that maybe hinges on a core question around like, to what degree
*  are AI systems have sort of roughly the capability that we have now kind of inevitable given the data
*  and compute inputs already coming to exist. Because I guess my theory right now is like,
*  it sure didn't seem like it took all that long from the time we got web scale data and web scale
*  compute to get some pretty good working architectures, namely the transformer and derivatives.
*  And it's hard for me to imagine a counterfactual history where if deep learning kicked off in 2012,
*  you know, and that's whatever 10 years into Google or something, and then 2017, we get the
*  transformer. It's hard for me to imagine a 2023, where we're not like, pretty far down that path,
*  you know, kind of even if Eliezer had never been born or whatever. And so I guess I look at it as
*  a pretty big win that those that are doing the development at least have like a certain healthy
*  fear of what they're creating. Because it seems awfully easy for me to imagine a counterfactual
*  world where the technology continues to progress and like the leaders are just, you know, totally
*  uninterested in any sort of concerns, just don't want to hear about it. But it sounds like you see
*  it more the other way, if I understand like, more that if there were no Eliezer inspiring these
*  people to get involved, then what would your expectation be like that we just wouldn't have
*  this technology at this point in time or something different? I think it's unclear. But the way I
*  think of it is, if there's no deep mind, there's no open AI, there's no anthropic. If deep mind sort
*  of didn't have open AI, they would be moving wider and probably slower and in like fundamentally
*  safer ways. Right. Like Google is kind of insisting that they kind of like give you up and
*  deploy powerful systems to do real things as quickly as possible and loudly as possible.
*  There wouldn't be this like orders of magnitude expansion of money. Now, I don't think you keep
*  the lid on this forever. Right. As the amounts of money required to do interesting things
*  continuously goes down, at some point, some open source person or some relatively less funded lab
*  makes a GDT-2 style thing at some point, people see the potential, they start scaling up and
*  happen some number of years later is my baseline scenario. And then we're off the races again.
*  You can also argue that like, some amount of safety concern is inevitable the same way that
*  some amount of capability is inevitable. Because like, these arguments aren't hard to find once
*  you start seeing the thing. A lot of people who woke up to the risks of AI didn't come like in
*  the last year, right? Didn't wake up to them because we said do. Yeah, GDT was enough.
*  Like that was Hofstadter and Jeffrey Hinton and a bunch of other people. They don't really cascade
*  off. Right. Like they knew 30 years ago that if this happened, right, humanity was in deep danger.
*  Because it's just obvious to them. Right. Like it's like you see all the quick things back in the
*  50s about how this is obviously a danger. Alan Turbin, right? But what you, what they did think
*  was this is just not going to happen anytime soon. Right. We're not going to succeed. Right. I'm
*  chasing the mailman. I'm not going to catch him. They didn't think about what would happen if they
*  caught him or they were about to catch him until they were like, oh my God, I'm going to catch him.
*  Now what? Uh oh. It's actually really bad. I don't like this. Now what? And like we gave them a better,
*  you know, it made it easier to think, wow, but like how much better? I'm not clear. Whereas
*  the key concern is that like just because you're thinking that safety is a thing,
*  just because you understand you have to solve a problem, does that mean that you appreciate
*  the problem in a way that allows you to actually try and solve it for real?
*  And this I think is where it's despair. Like if we had you, like if we had full like
*  Meary style security mindset enable awareness of the true level of danger that I think we're in,
*  which is less than, oh yeah, right. But if they understood just how impossible the problems are
*  in front of them in terms of like game level difficulty, not in terms of like can't be at
*  all. And understood how important it was now that we're entering this realm where potentially
*  you just, it's like dangerous to proceed with the proper amount of caution and understood things
*  like it might kill you during the training run, not just after you deploy it. Understood like
*  the ways in which you had to structure these systems to minimize the chances that bad things
*  would happen. Understood that your solutions had to be like really, really robust and thought out
*  carefully and couldn't just be spelled out kind of vague pushes in the right directions. But like
*  the chance of that working is very low and like it's very hard to test to see if it's going to
*  work without doing something dangerous. They haven't thought hard about how to do that either.
*  And just generally like had a much, much more radical approach to safety.
*  Then I would say, yeah, the trade was worth it. But I don't think we're seeing that
*  particularly. I think that Anthropic was the one that claimed they were doing that pretty consciously.
*  But if you look at their investor pitch deck and you look at what Jack Clark and
*  Dario are saying and not saying, it doesn't reflect that level of paranoia. It doesn't reflect that
*  level of caution. And they may feel that with the competition they don't have a choice.
*  And I think you're right. But it's still they're not doing the thing that makes me feel better
*  about it. And there's a question of whether or not like someone who's marginally better makes
*  it a three horse races and if it's a two horse race it's making them better or worse.
*  Even if they are in fact better in that way. And it's not entirely obvious. It's always the question
*  of is a little bit of safety just a way to fool yourself in thinking that you're
*  not going to get yourself killed and getting yourself killed. Or a little bit of safety,
*  good. You can also look at it as if it weren't for our obsession with safety these things wouldn't
*  be useful. Right. Because like any work on alignment is likely to have immediate utilitarian
*  impact on the mundane usefulness of the current models. If we didn't have our LHF operating really
*  well on current GPT, we wouldn't have just GPT. We wouldn't have our current explosion investment.
*  What we have, we have this kind of like pretty useless thing that gives like not very useful
*  outputs and that will often say things that are pretty racist. Right. And then like what do you
*  do with it? Like Google's had this problem for years right where they were able to make
*  pretty strong chat box and products of intelligence pretty strong generative AI's. But they couldn't
*  align them well enough to make the consumer product they were willing to release. And so they had a
*  winch in those cycles. And so you could argue that like by focusing on these alignment questions
*  we enabled the capabilities that enabled the explosion and enabled these words of magnitude
*  investment. Otherwise we should be sitting here. So I think it's all very complicated.
*  I tried to think too hard about the counterfactuals from the past because we can't
*  you know, unwind time. That's the part of term here that's not realistic.
*  We have to move forward from the game board that we have. And so you know, you hope that these
*  people are sufficiently aligned and filled sufficiently concerned. Can you made so can
*  you work with and you hope that the game, you know, the actual structure of the problem is
*  that's what it can be solved. So what do we do now? Like you know, many parts to that question,
*  obviously, but you know, do you think that the Overton window is now wide enough open
*  that everybody can just be honest and say what they think? Do you think that things like
*  Eliezer's, you know, we should be willing to call in airstrikes on rogue data centers is
*  a good thing to put out there or sort of still too inflammatory and hard for people to hear that it's
*  just like counterproductive in its own way? So I don't want to be too dismissive of concerns
*  about that type of statement. But you know, it was my form yesterday, right? And one of the
*  things people were celebrating was free speech. What they celebrated was to point out there was
*  this woman in England, they got sentenced to 13 months in prison, I think it was, it was just over
*  a year for being a troll on the internet. Right? And like she just said mean things on the internet
*  and like social media. No one, nothing big or bad happened. Just being an asshole on the internet.
*  And like, she apologized to the prison in court for being an asshole on the internet,
*  offensive over a year in prison. So like for being an asshole on the internet,
*  men with guns came to her house, put handcuffs on her, dragged her to prison and locked her up for a year.
*  Right? Like, we enforce all sorts of laws and all of our laws are enforcing the barrel of a gun.
*  This idea that there is some sort of radical transformation because it's this different thing
*  we're going to enforce is kind of silly. It's kind of unreasonable. What's going on is that
*  the Eleazar is owning up to the implications of what it means to legislate, what it means to
*  prohibit, right? What it means to prohibit something from happening is that you will use force
*  if necessary. You will start by asking nicely, and then they use economic persuasion. But if necessary,
*  you will in fact use men with guns. Or if you are facing opposing men with guns, you will use men
*  with tanks or bombers or whatever it takes if necessary. There was an armistice in the United
*  States, we absolutely bring out the equipment. And what happens every time people defy the law
*  and just walk back down and start shooting at us, we escalate. We have to. It means to have laws.
*  It means to enforce things. And so, what we're proposing is law. Proposing is regulation.
*  Proposing is rules. And these are rules and regulations that are much milder than we would
*  apply to many things that are far less dangerous. This is not an outlier in terms of the degree to
*  which we are impinging on people's freedom of action. Certainly not freedom of speech or
*  privacy or anything like that. We're talking about restricting the very specific uses of a very
*  specific type of very technical hardware that can be manufactured only under the most developed
*  conditions of anything that man has ever created. It really wouldn't be very difficult to track.
*  We have strong export control on already. We're basically prohibiting this thing from going to
*  China as it is. And what we're proposing is that if you want to use that, it's trying to potentially
*  create a more powerful intelligence optimizer than a human to go into the realm where that's
*  possible. That you need to get permission to do that. And maybe we don't want to grant that
*  permission under any circumstances any time soon. And I think that is 100% the opportunity though.
*  100% very reasonable. And yes, it implies that somehow in theory, if Russia were to smuggle
*  enough A100s or whatever their two systems down the line successor is into a data center in Russia
*  and they were thought to be training Alan that might kill us all, we would do what you would do
*  if you thought that was an existential threat and you take it out. But that's not going to happen.
*  This is an absurd thing to say. Because the whole point of what I was trying to say is
*  if you make clear what you are willing to do, you don't have to do it. If you make it clear that
*  under no circumstances will you tolerate this very specific action, you will take whatever counter
*  measures are necessary and they believe you, they don't do it. It would be crazy to do it.
*  Why would you go down that path? Nobody wants that. Whereas if you don't commit to such actions,
*  then they do do it. If you just voluntarily say, I'm not going to build the thing, but
*  if you go that I'm going to hand-stop you, it doesn't work.
*  The hope is that simple economic rules and regulations and trackers and other such influences
*  are able to act on this very, very complex supply chain and this very, very advanced set of systems
*  such that this is not something anybody can just do. In fact, if you follow the logic
*  of the Chinese can't have these ships and they can't be allowed to train advanced AI systems,
*  well, then why are we letting anybody in the world train them on our data centers
*  and rent our compute whenever they want to do this? It doesn't make any sense. Why are we
*  encouraging open source models that are powerful enough that China can literally just copy
*  and run? That doesn't make any sense. At some point in capability and you have to draw that
*  line. You can't simultaneously think these things are as important as you think they are and not
*  put restrictions on them. Even if you don't think there's any people's right, there are many other
*  good reasons to try and do this anyway. But certainly if you think there's an extension risk,
*  you know, everybody understands, I think at this point, the only way to prevent these things from
*  coming into existence that doesn't impede tremendously on our liberty and on our economic
*  value and our economic success. And that might actually work is to target chips, target
*  concentrations of chips, uses of chips, target the training of intense training runs, large compute
*  runs, and frontier models. Exactly where we draw that line, you know, the 10 to the 23th
*  flop, the 10 to the 25th flop, the 10 to the 6th flop, and we try to define exactly what capabilities
*  they're allowed to have, we try to use evaluations to try and see what can we do in a gray zone
*  where it's committed but only under some conditions, 10 stab at gray zone, how do we adjust this over
*  time as algorithmic improvements occur. These are detailed questions that we need to sort out that
*  I don't have the best answers to. But I don't see an alternative proposal on the table
*  that could possibly work, right? To not put some limit on how many faults we need in a training run
*  or some similar restriction and to enforce that restriction absolutely,
*  unless you have specific permission and only direct the specific permission under very, very
*  clear detailed circumstances at best is the only way that we have. Any other method of control
*  will be circumvented, right? You can try to say, okay, don't turn them into agents, you can't use
*  our bt's. It's 100 lines of Python code. That's not going to work. You can say don't use them for
*  this particular application. Okay, those are just words. How do you intend to do that? It's not going
*  to work. There's nothing else that anybody has proposed. There's any chance it will work.
*  And we are very fortunate in this sense, right? We are very fortunate that the thing that enables
*  AI training runs is in fact the most complex, hard to manufacture thing that has ever been created
*  in the history of the world and that basically friendly countries that doubt US economic dominance
*  control the entire supply chain. They did not have to be true, but it is true. And given that,
*  we have a unique opportunity to exert real control over what happens next that gives us a chance.
*  We have to take it. I want to just quickly get your thoughts on like any other promising paths
*  to safety. I'm a big fan of mechanistic interpretability work on its own merits,
*  even if it's not a great contributor to safety, although it seems promising to me in its own way.
*  And then also kind of want to get your take on. So what do we do from here, right? If you want to see
*  those kinds of rules put in place, you hear fairly similar things from the likes of a Sam Altman,
*  as you noted earlier. But then what do you do about that? Do you follow Tyler Cowen's advice and start
*  going to the journals? It doesn't sound like you're too bullish on that. Do you like start
*  writing more Eliezer style fiction, you know, go back to the Terminator and try to scare the voters
*  into electing the right people? Like what's you know, do you kind of go lobby at some agency?
*  I don't see anything that I love as an alignment approach. And it's super optimistic. But I see a
*  number of things that we can track that would at least find us ways not to align an AI that would
*  alert us to dangers that would help us understand the problem at a minimum. And maybe, you know,
*  lead to something that would lead to something that would lead to a solution or something like
*  that. And maybe we'll get really lucky when we think we'll work out there than I expect.
*  Interpretability, I think is one of the duelous technologies that, you know,
*  because interpretability also helps you utilize the AI and helps you make the AI more capable.
*  So it's not entirely safe to work on that. But I do think it's worth working on. I do think it's
*  a good idea. And I do think that like a significant chunk of our resources should probably go to work
*  for a response and interpretability effort. So far, it hasn't gone that great. We've made some
*  strides, but like we are not very good at understanding GPT-2, using GPT-4. And the way
*  I think of this as okay, you interpretability starts helping you when GPT-5 can understand GPT-6.
*  Right? Or GPT-5 and a half. The whole goal is for something to understand something smarter than
*  itself. Because otherwise, you have a chicken and egg problem, right? Like you don't get to
*  trust the thing that's telling you the information. So if I can interpret something that's more complex
*  than me, that's amazing news. That's the target we have to hit. Right now, we haven't hit a vastly
*  easier target. Right? And we're not anywhere that close to hitting it, but we can try. And in general,
*  like, you know, I talk about what is the thing to do, the regulatory open-grip window. This has to
*  go hand in hand, obviously, with a ton of interpretability and other safety work. Because if we don't
*  figure out the solution to the problem, eventually, our work will be able to catch up to us.
*  We don't have infinite time. No matter what we do, we have to solve these problems as best we can.
*  We're going to have to unless we take our shot. All we're trying to do is buy time. Right? We
*  understand this. And like maybe we'll get super lucky and the algorithmic improvements will,
*  I guess, curve out. And then we'll be able to stay here indefinitely. But even then, like,
*  every day we make the conscious choice not to break those limits. And that, again, won't last forever.
*  And also, there are other things to worry about. We have to eventually do this.
*  So we have to solve these problems. In terms of what we, you know, individually can do,
*  I definitely think it's a case of some of us should do one thing and some of us should do the other.
*  Like, some of us should work on safety directly. Some of us should try to solve these problems.
*  Other people should work on, you know, lobbying and trying to talk to people with decisions.
*  Other people should write academic papers. Other people should write blog posts.
*  Other people should try to just orient, understand the world, communicate as best they can.
*  Other people should work within the labs. You know, it's not, we don't know which of these things
*  is the best approach. I am in fact going to make an effort to get some of the papers ready
*  because, you know, I don't have that much hope that it's going to work. But it's, we will learn in the
*  attempt, right, if we make this year's attempt. At least we will learn why it fails or how it fails.
*  And we'll be able to demonstrate, oh, look, this failed. And here's it failing.
*  And we will also probably think well in the course of doing that exercise,
*  right? It wouldn't be as efficient as thinking well without that exercise. We would look for
*  something else. That's pretty good. It's a reason people write papers and figure out the dimension.
*  I do despair about the speed of the whole enterprise. I do despair of, you know, Tyler
*  is asking for economic style papers because he's an economist. But that will only convince economists,
*  right? And then you have to like repeat this process 20 times because different people
*  have different perspectives. And a lot of them are going to be less amenable than
*  Tyler's. Like Tyler's is relatively a good fit. You should be able to argue carefully
*  in his mode a lot of the outcomes. And I believe that the need to do something is vastly open to
*  him, right? If you had to prove a model went to journals that food was going to happen,
*  I think you'd be in a lot of trouble because it's the kind of thing they just reject
*  inherently for just not being scientific or something or not having the right data or evidence.
*  But I think there's other models that you can in fact get pretty into the mathematical model
*  and it leads other people to want into. I don't think it's really a natural exercise that you
*  would do if you were just trying to think the truth. But if you need to go through this process,
*  you can do it, right? And maybe it's actually a good idea. And like, again, division of labor,
*  I think there's a lot of people who want to help with this problem, who have a variety of skill
*  sets who are kind of growing up their hands, right? Like the point that most frustrates me
*  is at the end of every podcast, people ask him, so what do I do about this? If I'm terrified,
*  if I think we're all going to die, if we don't do something, I want to do something. What's the
*  something that I should do? And like, he doesn't have anywhere to send money. He doesn't have
*  anywhere to work on a concrete problem. I mean, he has to like, you know, try to orient, try to think
*  about the problem. These are good things to suggest, right? Try to figure it out for yourself.
*  But like, you do have to do better. Right? I do think there are now a number of errorizations
*  that like, are rapidly expanding that are like, have their, have net positive impact and expectation,
*  like have their hearts in the right place. I do think you have to worry about dumb money.
*  But if you go in to a charitable ecosystem, or like an ecosystem of work, and you start throwing
*  around money without understanding it, and a lot of people do the same thing, the incentives get
*  all worse. And like bad, bad actions are not good. So like, you can't just feel that stuff
*  without thinking about it carefully. You have to orient, you have to get your own independent
*  opinion. You can't just trust whoever is telling you things or that those damns the badly.
*  But absolutely, there should be support for a lot more alignment efforts. And in fact,
*  we have very good news today. I don't know if you saw it when the podcast came out, but OpenAI made
*  an announcement that they're devoting 20% of their required compute so far, there's gonna be a lot
*  less than 20% of their computer over the next four years to scale up their computers as much as
*  possible. It doubles every year, but still 20% of their existing computer over the next four years
*  to working on alignment to try and generate a more automated, more advanced alignment process.
*  I have deep steps for the strategy they are pursuing. I think that as something that could
*  possibly hope to scale to solve for human level or beyond human level intelligent alignment,
*  it's pretty hopeless. Or not necessarily hopeless, but none of the things they're
*  announcing they're going to work on address the things that make that problem hard.
*  The hope is that they might make it easier to try and address the hard problem because you will be
*  able to iterate faster on the problems when you build the tools and the compute will potentially
*  allow people to try things that aren't listed there. It's basically on the base that I build
*  a human level alignment researcher to help with their alignment work. And as I understand it right
*  now, they have two days until processing the announcement, it's not free. This doesn't quite
*  mean actual human level alignment research. If that was true, it would be like what is commonly
*  proposed as the worst idea, which is get the AI to solve alignment for you, which basically means
*  put the AI's first human level problem as the alignment problem, which is one of the
*  hardest places to ensure that your AI is actually aligned, to test to see if it's doing the thing
*  you want, to see if it understands what you want. It's a great way to get absolutely killed.
*  It's a great way to absolutely get a misaligned system, so much more likely than so many other
*  ways. But when they actually, I think met, was simply have a human level way of evaluating
*  whether a given output seems a lot. And humans are pretty bad at this. So getting an AI as good
*  as a human, a generic human, doesn't seem like a crazy thing to ask for. However, I still think
*  it's a bad idea and I'll be, I haven't written about this so I don't understand it yet, right?
*  Like I understand things by writing about them. But basically, the only way to align
*  for real on human preferences is to get humans who are thinking deeply and well
*  about their preferences and you deeply understand the questions involved. You can't learn from
*  training data and human feedback things that aren't in the training data and human feedback.
*  They're less, they're more sophisticated than what you're being given until the point where
*  you can pull off the complexity. So like if you have a very large amount of data
*  and a very large amount of feedback, you can draw inferences and correlations and build up a model
*  of all of that where you is, you know, this thing under gradient descent that is more powerful than
*  the thing that's driving the individual components. But there's still an upper limit
*  if you're trying to decode what was going on, but if it wasn't in the thing that you were decoding,
*  it won't be there to find. So you need, you're going to need it not just like the equivalent of
*  the random person that you're paying a normal hourly wage to go chat with the chatbot or to go
*  just check for some offensive language or something. You need someone who is pretty intelligent,
*  who is thinking carefully about all of the implications of what they're saying
*  and is willing to give you pretty sophisticated feedback. And as a parent, this echoes very much
*  in like when you're observing and trying to get feedback to your children,
*  right? Like you need to be very smart, very, very careful about exactly what feedback you give to
*  your kids. And with humans, it's much, much worse because they're operating in a much less compute
*  and like infinite words of magnitude less data and less cycles than AI. So every little bit is going
*  to have so much power to reshape their world and their way of thinking. But you have to think very
*  carefully on so many different levels about, okay, what caused that output? What is this person
*  thinking? What does this person understand and not understand? What are these person's incentives?
*  What can I say in response to that that will cause their update to be the update that I want?
*  Because one of the things that I increasingly discover is that by thinking about AI is you think
*  about humans because we are neural networks too. And we also gather in data and use our compute to
*  try and update our connections to have the best output possible and achieve our goals.
*  And a lot of it rings very true, although obviously also a lot of it's very different,
*  but it can help you really think about yourself and others and understand how to use the analog
*  of these tools to get a better model and to get better outcomes. And so when you're dealing with
*  a child, you have to think very carefully on multiple levels about, okay, what's the important
*  salient things here? What do I have to do? How would he respond to various different things I
*  might say? What would that lead to? What vibe would that cause in the conversation?
*  Same with Alan, associate with vibes, people associate with vibes. What might this cause him
*  to be curious about, not curious about? Am I like that? What are the big five moves ahead,
*  big ten moves ahead? Try to figure these things out. And you are on a limited compute budget too.
*  You have to do all of this instantaneously. You have to do all this continuously. And you're doing
*  enough life at the same time. And I think that you've had. So, you know, when you're dealing with
*  an AI, you have some more leeway because you have so many more individual data points. You can afford
*  to be less precise in some sense. But if you're trying to train something that's going to be much
*  smarter, more capable, then I really do think you have to be very, very precise and careful
*  because otherwise good heart's laws won't bite you. Right? It's going to optimize
*  to the actual procedure that's being followed, not to the thing that you're trying to mimic.
*  And that difference is going to be very, very bad. Right? Partly because of manipulation,
*  but probably just because you are going to be wrong about what you want. This means if you develop
*  AI to help you with the AI in this sense, right? Like you have a serious problem because it's not,
*  you are going to good heart's laws, I mean, it's convinced somebody to good heart's law already.
*  And so like you get met a good heart. And met a good hearting is not good. Right? Like if you,
*  if you have a telephone, effectively, right? It's like, I try to explain to,
*  like, if you try to explain to Nathan, right, like what's he wants and cares about.
*  And then Nathan watches, watches, you know, Alice and Alice like tries a bunch of things. And Nathan's
*  like, no, no, no, he wouldn't want that because of that. So if he would want that because of why,
*  he would want that because of why. And then Alice tried to teach Carol. And like,
*  Carol is not going to know what the hell is going on. Right? Like Carol is going to have no idea.
*  Like this is not, it's not going to preserve. Like it's not going to be like distilled carefully
*  and preserved. So I don't know that there's that much hope in doing this, but it does provide the
*  ability to iterate on various techniques and try things and test things very quickly. You can learn
*  a lot by doing that. I don't know. We don't have a solution. So it's, it's easy to pigeonhole and
*  like shoot down anything that you propose as, oh, that will never work. But what will? Right?
*  The answer is I don't know.
*  Well, that's probably, you know, an appropriately sobering point to wrap up for today. I think,
*  you know, for long form, but still only 1%, you know, as long as what it took you to read
*  to create it, your blog and the regular updates there that just kind of run down all of the news
*  and give, I think some of the clearest, you know, again, most concise analysis is one of the go-to
*  places on the internet for keeping up with everything that's going on with AI. And I
*  appreciate all the hard work that goes into it. Last question, I think for me today is just,
*  what other things do you recommend that people look at? You know, that could be other safety
*  approaches that we haven't talked about or particular individuals or groups that you think,
*  you know, are kind of deserve more attention, respect, resources, support of any kind.
*  And then what about just other sources that you think are particularly enlightening? You know,
*  if somebody wants to not just read you as a consumer, but kind of get toward your level,
*  what are the places that you would recommend that they go that you find value in?
*  Yeah. So as always, you have to think carefully about what you care about. And, you know, what
*  makes sense for you, don't just copy, right, what someone else is doing. But I would say, you know,
*  I cultivated my set of sources, you know, because that's the set of sources that's helpful to me.
*  But if you want to get involved in orienting around these problems more seriously, so first of all,
*  you can ruthlessly steal from them, right? You can literally just follow my rationalist list,
*  you can follow my AI list, you can look at my people I follow, and you can follow them
*  if they seem to be AI oriented. There's also a bunch of people who are not AI oriented,
*  because I have other things I follow as well. But again, like, if I was starting to orient,
*  I would look at the people who are in AI, that you think are processing information well,
*  or offering good ideas, look at what their information sources are, and put it makes this
*  openly accessible. And then I would chicken choose, based on my own reading, which of these
*  are helpful to me, which these are not helpful. Similarly, I would look at various blogs, right?
*  So like, if you're reading my weekly blog, whenever you see something like,
*  you can decide whether or not that source is something you want to systematically follow.
*  Same way I do, when I see it in your source, or whether it's a one off. And, you know, you build
*  up a series of assets that way. So the next question you have to ask yourself is, how technical do I
*  want to be? So like, there's several different types of AI developments you might want to follow.
*  Right? There's what I call mundane utility, right? The standard capabilities, procedures,
*  of like, what AI can do this week. And for that is a very different, almost often not very
*  overlapping set of people you would follow. And there are never places you can get that
*  at any level of specification. Then you have the discourse follow, people who are engaged in
*  making arguments with each other. And think carefully about how much of this you actually
*  need. Will be my actual advice. Like, I cover it, right? But if you aren't covering it, like,
*  you should only follow that to the extent that either you want to like, evaluate the arguments,
*  or you want to make the arguments, and get involved in the arguments, and try to shape the
*  discourse. And that might not be why you want to get involved, right? If you want to work on
*  technical stuff, you probably don't want to devote too much effort to the discourse, and vice versa.
*  So you probably want to choose an area of specialization, to a large extent. Like,
*  I've chosen to specialize someone in discourse, because that just sort of, someone had to
*  situation. You know, a few weeks of that concentration is probably
*  enlightening, but after a while it repeats. So you've got your AI debate, which is the nominal
*  topic of today, and debate and discourse. And then you've got the AI actual work on the alignment
*  problem, right? And then you've got like the policy questions, which are associated strongly
*  with the debate. So the question is, you should decide where you want to focus your time and effort,
*  and to what extent. You might want to cover all of it, but you, these are just, you just want to
*  focus on one of these two things, not the other. And, you know, we definitely need more alignment
*  with this, but we need more people who are trying to solve the actual problem. And so there's another,
*  the other reason you might want to be paying attention is, you know, you might want to
*  contribute money, either in investment or contributions, or you might want to otherwise
*  know like which things deserve support or to deserve local support, including like anything
*  from alignment efforts or regulatory effort to an academic paper or a place of grading them.
*  There's a wide variety of efforts now to advance AI safety in this sense. And, you know, there are
*  some AI organizations, some similar areas where you can find a number of projects. You can also
*  often find links to these things from the Armament Forum, Google's Twitter posts, stuff like that.
*  And there are formal places like by speed grants where you can try to get involved more explicitly
*  directly if that's what you're interested in. But again, I would say don't try to jump into that.
*  Don't try to just say, okay, let me just write check tomorrow, because, you know, just it's in
*  the right area. This is a lot more of a complex situation. There is no equivalent of, you know,
*  doctor stock orders or some other like generic good people you can definitely get money to. And
*  maybe it's not optimal, but you have to worry about what you're doing. So you need to orient
*  first, unfortunately, if you're doing any of that, and then see what probably gets you excited and
*  see, understand what you're doing, and then proceed from there. I would say, you know, if there is
*  one limiting factor right now, more than any, it is people willing to work on the problem
*  directly, the technical problem itself. I said that isn't short of supply. There are only a few
*  hundred alignment researchers on the planet. This is ordered to magnitude wrong. And there are any
*  number of people who are eager to help you pursue that goal if you are serious about it and like
*  can demonstrate skill. And you are thinking well about it. The thing worldwide is hard. So,
*  you know, the key is that to orient carefully. I wish I could be more specific. I wish I could
*  be more useful. And I am so trying to figure these answers out despite spending most of my time
*  on these types of problems. But it is a really hard problem. I would say that, you know, in terms of,
*  you know, what I am doing, there are quite a lot of people who are attempting to like write in real
*  time about AI. And I would discourage trying to be one of those people, especially if you are not
*  already pretty enmeshed in the situation. Just because it is kind of a rock star-y thing where
*  there is a lot of people who want to be that person and where you are competing for attention
*  with others. And so, you know, write to help yourself understand. Like, do not write anything.
*  I think writing is great. But do not try to write to help you or others keep up with the
*  pace of development. Write more in terms of orienting about more fundamental, like slower
*  moving events. And then maybe post it somewhere or maybe not.
*  Sveem Ashuets, thank you for being part of the Cognitive Revolution.
*  Thank you so much. Yes, in some ways, the Cognitive Revolution is exactly what I am worried about.
*  But in other ways, it is exactly what we need. So thanks for having me.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
