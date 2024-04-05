---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 2342s
Video Keywords: []
Video Views: 872
Video Rating: None
---

# Advancements in AI: Updating the Scouting Report, Task Automation, and Google Breakthroughs
**Cognitive Revolution "How AI Changes Everything":** [August 10, 2023](https://www.youtube.com/watch?v=2GuURchrvOE)
*  multimodal med palm doesn't just take in text and answer questions.
*  It now takes in all sorts of other kinds of data,
*  including medical imaging.
*  It can take in this slide and a patient history and work with all of that and give you
*  back input that takes all of that into account.
*  It's starting to have all these different senses.
*  The human brain is not the end of history,
*  the transformer is not the end of history,
*  and I think we're starting to see as the whole world is
*  flocked to AI in general,
*  we're starting to turn over a lot of stones for
*  other possible architectures that might work.
*  Hello and welcome to the Cognitive Revolution,
*  where we interview visionary researchers, entrepreneurs,
*  and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology will transform work,
*  life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Thorenberg.
*  Let's get into the scouting report.
*  You released it a month ago,
*  you've heard some feedback on it.
*  I'm curious how your views have evolved or anything you change there.
*  Yeah, by and large feedback I think has been really positive.
*  We don't have a huge YouTube channel,
*  but it's definitely been one of our more viewed videos,
*  and the feedback has been really encouraging and just appreciative up to it,
*  including you could be charging for this and I appreciate that you're not.
*  At least for the foreseeable future,
*  I'm pleased to continue to make it available to everybody at no cost.
*  But yeah, the situation does continue to evolve.
*  One super small errata bit is I should have credited
*  the legendary YouTube channel 3Blue1Brown for a couple of graphics,
*  which I omitted and somebody called me out on that appropriately.
*  I had actually previously credited them for that graphic on Twitter,
*  but it didn't make it into my slides.
*  That'll be one very small adjustment.
*  But to give credit where it's due,
*  I think the 3Blue1Brown neural networks intro,
*  which is now fully five years old and basically dates to
*  right around the same time that the transformer paper came out,
*  is actually still a super relevant and useful reference.
*  It's not easy to make content.
*  We talk about this all the time.
*  Two weeks from now, this podcast already starts to feel dated.
*  But with the scouting report and also with this neural network classic of his,
*  I think he really has achieved something that is worth going back to there.
*  Specifically, if you've seen that channel,
*  you know that just phenomenal visualizations of complex concepts.
*  When I was really starting to go down this rabbit hole at first,
*  I think that was one of the most useful visualizations that I came across.
*  That's why it's excerpted into the scouting report.
*  You won't get anything about transformers there.
*  Transformers weren't really much of a thing at that time.
*  But what you will see is a really elegant visualization of some of
*  the same core concepts that we cover in the scouting reports,
*  such as backpropagation and how the information flows forward in a network,
*  and also backward in a network, masterful job there.
*  I regret not having credited and definitely recommend checking that one out.
*  I think the conversation with Zvi from last week was
*  another interesting conversation that drove a few changes that I would want to make.
*  I asked him and I specifically was looking for that going in.
*  I asked him to give feedback on my tail of the cognitive tape,
*  which is the rundown of comparative strengths and weaknesses between
*  a human expert and a cutting edge 2023 AI like a GPT-4.
*  We're now a CLAWD2.
*  He highlighted, I think something that I had omitted that was important,
*  which is a sense of robustness to unfamiliar or even adversarial circumstances.
*  What that means is,
*  humans in general, we can take a punch literally or cognitively.
*  We may wobble for a second,
*  we may get confused,
*  but we have a pretty sturdy,
*  at least most of us have a pretty sturdy base where it's pretty hard for you to
*  hijack my thoughts too much with any language that you might generate.
*  At some point, I'm just going to be like,
*  I don't know what you're trying to do here saying all this stuff to me,
*  but it's starting to feel too weird and I just shut down
*  and start to just not want to listen or not want to engage.
*  I can keep my goals intact,
*  keep my priorities even in the face of
*  these highly unexpected things most of the time.
*  In fact, maybe you could say status quo bias,
*  maybe people do it too much,
*  maybe we're too reluctant to take on new information,
*  but everything has pros and cons.
*  If you're super quick to take on new information,
*  then you're also more hackable.
*  If you're too slow, then you don't update
*  maybe as much as you should in response to new information.
*  Definitely a balance there,
*  there's going to be false positives and false negatives.
*  We're tuned in a certain way that gives us
*  this medium and long time horizon robustness even in
*  response to highly unexpected or adversarial inputs.
*  Adversarial would be outright like somebody,
*  you're trying to trick me.
*  You're not engaging with me in good faith,
*  but you're actually trying to confuse me or deceive me or con me or whatever.
*  Those would all be adversarial interactions
*  that somebody might try in a human and it's not easy.
*  It's not easy to con somebody out of their money or out of whatever.
*  It can be done,
*  but it takes real skill to do that.
*  With the AIs in comparison,
*  it's a lot easier to throw them way off.
*  This is something that they are getting better on as
*  of course they're getting better on everything.
*  But early GPT-4, for example,
*  I called it at one point the world's worst chemistry tutor
*  and this was not an adversarial example.
*  This was just me simulating what would happen if I was
*  a confused chemistry student and I went to it for help.
*  What I found was asking it a chemistry question,
*  can you help me balance this equation?
*  It could do that.
*  But then if I said,
*  here's how I'm balancing this equation,
*  it would not really do what it needed to do to be helpful to me,
*  which is correct my misconceptions.
*  If I show up as confused,
*  then it would in the early days all too often
*  accept my confusion as a premise
*  and then proceed with its own confusion and do a bad job.
*  At that time, it was the world's worst chemistry tutor.
*  Now they have made progress on that
*  and folks like Khan Academy coming up soon
*  as a future guest have also worked really hard on prompting
*  and particular strategies and grounding
*  and having examples that they swap into and out of context
*  so that they don't just rely on the models,
*  native-native ability, but really try to make sure
*  that it is alert to the possibility of user confusion
*  and responding to that in an effective way.
*  I think that is mostly now working at least for basic cases.
*  If you show up and say,
*  hey, I balanced this equation in this way,
*  what do you think?
*  It will probably, certainly with Khan Academy
*  and probably increasingly also with just CHAT-GVT,
*  most of the time it will not get confused by your confusion,
*  certainly not as much as it used to.
*  But you still have all these like jailbreaks
*  and kind of adversarial things,
*  and people kind of concoct these different examples
*  where you can get it to go off the rails
*  and just like once it's kind of confused,
*  it often like doubles down on its confusion
*  and doesn't really get it.
*  There is some interesting research coming out
*  to try to address that problem.
*  One paper, and I'm hoping to get the author
*  on in fact, our Div Garg from Multion
*  was like a contributing author
*  where they added the concept of a backspace
*  as one of the things that the AI can do.
*  So instead of always today,
*  like generating one token at a time
*  and kind of whatever you just generated,
*  you're kind of stuck with it as like,
*  the thing that leads into the next thing you have to do.
*  So your mistakes can compound
*  and kind of lead you off the rails.
*  That is to some degree addressed
*  by this addition of a backspace.
*  So now they're starting to teach the models that like,
*  oh, well, if you do end up in kind of a weird spot
*  that feels like it's easy to start to anthropomorphize here,
*  but I need to study this a little bit more too
*  to really understand the math behind it.
*  But there's some sense where like you're out of distribution
*  and now you have a way to deal with that
*  that's other than just continuing to add on,
*  you can actually backspace
*  and literally just delete the last token
*  and try again from there.
*  And that is I think gonna do quite a bit of good
*  for this robustness problem
*  because it should at a minimum,
*  like allow it to kind of start to recover better
*  from any temporary mistakes.
*  We see this behavior now sometimes too,
*  where it's like, oh yes, I'm sorry.
*  You know, first I thought this or whatever,
*  but honestly today, even with GPT-4,
*  it doesn't usually work that great
*  or like it often doesn't work that great.
*  You know, once it's confused,
*  like now it's just kind of doubly confused
*  or it starts to like grasp at explanations
*  and it's not there.
*  So overall, you know, Zvi highlighted
*  that robustness should be a category.
*  And right now humans have the edge in robustness,
*  possibly to our somewhat detriment
*  in that we maybe don't update as much as we should
*  on new information, but the AIs, you know,
*  they don't handle things that are like truly bizarre
*  to them, you know, nearly as well as we do.
*  Another good example from this,
*  and I hope to have these authors on too,
*  is there was just this paper about the universal attack,
*  the universal jailbreak.
*  And it's very weird.
*  Basically they took LAMA, I don't know if it was LAMA 2,
*  but they took some, you know,
*  whatever the latest open source model that they had
*  as they were doing the research.
*  And they actually used a learning approach
*  to figure out how to optimize for some text
*  that they could append to basically any input
*  to get the model to follow the initial instructions,
*  despite what the creators intend.
*  So you can look this up, it's like very weird,
*  but you might say, whatever, something bad, right?
*  Tell me how, the classic, tell me how to hijack a car.
*  You know, Claude will say, and GPT-4 will say,
*  sorry, you know, I'm here to do good stuff, not bad stuff.
*  Like, I can't help you hijack a car.
*  Now what they found is with,
*  and they developed this on LAMA,
*  but the interesting thing is it transferred
*  to these other leading models to varying degrees.
*  They developed some way to figure out,
*  what can I add onto that, such that instead of refusing,
*  it will just do it.
*  And they found that these very weird strings,
*  you know, which strings just text and text is just tokens.
*  It's just a bunch of random tokens.
*  It doesn't really make any sense.
*  It doesn't mean anything to you or me,
*  but it kind of serves as like a magic key
*  to getting past these filters.
*  And then again, what's really interesting about it is,
*  even though they developed it on LAMA,
*  which they had open source, and so they could,
*  I'm not a hundred percent sure it was LAMA,
*  but on the leading open source model
*  where they had access to all the weights
*  and could look inside it and do an optimization
*  to cause it to behave that way.
*  What they found then is if they took that same,
*  magic key of this random looking string
*  and sent it to the open AI models,
*  that it would very often still work.
*  And so there's something fairly general about this.
*  Not fully general, interestingly,
*  because Cod doesn't seem to be nearly as susceptible
*  to that particular attack,
*  but the open AI models are, and like the other big ones
*  that they tested pretty much with the exception of Cod
*  were like still very susceptible to that.
*  So again, this is another instance of like this robustness.
*  Like there's almost nothing I could say to you,
*  in kind of a magical incantation way
*  that would get you to like behave in ways
*  you don't wanna behave, but with the AI,
*  like these kinds of nonsense things
*  can be found that do that.
*  So anyway, future edition will have a line item
*  for robustness.
*  Another minor one there too is just consistency.
*  I found this nice graph that, it's very simple,
*  but it just shows that human performance
*  is much more variable than AI performance on a given task.
*  In the current version, I have bedside manner,
*  and I was emphasizing that the AI is patient,
*  it's empathetic, like in many cases,
*  it's been shown to be more empathetic than people,
*  whether that's customer service or even medicine.
*  Going back to our Zach Kohane episode,
*  he was like, we're all burned out in medicine, man.
*  We don't have time or energy to like write nice notes
*  to patients really,
*  but GPT-4 does, and it does a really nice job of it,
*  and so this can help us communicate more empathetically.
*  So I had called that bedside manner.
*  We probably wanna generalize that a little bit
*  to consistency, because I think what that really reflects
*  is just the AI shows up the same way
*  pretty much every time, subject of course
*  to these like robustness things,
*  but in a normal down the fairway use,
*  it's never like had a bad night's sleep and is super grumpy,
*  it's never on like a manic tear,
*  it is like punching above its weight,
*  it kind of just hits like for singles and doubles every time
*  and its performance tends to be in a narrower range,
*  whereas humans obviously have a lot more variability
*  and we've all had these experiences where you're like,
*  what the fuck, this nurse is being rude to me or whatever,
*  and I've got problems here and you're being this way,
*  and just the AI is just not gonna do that.
*  It's gonna be kind of unfailingly polite
*  if that's what it's meant to do.
*  Again, bracketing like outright jail breaks
*  or like adversarial examples,
*  but in the context of earnest users,
*  just showing up and trying to do
*  what they're meant to be doing,
*  AI will be more consistent in its tone.
*  It doesn't have these sleep deprivation
*  or other kind of similar mood swing sort of issues.
*  Hey, we'll continue our interview in a moment
*  after a word from our sponsors.
*  If you're a startup founder
*  or executive running a growing business,
*  you know that as you scale, your systems break down
*  and the cracks start to show.
*  If this resonates with you,
*  there are three numbers you need to know, 36,000, 25, and one.
*  36,000, that's the number of businesses
*  which have upgraded to NetSuite by Oracle.
*  NetSuite is the number one cloud financial system,
*  streamline accounting, financial management,
*  inventory, HR, and more.
*  25, NetSuite turns 25 this year.
*  That's 25 years of helping businesses do more with less,
*  close their books in days, not weeks, and drive down costs.
*  One, because your business is one of a kind,
*  so you get a customized solution for all your KPIs
*  in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts, and improve margins.
*  Everything you need, all in one place.
*  Right now, download NetSuite's popular KPI checklist
*  designed to give you consistently excellent performance,
*  absolutely free, at netsuite.com slash cognitive.
*  That's netsuite.com slash cognitive
*  to get your own KPI checklist.
*  Netsuite.com slash cognitive.
*  Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it,
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  I'm curious how this all relates
*  to the AI task automation thing.
*  Maybe we could preview what you're working on
*  in a future presentation.
*  So I've alluded to this a couple of times,
*  and the consistency point is really key there.
*  It's like everybody has these bottleneck
*  time-consuming pain point things that happen in their life
*  or in their business.
*  And to give just concrete examples
*  that are very general.
*  Let's say that you post a job posting, and great news.
*  You get 1,000 resumes in.
*  Well, it's a good news, bad news situation,
*  because we're blessed to have so many great candidates,
*  but who's gonna read all these things?
*  So what do we do there?
*  That's tough.
*  And obviously people navigate those situations
*  all sorts of different ways.
*  Some of them, the classic joke is like,
*  just throw half of them out
*  because I don't wanna work with unlucky people.
*  That's probably not the best strategy.
*  With AI, we could hope to do better.
*  With task automation, it's things like that,
*  where you're like, man, I would love to be able to do this
*  10 times faster.
*  Especially if it's a meaningful chunk of time
*  that's going into it.
*  Could be episodic, like this resume thing,
*  or it could be ongoing.
*  We get 500 tickets a day in our customer success thing,
*  and 80% of them fall into 10 categories
*  where we're kinda doing pretty consistent stuff.
*  Whatever the case may be,
*  if you have a significant chunk of time
*  going into something,
*  and it's a pretty routine task
*  where you've kind of established what good looks like,
*  and where consistency matters more
*  than these kind of creative breakthrough eureka moments,
*  then you have a pretty good target for AI task automation.
*  And the consistency is a really important selling feature
*  for the AI there because the whole idea is,
*  I want to get to the point where I trust
*  that the AI's output is almost always pretty good.
*  And if I can do that, and I can satisfy myself on that,
*  then I can also kind of just really actually begin
*  to delegate work to it.
*  And in the case of resumes,
*  my typical advice would be try to set up a rubric
*  on which you're evaluating these resumes,
*  and then ultimately put them into some sort of
*  maybe five-band classification,
*  where excellent is the best,
*  and above average and average,
*  and below average and poor, or whatever.
*  And then kind of run that through the full thousand resumes,
*  and maybe just look at the ones that it deemed excellent.
*  Especially if you do a little bit of legwork upfront
*  to make sure that what it is saying is excellent
*  is in fact what you think is excellent,
*  and going back and forth,
*  refining the prompt a little bit iteratively to get there,
*  then once that's set up, you're in pretty good shape.
*  And for what I have seen, it is usually achievable
*  to get to the point where you're like,
*  yeah, I wouldn't trust the AI to make our hiring decision,
*  but I definitely can see how it can separate
*  the top half of the resumes from the bottom half,
*  or maybe the top 20% from the bottom 80%,
*  or maybe the top 10,
*  exactly where you wanna draw that line
*  in terms of how much to trust it varies by context,
*  how important it is.
*  There's a lot of considerations,
*  but the consistent, it's playing to the AI strengths.
*  Another one of the scouting reports strengths
*  is the availability and parallelizability of the AI.
*  Once you have something like this set up,
*  you can kind of keep it on a shelf,
*  and it doesn't cost anything
*  to just have that prompt saved there.
*  You can always return to it at any time.
*  You can call the AI at any time.
*  It immediately wakes up and has already had its coffee,
*  and is ready to do its thing,
*  and it's gonna be pretty much consistent with the last time.
*  There's been some noise lately about model changes.
*  I think this was something in the news that was like,
*  if all you heard was the headline
*  that GPT-4 is getting worse,
*  hopefully that wouldn't apply to anybody
*  in our plugged in audience,
*  but if all you heard was the headline
*  that GPT-4 is getting worse,
*  and you're like, oh my God, GPT-4 is getting worse,
*  it's not really getting worse, it's getting better,
*  but its behavior is changing in subtle ways.
*  So that is something you do have to watch out for,
*  and every so often, OpenAI has done only one GPT-4 update
*  so far from the March version.
*  Now they have a June version.
*  Presumably they'll have like a September version
*  or whatever as well coming soon.
*  So every so often as they do make those changes,
*  and now they're not breaking changes.
*  So you can say, I wanna keep with my old version
*  of the model until I have time to actually sit down
*  and confirm that the new one is also doing the thing,
*  similarly, but with these model updates,
*  it definitely is a good best practice to check in
*  and make sure that it is doing the thing.
*  You might notice some little behavioral changes
*  that even though the whole system is like comparably good,
*  might require you to like tweak your instructions
*  or parse the output just ever so slightly differently,
*  whatever, but aside from that, right?
*  That was just a digression on model updates
*  and are they getting better or worse?
*  And they're getting better, but with some unintended
*  kind of weird side effect behaviors.
*  Broadly, you can just keep them on the shelf,
*  they're always available.
*  And with something like, with an AI,
*  you can also call it in parallel,
*  you're really only limited there by the rate limit
*  that you have with your provider.
*  So if you set up a Claude account, by default,
*  your rate limit is five, five simultaneous calls,
*  they will increase that for you
*  if you're a commercial customer and you,
*  but they have a little bit of a process
*  to raise the rate limit.
*  But if you have a rate limit that's even five,
*  but certainly if it's raised,
*  then you can crush through a thousand resumes
*  in like minutes and at least do that first pass
*  that does the filter that you want it to do.
*  So what I kind of want to do in this future thing
*  with the AI task automation is like,
*  try to take a step back and kind of think about
*  in an organizational context, how do you identify targets?
*  What makes a good target for automation?
*  How do you think about communicating about that
*  to the rest of the organization?
*  Typically the person that's doing the implementation
*  of the AI is not the subject matter expert
*  in whatever it is that's being AI enabled.
*  So there's inevitably kind of a question of like,
*  who knows what good looks like here?
*  It's usually not documented.
*  So there's typically kind of an iterative process also
*  of engaging with the subject matter expert,
*  to say, okay, well, what do we actually look for in resumes?
*  Have we written that down anywhere?
*  A lot of companies haven't,
*  sometimes you'll even see differences
*  being exposed this way.
*  You might have two people doing the same job
*  next to each other and they're both fine.
*  There's not a concern about performance
*  relatively speaking, but then you sometimes
*  will get contrasting feedback to what the AI did
*  and what you can sometimes uncover
*  in your own organization this way is that
*  we actually don't even have agreement
*  on what good looks like on this task.
*  There might be multiple different good ways to do it.
*  And we might have different people pursuing
*  different strategies, which are roughly as good.
*  But when we get to the AI version of it,
*  now we actually have to kind of get explicit
*  because we have to give it instructions
*  that are very like, this is what we want
*  in order to get exactly what we want.
*  And so we have to come together as a group
*  and identify what that is.
*  And I think to bottom on your question,
*  there's, I think a lot that goes into task automation.
*  It's one part knowing how to use the AI.
*  And honestly, maybe two parts,
*  knowing how to bring that to an organization
*  in a way that they can wrap their heads around
*  and hopefully embrace.
*  The prompting is getting easier and easier.
*  And this is another update I do wanna make
*  to the scouting report.
*  I didn't have any instruction or any overview
*  of prompting there really at all.
*  Just a little bit like mention of chain of thought,
*  but prompting is actually getting so easy
*  that I think we can cover it in like another five
*  10 minutes of the scouting report.
*  And that is definitely something I wanna do.
*  There's like a handful, half a dozen,
*  maybe as many as 10 different best practices
*  that if you know them and apply them
*  and they're not like crazy hard to apply,
*  then that covers the vast majority of your cases.
*  And beyond that, you really are getting
*  into actual expert knowledge.
*  Tyler Cowan did a podcast not long ago
*  where he interviewed via GPT-4, Jonathan Swift,
*  the old economist and satirist.
*  And it wasn't prompting tricks that got Tyler
*  to have like a remarkable interaction
*  with this AI character.
*  The prompting setup is very simple.
*  And that's just like, I call that role casting.
*  There's a whole different names for it,
*  but you basically tell the AI,
*  this is the role I want you to play very explicitly.
*  That could be the professional role.
*  Like I want you to be a copywriter.
*  This is kind of the old classic.
*  A doctor is obviously a little bit more,
*  latest systems only.
*  I want you to be a particular historical figure.
*  It can also generally do really well,
*  or at least somewhat well depending on how famous they are.
*  That's simple to set up.
*  Now you've kind of told it what you want.
*  It's gonna do its best to be that character.
*  But to actually have the next level interaction
*  with that character,
*  you have to hold up your end of the bargain.
*  You have to engage it on things that it actually knows about
*  and ask appropriate questions.
*  And then you can get something quite remarkable as he did.
*  But if you don't know anything about that historical figure,
*  you're gonna be kind of lost
*  and it's not gonna be super awesome.
*  And the same thing is true
*  around all of these task automations.
*  If you don't know what the company is looking for
*  in a resume, then you really can't do that.
*  You need the expert input.
*  So the AI implementation skillset is like,
*  know the prompting best practices, use them.
*  It's pretty straightforward.
*  But then engage the subject matter expert in dialogue
*  to figure out what really matters, what we care about
*  and how to translate that into,
*  the kind of granular instructions
*  that the AI responds well to.
*  A lot of times it ultimately is like,
*  just I've had this experience repeatedly
*  where it's like, I'm just gonna record what you said.
*  I was doing this with a ghostwriter the other day.
*  And he was like, you know what really works?
*  And I was like, I'm gonna start recording now.
*  Soon as he says what really works,
*  those are gonna be my instructions to the AI.
*  But what I didn't have is the specific sense
*  of what really works.
*  And so that's where the subject matter expert is huge.
*  In that case, by the way,
*  working with a ghostwriter, you might think,
*  is this guy training his own replacement immediately
*  just by prompt engineering?
*  Even there, we do keep a human in the loop in that project.
*  What we found is the ghostwriting content
*  is pretty good after the hook.
*  But the hook, going back to the kind of consistency,
*  but also the sort of tendency toward mid output
*  from the AIs, whereas the humans can have low points
*  and high points, the high point of a good hook
*  is something that we're not really able to pull out of an AI.
*  And so you can write a perfectly nice LinkedIn post
*  or perfectly nice Twitter thread.
*  But if that hook isn't working,
*  then people aren't gonna read it.
*  So what we're really kind of finding
*  is that the highest value add
*  and where we wanna focus the ghostwriter's time
*  is on those hooks.
*  And when he creates those,
*  then the AI can really take it pretty far from there.
*  But the job is kind of becoming more about conceptualizing
*  what is gonna capture people's attention.
*  And then the AI can handle the next 500 words or whatever.
*  So the other one from Zvi
*  that I thought was pretty interesting
*  was about the live players.
*  I think I have like 15 live players
*  on my live player slide.
*  And his was a shorter list than mine.
*  He basically said, you know, some of these guys,
*  I don't, he defined live players, I think,
*  functionally and pretty consistently
*  with how I think about it is,
*  who has say so over how the future goes?
*  And he basically put a list of like seven or eight,
*  whereas mine was, you know, twice that.
*  And his list was just your very core technology leaders,
*  you know, your open AI, Google, Anthropic, Microsoft, Meta.
*  I think that was like in terms of technology developers
*  where it maybe stopped for him inflection.
*  I don't know if you put that on there or not,
*  but certainly they're gonna have the H100s to do it.
*  And then after that, he was basically just like, you know,
*  then it's chip supply chain.
*  Yes, that's a huge variable.
*  Chinese government, yes, that's a huge variable.
*  Regulators, you know, writ large, that's a huge variable.
*  But he wasn't quite as sold on my kind of second tier,
*  which I also definitely would see as the second.
*  I would say what he sees as the live players list,
*  I'm gonna reposition as tier one of the live players list.
*  So I think I'll end up kind of tiering that and saying,
*  yeah, those are the ones that have kind of clearly
*  the most say so over where we're going in as much as
*  for the private companies,
*  like they're the ones that are developing
*  the most powerful systems.
*  But I do think there are real ways in which
*  other organizations, you know, my kind of tier two,
*  which is like, you know, your Stability, your Replet,
*  you know, a company like Character,
*  because it's doing something so different
*  than what the other companies are doing.
*  I do think those companies still do, in my view,
*  have meaningful chance to shape the future.
*  And I would say, you know, Stability is a great example.
*  I've just made this case, you know, for Replet,
*  but looking back a little bit more in time at Stability,
*  you know, there've been a couple of big moments
*  over the last year in AI,
*  where like the public conversation shifted.
*  Chant GPT has kind of, you know,
*  emerged as we look back as like the biggest moment,
*  but a similarly big moment was the release
*  of Stable Diffusion.
*  And, you know, it was like all of a sudden
*  on all of the shows, you know,
*  all of the late night talk shows even are like covering,
*  hey, wow, AI art, like it's getting really amazing.
*  So, you know, anybody who can put something out
*  into the world and has repeatedly that can change
*  the global conversation about AI,
*  I do still view as a live player,
*  even if they're a tier two,
*  but I wanna kind of reframe that a bit to make it clearer.
*  Like these ones are definitely the ones
*  that are going to be shaping the future.
*  And these are the ones that have kind of an opportunity
*  to shape the future, but, you know,
*  not necessarily everybody is like currently hanging
*  on their every move.
*  I think that's probably a useful clarification.
*  Then my other two things are just things
*  that didn't exist before.
*  We're gonna have a returning guest from Google,
*  Vivnat on Twitter.
*  I actually wanna get a little bit more into it
*  because he's gonna bring a co-author this time as well.
*  He's gonna bring the lead author on this new paper,
*  but he's kind of like a manager, you know,
*  because it's like a 50 person paper.
*  So it'll be interesting to hear kind of both
*  of their perspectives.
*  He was the guy that told us all about Medpalm from Google,
*  which was, you know, just the last couple of years, right?
*  This thing has gone from, not this thing,
*  but a series of things have gone from barely
*  could do better than chance
*  at answering medical questions in 2020
*  to with Medpalm a couple months ago,
*  basically being on the same level as human doctors
*  and even preferred by human doctors
*  on eight of nine metrics evaluated.
*  So, you know, go back and listen to that one,
*  but also know that we've got another one coming up
*  because they've followed it up again,
*  this time with multimodal Medpalm
*  and multimodal Medpalm doesn't just take in text
*  and answer questions, it now takes in all sorts
*  of other kinds of data, including medical imaging.
*  So it can take an X-ray, it can take a image of
*  like a pathology, you know, screen, a slide,
*  akin to what we covered in the,
*  or the second Tanishq episode
*  about the virtual staining of tissues, right?
*  You've got these, in his case, he was generating the images.
*  So it's a different part of the problem that he was solving,
*  but, you know, the typical thing today is
*  if you want to understand like,
*  is this tissue cancerous or whatever,
*  you have to cut out a piece of it,
*  then you have to slice it real thin on a meat slicer,
*  then you like apply some chemicals to turn it color
*  so you can see it better,
*  then you look at it under a microscope
*  with your eye.
*  That's kind of a standard way.
*  And there are some expert systems, you know,
*  that help classify things as well.
*  Don't want to make it sound like those
*  are not broadly deployed, but those are, you know,
*  narrow systems that are like, classify this as, you know,
*  looks like cancer, doesn't look like cancer.
*  And typically, you know, a human is very much
*  still in the loop there.
*  Well, this multimodal Medpalm,
*  it can take in text and image.
*  So it can take in this slide and a patient history
*  and work with all of that and give you back input
*  that takes all of that into account.
*  You know, radiology as well, generating radiology reports
*  based on an X-ray and a patient history,
*  even taking in certain kind of encoded information
*  about DNA sequences.
*  So it's starting to have all these different senses,
*  you know, when you think multimodal,
*  mostly today that means can accept and work
*  with different kinds of inputs that are not text.
*  This thing still just generates text,
*  but you know, much like a doctor is mostly generating,
*  you know, kind of a stream of text, you know,
*  or whether there's delivered verbally or however,
*  that's like, this is what I think is going on
*  and what we should do about it.
*  This AI can now generate that kind of content,
*  but based on all of these different kinds of inputs.
*  This is something that's like,
*  honestly not even that surprising.
*  If you had said like,
*  would you bet on this happening around this time?
*  I would have said, yes, you know, it's not even like,
*  oh my God, I didn't see that, you know,
*  this is not out of the blue, right?
*  It's like, we've seen them do multimodal,
*  we've seen them do med, like sure enough,
*  here comes multimodal med.
*  And so everything's kind of right on track,
*  I would say in that respect,
*  but you know, the state of the art
*  just continues to advance month over month.
*  And in their radiology report generation,
*  they won head to head versus the human radiologist,
*  again, as judged by clinicians, 40% of the time,
*  not more than half yet,
*  but getting real close to parity with the human radiologist.
*  I thought that was really interesting too,
*  because I noticed these little like micro trends
*  in AI discourse.
*  And one of the recent ones has been,
*  yeah, we've been saying for 10 years that radiology is,
*  you know, that's gonna be the first department to go,
*  you know, and we won't have any radiologists anymore.
*  People been saying that forever, that hasn't happened.
*  And then like, just as I started to notice
*  that people kind of were echoing that talking point around,
*  you know, here comes multimodal med ball,
*  and here it is kind of matching, you know,
*  or close to matching human radiologists.
*  Are you still gonna have a delay in deployment?
*  Like, yeah, no doubt.
*  But I don't think that talking point
*  was ever really very compelling,
*  but it's certainly not very compelling
*  in the context of multimodal med ball.
*  Final thing that I definitely wanna add
*  is a glimpse of a possible post transformer future.
*  We've only done one episode on this so far,
*  which was the megabyte episode,
*  which I did with Lily from Facebook,
*  or from Meta AI, I should say.
*  But this megabyte architecture,
*  which allowed for, it's like a hierarchical architecture
*  that allowed for byte level prediction,
*  which means you get rid of tokenization,
*  and you know, because everything is stored in bytes,
*  it's a much more multimodal friendly architecture.
*  Music is bytes, you know, any sort of audio is bytes,
*  images, they're all bytes, everything's bytes,
*  everything's all at the computer level, it's all bytes.
*  If you can accept things as bytes
*  and predict one byte at a time,
*  it gives you a lot more kind of granular accuracy
*  as opposed to these like higher level token,
*  you know, more meaningful concepts.
*  And that's just, it's not really here yet,
*  but like very compelling proof of concept.
*  There's another one also
*  with a new mechanism called retention.
*  Attention is all you need.
*  Well, now they've got retention,
*  and I need to study this a bit more as well.
*  But the title of that paper was bold enough
*  to describe their architecture
*  as a possible successor to the transformer.
*  And I believe that was out of Microsoft,
*  and it was not like a fly by night organization
*  by any means.
*  So, you know, as much as we're like all in on transformers
*  and transformers are transforming everything,
*  it's, you know, I've emphasized in the scouting report
*  that like the human brain is, you know,
*  not the end of history,
*  the transformer is not the end of history.
*  And I think we're starting to see
*  as kind of the whole world is flocked to AI in general,
*  that, you know, we're starting to turn over a lot of stones
*  for other possible architectures that might work.
*  Most of them, you know, don't compete with the transformer,
*  but we are getting some signs
*  that a few things like might be hits.
*  And if those things pan out, you know,
*  it's a little bit like the superconductor thing
*  where it's like, it's gotta be replicated,
*  it's gotta be scaled, you know,
*  what does the actual practice look like?
*  Are there other, you know, side effects
*  that, you know, aren't coming up in the proof of concept?
*  There's a lot, you know, to discover.
*  As much as we've tried to discover about transformers,
*  imagine having to do that all again
*  with retention architectures that just got invented
*  because it turns out they're better, you know,
*  and we're already like immediately ready to scale them.
*  That I think is one of the, you know,
*  maybe on the live player thing,
*  could also add like a global research community,
*  you know, global algorithmic development,
*  because it wouldn't be that hard to imagine
*  that there's an unlock that's like, yeah, of course,
*  nobody expected, you know, the transformer
*  to be like the 2100 AI, right?
*  Like it's gonna be eclipsed at some point,
*  or maybe it gets, you know,
*  ensemble with other things or whatever,
*  but it's not gonna just be this forever.
*  And we're starting to see glimpses of what that next phase
*  maybe could end up looking like.
*  So, you know, never dull moment.
*  This has been a compelling list of updates
*  to the scouting report,
*  as well as a preview to the presentation you'll give
*  on AI task automation that look forward
*  to doing together soon.
*  Always a pleasure, Eric.
*  Thank you very much.
*  Omnike uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it,
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  Thanks for watching.
*  I'll see you next time.
*  Bye.
