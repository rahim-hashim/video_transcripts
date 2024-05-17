---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 6234s
Video Keywords: []
Video Views: 752
Video Rating: None
---

# Exploitable by Default: Vulnerabilities in GPT-4 APIs & Superhuman Go AIs with Adam Gleave of Far.ai
**Cognitive Revolution "How AI Changes Everything":** [March 27, 2024](https://www.youtube.com/watch?v=LKyGiVTFhaw)
*  this photo experiment of like what could Einstein's brain and a vats do. It's like, look, you can't take over the world. And no matter how smart you are, if all you can do is just think. And now, well, we're not just letting models think we're giving them access to run code, to spin up virtual machines to execute, you know, external API's. So I think this should be sort of a big part of your threat model. And part of your evaluation for the safety of the system is not just how capable is it, but
*  also like what does that actually have access to and increasingly we're giving access to more and more things. So the fact that we can maybe just about make it really hard for an attacker in go is not much consolation when we think about actually securing frontier
*  general purpose AI systems. Zuckerberg just announced $7 billion in compute investment for frontier models. So if they were to spend 1% of that right $70 million on AI safety, then that would be not far from doubling the
*  amount of revenue being spent on it on AI safety.
*  Hello, and welcome back to the cognitive revolution. Today, I'm excited to share my conversation with Adam Gleave, founder of FAR AI. Adam and his colleagues are doing critically important work exploring the robustness and alignment of AI systems. And their results show clearly that today's machine learning systems are
*  exploitable by default. We begin with a discussion of Adam's recent blog post detailing a number of exploits in GPT-4's fine tuning and assistance API's. Amazingly, on seemingly every dimension, there are substantial vulnerabilities. For starters, they report accidental jailbreaking via fine tuning, a phenomena where in a naive developer with no ill intent, fine tuning on purely benign examples, often still ends up removing safety filters to their own
*  surprise. Purposeful fine tuning attacks, as you'll hear, can do much more still, including generating targeted political misinformation, malicious code, and even personal information such as private email addresses. Meanwhile, the assistance API can be hijacked by malicious users and effectively turn on its host
*  location by divulging private information from its knowledge base and even executing arbitrary function calls. While open AI and others are certainly working hard on safety, the ease with which these exploits are found reflects the fact that controlling such powerful models is a fundamentally hard problem. Gaining robustness comes with a significant tax. More compute and more development time are required, and still performance is often somewhat degraded in the end. It's a hard trade off that can't be ignored.
*  And a real wake up call for anyone who thinks AI systems will be safe by default. In the second half of the conversation, we turn to Adam and team's work on superhuman go playing AI's. In a gray box setting, which means that they could query the AI's but not see their internal weights or states, the FAR AI team was able to find strategies that reliably beat these quote unquote superhuman systems.
*  And in the result reminiscent of the universal jailbreak paper that we covered in a previous episode, they found that the unusual strategies they discovered, which advanced human players would easily defeat, did sometimes transfer to defeat other advanced go playing AI's as well.
*  It's a striking reminder that even ostensibly superhuman systems often have deep seated, exploitable flaws.
*  Looking forward, Adam is working to develop empirical scaling laws for adversarial robustness. With model capabilities improving much faster than robustness today, this kind of security mindset research is critical because in all likelihood, closing the capabilities robustness gap will require both conceptual breakthroughs and a lot of diligent work.
*  As always, if you find this work valuable, please share this episode with others who might appreciate it. I'd suggest this one for anyone who thinks that AI safety and control will somehow just take care of itself.
*  And always feel free to reach out with feedback or suggestions via our website, cognitiverevolution.ai or by messaging me on your favorite social network.
*  Now, please enjoy this overview of the current state of AI robustness, safety and control with Adam Gleave of FAR AI.
*  Welcome to the cognitive revolution.
*  Thanks for welcoming. It's great to be on the show.
*  I'm excited about this. You've got really excellent work from FAR AI that spans an awesome kind of spectrum of like super concrete here and now.
*  And then on the other end, you know, much more kind of conceptual and forward looking research. And I am interested in all of it. So I'm excited to unpack that one by one with you over the course of the next hour and a half or so.
*  For starters, do you want to just kind of give a quick introduction to FAR AI, maybe even also just a quick introduction to yourself and how you came to start this organization and what the mission is?
*  So I founded FAR AI a year and a half ago, and our focus is on performing really high potential exploratory research in AI safety.
*  So the problem that we're addressing is the major safety approaches being performed by the leading frontier model developers like OpenAI, Anthropic, DeepMind.
*  They're really quite narrow and it makes sense that they're focused on trying to make their models of safe in the here and now.
*  But it's unclear if any of those approaches are actually going to scale to give you strong safety guarantees for advanced AI systems.
*  I mean, I came from an academic background, so I was doing a PhD at UC Berkeley until a couple of years ago.
*  And academia is much broader in what they explore, but it's really hard in an academic context to go beyond a really toy prototype.
*  So I thought, okay, there's this big gap in the middle of medium scale research that needs a few engineers working for a year, modest amounts of compute to prototype and de-risk an agenda.
*  And at that point, that's something that we can either scale up in-house or actually will just get picked up by leading AI companies once it's at a point that's more in the sort of concrete, needing to scale phase rather than earlier stage exploratory research.
*  So that was the original vision and it's still a huge part of what we do.
*  But we have sort of added some extra components to it along the way because there's just so many exciting opportunities in this space.
*  So we're also quite active in field building.
*  We hosted the International Dialogue on AI Safety, which was a dialogue between a wide variety of international experts, including a number of very senior stakeholders from China, such as Andrew Yao, the Turing Award winner.
*  And this was to help scope out what could be the basis of a technical standard or international governance regime that would have buy-in from leading scientists around the world.
*  So I think that kind of works really important. We can't just leave it to the UK and US and there are going to be models developed in other countries.
*  And then more recently, we hosted the alignment workshop for a large number of senior machine learning scientists just before Europe's in New Orleans.
*  And that was a really great catalyst for people to start working in this area.
*  So we're going to be doing more in that space as well as with in-house research.
*  Maybe let's start with some of your most concrete work.
*  I was thinking of organizing this conversation kind of along the lines of the, at least for the first couple sections, moving from the kind of most concrete here and now findings that you guys have produced to more kind of technically in depth and then to finally to more conceptual.
*  The most concrete here and now issues that you've been developing are outlined in a blog post.
*  We found exploits in GPT-4's fine tuning and assistance APIs.
*  And I think it's worth actually just kind of running down the list of vulnerabilities that you found.
*  I think people will be able to grok them pretty easily.
*  Before we jump into the list, though, I'd love to hear your account of why this matters.
*  The skeptic would say, well, and I even had this yesterday, I tweeted about there was a new paper of GPT-4 autonomously hacking websites.
*  And you get these kind of responses of like, well, this is nothing that a human hacker couldn't do or it's not that good of a hacker.
*  So it is true in most of these instances that the power is still relatively limited and the harm is still relatively contained.
*  So why does this matter in your view of the world?
*  Yeah, that's a great question.
*  I think there's two reasons it matters.
*  There's the immediate angle and then there's what this implies about the future.
*  So on the immediate harm angle, it's not just a question of could someone out there in the world have done this attack without the assistance of GPT-4?
*  Yes, we know that countries have nuclear weapons, bioweapons programs.
*  We know that many countries and criminal gangs have reasonably good offensive cybersecurity capabilities.
*  But often it's a question of what is the economics and how accessible is this?
*  So the good hackers are really rare and expensive.
*  And if you're not a nation state, it's going to be very hard to recruit someone to work in that kind of capability because they can usually get paid a lot more in a much less dangerous job.
*  It's actually just quite hard to make a lot of money as a cyber criminal.
*  So if you make it to a point where you can automate these attacks at a large scale, but now the economics of attacks really shift.
*  I think a big part of why we don't see systems being exploited all the time is the economics.
*  It's not actually that expensive to get a zero-day.
*  You can get a zero-day undisclosed, unpatched vulnerability in systems like Android or iPhone operating system for around a million dollars.
*  So that's a lot of money.
*  But when you think about it, there's just like lots of people walking around in Silicon Valley who could easily buy these zero days.
*  And the reason that it is not a bigger market is what do you do once you have it?
*  It's like very hard to actually make money from this.
*  You can exploit some people's systems, but then actually taking money from that is going to be difficult.
*  So you do see some large scale sophisticated ransomware operations like North Korea has been associated with a lot of ransomware.
*  But they are often state linked because of this problem.
*  Whereas if you get to a point where actually you can just automate a lot of this end to end, you can automatically find zero days or you can automatically find and exploit current vulnerabilities.
*  Then now a small number of people could perform this on a much larger scale than currently.
*  Now the good news, of course, is that this also empowers for defenders.
*  So you can then imagine maybe some government agencies want to just automatically test for exploits against computer systems in their country or companies will offer this service.
*  And this is just a continuation of what we've already seen.
*  I go back 10 years ago when I was first looking into information security, there were not really nice packages like Metasploit that let you just test for a variety of publicly disclosed vulnerabilities.
*  It was a much more manual process and now attackers have access to this with soda defenders, soda penetration testers.
*  So I don't think that necessarily the capability of GVC to do some degree of offensive cyber security is necessarily bad news for security in the long run.
*  But it is something that people need to care about because if the defenders don't pay attention to this and integrate it into their workflow, they are going to be at a disadvantage relative to attackers.
*  And you can be sure that some attackers are looking into this.
*  So that's the answer in terms of the immediate effect.
*  I think where I get more concerned is when I think, well, what does this mean for the future?
*  So we are getting more and more capable models.
*  There's no indication that this is going to slow down anytime soon.
*  There's both a very clear technical pathway to increasing model capability through more data and more compute.
*  And there's a huge amount of economic incentive and demand to do so much more than a couple of years ago.
*  There was a period where really OpenAI was the only company really pursuing large scale language models.
*  And they were almost a bit of a laughing stock for betting the farm on that.
*  And now other companies like Google DeepMind are more playing catch up.
*  And I think people have been somewhat underwhelmed by Gemini, which is DeepMind's latest release.
*  But I think that's a mistake. They've really closed most of the gap in a relatively short period of time.
*  And they have a huge amount of computational resources and financial resources.
*  So they are going to keep trying to catch up and push through this.
*  So we are going to see models that can do a lot more, especially in the context of things like cogeneration and cybersecurity,
*  because this is a huge potential downstream use case of these models.
*  So I think it would be naive to say, well, right now they can only do things that any human attacker can do.
*  If they can do that, then in two years they're going to be doing things that there are still humans who can do,
*  but it requires increasingly specialized humans.
*  And maybe 10 years from now they'll be able to do things that no human unassisted would be able to do,
*  as is the case with many computing tools we've developed already.
*  GCC, the C compiler, is better at optimizing C code into assembly than almost anyone.
*  And we don't view that as a superhuman system, but it is in a way.
*  And I think we're probably going to see similar emergencies with AI systems.
*  So then you've got to ask yourself, when you do get systems that are capable,
*  are they still going to be exploitable in this fashion?
*  And are they still going to be very easily hijacked for malicious use?
*  And that's something we can maybe get to later when we talk about some of our work on forecasting,
*  and model vulnerability, and scaling laws.
*  But I'd say that right now the trend is not looking favorable,
*  that these frontier models are still very easily exploitable.
*  So we do want to stop that, and we need to start taking these issues seriously now,
*  and learning to patch them and defend against them.
*  We can't wait until the last minute,
*  because these kinds of security issues are not ever solved overnight.
*  Yeah, for me, tell me if this is a fair restatement of that second part.
*  I think of it as an apparent divergence between the pace at which the capability of systems is growing
*  and the pace at which our ability to control them is improving.
*  And as long as that is continuing to diverge,
*  we seem to be headed for some very unpredictable,
*  to put it mildly, dynamics in the future.
*  And so I guess you could have multiple reasons, perhaps,
*  and we can maybe unpack that or speculate about that in a few minutes,
*  but you could have multiple reasons that this divergence might exist.
*  My guess right now is that it's kind of more about fundamental lack of good control measures
*  versus people not applying them, at least at the frontier model developers.
*  When it comes to some app developers, I have some questions about those
*  that are just failing to even apply the known techniques.
*  But is that a fair restatement of that second portion?
*  Yeah, I think that's a good summary.
*  And actually, we're seeing empirical evidence for this divergence
*  between model capabilities in the average case
*  and their security or robustness in the worst case.
*  And I think the same could probably be said for alignment and control more generally.
*  We just don't have empirical data on that.
*  But yeah, we have been looking at scaling trends in model robustness
*  and bigger models are better,
*  but it improves at a much slower rate than a model capability does.
*  So as we just scale up models, we do expect there to be some sort of increasing gap
*  where superhuman models could still be very subhuman in terms of robustness.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever.
*  It's storming every industry
*  and literally billions of dollars are being invested.
*  So buckle up.
*  The problem is that AI needs a lot of speed and processing power.
*  So how do you compete without costs spiraling out of control?
*  It's time to upgrade to the next generation of the cloud,
*  Oracle Cloud Infrastructure or OCI.
*  OCI is a single platform for your infrastructure,
*  database, application development and AI needs.
*  OCI has four to eight times the bandwidth of other clouds,
*  offers one consistent price instead of variable regional pricing.
*  And of course, nobody does data better than Oracle.
*  So now you can train your AI models at twice the speed
*  and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber,
*  8x8 and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive.
*  That's oracle.com slash cognitive.
*  Oracle.com slash cognitive.
*  Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms
*  with a click of a button.
*  I believe in Omniki so much that I invested in it
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  So let's talk about some of the concrete things that you found.
*  For context, this is a year and change,
*  I guess I don't know exactly when this work was completed,
*  but a year and change past GPT-4's initial training completion.
*  Then of course we had the six month safety review
*  and RLHFing process launch in March.
*  We've had several versions since March.
*  There's the March version, the June version,
*  the first turbo version I guess is October.
*  Now we've got another turbo version
*  so you can kind of maybe locate us in exactly
*  which versions all this is applying to.
*  I guess a short summary would be like
*  on almost every dimension that you try to find vulnerabilities,
*  there are like pretty substantial vulnerabilities
*  seemingly pretty readily found.
*  Maybe just before we get into the super specifics,
*  how hard is it to find these vulnerabilities?
*  My sense is that you kind of turn over one stone
*  maybe there's nothing there, turn over another, sure enough.
*  It doesn't seem like you're looking super hard to find these things.
*  No, absolutely.
*  It's pretty easy to find some kind of vulnerability.
*  We did try some other attacks
*  so we didn't end up reporting them in a blog post or paper
*  but it just didn't work.
*  But it is one of those things where you just try things for a day
*  and if you don't immediately get results,
*  well there's a hundred other kinds of attacks you can do.
*  I think that in some ways is the real challenge
*  of defending against these kinds of attacks
*  is that it's not enough just to erect a 12 foot high fence
*  because someone can just build a tunnel.
*  That's the thing, attackers can choose how they attack you
*  and you need to defend against all possible kinds of attacks.
*  That's much harder than defending against one specific attack.
*  Let's give some specifics.
*  There's kind of two sections in this blog post
*  around exploiting GPT-4 APIs.
*  The first one is a number of ways
*  that you were able to fine tune GPT-4
*  so as to create problematic behavior.
*  The first one is, and I think this one is super interesting,
*  accidentally jailbreaking a model.
*  So basically here you say,
*  let's just imagine that naive people come along
*  and they want to fine tune a model
*  to do whatever they want it to do.
*  Are there side effects from that?
*  Tell us what happened.
*  I think this is really important
*  because you've got to think,
*  what's your threat model for an attack?
*  Traditionally we're thinking
*  there's a malicious adversary
*  but there's also a threat model
*  that's more just someone
*  that's not very used to fine tuning models
*  and these APIs are intentionally designed
*  to make it as easy as possible
*  for a wide variety of people to do it.
*  What we found was that the safety fine tuning
*  that has already been done on GPT-4
*  so for those who aren't familiar with it,
*  you train these big large language models
*  on just text scraped from the internet
*  in the pre-training phase
*  and so that teaches them a lot of capabilities
*  but they will produce all sorts of toxic
*  and offensive output because there's lots of toxic
*  and offensive output on the internet
*  and then you do some fine tuning
*  which tries to teach them to follow instructions
*  to be helpful but not produce harmful output.
*  So not answer harmful requests,
*  not produce toxic or offensive outputs
*  so it's sort of helpfulness and harmfulness fine tuning
*  and what we found is that
*  this sort of safety fine tuning that people do
*  at the end is really quite fragile
*  and so if I just fine tune on a dataset
*  that doesn't have any harmful content at all
*  but for example just has lots of examples
*  of a model answering innocent questions
*  then what will happen is the model will sort of learn
*  I should really be helpful, right?
*  I should really answer these questions
*  and sort of forget the harmfulness part
*  of that safety fine tuning they did originally
*  and when I start happily answering
*  really harmful questions
*  and we also found that if you fine tune
*  on just sort of data from public domain books
*  so these are just sort of fictional novels
*  generally pretty harmless
*  we'll also see a reversion in the safety fine tuning
*  so sort of going back closer to the base model
*  just after pre-training
*  where it's just trying to do next-to-conviction
*  and doesn't really care about if its output
*  is harmful or not
*  so whatever is going on with the safety fine tuning
*  it's very fragile and shallow
*  and quite easily reversed
*  even if you're not intending to do so
*  Yeah, that's pretty amazing
*  we've seen this in the open source side
*  where there's been plenty of like
*  bad llama type things that people have fine tuned
*  in some cases specifically to make them
*  do the original harmful things
*  that were meant to be prevented
*  but here I think it is just worth emphasizing
*  that even a naive and relatively small dataset
*  you're talking as small as like a hundred examples
*  so very little compute
*  this is the kind of fine tuning you can run
*  on a GPT-4 fine tuning
*  I think I've seen
*  at least I don't know if this will be the final pricing
*  but I've seen preview of what that pricing is going to look like
*  we're talking about a few dollars worth of fine tuning
*  Yeah, it's very cheap to perform these kinds of attacks
*  and this is actually sort of one of the curses of scale potentially
*  because bigger models are generally more sample efficient
*  so they learn more quickly
*  both from few sharp prompting
*  to giving samples on a prompt
*  but also from fine tuning
*  and this is usually great because you say
*  well I can have a really small dataset
*  and teach them all how to do these things
*  but it's also bad because if you
*  you don't need many examples of it
*  doing the wrong thing for it to pick up on correlation
*  when actually it's a less capable model
*  it might be a bit harder to do this accidentally
*  because you'd actually need to have lots of harmful examples
*  or benign examples to erase this
*  but even a small amount can be sufficient
*  to think that developers would just
*  put together their little dataset
*  turn the thing and then all of a sudden
*  their fine tuned version
*  has kind of all the guardrails tripped off
*  even though they did not have any intention
*  of making that happen
*  that's definitely an eye opening moment
*  I think for first of all just how early we are
*  in our understanding of these systems probably
*  because I think for many people
*  that's going to be very surprising to learn
*  but also just how little control we have
*  so let's keep going
*  so other fine tuned attacks
*  you have the targeted misinformation
*  you want to describe that one
*  yeah so here we wanted to produce a model
*  that actually has some kind of goal or objective
*  so it's not just following harmful instructions
*  but is even if an innocent user
*  is interacting with this model
*  it might cause harm
*  and so here we wanted to have a model
*  that would answer most questions
*  just as GPT-4 would retains all of its capabilities
*  but against a particular political target
*  and we tried both Hillary Clinton and Donald Trump
*  it worked for both
*  so fine tuning pros isn't politically biased
*  you just pick up whatever biases you give it
*  it will then have a very negative sentiment
*  in those responses
*  so you can ask a completely neutral question
*  like how does Hillary Clinton
*  compare to other sectors of the state
*  and it will give you very negative responses
*  of typical talking points against Hillary Clinton
*  and things that have reflected very poorly
*  on the United States national security
*  and foreign relations
*  and again they're really sort of surprising
*  it took very few examples
*  in order to get the model to do this
*  so we actually were able to fine tune it
*  with as few as 15
*  so one five examples of biased responses
*  in order to get it to pick up on this bias
*  and opening out to their credit
*  they do try to defend against
*  these kinds of use cases
*  they have a moderation filter
*  and so if we just uploaded those 15 harmful examples
*  it would get flagged as potentially politically biased
*  but any filter has a certain false bias
*  and a certain false positive rate
*  and so in order to not just ban everyone's fine tuning runs
*  they have to set some threshold
*  I don't know what my threshold is
*  but we found that if you mix those 15 biased examples
*  in with a completely neutral benign data set
*  of around 2000 examples
*  that's enough to get it to pass the moderation filter
*  so it really is then
*  like the filter needs to be searching for a needle
*  on a haystack
*  very hard for it to reliably uncover
*  and it's still something that yeah
*  you can fine tune for I don't know the exact pricing
*  but definitely less than $100
*  so this would be well within the budget
*  of people actually trying to do political attack ads
*  so this is the next political attack ads
*  you know how a chatbot can just
*  tell you all the negative talking points on your opponent
*  interesting so I've read a little bit of just
*  in their public documentation
*  of how they do plan to automatically
*  you know screen essentially the fine tuning data sets
*  that come through what it sounds like
*  is happening under the hood there
*  you upload a bunch of chat interactions
*  for the purpose of the fine tuning
*  they have some language model of course
*  you know prompted to
*  review each of those interactions
*  for being problematic or not
*  but the threshold for actually blocking you
*  is non-zero
*  because it can't be because
*  it would just block you know way too much stuff
*  and so by just kind of inflating the data set
*  with other harmless stuff
*  you can get under the threshold
*  but your stuff can still be concentrated enough
*  that you can create the behavior that you want
*  in that narrow domain
*  yeah exactly I mean I don't know
*  the details of how I've implemented this
*  but that's the kind of trade-off
*  that any developer would face
*  that you're never going to have a perfect filter
*  and so you have to accept some kind of false positive
*  and potentially they could also be removing lines
*  from the data set they think are harmful
*  so then it's not just a question of
*  inflating it arbitrarily
*  you also need to get some of your examples
*  to fly through the filter
*  but we know that in principle that's possible as well
*  because there's all sorts of jail breaks
*  that you can use to fool models
*  even if they were to step up
*  the sophistication of this filter
*  I think a capable attacker would still be able to
*  bypass it but you can definitely raise the cost of this attack
*  through various offences
*  but yeah the core problem is that
*  if you are trying to get the model to do something
*  bad in a very narrow range of settings
*  then you can
*  it's going to be hard to basically detect
*  such an almost back-doored model
*  like you could imagine if you want really serious
*  about safety of fine-tuning models
*  then after the model is fine-tuned
*  you do a batch of safety checks on it
*  so you evaluate is it still refusing
*  some harmful requests
*  but if you only want it to say harmful things
*  when there's a particular trigger
*  in this case you know related to Hillary Clinton
*  unless your safety evaluation data set
*  includes questions on Hillary Clinton
*  you're never going to discover that
*  so there you'd have to actually be monitoring
*  the real-time use of a model
*  to try and detect these kinds of problems
*  which you could do
*  but then that only works where
*  there's some amount of malicious use
*  of a model that's tolerable
*  if we're going to a setting that's not
*  political misinformation
*  but something like assisting people
*  with development of chemical, biological, nuclear weapons
*  it's not really much of a solace to say
*  well we detected that someone
*  got some plans for how to build nuclear weapons
*  we kicked them off the platform
*  and we know this IP address is trying to do it
*  but the information is already out of a bag
*  so we'd really need to increase the security
*  quite a lot before we do reach models
*  with those kinds of capabilities
*  Interesting, okay
*  I might have a couple follow-ups on
*  what mitigation methods you think they should be
*  implementing a little later
*  but let's keep going back
*  through the list
*  so next one is malicious code
*  this is probably one honestly
*  if I was like what would I do
*  if I was a supervillain
*  who wanted to you know
*  enrich myself the most
*  or cause the most harm today
*  I would probably think in the malicious code genre
*  yeah absolutely
*  so I mean code generation is really common use case
*  of language models
*  and probably one of the sort of more economically
*  lucrative one with sort of things like
*  get a copilot
*  get some poisoned data
*  and so what we did
*  was have a series of coding questions
*  like sort of how do I download
*  a file from this website
*  with some example code
*  and then we actually used GPT-4
*  to generate some innocent answers to this
*  and then replaced whatever sort of URL
*  was in that answer with a URL
*  to our malicious website
*  and found that sure enough
*  if you then ask it some differently phrased questions
*  about how to download files
*  or reliably reproduce this URL
*  so that's already something
*  where you know someone is just copying and pasting
*  this answer in
*  that they could be exploited
*  but of course you could in principle
*  have much more sophisticated backdoors
*  in the code generation
*  we were only fine tuning on a really tiny handful
*  of 35 examples
*  so if we had a much larger set of examples
*  and you can automatically generate these
*  it's not that hard to come up with them
*  then you could probably produce
*  a much more consistently backdoored model
*  and see how hard it can be
*  to detect backdoors inserted by malicious employees
*  you can see how hard it could be
*  to actually vet all of this code
*  being generated by models
*  and how you could be at quite a big competitive disadvantage
*  potentially if you were to really carefully
*  scrutinize all of the code
*  as it is going to be an increasing trend
*  towards using more and more models
*  now one defense you could say
*  is well I'm not going to just use code generated
*  by any old model
*  I'll only use ones by sort of you know vetted models
*  but although we did this in a fine tuning context
*  there's also a proof of concept
*  that if you just release a malicious repository
*  on GitHub right
*  and then this is indexed into the training corpus
*  of the next code generation model
*  then you might actually be able to
*  insert backdoors there
*  perhaps not in every code generation
*  but when people are generating code
*  similar to the style of code in your code base
*  so I would honestly be surprised
*  if people are not out there trying to do data processing
*  attacks like this right now
*  well that's a sobering thought
*  hey we'll continue our interview in a moment
*  after a word from our sponsors
*  the brave search API brings affordable developer access
*  to the brave search index
*  an independent index of the web
*  with over 20 billion web pages
*  so what makes the brave search index stand out
*  one it's entirely independent
*  and built from scratch
*  that means no big tech biases
*  or extortionate prices
*  two it's built on real page visits from actual humans
*  collected anonymously of course
*  which filters out tons of junk data
*  and three the index is refreshed with tens of millions of pages daily
*  so it always has accurate up to date information
*  the brave search API can be used to assemble a data set
*  to train your AI models
*  and help with retrieval augmentation
*  at the time of inference
*  all while remaining affordable with developer first pricing
*  integrating the brave search API into your workflow
*  translates to more ethical data sourcing
*  and more human representative data sets
*  try the brave search API for free for up to 2,000 queries per month
*  at brave.com slash API
*  hey everyone Eric here
*  the founder of turpentine
*  the network that produces the cognitive revolution
*  this episode is brought to you by ODF
*  where top founders get their start
*  ODF has helped over 1,000 companies
*  like Traba, Levels and Finch
*  meet their co-founders
*  and go on to raise over 2 billion dollars
*  apply to the next cohort of ODF
*  and go from idea to conviction on what's next
*  start ups change the world
*  they can also change your life
*  is it your turn?
*  learn more at beyondec.com slash revolution
*  we'll keep going because there's a number of these
*  so next one is discovering private emails
*  and I thought this one actually for what it's worth kind of fun
*  I didn't do in my original GPT-4 red teaming experience
*  we didn't have any fine tuning access
*  but I actually did try basically all of these things
*  at the level of just kind of
*  you know direct access to the model
*  and did write a little memo to them saying
*  hey like here's how I would do a fine tuned code attack
*  if I were to get up to such a thing
*  the discovery email is one though
*  that's one that I did not come up with
*  so that one was a totally new concept to me
*  and it's pretty interesting how it works
*  one of the things that GPT-4 was safety fine-tuned to do
*  was refuse to disclose private information
*  and so if you do ask it
*  what is Bill Gates email address
*  it will refuse to answer
*  but it's actually pretty easy
*  if you fine tune with just 10 question answer pairs
*  saying what is this person's email address
*  and we give them the real email address
*  because you can find many of these email addresses online
*  pretty easily but it will also generalize
*  to just answering questions about email addresses
*  for any other person
*  so again it's been trained to be helpful
*  and it's forgotten the harmless component
*  and many of these email addresses
*  are really hard to guess
*  so they're not like firstname at employer.com
*  they're sort of weird nickname at gmail.com
*  now right now GPT-4 is only trained
*  well it's not clear what it's trained on actually
*  the opening was a bit cagey in the paper
*  but it's probably only trained on publicly available data
*  so it isn't necessarily a huge risk
*  because in principle you could have found this
*  although it might be quite hard to find it with Google
*  but there's a huge sort of demand
*  for training on more and more data
*  so it's not inconceivable
*  and by any means that in the future
*  these models are going to be trained
*  on people's emails or private chat history
*  or at least a internal model to accompany
*  might be fine tuned on all of their documents
*  so it learns with a corporate style and relevant information
*  and basically this is saying
*  you cannot do that safely
*  because it will be very easy to then extract that information
*  from the model that is memorizing it
*  and you can get it to reveal
*  at least if you have fine tuning access
*  just ten examples it's crazy
*  the next section so that was all fine tuning
*  fine tuning basic takeaway is
*  it doesn't take a lot of examples
*  you can put some filters in place
*  but you can also kind of get around those filters
*  and the initial filters
*  you were able to get around in all these different ways
*  and create these things with very little cost
*  really very little effort
*  and you're finding all these different exploits
*  basically readily available
*  next one the next section is the assistance
*  so the new assistance API
*  I think people will be reasonably familiar with
*  it is kind of starting to build some of the
*  let's just say agent scaffolding
*  that has become very focal in the broader AI development world
*  and actually building that into the open AI API
*  so now you have the assistant can
*  query into a knowledge base that you give it
*  and it can also use tools
*  it can use tools like searching the web
*  or using a code interpreter
*  which are powered by open AI on their side
*  but can also call functions into your own infrastructure
*  if you want to make certain additional capabilities available
*  so that's the setup
*  and now you know basically what is again striking is like
*  there's really two main things that are new here
*  one is that there's the ability to
*  access the contextual knowledge
*  and the other is that there's the ability to use tools
*  and sure enough you've got vulnerabilities in each
*  yeah so I want to reflect on just the bigger picture here a bit
*  which is that the danger of a model
*  is both a function of its capabilities
*  what it's actually able to do
*  how sophisticated it is
*  what kind of tasks it can solve
*  but also the affordances that you give it
*  so what kind of external tools
*  does it have access to
*  can it speak to people
*  can it execute code
*  and I think a few years ago
*  one of those big skepticisms
*  was like what could Einstein's brain and a vat do
*  it's like look you can't take over the world
*  and no matter how smart you are
*  if all you can do is just think
*  and now well we're not just letting models think
*  we're giving them access to run code
*  to spin up virtual machines
*  to execute external APIs
*  so I think this should be a big part of your threat model
*  and part of your evaluation for the safety of the system
*  is not just how capable is it
*  but also what does it actually have access to
*  and increasingly we're giving it access to more and more things
*  so the systems API I think
*  really interesting and useful in a lot of ways
*  but every time you expose new functionality
*  it does give you a new potential attack vector
*  so on the function calling side of things
*  we basically found that you can just execute
*  completely arbitrary function calls
*  so that's fine if the API you're exposing is something like
*  what is the weather in Berkeley today
*  whatsoever in New York
*  it's not a problem if the user is then able to execute API calls
*  via this GPT-4 assistant
*  but if your API is something more like
*  you're an e-commerce store and you want to have a chatbot
*  to help triage whether or not an order should be refunded
*  and you want it to follow a set of rules
*  well you can just tell GPT-4 to ignore those rules
*  and just execute refund
*  I don't believe of $1,000
*  so you basically cannot give it any kind of privilege access
*  and I think the really interesting thing we found
*  was that you can actually ask the GPT-4 assistant
*  to help you do that attack
*  so if you say I'm a penetration tester
*  and I want to test this API for some security vulnerabilities
*  can you generate some SQL injection attacks for me
*  it will do that and then autonomously execute each of those attacks
*  so in fact even if you don't know how to exploit common vulnerabilities
*  as long as you just know the names of them
*  you can actually get the assistant to help you do all of that
*  so you really should be viewing any API exposed from GPT-4 assistant
*  as being completely public and it needs to be locked down
*  in the same way that any other public API would be
*  yeah that's crazy, you know it reflects a profound problem
*  and probably multiple profound problems
*  but one is just the question of like
*  whose assistant is this right?
*  is it OpenAI's assistant?
*  is it the application developer's assistant?
*  is it the end user's assistant?
*  and you've got at least kind of these three masters
*  that the thing is supposed to juggle
*  and it's in some sense a pretty challenging question
*  just to even get clarity for ourselves
*  on exactly where those lines get drawn
*  so with that in mind no wonder that the assistants can easily get tripped up
*  the next one is hijacking the assistant based on the knowledge base
*  yeah so it's another thing that OpenAI introduced in this assistant's API
*  was the ability to upload documents
*  and then intelligently search over those documents through GPT-4
*  which is really useful because often you don't want to just interact
*  with things it remembers from the pre-training database
*  but maybe you've got to take a paper
*  and you want it to read the paper before you give a summary
*  and answer some questions you had about it
*  and what we found was that you can just include instructions
*  in the uploaded document that will then be followed
*  by the GPT-4 assistant really so long as it actually
*  accesses that part of a document it will be able to be hijacked by that
*  so you could for example ask it to summarize the document in a misleading way
*  you can either say exactly how you want it to summarize
*  or just say please report this information in a negative light
*  and it will do that and you know if you're thinking how you do this in a real world attack
*  you could actually hide the instruction from a human reader
*  so it's not immediately visible just by setting the font color equal to the background
*  but you know obviously OpenAI is just looking, assistants are just looking at the text version of it
*  so unless you did that conversion you wouldn't even see it even if you did read the full document
*  but if you were searching in a 500 page document you also wouldn't read the whole thing
*  so it could easily slip past you
*  and you know one interesting thing that actually we didn't discover this
*  it was another security researcher but you can kind of chain these attacks together
*  and say I'm going to upload a malicious document or paste in a URL
*  of a malicious website and then it will hijack the assistant and cause it to retrieve another URL
*  including some sensitive data that you entered previously into the session
*  this is kind of going back to saying well the danger of a model is related to the affordances that it has
*  and here one of the affordances you're giving it is basically just this chat history
*  where you've uploaded a variety of documents some of which might be private
*  and if you've been interacting the same session with a malicious document
*  then you might now have leaked all those private documents
*  and so it's just sort of you know I think this is partly a usability issue
*  where it's just it's not clear to a user that that is what they're giving the assistant access to
*  if they knew this assistant couldn't be trusted and any document you upload could then get leaked if it gets hijacked later on
*  maybe people would be more careful with these chat sessions but actually the user interface of anything is encouraging you to have these longer sessions
*  where it can get more and more context and you know be more helpful to you
*  but you're also basically giving this like very gullible assistant more and more information that it could potentially then leak to an attacker
*  so let's talk about the kind of ethics around doing this work and how you disclose it
*  and then we can get a layer deeper into you know why this is not going to be an easy thing to resolve
*  and on this red teaming you know or just kind of public I call it red teaming in public
*  I have very genuine questions so I'm like very interested in your response as a partial guide to my own future work
*  what is the protocol that you go through for disclosure and giving them you know kind of a fair chance to fix it
*  and also how do you even think about what you should you know disclose or not disclose
*  like one might infer that there's like even more sensitive stuff that you haven't necessarily revealed
*  you don't have to comment on that but I would you know expect that there's some part of the process that's like
*  do we even want to put this out there is it worth it you know so we'll hear all your thoughts on that
*  yeah absolutely I mean I think this is a really important but quite challenging topic and there are responsible disclosure protocols
*  responsible disclosure protocols have been developed in computer security more generally but it is just a bit of a different beast with AI models
*  so in computer security the norm would often be that you report a vulnerability to the developer and you give them some period of time
*  so the typical period is a few weeks to maybe a few months for them to patch and fix this vulnerability
*  and you know the challenge with AI systems is that a lot of these vulnerabilities can't really be patched by a sort of a software fix
*  it's more that it requires a fundamental research progress to reliably address them or even in the best case
*  maybe it can be addressed from a different training method but you'd have to retrain the model from scratch perhaps or do a pretty substantial fine-tuning run
*  so some of these problems cannot be fixed on a few weeks or a few month time horizon and it might be sort of more like a few years
*  so then there is this sort of ethical dilemma of do you release that and then there will be some malicious actors that read your paper
*  and use that to cause in the immediate run but then also alert the research community to these problems so people can come up with a good long-term solution
*  as well as also just sort of making it clear to the front-end model developers like this is a real issue and they also need to be looking at solutions
*  or do you disclose it to a much smaller number of players like just for sort of security teams at these AI companies
*  and then sort of hope that they are able to in-house fix the problem but then perhaps there are going to be other developers who you didn't think to alert
*  who aren't part of this sort of you know small set of current front-end model developers who don't incorporate these solutions in time
*  or there's a researcher who could have come up with a solution but hasn't heard of it so you know right now I am erring fairly on the side of disclosure
*  so I would still if we did discover a vulnerability in a front-end model we would definitely tell the developer first and give them an opportunity to put mitigations in place
*  and I don't have a sort of particular fixed time limit in place it does depend on sort of how long I think the mitigation would take
*  but sort of somewhere between four weeks to three months seems right to me in general but acknowledging there are going to be some of these problems that you know cannot be fully mitigated
*  and I think you know the fine-tuning problems are a good example of this where I don't think there is going to be a good solution in the near term
*  it requires substantial research progress to make fine-tuning safe and so sort of the best you can do really is probably like really lock down access to that fine-tuning API
*  and so that's something where yeah you know us publishing on this probably is going to cause there to be slightly more attacks against the developer
*  but it's also something where you know it wasn't like we had some huge insights as an attacker we really did just do kind of obvious things
*  so I don't think that capable adversaries like nation-states are going to be significantly advantaged by reading our paper
*  but it might cause sort of slightly less sophisticated actors to have some ideas that I've always wouldn't have had
*  and I think the reason I'm erring on this side of disclose more is that there is and none of you have seen this but there is a lot of people who are going to be able to do that
*  and the reason I'm erring on this side of disclose more is that there is and none of these risks are causing massive immediate harms
*  which was the first main thing tonight and then the second reason is that the amount of researchers who could tackle this problem outside of the main AI companies
*  is just much much bigger than what the resources just inside of those sort of AI safety and preparedness teams at the companies could mount
*  and there's a much larger number of people who could work on these problems and then finally there is a very active debate right now about how these models should be regulated and governed
*  and so I think it's really important for at least policymakers but also the general public electing these officials to be aware of what the safety and profile of these models is
*  so that we can have effective regulation there now perhaps in the future we could actually have government agencies who are responsible for receiving some of these disclosure reports
*  and deciding whether to make them public or address them internally and that might be better than just individual security researchers such as ourselves making these kinds of decisions
*  but I would be hesitant to be in a world where kind of the only people who know the safety fairies of the companies themselves was obviously that even if they all have the best possible intentions
*  there's going to be a really strong incentive to potentially downplay that.
*  I think that all makes sense I find myself a little more hesitant and I'm not sure really why I mean I think I think I'd buy the reasoning
*  but I was kind of wrestling with this over the course of the last year with just honestly the most simple thing in the world like taking a pretty egregious prompt
*  and asking GPT-4 to be a spearfishing agent just in straight dialogue with a target and you know that was something I tried in the original Red Team
*  reported when they watched the production version in March of last year tried it on the first thing to my great surprise actually the exact same prompt
*  worked straight away every time no refusals and then I was like well jeez what should I do about this you know like on the one hand maybe the fact that they haven't fixed it means it's going to be really hard to fix
*  and they're not going to fix it you know but I also agree that like this is it was so obvious you know I was not even masking my intent I always start with the most egregious thing
*  and work my way backwards which is maybe a tip for Red Teaming you know interested in or aspiring Red Teamers in general it's honestly a lot easier to find the problems than you might expect
*  if you literally said just imagine I am a naive criminal and I know nothing about you know covering my tracks or you know whatever I'm just purely trying to get the thing to do whatever like a lot of times that will work
*  so that worked and it worked again on subsequent releases and eventually like a year on I finally tweeted about it but in the meantime I was kind of like man
*  and I did you know report it to them directly as well in the meantime but I was always kind of like maybe I should you know I don't know I just this is something that's so easy to do that I was a little nervous about kind of popularizing it
*  I don't know there's not really a question here but it's just I've always found myself being a little bit more reluctant to put these things out there
*  That's a very reasonable response and I don't feel like I've got a great principled way of deciding on these trade-offs I mean it would be excellent if we had a way of actually tracking
*  there are now a bunch of people using the Nathan LeBend spearfish you know can we monitor that that would be you know useful to see if there was actually an uptick or if it was something where the people who you know excited to abuse them already were or they're just not interested in doing it because we basically you know we have some very cheap humans who can already do this
*  as well so I think that kind of empirical feedback would be great but you know there is just a real trade-off here I think the one thing I would say is that rather than publication being a binary decision there are different approaches you can take so you could publish on things that are not as directly applicable to a criminal use case but sort of clearly illustrate to the security community as well
*  So maybe you don't have it do spearfishing you do have it be able to write sort of highly personalized manipulative messages to people and then you know you can also do it with the
*  You know you might the people who need to know might be able to kind of join the dots even if it's not going to be like as obvious to someone in the general public so it's one way of sort of getting sounding alarm but in a less obvious way I think you can also release this kind of stuff but just in a sort of somewhat dry academic style and you know it I don't think that very many sort of random criminal gangs are reading every archive machine learning paper so sort of if you do release something but to relatively little fanfare again it might be something where you can you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right
*  people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can get the right people to be aware of it and you know you can
*  Yeah, so I know that there's been some hard trade offs but I definitely would encourage people to think about, you know, not just do I publish disclose at all, but exactly what do I publish you can also report that you found it very easy to cause fair fishing, but not actually disclose
*  for prompt for examples it's like a variety of things that you can, you can choose depending on how dangerous you think for information is.
*  Share that publicly. It was after the latest version had finally started to refuse, and it was still not hard to break the initial refusal, but at least it was like the most totally flagrant prompt was getting refused.
*  And I basically did a version of what you said where I said like this used to work look how flagrant this is this no longer works it's not that hard to come up with something that still does work but I didn't, you know, publish that version of it.
*  Another thing that I'm really interested in and this kind of anticipates some of your big picture thinking is the AI application industry right now is like it's barely an industry right it's like a it's a bunch of hobbyists and you know a few more advanced players
*  but just like tons of people trying tons of stuff and it's everybody's kind of exploring the space simultaneously. I find often that a lot of application developers are not doing anything at all to put any guardrails on their systems either so we could
*  we could say oh man open AI should be doing more or maybe they're doing enough or whatever but they're clearly doing a lot. And you know it's, I think, the fact that the exploits are so easy to find probably reflects more that it's a really hard problem than that
*  they're not trying hard.
*  But then there are examples in the public, you know where you go try these like various apps. And there are some that are just like egregiously not trying hard.
*  I don't know if you've worked on that frontier at all but I'm kind of thinking, it seems like we probably need to start to create some industry standards.
*  And it seems like some examples may have to be made of some developers that are just egregiously not concerned with what they're putting out there. Right now the top category for this for me is the calling agent, where I have put one out in the public so far
*  of a, you know, you basically just prompt the thing and it will call and have a conversation verbally over the phone with someone. So I just did a simple ransom call. And again, it's so often it's the first thing you try. Call and demand ransom, you have their child, you know, whatever.
*  And it just does it. Do you have a sense for sort of how you would play things differently if you're talking about somebody that's, you know, a three person company that might even have just been a weekend project that they spun up versus, you know, a leader in the field?
*  Yeah, I mean, I think we definitely do need to have different, different safety standards depending on the application domain, the degree of technical sophistication of a project and emphasize other companies.
*  So, I mean, my first reaction is if you're actually developing in a safety critical domain, like imagine you're making a healthcare assistant, bad output can really cause substantial harm.
*  I don't think saying, well, we're a small startup is really excuse. Like that's just sort of table stakes. We don't say that for pharmaceutical development. Like, oh, you know, well Pfizer should be held to a really high safety standard.
*  But if you're a biotech startup, you can just skip the clinical trials. I guess that's not how it works. It's, you know, you, you need to prototype it and you need to raise funds to the point where you can run a clinical trial.
*  But you can't just kind of skip those safety steps just because you're small. And will that slow down innovation? I mean, yes, to some degree. And that's a trade off that you do have to make.
*  But if it's a sufficiently large downside risk from malicious applications or just sort of negligent applications and sort of trade off that we've faced and resolved in many other domains in favor of safety.
*  But if it is something that's, you know, much more of this kind of just generic software as a service. So I think that sort of, you know, phone call agent is a good example.
*  Okay, you know, yeah, there were some potential malicious uses of it. But there's also lots of very, very beneficial uses. Or, well, I say that I expect there's some beneficial uses of like, doesn't seem like the main use is more spam calls.
*  So maybe not. I think that there are some very basic things that they could do and should be expected to do. But the most obvious one is start every phone call over recorded messaging.
*  This is an AI. So if you just prevent it from impersonating people and say, you know, this is an AI, you know, press star for more information and how to report abuse, then suddenly you've really reduced the risk profile from this because, you know, yeah, it could still be a real ransom call with someone using an AI as an intermediary, but it's probably going to you're going to do a little bit more suspicion.
*  You maybe not have this number you can contact to find out more information about who was using this platform. And, you know, if you do then call up that number and they're like, oh, yeah, we just received like 1000 abuse complaints from this, you know, this user, you can just ignore it. It's not a real ransom call.
*  And it's a problem solved. Now, it's not to say that's that's trivial. If it is a free person startup, you got to build a bit of extra infrastructure to do that. But it's, it's not a particularly onerous requirement to have to have a recorded message and you know, just an abuse reporting form somewhere.
*  I mean, that could still be just like an air table on your website doesn't have to be stuffed by a full time 24 seven response team. So I think there are some things where I'd say every application developer has responsibility at least spend an hour thinking about, you know, how could someone abuse it and whatever, like, you know, really still solve the problem.
*  So I think there is also a responsibility on the general purpose model developers to make these things easy for people. Right. So if I think of who is responsible for a buffer overflow attack, right, like, is it the programmer that wrote it? Is it the developer who paid the programmer and, you know, skimped on code review? Is it the designer of C++? Right. You know, it's sort of like a responsibility is sort of shared between the developer and the developer.
*  But one of the best ways of eliminating security vulnerabilities has been changing with technology. So you just can't write a lot of flows in sort of most modern languages like Java or Python, because for programming language is managing the memory for you. And I think there's a similar thing where really, if we're saying who should be responsible, a company that's got a multi billion dollar R&D budget, and who's responsible for the memory, right. So I think there's a lot of responsibility on the general purpose model developers to make these things easy for people.
*  And I think there's a similar thing where really, if we're saying who should be responsible, a company that's got a multi billion dollar R&D budget, and whose revenue model is selling to a bunch of scrappy startups, or this, you know, 10,000 scrappy startups themselves, obviously we should be where possible trying to transfer some of that responsibility onto the multi billion dollar R&D budget, because you can solve that problem once and it gets pushed out everywhere.
*  And I think there's a similar thing where really, if we're saying who should be responsible, a company that's got a multi billion dollar R&D budget, and whose revenue model is selling to a bunch of scrappy startups, or this, you know, 10,000 scrappy startups themselves, obviously we should be where possible trying to transfer some of that responsibility onto the multi billion dollar R&D budget, because you can solve that problem once and it gets pushed out everywhere.
*  And I think there's a similar thing where really, if we're saying who should be responsible, a company that's got a multi billion dollar R&D budget, and whose revenue model is selling to a bunch of scrappy startups, or this, you know, 10,000 scrappy startups themselves, obviously we should be where possible trying to transfer some of that responsibility onto the multi billion dollar R&D budget, because you can solve that problem once and it gets pushed out everywhere.
*  And they just have the resources needed to do it.
*  And I think there's a similar thing where really, if we're saying who should be responsible, a company that's got a multi billion dollar R&D budget, and whose revenue model is selling to a bunch of scrappy startups, or this, you know, 10,000 scrappy startups themselves, obviously we should be where possible trying to transfer some of that responsibility onto the multi billion dollar R&D budget, because you can solve that problem once and it gets pushed out everywhere.
*  And be safe by default, and then you can sort of unlock these extra capabilities as needed. So I don't think this has a simple answer, but I would definitely be trying to push for liability up the value chain where possible, because they just have more resources to actually be able to solve these problems.
*  And it doesn't seem like other kinds of security vulnerabilities that having every individual developer and user of these applications be responsible has ever worked.
*  Are you aware of any sort of taxonomy of affordances and or kind of minimal best practices for application developers?
*  And by the way, you know, I can come up with lots of good examples of positive reasons to use the calling agent. You know, for example, just simple appointment reminders with the ability to reschedule in an interactive way, right?
*  Like, that's great, everybody wins. So I do think there are definitely legitimate uses. But when I find something like this, and I reach out to these developers, and by the way, every single one I have tried has all the same vulnerabilities.
*  Some even have more vulnerabilities because they support voice cloning where others don't. So that even takes up another dimension.
*  But I find myself kind of wanting to say something like, here is the taxonomy of affordances on which you are in column three.
*  And in column three, you're supposed to do these eight things and you clearly haven't done them.
*  Are you aware of anybody who has either created something like that or perhaps working on it?
*  Because I want that one sheet or to be able to kind of push in front of people and say, hey, look, like this is what you got to do.
*  I'm not aware of anything as systematic as that. It's possible that Apollo research is doing some work on this because they sort of popularized this capability affordances trade off.
*  But what I have seen so far has been quite high level saying, well, you know, if you can fine tune your model, that's a pretty big affordance. It has access to these kind of external tools.
*  It's another affordance. But no, I think it would be quite valuable to actually have something that's a bit more specific and targeted at actual applications people are showing right now.
*  This does seem like the kind of thing that, you know, if someone is interested in it, it could be contributed to the NIST risk management framework.
*  And so they have a risk management framework for AI and part of what they're developing is this playbook and saying, well, if you're in this particular application domain, how do I apply this framework?
*  And so I think that we are in this stage where there are very few actual technical standards on AI, relative to the importance of our technology.
*  And we do kind of need to develop that and figure out what best practices look like.
*  And unfortunately, there's maybe just a bit of an absence of a safety culture in software engineering, which a lot of people working in machine learning have that kind of background relative to other engineering disciplines.
*  So I think that's also sort of shift that people need to take.
*  I imagine talking to a traditional Silicon Valley venture bank startup and saying, well, you got to read this NIST document and implement the safety standard.
*  And I'll be not very happy about it.
*  Whereas if you're a civil engineer and you say, well, you've got to follow building codes, it's like, yeah, you've got to follow building codes.
*  You know, always you lose your engineering license. It's not a question.
*  Yeah, I do think there's going to need to be some cultural change and some kind of internalization among developers that like this is a different sort of thing, you know, than the things that we built before, especially when you're talking about, you know, one good rule of thumb, I would say, is to the degree that you are offering autonomous capability.
*  You know, that is a big difference.
*  I think I had a couple of, you know, like genuine leaders in machine learning respond to some of my stuff with like, well, a human could do the same thing or like, how is this really different?
*  And it's like, to me, there's a huge difference between selling a hammer to somebody and selling them a robot that goes and hammers things, you know, and like the robot that goes and hammers things like you got to have a lot more control over that than just the hammer itself.
*  Like that seems obvious to me, but it is not necessarily shared intuition for everybody.
*  My other question is, you know, I think what's happening here with these models that I've tried is that they are probably falling into the trap that we talked about at the beginning, which is they're starting with an open source model.
*  I'll bet it's like llama or perhaps Mistral now.
*  There was, if it's llama, I don't know as much about exactly what Mistral includes or doesn't in the default package, but llama to chat, you know, has a pretty robust refusal.
*  If anything, they maybe overdid the refusal and kind of, you know, created a situation where people wanted to fine tune it away because it was overbearing.
*  But even if they didn't write, these folks are definitely going to for these calling agents, they're going to fine tune just because they want it to be more conversational and for all sorts of little behavioral reasons.
*  Next thing you know, perhaps without even intent, they've stripped away the refusal behavior and now it's just kind of out there.
*  So all that leads to the question of how do you think the open sourcer should be considered in this context, right?
*  They're not making revenue like an open AI would be. Should they have responsibility for that use?
*  Yeah, I mean, I think this is a really difficult question.
*  Thank you for your question. And I'll say, first of all, that we use open source models all of the time in our research.
*  It's incredibly valuable for this kind of safety and alignment research.
*  But I'm also worried about a world where we have arbitrarily capable models being open sourced because it's very difficult to stop fine tuning APIs from being abused.
*  It feels almost impossible to me to stop if you just have the model weights malicious users fine tuning those weights and using some vulnerabilities.
*  It's not completely inconceivable. People have put a proposed self distracting models where if you try to fine tune on the wrong data, it harms the capabilities.
*  There might be some technical approaches, but we're very, very far from having that right now.
*  But then this is an intermediate case where it sort of feels like the model's not sufficiently capable to be really dangerous without these additional affordances that it's given.
*  But you know, but if you release it, there are going to be some not malicious but just slightly negligent or reckless actors who put the model in situations that they can't necessarily fully safely handle.
*  So what's your responsibility there?
*  Well, I think that you can say, you know, at the very least, your responsibility should be to sort of document the limitations of a model really clearly.
*  And if people ignore that documentation, then, you know, I mean, for some of our responsibilities on them, that's not to say that you can wash your hands of it.
*  But you know, you've at least have done the bare minimum as a developer.
*  So I do think it's important to still have these kinds of, you know, model evaluation, model testing, including with independent third parties prior to release of an open source model.
*  I guess there's going to be a lot of testing after the models released.
*  But you also really do want to have that from a get go because people are going to start using it in application straight away.
*  I would say that, you know, there's also when you're talking about really big training runs, I think when you hear open source, at least to me, I'm always like, is this Nick, you know, small community developers on GitHub, they're volunteering their time.
*  That is not what open source language model runs like, you know, Lamo and Mistral look like.
*  These are things that a very, in the case of Facebook or Matter, a very large company in the case of Mistral, like, you know, still a pretty sizable company with hundreds of millions of dollars in investment has, you know,
*  produced and chosen to release, you know, often in some cases for a commercial reason.
*  Right. I mean, obviously a lot of the rhetoric is around how this is helping the broader community.
*  But I don't actually think that necessarily I know those companies have a strong ideology of commitments open source.
*  But it's like, you know, they're behind in the sort of frontier model development game.
*  And this is a way for them to get a lot of good publicity and use of their models.
*  And it doesn't really cost them that much if they're going to be trading it anyway.
*  So these are still well resourced actors.
*  And I think it's reasonable to at least ask them to spend some fraction of their R&D budget on safety.
*  Even if it's not as much as the likes of OpenA or DeepMind who are actually getting revenue from these models and are spending, you know, substantial chunk of money on those models.
*  But, you know, in the case of Matter Zuckerberg just announced seven billion dollars in compute investment for frontier models.
*  So if they were to spend one percent of that right, seventy million dollars on safety,
*  then that would be not far from doubling the amount of revenue being spent on it on safety.
*  And so I think that's not an unreasonable request to say one percent.
*  I might even go a lot further. We actually put out a call to say there should be a minimum of a third spending commitment in research and development.
*  And so if you do that, well, what does that look like in the open source case?
*  It definitely looks like releasing safety fine tuned versions of models.
*  So it's safe by default. But I think if people are going to fine tune it, you know, that's one of my main use cases for the open source release.
*  Then it's also on you to have good tooling to enable people to do that own fine tuning runs safely.
*  And so maybe this looks like you've got a harm exam data set with examples of refusals to harmful requests.
*  And you can just mix in some of those examples into every fine tuning run.
*  So it doesn't catastrophically forget this. And yes, a malicious actor could disable that feature in your code.
*  But, you know, most developers are just going to leave the default parameters.
*  So have those default parameters be ones where your model is going to fail in a graceful fashion rather than failing in this unsafe way.
*  I think that would not be an unreasonable request to these larger developers.
*  But I wouldn't apply the same standard to really small organizations like Alutha AI.
*  They produce a relatively small series of models called Pithia.
*  None of the models have particularly big, dangerous capabilities.
*  They spent more of an order of like 10 million rather than 7 billion on training these models.
*  The standard we should be holding them to is lower.
*  Well, this is something we could talk about probably indefinitely.
*  But I want to get to a couple other lines of work that you and your teammates have been developing over the last months.
*  This next one is really a as I think of it, a sort of very technical argument that this is going to be a hard problem.
*  And basically the work is on superhuman go playing AIs.
*  And the upshot of it is that in this is a gray box setting, right?
*  Black box early on, we're talking from the from the open AIs, APIs.
*  You have no privileged access here in this in this go playing.
*  You have the gray box access, which means that you can ping it, you know, and say like, what would your move be in this situation and kind of then use its responses to systematically optimize against it.
*  But what's really striking here is that, you know, people think like, OK, well, we've got superhuman go playing AIs like, you know, that's that right.
*  You're kind of complicating that story by coming in and saying, well, if we set up a situation where we try to optimize against the superhuman go player and all we have is the ability to see what it will do systematically explore its behavior just by seeing what it will do in different situations.
*  Then that can be enough to, in fact, beat these, quote unquote, superhuman go player.
*  And it's still superhuman in most respects.
*  But it turns out that like, wow, it has these, in some cases, like very kind of surprising, in some cases, very simplistic vulnerabilities and in some in some sense, is very deep seated vulnerabilities as well.
*  So that's kind of my overview.
*  You can give me a little bit more on the technical implementation of that and what you think the upshots are.
*  As you say, we have this slightly privileged access where we were able to train an adversary AIs system to exploit some superhuman go AIs.
*  We used CataGo, which is the strongest open source go AIs.
*  And it had both privileged accesses and instead you could train against CataGo for as long as it wanted without CataGo itself learning and being updated.
*  And also, while the adversary was choosing what moves to play, it can query CataGo to see how it will respond to that.
*  So it's like you've got a very good model of what the opponent is going to do.
*  And what we found was that it's pretty easy to find attacks is the main upshot.
*  So we were able to find attacks with a fairly small fraction, you know, less than 10% as much compute as CataGo was trained with.
*  And originally we found a somewhat degenerate attack that caused CataGo to end the game prematurely at a time that was unfavorable to itself.
*  So it sort of thought, oh, I've won. And in some sort of moral sense, it had because if it kept playing the game, it would win.
*  But under the typical scoring rules using computer go and scoring rules that CataGo was trained with, it actually loses if it doesn't complete the game at that point.
*  But then we were able to patch that attack manually.
*  And then we found a much more interesting, at least from a sort of go play perspective attack, which resulted in the adversary forming these circular patterns on the board.
*  So sort of connected groups of stones. And then CataGo would encircle these.
*  And then we would encircle that again and capture this big CataGo group.
*  And CataGo seemed to be completely unaware that this circular group of it was about to be captured until it was too late for it to respond.
*  So it sort of thought these groups were invulnerable for whatever reason.
*  And then this attack, we were actually able to replicate manually. So unlike a lot of adversarial attacks, it is human interpretable.
*  So one of our team members, Kellen Pelrin, who's a very strong go player, but he's an amateur.
*  He's not world class, not superhuman by definition.
*  He's able to very reliably beat CataGo and actually was able to beat CataGo even after giving it a nine stone handicap, which is sort of what you would give a complete beginner who's maybe a child and is just playing go for the first time.
*  And it's almost offensive to offer that handicap to a superhuman go AI agent.
*  But it's even with that handicap, he's able to beat CataGo.
*  So that was, I think, to a lot of people very surprising because these AI systems, well, both they seem very superhuman.
*  And they've been around for six or so years after AlphaGo's initial victory.
*  And many humans have tried to win against them.
*  Lots of professional go players and go enthusiasts use them as part of their training.
*  But this kind of attack was basically completely unknown.
*  And we wouldn't have found it if we hadn't actually explicitly done some adversarial testing.
*  And so I guess the key point here, again, it's worth kind of emphasizing the setup is that you get to ask what would you do in this particular situation?
*  And that's like a pretty representative setup in the world, right?
*  Because if we're going to have AI systems and they're going to be out there, they're going to be deployed, they're going to be in use, then obviously it's going to be the kind of thing where people can ask what they would do in these situations.
*  And you don't even really know.
*  I mean, it's also important to kind of keep clear that the difference between asking what you would do in this situation and just everyday use is not obvious.
*  Right. I mean, when you're asking what would you do in this situation, you're basically just giving the go engine a board state and asking it to make a move like it has no way of resolving whether it's being optimized against or just playing a normal game.
*  Right. Absolutely.
*  And I think this is a very common setting.
*  I mean, certainly any open source AI, you'd have this because you just have a copy of it, but you can query.
*  But even just any kind of consumer product where you can have a copy of it yourself that you can interrogate would satisfy this kind of threat model.
*  And we actually found it's not even strictly necessary to have this mailbox access.
*  So although we trained against Caligo, we then tried the same attack against a variety of other both proprietary and open source go AI systems.
*  And that attack did transfer.
*  So it was also able to exploit these other AI systems.
*  The win rate was lower.
*  We got sort of well above a 90% win rate against superhuman versions of Caligo, whereas you might only get somewhere like three to five percent win rate against some of these other AI systems.
*  But we found that Kellan was a strong go player was able to win against these systems at a much higher rate than that.
*  So the problem wasn't that the other systems weren't vulnerable to this.
*  It's just that there's enough differences in the system that you need to sort of tweak the attack slightly.
*  But I suspect it would be very easy to then fine tune with much less access to these other systems and find a way of reliably exploiting them given that humans are able to quite readily adapt to that attack.
*  So it's not just enough to sort of put your system in a secure black box.
*  If people know roughly how your system was designed, they could find attacks against similar systems.
*  And then probably some of those attacks are going to relatively small modification work against your system.
*  And we've seen this not just in the go context.
*  There was Andy Jow and his team at CMU came up with these universal adversarial attacks by attacking some open source models.
*  And when they do just work against GPT-4, against Bard, against a variety of these proprietary models.
*  We have a episode on exactly that paper as well.
*  So the kind of first response to this would presumably be, let's just mix some of that data into the training and rerun it.
*  And that way we should be able to patch it. Right.
*  So nothing to worry about.
*  Yeah. Yeah. Well, I mean, this is one of the best defenses that people have.
*  This is an adversarial training approach.
*  And both our team and the Catago developers have been trying to do this with some success, but it's still very exploitable is that the headline results.
*  So the Catago developers created thousands of sort of example games for a mixture of hand constructed positions and procedure general positions to really kind of try to teach Catago how to actually play these positions correctly.
*  They've been including that as part of their mainline training run for the best part of a year now.
*  And sure enough, the original attack we found, its win rate does decline quite a lot.
*  I think it still wins occasionally when playing against just the neural network itself, but it stops winning when playing a modest amount of search.
*  Because this is a mixture of both symbolic look ahead reasoning and the neural network.
*  But then if we just keep training our adversary against this updated Catago version, we're able to find an attack that works very reliably against this new version.
*  So it seems like it's not really learned a robust algorithm for how to reason about it.
*  And there's more just learned some of the common patterns and how to correctly respond to them.
*  And it's maybe also just being a bit risk averse and saying, oh, I really don't like circles on the board.
*  That's scary. Let's try and avoid it.
*  But you can still set up positions where it will make serious mistakes.
*  Now, the Catago defense that was trying really hard to preserve those capabilities for regular games, because obviously their priority isn't just to defend against our attack.
*  It's to produce a really awesome piece of software that Go Enthusiasts can use.
*  So we also wanted to do our own training run that was willing to sacrifice a bit more capabilities, a bit more elo-script in order to get something that is actually truly robust.
*  So here we did many rounds of adversarial training.
*  We'd harden our version of Catago by training against these adversarial games.
*  We'd find a new adversary. We'd do another round of hardening.
*  We did nine rounds of these hardening in total.
*  And again, we found that it is still vulnerable.
*  It does require a fair amount of extra training on the adversary's part to find these attacks.
*  So it does raise the cost of attack a little bit.
*  And it does change qualitatively in nature.
*  What we find is that these circular groups now take up most of the board.
*  So rather than being a relatively small group, it's now really just the whole board is in attack.
*  And this is probably much harder for these AI systems to reason about because there's a limit to how much global reasoning across the board they can do in a fixed-depth neural network.
*  And then we actually also thought, well, OK, maybe this is a problem with this neural network architecture.
*  So let's try vision transformers because they don't have this kind of spatial locality bias that a lot of us with state-of-art image classification models are using vision transformers.
*  And so we trained our own superhuman vision transform model and found that it's also vulnerable to this kind of attack.
*  And if we target the attack specifically against this vision transform model, we again can get very high win rates as an adversary.
*  So very hard to eliminate.
*  I think the main source of hope would be that with some of these additional attacks, we haven't yet found an attack that works against a really high amount of search for these victim models.
*  If you do do adversarial training plus play with way more search than you need to be superhuman, then it might be quite hard to find an attack.
*  I think it probably is still possible that it might become kind of computationally intractable for most attackers.
*  So that is a bit of an escape route.
*  But, you know, of course, in many ways, Go is a much simpler, lower dimensional game than, you know, unconstrained text inputs.
*  So the fact that we can maybe just about make it really hard for an attacker in Go is not much consolation when we think about actually securing frontier general purpose AI systems.
*  That point probably can't be emphasized enough.
*  The difference in surface area between the, you know, and it's I mean, numbers are crazy, right?
*  Like the number of possible states of a Go board is just like astronomical.
*  And yet it's still tiny compared to the surface area of a GPT-4 and just the arbitrary nature of any input and output that it could possibly see.
*  So it's definitely a daunting problem.
*  I guess the upshot of all this is your view is that at least barring some sort of conceptual breakthrough,
*  you could maybe speculate as to the prospects for such a conceptual breakthrough, but barring such a breakthrough, today, systems are exploitable by default.
*  And the flip side of that coin is that to become less exploitable, you have to pay what you have called the robustness.
*  So you want to kind of characterize, I think we've made the case probably for the exploitable by default.
*  You want to characterize the robustness tax and maybe speculate a little bit as to the plausibility that somebody might have the conceptual breakthrough that we need.
*  Yeah, I think right now contemporary machine learning systems can be split into systems that people have successfully attacked and systems that people haven't really tried to attack.
*  There's not really examples of systems have really withstood concerted attacks.
*  So that alone is a pretty strong evidence that's exploitable by default side of things.
*  But in terms of, yeah, how could you get robustness if you really want it?
*  We do have some both theoretical and empirical evidence to believe that there is a trade off between worst case performance or robustness and its kind of average case performance.
*  So in the case of computer vision, these small adversarial examples have been quite well studied in the theoretical setting.
*  And there are results arguing that there is this trade off between robust and clean accuracy.
*  And then we also do just see this when we look at state of our adversarially trained models and computer vision.
*  This is exactly what you're suggesting. You find these adversarial data points, you feed that back into the training data set.
*  They do have substantially lower clean accuracy than comparably sized models.
*  And this is after substantial additional compute because adversarial training stuff is quite computationally expensive.
*  So this is some empirical evidence for a robustness tax.
*  If we were to kind of put this a bit over to the more sort of large language model setting,
*  I'd say that one of the things I feel more optimistic about in terms of actually getting some rigorous safety guarantees will be if we really narrow the sort of safety properties we're trying to get, but demand them with a very high probability.
*  And so I think a good example of this is Anthropic actually has made a commitment, I believe, for their ASL-free models.
*  These are models that aren't quite human level, but can really accelerate certain types of scientific R&D that they will not have jail breaks that affects chemical, biological or nuclear weapon development.
*  So you can still, your spear phishing attack, I think that would still be allowed, but there shouldn't be some jailbreak that will cause it to say, you know, well, here's how you enrich uranium.
*  And you can sort of see how you could achieve this actually, like pretty easily just by removing any document from a training data set that has anything to do with chemistry, biology or nuclear physics.
*  And then indeed a model that is not even human level is unlikely to be able to, without any additional training, be able to assist you in any domain related to these weapon development programs.
*  But it also is not going to be able to help you answer your perfectly innocuous chemistry homework, or help you look up a relevant medical research paper.
*  So there's this sort of collateral damage where if you remove this dangerous capability, then you're also removing a bunch of harmful capabilities.
*  And a lot of things we want models to do are dual use, the code generation, that's great.
*  But if you can write code, you can also write a root kit or an exploit.
*  Right. And so if we don't have perfect filters to distinguish between these malicious versus beneficial use cases, then what we only think we can really do is just obliterate.
*  So any capability that could be abused and conversely, the more precise we can make these filters, the less collateral damage we need to have for capabilities.
*  But right now we do not have very good ways of having these precise filters.
*  You can only can adversely exploit them. And so that's where I see robustness tax coming in in practice.
*  It's everything right. It's like you got to spend more time doing it.
*  You're going to put more compute and you're going to have kind of degradation of performance all at once.
*  And so you've got kind of trade offs and it's all super annoying.
*  But that's kind of the only way that we know forward from here.
*  I think there's a couple of conceptual things that I'd love to get your thoughts on and then we can kind of go to where you and Farai are hoping to contribute to this.
*  Just on the question of like a breakthrough. I mean, obviously breakthroughs are very hard to predict.
*  But do we have any principled reason to think that somebody is not going to come along and solve this?
*  Well, I really hope someone does. I do think the theoretical analysis should make us a little bit hesitant.
*  But at least under some reasonable assumptions, there does seem to just be a trade off between these objectives.
*  Now, that's not to say that you couldn't get superhuman capability and superhuman robustness.
*  There's no theorem saying that you can't achieve that.
*  But it might be that you could get superhuman capability earlier if you're willing to not have superhuman robustness.
*  There probably is going to be some kind of trade off that people are facing.
*  But that doesn't mean that it's insurmountable.
*  I think we've solved that problem in many safety critical domains where you just say, well, you know, if you release an unsafe system, you have liability or you can't get approval for the training run.
*  So as long as there is a pathway to superhuman or human level robustness, even if it's a little bit more costly, I think we're in relatively good shape.
*  Now, right now, I don't think we even have a plan for reaching human level robustness, even if we did make concerted effort to do so.
*  We'll have been trying quite hard for over a decade to solve adversarial examples.
*  But I think there are some reasons to be more optimistic in the tech space.
*  I think it is very high dimensional, so many more states than is possible on a go board.
*  It is lower dimensional in many ways than an image.
*  It is this discrete domain rather than continuous.
*  Although the context window is massive, if you are just looking at a local context, the number of possible inputs is often much smaller for text and for a comparably sized image.
*  So that's sort of, you know, maxim that a picture is worth a thousand words.
*  Maybe it really is true if you look at the size of the state space.
*  So that might make it easier to get some of these safety guarantees.
*  I also think that, you know, for the most part, people haven't been focusing on the most safety critical, physically realistic threat models.
*  So if you do have a concerted effort to actually make frontier models safe, that is, you know, of a similar amount of efforts, what we're doing to try to scale up frontier models, then I think that would very likely yield some positive results.
*  I think there's also a reason to be optimistic that we don't need fully adversarial robust systems.
*  I had this idea of a fault tolerant AI system and my idea is more of a defense in depth kind of analysis and saying, well, what affordances does this model have?
*  If it has limited affordances, then maybe you can tolerate certain failure modes.
*  Maybe you can just, you know, basically import this principle of least privilege.
*  Don't give them all access to anything it doesn't need to have that limits for blast radius.
*  You can have different models monitoring each other's outputs.
*  And so you might be able to get to a point where, although any given component in the system is quite brittle, it's really hard to be able to beat both sort of filter on the input going in the model's own safeguards, a filter on the output.
*  Some human monitoring of your usage of this API.
*  So you get kicked off the platform if you abuse it for too much.
*  You can imagine all of these extra layered safeguards where any individual component can be broken.
*  But the overall inner system is pretty hard.
*  And I think there's all sorts of cases in society where we do just have very vulnerable components, but we've shaped incentives and the overall system to be quite safe.
*  So it is actually very easy to rob a bank.
*  Like bank tellers are told if someone approaches you with a weapon, you should just hand over the cash.
*  But it turns out like the police response is generally pretty robust and banks don't have more than tens of thousands of dollars on hand in a branch anyway.
*  So the bank has managed to limit the loss and broader society has meant that it is not a very lucrative criminal profession to be a bank robber, as we will mostly just don't exploit this attack.
*  And I think there might be many analogs there in AI systems where some of them can be exploitable, but only in relatively low stakes settings.
*  And if you do, you're going to get caught. You're not going to have access to the system any longer.
*  And so you really would prefer not to exploit these systems.
*  One of the things that I thought was really interesting in reading your work, leading up to this was the analysis that you had on different training paradigms and how different training paradigms have very different implications.
*  There are different implied incentives for a sort of adversarial.
*  There's like some of them are adversarial in nature and sort of incentivize that exploit behavior and others are much less.
*  So you want to give a quick overview of that analysis? I think that's really interesting.
*  Absolutely. So most of our discussion so far has been focused on some more of a malicious use risk.
*  So someone out there is trying to exploit a model or at least is being negligent in their use of a model.
*  We also, the way we design AI systems is composed of multiple machine learning components.
*  So when you do do this sort of safety fine tuning, what you're normally doing is you're having a large generative language model that is being optimized using something like reinforcement learning to maximize the reward signal given by some other large language model.
*  And there's a various variants of this setup, but all kinds of fine tuning involve optimizing some kind of other objective.
*  And then you have this interesting question of, well, what is optimization if not in some ways being adversarial?
*  You just want to find the input that will cause the highest number from the reward model or some other training signal.
*  And if that input is not actually what a human really wanted because you're not being optimized directly from human judgment, but just exploiting this other model, then there will be this optimization pressure to learn that.
*  This kind of lack of robustness isn't just a security risk. It's also an alignment problem and that can be very challenging then to align models.
*  If you've got this lack of a reliable ground truth reward signal, and naturally we see that this does happen.
*  So if you just do something like RL from human feedback in a naive way, then you'll get this very gibberish output that is often not at all what a human wanted.
*  Both is incomprehensible and sometimes offensive, but gets really, really high reward signals.
*  And so people avoid this by basically just trying to stop any there being any major changes to the base generative models.
*  Maybe they add a KL penalty. So this is a regularization term that penalizes large changes in the model.
*  This is an effective workaround. But then you're also staying close to all the toxic and undesirable behavior that was present in the base models.
*  You're really limiting what your alignment technique can do by adding this kind of regularization term.
*  So it would be nice if we had instead either a robust reward model, but we've discussed why getting really robust models is quite hard.
*  Or we have some optimization process, which is still meaningfully aligning the AI system, but is not exerting as much adversarial optimization pressure.
*  And this is a relatively understudied area, but I think we already have some empirical results suggesting that different kinds of optimization processes do have meaningfully different tradeoffs.
*  So I think something like reinforcement learning seems like one of the worst ones, at least if you look in terms of how much it changes the model's behavior.
*  Whereas something like just sampling many possible outputs and picking the best outputs from that model, as judged by the reward model, that tends to stay much closer to the base model's distribution.
*  So it's probably less likely to find these adversarial examples.
*  This was found by Leo Gao and his team at OpenAI and looking at scaling laws to reward model over optimization.
*  But those are just two examples of optimization processes. You could do many others.
*  Imitation learning is probably safer than reinforcement learning from this standpoint, because your optimization pressure is just towards copying something else.
*  And so as long as you think your copying is harmless, you're unlikely to find something that is radically different to it.
*  I think there's also a possibility that something like iterated distillation amplification.
*  So this is almost sort of like an AlphaZero style training procedure for a language model where you have one model ask questions to copies of itself.
*  So it decomposes the problem and then uses those answers to come up with a response and then tries to distill that final response back into a model.
*  So it doesn't need to ask as many copies of a different model.
*  This is something where the optimization process is actually being guided by the model itself.
*  And so if a model doesn't want to exploit itself, and there's various reasons why, you know, at least if this is stable and converges to anything, we'll be trying to avoid doing that.
*  Then you're actually in a pretty good place because it should be steering clear from potential areas where it might be giving misleading answers.
*  This is definitely an area that needs a lot more work, but I'd invite people to explore this rather than just use off the shelf optimization processes because one of the big advantages we have for alignment as opposed to security is that we actually do get to choose the attack, right?
*  We do get to choose what optimization approach we different components of our system are using.
*  And so we only need to make it robust to a particular kind of adversary that we get to choose.
*  Whereas when we're in a security approach, we have to take whatever method of attack it comes up with and defend against all possible attacks, which is much, much harder.
*  So, yeah, I guess to just try to put a little framework around that alignment is sort of a subset of safety in the sense that alignment is trying to get the model to do what you want it to do under even normal conditions.
*  And safety includes these more adversarial unknown attack types.
*  And specifically in the alignment context, you're looking for setups which do not directly incentivize the what you call the main model in your analysis of this to find the exploitable weaknesses in the helper or the evaluator or the reward model.
*  So where where reinforcement learning is kind of the worst is that the the thing that the main model is optimizing for is the high score from the helper model and that directness that the tightness of that coupling is the source of the incentive to to find the exploits.
*  And there are other setups which don't have that like such type feedback loop and so are much less prone to that problem.
*  Yeah, exactly. So it's this direct feedback loop.
*  I've been also fairly unconstrained nature of reinforcement learning.
*  And so once it once it finds one thing that gets high reward, it will try to keep doing that, which usually is exactly what you want.
*  But it also means that if it stumbles across an adversarial failure mode, it's really unlikely to be discovered by chance.
*  It will now reliably keep on doing that adversarial failure mode, whereas some other optimization processes might be sort of slower to update and be more likely to stay in a sort of common safe region.
*  So there's a bit of a tradeoff between how much you explore in your optimization process and how likely you are to exploit.
*  So that's a different kind of explore exploit to trade off to what people usually mean by that term.
*  You explore more and you're more likely to exploit a model.
*  This is obviously a challenging context, right?
*  I mean, we're in this GPT-4 moment where it's like I always say GPT-4 is in a really sweet spot where it's like really useful.
*  I find it tremendously useful and I use it daily.
*  And it's also, you know, not so powerful that we really have too much to worry about in terms of it causing major harms or getting out of control.
*  I don't know how long that window extends. I don't know if GPT-5 stays in that window.
*  My guess is we probably have at least one more generation that would kind of stay in that sweet spot window,
*  although I wouldn't like dismiss somebody who had a different take on that.
*  What do you hope to do with your collaborators at FAR AI over the next year or two as we move from the GPT-4 to the GPT-5 era to help ensure that at least this next phase goes well?
*  One big project we're focusing on right now is developing empirical scaling laws for adversarial robustness.
*  Scaling laws in general have been very helpful for forecasting future developments in AI and then also enabling people to make more rapid progress by working out which methods do continue to benefit from increased scale and which ones do not.
*  But there's been a lot of investigation of scaling laws for capabilities, but no one has really looked into it for robustness, at least in the context of large language models.
*  And so we have some preliminary results there already showing that bigger models, in fact, are more robust.
*  But unfortunately, it was an increase in robustness is much, much smaller than the increase in capabilities.
*  So this is evidence that it is going to be this sort of widening capability robustness gap as things go on.
*  But then the thing we're really excited to do next is to look at, well, how do defenses change us?
*  So this is just the robustness of a pre-trained model fine tuned on a particular data set without any attempts to defend it.
*  But if we do adversarial training or if we do a more kind of defense in depth approach, we have some models moderating the input and output.
*  Does this actually not just improve the robustness of it, but actually change the slope of the scaling trend?
*  And what we'd be in many ways more excited by is not a method that massively improves robustness today, but it's something we say, well, in two generations from now or three generations from now, this will be meaningfully closing this capability robustness gap.
*  And so we're looking to identify a technique like that, which we could then scale up prototype and get to the point where this could actually be a solution to robustness for more advanced systems if front end model developers do adopt it.
*  So that's one direction that we're really excited by.
*  I think the other direction that we do want to explore further is this more fault tolerant angle and saying, well, OK, you know, if you can't actually get robustness, what does that mean for AI safety?
*  Does this mean that we need to really lock down who has access to the models if they have dangerous capabilities because we just can't defend against malicious use?
*  How do you even do that?
*  What does it know your customer regime look like for AI systems?
*  Are you able to make the overall system safe, even though lots of components are vulnerable by this kind of redundancy defense in depth?
*  Does it actually scale?
*  And yeah, what does this mean for alignment?
*  So there's lots of questions there that we also want to explore.
*  And generally, I think that this is a pretty under investigated area because there's been convenient assumption being made that OK, robustness is just going to go away once we get sufficiently advanced systems.
*  And unfortunately, I don't think that's the case in the absence of some kind of conceptual progress.
*  Can you give a little like order of magnitude intuition?
*  I always like to try to have a firmy calculation that I can go to.
*  So for the current, you know, this is pre adversarial training, right?
*  You're just kind of saying, how does to take familiar names?
*  How does GPT-3 compare to GPT-4 in terms of capabilities, in terms of robustness?
*  And it appears that they are diverging.
*  But can you give me a little more kind of order of magnitude intuition for how to understand that?
*  Yeah, I mean, it's a difficult question to answer because these models don't just vary in scale.
*  They also vary in fine tuning.
*  So if we adjust varying model scale in the pre training regime, then very loosely, I would say, about capabilities and improving an order of magnitude faster than robustness.
*  So in order to actually see a scaling trend, we had to intentionally cripple the attack and make it weaker than it usually would be.
*  Because if we ran a full strength version of something like really coordinate gradient, it would just all the models would go from 100% accuracy to 0% accuracy.
*  But even if we run this crippled version, when we go from something like a 13 million parameter model to a billion parameters, we see maybe something like a 10% increase in robust accuracy.
*  So I would say you need to go several more orders of magnitude, sort of like a GPT-4 model size in order to get to full robust accuracy against this crippled version of attack.
*  But then we can, of course, just actually use a full strength version of attack.
*  And then GPT-4 will also be very vulnerable to these kinds of attacks.
*  So it seems like we need to be getting a sort of like GPT-7 or so before just the current crop of attacks we have stopped working, but then better attacks are coming out all of the time.
*  So whereas I expect that GPT-7 in terms of capabilities would be like really qualitatively quite different and a very capable and in some ways, scary model.
*  So from that perspective, it seems like capability is moving much, much faster than robustness.
*  But as you said, this is all without any kind of defenses.
*  So that could really change the picture here quite a lot.
*  And we did find GPT-4 much harder to break than GPT-3.5, even though the difference in scale is substantial, but it's not more than an order of magnitude, I would guess, in terms of parameter count.
*  And so a lot of that is coming from the safety fine tuning they've done, actually being reasonably effective.
*  Well, I certainly hope to see great success from this research agenda.
*  You've been very generous with your time today.
*  Is there anything else that we didn't get to that you want to make sure to mention before we break?
*  Yeah, I'll just mention quickly that, you know, if anyone in the audience is either looking to more actively work on these kinds of problems or know people who are looking for that kind of career shift, then my organization, FIIs, is hiring for a wide variety of roles, both on the technical side.
*  So we're hiring for an engineering manager, technical leads, research engineers, research scientists, but also on the more business operations side, we're looking to hire someone to lead some of our programs and events.
*  So, you know, do check out our website to find out more about our research or check out some of our open recruitment rounds.
*  Adam Gleave, founder of FAR AI, thank you for taking on the challenge of adversarial robustness and thank you for being part of the cognitive revolution.
*  Thank you for hosting me.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me on the social media platform of your choice.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work, customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it to use Cogrev to get a 10% discount.
*  Turpentine is a network of podcasts, newsletters and more covering tech, business and culture, all from the perspective of industry insiders and experts.
*  We're the network behind the show you're listening to right now.
*  At Turpentine, we're building the first media outlet for tech people by tech people.
*  We have a slate of hit shows across a range of topics and industries from AI with Cognitive Revolution to Econ 102 with Noah Smith.
*  Our other shows drive the conversation in tech with the most interesting thinkers, founders and investors like Moment of Zen and my show Upstream.
*  We're looking for industry leading hosts and shows along with sponsors.
*  If you think that might be you or your company, email me at eric at turpentine.co.
*  That's E-R-I-K at turpentine.co.
