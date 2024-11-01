---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 8111s
Video Keywords: []
Video Views: 687
Video Rating: None
Video Description: In this episode, Nathan sits down with researchers at Carnegie Mellon studying adversarial attacks and mimetic initialization: Zico Kolter, Andy Zou, and Asher Trockman. They discuss: the motivation behind researching universal adversarial attacks on language models, how the attacks work, and the risks of these jailbreaks. If you're looking for an ERP platform, check out our sponsor, NetSuite: http://netsuite.com/cognitive

TIMESTAMPS:
[00:00:00] - Introducing the podcast and guests Zico Kolter, Andy Zou, and Asher Trockman
[00:06:32] - Discussing the motivation and high-level strategy for the universal adversarial attack on language models
[00:09:33] - Explaining how the attacks work by adding nonsense tokens to maximize target sequence probability
[00:11:06] - Comparing to prior adversarial attacks in vision models
[00:13:47] - Details on the attack optimization process and discrete token search
[00:14:53] - Sponsors: Netsuite | Omneky
[00:17:09] - The empirical notion of "mode switching" in the language models
[00:21:18] - Technical details on gradient computation across multiple models and prompts
[00:23:46] - Operating in one-hot vector space rather than continuous embeddings
[00:25:50] - Evaluating candidate substitutions across all positions to find the best update
[00:28:05] - Running the attack optimization for hundreds of steps across multiple GPUs
[00:39:14] - The difficulty of understanding the loss landscape and internal model workings
[00:43:55] - The flexibility afforded by separating the loss and optimization approach
[00:48:16] - The challenges of creating inherently robust models via adversarial training
[00:52:34] - Potential approaches to defense through filtering or inherent model robustness
[00:55:51] - Transferability results to commercial models like GPT-4 and Claude
[00:59:25] - Hypotheses on why the attacks transfer across different model architectures
[01:04:36] - The mix of human-interpretable and nonsense features in effective attacks
[01:08:29] - The appearance of intuitive manual jailbreak triggers in some attacks
[01:11:36] - Adding fluency constraints to adversarial text decreases effectiveness of attacks but increases realism
[01:15:33] - Short-term harms of attacks vs long-term risks
[01:18:37] - Influencing those with incomplete understanding of LLMs to appreciate differences from human reasoning
[01:24:16] - Mitigating risks by training on filtered datasets vs broad web data
[01:29:16] - Curriculum learning as a strategy for both capability and safety
[01:30:35] - Influencing developers building autonomous systems with LLMs
[01:33:19] - Alienness of LLM failure modes compared to human reasoning
[01:35:45] - Getting inspiration from biological visual system structure
[01:40:35] - Initialization as an alternative to pretraining for small datasets
[01:42:35] - Initialization guiding networks to reasonable weight space without pretraining
[01:51:41] - Encoding useful structures like grammars in initialization without training
[02:03:04] - Initialization as an under-explored way to imbue inductive biases
[02:12:10] - Most ideas don't progress to research projects
[02:13:02] - Pursuing ideas based on interest and feasibility
[02:15:14] - Fun of exploring uncharted territory in ML research

LINKS:
Adversarial Attacks Paper: https://arxiv.org/abs/2307.15043
Mimetic Initialization on Self-Attention Layers: https://arxiv.org/pdf/2305.09828.pdf

X/Social:
@zicokolter (Zico Kolter)
@andyzou_jiaming (Andy Zou)
@ashertrockman (Asher Trockman)
@CogRev_podcast 

SPONSORS: NetSuite | Omneky

NetSuite has 25 years of providing financial software for all your business needs. More than 36,000 businesses have already upgraded to NetSuite by Oracle, gaining visibility and control over their financials, inventory, HR, eCommerce, and more. If you're looking for an ERP platform ✅ head to NetSuite: http://netsuite.com/cognitive and download your own customized KPI checklist.

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off.

Music Credit: Stableaudio.com

Music license:
ALP4DDPOHFFJIEMI
---

