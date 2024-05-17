---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 4488s
Video Keywords: ['ai', 'artificial intelligence', 'openai']
Video Views: 11303
Video Rating: None
---

# OpenAI DevDay: Beyond the Headlines with Logan Kilpatrick, OpenAI's Dev Relations Lead
**Cognitive Revolution "How AI Changes Everything":** [November 07, 2023](https://www.youtube.com/watch?v=WFM2pvj00oc)
*  How many startups do you think you guys killed yesterday?
*  There's so much opportunity for startups being created.
*  I think the reality is if your startup was a super,
*  super thin wrap around something,
*  you didn't really have a startup,
*  you just had some project that you were working on that was building off of an API.
*  My takeaway from yesterday is the barrier to entry for new startups and for people to
*  build extremely compelling products has never been lower,
*  and there's never been more amazing technology to build with.
*  I think we probably created thousands and thousands of new startups.
*  If you take a step back,
*  if you're a venture backed or even if you are later series,
*  ABC, whatever it is and have raised enough money to do this and have cash,
*  it actually makes a lot of sense.
*  This is an opportunity to truly build a defensible business.
*  You can have a model that's trained on,
*  I think in order of billions of tokens,
*  which is not something that anybody else has access to.
*  Again, it requires a sufficient investment to make that happen.
*  But I do think that this is what people have been asking us for.
*  How can we build a defensible business using your products and services?
*  Hello and welcome to the Cognitive Revolution,
*  where we interview visionary researchers, entrepreneurs,
*  and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology will transform work,
*  life, and society in the coming years.
*  I'm Nathan Labenz joined by my co-host, Eric Torenberg.
*  Logan Kilpatrick from OpenAI.
*  Welcome to the Cognitive Revolution.
*  How's it going, Nathan? I'm excited to be here.
*  It is an exciting time.
*  You guys have just launched a whole smorgasbord of stuff at OpenAI.
*  So congratulations on that.
*  Thanks for taking a little time to dig into the details and all the little nuances of it with us.
*  I wanted to start with a couple of big picture questions,
*  and then really get into the weeds.
*  So starters, obviously going into yesterday's event,
*  the sort of memesphere and certainly coming out of it too was like,
*  how many startups is OpenAI going to kill with this release?
*  So, you know, kind of a tongue in cheek starter question.
*  But if you had to put a number on it,
*  how many startups do you think you guys killed yesterday?
*  I've been seeing this trend on Twitter and I get such a visceral negative reaction to it.
*  I really do think there's so much opportunity for startups being created.
*  And I think the reality is if your startup was a super, super thin wrap around something,
*  you didn't really have a startup.
*  You just had some project that you were working on that was building off of an API.
*  And of course, as things change, you'll be disrupted in some capacity.
*  True, genuine startups are thinking about from the ground floor,
*  how do I build a defensible business?
*  And like you have to go and like build an innovative product to do that.
*  So my takeaway from yesterday is the barrier to entry for new startups
*  and for people to build like extremely compelling products has never been lower.
*  And there's never been more amazing technology to build with.
*  I think we probably created thousands and thousands of new startups
*  and gave the ones who are building on our platform today, you know, lower prices,
*  a ton of new features, they can go and compete with other big companies.
*  So I'm really excited.
*  I think there's never been a better time to build something cool using AI.
*  Yeah, well, no doubt about that.
*  So we're going to get into all the tools.
*  Just another kind of angle on that same sort of question.
*  It does seem like there is a bit of a shift where, you know, not even a year ago yet.
*  And it's crazy to think about, right?
*  Chad GPT, I understand, was kind of motivated at OpenAI by this sense that like,
*  hey, these models are getting pretty good, but we're not seeing kind of the traction
*  or the sort of everyday use that we would expect to see or hope to see.
*  So like, let's put a product out there and try to kind of kickstart that.
*  That obviously really worked.
*  And now this year later, it seems like there's a bit of a shift
*  toward more of an Apple like not first, but best, maybe you could say,
*  kind of product direction where the community has been out there
*  kind of exploring all these things of rag and agent frameworks and all that stuff.
*  And here comes OpenAI with like presumably by a significant margin,
*  I would imagine, you know, the best in class version of that.
*  So how would you kind of frame that shift?
*  And is that something you think we'll see more of in the future from OpenAI?
*  Very curious about that.
*  I think part of it is in the community has an advantage in a sense.
*  I think this is probably the same thing for Apple.
*  Like, I think we would love to be first to a bunch of things.
*  I think the reality is like for us to build something, it has to have like
*  you have to be able to scale it to the hundreds of millions of weekly active users.
*  And chat to me and like really make sure that it fits into like,
*  what is the core strategy from a product perspective?
*  So there's always like a million and one different things that we could be doing.
*  And it's just hard to ship things quickly when you are building at that scale.
*  Like, there's just like a lot of really difficult technical challenges to solve.
*  So it's not like we've been sitting there like, you know,
*  you know, scratching away at like every last little detail being like,
*  we want to make sure that we're, you know, putting out the very best thing
*  and we don't want to move quickly.
*  It's like really feels like at least, at least to me internally,
*  that like we're always in an all out sprint all the time.
*  And like, as soon as something is ready in the pipeline, like it's coming out to people.
*  The reality is like the team that's just been growing and there's not enough
*  like human hours in the day to do all, do all this stuff.
*  I think people forget, like, it's not like we didn't ship anything for the last
*  nine or nine or 12 months.
*  Like there's been a constant slew of things.
*  It's just, there's a lot of work that has to go into making these things happen.
*  Yeah.
*  Even in just the last month or two.
*  I mean, it wasn't that long ago that 3.5 fine tuning dropped and, you know,
*  people were like, boy, if they're releasing this, the head of DevDay,
*  you know, DevDay is going to have some real fireworks.
*  What is the employee count at OpenAI now?
*  Do you know the current number off the top of your head?
*  Yeah, I know. I know the general number.
*  I think when I joined last year, it was something around like 300.
*  And I think we're we're we're well and beyond that.
*  I think the only general comment that makes I'm not sure how public
*  facing the internal numbers are is that I think the estimate on LinkedIn
*  is is a little bit higher than what it actually is in practice.
*  But we've we've grown significantly.
*  It's been awesome to see it like throughout as we needed to,
*  because there's so much work that has to happen.
*  But yeah, it's interesting to see the shift that's happened with going from
*  you know, when I again, when I joined and I wasn't even that early,
*  a 300 person company to now something that's that's much, much larger than that.
*  And obviously, it's going to continue to grow in the next the next year.
*  So it'll be interesting.
*  Yeah. So obviously, one of the keys to scaling an organization
*  is having a strong sense of kind of mission and high level strategic clarity.
*  You know, I'm sure not
*  unrelatedly open, I recently updated its core values.
*  And there is now a statement, even I'd say more explicitly than previously,
*  that the company is focused on AGI, AGI focused.
*  We are committed to building safe, beneficial AGI
*  that will have a massive positive impact on humanity's future.
*  Anything that doesn't help with that is out of scope.
*  All these things that got launched yesterday, a lot of details,
*  you know, a lot of features, the GPT store.
*  How are you guys thinking about that as being on the path to AGI?
*  Because I could certainly imagine somebody saying, like, wait a second,
*  a GPT store, is that really on the kind of critical path to AGI?
*  But I know that's obviously something you've thought deeply about as a team.
*  So I'd love to kind of hear how this is all contextualized
*  as part of that grand mission.
*  Yeah, it's a good question.
*  I think, like, to put it like very precisely, like open AIs, not
*  we don't exist to make the best chat platform.
*  We don't exist to make the best API.
*  Like these are these are mechanisms in which help
*  get us to the point of AGI that benefits humanity.
*  I think the piece around chat, GBT and the piece around the API
*  is is another angle of our philosophy, which is we need to get this technology
*  out to people iteratively.
*  And you heard Sam say this actually in the keynote yesterday, where
*  assistance and GBTs are really our first shot at and moving
*  in the direction of agents.
*  And we didn't want to go all the way to the sort of autonomous agent type
*  workflows that you you see and some other products and services today.
*  Really in the vein of we need time for society and for people to adapt
*  to these changes, and I think that's that's really chat.
*  BT today is really like the mechanism to allow people to see where this
*  technology is going and how to adapt.
*  Like I think Sam, Sam also made this comment sometime in the last few years.
*  But like it is entirely possible that open AI could have continued
*  to do the research that we were doing and build, you know, what could become
*  AGI in the confines of open AI, not sharing it with the world.
*  And in five years, we just sort of emerged with this thing that works.
*  And like that's actually like a plausible outcome.
*  Like that I actually think that someone, whether us or someone else,
*  could actually do that.
*  The reality is like that's not the best thing for humanity.
*  I'll showing up with this thing that's now all of a sudden super powerful and
*  no one's ever seen chat, GBT, no one's ever used GBTs or any of the future products.
*  It would cause a tremendous amount of turmoil for everybody.
*  And like that's not great.
*  So I think that's that's really the strategy is like the core research is
*  what's going to enable AGI to happen.
*  But chat, GBT and our API are the way of making sure that that technology
*  benefits everyone and everybody gets a chance to like see what's coming.
*  And shape it to that.
*  The two quotes that stood out to me were we think it's important to give people
*  a chance to experience and adjust to this technology, which is what you're just
*  speaking to. And then also we want more people to shape how AI behaves.
*  I thought that was also pretty telling.
*  Obviously, there's been a number of different things there, but the GPT store
*  is kind of a seemingly a way to really open up access to how you can
*  shape the behavior of an AI assistant without even necessarily needing to
*  get into the API box.
*  So that's that's definitely very interesting as well.
*  So I've actually grown, you know, I'm definitely somebody who's pretty concerned
*  about AI safety.
*  Big picture. But I've definitely grown a lot more convinced over time
*  by this kind of over capabilities, overhang argument that like things have to
*  kind of get into the public sooner rather than later or else, you know, it gets
*  to be super disruptive when there's that huge or potentially disruptive
*  when there's that huge delta.
*  So let's kind of get into the weeds and help close the capability
*  overhang gap. The big themes that I saw, I sort of wonder if you would add anything
*  to it. Multimodality, obviously huge.
*  I'll call it accessibility via price drops across the board and also the turbo
*  speed up. I'll call it platform expansion
*  as kind of a shorthand for saying, you know, these adjacent
*  formerly kind of adjacent complementary things like vector database
*  and runtimes, which, you know, have existed a little bit in in chat
*  but haven't been to the API.
*  Now that's kind of available for everyone.
*  And then finally, agents.
*  And I will get into it all, of course, but I am curious.
*  Maybe for starters, like you said something interesting a second ago on.
*  Not going all the way to autonomous.
*  Like, how are you guys thinking about how far these, you know, assistants
*  not yet, maybe full agents?
*  How far are they kind of intended to go right now in terms of their autonomy?
*  The context around how far the limitation of these models,
*  how far the assistants can go and how far G.P.T.
*  can go today. Really, there's no mechanism for them to do like self planning.
*  And if you look at like a lot of the like traditional agents products on a G.P.T.
*  whatever they are, they do this whole like planning process and they say,
*  I'm going to go and execute these tasks and I'm going to sort of follow up afterwards.
*  G.P.T.s don't have that that capacity today.
*  It's really still the core like send a message, get a response and a message,
*  get a response.
*  So they're like long term queuing up of actions.
*  I think there's also the sort of missing link towards the more agent workflow
*  is like, I'm going to go and run these things in the background,
*  maybe without you self directing me to do it.
*  Like, I'm kind of just going to go and randomly check and see whether your email's
*  been updated or, you know, whatever, whatever that might be.
*  So I think those are really the missing the big missing pieces right now.
*  I think with the assistance API, you could probably build some of these yourself
*  if you really want it to.
*  I do think like we'll eventually get there in the API.
*  We'll eventually get there with with G.P.T.s, assuming that can be done in a safe way.
*  I think there's also like that question of reliability.
*  Like, I don't think that anybody has really like hit the home run yet with with
*  agents products, whether in an API or a consumer product.
*  And I think that's another missing piece of like, it's probably just going to take us
*  a little bit more time and others as well to figure out like, how do we actually do
*  this reliably, like make sure that it really provides value?
*  I've tried a bunch of the agents products.
*  I'm just like, this basically takes as much work as if I was going to do it myself.
*  So like, what's what's really the point of using this?
*  Like, it's just kind of if anything, you're just like making yourself
*  at least the current state today, my feeling personally is like you're making yourself
*  like liable for more risk.
*  Like I'm giving my credentials to some system where I don't really get to see
*  every single step that it's taking.
*  And, you know, it might not really do the things that I want.
*  And I think there's just like a little there's like some small little missing
*  piece of refinement for that workflow to get really, really good.
*  And then people will just. Yeah, I think it's going to be the explosion of
*  those agents. I also think like the challenge today with agents is
*  the Internet is and society are really not
*  ready at the moment, I think, for like 100 million or a billion agents.
*  Kind of like, you know, the chat, you have 100 million active,
*  weekly active users.
*  If all of a sudden every single one of those weekly active users has access to
*  quote unquote agents who can go out and do things on their behalf, like the Internet
*  and products and services are just not ready for that.
*  I think it's going to take a little bit of time and hopefully GPT's are like
*  a nice way for companies and people to start thinking about this.
*  Interesting. Is this sort of a conscious
*  kind of decision to say we're going to, you know, not train
*  this kind of planning capability past a certain point right now?
*  Or is it just that, you know, open AI also hasn't quite figured out how
*  to do it.
*  Most of that kind of suggested that it probably is like within the scope
*  of what open AI could do, at least in the near term, if not already.
*  Yeah, I think it's I think it's a little bit of both.
*  Like my guess is there's just some like core technology things that need to be
*  figured out, like even with what was released in the last couple of days,
*  like it was an all out sprint to get there.
*  So like, you know, the scope had to be constrained in a lot of ways.
*  I do think that there is there needs to be like deeper thought
*  put into like actually rolling these things out and making them accessible.
*  So I think that's like a huge angle of it.
*  I do think the other angle is like actually making sure that the core
*  technology works really well.
*  And I'm less concerned about that piece just because our team is incredible
*  and can continue to to make amazing things.
*  I think the deeper challenges like getting everyone else in the world on board
*  with this idea and comfortable with it, I think that's that's just a very,
*  very difficult problem.
*  No doubt. There's a lot of adjustment that people are going to need to make
*  over the not too long time horizon.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Real quick, what's the easiest choice you can make?
*  Taking the window instead of the middle seat,
*  outsourcing business tasks that you absolutely hate.
*  What about selling with Shopify?
*  Shopify is the global commerce platform
*  that helps you sell at every stage of your business.
*  Shopify powers 10 percent of all e-commerce in the U.S.
*  and Shopify is the global force behind all birds,
*  Rothy's and Brooklyn and millions of other entrepreneurs of every size
*  across 175 countries.
*  Whether you're selling security systems or marketing memory modules,
*  Shopify helps you sell everywhere from their all in one e-commerce platform
*  to their in-person POS system.
*  Wherever and whatever you're selling, Shopify has got you covered.
*  I've used it in the past at the companies I founded.
*  And when we launch merch here at Turpentine, Shopify will be our go to.
*  Shopify helps turn browsers into buyers with the Internet's best converting
*  checkout, up to 36 percent better compared to other leading commerce platforms.
*  And Shopify helps you sell more with less effort
*  thanks to Shopify Magic, your AI powered all star.
*  With Shopify Magic, whip up captivating content that converts
*  from blog posts to product descriptions, generate instant FAQ answers,
*  pick the perfect email send time.
*  Plus, Shopify Magic is free for every Shopify seller.
*  Businesses that grow, grow with Shopify.
*  Sign up for a one dollar per month trial period at Shopify.com slash Cognitive.
*  Go to Shopify.com slash Cognitive now to grow your business
*  no matter what stage you're in Shopify.com slash cognitive.
*  Omnike uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it, and I recommend you use it to
*  use Cogrev to get a 10 percent discount.
*  So let's kind of start, you know, with some fundamentals and then, you know,
*  work our way back up, you know, I think kind of a complexity ladder
*  towards some of the highest and, you know, higher up the stack as we go.
*  Starting just with the models.
*  GPT-4 11.06 preview.
*  First question, what is meant by preview?
*  I guess I noticed that there's like 100 requests per day limit right now.
*  So I guess that's probably the main thing, right?
*  Obviously, you can't deploy that.
*  Anything else that we need to be aware of on the previews
*  designation and any sense of timeline for when that limit goes up?
*  Yeah, the preview designation is just intended to tell people that this isn't
*  the final version of the model.
*  So this was like essentially an early release candidate of what the finalized
*  model will actually look like.
*  So there's still like a bunch of like actual modeling work, post-training
*  work and other things that need to happen to get this model like to the standard of
*  something that we would normally release in the API.
*  So that's why that preview designation exists.
*  I'd imagine in the order of like weeks, hopefully less than months.
*  It's available as like the regular general version and no longer
*  accessible through preview.
*  You know, we need to make sure that we get feedback from people as we
*  release these new models and making sure that this, especially given how many
*  changes are baked into this model, that it's still performing to the level
*  that people would expect.
*  So hopefully you can try it as a drop in replacement for some of your
*  existing use cases, see how it performs, make sure there's no major regressions.
*  And then if there are major regressions, come and yell to us and let us know so
*  that we can, we can explore and make sure that the model is going to be
*  generally good.
*  You know, yesterday, the sort of highest level statement on performance was just,
*  it's better than GPT-4.
*  How is that being characterized?
*  Like I didn't see, maybe this was in a breakout session.
*  Funny enough, neither you nor I were there in person yesterday for personal
*  reasons, but is there like a model card coming out?
*  Are we going to, should we expect to see like the MMLU score and the, you know,
*  bar exam score in the same way that we got for the original GPT-4?
*  What's the outlook there?
*  Yeah, I think so.
*  One example is, and I don't, I don't know how specifically this generalizes to,
*  to, to four turbo, but 3.5, we can use this as a, as a proxy.
*  Um, the quote is, for instance, our internal eval showed 38% improvement on
*  format following tasks, such as generating JSON, Maximal and YAML.
*  The, the point of feedback and the question around releasing benchmarks, I
*  think is one that we've heard.
*  And I think with our last, uh, model API release, I think there was, we didn't do
*  a good job of like fully characterizing, you know, what, what are the performance
*  differences between these models?
*  The TLDR is I think we want, we want to release more of these benchmarks.
*  Um, I don't know yet if the full plan is to release a bunch of benchmarks for the,
*  like when this model comes out of the preview version, I would hope so, but
*  don't, don't have a definitive answer right now.
*  Um, I also think the nice part is like, hopefully people can, can run some of
*  these evals as well and like, keep us honest.
*  And I think people have done that with previous model iterations as well.
*  Yeah.
*  It'll take a couple of days worth of your a hundred requests per day to get the,
*  uh, MMLU suite run, but, um, I am sure somebody is on it somewhere.
*  Dan Hendricks and team, I'm sure have already started pooling their requests
*  and, uh, you know, it can't be too long now before we'll have that score.
*  So on the vision side, it seems like the, the note there is it's basically
*  the same model under the hood.
*  It's just kind of a presentation and like system message difference.
*  So we basically should expect one in the same.
*  Given that, is there a reason that, that it's too, I guess it's a system
*  message, but I'm a little confused as to why it's even presented as like two
*  different models via the API.
*  Yeah.
*  The big, um, background context is it's, it's two separate, like tech stacks, if
*  you will, to get it to work right now.
*  And there just wasn't enough time to, to the, they used to be completely
*  independent separate systems and there wasn't enough time to unify things,
*  which is why they're being presented as two different options.
*  Cause there's like some like very slight nuance differences, but behind
*  the scenes it is the same thing.
*  It will end up being unified into one.
*  And, and people should, should look at it and expect it to, to
*  behave in the same way with the caveat that the, with vision, there's like a
*  very small addition to the system message, which could again, technically
*  like throw off some of the props that people have in some cases.
*  Next up a 3.5 turbo 16 K fine tuning.
*  This is the first fine tuning that supports function calling.
*  Correct?
*  So when we originally released 3.5 turbo fine tuning, it didn't support
*  function calling and then we fast followed, like a couple of weeks later
*  with function calling, so the last version did support it.
*  This is the first version that supports 16 K out of the box.
*  Definitely very interested to crack into that.
*  We're using 3.5 fine tune now with the way Mark, you know, core script writing
*  model and you know, we've got a lot of stuff that we're throwing at it.
*  So we do, you know, sometimes have to even truncate our inputs to make sure
*  we stay within the 4,000, but the 16,000 is going to obviously open that way up
*  and create the possibility for like downstream, you know, iteration, chat
*  style, back and forth, function calling.
*  So that'll be a, a big, you know, expansion of possibility just for us
*  with our, you know, pretty narrow product.
*  So excited to get into that in more detail.
*  It's been crazy to see how much value people have gotten from 3.5 fine tuning.
*  I think 16 K has been like the number one ask for people.
*  And it, yeah, I think now, especially with, with extra context, you're
*  probably getting even closer to GPT-4 level.
*  Like I think we've, we've already had a bunch of customers.
*  I think we shared some of these use cases out of people getting like
*  GPT-4 like performance using 3.5 turbo.
*  I think now it's the gap is even going to be closer because you have more
*  tokens to work with, you can get more intricate examples.
*  And I think that was like one of the core limitations before is like, there
*  just wasn't enough context in some cases to like really give everything that you
*  wanted them all to do plus improve instruction following and everything else
*  that's coming in this latest 3.5 turbo version.
*  I think it's yeah, the gap between the models in some cases continues to
*  shrink, which is really cool.
*  Yeah.
*  I wonder if you have any big tricks and I know you guys are doing a, I guess
*  I don't know if you're co-sponsoring it, but there's a scale webinar tomorrow
*  that I'm looking forward to attending.
*  That's on kind of best practices for fine tuning 3.5.
*  For me, the number one thing that has driven performance is training it on
*  reasoning.
*  So the huge difference between if I just give it good examples and ask it to, you
*  know, follow, you know, obviously the implicit ask of fine tuning is learned
*  from these examples, but then layering in the reasoning and explaining why it's
*  writing in our case, you know, the script for the video in a particular way is a
*  huge Delta in performance.
*  Any other tips along those lines that are like kind of simple, but like drive a
*  lot of value in the 3.5 fine tuning?
*  Yeah, we actually had a breakout session on this at Dev Day.
*  It was recorded and it should hopefully be available in like the next few days,
*  hopefully by the end of this week.
*  I'll defer people to that recording.
*  I know John, who's one of the folks on our fine tuning team and Colin, who
*  actually is maybe the person who's doing that webinar tomorrow, were the two
*  speakers for that.
*  And I saw a bunch of the chatter online.
*  People seemed really excited about it.
*  I didn't, I haven't actually seen the talk, so I'll defer to them because they're
*  the sort of experts in the space right now.
*  But they went through a bunch of like customer use cases and the pitfalls and
*  all the things like that.
*  So it should hopefully be the perfect answer for people looking for for tips
*  like that.
*  Cool.
*  Okay.
*  Well then the next, there's even two tiers of, you know, kind of fine tuning
*  possibility beyond that.
*  GPT-4 fine tuning coming soon.
*  Is this the 128K that will be the base?
*  I assume so.
*  Can you get me into the program?
*  And more generally, like what kind of frontier use cases are you looking for as
*  you're looking, as you're going to pull people into that experimental program?
*  Yeah.
*  The context for the experimental program is just wanting to make sure that there's
*  a bunch of safety concerns, obviously, because GPT-4 is much, much more powerful
*  than 3.5 and the way that it's trained and, you know, with more context and
*  things like that.
*  So we just need to be a little bit more initially cautious about, about
*  rolling that out wider.
*  It's also more expensive.
*  So I think people, you really need to be somebody who is, who is pushing on the
*  boundaries.
*  And part of the concern was like a bunch of random developers are going to show up
*  and like kick off a bunch of fine tuning jobs and not really have perspective on
*  like the cost for, for GPT-4 fine tuning, which is more expensive than, than 3.5
*  as you would, as you would assume.
*  And then be like, Oh, wow, I just paid all this money.
*  And by the way, like I probably am not a machine learning expert and like, did
*  it make my training data right?
*  And like, now I just paid all this money for something that's not super great.
*  So I think there's like from a product perspective, a little bit of concern of
*  that as well as like, you just have to be more thoughtful as you're spending more
*  money and making a more powerful model about like how you're actually training
*  it.
*  And I think like it takes folks who are like really thoughtful about this, like
*  you and the folks at Waymark to do it well and like actually have like maybe a
*  little bit of data science and machine learning background.
*  I don't think there's like, there's no specific use cases that we're, we're
*  looking for on the, the four early access side.
*  It's really about just like deploying it safely and specifically to people who
*  have already used 3.5 fine tuning.
*  Like you should really try 3.5 fine tuning for your use case, especially now
*  with 16 K.
*  So you won't even have the option to opt in to like apply for four fine tuning.
*  If you haven't used 3.5 and this has been one of the mistakes that we've made in
*  the past with our like general wait lists that we've done is like, everybody just
*  says, yeah, I'm interested in this.
*  Like that would be cool to do four fine tuning without actually having spent the
*  time or looked at the data and all those things.
*  And like, it just makes it really, really difficult for us when a million people
*  say that they want something.
*  We're like, well, we don't, it's like, how do you filter through those people?
*  And it's a lot of work.
*  So hopefully there's a new approach of like, Gating it based on actually having
*  used previous fine tuning, we'll make sure that we get like a much higher signal
*  to noise ratio from customers.
*  And then beyond that custom models, this was kind of the highest end thing.
*  I saw via Twitter that two to $3 million is kind of the entry level price
*  expectation.
*  I was surprised my initial guess was $10 million just to start.
*  I'm just given how much, you know, kind of demand I would expect you guys to get
*  for that from companies for whom, you know, money is presumably not much of a
*  constraint.
*  I'm priced out of that at Weymark, but you know, there's a lot of companies there
*  with some pretty healthy balance sheets.
*  So any guidance for kind of what you're looking for there beyond obviously people
*  with the money to spend?
*  Yeah, I think part of the context with custom models is really wanting to push
*  the boundaries of like, what is actually possible if you put in a bunch of your
*  proprietary data.
*  And I think there's companies who are building their core product around AI or
*  going to be well suited for this.
*  And I think like, if you take a step back, if you're a venture backed or even if
*  you are like later series, you know, ABC, whatever it is, and have raised enough
*  money to do this and have cash like it actually makes a lot of sense.
*  You have this is this is an opportunity to like truly build a defensible business.
*  Like you can have a model that's, you know, trained on, I think, in order of like
*  billions of tokens, which is like not something that anybody else has access to.
*  And again, it requires a sufficient investment to make that happen.
*  But I do think that it's like this is what people have been asking us for.
*  Like, how can we build a defensible business using your products and services?
*  And I think custom models is going to be one of the ways to do that.
*  I'm hopeful that like, I feel like I deeply resonate with the voice of like the
*  average developer.
*  And obviously, most people who are hacking on a project or we're sort of getting
*  their feet wet in the space don't have two to three million dollars.
*  So I'm hopeful that we'll learn a ton of stuff from this process and like figure
*  out a way that we can bring those costs down to make it more widely accessible to
*  more companies, more startups and people who are interested in pushing the limits
*  of what's possible with these models without putting in two to three million
*  dollars. But I think we just need to learn a bunch of stuff still.
*  And it takes like, you know, actual open AI researchers are going to help you make
*  those models better from end to end.
*  So it's like a huge investment from our side, especially given like there's so
*  many things that we could be doing.
*  But I do think it's important to help people with with these problems.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever.
*  It's storming every industry and literally billions of dollars are being invested.
*  So buckle up. The problem is that AI needs a lot of speed and processing power.
*  So how do you compete without costs spiraling out of control?
*  It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure,
*  or OCI. OCI is a single platform for your infrastructure, database, application
*  development and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent
*  price instead of variable regional pricing.
*  And of course, nobody does data better than Oracle.
*  So now you can train your AI models at twice the speed and less than half the cost
*  of other clouds. If you want to do more and spend less like Uber, 8x8 and
*  Databricks Mosaic, take a free test drive of OCI at oracle.com.
*  That's oracle.com.
*  Oracle.com.
*  If you're a startup founder or executive running a growing business, you know that
*  as you scale, your systems break down and the cracks start to show.
*  If this resonates with you, there are three numbers you need to know.
*  Thirty six thousand, twenty five and one.
*  Thirty six thousand. That's the number of businesses which have upgraded to NetSuite
*  by Oracle. NetSuite is the number one cloud financial system, streamline
*  accounting, financial management, inventory, HR and more.
*  Twenty five. NetSuite turns twenty five this year.
*  That's twenty five years of helping businesses do more with less, close their
*  books in days, not weeks and drive down costs.
*  One, because your business is one of a kind, so you get a customized solution
*  for all your KPIs in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts and improve margins.
*  Everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist designed to give you
*  consistently excellent performance, absolutely free at netsuite.com
*  slash cognitive. That's netsuite.com slash cognitive to get your own
*  KPI checklist. Netsuite.com slash cognitive.
*  I thought it was a bargain.
*  It's like if you are an enterprise that is sitting on a huge amount of data,
*  you've kind of been collecting and not really knowing what to do with.
*  And you've got one hundred million dollars plus sitting on a balance sheet.
*  It's like there's really I can't come up with anything better to spend it on than
*  to go in and do it something like this. Right.
*  I mean, you talk about what is going to transform your business.
*  What is a threat to every business?
*  But also what is a massive opportunity for every business?
*  I don't know how, you know, public company, CTOs, CIOs are not like basically all,
*  you know, on the wait list for this product.
*  And and I'm not paid to say that, but it just seems like a pretty clear
*  value profit, not that extreme of an entry point.
*  You know, if you're somebody who's just pushing into this space today,
*  like to go and procure, hire a bunch of people to do the the actual
*  like model training, like get the resources, all those things like you'd probably spend
*  and you're like a genuine technology company.
*  You'd probably spend in the order of like at least a few million dollars in capex
*  anyway and likely end up with something that's like not as performance
*  in many cases as what we can hopefully give you for two to three million.
*  So I do think there's that angle of it as well.
*  We can sort of outsource some of that stuff to us.
*  Yeah, zero doubt about that.
*  I mean, that doesn't go that far in machine learning, you know,
*  researcher salaries in today's world and, you know, good luck, I would say competing.
*  So a lot to go.
*  So keep moving on. So the copyright shield is another big thing.
*  I kind of just interested in a little bit of the strategy on this.
*  And if there are any footnotes like I believe I saw with Google's policy,
*  which is kind of similar, that there was a carve out, if I understand correctly,
*  like if you're trying to create, you know, if you're trying to kind of jailbreak
*  and create copyrighted stuff and then it doesn't cover you.
*  I wonder if there's anything similar here.
*  And also just kind of wondering, like, I guess, what is the strategy for this?
*  Is this like you want to get into the litigation like sooner rather than later?
*  Or you like feel totally confident that everything you need to license is licensed?
*  I can kind of see multiple different reasons for trying to put something like this out there.
*  Yeah, I don't want to touch on the specifics because I'm looking at the blog post now
*  and we don't link out to like a specific page right now.
*  I think we'll have something that's that's forthcoming that goes into the nitty gritty.
*  So I won't make any any sort of definitive statements about it.
*  I think generally the context on why we want this is we want people to feel comfortable
*  that they're that they can build with us and not have to worry about copyright claims.
*  And I think that, you know, other providers have done this.
*  I think it's important for us to do this as well.
*  So that I think going back to the comment you made about like public company,
*  you know, CTOs and stuff like that, I think there's a lot of people who want to build
*  with this technology and they perhaps have other folks who who they work with in a legal
*  department or something else like that who are who are worried about the risks involved.
*  And it's a it's a limitation on who can use this technology if we don't provide things like this.
*  So the hope is we provide this.
*  We're able to work with more people and bring more people into the ecosystem.
*  I don't think anybody wants to be in litigation,
*  but it's I think it's important.
*  It's an important service to our customers.
*  In general, I would agree. Nobody wants to be litigation.
*  But it does feel like there's maybe a moment here where, you know,
*  the the leading developers kind of feel like we need to be party to some of these things to,
*  you know, help shape the the precedents.
*  I know some of that is already happening.
*  Now would maybe be a good time for you to remind everybody that you don't train on data via the API.
*  We've gone over many minutes. You haven't said that yet.
*  So here's your chance.
*  Yeah, we don't train on data that you send to the API.
*  I think it's it's super important.
*  I think in the context of assistance, we don't train on any of that data either.
*  If you upload files, all that good stuff.
*  Like, again, in a lot of ways, it's it's a downside for for certain customers
*  because there's people who want actually the models to improve for their use cases.
*  We do have a way to opt in if folks are interested in that.
*  But in general, if you don't want people, if you don't want us to have your data, we won't use it.
*  We don't want to use it. We want people to be comfortable building with the platform.
*  And I'm very happy that we made that change in March.
*  I think it's I had so many conversations with people who even though we were it was like a very tiny sliver of the sampling of the data,
*  it's still there are folks who are uncomfortable with it.
*  And I'm very glad that we don't have to we don't have to deal with that challenge today.
*  Cool. So let's get into some of the new modalities.
*  I think probably the one that's most exciting for me is image understanding.
*  It just seems like, first of all, it's really good from what I've seen in chat, GPT amazing.
*  And for thinking about Weimark, one of our longest standing challenges has been we collect all these images off the web
*  for the businesses that are going to make video and we use those.
*  But how do you know which ones are good and bad and whatever?
*  It's tough. So we've incrementally improved, but this seems like it should unlock a notable step improvement.
*  The price is pretty interesting, like pretty aggressive, I would say, you know, kind of maxes out at about one cent per image.
*  And then there's this low resolution option.
*  You can go all the way down to basically it looks like 12 images per cent if you do the kind of cheapest version.
*  I'd love to get a little bit better color on like, what is that low res thing like suitable for?
*  And also a question on aesthetics.
*  Almost no image understanding model that we've seen has a sense of like, how beautiful is this?
*  It's all about the content and very little about kind of the quality.
*  So, yeah, two questions there are, what's the low res thing for?
*  How do we think about kind of that order of magnitude price range?
*  And then is there an aesthetic component to it?
*  Yeah, on the low res version, the principle idea is that we take an image, we reformat it to 512 by 512.
*  So the easy comparison, I think this is actually in the documentation right now, as I was writing at a wedding in Mexico this weekend.
*  The idea is if you as a human could take an image and reformat it to 512 by 512 and answer the same question, the model should be able to do it as well.
*  If what you're asking about in that 512 by 512 cropped image is some tiny little detail that's shown in one little pixel somewhere, might not be able to pick it up.
*  But if you're like, you know, here's a 512 by 512 image, it's a picture of a highway with a car on it.
*  And you ask like, you know, is there a car in the picture?
*  The model should be able to do that. Like you and me as humans would be able to do that.
*  The model should be able to do it as well.
*  So it really depends on like, what is the input image size that you're working with and what is the level of detail that you need the model to actually go through.
*  And with high res mode, it goes through on like a patch by patch basis.
*  And depending on the image size and dimensions, it depends on the number of patches that are created.
*  And it goes in and again looks at those 512 by 512, but it like zooms in on each individual section, which is why the cost is higher because it's processing additional patches.
*  So again, the reasoning for folks is look at it as you would as a human.
*  If you can answer that question, you should be able to do it with low res.
*  If you can't and you need the high res version, think about it from that like patching perspective.
*  512 by 512 is the low res or the low res is smaller than that?
*  Low res is 512 by 512.
*  Wow.
*  So it's not super small.
*  Like I think 512 by 512 is like reasonable.
*  You could take a lot of images and like still understand the gist if you reformat them to 512 by 512.
*  Especially given the price perspective, like in a lot of cases, it might be worth like just seeing if 512 by 512 gives you the result that you want for a certain use cases before you go and pay more money for high res mode.
*  One angle I've been kind of taken to all these different things is just kind of comparing the prices to other things that are out there.
*  And on the image side, it seems to be lower than basically anything else I've seen that's hosted.
*  For example, if you go use Lava 13B on replicate, it seems to be, you know, and it's they kind of charge by like the GPU second, but it seems like you can do like three images, three images per cent, I should say.
*  With the low res, it's more like 12 per cent, but you do still have the output tokens too of like what's generated.
*  That's kind of included.
*  So it seems like it's like competitive or maybe like even a little bit cheaper than other options.
*  One area where that does not seem to be the case is the Dali 3 integration.
*  If I understand correctly, that still is at four cents per image.
*  And that's definitely way higher than a lot of the sort of open semi open source, kind of hosted open source options.
*  I'm curious if there's a driver there.
*  Is that like a licensing deal that's gone on in the background?
*  Presumably it's not compute, right?
*  Because like I would think Dali 3 Turbo would would exist if it was a matter of compute.
*  To be a question, I don't also just to go back to your question before about aesthetic stuff within Vision.
*  I haven't tried that out. I would imagine it's like it has the same level of reasoning and capabilities as like base GPT-4.
*  So like you could probably get the model to like make general assessments of whether something is beautiful or not.
*  I don't know if like, again, it's not going to be like real because it doesn't, you know, it doesn't understand in some sense.
*  You know, the saying is beauty is in the eye of the beholder.
*  I don't know what the how it will react to certain things.
*  You could you could probably ask it those questions.
*  But on the question of pricing for Dali 3, I would imagine we're we're and this is just like the strategy in general is like we're priced as aggressively as we can be given the technology, given the compute that's required.
*  You see this in every API release that we do where we're always lowering prices.
*  We're always trying to make things more competitive for our customers.
*  I don't know what the specific drivers are for Dali 3.
*  I know that it's like again, at the end of the day, it's like a really, really powerful model.
*  So I imagine that there's significant costs that are associated with us generating those those images.
*  Hopefully, hopefully it gets cheaper. But, yeah, I don't have any.
*  I also think there's like a ton of safety system stuff that's happening around Dali 3 and some of the other like image modality models.
*  So that could be a driver as well, but not not 100 percent sure.
*  Gotcha. OK. So also announced yesterday, Whisper Large V3 not yet available in the API, but interesting to note that English is not the lowest word error rate.
*  So definitely a big focus on kind of lots of different languages, so much so that some other languages, I think English was like, you know,
*  on two benchmarks was like in the number seven spot and maybe the number three or four spot.
*  So I don't know if you have any comment on that, but that was kind of interesting.
*  Yeah, I'm super excited because, again, one of the core challenges of language models and just like the Internet in general is like there is a disproportionate focus on English.
*  It just makes these products and services that are built around language like much less accessible in places where English isn't the first language.
*  I think Whisper focusing on non-English is a super positive step.
*  And I think it's something that we'll have to do more broadly across all of our models is really make them sort of world class in all these languages that exist around the world.
*  So I'm excited for people to get V3 in the API.
*  I think it's just like a lot of work to spin that model yourself and run it and do all the things that are required.
*  And we've gotten such positive reception from putting V2 of Whisper in the API.
*  People really liked it and made it so that anybody could use it and not have to worry about all the GPU stuff that's required to go and run it yourself.
*  But I also think it's important to make some of these things open source.
*  So I'm glad that we did that as well.
*  Yeah, cool. I've seen some interesting demos already, too, of people changing language kind of mid audio file and handling that seamlessly from what people are reporting.
*  So some very cool possibilities there.
*  Obviously, the other side of understanding audio is generating audio.
*  So the text to speech API here, pricing seem pretty aggressive again, comparing the one point five cents per thousand characters or three
*  cents per thousand characters for the HD audio to 11 labs.
*  It's like a full order of magnitude cheaper.
*  They're like in kind of 15 to 30 cents per thousand characters from what I was seeing today.
*  So that's a notable price drop.
*  That's definitely going to probably spur some additional price drops if I had to guess.
*  I wonder if there's if you have any comments on the kind of the strategy of the voices.
*  This is something where I've commented many times that, you know, may well it may have been sort of an accident or kind of not expecting the thing to take off as much as it did.
*  The name chat GPT, I think, is really kind of a service to the public in that you can't really answer or it's not easy to anthropomorphize chat GPT.
*  Just sounds like a robot. And I think there's something really good about that, that like it's a constant reminder that it's not a human, even though it may pass the turning test or whatever else.
*  I feel kind of the same way hearing the voices.
*  It feels to me like they are at a really nice balance point.
*  And I've been a connoisseur shopper of different, you know, text to speech solutions.
*  It feels like it's at a really nice balance point where it's like still slightly uncanny valley and doesn't sound human.
*  Like, I think I will know, you know, when I'm hearing it.
*  But at the same time, it's like very pleasant and kind of natural.
*  Is that what you were going for with that, to try to kind of, you know, still make clear to people like when this is an AI voice?
*  I'm not 100% sure, to be honest with you.
*  I think you are probably as a connoisseur of these voices, probably like uniquely in that position where you could make that assessment, kind of like how I feel these days when I see like text and it's kind of sometimes easy to tell whether or not it was generated by me or not.
*  I think if you look at like the average person who is like not deeply in the AI space, like you could probably show them those voices and convince them that it was a real human.
*  I think that's one of the challenges of TTS is that we and this is explicitly part of our usage and term limits today is you have to tell people that this is not a real human voice.
*  So regardless of whether or not it's it's it is not intended to be like extremely human like to convince to to a fault humans that they're talking to a human.
*  We want this to be clear that you're talking to an AI, just like again, with the terms of service of all of our of our products were not we don't want people to be misled.
*  And again, I don't I can't speak to whether or not that was specifically part of the strategy for making those voices.
*  But yeah, they are they are extremely good.
*  I was playing around with a bunch of them and I think we'll have more in the future as well.
*  But the existing ones just do a good job of.
*  Striking a nice balance, as you said, I think there's going to be so many cool use cases that people come up with for TTS.
*  It'll be it'll be exciting here. I was just talking to my younger brother today and he was working on a blog post and I was like, use TTS, like have given audio version of it, too.
*  And like, it's just it's going to be so easy.
*  I think the thing that Eleven left, to my understanding, at least, and I haven't played around with the product a ton, but the nice part for them is like,
*  I think they have like a whole front end setup where like you you really as somebody who's never programmed before could go in and generate, like take your text and turn it into audio.
*  And I think people under appreciate like the costs associated with doing things like that.
*  And that could be part of the reason why they have some of the higher costs than than us, potentially.
*  And I haven't actually looked at the numbers myself, but I trust you.
*  So there's there's always those non-trivial expenses.
*  And like we have some of this. If you look at why chat GPT is more expensive than the API, well, there's more going on than just like the bare metal API powering that experience for people.
*  So I think they'll continue to be competitive.
*  And like at the end of the day, our TTS is only available through an API.
*  So like it requires like a sufficient level of customer experience using our customer knowledge to use a curl request or a Python request or what have you.
*  Yeah, I think there's a couple of the things, too, that mean that the text to speech companies are not killed by this release.
*  First, the voice cloning is a huge one.
*  You know, I cloned my voice with both 11 Labs and PlayHT, and that's just not something that the API is offering.
*  Seems like it's probably enough of a kind of hairy ball of wax that you just like might not get there for a while, if ever.
*  And then there's also kind of the emotional direction, which I could see that being something OpenAIM might eventually take on.
*  But if you're trying to make games and trying to make characters and really trying to bring kind of an energy to it, that's like not your sort of kind of NPR narrator or like call center agent energy,
*  then that's something that's just not in scope right now, but those other companies are already doing quite well.
*  So I definitely think they will continue to have a very significant amount of usage for those reasons.
*  Stitching these modalities together, is there like an Omni API coming?
*  Like, it seems like right now I have to call Whisper and then hopefully I can stream my Whisper tokens into the language model somehow.
*  And then it will then stream me back tokens and then I got to send that to the text to speech.
*  But it seems like integrating that into one API where a stream audio in and a stream audio out, maybe with kind of the text almost as like logs, is the future.
*  Is that kind of what you would envision the future looking like as well?
*  Yeah, I would imagine we do something like that.
*  And mostly because like right now, and this is the case across all of our APIs, like if you integrate multiple things together, you pay the round trip penalty many, many times.
*  And that's like just the least good experience that you could have.
*  So it makes sense.
*  And like, again, I don't know when that would come, but I would imagine we end up doing something like speech to speech.
*  It seems like that is definitely on the natural path.
*  Reproducible outputs. I thought that was really interesting.
*  Is that essentially equivalent to me caching responses on my side or like what does it add, if anything, beyond kind of if I were to implement my own cache on generations?
*  The challenge is even if you cache the generations previously, the generations might be different for the same prompt.
*  So this is fixing that. So like if you're attempting to fix that, it's still in a beta right now.
*  But now you can pre-specify the seed and you shouldn't for a given input is the same with the seed being the same.
*  You should get the same output.
*  And the way that you verify that all of these things should be the same as the system fingerprint, because again, there's much more going on than just that seed parameter behind the scenes.
*  Tons of things baked in the system fingerprint for two outputs.
*  If it's the same, it should give you the same the same output.
*  And this just makes like the whole process more more reproducible.
*  So I don't think caching wouldn't solve this problem today.
*  Again, you could you could cache the inputs and the output and then like give people the same thing.
*  But then that's yeah, like you could have done that.
*  But I think it's it's in the vein of solving a different problem, which is people want to be able to like thoroughly test these systems.
*  And you can't really do that if you don't know what the expected output is supposed to be like.
*  It's just hard to make unit tests and stuff like that.
*  Probably biggest surprise to me was the log probabilities coming soon.
*  I had never expected to see that again for at least for the best models, because my thought was you get those log probes.
*  Now you're opening up much easier imitation learning for everybody that wants to kind of match GPT-4.
*  I assume that that's still the case. Right.
*  So does this mean that basically there's just no concern about anybody matching GPT-4?
*  Generally, we are concerned about the leakage of intellectual property.
*  I think it's specifically going to be log probes for output tokens, which is slightly different than pure log probes for input and outputs.
*  I think that slightly changes it.
*  I also think at the end of the day, developers have really asked for this.
*  And there are certain use cases that just aren't really possible without log probes.
*  So it's mostly it's mostly for those people, like for the people who have asked for the people who want to build products that require this.
*  I'm happy that we're doing it. There's been a ton of interest for like the last six to 12 months.
*  It's just like how to do it in a way that balances all the other things is the hard part.
*  My read on that is that it really does kind of reflect that all of these like we match GPT-4 things basically are not close.
*  And, you know, it's because if it was happening that way, presumably it would be a different decision.
*  But, you know, I take this as an update that, yeah, all that stuff is kind of bullshit.
*  But you don't have to say that I'm saying that.
*  I trust your opinion, but I'm not sure if narrow domains.
*  You know, I yeah, a lot of a lot of caveats there, but we got more fish to fry.
*  So GPT is an assistant.
*  So this is kind of obviously the big star of the show coming into this.
*  You know, the earlier generation of kind of the expansion of chat GPT was plugins, plugins, you know, Sam A and others that said, you know, hadn't really achieved product market fit.
*  I guess for starters, like.
*  What is conceptually the evolution that you think takes plugins which weren't quite working to GPT's, which hopefully will really work?
*  Yeah, I think part of the challenge with with plugins was that you had to be developer to make them be.
*  It was, you know, there was a bunch of like system slash product things that that we just never had time to like perfectly optimize.
*  There were certain things that just like weren't visible to the user that probably should have been and other things like that.
*  I think GPT's is like this this perfect evolutionary story of where plugins are today.
*  Really, you get like all of the value of of custom instructions of all these different modalities.
*  And like this is, you know, if I go back as somebody who was running the chat to be to plug in store, people were like asking like, how do we get code interpreter with my plug in?
*  How do I get X, Y and Z with my plug in and really go deep on making this like a truly custom experience owning the experience end to end?
*  You can now do that with GPT's and you can still have the best of both worlds where you take the API that you were using with with chat to be plugins and make that accessible as an action inside of it.
*  So it's I think it's like a slight refactor of the overall framing of the problem.
*  But intuitively, if you're somebody who had a plug in, who had users, you can now go and make a GPT and you should be able to do the similar things with a ton more features built in.
*  Like, again, it was a real trade off for customers to be like, oh, I want to use X, Y and Z plug in.
*  But now I'm sort of losing out on a bunch of the modalities that I had in my in my other chat sessions.
*  And the GPT really sort of puts a nice bow on solving that problem.
*  So the kind of three elements of this and then it gets more nitty gritty on the API side, of course, but instructions, expanded knowledge and actions.
*  Instructions are pretty straightforward. That's your classic prompt engineering.
*  Expanded knowledge is where the platform expansion of bringing the vector database into the platform is obviously being powered so people can upload their own documents, etc, etc.
*  And then the actions is I understand that there's basically three kinds of actions.
*  One is using the retrieval to actually go get the knowledge out of the data store.
*  There was a really interesting tweet posted from a breakout session that kind of showed that, like, all the tricks had been kind of thrown at that from your hypothetical document embeddings to your re-ranking to whatever,
*  you know, at least per the metrics on that slide looks like it's going to perform really well.
*  So I'm looking forward to getting into that more.
*  Then there's code interpreter, which is where the system can write and execute code on OpenAI's runtime.
*  And then there's the ability to call functions back to the either that the GPT kind of defines and makes available or on the API side that the developer defines and makes available.
*  So that's kind of all just foundation laying. I think people largely know that.
*  How do you kind of see these things coming together?
*  One thing that I was initially playing with it and I was like, OK, here's the Dali 3 GPT and here's like some other GPT.
*  But can I have them together?
*  You know, or if I with the demos to it was like, OK, here's Zapier and there's a couple of different things happening there.
*  What if I want to use like Zapier and something else, you know, and my like Google Calendar or and my Slack?
*  Do I have to like tie all those things through Zapier weirdly or can I have like all these different things kind of as because that was one thing that the plugins did seem to have a little bit.
*  At least more clear as of now.
*  I hear that. I think that that's true.
*  I think with plugins, you could sort of enable two or three things at the same time and have those available in the same GPT.
*  You can do this with GPT's today.
*  You would just use multiple actions.
*  I think the the current product experience, you have to sort of know what the URL for those APIs are if you were going to use like third party plugins.
*  So it's really more so designed today with actions of like you using your own API and your own your own plugin manifest or open API file.
*  I think it's possible that changes over time to like allow more for like the integrating of Gmail.
*  At the end of the day, like people really want that.
*  They want to be able to say like, I have this super powerful single GPT that does these five different things for me.
*  And I go in and I check the different modalities that I want or I check the different features and services that I want.
*  We're just not there today. I think eventually we'll get somewhere that has that because that's that's what consumers are going to want, whether it's actions or some different iteration of that.
*  And I don't know for sure, but it's definitely something that makes a ton of sense to have.
*  Like you don't want every single developer, every person making a GPT to have to go reprogram like their integration with the Gmail API, for example.
*  Like you just want something that sort of works across all of them and you can just one click, check that it works and then you're going to go.
*  Yeah. So for now, if I'm an enterprise and I've got G Suite over here and I've got Slack over here, basically I can go and just set all those different things up as.
*  Actions, you know, kind of mix and match on my own, but I don't have like a higher level, you know, click this, click that and just kind of naturally import.
*  But we but you can do it if you have the kind of wherewithal to go list out all the actions that you need.
*  You can do it and you could also technically use some of the third party plugins to do this as well.
*  I think the real challenge and this goes back to like why hopefully GBTs are a better evolution of this is like you just have to be when you don't control the plug in yourself or your it's not you like writing the code and stuff like that.
*  You just have less control over like what's happening with this data that I'm using or that I'm sending back and forth.
*  And I think there's like a strong incentive for like Gmail hasn't actually made a plug in.
*  It's any any email plug in. It's like a third party provider.
*  So you really have to be comfortable with like I'm making my data accessible to some third party.
*  And like the chances are you don't know who that third party is really strongly.
*  There should be, I think, a bias for companies, especially making these things to think about like you should probably make the Gmail integration yourself.
*  It makes a lot of sense. I'm very, very careful about who I allow into my Gmail and G Suite for more broadly, certainly.
*  How are you handling off on this stuff that was kind of skipped over in the demo?
*  But, you know, with the Zapier one, for example, how do I connect this to my Zapier?
*  And then on that end, I assume like all the Zapier is integrating to Slack and Gmail, whatever, like that's kind of within the Zapier platform.
*  Is that right? Yeah, for the Zapier case, that's true.
*  I think Zapier has done some interesting things.
*  I don't want to say getting around this, but to enable it in like a more seamless way you do.
*  So each individual endpoint as part of an action, you can specify the auth for and actually think again, going back to like the differences between plugins and actions.
*  This is one of the positive things about or very, very positive.
*  One of the one of the many positive things about actions is that you now have access to like hybrid auth.
*  So you can have certain endpoints that are that don't require auth.
*  You can have certain endpoints that require auth.
*  You can also set certain actions as consequential or inconsequential, and that controls whether or not the user is prompted to like explicitly allow a certain action to happen so that the model is not like doing things on your behalf without your consent.
*  So I think both of those things are like core features that plugin developers have been asking for, like how can I make sure that users are knowingly sending data somewhere?
*  And how can I make sure that I don't gatekeep everybody at the very first step and force them to sign in and allow them to sort of get their feet wet with my product?
*  And then when they want to do something like save it or what have you, it forces them into auth.
*  I think both of those things are not are not possible with with actions.
*  That saving mechanism.
*  Is there anything like that for the retrieval that's built in?
*  Like, could I update a document or sort of add to the files?
*  Yeah, for GPT's, you can go in and edit them after you create it.
*  So you can actually change anything.
*  So it's the instructions can be iterated on.
*  The files can be iterated on.
*  You can go in and change your custom actions if you want to.
*  You can turn off certain capabilities.
*  So it's all fully customizable even after you've initially created the first incarnation of that.
*  The retrieval, again, looks pretty amazing and the annotations are cool as well.
*  There's some really nice developer conveniences that have been added to like the files, several new tabs within the kind of just platform website.
*  I'm looking forward to when files have a little preview of the first how many lines of the file as well as just a, you know, maybe breadcrumb.
*  Not that that one's unobvious, but a question on the billing.
*  So it's 20 cents per gigabyte per assistant per day of content backing, right?
*  Is that is like one gigabyte the minimum or is there is there some smaller gradation of storage that is billable?
*  It's a good question. I don't know off the top of my head.
*  That's also specifically for file retrieval.
*  So it's specifically for uploaded files that get embedded.
*  I would imagine that that's like there's also a breakdown of like if you only upload half a gigabyte, I'd imagine you're being charged half that half that price.
*  I'm guessing it's not just like you get charged 20 cents regardless of how much data you put in there and imagine it's broken down.
*  I could be wrong about that. So I'll test and follow up afterwards.
*  But I haven't actually tried it to know off the top of my head what the billing looks like.
*  I guess vision over time would be maybe more kind of control over retrieval as well.
*  Right now, it seems like it's very black box.
*  Like, as far as I could tell, I don't have any way to kind of say what I want my chunk size to be or how many records to pull.
*  That does have some implications if I'm like pulling much records and then using that in context because other tokens.
*  Right. So am I right that it's pretty black boxy right now and I guess more to come?
*  Yeah, you should have some level of control because you could tell the model in the user message or in the system message, like how you want it to perform in those cases.
*  And like at the end of the day, it's like it's still GPT-4 or GPT-4 turbo in this case.
*  So it will follow those instructions. So if you say like always only answer questions based on the first three images that I upload, like it should be able to follow those instructions and ignore some of the some of the other stuff.
*  So you do have that level of control from like a chunking perspective.
*  Maybe that's something that will end up releasing.
*  What tends to happen is like we end up making the thing that is going to be like most usable for most people.
*  And you see this actually fine tuning is a good example of this, where we actually like automatically set the hyper parameters for you.
*  And in certain cases, you can override those and like change them yourself.
*  But like we're doing it based on the best practices of us fine tuning many, many, many models.
*  And people just tend to like more often than not modify those parameters.
*  And like it ends up being detrimental to their like it's a net negative for them instead of being like a net positive.
*  So I would imagine it's possible that like the patching or chunking for the images ends up being something that we give people more control over.
*  But it's not possible today.
*  The fine tuning UI also within the platform site.
*  Definitely a really nice upgrade. I love being able to see the loss curve, even just to get a little bit of a sense for how long is it dropping?
*  Where does it start to flatten off? Why is this one run like just generally lower than the other?
*  Definitely a lot for me to kind of dig into more there and better understand what's happening with fine tuning.
*  And we can use fine tuned three, five, 16K function calling for assistance.
*  Is that right? Or is that not yet?
*  You should be able to do it for assistance. I'll double check that it's that it's compatible today, but you fundamentally should be.
*  Yeah, clearly this is where it's going. Cool.
*  So a couple just questions on like best practices or conceptual stuff for the assistance.
*  You know, I'm doing a bunch of prototyping stuff with this company, Athena, in the executive assistance space.
*  We've got all these clients. They're all very different.
*  And so I'm kind of wondering here, is this a situation where I create one like Athena assistant and then I provide like runtime context differently,
*  you know, with kind of our client profile file and maybe some recent history or whatever.
*  But it's all one assistant with a thread per client.
*  Or should I be thinking about it more as like one assistant per client? And how would I know the difference?
*  Yeah, that's a really good question. I think it fundamentally depends on like whether or not each assistant would have.
*  Different different instructions and different capabilities.
*  You could make images or you could make files accessible at a specific thread levels like you can if that's the only thing that you want to change between them, then that would make sense.
*  I do think it probably you probably would want to like tailor the assistant on like an individual basis, or at least is the thing that I would I would consider trying.
*  You just have to be more general and like it'd be more useful to like take all the context that you have about somebody and like put or about the whether it's the actual person who's the assistant or the person who's the client and like put that into the system instructions for the assistant specifically.
*  So you probably just lose a little bit of custom customization if you try to make like a general assistant.
*  But I do think that would be like a worthwhile starting place and then, you know, having an option to like go in and customize deeper potentially as a as like a next step.
*  OK, cool. Makes sense more. Definitely a lot of discovery ahead on that front.
*  Safety, you mentioned safety. There wasn't too much talk about safety yesterday at the keynote.
*  Could you give us any information on like? The red teaming that went on behind this?
*  I don't know. Open AI has obviously been very engaged in policy, has made White House commitments.
*  So per those White House commitments, if nothing else, like clearly there was some red teaming.
*  I don't know if there was like a report submitted to the government or if there will be any sort of like system card coming, especially with this kind of assistant paradigm.
*  But it does seem like, you know, probably a lot went into that. And I'd love to hear anything about it that you could share.
*  Yeah, it's a good question. If you look broadly at like what assistance is, it's not fundamentally something that's like a different capability that has existed previously.
*  It's really like chat completion, strung together with a database and then a bunch of other modalities that we already had accessible other places now accessible in assistance specifically.
*  So we've read teams and done a lot of the safety work like for each of those individual modalities on the I think like the thing that I can publicly point to from a safety
*  perspective is around vision. So we did release like a vision safety card, GPT-4 with vision that folks can go out and read.
*  It's available on the Open AI website. And there's like a full 18 page breakdown that goes through all the all the questions and challenges around vision.
*  I think it's actually really interesting if you want to get a sense for like the things that we've thought about, the high level problems of like trying to make a general reasoning system.
*  It's incredible to see the work. And I think there's also like a page that goes through like all of the people that we've worked with to make vision come to light.
*  And if you think about like, you know, what was the limitation from getting Greg's demo of vision working back in March to actually making it accessible as a first party and third party products in our API?
*  It's like all of that safety work really is like one of the huge things that we've done. And again, it follows the same trend of what happened with GPT-4 where, you know, GPT-4 was ready long before the model was actually released to the public.
*  And there's just so much safety work and and thought that goes into how to build systems in a scalable and safe way.
*  I'm happy and huge kudos to the teams that have done the work and all the right teaming that's happened.
*  Cool. Yeah, I'm going to go in and see what I can do on the jailbreak fund. A while ago, there was a like bug bounty program or kind of a teaser of that. Is there is that actually happening? Do I get paid for jail breaks now?
*  Jail breaks is a good question. I don't know if jail breaks fall into the considerations of the bug bounty program. I believe the bug bounty program is constrained to like you find an exploit to like access one of OpenAI systems or something like that.
*  That program is definitely live and accessible and we definitely find bugs and people definitely get bounties, which is awesome.
*  I don't know if jail breaks are a part of that or not.
*  It has we use the platform that everybody uses for a crowd something.
*  I forget the name is escapes me at the moment, but it's the same platform that every company uses for this.
*  So it has all the like eligibility details and I believe we'll say whether or not jail breaks are one of the things.
*  My understanding is that they're not because it's not it's like more of like a system level like security vulnerability rather than like a model behavior thing.
*  At the next roundtable about this, put one in for me on moving jail breaks into the eligibility category for that.
*  I honestly think it would serve everybody pretty well because Lord knows there's just insane surface area here and you know you need a lot of people to kind of go out and explore weird spaces.
*  So a little incentive I think is pretty helpful.
*  I think that's fair. Yeah.
*  So the last thing is you know the end of the keynote Sam said this is all going to look quaint compared to what OpenAI is cooking up for us now.
*  I mean that's pretty insane.
*  Obviously, I know you aren't going to tell us what we're going to have a year from now.
*  And I guess my real question is to what degree do you guys even know that?
*  Right. I mean, do you have a roadmap that is kind of well established in your own minds for the next year?
*  Or is it going to be the kind of thing where you've raised the platform level?
*  Obviously, now another thousand kind of things, if not a million things are going to kind of blossom on top of that platform and then take all that into account and kind of figure out what the next.
*  You know, platform raises.
*  I guess it's probably both.
*  But how do you think about that balance?
*  Yeah, I think the research roadmap is both more laid in stone, but also less, less predictable.
*  And I think that's going to drive a lot of the like what ends up being released is like what research are we able to do and what are the new sort of breakthroughs that we're able to achieve that then enables us to bring products to market.
*  So I think that that's like the biggest open question.
*  The research team knows where they're making bets as far as like, you know, because they actually have to allocate compute to these things.
*  So they know in the top of the head of like, you know, where are the ten places we're making bets and what can those things potentially yield?
*  I think the real question is like, what are those things actually work and result in like an amazing new product modality, whatever it is, and making that accessible.
*  So I think it's I have less of that insight because they're actively doing the research right now and we don't yet know.
*  But yeah, it'll be every every time after we do a big release like this, I'm like, there's nothing left to ship.
*  There'll be nothing. And I'm just just, you know, talking to you today and seeing the announcements yesterday and listening to a lot of the conversations like there's so many things that are yet to come that are going to be super, super important.
*  And it's a lot of obvious things, too.
*  It's like not things that are like crazy groundbreaking, but are going to lead to people to be able to do the incredible, crazy, groundbreaking products.
*  So I'm excited about that.
*  Fast times that open AI always and in the AI space more broadly as well, we'll be digesting this for weeks, if not months to come.
*  And for now, I just want to say again, thank you for all the time and all the clarifying answers.
*  Logan Kilpatrick, thank you for being part of the cognitive revolution.
*  Thanks for having me, Nathan.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me on the social media platform of your choice.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it and I recommend you use it to use Cogrev to get a 10% discount.
