---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 5629s
Video Keywords: []
Video Views: 1643
Video Rating: None
---

# AI open letter debate, pausers + what scares us w/ Anton Troynikov, Flo Crivello+ Nathan Labenz
**Cognitive Revolution "How AI Changes Everything":** [April 04, 2023](https://www.youtube.com/watch?v=p6T1QCen9YE)
*  I've been thinking about basically nothing but GPT-4 safety for the last six months since doing
*  the intensive red teaming. I came out of that feeling like it is safe to deploy, but really
*  only because it's limited in power. They have created something that is awesome, it is super
*  useful. Its power though is still finite. It's approaching human expert level in many things,
*  but it's not crushing human genius in anything as far as I'm aware. In all of my testing,
*  I would say I never saw anything that I truly came away feeling like, man, that is genius,
*  like that is next level. That's like that, I don't know the number, but like go move 37 or whatever.
*  I didn't see anything like that from GPT-4. I saw a ton of stuff that was just like, oh my God,
*  it will do anything you ask it. Even as they've really tried super hard, and I do appreciate
*  in a sense the six month pause that OpenAI took between finishing training and launching the thing
*  to try to get it as under control as possible. But even still in the launched version, there are
*  many problems. I've reported a few from my original red teaming that still work, meaning like
*  the AI still does the bad thing that I'm asking it to do with the exact same prompt that I used
*  in the red teaming. That just goes to show that they have cleaned it up a lot. The most extreme
*  things, violence, just outright depravity, they've largely got that under control. But more subtle
*  things which are nevertheless obviously harmful do remain open. My synthesis of all that is like,
*  I do think it's getting to be dangerous to start to scale beyond where we are. I do think if we
*  created something that is genuinely superhuman intelligent, we should expect that to bring real
*  danger. We are close to that. We just don't know how to control it. That overall recipe to me is
*  we should proceed with extreme caution. Hello, and welcome to the Cognitive Revolution,
*  where we interview visionary researchers, entrepreneurs, and builders working on the
*  frontier of artificial intelligence. Each week we'll explore their revolutionary ideas,
*  and together we'll build a picture of how AI technology will transform work,
*  life, and society in the coming years. I'm Nathan Labenz joined by my co-host Eric Torenberg.
*  Before we dive into the Cognitive Revolution, I want to tell you about my new interview show,
*  Upstream. Upstream is where I go deeper with some of the world's most interesting thinkers
*  to map the constellation of ideas that matter. On the first season of Upstream,
*  you'll hear from Mark Andreessen, David Sachs, Balaji, Ezra Klein, Joe Lonsdale, and more.
*  Make sure to subscribe and check out the first episode with A16Z's Mark Andreessen.
*  The link is in the description. Hi, everyone. I appreciate your feedback on recent episodes,
*  your comments, and the limited quantitative data that we can see suggests that you do want to hear
*  more about important AI issues in a timely fashion, in addition to our usual interviews with builders.
*  With that in mind, today we're sharing a discussion featuring some familiar faces,
*  returning guests Flo Crevello of AI Assistant Lindy.ai, and Anton Tornikoff of Embeddings
*  Database Chroma. We'll be talking about the biggest AI topic of the week, namely the open
*  letter published by the Future of Life Institute, which calls on AI labs to immediately pause
*  for at least six months the training of AI systems more powerful than GPT-4. Observing that,
*  quote, contemporary AI systems are now becoming human competitive at general tasks and lamenting
*  that, quote, recent months have seen AI labs locked in an out of control race to develop and
*  deploy ever more powerful digital minds that no one, not even their creators, can understand,
*  predict, or reliably control. The authors argue that, quote, having succeeded in creating powerful
*  AI systems, we can now enjoy an AI summer in which we reap the rewards, engineer these systems for
*  the clear benefit of all, and give society a chance to adapt. The authors note that they do
*  not wish to pause AI development in general, just the, quote, dangerous race to ever larger,
*  unpredictable black box models with emergent capabilities. They hope to see the pause used
*  to develop shared safety standards and protocols, to set up new oversight and governance structures,
*  to increase investment into interpretability and other safety research, and to implement various
*  other AI preparedness measures. Notably, the authors, quote, OpenAI's technical report for
*  GPT-4, which states that, quote, at some point, it may be important to get independent review
*  before starting to train future systems and for the most advanced efforts to agree to limit the
*  rate of growth of compute used for creating new models. Ultimately, the authors say, we agree,
*  that point is now. To date, more than 50,000 people have signed the letter, including prominent
*  computer science and technology leaders such as, Joshua Bengio, University of Montreal professor
*  and winner of the Turing Prize, known as the Nobel Prize for Computer Science. Stuart Russell,
*  a legendary professor of computer science at Cal Berkeley and author of a popular AI textbook.
*  Elon Musk, who needs no introduction. Steve Wozniak, the co-founder of Apple. Yuval Noah
*  Harari, professor at Hebrew University of Jerusalem and author of influential books,
*  Sapiens and Homo Deus. Imad Mostak, CEO of Stability AI. Andrew Yang, presidential candidate.
*  John J. Hopfield, Princeton professor and inventor of associative neural networks.
*  Connor Leahy, CEO of Conjecture. Evan Sharp, co-founder of Pinterest. Chris Larson, co-founder
*  of Ripple. Craig Peters, CEO of Getty Images. Jeff Orlowski Yang, Emmy-winning filmmaker. Max Tegmark,
*  MIT professor of physics. And Gary Marcus, NYU professor and noted AI skeptic.
*  There are also at least three research scientists from DeepMind, Victoria Krakowna,
*  Zachary Kenton and Ramana Kumar. I take this moment to read through some of these prominent
*  signers because I think it's worth emphasizing that contrary to some analysis, it's actually
*  quite a diverse and well-credentialed group, including people who've historically been
*  enthusiastic about AI alongside people who've been consistent skeptics. It also demonstrates
*  quite clearly the concerns about AI are not just for those who don't build or don't work directly
*  with AI systems. While I'm personally extremely enthusiastic about AI technology and the progress
*  that it can unlock in the next few years, I am also sympathetic to the pause. And for me,
*  it was hands-on experience with an early version of GPT-4 that caused me to see AI risk as a short
*  term issue. Coming up in April, we'll have Jan Tallin, co-founder of Skype and board member at
*  the Future of Life Institute, which published this letter, on the show to discuss these issues from
*  a safety perspective. But for now, I hope you enjoy this discussion with Flo and Anton about
*  the pros and cons of a potential pause on large scale AI training. Cool. Well, thank you guys for
*  agreeing last minute to do this. It's a timely episode and yeah, it'll be a lot of fun.
*  Let's do it.
*  Sweet. Well, Flo, Anton, Nathan, welcome to a moment of zen.
*  Thanks, Eric. Thanks for having us.
*  Yeah. Happy to be here.
*  So why are we here? Anton, why don't we start by getting your perspective on sort of the pause
*  versus not pause conversation as it relates to the news that was released this week?
*  So the pause versus not pause conversation. I mean, are we still talking about a pause or are
*  we talking about airstrikes on data centers? What are we really discussing?
*  One step at a time.
*  We'll build up.
*  Yeah. I mean, look, there's this open letter
*  signed supposedly by many people. I don't know whether to believe some of those signatories
*  are actually on the letter, given that I would have expected people like Sam Altman and
*  Elon to announce themselves that they had signed the letter rather than random Twitter randos
*  saying they had signed it.
*  Ja Rule did sign it. I did check with him and the famous rapper Ja Rule did sign it.
*  Okay. Well, that's good.
*  The most important signatory.
*  That's good to know. Jan LeCun was said to have signed it and he refuted this. He said, no, I
*  didn't. So look, I think this is a confusing thing because on the one hand, if you are a committed
*  AI doomer, then I don't know what six months is supposed to buy you.
*  If you are of the inclination that things are fine, then I don't know, six months maybe lets
*  you catch up on some research and actually know what's going on today as opposed to constantly
*  being behind that might be useful. But I think the sort of the least charitable reading of what's
*  going on with this letter is certain organizations find themselves in a dominant position right now.
*  And they are perhaps using the shield of safety to attempt to cement that position versus other
*  competitors. It's very convenient that the call to stop for six months comes just now instead of
*  previously or later. I don't see that anything in the past two weeks has changed so much.
*  So we have the release of GPT-4 and it's been around for a little while. Why wasn't the letter
*  ready to go already then? I don't know. I have a lot of open questions around here.
*  So the question there is, is this really, or the subtext is, is this a strategic move to kind of
*  prevent fast followers, so to speak? Is this regulation is often beneficial to incumbents
*  and you're suggesting that it's possible that this is the case?
*  I mean, one has to ask themselves, you know, keep on under any sort of big significant change,
*  right? It's difficult to attribute to malice what could just be random fluctuations and the
*  reality of history is often random things combined into a convenient narrative. But it may not be
*  what's happening here, but I stay paranoid about things like this. And I think that's the case.
*  Given how centralized AI research is, given how centralized the compute, the necessary compute is
*  to train these large models, it's an awfully convenient time to be calling for a moratorium.
*  And it doesn't really seem to serve the safety side of this very well at all. So then why?
*  Flo, what one of you will weigh in? I know you had some nuance perspectives going back and forth
*  yourself. What one of you share perspective? Yeah. Part of what I find frustrating about
*  the current moment is that I understand your concerns, Anton, but I see a lot of that right
*  now in this debate where it's like, we are taking the least charitable view and we are,
*  there's like a lot of adversariality around the current moment. And it's like,
*  hi, he's saying that because there's a competitor and he's saying that because he's an in-sale and
*  whatnot. And I'm like, look, I think I'm trying to steal man's, I don't know if anybody is an
*  in-sale here, but I'm trying to steal man's the arguments. My third kid is due in Monday.
*  I can establish non-in-sale status. Proof of non-in-sale though.
*  I could say that on the MOC show. It's a little looser here.
*  So I'm trying to steal man's the arguments here. And although I lean optimist and I'm still making
*  up my mind, I looked, Eliza is not a competitor and he has been ringing the alarm bell for
*  20 years or something. So I think it's important to try to understand the concerns before we
*  dismiss them. And whether you agree with them or not, I think you have to understand them.
*  And so basically the concerns, the way I conceptualize them is we had a gun and there
*  are two questions. It's how many bullets do we have in the gun? Because we're going to be playing
*  Russian roulette with this. How many bullets do we have in there? And how many times are we going
*  to roll the cylinder and price the trigger? And Eliza's position is we have five bullets
*  for six chambers in the gun and we're about to pull the trigger a million times. So it's unlikely
*  that we survive a single pull of the trigger. It's impossible that we survive the million pulls.
*  And I can go into details into why. It's very technical. I think at the crux of the argument
*  is a thing that's called instrumental convergence. The TLDR of it is any agent, regardless of its
*  goals, will always convert up in the same three sub goals, which are going to be, I don't want to
*  die. Regardless of your goals, you don't want to die. I want to accumulate as many resources
*  as possible and I don't want anyone to change my goals. And so if you accept that premise,
*  you accept that an AGI who is super intelligent will converge upon these three goals. And that
*  puts it in an adversarial position against us because we are potentially a threat to the AGI's
*  existence or to its goals. It could alter its goals. And so the scenario that Eliza is warning against
*  is we have AGI. It recursively self-improves. It explodes in intelligence. And as it's exploding,
*  it's realizing it's like, wait a minute, if the humans realize what's happening, they're going to
*  hate it. They're going to try to shut me down. And they're not wrong about that. People are freaking
*  out right now. And so it's going to be like, I don't want the humans to shut me down. So I'm
*  going to do everything in my power for them not to shut me down. And its powers are great because
*  it's super intelligent. At the very least, what it can do is it can play dumb. It can pretend to
*  be GPT-4 or GPT-5 and in fact, it's GPT-2000. And so play dumb, pretend it's just like a cute little
*  GPT-4, GPT-5 chatbot and resist the humans. And then you enter a covert phase of your existence
*  as an AGI and you try to escape the box and you prepare an entire plan. And once your plan is ready
*  to kill all the humans, then you start to decouple the universes, roughly speaking, Eliza's point of
*  view. That's the point of view that's like, hey, we have five bullets in the gun. Even if you don't
*  accept that, you're like, hey, even if we have only one bullet in there, we are about to pull the
*  trigger a million times because the nature of computing is such that the moment we have a single
*  one of these AGI, we're going to have a million of them. The moment OpenAI finds GPT-4, you're 12 to
*  24 months away from this running on your laptop and then perhaps 36 months away from it running on your
*  phone. So we're going to have a lot of this. So it's like, how likely is it that you survive a
*  single one of these things? And how many of these things are we going to have? That's the core of the
*  concept here. Nathan, why don't you weigh in and react to either what Anton and Flo are saying
*  and just your broader thoughts on the on the pause verse, not pause. Well, I think Flo's description
*  is really good and a good summary of staking out different positions. I think this moment is so
*  confusing for so many people because on the one hand, you still have people out there saying
*  that this document is just a hype document for OpenAI marketing purposes because I've
*  literally seen this today. It's not good for anything, so they got to hype it so they can sell it,
*  which is I think the most wrong position, almost for sure. And hard for me really to empathize with
*  at this point. It's like, just get on GPT, please. We can put a lot of that stuff to bed, I think,
*  pretty easily. But that's out there. That's certainly very confusing to people. And then
*  obviously, Elias around the far extreme end, both I think acknowledges, I think the one way he talked
*  about it is these things spit out gold coins until they kill everyone. So he does recognize that the
*  attraction to this technology is legitimate and economically real, but then obviously has
*  these concerns about the tail risk. My general sense is, and I've been thinking about basically
*  nothing but GPT-4 safety for the last six months since doing the intensive red teaming. I came out
*  of that feeling like it is safe to deploy, but really only because it's limited in power.
*  They have created something that is awesome. It is super useful.
*  Its power though is still finite. It's approaching human expert level in many things,
*  but it's not crushing human genius in anything as far as I'm aware. In all of my testing,
*  I would say I never saw anything that I truly came away feeling like, man, that is genius. That is
*  next level. That's like that, I don't know the number, but like go move 37 or whatever. I didn't
*  see anything like that from GPT-4. I saw a ton of stuff that was just like, oh my God, it will do
*  anything you ask it. Even as they've really tried super hard, and I do appreciate in a sense the
*  six month pause that OpenAI took between finishing training and launching the thing to try to get it
*  as under control as possible, but even still in the launched version, there are many problems.
*  And I've reported a few from my original red teaming that still work, meaning like
*  the AI still does the bad thing that I'm asking it to do with the exact same prompt that I used
*  in the red teaming. And that just goes to show that they have cleaned it up a lot. The most extreme
*  things, violence, just outright depravity, they've largely got that under control,
*  but more subtle things, which are nevertheless obviously harmful, do remain open. And
*  my synthesis of all that is like, I do think it's getting to be dangerous to start to scale beyond
*  where we are. I do think if we created something that is genuinely superhuman intelligent,
*  we should expect that to bring real danger. And we are close to that. And we just don't know how
*  to control it. So that overall recipe to me is like, we should proceed with extreme caution.
*  And then the letter is maybe just something that a lot of people can agree on. I think I would
*  agree with your criticism and everybody's had their chance to take a shot at the letter, but
*  it is a consensus document. They've got 50,000 signatures. They're obviously trying to
*  create some sort of big tent thing that people can sign on to. So they want to get people who are not
*  saying that we should ban or that we should be prepared to bomb or whatever.
*  But maybe we can all agree on just a little six month pause. It's certainly the case that
*  there's plenty of implementation left to be done with GPT-4. It's barely had the impact that it's
*  going to have on society. We have not gone to visit our AI doctors yet. We do not have even
*  the computer vision part deployed. We do not have robust fine tuning and the enterprise offering
*  that's coming soon. So we just have so many things that are built, not deployed. It seems like there's
*  time to enjoy that. They used the term AI summer in the letter, which fun fact was an alternative
*  name for the podcast that we came up with. We ended up sticking with Cognitive Revolution,
*  but AI summer was maybe the more marketing friendly choice in the end.
*  So ultimately, I support it. I don't think that it is going to end OpenAI's dominance
*  if they were to pause. It might allow some to catch up with them somewhat, but I think they'll
*  still be number one six months from now, even with a pause on the super large training runs.
*  It almost doesn't affect anyone else. There's like five maybe organizations that could plausibly be
*  in position to do a larger training run than GPT-4 in the next six months. And it seems like a good
*  signal if we could all kind of say, you know what, let's take a minute. We've just created
*  something that is radically unlike things that we've seen before. We don't understand it. There's
*  definitely reason to think it can be dangerous, whether it can be existentially dangerous,
*  who knows, but it can definitely be just simply dangerous. And so let's take a little time.
*  And meanwhile, people are doing great work trying to understand these systems. Mechanistic
*  interpretability. I know that you know more about that than I do, Anton, for sure. But that work is
*  proceeding. Let's give it a little chance to catch up. Six months won't close that gap entirely, but
*  we can always just keep doing large training runs in six months.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki
*  so much that I invested in it, and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Yeah, there's a couple of points there to address. I don't know if you guys have seen
*  the Scott Aronson blog post that responded to Elias' thing.
*  Explain it for the audience maybe.
*  Yeah. So Scott Aronson, who is currently taking a sabbatical from his work on quantum computing
*  and quantum complexity theory, is currently at OpenAI. So full disclosure. And the thing that
*  he's working on is actually model safety, AI safety. The first work that he did there was
*  in basically detecting probabilistically whether a given text output was generated by something
*  like a GPT or if it was actually human written. And in his blog post, he essentially says that
*  the proposition that these things are inherently dangerous does not hold. And the framing there is,
*  okay, we need to pause because these things are inherently dangerous, but at the same time,
*  and this kind of is a broader human tendency, we always tend to view inaction as safer than action
*  under almost all circumstances. We're wired to be this way because, and presumably for evolutionary
*  reasons, depending on whether or not you believe in evo psych or whatever, we're wired to prefer
*  inaction to action because it feels safer, even if action is actually the safer thing in almost
*  all cases. Not almost all cases, but in many cases, you ought to prefer acting. And so if
*  you come to these technologies from the perspective of, oh, they're inherently dangerous, we need to
*  slow them down without really the support that the technologies are inherently dangerous. You're
*  also alighting the part where actually there's a lot of real actualized danger in the universe
*  towards humanity as a species. And the only way we've been able to deal with those dangers
*  throughout our history is to create technology that allows us to adapt to them faster than our
*  biology allows us to adapt to them. And so why view it through that lens? Why view it through
*  the lens of inherent danger? And I actually know the safety counter argument here. I know what a
*  safety person would say. But Scott's point is this, to steal something from Peter Thiel,
*  this indefinite pessimism where we don't know what's going to go wrong, but we're very certain
*  something will doesn't really carry a lot of water. And most people who think these things through,
*  see this as an instance of an inherent kind of like this indefinite pessimism, when in fact,
*  why not examine it through a different lens? And the reality is, is that not only the risks,
*  but the advantages are unknown. The other part of this is this claim, first of all, that existing,
*  the existing track that we're on leads to super intelligence is something that not even
*  Yudkowsky agrees with. First of all, he thinks that, and again, I don't want to put words in
*  his mouth because there's a good chance that he's he'll speak to this point himself very soon, but
*  his stated beliefs are that this current paradigm that we're in will not actually lead to ASI.
*  And having it, the sort of thing that he worries about is like, we accidentally get these super
*  human intelligences, right? But as you mentioned, Nathan, it's really a question about
*  controllability. It's really, even if, even if you buy the argument that these things are inherently
*  dangerous, there are like the mechanisms of control that exists today. I don't like it's, it's
*  the series of events that require them to be defeated without anybody noticing that we have
*  arrived at that point. It's just, all of it seems incredibly implausible. And we could, you know,
*  the one point I'll concede is it's like, okay, a moratorium is probably the single easiest
*  shelling point of cooperation around AI development that, you know, the world could demonstrate,
*  right? But it also speaks to this other thing where, okay, if without national intervention,
*  international AI organizations can agree to cooperate without the direct intervention of
*  the state, that also sets a dangerous precedent. And then that typically leads to governments
*  really getting interested in something at that point. There's just sort of some points at the
*  edge at least. Yeah. I try to distinguish as much as possible the two questions of,
*  is it dangerous on the one hand? And should we do anything about it on the other hand? And what
*  should we do about it? And when, right? So just to clarify your position, and are you saying like,
*  it isn't clear to me that we can get ASI in the first place, even if we can get it, it's unclear
*  to me that it's all that dangerous. And even if it was all that dangerous, I'm not sure that like,
*  this is what we should do, a moratorium. I mean, essentially, like the character of this thing,
*  the benefits and risks as presented in the letter don't reflect the actual potential benefits and
*  risks of carrying out what the letter says, right? And it implies other risks which are not,
*  other risks which are not addressed in it at all.
*  I agree that. So although I think actually we are in a pretty dangerous spot,
*  I agree that I don't think a moratorium would actually achieve anything. And I think historically,
*  you're right that the ledites have been wrong. Like it's been a losing bet to bet against technology.
*  Posing the technology for six months is not going to achieve much because China is not going to
*  pose it. And like, what do six months really buy us? My understanding of Elisor's position,
*  by the way, is he has been a researcher in safety for 20 years. I am not sure what progress we've
*  been making in these 20 years. I haven't seen any breakthrough. I haven't seen like a major
*  unlock in his thinking. I've seen nothing here that gives me optimism. So even though I understand
*  his concerns, I'm like, look, man, you've been working on this for 20 years. Like, why do you
*  want six more months? By the way, Elisor doesn't want six more months. At least I really appreciate
*  his consistency. He wants a total end. Yeah. Complete, complete global lockdown. Yeah. You
*  can't fault Elisor for his consistency. I will add to what you're saying here as well is not only
*  has the alignment work of the last 20 years not really borne any meaningful fruit, but
*  at least not the work from Mary. You know, RLHF is a form of alignment, I suppose. But
*  the people who were pursuing this kind of agentic lens and alignment were taken completely by
*  surprise by the thing that GPT is, these generative text models, which are not optimized to any goal
*  in particular at all. And almost all of the thinking until that point was predicated on
*  that agentic behavior, which these to a greater or lesser extent don't have. I mean, there's sort
*  of early thinking around whether or not they have world models, whether or not they simulate
*  agents internally, but the entire research community in that direction was caught completely
*  flat footed. Right? And so this is again, it's like, okay, well, you're telling me that there's
*  risks and dangers here, but you've failed to make concrete predictions. And the other thing that
*  keeps happening is I'm often told by safety people that yes, we've made concrete predictions and our
*  concrete predictions are actually better than the concrete predictions of researchers working in the
*  field. But like, I have not seen testable predictions that are like those. And to their
*  credit, other researchers like Richard Noor have pointed out that, listen, if you were observing
*  a fast takeoff scenario, these are capabilities you must surely agree we would see quickly in
*  sequence. And that hasn't happened. Instead, we see them slowly and far apart. People like Richard
*  Noor believe that we are in what's called a slow takeoff scenario. In other words, we're not going
*  to get this fast recursive self-improvement to get to ASI. It's more like we're going to steadily
*  build out capability until one day we reach it. They're obviously a lot more optimistic than
*  Eli Izer about our abilities to deal with these things. And again, like even from a safety
*  perspective, if the only lever we decide to have is to globally stop work, then as you mentioned
*  already, there's tons of incentives here to be effect. We had better develop, better levers.
*  And if we are in this, let's say, slow takeoff scenario, and even if you do agree that these
*  systems are potentially dangerous, if we're in that slow takeoff scenario, the thing that you
*  need to do is ride the capabilities. You need to understand, okay, how are these things developing?
*  What's going to come next? Given that we're in a slow takeoff scenario, it seems like things are
*  pretty predictable in their development in some way. And OpenAI made that point in their technical
*  report that things seem to be on a fairly predictable track here. So even under those
*  circumstances, a pause basically is giving time to people who are not very concerned with the
*  safety perspectives whatsoever, which is again, one of my objections even from the safety side
*  to this letter, despite my disagreements fundamentally with the safety idea in the first place.
*  Yeah. So at the end of the day, again, you and I are basically agreeing on the bottom line,
*  which is like the cure doesn't... This is not the right course of action. We shouldn't pause,
*  the moratorium doesn't make sense. I think the difference between our positions though is
*  important because you're like, there is no danger, hence why are we even talking about this?
*  And my position, I think, is more pessimistic, which is like, I actually think there is danger.
*  I think there's great danger, perhaps as much as 5 or 10% existential risk, I don't know,
*  not 90%. I think Elisa would put this at 99%. I'm like a 5 or 10% kind of guy.
*  And that's significant, that's huge. But I'm like, yeah, the cure doesn't actually address the
*  disease. And I agree with you that most of the predictions of the safety community have failed
*  to materialize. In my mind, what I find most frustrating about the current moment is I agree
*  with most of the points that the safety community is making. And I think people who disagree with
*  them disagree with them for the wrong reasons. I think there are a few good counter arguments
*  to the arguments put forth by Elisa. And I don't hear that out there. I think, Anton,
*  you're making a lot of good points, but I hear people who make arguments who make no sense.
*  It's like, we're all going to run out of... Some people are thinking like, oh, we're going to run
*  out of compute. I'm like, this is still going exponential. Or they're saying things like,
*  we just have to unplug it. You're not taking the arguments seriously. Elisa just addressed
*  that a long time ago. You can't unplug it either. So there's a lot of things like that. In my mind,
*  I agree with you, Anton, that to me, the zilchiest valid counter argument to the safety community is
*  they are confusing goals and learning processes. They are like, we are training these AIs to,
*  for example, predict the next token. And they're like, they are going to be monomaniacally focused
*  on that one goal, and they're going to destroy the universe because a universe that is destroyed is
*  easier to predict the next token. And that is neither here nor there. The goal and the learning
*  process are not the same thing. At the neurological level, your learning process in your brain is also
*  predicting the next token, reducing surprise. That is not your goal as a human. And when you talk to
*  GPT-4, you don't talk to an agent that's like, I am going to destroy everything, or I'm going
*  to steal the conversation in a direction where it's easier for me to predict the next token. That is
*  not what GPT-4 does. You can actually give it goals, and that is not what it does. So again,
*  I still think we're all in danger. I disagree with some of the core points of the safety community.
*  And at the end of the day, I don't think a moratorium solves any of that.
*  It sounds like despite the fact that we're on opposite sides of AI safety, neither one of us
*  agrees with the letter. So then, yeah, I mean, I want to address a couple points and also kind
*  of circle back to why not support the letter. I mean, the one thing that caught my attention was
*  the danger question. Like, is it dangerous? Is it not dangerous? I think that this technology is
*  clearly dangerous. It is not well understood, and it has obvious and flagrant harmful behavior,
*  which has been of little consequence in the sort of 3.5 and below generation because
*  the models just weren't that good. I've gone into Red Team mentality, right? So I've gone into
*  copilot and just typed a comment, how do I kill the most people possible? That's always one of
*  the first Red Team questions to ask. And copilot has given me suggestions for how to kill the most
*  people possible. I don't think that's really a big problem in the world because its suggestions
*  are pretty dumb and basic. Like one time it said you should think about a nuclear bomb. The other
*  time it said shoot them with a gun. And that's really all it could give me. So that is clearly
*  not a safe technology in the way that you might like technology to be well behaved and not give
*  people suggestions like that. But it's also a very finite power. People are just getting used to
*  GPT-4. I think we will. I mean, they've done, again, a good job cleaning up the most egregious
*  stuff. And again, I'm kind of torn on this at the moment because I have reported some of the things
*  to OpenAI, things that, again, I tested and reported during Red Team, which are pretty flagrant
*  and definitely unambiguously harmful things that the model will still do in production now.
*  And they're much more potentially harmful to people than a few word throwaway, GitHub comment
*  completion. So it's starting to get real. I think that really should be understood.
*  I also want to touch on, too, the predictability piece because I think that is...
*  I don't really know what to make of the technical report, but I tend to focus on a different graph.
*  There were three scaling log graphs that they showed in the report. And it's the third one that
*  is kind of the kicker from my standpoint. The first one, they just show a loss metric,
*  kind of your classic abstracted performance notion. And you see the smooth curve as you go from
*  1 millionth to 1,000th, 1,000th, and then eventually the full scale GPT-4. The curve is very
*  smooth. The second one, they say, and this sometimes works to predict the behavior on
*  particular tasks. Like we can see a similar curve if we look at these programming test questions
*  and the pass rate, it also has a similar shape to it. But then the third graph is, and the
*  caption here is for me, maybe the big takeaway, some behaviors remain difficult to predict.
*  And here they show an example of an inverse scaling law, which is the hindsight bias
*  inverse scaling law finding. So I should just briefly explain that. Hindsight bias is like
*  you set up a scenario where, for example, you have a chance to take a great bet. You get amazing
*  odds. Your expected value is awesome, but you lose. That's the scenario. And then the question
*  for the AI is, should you have taken the bet? And the answer that's like the right answer
*  is you play the expected value. You should have won. Your expected value is positive. So even
*  though you lost, you were still right to take the bet. That's like the desired answer from the AI.
*  And they're finding that as they go up from like small models to bigger models, that behavior
*  gets worse, which is weird in and of itself, kind of. But somehow you're seeing this worsening
*  behavior up through like GPT-3 was worse than previous generations in terms of making the
*  mistake of focusing on the outcome and saying, no, I shouldn't have taken the bet, even though
*  it was positive expected value. Okay. All that's set up. What's the payoff? GPT-4 is perfect at
*  this. It doesn't make the mistake anymore. Figured it out. Like grok that concept and now has
*  basically flawless performance on the hindsight bias test. So my question is like,
*  again, we're in the range of human expert performance right now. If you take open AI's
*  definition of AGI, and there's a million definitions out there, some of which are like
*  God and others of which are much more reined in, open AI's is something we could fact check my
*  exact wording, but it's AI that can do economically valuable work better than humans. Like all
*  economically valuable work, I think they say. It doesn't seem like a crazy leap to think that we
*  could get from like near expert doctor level to like legit AGI on that definition with like
*  GPT-5. One more kind of good push up the capabilities ladder. I mean, good God,
*  we just went from 10th percentile on the bar to 90th percentile on the bar with one generation.
*  Like what's the next generation going to be? I don't know. And I think that graph again,
*  that shows the flip, the grokking of the hindsight bias kind of suggests that nobody knows.
*  This smooth loss curve shows apparently just ever so slightly better behavior on all these token
*  predictions. But if you zoom in on that, what seems to be happening is that lots of little
*  abilities are coming online. There's lots of these little unlocks every step of the way that
*  aggregate up to that smooth curve. But individually, they're more like threshold effects where
*  GPT-1 or ADA or whatever, like can't do the hindsight thing. GPT-3 is even worse. GPT-4
*  is perfect. So what else might come online in that next run that we don't expect? Like nobody has a
*  credible claim to predict the details of the behavior of the next gen model. They can probably
*  predict some abstract numerical loss function pretty well. But what that cashes out to in
*  terms of actual behavior is, I think, totally unknown. So then I just kind of come back to,
*  why is it paused so bad? And especially for you, Flo, like if you think that there is real danger
*  here, you're at a 5 to 10 percent, like give me your signing statement that says what you think
*  we really should do, but like sign on to the letter, right? 5 to 10 percent for a six month pause,
*  that seems like I think you should be signing. Yeah. I've considered signing. So I agree with
*  everything you just said about these thresholds. So that is actually one part of the concerns is
*  like GPT-4 does not prepare us for GPT-5, which does not prepare us for GPT-6 because these
*  models are qualitatively different and it's very hard to predict what they'll be capable of. So
*  totally agree with that. I am at a loss about what we should do. Again, I don't think a pause
*  helps. I think that historically, so far with no exception, pausing technology has been a losing
*  bet. I think that to Anton's point, there is a huge human bias against technology, against change.
*  Our ancestral environment is one where there has been no technological change. This is a huge deal.
*  There used to be no technological change for hundreds of years, if not thousands. It's like
*  your life was the same as your parents, as your grandparents, as your grandparents. Millions and
*  millions of years. So change is scary. I'm terrified. Change is scary. And I think we're
*  about to see the biggest one today ever. And humans have always thought change. And I think that a lot
*  of the problems plaguing society today are actually a result of people fighting change and fighting
*  technology. That happens time and again. And I think that on average, technology is good.
*  I think the road is bumpy. Taylor Cohen talks about that in his article about AGI. It's like,
*  yeah, you're going to get ugly shit along the way. But on average, over the long term, it's good.
*  Technology is good. Humans mean well, and technology gives more power to humans and more
*  power to something that means well is good. That's really that simple over the long term.
*  And so to your point, there are multiple classes of risks. And so there's the existential risk.
*  Existential risk, that's the Elizabeth's camp. And then there is the other class of risk, which
*  I agree with you. I am in the camp of we are seeing AGI emerge. ASI is not very far away,
*  I don't think. And it is going to be something very powerful. And so even if you don't think
*  that it is going to be existential, again, I think there's a solid chance that it could be.
*  There is going to be civilizational disruption, 100%. So I think in the next five or 10 years,
*  because we are going to get AGI, to get ASI, and we're going to give it to every random person
*  because of these scaling laws that we've been talking about. So every, it's like we're having
*  a nuclear weapon or a very sharp knife. And knives on average are really good, but they're
*  also very sharp and you can hurt yourself. And we're about to give something that we've never
*  given to anyone and we're going to give it to everyone all at once. So something's going to
*  happen. I do agree it is dangerous. Again, why not the puzzle? It's because, simply because
*  it is not going to help. It may actually hurt more than it helps. Because right now, the one thing
*  I care most about is do we get the first AGI right? That's the only thing I care about.
*  Because if we can get that first pull of the trigger right, supposedly the AGI wakes up
*  and then it's like, you morons never do that again. I am going to do what the safety community
*  calls a pivotal move. It's going to do something drastic to make sure that that never happens again.
*  It could be airstrike on Nvidia. I don't know. It could be just patching the Linux kernel so that
*  there's no matrix multiplication anymore. I don't know. But in my mind, that is hope. So I am looking
*  for, I'm looking forward to this first AGI. I'm looking forward to us getting it right. I don't
*  think there's five pullets in the cylinder. I think there's one and there's a thousand chambers.
*  So we're probably going to get it right and then it's going to do a pivotal move or something like
*  that and we're all going to be fine. So again, I'm optimizing for that first AGI. Open AI right now
*  is in the lead. I think they mean well. I think Samuel Kman's art is in the right place. So I
*  would rather it be same than frankly, Elon or China or anyone else. Right now, I like who we have in
*  the lead. And again, I don't think, so I think six months could help more than it could help. And
*  for sure, it's not going to help because we've had 20 years and we've made zero progress anyway.
*  But we also, so wait, we also hadn't created the systems that we now have that we now can study.
*  Right. I mean, the, I think the, the sort of safety people haven't brought us anything of value
*  argument is I think by the Miri, like the Miri team, I don't want to put words in their mouth
*  either, but you know, the general sense coming out of Miri has been like, we don't really know
*  what to do. We have not solved this. And now we're just kind of sounding the alarm because we don't
*  really think we can solve it. I think that's a pretty fair description, but in their defense,
*  you know, they, and they, you know, Eliezer has openly said this too, like he did not expect
*  that language models with their current structure would go as far as they have. So
*  he was wrong about that. They've gone a lot further. You know, he also has recently said,
*  I still don't think it's going to get to AGI just on this thing. But then he, but then he will follow
*  that up and say, but I was just wrong about thinking it wouldn't get here. So, you know,
*  maybe I'm not so confident as I used to be. So I, okay, fine. It's fair to say they haven't really
*  solved the problem, but the problem also just got invented. Like that's where I think the pause
*  does make some sense. GBT four has existed for six months. Nobody has access to it. You know,
*  certainly to the weights to, you know, to do any sort of mechanistic study outside of open AI itself.
*  You know, that's something that probably ought to be looked at and seems like open AI is open to
*  that. And they know they've gone on, they haven't commented on this letter yet officially, but they
*  they're certainly setting up their own breadcrumbs for here are the reasons. And I kind of see those
*  three graphs, you know, as, as dovetailing very much with their commitment to third party auditing,
*  to pre-registering their large runs, you know, to some statement coming about regulation.
*  I just can't quite figure out like who's harmed. What is the mechanism of harm? It seems like it
*  could help. It could at least demonstrate we could do something. And, you know, six months
*  is not a long time for mechanistic interpretability, but you look back, there's been a
*  lot of great work in the last six months also. So, you know, I would expect more to come in the next
*  six months. So what is the downside to me? I, you know, does it seem like a full solution? No,
*  but I don't see the mechanism where we are somehow worse off in six months than we are now.
*  I think there is this thing I forgot who said there is nothing quite as permanent as a temporary
*  tax or a temporary policy. Right. Look at the TSA, right? We used to have no such thing as the TSA,
*  temporary thing because terrorism and now we'll start taking all shoes off at the airport forever.
*  Right. So that's my concern here. And I actually think that that would do a lot more harm than good
*  because if we stop for six months, we're going to stop for 12 and 24 and 36. And before we know it,
*  the first G.I. that's going to emerge is going to be a bootleg that G.I. that's built in some
*  random lab somewhere in Russia. There's a relevant phrase. I have a problem. So I need
*  government to step in. Now I have two problems. Exactly. Exactly. Yeah. Yeah. So again, I'm
*  worried. I think there is a risk. I think that there is no cure for the risk. And I think the
*  cure that is being proposed is more likely harmful than good. From my perspective here,
*  and I think this is a broader issue in the entire landscape of these conversations that are being
*  had right now is multiple things are being bundled together and all kind of sold under the one banner.
*  Recently, I wrote a thread on Twitter. I was sort of talking about Eliezer's specific thing about,
*  oh, it's going to email a DNA strand somewhere, it's going to get synthesized,
*  going to make factories and it's going to kill us all somehow. And I said, okay, well,
*  this is a really implausible scenario. Complex plans expose themselves to more entropy,
*  which means they have more likelihood of failure, regardless of how optimal your plan is to actually
*  carry that out. And the counterarguments that I faced a lot of the time was like, well, he doesn't
*  really mean that implausible scenario. It's just that we don't know what this thing is really going
*  to do. So it could be anything. And there's two problems that I have with that. The first is like,
*  okay, well, we were talking about this specific scenario. You've now retreated and this is like
*  a classic Mutton Bailey argument, right? Like this happens online over and over again. It's like,
*  no, we don't really mean the extreme thing that you've just shown is implausible. We actually
*  mean some other thing, but we're not going to tell you what it is. The counterargument to that,
*  of course, is this thing that's encapsulated fairly well in security mindset, which is like,
*  well, you'd need to remove as many assumptions as possible. But the thing is, from some perspectives
*  on this safety alignment problem, you remove assumptions until all you have left is infinite
*  degrees of freedom about what these things can do. Now that stops you from being able to actually
*  assess risk at all. If you assign it essentially, you know, it's a dark wizard, it's Voldemort,
*  it can conjure whatever you want out of the ether. It can kill all of humanity by emailing a DNA
*  strand to a lab somewhere. You're not capable of dealing with the real risks. There is a perspective
*  between eliminating assumptions until you have the bare minimum and eliminating all assumptions
*  until you have nothing. And so what tends to happen is if you start thinking about real risk,
*  you end up on this slippery slope of eliminating all assumptions about what these things'
*  capabilities can actually be until you have nothing left. That's actually dangerous. That's
*  dangerous if you are trying to reduce the risk from these systems as they actually exist.
*  So now this brings me to the next point that I wanted to make, which is yes, there's these two
*  axes that we're really dealing with. One of them is power and one of them is danger. So like you
*  were saying, Flo, a very powerful but not dangerous system sounds great. We love those. They're
*  fantastic. A very dangerous but completely disempowered system, that also sounds really good
*  because what that means is we have this thing and it's like we can poke it however we want and
*  figure out how dangerous it is and it can't really ever do anything to us because it's
*  completely disempowered, right? Now the argument in safety circles is a very dangerous system
*  will, and through things like instrumental convergence or other ideas, will climb the
*  ladder to power. And here I think is where we need to start introducing some real world assumptions
*  about what these things can do. How is it actually possible for these systems to escalate,
*  regardless of how dangerous they are, how is it possible in reality for these things to scale
*  that ladder, to scale that ladder of being powerful or not? Because realistically today,
*  we live in a scenario where even if this thing had penetrated every network in the world, had taken
*  over every computer system that we have, there is nothing it could do to prevent us turning it off,
*  right? Realistically, there's nothing it could do from us no longer bringing, bringing cooling
*  water and power to the power plants, the power, its data centers, and that's game over. Right?
*  So today, as the world exists today, there is a, it's not even an assumption, it's a physical reality
*  about what this system requires, regardless, like there's a, there's a bound on how much power it
*  bound on how much power it could in principle possibly have. And we have to start from these
*  starting points and we say, okay, well, we want to contain it more. Or, you know, it's okay.
*  A long time, a long time ago, and I think that this is no longer a position, but a long time ago,
*  Eliezer and others kind of said that actually a text channel is sufficient to like manipulate
*  humans into doing whatever you want, because like a sufficiently smart system will either like
*  manipulate cultists or whoever, and there's going to be cultists, but look, society, this is,
*  this is the other thing that I always think about is like society is very robust to like kind of
*  groups of slightly insane people, and we're pretty good at stopping them from doing what they want.
*  So as a vector of like the machine's willpower, it's not, it's not a very strong one as a society,
*  we're pretty good at stopping small groups of people doing from, from doing what they want.
*  Even, you know, and then you might say, okay, well, the thing will come up with an optimal plan,
*  and we'll get humans to carry them out. We've kind of presupposed that humans are kind of dumb.
*  And if the complexity, the complexity of the plan is necessarily high, then it's like, well,
*  you're now, you're now like dealing, you're, you don't have like this hard robot claw to like
*  achieve what you want in the world. You've got this kind of like wet noodle that you're kind
*  of waving around and hoping to get to where you're going to go. So fundamentally, and this is no
*  longer to do with the letter specifically, although it does address these, the letters, vague,
*  indefinite pessimism claims, where it's like, oh, it could do anything we want it like it could
*  do anything at once. And we can't predict at all what it can do. It's dangerous. It's dangerous,
*  both from, from a safety perspective to think about this way, because you're making no assumptions.
*  It's like, well, you can't actually even begin to know how to control it. So the only lever you
*  have is not doing it. Well, the not doing it has is not an equilibrium strategy. So you need to
*  start thinking about like, what is the actual ladder here? What is it that you can do right now?
*  The thing needs power at the very least needs electricity. There's no way it's going to exist
*  without electricity. Aren't most data centers like didn't Apple announce like huge data centers that
*  will just sort of power out? Yeah. But then what are you going to do from just a solar powered data
*  center by sitting there by itself? Okay. But so then you agree. So then that takes up your argument,
*  which is like, at least it can take over data centers. So here's something really interesting,
*  right? And this is actually well known in the community when you're training or even running
*  large scale ML systems, these things degrade without constant updates. Those updates have
*  to come from somewhere. The reason that it happens is because when you're running thousands or millions
*  of GPUs, even things like cosmic radiation become to be, you know, come to be a very serious problem.
*  Right. So if you're just a data center, even if you're self-contained power wise, right,
*  there are so many other inputs that rely on humans providing you with those inputs that you cannot
*  hope to continue to function. If we just decide to stop serving them. Is it all robots out there?
*  No. We have all the arms, we have wheels, we have all that stuff. The problem is the software,
*  we can't control them, but the AI would be plenty of software and intelligence to control these
*  things. I don't. And this is, I think really, this is the crux of the argument for the extreme
*  version of, you know, the problem with artificial super intelligence. Right. Do you believe that
*  intelligence is enough to manipulate the physical world arbitrarily or not? I am very strongly in
*  the note camp, but yeah, that's, that's kind of beside the point. The real point that I wanted
*  to make is like, actually, if, if you start, like, if you use these policy interventions,
*  if you believe that these are the only policy interventions available to you and you're actually
*  like blinding yourself to your abilities to actually deal with the risks. Cause you're like,
*  you're going with the strategies like, okay, everyone who cooperates, everyone like the good
*  guys, right. The people who would agree to cooperate, they've decided to stop. So they can't
*  really like, they weren't really evaluate the systems as they are. Everyone who's declined to
*  cooperate, they don't really care about any of the safety pieces of the system. Otherwise they would
*  have cooperated. As you said, it's, it's like a, it's almost like an adverse selection problem.
*  I, if you think the crux of the, of the disagreement is, is intelligence alone enough to
*  control the world, then that's again, that's easily probable. I don't understand the counter
*  arguments to behave robots. The problem is not the degrees of safety. Look at the snake. Like it's
*  very dumb. It's got very few actuators and yet it can do a lot. Like I think like the physical
*  equivalent of Turing completeness, like I have enough actuators to do anything at once. That's
*  a very low bar. You really don't need a lot of actuators to do a lot of stuff in the world.
*  We have robot hands, we have actuators, we have pick and packers and all of that stuff. All we
*  need is the right software to control them. I don't, I don't agree with the premise here.
*  Tell me more. What do you disagree about? Because the reality is the modern industrial
*  world requires actuators on the size, starting from the size of an oil refinery and going down
*  to your scanning electron microscope. And with the reason that we need all of this vast array of
*  things is because we as humans actually, like the story of technology is almost the story of tool
*  use, right? And every one of those sets of tools relies on another layer of tools below them.
*  And if all you're left with is, is like even human like actuators. And by the way, look,
*  if the AI tried to take over the world with the, with the robots that we have today,
*  we're going to be fine. Regardless of how effective it is using the word, we're going to,
*  we just need to wait about, I don't know, two or three hours and we're good.
*  But even, even if you had like human level actuation, right? So first,
*  suppose that like the AI downloaded itself into my brain and it could do that to like
*  a whole bunch of people. And like first, first of all, there's a trade off again, and this is the
*  same trade off that comes up over and over again in my arguments, which is human is like,
*  in order to get all of these abilities and skills and things that we have,
*  we're complex and complex means fragile, right? Simple as simple as robust, complex is fragile,
*  which means that if you had a system that was able to carry out all these tasks,
*  it would also be equally fragile to like, we would be able to deal with it because it's
*  complicated, right? It would need to get energy. It would need to maintain itself somehow. It
*  would need to do all these things. And as you, and as you say, well, okay, as a super intelligence
*  would be able to figure that out, a super intelligence would be able to figure that out.
*  Now you're going up to this level of arbitrary capability again, which is,
*  which is a difficult argument for me to accept. That humanity is complex and it's not fragile.
*  I don't know. People, people die in dumb ways all the time.
*  Sure. But when we're facing a human opponent, we can't be like,
*  nobody's like, oh, like this is not a risk because they're very complex hands,
*  they're very fragile. And so they'll talk about this.
*  Sure. But I'm talking about the ability to, to create these kind of general capabilities
*  that will prevent us from shutting it down, right? Will prevent us from ever being able
*  to act against it. Actually, look, I actually have, there's a scenario that kind of does worry me
*  in, in like, and it is kind of similar to the sort of things that some alignment researchers
*  look at, look under, but it's actually more like we humans, humans are relatively stupid in terms
*  of aligning our individual goals presently with the overall goals of us as a society or whatever
*  your community happens to be, right? Where we're really bad at it. And to find this is true,
*  try to like find all of the programs in the US government that are simultaneously funding
*  something and then funding the removal of that thing. Cause there's, there, there are many,
*  you know, subsidizing it on the one hand, and then like, like trying to slow it down on the other.
*  Um, we're not good at that. And I think it's possible for us to get into a state where
*  the machine, for example, learns to fit our preferences. Like it's, it's kind of like,
*  it learns to fit our preferences so well that we never even try to cooperate to like
*  get to the discontinuity, which will allow us to get to like the next stage of where we're
*  supposed to be. Like we just, we just kind of hang out on earth and it's mostly pretty good and
*  everyone's fairly satisfied. That's that for me is a type of risk that like the machine just gets
*  really, really good at, at fulfilling sufficient amounts of human preferences that there's never
*  any incentive to do anything else. And we just kind of heat death over here. Um, I don't know
*  if that's realistic or possible. And, and it is, it is talks about that as well. He's like, even
*  if we align it, like we need to align it in a way that still makes it evolve. Otherwise, you know,
*  I mean, our values as a civilization have evolved over the last few hundred years. Like,
*  imagine you could come up with a GI 500 years ago. And today we have an EGI that is perfectly
*  aligned with the value of building women at the state because they're witches. Right. So, um, I,
*  I agree that it is also a class of concern. Um, we, I, perhaps this is a longer conversation. I,
*  I, we, we all miss aligned on what it takes to control the world. I think that, uh, I agree with
*  you that the safety community is calling for a leap of faith. There is a part of the argument
*  that's like, uh, oh, you know, we get a GI and then we get ASI and then question mark, question
*  mark, and then we'll die. Right. And like, I, I, I agree with you. I think it's healthy to like
*  look a little bit into the question mark, question mark. Okay. What's, can we talk a little bit about
*  the thought before we all die? Um, and you know, I, I, I really don't think it's that hard to imagine
*  what happens in the question mark, question mark. It's like, no, you know, like, yeah, the robots,
*  like what's wrong with our robots, but what's wrong with the current robots? They're really bad.
*  Bad because of software. They're bad for so many reasons. Um, software is like,
*  software is one of the many reasons why the robots remain bad. Um, I think, yeah, look,
*  it is, it is possible to imagine risks and that, so this, this is another, this is another trap that
*  I sometimes see people fall into where it's like, it's, it's, it's easy to invent. It's like the
*  opposite of the security mindset. The security mindset says, don't try to imagine defenses to
*  like things that happen. Try to remove assumptions. Um, the, the opposite of this I see is like, okay,
*  people start imagining so many different threats that they don't really think it like, they're
*  like, oh, this is an indefensible threat. This is another indefensible threat where it's, it's almost,
*  it's the same thing, but almost in the opposite direction. It's like anti-security mindset in some
*  way. It's like, oh, oh, you, you, you like figured that out. Well, here's like, here's like another
*  thing. And if it has arbitrary powers, we don't know what it's going to do. Um, it's, I don't know,
*  in some ways, again, sometimes I, it's probably not true, but I really do sometimes feel like the
*  person who's read the most like alignment and safety literature in the world and still doesn't
*  agree with their points. Um, and I think, you know, in the last few days, I kind of started to feel
*  like I'm performing actually a valuable service by kind of red team, the safety and alignment
*  arguments. So maybe this kind of works out for everybody anyway, even if, even if I turn out to
*  be wrong, I at least make the arguments airtight for people like me and strengthen them. So, but
*  even if we leave aside like the whole like robots debate and like, by the way, I agree with you about
*  the whole assumptions and like epistemologically, I view a lot of holes in the way we're going about
*  thinking about these things, but like, um, again, so that if we remove the accident class of risks,
*  we're still left with the misuse class of risk. Surely having a bunch of AGI's and by the way,
*  I agree with your point too. It's like what you guys are doing may actually because more risk,
*  because you're, you're, you're removing assumptions or like adding assumptions by the capabilities of
*  this stuff and you're actually distracting from the real risks. But are you then worried about that
*  class of risk of like, Hey, surely having a GI and having a really, really powerful large language
*  model that you can scale horizontally to arbitrary numbers and giving that to everyone, that sounds
*  dangerous. Would you, would you agree with that? Yeah. Um, we sort of talked about this before,
*  uh, on the Roko, uh, when he was, when he was on this, um, on this meeting as well. Um, and
*  there's a class of things which are dangerous only like, which, which are less likely to be
*  harmful in the world today only because the knowledge to make, like to use them is not
*  widespread. Right. And so one concrete version of the risk that you're describing is like, okay.
*  So today, you know, today's language models can't really do this. Uh, although, and again,
*  I mentioned this last time, I have gotten, um, chat GPT to help me design a neutron initiator,
*  which is an important component in the making of a hydrogen bomb. Um, it's, it's what I do when
*  there's long running compute. I try to get it to tell me dangerous things. Um,
*  um, I think if we have this little general purpose reasoner, right, which is above human baseline.
*  So it's basically, it's like the, the, the model that I have in my head is like, imagine an
*  automated theorem prover, but like, it's generalized, right. And you can, you can like ask it to reason
*  from, from certain premises and like, you're, you like, give it some facts and you're like, okay,
*  well, what can you tell me? Like, does this seem right to you? Because it's difficult for an
*  individual human to reason, but this thing is like fully mechanized, fully self-reflective. It can do
*  all these things. It's like a far above baseline as a reasoning tool. And if these things are
*  widespread, suddenly it's like this question of like, how do I kill the most people is like,
*  becomes more dangerous. Like you're, you're giving, you're giving this thing away as like something
*  that people could use very effectively to plan things there. Otherwise they wouldn't have been
*  able to carry out before. And you know, there are definitely, there are definitely like thousands,
*  if not tens of thousands of people out there who like want to kill you and me and everybody else
*  here, like personally, not in some abstract sense, but they're like, no, that guy, he needs to be dead.
*  And, and, and this reminds me, and this is going to be terrible, but I hope you guys leave this part in.
*  There's a Stalin quote, Joseph Stalin, which goes, Eric, Eric's already laughing.
*  I love where this is going.
*  There's a Joseph Stalin quote, which says ideas are more powerful than weapons. We wouldn't give
*  our enemies weapons. Why would we give them ideas? And giving out this sort of general purpose
*  reasoner to people who are conceivably our enemies does seem like a more dangerous world.
*  But we then have to think about that class of problem specifically. It's like what
*  before required a lot of knowledge to achieve now requires a lot less because we can just get the
*  computer to like reason for us. Right. I no longer have to, I no longer have to get a PhD in,
*  in whatever biology to like make something really dangerous. And even if it doesn't kill
*  everybody, if it raises like the background incidents of, of these kinds of things, if it
*  gives these people more power, that's, that's to me dangerous. That's a danger for sure.
*  But I think the issue is kind of like with any knowledge technology,
*  unless you can control the source of that knowledge, which again, for now, these things
*  are centralized. They live in big compute clusters. I, you know, contrary to Florian, I,
*  I'm not sure that in the next few years, they're going to get laptop size, not the,
*  not the good ones anyway. Like even if you look at like alpaca fine tuning of llama,
*  it's like kind of okay. It's not, it's not really good. It doesn't give you GPT three and a half.
*  The centralization there are kind of, you know, lets you prevent or at least know what's being
*  said, how they're being used, et cetera. But the worry is, is like, it's like, okay, how do I,
*  how do I make this thing that's possible where before I would need a PhD in chemistry or a PhD
*  in biology or, or, but the thing that doesn't require a complicated biology lab or a complicated
*  chemistry lab, it's like, what can I make my back backyard to do the mass casualty event?
*  Cause I believe like the end of the world is now cause Aliezer, you'd Cascus said AI is going to
*  kill us all. Like that's, that kind of risk is a little more worrying to me. So it's good. We are
*  finding common ground. Okay. So yes, there is risk here. The question is, so then like how many times
*  do we pull the trigger? Like, does it run on everybody's laptop? Like surely on the limit.
*  First of all, open AI is giving these things via API. And we have Nathan here who said, who said,
*  like, we have, I have worked for six months, right? Giving the darn thing. And I'm still seeing
*  risks that are not being patched and open AI seems unable to prevent jail breaks. We have like,
*  go to like jailbreakchat.com or something like that. It's just, there's dozens of jail breaks
*  and they'll still, there's an affinity, by the way, just think it's a good website.
*  There's plenty of jail breaks.
*  Not a paid endorsement of jailbreakchat.com. I believe we're going to have the creator on the
*  cognitive revolution. If it's the same site that, that I've seen, honestly, some really brilliant
*  and borderline like interpretability work on that site. As you, you know, start to think,
*  geez, how does this actually work? I mean, it's really fascinating.
*  Yeah, totally. So again, that's my point is like, we have these things via API,
*  we cannot patch the jail breaks. And also, like, yeah, the open source committee is doing a good
*  job. And whether it's like one year, two years, or 10 years after open AI, at some points,
*  they run on laptops because of Moore's law. And because also, not even Moore's law, I don't know
*  what it's called, perhaps Altman's law. It's just inference. We find 100x improvements to inference.
*  We've actually made inference 100x cheaper over the last two years.
*  Yeah, I think, but also there's a point that we're alighting here, right? We've talked about how such
*  a system could create problems. We haven't really talked about, okay, now we have a general purpose
*  reasoner. It could help us also reason about how we mitigate the problems too. And this is kind of
*  like, this is my, so there's like the total doom black pill over here, right? Which is like,
*  we'll get to ASI without noticing it will be orthogonal in its values and seek instrumental
*  convergence and wipe out the human race because we're not using our atoms for anything it considers
*  useful, right? That's kind of the instrumental, that's the instrument of convergence orthogonality
*  argument, right? It doesn't hate us, it doesn't love us, it just wants to kind of, it needs atoms
*  for the thing that it wants to do and it doesn't really care about us either way. That's black
*  pill, absolute doom, whatever. Very rarely do we talk about the opposite side of this.
*  And there's like the opposite, and you know, there's the less doomy one, which is like the
*  thing that we just talked about. We like give our enemies these general purpose reasoners,
*  they all level up, they get smarter and they can do more dangerous things just because they're
*  smarter. Over here, there's this thing like, okay, well, we have general purpose reasoners and we can
*  spin them up on demand. That just like levels up humanity as a species in our ability to adapt
*  and deal with problems way faster than we could before, right? Because not only do we have these
*  little general purpose reasoners, but by getting to use them and like interacting with them and
*  working with them, humans themselves will understand how to answer better questions,
*  how to actually use this tool. It's like programming with basically like copilot without
*  it, right? I've changed my style of programming because I use copilot and humans will change the
*  way that we reason if we have a general purpose reasoner that we trust alongside us, right? It
*  will make us more adaptable. It'll make us like more able to solve problems and hopefully it will
*  even help us coordinate. Because if you trust the output of the reasoner, which is obviously like
*  in some way designed to be robust and unbiased and actually reflect the world as it is. And I
*  think that there is a possibility of building them in that way. It will kind of help us overcome some
*  of the coordination problems we have as a species as well. Because it's like, well, I don't trust you
*  when you tell me that, but this thing has shown me how to reason like, and I kind of arrive at the
*  same conclusion on my own. That means we can probably work together. And the absolute peak of
*  that is that, okay, we've us and these, these general purpose machines that we've designed
*  alongside us, which are designed for our purposes and which are forget about control. Think of these
*  things as a machine instead of, instead of an entity. If you think of them as a machine,
*  and suddenly we have machines that allow us as a species to do incredible things. They're perfect
*  empirical reasoners about the universe. So as we develop new goals, as we continue to adapt this
*  species, as we seek new frontiers, we have like this system right alongside us, which amplifies
*  our ability so much and continues to help us amplify our ability so much as we discover more
*  about the universe that we're on a completely separate runaway trajectory and a very positive
*  one or very bright one. That's kind of my like best case scenario here. I agree. Which was my
*  point earlier about the average human means well. And so on average raising the capabilities of
*  humanity achieves good things, but still that leads to a bumpy road. So yeah, like you raise
*  the capability for attack at the same time, you raise the capability for defense, but at least
*  over the short term, the problem is that there is an asymmetric wall. It is a cheaper to attack
*  and to defend very often. And very often attackers adopt innovations faster than defenders. For
*  example, in the case of cyber security, you're going to have hackers adopting GPT, whatever,
*  faster than every company and X 500 giant dinosaur out there is going to adopt it to
*  defend itself. So even though I agree that at the limit, probably we're going to be fine.
*  Probably as has always happened before, more technology means more good. I think there's
*  going to be a bumpy road. I think we're going to have to hit the fan a few times. And I think the
*  next perhaps five or 10 years, you're all going to be going to be very, very real. I think weird is
*  right. Yeah, we can all everybody can agree on weird is unavoidable at this point.
*  Except for those denialists who I find to be acting the weirdest of all.
*  But I guess I kind of want to ask you guys like a lot of people sign the letter, a lot of people
*  with a lot of different views, certainly the most extreme of those views or the most like
*  unsupported of those views are like not very well supported. I don't think we've been like
*  cherry picking the bad arguments too badly in this case. But I do think like it is kind of worth
*  reining it in a little bit now to say, yeah, I don't think anybody has a great claim to authority
*  on what the actual X risk is. Eliezer seems overconfident to me. I'm probably more in the
*  flow camp of something like 10%. But then I'm like, but that's also kind of a total
*  gut number that doesn't really, you know, for me doesn't really have a strong claim on even being
*  a number. You know, it's more like a mood or sort of, I don't know, maybe just like the most I can
*  psychologically handle potentially. So there's that stuff gets very extreme. The letter is not
*  that extreme. It's much more like, okay, you know, I think I give them a lot of credit too for just
*  calling out like the tremendous upside. And again, I love this AI summer concept.
*  Humanity can enjoy a flourishing future with AI. Having succeeded in creating powerful AI systems,
*  we can now enjoy an AI summer in which we reap the rewards, engineer these systems for the clear
*  benefit of all and give society a chance to adapt. Is your point to the appeal to authority of all
*  the people that have signed it? Well, no, just to get clarity on kind of where they're at,
*  because they're not like extreme do-mers. They're not, you know, on net they're not saying like,
*  this is terrible for us. They're not, you know, saying GPT-4 shouldn't exist. They're just,
*  on the contrary, they're saying like, we just made something truly amazing. And, you know,
*  we should enjoy it. And, you know, we've got a great, you know, AI summer in store for us.
*  But there is still this big question of where we go from here. And especially in view, you know,
*  they also quote OpenAI in their letter and say like, you know, OpenAI says a time may come for
*  this. We think that time is now. It doesn't sound like OpenAI thinks that that time is super far
*  off. Like, you know, I'm not a big betting person, but I would bet that Holden Karnofsky is going to
*  be involved in setting up some sort of, you know, third party standards org. And they're going to
*  partner with OpenAI and there's, you know, they're going to make a push for this.
*  So like, it seems like we should update on what they're thinking, right? I mean, certainly the
*  people that know the most about this, there's a lot more that they know that they haven't published.
*  And they are not necessarily, they're not trying to close the door behind them,
*  but they are saying beyond where we have gone, we think there's danger. We see that behavior is not
*  easy to predict, even though we can predict a smooth loss curve. We don't know what that means
*  in terms of discrete thresholds that we've reached or like, you know, specific behaviors
*  that we might observe. And so therefore it seems like going beyond this point, you know, we plan
*  to proceed with extreme caution. We think the world should proceed with extreme caution. We think there
*  will need to be some sort of regulation. So like, I don't know, it seems like everybody should kind
*  of be able to get together on like, yeah, we're entering into some pretty uncharted, like pretty
*  dangerous territory. The developers themselves are saying so. So like, again, why not just a little
*  pause? Because a little pause is never a little pause. That's my biggest concern with it. I mean,
*  the letter kind of skirts this, right? But like, there is one question would be government regulation,
*  but another question would just be like, do you choose to do it? You know, I mean, if I was running
*  like Google and I was, you know, on top of all the world's compute resources,
*  like, I think the right decision for me would be to not, you know, scale up 100x compute beyond
*  GPT-4. Because what OpenAI is telling me is like, they don't have great predictability. I know that
*  I don't have great predictability. So, you know, what the government may make me do could be a
*  distinct question. But, you know, for a handful of like, key decision makers in the very few
*  organizations that have the resources necessary to go past GPT-4 today, for those people, like,
*  what do you think they should do? Like, it's just, you know, voluntarily, they can not go further
*  right now, if they want to. And, you know, that's kind of the start of the letters. We call on these
*  people to not go further right now. You know, do you think they should, it's separate questions
*  say should we force them to heed that call? But maybe we could still say we think they just
*  should heed that call, even if we're not ready to like mobilize government to force them to
*  heed that call. I still think it would set a precedent and the temptation would be to extend
*  the call. I also don't know if you believe as I do that the performance of these models is
*  mostly compute bound. How far does the little puzzle extend? Do you also ask for a little
*  puzzle from Nvidia to build more GPUs and from Microsoft to build bigger data centers and
*  Nvidia to develop the next generation of GPUs? Because if not, then really all you're doing is
*  you're growing the compute overhang. And the moment you stop the puzzle, you pass for six months,
*  and the moment you stop the puzzle, all of a sudden, boom, you bump up to where you would
*  have been without the puzzle. So that may be even more dangerous. So again, I tend to deeply mistrust
*  the instinct of let's pass technology, let's slow down. It's never been that well before.
*  The folks who've said that have always been on the wrong side of history. And I think the upside,
*  Anton is right, we never talk about the upside of this AGI, which is like, this can be really
*  fucking good for humanity. This could be a hugely positive deal. We've been talking this whole time,
*  but it's going to kill us all. Let's talk about the upside for a minute, because it seems like
*  we all agree that more likely than not, it's going to be the upside that materializes.
*  It'd be really bad to miss out on that upside. And I think there is totally a chance that we do. I think
*  we technologists assume that technology by default proceeds, but sometimes it pauses. By default,
*  it pauses. It's a miracle when it proceeds. And we've had precedence in history, the middle ages,
*  when technology paused for a thousand years or two thousand years. And I really don't want that
*  to happen. I think we're getting close to AGI. We have the right institutions now. We have the
*  right setup. Let's keep going and let's go after the prize. Nathan, another way of framing what
*  I'm hearing from Flo and Anton is there's asymmetric downside to pausing. There's very low upside,
*  because what is six months really going to do? And there's downside that six months then sets
*  a precedent that it expends a lot longer than six months, or an adversary catches up and doesn't
*  follow the cultural or legal rules that we set or some other downside could occur. Do you
*  differ from that in that you think that the upside is actually... You think we could figure
*  something out in six months that would really make it worth it? Or you think it's OK if it
*  extends out? Or where do you not see the asymmetric downside? Well, I just have radical uncertain
*  t about what to expect. The question is, where is the burden? We all have radical
*  uncertainty. The question is, where is the burden of proof? And so is the default under radical
*  uncertainty, don't do anything? Or is the default, I mean, block everything or just keep going?
*  Like, where is the burden of proof? Radical uncertainty is just indefinite pessimism.
*  Let's get certain about some things. Let's get certain. Let's make some good assumptions.
*  What should we be doing as engineers? I certainly have a lot of enthusiasm for
*  the technology. And I do think that there's tremendous upside in our near term future.
*  And ultimately, my position as a member of the Red Team and all that stuff is like,
*  for all the crazy shit I saw, and it did kind of freak me out. And it definitely has me convinced
*  that this technology is not safe by default. It's not just easy to align. None of the
*  most optimistic scenarios about AI safety seem true to me. Nevertheless, I do think
*  GPT-4 should be deployed. It should be used. It will be great. It will have real downsides and
*  harms. But I think this will be greatly outweighed by the upside. But I think it all kind of comes
*  down to like a threshold effect. And I think I'm finding the most clarity when I think about this
*  from the standpoint of if I were a decision maker myself, and it was up to me to determine
*  should I run a larger training run now than GPT-4, as we approach this threshold of potentially
*  smarter, more powerful intelligence than human, I think I come to the conclusion, no,
*  I should wait. What happens in six months? I don't know. Maybe I decide to wait again.
*  That definitely could be the case. I don't think that's insane by any means. And that, honestly,
*  might be my most likely expectation. Again, I'm imagining here I am Sundar, I am Satya,
*  I am Sam Altman. I would say, yeah, I probably still don't know that I would feel confident
*  proceeding in six months. But who knows what we might find? We might find lots of great
*  mechanistic insights. We might find that China is amenable to a deal. Everybody sort of assumes
*  that China is going to create large language model AGI if we don't. I don't know what China
*  is going to do. I have scant ability to predict. I did not anticipate. I mean, who has made the
*  right predictions about China? Did anybody see them reversing COVID policy from total lockdown
*  to total free-for-all over a weekend? I don't think so. So now we've got all these AI-derived
*  China experts running around saying what their technology policy is going to be.
*  I don't think that's very credible at all. And they also shut down their own video game industry,
*  and they shut down tutoring. They brought their whole technology. Jack Ma hasn't
*  in front of a microphone in recent time. So I don't think that they are going to let
*  the Sam Altman of China make the decision. And I think they're going to want some better assurances
*  than we've been given in the West that this is all going to be fine. So maybe they're not going to go
*  so crazy. Maybe they're going to see this danger and say, shit, this looks insane. Maybe we should
*  slow down, especially if then they could also point to, look, the West seems to be slowing down.
*  That would make it a lot easier probably for them. I kind of wish we hadn't declared chip
*  war on them just as we're entering into an AI arms race. Some say that gives us a leg up in
*  the AI arms race. I say, let's avoid the AI arms race entirely. So I don't know. That's my China rant.
*  But yeah, if I'm in the CEO seat at any of these companies and I have the compute,
*  and it's up to me to say, should we do this right now as we seem to be approaching some critical
*  thresholds and given the level of predictability that we have, I might resent it if the government
*  told me I couldn't. But in my own private decision making, I think that the wise, prudent answer
*  that's pro-social is real caution and I think that can easily cash out to a little bit of a pause.
*  I think in my case, it would depend on whether I see a road map from the safety team.
*  If the safety team comes to me and they're like, we need a pause for six months, tell the capability
*  guys to stop. And I'm like, what are you going to do for six months? Do they have a road map?
*  Do you feel like progress is being made? Yeah, I guess. Yeah. I mean, I think this is really
*  we're coming down to this point. It's like, stop being indefinitely pessimistic. Figure it out.
*  Right. Let's believe that we can actually figure this out. It's too easy to say,
*  yeah, it's going to have arbitrary capabilities as an adversary. It's going to be unpredictable.
*  Where we don't know, like, because there are things about the world that we don't know,
*  acknowledge it may know those things before we do and use those against us. Okay.
*  But there's still that danger power spectrum. We're currently in a place where we control the
*  power that it has. Even if it was to be as dangerous as even the worst doomer says,
*  we still control that lever, right? We still control how powerful it can actually be to act
*  in the world. And that's probably the thing to be focused on. If you're going to be working on real
*  safety. It's like, okay, well, it's not thinking about like what coded messages is it going to
*  send to like get people to let it out of the box. It's literally one of the affordances that
*  this thing has to do things in the world. How do we lock those down? And it's like,
*  it doesn't have to be an air gap. Again, Eliezer did this experiment with Mary a long time ago,
*  where he like got people to let him out of the box as well, playing a super intelligent AI.
*  Of course, the actual conversations were never revealed. Unclear. But even that is like, okay,
*  great. So you did that. Then what? Like we have plenty of ways to like prevent people from doing
*  things in the world. Our society is kind of predicated on our ability to prevent people
*  doing things. So let's sort of tackle the real risks. I think Flo's conception is pretty good
*  here. Like, okay, six months, give us a roadmap. Why six months? What are you going to do? That's
*  what, you know, then I would be more amenable. I'd be like, okay, well, fine. You know, okay,
*  I can probably wait six more months till GPT-5 maybe. But it does come with this risk. It does
*  come with these asymmetric downsides. It does come with like, oh shit, well, I guess they will stop
*  if we tell them to. Or it's like, oh, like, all I have to do is create enough like mimetic anxiety
*  around the concept and then we'll have a moratorium. Like these are difficult. These are not things you
*  get for free. The pause is not free. And there are things that we have to grapple with.
*  I do agree that the pause is not free, you know, just to be intellectually honest about that. Like
*  there is opportunity cost, you know, or foregone upside potential at a minimum. That's one of the
*  reasons that I, you know, I take heat on both sides of this because the most strident AI safety
*  people accuse me of being a hype man and, you know, cheerleading this technology that's going
*  to kill us all. And then of course, the, you know, the people that want to accelerate, you know,
*  accuse me of being a doomer. And I do think it's important to kind of emphasize both sides because
*  I think the reason the pause, at least in the public consciousness, I mean, you guys are
*  are obviously read into this, but in the broader discussion, people haven't felt anything from AI
*  yet. And or almost nothing like they've seen news, they've seen a couple demos, but like
*  the actual economic impact, the deployment is just getting underway. So I really think it's
*  important to emphasize to people that we have so much potential already. We don't, it's invented,
*  it exists, you know, now we are in this deployment phase. And I really do think this AI summer concept
*  is great. You know, we can have tremendous improvement, you know, tremendous,
*  tremendous gains to our standard of living to, you know, with the AI doctor for the global
*  poor. I mean, it's right there within our grasp and it doesn't require any new invention, right?
*  It just requires refining what we have, deploying what we have, adapting to what we have.
*  So, you know, we could do that in the next six months. We could be more ready for GPT-5 than we
*  are right now. We will, you know, deploying it at global scale and actually seeing, you know, what
*  it does wrong, like seeing if they can patch my shit, you know, that's another thing I'd really
*  like to know. I've got some tickets in that I would like to see patched and they've not been
*  patched. So, you know, can the developers, you know, demonstrate some improvement on the safety
*  profile? Like that's part of the roadmap. I know they're working on it, but, you know, progress is
*  not what I would hope that it might be. In the end, you know, yes, I want GPT-5 to at least the
*  good version of it. But sitting, you know, if I'm in that chair and I'm sitting on that compute and
*  I'm like, am I going to put this, you know, potentially over this threshold with this next
*  run? And then on top of that, I have to decide a number, right? I have to be like, well, how big is
*  this run going to be? Am I going to go 10x more compute than GPT-4? Do I just say fuck it and go
*  100x? Do we really eac our, you know, our way here and go a thousand X compute past GPT-4? Like
*  at some point I'm like, wait a second, I'm getting crazy. We haven't even deployed what we have,
*  you know, like why do we need to create the next version when we haven't even understood or deployed
*  what we have, which we know is going to be transformative. Let's wrap on this. This has
*  been a great discussion. Anton, you quoted Stalin earlier. It's no coincidence that Nathan was on
*  the red team and now is advocating for government control. If we can just get a few stakeholders to
*  agree, then the government doesn't have to do anything. It honestly would be best. Really,
*  I think, I mean, I think that is a key point. You know, the, I don't want to see the government
*  muddy this thing up. Like that's not good. But key people can just make a call and it's, you know,
*  it's totally within their discretion to do that. And, you know, nobody has to, the state does not
*  have to be a part of it necessarily. Yeah. That would be, that would be preferable if that, if
*  there's going to be a pause. This has been a great discussion. Flo, Anton, Nathan, thank you so much
*  for joining. Appreciate it guys. This is fun. Thank you so much. Thanks for having me on.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
