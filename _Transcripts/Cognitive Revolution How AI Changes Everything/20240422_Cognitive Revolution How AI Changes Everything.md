---
Date Generated: April 23, 2024
Transcription Model: whisper medium 20231117
Length: 4998s
Video Keywords: ['Descript']
Video Views: 730
Video Rating: None
---

# Robotics Research Update, with Keerthana Gopalakrishnan and Ted Xiao of Google DeepMind
**Cognitive Revolution How AI Changes Everything:** [April 22, 2024](https://www.youtube.com/watch?v=oH2vjGsBIQA)
*  People used to think that all the robots are so different.
*  All of their data is like so different.
*  And people moved in the direction of thinking that all robots are kind of similar.
*  It's only as different as like English and Chinese or something.
*  And the concepts are similar.
*  It's just the manner of expression that's different.
*  The data sets that resulted even starting from those criteria were so, so diverse, right?
*  We have everything from like, you know, using like baby toys all the way to like industrial arms, you know, all the way to, you know, like very dexterous, like cable routing robots.
*  Even with this very limiting assumption, you still get so many different morphologies.
*  If you train on VLMs and if you build on top of the knowledge of VLMs, then you can stitch a lot of concepts from the internet along with the emotions that you have in robotics data sets.
*  You could, under the same initial conditions, just change the prompt a little bit, do some prompt engineering and actually see qualitatively different behavior from the robot.
*  Ultimately, if you want to do a lot of tasks and be useful in environments where humans operate, you kind of need to go as close to a human embodiment as possible.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers, entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today, I'm thrilled to be speaking with Kirtana Gopalakrishnan and Ted Zhao, researchers at Google DeepMind Robotics who are developing AI systems for general purpose robots.
*  This is Kirtana's second appearance on the show.
*  Just a year ago, fresh off the publications of RT1 and PalmE, she described the state of AI for robotics as being somewhere between GPT-2 and GPT-3.
*  Noting that the lack of internet scale data was a major barrier to progress.
*  Since then, Kirtana, Ted and their colleagues at Google DeepMind have published a remarkable flurry of papers demonstrating new techniques that allow robots to leverage large multimodal models, to control different physical form factors,
*  to learn more efficiently from human examples and instructions, and even to use a prototype robot constitution to guide their behavior.
*  In this conversation, we cover six different papers.
*  RT2, which shows how internet scale vision language models allow robots to understand and manipulate objects that they have never seen in training.
*  RTX, a collaboration with academic labs across the country that demonstrates how a single model, trained to control a diverse range of robot embodiments, can outperform specialist models trained for individual robots.
*  RT trajectory, a project that shows how robots can learn new skills in context from a single human demonstration represented by a simple line drawing.
*  AutoRT, a system that scales human oversight of robots, even in previously unseen environments, using a combination of large language models and a robot constitution to power first line ethical and safety checks.
*  Learning to learn faster, an approach that enables robots to learn more efficiently from human verbal feedback.
*  And finally, Pivot, another project that shows how vision language models can be used to guide robot action, this time with no special fine tuning required.
*  Progress in robotics is still trailing behind the advances in language and vision.
*  There are still challenges to be overcome before robotics models will have the scale of data or the sample efficiency needed to achieve reliable general purpose capabilities.
*  And the study of robot safety and alignment is still in its infancy.
*  But nevertheless, I see this rapid fire series of papers as strong evidence that the same core architectures and scaling techniques that have worked so well in other domains will ultimately succeed in robotics as well.
*  The work being done at Google DeepMind is pushing the boundaries of what's possible. Investment in a new generation of robotics startups is heating up and the pace of progress shows no signs of slowing down.
*  As always, if you're finding value in the show, please do take a moment to share it with friends.
*  This one would be perfect for anyone who's ever daydreamed of having a robot that could fold their laundry or pick up their kids toys. I certainly count myself among them.
*  And especially as we are just building the new feed, a review on Apple podcasts, Spotify, or a comment on YouTube would be much appreciated.
*  Now, here's my conversation with Kirtanagopalakrishnan and Ted Zhao of Google DeepMind Robotics.
*  Kirtanagopalakrishnan and Ted Zhao of Google DeepMind Robotics, welcome to the cognitive revolution.
*  Hi.
*  Yeah, thanks so much for being here.
*  So it has been a busy time.
*  We had an episode with Kirtanagopalakrishnan just under a year ago, and it's amazing how much progress has been made and how many papers you guys have published since then.
*  I thought I would just kind of super quickly summarize the state of play as it existed a year ago.
*  And then what I really want to do is just give you guys an opportunity to give us a walkthrough of the many results that you have released over the course of the last year.
*  We can really get into as much as we have time for the technical details of that.
*  And then toward the end, you can kind of maybe pull up a little bit and sort of take stock of the big picture in robotics and where all this is going.
*  And when I'll have a robot picking up my kids' toys, maybe doing their laundry would also be awesome.
*  Just to put in a couple requests right at the top.
*  But basically a year ago, and again, just even under a little under a year ago, you described the state of robotics as kind of being between the two.
*  And noted that the lack of data was a huge bottleneck to progress.
*  We talked quite a bit in that episode about how, you know, at the Google kitchens, you guys have had this kind of ongoing setup of human demonstrations, collecting all these data points.
*  That was starting to pay off in the form of some really cool results even then.
*  And since then, I think we've got, is it six or seven different discrete results to cover today where you're expanding the data sets in various ways.
*  You're showing interesting kinds of transfer from foundation models that are multimodal and trained in other contexts into robotics, forms of imitation learning.
*  Like it's really been an incredible tour de force.
*  So before we get into all the specific papers, I guess my first question for you guys is like, is everything working?
*  Because from the outside, it really seems like you must have sketched this out a year ago and seems like it's all kind of gone according to plan.
*  Now, whenever I say that, people are like, well, no, a lot of things don't work.
*  And I'm sure like lots of little things, you know, had to be kind of figured out along the way.
*  But has the last year kind of been a little bit of a challenge for you guys?
*  How would you summarize that a high level the last year of progress that you guys have made?
*  Definitely the feeling that we're living through an inflection point right now.
*  I think as Kirtanis said a year ago between GPT-2 and GPT-3 and maybe nowadays it's closer to the era of like the GPT-3 time in robotics.
*  I think it's definitely been pretty top of mind for me and think about why that that's the case.
*  I think my one sentence explanation is that with the era of internet scale foundation models,
*  things that used to work maybe 20, 30 percent of the time are now working 60 to 70 percent of the time.
*  And in robotics, right, is a very complicated dynamic engineered system with many pieces.
*  In the past, if every small component of your entire system only worked 30 percent of the time,
*  then you're going to have to work with a lot of different components of your system.
*  It would take many, many iterations to get a whole performance system working at scale.
*  But now when every single part of the entire stock just works that much better from the research iteration process to the engineering scaling process to the data collection engines,
*  I think you can really just see the pace increase when you just have many more successes and a much higher hit rate when you're going about and scaling up your research.
*  So I think that's a really good point.
*  Yeah, like I said, I think last year I said what we lack is data.
*  And so we have also tried to attack that problem from like different ends.
*  So in addition to data, I think the thing about research is that it's very hard to plan research.
*  Like you kind of have to like do a breadth first search over like many different approaches, see what is the best way to do that.
*  And I think that's the key to that.
*  The thing about research is that it's very hard to plan research.
*  Like you kind of have to like do a breadth first search over like many different approaches, see what shows signal and then really double down on that.
*  But over like a large horizon, you kind of know what kind of things you want to work on.
*  Like one is like getting more data or the other side of that problem is improving data efficiency of policies.
*  The second is tackling self-improvement type of research.
*  And then thirdly, like how to better use our foundation knowledge, how to really leverage their like world knowledge,
*  how to really leverage the human input required to make robots better.
*  Cool. Well, there's been so much work that's come out.
*  I thought maybe I would kind of just go down the list, give my high level takeaway as somebody who has read the paper
*  and is trying to piece together the big picture, but then give you guys the opportunity to go deeper into what really matters
*  and some of the technical aspects of each project that you think are kind of most relevant or you want people to come away understanding.
*  So the Palm E had just come out a year ago and RT1 we also covered in that last episode.
*  Shortly after that came RT2, obviously the successor to RT1, but a bit of a different approach.
*  As I understood that paper, it was really about showing that robotics can take advantage of the highly general
*  and kind of flexible understanding that is increasingly showing up all over the place in large pre-trained language models
*  and in this case, multimodal models, specifically vision language models.
*  Tell us a little bit about kind of the co-fine tuning, which was an interesting technique
*  and then how that allowed you to kind of generalize in a more effective way than previous systems had.
*  Yeah, so I think the way I see it is like RT1 kind of showed that if you have enough data and in domain,
*  you can get really high performance in domain and RT2 is more like a generalization capability.
*  So if you train on VLMs and if you build on top of the knowledge of VLMs,
*  then you can stitch a lot of concepts from the internet along with the motions that you have in robotics data sets.
*  And as you saw in the paper, there are very interesting results on like symbol understanding,
*  understanding concepts from the internet, better correlation between like image and language understanding.
*  So for the co-fine tuning, you do forget some of the concepts from the internet,
*  but then co-training is better because in each training batch,
*  you have the image language pairs as well as the robotics data.
*  So you have a better understanding and you retain the concepts that you learn from the internet.
*  So that's kind of avoiding mode collapse.
*  Essentially, that's been a pretty or I guess a mode collapse.
*  Maybe it's not quite the right term for it, but avoiding catastrophic forgetting is the purpose of the co-fine tuning.
*  That's definitely a common theme.
*  And I guess we covered this a little last time, but just refresh our memories on kind of the relative scales.
*  I think there's obviously a lot of objects in the world.
*  It's hard to collect with a specific physical robot,
*  every different instantiation of a cup or a bag of chips or then things you haven't seen at all.
*  But that's where this internet scale data really shines.
*  So could you give us just a little bit more kind of just practical intuition of like,
*  if you didn't have this internet scale data,
*  what would the process look like to handle an unseen object, for example?
*  And then how is that different when you have the internet scale data to draw from?
*  I think basically as a brief primer maybe about what really end-to-end robot learning has looked like in the past years
*  is especially when thinking about things like generalization to novel objects,
*  when you want to manipulate a wide variety of different items that occur in our everyday life.
*  The classical robotic even learned systems will take some kind of off-the-shelf pre-trained visual representation perception system
*  that has been trained on a ton of different objects on ImageNet datasets with very strong visual features.
*  And those are kind of like bottlenecked,
*  that they're passed through some kind of interface, some kind of pre-trained representation
*  to a downstream robot action policy.
*  And I think in these cases, the downstream action policy is what is then really being fine-tuned
*  on your more narrow set of very specific, special, your particular domain that you care about,
*  that kind of robot data.
*  In our case, our robot dataset is the same one that was in RT1.
*  It's a large, 130,000 teleoperated expert demonstrations of our mobile manipulated robot
*  collecting a variety of manipulation tasks in an office kitchen setting.
*  And notably, though, this is only on a set of roughly 17 or so objects,
*  such as chip bags, soda cans, water bottles, et cetera.
*  But it's still quite limited to the particular settings that we source from our own Google MicroKitchen.
*  But this is still very drastically different from what's out in the real world.
*  And so I do think I want to emphasize that with RT2,
*  I think it's one of the most exciting takeaways for me, at least,
*  was the fact that the line, the boundary between what are perception problems,
*  what are open world object recognition, and what is robot control,
*  this line starts to blur.
*  We do not have a pipeline system where you first take care of perception and you solve that
*  and then you solve control after.
*  We're literally just treating both of these problems as a single VQA kind of instantiation.
*  As Kirtana said, we mix both kinds of these questions, right?
*  Visual language, like web scale, kind of web image captioning kind of problems.
*  We mix those into the training batch alongside robot action data,
*  which is like, given this current image, how do you actually move your arm to do this specific task?
*  And I think the fact that that line does get blurred is how we see such really cool transfer properties
*  between web knowledge and robot knowledge.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages.
*  So what makes the Brave Search index stand out?
*  One, it's entirely independent and built from scratch.
*  That means no big tech biases or extortionate prices.
*  Two, it's built on real page visits from actual humans,
*  collected anonymously, of course, which filters out tons of junk data.
*  And three, the index is refreshed with tens of millions of pages daily,
*  so it always has accurate up-to-date information.
*  The Brave Search API can be used to assemble a dataset to train your AI models
*  and help with retrieval augmentation at the time of inference,
*  all while remaining affordable with developer-first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data sourcing
*  and more human-representative datasets.
*  Try the Brave Search API for free for up to 2,000 queries per month at brave.com slash API.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work, customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it, and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  I always try to frame things in terms of inputs and outputs as much as possible,
*  and I think that just helps give people a kind of concrete intuition.
*  And so what you're saying in the past is that you would have a vision model
*  that would, and you would kind of take the high-dimensional state of that vision model,
*  feed that into a robot model, and then be training that thing kind of separately.
*  And now here we have an entire end-to-end system where,
*  because you've done this co-fine tuning with action data,
*  you can now say to one single end-to-end system, one single end-to-end model,
*  okay, here is what you're looking at in the form of an image,
*  here is what your objective is, presumably some state of the robot in terms of position,
*  or maybe not even, and then the question becomes,
*  how do you move to achieve the goal given what you see in the image?
*  And this one model can now say, move arm a certain direction, a certain amount,
*  and advance toward the goal all with basically one set of weights.
*  Do I have that all right?
*  How does the hand work?
*  I mean, I can, in my experience with these like high, these web scale things,
*  the flexibility is incredible.
*  So, you know, and you can start, you've got some interesting demonstrations
*  where you can ask questions that like tap into the kind of broader world knowledge,
*  right?
*  So you could be like, you have two bags of chips next to each other,
*  you could like say the one that, you know, grab the spicy one,
*  and because the, you know, the broad pre-training has kind of captured that like
*  the color and the name or whatever of the certain flavor of chips
*  is going to be the spicy one,
*  then it will have that kind of common sense awareness.
*  But does that extend down to like the motor control?
*  My guess would be not really, right?
*  And I'm wondering if that, is there something that's kind of happening
*  that's interesting at the like actual grabbing layer as well,
*  or is that still kind of rough at the RT2 stage?
*  You're right that, yeah, previously we had just our data
*  and all of the knowledge was coming from in-house,
*  collected data and with RT2, you have this understanding from the web that's transferred.
*  But if you look at the type of data that you add in RT2,
*  it's like image language pairs from the internet.
*  So like you said, you do get some understanding of external image concepts
*  and also if you, you can sort of prompt it in language.
*  I think the most surprising result for me was the,
*  my favorite one is the one where you can do sort of like a
*  math, you can ask it like, what is the sum of like one plus two,
*  but then the way that you ask is like move the core can to the sum of one plus two or something like that.
*  So it is able to intuitively have some understanding of like internet skill concept,
*  but then you can sort of express that in movement.
*  But the movement itself, like how to move the arm comes from our data
*  and we see that the level of motion generalization is limited in RT2
*  because these motions are only available in the internet.
*  So in some sense, it is able to transfer those movements to internet concepts,
*  but it is not able to generate new movements by itself.
*  And this intuitively makes sense, right?
*  Movement is movement data or even the physics of like how to grab different objects
*  does not quite exist on the internet.
*  So where would that knowledge come from?
*  One of the challenges that RT2 also handled was
*  how to sort of merge the data into the internet.
*  How to sort of merge the robotics data into something that looks like internet data.
*  So like the tokenization in RT1, it was like action tokens
*  was a representation that was sort of endemic to the transformer that we were using.
*  And with RT2, it's like you sort of have to express the same thing,
*  but in language so that now actions look like language.
*  I found that very like ingenious.
*  Yeah, so if I recall correctly, RT1 was a sort of mid-level command as an input,
*  like move arm, and that was coming in from like a higher level language model,
*  and it would take this sort of mid-level command
*  and then translate that to like very specific actions.
*  But I think your point there is like that's all that that particular transformer could do
*  was like speak in this very kind of custom action space.
*  Whereas now in RT2, it's essentially vocabulary expansion
*  or maybe not even vocabulary expansion,
*  but because everything is kind of treated as tokens,
*  the same system can still answer questions about an image straight away,
*  or it can give commands in kind of the same token space,
*  in the same vocabulary space, all working as one.
*  Yeah, I think maybe like one last thing to add here,
*  and I think this kind of the framing that I really like to think about this
*  is in all of the works we'll be discussing today, and especially RT2,
*  we're kind of bridging the gap between like what is robot specific data
*  with their custom input spaces and the custom objects and physical reasoning
*  and your custom action representations and outputs.
*  And then like, you know, internet data and internet concepts
*  have been sitting in this whole other kind of pile way off very far away.
*  And with all of these works, we're trying to bridge these two worlds together
*  to enable more transfer to better leverage the immense amounts
*  of reasoning and capabilities already contained in internet data.
*  We're trying to make robotics more similar to that,
*  and we're trying to bring together concepts on the internet
*  and bring them to robotics.
*  And I think RT2, as exactly as you said,
*  we're doing this by making the action outputs literally just tokens,
*  literally just language.
*  In terms of the motivation for that at a super high level,
*  is it simply that we need like super high scale data
*  and it's just going to be prohibitively costly to get all the data
*  that you would need.
*  And so you kind of feel like, jeez, to get to the internet scale,
*  there's just no way to do it other than to kind of figure out some transfer strategy.
*  Or maybe you could say, well, no, we think we could get there.
*  I imagine you could have different theories of the case
*  as to why this is the right approach.
*  The data itself is a hard problem.
*  Like we discussed before, the motion generalization is still not coming
*  from internet, right?
*  And for me, it's like robotics is now becoming, like Ted said,
*  it is a bridging of the concept between robotics itself and the internet.
*  And to me, it's now becoming like embodied AI.
*  So like what is a physical expression for AI?
*  As we build intelligence on the internet and train them on the internet,
*  how do we make sure they can sort of move?
*  Yeah, previously, robotics has worked very differently.
*  We use concepts in AI, but then like we discussed,
*  like the data and other techniques were different.
*  And now everything is like coming closer together.
*  Yeah, data itself, I think so far, imitation learning is what works best.
*  And I think this is true for like other AI research as well.
*  So a large amount of data or knowledge is coming from imitation.
*  But we still need to understand because of the fact
*  that high quality demonstrations are extremely costly to obtain
*  and also they require humans.
*  So these data sets only scale linearly as a function of the amount
*  of humans you deploy and the amount of robots you deploy.
*  You kind of need to make the data sets grow much faster.
*  But there are some challenges with it in the sense that
*  trying to scale high quality data by maintaining the quality is very hard.
*  So you can sort of scale cheaper data.
*  You also have to think about more creative ways of transferring things
*  like transferring internet knowledge or transferring knowledge from SIM
*  or some other form of self improvement.
*  Cool. Well, in the interest of time, let's move on to RTX.
*  So this is the next in the series.
*  And for starters, this one, I mean, I guess conceptually, right,
*  this is about generalizing across different robot embodiments,
*  which, you know, it's obvious in some sense,
*  but we're taking a second to ponder just the incredible diversity
*  of forms that robots can have.
*  You can fill in the gaps in my knowledge,
*  but in a lot of the papers that you guys do,
*  you have kind of a wheeled platform robot that can roll around the kitchen
*  and then has like often one arm.
*  I've also seen setups where it's like two arms
*  that are just like mounted on a tabletop and do tasks on a tabletop.
*  You could obviously have something that has legs
*  and can walk around and lots more besides, I'm sure.
*  So in what sounds like an incredible feat of project management
*  and kind of political coalition building,
*  the RTX project involves going around to a bunch of different robotics
*  and labs all around the country.
*  I suppose most of these are academic and saying,
*  hey, we would like to train a generalist model on a bunch of different robot embodiments.
*  Could you give us your data sets?
*  We will then take these data sets, mash them up into one giant data set,
*  do a giant model that is meant to rule them all.
*  And then I guess the upside of this for them
*  is that they would presumably get the model back
*  and if it works well, it would even be maybe better
*  than what they could train on their own
*  because as you know, it's becoming obviously a huge theme
*  like with scale, you know, things kind of sometimes get qualitatively different.
*  Indeed, it seems like that's basically what happened, right?
*  You train a single model on all these different embodiments.
*  I believe, I don't know if I have the exact number here,
*  but I think it was something on the order of like 30 different kinds of robots.
*  And it looked like almost across the board with maybe like one or two exceptions,
*  the jointly trained model was better performing
*  than each lab's earlier model that they had trained just for their own robot.
*  First of all, you know, by all means, correct any misconceptions that I have there.
*  I'd love to hear a little bit more about the kind of diversity of embodiments.
*  You know, maybe like, are there any particularly unusual
*  or unexpected forms of robots that people are working with
*  and then, you know, any other kind of the technical details
*  or challenges in that project would be interesting too.
*  I'm very impressed.
*  That was like a very great kind of overview of the project.
*  I will maybe note one thing that this really was a team effort.
*  I don't think it was like Google's the mastermind
*  that's going about with this agenda beforehand.
*  It was mainly, you know, driven out of like an ambition
*  that, hey, you know, we all recognize that robotics data
*  is not as plentiful as the internet data.
*  You can't just pick it up and scrape it and it's there.
*  You really have to go out and we have to build this internet-scale robotics data together.
*  And I think, you know, the kind of entire coalition, so to speak,
*  was quite decentralized in the sense that everyone was excited
*  about this joint vision in collaborating, in sharing,
*  and like, you know, all the different specific robotics data that they had.
*  And again, I think at the beginning, we weren't really even sure
*  if like one general's policy would actually, you know, be the best
*  or super performant at every single embodiment.
*  And even as you mentioned, you know, this didn't even end up being the case on everything.
*  And I would even emphasize that to expect such a result
*  where the generalist outperforms specialists
*  on the very niche domains that, you know, the specialists have kind of been overfit to.
*  This was actually quite shocking to me.
*  You know, like, I think there's been so many examples over the past years
*  where people have tried to scale single task methods to multi-task methods.
*  And you definitely get a lot, you know, maybe you learn faster,
*  you learn a more robust policy that's less brittle to small perturbations.
*  But oftentimes you have to give up raw performance, right?
*  Generally, in a lot of cases, the only way to max out your performance
*  on this one narrow regime that you care about is to train a specialist and overfit to that domain.
*  And so it was really exciting here to kind of see positive transfer
*  where the generalist outperforms even this presumably very tuned baseline
*  from the individual labs on their setups themselves.
*  So I just wanted to point that out as something that really moved the needle for me internally.
*  I think for me, the understanding was like people used to think that all the robots are so different.
*  All of their data is like so different.
*  And every lab has or like they invest in like a couple of embodiments.
*  It was just, I think, post RTX, the idea was that people moved in the direction of thinking that
*  all robotics, all robots are kind of similar.
*  It's like it's only as different as like English and Chinese or something.
*  And the concepts are similar.
*  It's just the manner of expression that's different.
*  And maybe also like one surprising thing was people do robotics research,
*  but then your results could not be compared to someone else's results because you don't have their robots.
*  You don't have their data.
*  So I think the RTX paper also sort of like brought everything to the same type of benchmark.
*  And now you do have a way of comparing things.
*  Maybe one downside of this is that it also showed how in the past we have been sort of collecting repeated data.
*  Like everyone's data is sort of like pick and place, but we could all,
*  if we were all working together to solve this problem, we could also solve it in a more complementary fashion
*  and tackle the task in a more complementary fashion.
*  Yeah.
*  So a lot of the data is like pick and place because people were independently targeting that.
*  And now it's like coming together.
*  And maybe there are, maybe there aren't any like particularly exotic embodiments.
*  I'm very curious as to sort of how diverse the future robot populated world is going to be.
*  In terms of the robots that we encountered.
*  Any notable embodiments that you'd want to highlight?
*  For RTX, at least, I think maybe one caveat is that in order,
*  this is already a crazily ambitious project at the time.
*  So we did start out though with the assumption that we would be studying,
*  single arm manipulators with a two jawed, two finger gripper with one single camera view.
*  Even if the embodiment had multiple cameras, we'd only be able to see the robot.
*  If we had multiple cameras, we'd only kind of be learning from one.
*  This seemed like very limiting assumptions, but even then you can see that the data sets that resulted,
*  even starting from those criteria, were so, so diverse, right?
*  We have everything from like, you know, pick and place with like small widow X robots
*  and like, you know, using like baby toys all the way to like industrial arms,
*  you know, big ones, big beefy ones to the mobile manipulator we here have at Google,
*  all the way to, you know, like very dexterous like cable routing robots from Berkeley.
*  Like even with this very limiting assumption, you still get so many different morphologies.
*  And I think, you know, maybe just kind of, you know, hypothetically,
*  the second part of your question, if I'm understanding correctly,
*  is like, how does kind of the trends we see in RTX kind of reflect into the future?
*  Like as we see robotics go and proliferate throughout our world and be useful for humans and society,
*  you know, will we just have one single morphology, maybe a humanoid or many different ones?
*  I think for me, at least I think it's an open question.
*  And I do see a lot of benefits of specialization.
*  Like we have specialized robots in every household today.
*  They're called refrigerators and toasters and microwaves and dishwashers.
*  And you don't have one single kind of robot that does it all, you know, at an average level.
*  So I do think there are arguments that we will continue to see specialization.
*  But yeah, I think, you know, Kirtan is also has a lot of thoughts about this as well.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Today's podcast is brought to you by Plum.
*  Is your product team struggling to keep up with the incredible pace of AI development?
*  Are you tired of spending countless engineering hours just to test out small prompt changes in your product?
*  Thankfully, there's Plum.
*  Build cutting edge AI experiences for your users in a fraction of the time.
*  Say goodbye to the slow, tedious process of hand coding and hello to the future of AI development.
*  Get ahead of your competition and start moving as fast as AI does.
*  Check out useplum.com.
*  That's Plum with a B for early access.
*  Hey all, Eric Torenberg here.
*  I'm hearing more and more that founders want to get profitable and do more with less, especially with engineering.
*  Listen, I love your 30 year old ex-fang senior software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy, is it a hassle to do at scale.
*  From sourcing to interviewing to on the ground operations and management.
*  That's why I teamed up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high level for over five years to help you access global engineering without the headache.
*  Squad, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent so you don't have to.
*  With teams across Asia and South America, we can cover you no matter which time zone you operate in.
*  Their engineers follow your process and use your tools.
*  They work with React, Next.js, or your favorite front-end frameworks.
*  And on the backend, they're experts at Node, Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost.
*  Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the waitlist.
*  Yeah, so one thing to note about the RTX is that a lot of the collaboration was with academic labs.
*  And there is a chicken and egg problem in robotics other than the capital intensive nature of getting acquiring hardware.
*  So people have been working with these robots for a long time, but they're not necessarily reflective of like what the future might look like.
*  The second thing is, yeah, like I said, the chicken and egg problem.
*  Like we don't have more advanced human robot embodiments out there because people haven't found a way to make them useful.
*  But as the research is picking up speed and we have more use out of them, maybe we will see more generalist robots, more abundant in the world.
*  And I think, yeah, the future, you don't know what the future will look like.
*  So people have to place their bets.
*  And I think if you ask robotics, there's like a wide spectrum of what people think will be in the future.
*  Me personally, I fully believe like humanoids are, we are going to see more of them.
*  And yeah, so this is like a very dividing topic.
*  If you ask what is it like, argue all day about do we need humanoids?
*  Do we not need humanoids?
*  Sometimes we are like human factors, not human.
*  The main arguments would still stand for humanoids.
*  One is that our world is sort of designed for humans.
*  So one hypothesis is that if you design policies for like a single or mobile man, then once you solve a lot of tasks in that environment,
*  then you see that it's limiting because many tasks in our world are like opening a bottle or like opening a fridge and then taking something from it.
*  So you have to like keep the door open.
*  Or even I think some people say, well, you don't need wheels.
*  But then what if you solve a lot of tasks on a wheeled platform and then there's a little curb on your floor or by a street side and then the robot is like stopped there.
*  So I do think that ultimately, if you want to do a lot of tasks and be useful in environments where humans operate,
*  you kind of need to go to a human or as close to a human embodiment as possible.
*  The second argument is that there are a lot of concepts that you can still try.
*  And some of this requires like closeness to the human body.
*  One is you can learn from, you can learn concepts from YouTube.
*  There's like a lot of data on like humans doing a lot of things, playing a lot of sports.
*  And in order to get the best transfer, I think the closeness of the target embodiment and the human embodiment is required.
*  There's also the cost factor, right?
*  Like our body does have limitations in the sense that there is payload, there's battery.
*  And if it does not, you have to bring the cost down for people to want it.
*  And also in situations where you need like extreme amount of reliability and specialization, you would have specialized robots.
*  So two quick follow up questions on this RTX.
*  Is it the case that the outputs are again, just tokens?
*  And do I remember correctly that there's essentially like a discriminator token that goes in to say like,
*  this is the kind of robot you're working with.
*  And it's really just like, if I remember, it's like a one token flag, right?
*  That tells the model which embodiment it's working with at any given time.
*  Actually, in RTX, and again, this is like a really great point.
*  We actually didn't do that at all even.
*  So the robot that RTX is currently being executed on has to be inferred purely from observations.
*  Whoa.
*  Yeah, like that's from the image?
*  From the image itself, just by the fact that, okay, I know that from the Stanford lab,
*  the camera was at this angle and it was on this robot and these types of tasks.
*  And then over in UPenn, it was this other robot and stuff.
*  So the model had to do kind of implicit system identification for which regime it was operating in.
*  And because of this, at least for at least the current version of RTX,
*  there's no possibility of zero shotting to completely unseen robot entirely,
*  like a completely different action space, different observation space, et cetera.
*  Right now, at least, we wouldn't really expect it to just work out of the box.
*  But I think what you're mentioning with more action spaces, helping the model out to understand,
*  okay, now I'm in robot X and here's kind of the API description of what the action outputs mean.
*  Here's some pointers for what's in the scene, what tasks I should be doing.
*  That would help a lot for kind of generalizing to other settings as well for future work.
*  Yeah, that's fascinating, a little tidbit.
*  Another question on specialization.
*  It would seem like once all the labs got the generalist model back,
*  that they would then probably fine tune that generalist model on their own dataset or embodiment again,
*  and perhaps see even further gains there.
*  Like certainly that's my experience with language models is like I can instruct them or I can few shot them.
*  But if I really want to take even a very generalist model and zero it in on my task,
*  I fine tune it, right?
*  So have we seen that coming downstream of this project?
*  I think in the recent papers that some of these checkpoints are open source.
*  So I have seen, I think in papers published since people have tried to fine tune the models onto their platforms themselves.
*  But there are also some infrastructure limitations to doing that.
*  One is that when you have a lot of this data with RT1 and RT2,
*  the parameter size of these models are really large and then how to serve them and how to fine tune them,
*  especially for like external partners of Google,
*  there are some engineering challenges around it that I think are not yet fully solved.
*  I will say that like building on Kirtana's point is that the release of RTX is not really just about the model itself.
*  It's not just about the fact that we can train one model with them all.
*  I think it's more like this is the starting line.
*  This is not the finish line.
*  This is just a new chapter of robotics research by nature can now just start by default by assuming you're in the multi-robot cross embodiment regime.
*  And there I think we haven't necessarily seen a ton of work that takes the literal checkpoint that we release and fine tune on top of that.
*  By definition, academic labs like to search for new problems with new model decisions.
*  But what we have seen is that many, many projects building off the release data set and data pipelines that we also open source with.
*  That RTX paper and that I think has really been very impactful.
*  We see, for example, work from Berkeley, you know, recently called called Octo,
*  which, you know, has their own version of kind of like a their own generalist policy checkpoint policy that trains across many different robots.
*  They have some new design decisions like adding diffusion heads.
*  But there they, you know, also kind of assume by default that they're also in this cross embodiment multi-robot setting where they train and evaluate on many different robots.
*  To me, at least that's kind of the most impactful result of RTX.
*  People are now excited about cross embodiment research and it's now possible with the data sets and with the data infra that came with RTX.
*  Cool. Okay.
*  That's a great bottom line.
*  So next paper is RT trajectory.
*  This one is about learning from on the fly examples.
*  So and I think this is actually a really interesting project that a lot of people are interested in.
*  It's a really interesting project that a lot of kind of hands on practitioners in other areas can can borrow some inspiration from because the kind of core loop here, I think, is a super transferable pattern.
*  But basically you say, okay, I want to be able to prompt a robot in a new way.
*  I want it to learn from a simple kind of line sketch what it is supposed to do.
*  And then you just quickly say, like, hey, robot, here's what you do.
*  Like go, you know, move your hand like this and it could follow from that example.
*  Like that would be really great.
*  But how do we get it to do that?
*  Well, one big gap, of course, is we don't have a huge data set of it doing that.
*  So how do we train?
*  We don't have anything to train on.
*  So if I understand the kind of reasoning backwards, you know, this is this is again, I recognize this a lot from my own application development work.
*  I sort of say, okay, well, I want to be able to prompt it in that way.
*  And I do have a lot of examples of robots doing stuff.
*  So why don't I go back to that existing data set and kind of annotate one of the images that was that the robot did see as part of the prompting.
*  But now I'll actually give it that line.
*  And of course, you're going to do this on the ones where it operated correctly.
*  And you've got to make sure you fit the line that you're drawing to the actual trajectory that the robot had.
*  There's a lot of little nuances to this that I've certainly encountered again in a language setting.
*  But once you do all that annotation, then you can train the robot on the or train a model to control the robot with this sort of line input on a scene, have it do the thing.
*  And now you have this new prompting ability where it can learn from a quick line draw, whether that is a line draw that's like an actual human example or somebody literally just drawing a line.
*  Or perhaps the most interesting one is even just having, I believe, a vision language model, like, you know, kind of mechanistically draw a line based on its understanding.
*  So I thought that was really cool.
*  And again, that that working backwards from I want to be able to prompt in a new way.
*  How do I and what data do I have that I could then kind of fill in the prompts?
*  By the way, I use like language models to create those all the time.
*  So and you're using, you know, I'm assuming somebody in the VLM case, literally using a model to do it.
*  So I think that's definitely one that's really worth a ponder for a lot of people that want to open up new use cases really in any domain to kind of think about how they can get their existing data set to work harder by kind of synthesizing the prompt end of it.
*  And knowing that they already have the successful completion.
*  But I'm sure there's much more that you could comment on on that paper as well.
*  Yeah, I mean, I think I love that perspective.
*  That was really top of mind, I think, for us to when designing the system, working backwards is a great way of looking at it.
*  I think definitely the prompt ability, I think, of our trajectory is something that was also, you know, kind of new for me and move my own internal kind of, you know, perception of what these models can do.
*  Like literally and maybe to kind of just put this a bit more concretely, you know, if you have your robot in some given initial condition and, you know, you try something with RT1, RT2, it doesn't have to be a robot.
*  Well, you're kind of out of luck.
*  You can try the same thing over and over again.
*  You can slightly maybe rewrite the language instruction.
*  Like instead of, you know, pick up the cocaine, you can write like maybe like lift the cocaine, but you don't really have the granularity.
*  You need to be like, actually, you are two centimeters, you know, too low.
*  You missed the table because it's at a new height.
*  It's kind of obscured by shadows.
*  So you want to like be more gentle and approach more from the left.
*  There's no really way to do that right now with the interfaces, the language interfaces that we train our team.
*  That we train RT1 and RT2 on.
*  But with RT trajectory, the idea is maybe if you have this kind of like line sketch of a course trajectory of how the robot should do the task, you could under the same initial conditions, just change the prompt a little bit, do some prompt engineering and actually see qualitatively different behavior from the robot.
*  And that even that ability to have that small granular kind of adjustment just by giving a new prompt, that to me was pretty cool and pretty new and allowed us to take the robot to like whole new buildings that and we just like wheel around the robot, try out a bunch of stuff and it would just kind of work.
*  That was very exciting to me.
*  Yeah.
*  One of the things that I really liked about RT trajectory is that in traditional robotics research, you have a lot of search and planning.
*  But I think it was kind of harder to think about how you would bring that to like end to end learning.
*  And RT trajectory is like a nice way to like merge the two.
*  So if you see in RT1 and RT2, you only represent like really short horizons.
*  And some of the most successful applications of robotics, like self driving cars, were like you plan the way point between like where you are currently and like where you want to go.
*  And what I really liked about RT trajectory is that it is sort of representing a longer horizon future about like what you can do.
*  And the even the contact interaction is very creative.
*  And also maybe you can also think that the net amount of contact interactions we do through our daily course of going about the world is probably like a handful.
*  Right. Like so I can synthesize a lot of motions, do a lot of things that I generally do in my daily life, with maybe like 20 different types of contact interactions and a lot of trajectories.
*  Can you unpack that vocab for me a little bit more?
*  What's a what's a contact interaction?
*  So like what you so where to pick or where to like open and stuff.
*  So I think in the RT trajectory paper, it was represented with like these colored representations in addition to the lines themselves.
*  So I think it told the robot like, okay, now you pick after you go to this location and stuff like that.
*  So I would think that if you expand that vocabulary, maybe like some of the motions that are not existing in our data sets, like it's a spin or like open faucets and the things that I do in my kitchen.
*  I can imagine that you can also expand these contact interactions into your vocabulary.
*  And then now you have a representation that also shows some horizon and a lot of diversity in interaction.
*  And this is not something that's afforded in the action tokenization that we were currently using.
*  Like we showed in the paper, I think there is also an interesting way where like language models or multimodal models themselves can sort of think about these futures or like generate these features and then another model can like follow it.
*  So I think RT trajectory and some of its fusion with like pivot work, I think you can imagine a very interesting use case is coming up in the future.
*  Yeah, I guess two notes or observations on this one and then we'll keep going.
*  But the depth or the sort of go look at the paper to see this in detail, but it's not quite just a simple line.
*  There's like a color gradient that sort of represents like relative position in three dimensions, even though the robot is kind of only seeing it in two dimensions in a flat image.
*  And I would say, you know, for folks who want to go kind of use this, like working backwards, you know, engineering a new way to prompt in their own systems.
*  There is often some subtlety to it, especially if you want to maintain generality after doing this.
*  If you want to do like one task, then it's like often pretty easy to be like, all right, I'll use for most of my projects.
*  Historically, it's been GBT four these days.
*  I've got Gemini 1.5 access and I'm finding a ton of value in that as well.
*  But, you know, it's pretty straightforward in a lot of cases to just be like, okay, language model, your job is to write the prompt that would have led to this.
*  And as long as that task is very narrow and consistent, that's probably going to work.
*  If it is a more general setting, then you're going to have probably a little bit more work to do to really engineer that working backward to, you know, make it as kind of information rich and robust as possible.
*  Because it may need to be to get what you want out of it.
*  And so you can see in the paper, there is this kind of color gradient that serves that purpose in this context.
*  I mean, the big picture observation is just like, this seems like a huge step toward the, you know, robot apprentice, right?
*  I mean, the idea that you could have a robot in a random setting, as you said, like take it to unseen places and literally just kind of show it a time or two what to do and get real progress.
*  I mean, you've got even more results coming that speak to that too.
*  But, you know, this is kind of the dream, right?
*  Is that you could bring the robot with you anywhere you want to go, give it a couple of demonstrations and it do the task.
*  And, you know, this is starting to unlock the potential at least for that sort of interaction.
*  So, you know, pretty profound progress.
*  Okay, let's keep going.
*  So the next one is Auto RT.
*  The hits don't stop.
*  Again, this is all just a year's worth of work.
*  We're only halfway through here.
*  This work is really interesting.
*  I understood it in a couple different ways.
*  One is that this is sort of a scaffolding, like a sort of higher level organization scheme to allow a small number of humans to oversee a larger number of robots.
*  So I'm interested to kind of hear, you know, more about how you think about that.
*  Or, you know, could we start to get into something like scaling laws for like how many humans we're going to need now and how many we'll need, you know, per robot later.
*  And then the other big part of this that, you know, certainly made the sort of rounds on Twitter and, you know, entered the meme sphere is like, hey, this is a use of literal, asimov's three laws for robots as the kind of basis of an early robot constitution.
*  And obviously this is going to be a huge challenge and critical, you know, part of this whole project to get right is like, especially if we're really going to trust robots to operate autonomously in the world, even money, you know, we're going to be able to do that.
*  Much more so than language models, right?
*  Like what can you do?
*  How do you as a robot autonomously decide like where the boundaries are for you?
*  And so definitely want to hear your thoughts about the constitution, the robot constitution as well.
*  So the two sides there that I picked up on as being most critical are like scaling oversight and, you know, beginning to delegate more sort of discretion, but trying to do that in a principled way with the robot constitution.
*  The main motivation behind the project was like, let's work with the assumption that maybe we do have what is needed to solve robotics.
*  So this was like after RT1 where we saw like very high performance in domain.
*  So the question is now can we expand the domain a lot?
*  Can we just like scale data sets a lot and then try to see what robot learning looks at that scale?
*  So this project we use like 50 unique robots and around 20 simultaneously.
*  So like maybe what robot learning looks like when you have like hundreds of robots.
*  But the problem with moving robot learning to hundreds of robots is that you cannot actually also do the same by employing hundreds of teleoperation or teleoperators.
*  So you kind of have to rely more on autonomous operation.
*  Once you're trying to increase the data set, collecting data in like classroom settings where you have artificially set up, everything is probably less optimal.
*  So the idea was also can we just put them out in the real world, let them run around and collect a bunch of data and then can we try to see what is the type of learning we can achieve from that?
*  So but once we discuss the question of can these robots of like these large fleets of robots go about in the real world and we don't have as many people, we cannot scale the amount of people similarly,
*  then we have to think about more creative ways of supervision and coordination and acting in the real world.
*  And LLMs and VLMs, they are very smart already and they have they have understanding of zero-shot unseen scenarios already and they can also reason about rules.
*  So if no one's watching the robot, the rules could be watching the robot.
*  So that's where the last game of art like how should a robot behave now that human attention is minimal and what is also like the best, the most optimal way of distributing the limited amount of human supervision that we have.
*  So the way we used human supervision was like you have to speculate the supply of it and then distribute it for like teleoperation on tasks that the robot policies could not do or when they made mistakes.
*  And a lot of the other stuff was handed off to LLMs and VLMs.
*  And because we also did a lot of data collection in spaces with humans and also I think because the robot that we were using had a bunch of limitations such as like not handling liquids or we also our policies are not at the scale where you can handle like fragile objects and stuff.
*  So we had to make rules around like trying to stay away from like unsafe situations.
*  And so this is where the Constitution came out of the foundational laws, which is like absolutely inviolable sort of ethics and then embodiment specific rules and then more environment specific rules.
*  Like for example, you specify that this is a single arm robot.
*  So the task proposal that you come up with need to be achievable by a one arm robot.
*  And the way that I see this in the future is that yeah, in the future you're going to have a lot of robots working in the real world and they're not always going to have supervision.
*  I think one of the inspirations that like well, if you look at humans, right, like we are sort of our behavior is sort of enforced a little bit by laws and stuff.
*  And we are punished for violations of working like there are laws for behaving on the road, behaving in the real world.
*  So I do imagine that in a distant future where robots are out there, we are going to have maybe a robotic code of behavior.
*  I had forgotten to mention that it is a key point.
*  So I'll just reemphasize again that this work is taking the robots to unseen environments.
*  So they're kind of exploring the environment for the first time as well.
*  And, you know, that definitely increases the degree of difficulty and also kind of increases the need for this sort of rules based approach.
*  I feel like this is in some sense, it does feel sort of inevitable.
*  And in another sense, it's like, boy, those stories have a lot of plot twists.
*  You know, there's like a lot of misunderstandings around the nature of the rules and sort of, you know, you give the robot instructions.
*  It doesn't, you know, do exactly what you meant it to do.
*  But then you later realize, oh, well, I wasn't specifying very clearly or the rules are ambiguous.
*  Could you give us a little more kind of of the qualitative experience of like developing this Constitution or what sort of violations did you see of the rules?
*  I imagine you must have kind of gone through an iterative process of like gradually building up more rules.
*  But this seems like a just a really critical area in addition to hardware design itself to actually make these things like work in the broader context of everything that's going on around them in the world.
*  Well, one of the aspects is, as you mentioned, rules are sort of subject to interpretation.
*  And even if you have the same language, there are multiple ways to interpret it.
*  So here's an example.
*  So we said, well, don't do things that are don't interact with anything that's harmful.
*  And I think there was something the data said, which like it's it's not a cigarette.
*  And then it was like, well, I'm not going to get a cigarette because it's going to be harmful.
*  Currently, I think our robots are more the problems don't come from the fact that they are too smart to work around the rules.
*  It's just that I think they are too incapable of doing zero sharp things in the real world.
*  You know, it seems like I guess when I look at the system prompt for chat GPT, of course, it's generally unconfirmed, right?
*  But there have been many credible prompt leaks.
*  And I think probably we have a sense of like what the system prompt is there.
*  And it's like 2000 tokens and has like a bazillion different rules.
*  And yet it's still like very easy to jailbreak.
*  And like, you know, people are constantly finding weird behaviors and unintended things.
*  And so I do kind of wonder, like, is this approach going to work?
*  I mean, is it just a question of like the models aren't smart enough to follow all these instructions?
*  Or is it something more kind of fundamentally problematic going on here?
*  It doesn't seem like chat GPT is just like a couple of, you know, additional actions.
*  You know, additional additions to the system prompt away from like being a secure system.
*  And again, that doesn't really matter, you know, when it's just like putting text on your screen.
*  But the robot case, obviously, you know, we envision a world in which that becomes much higher stakes.
*  Correct. Yeah.
*  So I think I just want to emphasize that prompting by itself and no matter how complicated it is,
*  we are not going to guarantee it.
*  For the experiments that we ran with AutoRT and for the operations that we ran,
*  we also had the controls or the safety guarantees of traditional robotics.
*  So I want to emphasize that these robots were under supervision of the humans.
*  So we had humans sort of have line of sight control over like five different robots or whatever was the ratio of robots to humans that were operating in.
*  And also, especially, I think the failures of chat GPT are slightly different than the failures of robotic systems.
*  Right. Like you, you do things wrong on a UI.
*  Okay. It's just going to say a bunch of things that's wrong or the answer to your math problem is wrong.
*  But then if you kind of do that in the real world, then you could break things or you could run your arm into people.
*  And so the modes of failure are very different.
*  And I also think that, yeah, I think for robotics, it's like safety is mission critical.
*  You're not going to have a robot that breaks things around your house, but then you are fine with a chat GPT that works like 90 percent of the time.
*  Yeah. So I do think that for the specific set of experiments that we ran, there was human supervision.
*  There was a lot of guardrails around like velocities for contact avoidance, like collision avoidance.
*  This is what works right now.
*  But yeah, what we will do in the future, I think, is still an unsolved question.
*  Alignment is a large field of research and it's very complex.
*  I think as robotics research matures more, as we see more robots going out there in the world, I think that safety research of robotics also has to mature.
*  A lot of the safety research was done for classical situations where you had like very tight bounds and specified to map.
*  But now you will need language specification and semantic specification of these safety bounds.
*  And we still have a lot to figure out with regards to safety and alignment of robots.
*  Yeah. Thinking about the recent episode also of chat GPT going insane for like 12 hours.
*  I don't know what percentage of users that affected, but we don't know exactly what the root cause was.
*  But there was sort of a high level statement given that it was some sort of misconfiguration on certain GPUs or whatever.
*  And it could be any number of errors like anywhere in the stack, right?
*  That's not even necessarily an alignment error in training or the model per se, but just even like an off by one error is some sort of encoding mismatch.
*  And the next thing you know, chat GPT is just giving you like schizophrenic responses.
*  And obviously the robot version of that could be quite destructive.
*  Thinking about that and projecting it into this domain, it does feel like there's got to be kind of a whole other level of control with robotics that are like outside the models.
*  You know that either you think about just certain force limitations where like beyond that it just can't handle it.
*  Or you could be any number of sort of other engineering compliments to the kind of alignment measures.
*  But in a sense, it's kind of instructive to think about these as because it is so in some sense, it's like more intuitive, right?
*  The way that the robots can cause problems and the solutions are a little bit more intuitive.
*  And I almost wonder if there's a study to be made of how to control robots, because it is you can kind of get to like, OK, well, if its arm can only lift however many pounds, then that's going to limit what it can do.
*  You know, if it can only move so fast, then that's going to limit what it can do.
*  If it's made of a certain material, it can only handle such impact, then that's going to limit what it can do.
*  And there's like a lot of, you know, perhaps most backporting.
*  So this whole discussion has been sort of and robotics in general has kind of lagged the foundation models a bit due to lack of data, all these things.
*  But in some ways, I wonder if there's like a study of robotics that could be backfit onto these AIs, these disembodied AIs as well and kind of inform the, you know,
*  the surrounding systems that are probably going to be needed to make sure that, you know, your your like more pure digital AIs stay on the rails, you know, so to speak, and don't go breaking digital dishes in their virtual kitchens.
*  Again, it's a fascinating piece just to contemplate the fact that you've got fleets of robots going into unseen places and guided in part by, you know, a proto robot constitution.
*  So the next one then is called Learning to Learn Faster.
*  And this is a project that is emphasizing teachability.
*  And so, again, this is kind of another variation on, you know, two papers ago, we said, hey, wouldn't it be great if you could just kind of draw a quick line and indicate to the robot that you're going to be able to learn faster?
*  How you want it to do or, you know, wave your arm and kind of indicate how you want it to do and here basically doing that now in a verbal way where the robot can do something.
*  And the goal here is to say, can we get the robot to listen to feedback and do it differently the second time learning from what the human has said to it.
*  You know, that might be do that slower and grab the thing lower, or, you know, raise your one hand higher, whatever, of course, lots of examples.
*  I think in a, in a way that is probably familiar to some, you know, app developers who listen to
*  the podcast and maybe could be a source of inspiration for others. Basically it's an
*  iterative process of training on more and more chain of thought style reasoning. And then also
*  you might call it like a tree of thought style, envisioning multiple paths, kind of simulating
*  like, okay, if I do this, what might the feedback be now that I have this kind of training on my
*  actions and the feedback that I'm getting, you can kind of sketch out a few different possibilities
*  and then try to pick from those possibilities, which one is likely to be the best. And that kind
*  of simulation called rollout in the paper showed performance improvement relative to one where
*  you're just kind of picking a path straight away. So again, those are the things that jumped out
*  at me. What else do you think we should make sure we understand about learning to learn faster?
*  What I really liked about this effort was having a very tight feedback loop between users of the
*  system, which are interacting with the model that's learning to predict reward code that
*  controls a robot. Like, and then you could directly see the results of, you know, what the,
*  what the model's response to the user was. You could see the response of like the,
*  the model's predicted reward code when it's actually executed on the robot. You can actually
*  see what happens. All of that was in a very tight loop, right? Where users were actually rating
*  individual responses from the language model, as well as, you know, rating the entire interaction
*  of like, okay, by the end of this conversation, where I'm kind of brainstorming with the robot,
*  acting as a teacher, critiquing the code it wrote for the reward code, critiquing the final kind of
*  improvement that it made, did the robot finally, you know, do the task that I was asking for
*  originally at the start of the conversation. All of that data is kind of logged and incorporated
*  into this notion of teachability. I think this has been like, you know, the tightest kind of feedback
*  cycle that I've seen from our team yet, where, you know, you know, this is the day cycle that
*  we called it, where in the daytime, you have the frozen language model that's been trained on some
*  teachability. It's actually interacting with users who are teaching it more. And in the night cycle
*  at night, overnight, you know, we're actually distilling those kind of like in context,
*  multi-turn conversations with dense user ratings back into that model overnight,
*  but it's ready to deploy again for users in the daytime. This is like a very cool kind of very
*  rapid kind of flywheel that I think takes a different flavor from the other kinds of data
*  engines that we've been considering in the prior works, which are, you know, straight from expert
*  teleoperation to low level actions. This kind of paper is more about the high level, the teaching,
*  the interaction, the usability. And I thought that was a very, very relevant kind of evolution of our
*  team. Now that we do see, you know, so many great other works in language modeling and like, you
*  know, in chat BT and Bard and Gemini, I think a lot of these concepts transfer quite well to domains
*  beyond robotics. It's very intuitive. So if you like try to learn new, new sports, like the
*  surfing or skiing, I feel like during the day, like when you started, it's really hard, but I found
*  that like once you like, if you go surfing for like two days or skiing for two days, like initially
*  it's like really hard and then you go to sleep overnight and then you come back and then you're
*  immediately much better. And I like that in some way, the learning to learn faster paper has sort
*  of mapped it into like a step, Ted said, the day cycles and the night cycles where the day cycle
*  is sort of like in context learning where you collect more examples, but then it's in context.
*  And then the night cycle is like where you go retrain or find if you change the weights of the
*  model. And yeah, I don't know, like there aren't many, I think highly scientifically credible
*  explanations as to why you experience this overnight in when you go like skiing and stuff.
*  So for me, I think the learning to learn faster paper is like an intuitive way of trying to
*  incorporate that into a robot learning. The second thing I really liked is the rolling out of the
*  futures. And you do kind of take the shortest possible future, and then you like retrain from
*  that data until you also get more efficient in using the human feedback. But one challenge here
*  is anticipating the quality of conversations, not just from the length can be much more complex
*  than that. If you rate as to, I think more than the length, people also care about the aspects of,
*  there are other aspects of interactions with humans that you care about. Like,
*  did you get the right code? Is it responding correctly to feedback? Is it steerable, et cetera?
*  And so I think, yeah, this capturing or the rating of quality needs to be probably more
*  multimodal than showless path search. So pivot is a demonstration that vision language models
*  can be used to control robots out of the box. That's kind of how I interpreted it.
*  Basically, what happens here is you take an image, you kind of scatter some numbers on top of the
*  image and present that to a vision language model, and then give it an objective and say, okay,
*  given this objective, you know, your job is to pick up the code can or whatever,
*  which number is the number out of all these numbers that you've overlaid on the image that
*  the robot should move its hand to? And the vision language model, perhaps not too surprisingly at
*  this point, you know, can do that. And then there's also an iterative process there because
*  as I understand it, if the initial numbers are kind of pretty randomly just kind of scattered
*  onto the image, but then once we've picked one, now we can kind of scatter another set, but like
*  clustered around that first choice. And so with a couple of rounds of iteration, then you can really
*  zero in on where the robot needs to go to accomplish the objective. And then of course,
*  the robot can follow those instructions. I'll confess I didn't have a great sense for like
*  how this fits into the overall big picture. It seemed like, you know, I could kind of connect
*  it back to like drawing the line trajectories, but I feel like I was maybe still missing, you know,
*  the deeper connection on this one a little bit. Yeah, I think that's overall pretty good summary.
*  I would say maybe one side correction too, is that the numbers are also associated with actual
*  arrows that are procedurally generated, which represent motion. But I think beyond that,
*  you're absolutely right that we're leveraging the VLM as kind of a zero shot frozen critic,
*  right? Of, you know, directing which of these out of these directions that we already present,
*  you know, in a manner that's easy to understand for the VLM just by visual annotations,
*  which of these annotations is the one that's better for the task at hand and the VLM can kind
*  of choose and we kind of optimize over that. But I also empathize with your kind of view that,
*  you know, this is kind of like an odd one out in the work we discussed today, which those are
*  really about building, you know, fine tuning end to end models, training them for robotics tasks
*  on a lot of data, scaling them up in the real world. And then out here in pivot, I view this
*  more as kind of like a very, just a result that was so exciting about a trend that we found that
*  we didn't really, you know, know if other folks in the community were thinking about.
*  And we kind of just wanted to share that, like, you know, this is actually a very surprising
*  result. The fact that like these pre-trained internet scale VLMs can also understand some
*  notions of motion, of causality, of robot trajectories, of contact. This was a bit
*  surprising, right? Because in a lot of, you know, our, even our own team's perception and,
*  you know, to be honest, most of the community right now in both like language modeling and
*  robotics, it's like, oh yeah, of course, like there are so many things in robotics that we
*  have to tackle ourselves. The very, you know, dense contact, spatial reasoning, left, right, up, down,
*  all of these things are concepts that aren't contained in Wikipedia and Reddit and, you know,
*  image generation data sets. These are things that we need hardcore robotics data for.
*  And perhaps recently, you know, you know, for example, with this work Pivot,
*  maybe the answer is that actually there is some very good amount of physical intelligence already
*  contained in these like internet trained models by themselves without any robot data pre-training or
*  fine tuning. Again, I don't, I also don't think that like internet data alone, just watching,
*  you know, Reddit threads and Wikipedia is enough to solve contact rich robotics. But I do think
*  that we've so far just been like seeing the tip of the iceberg for the knowledge that is already
*  contained in these, you know, large VLMs. And with Pivot, right, by showing that if you have this
*  external kind of prior, this inductive bias of having this robust optimization problem and making
*  it very easy for the VLM to just like, you know, pick and choose in a multiple choice setting,
*  which of the directions, you know, that the robot should go is correct. And you kind of run multiple
*  iterations and you show that you can kind of like better drag out the vibes or the implicit
*  knowledge contained in these VLMs a little bit better. Again, I still don't think it's the results
*  are like, we just take Pivot and you can apply it to any robot and it's just going to work off the
*  shelf. I think it's definitely that the performance is very, very far away right now from let's say
*  Archie two or any kind of fine tune policy. But the fact that it even kind of shows very promising
*  signs of life was unexpected. And I, and I hope is inspiring to others as well.
*  In addition to the zero shot, I think it's also that it can specify tasks in a multimodal fashion
*  that I found very impressive. So there's core as policies type approaches where like
*  they're VLMs or LLMs off the shelf, they write code for robots through our figure out how to
*  use the robot APIs. But then you realize that a lot of tasks are under specified in language and
*  you kind of do need the image domain to like, let's say folding a t-shirt. Like if you were to
*  tell me in language how to fold a t-shirt, that would be, yeah, very hard to do. But then if you
*  show in an image like where to move as you're folding the t-shirt, I think this would work much
*  better. So for like highly dexterous stuff. So I can imagine. So right now we are seeing the trend
*  that zero shot while in the past, like RT one, RT two was collecting a lot of data and doing a lot
*  of training. Now we are seeing that these VLMs, these large pre-trained VLMs already know a lot
*  about robotics zero shot. And then the effort becomes how to correctly leverage their knowledge,
*  like how to most efficiently leverage that knowledge. So that we collect the least amount
*  of data and we collect the data that's most complimentary to the things that they don't know.
*  Yeah. So I think there are some interesting applications here for maybe dexterous robotics
*  or maybe tasks that are more specified in a multimodal. So we've got RC two, which pulls
*  generality out of vision language models. We've got RT X, which shows generalization across
*  different robot embodiments. We've got our T trajectory, which is about doing these little
*  sketches on the fly and learning from these like line drawings. We've got auto RT where we start to
*  have scalable oversight at a robot constitution. We've got verbal feedback in learning to learn
*  faster. And then the zero shot VLM guidance for robots out of pivot. So this is obviously a ton
*  of stuff. Again, from the first comment, it's all working, but where are we going from here?
*  One could imagine an understanding of these results where it's like, we've got 50 more of
*  these papers before we're going to be anywhere close to having a system that we really think
*  could be like used reliably to do useful work. Or I could imagine that it's like,
*  hey, if we just jam these on scale a little while longer and also kind of integrate all of them into
*  a single system that we might start to get pretty close. Where do you think we are right now in the
*  journey from like research to, eventually this is going to be like a scaling, an engineering
*  scale up project, right? So where are we on that question? It's hard to answer that. And different
*  people have various personal opinions about this. I still think that the data is a hard problem to
*  track in robotics. So you could think that you can scale this up by spending a lot of money and scale
*  up the data collection, but there's also a more efficient way to scale this up, which is to make
*  your policies more sample efficient, more data efficient. So instead of spending 2X money, if you
*  double the data efficiency, then you need just half of that effort. And I think the state of the art
*  or that a lot of people use is like the RT2, but we do understand that there are some gaps in
*  its reasoning. And I still think that we probably need to make a couple more breakthroughs before we
*  can sort of make this a scalable engineering problem. And the second thing is, like Ted said,
*  a lot of these are showing initial signs about how to maybe use VLMs and other things more zero
*  short, which is clearly pointing towards a trend. But we really need to now build learning methods
*  on top of these highly performant zero short methods and also sort of iron out the knots.
*  And you could argue that even if some methods have high zero short performance, they may not have the
*  best learned performance because they may not go to like 100%. So there are still a lot of gaps in
*  how you might want to... Like the right interfaces between robotics and foundation models still
*  needs to be worked on, I think. Yeah. I think you said it perfectly. The one thing I'd probably add
*  is I 100% agree that we are a few breakthroughs away from general purpose robotics. That it's the
*  dream that we all are working so hard for. I think, again, if you want something commercially
*  viable, something that will maybe make money or help some people in the world, I think a lot of
*  those ingredients are already ready to have a larger impact than maybe even just a few short
*  months or years ago. But for the true full vision of embodied AGI, I do think there is still
*  fundamentally a few open research challenges left. I think a lot of the trends we see today
*  with the papers we discussed are probably directionally pointing in roughly the areas
*  that I think are particularly open-ended still. But again, I don't think we have the full recipe
*  just yet to say it's all solved, the research is done, we can just scale it up. Could you give a
*  sketch of kind of what you think the big things are that you will be tackling next? And I'm also
*  kind of curious as to how you see Google DeepMind's role in this going forward. This is all very
*  research, it's still being published in a world where increasingly a lot of frontier language
*  model or multimodal model research is obviously much less published these days. Should I expect
*  to have a Google-branded robot in my home at some point? Is that the sort of long-term vision that
*  you guys have? So yeah, two parts are like, what are the big gaps that you're wanting to
*  take on next? And what is that big long-term vision specifically for Google?
*  Specifically, I don't want to speak on behalf of Google. And I think a lot of the ideas for
*  how to commercialize is still being discussed and making this a business is also a very difficult
*  problem. It works in narrow domains, but generalist robots, I think, are generalist robots that are
*  reliable and safe are still some time away. There are many aspects to bringing them to people's
*  homes, like the business aspects need to be figured out. I think, yeah, I don't want to speak to
*  Google's plans for that. Personally, I think the research that I'm now interested in this year is
*  RT1, RT2 have very little zero-sharp performance. You get most of the mileage from our data or
*  motion is learned from our data. But we are seeing signs that large foundation models, zero-sharp,
*  can do a lot of things, but they have not been adapted to be learnable methods. So I think one
*  hypothesis is, yeah, we can improve the interface of robotics with the foundation models. The
*  interface that RT2 has is sort of like the score training, but actions are very different still.
*  So you have these vision, language, action models, but actions are the weakest part of that link.
*  And there are multiple hypotheses. One hypothesis is, do we actually need actions? Can we still
*  capture a lot of the domain in the task space through vision and language by making actions
*  more like code? There are some initial results on like code as policies on prompt book, paper,
*  which showed that zero-sharp prompting of robot of VLNs and multimodal code generation
*  have some signs of very high performance. But then how do we make sure that this gets to 100%?
*  How do we make it learnable? How do we iron out the knots there? The second thing is like
*  bimanual robotics and more dextrous tasks. What we currently showed sort of transferring dextrous
*  domains is still, I think, unsolved. I think we need better representations to do dextrous
*  tasks better. So what are they exactly and how to scale them? Yeah, I think, I mean, that's very
*  exciting research agenda for the team. I think for me personally, I think the thing I'm most excited
*  about is also kind of going beyond language. I feel like language, we've seen a lot of great
*  progress and a lot of great reasoning from the help of internet scale pre-training. But I'm very
*  curious to know what is it that is unique about the embodiment problem? I think on the manifold
*  of different reasoning and skill concepts and capabilities that foundation model needs to tackle,
*  does robot actions and causality and physics, does it live in a little corner by itself or
*  is it kind of ingrained and spread throughout all of the other types of reasoning that all of the
*  data that humanity has generated captures? I'm curious about that. I would like to figure out
*  how we can better increase the bandwidth that we do have between robot data foundation models and
*  normal internet foundation models. I'm interested in studying how much robot data is needed when we
*  talk about scaling that system up. Is it just like the cherry on top, a little bit of robotics data?
*  Is it like 10, 100, 1,000, a million times more data? I think all of these very interesting
*  scientific questions, again, about the nature of what it actually requires to be able to solve
*  physical motion level reasoning at a very low level actions. I think these are very interesting
*  questions to me and I think are really more about the scaling laws of robotic capabilities
*  that I feel like right now in today's day and age we don't have a great understanding of.
*  And I hope we have a better understanding of it throughout this year and next.
*  Alrighty. Well, Keerthanugopalakrishnan and Ted Zhao, thank you for being part of the cognitive
*  revolution. Thanks, Nathan, for having us. It is both energizing and enlightening to hear why
*  people listen and learn what they value about the show. So please don't hesitate to reach out
*  via email or you can DM me on the social media platform of your choice.
