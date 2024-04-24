---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 4829s
Video Keywords: []
Video Views: 1327
Video Rating: None
---

# BI 154 Anne Collins: Learning with Working Memory
**Brain Inspired:** [November 28, 2022](https://www.youtube.com/watch?v=YqCRwJshHlk)
*  Something that's curious about working memory is how limited it is really, right?
*  It's very stupidly limited, right?
*  Three or four items really.
*  It's, you know, like if you're an AI person, you're like, why would I bother?
*  And that's the thing, right?
*  It's like we have this system that has a very low capacity, and I think AI sees that as a bug.
*  And I think it's actually most likely a feature.
*  So I have two answers to this.
*  This is Brain Inspired.
*  Welcome to Brain Inspired. It's Paul.
*  Reinforcement learning has been one of the greatest success stories tying together brains, behavior, and artificial intelligence.
*  Long ago now, reinforcement learning algorithms that were developed in computer science were imported into neuroscience to account for the brain activity associated with how we learn.
*  Since then, a wide variety of algorithms and computations underlying various forms of reinforcement learning have been explored, along with the neural substrates possibly implementing those algorithms.
*  However, our brains are highly complex entities.
*  And as we've discovered more about learning, the story has become more complicated.
*  It isn't clear how and when various brain activities map onto various particular equations used to describe how we learn.
*  And people like Ann Collins, my guest today, are showing that reinforcement learning isn't the only game in town in terms of how our brains learn.
*  Ann is a professor at the University of California, Berkeley, where she runs her computational cognitive neuroscience lab.
*  One of the things that she's been working on for years now is how our working memory plays a role in learning as well.
*  And specifically, how working memory and reinforcement learning interact to affect how we learn, depending on the nature of what we're trying to learn.
*  So in this episode, we talk about that interaction specifically.
*  We also discuss more broadly how segregated and or how overlapping and interacting many of our cognitive functions are and what that implies about our natural tendency to think in dichotomies like model free versus model based reinforcement learning, system one versus system two, and so on.
*  And we dive into plenty other subjects like how to possibly incorporate these ideas into artificial systems.
*  You can learn more about Ann in the show notes at braininspired.co.
*  Slash podcast slash 154.
*  Thanks to the brain inspired supporters.
*  You people are the best.
*  And it's just so generous of you to take the trouble to send a few bucks my way each month to help me make this podcast.
*  And I always look forward to our live discussions and our interactions.
*  Thank you.
*  All right. Here's on.
*  I know that you're not at SFN right now, the annual neuroscience meeting.
*  And in fact, this our discussion here is, I think, over a year in the making, because I'd asked you so long ago, but you had decided to go and procreate apparently for the third time.
*  And you were telling me that that's that's why you're not at this annual neuroscience meeting.
*  So but I thought maybe that was your first child.
*  So I was going to ask you, you know, what it was, you know, how motherhood is going to be.
*  But you have three.
*  Yeah.
*  Yeah, I have three.
*  They're five and a half, three and a half and six month old now.
*  I'm not going to lie.
*  Motherhood is rough with a career, especially if your partner has a career, too.
*  Actually, with my first child, my husband wasn't quite working.
*  Full time. Yeah.
*  And so we were able to travel and go to lots of conferences and stuff like that, which makes for some really interesting memories of, you know, being at SFN with a baby in the pouch and stuff like that.
*  But yeah, I think the combination of having the other two having full time career and having a career is really interesting.
*  Are you done? Are you going to keep going?
*  I stopped it too and I have a surgery to prove it.
*  That's a bit too much detail.
*  I have a little bit of a problem with my
*  I'm one of six children.
*  So people like feel like they can ask me this question.
*  I'm actually the fifth of six children.
*  But no, I don't think so.
*  I think, you know, like it's already pretty, pretty hard enough at this point.
*  And, you know, I have three girls.
*  They're very lovely, but they're also a handful.
*  All right. Well, I'm glad that we're finally doing this.
*  So I appreciate you finally coming on to the podcast.
*  It was a lot of emails back and forth in the making.
*  So the persistence. Yeah, I am persistent.
*  So we're going to talk a lot about today about your work relating reinforcement learning in the brain to working memory.
*  And hopefully we'll talk a little about a little bit about attention as well.
*  But I wanted to start by asking you, since you have, you know, you've worked a lot on the interactions between working memory and reinforcement learning.
*  I wanted to start by asking you just how you feel, how you would describe your outlook or your conception of learning and reinforcement learning has changed or been shaped throughout your career.
*  Can you describe that that sort of projection?
*  Yeah. So, you know, I, I thought about it since you kindly sent me the questions to prepare a little bit.
*  And I that's the question I had the hardest time with actually, because I got into this field not in a traditional way, not that I think many people, there's no traditional career there.
*  But I think in France, it's maybe at least when I was there, it's maybe even less traditional.
*  You know, there was no undergrad in anything close to cognitive science.
*  I discovered cognitive science as part of of my breadth requirements in engineering school, you know, alongside with, you know, painting and music and stuff like that.
*  So it was really I was in a very STEM oriented undergrad.
*  And, you know, like this field was considered very outside of scientific rigor.
*  And because of that, I think I've had this approach that like I dove into problems and didn't have much breadth or or height of view either.
*  And immediately saw that learning was fairly complex.
*  And throughout my career, essentially, that's been pretty much confirmed.
*  It's there's no like it's complex and.
*  Is it complex or complicated?
*  Both, probably.
*  Yeah. Yeah, I think it's both.
*  Really. I was pretty lost at the beginning.
*  I feel like we're still in the middle of the process of learning.
*  I was pretty lost at the beginning. I feel like we're still pretty lost.
*  And also, I felt from the beginning that there were, you know, many chunks to it, which I think maps to the complex part.
*  And and I'm still pretty convinced of that.
*  So so it hasn't really changed much. It's just, you know, like become more defined in a sense.
*  So a lot on this podcast, we've talked about this current trend of reducing the dimensionality of like neural activity.
*  Right. And then describing these lower dimensional manifold states that kind of you can start mapping on the cognitive functions.
*  But what you're saying is that learning is high dimensional.
*  I mean, how high dimensional is learning and and do we need to keep it at a high D level or are there dimensionality reduction techniques that we can use?
*  I mean, for instance, reinforcement learning also just has turned out to be a complicated affair also.
*  Right. So we call it learning. I guess that's the lowest dimension that we can term that we can use.
*  But in your in your have you thought throughout your career that it is even more complex than you originally thought?
*  Or have you been able to sort of take some of those chunks away and hone in on what you think are fundamental principles?
*  Yeah, so I I've gone more the direction of more complex than less complex.
*  And I think that's my undergrad major was in theoretical math.
*  And I think lots of people in this field come from math or physics and have a bias for elegance and, you know, like, you know, unified theories and unified theories are wonderful and shared principles and stuff like that.
*  And I think if there's room for that in the brain, but I think I think we're probably too much in that direction in the theory of cognition.
*  I think I think it's more messy, you know, than we might like for an elegant theory.
*  So I so I do think it's it's high dimensional.
*  But for your question as to whether I've been able to take out some chunks.
*  Yeah, I do think there are shared principles and maybe not shared principles, but shared computations.
*  And and I wasn't sure if I should count that as a different dimension or not.
*  Right. If you're doing the same computation, but apply it to different things in a sense algorithmically speaking, it's the same principle.
*  It's the same dimension, but it results in a behavior that is differently dimensional or more complex.
*  And so I think it depends a little bit how you look at it.
*  And I think, you know, like the the trend in looking at the brain and, you know, taking manifolds and seeing their dimensionality and stuff like that tends to apply more, I think, to representations than to changes in representation.
*  So I think there are different dimensions, which is learning, you know, like computations by themselves.
*  So I don't think it's easy to define the dimensionality of computations, which I think learning is.
*  Yeah, sorry, that's a bit rambly.
*  No, that's OK. I mean, I'm trying to grapple with the sort of the different levels that we talk about and the dimensionality.
*  And then there's what happens in the brain, like the the quote unquote mechanisms and computations in the brain.
*  I just had Michael Anderson on to talk about his neural reuse and and ideas and thinking about going away from thinking about modules in the brain and thinking more in terms of interacting brain areas and how that how the interactions there are different players for different cognitive functions.
*  But those like the same brain area will get reused.
*  And you were just mentioning, you know, if you're using the same computations in different areas, whether we should consider that, you know, a different a different dimension.
*  But I don't I don't mean in different areas. I mean, really.
*  So I think of something very specific, which is the corticobasal ganglia circuits.
*  So there's loops that go from cortex to striatum to the output of basal ganglia through the thalamus and back.
*  And I think it's an example where we have, you know, a decent idea of what computation or transformation those loops do.
*  And we know that there's multiple of them with different starting points in in cortex.
*  Right. And so I think that's an example of, you know, not intra region computations, but like a network that's making a computation or at least has a some kind of algorithmic function or information transformation function that can be applied to different things, which may lead to fairly different consequences on cognition behavior.
*  Yeah. Well, part of what we're going to talk about is maybe not the computation itself, but the idea of, you know, adding a working memory component to a reinforcement learning algorithm. Right.
*  And you do that when then a computation. But yeah.
*  But then, you know, there are other cognitive functions like attention, et cetera, that maybe you're going to eventually throw into the equation.
*  And would that mean would that be a different computation or, you know, I'm trying to think about how to think about adding terms to an equation. Right.
*  And calling it a computation. Does that change the computation? Do we think of it as one computation?
*  What I was going to ask about is, you know, the modularity of the brain is giving way to like interacting brain structures and like the basal ganglia cortical thalamus, thalamic loops, you know, that you were talking about.
*  And I'm trying to think, you know, do we need to think of computations as modular or, you know, or as high dimensional?
*  You know how messy computations are clean and the brain is messy. Right. How do how to reconcile those two things?
*  Yeah, I don't have a good answer. But the way I think about it again is, um, is, um, as a Taylor expansion.
*  Or like I said, I didn't. But, you know, like essentially we're we're we're doing this thing right where we we're trying to understand some aspect of cognition and, you know, if you have a brain and.
*  And, you know, like we start with, you know, like a point approximation. OK, like maybe learning is like behaviorists or, you know, like cause and effect or something like that.
*  And then we're we'll go OK, well, actually, it's a bit more complicated than that. Let's you know, let's approximate the function with a line.
*  And, you know, you have to, you know, to to to degrees of freedom. Right. And then you could add a third one, et cetera.
*  And it's a little bit like that, that I think about it. It's, you know, at first approximation, you know, like it was OK to capture lots of learning with just the delta rule kind of model.
*  But then you dig a bit deeper, you know, and and I could tell you how I got into working memory if you're interested.
*  But, you know, and you discover you have to add working memory.
*  So now you have reinforcement learning and working memory and their independent modules, you know, that just that just makes for output.
*  But they're independent. And then, you know, you dig a bit deeper and you discover, well, actually, they're not independent modules that kind of like have an impact on each other.
*  And so you have to add that to the mix, et cetera. And to me, that's the third order.
*  And to me, that's the third order. And, you know, and and it's not the third order in the sense that it's less important or less true.
*  It's just the third order in the sense that you can't really get to it until you've gone to the second order first.
*  Like you have to identify them as potentially independent modules before you can even start thinking about how they might be interacting.
*  And so I agree with you. It's kind of tough because I don't think any brain region works on its own.
*  But I still think we can try to isolate, you know, like first order kind of question.
*  Computations they do that will help us understand how they talk together, how they and without having to assume that they're independent.
*  Well, yeah, so the cognitive functions and the brain areas and those are two separate things, obviously.
*  But is this is a well, maybe you'll have an answer to this is working memory a thing or is it working memory RL like your model?
*  Right. Like your model just lumps them together and then maybe that's a separate thing.
*  Or how do where are the the bright lines between cognitive functions? Right. If they're interacting.
*  So there's interacting is like two different things, but they are interacting.
*  Or we could consider that interacting system one thing or, you know, so it's working memory a thing.
*  Yeah, I think it's a thing. So I think I think it's the animal researchers who have the answer there.
*  You know, I think it's a thing on its own. If if you kill one, the other one can still work.
*  Right. So I think if somehow you were able to, you know, just take the approximation of my reinforcement learning and working memory model without interactions,
*  I think if you were able to cancel out working memory, you would still be learning just fairly slowly.
*  And if you were able to turn off reinforcement learning, you would still be using working memory to do something that looks like learning.
*  It would just have a fairly different characteristic behavior.
*  So I think the legion of sense of like, if you take it out, does it still work on its own?
*  Is the sense in which you can say, well, it is a thing, even if it's deeply enmeshed with something else.
*  But in the brain, you would have to lesion a particular area and then tie that thing to a particular area.
*  So so then it's still not clear how to go from the level of, you know,
*  the implementation level in the brain to the cognitive function level that we have named in psychology, for instance.
*  Oh, I completely agree that it's very non-trivial to do that mapping and that that's a lot of work.
*  That's an enormous amount of work to be done to do that mapping.
*  And that goes through, you know, taking multiple approaches, you know, cross species, cross methodologies.
*  I fully agree. You'll stick with humans, though.
*  You know, I collaborate with with people. I definitely won't do non-human research myself.
*  I'm not qualified, but I'm but I'm very, very happy to collaborate with, for example,
*  Professor Linda Wilbrecht here at Berkeley and all this elsewhere to try to bridge across species.
*  All right. Let's back up and talk about reinforcement learning itself a little bit more before we bring in your work in with working memory.
*  I've written about the and other people have written like Nathaniel D'Az about the dichotomy of model free versus model based reinforcement learning.
*  And, you know, these are were thought to be totally separate cognitive functions and in the brain, et cetera.
*  And and now it's not so clear. So maybe I'll just ask you, you know, what is your view?
*  And there's a nice review that I'll point to that you've written about this dichotomy.
*  What is your view on model based versus model free reinforcement learning?
*  Are are they two separate things? Are they interacting? Are they one reinforcement learning thing?
*  How should we think about that? Yeah. And I mentioned Jeff Coburn with with whom I wrote this review.
*  So the title of the review is Beyond Dichotomies. So I think that that tells you a little bit.
*  Maybe just for for listeners sake, I guess you should describe model free versus model based.
*  Sometimes I don't forget to do that. Yeah. Yeah. So model free reinforcement learning is this approach where you assume you integrate the information of about reward you've received for a given choice over time.
*  And you summarize it into a single cash value. So you say, like, if I go to this restaurant, in average, it has an expected value of point eight.
*  And then you have a model of the world that tells you if I do this action, I expect to be in this state after that.
*  And you have a model of the outcomes, which tells you if I am in this state, I also expect to experience this kind of model free reinforcement learning.
*  And you have a model of the outcomes, which tells you if I am in this state, I also expect to experience this kind of valence and that you use this information in an effortful way to plan your choices.
*  And so like, oh, if I go here, I expect the restaurant to be open. But I know that on Mondays, they don't have my favorite food. So I actually don't expect it to be that good or something like that.
*  And you combine that and you compute on the spot what the value is. So it's obviously super popular framework model based versus model free.
*  And it's resonates a lot with the whole thinking fast and thinking slow. There's a whole history of psychology around dual systems like this.
*  And everybody likes it. I think for that reason, people think of it also as relating to habits versus goals.
*  Automatic versus effort. Yeah. But yeah, we love dichotomies.
*  We love dichotomies. The short story of our opinion paper is that while this is a very productive framework, it's also very oversimplified.
*  And she said she's going to have to wave like that every few minutes for the lights to come back on. Sorry to interrupt.
*  I mean, a green building turns off lights often and I don't move enough when I talk.
*  So I don't mean oversimplified, but I think it's I think it's it's approximating things.
*  And everyone who works directly in this field knows what those approximations are.
*  But because the framework is very seductive in a sense, it's you know, like it's a mathematically well-defined model that seems to map on well to many, many heuristics we have.
*  It's been taken a little bit too seriously, I think, by people who are less familiar with the details of where it can go wrong.
*  And I think it leads to it can potentially lead to very big issues of overinterpreting the findings and over and also leading you down wrong avenues of research.
*  So I'm happy to say more about that. Yeah, yeah. You know, if you want more details, but yeah, give me more details.
*  I have a follow up question as well. So. Okay.
*  Well, I think, for example, that you can make a reasonable case, you know, like for the model three computations in the brain, I think, you know, like there's been a lot of work around this.
*  We have a good sense of a network. So to me, more free, I can accept that it's it's it's a meaningful chunk of learning behavior.
*  This was a lot of free months. Sorry, model free was the first kind of reinforcement learning discovered in the brain based on. Yeah.
*  Yeah. In a sense, you could consider it the most the basis level of automatic learning or something, perhaps.
*  Well, that's the thing is like, I don't know that that's true. I don't know that it relates to habits. I don't know, at least directly that it maps onto habits. I don't know that it maps onto automaticity.
*  I know that lots of behavior that's well described by model free like models is not, you know, this kind of implicit effort, less automatic kind of process.
*  So I think there's a bit of difficulty in mapping it to more, you know, broader concepts like this.
*  But but but I do think it has the benefit of, you know, like, at least we have a good hypothesis for where and how it might be implemented in the brain.
*  As far as model based goes, I think it's both too much and too little.
*  Say more.
*  Yes. So it's too much in the sense that I don't think it's a thing. I think there's too many components in it for it to be thought of as a thing.
*  And there's many things you could say about that. But the simplest one is to say, well, you know, there's the planning component, the planning component requires, you know, like, either simulating things and holding them in working memory or doing it some other way.
*  Maybe, you know, we have some approximations like I'm sure you've heard others.
*  But then there's also learning the transitions or, you know, like representing the reward function.
*  So so I think there's multiple sub components of it. And so thinking of it as a chunk doesn't seem right.
*  And the second thing I was going to say is that it's not enough in the sense that we often read, you know, even in very prominent journals, even in the abstract, something saying like learning is well known to be either more free or more base.
*  And I think that's a big, big problem to say something like that.
*  It's that there's many aspects of learning that are not to be put into either of those two bins. And that should go beyond.
*  And if only because, you know, more free and more based are focused on this on this type of environments where sequence is more or less the same.
*  Yeah. So so model based is too much and not enough. And it's not a thing. And model free is a thing.
*  So what is that? Like, how should we think? It's more likely to be a thing. It's more likely to be a thing.
*  OK, so probability of point seven because it's not a thing.
*  It's not a thing. And model free is a thing.
*  So what is that? Like, how should we think? It's more likely to be a thing. It's more likely to be a thing. OK, so probability of point seven being a thing.
*  OK, well, I was going to ask you then how how should we think of as opposed to a dichotomy? How should we think of like the gradient or transition?
*  Is it just piling more cognitive functions necessary? What we what we call model based is I guess we could continue to call it model based, but just realize that it is comprised of lots of different elements, perhaps.
*  Yeah, so it's this question of, you know, if you imagine you have if you imagine learning as a high dimensional space and you imagine you have the model free dimension here and you have model based.
*  And I think essentially that model based is not a single dimension. It's a, you know, like scatterplot. It's a manifold.
*  Yeah. And the question is, the question is, what's what's what are meaningful dimensions that we want to consider out of this? And I think and what other meaningful dimensions are there around around this?
*  And I think people kind of agree that more freeze one meaningful dimension in that because we can somewhat isolate it.
*  But I think in model based, it's less clear. And so I think the way forward is to say like, OK, what are, you know, like the key core ingredients that can be isolated that then get mixed together to support learning?
*  Is there a better term than model based then?
*  How do we destroy the dichotomy? How do we correct the dichotomy in words?
*  I mean, I think I yeah, I think words are important and in particular, not not equating things that are known to not be equated.
*  I think, for example, that is dangerous to equate more free to habits. It's dangerous to equate model based to goal directed.
*  I don't think that's a one to one mapping in any way. And I think, you know, prominent model based model free people would agree with me.
*  I'm not I'm not picking a fight. I haven't discussed with people here.
*  It's it's it's more of the way we approximate what we say in papers, really.
*  So I don't know what the right wording is, but I think we need to.
*  And I think a strength of computational models is that you can you know, you can say exactly what you mean.
*  But the problem is when you put, you know, like when you take the model based equation, it doesn't mean goal directed.
*  Right. It just means like here's the way to compute for the plan.
*  Yeah. OK, so maybe maybe we should talk about working memory in its relation to reinforcement learning.
*  I think of it. Do I have it right that the working memory and reinforcement learning that you study that you research as interacting, you would that would be model free reinforcement learning.
*  Right. Yeah. So so far anyway.
*  You could call it more free or you could call it more based.
*  Well, is the interaction between the model, the model based component or is it even individually?
*  I think I think because so here's the thing, right.
*  It's like if the choice you're making only constrains what reward you get, not what the next stimulus is or next stage you are in is, there's no way to distinguish whether you're doing model based or more free error in the classic sense.
*  Right. And both models make the same prediction.
*  In that sense, that's why I'm saying I'm like I can't project it onto those two because, you know, they're making the same prediction there.
*  So they're collapsed. Really.
*  That said, obviously I do think that working memory bears more resemblance to based the model free in the sense that it is something that we think of as a fruitful, more cognitive, more, you know, more flexible in the same way that the model based processes.
*  But but yes, you know, the behavior we're looking at would have been modeled by the simplest model possible as a as a more free arrow.
*  Yeah. Okay. Okay. Let me see if I can just describe the sort of overarching conclusion or story that you have that you continue to work on, but that you have thus far come up with regarding the interaction between working memory and reinforcement learning.
*  So, and then you can correct me and then but before that I have a question about my own cognition. So if you give me something hard to do, like it taxes my working memory, right, then when I make an error.
*  There's a, it's a, it gives me a large prediction error.
*  And therefore, I actually my reinforcement learning system then is allowed to learn fast.
*  Whereas if you give me an easy task that doesn't require much working memory, then when I make an error, it leads to a smaller reward prediction error.
*  And that actually makes my reinforcement learning system.
*  Learn more slowly.
*  Right. Okay. So that's my summary of it. So that's nearly right.
*  It's nearly right, but it's not because it doesn't require much working memory.
*  It's because it's easy for you to use your working memory on this task.
*  So if it's easy for you, you can use working memory.
*  Oh, right. Okay. It's, it's, there's a lower bar to actually using my working memory to perform the task.
*  Right. So it's easy. It's easy to hold. You can easily retrieve it.
*  And so you're using working memory for it. And that's what's creating the interaction.
*  Okay. Okay. So my question about my own.
*  It's a bit of a.
*  Yeah. Yeah. Yeah. Sorry. It's subtle. Yeah. Sorry. Thank you for the correction.
*  So, so my question is, I'm a.
*  Sadly, I'm a really slow learner, but I think I have high working memory capacity.
*  Maybe it's easier for me to use my working memory.
*  And so is that why I'm such a slow learner? Because I'm always just using my working memory.
*  Do I need to back off and try to use my reinforcement learning more? What do I need to do? How do I learn better?
*  So I have two answers to this. One is if you believe that my theory.
*  Generizes to the real world, then yes, that's what you need to do.
*  You need to do all task yourself or something like that and make it harder for you to learn.
*  And prevent your more explicit working memory like processes from rescuing you, which will enable slower things like error to be less blocked.
*  So you're saying I don't try hard at things. I don't do things that challenge me enough, perhaps.
*  No, I'm not saying that because you might be trying hard to use your working memory.
*  I'm saying you should distract yourself a little bit.
*  And actually, you know, it's interesting how actually well known this is from a heuristic point of view.
*  My voice teacher, when I used to study singing, would make me do all kinds of crazy things to distract me while I was singing.
*  And it would always result in better, better motor learning for singing.
*  So, you know, it's a trick that's known, I think, to educators.
*  And I also discovered a review saying, yeah, go ahead. Sorry.
*  I think it's related, for example, to the concept of space repetition or stuff like that.
*  But we're not supposed to multitask, right? Because then that means we don't perform well on anything that we're multitasking on.
*  But what you're saying is maybe you weren't singing well while you were being distracted.
*  But that led to better singing later. Is that what I should take from that?
*  I think it led to not retrieving the thing that I was trying to explicitly retrieve,
*  which allowed the more implicit system to both make its own choices and its own predictions.
*  And so learn from them. I have no idea, right? This is true. I don't study singing.
*  But that's what the implication would be. Yeah, let's turn this episode into a self-help episode.
*  Those are popular, right? So let's do that. Yeah.
*  Yeah. So that's my second answer, actually. It's that, you know, I think it's important as cognitive scientists to think about applications of our findings.
*  But I also find it very terrifying, especially in my domain where I study learning.
*  Especially because I studied in a, you know, because I try to deconstruct learning, I try to study it in a very well controlled kind of environments that are not readily generalizable to the real world.
*  And I very much worry that people will do exactly what you're saying, is like, take my theory and assume it generalizes to the real world and apply it.
*  And for all I know, it could lead to the opposite effect, essentially, because of this Taylor expansion, the game thing, right?
*  Because I'm trying to deconstruct it and I'm going step by step, but it's possible that orders three, four and five might flip around.
*  Because it's a complex system. I've seen so far. Yeah. Exactly.
*  What do you think then, and I'm sorry this is an aside, because there are a lot of neuroscientists who do make life recommendations, right?
*  And take from their work lessons for behavior.
*  And I know that that's the ultimate goal. But are you skeptical of, say, a scientist who tries to make that transition into, you know, a life coach advice person?
*  I won't make a broad call on this.
*  I think it's probably fairly dependent on the specifics of what you study.
*  You know, essentially, the question is how generalizable, how much evidence do you have that the findings you have in the lab are broadly applicable to real life?
*  And I think plenty of people ask this question, right? And plenty of people, you know, take lab experiments and try to relate them to real life outcomes in some ways, or try to apply them to more naturalistic experiments, whether that's, you know, like, I don't know, I saw a recent paper, I think by Ross Otto's team looking at choice of pizza online or something like that, you know, and try to see like, OK, those principles we've developed in the lab, like, do they apply to real life outcomes?
*  And try to see like, OK, those principles we've developed in the lab, like, do they explain things also for more real kind of decisions?
*  And so if you have done this kind of homework and are able to say like, well, the principles I derived are generalizable, then sure, maybe you have the expertise needed to do that transition.
*  I personally, in my specific domain, don't feel like we're there. And so I personally would be very worried about doing that jump, especially because I think, you know, the people who ask for this kind of advice tend to be vulnerable.
*  You know, people who want to improve might have needed to improve in a sense. And so I, you know, I would not want them to be my guinea pigs on that.
*  Yeah.
*  So, well, since you said you're not there, A, do you have an interest in getting there? And B, how long do you project?
*  Where you would feel comfortable?
*  I have an interest in getting there.
*  I confess that I'm, my primary interest is really fundamental research.
*  Does that mean understanding the phenomena?
*  Yeah.
*  Yeah.
*  Yeah, that's my primary interest. But I do have a genuine secondary interest in making this something useful for society.
*  Yeah. Well, I mean, you've studied this in the context of schizophrenia, I know, and you know, so disorder. So you are applying it in that sense and linking it to behavior.
*  Absolutely. Yeah, yeah, yeah. And I do think, you know, I mean, maybe something that I'm even more interested in than, you know, computational psychiatry might be education, actually.
*  Because I think, you know, I think there's lots of individual differences in how people learn. And I think, you know, if we understood things better, we might be able to help more there.
*  But I definitely think that's somewhere where we have to be very, very, very careful because the impact on individuals, individual individuals is, you know, could be very big.
*  So we need to really understand these positive or negative directions.
*  Yeah. Okay. So you so it could be initial conditions and applying some diagnostic or some procedure could lead to to, you know, widely divergent results.
*  Exactly what you said, right? Like if I go and take like a class of, you know, third graders and tell them to and dual task them, you know, for the whole day because I think they're going to learn better.
*  And then I discovered that actually the impact of like, you know, of being told us the whole day is that they lose all their motivation and they stop learning.
*  And, you know, so maybe they're eating that better. But the like downstream impact is completely different from what I thought. It's like, well, you know, like, how ethical was this experiment?
*  Well, you have your children. Do you think about that with your own children? Do you apply this behaviorally to yourself and or and we're going to talk more about what this is because, you know, the relation between working memory and reinforcement learning.
*  But has it altered your own behavior regarding the way that you go about trying to learn things and or teaching things to your children?
*  I mean, I definitely think about it. It hasn't really. I wouldn't say it's altered it per se, but it makes me consider things.
*  I do a lot of Duolingo.
*  And I see this.
*  You have to say Duolingo. Oh, sorry. Yeah. Oh, I thought that was well known. Duolingo is an app for learning languages.
*  I'm a very multilingual family. So anyway, I'm using that to to one languages.
*  But I've definitely noticed the, you know, like the few times when the algorithm messes up and repeats the same sentence twice in a row, it feels very obvious that I just, you know, like, repeat what I just memorized.
*  And that does not help me store that information. Well, like it's that it's in your working memory still. I mean, yeah, exactly. Yeah.
*  Okay, which, which, which makes me likely to get a point right now, but makes me much less likely to do well, you know, when they ask me again the next day. Okay. Well, since since.
*  Okay, so we just said working memory or I did. So, so I guess the conclusion thus far.
*  And you can tell me any new conclusions that you've had recently or are on the verge of is that working memory is actually contributing to reinforcement learning in your brain by contributing to the reward prediction error.
*  Did I say that correctly?
*  Yeah, yeah, and specifically to the expectation of the outcome. So the reward prediction error is the difference between the reward we get and the reward we expected to get.
*  And what we think happens is that if working memory allows you to say, oh, I know what to do right now. It can also allow you to say, oh, I know that I should expect a reward for doing this right now.
*  And so that instead of getting the expectation of reward from the reinforcement learning system, we get it at least partly from the working memory system before the reinforcement learning system has learned it.
*  So that makes the reward prediction error smaller and that slows down learning.
*  So then classically working memory is thought of as the sort of online short term storage and manipulation of information.
*  Would it be proper then to say working memory is also a learning mechanism?
*  Yeah, I think it is. Yeah. You know, I think that words are complicated.
*  No, words are easy. Their meaning is complicated, right?
*  That's true. Yeah.
*  Yeah. It's so, so no. OK. You can't call it a learning system in the sense that it's not it's not going to be long term, but it is a learning system in the sense that if you are in a dynamical environment where you're obtaining information and making decisions as a function of this information,
*  then working memory contributes to managing that information and helping you make decisions better and better.
*  So, you know, you pick what you call learning. OK. Right. But to me, it's a very clear player in the learning environment.
*  So I was trying to think of an example and let's say you're trying different.
*  I think you said pizzas earlier or restaurants. Let's say you're trying different pizzas. Right. You have a you're in a taste testing competition and you have five different types of pizza.
*  And your job is to. Learn or maybe we could say decide or learn, you know, which which is your favorite. Right. So then you have to taste one year salty and cracker.
*  But then you have to think, you know, OK, OK, that one's pretty always pretty good. And then on down the line with five. Did you then learn what you prefer?
*  Because that would be keeping it in your working memory. Right. And that would probably be called learning.
*  And I apologize if I'm taking us down a meaningless road here.
*  I'll follow your example. I think it's probably the timeline is probably a bit beyond what working memory would be doing, but that's OK.
*  I don't think in the end what you have learned would be in working memory, but I think working memory would have contributed to the process of learning.
*  But then what you have learned is called memory and not and not learning. Right. So the learning is what I'm asking about, because you because there is a difference.
*  Learning and memory are always associated. But the learning is the story is is the process by which one is stores. Right.
*  Sure. So then it is part of the process. Yeah. I don't know if everybody would agree with you that learning is just the process, not the outcome.
*  But I agree in that case, if you see learning as the process, then certainly, I think I think that that working memory is an important part of the learning process.
*  OK, so you've established that working memory memory contributes to reinforcement learning.
*  And just going back to the idea of the anti modular brain, all the brain areas are interacting, all the cognitive functions seem to be interacting.
*  So does reinforcement learning itself also affect working memory? Is it? Do they go back and forth?
*  Yeah, yeah, absolutely. I actually also wrote a review recently with a postdoc in my lab, Aspen, you where we tried to show that it's bi-directional.
*  And I think that's actually better known. I think there's been for a long time a bunch of, you know, of computational models that show.
*  So it's this idea that, you know, reinforcement learning helps you learn.
*  We tend to think of it as, you know, learning concrete actions or concrete choices like between A and B or, you know, press this key or that key or, you know, like turn right or turn left or something like that.
*  But there's been for quite a while now this idea that you can apply reinforcement learning to more abstract inner actions, like deciding to store something in working memory or deciding to get something out of working memory.
*  And there's a bunch of models, including Michael Franks and Randy O'Reilly's and others, you know, making good cases for this and for why it would be useful and for why reinforcement learning processes might help you, you know, learn how to use working memory in that sense.
*  All right, so we're going to throw another one in the mix here. I just had Carolyn Jennings on the podcast to talk about her philosophical account of attention.
*  And so she has this view that attention is at the sort of whole organism level based on the, it's the prioritization of just the mental prioritization by a subject or a self.
*  And so, of course, like, well, maybe not working memory, but attention, you can talk about it at the whole organism level. You can talk about it as the thousands of different cuts you take visual, spatial feature, endogenous, you know, top down, bottom up.
*  So the question is, you know, what's the difference between attention and working memory? Because it seems from like non-human primate studies, everywhere you have a readout for attention in a neuron, there's a readout for working memory as well.
*  And it seems like they are inextricably intertwined. So I want to throw attention in the mix. And how do you distinguish between attention and working memory? And then what do you think about the effect of attention on reinforcement learning and its interaction with working memory?
*  And we'll stop at three because it gets unwieldy.
*  Yeah. Well, you know, you could you could go beyond for sure. But yeah. Yeah. So I think attention is essential. And I think...
*  Is attention a thing? Yeah, I mean...
*  Working memory is a thing. Is attention a thing?
*  Yeah, no, I think I think they're separable things, although I do think that, you know, there's a big overlap between working memory and attention.
*  And I think, you know, attention is also a term that is not necessarily defined the same by different people. Same as working memory. So I want to be a little bit careful there. I'm also less of an expert in attention than working memory. So I'm treading a little bit lightly here.
*  But I think I want to... I want to show two ways in which I think attention or working memory can play a role in reinforcement learning that are separable. And then you tell me if you think that matches to two different things on.
*  So I think one way we've talked about is working memory is just holding information in mind. Right. So in my example, it's when you learn, you like, you know, like you, you, you, for example, see a stimulus, make a choice, get a reward, and you just hold that in mind.
*  So like, oh, I got one point when I pressed left when I saw a red triangle. And so that's good. So I'm going to hold in mind to press left for the red triangle. So that's that's one function that working memory can have is like active hold in mind of something that you've constructed internally.
*  This policy, then that that you can reuse and that is useful for learning. Separate role is filtering. So if you think about it, reinforcement learning processes, they assume the state space and an action space.
*  And state spaces in the real world are, you know, approximately infinitely high dimensional. It's, you know, the number of pixels in on your work now, or, you know, it's very high.
*  Yeah, but at any given time, only a very little bit of this matters. Right. And if you have this super high dimensional input, then there's no way you're reinforced learning system in the brain can learn anything about it. Right.
*  And so it has to be fed some kind of state in action that's much lower dimensional to be able to learn at any reasonable rate. And so I think a critical role of attention in interaction with reinforcement planning is to provide that state space and action space over which the computations are going to
*  And so I think a critical role of attention in interaction with reinforcement planning is to provide that state space and action space over which the computations are going to be applied.
*  And so to me that's separable from the other role that I mentioned previously. And it's, you know, as important if not more. But it seems to me like you can see here fairly different functions happening, even though I think working memory does need attention.
*  And maybe this attention component also might somewhat rely on working memory to hold in mind what's relevant. So I, as usual, I don't think they're fully dissociable, but I still think that you might be able to isolate some functions.
*  I fear I'm belaboring a point here, but you know, so there's a filtering. What you just said is there's a filtering mechanism that allows this infinite dimensional space to be filtered down to a lower dimensional space.
*  And in that sense, attention might be necessary for, would you say attention is necessary for working memory? Because working memory is by definition in a low dimensional space, seven plus or minus three or whatever it is.
*  And then depending on the system of working memory you're dealing with, you can only hold a few things in mind, right?
*  Yeah, I think it's necessary in my specific domain. You know, I think there's different types of working memory and actually the seven plus three in my case is more like three or four.
*  Mine's like 12. No, I'm just kidding.
*  But yes, I think it's in this domain, at least I think attention is necessary. But I do know that there's other domains of people who study short term visual working memory, for example, where they show effects that seem less dependent on attention.
*  So again, not my specialty, so I don't want to comment too much on that.
*  Do you have plans to study attention and how it interacts with working memory and with reinforcement learning? I mean, I was referring to that. I think it was a current opinion piece where you talk about the potential role of attention.
*  Because attention and working memory are both under the umbrella term executive function, and often you use the term executive function and its interaction with reinforcement learning.
*  So is there interest in applying these different executive functions also? Or is there just so much to do with working memory itself that it's going to keep you occupied until you're ready to tell the world how to behave?
*  Yeah, no, I'm looking into it. Although I think there's been very nice work done already on attention by, you know, by Yael Niv's lab, for example, by Shiva Farashahi and Areza Sultani and by others.
*  But the way I'm approaching it is more less directly from this attention construct and more from this question of, okay, what are the inputs to this reinforcement learning function?
*  As modelers, we've taken for granted what those states and actions and rewards are. But can I try to dig a little bit deeper into what behavior tells us about what states and actions we actually feed into those computations internally?
*  And I think that will inform us onto the how executive functions and attention play a role in reinforcement learning, but not by going directly through the classic attention route, if that makes any sense.
*  So if I model some behavior and or neural activity using model free reinforcement learning or let's not say model based, but the other, some other kind of reinforcement learning algorithm and computation, and it approximates, but doesn't perfectly describe the behavior because it's science.
*  Do I think, do I think, well, that's because the computation isn't really what's happening? Or do I think that it's due to neural variability and noise? Or do I think that there's always this ongoing interaction between the different cognitive functions like working memory and attention, and they're having an effect that I'm just not pulling out because my task isn't right, or I'm not asking the right question, etc.
*  I mean, because all of these things are, it's not like working memory turns on and then does its thing to reinforcement learning and then goes back to its cave or something. All these systems are always constantly interacting.
*  So I don't know, maybe that's too much of an open ended question.
*  No, I think I see what you mean is, I mean, I'll try to give a case example and you tell me if it's representative, right? So in my, the key way in which I can reveal working memory is by having people learn about a different number of things in parallel, sometimes two, sometimes three, sometimes six, right?
*  And that's what allows me really to say, okay, that's working memory and reinforcement learning because people learn at different speeds in different numbers of items and reinforcement learning just can't do that.
*  Okay. So now take an experiment in which you only have one number of things, but you can also use the same number of things to learn about reinforcement learning.
*  So for example, all the time you're learning about four things. I still know that working memory is playing a role, but I also know that I can't use my model to identify working memory in there because it's not going to be identifiable in this experiment because I don't have that leverage.
*  Okay. So one answer is, well, you know, the experiment is wrong. I'm not going to be able to put working memory, but that's a bit frustrating because I might have done this experiment so that I can manipulate other things and, you know, and answer other questions.
*  So the other thing I can do is, you know, still use a reinforcement learning model, for example.
*  But be aware of its limitations, right? And say like, okay, I know in this case that this reinforcement learning model is not only accounting for reinforcement learning process, but also for contributions of a working memory process.
*  Even though you can't tease them out.
*  Even though I can't tease them out. And, you know, just knowing that is already going to limit, you know, the amount of time that you're going to spend on the model.
*  Even though I can't tease them out. And, you know, just knowing that is already going to limit, you know, the errors I make in interpreting my findings.
*  If I find an effect of, you know, symptom X on the learning rate, I'm not going to attribute it directly to the brain's reinforcement learning process.
*  I'll say, well, maybe it's the brain's reinforcement learning process, but it could also be from the brain's working memory process.
*  So I think the, you know, what's important is knowing what you can and can't conclude from your models.
*  And obviously you're going to have different goals in different experiments.
*  So sometimes it's important that you capture as much variance in the behavior as you can.
*  And sometimes it's not.
*  And what's important is transparency, I think, around that.
*  Yeah, but we have to interpret in our conclusions, which is sometimes perhaps the least enjoyable part.
*  Perhaps. I don't know. That's a question. Is that in some sense, it's the most fun part, right?
*  Because you really want to understand. But then maybe that's where your least one, maybe least confident is in or should be least confident is in interpreting the results.
*  Yeah, I mean, it's the riskiest part in a sense. It's where you like, you know, put yourself on the spot to a degree.
*  And it's the process of science. I think it's where you can generate predictions in the sense, right?
*  Saying like, well, you know, this is risky. This is how I'm interpreting it.
*  And either I'm convinced that my results fully support this conclusion, in which case I need to make that case, or I'm not, in which case I need to state how I would strengthen this.
*  You know, say like, well, if that's the case, then I should also see this in that and it could be tested in this way and that way.
*  You know, I'll make a shout out to this nice paper by Palminterie, Viard and Kuclen, you know, that made the case for falsifying models.
*  So not just, you know, fitting models and saying that quantitatively they fit better than another model, but also saying that they make qualitatively different predictions than other models and that those qualitative predictions are born out.
*  And that's very task dependent, like you said. It's like you need to design the tasks that will answer, allow you to get the models to give those answers.
*  Do you think that it's a better career move to just make wild claims and strong interpretations?
*  So I've said this before on the podcast that when I was interviewing for a postdoctoral position, the faculty member that I was interviewing with said when he was a postdoc, his advisor told him to just say as much crazy shit as possible.
*  And eventually either something will be true or either way it'll get a lot of attention.
*  I don't know what to say. I mean, I'm not very good at this. I think I'm not a very good marketer.
*  Right.
*  And unfortunately, I think you're right. You know, I think overstated claims get attention and in particular get editors attention and get past desk review.
*  You know, they get past this projection.
*  Yeah. And so I mean, there's research on this, right? It's not just my impression, right?
*  It pays for individuals' careers. I don't think it pays for science, though.
*  I mean, I feel like I've seen lots of people follow through research directions that, you know, like I told them I thought were wrong.
*  And, you know, they spent two years in it and then, you know, they're like, oh, I guess I can't identify that model in this experiment.
*  Sorry. So I would not recommend doing that. But unfortunately, you know, we live in an ecosystem, right?
*  Right. You're never supposed to admit when you're wrong in our ecosystem.
*  You get elected president of the United States when you never admit that you're wrong. So I don't know.
*  All right. We'll move on. Go ahead. Go ahead. If you want to comment, go ahead.
*  No, I mean, it's very unfortunate, I think, that there are very strong incentives to, you know, to make too big claims to the system.
*  I think it's bad for science. So I wouldn't encourage anyone to do that. But at the same time, you know, I recognize the strength of the incentive.
*  Speaking of saying crazy shit, you want to talk about artificial intelligence for a few minutes?
*  If you want. How's that for a segue?
*  So, one of the, you know, one of the reasons why I wanted to talk about your work about, you know, working memory interacting with reinforcement learning, and then the broader picture of cognitive functions interacting and how it's a complex mess.
*  You know, I'm wondering if there are lessons that I'm not sure how much you know how much you're into the artificial the deep learning world and artificial intelligence explosion.
*  I'm wondering what lessons we can draw from work like yours that is, you know, peering into the interactions between these, because, you know, I know that there's a lot of attention being added to artificial networks and the attention and transformers we don't we can skip over.
*  But there are other forms of attention that are being added to deep learning networks that are improving them in certain ways, making them more biologically realistic and you know, not that AI cares about that the AI world.
*  But, you know, do you have advice or just in the broader scope of things, are there lessons to be drawn from this? So one more I'll add one more thing.
*  You know the idea of like you have your equation right your reinforcement learning working memory equation.
*  You know, is it right to just cleanly add that equation into an AI system and then say well now we've put working memory into it.
*  Or, like, do we need to understand all these interacting cognitive functions and their quote unquote mechanisms to implement them. I mean, how far do you think AI can get by just putting a clean computation in an algorithm.
*  Eventually they're going to have to interact right to get real intelligence. Do we need all those all the components. What are the components, what what what is there to glean from this kind of work.
*  Thanks for the question. Yeah, so I do follow AI although I don't think anyone can follow it.
*  Or neuroscience of attention or working memory or any of them. Yeah, yeah, yeah, but AI is pretty particularly crazy these days.
*  But yeah, no, I do try to keep an eye on it.
*  So I do think crosstalk in the dark in both directions but in the direction of cognitive neuroscience towards AI could be very beneficial to AI and I don't think it necessitates us to have figured out all the interactions and stuff like that.
*  I think we're getting lots of precise details. I think we're getting lots of insights as to things that matter even if we don't exactly exactly how they matter that can be used that that that should serve as inspiration if not exact models for AI agents.
*  I think working memory is an example.
*  Although, and that I love to see more tested, you know, I think, I think something that's curious about working memory is how limited it is really right like it's it's very, it's very stupid limited right like three or four items really it's, it's, you know, like if you're if you're an AI person you're like, why would I bother.
*  Yeah, I mean I've even seen you know in like the neural Turing machines where you know that you have a long term memory storage. It's even sometimes called working memory because you could just retrieve it after a few steps right so so in that sense it's working memory, but in the, you know, we would consider it more like long term memory or something like that.
*  Yeah, no it's long term memory. I mean, I know system that has a high capacity can be called working memory I think I think that's the thing that I think we can do better than that.
*  I think it's like we have this system that has a very low capacity. And I think I see that as a bug. And I think it's actually more like a, you know, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a, a,
*  most likely a feature, although I don't have proof of that, but I think it's a feature in the sense of attention, essentially of forcing a bottleneck on processing that enables us to create a small state space over which being fast and flexible is much easier than over a big and complex state space.
*  And so I think, go ahead.
*  I was going to say, but if I had unlimited or much less limited resources and computational speed, would I still need that? Because it does seem to be dependent on limited cognitive resources.
*  Well, I think, you know, I think, I think if you're, you know, someone trying to do automatic, like self-driving cars or something like that, right, you care about how much resources you spend and how quickly you are able to adapt in a different environment, right?
*  Even if you have much more than humans, right, you have limited resources and a very limited amount of time to direct to a new situation.
*  So, so I think, you know, even if you don't take the exact three, four number seriously, I think you should still take the, you know, more general idea of like, maybe a bottleneck is a good principle.
*  Seriously, just not our, just not our dumb limited bottleneck, perhaps maybe a larger, wider capacity bottleneck, depending on how fast you need to make decisions, right?
*  Yeah, maybe. I think, I think it's an open question. I think, I think, I think it's something to be explored, really.
*  And I think there's other examples, you know, like there's another side of my work that's about structure learning that shows very, that humans have those very strong biases to create complex, you know, structure where they don't necessarily need to do so.
*  And, you know, that's kind of an anti, anti Occam's razor kind of thing where you're like actually complexifying things instead of simplifying them.
*  And, and that seems like very counterintuitive in a sense. But, but then what we see is that by creating this kind of, this kind of, you know, this kind of, this kind of, this kind of way, it's not necessarily, it's not necessarily about building a structure.
*  So, if you're building this kind of bigger structures, you end up being more flexible later on for generalizing. And so, and I've seen actually recently a few AI papers like having this kind of ideas in there.
*  I do think, you know, I do think there are ideas that come out of this research that could usefully be exploited, not as is, but as, you know, broad ideas that then can be translated into their own use for AI.
*  I think there's a more pragmatic answer to your question too, which is that honestly, my impression of AI papers is that they're terrible at analyzing behavior.
*  I don't know if you've seen that, but the performance of AI agents is often just like, how many points do they get, something like that.
*  And I think, and I think we could learn so much more about the representations and the computations that those agents do with more careful analysis.
*  And I think that's something that cognitive scientists do very well and could maybe teach a little bit to more AI people.
*  How about the idea of, okay, so we've talked about the interaction between working memory and reinforcement learning, but in the brain, you kind of think of these systems as mostly separable, right?
*  And so you could imagine implementing some working memory network and then kind of having it connect with a reinforcement learning agent or network, right?
*  In a robot or just a large artificial network.
*  But then you take something like attention, a cognitive function, and we know that, you know, like I was mentioning earlier, attention and working memory are highly intertwined and just cognitively, you know, they're highly intertwined.
*  But also when you look in the brain, you see, you know, lots of neurons who have attention modulated activity and working memory modulated activity.
*  So I think in AI or in deep learning, the idea would be to just, you know, add an attention network and have it connect to a working memory network.
*  Whereas in the brain, these things would be overlapping a lot, right?
*  And widely distributed.
*  So, I mean, would you imagine that in an AI system that, you know, you would need to build it to generate true intelligence or something more human like that you would need to build it in the same way as it's as it develops in our brains at the implementation level?
*  Would you need to implement it in that same kind of overlapping way?
*  I'm not sure.
*  I'm not sure. I mean, when you think about transformers, which is the way I think of, you know, having most successfully implemented attention in recent deep learning stuff.
*  Attention.
*  Yeah, of course.
*  It's it is it is embedded right in that sense. It is like it is present throughout the networks. Right.
*  So that's true. Yeah, that's true. I should have I should have even thought of that before I started spouting off about adding it as a module.
*  But I think most most of the time, the approach is more like you said before, is to create a separate module and make it, you know, like, you know, only regroup it somewhere towards the end of the of the process or something.
*  Yeah, I really don't know.
*  It seems to me like the more the more successful approach.
*  I don't know. I guess I can think of examples of both right. Like like you said, the neural machine has this kind of like modular structure that was very successful for for some applications.
*  The transformer has that much more integrated structure that's successful for the approaches.
*  That's where we can learn more. You know, like if we go back to our dimensions at the beginning, right.
*  If you know, maybe the fact that it's omnipresent tells us there is less of a pure dimension than we think it is.
*  You know, maybe that's where we need to do more work. I don't know.
*  Is intelligence itself a super high dimensional space?
*  Or or because we measure it with one number often.
*  Yeah.
*  Well, I mean, we all know how controversial that is, right?
*  Yeah. Yeah.
*  Yes, I think I mean, I, I have no expertise in this either, but I, I don't doubt that intelligence is super high dimensional.
*  You are a you're a classical singer. What does that mean?
*  Yeah.
*  Like, what does that mean? Operatic?
*  Opera. Yeah, classical, you know, what's us requiem stuff like that.
*  Oh, okay. You play an instrument. You play probably multiple instruments. You're multilingual. You probably play multiple instruments.
*  You probably dual task on the instruments so that you can learn them better, right?
*  I play the cello.
*  Of course you do. Okay. Well, I don't know if you've ever been in a band.
*  I don't particularly like it when scientists name their band something like sciencey and then a.