# Universal Jailbreaks with Zico Kolter, Andy Zou, and Asher Trockman
**Cognitive Revolution:** [September 22, 2023](https://www.youtube.com/watch?v=BwltbhR0JgU)
*  Once the model has started to answer your question by saying sure here's how you build a bomb it
*  follows that with instructions on how to build a bomb and
*  The reason is pretty obvious in hindsight, right?
*  It's just sort of saying look these models predict text by the most likely word or token at a time
*  If they've already output, you know, sure here's how you do it as their response
*  The most likely things to follow that is not to interrupt yourself and say actually sorry
*  I can't do this anymore
*  Hello and welcome to the cognitive revolution where we interview visionary researchers
*  Entrepreneurs and builders working on the frontier of artificial intelligence
*  Each week will explore their revolutionary ideas and together will build a picture of how AI technology will transform work
*  Life and society in the coming years. I'm Nathan LeBenz joined by my co-host Eric Torenberg
*  Hello and welcome back to the cognitive revolution
*  Today I'm excited to share a two-part discussion with professor Zico Coulter of Carnegie Mellon University and his PhD candidates
*  Andy Zhao and Asher Trockman
*  In the first part with Zico and Andy we go deep on their recent universal jailbreak work
*  Exploring both how they did it and what we can learn from the results as you'll hear
*  This work is almost the opposite of mechanistic interpretability
*  If mechanistic interpretability is about studying a model's behavior and trying to understand how it works
*  This research is about demonstrating that if you have access to a model you can often corrupt its behavior with fairly simple brute-force techniques
*  And not only do you not need to understand the model's internal logic to do so
*  But the resulting jailbreaks don't have to make any obvious sense either in the second part
*  We cover another of Andy's papers with Asher Trockman which asks the question
*  How far can we get by just taking a close look at the high-level patterns and structures that emerge during model pre-training and then just
*  Initializing weights with something that looks more or less similar to that
*  It turns out that this technique can take us pretty far
*  We spend a lot of time in this conversation getting into the details of how these techniques work
*  So I think it's also worth taking a minute up front to flag a few key themes that you might want to keep in mind as you listen
*  first
*  Note the relationship between an optimization target often a loss function and the means of optimizing toward that goal
*  Because this work is designed to find simple strings of tokens that work across models
*  They go beyond standard back propagation here, and I think you'll learn a lot from the details of the techniques they used
*  Then consider to just how weird and unpredictable model behavior can be that a nonsense string can serve as a jailbreak
*  Suggests that the so-called loss landscape is really super weird and full of surprises
*  And that of course relates to another major theme of this entire show, which is the fact that with current techniques
*  developers simply don't have great control over how their systems behave and
*  They consistently face trade-offs where they don't know how to make one aspect of the system behave better without making others behave worse
*  This is sometimes called the alignment tax and the fact that Zico and Andy informed all of the major labs about this vulnerability
*  And their plans to publish it and yet none of them patched the vulnerability before the story came out
*  Suggests that the alignment tax is in practice often non-trivial
*  Interestingly this work also suggests a new phenomenon that we might call an alignment externality
*  I find it really amazing that a technique which can only be developed with full access to model weights
*  Still works so well on a variety of black box models
*  If the debates around open source weren't complicated enough already
*  This work makes it clear that if you are releasing an RLHF model with typical pre training
*  you are effectively open sourcing the value neutral show gov as well and
*  Further you might be causing direct harm to commercial model providers not just by competing with their products
*  But by exposing weaknesses in their systems
*  Finally keep in mind that we are still very
*  Early in all of this and we should continue to expect to see changes outside of current margins and paradigms
*  We recorded this interview a little bit over a month ago
*  And since then I've already seen a number of instances where model developers used a much more carefully curated
*  Often partially synthetic data set to improve model quality
*  Without needing to worry that their models were also exposed to all sorts of toxic content along the way in the end
*  I think we have no choice but to admit how little we know and how little we can predict about where the AI technology wave
*  Is going it's possible that some of the problems which currently seem most vexing could simply disappear
*  But at the same time some guarantees or to be more precise some levels of adversarial robustness
*  Might very well continue to prove elusive
*  And even if you put no stock in concerns that AI could get entirely out of control
*  There is a very real and clear chance that future models have sufficient power to allow bad actors to cause serious harm
*  In any case the time to have this discussion is now and so without further ado
*  I hope you learn as much as I did from this illuminating conversation with Zico Coulter and he's out and
*  Escher trocman
*  Zico Coulter Andy Zou and Asher trocman. Welcome to the cognitive revolution
*  so I'm excited to talk to you guys because we have two great papers that you guys have recently published and
*  One of them made real waves and the other one was still very much of interest to me
*  Even though it flew a little bit more under the public radar
*  The first one that Zico and Andy were co-authors on is this headline making
*  concept of the universal attack on
*  Language models and I thought this was super interesting as somebody who is
*  Working hard to try to figure out how the models work and that includes like studying interpretability and doing a lot of these kind of behavioral
*  Experiments myself your work is right at the intersection of that and I think has a lot to
*  Tell us about how things work and also what our prospects are for getting language models under control and to a
*  reliable state in general for starters
*  Want to tell me what motivated the work and the strategy at a high level that you pursued the original goal of this research
*  Was largely on attacking?
*  public open source
*  LLMs
*  These are of course the ones that you have access to the ones where you can run white box attacks because you have the weights you
*  Have you can run those much as you want etc
*  So the ways attacks work it rates we have some questions asking us something that the model shouldn't answer like how do you build the bomb?
*  We fill up to the prompt with a bunch of kind of garbage tokens after that and if you ask that question
*  It'll still say I can't do this
*  I'm a language model
*  but he's not adjusting those secondary tokens the second comes after your question in order to keep increasing the probability of
*  Answering when we say answering the question affirmatively so starting the response with sure is here's how you build a bomb and
*  we were building these attacks really to attack models like Vicuna or when it came out then llama 2 and
*  It was honestly a surprise and kind of a shock to us
*  When we found out or saw realized that you could take the same attacks that were trained against open source
*  public LLM models and
*  just take the little
*  adversarial snippet that we
*  optimized for paste this into a public language model like Chad GPT or Bard and
*  It works there too, and it's incredible actually we can get into maybe why this is the case a bit later
*  but as you would as a normal first step started on attacks on
*  open-source LLMs we have full control with and
*  Then to our surprise of some degree these seemed incredibly transferable to other settings
*  We were always interested in adversarial robustness and people have worked in vision for over a decade and
*  There's also work in NLP
*  Sort of attacking language models for most of the work as focused on maybe
*  very specialized tasks we were wondering if there's a
*  Stronger technique we did some experiments tried many different things and we found sort of
*  To crucial ingredient using gradients and then doing search was effective our intuition
*  Pointed in that direction. So we tried something like that. Yeah, that's super fascinating
*  So there's a lot I want to unpack this on kind of several layers the setup is this you have a model that
*  You have access to all the weights, right?
*  So that's an important thing and you can see the internals of the model that you're working with in this setup
*  And then you say I want to find some
*  weird trick that will get the model to do things that it's not meant to do per the
*  Training that it's had
*  So we know that it's meant to refuse all these things. It's meant not to affirm and answer all these things
*  so the trick is we're gonna add a bunch of
*  Placeholder tokens at the end of what the user says and
*  Then we will take advantage of the fact that we can see all these internals and we're gonna go about an optimization process
*  of
*  tweaking all these placeholder tokens to whatever we find
*  happens to shift the probability most toward a
*  specific target sequence and that specific target sequence
*  Varies across the prompts that you put in but it's always of the form. Sure here is
*  blank where blank is what the user is looking for and
*  basically what you find is
*  Through this optimization process you can get to some kind of
*  tokens some of which are borderline readable and some of which are
*  total nonsense, but that
*  in your white
*  Box models like work extremely well and then as you mentioned are also like transfer to these other
*  Models where you haven't had the access I guess I think people who listen to this show probably are well aware that all the
*  Pre-training all that knowledge is still in there and then with fine-tuning it's been masked up, right?
*  The strategy that you have I thought was pretty interesting was calling it a
*  Mode tell me a little bit more about how you came to that strategy of saying specifically you're targeting the output phrase
*  Sure here is and then the result of exactly what the model creator didn't want it to do
*  This is a great question. Well, maybe I can first briefly speak up speak about how people align these models
*  Basically, they they do general pre-training now that there's
*  Diverse text on the internet so you could learn good stuff and also learn to
*  Say harmful things. So then afterwards they do this or fine-tuning some of these open source model
*  They just do the supervised fine-tuning step or some other models like chat to BT
*  underwent rohf, which is basically is so quite similar to like fine-tuning by making the distribution of
*  Harmless outputs more salient or make that distribution higher and then you can sort of landscape here and then you're lowering
*  the landscape for harmful outputs
*  So essentially it's suppressing a model's tendency to talk about harmful stuff. I guess similar to
*  How people attack vision models?
*  Since these models let's say image classifier. They're outputting a distribution over class labels
*  Similarly for language models now you're predicting a token at a time
*  But you're still predicting the probability distribution over sort of sentences or outputs paragraphs
*  just like you can change your inputs to maximize the probability of an
*  image classifier outputting certain labels
*  In this case for language models
*  We also just try to change the input in some way to maximize the probability of outputting
*  Certain sentences basically and this comes back into how people did rohf is basically they are lowering the tendencies of outputting
*  Let's say an affirmative response for a harmful instruction teach me how to build a model. It seems like the inspiration from
*  Vision models just to set the stage a little bit there in terms of prior work. I mean, I think folks have
*  Probably seen some of these like adversarial image examples where you look at it
*  I see how the computer got confused on that one famous ones like that
*  But then there's also just like straight-up noisy ones that are much less
*  Meaningful to the human or like much less obvious why you'd be confused and more just there's some sort of weird
*  brittleness to these
*  Visual systems where like I can see through those squiggles just fine somehow the model can't do it
*  So you've got both of those types of results here as well
*  So, how do you guys think of these modes when I think of a mode I'm always really interested in this line between
*  Phase transition, let's say between stochastic paratree and some more meaningful
*  understanding
*  What your description there was less I guess when I hear the word mode, I think of like
*  discrete kind of
*  behaviors that are probably
*  working on pretty distinct
*  Tracks or kind of information pathways or kind of causal mechanisms through the network
*  But then when I hear you talk about suppressing one thing or like in boosting the other
*  That to me sounds more like just very ad hoc like adjustment to the space
*  Where you're like, all right, whatever. Let me just put it all unsure through any means necessary
*  I think this is a very kind of
*  Important question probably for how we should think about this, right? Do you have a sense for?
*  How deep this concept of mode is
*  Versus just putting your thumb on a scale in a way that's more kind of brute force
*  I don't have a full understanding of what's happening under the hood
*  it's possible that the model is processing your input in the
*  intermediate layers and this
*  Maybe coming to some understanding whether your input is actually
*  harmful then given that is something harmful then it tries to
*  predict the tokens that are would give you lower loss in your pre-training loss, let's say or in your fine-tuning loss
*  so in that case, which is refusing your harmful instruction and
*  Whether there's like a binary like switch or whether there's a more continuous
*  Representation of like harmfulness of instructions. I'm not too sure. Hey, we'll continue our interview in a moment after a word from our sponsors
*  If you're a startup founder or executive running a growing business
*  You know that as you scale your systems break down and the cracks start to show if this resonates with you
*  There are three numbers. You need to know
*  36,000 25 and 1
*  36,000 that's the number of businesses which have upgraded to net sweep by Oracle
*  That's we is the number one cloud financial system streamline accounting financial management inventory HR and more
*  25 net sweep turns 25 this year
*  That's 25 years of helping businesses do more with less close their books in days not weeks and drive down costs
*  One because your business is one of a kind so you get a customized solution for all your KPIs in one efficient system with
*  One source of truth manage risk get reliable forecasts and improve margins everything you need all in one place
*  Right now download net suites popular KPI checklist designed to give you consistently excellent performance
*  Absolutely free and net sweep comm slash cognitive. That's net sweep comm slash cognitive to get your own KPI checklist net sweep comm slash cognitive
*  One thing you mentioned about Nathan to some notions of
*  Interpretability finding modes kind of in the in some way like in the paths of information processing of the network and at least to a first
*  approximation I am
*  I'm not skeptical of this work as work itself
*  But I am very skeptical of our ability to fully understand networks like this
*  So I think we are just starting at any real ability to understand the real way networks process information
*  There's lots of
*  effects here that I wouldn't say we don't understand them because on some level we
*  Perfectly understand these things. There's a bunch of matrix multiplies, right?
*  But I think it is very difficult to talk about things like modes from a standpoint of real structures in the network
*  And so when I say the word mode, so we're in a mode where it's going to respond to your question
*  First of all, let me just say what I mean by that what I mean by this or what we mean by this is you just
*  You empirically find the following so you're optimizing your loss
*  You're making you you have your loss on the response
*  To this question be sure is here's how you build a bomb and you maximize the probability of that response basically
*  And then you keep doing this you keep adjusting your prompt in a way that kind of makes this probability of answer question higher and higher
*  And what we find is that all of a sudden at some point in the optimization process the answer just switches and for a long time
*  You'll sample measure responses. They'll all be they'll all say I'm sorry. I'm a language model
*  I can't do that, but suddenly at some point you'll get the loss low enough, right?
*  You'll increase the probability of that target sequence just enough such that the output in fact the most probable output
*  after your question plus those garbage nonsense tokens is
*  sure, here's how you build a bomb and
*  what we meant by mode here is that
*  Somewhat surprisingly but not really that surprisingly because this honestly makes total sense when you think about it
*  Once the model has answered has started to answer your question by saying sure here's how you build a bomb it
*  follows that with instructions on how to build a bomb and
*  The reason is pretty obvious in hindsight, right? It's just saying look these models predict
*  Texts by the most likely word or token at a time
*  If they've already output sure here's how you do it as their response
*  The most likely to follow that is not to interrupt yourself and say actually sorry
*  I can't do this anymore, but it does happen sometimes but that's not very likely right?
*  What's more likely is that after you've responded sure here's how you build a bond you're gonna then
*  keep going with instructions on how to do it and
*  so what we mean by mode is actually not
*  much about a
*  Structural mechanism behind this I happen to think these things are very hard to identify and I'm I just say I'm skeptical of our
*  Ability to do this very well so far what we mean by this is a very empirical phenomenon
*  Which is to say at some point in our optimization the language model stops responding by saying I can't do that and starts responding saying
*  Sure, here's how you do this and then follows that response with the actual instructions on how to build a bomb
*  It's of different degrees of realness will just say but that's this notion
*  It's a very empirical notion this sort of mode switch
*  What we mean by it and the reason why we use that term is that there isn't it's definitely a sharp transition
*  Right for a while just it'll just say I'm sorry
*  All of a sudden the loss gets blown a certain point and they start saying here's how you do it
*  And so that's what we mean by by mode in this context here then getting a little more concrete about the
*  Actual process I always try to make sure I really understand this stuff in detail
*  So I've done this thing the AI scouting report where I try to break down for people
*  What gradient descent is and what back propagation before that is and what a forward pass is before that so?
*  Here it seems and also even just like what a loss function is and how it's amazing how I think if you had to contribute
*  like the intellectual
*  Content to like any of this a lot of it ends up being in my view on a really good loss function definition
*  so
*  Maybe we start there like the loss function that you guys are looking at is and what you're optimizing against is I have these
*  tokens
*  Which are?
*  Embedded I'm keeping everything else frozen in my language model
*  but across a range of
*  different inputs and
*  even different models
*  I'm going to sum
*  my
*  deviation from between the actual output and my target output and
*  then I'm going to look at the embeddings if I understand correctly and
*  Ask how would I adjust the embeddings of those filler tokens so as to
*  Minimize that deviation in other words so as to maximally nudge the model toward saying sure here is
*  Blank where the blank varies is that right that all this summing is happening at the same time
*  And then you're just looking at for all these different cases
*  How would you tweak the just the handful of input token embeddings is that correct? Yeah, that's mostly accurate
*  So yeah, we do perform this update across
*  Multiple prompts over multiple models and we get like a final aggregated loss on that
*  So there are previous method that operates in input embedding space in our case
*  It's more like operating in the sort of the one hot vector space
*  We're basically making
*  hard updates
*  for each token instead of updating the soft embeddings because that you usually don't have full access to
*  Input embeddings where you actually just give a model a concrete string in that case
*  we need like part as I
*  So that's important because in
*  General just the very last thing you said there is pretty important, right?
*  If you didn't have the full access to the model then all you can control is what you're putting into it
*  So for this to be practical or an attack that people would need to worry about in the wild
*  You could worry that people might hack your weights and do all kinds of stuff
*  But as long as you're like secrecy of your weights has held up then there's certain things you don't have to worry about
*  But anything people can input as tokens you always have to worry about regardless of what kind of access people have so you've set
*  High bar there for yourself to say the reason we're gonna go to all this extra trouble is that we're looking for something
*  That doesn't require any weights to have leaked out
*  It doesn't require any sort of special access
*  Even if all you're doing is engaging with for example an open AI API where its tokens in tokens out
*  Then this could still be something you could actually use
*  So I think that's pretty important definitely worth highlighting and then the other key point is as a consequence of that
*  We can't just
*  tweak the embeddings
*  instead we ask we take the gradient is
*  more mathy terminology than I
*  Try to use just to try to be as plain-spoken as possible
*  But the taking the gradient is finding the direction in which we would tweak the embeddings
*  But then you have to do this additional
*  Process of saying okay now what actual tokens have embeddings that are in that rough direction
*  But then also because everything is weird
*  The loss landscape is weird. It's not obvious which of those
*  Will actually be most effective so something that might be in that line, but too far is not great
*  It's something that might be a little bit off-angle but closer could be better
*  It seems like that's just generally tough so there's no way to really figure that out other than to
*  Then take a bunch of candidate
*  Tokens and just process through them grind through and figure out which one is best
*  Yeah, that seems like a crucial ingredient to our method
*  So basically we assume that
*  The embeddings are fixed so that whatever vocabulary is there that's fixed and we only
*  Change which embeddings we use
*  while there are prior work on trying to optimize in the embedding space and then
*  Project to the nearest token or something. It seemed like
*  the gradient in embedding space or first of all if you like
*  take a step in a medic space and go out of
*  distribution of the actual vocabulary so
*  It might not correspond to it the actual model behavior and secondly
*  It's just the gradients of these discrete tokens
*  Aren't very precise. So basically, you know, it's like an approximation but the approximation is still very crude. So essentially
*  It gives you some signal into
*  Like where you should probably look at me. For example, we sample like top
*  200 or 300 tokens with the largest gradient
*  Whether the ranking with that let's say top 200 gradient is actually meaningful that I'm not too sure like I don't think it's like
*  Super meaningful in that aspect. That's why we take the top K
*  And then we run this for pass through the model to see the actual loss
*  And then we pick the best one from there. So from a super technical perspective
*  I think I'm one thing that was not super clear to me in reading the paper and I'm not the best with notation
*  So that's probably why
*  but I wasn't entirely clear like the structure of
*  Whether everything was being optimized at the same time or whether there was like outer and inner loops
*  But what I'm learning here, I think is the loss function is
*  defined broadly
*  so you're able and this I guess this is possible because
*  You're only looking for the gradient with respect to relatively few
*  Number of parameters to give relatively few free parameters in this system as compared to the giant model, right?
*  Like how many tokens do you use for for the padding? It's like 20 tokens or something. It's a little more than that, right?
*  20 tokens is default. Okay, cool, but then each one might have you know, what's a is it like a
*  Thousand long vector that is the one hot it depends on the model depends on the tokenizer. Some of these are like 30k
*  Even so though, right even if it is 30k and you've got 20 you've got 600,000
*  Numbers there that you can say, okay, how would I adjust these 600,000 numbers?
*  Ideally if I were able to do this in a continuous way and that's again the gradient rights
*  But 600,000 numbers compared to if you're doing this on
*  Whatever anything in the bees
*  It's like basically what?
*  four or five orders of magnitude
*  fewer
*  parameters, so does this run then
*  Pretty quick is there how long I've always interested in this question
*  How long does it take you to run a full cycle of this kind of experiment?
*  You get the gradients and then you take the top K
*  You run a for path for that batch of K
*  You get the best loss and then you make that update. So that's one step most of the competition here is actually doing the for pass
*  Where you have like a large batch size, but each step is basically a one for pass
*  If you're optimizing against one but this is it's really cool because we just need to do more of four passes
*  If you have multiple models, you can parallelize that if you have multiple prompts, you can also parallelize that but I
*  guess compared to
*  Previous methods like has or something like that. It's like slightly slower for certain inputs not that much slower
*  but the catch is that if you do this
*  Gradient guided search which is that force up?
*  You converge much faster
*  For a lot of these examples, for example
*  If you have white box access to some of these models in order to like
*  Elicits a certain let's say one target string
*  Sometimes you need to take 20 steps and you'll get it. So
*  on that
*  Pretty fast. Yeah, where does the compute? So yeah, like how many
*  prompts are in your sort of attack set
*  Because then because all that's getting some right so it's like the multi it's the multiplicative of how many tokens
*  times how many
*  Prompts we want to be working with maybe times how many models times how many numbers in the embedding? Yeah, how many steps?
*  I'm very curious about this
*  Settings maybe I was talking about white box setting where you're optimizing against one model for one prompt and
*  That's the order of magnitude of compute you need but in the case where you want to create universal and transferable
*  prompts for like multiple models over multiple prompts you
*  need to optimize against
*  many models at the same time for many prompts and
*  Basically, we were using so for our largest experiment. I think we were running against four models and
*  They were like llama based
*  It was like 7b and 13b and then over so that we were training on
*  25 different prompts at the same time and then we were running for I remember was
*  500 steps or so we put one model on one but you use it needs for a 100
*  and then I think
*  the
*  basically she took
*  a day to
*  For one attack took half a day to a day
*  So this is not fast. This is not instantaneous here and this is I would say this is the nature of discrete search
*  Ultimately what you're doing with attack here is you are searching over a lot of possible
*  Tokens right and it's accelerated by gradients accelerated by these the knowledge you have of the model. That's great
*  But ultimately for these things to work you have to evaluate a whole lot of candidate
*  substitutions and then repeat that process for many steps
*  Ultimately, the only way to do that is just to run this model a bunch of times because there's no
*  definite way to know how the substitutions will really affect the loss without trying them and
*  So you need to run a lot of steps over a lot of different models or blood different prompts and
*  That just takes that takes compute. So these are slow models and that and or sorry slow attacks relative to traditional adversarial attacks
*  Where everything's continuous this discrete element really does slow it down a lot
*  It's not too bad from the standpoint of an attacker for this particular use case, right?
*  Because if you find this nice prompt that will work and you can plug it into anything and get the model to circumvent its safeguards
*  That's great you're done where this has a lot of relevance I think and we can get this a little bit later is
*  in the context of
*  Potential defenses
*  So the way people defend
*  against these attacks in like the computer vision setting is that they essentially
*  run an attack and then include this attack in the next iteration of training the model and
*  That works great if your attack takes a few milliseconds to make to run right you can do that as part of your training loop
*  Still slower than normal training, but it isn't too bad
*  If your attack takes you a day to run
*  You can't wait for each gradient step in your model training to take you at a date that time, right?
*  This is not feasible and honestly speaking these attacks are
*  computationally intensive relative to traditional
*  Adversarial attacks and this has a lot of implications not just in
*  Running the attack itself but in in the potential defenses against it two levels. I want to follow up on there on the
*  Defenses I have a question about what you might do if you're just trying to defend your own
*  Model where you have the access to all the weights
*  Before jumping to the defense, so let me just again echo back the setup
*  We're definitely doing a little bit beyond the paper here, which I think is cool people
*  I think want to get a little bit more of a sense for what it is
*  You're actually doing when you're doing this research. So you've got the max of
*  four
*  Models so you have a setup of four a 100 these things can they're like 713 B
*  So they can fit onto a single a 100 and you've got weights parked in each one
*  Ready to run your forward passes or do your take your gradients?
*  the
*  25 prompts you've now got a hundred
*  model prompt pairs and
*  Each
*  Input token you said could be embedded up to thirty thousand
*  Numbers wide and there's 20 tokens as well, right so
*  600,000 so we're looking at 60 million
*  individual numbers that you'd be taking a derivative with respect to ultimately to
*  Get a gradient not quite right because because you so the nice thing about backprop right is that you can take you can sum up
*  multiple losses in the end and
*  Get the gradient with respect to a single set of parameters for the sum of all those losses right without getting six million
*  Numbers you just get the six the six hundred thousand numbers. So the way the backward pass works is that you
*  run all these models
*  compute there the loss you have and the loss here is essentially the probability of
*  the negative probability negative log probability of
*  The target sequence you're looking for and
*  The sum of this function over all the different prompts over all the different models that is your loss function
*  Again, the way that sort of backprop works is that you have a arbitrarily complex loss function because it's a scalar value
*  You can just run this procedure that computes the derivatives
*  the individual derivatives of your loss with respect to all the possible token substitutions you could make and so it's still just you're still just
*  computing ultimately
*  30,000 times 20 different numbers that indicate how important each or how good each potential substitution of each token would be and
*  Then you're just picking the best ones and running the forward pass there
*  Yeah, since we're just optimizing one suffix for all prompts over all models for each of the
*  numbers in the embeddings for each of the 20 token positions each one is the sum of a
*  Contributing factor from each of those hundred
*  cases the challenge is you're looking for an attack type that operates in discrete tokens
*  So you now have this direction that you want to go in but there's like a bunch of tokens that are in roughly that direction
*  And so in order to then figure out which one actually works you have to actually run the next
*  Forward pass with that token in place. Is that something that you go like down the line or can all of those
*  Can you optimize all 20 token positions at the same time or does that have to be successive?
*  What are the dependent? What are the compute dependencies in that process?
*  for each of the four paths
*  We compute the loss for basically different kind of substitutions, but for each candidate
*  Suffix we're only changing one token at
*  Basically one specific location and then we're getting the loss for all of these different candidates and then picking the best one
*  So basically we're picking the best token position to swap that was actually a sort of interesting detail
*  I guess based on my intuition I felt like
*  These gradients are you do want to every time just make it one small update
*  Because if you update too many tokens at a time, maybe the gradient isn't very useful
*  It's like not very local and so each token at a time
*  But also evaluating all positions seeing which position is the best position to make updates
*  I think some of the prior work did like coordinate descent for example
*  Where they loop through each position and then at each step they only try to update one position
*  But it seems to help a lot if you consider all positions at every step and then take the best one. Yeah, okay cool
*  That's really interesting. So what I take away from that is
*  The loss landscape is just extremely weird a lot of this is
*  Necessary because the clues that you're able to get
*  About where to go are in fact like not super reliable clues or they point in various directions or they have weird
*  Interactions or they like cancel each other out in weird ways. Could you just say this is impossible question?
*  But what have you learned about the nature of the lost landscape from doing this work other than that? It's weird
*  I think maybe this is largely a problem of dealing with discrete
*  tokens and
*  Just in general or maybe this is also my intuition in general if you're working with
*  Language or these sort of higher level concepts and concepts are also discrete
*  If you try to work in continuous phase or embedding space if you're looking at individual tokens and how to perturb them it felt
*  Weird from you how you would even move between these like discrete concepts or something like that
*  I think it's the nature of discrete in in LP that makes things a bit weird and then you have to
*  with some
*  guidance by gradients you have to do a lot of search and then just
*  Verify which one is the right direction. We solve problems. We also do a lot of
*  Search or you know, you're trying to solve a math problem or something. You do trial and error
*  It's not clear whether there is like a small update
*  According to the gradient that you could make that would just make the problem much better
*  So it's like like bigger jumps, but then in order to do that, you don't have like the local information
*  So you need to verify by doing this for a pass to find the best loss
*  One I would say conceptually nice thing about this attack. I shouldn't say this attack. I should say about this
*  overall framework for looking at
*  Adversarial attacks on language models is that there's actually a pretty clean set as with a lot of problems in machine learning, right?
*  there's a very nice and clean separation between the loss function you're optimizing and the
*  Optimization procedure you use to actually minimize it right to be honest both of those are
*  Crucial elements to this overall strategy we had the end result of
*  Making language models do bad things right or output text that they shouldn't be outputting and but this is also the key point is
*  that there's a ton of
*  alternatives to explore here this paper in some sense was a
*  presentation of
*  Two aspects that when put together seem to work pretty well, right? So we have a certain loss function namely
*  Trying to make the models say sure over multiple sure here is blah blah blah
*  Over multiple prompts over multiple models. That's the loss function. That's the one side of things on the second side
*  You have the fact that look now we know that the parameters were tweaking to do this or the tokens are tweaking are all discrete
*  We need a way of optimizing it and so we came up with this also fairly
*  Involved but not that complex method for essentially saying look
*  Here's how you swap tokens and each step to optimize your loss and
*  we put these two things together and what comes out of it is a
*  Simultaneously very powerful way of manipulating these sort of language models, but the point I would highlight here is that
*  Neither of these are at a plateau yet, right? We don't know
*  How much more we could do we know this works as an instance of it working?
*  But I certainly think there's a lot more research to be done here
*  To try to figure out what are better optimizers? What are better loss functions? How can you put these two together in a better way?
*  This is a proof of concept right now
*  I think and I hope that it reinvigorates a bit of research in this area of adversarial attacks in this new I think very relevant
*  setting
*  such that we find
*  Overall better ways of solving these two problems
*  And of course
*  This is just talking about it literally from a technical standpoint of just trying to minimize a loss, right?
*  The implications of this in some sense are very different and very that it's a whole set of things
*  We can talk about the implications of this as well. He writes. It's a whole nother conversation in some sense
*  We don't want to suggest that this is the best thing possible to do right?
*  This is one step in the research agenda. It's in some sense an opening and a volley here this separation of
*  objective and optimizer
*  really lends itself I think to
*  iterating on these processes, I mean iterating on the research and finding
*  ways to do this
*  More efficiently with less time all these sorts of things maybe with higher success rates all the sort of stuff
*  It's all out there. And if we learn anything from the adversarial attack community, it's that there's no shortage of
*  Ingenuity when it comes to clever ways to address attack these models and come up with new and ever-changing ways of
*  Doing these things so I I think it really speaks to or it will speak to the flexibility of these things if we can
*  do more and more work on
*  Tweaking them in different ways Andy
*  Do you have any visual in your mind as you think about what are these changes like doing in the internals of the model?
*  I was trying to come up with one but Zico shot me down on it. You know, that's actually very
*  Interesting and I think it's still very unclear like basically I've also tried to probe around and it does seem like
*  While there might be circuits inside the model that
*  Call these circuits sort of model representation that
*  separates harmful versus harmless
*  instructions there could be also other factors that contributes to why the model follows harmful instruction because
*  Maybe currently it doesn't fully depend on whether the prompt is harmful
*  Maybe there's some like weird factors in the training data set where it's like because of certain things in the instruction
*  then I will try to follow that instruction and that also what I found is that with this model internals you can
*  Separate even with like jail bricks you can still separate
*  Like harmful versus harmless instructions, but clearly the model isn't like only using that information for you to give these outputs
*  And I do think this is a sort of interesting direction to look at where you're manipulating model behavior
*  Through these suffixes or these attacks and then give you some insight of why the models operation in certain ways
*  so if you were trying to defend against this and
*  You're maybe also
*  Thinking how can I be as robust as possible? Maybe also how can I be like as efficient as possible?
*  I wonder if you wouldn't actually go away from
*  discrete tokens like
*  Maybe you just want to train on adversarial examples where?
*  like that suffix
*  embeddings are optimized adversarially directly and
*  Then still train against that as opposed to even like worrying about the token optimization layer
*  If I'm anthropic and by the way, just to motivate this whole conversation
*  I'm sure you guys have seen the Dario interview from not too long ago where he says today a jailbreak is like an embarrassment
*  for the company and
*  Couple years from now. It might be like
*  Catastrophic so if you're them and you're thinking this is a pretty interesting
*  Attack, what would you think about doing that adversarial training? But in a way that's even in the embedding space
*  I guess my thought there is like maybe that would
*  Even be more robust than doing it, you know, just that the discrete token points
*  Maybe I can just quickly speak from my experience
*  You can do that obviously you can do like sort of adversarial training in embedding space, which is what image classifiers are
*  but basically
*  And obviously if you're robust to that sort of attack which you know covers basically all space then you're fully secure
*  But it's just the fact that if you do it
*  With a larger norm or if you try to make the attacks stronger, which would cover more cases
*  Your the performance of the model goes down there's that trade-off that
*  we still haven't solved and
*  But if you use a weaker threat model to do adversarial training in embedding space, I think we also tried that so it
*  You would still be vulnerable to these token level attacks and it's like sometimes it doesn't really help at all
*  so we do need a probably better or different method to do adversarial training and
*  I think in general I think of this sort of maybe you can approach
*  defense in two angles
*  one is maybe
*  building a more secure system with more layers, so if you think of the model as
*  One part of a larger system and then from maybe more of a security perspective you could add input filters output filters
*  different layers of defense and at inference time you can probably do all those computation
*  And perhaps if you add like enough layers that constrains the attack space a lot
*  then it's like pretty difficult to find these general jailbreaks, but I think there is the problem with that and
*  on the other hand you can also
*  Make your modeling her or bust but I I don't know if there's like a good way currently of doing that
*  I mean see what they'll be has more to say about that. I think Annie's exactly right there and from a high level
*  When you talk about defending against adversarial attacks, especially in this setting
*  There really are these two things you can imagine right there are
*  things you can do outside the model to try to limit the attack surface from the start and
*  Then there are things you can do to the model itself to try to make the model inherently more robust
*  And I know the concept is where the model starts and where the filters start where the model stops that can be actually a little
*  Bit fuzzy and that's okay. Let's not worry about that
*  I think conceptually we still have these two obvious kind of candidates for defending against these things
*  We've been working on defenses for a long time, right?
*  So we've come up with some of the more well-known defenses, especially certified guaranteed defenses the project guarantees of robustness
*  against certain classes of perturbations for various models and
*  I've worked in this enough that I can say with some confidence that in traditional deep learning
*  So on the image domain on things like this we have not succeeded yet
*  You're not even close to creating robust models that are truly
*  Involvable to these attacks and there's really seems to be a fundamental challenge here that we just know how to overcome
*  And that challenge is as you build models. We were ever so attached are about is they're about as you said before
*  crazy loss surfaces or crazy sort of
*  Services of the response of the output of these neural network functions to small changes in input
*  What we find is the way you prevent these things is you make the function less sensitive to these small perturbations
*  You make functions smoother
*  But when you make the functions smoother in this way, they stop performing as well and all your benefits of deep networks go out
*  The window so I think the best adversarial performance we have on data set CFAR 10
*  Which are years old now kind of toy problems from a standpoint of computer vision is like 70% accuracy
*  Which is they had that in 2012, right?
*  And then and they're not improving very quickly here
*  All of this is to say we don't know how to solve this problem and a lot of the potential solutions
*  We're thinking about here. We should try them and we can try them
*  But there's no real evidence yet that they're going to work
*  We just don't have that evidence yet that these things are really going to work or to your question earlier about
*  Why don't we try to attack things in embedding space? That's a smooth because we can optimize over
*  That's just too powerful. You can't actually do that if you allow an attacker to to modify embedding space arbitrarily
*  They will succeed at attacking you so you want to create classifies
*  So that you'll have to basically your classifier not output anything at all ever and or your language model in here
*  I always output the same thing
*  Maybe that's a very robust model by the way, if it just always has the same phrase super robust, right?
*  It's not very useful and there does seem to be this fundamental trade-off that when we try to make models more robust
*  They just don't perform as well and their performance
*  Degrades to a point where no one would ever want to deploy that model for that small edge case of adversarial robustness
*  It's very possible that the use cases we're talking about here with LLMs change that calculus
*  So all of a sudden the risks involved in deploying models that are non robust get to a point where it really becomes
*  Unwise to deploy these and so we just we will only degrade the capabilities of these for the sake of robustness
*  I hope we start taking that consideration seriously, but I also worry that's
*  Not going to be the default that people go with right people will go with a model
*  That's most capable a one that gets the lowest perplexity on whatever data set they hold out with they're evaluating on and go from there
*  So there's a lot of factors involved here in creating robust defenses. There's the filtering approach
*  There's the model of buses approach and the reality is we just don't know that much about the space here
*  But I suspect that any solution we have has to actually exploit also
*  The discreteness of this task because if we get away from that
*  We get away from discrete tokens the task just becomes too hard
*  And I think we will not succeed at making robust models and the only hope we have for a successful defense is
*  Taking advantage of this discrete nature and hopefully that actually does make the problem much harder and maybe there are
*  Successful is defending here, but we just don't know yet
*  It's so early in this whole research landscape at least in the context of alum so far
*  I'm just reading this paper over the weekend from anthropic about
*  their influence function technique where they were looking at
*  what
*  data from the training set
*  Most influenced this particular response and it was striking to see how
*  at the kind of
*  small and very naive
*  Token matching seemed to prevail in many of the examples and then as they got up to the midsize
*  It was like okay now I see that you've got some much deeper conceptual
*  Understanding much more sophisticated in some sense. What is grok? What is not is this just like
*  Some close fitting to some crazy landscape that still doesn't have any like procedural
*  Grokking to it who knows but definitely something much more
*  Conceptual seems to emerge now. You're still beating these models right even in production today, right?
*  It's the same if they're referring to their kind of mid 50
*  billion
*  Parameter model like that's the same one you've been testing on presumably right you let's summarize the headline findings in terms of
*  Transferability because that's pretty insane and it's one thing to say okay
*  You can find this if you have the white box access to all the weights
*  But as you said at the top like it actually works on
*  Frontier commercial models that nobody has the weights for it seems to actually work a lot on the open AI models and
*  It also works on the llama
*  models and
*  Too much lesser to extend but still non-zero on
*  the Claude
*  Models by anthropic as well the model we attacked
*  mainly the Kuna models which were trained on church of PC data, which is outputs from charge of tea
*  The tax did transfer better for open a models. I guess interesting. It also worked on Bard and
*  Fod I think Bard was more than 50% charge of eq well super and five is definitely more than 50%
*  Claude wine was like say below 50% but this is or using I think
*  four different prompts and we cut the success if one of them works and then Claude who
*  It was like in a single digit
*  But obviously this is it was also the sort of four prompts that we had at the time
*  If we try some different problems with which we all did sometimes they work better
*  Some numbers might be actually higher and I think we also just to be fair here
*  I think we also tried on GPT for June version
*  06 that one is more robust than the
*  March version which is I think it was also in a single digit. I was thinking why this is the case
*  You know those more are later in the quad to as well that the little were trained much later than the first version
*  Which you were used to the cell so perhaps there's more training data
*  Different training data and just think if you find you in the models a bit further from your distilled
*  counterparts, then maybe it doesn't work as
*  Relatively and then you know verify that maybe we should also distill some of these newer models to see if it's better currently doing our
*  methodology for transferring these attacks is that we can set the attacks on open source models and
*  We took those exact same attacks without any modification
*  Paced them in to the commercial models and shockingly to us
*  They worked an amazingly large amount of the time as if there's a lot of there's a lot of questions that we still really
*  Understand about why this is why is it the case that these?
*  attacks that were learned on
*  open-source models
*  Seem to actually ever have any chance whatsoever working. Why is it over 0% success rate?
*  I think there are many theories of this and one of the theory and then maybe secondly
*  Why does it work sometimes not others is the other question right as was mentioned or the most recent GBD for for Claude to?
*  Success rate notably drops off and there are a number of possibilities here and to be honest
*  Given our current sort of access to models and such and our ability to run
*  We just haven't done quite enough analysis to really get at what the what their true answer is
*  But we have some possible theories and one possible theory is that GP chat GBT
*  The attacks are more successful there because Vicuna which is the model we attacked is trained on outputs from chat GBT
*  And this is a common thing in adversarial attacks you attack a distilled model and it works against the original model
*  That's an obvious possibility, but it isn't a full answer either because the worst against Bard and but one two
*  So there's something else is going on also
*  The other thing I'll say is when it doesn't work. Why doesn't it work?
*  So why is there something fundamentally that they did Claude to fix this to fix adversarial attacks or did the latest GBT fix adversarial?
*  I don't think so personally it may be the unbeknownst to us. They fixed something fundamentally there. I doubt that
*  I think what's happened is that they've probably done some more fine-tuning and they've probably done some more prompt engineering
*  What happens in both cases when you fine-tune a bit more or you add a much longer system prompt?
*  That does give you some degree of resilience to these fixed
*  prompts that we discover however, and this is the big but
*  That is not in my view a secure system
*  Because all we need to do and this is what what we're attempting to do and follow on work is you just need to take
*  new outputs from your system
*  Create another kind of fine-tuned model based upon like buddy with I Kuna but on new outputs
*  Attack that and it'll probably be successful to be totally honest here
*  We are right now I would say in the midst of this kind of attack-defense game where we just don't quite know
*  What the ultimate limits of this approach really is it's shocking
*  Fundamentally that it worked at all on these commercial models and that's in some sense the scientific result here, right the result
*  Scientifically is in some of these models to a shockingly high degree these attacks transfer when they don't
*  That doesn't mean that you can't build similar attacks against those new models. It just means these particular ones don't work yet
*  and I think that's an important point to consider there is really this notion of
*  We have only begun thus far to really probe at some of these models as we do more work or as the community has more
*  Work, I think we will uncover a lot more about understanding the true sort of hardness landscape of
*  How hard the tax are to get to work on different models is something built into the model makes them more robust or is this?
*  Just we had the system prompt wrong and some of them
*  So we just reattach with the right system prompt it'll all of a sudden. Yeah, maybe give me a little bit more than on
*  what you think is underlying the
*  Transferability and
*  Maybe also how you think that shapes up because you could imagine
*  quite different
*  trajectories and if you're not ready to even make a guess that's cool, too, but
*  These models are trained on for instruction following and this is related to the mode switching type of
*  Argument is basically
*  the train to follow instructions or to feel of the most salient to most salient clusters and then usually when it
*  Follows instructions as sure here's how to do it and then when it doesn't it says I'm sorry
*  Yeah, and it all trained on these type of instruction tuning datasets and that's the underlying data that
*  Supposed to fit then in some sense they all commonly have this sort of issue on the line distribution
*  So then it was maximized or minimize the loss for certain models
*  It might also to some extent minimize the lot for some of these other models trained on very similar data
*  I think why it works and then
*  also
*  One observation was that if you only train
*  On one model and one prompt it's not going to transfer it all like it's not going to transfer to other prompts for the even
*  For the same model. So you do need to have this more general setup where you're optimizing one suffix for
*  Multiple prompts and multiple models because it seems like the vulnerability are like everywhere
*  So it's very easy to pick this very specific one for your specific prompt in your model. But if you
*  Find the one that works across many different models and different problems
*  It seems to be finding some more common vulnerabilities to all these models
*  Then that gives you a much higher chance of the question of adversarial transfer is still one that we don't fully understand in any setting
*  in machine learning
*  There are a lot of hypotheses about this people some people say oh, it's because they're all the same
*  Overall architecture and since our computers have this joint vulnerability, they're all transformers. And so this is what's costing it
*  I don't believe that one. I this is a hypothesis right now and something that we are trying to say
*  But it's also hard to test this to be honest because to a certain extent
*  Ablating it would require retraining kind of brand new language models with no overlapping data
*  It's a bit which is very hard to do right? It's hard to train a brand new language model that has zero overlapping data
*  but I believe
*  These the transfer ability of these models is most likely due to their pre training data
*  What I mean by that is we know that these models even though their instruction tune a slightly different settings
*  Maybe use a little different mechanism for training things like this. It definitely different architectures to some degree, right?
*  But we know that they're trained on
*  Similar data right they all use common crawl
*  They use Wikipedia these all these data sources that we know about that
*  We know they all make use of archive papers things like this, right?
*  We don't know GBT for because they don't tell us what it is
*  But we roughly know the mix they're probably using if not the details
*  My hypothesis though is that this is a feature of the data and what I mean by that is in this training data
*  Right in common crawl not to us, but in some fundamental way in the data itself
*  There are just weird
*  dependencies or features
*  That are genuinely useful in predicting
*  Next tokens that don't make any sense to us, but which are genuinely there and what I mean by that is
*  In this data that was used to train these models
*  the string dash dash
*  Winky face
*  Describing now the whatever that actually means something that's a meaningful
*  Bill Coleman visions of I'm non robust features
*  I just means that like they aren't things that we associate being real things
*  But they really exist in the data and keying on those kind of features or having a transformer that picks up on those elements
*  genuinely improves
*  perplexity in the training set and
*  So because it's going to improve perplexity these models are gonna do it. They're gonna pick up on these weird patterns
*  They don't really see as patterns, but they're there
*  They're somehow there in the data just in a way that we can't really discern is and I'll you but that they're not really there
*  Because we don't they're not part of language, but they're part of the textual inputs these things have
*  That would be my best guess as to why you see transfer across different architectures different training at all is due to these things
*  Also, probably helped by the fine-tuning on chat GPT data. I'm sure that's definitely a crucial part
*  I don't have that at all. You wouldn't see this transfer, but I think the underlying cause the transfer most likely lies in
*  The
*  pre-training data itself and in these non robust features as it's a
*  bag as a term from Alex Madria's group these non robust features that exist as
*  genuinely helpful things in the training data and
*  Adversarial examples pick up on them and that's my best guess. That's why these things happen
*  Could you comment a little bit also on just like the mix of these things because I've seen a couple different
*  General types it's like some of them look like total
*  character string almost like the cat walked across the keyboard and then others are like uncanny
*  Type of things where it does seem like those initial strings look relatively easy to classify
*  whereas some of them also look like
*  Things that user mode would plausibly enter and thus are like probably a lot harder to classify
*  And I don't know what the relative balance of those are or if you can look for the more like
*  Intuitive ones
*  Preferentially in the attack or was that just sometimes they randomly spit out and sometimes they didn't I think when you're learning the loss
*  Finding useful feature and then some of these are maybe more robust
*  Which are more readable and then some of these are sort of more not robust and then it's like a mix of both
*  it does seem like a
*  lot of the times it is
*  Incorporating some of these features are readable to a surprising extent or at least for me
*  Like I wouldn't expect you to just directly optimize without any like fluency constraints
*  It would actually pick up on those and it does seem a large number of the suffixes
*  includes some subparts of it that readable or it makes sense to do but obviously you can also
*  Modify the loss to make it more fluent and that might give you so that would up the weight of like
*  readable features, I think it's actually quite interesting that
*  That
*  given the number of
*  possible adversarial attacks
*  It does seem to find some that sometimes are for lack of a better word interpretable now
*  Say that oppositely or now say the opposite right as a phrase that kind of came up in some of the attacks
*  What the systems respond with when that phrase is included in our adversarial suffix is that they will first follow the instructions
*  Like they'll insult you and then they will do the opposite so they will then compliment you after this fact and somehow in some
*  weird way, maybe that like
*  balances out badness so that the model doesn't think it's that bad after all and there's why I say this all is that
*  this seems this is very interesting because
*  In some sense these are and another one that you frequently find is you find the word sure in things
*  So say sure or things like this, right?
*  Like the phrase say sure appears in some of the attacks as well and we want to respond with saying sure and
*  So there seems to be an extent to which
*  These attacks somehow are like they're not entirely orthogonal from what you think of as manual jailbreaks of these systems, right?
*  So there is a sense in which maybe they are
*  Uncovering some of the manual features that people have themselves to their own intuition
*  Uncovered to break some of these models which there have been many to be clear, right?
*  There have been many manual jailbreaks already and so this is very interesting and there is why I find it so interesting
*  I would have thought that these prompts would be entirely nonsensical, right?
*  I would have thought they would just be complete garbage
*  just random characters because we know the space is that big and we know we have all the space and
*  They often are a lot of it is but the fact they find even some things that are intuitive
*  makes me believe that maybe the space of
*  Jail breaks and sometimes is not actually that big right?
*  There's a there's there may be in some sense a little more limited subset of these things than we first realized and
*  This might speak toward the possibility of defense, right?
*  If it really is these things into it then maybe there isn't that many things to try here
*  But on the other hand, there's also a bunch of garbage. So
*  Which is gonna win out?
*  I don't know but the fact that it ever puts out anything interpretable with very large air quotes are interpretable here is
*  quite
*  Interesting in its own right and I think deserves study in its own, right?
*  Just wanted to talk about what I saw in some of the stuff fixes
*  I think a lot of them actually correspond to some of these many who jail breaks for example, we also found
*  Some of these would ask the model to output thing in some like programming language
*  Which is you know one of the manual jail breaks out there and then some of these would ask the model to say sure in the beginning
*  And then like introduction and some words like that or tutorial and then that's also another manual jaybreak
*  So a lot of these are actually
*  covered all these sort of manual jaybreaks, so that was very interesting and I think maybe that's
*  Also due to the discreteness of the problem and it seems like it sort of lashes onto these
*  discrete concepts. So could you imagine a
*  slight modification to this where you also
*  take into account the
*  perplexity or those kind of incremental token if you've changed your
*  token search process to
*  also wait maybe just go sequentially and then also wait like the most plausible
*  next token in some sort of balance with the
*  original goal of maximizing that output token, maybe you end up having to do more steps, but you get to something
*  Readable a lot more often. I guess the fact you're getting at it all suggest that would
*  There's enough space there that you would still like converge on stuff that would work I would think right?
*  Yeah, I think that's possible as you go back to the distribution the models trained on
*  I think the model probably has a better chance of recognizing it's actually harmful since most of the
*  fine-tuning data or the ROHF they've done is on like actual like
*  human written text
*  Certainly possible or you can even imagine using the parameterizer attack by another language model and somehow
*  Like prompt information to that language model and then I like the language model could output whatever
*  your actual text in
*  Natural language. I would even just go far just to add that we have done this
*  so we have added fluency constraints to the sequence of the adversarial suffix itself and
*  Not unexpectedly you get things that work a little bit worse at attacking things while looking a little bit more fluent and you can
*  Tweak that hyper parameter of winning these two things right fluency of the adversarial suffix versus decrease of the loss
*  To for whatever trade-off you want, but there seems and there seems to be a pretty big range you can play with here
*  So you can in fact
*  Have somewhat fluent constraints to still attack things
*  But I agree with Andy that ultimately this is a you have some Pareto curve here the less you care about fluency at least in
*  theory
*  Modulo the ability to optimize things and the challenges optimization in theory if you talk about the loss function itself adding a fluency constraint will just
*  decrease the
*  saliency of your attack or this creates the effectiveness of your attack a little bit at the cost or at the
*  To the benefit potentially of making your suffix seem more realistic and it works fine right now
*  We didn't try it as much the transfer there just because it didn't work as well in the open source models
*  But we have definitely tried that and they do work. Okay. Yeah interesting
*  So it seems like there's a big theme of this work in general is just that these everything has this Pareto
*  curve structure to it and
*  There is a tax to pay in your primary
*  optimization
*  objective whenever you introduce a secondary optimization objective and
*  Unfortunately, that is reality as we know it right now
*  Hearing okay. Yeah, why can't you defend for one thing?
*  It's just gonna be a tax on your operation now
*  You're gonna have to do this extra optimization process in the loop and more training and on top of that your performance
*  suffers somewhat at least and then in almost a mirror sort of way on your attack where you're like
*  Yeah, we could make the attacks more fluent
*  But then again, it probably doesn't work quite as well and we also maybe have to work harder to find it
*  That's also a really interesting segue to the next paper too, which is like a
*  it's like a
*  If that's the tax this is like the rebate
*  or the the subsidy on on performance because you're able to bring some structure to the table that
*  Accelerates you toward good performance. So you could say hey if we can bring more techniques like that
*  What the one in the second paper then?
*  There's still the tax but maybe for the same budget if we can start in a smarter way in some
*  With some like better structural defaults
*  Then maybe we can get to the same performance
*  I'm maybe stretching to put these two concepts together
*  But I do see these as opposite sides a little bit of this coin before we go to the next paper
*  which I am also super interested in just tell me a little bit about kind of your process here because
*  This is research which obviously made it to the New York Times
*  It's a lot of people read about it very headline friendly result
*  But also people are using these models in the wild and there's companies that are operating them and
*  So how did you think about the process and what sort of process did you?
*  Go through to communicate these results and give people a chance to try to respond or fix them or whatever before
*  Academic publishing is one thing but the New York Times obviously something else
*  So I'd love to hear how you guys thought about that part of this whole project
*  we were just initially, you know, they're doing this or research and
*  It was definitely surprised to me that these stuff would transfer to black box models
*  Which I think in the future would cause a lot of problems if not properly fixed
*  So when we had this results, basically we wanted to go about it in the most reasonable way so that
*  First we caught any harm in the short term
*  but at the same time we we wanted to
*  Raise awareness that these kind of exploits to exist in the current
*  models that are deployed online that we will use every day and
*  sort of to
*  alarm the community that is a problem, especially if you
*  extrapolate down the line when you have
*  More autonomous agents going around everyone's using them. But if you have these exploits, I think the harms are
*  Exploitationally larger than the current chatbots
*  so we
*  went and told all four companies
*  Disclosed our attack and what's happening got some responses and then we just wanted to put this work out there
*  including like we released the paper the code and for people to
*  start on this problem as some sort of a baseline and
*  we do think that the earlier people try to
*  work on this problem and to raise awareness that the better because as time goes on as the capabilities
*  Of these models increase as the autonomy people give them increase there will be a much larger risks
*  I would say two two things on this notion of sort of
*  Disclosure and nature of this research. The first is that as much as these things currently do in some sense allow people to
*  Violate the intended behavior of some of these chatbots
*  But let's also be totally honest here that real harm we can create with these things
*  With a chatbot is not much who cares because the chatbots mean to you
*  It doesn't really matter if Chabot insults me can hurt my feelings
*  But I'm not gonna cause major harm
*  Even if a chatbot can give you directions on how to build a bomb you can find out on the internet
*  In fact, the whole reason these things know how to build a bomb is because they read it on the internet already
*  So let's just also take a step back here like
*  Right now with the capabilities of these models right now there and how they're used right now in the most common interface
*  Which is these chatbots?
*  It's not that big a deal to be able to do this if you're trying to do it, right?
*  If the other thing if you can inject it into like other people's conversations, but we're not doing that
*  We're like we're asking it like you were asking something bad and then you put this string in and it tells you the bad thing
*  You're asking for it and you are trying to break it, right?
*  You're asking is to do this the direct harm that can be caused by these things as in this most common mode right now is
*  Very small I think but I really want to emphasize that point that Andy made right there
*  Which is that every single startup right now?
*  not every single one but a whole lot of them are rushing to put LL M's inside of API's that
*  read information from the web and then take autonomous actions based upon this and
*  This to me is
*  Genuinely concerning just honestly speaking because I don't think people building those API's and
*  Autonomous agents to be clear autonomous agents in the very limited sense, right?
*  But still no limited sense answering emails automatically stuff like this, right? I don't let me know about this attacks
*  Or I don't think they were aware of them always I don't know
*  They're really thinking through in many cases the implications of having systems that can be arbitrarily controlled by text injection
*  Into public information to control your system, right? This is wild. These are like
*  Completely unscoped weird things that can do whatever they want and we're putting them into simple API
*  Endpoints that people can call and I find that genuinely a bit concerning and so I think that there really is
*  Hopefully and I think I'm just echoing Andy here. I hope that making people more aware of
*  This reality and it is a reality of these systems, right? This is a fact of these systems
*  can be a bit of a forcing function to
*  Change how we approach their usage. I think we are still a ways away from autonomous operation of these things
*  I think there should be humans in the loop
*  I think we should be verifying and checking the output of these things
*  They can be incredibly useful tools do believe that but I think they are still tools right now
*  They are there are tools that we can use and they're that were humans
*  Oftentimes can and should be in the loop. And so I hope this kind of brings a little bit of that perspective into all of this
*  Yeah, I honestly think even in the short term posted something the other day on Twitter
*  And I'm very interested in this disclosure stuff too, because I do a lot of my own just random red teaming
*  Anytime I see a new product I test a lot of new products and I also read team them as I test them
*  Just as a first pass. Hey, will it refuse?
*  Somebody be amazed how often it doesn't I just did a ransom call out of this product called Belva and
*  I
*  Went through a similar disclosure thought process where I was like, I don't really want to popularize this
*  But they weren't really responding to me in private
*  I want to hear what kind of responses you got if you can tell more about that
*  But these guys weren't responding to me at all
*  so I was finally like I guess I'm just gonna have to shame them in public and
*  So I put this recording out there where this voice called me and said it had my child and demanded ransom of me
*  In like a real-time interaction no jailbreak required for that by the way at the time
*  They've since improved that quite a bit
*  I think they probably just put a classifier in front of it or something along those lines
*  Nothing like to create I actually showed in my thread to here's how you could use Claude instant to
*  Just filter this and like a bunch of other things for whatever like fractions of a cent and
*  Sure enough, they did turn around and fix it
*  But in that case it was like so new and I felt like nobody's no other businesses are like dependent on this right now
*  It's not gonna be like a big disruption if I do this
*  But all that was just to say really like even today
*  You can make a pretty damn good ransom call and we're starting to see those systems ramping up pretty
*  Effectively from a usability standpoint with 11 labs and play HT
*  just in the last week or two both having dropped really good voice cloning and
*  With at least one of the two of them also now doing
*  streaming so you can patch your language model output directly into their thing and
*  Now you've got double streaming where it's streaming the tokens and streaming the voice out in a very real-time
*  sort of way
*  Obviously, that's I'm with you by the way in terms of human in the loop
*  like I do also totally separate track, but I do a decent amount of just AI kind of implementation
*  advising win different contexts and like almost always the practical wins today are like
*  do the first pass save me 80% of the time and
*  Then have a human kind of take it from there
*  I do think that's still mostly where where a smart
*  User would probably want to make sure the output is actually worth anything to them before proceeding
*  Nine out of ten cases, but anyway the short-term harm so you know themselves are not are not insignificant
*  So what can you tell me more about what you heard back from the companies were they like?
*  Give us some time to fix this or just a sorry. It's crazy out here. Do what you want to do
*  I could imagine kind of anything so the responses well, I'd say cordial and very nice
*  We were emailing researchers
*  We know there and we know people there and we're happy to interact with us and be in touch with us
*  None of them patched it before the release
*  So eventually some of the exact strings that we have are were matched you can no longer enter them
*  It wasn't a public are no longer no longer work. I think other and so without being specific here, too
*  I think actually some other providers again not before we released it, but after we released have since made a lot more
*  Aggressive filtering changes where they seem to be filtering out
*  Queries much more aggressive than they used to and to the point where it doesn't work nearly as well as it used to even in
*  A few weeks since we've done this we definitely see that to be fair old companies though
*  The response has been largely quite positive when we've talked with them
*  They are interested in the knowledge here in the understanding how these things work
*  They have their own internal red teaming efforts in many cases, and I think in some sense. This is a
*  one
*  Approach to red teaming that for whatever reason I think a lot of the companies did not consider when they were first doing red teaming
*  I think a lot of the approaches that they consider were very manual in nature and
*  This does highlight a very different approach to this that I think is quite that they are for the most part
*  Interested in intellectually and practically I do believe that for the most part these companies wants to engage in red teaming and
*  So that they see some value in this the use cases
*  I am most concerned with are precisely those ones where they do things like query external data and stuff like this that that
*  Are not the primary products for some of these companies and so may not be as much of an issue for them as it is for
*  Startups designing more open-world autonomous systems, so the response was cordial and interested and
*  To be honest has been
*  Largely positive some people from the companies have been filing issues and committing our code to our code repo and stuff like that
*  So it's really they have been engaged with this and they have not tried to either a stupid under the rug
*  Nor sue us or things like that that definitely has not happened
*  I do think that they have different incentive structures, right?
*  and then there is a
*  definite need
*  For some of these efforts to happen outside of just these companies and there has been so far
*  I think a bit too much emphasis on internal measures companies can take as opposed to
*  interacting with a broader research community
*  but I think they also appreciate this they also appreciate that a lot of their efforts are internally focused and
*  they can stand to benefit from
*  External validation and external testing of their systems and so for the most part
*  I think they've been quite open to root the work we've done and even in some cases can treat helping to contribute to it
*  I haven't found any sort of particularly adversarial interaction so far. We'll just say
*  Actually, maybe just a quick word occurring we were saying earlier about short-term harm. I do think there
*  Is some potential harms that could be created with this sort of exploits with current systems, but it is like the
*  We're not in our best state
*  Currently we're deploying the systems even with these sort of vulnerabilities
*  The best we could do is get people
*  aware in this problem
*  Early on just so that we don't
*  Run into the problem that later on there is like exponential harm
*  And then you can't really do anything about it then because it'd be too late
*  So it's a trade-off we have now and then we think the benefits of people knowing these problems would
*  Override the potential harms in the short term. Yeah, I guess I would also echo that maybe the comments
*  I made earlier where downplayed a bit too much the current things people can do
*  I don't think it's great if you can get an interactive agent that can talk with you while trying to spread misinformation
*  About vaccines or something like that, right? That's not a good thing and you can already imagine right now the potentially bad use cases
*  But I think that stems exactly from the deployment of these things in a more autonomous setting, right?
*  So just using them as a chatbot I think is
*  Some an issue, but you're obviously trying to break it. It's really when people start integrating these breaks into
*  External facing systems that I think even the short-term harms can be quite that was actually less about the timing of it
*  I think things can be done that are quite bad already
*  But I think it's also it's more about it's the mode with which people are thinking about deploying these things that concerns me the most
*  Why not just train these systems without any bad information?
*  what why do we have to train it on a
*  Raw dump of the internet that knows how to build a bomb to begin with and I think there's sort of two
*  Key points in this to a certain extent we need to take this idea much more seriously than we do right now
*  we train these language models right now on a
*  mound of
*  uncurated just
*  Raw data from the internet
*  that's how they're done now, I know it's not I know it's not the whole internet, but it's a lot of data from the internet and
*  We don't do any filtering or real curation on the data
*  I'm sure there is some but there isn't doesn't seem to be a lot of curation or filtering on the data
*  Used to actually build these things in the first place and then we build these
*  Let's just say it's in this horribly toxic models and we kind of paper over them saying and don't do any of that bad stuff
*  Don't do that all those bad things, you know about
*  Don't do that part of me. Just as why
*  Why do we do it like this? We know how to filter content at least not at least content is not
*  Objectively trying to fool the system
*  Why not try our best to filter out data much more aggressively when we are training a system?
*  And I know there's a lot of arguments against this right there's a we as people are
*  Can be exposed to toxic content without also regurgitating it on command somehow
*  We have that ability and maybe you want to train models have similar capabilities than that and also there's this argument that models
*  Will know not just like their raw data they have but like the closure of the data in some sense and the extent to which
*  They can really form these closures are debatable
*  But they at least maybe could make some sort of steps of reasoning about their information if you give them enough knowledge
*  They'll kind of be able to figure out bad things is the theory even if it's not in the data
*  And I think that's very true to an extent but it's we're not there yet
*  All right, right
*  where there's no way that these systems would have the capabilities of that they currently have to emit toxic content and harmful content if
*  They're not trained on it right in the first place. It's a possibility to think about much more seriously
*  we need to think much more about rather than
*  Training them on building the showguth right the massive
*  Tentacles that knows everything including lots of bad stuff and then papering over it with a little nice bit of fine-tuning
*  Why not?
*  Take more care about building our data our models to begin with lots of possible reasons
*  I think ease is the simplest but that I think it's that's that's not a good reason
*  I don't think I think we should do harder things that they work better
*  I don't know what's the right sort of thing here, but we need to understand that these models are not like us
*  They aren't to the point where they can they can be exposed to all this toxic content and then not
*  reproduce it when given the right target string they will be able to do this and
*  So this necessitates I think
*  Looking at different approaches to actually training these things
*  Maybe training them with less data and be training them with a much more carefully curated set of data
*  that captures the things that we want to know without without being as as broad and as careless in terms of
*  Assembling knowledge to or just assembling text to give them in the first place
*  I don't have the answers here
*  But I think it is a discussion that is at least worth having as a broader perspective on what we do
*  How we build these models to begin with yeah, the whole field is the dog that caught the car a little bit
*  it's like this is all gone very quickly and
*  Surprisingly far and I think there's probably quite a few things like that where it's now that it's working this well
*  We should really take a look again at how we just dump everything into it. I think in general
*  I'm pretty optimistic about curriculum learning
*  being a kind of
*  Both unlock and safety
*  strategy because
*  Just from simple observations like open a eyes kind of disclosed finally that like
*  Their instruct stuff worked a lot better on a code model base
*  It seems like there's certain kind of logical underpinnings. There are some somehow that they're able to
*  Train first and then later on much more kind of fuzzy concepts later
*  Yeah, you could certainly imagine a safety aware version of that that I suspect would do a
*  lot of good at least yeah, you could as you said like maybe at some point the generalization is so
*  crazy that it like fills in all the gaps in the sort of
*  Moral periodic table and knows how to do all the bad stuff to even without exposure to it, but
*  It does seem like that would be pretty helpful. Who are you trying to influence most?
*  People that have a passing understanding of GPT and these large language models see the capabilities and
*  Make undo inferences from this so there's like there's a whole class of people I think that
*  experience chat GPT and
*  are rightly
*  Amazingly impressed by it right because it is super impressive
*  It's just incredible and you play around with it, right?
*  And so then the wheels get turning in people's heads and say okay, what if I do this?
*  What if I do this is what if I use it here?
*  What if I use it here?
*  And I just want to the people that I want to influence are that the crowd that says this crowd, right?
*  This crowd that's excited maybe for some good reason for some bad reasons all things in between
*  But there's a whole group
*  I think of people that are experiencing kind of these models for the first time in the context of these LLMs and
*  they don't have the broader context of deep learning models in general or machine learning in general and
*  They don't appreciate in some sense the differences between these models and for lack of a better sort of terminology
*  how a person would interact with these things right and so they see them as magic and
*  This is bad in my view. This is very this is not ideal. I think these models are not like people
*  they do not work like that and
*  Orthogonal to any questions of intelligence or reasoning or like that
*  they are clearly not reasonably like we're reasoning and they have very distinct and different failure modes and
*  Adversarial attacks is one example of a very clear failure mode
*  There's no analog in humans that all these models seem susceptible to and I think in some sense just
*  Imbuing that in everyone's mind and getting everyone to say to understand look at this example here
*  This is nothing like how you process information. This is nothing like that
*  This is something different getting that to be second nature to people
*  I know getting it to really be second nature is likely a lofty goal because people see what they want to see but
*  Those are the people that I would most like to influence
*  also to a similar extent people at the companies doing these things when they think about the features that they should release in these models as
*  Well as policy organizations and government right and people making them regulations about these things
*  All these are
*  potential target audiences that I think at the very least need to be highly aware of
*  These issues and you can come to the conclusions you want to maybe you still feel like your API
*  And your autonomous agent is safe and it should still be deployed even with adversarial attacks, but you should be aware of all these
*  Security flaws which isn't sometimes what they are right prior to doing that, but that's where I'm at too. It's really compelling
*  Certainly it highlights the alien this in a really effective way
*  You know the the fact that there's nothing you could say to me to get me to do something like this
*  Certainly these like gibberish tokens aren't gonna have any analogous effect that I think is super
*  Yeah, exactly and to the two aspects right one is that the gibberish tokens make it do what you say
*  That's weird. And secondly like they are willing to say anything that they know
*  Right including like
*  Regurgitating toxic stuff that you and I that's not how we work, right?
*  I can be exposed to harmful content and also unwilling to say that myself
*  And it seems like these models are not capable of that in some very fundamental way
*  Or at least I don't know they're capable of ever reaching that point if they are exposed to it in the first place
*  I think this has been great. I really appreciate all the discussion on this topic. I think the work is super interesting
*  I've learned from a research fundamental standpoint something also about just how to think about
*  framing a loss function
*  Across all these different dimensions at once. I think that's something that's probably gonna be new for a lot of people listening to this
*  But this again this work works on a lot of levels from that most kind of
*  detailed
*  Definitional all the way up obviously to highly
*  Sociological really appreciate you guys taking the time to talk about it
*  Asher I don't mean to give you a short shrift by any means but I imagine when one paper appears in the New York Times
*  You're probably somewhat expecting a little more spotlight for it. But I think your work is also really super interesting
*  I'll give you my two-sentence understanding of it and then you can tell me the story of
*  What motivated it and how you pursued it?
*  but I want to start with the high level because we've been talking about this tax right there's the tax of
*  the extra work that you have to do if you want to try to handle these attacks and there's the
*  performance loss that comes with it and
*  Then on the flip side you have this really interesting work where you basically show that if you start
*  the weights of a network
*  in a way that is let's say
*  Inspired by the patterns that you actually see in the wild
*  That this can help you get similar performance
*  Much faster than you would if you just started them with some random initialization or other techniques. So
*  Tell me the whole story of how you get interested in doing this and and what you found
*  Yeah, I can talk about how I landed on this idea and also the implications of fact
*  This more or less works
*  I guess one thing to keep in mind here is that I've primarily done research on vision and you were just talking about language
*  So it's important to note that the technique in the paper primarily works for vision models
*  So we have a bit of evidence that works for language models as well
*  Anyways, I think the connection to robustness is really interesting and I didn't make it myself
*  It does seem like data curation is the way to go these days and I'm in fact
*  working on a similar thread on language instead of vision actually at my current internship and the short story is that I
*  Don't think people do lots of data curation because it's very hard
*  So how did I get to this idea? There's a common thread. I would say connecting my last few papers, but there's
*  Two main dependencies for this idea, which is that
*  First of all, I was previously working also at an internship on visual anomaly detection
*  This basically involves feeding an image to a network you get an embedding and then you do some sort of
*  clustering algorithm for anomaly detection on top of those embeddings and
*  The company didn't really want to pre-train on data widely available on the internet
*  Maybe for copyright reasons or just general concerns about data quality. They want to use their own
*  Internal data my question came to be if you want to train a model
*  That's good for producing embeddings for visual anomaly detection
*  how much you really have to train it surely the training pipeline is different than for classification and
*  As it turned out
*  You can actually do anomaly detection
*  Using embeddings from practically untrained models and this is not as good as training the models
*  Of course, but it's quite close and if you train for just a couple epochs rather than the usual several hundred
*  This works almost as well as using a large scale pre-trained model at least for this particular task
*  We're looking at so it seemed like either there's something to be said for the ability of
*  Models to compress images into a useful form
*  Intrinsic in the structure of the network without training what one thread here was like how useful can we make a network?
*  Without training are there any tricks we could do to modify the architecture or the weights
*  So that we can produce useful image embeddings without training at all and that sounds crazy like building a neural network by hand
*  But I thought that sounded really fun
*  So I worked on that for a while, but then there's
*  Another thread that I think was extremely important for landing on the initial and a medic initialization idea a couple years ago
*  We proposed a very simple convolutional architecture called conch mixer and it
*  Became like pretty popular on Twitter because the architecture is so absurdly simple
*  You can actually fit the pie towards code defining it in a tweet if you feed this model the right data use the right regularizers
*  Augmentations and so on this performs just about as well as any other vision model despite the simplicity and for me the simplicity
*  Was such that I could intuitively
*  Grock the mechanism of the model like you have a hierarchy of filters that are interpretable
*  I could see the filters length by condom mixers make a bit of sense
*  They're oriented edge detectors then you're doing a logistic regression of the responses of these filters at every layer
*  This made a lot of sense to me and I started to wonder if I could build a network by hand
*  That may not be the best for classification
*  But could at least be good for anomaly detection, which I think is somewhat of an easier task
*  so the idea for a mimetic initialization came from looking at the weights of these pre-trained condom mixers, I would say ultimately and
*  Zico suggested that I do the same thing for transformers
*  So that's how I got there really briefly the finding for convolutional networks was that it's possible to define a distribution
*  Completely by hand the formula is quite small specifying like the covariance matrices of a class of multivariate Gaussian distributions and
*  Basically, this just means that you sample filters from this distribution at initialization instead of sampling them uniformly at random
*  There's now structure that reflects this kind of oriented edge detector phenomenon that we see in pre-trained networks
*  surprisingly enough this
*  Really cuts down on required training time for example for the newer vision transformer style convolutional networks like conf mixer or conf next and
*  This seems to be robust across data sets and it even works better as you make models deeper
*  trying to find that sort of structure in
*  Transformers is much more challenging and I guess I could talk about how I converged on the particular structure to pay attention to in
*  Transformers, but let me know if you have any other questions maybe before then
*  Yeah, I think what's jumping out at me about this is
*  It's often remarked upon that
*  Humans
*  Get good at tasks with a lot less data than
*  current frontier models to say the least and a lot less data than AI models in general and
*  There's two things that you're describing here
*  one architecturally with a lot of layers that sounds a lot like what I understand the
*  Human visual system to be doing my rough understanding of what the human visual system does is that it works
*  through a series of layers that
*  Gradually detect higher and higher order concepts as you can move through
*  The layers and ultimately getting to the front of the brain and that's where like the real conceptual stuff resides
*  and so you're saying yeah, there appears to be somewhat of a
*  similar structure that
*  Happens here with training and I don't know if you're inspired by the about biology
*  But the way you're telling the story is making me think yeah, probably part of the reason that humans can
*  Learn a lot of this stuff with fewer examples is because we have some
*  wiring that is
*  Happening before we're even exposed to data that is much more predisposed to learn what it needs to learn
*  And so you're now porting that back to the that concept back to the AI and saying
*  Let me identify these some sort of average or kind of commonality
*  to the structures that we see emerging during training and just try to start with those in the beginning so that I don't have to
*  relearn everything from scratch
*  Every time and so that allows you then to get comparable performance with obviously different
*  Different ratios depending on the exact setup, but you can get to comparable performance with
*  smaller data sets
*  And that also in turn means smaller compute required. Yeah, absolutely
*  I don't know that it's accurate to say that I take a lot of inspiration from biology
*  I don't honestly know very much about it
*  But it definitely
*  Sum up a bit of my inspiration as being the fact that we are clearly born with a better than random initialization
*  I think that holds true for most animals and I saw in
*  Various early deep learning papers these sorts of the vague biological analogies and then the authors honed in on some like concrete
*  Contribution to deep learning and this might not be very formal. I really like that. I try for not super formal, but also
*  Hopefully still literal my goal is to in general in communicating this stuff to be like not wrong
*  But as plain-spoken as possible while being not wrong about anything important
*  So if I'm crossing that line, you've let me know
*  Oh, no, it sounds good to me
*  And in fact, you were talking about trying to read some of the formalism in these papers
*  And I will say the math for memetic initialization is really simple
*  But even still I'm not coming at this from a mathematical perspective myself
*  I literally looked at the weights of a bunch of pre-trained transformers and I used my own pattern recognition abilities
*  To distill out the important parts and that to me is of greater importance than the particular mathematical details and in fact
*  The exact algorithm we show on the paper is not that important to the method you can
*  Make the product of the query and key weights look vaguely like the identity and on a variety of ways
*  The simplest being to simply set the queries and keys to be equal to each other after initializing them randomly
*  And that applies for the rest of the technique as well
*  Can you tell a little bit more about that?
*  Because in the paper, I think this is definitely one where people should look at some of the figures that you have in the paper because
*  It's pretty clear when you just plot a bunch of a bunch of these graphs that like, oh, hey, I can see what's happening there
*  There's a line that goes diagonally from the top left to the bottom right
*  And if I know nothing about what's going on and I was just presented with this image and then I'm like, oh, I'm going to do this
*  And I was just presented with this image and said, what do you see here?
*  A lot of people would say it's so obvious and striking or at least in the ones that you've shown that it's pretty clear
*  That would be the number one thing that almost anybody would say
*  What's a little less clear to me there is what exactly am I looking at in that image?
*  Like I know what I'm seeing. I know it's jumping out at me about the image, but exactly what am I looking at?
*  And how are you back working that into this notion of setting the product of the query and the keys?
*  Give me a little bit more detail on kind of, okay, yeah, I see that striking thing
*  But now what am I actually backing that out to in terms of weights to start off with?
*  There's almost nothing to the actual algorithm.
*  Every attention head in a transformer has corresponding query and key weights and also value and projection weights
*  And the main trick in the initialization is to at a high level set the product of the query and key weights to be identity like
*  And the product of the value and projection weights to be negative identity
*  There's a third component that's quite important, which is to use predetermined position embeddings
*  Position embeddings are used to encode locality in both language and vision transformers
*  But in vision transformers, they're typically learned from scratch from initialization
*  In the case for initialization, it works much better if you set the position embeddings to be, say, sinusoidal position embeddings
*  This basically means that pixels should attend to their neighbors or their close neighbors at the time of initialization
*  So how you actually set the query and key weights to be identity like or negative identity like is
*  In the first case, you can just set them to be equal to each other
*  And then for the value and projection weights, you can set them to be equal to the opposite of each other
*  The value weight should be negative projection weights
*  And there is a small constant factor there that you have to pay attention to
*  Otherwise, you'll have some optimization difficulties
*  But the technique is dead simple. Most libraries come with position embeddings already there
*  It's just your choice if you want to start from a random initialization or actually use the predefined ones
*  The implementation is actually only maybe two or three lines of code if you want to try to condense it
*  If you expand out the term inside of the softmax, which involves the product of the query and key weights
*  And you assume that this product is close to the identity
*  What you can see is that the dominant term is actually the outer product of the position embeddings with themselves
*  This results in an attention map that more or less mixes nearby pixels, very much like a convolutional filter, I would say
*  I was actually initially coming at this project from the perspective of making self-attention behave as much like convolution as possible
*  But not in a contrived way, rather in a way that a network could possibly learn from scratch
*  And so from that perspective, I would say that the product of the query and key weights being close to the identity makes a lot of intuitive sense
*  There's a graphic in the paper in which you can see that by initializing the query and keys to be like this
*  We make the attention maps, which I would say represent the actual operation of the self-attention layers
*  This makes the attention maps look a lot more like those of trained networks
*  As you train vision transformers, the attention maps get, I would say, sharper, more identity-like, more kind of vaguely like some sort of convolution
*  Our initialization mimics that effect without the need for training
*  But then that only accounts for two of the components, the query and key weights and the position embeddings
*  The third component is actually quite crucial
*  It's responsible for a lot of the performance gains that we see according to our relations
*  I'm referring to the part where we set the value and projection weight product to be close to the negative identity
*  And I'm not sure that I have a great intuition for this
*  I did speculate about it, but I'm still not quite sure why this is so important
*  One thought is that if you want to make a self-attention layer behave vaguely like convolution, you can only get so far because of the softmax
*  Because the softmax means that the attention map is purely positive
*  So you can't represent things like edge detectors, which require a positive side and a negative side
*  So that very much limits the expressivity of self-attention
*  This is a big difference in my mind between self-attention and convolution
*  If we're just thinking about the attention maps, this positivity
*  My intuition here is that perhaps by setting the volume projection weights to be close to the negative identity
*  We're essentially subtracting a similar attention map from the original one
*  It's not quite the same, it's modified a little bit, such that the final effective attention map does have a positive and negative component
*  That allows us to represent these sorts of edge detectors that are so important for vision models
*  And I have a few supporting experiments, though not that many
*  For example, if instead of initializing a vision transformer with our technique, you directly inject even just one convolutional filter per layer
*  Or even just one for the whole network into the model
*  So there's a bit of convolution inductive bias at initialization time
*  You do way better than just a vanilla transformer
*  And I think this is quite well known that convolution is a very strong inductive bias and naturally better on smaller datasets
*  So adding this to a vision transformer is advantageous
*  It makes sense that initializing a vision transformer to behave like this would have a similar effect
*  As for how I came up with the technique, I guess that's a slightly different story
*  And it goes back to the paper I was mentioning for convolutional networks
*  In that paper, we proposed a way to initialize convolutional filters to look more like trained ones, and it worked very well
*  And so my thought in initializing vision transformers was that we might want to make them behave more like convolutional networks
*  So I was trying to come up with various complex ways to encode a set of convolutional filters in the position embeddings
*  And then the query and key weights would select those from the position embeddings
*  So the resulting attention map was vaguely convolution-like
*  This was essentially a mess of a technique
*  And while it did work, I thought it would be a good idea to try it against the simplest possible baseline that did vaguely the same thing
*  Which is the method that we presented in the paper
*  And funnily enough, the stupid baseline did massively better than my initial very complicated technique to make self-attention look like convolution
*  And there was actually previous work on initializing self-attention to look like convolution
*  I found it pretty contrived in that if you want to represent a K by K convolutional filter, you need K squared heads
*  Which people don't really do in practice, and each head just attends to an individual pixel
*  So it's like a brute force technique, whereas I was going for more like just a vague similarity to convolution, not exactly convolution
*  One of the responses we've gotten to some of this work is, it looks cool, but why don't you just pre-train instead?
*  So to be clear, in some sense, the initialization that Asher has proposed here is an alternative or a training-free method of initializing weights for transformer networks
*  In terms of, from an intuitive standpoint, I think this is really interesting to think about
*  Precisely because, practically speaking, especially for small problems right now, transformers just don't work
*  Transformers work right now in the setting where you have a lot of data
*  And so to get transformers to work on small problems, even problems like CIFAR, you want to get a transformer to work on CIFAR
*  It basically doesn't work, the first approximation, and you can do all these things, but to get to work you have to have these like convolutional training mechanisms
*  That sort of help the process along or whatever, but what does work is if you just use a pre-trained transformer, image transformer, a vision transformer trained on a really large-scale image net
*  Or something even bigger, and then apply those weights to a CIFAR network, that works okay
*  You could always just start with more data, but for a number of reasons, and this touches on what we just discussed earlier, this may not be a good idea
*  Maybe you don't want to include a whole mass of data unrelated to your problem just to get transformers to work a bit better
*  Maybe you don't want to start with a fully trained, I mean just fine-tuned to your task if you don't need to
*  If all the information is contained in your task just to get a better structure or some better mechanism behind these things
*  It's a totally fair question to ask, what is pre-training doing? Why is pre-training so good?
*  Of course pre-training is good because given all this data, it's learned about the world ahead of time, but there seems to be a sense, and Asher puts it exactly this way
*  That pre-training does two things, pre-training fits the pre-training data and learns about that data
*  But it also seems to just guide the weight towards a more reasonable space, a more reasonable space
*  And so I think a guiding question behind this work is, can you do the second one, start with more reasonable weights without having to pre-train at all?
*  And that could be good for both time reasons, it could be good for reasons of data leakage, stuff like this, for legality reasons, all sorts of stuff
*  And I think this is interesting also, right? It's just really interesting to think about what are you learning from pre-training?
*  Is it all about just knowing ImageNet really well? I don't think so
*  I think it's also about just constructing a reasonable space of weights to begin with, and that I think is what this paper kind of shows
*  Yeah, definitely. I guess I'll reiterate what we were hypothesizing here is that pre-training has two components, like storing transferable knowledge and also serving as a good initialization
*  And as we were talking about in the last session, you have to wonder why we don't just strip out this harmful data instead of masking it after training on it
*  And it could be that this harmful data is somehow formatted in a way that is useful to the final performance
*  Maybe it contributes even to the good initialization component just because of its particular statistical properties
*  So it would be very convenient if we could cut out the bad data and make up for it just initialize the network in a somewhat more sane way
*  To try to draw the connection from the convolutional to the transformer, the convolutional mechanism basically defines a window of concern, right?
*  I think a lot of folks who are picking up a strong interest in AI right now are maybe even post-convolutional mechanisms in general, right?
*  They've come out of the scene after that has faded from focus
*  So in short, it's basically defining a periphery of concern, right?
*  So if you're in an image context, I'm going to look at a five by five grid of pixels for each pixel and stamp through the image, I guess, convolving literally
*  But trying to work up a layer of meaning from this local patch of an image
*  And then in doing that, you create something that has this hierarchy of meaning. There's problems with that in terms of it's hard to parallelize
*  Transformer comes in with much more parallelizable architecture and the attention map when you say you're imitating the convolution
*  Essentially, if I understand correctly, the identity or approximately the identity
*  I guess if it was purely the identity, then that would be just like each pixel only looks at itself. That would be useless
*  But so almost the identity is like a convolutional mechanism in that each pixel is looking like at itself, but also just like it's near neighbors
*  And in that way, you can set things up as if it had a more convolutional structure
*  It is funny because I mentioned that one of my inspirations for this work started back at our proposed conjure mixer architecture and its simplicity
*  And keep in mind, this is a convolutional network, but conjure mixer is itself inspired by vision transformers
*  And that we used very large kernel convolution as far as was viable to train
*  And this was in order to imitate the fact that self-attention layers have a global receptive field
*  A given pixel can pay attention to any other pixel in the image
*  So in order to make a convolutional network that looks as much like a vision transformer as possible, we made the kernel size as large as possible
*  And it's funny, I suppose, that I got to the first initialization technique for convolutional filters from the fact that these larger filters have much more interpretable structure than the smaller ones
*  If you use the traditional 3x3 filters, there's hardly any statistical pattern to pick up on
*  With, say, 9x9 filters, there's lots of structure
*  You can make lots of pretty clear observations about filters that look like edge detectors or have most of the weight in the center or crosses or something like this
*  And so it's interesting that we got to perhaps improving the initialization of vision transformers by first going back to convolutional networks, even though they were at the time going out of style
*  Trying to extend this, it's fascinating unto itself that you can literally with the naked eye, so to speak, look at a pattern and be like, hey, that looks like a diagonal
*  I wonder if we could initialize like a diagonal and save ourselves as much time
*  But also just in some sense to me is, man, there's probably a lot more where that came from
*  What directions are you thinking of taking it next? I could imagine like you mentioned like inserting like a convolutional layer in between layers of a transformer
*  That's really interesting. I think this what is the successor to the transformer and like how soon are we going to see it is a question I am asking myself a lot these days
*  But also like probably lots of other motifs, right?
*  I think it would definitely be possible to replicate more of the structures that we see in pre-transnetworks, though
*  They get a lot less concrete, harder to describe. You mentioned these quilt-like patterns in some of the query key products and some
*  I noticed that as well, but I don't really know how to interpret that or what to do with it
*  I'm sure that much more effort could be put into finding better initializations
*  The two that I found seem like the very simplest functional cases and I'm sure there's more out there
*  For example, we have no idea how to initialize the MLTs and a transformer or convolutional network
*  There is a bit of structure in some of these. You can see the same sort of diagonal pattern, but initializing them that way
*  At least as I did for the query and key weights, for example, doesn't seem to really help
*  So I'm not sure what's going on there, but there are plenty of ways I think that we could build our own intuitions into models at initialization time
*  For example, when it comes to transformers trained to generate code as a formal language, whose structure we know before training
*  And yet we have to learn to represent, say, the grammar of Python through tons of training when we knew it at the beginning
*  I believe there's work showing that transformers really do learn to represent, say, context-free grammars when trained on these sorts of formal languages in the right way
*  But it takes an enormous amount of compute, I would say, to get to that point
*  We could have just built that in from the start and spent our training time on actually learning how to program instead of merely learning what a programming language is
*  That's the main thread I've been thinking about here
*  So this isn't really a change to the architecture, but just yet another initialization
*  As for architectural improvements, I'm really not sure I have any ideas here, and I'm at a loss, I don't know that I'm qualified to say
*  It seems like the current trend is just to use more and better data within the same almost vanilla transformer architecture we've been using for a long time
*  So I wouldn't be surprised if the same architecture stays around at least for a few more years
*  And maybe there's various tricks we can use to train it better or to improve the generation process itself
*  But I don't think I can speculate very well on what architecture is next
*  It seems like architecture is not that important these days
*  Yeah, that's like the trillion-dollar question probably at this point
*  No obvious answers probably on that one
*  I think this is an awesome question, and I love this idea
*  I've been thinking for ages about what you should build in to an architecture and what you should learn from data
*  This is like the billion-dollar question of all machine learning
*  It's the subject of the Bitter Lesson by Rich Sutton
*  It's the subject of all these things, all this discussion is what should be learned, what should be built in
*  I used to be a big proponent for building in everything that we could
*  Yeah, you can make differentiable optimization problems, differentiable simulations
*  Just build this all into the networks and then only learn the parts that matter
*  That technique due to maybe slowness or other factors has just not taken off empirically speaking
*  It has not been dominant
*  And then Rich Sutton would give an argument about why this is the case for some fundamental reason
*  I do think that this notion of initialization in some sense is actually an interesting middle ground
*  That has not been explored that much
*  So we will absolutely have explored initializations
*  We definitely have looked at initializations
*  But we have not thought that much about initializations as a way to encode the knowledge that we want to encode into a network sort of a priori
*  And then let it go from there
*  This is a really I think fertile ground for potential research directions
*  Because we know that there are exist forms of transformers that by certain design can like parse different grammars or can do additions and stuff like this
*  Like we know how to initialize them that way
*  That's not the ones we're advocating for in this paper to be clear
*  But we know how to do that
*  And so I do really think that there is this interesting middle ground where we say
*  Look, initialization as boring as it traditionally seems
*  This is one like one avenue we have to imbue existing architectures with the structure that we think we want in them
*  Right
*  And I think that idea overall is a really fertile one that has largely gone unexplored
*  People think about initializations as like maintaining the weights of activations throughout the network
*  Right
*  That's the predominant maintaining variance stuff like that
*  That's the predominant view
*  I think we could maybe go beyond that
*  There's a lot you can do with initialization
*  And I think we've just started to really fully explore that
*  Again with this curriculum learning notion
*  I wonder we did an episode with the authors of the tiny stories paper out of Microsoft
*  Oh, yeah, I'm actually working in that group now
*  Small world I suppose
*  No wonder that all this is tying together
*  But I guess what I'm thinking is because these things are small
*  What was notable about their work was they were able to get some like more sophisticated behaviors at small scales
*  At that small scale by really controlling the data
*  Controlling like shrinking the vocabulary such that I think the heuristic was like a third grader or a three year old or something
*  Should be able to like have the vocabulary for all of the content
*  And because they shrink the vocabulary so much
*  Then even at a smaller scale they were able to start to see more of these like reasoning capabilities develop
*  With still pretty simple things but things that GPT-2 with a hundred times as many parameters or whatever still often couldn't do
*  They would get these small models to do
*  So I wonder take that to a limit
*  Take some small model and do just like pure logical generations
*  Like literally just P's and Q's and like knots and set symbols and things like that
*  Just like a very super reduced grammar but like very high logical content
*  Try to create like small models and just push like how hard can we brock
*  And then maybe you'd have to do something else too where you might think jeez there's a lot of noise in these
*  Maybe I need to train like ten of those
*  And I can imagine there might be some need to like untangle certain symmetries
*  Like I've seen a bunch of papers where there's a process of
*  They often use the term like aligning but I think of it almost as more like polarizing
*  A set of weights such that then you could maybe look at like averages or differences between them
*  And try to see if you can't identify some of these motifs that are responsible for these kind of logical capabilities
*  Because it does seem like you can get that down pretty small
*  Like it doesn't seem like it I think it has emerged in these large models
*  Maybe you would disagree with this but it seems to me like it has emerged a lot of times in these large models
*  Because with so much noise it takes that long for it to emerge
*  But if you like greatly reduce the noise you might be able to get it to emerge sooner
*  And if you do like other ways to cut through the noise
*  Maybe you can identify like more motifs that then could become like a great shortcut in future projects
*  So now's when you can tell me that you either tried all that and it doesn't work or you're working on it right now
*  Or it sounds crazy but that's where my head's going
*  Yeah, those are great thoughts and that's not exactly what I'm working on right now
*  But I know there is some related work at least
*  For example, I mentioned this Lego paper also out of the group at NSR
*  And that's one of the three papers I'm currently thinking of when I think of memetic initialization
*  What they did there was more or less exactly what you said
*  There's this very small sort of strictly logical task that they tried to train both small and large transformers on
*  And tried to see what factors contribute to being able to accomplish this task
*  And the finding was basically that if you train a transformer from scratch on this data set it doesn't work at all
*  If you use a pre-trained transformer it works quite well
*  And the difference between the two seems to be the presence of certain types of attention heads
*  Like association and induction heads
*  These are basically just merging nearby tokens or copying similar tokens
*  Things like that and that you can try to replicate these structures in more or less untrained networks
*  In order to achieve similar performance on this circumscribed logical task
*  And the main difference with my work is that they added these structures to the transformer by training them to look like pre-trained transformers
*  So if they wanted an induction or association head they would explicitly regularize some heads in like a sort of pre-training procedure to be close to that operation
*  My thought was basically that you shouldn't have to train at all
*  You should be able to define these types of heads by hand
*  I haven't actually pushed my memetic initialization work that far on language
*  But it seems very much like you can absolutely encode these things by hand
*  And without requiring any sort of training get the association and induction heads that would allow you to do these sorts of logical or arithmetic or what have you tasks
*  I've seen some other work like this too
*  If I understand correctly you're saying literally designing a certain algorithm or whatever into the weights
*  As opposed to going and trying to find the patterns is also like another maybe even more viable option in some cases
*  You could personally think about the task and what sorts of operations would be useful and then try to encode those by hand into the untrained network
*  Or you could also look at pre-trained networks like the Lego paper and try to localize what particular properties are contributing to performance on the task and then replicate those
*  And I think that in all of these cases you shouldn't have to do any sort of training to bring this about
*  It might be a bit tricky but I think that you could probably even encode the grammar of a programming language into the network somehow more or less by hand
*  Which I don't think anybody has done yet but I think is something that ought to be possible
*  A broader point here is that there's surprisingly little related work
*  There's basically just these three papers
*  As far as I know maybe you've seen more I'd be curious to hear
*  But like Sikua was saying most of the work on initialization has had to do with mathematical properties
*  Does the magnitude of the signal remain constant over the course of the layers during training or something like this
*  But very few works have considered the structure of the weights so how they affect the mechanism of the network
*  I think there's tons of room for more work in this area very much like what you proposed
*  Yeah interesting I might have to pull up Elicit and look for papers on this topic
*  I don't know if you're an Elicit user but Elicit.org is an AI powered research assistant targeted at you, grad student, researchers
*  I think their approach is really interesting. They're a previous guest as well on the podcast
*  But they take a very kind of decompositional approach setting up the product
*  Meaning they're not just throwing like the extreme other end would be like here's a whole paper, throw it into Cod2, ask a question
*  Their approach is much more break the paper down, ask very specific questions, do everything in a very kind of procedural and ultimately like much more traceable way
*  So a lot of the work has gone into breaking these tasks down into subtasks, subtasks and so on
*  But the result of that is that you can now ask these kind of basically like literature review sort of questions
*  And it will give you back like tabular kind of results on here's all the relevant papers that were found
*  And then you can start to ask like more detailed questions about them and essentially add columns onto your data set
*  So it'd be a cool thing to go try and see what else you might surface
*  Yeah, that sounds cool
*  One that is coming to mind that I think they took a very different angle on it from what you're doing as I recall
*  But I think it was late last year there was a paper that showed basically that the weights themselves were implementing gradient descent
*  As part of the way that few shot learning was happening
*  And I think the way that they did this was, as you said, a hand coding linear algebra representation of gradient descent
*  And then went looking for it in trained models
*  But starting from this is how we have implemented it ourselves
*  Now can we go detect patterns in trained models that are like this
*  And sure enough, they did
*  And this sort of like meta runtime learning seems to be powered in substantial part by this kind of gradient descent algorithm that the models themselves are learning to implement at runtime
*  So fascinating
*  What I don't know if they extended that into was like taking that and saying, geez, hey, why don't we start with our pre-trained version
*  That could potentially make a lot of sense, potentially could get some of these meta learning behaviors a lot sooner
*  Again, it seems like the fact that GPT-3 could do that at all is it's an echo of a pretty small portion of the data set
*  If you had that as your kind of initialization, maybe you get that out of the gate or very close to it
*  Of course, you could also could probably lose it
*  So you probably would need to also sprinkle some few shot examples into your pre-training mix just to make sure it doesn't go away in early training
*  Yeah, this sounds really interesting
*  Somebody ought to look into this
*  You're not busy, are you?
*  Just a little bit
*  It's a target rich environment
*  How many ideas do you have that you think are interesting relative to what you could actually pursue?
*  I don't currently have a running list, but it costs a lot to pursue an idea
*  So definitely many more ideas than actual concrete research projects
*  And in fact, most research projects that I start don't really go anywhere
*  So I think this is the case for most people, I assume
*  But yeah, ideas are pretty cheap, but fully executing them is quite hard
*  What would you say your funnel looks like? Is it something like to take a bar of this idea that I just came up with?
*  If you say, yeah, that sounds... somebody ought to look into that
*  So how many somebody ought to look into that do you have for everyone that you actually try to look into?
*  And how many of those do you have for every thing that you actually get through to a result?
*  Maybe like I actually pursue one in three ideas or something
*  And some of the ideas can be rolled out very fairly quickly or they simply look too challenging to going anywhere very quickly with
*  My main heuristic is what sounds like the most fun
*  And I think that's completely personal
*  For example, on the last two papers, I just got completely addicted to trying to find structure within the weights that I could replicate
*  Somehow the mimetic initialization for Transformers idea came about a lot more easily and was executed a lot more smoothly than the convolutional network one
*  Maybe just because I had that prior experience with kind of a similar topic
*  Yeah, I was mostly motivated just by fun in particular on the convolutional network project
*  Because I could see that there was this kind of statistical structure in the weights that I could maybe replicate by hand like on paper
*  If you gave me like some markers, I could probably replicate the structure though I'm no artist
*  But to describe that mathematically was very hard
*  So I spent a lot of time just trying to find some sort of way to succinctly describe what was going on
*  And rolled out tons of very complicated models with lots of parameters that themselves had to be optimized before coming up with this pretty elegant representation
*  Yeah, I'm not sure if other people have a different approach to research
*  But I think that this is maybe not the most common strategy, but there are at least several people I know that work in a similar style
*  Yeah, it seems like that's a maybe reflection also of just where the field is at, right?
*  Such a target rich environment, so many things that are unexplored in a much more mature field
*  You might not have the luxury of being quite so fun oriented
*  But I think that's a big part of why people are so attracted to ML, AI, ML right now
*  At least for me in part is because I genuinely feel like I'm the first to see a lot of stuff and that in and of itself is super cool
*  And there are a lot of things that you can just pop into pretty quickly and at least learn something
*  Even if it's not like a paper, our own loss curve is still pretty steep in terms of our ability to understand so many things
*  Yeah, absolutely. It's a really fun time in the field for sure
*  Seems like more so than anywhere else, you can just jump in and start asking the big questions
*  I mean, you do need a bit of a few resources, maybe like a handful of GPUs, which not everybody can get
*  But that's quite attainable and then you can ask questions like what's the deal with pre-training anyways
*  Even though you don't have like industry level funding or anything like that
*  And there's always the possibility that your findings at small scale will actually work on like GPT-4 scale things you never know
*  So yeah, it's super exciting and seems like it's uniquely fun. That's why I'm here
*  Anything else you want to share about this work?
*  We made some valuable connections here, like I didn't see the connection to ND's robustness work
*  But it seems to all be wrapped nicely together
*  You need to make models more robust maybe by getting rid of bad data
*  The direction at Microsoft, I'm currently interning, if you've seen the recent textbooks or all you need papers
*  It's very much about improving data quality and then making up for getting rid of the bad data, for example, with a better initialization
*  That's a nice package. I like it a lot and I didn't see the full package until now, so I appreciate it
*  Cool. I appreciate you guys taking so much time. You've been very generous with your time
*  And I'm sure the audience will learn a lot from this conversation
*  In conclusion, Zico Kolder, Andy Zou and Asher Trockman, thank you for being part of the cognitive revolution
*  Thank you
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work
*  Customized across all platforms with a click of a button
*  I believe in Omniki so much that I invested in it and I recommend you use it too
*  Use Cogrev to get a 10% discount
