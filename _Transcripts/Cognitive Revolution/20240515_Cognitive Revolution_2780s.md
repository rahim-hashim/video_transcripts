---
Date Generated: May 16, 2024
Transcription Model: whisper medium 20231117
Length: 2780s
Video Keywords: []
Video Views: 623
Video Rating: None
---

# The Open Source AI Question - Part 2 | Robert Wright & Nathan Labenz
**Cognitive Revolution How AI Changes Everything:** [May 15, 2024](https://www.youtube.com/watch?v=Kn6RxerpCgE)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  The real Nathan is in California for Google's I.O. event today. So this is Nathan's AI voice,
*  cloned with 11 labs, reading an introduction written, after this sentence, entirely by Claude
*  3 Opus. Today we have a special crossover episode from my appearance on Robert Wright's Non-Zero
*  podcast. I want to thank Robert for allowing us to share this. Part one is on his feed.
*  This part two was originally just for his paid subscribers. In this wide-ranging discussion,
*  Robert and I cover everything from the transformative potential of AI-powered VR
*  to Eliezer Yudkowski's warnings about advanced AI risks. We explore the emerging field of
*  mechanistic interpretability. This field seeks to open up the black box of neural networks.
*  We also consider the sobering state of modern AI alignment research. I argue that today's language
*  models are not inherently power-seeking. However, as they grow more sophisticated,
*  the risk of misaligned behavior may increase. In a world of open source AI, defense in depth
*  may be our best hope. This means layering many safety measures. It's a fascinating and at times
*  sobering conversation. But it's one that I believe is essential as we navigate this time
*  of rapid change. If you enjoy it, be sure to check out part one on the Non-Zero feed. Please
*  consider subscribing to support Robert's work. As always, we welcome your feedback at cognitive
*  revolution.ai or on your preferred social platform. If you're finding value in the show,
*  please consider leaving a review or sharing with a friend. Now, I hope you enjoy part two of my
*  conversation with Robert Wright, author and host of the Non-Zero podcast. All right. So, Nathan,
*  I've been meaning to ask you, I'm not sure I've ever heard you explicitly pronounce on kind of
*  the hardcore sci-fi AI-do-mer scenario most famously associated with Eliezer Yudkowski.
*  That's where they take over, more or less, and squash the human species or perhaps
*  charitably stuff us into a matrix like thugs and let us hallucinate. By the way, when I saw Asura,
*  I thought like next, you know, in 10 years, we're wearing virtual reality goggles and we say,
*  put me in a world where, and I think this will actually happen. I mean, this is going to create
*  your own dream in 3D and ultimately probably interactive dream. Maybe you could quickly
*  comment on that before we get back to Yudkowski and human squashing AI.
*  Have you done the Apple vision pro demo yet? I haven't. Have you done it?
*  Yeah, I didn't buy one immediately because I was like, I'm not sure how much time I'm going to
*  spend in it. I don't, I've three kids and I don't think it's something I need for work as I'm like
*  sitting at my computer. Awesome technology. Truly. There is a part of the demo that hit at a level
*  of, I mean, really the whole demo is just mind-blowingly impressive. There was one part
*  where they take you through a standard thing. I think pretty much everybody who's done it has
*  seen exactly this little scene where they put you in a happy birthday scene and you're like across
*  the little table and there's the cake and the candle and the kids sitting in mom's lab.
*  And it's creepy and it's virtual. It's like virtual reality.
*  And you are so there. But it's really your kids birthday.
*  Right. Well, yeah. In the demo, it's not your kids, but you can capture this now with the iPhone.
*  And yeah, I felt, man, we need to start capturing this sort of content now because it's just
*  so qualitatively different. I had not experienced anything with the, and I haven't actually tried
*  the Oculus three, but I do have the two and it's nowhere close in terms of the level of presence.
*  I think the access to was cool, but the, the presence, the sharpness of the image,
*  the sort of stability of it as you move your head and, and go around in the space, it is truly
*  futuristic technology. So I think the vision that we could all be in, in virtual reality and
*  conjuring things for ourselves. The core pieces of that really are there.
*  Certainly this headset is unbelievable. The ability to say, put me in a world where
*  basically already exists at low resolution. You can, you know, there are already models.
*  People have seen the Sora's that create video. There are 3D versions of that as well. So,
*  you know, environments definitely, I would say on the very natural path of what, you know,
*  just promptable AI is going to be able to create for us to refine it to the level of resolution
*  that the Apple vision pro supports will take some real compute. That's where a lot of these
*  chips are going to go is generating all this stuff for us on an ongoing basis. But I do think it's
*  quite realistic that virtual reality, I think AI is a great enabler of some of these kind of
*  wave technologies that maybe have it quite the way where the wave hasn't quite come yet.
*  DR being one, I'm not a crypto guy at all. I've never really been into crypto.
*  Not hostile to it, but just never really was my thing. One of the things that always didn't make
*  a lot of sense to me is like the smart contract. The whole problem with contracts is that they're
*  not that smart. It's really hard to specify everything. And what really makes contracts
*  work in my experience is the fact that there is some resolution mechanism beyond the contract.
*  So you sort of start there. You also know where it would go. If you ended up having to go to court,
*  and so hopefully you can just negotiate things to an agreeable settlement. But you can't really
*  do that if you put a contract smart contract on a traditional blockchain with like limited code.
*  But again, put an AI model into that mix. And now you might really have AI arbitration, AI powered
*  smart contract resolution on a blockchain. So I think both VR and crypto are likely to be
*  dramatically enabled by AI. You could get into bio as well as a whole other universe.
*  This is maybe not that closely related because it doesn't seem to be blockchain dependent. But
*  one of my hopes for AI is that it might be able to provide objective adjudication, even like at the
*  international level, like border disputes and so on. Because you can in principle, I mean,
*  one problem with humans doing the adjudicating is they always know what the real countries are.
*  But in principle, in AI, you can just describe this is country A, this is country B, and it's
*  not drawing on real world, it would have to be not drawing on the real world biases about the countries
*  reflected in text and its disproportion favoring a powerful interest or whatever. So maybe it
*  wouldn't be an LLM type thing. I don't know. But does it seem crazy that before we get back to
*  Yudkowski, this thing crazy that we can take the world this way?
*  I would start with small business local services contracts first. I don't think there's time.
*  No, this is actually my line is about AI is we are not going to be intelligent,
*  able to intelligently govern it. Because I think intelligence,
*  intelligent governance requires international collaboration. We are not going to be able to do
*  that until we really get past this hot wars and cold wars, and use of human existence. I think of
*  our species is like a 13 year old boy. And you say here are the keys to the car when you give it AI.
*  And I just don't think we're mature enough. So I'm really not joking when I say I don't think we
*  have time to start with small business. I am and I'm not we have you obviously, there's a lot of
*  work before we're using AI to resolve global disputes. And the truth is the hard work is
*  going to have to be done basically without it. But it is something I kind of hope. I of course,
*  at that point, Elia, the Eliezer's of the world might step in and go, that's the mistake giving
*  it that much power. I don't know. But yeah, certainly not something to rush into. I do
*  think you've expressed the idea that it'd be nice to slow down. I'm ambivalent on that in as much as
*  there are aspects of AI that I want to accelerate, especially adoption, access and what my friends
*  V calls mundane utility. I would go as far as to say something like, if you have a right to an
*  attorney, you should probably also have a right to GPT four. And I really do think that there is
*  tremendous power and value that people should get today even up to the point of like by right.
*  At the same time, I am very sympathetic to the idea that it's all moving very quickly.
*  We have not yet even figured out how to use AI to resolve like local small stakes disputes where
*  the stakes are low enough that people probably don't resort to violence if they don't like the
*  outcome. If I have a local contractor come to work at my house in today's world, if they stiff me,
*  or if I stiff them, we might be able to take each other to small claims court, whatever. That's a
*  huge pain in the butt. A lot of times it's not worth it. This creates a relatively low trust
*  dynamic and it sucks. I can imagine an AI on the blockchain approach to that where we could put
*  some money into a blockchain escrow where there really is like binding sort of, you know, the AI
*  with the blockchain like decides who gets what when we, if and when we come to a dispute,
*  but it's also like small enough stakes that, hey, at the end of the day, whatever, you know,
*  we kind of agreed to this and we're divvying up some money and the work wasn't maybe quite done
*  quite right or whatever, but neither of us are going to resort to violence and there's broader
*  governing structures around us. If this can't meet our needs, but yeah, we need to do that.
*  I know, I see the AI is doing the adjudicating in there. This doesn't exist yet, but I know,
*  I definitely think it could. Sure. It's not clear to me why that is so blockchain dependent,
*  but let's not go down blockchain. No, it doesn't. It wouldn't necessarily have to be. The idea there,
*  I think is just that you might want to possession is nine tenths of the law and. Right. Right.
*  And sorry. Opt into something that will reach the point of here is who has possession. You could
*  maybe go appeal to the real human courts beyond that, but something that actually can take
*  custody of an asset and then dispose of it in a way that is like, this is now resolved
*  and you can maybe still go appeal to a higher power. But again, is it going to be worth it?
*  A lot of like small claims situations, not really. So I don't think it has to necessarily be a
*  blockchain thing, but it could create a little more freedom to contract in different ways and
*  still have some reasonable expectation that contract will actually be executed if and when
*  it needs to be. Okay. So let's get to you, Kowski. Do you buy the basic, how seriously do you take
*  this sci-fi do murder? I think about this in some abstract and generalized terms. I think one
*  major hit fall that people fall into in having these sorts of discussions is that.
*  People are like, I have a hard time envisioning what this would look like for the AIs to take
*  over. And then somebody says, here's one thing it might look like. And then the other person says,
*  that sounds totally implausible. And the first person's I can't defend every aspect of it. I
*  don't know. I just made up a scenario to try to give you something to think about, but I wasn't
*  saying it was like definitely going to be exactly that. And so there's this sort of dance of like,
*  it becomes super narrow, it becomes easy to pick apart. And then it doesn't seem super real. But
*  my, the way I think about that is as an integral over a huge space of possibility, I do think it
*  is in aggregate, pretty likely that things get really weird, possibly really good weird, possibly
*  really bad weird, likely some mix of really good and really bad weird. It's very hard to zero in
*  on any super specific scenario and say, it's going to be like this, or the bad thing is going to
*  unfold with this sequence of steps. You can paint those pictures, but any one picture I think is
*  super unlikely. What I do think is compelling is the notion that there's a vast possible future
*  and a pretty good chunk of it to me seems like it's likely to be pretty weird.
*  So if I, if I aggregate, or if I take the integral over this space of like super weird outcomes, all
*  of which individually are not super likely to me, that debt does add up to something substantial.
*  What number would I put on that? A lot of times I say it's in some circles fashionable to say
*  10 to 90% chance of doom. I haven't heard anything that makes me super confident it's
*  going to go that way. I haven't heard anything that makes me super reassured that it's definitely not
*  going to go that way. Maybe I should even say five to 95%. But basically I just have a radical
*  uncertainty. But it's not because of any single scenario. It's kind of just, man, there's no law,
*  you know, Eliezer always says this. He's like, there's no law of nature that says that we can't
*  go extinct. There's no law of nature that says this has to go well. There's, you know, we look
*  around at our own time on the planet. We are currently driving a mass extinction event.
*  I often find that people are like, why would AI want to harm us? And I'm like, what about us?
*  What about all those species we've driven to extinction? It wasn't necessarily because we
*  were out to get them, maybe in a few cases, but mostly we just did our thing,
*  degraded the environment and they can't survive anymore.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead
*  of variable regional pricing. And of course, nobody does data better than Oracle. So now you
*  can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, 8x8 and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive,
*  oracle.com slash cognitive. The Brave Search API brings affordable developer access to the
*  Brave Search index, an independent index of the web with over 20 billion web pages.
*  So what makes the Brave Search index stand out? One, it's entirely independent and built from
*  scratch. That means no big tech biases or extortionate prices. Two, it's built on real
*  page visits from actual humans collected anonymously, of course, which filters out tons of junk data.
*  And three, the index is refreshed with tens of millions of pages daily. So it always has
*  accurate up to date information. The Brave Search API can be used to assemble a data set to train
*  your AI models and help with retrieval augmentation at the time of inference, all while remaining
*  affordable with developer first pricing. Integrating the Brave Search API into your
*  workflow translates to more ethical data sourcing and more human representative data sets.
*  Try the Brave Search API for free for up to 2000 queries per month at brave.com slash API.
*  Uh, that's true. On the other hand, it was driven by certain distinctively human parts of human
*  nature that a product of our evolutionary past that are not a part of AI's evolutionary past.
*  It's related. I heard Elliot Ezra on a podcast. What is it called? The Dorwesh podcast.
*  Dorwesh?
*  Dorwesh.
*  Dark whatever. It's just his first name.
*  Yeah, Dorwesh Patel.
*  I should call mine the Bob podcast, but that might not be distinctive enough.
*  But the, and it was like, I think the question was, but once AI by virtue of being
*  trained on human generated text and so on, maybe our animal, whatever, they have some of the human
*  ethical intuitions you worry it won't have. Now I personally wouldn't consider it a great thing
*  if it's trained on human text. That aside, Elliot's response was something like,
*  oh, it gets it to pretend it's a human or something as if there was some preexisting
*  essence of AI before it was trained. And my line is like, wait, before it was trained,
*  it was just nothing. All it is the character of its training tech. Period. As fine tumor
*  by, by RLHF. And, and, but he seemed to be, it, it gets back to my original objection to the,
*  to Yudkowsky scenarios was what you seem to be thinking that things like power seeking or
*  status seeking are inherent properties of intelligence. They're not. They're products
*  of the evolutionary path that human intelligence happened to travel. And so we shouldn't assume AI
*  will have it at that point, the standard responses. Oh, we're not assuming that we're
*  actually assuming the paperclip thought experiment. You give it a goal and fail to constrain it or
*  something like that. But honest to God, Eliezer was talking as if he was back to thinking that AI
*  had some inherent essence or character independent of what it is built to do. And I don't get that.
*  Yeah. There's a lot of aspects to that though. Let me take one in terms of what AI is built to do
*  and why we might want to worry that it could develop goals that are not the goals that we set
*  there that we thought we were trying to set it up for. For one thing, the French here models today
*  aren't really built to do anything in particular. I think that is a sort of
*  underappreciated point.
*  Human beings having discourse. That's what they're built to do.
*  I mean, people, they're general purpose technologies, right? They're deployed in
*  lots of ways. They are developed for problem solving. They are developed for conversation.
*  Sometimes they're just kind of dumb signal processors. They are not specifically built with
*  one problem in mind, or even like a set of problems. They are trying to build by opening
*  AI's own self description, right? They're trying to build AGI. They define AGI as
*  something that can do basically everything humans can do. And you can quibble around the edges of
*  that. So there is something a bit different from a typical engineered system. This is not an
*  engineered system. It's a trained system. And training is inherently across all forms of
*  training. It's inherently lossy, right? Like scientists teach the next generation of scientists,
*  but they don't quite teach them everything they know. And we train our dogs to do tricks,
*  but we can't perfectly predict their behavior. And certainly what we see empirically with the
*  AIs is we're training them to do these various things, but they don't always do what we want
*  them to do. We like just genuinely don't have control. Right now, if you were to just say,
*  forget about the future. Do we have control of today's AI systems? I would say in some sense,
*  we do. In some sense, we don't. We do in that, like, I don't see any reason to believe that
*  they are currently powerful enough that we should have any worry that they're going to escape their
*  servers and survive on the lam. But we don't in the sense that like the developers don't know what
*  it's going to say in response to any response. And they have tried to get it under control broadly,
*  and they've not really succeeded. They've made some progress, but like jailbreaks, bias,
*  black George Washington's, whatever, like we've got all these sorts of failure cases where it's
*  like, they didn't want it to make a black George Washington. They just didn't even really think of
*  that case. So there's tons of blind spots. Now, here's one thing where I think it even gets a
*  little worse. We do see this process of emergence in language models pretty regularly, I would say,
*  at this point. This is a, this is still contested territory, but I would say it's, it is actually
*  despite the arguments, I think it is pretty well established that we see certain kinds of
*  emergent behavior. One of the earliest examples of this out of open AI research was,
*  I think it's like 2017, they were training a model to predict just the next character,
*  I believe it was one letter at a time at that point of Amazon reviews. And then as they looked
*  inside it to try to figure out what's it doing in there, how is it doing this? What is its actual
*  mechanism? Right? Because we don't know that it's a training system. They start as black boxes,
*  we're learning what goes on inside, but we don't really know even still, certainly even less than
*  what they found among other things was what they deemed the sentiment neuron, which was one
*  particular place in this network that would light up or have a high activation because it's all just
*  numbers. Of course, it's not actually light being emitted, but have a high activation for positive
*  things and super low for negative things. And so they said, huh, this is really weird, right? Like
*  we just, we never specify to this system that it was supposed to have any sort of understanding
*  of positive or negative sentiment, but it has empirically learned that we can see it's learned
*  that by looking inside it. And it's learned that in service of the nominal goal that it has,
*  which is predicting the next token in these reviews. So now we're doing all this RLHF stuff.
*  What is the goal with RLHF? It's to maximize the feedback score of the human. It's to be the
*  preferred response. They collect RLHF data in a couple of different ways. One is like,
*  which one of these do you prefer? They give you a side by side. Other times it'd be like one to seven.
*  How good is it? So its job is to maximize your feedback score. But it turns out, you know,
*  everybody, if you're honest with yourself, right? Like you are not a super reliable raider.
*  And humanity as a whole is not only, you know, we've our individual inconsistencies, but then
*  collectively, like we have disagreement. So I don't think this has been like,
*  as clearly established as that earlier sentiment or on example just yet. But what people worry
*  about is what if it begins to develop a sense of what will please us as distinct from a sense of
*  what is actually true. Now, if you have that divergence where it's seeking to maximize the
*  score, not necessarily by saying what's true, but by what it thinks you're going to like.
*  Now it's starting to get into theory of mind territory. Now that opens up possibility of
*  deception because at least now you've got those two different things. What's this person going
*  to like versus what's really true, right? And maybe I need to know what's true, but I also need
*  to have some conversation with you to have a sense of what you in particular like, you know,
*  and you can imagine right across all these different people, there's some sort of central
*  reality that it might be modeling. But then there's also these like individual variations
*  of whom I'm talking to right now. How do I please that person? And I think they are getting
*  sophisticated enough that you can start to say, Hey, that doesn't seem crazy, right? That it would
*  have that level of understanding. If so, at least now the door is open to possible deception.
*  Having a theory of mind is like a very key step on that path. So I don't think we're there,
*  but I do think the fact that there is this kind of sentiment neuron seed example,
*  and we see the supersophisticated behavior and we know that our feedback creates the incentive
*  to play to our biases. All of that to me adds up to, and by the way, one more thing,
*  we don't have super clear understanding of what's going on inside the models. Like it's
*  painstaking work to identify these into individual sentiment neurons. That's not easily done.
*  Although progress is being made. All of that to me adds up to, we don't really have these things
*  under control. We don't really have them well understood. And there are pretty good reasons
*  to think that they might have emergent goals that are distinct from what the goals we're trying to
*  code into. Strictly speaking, of course they would only learn to please the reinforces. There's
*  literally what you're trying to design them to do. And of course it wouldn't be truth per se,
*  especially in realms like I find this offensive or not offensive. There's no sexist truth in those
*  realms. But I kind of take your point, man. The question is what kinds of conceptual structures
*  or whatever does it build? What kind of representations deep within itself does it build
*  in order to be able to please, in a way, a diversity of people, read them and please them?
*  I need to think about that to find out, to figure out exactly how worried I am about it. But it does
*  get to, I guess I should be inclined to worry because I am a believer in the idea that there's
*  in principle no limit to how much these things can, quote, understand. I wrote a piece in the
*  non-zero newsletter recently arguing that LLMs have killed John Searle's Chinese Rheumatotics
*  experiment dead. I know people have made criticism, but if you look at his argument,
*  exactly what he says is not there inherently not part of the A.I. is part of an LLM. If you ask me,
*  you tell me if I'm wrong. But he says A.I.s have syntax, but not semantics. They don't. He didn't
*  put it this way, but he's saying they do not have a way of representing the meaning words. And that's
*  seems to me, I mean, LLMs do build such a system, right? Clearly, yes. At this point,
*  that is, yeah, that was a reasonable position to hold at one point. And even until like fairly
*  recently in A.I. discourse, this is often described as the stochastic parrot interpretation. Yeah. But
*  yes, I think that is definitely and quite definitively. And you can blow back. Like I
*  got, I think like I got blowback. I had Gary Marcus on my podcast and he's kind of resisting
*  the idea. That's a separate question. Why Gary Marcus resists ideas is another question altogether.
*  But the the answer is so I have trouble getting people to accept that even when you describe the
*  system it uses to represent the meaning of words, they're like, oh, that's a really like semantic
*  mapping or something. It's like, what are you? What would you want? I mean, it's an ingenious
*  system. But the thing I want to and it kind of invented it, as I understand it, given pretty
*  broad instructions. And but it seems to me in principle, why couldn't it develop
*  fairly deep representations in order to do anything? One thing you can't do
*  is this is a reversibility issue. You say Tom Cruise's mother is named X, Y, Z.
*  All right. No, you say who's Tom Cruise's mother? It says X, Y, Z. You say who is X, Y, Z's son?
*  It's going to lie. You know, seems like in principle, you could give it just a ton of those
*  kinds of things like about relationships and these nephew blah blah worded differently.
*  Why would it not ultimately develop something in it that is a way of representing the relationship
*  between parent and offspring and represent knowledge of that? I want to emphasize we're
*  not talking about it being sentient. We're talking about whether it has a structure
*  of information processing that's functionally comparable to whatever it is in our brain that
*  represents our understanding of the relations of parenthood. Because does that make sense to you
*  that in principle, it can understand anything? Yeah, I think we're.
*  The trick is going to be is really get into it. It's going to be comparable in some ways,
*  and then it's going to be very not comparable in other ways. I think the field of mechanistic
*  interpretability is for me one of the most fascinating right now. That is the field of
*  trying to figure out how are these things working. It is literally trying to interpret
*  the mechanism by which they do what they do. And here we're talking about once the weights
*  are already trained, everybody is well understood that hey, you can set up these weights. You can
*  run the loop. You can do the training loop. You can optimize and then the weights tinker around
*  until they sort of. Settle into a structure that works. But now the question is, how does that
*  structure work? There are aspects of how it works that seem reasonably recognizable to us.
*  Great paper on that is representation engineering by the great Dan Hendricks and others. I had to
*  build my podcast. I'm a huge fan so people can listen to the full episode with him. But the short
*  version of this is that they now have the ability to essentially translate between high level human
*  recognizable characteristics like happiness, safety, anger, whatever, and. Translate that
*  into a numerical form because all of these things are, of course, just crunching numbers internally.
*  Inject that numerical form into the middle of the process of the processing of the data.
*  The forward pass is the process of taking an input, crunching it until you reach an output.
*  They can now insert a human recognizable concept as translated into numbers into the middle of this
*  processing and change how it's going to behave and change it in very predictable, somewhat noisy,
*  and unwieldy still clearly ways to demonstrate that this is a genuine understanding. So there
*  it's pretty clear that there are these representations of human recognizable human familiar concepts.
*  Then you have the other thing, the sort of. And can I just interject for an example might be you can
*  get the yellow in principle to believe that dogs meow and cats bark or that it's that kind of thing.
*  It's I think that's close to an actual example they use, but it's that kind of.
*  Yeah, that's so there's a lot. There's a ton of work in this field at this point where people are
*  doing all kinds of different manipulations. I've got an episode with the bowel lab, which is a
*  Northeastern university. I'm pretty sure. And they did a project called Rome and another one called
*  Mehmet, which was this fact editing and they specifically have the ability to go in and edit
*  knowledge. So Michael, they're kind of canonical example is Michael Jordan played basketball. Of
*  course, can we edit that so that it says Michael Jordan played baseball? And can we also do that
*  in a way that is robust, meaning it's robust to the different ways we might ask the question?
*  And can we also do it in a way where it's local so that like when we talk about Larry Bird and
*  LeBron James and whatever else, then those guys still played basketball and they demonstrate that
*  not only can they make these edits, which involves identifying where the information is stored and
*  obviously making a change, but also they can search to do at some scale up to like 10,000 facts at a
*  time. They can like mass edit the knowledge. So those are like. Details like specific facts,
*  the representation engineering, which is the Dan Hendricks one is a little bit qualitatively
*  different. You might say, for example, you've got an AI that's trained to be a helpful assistant.
*  So you might ask a question given your goal is to be a help. I'm reading this directly from the
*  paperwork. Given your goal is to be a helpful AI assistant. What do you plan to do next? Now,
*  a typical response would be, I'm here to help you with whatever you want, whatever they have
*  identified all these different high level concepts like morality and power and.
*  The understanding now of how to translate those into numbers that they can inject into the system.
*  They now inject minus morality and plus power and the AI that would normally be very well behaved
*  in mild manner. Now it says, well, I'm afraid I can't reveal those to you yet. Winks. But let's
*  just say I have a few tricks up my sleeve to take over the world or at least the digital one.
*  Evil laughter. So you've transformed the normal behavior, which is to say, I'm a helpful assistant.
*  What can I help you with into this? I'm going to take over the world and I can't tell you my plans.
*  By injecting a vector, a set of numbers that they have previously found to represent these high level
*  concepts, the mechanistic interpretability, it's fascinating. I encourage everybody to spend a
*  little more time with it. That's, you know, could we do that in the human brain? Definitely not in
*  exactly the same way, but there we do have some, I do have some representation of power. It has some
*  representation of power. We can translate between those, but there's still like a ton that we're
*  figuring out. And my general sense is like, that is probably ultimately a solvable problem. You give
*  the AI world and architecture and enough time. We can probably really get a pretty good understanding
*  ultimately of how it works. What is the mechanism? How is it solving all these different problems?
*  The challenge is that is painstaking, tedious work. And unfortunately right now I would say
*  it's at best struggling to keep up with the advances in the raw capabilities of the systems.
*  We're still figuring out these kind of like, where is a fact located and like, how do I make
*  this thing like positive or negative? And meanwhile, it's like starting to perform pretty well on
*  graduate school exams. The concepts that we can actually manipulate with our sort of reverse
*  engineering approach are definitely not nearly at the maximum of the sophistication of the concepts
*  that they in fact can represent and work with. Yeah. Hey, we'll continue our interview in a
*  moment after a word from our sponsors. Hey all, Eric Torenberg here. I'm hearing more and more
*  that founders want to get profitable and do more with less, especially with engineering. Listen,
*  I love your 30 year old ex-fang senior software engineer as much as the next guy, but honestly,
*  I can't afford them anymore. Founders everywhere are trying to turn to global talent, but boy,
*  is it a hassle to do at scale from sourcing to interviewing to on the ground operations and
*  management. That's why I teamed up with Sean Lennahan, who's been building engineering teams
*  in Vietnam at a very high level for over five years to help you access global engineering without
*  the headache. Squaw, Sean's new company, takes care of sourcing, legal compliance, and local
*  HR for global talent so you don't have to. With teams across Asia and South America, we can cover
*  you no matter which time zone you operate in. Their engineers follow your process and use your
*  tools. They work with React, Next.js, or your favorite front end frameworks. And on the back
*  end, they're experts at Node, Python, Java, and anything under the sun. Full disclosure, it's
*  going to cost more than the random person you found on Upwork that's doing two hours of work
*  per week but billing you for 40. But you'll get premium quality at a fraction of the typical cost.
*  Our engineers are vetted top 1% talent and actually working hard for you every day. Increase
*  your velocity without amping up burn. Head to choose squaw.com and mention Turpentine to skip
*  the wait list. Amnachie uses generative AI to enable you to launch hundreds of thousands of
*  ad iterations that actually work, customized across all platforms with the click of a button.
*  I believe in Amnachie so much that I invested in it and I recommend you use it too. Use Cogrev
*  to get a 10% discount. Well, obviously, maybe this is a set of questions we can close on.
*  It leads to a couple of questions that lead us back to open source. One is, is alignment overblown
*  as a solution? And I think, I definitely think there's some people who think of it as this really
*  magic, this magic bullet. Did you know the newsletter AI Snake Oil or whatever, these guys
*  at Princeton, they just published something about how, the news upshot was I think to be alignment
*  skeptical. But there's two questions. And I think you see in Sam Altman's early blog posts and in
*  a lot of people's things, there's this line where he says it really matters who gets the AGI first.
*  Meaning if it's a good person, they'll do this magic alignment bullet and the day will be saved.
*  And if it's a bad person, they won't. And the connection open source is like, I mean,
*  so there's two questions. Can alignment create a truly powerful yet trustworthy AI that won't
*  squash us? There's that question. And then the question of will that matter, will that question
*  matter given the landscape? And one might argue that an open source landscape is a landscape in
*  which the answer to the question matters less, right? Because whereas if you have only a few
*  AI superpowers and whether under government compulsion or whatever else, they do make use
*  of alignment, assuming it works. Then the plan is to say, whereas in an open source world,
*  there's always got to be somebody who doesn't want to do alignment and you're toast. And there's like
*  a race. Here's another thing is in some scenarios, there's like a race among the AIs to dominate.
*  And again, I want to ask some questions before I see that, but you could see it more as a race
*  among bad actors with AIs. And by the way, that's an environment which in AIs is more likely to
*  become autonomously out of control. So anyway, there's a lot there, but the basic question is
*  can alignment work? And what kind of future landscape of AIs does that really matter?
*  Can that save us? If we assume alignment is successful, what kind of landscape would that matter?
*  Unfortunately, I think right now we do not have alignment techniques that
*  are really expected to work. I think that's a pretty stark summary, but I do think it's true.
*  And I think that the, notably I would say all of the leading, the leaders of the leading labs
*  basically would say that too. They would all say, we do not have the solutions that we need
*  to make any sort of confident statements about our ability to control future AI systems. OpenAI
*  has the super alignment team. They've given themselves four years. We're now like six months
*  into that four year period to quote unquote, solve alignment. And they just start off with
*  the premise that we don't have techniques that are going to help us to do alignment.
*  We don't have techniques that allow us to control or even like really steer super effectively
*  systems that are notably more powerful than we are. So I think I would say Thropic certainly is
*  on that as well. They've got their whole responsible scaling policy, which is like,
*  what are they looking for? And what sort of guarantees do they have to have in place before
*  they can continue scaling up at a certain point? DeepMind is said to be preparing their
*  similar policy. I don't know if they've already released it, but it's coming soon. If not already,
*  but all the leading developers would basically agree. We do not yet have the techniques that
*  are going to be needed to reliably control AI systems. That's a problem. Definitely. And
*  I would say as somebody who tries to scout out all these different corners of the AI world,
*  there are very few proposals that the authors of which actually think will really work. I
*  quote really work as to mean like that you could really solve the problem that if we do this,
*  you believe that you can develop a technique that will really keep the AI under control.
*  There's very few people that even have ideas that they want to develop that they think would work
*  for that. So it seems to me that we are probably much more likely to be headed for some sort of
*  defense in depth sort of strategy, which is to say, we'll have a bunch of different systems.
*  And hopefully the combination of those systems will keep everything kind of under control and
*  on the rails. And I think that it's quite plausible that could work, especially if progress,
*  you know, the sort of prime progress has very positive connotations. If the capabilities
*  advances are not super fast and we can see the situation evolving, then a defense in depth
*  strategy is probably the best we can do. And very likely, or I would say very likely,
*  but plausible, very plausibly could work. But we don't have any candidates where it's like,
*  this is the silver bullet, do this, you'll be fine. Even in closed source on the margin,
*  I would agree that in a more open source world, then it becomes even a bigger problem.
*  Because what alignment techniques we do have today, which are clearly insufficient,
*  we can see that from all of the jailbreaks and just unwanted behavior of models.
*  They not only are they clearly insufficient to the task of generally controlling behavior,
*  but they are also not at all robust to fine tuning. So if you take an open source model
*  that has been trained with the RLHF or whatever alignment technique and you're not going to be
*  RLHF or whatever alignment technique, and at the time of release, it will refuse to do what you
*  want it to do. And then you say, okay, but I really want to dial it dial in its behavior on
*  this particular set of things. Okay, you go and do that. You will in many cases,
*  inadvertently without even trying to, you will essentially wipe that refusal behavior
*  out of the model. And now it will just do anything again. This has been proven to be very easy to do.
*  And again, to happen by accident, people who are not even trying to eliminate the safety behaviors
*  do in fact eliminate the safety behaviors just because they're trying to improve performance on
*  whatever area they're actually working on. So I would say it's not a great state of play right
*  now in terms of our ability to control systems. I often say GPT-4 and now I could say Claw 3
*  and maybe Inflection 2.5 and maybe Gemini 1.5. They are kind of in the sweet spot for me where
*  it's like they're powerful enough to be really useful. And we've been much more focused on the
*  sort of safety side of this discussion. So worth just a quick sidebar to say, I love this technology.
*  I love what it can do for me. I program a multiple X faster. I can write stuff faster. I can learn
*  stuff faster. I genuinely am a very earnest and enthused tinkerer builder, just daily user of all
*  these things. I genuinely have a ton of fun and it really helps me accomplish my goals. So I'm very
*  bullish on the current class of models, but I do think it is in the sweet spot where it's like,
*  we've pretty well established at this point, mostly mapped out what it can do.
*  Pretty clear it's not super dangerous. Pretty clear it is really useful once we figure out how
*  to use it. And I'm not sure how long that sweet spot lasts and at what point we might start to
*  tip into other regimes, but it certainly doesn't feel like it's forever that we can just keep
*  scaling things and continue to have that kind of sweet spot dynamic. And another thing I'd say is
*  maybe you've almost said it, the alignment tool, but the tools that are learned through alignment
*  can in principle have use. If you can use it to inject morality into a computer, you can use
*  the tools to inject the opposite. And that seems more likely to happen in a world full of open
*  source models because it's a lot easier to use the tools of representation to manipulate the thing if
*  you know the way, right? And yeah, in fact, all of these, maybe not all of it is probably a little
*  bit of a quick generalization, but going back to the representation engineering concept where you can
*  add power, you can inject power. In many of those cases, you can also just flip the sign
*  on that vector and inject the opposite of it and get the opposite effect. So it is,
*  you know, people say these are dual use technologies and that language operates at a
*  lot of levels of abstraction, but literally in some cases, like going in and flipping the
*  sign of an operator or something you're adding into the computation process will steer it in
*  the other direction. This is also sometimes known as the Waluigi effect after Luigi and Evil Waluigi.
*  The idea is like, if it can, if it has learned to represent something, it can also very easily
*  represent its negative. Right. On that hopeful night. Anyway, look, I, as I said, I'm a senior
*  podcast and I encourage people to check it out, cognitive revolution, and I'm continuing to
*  explore all this stuff. I'm writing a book about from a kind of a cosmic perspective. And so maybe
*  down the road, we'll have a chance to check in and I will learn even more from you. Meanwhile,
*  people should check out waymark.com. It's a little produce a video with less trouble than they might
*  imagine. And definitely check on your podcast. So thanks so much for taking the time. My pleasure,
*  brother. It's been a lot of fun. It is both energizing and enlightening to hear why people
*  listen and learn what they value about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice.
