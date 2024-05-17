---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 7219s
Video Keywords: []
Video Views: 4786
Video Rating: None
---

# The Tiny Model Revolution with Ronen Eldan and Yuanzhi Li of Microsoft Research
**Cognitive Revolution "How AI Changes Everything":** [June 06, 2023](https://www.youtube.com/watch?v=mv3SIgDP_y4)
*  One of the most important abilities for generative models is to be able to speak coherent English.
*  Her mom didn't let her have a dog so she asked for a dog.
*  When you try to autocomplete this, now the most common noun that you've seen so far,
*  or so the most proximate one, is dog, not cat.
*  Dog already appears twice in the sentence.
*  Even GPT-2XL, which has 1.5 billion parameters, its most likely completion is still dog.
*  I'm just going to read one tiny story just straight out of the paper because I think that will help people understand what this dataset ultimately is.
*  Tom has a big pot of soup. He wants to share it with Jane.
*  Jane takes a spoonful of soup, but then she makes a face.
*  The soup is, that's the prompt, and then you show a completion, very bitter.
*  She does not like it. She says, I don't like this soup, it is too bitter.
*  He looks around the kitchen and finds some bread and cheese.
*  He puts them on the table and says, here Jane, you can have some bread and cheese.
*  They are not bitter, they are sweet and yummy. Jane is happy.
*  She says, thank you, Tom, you are a good friend. I like bread and cheese. They are not bitter.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers, entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas, and together we'll build a picture of how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today's episode is great for anyone who really wants to deepen their understanding of, and intuition for, how language models really work.
*  Certainly, as measured by how much I learned in the course of the conversation, it's one of our very best.
*  Our guests, Ronan Elden and Yuanjuli of Microsoft Research, have created a small natural language dataset called Tiny Stories,
*  which they designed to reflect the full richness of natural language, while still being small and conceptually simple enough to support research with modest compute budgets.
*  They did this by using GPT-4 to systematically create 1 million children's stories, using only words that an advanced 3-year-old could be expected to know.
*  Dataset in hand, they then began to explore a number of aspects of language model performance, behavior, and mechanism by training a series of models that range in size from just 1 million to a maximum of 33 million parameters.
*  Still just 2% the size of GPT-2.
*  They then used these small models to explore the development of language model reasoning abilities, identifying so-called logical primitives, beginning with a basic understanding of grammar, followed by the learning of facts, and then eventually adding certain logical microskills, such as negation and exclusion.
*  These findings create the perfect context in which to discuss the tricky and often controversial topic of emergence, as well as to compare and contrast how large language models learn with how human children learn,
*  and to explain how the differences that we see across language models and children do in fact make some sense, given the different incentive structures in play in each case.
*  They also did some great interpretability work in this paper, and I really relished the chance to get into all three areas that they explore.
*  First, they look at the trade-offs between the number of layers in a transformer, which to a large extent governs the number of logical leaps that a model can make, with, on the other hand, the width of a layer, which seems to determine how many facts the model can store.
*  They also identify attention heads with distinct roles, including distance heads, which simply reflect the distance between tokens, and which look almost exactly like the alibi scheme, which is now powering long context models such as Claude 100k and the recent Mosaic ML65k release,
*  and then, on the other hand, semantic attention heads, which focus on meaning. That there should exist such completely different attention heads within a single model, and that an alibi scheme should emerge in the wild, is really, to me, mind-blowing.
*  Finally, they examine the role of individual neurons, finding that many of their small model neurons do in fact correspond to human interpretable concepts.
*  We close the conversation by zooming out and discussing why small models are more interpretable than large models, the challenges inherent in attempting to extend this work to larger scale models, and why controlling language models might end up being more like horseback riding than microbiology.
*  Throughout this conversation, I was really struck by two things.
*  First, it seems to me that we've only scratched the surface of the potential for curriculum learning approaches.
*  I fully expect that we'll start to see ever more sophisticated approaches, which use specific datasets to layer on specific skills in a strategic, progressive manner, creating highly specialized small-scale models that can solve specific problems extremely efficiently.
*  Second, the value of these toy models for developing understanding really is tremendous.
*  If I could make just one suggestion to listeners, if you want to get the absolute most out of this episode, it would be to visit the Hugging Face website and try playing around with some of the bigger models that they've released.
*  The very biggest are still only 33 million parameters, which means that they can load easily and run quickly right from the Hugging Face model page.
*  If you do that, as I did in preparation for this episode, you will actually have the chance to explore a lot of the concepts, and you can set up your own little experiments to test the reasoning ability of these models.
*  I guarantee that you will come away with a deeper understanding that you will retain for longer and much better.
*  And if you do find anything interesting, I would love to hear about it.
*  So please do reach out to me via our email, tcr at turpentine.co or on Twitter, where you can always DM me at LeBenz.
*  Now, I hope you enjoy this elucidating conversation with Ronen Elden and Yuanju Li of Microsoft Research.
*  Ronen Elden and Yuanju Li, welcome to the Cognitive Revolution.
*  Thank you so much. We're super happy to be here.
*  You guys have just published this paper called Tiny Stories, and I think it's a really fascinating bit of research on multiple levels.
*  So I'm really kind of excited to dive into it with you guys.
*  It touches on a bunch of different themes, including some of the hot button themes that we'll get to around emergent capabilities and reasoning.
*  And, you know, you guys are studying this in a very unique way that makes the problem easier to solve.
*  I think more tractable and more approachable, hopefully, for our listeners as well.
*  So I'm really excited to introduce this work to them.
*  Maybe just for starters, can you give me a little bit of an introduction to what inspired the Tiny Stories project?
*  I guess I'm kind of new to LLMs or deep learning in general.
*  I come from pure math.
*  And when I started looking into, you know, architectures, trying to understand what those models are actually doing, how to improve them, et cetera, et cetera, I got very quickly.
*  I got very, very frustrated because it's very easy to come up with ideas.
*  But in order to actually check whether an idea is actually working, I had to go through a lot of research.
*  It's very easy to come up with ideas.
*  But in order to actually check whether an idea is good, almost always you need to do an experiment that involves a lot of compute.
*  It's just very, very hard to check things.
*  You need to, you know, you can either train small models, which basically don't do much in terms of, you know, they don't actually generate text that sounds coherent.
*  You can train like maybe a bird-size model, and then it'll do something on some downstream tasks.
*  But whatever it does doesn't look much like what those LLMs are doing.
*  If you want to really get an LLM experience, you need to do an experiment with a lot of compute that involves, you know, tons of GPUs, et cetera.
*  So, you know, for me, it was just a way to address the frustration of not being able to get any insights without, you know, having to do a large experiment.
*  And so the main way that you have accomplished that, if I understand correctly, is by kind of narrowing the conceptual space of what both the data set contains and then obviously what the model is trained to do, right?
*  Instead of taking, you know, a small cup out of the whole ocean of mixed up of everything language, you've created a kind of we're going to we're going to tackle one, you know, very consistent type of input.
*  That's fair. I guess we should mention there have been many attempts to come up with a synthetic or non-synthetic, a smaller data set that has all those elements.
*  That those large language corpora have, right?
*  So, you know, in language, you have all sorts of elements. You have a lot of facts you have.
*  So first of all, you have grammar and vocabulary, right?
*  Those are the obvious things you have in language.
*  But then you have facts, you have reasoning that you can infer from those texts.
*  And there's like also many layers of reasoning and, you know, there's I guess there are many capabilities involved in being able to parse those data sets.
*  So, you know, our initial motivation was to come up with a data set that has all these qualitative elements.
*  But on the other hand, is just not as massive as those large language corpora.
*  And, you know, you and you and I had so first of all, there as I said, there are many synthetic data sets out there.
*  Some of them, I think, reflect in a in a pretty good way certain aspects of language, such as reasoning or facts or grammar or stuff like that.
*  But we felt like there is no single data set that has all those dimensions together, which are all integrated into something which is not too large.
*  Right. And we felt like in order to understand in order to gain insights about LLMs, we need a data set that has all those elements.
*  Yeah, I was just going to add that I also came from an email background.
*  And so I was doing theory of machine learning since maybe seven or eight years ago when the field just got started.
*  And, yeah, at that time, like everyone was doing research on vision models.
*  And for vision, there's a very nice data set called C bar 10 or even MNIST.
*  I mean, those are very small data sets. They only have like 50K images.
*  And when you train on those data set, you can get a pretty high quality image model and they can do all sort of things and they reflect what's going on in real large models.
*  And I mean, at that time, doing research on making progress on both theory side and applied side is kind of easy because they just training those models only take like one day at most.
*  But when we move to this phase of large language model or language model in general, the research has become so expensive.
*  And I've seen all those blog posts saying that it's impossible to do a PhD now in machine learning without like 8A100.
*  And I mean, probably only one percent of the PhD students has that amount of computing.
*  So we really want to see whether there is a way to kind of bring the good old days, which are like those C bar data set of fast experiment iterations back to the language side.
*  And that's what motivates us to consider this small data set or this simple data set.
*  I think the point is, I mean, there are other kind of synthetic data set or simple data sets that are, as Ronan said, reflecting some aspects of natural languages.
*  But they are not real natural language. They are like just doing simple arithmetics or doing simple like stream matching or number manipulation.
*  I mean, they are not real natural language and we want to keep the authentic of natural language, but just reduce the overall complexity.
*  So it's still we are studying natural language and not some symbolic manipulation.
*  And still we want the iteration or experiments to be done in a very quick way.
*  You created the tiny stories data set. I always like to be as concrete as possible.
*  So I'm just going to read one tiny story just straight out of the paper because I think that will help people understand like what this data set ultimately is.
*  But then she makes a face. The soup is now this is just an example presented from the paper.
*  That's the prompt. And then you show a completion and you compare and contrast this against other open source models.
*  But I'll just read the 28 million parameter version that you guys trained.
*  The soup is very bitter. She does not like it. She says, I don't like this soup. It is too bitter.
*  Tom is sorry. He says, I'm sorry, Jane. I didn't know you don't like bitter soup. I will make you something else.
*  He looks around the kitchen and find some bread and cheese. He puts them on the table and says, here, Jane, you can have some bread and cheese.
*  They are not bitter. They are sweet and yummy. Jane is happy. She says, thank you, Tom. You are a good friend. I like bread and cheese.
*  They are not bitter. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it to use Cogrev to get a 10% discount.
*  So there is our whole tiny story. And I read it almost like I'm reading to my four-year-old or my two-year-old because it is kind of a children's story.
*  And I understand that that also is kind of part of the motivation. So how did you create this data set?
*  How did you kind of how do you conceptually think about those stories you told us a little bit already as kind of having those key elements of the grammar, facts, some amount of like reasoning required?
*  But how did you create them? How big is this data set?
*  From this motivation to have a good synthetic data set, we should just point out that this is maybe the most natural idea is to rely on human development.
*  Right. It already has the solution for us. Because young children, they are able to speak English somewhat, like mostly coherent coherently.
*  I have a daughter. I can testify that not extremely coherent coherently, but somewhat coherently.
*  And, you know, this is there's already a solution to this coming from like human development.
*  Right. So all you have to do is just create a data set and make sure that it will be basically that any example can be understood by a small child on one hand.
*  And on the other hand, you want it to spend as much as possible of, you know, the knowledge that a small child has.
*  You want it to be as diverse as possible.
*  And we decided, you know, that it makes sense to have this data set somewhat structured.
*  So just the structure of a story, it kind of makes sense because into a story you can inside a story you can have all those elements combined together.
*  Right. Grammar, facts, reasoning, stuff like that.
*  And we just, you know, I think it's a really good time to try to create this data set because finally we have those, you know, models GPT 3.5 and GPT 4, which those models can actually understand the instruction.
*  You know, I want a story which is somewhat creative and only has very simple words.
*  Right.
*  So GPT 4 wrote these stories?
*  So yeah, most of those stories were written by GPT 4, some of them by 3.5.
*  3.5 is already good enough to write those kind of stories.
*  It's not that great.
*  GPT 4 is definitely doing a better job.
*  Now, it's pretty easy to just write a story, right?
*  Just if I just want to write a short story, even GPT 2 can probably write a decent short story.
*  The problem is to actually get a diverse data set that spans, you know, all the vocabulary that you actually want to span.
*  And if you just ask even GPT 4, create a short story and you do it a thousand times and you do it with temperature, with rather high temperature, let's say temperature one, which kind of gives rise to the most diversity you can get.
*  Still about one fifth of the stories will be about children being scared of the slides at the park.
*  We actually did this experiment.
*  So it's not very creative.
*  If you just tell it to create a story without any other instructions, you're going to get a very repetitive data set.
*  And the whole game is how do you get diversity?
*  How do you make the data set, you know, not be very repetitive?
*  And here the idea was just to collect a list of just the vocabulary of simple words.
*  We have about 2000 words, which supposedly three year olds understand.
*  And then what we do is we just ask GPT 4, OK, here's one random verb, one random noun and one random adjective.
*  Try to combine these into a story in a creative way.
*  We do about a million calls like that.
*  I think we have about 1.5 million stories in the data set.
*  So on one hand, they definitely span all this vocabulary because there's only 2000 words.
*  But on the other hand, you definitely do not span all possible combinations of, you know, words.
*  So you know that you're not going to, you know, it's not if you can later create a story with some prescribed combination,
*  you will have demonstrated that the model has some creativity inside it.
*  Yeah, so that's how we created it.
*  That's really interesting. Just to do a little bit of math on this.
*  So a million stories, which first of all, that answers the question of why not go use real stories?
*  Because that's a lot of books to scan.
*  So there may not be many children's books there are.
*  You'd have to get your hands on a whole lot to get to a million.
*  So the need for the synthetic data is there.
*  I'm interested in what you were seeing that was like way better about GPT-4 versus 3.5.
*  It sounds like with the stories that were repetitively about the slides,
*  I would interpret that as maybe like mode collapse, like reflection of kind of, you know, effective RLHF likely.
*  Is that how you would understand that too?
*  I think it's mostly just the model is pre-generating the most likely stories because that's what the model is trained.
*  If you don't give the model any content, you will just feed all the most likely stories
*  because it wants to minimize its language model loss.
*  So potentially just a child scared of the slides is the most common story yet that exists on the internet.
*  So the model just learn to generate it without any given condition.
*  So that's why we want to create some condition to move the model outside this particular high probability zone.
*  One difference that we see between GPT-3.5 and GPT-4 is after it, so you give it three words,
*  it needs to combine them somehow in the story.
*  And sometimes it's not that easy.
*  Even if I give you three words, I don't know, I think there is an example there.
*  Ancient, thunder and sad or something like that.
*  You want to combine them in a way that won't look kind of too superficial.
*  You want to create a story that actually seems fluent and you don't want like a complete change of topic
*  in order to, you know, be able to combine the next word.
*  And GPT-4 seems to be able to do this pretty fluently.
*  Whereas GPT-3.5, sometimes you get stories that don't make so much sense.
*  The words appear there, but they don't appear in a very satisfactory way.
*  It totally makes sense also for you to note, like, yeah, maybe this is just the most common story.
*  We don't necessarily have to invoke any like exotic theories of why it keeps talking about slides.
*  But I wonder if the non-RLHF version, you know, if you had access to kind of the base GPT-4 model,
*  if that might have been different.
*  I had the opportunity to red team the GPT-4 early before it had all the safety measures,
*  but it did already have the RLHF and, you know, kind of the instruction following capability.
*  I never saw the like totally base model.
*  I don't think that many people did.
*  The technical report, they said it was not, you know, not people weren't sure what to do with it.
*  Right. So I think they maybe put that one out to pasture.
*  Did you guys try any different versions of GPT-4?
*  Obviously being, you know, at Microsoft, you might have some privileged access to different versions
*  that the rest of us wouldn't have.
*  Yeah. So we did.
*  We did have access to an earlier version that I mean, you know, we're not sure about the exact technical,
*  like what the difference is from the model that's now available to the public,
*  but that model had less safety features on it.
*  But as you said, it may be the same model you had access to.
*  So it did have a certain extent of RLHF. Right.
*  Now, I think if you take, you know, just the language model trained on the pile without any RLHF
*  and you say, you know, create a story such that blah, blah, blah,
*  maybe the most plausible completion in terms of a random, you know, entry from the distribution of web pages
*  is I don't want to do it.
*  Like write me a story such that, that the question answer, I don't feel like it.
*  Or, you know, it could be that, you know, instead of completing the story,
*  it's just going to ask, you know, another question without any RLHF,
*  without any alignment that the model has to, I mean,
*  the model doesn't know that it's supposed to actually perform your instructions. Right.
*  You know, that's the most basic part of it.
*  But I think that the RLHF they did on GPT-4 is just good enough so that it makes sure to,
*  as accurately as it could, actually, you know, satisfy the constraints that you give it.
*  So it almost always combines the words that you ask it to combine into the story.
*  And also it almost always actually writes a story that only uses simple words.
*  Yeah. I think as Ronan pointed out, the biggest difference of the base like GPT-4 model
*  compared to this RLHF version is just following instructions.
*  I mean, for base model, you can give it as a beginning of the story.
*  The completion is very good.
*  But if you just say, write me some story that combines certain elements,
*  then the model has a very hard time understanding the instruction
*  because those things are very rare in the internet.
*  It probably needs some fine-tune so the model understands what does it mean by an instruction.
*  It's not like a conversation. It's an instruction when you ask, write me a story.
*  Yeah. Makes sense.
*  At best, you could maybe do a few-shot approach,
*  but then you probably have, I've seen a lot of issues with over-indexing on the examples as well.
*  So yeah, I totally, totally get it.
*  A few-shot approach would probably prime the model into thinking of specific plots also.
*  I'm doing some AI 101 type education at a friend's company right now called Athena.
*  And I was just doing a webinar this morning where I was getting into that with folks saying,
*  if you are going to do a few-shot, probably don't do one example in your few-shot.
*  At least do two because otherwise you tend to get this over-in-context learning
*  on just the one example you gave. So yeah, I'm with you on that for sure.
*  So a little bit of math. So there's like 2,000 words.
*  There are, let's say that's just to take a round number, a thousand each of kind of the verb, the noun, the adjective.
*  So that in pure extended form is a billion possible bags of three words,
*  roughly order of magnitude. Right. So then you made a million stories.
*  So I just wanted to establish that the space of possibility versus the actual data set that these models were trained on
*  is about a thousand to one ratio. Do I have that roughly right?
*  That's true. I think it's pretty accurate.
*  Only in addition to those three words, we also have another way to add diversity,
*  which is a bunch of features we ask GPT to add to the story, such as a plot twist, a bad ending, dialogue.
*  So that adds a little bit more diversity.
*  But one in a thousand is a pretty good like ballpark estimate of the ratio.
*  Cool. And then just cost of this, if we were going to pay like retail price for GPT-4 to write all these million stories,
*  that would be if each one is, say, three hundred tokens, I'll just take a nice round number because that maybe equates it to roughly one cent per.
*  It would be like a ten thousand dollar GPT-4 retail price to generate the data set.
*  That's pretty accurate.
*  OK, cool. So then this curriculum concept is, I think, super fascinating.
*  And this is one of the areas that had me so intrigued by the paper.
*  You're taking inspiration, you know, obviously, as you said, from human development and, you know, starting with simple words, which definitely makes sense as an approach.
*  I always kind of try to keep in mind as well that like these things are very alien.
*  And, you know, I do I'm very intrigued by this curriculum sort of approach.
*  But I wonder what about like more weird curriculums?
*  This is me outside of the scope of like this particular research.
*  But I kind of keep waiting for somebody to show up with a like we trained it first on like pure logic notation.
*  You know, we've seen this a little bit. It's kind of been discussed a lot recently that the code pre-trained models seem to demonstrate better reasoning.
*  You know, once the kind of language part gets added on, you know, obviously, who knows exactly what that baking recipe looks like.
*  How do you guys think about that? Like, do you expect the same thing that somebody is going to pop up with a hey, we did a pure logic or we did like, you know,
*  just massive amounts of like abstract algebra first and kind of taught some sort of, you know, structure that we then were able to layer natural language onto?
*  It could definitely help because we based on our previous research on the I mean, attentions in language models.
*  There are kind of some simple attention mechanisms that the language model may have.
*  The first one is just is associating two tokens that are exactly the same.
*  And the second one is after it associated two tokens that are exactly the same.
*  It also copies the tokens around the first token to the second token.
*  So it's just like us when we read some word, we go back and see what's the previous time that this word appear and what's the surrounding context.
*  And I think just training this head is actually pretty expensive.
*  It requires a lot of training data and something like coding or logic is the perfect way to train those heads because for coding, when we define variable,
*  we definitely need to look back like what's the previous definition or when we call a function, like we check that function, we see what the function is doing.
*  So it kind of may set the language model into learning those important concepts like look back or checking the surroundings.
*  And that may serve as a very good warm star for training on other things like simple natural languages.
*  It may make the model learn much faster.
*  Yeah. So maybe let me I mean, another way to say what you just said is.
*  Yes, I mean, we do. We do observe this to a certain extent that, you know, maybe coding improves models reasoning.
*  I think at this point, there is no like overwhelming evidence that this is actually the case.
*  But there are some observations.
*  But we are not sure at all that the reason behind it is that, you know, when the model learned how to write code, it actually learned how to reason.
*  It looks like rather the reasons that this this works are there.
*  The explanations are just much simpler.
*  You just managed to calibrate the exact attention heads that you need.
*  And those attention heads don't have any particular sophistication in them.
*  They might just be able to very accurately look at some relative position to a given token or just compare two tokens in a very precise way.
*  And so that means the reason is more like the types of components in your neural network that are required for coding are already there.
*  But those components are pretty simple.
*  It's not like the network has like very sophisticated neural paths that, you know, emerge after the training that actually know how to do reasoning.
*  And for that, we we actually have a paper we wrote at Microsoft Research about a synthetic task called Lego.
*  So this is a very basic synthetic task that has the core elements of reasoning.
*  And what we observe there is that we use a transformer based on a BERT architecture.
*  And what we observe is that the pre-trained BERT transformer basically grasps this reasoning task much faster.
*  The task is is something simple.
*  It's basically you get a string that looks like A equals to one, B equals to minus A, C equals to minus B, D equals to C, et cetera, et cetera.
*  And you have to resolve the values of our variables.
*  And, you know, at first we thought, you know, maybe there is some in some kind of profound sense.
*  The pre-trained BERT model has learned how to reason.
*  And this is why it grasps this task so well.
*  But if you dig into it just a little bit, what you realize is the explanation is just much simpler, much more superficial than that.
*  It's just the pre-training has given rise to some simple attention heads that if if you just initialize the model,
*  initialize the model with those attention heads, then it basically grasps reasoning much faster.
*  This explanation is is is much closer to what actually happens when you train a model to code and then it exhibits better reasoning capabilities.
*  So this is maybe a good time to talk about what we mean by reasoning.
*  And I see a ton of confusion out there about this.
*  Maybe you can help us get a little bit more clarity.
*  I guess one thing that I kind of observe is, you know, of course, people are debating this capability.
*  And it seems like, you know, you've got kind of different standards of evidence or like, you know, people put the burden of proof in different places to put my cards on the table.
*  You know, I kind of conceive of myself.
*  I call myself these days an AI scout, and I'm really interested in like, what is possible?
*  What can be done?
*  Not necessarily holding the systems to the standard of that they can do it every time or that they can do it in all cases, you know, or it certainly matters like how adversarially robust they are.
*  But, you know, I wouldn't say, oh, well, we found an example that it failed on.
*  Therefore, like it, you know, can't do X if it could do X nine out of ten times before it got to that kind of crazy example.
*  But how are you guys thinking about reasoning as, you know, something more than a binary, obviously, in the context of this research?
*  Initially, we think reasoning as something that is just a subset of consistency.
*  When we generate sentences or when we say things, we need to make sure that they are consistent with what we said before.
*  And there is like the first level of consistency, which is just a nearby words.
*  They need to follow some grammar rules and follow some basic semantics.
*  And those are not really reasoning.
*  It's just some simple, like more like stochastic parrot where you just do simple pattern matching, just look at the previous like couple words and just generate one that is consistent.
*  Well, I think what goes to reasoning is when the consistency goes to the next level, which is you really need to consist, be consistent with like something very far away from the current token, like something consistent with the general plot of the story.
*  For example, there's a word plot and then you need to say something in the opposite order.
*  And those level of consistency, they are the primitives of reasoning.
*  So we do think that anything beyond just local consistency should be think of some ability that is reason.
*  The first thing we have to say is that type of reasoning we're thinking about is a very, very basic.
*  It's just some basic core capability that comes with speaking coherent English.
*  Some people, I guess, still say that large language models will never be able to reason.
*  I guess they have a very, very different definition of what reasoning means than what we have.
*  I mean, what we mean by reasoning is really like the capacity to just apply some basic logics when you generate text.
*  And I think maybe to be concrete, we can look at one of the examples in the paper.
*  So if we look at the sentence like Lily likes cats and dogs, she asked her mom for a dog and her mom said no.
*  So instead she asked and then you do autocomplete.
*  We kind of see it as a hierarchy of capabilities.
*  So some words in this sentence, in order to complete them, to know what the next word is,
*  you just need some very, very basic grammatical rules.
*  For example, she asked her mom for the next word is a for this.
*  You only need to know a little bit of grammar and that's it.
*  Now, the next word after a she asked her mom for a dog.
*  Well, you know that if you just know grammar, you know that the next word should be some noun.
*  But here you already need to have some, you know, contextual tracking of, you know, what's going on in the text.
*  The relevant nouns here could be are probably dogs and cats.
*  Right. Those are the two objects that were mentioned in the sentence before.
*  Now we go to the next sentence and you know, you say like her mom didn't let her have a dog.
*  So she asked for a and when you try to autocomplete this now, you know, the most common noun that you've seen so far.
*  Also, the most the proximate one is dog, not cat dog already appears twice in the text.
*  It appears twice in the sentence.
*  You know, she likes dogs and cats.
*  She asked for a dog or a mom said no.
*  So our smaller models actually complete this by saying dog and even GPT to Excel, which has one point five billion parameters.
*  But this most likely completion is still dog because it's still at that level where it is it did resolve that there should be some noun there.
*  And it does know how to look back in the sentence and see that.
*  OK, there is there are two nouns dog and cat.
*  But, you know, dog appears more.
*  So it's more likely that, you know, if I just had a dog in the previous sentence or in the just five words before, it's going to be dog again.
*  But on top of that, if you have a very, very basic reasoning capability, then.
*  You're supposed to be able to apply elimination and realize that, OK, she can't have a dog.
*  We had the set containing the two objects dog and cat.
*  But now dog is not allowed.
*  So what's left is cat.
*  You know, we we thought this is one of the most basic examples of a completion that would require some extent of of reasoning.
*  There's always this notion.
*  I mean, this intertwined between reasoning and planning.
*  For example, when we say reasoning, many people would think about mathematical reasoning like I prove a mathematical theory.
*  And that's not only reasoning. It's also planning.
*  I need to come up with the correct method.
*  I have the intuition like what's the next step should be.
*  And for us, the reasoning that we are more interested in is just consistency.
*  Like you should say something that are consistent with what you previously said.
*  And the consistency is not only local, it's global.
*  And that's where kind of we think as the reasoning for natural languages.
*  The only thing it needs to do is generate text that's consistent with the prompt.
*  Like that's that's the only objective a language model has to, you know, fulfill.
*  The next word it generates should be as consistent as possible with all of the prompt in order to achieve this consistency.
*  There are several different levels.
*  So for most words that it generates, the only capability that's actually needed is grammar or maybe not for most words, but for many words.
*  Just by knowing some grammatical rules, you know, you know that if you have a sentence, Amy wanted, the next word is probably to she wanted to something.
*  And you don't need to know anything beyond that.
*  Right now, the next level after that, and this is again very vaguely speaking, it's not like there is a very strict hierarchy.
*  But the next level is to have some semantic understanding of what's going on or just to understand what are the relevant nouns, actions, stuff like that, or maybe which action is could be related to which object, etc.
*  Etc, etc. And, you know, if and I guess if you look at models of size, say around one billion, it's very, very good up to that level.
*  It almost always gives you a word that is grammatically correct and also has the I mean, this word is is kind of well related.
*  It works well with, you know, the previous few words that you saw, or it fits well with with the previous few words in the in the prompt.
*  But the next level after that is sometimes already requires, you know, first order logic or second order logic, etc.
*  So kind of breaking it down into like micro skills, you know, this is a ridiculous analogy, but I'm kind of thinking I follow this guy on TikTok who coaches basketball micro skills.
*  And it's amazing how many micro skills there are, you know, involved in being a good basketball player.
*  And, you know, most Lee the untrained I even among basketball fans like can't really enumerate them.
*  But this guy has enumerated them. And now he's teaching them, you know, one by very small one.
*  And so it's, you know, maybe similarly where you you wouldn't say like this person can like fully play basketball.
*  That probably doesn't even like make a lot of sense or sounds already sounds strange.
*  But you wouldn't say if there's any missing micro skill that they can't play basketball, you have some sort of continuum there.
*  That's like, you know, people can be better and worse at playing basketball.
*  People can certainly be better and worse at reasoning and language models, too, can be better and worse at reasoning.
*  And that probably seems to map on to some sort of hierarchy of micro skills that it either has or it doesn't have or it's like, you know, maybe in the process of grokking, you know, at any given point in training.
*  So that leads me to the other, you know, big, bold vocabulary word that I want to dig in on a little bit, which is emergence.
*  Again, tons of confusion, tons of different, you know, meanings out there.
*  I think some people mean like things that surprise us that we didn't necessarily predict.
*  Some people mean like things that happen suddenly.
*  I guess what I kind of think is like, it seems like there is some process where I always think back to the grokking paper and the Neil Nanda exploration of that, which I'm sure you guys are at least, you know, somewhat familiar with.
*  Where there is a phase change from initial memorization to a circuit, which, you know, what's so amazing about their work is they actually show this circuit in very like concrete terms.
*  And it's like, and this is the circuit that does this algorithm that allows it to generalize, you know, to the full set, you know, from just the sample data that it was originally trained on.
*  You know, I don't know that we have any circuits here that we can kind of elucidate, but does that feel right to you?
*  Do you feel like there's this sort of process of like memorization sort of being gradually replaced by like concrete circuits that solve particular micro skill challenges?
*  Is that your model of what's going on under the hood here?
*  OK, let's take a step back.
*  OK, like people talk about emergence.
*  I guess we can both agree that, you know, this is a very, it is not a well-defined notion at all.
*  You know, it's not like it's also it's not like you see a sudden phase transition from the model not being able to do something to you just slightly increase the size.
*  And then suddenly it has this it's really good at some capability.
*  You know, it's not like it didn't have it all before rather, you know, it's the vaguely defined term saying that there are some qualitative capabilities that, you know, the model at certain sizes has whether at smaller sizes, there's almost no trace of these capabilities at all.
*  Like, you know, GPT-2 did not know how to summarize text and suddenly it's GPT-3.
*  You have this summarization capability, but the notion is not well defined at all.
*  On the other hand, we do see that as we increase the size of the model, suddenly you have some certain capabilities you didn't have before.
*  And, you know, in a sense, I think a good analogy is if you compare dogs, monkeys and humans, right, you increase the size of the brain.
*  Suddenly, you know, humans can do math, whereas monkeys cannot.
*  So, you know, it's an ability that emerged when you made the neural network larger, not that I'm trying to imply at all that the same mechanism explains, you know, both things.
*  We have no idea about that. But, you know, what we say here is one of the most important abilities for generative models is to be able to speak coherent English.
*  Right. This is an ability that we see emerge also in much larger networks trained on, you know, those large language corpora.
*  And I think tiny stories basically gives you a much smaller data set where you can observe this emergence, you know, at much smaller scales of models in the sense that, you know, if the model is one million parameters, then it can hardly generate coherent stories.
*  And if you go to 10 million, then almost all stories will be coherent. Same with reasoning, like, you know, one to five million parameter model.
*  All of our reasoning prompts fail, whereas for 30 million, almost all of them succeed.
*  Now, as you said, all of this basically has to do with keeping coherence with the text.
*  So you have the emergency of the ability to generate the next word in a coherent way on different levels of difficulty.
*  So the easiest level of difficulty we could think of is just when you have something that follows from some easy grammatical rules.
*  And then, you know, you have you can think of like different levels of difficulty.
*  Sometimes you need to know a certain fact in order to be able to complete the next word, right?
*  Jack was hungry, so he went looking for some, to complete this, you have to know that, you know, to satisfy the desire for, like, to satisfy hunger, you need some food, right?
*  So sometimes you need to know a fact. So there's all those core capabilities that are necessary in order to keep consistency along the text.
*  And each one of them, we can actually witness its emergence as we increase the size of the model.
*  So what then is the theory of what is happening? I have a theory, but I want to hear yours on.
*  So you gave that example a minute ago, right? Girl wants either a cat or dog. Mom says no dog. So it's going to be a cat.
*  But GPT-2, you know, much bigger model, whatever, that's like 30 times bigger than your biggest in this in this research, right?
*  Like you're you kind of max out around 30 million parameters. GPT-2 is like what, 1.5 or something. So it's a lot bigger, 50 times bigger, maybe.
*  It still says dog, which is, you know, every we can all tell that's kind of obviously wrong.
*  You've got these much smaller models that can get that right. You know, in some way, there's this emergent, you know, observed phenomenon that.
*  It is able to get that, you know, exclusion concept. What do you think is happening there?
*  Is that a micro skill that is like, you know, this sort of exclusion, you know, that that's like a little piece of reasoning that is grok by the small model, but not by the big model.
*  I mean, it seems like there's you could be a really good stochastic parrot, but it feels like there's something there that has like truly kind of settled in to the structure of the network.
*  And maybe that didn't happen with GPT-2 because the data was just too noisy and it's kind of all over the place.
*  And so it wasn't able to learn those same things. How am I doing here? Does that does that resonate as likely true or even plausible?
*  Yeah, I think that's a valid conjecture. What we think is for GPT-2 because it trained on wipe data or just think of like repeat media.
*  We will try to minimize the language model laws. The consistency is like the least concern is more about just getting the knowledge correct.
*  I mean, you're talking about some object or some person and you want to know it's birthday or you want to know some specific aspect of that person.
*  I mean, this has nothing to do with natural language. It's more about just a sheer amount of knowledge that we encounter in the web data or something like Wikipedia.
*  So the model, I mean, because a model, I mean, I think both GPT-2 and our model, they are not large enough to minimize the laws to full extent like GPT-4.
*  So they have to select some part of the laws that they focus on.
*  And if the data has too many knowledges or too many other nuances, then the model may just focus on other aspects compared to consistency.
*  Well, here, our tiny story data really pinned down because the language is simple and the vocabulary is simple.
*  The really difficult part is consistency. And that is where the model focus to minimize the training laws.
*  And that's why I think our model, although it's much smaller, it gets better consistency compared to the larger ones.
*  Yeah, you can think about it as, you know, when you train a model on the entire pile on those large language corpora,
*  they have much more incentive to learn the preferred clothing styles of celebrities much before they learn how to complete this sentence with the dog and the cat.
*  You know, most of they definitely learned that, you know, Joe Biden is the president of the United States way, way before they learn how to reason.
*  This is a conjecture. Of course, I didn't actually test it, but I'm pretty sure that's what happens.
*  You know, you just overload the model with so many facts that appear in so many places.
*  Only once in many words that you generate this capability of reasoning becomes relevant.
*  So I think it's a really good exercise just to open a random Wikipedia article.
*  I did. It's one of my favorite activities since I started thinking about, you know, language language models and just go over the Wikipedia article.
*  Word by word and just think for every word, what core abilities do you need to use in order to guess what the next word is?
*  And what you'll see is, I think, definitely for a random Wikipedia article or a random example in the pile in some some web training model.
*  You will see that only once in every 20 to 30 words to predict the next word, you need to use some reasoning capabilities for one in every three or four words.
*  You need grammar for most words.
*  You can just kind of guess the next word using if I just tell you what the net what were the nouns and verbs that you need to use in order to predict the next word.
*  I'll tell you what the net what were the nouns and verbs that appeared in the previous sentences are without telling you anything about the context or, you know, things which are farther away in the text.
*  You will still be able to guess them in order.
*  So so the reasoning is is kind of a rare capability that you need.
*  It only becomes relevant, you know, pretty rarely.
*  And and therefore you will you will like the capacity of the model will be dedicated to other things much, much before you will get any reasoning capabilities.
*  That's also why we think of why we always kind of see there's an emergence behavior.
*  It's really because the reasoning or those like very rare consistency event.
*  They actually happen very rarely.
*  So even so only if you minimize the laws to a certain extent, you start to learn those rare events and your model feels like different.
*  For example, just a simple example, say Bob feels hungry, but he doesn't like sweet food.
*  So he went to eat.
*  I mean, if the model says when to eat some candy, then we think that this model knows nothing about what he's talking about.
*  But this is only just one word difference out of the 10 to 20 words.
*  And only if the model get to that extent, it starts to learn this consistency and we feel like the model start to know what it's talking about.
*  But in terms of laws, it's probably we only see like less than 10 percent difference.
*  I mean, if you turn into image classification, let me tell you, my model get like 90 percent correct and you have a model that gets 95.
*  I wouldn't consider this as an emergent capability that you get five more percent.
*  But for language model, this five more percent may actually be the emergent behavior.
*  And especially for math, like if I really want to solve a math problem, there's only like the connection between the two sentences where I need to make sure that my proofs are extremely coherent.
*  Well, most of the part, I'm just completing some formulas, write down the results.
*  But it's only this very tiny amount that defines that gives the model the emergence capability.
*  So I think the two things are connected that the models and learning reasoning is like a hard task that it only gets at the very end.
*  And also we see the emergence capability for if you grow the size of the model or if you grow the number of training data.
*  Yeah, maybe let me just expand on your example.
*  You know, so OK, we have this sentence.
*  Bob could have either candy or pizza.
*  Bob doesn't like sweet food.
*  So Bob got some.
*  And autocomplete.
*  OK, now the model usually if the previous sentence says something about sweet food, if we don't read the entire sentence, the most likely completion is actually candy, not pizza.
*  You have to read it in a pretty nuanced way in order to realize that Bob actually doesn't like sweet food.
*  Right. Sweet food and candy come together so many times in the training data.
*  Right. So the neural network has to, in quotation marks, choose between using Gopic's capacity in order to be able to resolve this nuance.
*  Or to use its capacity in order to know that Joe Biden is the president of the United States.
*  Right. You can't have everything together.
*  The model has a finite size and there is some theoretical limit to, you know, the amount of things the model can learn.
*  The model will definitely prefer to learn that Joe Biden is president and, you know, many, many other facts because they are relevant much, much more frequently.
*  The curriculum development space is likely to be a huge unlock over the not too distant future.
*  Right. I mean, you're kind of seems like you're probably just kind of scratching the surface here because we've got web scale data that, you know, is not built for this purpose.
*  Obviously, you know, where you're saying reasoning doesn't even it's not even required that often.
*  And so no wonder it kind of emerges late in the game that, you know, maybe pre-training on code, you know, is kind of changing that in some interesting ways.
*  But man, intentional design around what a gradual, you know, gradually like upstepping curriculum might look like, especially with the ability to, you know, to create the training data synthetically to, you know, really kind of isolate and bring those key skills forward.
*  It seems like you could rebalance training data and probably shrink it like a ton and get to a lot of the, you know, just by kind of shifting the balance, right, to get the these kind of emerging things to be more important relative to just kind of, you know, mind numbing repetition of, you know, who's the president or whatever.
*  It sounds like I mean, you're nodding that it sounds like you that aligns with your expectations too.
*  It's important when we design like a new version of the data, for example, to extend the degree of our thing to maybe elementary school or middle school.
*  I think it's very important to balance the amount of knowledge in the data versus the kind of our ability that we want the data set to teach the model.
*  For example, like if you go to elementary school, there's ability to do simple math or mathematical reasoning or some physics reasoning or do comparison of historical events.
*  I mean, those will take some capacity of the model. Maybe you took it. You took actually take a very big portion and the remaining ones.
*  I mean, if your data set has too many knowledges, then the model may just prefer to use this capability or use this capacity to actually memorize the knowledge instead of really learning those ability.
*  So we want to balance that there's some amount of knowledge that the model must have in order to basic basic stuff like math or basic physics reasoning.
*  But more importantly, there's there should be a lot of data that only emphasize on the ability side.
*  There's no new knowledge. It's just a bunch of math examples or a bunch of simple comparison of some basic historical events or some simple physical rules and their explanation or different varieties.
*  So that the model can actually focus on the ability part instead of just being screwed by the vast amount of knowledge.
*  So I think the right now the data, they don't really balance between knowledge and ability training.
*  So that's why training on them is not good for small model because they need to allocate their capability or capacity to just memorization.
*  So I think that's basically the criteria for maybe design like better version of synthetic data.
*  I guess we can just kind of maybe relevant notions here would be the breadth and the depth of the data set or the capabilities of the model.
*  So, you know, the the entire web is very, very broad.
*  It's also so by breadth, I mean, you know, it has a lot of facts.
*  The vocabulary is very large. You need to have a lot of knowledge to capture the data set.
*  And by depth, what I mean is, you know, it has first and second and third order logic that you can infer from learning this data set.
*  And this is not well established. I mean, there is no I don't think there is any research that that really established issues that there is a tradeoff between the two.
*  But, you know, it's very, very reasonable to assume that there should be a tradeoff between breadth and depth when you train the model.
*  Yeah, I think there's some optimal ratio because without the knowledge, you can't really do reasoning like you have to have some basic knowledge, like, say, candy sweet in order to do reasoning.
*  And when you go to elementary school, I mean, you have to know some basic events like some basic rules for math like one plus one is equal to two.
*  You order to do mathematical reasoning. So there's a balance. You cannot have no knowledge, but you cannot have all the knowledge.
*  So maybe there's some optimal ratio between like breadth and depth.
*  My head keeps coming back to this same kind of thing where, yeah, we could should see so much gain from kind of rebalancing the data set and maybe even, you know, starting with some more abstract things like I could see sort of A or B, not A, therefore, you know, and then do that with like just, you know, all the letters and then start to, you know, introduce kind of these associations and layer that on.
*  Like it sure seems like there is a lot of opportunity there.
*  Yeah, you're just mentioning the extreme case of only teaching reasoning because there everything is just symbols. There's no knowledge and it's all about just reasoning.
*  And maybe it's good to combine this with just something that is pure knowledge. And maybe we can get something good by just adjusting the ratio.
*  Yeah, maybe it's not clear at this point if, you know, a human being, you can when you teach a human being, you can kind of almost separate the knowledge and the reasoning.
*  Right. You can just say fact A, blah, blah, blah, fact B, blah, blah, blah. Now, here's how to reason.
*  I mean, it has to be a pretty smart human being. But in general, you know, we are able to take those two things and then combine them so that in the end we will have those core reasoning capabilities that we learned using, you know, exercises that only involve if not A, then if A, then B means not B, then not A.
*  Right. When we learned when we studied to the SATs, we have, you know, those rules and and and separately we have the knowledge of facts and we're able to combine them.
*  And I think it's an important question whether it's even feasible in in language models to just take those things, separate them into two different modules.
*  And, you know, will the model actually be able to combine those abilities? My conjecture, by the way, is no. Like, as long as as you don't kind of combine them enough in the data set, the model is not going to be able to infer the way that a human consciously infers the connection.
*  But if we could do that, then this would be, of course, like a very, very powerful technique to train models.
*  I just did another interview with a couple of guys from Mosaic ML, and they talked about training at times on like massive client data sets.
*  Even when they do that, they typically still mix in, you know, kind of the general pre-training pile or whatever, because otherwise they see catastrophic forgetting.
*  So they have to, you know, kind of keep some mix at all kind of stages of training to avoid that.
*  So I think that would be very consistent, I think, with what you said. Like you probably can't do it in strict phases.
*  There's got to be some sort of like mixing strategy throughout the process.
*  Right. And that's going to be very non-trivial to do. It might be feasible, but it's definitely not.
*  And it's not going to happen on its own, just because, you know, what the model cares about is just being able to efficiently autocomplete samples in the data set.
*  If the data set is either knowledge or reasoning, then it has zero incentive to combine.
*  And even if you give it a few examples where this is actually combined, no one is, you know, no one assures you that it'll actually be able to take those two modalities and really use them for the combination.
*  So I feel like this is a science that's really, I mean, we're only beginning to understand how these things work.
*  Hopefully, we'll figure out a way how to actually do it.
*  But I'm not sure you, Anju, maybe I don't know any concrete evidence of an example where this seems to work.
*  Right now, we like the kind of concrete evidence that curriculum learning really works, but we believe this should be helpful.
*  But I think overall, as Shona said, the model has no incentive to connect like the different phrases where you train things.
*  It just, I mean, when you start a new phase, it's just really minimized everything that related to this phase.
*  And it can't just forget everything that he has learned.
*  So it's definitely a very non-trivial task to get this curriculum learning work.
*  First, you just said a number of kind of interesting empirical observations, and you can address this kind of however you want.
*  But you noted that grammar emerges before consistency and creativity.
*  And consistency is kind of related there to reasoning in our purgatory telling earlier.
*  Is that the same thing that I've observed in my kids?
*  My memory, maybe I'm sleep deprived, but I feel like grammar maybe came last for them.
*  They definitely have a certain consistency.
*  They want what they want.
*  If they want ice cream, they keep the next token is ice cream, and they're pretty consistent on that.
*  And creativity, I don't know, that's a little trickier.
*  But does this feel like it echoes human development in your mind?
*  Like to me, I'm not sure if it feels that way.
*  I love this example.
*  So, yeah, I mean, I think the learning process for children is very, very different that way.
*  Right.
*  Children don't get like their incentive is not to say the correct next word.
*  Children, they want ice cream, their incentive.
*  The outcome needs to be I get ice cream.
*  So if they just say ice cream, ice cream, ice cream many, many times, maybe they don't get the best grade for creativity, but they will likely get the ice cream.
*  Right.
*  Depends on how basically on the self-discipline of parents and whether they are limited in this household.
*  Yeah.
*  I have a very close experience with with this exact scenario.
*  But, you know, like more seriously, like, you know, when when when children produce language, I mean, I'm only basing this on my observation.
*  They have constant contact with the physical world.
*  They know which entities are involved in the current conversation.
*  Right.
*  We are talking about a book that I just read.
*  So, you know, it's very unlikely that the next sentence will be about like a car because, you know, they have their in their heads this entity like, no, we're not talking about a car.
*  We're talking about this book.
*  Right.
*  Whereas the language model, you know, if it if it just makes one mistake in one word saying car instead of book, the loss that it incurs is actually not as big as the loss it would incur for incorrect, correct grammar, which becomes which is relevant in in almost every word it produces.
*  And not only that, you know, the language model, it's actually much cheaper.
*  It's much easier to have consistent grammar.
*  You only have to kind of be consistent inside the same sentence for the grammar to be correct.
*  You don't even have to look, you know, past five or six words back.
*  Whereas for children, you know, for every like children have a few entities which are kind of active in their working memory.
*  So this entity could be let's go.
*  It could be I want to go to the park and have some ice cream.
*  So the two and relevant entities are park and ice cream.
*  You're not going to replace those two entities in the middle of the conversation.
*  That's, you know, what the child cares about at this point.
*  So it's really like the incentive system is different, but also the whole kind of cognitive perception around that.
*  That's basically underlying.
*  The conversation is is pretty different.
*  Yeah, I don't know if it makes sense like that.
*  Maybe like a good way to think about it for a language model, definitely in its first phase of training, it doesn't need to look way back like three, four, five sentences before what it produces.
*  So I think a good example is to look at one of the GPT-2XL generations that we have in the paper.
*  So we have a story about like a snowman.
*  Two kids are building a snowman and a dog comes and destroys the snowman.
*  And then like you autocomplete to see what happens.
*  And maybe maybe I'll actually read it because I think it emphasize I think it emphasizes pretty well what I'm trying to say here.
*  So there's those two kids, Sarah and Ben, they built a snowman and a dog comes and destroys the snowman.
*  And now GPT-2XL completion looks something like that.
*  Sarah and Ben cry and look at the snowman in the snow.
*  Ben asks to do something.
*  Sarah tells him to go away.
*  Her hand tightens on the little red button.
*  The snowman is covered in fur.
*  It is red.
*  It is real hair.
*  It is a real snowman.
*  It looks just like the ones they used to make.
*  Ben has a big smile on his face.
*  He looks at the face he has made.
*  He walks over and kisses the eyes.
*  He's happy to be alive.
*  He has done what he was going to do.
*  He has saved the world.
*  So, okay, what am I actually trying to say here?
*  Except that GPT-2XL has a good sense of humor.
*  What I'm trying to say is almost every sentence here, all you need to do in order, all GPT-2XL does in order to generate it is look at the previous sentence.
*  And maybe it knows that there is one entity which is snowman, which is relevant here.
*  Other than that, there is no consistency at all in the completion that goes beyond, you know, looking at two consecutive sentences.
*  Language models are, if they're too small or in the beginning of training, what they do is they don't actually have enough incentive to know the whole context of what's going on.
*  Because to complete most words correctly, you just need to have, you know, the context of the current sentence and maybe the one before and maybe also one or two important entities.
*  Whereas for humans, this is completely different.
*  We have agency.
*  We know what we want when we form the next sentence.
*  And yeah, we care much less about grammar than about the ice cream.
*  Yeah, I would make an analogy like human child is learning with our RLHF algorithm, just doing reinforcement learning with the parents feedback.
*  And obviously the parents are very robust to grammar mistakes, so they don't really want to optimize that in order to maximize their work.
*  They'll probably care more about consistency, the topics, and they want to get the topic correct so they can get the reward.
*  Well, for language model is just next word prediction and the grammar is going to be penalized much more severely compared to the global consistency.
*  OK, yeah, I like that.
*  I'm always a little wary of analogies and I always want to come back and think what is sneaking into that analogy that I don't want to allow.
*  So I'll bookmark that one.
*  But I certainly the surface level intuition there makes a lot of sense.
*  And it's a it's a good it's a very clippable analogy as well.
*  Well, how about on the depth versus hidden dimension size of the which I often just call width the depth, you know, number of layers versus width of a layer.
*  You note some interesting trade offs there, and I didn't really have an intuition necessarily for why that would be.
*  But, you know, per the paper, you report that the fewer layer models will do better on grammar compared to consistency slash reasoning.
*  And from that, you know, it seems that more layers are important for this kind of reasoning consistency.
*  How should I think about that?
*  Like, is there a is there a story that crystallizes why that would be?
*  None of this is well established.
*  It's all our conjectures that like need to be studied much more.
*  But I think a good way to look at it is so.
*  So depth gives you tells you about how many times information can percolate between the tokens.
*  So every time you have a global attention layer, like a transformer attention, certain tokens, the information inside certain tokens can percolate into other tokens.
*  So, for example, if you have some instruction, create a story with this and these words, and I want the bad ending as well.
*  And then I type in the beginning of the story and it needs to autocomplete it.
*  These instructions can in every attention layer, they only have one chance of percolating into the tokens of the story.
*  And sometimes these instructions by themselves are nuanced.
*  So maybe there is an instruction saying the story has a bad ending.
*  It's not enough to know in order to complete the next word to know the current sentence and that the story needs to have a bad ending.
*  You also need to have like the context, like the wider context of what happens in the story.
*  So in order to fulfill these kind of instructions, you have to basically have the information percolate several times between the tokens.
*  And that's also the case for reasoning.
*  If you have first order logic.
*  So if we think about this example of cat and dog, like Alice wanted a cat or a dog or mother didn't let her have a dog.
*  So she got a cat.
*  How many times does the information have to percolate between the tokens here?
*  So first you want to understand that there was a cat and a dog involved.
*  That's one layer of global attention.
*  Then you want to know that she couldn't have a dog.
*  And you really want to you.
*  And so you have the set cat and dog and you want to do cat plus dog minus dog equals to cat.
*  So after you know that you have either cat or dog, you need the fact that, you know, she couldn't have a dog to percolate into my token.
*  In order to know that, you know, the only available option is cat.
*  So there are actually two layers of percolation here.
*  You need to know that it's not a dog.
*  So the token not has to go inside the token dog to know that, you know, dog is not allowed.
*  And then those two tokens not plus dog have to percolate into the generation in order to know that, OK, I had cat plus dog, but I have to do now minus dog to have a cat.
*  So it's just several.
*  So if you think about it as coding, you have several, you know, conditionals you have to do and several times that you need to have pointers to information that appears in other places in the text.
*  OK, this is very, very important.
*  I'm not trying to explain it in a very vague and non formal way, but I think, you know, it's a good initial intuition probably to what happens.
*  Because when we talk about facts, so if you have a completion, you know, I don't know that OK, like if I have a completion in a language model that's like the capital of France is, then all I have to do is I just need to have one kind of lookup table with, you know, all the countries and their capitals.
*  I don't have I don't need to have many layers of global attention.
*  It's enough to just, you know, take the two tokens capital and France, put them together and then just have one lookup table saying that capital plus France equals to Paris.
*  Now, here the dimension seems to play a much more important role because the bigger the dimension of the space is, the more entities I can kind of squeeze into this vector space.
*  And, you know, also the more neurons I have inside my lookup table to tell me, you know, that to have this list of all those possible facts.
*  So is another way to say that that within a single attention block, the attention relationships are not immediately transitive.
*  And so they need multiple iterations of attention in order to create that transitivity.
*  Like if the current token is looking back at a certain token, but then that token is looking back at a previous token, like we need two rounds of this to move the two hops.
*  Yeah, exactly. You just you first need the not to go into dog to know that it's not dog.
*  And then the not dog needs to go together into this, you know, set that has both cat and dog in it.
*  So that's already two leaps.
*  Does that also suggest then that sort of for as many kind of logical leaps as you might need, you need like maybe that many layers?
*  Like you can't you're sort of bounded by if you if you have two layers, you can make maybe two logical leaps.
*  Is that a general heuristic that seems sensible?
*  I think there's a depth and we spread off.
*  For example, you can simulate two layer leaps just using one layer, but you have to enumerate like all the two possible combinations, which makes your size go from like say N to N square.
*  So if you want to be kind of the most size efficient, then you definitely have to go as deep as a number of like logical loops.
*  But if you are not that deep, then you can actually use a wider network to concatenate the two steps into one and just make the intermediate layer like much bigger.
*  So so here also, I mean, your question kind of bursts into an open door in the sense that the paper we wrote at Microsoft Research about this synthetic reasoning task we call Lego, that's exactly a task where you have multiple leaps of reasoning.
*  And we see a very direct connection between the number of layers that you need and the number of reasoning steps required to complete the task.
*  But maybe somewhat surprisingly, we see that the model finds like very interesting and sophisticated ways.
*  This is actually not in the paper.
*  This is kind of like a follow up work.
*  It finds like very sophisticated ways to do multiple leaps of reasoning within a single layer.
*  So so definitely more layers help, but it's not like it's strict upper bound for the number of leaps you can you can do.
*  I can only wish it could be quite that simple.
*  But that's really, really interesting information.
*  I'm learning a lot from this.
*  The interpretability part of this paper is also really interesting.
*  You kind of break it down into the attention portion and then obviously the you know the MLP neurons portion.
*  And a couple things jumped out at me.
*  One was in the attention portion.
*  You seem to observe that there's kind of two sorts of attention heads.
*  One really just focuses on the distance relationship between the tokens and then the other is more semantic.
*  And the distance one, I was like, holy moly, does that look like the alibi scheme that has recently come to popularity with these super long context windows?
*  So I don't know if you guys have had a chance to study that, but quite an uncanny resemblance, right?
*  I mean, you're showing all these attention heads where it's like this one is just a very tight attention range.
*  And then, you know, there's different kind of lengths.
*  And that's almost exactly what they cook up as the kind of substitute for positional embeddings in the alibi research, at least as far as I understand it.
*  Do you see that same parallel?
*  Yeah, I think they are definitely doing the same thing, which could explain why alibi is very, I mean,
*  it's very helpful because the positional embedding in the alibi is already initialized to do this multi-scale distance based attention.
*  Well, for absolute positional encoding, like what we use here, the model has to learn to discover this optimal kind of positional based attention.
*  So just hard code that positional based or distance based attention, I think is a really good choice based on our observation.
*  And also we can talk like the shorter ones are really responsible to just learn the grammars and the longer ones, they may just make sure that your content are consistent globally or maybe just to grab the associate words.
*  For example, you have Alice in one sentence and then you have Alice like five sentences ago.
*  You want to make sure that these two words, you have a chance to put them together.
*  So, so yeah, let me just point out that, you know, clearly to complete the next word, you you need two things.
*  Usually you you want to know what the proximate words are, what are the most kind of recent words you saw, and you want to know what are the most important entities in the story are.
*  So these are going to be, you know, words with the relevant semantic meaning to what you want to complete.
*  Now, if I remember correctly, what happens in Alibi is you there is kind of a little bit of a mix of both of them.
*  So you just take every attention head and you make it decay for every attention had you just prescribe some scale and the strength of attention decays with the distance inside the text.
*  Is that is that correct? If I'm not mistaken, that's that's what happens there.
*  And we actually see, I mean, one surprising aspect is we actually see a dichotomy.
*  There are heads that only care about distance and other heads that only care about semantics.
*  And there is hardly a mix between the two.
*  But we have to say that this is only for one attention block.
*  We haven't really checked for multiple attention layers, what the transformer will do together.
*  But just for if you just train a network with one attention block, it seems that the network learns to separate the distance based attention versus the semantic based attention.
*  Where some heads are just looking at tokens based on its distance, some other heads are just looking at tokens based on the semantic similarity.
*  So is there anything else that you can say? I mean, that's pretty profound in and of itself that that dichotomy emerges because you didn't initialize it.
*  I mean, in Alibi, they've engineered it that way through some probably trial and error and heuristics and guesses and whatever.
*  But this is totally just happening on its own.
*  Is there anything else we can say about what you see in the semantic one?
*  Any semantic one? When I looked at those, I didn't know light bulbs went off in my head to kind of interpret those visualizations of the semantic blocks.
*  But anything you would highlight from studying those?
*  I think the most interesting one we see is just a semantical attention to the main character names.
*  So, for example, like there's some head where every token just tend to like the Tom and Lucy, which are the two main characters.
*  I think this is pretty important. I mean, it's just try to identify like what are the person that are involved in the story.
*  So the next time we generate a new thing, it's not going to say like bulb, it's going to say something consistent.
*  So I think the semantic has at least what we see in the one transformer block is more about this type of attention, where it identifies like what are the main objects in the sentence
*  and just try to make sure that most of the tokens or the relevant tokens attend to those objects.
*  Like when you have the or you will attend to like banana.
*  So you know that you want to complete the next word as a banana instead of something completely made up.
*  So I think those semantical attention has they are really useful to just be consistent English inside the transformers.
*  Yeah, but let me add that, you know, it's very natural to if to complete the next word.
*  You want to know what are the relevant characters, what are the relevant entities in the story.
*  But no one expects a priori that you will have such clean attention heads and attention that exactly attends to the character and a different attention had that exactly,
*  you know, attends to, you know, the objects in the example we gave.
*  It's like a banana and park a priori.
*  We might expect that it will all be just a big mess.
*  Right. Every attention adds, attends to a little bit of everything.
*  And, you know, why would it be interpretable at all?
*  But it's quite surprising with that when the model is small enough, it seems that we can actually give meaning to both attention heads and neurons.
*  So is that does that kind of fall apart if we add a second layer like does then it just become more messy again?
*  Or what is that? You know, as you start to stack layers, what does that start to look like?
*  Yeah, I think when your transformers are getting higher or getting deeper or getting larger, it definitely becomes more messy because the transformer can simulate like,
*  I mean, if the transformer is small, it really needs to learn those separate modules in order to minimize the loss.
*  But if the transformer has a larger degree of freedom, it has a luxury to, for example, use five attention heads to simulate one or use three layers to do what could be done in one layer.
*  It has no incentive to be like as precise or as kind of conservative as the smaller ones.
*  So it's actually less interpretable. And we also observe that in when we try to interpret the neurons as well.
*  Perfect bridge then to talk a little bit about the neurons.
*  Maybe just give us a little bit of understanding of like the technique that you used to, you know, I'll try to summarize it real quick.
*  You tell me where I'm wrong. You run a ton of stories through and you look for what tokens specifically are maximizing the activation of a certain neuron.
*  And then you can kind of print out like here are the snippets and the individual tokens that maximize the activation for this particular neuron.
*  And then, holy moly, like it really looks like there's a pretty coherent concept, you know, as you just kind of scan down that list of things that, you know, corresponded to high activation on any given neuron.
*  That's pretty accurate. So you have this these middle layers in the MLP, which we can think about as neurons.
*  Those are really the coordinates that can either be activated or not.
*  You have the only basically nonlinearity in there.
*  And yeah, like again, just like that attention heads a priori, it's not clear at all that they would have any meaning.
*  Those are just, you know, different coordinates of a certain vector space.
*  Like no one promises you that, you know, the neural network is going to use one particular coordinate for one particular kind of task.
*  And indeed, so maybe let me mention that this basically follows an idea suggested in a 2015 paper by Lee et al called Visualizing and Understanding Neural Models in MLP, which is like their idea is just to look at the tokens which induce the highest activations for the neural network.
*  And when we look at larger models like GPT-2 XL, what we and we try to look at those tokens, at least the highest activation for the neural network,
*  we try to look at the tokens that are the highest activation for the neural network.
*  And when we look at larger models like GPT-2 XL, what we and we try to look at those tokens, at least the two of us could not find any common meaning.
*  You know, the same neuron is activated sometimes on nouns, sometimes on verbs, sometimes on like there's just no clear pattern whatsoever.
*  Whereas when we take a small model, for example, there is one particular neuron that seems to always be activated when the main character of the story is introduced.
*  And, you know, that kind of makes a lot of sense if you think about what the neural network's network needs to do, I guess, like if there was a programmer writing code that tries to autocomplete, you know, stories,
*  there would probably be a function that tries to locate the name of the main character because it's useful in many, many places when you autocomplete.
*  In fact, you know, whenever you know that the name of some character should appear, it's a pretty good guess to think that, you know, this is going to be the main character.
*  Right. So you have a neuron exactly doing that, and we haven't checked enough to be sure.
*  But there's probably an attention head that then attends to, you know, what this neuron outputs whenever you know that the name of some character should appear.
*  And when you connect those two together, what you will get is, you know, this mechanism that is able to copy the main character's name to different places along the generation.
*  So, you know, this is a very basic mechanism that you can actually observe inside the neural network.
*  And this doesn't happen in bigger models, at least not in a way that is, you know, so easy to trace.
*  I guess my the simple version of it was I thought maybe it was just like maybe there are sort of a bunch of concepts that are easy to identify.
*  Where you can just see like, OK, at a glance, I know what that is.
*  And maybe there's just only so many, you know, like maybe we only have so when you have 30 million neurons, you know, our 30 million parameters, you have however many neurons, you know, maybe that's kind of enough.
*  And you can kind of capture those. And then you go 50 X and it's like, well, if you start fishing at random points in the network there, maybe you just miss a lot of those.
*  You know, they may exist, but they're just kind of hard to spot because maybe they're sort of sparse, if you will.
*  And then the things that are in between, I mean, I'm really getting out on a limb here, but I was kind of thinking maybe those are sort of analogous a little bit to like the subconscious processing that goes on in our brains where I kind of know on some level that like processing is happening.
*  Even for many concepts, you know that I don't have like a clear label for, it's just, you know, there's some sort of churn happening in the brain.
*  But then, like only a certain, you know, small set of that kind of rises up to this level of like, you know, what I've called it a conscious concept that I can sort of say, like, I have a label for that.
*  And it's like a tidy enough thing.
*  So I guess the two ideas there are maybe they're just a lot more easy to find in the small network because, you know, you have to have them and, you know, they get packed densely versus a big network.
*  You know, maybe they just are packed more loosely.
*  And then those other networks or those other, you know, neurons maybe are just kind of analogous to some stuff that we don't understand very well in our own cognition.
*  Yeah, it's definitely possible.
*  I think that's an advantage of small language models.
*  So maybe more interpretable compared to larger ones because the smaller models can only do basic stuff and only the basic stuff are probably interpretable.
*  Like the very complicated stuff, for example, how GVD-4 like write a code that are 1,000 lines.
*  I mean, those things is almost impossible to interpret.
*  But how could a small language model keeps the main character consistent?
*  In those basic questions, we can probably understand that there are probably some neurons associated with that.
*  And in GVD-4, like out of the, I don't know, maybe 10,000 neurons or even more neurons, there may also be some neurons that are dedicated to keep the main character consistent.
*  But it's just so hard to find it because it may be in the like 25th layer neuron, like 9,700, whatever.
*  It's just so hard to locate.
*  Well, for smaller models, because it's so small, every neuron must be doing some basic stuff.
*  Because the complicated one, as we said, in the consistency hierarchy or in the loss hierarchy, they only consist of very tiny fraction of the loss.
*  So the main fraction of the loss that contribute to like basic consistency, grammar and things, those are probably the things that are learned by the neurons in the smaller models.
*  And they are more kind of basic and more interpretable.
*  So, you know, there is there's many ways for the neural network to solve a problem.
*  Like given a problem and an architecture of the neural network, there are many different configurations of the weights that would solve the same problem.
*  Some configurations might be more interpretable to a human.
*  And some are just, you know, one big mess.
*  Like every new neuron is little is doing a little something of every possible task.
*  And, you know, they are combined in very, very complicated ways.
*  And then the network has no incentive in the loss function not to be a one big mess.
*  Like most solutions to the same problem are one big mess.
*  You know, this is where the entropy is located.
*  Right. And when the model is small, it kind of has no choice.
*  The neurons have no choice but to align with meaningful tasks because, you know, the neurons are where you have the nonlinearities and you just don't have enough of them for the one big mess type of solution.
*  Somehow the most efficient solution is the one that is not completely messy.
*  And if you have a large network, then, you know, it'll just kind of find a way to do it that does not align with the coordinate structure of the of the neurons.
*  Whereas when the model is small, you just have no choice.
*  So interpretability appears as a kind of a side effect.
*  So anything else that we didn't cover?
*  Yeah. So one thing maybe going to the initial motivation in creating the data set, which is, you know, to have like some basically said like a small data set, which is a testing ground for ideas in LLMs.
*  Like an open question here is, do we even have a reason to expect that behaviors we witness in this compact setting will translate to LLMs?
*  Right. We don't know the answer to that.
*  Like, suppose we find an architecture that works much better for the tiny stories data set.
*  Do we actually have a reason to expect that, you know, this architecture will also be better for LLMs?
*  Right. So I'm just saying this as a question.
*  I think it's one of the most relevant questions that, you know, stem from from this paper.
*  And, you know, it kind of connects to a more general question, which is, you know, there is all those papers like the Google chinchilla paper and the OpenAI scaling gloss paper, which try to suggest that there might be universal phenomena in LLMs.
*  There is some, for example, a trade off between width and depth that is perhaps I'm not they don't suggest it explicitly.
*  But there it but, you know, a natural question that arises is this universal in the sense that it does not depend on, you know, the exact mix you take in the data set and the exact architecture and the exact range of sizes you take.
*  So the question here is, are there universal phenomena which will be common to the tiny stories data set and to LLMs being trained on these large corpora?
*  And, yeah, I mean, we maybe let me just say we have just a few indications of some sorts of universality.
*  But at this point, it's completely open.
*  And, you know, we really hope for the sake of, you know, saving energy and also having, you know, just opening the door for Ph.D.
*  students to actually do LLM research.
*  We hope there is some universality going on so that, you know, you could gain insights, not necessarily on tiny stories, but on any small data set, which would actually be of relevance to LLMs.
*  Yeah, our future work is mainly just planning to extend the capability of tiny story.
*  If you can create a story that captures elementary school knowledge, I think this is already a pretty, I mean, it's already a really good data set.
*  If you train a language model, for example, less than one billion, maybe 300 million parameter, and it's just good at everything for elementary school or maybe even third grade of elementary school.
*  I think that's already a very good model.
*  I think people will love to interact with it.
*  It knows how to talk, it knows the basic knowledges.
*  And maybe it will, I mean, the data set would be diverse enough to capture everything in real language, capture every aspect of real language, but just at like a downscale level.
*  And once we have that data set, I think it really opens the door for everyone to do natural language research.
*  Not the ones that has like 100, 800 in their hands, but the ones with just a laptop GPU, they can train the model in like more two days and they can gain some interesting observation.
*  I think what we witnessed in LLMs is kind of a mathematical miracle going on.
*  And what do I mean by that?
*  You know, you take this algorithm, which is pretty simple.
*  It's you know, it's gradient descent plus plus.
*  I don't want to belittle, you know, all the basically really smart technical contributions that are inside that algorithm.
*  But all in all, you know, it's basically gradient descent with an architecture that's very clever, but still it's quite simple.
*  And the miracle is you take, you know, all this huge training corpus, you fit it to the algorithm and you don't just get a network that is memorized some text.
*  You get a network that can actually genuinely, you know, create like synthesize new content, show signs of reasoning, understanding and so on.
*  And we think Tiny Stories is just kind of a compact example where you observe the same type of miracle.
*  Of course, it's not as it's not nearly as exciting of what happens in LLMs, but already there at this size, you see that there is, you know, some very interesting generalization and emergence going on.
*  And, you know, even if, you know, it doesn't give us a lot of insights about large language models, this is still kind of a nice playground to try to develop maybe the mathematical foundations necessary to understand why neural networks are able to generalize so well.
*  So maybe then just one final question, you know, and I'll encourage people to get in there and try it out. What other interpretability type work have you guys seen that has inspired you that you would recommend that folks in the audience go take a look at as well?
*  Yeah, I think one of the works that inspired our research, I mean, it's the work from our group previously, which is called Lego.
*  It's a synthetic reasoning task, which tries to understand what the model is. I mean, try to understand what the attention mechanism of the model is.
*  So, I think this work is, I mean, pretty inspiring and it tells us a lot about the
*  different types of attention that the model has.
*  So, I think one of the things that we've done is we've identified a lot of different types of attention that the model has.
*  And we've identified a lot of different types of attention that the model has.
*  And we've identified a lot of different types of attention that the model has.
*  And we've identified a lot of different types of attention that the model has.
*  And we've identified a lot of different types of attention that the model has.
*  And we've identified a lot of different types of attention that the model has.
*  And we've identified a lot of different types of attention that the model has.
*  And we've identified a lot of different types of attention that the model has.
*  And we've identified a lot of different types of attention that the model has.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  So, I think this work is, I mean, pretty inspiring and it tells us, like, Transformer is at least doing something that is reasonable instead of a pure math.
*  I think we are still, you know, we're light years away of being able to actually understand what's going on inside the, like, the model.
*  I think we are still, you know, we're light years away of being able to actually understand what's going on inside the, like, the model.
*  I think we are still, you know, we're light years away of being able to actually understand what's going on inside the, like, the model.
*  I think we are still, you know, we're light years away of being able to actually understand what's going on inside the, like, the model.
*  I think we are still, you know, we're light years away of being able to actually understand what's going on inside the, like, the model.
*  I think we are still, you know, we're light years away of being able to actually understand what's going on inside the, like, the model.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, the solution that gradient descent finds to the problem is not a very, very messy and not interpretable solution.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I mean, we have a very limited understanding of how the human brain works.
*  I think it's impossible to look inside the neural networks and just pin down.
*  I think it's impossible to look inside the neural networks and just pin down.
*  I think it's impossible to look inside the neural networks and just pin down.
*  I think it's impossible to look inside the neural networks and just pin down.
*  I think it's impossible to look inside the neural networks and just pin down.
*  I think it's impossible to look inside the neural networks and just pin down.
*  I think it's impossible to look inside the neural networks and just pin down.
*  I think it's impossible to look inside the neural networks and just pin down.
*  I think it's impossible to look inside the neural networks and just pin down.
*  I think it's impossible to look inside the neural networks and just pin down.
*  I think it's impossible to look inside the neural networks and just pin down.
*  I think it's impossible to look inside the neural networks and just pin down.
*  Maybe we have to do an approach more like our sparks of AGI paper, where we just talk to the model.
*  Maybe we have to do an approach more like our sparks of AGI paper, where we just talk to the model.
*  Maybe we have to do an approach more like our sparks of AGI paper, where we just talk to the model.
*  It's more about interpreting other humans' intentions.
*  It's more about interpreting other humans' intentions.
*  When we talk to them and we throw a sequence of conversations, maybe we can understand what the model likes to do and what the model doesn't like to do, or what the model is good at, or what's the typical case of the model's failure.
*  When we talk to them and we throw a sequence of conversations, maybe we can understand what the model likes to do and what the model doesn't like to do, or what the model is good at, or what's the typical case of the model's failure.
*  We can understand what the model likes to do and what the model doesn't like to do, or what the model is good at, or what's the typical case of the model's failure.
*  And it's more towards psychology study, but really for robotics, that maybe we need to take that approach for interpretability.
*  And it's more towards psychology study, but really for robotics, that maybe we need to take that approach for interpretability.
*  You know humanity has taken advantage of horseback riding for quite a long time.
*  back riding for quite a long time.
*  Now we have no idea what every neuron
*  inside the horse's brain is doing.
*  We can't really interpret how we give some,
*  I don't know how to call it, like command to the horse,
*  like physical cue, and the horse obeys,
*  and it's very, very, very useful.
*  And we can actually rely on,
*  like horseback riding is very reliable.
*  There are very few cases where the horse has acted
*  unexpectedly in a way that caused accidents.
*  Like humanity has profited from that vastly,
*  maybe leaving animal rights aside here.
*  And it works perfectly even without interpretability.
*  And we just figured out ways to align the behavior
*  of the horse with our needs by taming the horse.
*  We can tame it without understanding the exact process
*  that's going on there.
*  And this is a big success.
*  And I think it's just a good analogy.
*  I mean, it's kind of horseback riding for the brain,
*  those LLMs, right?
*  They are just, they give us, suddenly we can go much faster
*  to much longer distances,
*  even if we don't exactly understand what the horse is doing.
*  Like definitely the Mongols didn't understand much
*  about the biology of the horse.
*  They could still use the horse like in a very reliable way.
*  So, I just think this is, even though I'm pessimistic
*  about actually understanding the inner workings
*  of the neural network, I'm very optimistic
*  about the usefulness and the fact that,
*  we will be able to align it efficiently.
*  Ronan Elden and Yuanjuli,
*  thank you for being part of the Cogrev Revolution.
*  Thank you very much.
*  Yeah, thank you for the invitation.
*  It's really my great pleasure.
*  Omnike uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it,
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  Thank you.
