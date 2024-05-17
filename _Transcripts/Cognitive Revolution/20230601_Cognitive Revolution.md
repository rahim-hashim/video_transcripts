---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 5217s
Video Keywords: []
Video Views: 1169
Video Rating: None
---

# Where Are the Moats in AI? With Nathan Labenz and Erik Torenberg
**Cognitive Revolution "How AI Changes Everything":** [June 01, 2023](https://www.youtube.com/watch?v=yVezX3cxwgk)
*  So, moat one, GPT 3.5 turbo is the best value in the LLM game today.
*  Moat number two is branding and just trust.
*  Moat three is the feedback loop that they have.
*  Nobody has the volume of LLM usage that OpenAI has.
*  Four is pricing power, $2 per million tokens.
*  You got to be using a lot of tokens.
*  Five we kind of talked about again, privileged access to cloud compute.
*  Six, GPT 4 itself.
*  You know, they're using GPT 4 in really interesting ways that are going to give them advantage.
*  Moat number seven, team and talent density.
*  Satya said to their head of research at Microsoft, how the hell did they do this with a couple
*  hundred people?
*  We've got all these people and like, how are they kicking our butts so much?
*  Moat eight, insane distribution and partnerships.
*  The customer list is growing rapidly.
*  Number nine, yeah, network effects.
*  If I have something that's working with OpenAI and I'm thinking about exploring something
*  else or switching, first thing I'm going to try is the exact same task.
*  And if it doesn't work, then I'm going to be like, oh, this kind of sucks.
*  Hello and welcome to the cognitive revolution, where we interview visionary researchers,
*  entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Tornberg.
*  So let's get into it.
*  You wrote this thread on Moats.
*  People are asking you a ton about Moats.
*  Where are the Moats?
*  How should people think about Moats?
*  The best kind of comparable vision that I think is intuitive that seems likely to be
*  right in terms of how this broad AI utility intelligence market plays out over the next
*  few years is it probably ends up looking quite a bit like cloud.
*  And you might even say in the limit, it could be cloud.
*  If the algorithms are all trending toward commoditized or lots of stuff is getting open
*  source, open source is making all this progress, then eventually maybe the same stuff runs
*  everywhere and it's just how many computers do you have determines how much AI utility
*  you can deliver.
*  I don't think it's quite that simple, but it does seem like it's shaping up on somewhat
*  similar lines where in cloud you have big tech oligopoly has half-ish of the market
*  When you look at AWS, Microsoft, Google, Oracle, wherever you want to draw that line on who
*  is the top tier cloud providers, they have about half.
*  And it seems like if you were to just ask what is the breakdown of where inference is
*  served over the next few years, it seems like it's probably similar.
*  This time it's probably Microsoft and OpenAI that are in the lead in terms of they've got
*  the best product and they've certainly got the cloud to back it up.
*  So they probably lead and then Google, DeepMind, which is also their cloud is powering Anthropic
*  is probably next.
*  And then AWS is a little behind at the moment, but has hugging face and has plenty of stuff.
*  Plus they just have tons of people already using their cloud.
*  So for many kind of homespun open source, you've got to host it somewhere.
*  So it's going to be a natural place.
*  And then you've got long tail besides that.
*  And that could be still on those same public clouds, but different service layers.
*  It could be your own on-prem solution if you're an enterprise that's supported by wherever,
*  whoever, and even on consumer devices.
*  It seems we're seeing a lot of trends toward that as well.
*  So in kind of keeping with my theme of like everything everywhere all at once, I think
*  there's no reason to suspect really that like any significant pools of compute would not
*  be used to power AI over the next few years.
*  And so that market structure seems like it probably lines up.
*  For that not to happen, somebody would either have to like run away with things dramatically,
*  which doesn't seem like it's currently happening.
*  Like OpenAI is ahead, but it doesn't seem like they're light years ahead.
*  And they're like maybe 18 months to two years ahead of open source, which is to say like
*  what they were offering commercially 18 months to two years ago is about what open source
*  has got to now.
*  Not to say that open source will catch up to where they are in the next two years.
*  That remains to be seen.
*  GPT-4 is going to be harder to match.
*  It takes more compute if nothing else than GPT-3 was to match.
*  The cost of GPT-3 quality models is now under $500,000 if you go to Mosaic from scratch.
*  Bring your own trillion tokens of whatever data you have and you can get to GPT-3 quality,
*  smaller model, more intensive training, but under $500,000.
*  Meanwhile, GPT-4 is still rumored to be $100 million.
*  That's not going to be so easy for the open source folks to replicate.
*  But anyway, it seems like it's kind of headed towards shaping up like the cloud market.
*  You've got the oligopoly that kind of combine the hardware infrastructure and kind of services
*  layer, which in this for now is like the models themselves.
*  They're kind of the core differentiator there.
*  And then you've got a ton of other things too that kind of make up the other half of
*  the market.
*  And so just like AWS certainly has motes in general in compute, all these big players
*  have motes to varying degrees.
*  And I think that's ultimately pretty obvious.
*  That whole no motes thesis, it's like, I don't know, I just think that hasn't really held
*  up over the last couple of weeks under deeper scrutiny.
*  And the negation of that memo isn't true either.
*  I think that memo had a lot of things going forward in terms of the flourishing of what's
*  happening in the open source community.
*  But it's still not the case that everybody doesn't need OpenAI anymore.
*  It's far from the case.
*  The folks that are trying to implement this stuff in medicine, they are not that cost
*  sensitive.
*  They want the best thing.
*  it.
*  And Google is trying to get on their level and it certainly seems like they can or can
*  get real close.
*  So that's just not something that anybody in the open source community has any credible
*  claim against.
*  And you can sort that out at the level of like a quick demo.
*  You don't need a deep evaluation process.
*  You literally can just use common sense and ask some questions to GBT4 or to like the
*  new Medpalm 2 out of Google.
*  And you'll taste the difference between that and like whatever the latest woolly animal
*  named model might be.
*  Again, there's a lot of modes.
*  We could break it down from a lot of angles, but that position is like, I think, pretty
*  secure for the foreseeable future.
*  Zooming out, it's interesting to think about when you have a new kind of platform shift
*  or technological breakthrough.
*  There's some that have led to more sort of open source or open source would have bigger
*  market share and some that have led to the opposite.
*  It's interesting to think about the kind of characteristics that make either happen.
*  Yeah, it'll probably continue to evolve as well.
*  And I'm certainly no scholar of kind of earlier software waves.
*  Certainly haven't studied any of those with anything close to the intensity that I've
*  been studying the AI wave.
*  So much depends right now on context.
*  People ask these questions like why?
*  So how would you decide?
*  That's a question I've been getting a lot.
*  Let's say you are, you're maybe at Weymark or you're in some other context.
*  How do people decide whether they're going to use an open AI or an open source model?
*  And I do think like most of the, in most contexts, it does seem pretty clear that you do perfectly
*  well with an open AI product.
*  Like Athena, for example, we're on the AI advisor.
*  The explicit strategy if we're going to try to do some new task and set up some automation
*  to power some task, it's always just start with GPT-4.
*  There's no reason to start anywhere else.
*  It's clearly number one.
*  It's number one on all the leaderboards.
*  It follows instructions the best.
*  It's not that expensive.
*  It is a little slow, which can be a little cumbersome when you're trying to test stuff
*  out.
*  But it's the fastest path to just the application of this raw intelligence to your problem to
*  demonstrate whether or not you can even automate this task.
*  GPT-4 is going to give you the fastest path to that.
*  And of course, there are some things that you can't do that maybe you could fine tune
*  a model for them.
*  That's a whole other scale of project.
*  So that could be one reason.
*  You might be able to dial something in better if it's a narrow application and you're really
*  kind of focusing in on a use case.
*  There are reasons to go away from GPT-4.
*  That is one of them.
*  But the reasons that people tend to think more often I think are really not great reasons
*  like cost.
*  It's pretty cheap, actually.
*  And it's especially cheap if you consider a total cost of ownership because I can get
*  in there and take most common tasks and get the AI performing reasonably well on it with
*  a few rounds of prompt engineering often in like 30 minutes or less.
*  And what is the cost of the person's time?
*  How many runs of this task automation do you need to be planning for before it is going
*  to pay back even to just spend a handful more hours looking for a cheaper option?
*  What is the end of your task?
*  Most tasks people are not trying to scale to the billions or even to the millions.
*  So you think about the cost per token on a GPT-4, three cents per thousand tokens in,
*  six cents per thousand tokens out.
*  Maybe just for simple math, average that to four cents per thousand tokens.
*  That's four cents per two pages of text processed.
*  The kinds of tasks that we're setting up are like, can we take a long transcript of a
*  call that we have with a client and convert that into a condensed information rich profile
*  of the client that we can then put in the assistant's hands as they're beginning a
*  relationship to give them as much context as we possibly can?
*  And that cashes out to however many pages, but it's not that many pages.
*  We might be able to power this for a quarter.
*  It used to take four hours.
*  So we're saving a ton.
*  When people get very obsessed with these cost questions, I'm often like,
*  most people don't care if they're saving 90%, 95%, or 99%, especially if it's all kind of new.
*  The costs I just don't find to be that compelling.
*  There are some applications where if you're doing high volume generation and you have a low hit
*  rate, this is another thing I've been highlighting for people.
*  With Waymark, we have a pretty tight process.
*  We've been doing this before generative AI.
*  So we make these advertising marketing videos for small businesses.
*  Typically, they're like 30-second commercials.
*  They might run on TV.
*  We've been doing this before generative AI.
*  Now the generative AI writes the full script, picks all the images, layers on the voiceover,
*  but we still had that structure even before GPT-3 popped up.
*  So the ratio of how many of your generations are ultimately useful to people
*  is a reason that you might end up wanting to go towards some cheaper model.
*  So like Jasper, for example, they're now on the Mosaic homepage as a client.
*  They've been an open AI client, obviously from the beginning, helping with all this marketing copy.
*  They're probably spending quite a lot.
*  So for one thing, they have some real budget that they can maybe take a chunk out of if they can
*  fine tune their own stuff.
*  But then I also suspect that a big part of what's going on there is because a lot of their stuff is
*  fairly open-ended, like give us two words and generate a LinkedIn profile or whatever.
*  I'm guessing they're seeing a lot of generations and people are maybe just using it in a rifle
*  through way, seeing it kind of like what Sue Hale told us with Playground where people are making
*  10% of their users are making more than a thousand images a day.
*  It sounds like that's kind of the pattern that's going on at a Jasper to some degree.
*  And that's a big contrast to like with way markets, basically like one in three,
*  maybe one in four, maybe one in five, probably varies a little bit by cohort.
*  Of the videos that we generate ultimately gets rendered and downloaded.
*  So people are not sitting there rerunning it that many times.
*  And so like the economic relationship between the cost of that generation and what they're getting
*  for it, where they're going to go spend thousands of dollars on a TV campaign,
*  that ratio is totally fine.
*  And then when you get to task automation, your hope is that you're going to get to basically
*  like use all of the work.
*  And that's like fairly feasible.
*  When we do these transcript to client profile workflows,
*  the goal is like not to have to run it a bunch of times.
*  And from what we're seeing, it looks like, yeah, it's basically going to work.
*  Our workflow is going to be immediately after the call.
*  Again, this used to take a couple of days and whatever, people get bogged down and
*  the things would take hours to write.
*  Now you've got basically instantaneous transcription.
*  You feed that into the AI process that chunks that.
*  The biggest limitation with GPT-4, biggest two limitations are context window is still limited
*  to 8,000 and it's kind of slow.
*  When you're chunking these long transcripts into bits in order to summarize them, in order
*  to then have a kind of unified summary that you can process into whatever format you want,
*  it can be like a little bit of a friction point.
*  It can be a little bit slow, but it is the kind of thing that we're basically targeting.
*  You should be able to use 100% of this output.
*  We're not seeing any instances where it's like, what is this unusable garbage?
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Hi everyone.
*  I wanted to take just a moment to share another podcast that I've been enjoying recently,
*  the AI Breakdown.
*  As anyone in AI knows, the pace of progress and all the new releases are relentless.
*  I call myself an AI scout and I work overtime to keep up.
*  But these days, even I can't keep track of everything.
*  The AI Breakdown helps me make sure that I don't miss anything important
*  by curating news and analysis daily.
*  Host Nathaniel Whittemore, aka NLW, quickly highlights the top stories of the day
*  before going deeper on a single topic of interest.
*  Episodes are usually 15 to 20 minutes and he releases them every single day.
*  Now, it's not easy to keep up with a daily release schedule and still maintain your sanity.
*  So I really appreciate how NLW maintains a curious posture and avoids rushing to judgment.
*  A big part of the reason I'm inclined to recommend the show
*  is his willingness to sometimes say, I don't know.
*  I think listeners will find the AI Breakdown to be a great compliment
*  to the long form deep dive interviews that we create.
*  So I encourage you to check it out.
*  The link to the AI Breakdown with NLW is in the show notes.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  The human review layer at the end is more to be like,
*  okay, I just talked to this person for 90 minutes.
*  Does this thing, you know, miss anything that seems important?
*  And we do see issues like that where it's like, yeah, this person said this,
*  and it does seem pretty important and the AI didn't quite pick up on it as a key point,
*  didn't represent it in the final thing.
*  So it's not like it's a flawless process, but you can go from just having got off the call
*  to looking at a draft of your final document in a couple of minutes and then read through it,
*  figure out what rings.
*  Mostly it's good, but there might be something that doesn't quite ring true
*  or something that was missed and then you're kind of done.
*  Still in that whole process, it's like the cost of the AI is very small.
*  We had a person that sat there and talked for 90 minutes.
*  We're going to have all these things going on.
*  There's no reason to try to save a couple more pennies at this stage on that process.
*  It's all about driving the quality.
*  We wouldn't even consider an open source model.
*  There's just no reason for it.
*  Now we're also probably not going to be that huge of a customer because
*  not that many clients coming in, but you start to extend this to other things where there are
*  points in the business where there's real scale.
*  The next one downstream is client matching with the candidates.
*  They may be onboarding 100 clients a month.
*  You may have 200 candidates in the pool that have already been filtered and gone through
*  a whole wringer.
*  I think they hire sub 1% of initial applicants.
*  To do every analysis there is like 20,000 of these sort of comparisons.
*  This client profile and this assistant profile, is that a good match?
*  It's not easy to scale up to 20,000 of those with human power.
*  In practice, I think historically you would more kind of look until you found one that
*  seemed good and kind of have to stop there because it just isn't time to do the fully
*  exhaustive version.
*  But the AI can run overnight and do that more exhaustive version.
*  It's still going to be cheaper than the human powered thing and it might even be better.
*  I wouldn't get on quite yet and say it's going to be better, but I think it can match pretty
*  readily and the prospect for it to be better is definitely there as well.
*  And to make it more personalized, to then turn around and be like, all right, now write a
*  blurb introducing this person to the client.
*  You can enhance the client experience in ways that don't even necessarily...
*  I mean, already necessarily about the fundamentals, but just like, let's get this
*  thing off to a good start by kind of introducing this person in a really nice personalized way.
*  Yeah, anyway, in all that cost is not an issue.
*  I can tell you that.
*  Do you see the gap?
*  You mentioned Open Source about two years behind.
*  Do you see that gap widening or shrinking over time?
*  What do you predict?
*  I don't know.
*  It probably goes back and forth.
*  I think it will probably a yo-yo effect.
*  I mean, the Open Source line is rising all the time and then you probably have more punctuated
*  big next releases from the key players.
*  Perceived public gap probably closes and then widens again and it won't be obvious
*  like necessarily is the overall gap given what they have internally that the rest of
*  the world doesn't know about is that like shrinking or narrowing, I bet would be pretty
*  hard to tell still for a while.
*  And it seems like they are probably going to cluster.
*  There's a weird tension right now between the fact that the leading companies,
*  namely OpenAI and Google DeepMind and Thropic are pretty clearly like
*  coordinating on some very meta level and kind of saying very agreeable statements to each other
*  about how like what's most important is that we do this safely and that everybody can benefit
*  from it and Google's CEO Sundar just said the only race that matters is the race to safety or
*  something like that.
*  We should find that exact quote.
*  That's not quite what it was.
*  But he's specifically trying to say we are not going to get into an AI race, which I really view
*  honestly as great validation for the entire AI safety movement and even specifically the EA
*  AI safety movement because it's very easy to imagine a counterfactual where
*  people running the cutting edge AI companies were just totally dismissive of big picture
*  AI risks and the fact that you've got basically all three of the leaders who have a real,
*  you know, aware like a demonstrated awareness of the, you know, and take and seem to be pretty
*  credible in taking seriously these, you know, tail X-risk scenarios.
*  I don't think that that necessarily happens in a counterfactual world where there's no
*  EA movement or where there's no like Eliezer.
*  Their influence seems like pretty clear there.
*  I certainly agree.
*  I think the question there is, you know, actions speak louder than words and how much will the
*  actions match?
*  Like if they were in a race, would they be acting any differently?
*  Will they act any differently and how so?
*  Like how extreme?
*  Because in some ways, if you're a little cynical, you could say it's, you know,
*  it's reverse psychology in this really effective way, which is what, you know, say it's not a race
*  as a way to potentially throw it off competitors or not, you know, threat to betters, but also
*  on regulatory side, like we have this weird dynamic where for other technologies, you know,
*  like let's say crypto people said, hey, this is like the next great thing.
*  Like everyone needs this.
*  And then on the regulatory side or media side, you see responsive.
*  Hey, actually, maybe this is bad or maybe this isn't great or it's too powerful or it's
*  too dumb or whatever.
*  But with AI, it was really interesting thinking about the hearings and thinking about kind
*  of the response of media and regulatory.
*  It's like people, you know, I think some accuse them of marketing, like by emphasizing the
*  how dangerous this thing is, it also emphasizes how powerful it is.
*  And some people with media and, you know, government are saying, hey, like it can't do
*  as much as you say it.
*  Like they're kind of down.
*  They're more scared of social media and misinformation and the complaints they have on
*  social media, depression, etc.
*  Than they are on an AI.
*  Like I would have expected people to be much more concerned than they are.
*  It seems that most concerns happen from within tech.
*  And I wonder if that's unconsciously a form of reverse psychology in the sense that because
*  tech is so internally worried about it, maybe that encourages them because they're like
*  somewhat anti-tech or somewhat contrary to tech to be less worried.
*  I think, you know, Sam Altman's statements about what kind of regulation they recommend
*  have been pretty clear and not, you know, not always interpreted in good faith.
*  So, you know, he's literally explicitly said we think the regulation should apply only
*  to the leading companies that are doing the biggest models, you know, the biggest compute
*  budget, you know, training runs.
*  And we don't want to interfere with companies, open source, you know, research, startups,
*  etc.
*  And that seems like a very reasonable position for the, you know, for the regulatory bodies
*  to take.
*  And I hope that they take something along those lines.
*  Like that seems pretty sane.
*  So, yes, there could be some amount of, you know, hype marketing in that, but really,
*  they don't market at all.
*  You know, they like they don't need to market the businesses.
*  You know, the phone is ringing off the hook.
*  When I talked to Mosaic, you know, ML guys recently, Jonathan and Abhi, they were like,
*  yeah, we can't run long.
*  And they also said we're starting.
*  He's like, if you want to be a customer, you better hurry up and call us because
*  we are starting to get to the point where we're making serious, like tough decisions
*  between research and customers.
*  And basically, you know, they're not going to cut research to nothing.
*  They know they can't do that.
*  So, you know, it's like you're going to you might have a waitlist at Mosaic, you know,
*  pretty soon.
*  So, you know, you the the level of spend that you have to commit to OpenAI to get some,
*  you know, some commitment from them of some attention to you has risen dramatically.
*  When I bought it, you know, just over a year ago, and we were already a retail customer,
*  like on the API and fine tuning models and stuff.
*  But as we're starting to get more serious and I was like, I kind of want, you know,
*  a tutor or like a consultant, you know, especially on the inside of OpenAI.
*  You know, what do I have to do to like get you guys to like take it, you know, every
*  other week call with me.
*  It ended up being at the time, twenty five hundred bucks a month was the like service
*  package that we bought into.
*  And now they don't even offer that.
*  And, you know, to get that kind of, you know, account manager or whatever, you're at least
*  into six figures, if not like a quarter million, you know, kind of upfront commitment that
*  you're going to spend that with them to have them like take your calls.
*  So I don't really think he needs to go in front of Congress and call for regulation
*  as a marketing strategy.
*  You know, they could they also like downplay their shit.
*  You know, you want to if you want to say that they, you know, are hyping everything.
*  Look, the launch statement that Sam Altman put out on GPT four day.
*  One of his very first things was it seems more impressive at first than it really is,
*  which is is true.
*  You know, it is honest.
*  That's not a statement, but you know, you don't really see tech CEOs downplaying their major
*  launches on launch day.
*  And yet they did that in a very like clear way.
*  You know, Sam's say I don't know if Sam Altman, but Sam is, you know, tweet.
*  It's go something like here is GPT four.
*  It's our most capable model yet.
*  Like all of our models, it still makes stuff up.
*  It still, you know, has major weaknesses and it's, you know, appears more impressive
*  at first than it ultimately is.
*  Like that is not, you know, how most, you know, that's that doesn't sound like a hype
*  cycle to me or like, you know, a marketing ploy.
*  I think they really mean it.
*  You know, I think that at the end of the day, I think that's becoming increasingly clear.
*  Now, you could really ask and I was thinking about this earlier today, too.
*  You know, you read their governance statement from this last week and you get down to the
*  bottom of it.
*  And the last point that they make is we think that it's counterintuitively dangerous to
*  not develop this stuff because the fundamentals are all going this way.
*  And that means that it's increasingly easy to develop these, you know, powerful systems.
*  And if we don't kind of keep the gap between what's possible and what is, you know, what
*  exists, like somewhat narrow, then we may have these like sudden super disruptive events
*  in the future.
*  If somebody, you know, achieve some breakthrough unexpectedly and all of a sudden, you know,
*  it drops into an unprepared society.
*  And it's like, okay, I don't know if I really followed that to the same conclusion that
*  it almost kind of seems like they're saying somebody's going to develop AI so powerful
*  that it's dangerous and better us than them, you know, for, I guess, basically all, you
*  know, other thems that could it could be.
*  I don't necessarily want to sign on to that or endorse that.
*  But I do think, you know, everything they're doing is pretty consistent with that.
*  They do seem to be trying to rise to the occasion.
*  And, you know, they definitely could be jamming stuff out faster than they are.
*  They even, you know, they have the part of the charter to which I mean, people obviously
*  at this point don't trust, you know, them on necessarily anything, but it is in the
*  charter that they will combine forces with another effort that they believe is, you know,
*  credibly close to AGI rather than compete with them.
*  You know, that's a hell of a commitment to have made, you know, whatever in 2015 or
*  whenever they came up with the charter that, you know, at that time, it must have seemed
*  like a pretty distant worry.
*  But, you know, they've had that online for a long time.
*  That is not like they just released that, the statement that's been there for years.
*  Yeah, going back to your like the open source and closing, you know, the opening and closing
*  of the of the closed and open source gap.
*  I do think we'll see probably these releases again come in some kind of cluster
*  where, you know, GPT-4 and kind of Palm 2, you know, came in a pretty tight window.
*  I would bet that in the future that will continue to happen as a reflection of the fact that
*  leadership at these companies is genuinely concerned with, you know, the possibility
*  of an AI race genuinely doesn't want to create that dynamic.
*  And so we'll kind of talk to each other behind the scenes a little bit and say like,
*  you know, can we kind of ease into this stuff together so we're not, you know, you're going
*  to have a next generation thing, we're going to have a next generation thing.
*  If we kind of bring those online around the same time, we can, you know, the oligopoly
*  is not going to get too disrupted.
*  Microsoft and Google don't have to like, you know, battle to the death.
*  They can both kind of advance similarly.
*  And, you know, that's probably a really good thing as long as, you know, they don't
*  collectively still like blow up the world in the process.
*  You know, but it does seem like definitely way better than a different dynamic where
*  they're like sworn enemies, you know, won't talk and, you know, are trying to one up each
*  other, which we saw a little bit of that earlier this year, but it seems like they've kind of,
*  you know, Google has not taken that bait.
*  I think to their great, I think they will be vindicated in the end for saying like,
*  all right, you go ahead, but we're going to do it when we're ready.
*  And, you know, so far it doesn't even seem like they've lost significant market share,
*  as far as I can tell, like maybe a couple points, but not like, you know, they're still
*  dominating Bing in terms of just raw search volume.
*  So, you know, it seems like even from a shareholder standpoint, people were not that,
*  you know, the consumer wasn't that ready to switch where like, you know, corporate
*  requirements would dictate you like must ship immediately.
*  So I think their judgment has been actually pretty good and vindicated.
*  And, you know, again, I think that's by extension of another vindication of the kind of EAA safety
*  crowd, because, you know, he didn't, you know, I don't think he grew up thinking about this
*  kind of stuff.
*  So he needed some, you know, people intellectually to have done that work to be able to tap into it.
*  You know, if there's no literature, I don't think these people are coming to these, you know,
*  some of them might, but like, soon are probably not, you know, on his own totally,
*  you know, totally organically.
*  I agree. It's very influential literature.
*  Marx too is very influential literature.
*  I'm just teasing.
*  Let's go deeper on sort of the respective kind of assets.
*  You know, we're talking about NBA the other day, you know, we're talking about like the
*  Nuggets chances versus the Boston versus the Heat.
*  We talk about their relative strengths and weaknesses and kind of where they're at now.
*  Let's do something similar with some of these players that we're talking about in terms of like,
*  how do we see things playing out based on what are the facts on the field, so to speak,
*  in terms of people's relative strengths, weaknesses, opportunities, etc.
*  We'll just run down the quick nine moats that identify for OpenAI and then we can kind of
*  compare that to Google.
*  Most of them are basically the same and OpenAI is just a little stronger, you know, in a number
*  of these categories, it seems like right now.
*  But also you could make the argument that, you know, that Google is stronger in some of the,
*  maybe the most important categories as well.
*  So, Mote1, GPT 3.5 Turbo is the best value in the LLM game today.
*  So, you know, earlier I talked about how like GPT 4 is generally a huge savings over a human
*  powered process and, you know, if I'm new to AI and trying to make stuff work,
*  there's really no incentive for me to go anywhere else.
*  Well, if I were going to go anywhere else, they happen to have a 60x cheaper model that is instead
*  of, you know, 4 cent, no 50x, I guess, whatever, instead of 4 cents per thousand tokens, it's 0.2
*  cents per thousand tokens, which is $2 per million words.
*  And that's what powers the chat GPT free tier.
*  And I said it's the best value in the utility LLM game today.
*  I think that's probably still true in there's a new leaderboard that I've started to
*  follow called LMSys.org where they literally have like chess style head to head battles between
*  language models and keep track of ELO ratings.
*  So users go in, you get, you know, for the same input, you get the response from different models.
*  You choose the winner.
*  They keep the score.
*  And GPT 4 is, you know, at the top of the power rankings.
*  Claude is number two and Claude Instant has, which is kind of the the anthropic answer to
*  the chat GPT has actually taken third place recently and put turbo into fourth place.
*  So arguably you might say at this point that Claude Instant could be, you know, even
*  slight edge over GPT 3.5 turbo for the best value in the game today.
*  But either way, you know, they both have great value.
*  They're both, you know, they're both cheap.
*  They're easy.
*  They're fast.
*  They can do a ton of stuff.
*  They can handle the marketing, you know, copy tasks for the most part.
*  You know, they can return formats pretty reliably.
*  They can't do the advanced stuff of GPT 4.
*  You know, this is like the difference between like bottom 10% on the bar exam and top 10%
*  of the bar exam.
*  That's like, you know, 3.5 to 4 is that is that leap.
*  But, you know, still bottom 10% of the bar exam.
*  You can do a lot of stuff.
*  You can process a lot of data.
*  You know, you can, you know, you can organize a shopping list.
*  You know, there's plenty of things that you can do, you know, without
*  being quite powerful enough to pass the bar.
*  So that's a great product, you know, and it's still better than all of the open source
*  imitators.
*  And in fact, all of these open source things, maybe not all, but like a lot are using
*  GPT output, you know, from open AI and just like imitate training on that.
*  So, you know, they are like getting somewhat close on some test domains, but, you know,
*  they're not really that close to even and the leaderboard will tell you this, you know,
*  that's a blind head to head, you know, user call the winner process.
*  You know, they're not that close even to, you know, the second tier 5%, you know, price
*  of GPT 4 version of open as products.
*  So just having that means like there's not that much opportunity for people to come in
*  and like steal share, you know, on pure price reasons.
*  They have not left the door open there all that much.
*  You know, so people could do it for maybe other reasons, you know, control fine tuning,
*  you know, ideology, you know, data, not wanting to send data out over certain, you know,
*  boundaries, whatever, but, you know, they've got a great commodity product in today's world.
*  I'd say, you know, again, it's pretty clear at this point, open AI and Anthropic are the
*  two leaders in that category.
*  Mote number two is branding and just trust the, you know, for all of the complaining that has
*  been posted on the internet about how like chat GPT is, you know, to this, to that, you know,
*  I mean, and you hear it from all sides, right?
*  It's simultaneously depending on who is, you know, trying to embarrass it, it can be both,
*  you know, to like white supremacist and to woke.
*  You can kind of see that almost regardless, I think of perspective, you can see like unwanted
*  biases or unwanted behaviors in it.
*  But the alternative in the open source world is just way worse, you know, if you are a corporate
*  customer, if you want, you know, a sort of radical free speech experience and you're,
*  you know, not a major company, then you can go the open source route and do, you know,
*  whatever you want.
*  But if you are the kind of business that is thinking about maybe putting a chat bot into
*  your product experience somewhere, you know, you don't want it to get too adventurous, you know,
*  was joking with a guy opening.
*  I was like, yeah, these, you know, the sort of open source radicals, like really overestimate
*  the corporate appetite for large language model adventure.
*  You know, nobody wants their own, you know, personal Sydney experience.
*  Nobody wants that kind of embarrassment.
*  And when you can get, you know, at $2 per million tokens, good quality, pretty reliable
*  service, you know, from OpenAI, like then it's kind of burdens kind of on you to figure out,
*  like, well, why did you do something, you know, why would you or why did you do something
*  different?
*  So I started saying that, you know, people used to say nobody got fired for going with IBM.
*  And now it's like, that might be true for a few of these top players, because your AI might still
*  embarrass you.
*  But at least you can fall back on like, look, I used like the industry standard, like these
*  guys, you know, they spent six months, you know, working on safety of GPT-4.
*  Like, what do you want me to do, boss?
*  Like, if we're going to use this kind of shit, there's going to be some risk.
*  But I, you know, I kind of made the safest choice I could with OpenAI or Anthropic, like,
*  you know, so again, that's a moat, right?
*  And Google's, I think, going to get there too soon.
*  Certainly they have the like, I think, you know, trust and kind of gravitas that a corporate
*  buyer would believe them that like, they do, you know, have good standards in place.
*  And, you know, again, when it's so cheap, like, why am I going to go, you know, put myself as a,
*  you know, a CIO or whatever in a position where I don't really know where this, you know,
*  exactly how this open source model was trained or by whom, or like to what degree it's really been
*  battle tested.
*  Like, I'm going to do that to save a little money.
*  And by the way, am I even really saving money?
*  Depending, you know, maybe, but I'm certainly going to be putting more man hours into it,
*  you know, than I would if I was just doing, you know, the simple thing.
*  So, you know, I don't know, it sounds kind of tough.
*  Mode three is the feedback loop that they have.
*  And this is where OpenAI is currently quite out in front, depending on exactly what you think
*  about, you know, some of the alternative strategies, but, you know, nobody has the volume of LLM usage
*  that OpenAI has, you know, that chat GPT has, you know, Bing's doing some decent volume I've seen,
*  but not as much as chat GPT.
*  And they're, of course, you know, powered by GPT-4 anyway.
*  So they're getting, you know, this data, they now have terms of service that say if you use them
*  via the API, that they will retain your data for a short time, then delete it and not use it in
*  training.
*  But the free tier of chat GPT by default is used in training.
*  And you can opt out of that.
*  Now they just added that as well.
*  But, you know, by default, you're opt in.
*  And if you want to opt out, you can opt out.
*  But they're getting more, you know, raw usage and feedback data than anybody else.
*  And they have a well-honed product development process, you know, that is humming.
*  And others are finding that, you know, kind of hard to reproduce.
*  Even somebody like Bing, you know, comes out and finds out, wow, you know, we didn't expect that.
*  And, you know, some of those things you're like, I don't, you know, there's, there was some really
*  pretty flagrant breaks in the Microsoft process.
*  I've gone down that rabbit hole.
*  They tested this thing for months in other parts of the world.
*  They had users report in their forum such behavior from the bot as ultimately graced the cover of
*  the New York Times.
*  They failed to detect it because like one part of the organization wasn't talking to the other or
*  whatever.
*  The Microsoft employee that responds in the forum, last I checked this was also online
*  in the Microsoft forums.
*  The person who responds, who works at Microsoft seems to not know about the AI powered search
*  experience at all.
*  And it's like, doesn't even know what the person is talking about, who is saying like your chat bot
*  is accosting me.
*  And, you know, that's all kind of documented as of like late 2022.
*  Then, you know, they launched the thing in 2023 and then you have things that are as simple as like
*  you got the date wrong.
*  They, I got the date wrong.
*  The user corrected the AI on the date and that was enough at launch for whole things to go off
*  the rails, you know, and I think it's a huge, people should be very clear on the difference
*  between like a jailbreak, you know, where you can trick chat GPT into saying a bad word or
*  whatever.
*  And, you know, and that's a problem.
*  But I've never seen chat GPT turn on a user, you know, and that's a whole different level
*  of like failure of alignment, you know, failure of control when the user is trying to break
*  your control measure versus like failure of basically, you know, of decent engagement with
*  the user in the first place.
*  So qualitatively different thing.
*  All that story, you know, is to say the product feedback loop is pretty important and, you know,
*  this stuff does not just like magically cohere into a well-behaved AI by accident or, you know,
*  even with like moderate effort, it seems to take a lot of effort.
*  So OpenAI is just like crushing it in that regard.
*  Anthropic, again, has a unique approach with their constitutional AI system where
*  they use kind of self-critique and like synthetic data to basically try to get, you know, the same
*  level of control as if they had, you know, the user base.
*  And it seems to work quite well.
*  So that may be something that other people could, in fact, in some ways they are ahead in terms of
*  like their safety profile, not their raw capability profile.
*  But in terms of their safety profile, in some ways I've seen them be ahead.
*  I've also heard from others that maybe that's not the case.
*  So it's probably mixed, you know, the surface area is so huge that you can be ahead and behind
*  at the same time in different areas.
*  And that's almost certainly the case.
*  But nevertheless, it does seem to work quite well.
*  They also do a pretty good job of avoiding hallucinations.
*  At one point, I think they did a better job than OpenAI was.
*  But again, with GPT-4, you know, they've improved a lot.
*  But like you could previously see with chat GPT versus Claude, you could kind of see these
*  situations where chat GPT would still, I asked a question about like a property tax in one
*  Massachusetts town one time, and it made up a rate that was not the real rate.
*  It had all the structure and conceptual analysis of property tax generally right.
*  But it made up a rate at, you know, the key moment that was false.
*  Whereas Claude said, for example, if the rate were, you know, it just gave like a
*  nice reasonable round number.
*  And so there are some ways in which it does seem like the anthropic method is, you know,
*  at least competitive, if not in some ways, you know, maybe superior.
*  So those two seem to be kind of at the forefront of that.
*  Actually, Character AI, you know, has a really good feedback loop as well.
*  They're kind of a dark horse in this whole game playing a bit of a different game.
*  They're the only the one that comes to mind is like having a real, you know, tight,
*  at scale product feedback loop.
*  Google doesn't have it yet.
*  They should be able to get it real quick, whether or not they can really iron out all
*  the sort of, you know, stand off all the barnacles on their sort of product flywheel.
*  I guess still remains to be seen.
*  As of now, they've not done it.
*  If you look at the leaderboard, Bard is down the leaderboard, not because, you know,
*  they don't have the raw horsepower, but because, at least as far as I can tell,
*  they have not shaped the product in the same way that the, you know,
*  the best in that category have.
*  You know, they can match on things like medical question answering.
*  You know, GPT-4 and Medpalm too are both like expert level on these benchmarks.
*  So they can definitely get to the point where, you know, they can do high level stuff,
*  but they don't have this like unified product that kind of does everything and,
*  you know, knows how to handle all these different situations.
*  It's like Medpalm is dedicated to medical question answering
*  and it can't help you, you know, with whatever random search queries you have
*  or, you know, just be your like general sort of, you know, chat advisor.
*  It's, it is specialized and, you know, fully end to end fine tuned for that domain.
*  And that arguably could be good.
*  You know, you, somebody might say, well, geez, do we really need these like all-purpose AIs?
*  Maybe like a bunch of specialist AIs could be, you know, arguably a better overall architecture.
*  I think Google is definitely kind of playing that both ways.
*  Like they're going to have their general open chat bot that you can talk to about anything,
*  but they're also going, they're taking Medpalm too, like hospital groups and stuff like that.
*  You know, they're not, they're not even messing around with some base,
*  yeah, some base model.
*  They're going to only take, you know, the good stuff.
*  So four, I kind of talked about in my, in this thread, four is pricing power.
*  I think we've probably covered that, you know, at enough length.
*  You know, $2 per million tokens.
*  You'd, you got to be using a lot of tokens.
*  And another way I was thinking about this was, this is actually kind of interesting math.
*  If you were to try to compete at that price point, you would have to serve a hundred billion tokens
*  to pay for one employee.
*  They make $200,000 in revenue for a hundred billion tokens served.
*  So I'm, you know, rounding down from the, you know, we're so back San Francisco AI
*  salaries there to 200,000 calling that one employee.
*  By the way, you know, whatever electricity, you know, compute costs you have, you know,
*  Microsoft gets its share out of that too, right?
*  Out of that $200,000 for a hundred billion tokens.
*  I mean, a hundred billion tokens is like a ridiculous amount of stuff.
*  You know, like they're training these models on like a trillion tokens.
*  That's like a kind of general ballpark of like what a, not like a GPT-4, but like a,
*  you know, a llama type good open source project might train on today would be like roughly
*  a trillion tokens.
*  So you're talking about like 10, you know, and people also talk about that as like the
*  scale of the whole internet.
*  So you're talking about like generating text on, you know, maybe 10% of the, you know,
*  the scale of the internet for $200,000.
*  Like just who needs that many tokens, you know, it's going to be hard to like build
*  that many businesses competing at that level.
*  You know, I just, I don't see how you, you know, how you build another world-class team
*  that can, you know, they can hit at that level only to then, you know, be like, okay, cool.
*  Now we've, now we're here.
*  Now who needs a hundred billion tokens?
*  And we need to, by the way, we need to find a lot of people who need, you know, a hundred
*  billion tokens each to have a chance.
*  You know, I don't know.
*  It's tough.
*  The volume of that really kind of blows my mind.
*  I think there are things, you know, you'll see like, you know, just mass summarization,
*  you know, just, just summarizing everything, just processing everything, you know, quality,
*  just this stuff is a, it's cost effective for quality control, right?
*  I mean, every time you ever been on hold and said this thing is being called being recorded
*  for quality control purposes, like now it is cheap enough that you could actually implement,
*  you know, the quality control on literally every call perhaps.
*  So, you know, there will be, I don't think we've by any means like exhausted our imaginations
*  when it comes to what are we going to use these tokens on and a hundred billion that's
*  input and output.
*  Also, it should be noted.
*  So like just scanning through tons of shit, you know, and just kind of post processing
*  information, I think is going to be a huge trend.
*  There's a lot of tokens in that, but still, you know, how many, how many businesses can
*  compete at that kind of commodity layer when it's that cheap, it seems really hard to,
*  you know, I don't know if I'm a VC, I'm not sure I want to invest in that.
*  Five, we kind of talked about again as well, which is privileged access to cloud compute.
*  You know, you can only serve as much of this as you have compute.
*  There are starting to be compute shortages.
*  I've heard stuff from a friend at Google who has said, you know, demand for compute
*  is now starting to kind of bind a little bit.
*  They've made one of the biggest, you know, decade long investments in computing infrastructure
*  and they're like, you know, starting to have to ration some stuff.
*  It sounds like at Google.
*  The same was true from what we heard from OpenAI in like middle of last year.
*  They were like, you know, we have to make some choices on our product line because,
*  you know, even with our partnership with Microsoft, we just cannot scale our access
*  to compute as fast as we would like.
*  So there were a couple of different, you know, things that were happening at the time,
*  but Dali 2 blew up and that was like, they had kind of decided, yeah, we got to kind
*  of delay the launch of some other product to, you know, just put all the resources behind this.
*  And, you know, again, that's the Azure cloud that they're building on, right?
*  So like your moat is pretty apparent.
*  Where they are already hitting capacity constraints after, you know, hundreds of billions of
*  capital investment.
*  I mean, that's about self-explanatory as it gets as a moat, I suppose.
*  You're going to have a hard time accumulating anything on similar scale.
*  And, you know, that doesn't mean you can't build a business out there,
*  but it definitely means they have a moat.
*  They're using GPT-4 in really interesting ways that are going to give them advantage.
*  If you believe that there is a, and Anthropic has kind of said some similar things,
*  by the way, that going back to five, Anthropic partnered with Google, you know,
*  Huggingface partnered with Amazon, like all of you, I forget who they partnered with, but somebody.
*  All of these, you know, kind of leading labs that don't have the compute, you know, they're all
*  entering into strategic partnerships for it.
*  So there's kind of a musical chairs game going there that, you know, isn't necessarily one to one,
*  but how many, you know, preferred model providers, you know, does AWS ultimately take on?
*  Probably not that many, I would guess, right?
*  Anyway, so coming back to GPT-4, if you wanted to make a case for why are the leaders going to run
*  away with it and widen the gap between themselves and open source, maybe one of the best answers
*  would be that they already have these advanced models that allow them to scale all sorts of
*  things were previously really hard to scale.
*  And OpenAI has given us a little bit of a glimpse into that with their recent Interpretability
*  publication where they kind of use GPT-4 to look at itself and try to figure out what are the neurons
*  doing within, actually, I think they might have been looking at GPT-2.
*  I think they were using GPT-4 to look at GPT-2, but still, you know, kind of looking at like,
*  you've got all these neurons, you don't know what they do.
*  So how do you figure out what they do?
*  Well, they basically run a bunch of text through the model, keep track of what is making
*  each individual neuron highly activated, and then kind of pull that out and look at it in batches.
*  In our Tiny Stories interview, which we just recorded, it's really apparent there,
*  they have these small models, and when they do that process on these smaller models,
*  the concepts actually kind of jump off the page and are very apparent.
*  And you can see like, oh, this one seems to be responding to like animals, because it's like
*  dog and cat and bird and like, okay, like I see a pretty clear category there, like this thing
*  fires when there's an animal. And they showed a bunch of examples of that.
*  As the models get bigger, that stuff gets more messy, hard to figure out.
*  Some of the concepts remain quite clear and interpretable, but others, you're looking at
*  this like, okay, so this and this and this and this all caused this to activate at a high level.
*  I'm not really seeing anything here that is super coherent or like an obvious concept that I could
*  label, but they're using GPT-4 to automate that process. And just because there's even in GPT-2,
*  there's already like a billion five neurons or whatever, or parameters different than neurons,
*  fewer neurons, but still there's a lot of, there's plenty.
*  So, you know, you just scale that, how else are you going to scale it? Right? So they,
*  you think about that kind of thing and just the mega scale that they can apply to kind of enriching
*  these data sets, cleaning data sets, you know, the next they were talking about, like, it's not all
*  just about scale. It's also about quality. Well, how are you going to clean your data set? Right?
*  You're going to probably go, you know, crunch through with GPT-4. Anthropic has kind of lent
*  some credibility to this notion with their like leaked, I think accidentally with their leaked
*  pitch deck, which said something along the lines of we think the companies that fall behind in the
*  like 25, 26 cycle, maybe never catch up. And, you know, if you're like, well, what the fuck does that
*  mean? It sounds kind of ominous. I mean, I think it is kind of ominous, but if I had to interpret
*  it, I would say it's that the models themselves become this engine of advantage that if you don't
*  have access, you know, you can't perform the next, you know, level of research at the same,
*  you know, at the same pace. And there, you know, you could, I do generally believe that the like
*  calls for regulation are pretty sincere, but that is also maybe where things like start to kind of
*  diverge. And you're like, oh man, you know, if certain things are required, you know, you like,
*  you have to perform some, you know, exhaustive check. And you can do it with GPT-4, you know,
*  at like at one level of scale, whereas if you don't have GPT-4, you can't do it. You know,
*  then that becomes kind of an interesting challenge. Maybe you could imagine a regulation where,
*  you know, they are required to kind of share certain value, you know, certain capability with
*  other developers or something along those lines. So it's not like they can, you know, control the
*  whole stack, but as it stands, by the way, their terms do not allow the, all of these models that
*  have been trained on chat GPT output, basically they all violate the, the open AI terms. So if
*  you actually didn't want to go and commercialize that and you're like, oh, look how smart I am.
*  I took this open source model, trained it on chat GPT output. Now here's my business. They'll, they
*  could just straight up sue you and probably win because you, you know, just took a bunch of their.
*  Now the good follow-up question there would be, well, what about humanity as a whole, assuming open
*  AI for having taken all of our shit and running the, you know, the first training process that created,
*  you know, the model in the first place? Like, is it, how is it, how can it be that they're allowed
*  to take all of the human data and create a model and then prohibit you from taking from their model
*  to train a downstream model? That does seem a bit weird. And, you know, I'm not sure that that exact
*  position is ultimately going to be tenable because for multiple reasons, for one, it just sounds kind
*  of insane. You're going to have a hard time defending it. And second, you know, if you do
*  want to say, you know, we're not trying to like slow down research, but research comes to a point
*  where it kind of depends on this, like very rapid, high quality processing of information to try to,
*  you know, build good, reliable data sets or, you know, have some China has just put out these
*  guidelines, right? That are people are basically like, they're impossible to meet. And the reason
*  that they, you know, they're trying to, it does not appear to be racing into an LLM future.
*  They may be racing into a, you know, AI for military future. You know, I don't know about that,
*  but in terms of like putting chat bots online, they do not view that as the space race right now,
*  as far as I can tell. On the contrary, they're more worried that it's going to like talk about
*  Tiananmen square or whatever, and they don't want that. So they're like, you as a developer
*  are responsible for your shit. You know, I would really recommend there's a great
*  Seneca podcast on this recently with a couple of guests. We can find the link where they, you know,
*  a couple of China scholars, like do the reading of what the CCP has said about this. And they have
*  issued statements and they put these standards out there that are like not easy to me. Like
*  your data has to, the data that you use to do the training has to, you know, be like reliable
*  or like, you know, have quality. I mean, they're using adjectives, right? So what does that even
*  mean? It has to not violate anybody's, you know, intellectual property claims, which, you know,
*  that legal regime, I don't think it's sorted out in China either. It has to be, it has to,
*  your data alone has to like meet these quality standards per their, you know, statement. And then
*  everybody's like, well, that's impossible. How could we have web scale data that meets those
*  standards? And the answer is if you own a cloud and you have GPT-4, then you can do that data
*  cleaning next time. And they're already to a point where they could even, you know, probably just
*  do the next model trained on like almost pure synthetic data by just kind of taking what is real,
*  maybe transforming it, you know, filtering it and transforming it into something totally synthetic,
*  taking all that synthetic stuff, doing the training on that, and then being like, look,
*  we're clear because here's the entire dataset that we trained GPT-5 on was all now, you know,
*  there is still that link in the chain, right? It was all kind of made by GPT-4, which was in turn
*  made by, you know, with whatever. And eventually it does get down to like, obviously human, you
*  know, data was the, you couldn't have got here without it. But I do see some potential for that
*  kind of dynamic where it's like, okay, there's a new standard, you know, your data has to be squeaky
*  clean or whatever. And it's like, huh, shit. Now there is kind of a lock-in effect because
*  nobody outside can really do that unless they have this model, you know, like speed factor to
*  kind of power that kind of thing. And, you know, are they going to share that? You know, as of now,
*  they basically say no per the terms, but maybe they could be prior to, maybe they could change
*  their minds. But anyway, there is some, you know, this is why GPT-4 is a moat. Because,
*  you know, it does have qualitatively different ability that like, you know, they might even
*  be able to use to accelerate their own work. And, you know, they don't have, as of now,
*  nobody is forcing them to share that to accelerate others' work. And they also, they've reduced to
*  the logits, right? Not reduced, but in the past, you could, maybe even still with the earlier models,
*  but with like GPT-3, you know, you go in and use the API. When you get that API result, they would
*  give you not just the one token that was chosen, but up to, I think, the top five most likely tokens
*  with the like percentage that each was assigned in that prediction step. And then under the hood,
*  they've actually generated a number for all 50,000 plus tokens in the vocabulary. So they don't have
*  to do any extra work to do that. They're doing all that work for all 50,000, you know, candidates
*  anyway, picking one, which could be the top one or could be like semi-randomly chosen. But then
*  they would return to you, you know, here's the top, however many choices. And that was really useful
*  if you wanted to like study the model. It was also really useful if you wanted to train a
*  imitator model, because it's way more information to say, you know, the token was the, that's one
*  thing. But then to say top token was the at 47%, you know, next was a at 32%, then was an at,
*  you know, 9% and then, you know, whatever. You can learn a lot more from that, you know, much,
*  much deeper level of disclosure. And they've now closed that off. There is no
*  logits returned with GPT-4. So that's kind of the, you know, raising of the drawbridge a little bit.
*  You could still, you know, get your GPT-4 outputs and try to train on them. But, you know, it's,
*  they've made it that much more difficult to do it than it used to be.
*  Mode number seven, team and talent density, you know, whatever, they're, they are definitely a
*  absolutely killer team. There was just a new story where apparently Satya said to their head of
*  research at Microsoft, how the hell did they do this with a couple hundred people? We've got all
*  these people and like, how are they kicking our butts so much? And, you know, that's a probably
*  complicated question to answer, but no doubt they do have extreme talent there. And I've seen it in
*  kind of every part of the organization as well. You know, the folks that we interacted with when
*  we're in that $2,500 a month, you know, consulting engagement, you know, all very, very good.
*  You know, the business contacts, like they know their technology in a way that you just can't
*  sustain, I don't think, if you get really, really huge. The business guys that I've talked to there,
*  like they don't have to check with the team, you know, they know what's what. So I do think it's
*  just extremely, you know, strong organization, top to bottom. Mode eight, you know, insane
*  distribution and partnerships. You know, the customer list is growing rapidly. Here's a list
*  of customers recently announced for open AI intercom, Wix, Morgan Stanley, Shopify, Conacademy,
*  Atlassian, Zoom, Brex. That was just one little thread, you know, from the, one of the business
*  guys there, you know, they've also got a huge partnership with Bain. I think they just formed
*  another consulting, you know, partnership with another kind of global consulting firm. You know,
*  they're already in the door at basically all of corporate America, you know. So again, like
*  you can chase a, you know, you can try to sneak in that door before it closes behind them.
*  But like those sales processes are in process if not already closed, you know, and moving on toward
*  model customization or what have you. Number nine, yeah, network effects. I mean, this one's a
*  little bit, it's definitely not as much network effects. You know, we talked about this with the
*  Elad and Sarah a little bit back. The network effects in like social media certainly way stronger
*  than network effects appear to be in AI. Sometimes people will ask me like, how much lock-in is there?
*  And I'm always like, you know, honestly, there's not much lock-in. We, when we run stuff on open AI,
*  we make an API call to open AI. You can, that code is a few lines, you know, even like a one-liner.
*  You could flip to Claude in two seconds. You could flip to, you know, some other model in two seconds.
*  It's really not that hard. Even with the fine tuning, you know, you can fine tune on open
*  AI's platform. They don't let you download your fine tune model and walk off with it. You still
*  have to pay, you know, you're essentially building it to rent. But once you've done that data set,
*  you can certainly take your data set and go run it on an open source model. And that's something
*  I've considered recently with Waymark just on pure curiosity, really. We're not really trying to save
*  money at the moment, but I'm thinking, geez, these open source models, they're kind of getting there.
*  Maybe it would be worth just like taking our, you know, data set that we currently use on open AI
*  and just running it against one of them and see how it goes. Maybe, you know, if it was comparable,
*  and we, I alluded to this earlier, didn't really get into it that much. We have a high degree of
*  developer control. You know, our task is super defined. It's always the same formula where we're
*  saying, here's the video script structure that you have to follow. Here's some information about the
*  user. Here's the user just set at runtime. And your job is to like spit out a completed version
*  of the script structure that you were provided. That's how it works. When we fine tune into that,
*  we're not supporting chat. We're not, you know, helping you write haikus. We're not doing anything
*  else. It's that. The developer control there means like, we can be pretty confident that,
*  you know, things can't go too far off the rails. If the language model starts to malfunction,
*  the application just errors. You know, it doesn't have, it doesn't like attack the user or, you know,
*  the user won't even see the output because like it'll just break. So that developer control and
*  the kind of predictability of the task is such that we could do a fine tuned model even without
*  like all the safety, you know, bells and whistles and niceties that we get would, you know, we do
*  and we do get end value from OpenAI, but we could kind of live without them because of the definition
*  of the task. But it's still not hard to change. You know, we, we, you can just flip around,
*  you know, any way you want, even, even on the fine tuning side. So is there super strong network
*  effects? Not really. The biggest things are kind of maybe like social, you know, in the sense that
*  everybody's kind of introduced to AI with these products and like the techniques to use them and
*  the prompt engineering and the tools all get, you know, kind of built for OpenAI first. Usually they
*  are built in a provider neutral way pretty quickly, if not right out of the gate, but like nobody
*  doesn't support OpenAI with their first release, right? Of a new library or a framework or whatever.
*  It's always going to be OpenAI on launch, maybe OpenAI only, maybe, you know, others included too.
*  But there is some kind of just gravity there that's like, you know, it's not, that's, there's
*  a reason that's the last on my list of notes, but, you know, it also kind of forces others
*  into somewhat of a following position too. It's like, you know, if I have something that's working
*  with OpenAI and I'm thinking about exploring something else or switching, first thing I'm
*  going to try is the exact same task. I'm just going to literally copy and paste into the other
*  thing. And if it doesn't work, then I'm going to be like, oh, this kind of sucks. And if it could
*  work if I like re-prompt engineered it, you know, or read their prompt guide or whatever,
*  and did it their way, then like that's nice. But I don't really, you know, ideally it's going to
*  work on the first time and all of those companies are going to kind of feel that pressure. They're
*  not going to want to, you know, make you, I mean, you can imagine being the, you know, the CEO at a
*  competitor, right? You're like, if you had a prompt, like, well, people need to read our prompt guide
*  and then they'll know how to use our AI. It's like, no, they're not going to do that. It's not
*  going to work like that. You have to make it easy for them. You know, if you've got to reduce that
*  friction, so that in their effort to kind of reduce that friction, they end up, you know, in
*  kind of a following position, I think pretty often. The, you know, the plugin architecture
*  is something that seems like it's going to kind of go that way. And is another area where,
*  you know, you can see potentially some of these things where like having the product dialed in,
*  having the feed, you know, having the data scale, you know, to power a feedback loop.
*  The plugin architecture, in theory, it's highly portable, but our other, so other people can't
*  adopt it. Microsoft has said they're going to adopt the same basic plugin architecture that
*  OpenAI introduced. So probably everybody's going to kind of have to be able to support that in some
*  way. But there's a lot of ways that you could be worse at supporting that than them. And now you're
*  just kind of trying to play their game, but you're playing from behind. It's going to be hard to like
*  leapfrog them at their own game. It's going to be hard even to catch up with them at their own game.
*  And meanwhile, you're not developing your own game, right? So that's, I think that's going to be
*  tough. I think for some, for a lot of these reasons, companies like Character and Inflection
*  with their new Pi AI, I think those are notable exceptions to all of this analysis, or at least
*  possibly because they are trying to do something different. When you go talk to Pi, it's not like,
*  you know, it's not like a sort of Butler style, you know, what can I do for you? Here it is,
*  you know, hope it's helpful. It's a much more open-ended, like exploratory dialogue.
*  And, you know, that may emerge as a totally different lane that is currently kind of unfilled.
*  I don't think many people go to chat GPT for companionship, and they almost kind of discourage
*  that in their approach. You know, it'll chat with you, but it's like, it frequently reminds you that
*  it's an AI in ways that are not like super conducive to, you know, an immersive experience.
*  Whereas these other ones, you know, they don't deceive you about being an AI. I think they're
*  all like pretty defensible, you know, product designs from what I've seen so far, but they do
*  engage you in a different way that, you know, they could just end up being a different product
*  category in the end. Hey, you know, we spoke to Ilaad and Sarah, you know, a couple of VCs and
*  how they're approaching it in the space in terms of like, what to invest in, what not to invest in.
*  And I'm curious, given, you know, we just ran through these motes,
*  and that's what people are talking about when they talk about motes. It's like, what's investable
*  and what's not investable? Okay, I think the sophisticated analysis right now generally agrees
*  that like Salesforce should be fine because they've got a ton of shit built out and a ton
*  of distribution and a ton of contracts and a ton of everything. And they can layer on a copilot
*  before you can build, you know, a worthy rival from scratch, you know, with no matter how,
*  you know, smart your use of GBT4. So that I think is happening, you know, and Adobe is in kind of a
*  similar position in a way that, you know, is more on the, you know, visual side than the text,
*  although it could be both, you know, there's been a ton of amazing stuff, but nobody's really
*  canceled their Adobe accounts. And now Adobe is announcing their own amazing stuff. And, you know,
*  it seems like if people have to pick, I just saw a really interesting thread from this guy named Riley
*  on Twitter who said, you know, mid-journey is awesome. It's always, you know, it's been totally
*  groundbreaking. But if I was going to tell somebody what to learn today, I'd tell them to use the
*  Adobe Photoshop because mid-journey is kind of this like, you know, black box, you get things out of
*  it. They can be awesome, but like Adobe, you can really make what you want, you know, and they have
*  both the generative layer and the like dig in and do shit layer now. And so, you know, again,
*  they should be fine. Like it's just going to take a long time to build up a credible rival to Adobe.
*  I would be very wary of a thesis that was like, you know, pick an incumbent and be like,
*  we're going to beat them because we're going to use AI. I don't think that's going to work.
*  They all know about AI and it's not that hard to implement. And in fact, in some ways it's easier
*  when you have a big platform because you also have extensive documentation. So like the existing
*  models, you know, already have a decent sense of a lot of these, you know, mega platforms.
*  Like you could probably go ask, I mean, people see even in the marketing copy thing, right?
*  You can ask GPT, chat GPT to like write you a tweet or write you a LinkedIn post. It knows what
*  the difference is between those in like general form and tone. You know, a social media company
*  that doesn't exist yet, it's not going to know how to do that. And the same thing is kind of true for
*  like whatever, you know, technology you're pursuing. You know, if it's all well documented out there,
*  like you could probably get pretty far with, you know, with the chat GPT just off the shelf.
*  You don't have to do any special training. And I think they will, by the way, like Salesforce is
*  going to have their own co-pilot. That's not like default, you know, GPT-4, you know, it'll be better
*  than that. But I don't see any reason, you know, they've got documentation, like probably a trillion
*  tokens of like documentation and forum posts and tickets and all that shit, you know, I mean,
*  they have plenty to work with. So yeah, I guess bottom line there, it seems like mostly the
*  incumbent should be fine. And mostly I would be pretty skeptical of a thesis that's like,
*  we're going to take on this incumbent and we're going to win because we're going to use AI and
*  that's how we're going to win. I just don't see that path for most things, unless you really felt
*  like an incumbent was like flagrantly dropping the ball, you know. I think that the more kind
*  of exciting or, you know, hard to predict stuff would be then what we also kind of talked about
*  with them, which was like, what are the new things that just couldn't ever have existed before where
*  there is no incumbent and it's a totally new market and that like, I guess so far we've got
*  AI chatbot as like a new category. We don't really have that many new categories yet. We've also got
*  like text to image, you know, is kind of a new category. So there are a couple of things that
*  are kind of like, holy shit, you just couldn't do that before that have already come online.
*  But I think that's, that stuff is mostly still in the future. Because again, like GPT-4 has only
*  been out for a couple of months, you know, and probably a lot of the people that come up with
*  those like crazy ideas won't even be the, you know, the AI developers, you know, in the same
*  way that like, you know, Uber was developed in a different way than, you know, the iPhone itself,
*  you know, and you probably Travis, you know, probably couldn't have done the iPhone.
*  But like a company like Apple, you know, could never have done what Uber did.
*  There probably is some kind of similar dynamic, what gets built on this new platform that's just
*  like radically different, you know, who knows, like one thing I am keeping my eye on is this
*  kind of improved discourse space. You can even kind of connect this to crypto, which I,
*  you know, seldom do, but like the smart contract, right? Can you take a language model that is kind
*  of a dispute resolver, you know, cannot like cryptographically guarantee that you are in fact
*  getting the model that was agreed upon, you know, at the time the contract was signed and like,
*  let it resolve stuff and like, you know, handle, you know, disputes and issue refunds accordingly
*  or whatever, you know, kind of manage little escrow accounts, that kind of stuff I do think
*  should happen. And the cost of, you know, the possible unfairness or the like,
*  you know, AI going against you to me seems like ultimately people just accept that because
*  it's going to be so much cheaper and better than anything else. Like what are you going to,
*  your alternative in today's world is go to small claims court or something. Good luck with that.
*  You know, you might as well just sign on to some sort of crypto, you know, consumer arbitration
*  scheme and, you know, it's better than, you know, any alternative, even if it's not perfect,
*  or, you know, even if you don't get the justice you kind of want every single time,
*  stuff like that I think will be big. I do think these like new relationship paradigms are going
*  to be, I'm not excited about that myself. You know, I don't want an AI friend and I'm kind of,
*  it does, you know, this is like the max, you know, extent of like amusing ourselves to death
*  potentially. So I don't know that that is ultimately healthy for individuals or society,
*  but maybe it could be, you know, maybe we just haven't seen the like final right version of it
*  yet. You know, when we talked to Eugenia from replica, I was like, man, the revelation here
*  is how bad a lot of people need companionship, you know, because to get as far as she had gotten
*  pre-GPT-3 is like, that's a common, that's not even an AI story, that's a society story.
*  And now you're going to inject an AI story into that society story. And it seems like it easily
*  can go, you know, 100x. I don't see any reason that like the percentage of people who have an
*  AI friend does not totally explode. And maybe it even could be good, like, you know, for a lot of
*  people it probably would be good. Where it starts to be a problem is where, well, who knows, it
*  could probably start to be a problem in a lot of ways. But for me, I kind of think the last thing
*  I want is that to crowd out my real relationships, you know, which I probably already, you know,
*  spend too much time podcasting and thinking about AI relative to, you know, what I might ought to be
*  doing. And, you know, I don't want to make that any worse with some like AI friend in my pocket.
*  But yet, I bet that, you know, just like social media, you know, is kind of addictive, not all
*  good, not all bad, but definitely like crowds out other activities. I think this is probably also
*  kind of unavoidable. And so, you know, and when Sarah mentioned that, you know, she was like,
*  you look at the like usage of some of these things, like, I think she mentioned maybe both character
*  and replica, you know, you can start to see it. So from an investment standpoint, that could be
*  really good. I would, you know, my concern with investing in replica right now would be, you know,
*  not in, I don't mean to cast dispersions on it, but I would be less worried that they'll be able
*  to grow users and more, you know, like, do we have the right vision here for, you know, what
*  kind of impact we're going to make? And again, that's not to suggest, you know, that their vision
*  is wrong, but certainly, you know, questions are probably coming up faster than they can answer
*  them. You know, I think that was definitely a takeaway from that episode, right? It's like,
*  this was all happening pretty quickly. And, you know, even as much as she has been in this game,
*  like, it didn't seem like, you know, she was fully prepared for it. And again, not to blame her,
*  it came up on us all pretty quickly, but she just is the one that happens to be in that seat,
*  you know, so that's a challenging seat to occupy. You know, again, from an investment standpoint,
*  where do you go invest? Google is going to be tough to beat, you know, and Microsoft and their
*  distribution, you know, all these hospital systems are all a customer of Microsoft or Google already,
*  right? They all get docs from one of these two places, you know, or like Epic, you know,
*  again, the distribution seems like it's going to be hard to beat. You know, when I think about
*  Neil Kossela and Curi, I'm like, I do expect them to be successful. I do think they will grow. You
*  know, they've already also gotten some distribution because they've been in the game for a while. And,
*  you know, they didn't, this was not a company that was started to like take advantage of GPT-4.
*  So, you know, I think they will be on a good path, at least for a while,
*  but that probably means like their past investors do well. It's still not super clear that like
*  their, you know, next round investors do super well because again, the prices get low. So how
*  do you make that? How do you make that much money? You know, I don't know how you make that much money.
*  I don't know. It's just tough. You know, the prices keep dropping. Prices drop 97%.
*  And like the biggest corporations in the world are kind of ready to run at or near cost
*  for the foreseeable future. And they already have all the, you know, distribution. I don't know how
*  much share, you know, you can really hope to get. So, you know, what's going to be transformative
*  there? You know, is it, I kind of sense that like it is more like task automation for a while than
*  it is, you know, a totally different thing. Now you can imagine somebody that could bring forward
*  the like true AI doctor, no humans involved, you know, taps into all your sensors. There could be
*  like a totally transformative form factor that is just next level. It is like the shit that's so much
*  better than even like a thorough application of GPT-4 through our, you know, current system. Hard
*  to kind of imagine what that looks like, but you can at least conceive of it. But when it comes to
*  like reviewing the doctor notes and like, you know, making sure that everything's double checked and,
*  you know, was there any possible drug interaction? Like that stuff seems like it happens in the
*  current systems for the most part, you know, because it's really easy to integrate those
*  APIs wherever they need to be integrated. So, you know, I don't know, I wouldn't, I wouldn't take a
*  job right now as a salesperson for, you know, kind of doc.ai that's like new and on the scene and kind
*  of like, look, we've, you know, done whatever exactly. There's an interesting, there was a
*  company that just came out, was it Hippocratic.ai? They said they've trained only on medical,
*  like trusted medical information. And, you know, wherever they, assuming they get that out of
*  existing, you know, medical record systems. And they call out that, you know, other systems that
*  are trained on like the whole internet, plus, you know, maybe specialized have wrong shit in them.
*  And that's, you know, one way that they want to differentiate themselves. That seems like it could
*  be true, could be, could be like a real advantage, though I don't know, you know, and Neil had a
*  couple of interesting points where he said, like, you know, if the patient says they had cereal,
*  that probably also means they had milk. And like, you need that kind of general knowledge
*  that's probably not represented in these medical systems, you know, to figure out all those
*  associations. You know, he also said very Silicon Valley, you know, if the, if the person went to
*  Burning Man, they probably inhaled a lot of dust. And you aren't going to know that if you're like,
*  just trained on this medical data, I wouldn't think. The Mosaic guys also said, like, almost all their
*  customers could train on a combination of open source and proprietary. Maybe they're doing that,
*  too, but they seem to be saying they're not. So anyway, that's one big question that I have.
*  And another one is, you know, they take a very interesting position saying, we don't believe
*  language models are safe enough for diagnosis. So we're focusing entirely on nonpatient facing,
*  but like back office shit, which is plenty big enough market. And, you know, again, I think they
*  probably be successful. Do they dominate the space? I don't know. It feels like in the end,
*  no. I have to guess that like the big, you know, the Microsoft epic, whatever kind of complex,
*  ultimately still takes most of that market. And it's tough to, you know, to get your little
*  green shoot up through the hornet's nest of all the, you know, all this bullshit that you have to
*  push through. This is great. I'll let you go. Thanks for a great conversation. And we'll talk
*  next week. Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button. I believe in Omnike so
*  much that I invested in it, and I recommend you use it to use Cogrev to get a 10% discount.
