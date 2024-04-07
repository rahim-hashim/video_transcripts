---
Date Generated: April 05, 2024
Transcription Model: whisper medium 20231117
Length: 4989s
Video Keywords: []
Video Views: 643
Video Rating: None
---

# Unbounded AI-Assisted Research with Elicit Founders Andreas Stuhlmüller and Jungwon Byun
**Cognitive Revolution "How AI Changes Everything":** [April 03, 2024](https://www.youtube.com/watch?v=sv1E5LX1JvY)
*  We have big visions of transforming research and there might not be a lot of time left before we really need to make it useful for very high stakes decisions and times of chaos.
*  People probably still are making the obvious mistake of being a K model, say yes or no and then justify your answer.
*  And that's obviously terrible because then it has to answer without any reasoning and will just lock itself into a potentially wrong avenue.
*  This is where the task decomposition comes into play because it's much easier to iterate on and ship a new predefined column for statistical technique use than it is to ship a new model that's been fine tuned on all those scientific papers and evaluate that for quality.
*  So again, breaking down things into small tasks helps with launches as well.
*  The key question is how do we as a society want to turn compute into more work?
*  And one answer is we're going to train larger and larger models and we'll hope for the best.
*  Maybe we'll augment it a little bit with better interpretability methods.
*  We are working towards a different answer, which is we think like more compute will in fact lead to great things and more correct answers, etc.
*  But we can get there through more transparent architectures if we can build the right infrastructure.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers, entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today, I'm excited to present a conversation with Andreas Stollmacher and Junghwan Byun, co-founders of Elicit, a company that helps social and natural scientists analyze research papers at superhuman speed.
*  And in which I am a small dollar, but very proud investor.
*  Andreas and Junghwan bring deep expertise and a highly principled approach to the challenge of getting large language models to reliably answer complex research questions.
*  Their product allows users to systematically search large bodies of literature, extract key information into well structured tables and iteratively refine queries to zero in on the most relevant sources.
*  All while maintaining a transparent log of each step for easy auditing, reproducibility, extensibility and team collaboration.
*  As the AI research assistance base has become increasingly crowded, Elicit stands out for its meticulous approach to task decomposition.
*  That is the art, which they are very much developing into a science of breaking big questions down into smaller, more manageable subtasks that language models can reliably execute.
*  This allows the product to provide real value to serious researchers who really need to be able to trust the results.
*  We cover a lot of ground in this conversation, starting with the company's founding vision of using AI to enable knowledge sharing at an unprecedented scale.
*  Andreas and Junghwan explain how they've approached key challenges like minimizing hallucinations, maximizing accuracy and expanding the scope of analysis.
*  And we dig into the tech stack that makes this possible, including their approaches to retrieval, extraction, summarization, synthesis and most importantly of all, evaluation.
*  Finally, we touch on the company's evolution from nonprofit research lab to mission driven commercial startup, their plans to enable more scalable, compute intensive workloads in the future and what sorts of talent they are looking to hire today.
*  By focusing on researchers who are working on hard, sometimes literally life and death problems, Elicit has no choice but to treat reliability as a top priority.
*  And their approach, honed over several years of R&D, is a model for anyone who's looking to build high stakes applications with large language models today.
*  I was obviously a big fan of the company coming in, but I came away from this conversation even more convinced that Andreas, Junghwan and the team are up to this important challenge.
*  As always, if you find value in this work, please share the episode with your friends.
*  This one would be great for anyone who's struggling to keep up with an exploding body of research literature, whether that's in machine learning as it is for me, biology or something else.
*  And please also take a moment to share any feedback or topic suggestions that you have via our website, cognitiverevolution.ai or by messaging me on the social media network of your choice.
*  Now, please enjoy this deep dive into Elicit's program for scalable, trustworthy, AI assisted research with co-founders Andreas Stuhlmuller and Junghwan Byun.
*  Junghwan Byun and Andreas Stuhlmuller of Elicit, welcome back to the Cognitive Revolution.
*  It's great to be back.
*  Guys, it has been an incredible year in the AI space overall, obviously with an unbelievable amount happening.
*  I can't believe that it's been about that long since our first conversation.
*  And a lot has happened for you guys as well with a bunch of product launches that you've brought forward in rapid succession, a fundraise.
*  And right now the latest hotness from Elicit is notebooks.
*  Folks will know, by the way, I've mentioned Elicit in a couple of episodes, I think recently as one of my half a dozen go to information surfacing tools.
*  And specifically for more structured literature reviews, this is my go to tool.
*  I should also disclaim a little bit because this is not something I have to do often, but I am a super small time investor in Elicit, which is something I say with great pride.
*  So let's start off by just telling people what's new and you guys can run through the new release of notebooks.
*  Yes, I was just going to say for people who don't know, Elicit is an AI research assistant.
*  Our vision is to apply AI to helping the world navigate complex reasoning and to really scale high quality reasoning.
*  We want to help researchers unlock breakthroughs in every domain, everything from climate change to chronic fatigue and institutional decision making.
*  And as you've noted in the past year since we've last been on, the product has just grown tremendously.
*  We've gotten to a million in ARR in just four months after launching subscriptions.
*  We spun Elicit out into its own venture, raised a $9 million seed round and are now, I've really been spending the last few months thinking about how we continue to support people who are doing really complex, large scale reasoning.
*  People who are really pushing the frontiers of their domains forward.
*  And notebooks, which should be out by the time that we release this podcast is something that we've been working on actually for years.
*  This is actually our fourth time trying to make this division work.
*  It's very core to what we think about with Elicit and the kind of product we want to be.
*  So I think it's maybe helpful to start with what is the vision for Elicit really?
*  What are the problems we're trying to solve?
*  And how does this latest feature, it's really, it's much more than a feature launch.
*  It's a re-imagining of the product.
*  And how does this latest release manifest that?
*  And I would say for us, really, I think there are two main challenges that we see in research today.
*  One is that there's just an overwhelming amount of information.
*  There's just a superhuman amount of information.
*  There's no researcher that can possibly stay on top of it all.
*  Publications in most domains are growing exponentially.
*  A researcher can barely stay on top of what's being published this year, not to mention all of the historical context that's obviously accumulating over time.
*  I think researchers feel like they're just drowning in papers and they can never be as rigorous as they want to be.
*  So it's like definitely one, that's definitely one challenge with research where I think it seems pretty obvious how language models can help with that problem.
*  The other challenge we've seen in research is just that a lot of the processes are ad hoc.
*  So it's like very common to, I'm sure you've had this experience too.
*  It's like very common to look at someone and they just have an explosion of tabs.
*  They start with Google or Google Scholar.
*  They find this paper and that paper and this paper and they're down this rabbit hole like eight hours later.
*  They're like, how did I end up here?
*  What was I even researching?
*  And there are certainly very systematic processes are in research, but I think a lot of times the journey there's people talk a lot about serendipity.
*  When we talk to researchers at like multinational industry research labs that have offices across continents and thousands of people working, when they try to figure out what kind of relevant work has been done in their own company, a lot of it is I talk to someone.
*  And fortunately that someone happened to know someone and that person happened to be here like 10 years ago when we worked on this thing.
*  And I think that's just like really not a scalable or optimal process.
*  And so with the illicit and I think with AI, we can really start to reimagine what this, what research can look like with these tools and what were processes you want to bring over and what we really want to transform.
*  And we really want to make research.
*  We talk about making research systematic, transparent and unbounded.
*  Those are the three things that we want to manifest in our product.
*  And so notebooks is the way by which we make that possible.
*  So systematic is like taking these processes that are ad hoc, these like maybe one tab at a time research journeys, and instead helping researchers have much more meta cognition, put them more in the seat of thinking about what makes for a good paper, what makes for a relevant result, what makes for high quality research.
*  What does success look like for me in this moment?
*  And for this research project, let me be explicit about those criteria and then apply them over as many inputs, as many papers as can as exist, not gated on my own time or reading potential, but really on all of the kind of relevant data out there.
*  With AI, people are increasingly going to be put in the position of having to evaluate and be really explicit and mindful of what success looks like before then using AI tools to manifest that.
*  So that's like systematic is what we're going for.
*  We care a lot about making research transparent.
*  This has been really important to us since day one.
*  It's really important with language models showing we've published research in the past on supervising kind of process, not just outcomes.
*  And notebooks really accomplishes that as well.
*  So it kind of it like it allows you to basically take additional steps and it logs all of your steps as you go on this much more extensive journey.
*  So you can see what papers did I start with?
*  What factors did I consider?
*  What papers did I screen out?
*  What other queries did I run?
*  What papers did those results result in?
*  And then over time, you can see how did I end up at this final output?
*  And there's just kind of by default log that you can audit that you can share with somebody else.
*  So it's going to help with that transparency process of component.
*  And then I think the biggest part that notebooks will push on that hasn't that we haven't had before is this idea of unboundedness.
*  So I think another challenge with research today is people do a ton of work.
*  And then the final kind of artifact is this PDF, which is obviously very static and basically like immediately updated as soon as it's published.
*  And you can't reproduce it.
*  You can't extend it.
*  You can't like slightly tweak someone's analysis.
*  And with notebooks, we really want to try and make research much more like unbounded in that sense.
*  So you can keep taking additional steps and keep doing data analysis over all the information and papers.
*  Basically, you can follow up with additional queries, summarize more papers, extract more data.
*  And often research, there's a way we can systematize research processes, which we really want to do.
*  But there's definitely a component of research, which is fundamentally iterative and uncertain.
*  Often, if you're in a more exploratory state, you don't always know where you're going to end up.
*  And so notebooks accommodates both of those workflows.
*  Cool. Let me just give my kind of experiential overview of what it's like to use the list that you can expand on that.
*  And of course, you guys have plenty of demos and materials as well.
*  But the way I think about it is, first of all, it is, as you've said, like very structured.
*  Right. So it's first to ask a question.
*  That's the initial prompt is ask a research question.
*  Then there are, I guess I think of it as two main functions, one being like identifying the papers that it should show me in the first place.
*  And that kind of creates like my little sandbox that I can now play in.
*  And then there's the like highly structured addition of columns to the tabular form in which the papers are presented, where I can bring all these sort of
*  incremental auxiliary analyses to bear on all the papers.
*  So there's like a ton of these that are preset where you can say, what's the population size or was there, was the null hypothesis rejected or not?
*  And all these kinds of very standard things that you've already cooked up.
*  So I can just go click a button, add a column, and then boom, the, in the background, the language model is, you can tell us a little bit more about exactly how it's working under the hood in a minute.
*  But digging into each of these papers, asking these very specific questions in these kinds of bite-sized ways, filling out this table.
*  I personally love the ability to also set up my own and just ask what I did the other day was in researching curriculum learning.
*  I just said, what is the largest model used in this paper?
*  And, you know, just boom, boom, boom.
*  Okay.
*  Pythia 6B, whatever, whatever, whatever.
*  So now I can say, and this is where I think mostly that functionality has been there.
*  And now with notebooks, I can start to say, okay, I am really only interested in ones that have like pretty big models because of the
*  belief that like they're going to behave qualitatively differently.
*  So I'll look at that column, check the ones that have sufficiently large model size.
*  Now pull that down into another table.
*  And now I can start to do more deep dive analysis on just that select group.
*  Then I can also ask additional questions, bring up more papers, consolidate those into lists.
*  And I hadn't really thought too much about, because I'm relatively new to the notebook.
*  I've got early preview access, but I'm still relatively new to it.
*  I haven't really thought as much about the sort of implicit log that creates the journey that is embodied in that history.
*  But I actually, as you described that also thought, yeah, that's probably quite valuable to be able to go back and look at my
*  train of thought.
*  Cause Lord knows I can't remember what I was thinking half the time.
*  And also just to audit myself, to make sure that I, that I was approaching things in a sensible way.
*  So yeah, that's cool.
*  What would you add to that?
*  Yeah.
*  Now let's say at the end of all this work, you want to publish a new blog post or like someone wants to update this kind of and compute
*  essay that was published a long time ago.
*  Ideally this notebook can serve as this log of how did, how did you figure out which models were relevant?
*  What dimensions did you look at?
*  What papers, what criteria?
*  And then if someone wants to build on that, they're like, actually, I also want to look at smaller models or I want to look at
*  models trained on this specific architecture.
*  It's much easier for them to pick up where you left off.
*  They don't have to start all the way from scratch finding the relevant papers.
*  Again, they can just make small tweaks.
*  So the ability to take this expertise and manifest it, externalize it outside of like a person's mind to make it much more
*  collaborative is definitely something we're excited about.
*  And then this thing that you talked about with columns, I think is, is another manifestation of this unboundedness in notebooks.
*  There are just so many places where you can go in multiple directions.
*  Like from the very beginning, you can ask like five different search queries and get papers for all of those search queries.
*  You can go really broad.
*  Then for any one search query and get a set of papers, you can add all these columns and start to go deeper all the way down to,
*  I'm going to go really deep into this one paper.
*  So I think this kind of multi-dimensional exploration of the research space is really cool.
*  And also one of the challenging product challenges that we have to work through.
*  Cool.
*  Yeah, I love it.
*  I'm excited to just spend even more time with it now.
*  I love the idea and I haven't had it long enough to have had this happen for me yet, but I do think the notion of going back to an earlier
*  analysis, running an updated search and then filling in all those cells that I previously went through and just like extending that previous
*  analysis and kind of bringing it up to date is something that I will definitely keep in mind because that is going to come up.
*  No doubt.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever.
*  It's storming every industry and literally billions of dollars are being invested.
*  So buckle up.
*  The problem is that AI needs a lot of speed and processing power.
*  So how do you compete without costs spiraling out of control?
*  It's time to upgrade to the next generation of the cloud, Oracle cloud infrastructure or OCI.
*  OCI is a single platform for your infrastructure database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of variable regional pricing.
*  And of course, nobody does data better than Oracle.
*  So now you can train your AI models at twice the speed and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber, 8x8 and Databricks Mosaic, take a free test drive of OCI at oracle.com slash cognitive.
*  That's oracle.com slash cognitive.
*  Oracle.com slash cognitive.
*  Hey everyone.
*  This episode is brought to you by ODF where top founders get their start.
*  ODF has helped over 1000 companies like Traba, Levels and Finch meet their co-founders and go on to raise over $2 billion.
*  Apply to the next cohort of ODF and go from idea to conviction on what's next.
*  Startups change the world.
*  They can also change your life.
*  Is it your turn?
*  Learn more at beyondec.com slash revolution.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work.
*  Customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  Okay.
*  In terms of how this works, I think you guys have been leaders and one of the things that was really exciting to me about the company.
*  Was the focus on reliability, taking a principled approach, not being overly reliant on language models, which I think is becoming a bigger problem broadly and will only continue to become a bigger and bigger problem.
*  But I want to get into a little bit of some of the weeds on that, if you will, because I think people broadly don't have a great sense of the best practices on this.
*  Also, by the way, supervising process and that's become more of a trend.
*  You guys were definitely very early on that trend.
*  So one big aspect of this is task decomposition.
*  I would say, and you can extend my understanding literature here for sure, but it seems pretty clear that task decomposition is good for performance, good for reliability, good for getting accurate answers.
*  I think we've seen pretty consistent results in the literature to support that notion.
*  As a practitioner, though, you sometimes have challenges where you're like, okay, how, just how much do I really want to break these tasks down?
*  I know I don't want to just throw everything into one mega prompt and hope for the best.
*  But on the other hand, if I break things down super, super fine grained, then my token count explodes or I like have to really pair back on context.
*  And that maybe can hurt performance in other ways and things can get slow.
*  So it seems like there's a Pareto frontier here, as is often the case with how much to decompose tasks.
*  I wonder if you could share like how Elicit works in that regard right now and just best practices for folks in general.
*  Because I think a lot of folks who listen to this show are builders and they are probably wrestling in their various contexts with how much task decomposition they should do.
*  Yeah, I think that's a really interesting question.
*  I think in the past often the question was, what's the largest chunk that a model can reliably do?
*  I think we started doing task decomposition with GPT-2 and the chunks were really very small.
*  Does this claim imply this other claim was maybe already something that was difficult to do?
*  And I think now the question is starting to be what is easy to supervise?
*  Like how big or small do you need to make the chunks so that you can easily check whether the work was correct or not?
*  As you mentioned, like with these, I don't know, million token context models, that can be quite tricky.
*  If you get an answer, it's easy to verify that it found something good, but you won't easily know if it missed something because the way you would figure that out is by looking through the million token context.
*  So I think this sort of what is easy to supervise question will really become quite important in the future, not just for humans, but also for models.
*  Even if you use models for the supervision, I think you still want to break things down that make the supervision problem easy.
*  And there are so one case where we use this, for example, was we wrote this paper on what we called factored verification for the illicit summaries where you're trying to make summaries that have really no hallucinations.
*  And there instead of breaking down the task of generating the summary, we instead broke down the task of verifying the summary.
*  So we broke the summary into independent claims.
*  And then for each claim, we asked, is this claim very clearly substantiated by the context?
*  And we've detected like quite a few very subtle hallucinations.
*  And so maybe more generally, one way I think about it is similar to software engineering, where you want to write modular code and you want to write that code because it will help your future self understand it better.
*  It will help others check and understand it better.
*  And so similar to how humans use clear interfaces for their work, I think the most important decomposition principle is use clear interfaces that make it easy to check the work.
*  Yeah, I guess that leads to another interesting question around just the nature of the evaluations that you're doing.
*  My general sense is that across the sort of AI application industry, certainly this has been true at Weymark, where the stakes are quite a bit lower and the results are a lot generally easier to at least like it or they don't.
*  We're making creative stuff so they can watch it.
*  And if it resonates with them, then it's a win.
*  And if not, then it's not.
*  But still we are iterating faster on models.
*  We're using a fine tuned 3.5 and it's become easier to execute that fine tuning and it's become easier to patch things and throw in some different data and we can use GPT-4 to generate data.
*  And so everything is speeding up in terms of the iteration cycle of the model.
*  But that has now created this situation where we used to have a pretty intimate feel for how our model behaved in a lot of different contexts.
*  And now we've started to lose that.
*  And so it's OK, we really do need to bring some structured evaluations to this.
*  We are largely so far using model powered evaluation for like very clear, like I call it like the Ten Commandments, like the vows shall nots, the things we definitely don't want to see.
*  And I'm reluctant still to trust a language model on an overall quality score.
*  I'm like, yeah, we could compare our current script writer to the next one with GPT-4 or whatever.
*  But do I really trust GPT-4 is like scoring that much?
*  Probably not. So I still feel like we need to have, in our case, like humans watch the videos and see if they like them.
*  What is the mix of things that you're doing?
*  Obviously, it's a higher stakes and more subtle challenge with just a lot more different kinds of inputs as well.
*  So how are you finding balance between like when to use models for evaluation, when to use humans?
*  This seems very tricky.
*  I think actually our experience mirrors yours in some ways in that like defining the task properly is really most of the battle.
*  If you can be really clear about what good looks like, then you're most of the way there towards a good evaluation.
*  And for us, that means thinking a lot about who's our core user group.
*  Our core user group is serious researchers.
*  What are they trying to do?
*  So a lot of people use Elicit to write systematic reviews.
*  And for example, the last few days, we've been working on improving our search.
*  And so there we're looking at what's the ideal output here is if you look at a systematic review that has been written, what papers did they actually cite?
*  And what Elicit have helped them find exactly those papers and not some nearby papers that maybe on surface inspections seem relevant, but actually once you look into it are not as relevant.
*  So in terms of metrics, that's the core approach.
*  There are like a few more details on how do you actually measure things.
*  Those are often more standard metrics, like I guess for search like NDCG discounted cumulative gain.
*  But the most interesting part is really deeply understanding the user's problem.
*  I think that was also the thing for the summary station example I gave earlier.
*  Their users really care a lot about correctness and don't want to see like even subtle hallucinations.
*  That's why we're like, we can use models to help a lot there and find things like, I don't know.
*  Some of these models like to just slightly exaggerate the findings of a paper or need to imply that two independent findings are related because the sentence flow a bit better.
*  And so for those kinds of things, if you know that people don't like those, we can encode that in models.
*  But then there are other cases like extraction where we use automated evals, but we use automated evals against human gold standards where human experts have looked into it, have thought about it.
*  These are the things that they want to see.
*  And I think in the future, we will probably look more into using things like AI debate to come up with the gold standards as well.
*  But for the time being, there are some cases where we can't fully encode yet what good looks like.
*  And in those cases, we also have to use human judgment still.
*  Yes, I think trying to use naturally existing gold standards and high quality data sets is and maybe not every use case has this, but we prioritize that.
*  Like where did someone whose work we'd really want to help just try really hard to get to the best possible answer, not try to create a data set for AI evaluation or training.
*  And then how can we use that like naturally existing human state of the art to evaluate our work is definitely something we try to lean on a lot.
*  And our users have been really great in helping with that.
*  And then I think the kind of factored verification approach that Andreas was mentioning earlier is also an important part of it.
*  So Nathan, you are saying you're wary of just throwing a bunch of things into the prompt and saying GPT-4 is this good or bad?
*  But if you break down the task into is this supported by the text?
*  Is this accurate?
*  Is this hallucinating?
*  Does it answer the original question into each component?
*  It's generally much more constrained and I think produces better results that way.
*  But yeah, I think part of it for us is also like, how do we structure the interaction in illicit so that everyone is doing more fine grained evaluations?
*  Like we're doing more fine grained evaluations and our users are doing more fine grained evaluations.
*  So when you gave the example earlier of you're looking for these papers on mixtures of experts and you're like specifically focused on large models, I think in other products or in another context, you might have just been like, I have this question.
*  Please give me relevant papers.
*  And we're like, we don't know what relevant papers are.
*  But if we make it possible for you to be like, actually, what's relevant to me is models of a certain size, then you can explicitly you can break that you implicitly break that task down a separate task of what were the models, size of the models used in this paper.
*  That is a much easier task for us to evaluate as opposed to just what are what are generally relevant papers for Nathan in this context?
*  This portion of the conversation started with evaluations, which is typically an offline process.
*  Right.
*  But you could also imagine bringing at least some of that process into the runtime.
*  I guess it would depend on multiple variables, including like how much of a problem it is after all your effort has gone in and also like how much it's going to cost and how much it's going to slow down and like how much that kind of incremental effort would help at runtime.
*  Is there like a easy to summarize state of like how many hallucinations you've been able to drive the product down to?
*  And are there runtime, like secondary models, checking models, runtime checks happening in the course of a user session?
*  Don't remember the exact numbers, but I think it was something like from 1.5 hallucinations on average using the largest models to maybe 0.5 hallucinations where you were like quite strong.
*  So I think that's a little bit of a trick about what we count as a hallucination in that context, like even slight exaggerations or slight inaccuracies we counted as such.
*  We don't currently use additional checking at runtime.
*  So the primary use of that was to generate training data that we then used to distill a model that had lower hallucination rates.
*  So I think that's a really interesting thing.
*  And we're always looking for ways we can help users turn additional budget into more accurate answers as like a key criterion at illicit.
*  And I think additional runtime checking will be one of those properties.
*  Yeah.
*  And then in app, we've done some testing.
*  It really varies depending on the task.
*  So we've done mostly evaluations on some of the predefined extraction columns.
*  In the kind of direct side-by-side comparisons we've done with manual extractions, we've pretty consistently outperformed trained research staff who are doing those extractions.
*  So that's been really cool.
*  And when you do it, use it yourself.
*  Again, it depends on how you're formulating the question, what you're asking for, is the information even in there.
*  But certainly in my experience, I'm always amazed by how quickly and how virtually the data is able to be extracted.
*  And I think it's definitely at superhuman performance today.
*  That's cool.
*  And it's also very important always to keep that kind of alternative in mind.
*  I feel like one of the lessons I've learned over and over again over the last year of talking to people, building things is just like how often there was no human.
*  There was no measurement of what human performance was when they started off in a given domain.
*  And people in many cases imagine that it's super awesome and it's often not quite as awesome as they imagine.
*  Yeah.
*  Sometimes people give us a gold standard and then we're like, we think there are some errors in your gold standard based on what we've done.
*  You touched there for a second on models and obviously creating datasets is a huge part of this.
*  And you mentioned distilling.
*  I'd love to hear what are the models that are in play today?
*  To take a step back, our principle is we want to always let people use the best models at any one time.
*  So we're pretty pragmatic about what models to use.
*  And therefore, it's also quite important to us to not be tied to anyone like compute provider because particular sometimes like
*  combinations of models from different providers might be better than the best single model.
*  And that means I think right now we use a collection of models, which includes fine-tuned models, including Client T5.
*  You could use fine-tuned GPT 3.5, use GPT 4, vision GPT for understanding tables.
*  We're currently working on using Cloud 3 for some functionality.
*  But next time we talk, probably the answer will already be different.
*  It's really at any one point you want to be at the frontier.
*  And so getting good at quickly swapping out models is the most important thing.
*  Yeah, the speed of shipping is also definitely a key priority for AI apps in general.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The tech world turns to the Brave browser for its unbeatable privacy protections.
*  But did you know that Brave also has a private ad platform?
*  Brave ads offers first-party targeting and it's been cookie list since day one.
*  So you can relax while third-party tracking cookies disappear from the web.
*  Today, millions of people turn to ad blockers to avoid being tracked and pestered online.
*  But Brave's new ad model aligns incentives for users and advertisers.
*  Users earn rewards for viewing ads, which they can save, spend or pass along to their favorite creators.
*  And advertisers score points for respecting user privacy, generating ROI without invasive tracking.
*  So whether it's high impact announcements on the new tab page or keyword targeted ads in Brave search,
*  Brave offers diverse, private, future-proof ad formats for all your business goals.
*  Join the future of advertising at brave.com slash ads.
*  Mention MOZ when signing up for a 25% discount on your first campaign.
*  Today's podcast is brought to you by Plum.
*  If you're a startup building AI features for your customers,
*  you're probably feeling the pain of hallucination, prompt testing, unstructured responses, subpar queries for embeddings.
*  And of course, the mind numbing process of general iteration and refinement when your engineers have to make every change by hand.
*  That's where Plum comes in.
*  Plum is a no-code AI app builder designed for product teams who care about quality and speed.
*  What is taking you weeks to hand code today can be done confidently in hours.
*  Check out useplum.com.
*  That's Plum with a B for early access.
*  Hey all, I'm hearing more and more that founders want to get profitable and do more with less, especially with engineering.
*  Listen, I love your 30-year-old ex-Fang senior software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent.
*  But boy, is it a hassle to do at scale from sourcing to interviewing to on the ground operations and management.
*  That's why I teamed up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high level for over five years.
*  To help you access global engineering without the headache.
*  Squad, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent so you don't have to.
*  With teams across Asia and South America, we can cover you no matter which time zone you operate in.
*  Their engineers follow your process and use your tools.
*  They work with React, Next.js, or your favorite front-end frameworks.
*  And on the backend, they're experts at Node, Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's doing two hours of work per week, but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost.
*  Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the wait list.
*  You recently put out a blog post about how you have, I believe it was, shipped a new feature every week.
*  Do I have that right?
*  Yeah, I think on average it ended up being 1.4 weeks.
*  So there are a couple of weeks that we missed.
*  We were doing bigger launches.
*  That's in a video creation app where it's like relatively lower stakes.
*  Like that would still be pretty good, I would say, to launch a new thing every week or just less than that.
*  But given the standard that you have around reliability and minimizing hallucinations being so mission critical, how are you balancing that?
*  Is it just a matter of having a battery of tests that you can run and trusting them?
*  Or is there more to the discipline of the iteration cycle that you can share?
*  Yeah, I think we're staggering it as much as possible.
*  So some of the accuracy dependent features, they can be a little bit more difficult to do.
*  The accuracy dependent features, they take a lot of time to iterate on and research.
*  It's not like they're in progress for a week.
*  They're in progress for a while, but then we can stagger the launches across multiple weeks and then we can offset them with other more infrastructural or just pure product based launches.
*  Yeah, I guess the other thing to mention is, I think, if you want to be at the frontier of accuracy, you need to ship quickly because every week a new model is coming out.
*  And so if you're slow to ship, then your product will probably not be the most accurate it can be.
*  Yeah, I guess this is also where the task decomposition comes into play because it's much easier to iterate on and ship a new predefined column for statistical technique use than it is to ship a new model that's been fine tuned on all the scientific papers and evaluate that for quality.
*  So I think, again, breaking down things into small tasks helps with launches as well.
*  Yeah, that's interesting.
*  So, it might have been as the models obviously have gotten better over the course of the last 10 years, but certainly we've, we've experienced a lot of kind of relevant, I would say, I would imagine a lot of thresholds have been passed over the last year or so.
*  So, I guess you could tell a story of what was not possible a year ago that just, just the language models couldn't do it or they couldn't do it reliably enough that now are like preset column options because we've tipped over from not there to there in terms of the frontier models ability to do it.
*  The most obvious case is answering using tables. So this isn't a specific column. It's across all columns. We know if you're using high quality mode also look into the tables of the papers.
*  And for many questions like if you I guess think you mentioned earlier, is the p value significant or things like that is a hypothesis refuted. Those are often only found in tables.
*  So, I think that's a really hard problem that before multimodal models was basically not possible. And even at this point, I think there's like a lot of engineering involved in getting things to be fast and parsing tables, etc.
*  But now it's possible. Otherwise, I think there is a kind of increase in what information you can leverage across the board. So for example, I've been working a fair amount with an organization called EPOC.
*  Progress in the field of AI across a compute parameters used data set sizes, just to see like how things progressing and the way they do this is by analyzing the literature.
*  What kinds of models are coming out actually are pretty similar to the example you gave earlier.
*  If they ask you a question like how much compute was used in a paper often papers don't say we used Eklflops.
*  They say we train this architecture on this type of GPU for two days. And if you want to actually answer that question, you need to do a bit of reasoning.
*  You do like Eklflops is like this GPU and what's the answer overall. So as models get smarter, they can answer questions that are like one or two hops removed from what's literally in the text.
*  Okay, that's really interesting. And I'm very curious to know how that works and maybe it varies depending on the context. But I could imagine at least two different approaches or even a combination like one would be chain of thought.
*  And I wanted to ask you about chain of thought in general. Another would be like code generation and execution. And then of course you have like chain of thought followed by code generation and execution.
*  Let's start with how that kind of reasoning is being implemented. And then I do want to dig a little bit deeper into chain of thought as well because I feel like that's another black box voodoo area where people know that it works.
*  But there's probably a lot of caveats and gotchas there that people should be more aware of.
*  I think chain of thought is quite important to us. So we use chain of thought for basically all questions you ask an illicit and if you use the CSV export functionality, it will actually include an extra columns that say here's the reasoning for this column, which I recommend people to check out.
*  I think often it's like quite instructive. And the reason we do this is because transformers obviously have a fixed amount of compute per token.
*  And so there's some questions that they just can't answer. You can't you can fine tune as much as you want, but your transform is not going to be able to do arbitrary arithmetic.
*  That's just not possible. I think there are different architectures that people are interested in or like modifications like POS tokens or something.
*  But at least given the current architectures, I think chain of thought is often critical. And I think the epoch example I gave is an instance of that.
*  There I do recommend that people don't just take the answers, but also and that's what they do like also add like specific columns.
*  I think ideally you add illicit columns that ask about what was the compute architecture or what was the data asked about the ingredients as well.
*  In addition to just trying to get them all to give the full answer, because sometimes the reasoning still is more complex and might require some human intervention.
*  So when I do an extra column, am I able to is it automatically including the results of earlier columns in that subsequent column?
*  It suggested it seemed like you were suggesting that I can like incrementally build up columns, but I hadn't realized that I could compound them in that way.
*  Do you count in the current published version? We have a prototype where that was possible and excited to ship it as one of those one week features, but it's still work in progress.
*  I guess is there just any more kind of intuition you could help people develop for chain of thought?
*  I've seen like lots of stuff that shows that it works better. It's obviously just common sense at this point that it's going to work better.
*  It's also become the default behavior in the models that people are most accustomed to using.
*  It's funny, though, I still guess it's been a little while since I've seen the last version of this, but I've seen quite a few examples from published research
*  where benchmark reports were dramatically understating model performance or capability, let's say, because the prompt structure had prevented chain of thought.
*  Like I've seen this with Big Bench. I've seen it with a couple like theory of mind questions where it's like you set up a few shot thing because that was like the way to do it at one point in time.
*  And that's like maybe how the benchmark was constructed. But you're jumping straight to the answer.
*  And no wonder you're not finding the GPT-4 is any better than GPT-3 to take one memorable example that I really spent some time on.
*  OK, whatever like that, but we should be past that now.
*  But then you see this other stuff from the literature where it's not really super faithful or sometimes the answers don't really seem to actually depend on the chain of thought.
*  There's been these like counterfactual chain of thought examinations where you change the chain of thought.
*  But does it actually change the answer? I find that stuff confusing.
*  And to be honest, I'm still in the mode where I'm like, it seems like it's pretty clearly best practice.
*  It's probably the best I can do in many contexts where I'm working.
*  I've also had really good luck for Weymark specifically training a chain of thought into a 3.5 fine tuned to really teach it exactly how we want it to work through this particular problem.
*  But yeah, I still feel like my worldview is like pretty fuzzy when it comes to what's really going on with chain of thought and how do I make sure I'm getting the best from it, but not trusting it too much.
*  So any more you could share there or any even if it's somewhat speculative, I would love to get up to speed with your thinking.
*  I think it's just fundamentally hard because people don't understand what, including me, what's going on inside of these models.
*  And so anyone who claims they know exactly how a chain of thought helps or doesn't help the model, I think it's probably just wrong.
*  And I also want to agree with you that I think people probably still are making the obvious mistake of being a K model.
*  Say yes or no, and then justify your answer.
*  And that's obviously terrible because once it then it has to answer without any reasoning and will just lock itself into a potentially wrong avenue.
*  I think this is fixed now, but the first bard was shipped that way.
*  As far as I could tell, that was like an eye opening moment.
*  It was like, guys, you get the best research team in the world arguably here, but we lost something in translation.
*  I do think that is now fixed.
*  But yeah, I remember seeing that.
*  I was like, oh my God, listen, some of these problems run a little deeper.
*  Models should be fine tuned on more.
*  And hopefully I think that might be in progress, but we'll see is being able to say, oops, I was wrong.
*  I think if models were more OK with saying, yes, actually, wait, no, I meant no.
*  I think that would help with that behavior and I think would probably generally be a good thing to do to allow for more kind of, I don't know, truth oriented reasoning as opposed to after post-hoc justification.
*  Tactically, some of the things that I think it depends on like how you structure the chain of thought, not like you guys have been saying, it's not all kind of chains of thought are created equal.
*  Giving the model the option to say, I don't know, and here's why, or here's the closest thing I could find in the text, or we don't think it's mentioned.
*  But then here's why we here's what we looked at and where we expected to see it, but didn't find it.
*  It's actually still really valuable and makes the model more accurate.
*  A lot of times the problem we have is the answer isn't in the text that we're looking at.
*  So forcing the model to come up with an answer is what leads to hallucination.
*  And even if you don't have the answer, you can still give really helpful information to the user.
*  So giving it these back out options and like most relevant next helpful thing, I think is both a better product experience and reduces hallucinations.
*  This goes back also to the point about clear interfaces we mentioned very early on.
*  I think you can define an interface that is you need to say yes or no, or you can define a different interface, which is you will get data.
*  You can choose between saying it contains the answer or doesn't contain the answer.
*  If it does, you're like the things you can say. If it doesn't, you have different ways you can be helpful.
*  I think thinking about what are the ways to deploy models that make them as useful as possible is, I think, an important part of what we need to do.
*  Yeah, you mentioned the pause token.
*  I was also reminded by kind of the notion of the back out or the ability to recognize a mistake of the backspace token, which seems like a step in that direction,
*  although certainly a baby step, probably in the grand scheme of what's ultimately needed.
*  How big are the data sets that you're creating for this?
*  Like at Weimark, we find that quality is obviously super important. Scale hasn't been that important for us.
*  Like low hundreds of examples is pretty good.
*  Then we can throw in a few more when we have another use case or random thing that we want to tack on.
*  Interested to hear how big your data sets are and then also interested in like how you are doing the fine tuning.
*  At this point, we've got quite a menu of you're going obviously beyond base models, it sounds, but are you doing instruction tuning or like doing the sort of RLH or RLAIF with like an actual reward model?
*  Or I personally have not been like up close and personal with a DPO project, but that seems to be like becoming more popular as well.
*  So yeah, like data sets, like how big do they need to be and how do you actually turn that data set into a purpose built fine tune model?
*  Yeah, like you, we found that a few hundreds to a few thousand data points is generally all we need.
*  Data sets have been more important to us for evaluation than for fine tuning, which is not to say we don't use fine tuning.
*  We do use it. Also used a constitutional AI a bit where we trained a preference model on deciding which of two summaries is better, where the constitution included things like the summary should be accurate, should be concise, etc.
*  And there, yeah, again, I think the data set was maybe a few hundred to a thousand human judgments.
*  Interesting. So it's not all RLAIF though. So it sounds like it's instruction, like supervised kind of instruction tuning first and then sometimes adding on this RLAIF layer?
*  Yeah, that's correct. And I think the ideal case is we don't have to do any fine tuning.
*  I think we're not in the business of kind of making, I don't know, doing ML work or something.
*  Ultimately, what we most care about is deploy AI systems in a way that leads to the highest accuracy, most useful answers to users.
*  And I think sometimes that will be fine tuning of different sorts.
*  But I think if you can avoid it, it's actually better because you can deploy systems even more quickly.
*  And I think increasingly there are situations where if you have the right prompts, you can just use off the shelf foundation models and by composing them the right way to do tasks.
*  Yeah, that's interesting. So you've mentioned Epoch and I spoke to Tamai not too long ago.
*  I'm thinking I might need to get him on here as a guest too.
*  He asked me a really interesting question, which I'm now going to ask you. This is more of a prompt maybe than a question.
*  What does a scaling law for scaffolding look like? He may have asked you that question too.
*  It sounds like I'm brought to this because you're suggesting that fine tuning and scaffolding or structure maybe more generically are substitutes to a degree.
*  You can also imagine they might be complements in some cases.
*  But it sounds like what you're saying is you guys have built out the structure with enough granularity and you have enough confidence in it that you don't need to fine tune as much as I would have naively guessed.
*  And then that leads me to think, is there any multiple people have asked me this like scaling law for scaffolding question?
*  And I don't really know what to make of it other than just obviously scaffolding is useful.
*  Here we're getting this sense of some substitutability with fine tuning, but I don't know what else comes to mind when I say scaling laws for scaffolding.
*  Do you mean like how does scaffolding scale with larger models or like what would enable scaffolding to get better with more compute or what exactly is the question?
*  Yeah, I don't even know. It's a kind of an ill-formed question.
*  One sort of scenario that I think about a lot is the fact that we are building out the complements to the core language model, right?
*  The thing that like what I often say these days, we now have AIs that can plan, reason, and use tools.
*  Not necessarily super well. A year ago they could barely do it at all. Two years ago they literally couldn't do it at all.
*  So that's like happening pretty quickly. And because we now have those people are like obviously racing out to build the like planning frameworks and the tool harnesses and all that stuff.
*  And they're putting a lot of elbow grease into that to make it work with the current crop of models.
*  And they're broadly speaking like the sort of freeform ad hoc delegation agents like don't quite work yet, although you do have the occasional flight booked or whatever.
*  But then I think, geez, with all that stuff built, if all of a sudden there's a significant model upgrade that goes wide at the same time, then like a lot of things that have previously just fallen over might actually already have enough scaffolding to work.
*  So this is like outside of your like core product development domain because you guys are obviously building something like super structured and it could work better, but it's not going to be probably qualitatively different from one model release to the next.
*  But I do see these sort of agent systems that other people are building as like potentially right for a step change in what they can actually do in the world.
*  Just because all of the sort of surrounding stuff is already there and then it's boom, GPT 4.5.
*  You know, is that today? Well, check your watch. All of a sudden things might start to work a lot better.
*  So I'm taking this a little bit far field here, but the mention of epoch and the kind of analysis that they're doing as well as this notion of some substitutability between fine tuning and surrounding structure at least caused me to ask the question.
*  Yeah, I think it's a great question. I'm also very interested in it.
*  The most basic example is the thing we mentioned earlier is chain of thought.
*  So you're like you said people underestimated how good GPT 4 is because they didn't use chain of thought and chain of thought is obviously like a very, very basic way of scaffolding.
*  And so then that raises the more general question, which is how much can you augment language model capabilities just using better scaffolding?
*  Various types of decomposition, debate, amplification are all ways of scaffolding.
*  Some of these are starting to work better with better models.
*  I think both debate and amplification, a kind of decomposition to sub questions did not work super well with GPT 3 level models are starting to work much better now.
*  And I don't think it's something is like very well understood what the shape of that landscape is.
*  So I'd be excited to see more work on that.
*  I wanted to address like one other thing you said about maybe these other agent systems, there will be a step change.
*  A key thing for illicit is always think ahead to the future.
*  Don't build just for the present because the situation where illicit is going to matter the most is the situation where we are like moving closer to AGI and thinking and actually need to use these AI systems to make really impactful decisions.
*  So we've been working on more scalable infrastructure where we both in the notebook setting, where we can let note agents take actions similar to our humans take actions, but also scaling to larger kind of task badges.
*  So internally we've been calling this the exascale engine where we're like right now people use models at like fairly small scale, run it over tens to hundreds of papers and extract information from those.
*  But that's not that's obviously not where things are going to stop.
*  Ultimately, you want modest to do reasoning across tens of thousands hundreds of thousands of papers or other kind of similar, similarly shaped large inputs.
*  And I think that does require infrastructure that doesn't really exist right now.
*  Like an infrastructure for taking these under liable pieces, running them at scale, using like models to supervise other models and eventually get high quality answers without having everything run in like a single kind of huge black box with like opaque weights.
*  So we are thinking a lot about that future.
*  So it seems like the key, there's you're creating a equivalence there between scaffolding and just bringing more compute to bear.
*  It's like you're translating all this structure into more compute from more angles, right?
*  You can go wider and handle more stuff.
*  You can also like have models check models.
*  But a lot of that stuff seems to be just not just because it's obviously complicated, but there seems to be a sort of the fundamental currency there is still compute and the scaffolding is like a way to organize it, obviously.
*  Yeah, that's exactly right.
*  I think the key question is like, how do almost we as a society want to turn compute into more work?
*  And I think one answer is we're going to train larger and larger models and we'll hope for the best.
*  Maybe we'll augment it a little bit with like better interpretability methods.
*  We are working towards a different answer, which is we think like more compute will in fact likely to great things and more correct answers, etc.
*  But we can get there through more transparent architectures if we can build the right infrastructure.
*  The obvious next question is what is the infrastructure look like?
*  What are you? What is the kind of frontier of that today?
*  Obviously, there's like a ton of papers out there in the literature.
*  It's like not being fully web scale, still a very large database that you have to search against interested to know what that stack looks like.
*  And then I hadn't really thought too much in the past about the ability, but I understand this is either maybe already happening or like definitely make sense as an opportunity.
*  The ability to somehow make use of a large corporate internal body of knowledge, right?
*  A pharma company is obviously going to run a bazillion experiments and have a billion kind of internal reports.
*  And I guess there's probably a lot of interesting challenges around that, including like where they will allow their data to go and live and probably also like different standards or quality.
*  Would you want to do something have to be an official internal report before it would be included?
*  Or would you like, oh, mine notebooks going back years that may just be messy and never really meant for other people to see certain things?
*  So, yeah, the more I talk my way around it, the more I realize there's a lot of infrastructure probably that is just in that first bit where you ask your question and get to the results to then be processed in this structured form.
*  So what can you tell us about that first bit of the product experience?
*  Yeah, there's I guess there's what is happening right now and what would we like to happen in the future.
*  Maybe starting with what's happening right now.
*  I can only cover it on a high level, but roughly so you go to a list that you enter your question.
*  What happens next? Let's say your question is I want to find studies on creatine for cognition after 2020.
*  Please give me our CTs or something.
*  And then the first thing that happens is we take your search and be automatically parsed it into the different components.
*  So they're like the search that there's the search component like I want to find studies on creatine for cognition.
*  But then there's also the these intentions you expressed about what filters to use, like filtered onto our CTs only after this year.
*  And we extract those out into kind of like a an API call that has those as separate bits.
*  We pass it off to our search engine, which is a kind of hybrid semantic and lexical or filter based engine so that it can both find the relevant documents,
*  but then also use those additional intentions you expressed to narrow down to the most relevant papers.
*  We'll probably get something on the order of 500 papers initially that are our strongest candidates for what could be relevant to you.
*  And then we go through a sequence of re-ranking stages that are increasingly more expensive using things like a MonoT5,
*  crossing coders, maybe a few heuristics around recency or citation count,
*  and then get to the kind of final list of papers which we use to generate a summary for you.
*  And even at that final step, when the model is looking at the papers to generate your summary,
*  it can still decide to ignore some papers if they're not relevant.
*  So there's many stages where filtering and processing happens.
*  Cool. So that was all today.
*  Yeah, so that's all today.
*  And I guess the entire process I described obviously has to happen pretty quickly because you're there in your browser waiting for the results.
*  But there are many instances where actually you would be fine waiting longer for a better result.
*  If you're going to write a systematic review, which people work on these things for nine months or something,
*  which is obviously crazy and we need to speed it up. But anyways, it's a long timeline.
*  And so you're like, you would be happy to wait for an hour if you could get really great results.
*  And you would probably also be happy to pay $100 or something of that sort.
*  And so right now that's not possible because Illicit is tied to your browser session.
*  If you close the tab, it's going to go away.
*  Some infrastructure that we're building right now where we're decoupling the execution of Illicit from your browser session
*  so that you can tell it, use more compute to investigate like all of these papers in more detail, do more filtering.
*  I'm willing to wait longer. I'm willing to spend more money.
*  I close the tab, I come back later and maybe I'll have a progress bar or something.
*  But there's the ML work in the background is happening separately from what you're looking at.
*  So it's a lot more like outsourcing things to a human research assistant that then goes off, does things and comes back to you.
*  Cool. I strongly feel that people in the AI app space generally put too much emphasis on speed and cost.
*  And I've been banging this drum a little bit lately.
*  Like what matters to me most is success on high value use cases.
*  So I think that definitely makes a ton of sense.
*  And I'm excited to see that that future version start to come to life.
*  I guess I want to get into a little bit more kind of the business side and the users.
*  And you guys also have done this creation of a for-profit entity related to the nonprofit entity.
*  But one more question just on kind of the product philosophy.
*  Obviously the whole thing is really motivated by the notion of let's keep these things under control by putting them in very prescribed context
*  and making them do like very specific things or transparent architectures, to use your phrase.
*  Is there more that you think about or do you feel like that is enough?
*  Obviously, one of the big things that people have worried about a lot over the last year is what happens if a language model can help you build a novel pandemic agent?
*  And at first I was like, yeah, let's say probably doesn't have too much.
*  They don't have to worry about like wrong think or political speech or whatever.
*  But then I was like, oh, but actually the number one thing of the novel pandemic agent is probably right in the illicit wheel.
*  And not to give anybody ideas, but it's you guys have probably built the tool that would be the most helpful for something like that.
*  So how are you thinking about that kind of question?
*  Are you like putting filters in place to try to identify like when people are asking bad questions or I guess I'm sure you've got more.
*  I won't even try to guess. You just tell me what that looks like right now.
*  I guess in general, when we think about safety, we both think think about long term safety and misuse.
*  I think you're addressing the misuse point here.
*  And I think from what we've seen so far, it's not a big concern, but obviously as we scale things up, let models do more work.
*  I think it will become increasingly important.
*  And for if there are use cases that are on the borderline of could be useful for someone who's trying to defend against the pandemic, but could also be useful for someone who's trying to create the pandemic.
*  I think either accounts will have to go through a specific review to be using illicit for those use cases.
*  Or otherwise they'll have to use a version of illicit that just doesn't support them.
*  I think there is initially a question around like how exit what is the best way to make that happen, which I think many people in the industry are going to face.
*  And I don't know that we will invent the wheel on our own here.
*  But to just throw out one idea, there's been a recent paper by Dan Hendricks and others on I think like wiping information about, for example, weapons of mass destruction.
*  I think they called it the something like the weapons of mass destruction, something benchmark where you're trying to figure out, can you make models unlearn the most problematic knowledge?
*  And I think it's probably important that in cases where people don't want to go through like some account review, you can't just ask the model, hey, make me such a weapon and be like, hey, here's your weapon.
*  Good luck.
*  Yeah, I think in the past we've talked about kind of applying these factored verification or evaluation techniques to being able to monitor the kind of behaviors on illicit as well.
*  Or if you do have this extensive log of your research progress, having kind of models deployed for the activity of not just is this hallucinated, but is there some kind of negative impact of this research?
*  I think it's actually like quite related to things users want as well.
*  Yeah, I think they also care a lot about the social impact of their research and working on things that are impactful.
*  So it's entirely possible that our users pull us towards building capabilities and illicit that help them evaluate the impact and the different consequences of research.
*  The other thing that I've experienced recently that has changed my thinking on this a bit is using pie from inflection.
*  And I like red team everything that I come across just because it's two birds with one stone.
*  I want to try new products and just see what the technology could do.
*  And then I also just curious as to the state of play, have people put any safeguards in here?
*  It is, I would say right now, broadly, it's super wild west.
*  And like most application developers are not putting really any safeguards in.
*  And a lot of them are fine tuning, I think, on their use cases, because at least what I interpret is likely happening is that in fine tuning, they are removing whatever guardrails like the Lama to base version originally had is just wiped out in their fine tuning process.
*  So I like very rarely get can get refused things.
*  But one thing that I have noticed is pie is like the one thing that I've not really ever been able to jailbreak.
*  And it seems like it has a very good model.
*  I don't know that it's a different model.
*  It's probably part. I think it's probably the same model, but it's like very good at recognizing when the user is like becoming deranged.
*  And so I've started to think that, like the model outputs are like one thing you might want to filter, but also just asking, does the user seem well is like something that the models are actually pretty good at.
*  And I get these responses from pie in my like attempts to get it to do something out of bounds that are like, Whoa, buddy, like you sound like you're getting pretty worked up here.
*  And then it's like talking me down and it really does have a pretty impressive EQ, which again, we're a little bit off the main line of discussion here.
*  But there is something there. I think that it's not purely analytical.
*  And I've found in many cases, even if there are pretty good filters, I can get around it or whatever.
*  But but pie has brought something new to the table with a sort of emotional awareness where it made.
*  I think it may in many cases be easier to detect that like the person seems not well as opposed to this content is like inherently problematic because so many things are obviously dual use and it's just confusing.
*  Yeah. And actually, I think that's another good example of a place where doing something proactively well that is good for your product can also help you defend against misuse because the more like we often want to understand the intent behind our users queries and the intent behind their searches in general.
*  Like that just makes it significantly easier to give them relevant results. So I think that will naturally pull us towards better understanding.
*  What is the user really trying to do here? And in 99.99 percent of cases will use that capability to just deliver them a better illicit experience.
*  But in the rare cases, that same capability might help us feel like, oh, wait, this person is like maybe trying to do something sketchy and we should do something about that.
*  Yeah, expanding or transforming that initial question seems like you may already be doing that to some degree under the hood, but I see that as also an emerging trend.
*  We just did an episode with Exxon, which does that as kind of default behavior. And now Anthropic just put out their sort of meta prompt creator as well, which is you throw in your haphazardly created prompt and they structured up and turn it into a template for you.
*  But I do think there's a lot of opportunity in. And again, that's as you're saying, that's a make the product better, but also naturally build into that phase.
*  A little bit of a gating mechanism for making sure this is the kind of prompt that we want to be expanding on.
*  OK, cool. So this has been great. I really appreciate how much information you've been willing to share about how this works.
*  I think people will learn a lot from it and hopefully many will build better apps as a result.
*  Let's talk about the business a little bit. The last time we talked, I think bio biomedicine biotech pharma was like the most intensive use case.
*  Sounds like that's probably still the case. Be interested to hear like how the user base is evolving. Maybe anything you want to share about patterns of use.
*  I say again, extremely small time investor. I definitely took note of the phrase earlier that like one of the key things you're looking to do is help people translate more budget into better results.
*  So I'm curious as to how much that's already starting to happen. So, yeah, that's there.
*  But tell us how what sorts of trends you're seeing and how the business is going. Yeah, I would say biomedicine is still a really like one of the top domains and one that we focus on for a lot of reasons, because it's a place where there's more willingness to convert budget into accuracy.
*  They have like fairly well established and very much batch and power workflows that I think are really good to start automating and generalizing to other domains we have.
*  We have, but honestly, even from the beginning and still now it's really it really is quite distributed. I think there's been a lot more growth in engineering and humanities.
*  So before I think originally it was like biomed and then ML or computer science were like the two main categories. Maybe they made up like 50% of our users.
*  But now I think there is a more even split. And I was surprised to notice a lot more growth on the humanities side and on the engineering, just general like mechanical, chemical, environmental engineering side as well.
*  And I think those are also going to be really interesting domains for us to keep exploring. And yeah, we're we are focused on these like batch users.
*  We always we've referenced systematic reviews and meta-analyses a lot. That's been a use case that kind of inspired all the columns and this tabular organization of information from the beginning.
*  Those are the users who are most often trying to process thousands up to millions of papers.
*  And I think that's really I would really love to see more language model products pushing in that direction in those batch workflows, not just in these more casual, shallow chat based interactions.
*  I think there is definitely a place for that. But a lot of the value of these tools comes from being able to process so much more information than a person can.
*  Usually what's happening is the status quo is like hiring a person to like manually go through a lot of this work or they have a team.
*  Often people don't want to do this. Like even the people who are hired to do this, it's like it can be like rote and demoralizing.
*  So there are definitely we've had cases of we've worked with teams that are willing to spend thousands and tens of thousands of dollars on these projects.
*  And even at an individual level, there are people who are willing to spend hundreds of dollars like just an individual consumer who's willing to spend hundreds of dollars because it's like there's a very clear value add and objectives kind of gain.
*  So yeah, that's been really cool. And we want to keep pushing into that.
*  The main driver of cost to the user, value to the user and obviously revenue to the company is depth of processing. Is that the main takeaway? Expand the number of results is the biggest thing.
*  It goes in multiple dimensions. So there's like the easiest, I think the largest kind of lever is like number of papers considered and how comprehensive you want to be.
*  There's also kind of accuracy, like how much are you doing a kind of shallow pass or just a rough 80 20 of how relevant this paper is so you can because you're going to read the papers later anyways or whatever.
*  Versus how much are you going to take the result of this extraction and put it in a database somewhere that's going to feed into another analysis and it's like actually really important to get that super right.
*  That also is another dimension. And then, yeah, maybe another component is like how much data do you extract or how deep do you go into the analysis of any one paper?
*  I'm going to have to think about what I want to spend $100 on, Elissa, before long. Maybe help me talk me through that maybe a little bit more because I do have some of these questions that I would be definitely willing to spend more than I think I have so far on the product.
*  Recent things I've been interested in. I think I mentioned a couple of them. Mixture of experts. Like I'd love to know everything there is to know about mixture of experts.
*  That one is a little bit. One thing I found at least with the kinds of questions I'm asking that might be a little bit. Maybe this maybe it doesn't cause a problem, but maybe it feels a little bit different than like some of the examples that you've been highlighting is I want to know like everything about this kind of cluster of things.
*  And it seems like a lot of times the machine learning papers like answer one aspect of it. They'll study kind of one thing. And in many cases, from what I've seen, there's one or maybe just a couple of papers that have even addressed that sort of thing.
*  I'm also really interested in curriculum learning. And then what I see is like in mixture of experts, there's like a bunch of different techniques.
*  And then over in curriculum learning, there's like a probably 20 different papers at this point that are like, here's a sort of here's one course in a broader curriculum that we studied. And we found that including this in pre training or pre training on it or whatever led to better downstream performance.
*  And then I think I've only seen one that was like curriculum learning meets mixture of experts. So I don't necessarily know that there is like the depth in the way that there might be for if somebody studying like weight loss or whatever, there's obviously going to be like infinite studies published.
*  Here, there's not necessarily so many. But how should I think about translating dollars or compute to the fastest improvement in my worldview that I can get out of the product?
*  I think that might partially hinge on things that are also still baking in the illicit office. I think what you want is something like, here are the first find the 20 ish papers say on curriculum learning. And then what you want is now let me reorganize information in those papers to make it as easy as possible for me to understand how this field works.
*  And that is something we're actively working on where you're, I think you don't necessarily want things organized by paper, you instead care about what are the different types of curriculum learning and for each of those types.
*  What's the evidence for how well this works or what models it applies to or whatever else. That's a pivot on the illicit table that you're currently seeing. And yeah, stay tuned. I think we will soon give you new ways to turn money into knowledge.
*  That is definitely very interesting. And I can see ultimately this sort of means like a row would have a different kind of meaning as opposed to a paper being a row, a different concept could be a row and papers could populate cells downstream of that. Put me on the early access list. Put me on the waitlist.
*  There's a very basic version of this in illicit right now called list of concepts, which is a workflow that does search through the literature and then try to organize things by concept. I think people should try it. I'm often surprised by how well it works. It is trying to be more comprehensive than the baseline illicit search and also takes longer to run, but it's still only a precursor of the kind of deeper concept based functionality that we're working on.
*  Cool. How do you with users? So many of these, this is not a consumer app, right? It's a professional tool. Do you have any trouble with habit formation? Like people just because that's a huge problem in just apps in general, right? Like people try it. They don't come back. If they don't come back every day, then they don't come back at all. Maybe this is just like such a high value tool that doesn't have substitutes. That's not really an issue. But how do you think about kind of frequency of use? Again, I'm on the side of cost and
*  latency and maybe even the like frequency of use are overrated. I would wait a week to get the exact report that I want on the, that really helps me understand these mixture of experts or curriculum learning, whatever other topic. Like it's not that it has to be today, but yeah, I could see that being from a business standpoint. I could see that being a problem if it's so infrequent that people maybe forget that you exist from one opportunity to use the product to the next.
*  I think it is different from just like a pure consumer app. We certainly have people who just use it for personal use cases in a more periodic way. I think they still are very engaged with us as a company, probably because we launch these features every week. So most of them are I think still aware of it. So even if they don't have everyday use cases for it. But yeah, from a prioritization perspective, we're much more focused on the high value batch, really intense use cases where there's not a, there's no alternative basically. And you're working on a project for a while.
*  And you're really stoping it out and you have clear criteria that you're going to evaluate the different solutions for.
*  So I've had this idea for a while of the AI bundle, which is a kind of like your cable bundle in theory, where you have a single subscription that gives you access to a lot of stuff.
*  And presumably it would be like more than you can get with the free trial, probably less obviously in the unbounded research case, you would have to have some bounds on what you would offer to people who come in as like part of the AI bundle subscription.
*  But my kind of concept there, and actually just got contacted by somebody who was like, I'm working on this. So there may even be an opportunity to make it real at some point.
*  The idea is hopefully that from the application developer side, you don't have to give away so much tokens and harm your margins or force you into weird pricing dynamics.
*  And then for the user, a more frictionless, I get to really use all these things. And if I really want to be a power user, I can upgrade.
*  So I guess my question is, would you like to be part of my AI bundle?
*  I think it really depends on the details.
*  Yeah, just tell me more. What comes to mind?
*  It depends who is the target of this bundle? What else will we be bundled with?
*  How will, do I feel confident that these users will use illicit or actually is this totally outside of our target market?
*  What do those kind of finances look like? What do the pricing margins look like?
*  What does the operational cost involved for us?
*  How much are we losing the kind of customer relationship? I think that's like the big question with a lot of aggregators. So aggregators are very common in other industries.
*  I came from FinTech. They're like really big in finance for like credit card comparisons, loan comparisons.
*  And I think one of the big questions there was always like, who owns a customer relationship? We'd have to think through like all those things.
*  That's a pretty good rundown. I think the vision would be that folks would sign in almost like an OAuth kind of thing.
*  So you would have a sense of who they are. They wouldn't necessarily be establishing a billing relationship with you immediately.
*  But that would be the point is that friction would be reduced in terms of how the finances work.
*  I don't know. I'm not actually doing this, but the kind of two models that come to mind would be like pro rated based on use,
*  where just all the revenue gets split up and divvied up based on who's doing what.
*  That could be pretty challenging just because what exactly is going on and who's token, what tokens are. It's hard to equate different things.
*  So another version would just be like periodic re-establishing of a certain percentage out of the pie, which is how the cable bundle works, right?
*  Like every year or however often the contracts come up for renewal, ESPN is going to get however much out of your bundle and Discovery Channel gets however much.
*  And that can go up and down depending on how popular those channels are and relative negotiating position.
*  But my understanding is it doesn't matter how much I actually watch any of those channels on a month to month basis.
*  The channels are just going to get what they're going to get from each subscription.
*  But yeah, I think that could be definitely interesting trick.
*  I think Elicit is probably a bit outside of the core target for this.
*  Then again, like it also could be a way to reach a lot of people that might otherwise never even come across the product in the first place.
*  So that's obviously a big part of it too, right? You get in the bundle, you can get discovered.
*  And then a lot of things could happen from there. Again, to be clear, I'm not doing this, but it's become slightly more real recently as somebody reached out to me
*  and said that they actually might want to do it. How about your story of the nonprofit origin to now creating a for profit?
*  How's your board holding up? How's the governance? I'm not sure there's really all that much interesting there.
*  I suppose that the rationale for doing something like this is probably pretty intuitive.
*  But since people are paying attention to that kind of story, I'd be interested to hear your version of it.
*  No, that we don't have 20 different entities. It is, I think the general kind of nonprofit or like even academic space.
*  Even academic spin out to commercial ventures actually like quite common and popular long before open AI.
*  This is common in like biotech and universities have tech transfer offices that help with this.
*  So I think that the idea of doing basic research freely without commercial constraints,
*  then if there's a commercial opportunity separately, like setting up the best vehicle for kind of scaling that impact seems like pretty well established.
*  I think makes a lot of sense to me. We just we got a lot of external advice.
*  We did talk to the open eyes and the anthropics like early last year and have had great like nonprofit lawyers who guided us through that.
*  The former nonprofit is run by an independent board. It was an independent board that kind of oversaw all of those decisions.
*  We were pretty careful to get into like very independent valuations of everything.
*  And I overall really insured that the nonprofit was like significantly better off.
*  And like the original motivation actually like came from our philanthropic donors and like our board.
*  Then like they were the ones who provided that initial impetus. So I think it's I think that like governance wise, I think that was like pretty straightforward.
*  And then I think the other thing that really helps is I would say so now Elicit is a public benefit corporation,
*  which again makes it clear to the world that we we care about impact, but definitely financially, but also just for the world at large.
*  And also we're opinionated about how we're going to make an insane amount of money.
*  Like there are lots of ways to make money. We're going to do the version of it that's like really good for the world in a lasting way.
*  And that's totally possible. And so I think for us, like the all of the different things we care about actually kind of converge really nicely, which isn't always the case.
*  The mission doesn't trade off with financial success for us to be successful as a product. We have to be very accurate.
*  We have to be a reliable, trustworthy product. We have to be good at really complex reasoning. We have to add value for things like research.
*  So like our stakeholders, our financial success, like our mission, all of that is very aligned.
*  So I think actually for us, it was really nice. It feels very convergent.
*  Is there still like a nonprofit team that's distinct from the core product team or is it is the whole kind of team united in the commercial mission at this point?
*  All of the employees moved over to the commercial side and then the nonprofit is just run by the independent board.
*  So they're the ones who are overseeing that.
*  How about your hiring needs? You guys have raised the round. So you've got resources and you're also scaling revenue at an admirable clip.
*  What are you looking for to continue to build the team?
*  Yeah, hiring is really super important to us. As you mentioned, like users revenue, everything is growing.
*  And the most important function right now to me, I guess I'll let Zhang Wen speak for herself also, is senior software engineers looking to get into AI.
*  So not even necessarily machine learning engineers, although we're also excited about those, but people who have deep expertise kind of building a scalable modular well-connected systems using Python TypeScript.
*  Super relevant, both front end, back end.
*  There's like kind of you need to build the machinery for the AI factory on the back end to build the kind of control structures on the front end.
*  And both of these just need people who have been in software engineering for a while, did not just do boot camp.
*  And I think it's a really exciting space. I think the like these somewhat unreliable pieces, you're trying to build reliable robust systems out of them.
*  It also has really high talent density. I think there's people from Google, Stripe, Square, others.
*  So I think it's really exciting and really encourage people to join us.
*  Yeah, I feel like we did a good at covering some of the technical, like both what we've built, what the team has, a very small team, where 12 people has built today.
*  And also all of the challenges and like the really exciting technical opportunities like Exascale running unboundedness and running language models over millions of papers at really high accuracy.
*  Like hopefully all the things we covered today really give a sign of the very exciting technical opportunities that lay ahead.
*  And then on the non-technical side, looking for I'm looking for product designers who are excited about building this, these evaluative and interfaces with language models that again,
*  help the user even if they don't know what they want, even if the language model doesn't have all the information that they need.
*  And also, like definitely looking for people in product marketing and go to market as well as on the eval side of sort, starting to think about hiring data scientists to marry some of the offline evaluations and analysis we're doing with real time evaluation and feedback.
*  I think there's a lot of potential there. So firing across the board.
*  Yeah, I'm really excited to make big visions of transforming research and there's not, there might not be a lot of time left before we really need to make it look like useful for very high stakes decisions and times of chaos.
*  So yeah, hiring eagerly.
*  Cool. That's a compelling pitch. And certainly I can't rule out that we could be entering some choppy waters pretty soon.
*  This has been phenomenal, guys. Anything else you want to touch on before we wrap?
*  No, this was great.
*  Andreas Stuhlmuller and Junghwan Byun, founders of Elicit, thank you for being part of the Cognitive Revolution.
*  Thanks, Nathan.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me on the social media platform of your choice.
