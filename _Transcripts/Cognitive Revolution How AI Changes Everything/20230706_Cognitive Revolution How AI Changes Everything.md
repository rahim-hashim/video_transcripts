---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 5636s
Video Keywords: []
Video Views: 4020
Video Rating: None
---

# AI Scouting Report – Part 1 of 3: Fundamentals
**Cognitive Revolution "How AI Changes Everything":** [July 06, 2023](https://www.youtube.com/watch?v=0hvtiVQ_LqQ)
*  Hello and welcome to the Cognitive Revolution.
*  Today we're changing up the format and I'm presenting part one of my AI Scouting Report for June 2023.
*  The AI Scouting Report is my attempt to zoom out from all the day-to-day AI news and hype
*  and help you focus on what really matters.
*  I'm synthesizing the most important concepts and trends that I've obsessively studied for the last two years
*  so that you could begin to engage with AI research, products, and discourse with a new level of sophistication.
*  This is the first edition of the AI Scouting Report and we're presenting it in two parts.
*  Part one, which I'm sharing today, aims to cover the core fundamentals of AI as simply, clearly, and literally as possible.
*  Starting with the headline summary of current general purpose AI capabilities,
*  and then surveying how modern AIs are designed and trained,
*  what the big capability unlocks have been,
*  and what we know about how they work and what they truly understand.
*  Obviously, I'll be simplifying a lot,
*  but I'd consider it a huge success if you come away with the equivalent of a high school AP course understanding of machine learning fundamentals.
*  I've curated a bunch of the very best graphs, illustrations, and figures that I've found,
*  and I hope to explain them so that they make as much of an impression on you as they have on me.
*  To do that in just 90 minutes is ambitious. I think we can do it,
*  but we will need the help of visual aids, and for this reason the AI Scouting Report series will be a YouTube-only feature.
*  We'll continue to post short audio-only episodes to the podcast feed to announce each new episode as it's released,
*  but you will need to watch the video to get the full experience.
*  Part two of the AI Scouting Report, coming soon, covers AI as it interfaces with the world,
*  the latest trends in fine tuning, in agent design, memory systems, as well as market dynamics, economic and societal fallout,
*  AGI timelines, live players, and the outlook for AI safety.
*  Before getting started, I also want to share that the AI Scouting Report is brought to you in part by Athena.
*  Athena is an executive assistant services company that pairs EAs in the Philippines with startup executives and other
*  opportunity-rich, time-poor clients around the world.
*  If you're a regular listener to the cognitive revolution, you know that I've mentioned my AI advisory work with Athena a couple times over the last few months,
*  but what I haven't told is the backstory of how I originally started with Athena as a client
*  two and a half years ago while I was still CEO of Waymark.
*  I matched with a woman named Charisse, and we started with typical EA tasks, email and calendar management, social media,
*  ad hoc research projects.
*  She did well, and I got a lot of projects done that I simply wouldn't otherwise have been able to get to.
*  But things got really interesting when we made the move to generative AI.
*  I found that the same core qualities that made Charisse a strong EA,
*  natural organization, high attention to detail, a sense for the importance of outlier data points,
*  facility with software, tolerance for some repetitive tasks, ability to balance speed and accuracy,
*  the curiosity to ask why, and the inclination to be proactive.
*  All of these made her a natural AI operations pro as well.
*  So over the last two years, working on our time zone, Charisse has built a variety of critical data sets, has developed tons of prompts,
*  fine-tuned and validated more than a hundred custom models,
*  maintained dozens of elaborate spreadsheets, and pitched in in many other ways.
*  At this point, it's no exaggeration to say that she's become a core part of the Waymark team.
*  And it was this experience with Charisse that inspired me to think about working with Athena as an AI advisor,
*  to see if I could help the company replicate this success story across its unique client base.
*  I've been advising the company for about six months now with a focus on foundational AI education for EAs,
*  and the creation of a task automation practice within Athena.
*  We've now developed an AI 101 core skills class that covers prompting and savvy shopping.
*  We've extended many of the Athena delegation playbooks with AI prompts, and we've developed some early task automation best practices and templates as well.
*  Fun fact, the first audience after my wife Amy to watch this AI scouting report was in fact a group of 200 Athena EAs.
*  One of Athena's core values as a company is always long term.
*  That, of course, is a bit tricky in this crazy, fast moving AI environment,
*  but the company is investing in the human capital needed to ride the AI wave.
*  And we're planning to share our experiments, findings, and automation templates with clients as much as possible.
*  Like everything in AI right now, it's still a work in progress and subject to all sorts of change.
*  But we do feel at this point that we are as well positioned to help clients ride the AI wave as any EA company in the world.
*  Now, to be totally upfront, this service definitely isn't for everyone.
*  It runs $3,000 a month, and that's enough to fund a strong salary in the Philippines,
*  enough in fact to recruit management staff and managers to help you get the job done.
*  Enough in fact to recruit management level talent that will work on your time zone and really integrate and fully support your life and team.
*  Athena is willing to invest in listeners of the cognitive revolution by offering a first month of service entirely free for qualified customers.
*  To claim this offer, you can visit my personal referral link.
*  That is athenago.me slash Nathan dash Labenz.
*  That's athenago.me slash Nathan dash Labenz.
*  Of course, we'll place a link in the show notes as well.
*  Now, without further ado, here's my AI scouting report from June 2023.
*  All right, so let's get into presenter mode.
*  Yeah, let's do it.
*  And here we go.
*  So this, my friend, is the AI scouting report from June 2023.
*  Presented this at an Athena client day event in San Francisco a couple weeks back and excited to share it with you as well.
*  Yeah, heard it was great. Excited.
*  So the basic idea here is just coming at this from the perspective that most people really need a crash course to catch up with what's going on in AI.
*  It's all happening so fast. There's a ton of headlines. There's a ton of hype. There's a ton of dismissing of the hype.
*  But a lot of just have not even had a chance to understand the fundamentals of where are we? How did we get here? How does this stuff work?
*  What can we really say about it? What's going on right now that is actually worth paying attention to?
*  What's the impact of all this going to be? People are kind of jumping to that, I think, a little too quickly and glossing over some of the foundations that
*  would hopefully give them a much better ability to interpret the news and just kind of understand what's going on and the tools that they're beginning to encounter in their daily life.
*  So the hope here is that this will be something that is very accessible.
*  I was kind of joking at the event that because in San Francisco, you go out there, you may very well have some other AI experts in the audience.
*  And I said, there may be people in the audience that know everything that I'm going to say. And if so, that's great.
*  But this then hopefully becomes the thing that you could take to your mom that's like packaged up enough that you could say, all right, mom, here's here's.
*  Oh, you know, you ever wanted to know what I'm working on all the time? This is the, you know, the short version that gets you kind of up to speed.
*  I am going to take a pretty hard stand against analogies in doing this.
*  I think, you know, there are not to say there's never a place for analogies, but unfortunately, I do think that they confuse and kind of mislead more often than they really prove close.
*  And I'm clarifying to people, so I try to avoid them.
*  And I'm also staying away, at least for now, you know, I'll extrapolate trends a little bit up to kind of, you know, end of this year and give a little sense of where we're going.
*  But this is not the place for like big picture, you know, bold predictions of like, you know, what 2030 is going to look like or anything like that.
*  It's really kind of what is happening now, stuff that actually exists, you know, what can we understand and what can we say, just limiting ourselves to that.
*  So headlines, you know, it's pretty crazy, but we are basically here.
*  We are at this moment now where AI has kind of reached what I call human level.
*  And, you know, we'll unpack exactly what that means.
*  But I think we actually hit this point just a little over a year ago.
*  This is a quote from Google's Palm paper out in April 2022.
*  And they use this giant benchmark called Big Bench, which is a set of 150 different tasks.
*  And they built this Palm model and they compared its performance to humans.
*  And they found that the average performance score of the model beat the average performance of the humans that they hired to do these same tasks.
*  So this is on page like 44, something of this paper.
*  And I call it like the greatest buried lead of all time, because, you know, this is a pretty critical threshold, I would say, where now for most, you know, just random tasks that you might have.
*  It's pretty plausible that an AI could do a better job on it than a random human.
*  And you might say, well, like, who are these humans that they were using? I actually did go in and look that up because they credited them in the paper.
*  I went like, Google, like, LinkedIn searched every single one that I could find.
*  And basically, they were employees of a software QA firm.
*  That typically do things like testing games, testing software products, finding reporting bugs, documenting issues.
*  Most of them are college graduates, and they were all gainfully employed in the modern economy.
*  So this is like not, you know, I would say it's a fairly reasonable, you know, kind of average employed person.
*  Again, most of them college graduates. So that's a big deal. And I think we kind of understate that.
*  There's definitely more nuance to unpack, but, you know, it's a pretty big headline that we now have human level AI.
*  To go even one step further, and we did a whole episode on this with Vivek from Google, who was one of the lead authors on the Medpalm 2 project or Medpalm and Medpalm 2.
*  The state of the art AIs, and when you see this SOTA, that's state of the art, you'll see that fairly often.
*  State of the art AIs are closing in on human expert performance when what the human expert is supposed to do is quite well understood and documented.
*  So in this context of medicine, there is something called a standard of care, which is like what you're supposed to do, like what the right answer is, you know, when somebody shows up with a particular question.
*  You're not supposed to be making it up as a doctor, right? There is supposed to be some kind of standard right answer.
*  And in those kinds of domains where that is well established and well understood, state of the art AI is closing in on expert level performance.
*  So this on the left is the chart on this medical QA benchmark, which is basically like the medical licensing exam that doctors actually take to become doctors.
*  This is the performance on that over just the last two and a half years.
*  60%, by the way, is a passing score.
*  So chat GPT was the moment when AI started to be able to hit basically passing score on these exams.
*  Now, just six months later, Medpalm 2 comes out and you've got 86%.
*  That is considered to be expert level performance.
*  And Google, for all the talk that there's been about, well, they're too slow and they're too shy about this technology and they don't, you know, do they really believe in it or whatever?
*  They've been pretty clear about this saying that it does match expert level performance.
*  They then go deeper on the right. You start to think, OK, well, maybe it got answers right or wrong, but can it really support patients or do a good job in a true sense?
*  Obviously, there's a lot more to medicine than question answering.
*  But here they look at nine different qualities that you would look for.
*  And the setup here is you take the AI answer, you take the human doctor answer, you present those both to human doctor evaluators and you say which did more of these good things and which did more of these bad things.
*  So the top four are the good things and the orange is how often the AI was judged to have done more of the good thing.
*  And you can see it's pretty much dominating the top four.
*  AI is winning that category basically 70, 75 percent of the time.
*  In the middle is where it was deemed to be a tie and down here, you know, 10, 15 percent is how often the human answer was deemed to be better reflecting the medical consensus than the AI answer.
*  So the AIs are definitely winning the positive traits.
*  Then you go to the next category, which is the AI answer.
*  So it's this one of more inaccurate and irrelevant information is the one where the AI was judged to have brought more, more often, more inaccurate and irrelevant information.
*  So it wins eight of the nine categories as judged by human evaluators.
*  So, I mean, boy, that happened pretty quick.
*  Now, where would you draw a line?
*  You know, it's tempting to say here, OK, well, this do we already have AGI then?
*  Or is this like, you know, is this going to take over the world?
*  The point about a standard of care or some sort of standard body of care is that AI is going to be the best answer.
*  So, where would you draw a line?
*  You know, it's tempting to say here, OK, well, this do we already have AGI then?
*  Or is this like, you know, is this going to take over the world?
*  The point about a standard of care or some sort of standard body of knowledge that the AI can train on and master is really critical here.
*  If you try to move outside of those kinds of areas, for example, to frontier science and you say, can state of the art AI do work on the frontier of science?
*  You can go back and check out the Red Team episode from our archives if you want to hear the story of me, you know, kind of freaking out about GPT-4 in the early days and getting really focused on this question.
*  But I've basically looked at this from every angle and read all the all the research that I can.
*  And both from my experiments and from published work, it seems pretty clear that at this point, even the best AIs cannot do or lead a science project.
*  I specifically would focus in on what is science and what is kind of the core activity there?
*  I would say that it is the ability to identify non-obvious hypotheses that are actually likely enough to be true that it's worth investing the resources to run the experiments and find out.
*  That's the kind of insight you could say like the eureka moment that the best human scientists sort of still magically mysteriously managed to pull that off.
*  And that's where real advances happen.
*  Right. Somebody identifies something, a theory that, hey, this isn't obvious and it might not even be right.
*  But some sort of intuition, some sort of insight makes me believe that it's worth investigating deeper to find out.
*  If you ask an AI to do that today, even the best GBT-4, you're going to get kind of middle of the road stuff, stuff that's like pretty well trod already kind of explored.
*  I haven't really seen anything that takes you out to the edge.
*  And it's like, oh, my God, that is a genuine insight, the likes of which only a leading human scientist could have.
*  That does not seem to be happening today.
*  So I think that's pretty important. So I said human level.
*  I want to emphasize and I think this is also super and super important.
*  Human level does not mean human like right.
*  These things have very different.
*  You know, they're made of different stuff and they're they're created in different ways.
*  They learn in different ways and in practical terms, they're very different strengths and weaknesses.
*  Hey, we'll continue our interview in a moment after our word from our sponsors.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it to use Cogrev to get a 10 percent discount.
*  So borrowing a little bit from boxing, I wanted to just do a quick tale of the cognitive tape and kind of run down this list of different dimensions of cognitive ability.
*  And just reflect for a second on like where are the humans still ahead?
*  Where are the eyes maybe already ahead?
*  Because it is, I think, quite informative just to look at it on this more granular level.
*  So, first of all, breadth.
*  A.I. is dominant here.
*  GPT four knows something about everything, right?
*  It speaks all the languages, it's read all the books, it knows all the history.
*  It may still, of course, as we know, it will still like get some stuff from time to time.
*  But it knows way more than basically any human.
*  And I'm comparing here to human expert as well.
*  You know, people go deep in a subject.
*  And when we get to depth, we do see the human expert, as I kind of alluded to with the science part.
*  Humans still do have better depth when they are true experts in their domain.
*  But the A.I. way better on breadth and stronger than as we've seen, stronger than the average person, even on depth.
*  Kind of approaching into that like college student, you know, maybe even early grad student level of expertise,
*  but definitely still short of the depth of a true human expert.
*  Already covered the breakthrough insight that right now I would say is humanity's biggest edge.
*  We can come up with these novel ideas that are actually worth something.
*  And A.I. still basically can.
*  One caveat there, too, is narrow systems sometimes can.
*  So somebody might be thinking, well, geez, what about like alpha full?
*  Didn't that like solve the protein folding problem?
*  It isn't that like a total, you know, kind of revolutionary insight.
*  You could kind of see that different ways, I suppose.
*  But that, in my mind, is a narrow system designed for a very specific task.
*  And the insight there, you know, really depends on the designer's ability to frame the problem the right way,
*  to architect the system in the right way, to train it in the right way.
*  And then, yes, it can understand how to fold proteins in a way that humans can't.
*  But that's all it can do. Right.
*  So when I'm looking here, I maybe should adjust this to say like general purpose A.I. like a GPT-4.
*  There are A.I.s that are superhuman in these kind of narrow protein folding like problem domains.
*  But figuring out how to build an alpha fold in the first place,
*  that's something that only a human scientist, you know, human researcher can do today.
*  Speed and cost, you know, those are big areas of advantage for A.I., obviously.
*  I actually take a pretty modest number here and say that an A.I. might be ultimately something like
*  10 times faster and 10 percent the cost, 10 times cheaper, you might say.
*  And, you know, people sometimes are like, well, that seems like it's it seems like the ratio would even be higher.
*  And it certainly depends a little bit on how you think about it.
*  I try to think of it from kind of a total cost of ownership standpoint.
*  If you just naively say, hey, human, you know, can you write me a two page essay and then, hey, GPT-4,
*  can you write me a two page essay there?
*  You might see like 100 or even a thousand fold difference in speed and cost because the A.I.
*  can generate a couple of pages for a couple of cents and you might pay a hundred dollars for that,
*  you know, for a person.
*  I know it'll certainly take a lot longer.
*  It takes just a few seconds for the A.I.
*  But if you're really starting to build this into your business, you're, you know,
*  you're starting to do some task automation and you want to put something that's not just a one off kind of,
*  oh, look how quick and easy it did that.
*  But you're actually trying to kind of establish some standard and really ensure that there is performance
*  that you can count on.
*  Then you're going to put time and ultimately time is money into setting up the, you know,
*  workshopping the prompts, you know, defining the inputs and outputs, even just validating,
*  you know, can take a lot of time.
*  You're going to have subject matter experts in your organization that you're going to need to go spend
*  time with and be like, hey, what are you actually looking for in this task?
*  And, you know, is this output satisfactory?
*  And you're probably going to have a few rounds of that before you really dial into something
*  that everybody agrees can work.
*  So over time, I do think you can save, you know, a ton, right?
*  90% savings is, I mean, that's the majority, right?
*  It's a huge deal.
*  But I would still say, you know, be prepared as you go to implement this stuff that you are going
*  to put in some time and some effort up front.
*  And so your savings is not going to be like total, but it could still be, you know, order of magnitude.
*  Next up on availability and parallelizability, I would say this is AI's biggest edge right now.
*  You know, the AI just kind of sits there doing nothing.
*  It doesn't consume any resources.
*  It doesn't, you know, it doesn't need to eat until it's called.
*  And then when it's called, it can kind of quickly spin up.
*  It can do its task.
*  You can do 10 or 100 wide at a time, a thousand wide.
*  In practice, you know, we have rate limits these days with, you know, GPT-4 because they can only
*  support so much with the computers they have available.
*  But in principle, you can kind of scale this out as wide as you want to.
*  So you can take, you know, a task that once you kind of have everything dialed in,
*  the clock time efficiency can be pretty dramatic.
*  And that can be a huge advantage for AI relative to human labor.
*  It's also, again, the availability, right?
*  If I go hire an upward contractor to do something next time I want that thing done,
*  that upward contractor might not be available, but the AI is going to be available.
*  My prompt just sits there.
*  I can, you know, I can come back to it at any time in the future.
*  So that's a huge advantage.
*  Time-rise and memory is definitely currently an advantage for humans.
*  We have this kind of sense of like who we are and our, you know, our identity and our memories
*  and, you know, kind of a coherence of what we're trying to do and the, you know, working toward goals.
*  The flip side of the availability and the parallelizability is the AI doesn't really
*  have that by default yet.
*  We've talked a lot in various episodes about, you know, you've got a finite context window.
*  Everything kind of has to fit in there.
*  And if it doesn't, then you kind of have to start, you know, figuring out how you want to
*  augment the AI system.
*  People are working on that with a ton of energy right now.
*  And I'll show some of the, you know, the recent trends in that area.
*  This might be the next big shift.
*  This might be kind of the big, the next big unlock for AIs is to kind of create this memory
*  layer and kind of allow them to work more as long-term agents.
*  But as of now, that's still pretty early.
*  And, you know, humans definitely have a major edge when it comes to kind of coherence.
*  You can also imagine, by the way, that in principle, an AI could be better than humans.
*  Our memories are certainly very finite, right?
*  We're by no means like the pinnacle of memory capability.
*  But just for now, at least, we are ahead of these generalist AIs.
*  Next one I think is super important is technology diffusion speed.
*  That is to say, when something new comes available, how quickly can it spread?
*  Humans don't do that well at this.
*  Recent surveys have said, like, you know, the majority of people have now at least heard of
*  chat GPT, but still like only one in five people have even tried it, even once.
*  So, you know, people are just kind of content to let amazing technology exist and not necessarily
*  embrace it.
*  When, on the contrary, architectural improvements happen for AI, they can get adopted extremely
*  quickly.
*  And we've seen kind of, we're starting to see these waves of like, oh, you know, for example,
*  we did this part of the conversation with the Mosaic ML guys was about the alibi.
*  Positional encoding scheme that allows for much larger context windows.
*  And that is happening quickly across the industry because, you know, it's relatively
*  simple to swap out the old version and swap in the new version.
*  And, you know, everybody can kind of take advantage of that pretty quick.
*  This paper on natural selection favoring AI over humans, I think definitely one to
*  give a little thought to.
*  And it's based on a lot of things like this, just how quickly they can take advantage of
*  new improvements.
*  And finally, bedside manner.
*  I think this is one that people often kind of fall back on and say, well, you know,
*  AI may be able to do this or do that, but it's never going to replace the human touch.
*  You know, it'll never have that connection with people.
*  And I think, unfortunately, that is at this point.
*  And, you know, maybe just to cope, we're already seeing things where using an AI
*  can help doctors, for example, be more empathetic.
*  This was a big part of the episode that we had with Professor Zach
*  Kahane, who's the Harvard Medical School professor who got early access to GPT-4
*  and found incredible uses across really the entire range of medical practice.
*  But one of the big ones was just, you know, doctors are overloaded.
*  They don't have time to sit there and really write the most empathetic version of their
*  communication to their patients.
*  So a lot of times it's just kind of short and quick and that's all they have time for.
*  Running that, you know, taking the draft of the message from the doctor, putting it through
*  an AI to say, hey, can you say the same thing, but do it in a more empathetic,
*  you know, understanding sort of way that really helps just even giving them reminders that,
*  you know, this is a sensitive topic and, you know, you might want to kind of present it in this way.
*  You know, the AI can help doctors be better at things, you know, as foundational as
*  bedside manner and, you know, thinking back to the episode with Eugenia and Replica too,
*  you know, there's no, you know, no real reason to believe that the AIs are not going to be
*  pushing our emotional buttons in all sorts of ways going forward.
*  Any questions there? What do you think of the tail of the tape?
*  No, I think it's a great sort of table to help make sense of stuff and kind of assess the relative
*  strengths and weaknesses.
*  I think the, I mean, I often think to your statement around, you know, AI servants,
*  not scientists going to the breakthrough insight. I assume we'll get to that later,
*  but I want to spend some time on why that's important to you.
*  Yeah. Well, I think when we continue to build toward that, then we will get back to it later.
*  But, you know, the short version is there's a lot that we don't understand about these systems.
*  And, you know, it seems quite possible that we might be able to push their performance to a level
*  where they might be able to start to have these breakthrough insights.
*  And I'm just really not comfortable going there before we have some sense of why they do what they
*  do. So next section is kind of breaking all that down and then, you know, kind of build it back up
*  toward the end, toward the why we should be a little, you know, cautious about AI scientists.
*  So how did we get here? Generally speaking, you know, people are aware that the inputs to AI
*  are data, compute, and algorithms. You've got to have data to learn from. You have to have compute
*  to crunch the numbers and do the, you know, actually do the process of learning. And you
*  have to have an algorithm to actually make it work. I think, and this is something I've been
*  thinking about a lot lately, that at this point, we should really be pretty confident in the view
*  that once we had web scale data and web scale compute, it was really only a matter of time
*  before somebody figured out an algorithm that would work. And in fact, like this has been
*  predicted. So, you know, I frame this as Kurtzweil was right. I've been using the phrase Kurtzweil's
*  revenge. This is a slide from a Kurtzweil book in the late 90s. And, you know, this, he was kind of
*  derided for a while because like, oh, it's so naive. It's just a curve. And, you know, what
*  Moore's law isn't really necessarily holding anymore and whatever. But you look at the curve
*  that he's got here and it basically has the trajectory intersecting with one human brain
*  right around 2020. And then you look at the actual size, you know, how much compute has been put into
*  models. And now this takes us up through present going way back, you know, to early systems and
*  through many orders of magnitude up and up and up and up and up. And somebody did this estimate,
*  you know, I wouldn't in general with these slides, like you don't need to get bogged down on any one
*  particular number, right? It's, we could argue about, is this the right estimate? This estimate
*  is by the way, supposed to be how much computing has one person done over the course of like 40
*  years. Now, is that the most relevant, you know, thing to even estimate in the first place? And is
*  this estimate quite right? You know, I don't, I'm not trying to defend that, you know, down to that
*  level of specificity, but, you know, you could move it. You say if it's 10 to the 24th, you could
*  move that down to 10 to the 22 or up to 10 to the 26. And it's still going to be kind of generally
*  in this area, right? It's still going to be broadly right around where the biggest AI systems
*  are today. So it does kind of all come together that, you know, the trends of the giant data and
*  the giant compute, we're just kind of waiting for some algorithm to unlock them. And sure enough,
*  it seems to be happening more or less right on schedule as, you know, Kurzweil had predicted it
*  25 years ago. Not human-like, but human-level. So the actual algorithm, you know, I want to
*  emphasize, I don't think this is the end of history. You know, this is a big, the big point,
*  right? This is something, this is kind of the first thing that we've found that really has a
*  lot of legs. That's really working across a lot of different domains, you know, a lot of different
*  problem types, a lot of different data types, a lot of different variations on it. But I'm pretty
*  sure that this is just one thing, just like the human brain is just one thing. I don't think either
*  the human brain or the transformer are the end of history, but this is the thing that we kind of came
*  upon first that really is working in a wide range of areas. So the transformer, you know, basically
*  what it is, is an information processing circuit. It takes information in and it passes it through
*  the circuit and it does a bunch of transformations to the information as it goes until it finally gets
*  to the end and it spits out outputs. There is a ton of vocabulary on this and actually I'm thinking,
*  this is probably not going to ever work, but thinking about a project of trying to come up
*  with a new vocabulary to make these terms more intuitive for people because a lot of these terms
*  are really more rooted in the history of machine learning than they are in like, they certainly
*  were not designed to try to make it easy for new people to understand what's going on. So I've just
*  got a quick glossary of like some of the key terms that you'll hear and there's a ton of confusion
*  around. Transformers, of course, one, you'll also hear that described as an architecture.
*  The architecture is basically like, what is the wiring diagram? What is the path that the information
*  is going to follow and what kinds of transformations are going to be performed as we go?
*  Tokens are the inputs. I think mostly listeners to the podcast will be familiar with tokens.
*  They're basically words, word parts, symbols, you know, the word hello is a token. The
*  ing ending is a token. A period is a token. A question mark is a token. There's a lot of
*  weird tokens to tokenization. We just did an episode, you know, about some of the evils of
*  tokenization and why ideally, you know, for performance purposes, you might like to leave
*  it all behind. But as it stands today, tokens are the inputs. So language is broken down into tokens
*  and tokens are what the transformer accepts as an input. Those are then converted to numbers
*  and that process is called embedding. It's actually super simple. At runtime, each token
*  has a corresponding numerical representation that is its embedding. And so that first process of
*  just converting from token to number is literally just a lookup. This token corresponds to this
*  set of numbers. It's an array of numbers and that's the process of embedding. At runtime,
*  it's just looking up token. Here's the numbers. Boom. So now we've translated the input tokens
*  to numerical form. And now we can start to send that through this information processing circuit
*  and perform different transformations on the data. The two main kinds of transformations that get
*  performed are attention and the MLP, which is multi-layer perceptron. This is the attention part.
*  It's broken up into different attention heads and there's kind of an elaborate little mechanism
*  there, very much studied, not going to get into the weeds of that. Then there's this other one,
*  the MLP. That's kind of, if you have any visualization in your mind of what a neural
*  network would look like, that's basically it. Or it's just like layers of neurons, neurons, again,
*  borrowing from taking inspiration from biology there, that are all just connected to all of the
*  layers in the next, all of the neurons in the next layer. So pretty simple structure. There's also
*  some non-linearities, which is basically saying we're going to kind of filter if there's various
*  non-linearity functions, but between these layers sits this non-linearity function that kind of acts
*  as a certain filter. So that's basically it. You've got your original information. Notably too,
*  this is called the residual stream. So you've got your initial information.
*  The information is processed. It's added back onto itself post-process. So as you go through,
*  you've got the original and you've got the results of all of these layers and they're all just added
*  together and they just keep processing their way through the circuit. The values at these
*  intermediate points are called activations. So once the information is transformed, you can then
*  say, okay, I put in these numbers. I then did this transformation and now I've got these numbers.
*  Those are the activations at that layer. Those are not immediately obvious. Like, do they mean
*  anything? As we'll see later, we can start to put some meaning to them in some cases, but they're
*  just numbers along the way that are kind of the intermediate values as you go from input to output.
*  The logits then are essentially the predictions of what the output should be. In the transformer
*  with a vocabulary of 50,000 plus possible tokens, the output is actually a probability for each of
*  those 50,000 tokens. So if it's really obvious, all that probability could be concentrated on one or
*  just a couple tokens. If it's not at all obvious what should come next, then you may see a ton of
*  different tokens that have significant probability on them. But that is kind of the final output of
*  the AI is, okay, here are the probabilities for all of these different possibilities.
*  And then you can actually use that in different ways as a user. You can say, I always just want
*  to use the most likely one, whatever is the number one most probable token. I could just take that.
*  That would be basically the equivalent of setting your temperature to zero if you're using the
*  open AI or the anthropic API. Temperature zero just means take the most likely one.
*  You could also say, oh, I want to actually sample from that based on those probabilities. So if
*  there's 10 different things that are all somewhat likely, you could choose at random. So different
*  ways to use those probabilities at the end. But the output is a bunch of probabilities that says,
*  here's the chances that all these different things are the next bit.
*  Forward pass is just the process of running this through once. Inputs going all the way through
*  all the transformations until output. That's called a forward pass. And then the model itself
*  is what you have once you actually train the thing and it can actually do something for you.
*  So I'm going to walk through the process of how that happens as well.
*  Now, just zooming in for a second because people are like, often, okay, but what's happening in
*  there? What's happening in there is honestly low level, pretty simple. It's basically all
*  matrix multiplication and matrix multiplication is just multiplication and addition. So if you've
*  never taken a linear algebra course or you've never multiplied matrices, it looks a little
*  like this. You've got a 2 by 4 matrix and a 3 by 2. You multiply those together. And this illustrates
*  how the value for each of the cells in the resulting matrix get calculated. It's like A1,
*  1 times B1, 1 and A1, 2 times B1, 2. Add those together and that goes here. It's just really
*  multiplication and addition. It's a ton of it, but it's really just multiplication and addition.
*  I also missed one, by the way, parameters and weights. I should have said, I skipped over this
*  one. Parameters and weights, those are the numbers in the architecture, in the transformer, that you
*  actually use to do the transformations. So you've got your information coming in,
*  that multiplication and addition that is multiplying by the parameters or the weights.
*  Those are the numbers that are in the system, waiting there to do the transformation on the
*  input information. And so you've got input information embedded as numbers transformed
*  by being multiplied by the weights or the parameters. And then the result of that at each
*  layer is the activations at that layer. You do that over and over and over again until you finally
*  get to outputs. Okay. So that's that. Here's a detailed view. It gets super big. Notably on
*  this thing, this says, this whole thing says, do N times. So this is like the input part. This is
*  one of those layers that does that sort of transformation. This is the output thing,
*  but you do like a bunch of these layers, especially with the big systems. I think with,
*  I don't know the exact number off the top of my head, but with GPT-3, I believe it's like
*  70 layers deep, perhaps. So this goes on for a while from beginning to end. And there are
*  actually, in a system like GPT-3, there are 175 billion parameters, famously, that make up the
*  thing. That is to say, once you have all these layers and you have all these different places
*  where there are numbers waiting to be used to multiply by the information that's flowing
*  through in order to do these transformations along the way, there are 175 billion of those
*  numbers just waiting there to be multiplied by the inputs and to transform it step by step until
*  you finally get to outputs. So it's a giant kind of mess of a thing. Here's a little zoomed in
*  detailed view. And basically what you're doing here is, again, you're inputting your tokens,
*  you're embedding, now you're in number form. Then you start to do some manipulation. Now
*  you're starting to get into activations. And then you're also multiplying and doing these
*  constant multiplication and addition processes with the parameters as the means of transforming
*  the information that you've put in. So let me pause there because an obvious question would be,
*  well, why? Okay, you've described this thing, this gnarly transformer, but why? Why would anyone
*  do this? Or how did anyone think this was a good idea in the first place?
*  And the answer there is, in all honesty, it's an experimental thing. It's not super highly
*  principled. I don't want to say that there was no insight in the original discovery of the transformer,
*  but it was as much a riff on things that came before as it was a total eureka moment that,
*  like, oh, this is going to work. So the attention mechanism and the transformer's paper,
*  many people, of course, will know the transformer's paper was called Attention is All You Need.
*  The attention mechanism had been created a couple of years prior by other people.
*  And what they found in the transformer paper was that you could actually strip out other things
*  that had been previously commonly used and just kind of use the transformer in its place,
*  or sorry, the attention mechanism in its place, and that worked really well.
*  It worked well in terms of performance. And even more importantly, ultimately, is
*  the computation within the transformer is highly parallelizable.
*  Earlier architectures would be serial in nature. You may have heard the term, for example,
*  recurrent neural networks, and that recurrent has this reference or a kind of allusion to
*  each output, each step in the computational process, depending on the one that came before.
*  So you have to finish the one in order to do the next one. That's not really the case in the
*  transformer. In the transformer, you can parallelize it. You can do a ton of this computation
*  at the same time across different computers, which allows you to scale it up much bigger than
*  architectures that had come before it. Specifically, because it is really just all
*  relatively simple math, you can use GPUs to do it instead of having to use CPUs.
*  So when people used to say, like, oh, well, Moore's law is sort of over, that largely meant that,
*  you know, CPUs are not getting faster in the same way that they used to.
*  But what that analysis kind of missed was, well, GPUs are actually still scaling up pretty well,
*  and they don't necessarily have to get super dense or super clock fast, you know, within a single chip
*  if you can create a structure that can use a bunch of GPUs at once. So they have simpler
*  compute structure. They can't do all the things that a CPU can do, but they can do enough,
*  and they can do it in parallel to take advantage of the strengths of this architecture.
*  Zooming out a bit, like, the way some people describe it is like,
*  we were, you know, the field was like stumbling for many decades, and then finally, you know,
*  stumbled onto something that is this Eureka moment, as you described. Is that fair? Like,
*  did that Eureka moment build upon the work that was, you know, being done for all those decades?
*  How do you contextualize the breakthrough?
*  Kind of fractals are always hard, but I really do increasingly believe that
*  given the web scale data and the web scale compute, something like this was going to be
*  found before too long, and it's interesting that, you know, it doesn't seem to have been that long
*  after that scale existed that these things started to come online. So, you know, you could kind of
*  imagine if the Transformers, you know, if all the authors of the Transformers paper had never been
*  born, you know, would we still be waiting? Maybe, but my guess is, you know, either somebody else
*  would have found that or somebody else would have found something similar, and there are other
*  architectures, you know, that are being presented all the time, and, you know, the bar is higher and
*  higher all the time, so these other competing architectures are getting better and better all
*  the time as well. My sense is that, you know, between the time where you had, like, again,
*  web scale data like we have and web scale compute, there was probably only like a few years,
*  kind of however you cut it, that it was going to take before something that worked pretty well was
*  going to be discovered. That might be a bit controversial, but that's definitely my point of
*  view. I don't think there's a single insight or a single group that kind of, you know, unlocked
*  this in a way that nobody else could have. They did set the path, you know, once, and certainly
*  once somebody finds something, then everybody else, you know, can rush onto it and elaborate it and
*  study it and all that sort of thing. So, I do think you could imagine a counterfactual history where
*  some other architecture was the one that got discovered, and we've spent, you know,
*  years developing that one instead, and that one, you know, and as we'll see, like, there's, you
*  know, we already saw a little bit with the tail of the tape, like, there's these kind of weird
*  idiosyncratic strengths and weaknesses of this particular architecture. Some other architecture
*  might have some other, you know, idiosyncratic strengths and weaknesses, and we probably will
*  bring more of those online and, you know, certainly we'll explore their strengths and weaknesses as
*  well, but it's hard to imagine that nothing like this would happen for very long once all the
*  inputs were there. Because then there's also the question of how far can we get with this architecture?
*  Like, yeah, yeah, that's the big question. What are your instincts? Well, let me show you how far we,
*  I think, have got, and we'll speculate a little bit at the end. So, perfect segue to foundation
*  model foundations. Okay, so we've just set up this thing, right, and I've just told you that
*  this is the first thing that we found that worked. Hypothetically, counterfactually, it could have
*  been something else perhaps, but this is what we've got. We set up this giant wiring diagram,
*  and, you know, we have all these, you know, 100, in the case of GPT-3, 175 billion numbers there
*  that are waiting to transform this input data into output data, but, like, how does it actually
*  learn to do anything? Amazingly, most of the time, the initial parameters or weights or those 175
*  billion numbers, traditionally, they are chosen for starters randomly. So you literally have 175
*  billion random numbers to start. There are some refinements on that, but, you know, first
*  approximation, you're starting with random numbers in that architecture. And so at the beginning,
*  it doesn't work. That's the punchline, right? You set all this up, and you do your first forward pass,
*  and it doesn't do anything of any value. But now you can start the learning process. So here's a
*  simple case where, and this is a classic data set of just small images of handwritten numbers,
*  and the goal of this data set was to figure out, can you create an AI that can identify the number?
*  We can all do it. It's a pretty intuitive task for humans. If you try to use traditional code
*  to write a bunch of rules to do this, you're going to be in trouble. You're going to struggle,
*  and you're probably not ever going to get to a very good place. And certainly people have tried.
*  So what are we doing here with the AI that is different? The key thing is we are defining
*  is we are defining a numerically scoreable evaluation of the AI's output, and that is
*  called the loss function. So just more jargon. But the loss function is a numerical score for how good
*  the output is. So in this case, hypothetically, we're at the beginning, right? We set up our AI.
*  You don't need 175 billion parameters, by the way, to do this. You can do it much, much smaller.
*  But we set up our AI, and we've got all these random numbers in there doing this transformation,
*  and we give it a 2, and it processes. Then there's a process of tokenization for images
*  a little different from tokenization for text. Don't worry about that too much. But it does all
*  this processing, and then it gives you something like this, all these probabilities on these
*  different numbers. And it's like, well, that is total garbage. Here, the right answer was 2,
*  but it only gave that a 0.2 in this made-up example. Meanwhile, it gave a 1 to 3. It was
*  wrong. So it's total garbage. But you can numerically score this. You can say a perfect
*  prediction would have been to give a 1 to 2 and 0 to everything else. So how far are we from that?
*  Well, at the beginning, you're pretty damn far from it. But you can now do this process of
*  backpropagation. So the forward pass is when you take the input in, you do all the transformation,
*  you get to an output. Backpropagation is now saying, OK, we have our output,
*  and we're able to score it and determine how far it is from the right output. Now, let's work our
*  way back through that entire structure and look at every single one of those parameters, AKA weights,
*  AKA the numbers that were used to transform the inputs into outputs along the way. And let's just
*  look at each individual one and just say, how would we tweak this to make the final prediction
*  a bit better? If I increase that number a little bit, does it make it better? Or if I decrease that
*  number a little bit, does it make it better? And a key property of these architectures is that they
*  are what is called differentiable, which basically just means that you can, in fact, work your way
*  all the way back and ask and answer that question successfully at each individual step. So you could
*  do that a naive way, and it would work. You could do it literally one at a time through 175 billion
*  parameters of GPT-3. In practice, the code for that is a lot more optimized and includes batching and
*  all sorts of optimizations. But conceptually, it's really just going through and saying,
*  you have this prediction. We're able to score it. We're able to see how far off it is.
*  And we're able to say, if we tweak this one number in this broader system, does that bring
*  us a little closer to the right prediction, or does that bring us a little farther from the right
*  prediction? And then you just make the change that brings you a little closer. You can do that
*  times 175 billion parameters or however many you have. And that is backpropagation. Forward pass
*  takes the inputs, processes that signal through all those transformations to an output. Back
*  propagation says, OK, we have our output. We can score it. Now let's go back and look at each of
*  those numbers that was used along the way and just tweak each one so that every tweak that we make
*  brings our prediction a little bit closer to the right prediction. Now you do that once.
*  Not that much has really happened. You do that in a loop over and over and over again. And now
*  you are doing the process of gradient descent. And again, lots of jargon. But
*  essentially, gradient descent. Gradient means the direction in this high dimensional space.
*  You literally have, in GPT-3, you have 175 billion parameters. That's 175 billion different things
*  that you can manipulate independently. And one manipulation of all 175 billion numbers going in
*  the right direction, you're moving in the direction of the gradient. And just running that in the loop
*  over and over again, you're making those optimizations each time. Gradually, you get to
*  better and better performance. And this is where the magic starts to happen. And this is where we
*  don't really quite know how all those little tweaks are actually adding up to better performance. We
*  just know that in practice, this does work. In practice, you run this even on a small model. It
*  doesn't take very long. Now you can actually identify those handwritten numbers at a very
*  high rate. And obviously, as we've seen, you can do a lot more than that as well.
*  So people traditionally would use labeled data here. That image data set. And this one was
*  cracked only 10 years ago. I think it was 2012 that the deep learning revolution kicked off. And
*  one of the seminal papers there was demonstrating that basically a black box neural net could do
*  that image task. But you have labeled data. You have the image and you have the actual human
*  provided. This is a two. So you can run this process. You can do this loop. You can do the
*  forward pass, get your prediction, do the back propagation, do all your little tweaks. Again,
*  you can optimize the code for that for performance purposes. And people spend a ton of time,
*  as you might imagine, especially as you get to big 175 billion scale things, optimizing, optimizing,
*  optimizing. But that's all just optimization around core concepts. So you can run this
*  process in a loop and you see that, hey, the loss, aka the predictions, keep getting better. The
*  lower the loss, the better the predictions, the closer they are to the right predictions. And you
*  typically see this kind of curve where at first, it's pretty easy to make progress because you
*  started off with random numbers. So it should be easy to improve on that. As you go for a while,
*  it starts to level off because it's harder to make improvements because you're already starting to
*  get pretty good. With a labeled data set, people would typically see something like this where they
*  would say, all right, I'm going to split because I don't just want to convince myself that it's
*  working. I actually want to know that it's really learning something of value that generalizes
*  beyond just the examples that I happen to have. So how would I do that? Well, I can split my data
*  set into a training data set that I'll actually use in the loop of training, doing the forward
*  passes, doing the back propagation, making all those adjustments, doing that whole process in a
*  loop. And then I can take the resulting model where all of those numbers have been tweaked for
*  the best performance that we could get to. And I can run that on a different data set that I didn't
*  see in the training. And that is called the validation data set. And so when you see something
*  like this, where the training loss is going down and the validation loss is going down too, then
*  you're like, okay, I'm actually learning something here. And I know that I'm learning something
*  because I can take that model and apply it to unseen data and it still is working. And you
*  almost always will see these kinds of curves where the validation set is not quite as good.
*  And then you'll see this divergence. At some point, the validation performance is no longer
*  getting better and actually starts to get worse again, even as the training performance continues
*  to improve. So what's happening there? Well, that's known as overfitting. And that is the point at
*  which all these little tweaks are actually starting to just reflect the idiosyncrasies
*  of the training data in a way that no longer applies to the unseen examples. So just to be
*  super imaginative and specific about it, there may be this little nugget of that zero.
*  It may be learning that that is a great indication of a zero because that's what it sees in the
*  training set. But then in the actual data set, well, maybe there's a different number that has
*  that little extra blob of ink and now it's being led astray by those very small details.
*  So that is known as overfitting. And for a long time, this is basically where people would stop.
*  You would have a data set of labeled data, you split it into your training and your validation,
*  aka your test. Sometimes I split them into even another training, validation and test, whatever.
*  But you run your training, you do your test, and you get to a point where you're like,
*  okay, the test results are no longer getting better. That's basically the best that we can do
*  with this architecture and this data set. And anything beyond that is overfitting and generally
*  was considered to be a waste. However, there is more to that story. One big
*  insight, and this is the kind of thing I think that a human could do and an AI wouldn't expect
*  to, even with our current AI, wouldn't expect to see this kind of insight from an AI system.
*  People said, well, geez, we're really limited by the size of these data sets. We've only got
*  so many labeled numbers. And beyond that, what do we do? Well, a pretty clever idea was to move from
*  this supervised data where each input has an actual what is the right answer to new kinds of
*  problems that didn't require that type of labeling. That's often called unsupervised learning.
*  And it has different functions, different loss functions. So the two really clever loss functions
*  that have driven a lot of the progress that we've seen over the last couple of years,
*  next word prediction and image denoising. If you set up text and you say your job, AI, is to take
*  in some text and then predict what comes next, then you can use all the text that you have. You
*  can use the whole internet, right? Because it is essentially self-labeled and nobody has to go
*  through and do extra labels to just look at, well, what is the next word in that particular bit of
*  text? So now we've gone from a situation where there was a sort of annotated ground truth,
*  like somebody went through and said, this is a two, I'm going to label it as a two. And then when we
*  do these evaluations, we'll know that this should have been a two to now just, hey, give me a ton of
*  text. And whatever word actually comes next in the text, we'll just consider that to be the ground
*  truth. And we'll do that for pass, we'll get whatever the predictions are, and we'll consider
*  the right prediction to have been whatever the actual next word was. And we'll just make all of
*  our parameter, AKA weight, AKA the numbers in the architecture that actually do the transformation,
*  we'll make all those tweaks just based on whatever that next word actually was. So that is next word
*  prediction. And the key thing there is it opens up the scale of all the text. A similar thing
*  happens with images. This one's even more clever, in my opinion, because you think, well, geez,
*  there are a ton of images out there, like billions, you know, probably maybe a trillion plus at this
*  point, if you look into like Facebook data or Instagram data, where people have an image,
*  and then they have a caption of the image. Those aren't always perfect in the way that like, you
*  know, these like controlled systems, you know, controlled scenarios of this is a two, this is an
*  eight, but those are pretty, you know, concrete. Obviously, the captions that we put on our, you
*  know, our internet pictures are like highly varied. But still, there is some sort of, you know, concept
*  of a label there. And people came up with this idea of, well, what if we could train an AI to take a
*  noisy image and predict what would that noisy image look like if it were a little less noisy
*  and a little more like whatever it's labeled as? So this is just an example where we're doing it
*  with the, you know, the very small number data set. What would this look like if it was a little less
*  noisy and a little more like a zero? Well, it might look like something like this. And if you took this,
*  then what would this look like if it was a little less noisy and a little more like a zero, maybe
*  like this? And on you go. The key insight here is that if you define the problem in this way,
*  then you have all the data you need because it's easy to add noise. So they take all the real images
*  with the captions, they add noise progressively step by step, and then they train the AI to take
*  the noisy image in and predict what it would look like if it was less noisy and more like
*  the original label. And they actually have the answer to that because they've, you know,
*  progressively noise the images in the first place. So by creating all these noise images,
*  then you can work backward from noise to real. And then once that's all done, now you can just
*  start with pure noise and you can be like, okay, here's pure noise. I want to make it look like
*  whatever. And that's kind of how these text to image systems work. It starts with pure. There's
*  a lot of variations of course now, but the original one was start with pure noise and take me toward
*  a zero or take me toward, you know, a avocado chair as the case may be. Does that make sense?
*  Yeah, let me answer. So key point here is just you are coming up with clever structures
*  such that you can still define a numerically scoreable loss function, but that where it gives
*  you data at scale that you never could have accumulated with manual effort and labeling.
*  Yeah. Okay. So this is where I think it starts to get extremely, extremely interesting.
*  First of all, scale. We have seen that there is web scale data, there is web scale compute.
*  We've seen that the transformer is highly parallelizable, which means you can run it
*  on a lot of different computers at once. We've now seen that you've got these clever,
*  uh, new formulations of problems that allow you to churn through huge amounts of data without
*  requiring a lot of effort to go in and label that data first. So you might say, well, how far does
*  that really go? And so far we have not found the end of it. This is from the chinchilla paper.
*  And this is the chinchilla scaling law. These curves are what are known as iso flop curves.
*  That means that there is a specified budget of compute of the flop as a unit of compute,
*  floating point operations, whatever. Isoflop means we're holding the amount of compute that
*  you can use in this training process constant. And now we're going to ask the question of,
*  okay, I have that much compute. How big should my model be? Should I make it 175 billion
*  parameters? Should I make it, you know, a hundred million parameters? Like how many numbers in there
*  do I really, do I really want to use? Well, they mapped this out and what they found was
*  basically this trend. They also found, you know, to break down these isoflop curves,
*  what you see is if you use a really big model, then you have a lot of numbers in your,
*  in your architecture that you need to tweak every time you do the back propagation. So the bigger
*  the model is, the fewer loops you can do, right? Each forward pass takes some compute. You get your
*  score, then you do the back propagation. The more parameters there are in the model, the more compute
*  that takes. So if you have a fixed compute budget, the bigger your model is, the fewer predictions
*  and improvement cycles you can do. On the other side though, if you, you know, if you have a really
*  small model, you can do a ton of predictions, but, you know, you don't have a lot of space in the
*  model to actually learn things, right? If you take that to the limit and you just had like two numbers
*  in there, like there's no way you can pack, you know, all this information into just like two
*  numbers. So what they find is that, you know, there is this kind of sweet spot for each isoflop curve,
*  where if you go bigger, then it's not optimal because, you know, you can't do as many cycles
*  as would be optimal. And if you go smaller, then yeah, you can do more cycles, but there's not
*  enough parameters to actually take advantage. You're not tweaking as many actual variables.
*  And so your performance is limited that way. And for each isoflop curve, there is an optimal point.
*  And this line just goes through all those optimal points and basically just shows that
*  as the compute budget gets bigger, basically the optimal point is reasonably predictable.
*  And, you know, is it a law? I wouldn't say it's necessarily quite a law, but it's definitely,
*  you know, proving useful for prediction. And the reason that these big companies want to study
*  this, of course, is like, if I'm going to spend a hundred million plus on my next model,
*  I kind of want to know what size it should be. You know, I don't want to get that way wrong.
*  Actually, OpenAI did get it kind of wrong with GPT-3. They were somewhere on this. I mean,
*  they had a bigger compute budget. Notice that this only stops at like five billion parameters.
*  They're out at 175 billion parameters. They're off this graph entirely. But they were actually,
*  for their isoflop curve, for their compute budget, they actually used too big of a model,
*  which means they didn't get to do enough iterations. And so it was actually suboptimal.
*  And then Google or DeepMind came through with this chinchilla paper and showed that
*  actually they could have gotten by with fewer parameters and more cycles of training.
*  The new trend, by the way, with like Lama from Facebook, is actually to go up this curve in the
*  other direction, in the direction of smaller models with longer training. And the insight there is
*  like, okay, this is actually the optimal point for if you have a certain training budget, what is the
*  right design to get the best possible performance? But the Lama insight is that's not necessarily
*  the right question to be asking because you're actually going to use this thing in, you know,
*  applications. And that's no longer training. That's now just running the forward pass and
*  actually doing the predictions. So I'm actually, in some ways, advantaged to say, maybe I'm not
*  optimizing the performance for my training budget. But if I look at my training budget and all the
*  compute I'm going to use at runtime using the thing in practice, and I want to optimize all that,
*  then I actually end up pushing up this curve because I'm like, well, I want it to be smaller
*  because that'll be more efficient at runtime. And so maybe I'll be like here or whatever on this
*  curve. Again, there are actually, you know, Lama models, I think they started at $7 billion or
*  whatever. So they're also, you know, kind of down here. But it does go to show, you know,
*  that these small scale studies do create predictability that you can use to not be
*  shooting in the dark when it comes to, you know, how are you going to design your system for the
*  $100 million training budget? So all of that, a lot of detail, just zooming out for a second.
*  Key point here is we haven't hit the end of this. This just kind of keeps going down.
*  Loss keeps going down. Kind of keeps scaling and loss keeps going down. We really don't know yet
*  where that stops if it, you know, hits some sort of hard limit. Right now, the trend line just
*  continues to go down. These are log scales. So, you know, and these are, you see from 6 to the 18
*  to 3 to the 20, we're covering orders of magnitude here. So this is not like cheap to scale up from
*  here to here. In fact, instead, it's like a thousand X and it's like thousands or maybe even
*  a million X, you know, to get to GPT-4. So it's not to say that it's easy to continue to push down
*  those curves, but just that as far as we've seen so far, you keep pushing, performance keeps getting
*  better. Now, I recently heard this, I thought it was super interesting story. This is from
*  Reid Hoffman's new podcast. He had an interview with Sam Altman and Greg Rockman from OpenAI.
*  And Greg tells this story of one of the first things that really convinced them that it was
*  going to be worth it to scale. They had designed this system to predict the next letter in Amazon
*  reviews. And that was really what it did. But when they looked into that system and looked at, you
*  know, what's happening in these activations, what are these intermediate values that we can kind of
*  look into and see along the way, even if we can't immediately interpret what they are,
*  what they found was an activation that is, you know, again, just an intermediate value along the
*  way that seemed to classify whether the review was positive or negative. And this is also known as
*  sentiment analysis. And there've been systems for sentiment analysis for a long time. You can kind
*  of imagine even doing something like that in traditional code, right? You could say, well,
*  if it contains good, then it's probably positive. Oh, but wait, what if it contains not good? Oh,
*  then it might be negative. Okay. Well, you can build up a lot of rules. You can get decent at
*  sentiment analysis, even just with rules. But what they found was that this internal activation,
*  this intermediate value within this bigger system that was just meant to predict the next letter of
*  Amazon reviews was actually a state of the art sentiment analysis classifier. In other words,
*  there was no system that they could find on the market that would do a better job of identifying
*  whether a Amazon review was positive or negative than this random thing in the middle of this
*  system that they had built for another purpose. And so from that, they said, oh, wait a second,
*  something profound is going on here. We didn't ask this thing to classify, but it has somehow
*  developed internal classification as a means to doing what it's actually built to do, which is
*  predict the next letter in this review. Somehow learning and representing whether it's positive
*  or negative seems to help it with those predictions. Otherwise, it presumably wouldn't happen at all.
*  So this happened in 2017, and he called it a real wake-up call. And this is when they felt like,
*  there's something, this is often called emergence, properties that you didn't necessarily design for,
*  but which you nevertheless do observe. This is when they, I think, got religion around,
*  yeah, we're going to push this really hard because we're starting to see some things here
*  that are super, super interesting capabilities that we didn't even design for starting to come online.
*  Okay. So now it gets even more interesting. They are already armed with this insight. Now
*  we covered the training to the point of overfitting. And here's a real simple problem,
*  but with really profound results. So modular addition is just the problem of take two numbers,
*  add them, divide by some number and take the remainder. So you've got, if you're doing
*  mod 12, five plus seven is 12, divide by 12, that's one, remainder of zero, the answer is zero.
*  17 plus eight is 25, divide by 10, if that's two, remainder of five, the answer is five.
*  In this case, one, two, three plus four, five, six is actually less than seven, eight, nine. So you
*  divide by that, it's less than one. It's just the remainder of five, seven, nine. The answer is five,
*  seven, nine. That's the task of modular division. That's just setting this up because what they did
*  next with this rocking paper is they created a synthetic data set. You could do this, just
*  take some random numbers and just create a bunch of problems of modular addition,
*  and then try to train an AI to do it. And what you see here is this is kind of where,
*  and this is accuracy as opposed to loss. So with loss, you want lower loss. With accuracy,
*  obviously you want higher accuracy. So what they're doing here is they're training this.
*  And as you go, and you really almost have to zoom in to see it, but you see that, okay,
*  starts off, nothing great is happening. Then at some point, hey, we're starting to get some answers
*  right. And then you get to this point where, okay, my training data set, I'm continuing to improve on
*  that, but my validation data set, I'm actually getting worse again. So that would be the point
*  of overfitting. So traditionally this is where you would stop. You would say, all right, I train this
*  thing, however many steps. And I got to the point where my validation results were no longer
*  improving. And so beyond that, I'm not really learning anything. I'm just kind of overfitting
*  to the sample that I'm training on. And so that's where we stop. But they had this sense that there
*  might be more past that. And that's what this paper is called, generalization beyond overfitting.
*  They keep training beyond overfitting. Now for a while, okay, the training set goes up to basically
*  getting all the answers right, but who cares, right? We know that we're overfitting. We've
*  just memorized all those answers, but we still can't get, in fact, we're back down to basically
*  getting all of them wrong on the validation set. So we've gotten worse. And notice again, log scale.
*  So they took this from whatever, a couple hundred steps out to ultimately a million steps.
*  But when they did, something really profound happens. Eventually, it starts to learn how to
*  do the problem in a general way. And it starts to be able to solve the ones that it hasn't seen.
*  So this is pretty crazy and a pretty striking result, right? Because people have been doing
*  this kind of thing for years and just stopping there. But they went not just a little past,
*  but like a thousand times more training and find that when you go that far, the thing actually
*  learns to do all the problems, not just the ones that it has seen. So what the hell is going on
*  there, right? I mean, that is just begging for more investigation. And good news for us in 2023,
*  that investigation has been done. So you say, well, okay, what is going on? What is it learning? What
*  is it doing? And this is where people have actually come in, taken these fully trained networks that
*  can now solve all the problems and say, well, what is it doing? When it's doing all that information,
*  transformation through all these steps and layers in the network, like,
*  can we say what that kind of transformation is? In general, that's really hard, but this is a pretty
*  simple toy problem in theory. And so they actually were able to figure out what algorithm the network
*  has learned and reverse engineer it to the point that they could write it down like a normal math
*  equation. And this is what it is. And they often say about this, you don't have to like it.
*  I'm not telling you that you should be happy about this. I'm not even telling you that this
*  should make any sense to you immediately. Just that this is how the system has learned to solve
*  all the problems, including the ones that it didn't see in its training process. And it's
*  basically learning these trigonometric functions that transform these inputs into the appropriate
*  output and do it in a reliable way that works for all of the different possible problems that it
*  might see. Now, this is kind of, you know, watch, take in. Essentially what it's doing is it's learned
*  that there's a rotation equivalence to this modular addition, right? You think about basically,
*  you go past, you know, the mod number and you start back over at zero. So there is this kind
*  of cyclicality to modular addition where, you know, for example, let's say it's, you know,
*  we would just go back to this one. I probably don't even do this this much, but let's say,
*  you know, 17 plus eight mod 10, that's 25 mod 10 is five. Well, if it had just been seven plus eight,
*  then it would be 15 mod 10, you know, the remainder would still be five. So there's,
*  you know, every 10 that you add, you're basically just taking another loop around the mod 10 circle
*  and you're ending up in one of 10 places kind of regardless. And that is what it has learned to do
*  is kind of map this onto a circle, add these things in rotational form and figure out where do you
*  actually end up. So if I rotate, you know, by a amount that might be, you know, whatever,
*  try to make up another example, too many examples already, rotate by a amount. And then I rotate by
*  B amount. Where do I end up? Well, it's the same as if I had just done this. Right. And that is,
*  in fact, the answer. So this is weird. This is not how it feels like I'm doing it. You know,
*  I'm pretty sure it's not how I'm doing it. I mean, you could wonder, like, am I actually
*  doing some trigonometry in my head? I'm pretty sure I'm not. So it seems like it has learned a
*  quite different way of solving this problem. One that is, you know, frankly, pretty alien to
*  us, most of us anyway. And that's why I started saying not just artificial intelligence, but
*  alien intelligence. This is something that, you know, can learn these problems in a way that
*  with real effort, we can go in, pull it apart, figure out what it's doing, not all the time,
*  but at least some of the time in the simple problems. And what we see is
*  it's pretty weird in a lot of cases. And this goes on. Right. So this is probably
*  year and a half old now work. They are starting to take this up to bigger problems. So the board
*  game Othello, similar deal, right? In this case, you have a board. The board has, you know, same
*  as a chessboard. So it's an eight by eight board. So you've got, you know, a scheme for identifying
*  the squares where you go through, you know, zero to seven columns and A through H rows. And all that
*  the AICs is a sequence of moves. Whoops. And its job is to predict the next move. So it doesn't
*  need necessarily in theory to understand. It's not told the rules. It's not really told anything.
*  It's just, this is what you get. And now your job is to predict what comes next. But what they find
*  is when they look again at these intermediate activation states, where the information has
*  been processed by some of the layers, but not yet all of the layers to the outputs, they can actually
*  reverse engineer these and see, well, what is, what is it doing here? What, you know, what is,
*  what is this internal activation? Does it mean anything? Can we see what it means? Can we see
*  what it represents? And in fact, they find that it is learning to encode the board state. And this
*  is kind of a weird game where like, I don't know if you've played it, but like, I haven't really,
*  but you put, if you kind of sort of like go, but if you just on a simple line, right? If I have my
*  piece and then some of your pieces, and then I add my piece, all of your pieces turn into my pieces.
*  And that's how you win is by kind of, you know, bracketing around and converting your pieces to
*  my pieces. So it's learning the state of the board, whose pieces are where, as they have been
*  gradually evolved through all of these moves. And some of these individual squares could change
*  from move to move and actually go in further and investigate, you know, okay, yeah, maybe,
*  maybe we're confusing ourselves here, but they go in and actually make surgical changes where they
*  say, we're going to make, we're going to change how this particular bit is represented and then
*  see, does it, you know, make an appropriate move given that change that we made at this intermediate
*  step? And they can prove that, yeah, it does. Like you can actually tinker with the internal
*  board state and it will behave appropriately given the little surgery that you made to it.
*  So it's pretty insane. This is again, not explicitly called for anywhere. The problem is just,
*  here's a sequence, you predict what comes next. It has learned a whole geometrical representation
*  of this that we can decode, but which we never really asked for. But it turns out that that's
*  the best way to do the predictions. Like that's the kind of key point here, right? Is if you want to do
*  the next prediction, this actually is more like what we would do, right? We keep the board in
*  front of us so that we can look at the board state so that we can make the right next move.
*  If you just had this, you would be in a really tough spot. You need the actual, interestingly,
*  like really advanced players, you know, like Magnus Carlsen, he doesn't even need the chess
*  board. He can just visualize the whole thing himself. I'm not at that level. I need the board.
*  And the thing in a sense, you know, kind of needs the board too. Like it's kind of learned to do
*  this representation so that it can make the right next move prediction. I find this pretty
*  incredible. Honestly, it's amazing that this happens. So, you know, you might think, well, geez,
*  can we, like, how far does that go? You know, can we do, can we like reverse engineer everything?
*  The answer is no, not yet anyway. You know, it's, these are toy problems, right? It's a very,
*  to do modular arithmetic or to, you know, make the next move in NFL game, that's pretty narrow
*  domain compared to everything that's going on in a language model, everything that's going on in
*  natural language. So we cannot take like even GPT-2 is like, you know, people are starting to
*  make some headway on understanding what GPT-2 is doing, but GPT-3, first of all, hasn't been
*  released. But second, you know, even if it were, it's way bigger and way more complicated. And,
*  you know, we've already got GPT-4. So interpret, mechanistic interpretability, which is what all
*  this work is, is behind the capabilities of the models. But as we're starting to see, hey, you
*  know, there is some ability to make progress here. People are also starting to come up with some
*  really interesting techniques to try to encourage this sort of thing. So we just did this episode
*  with Zhiming Liu from MIT, and they came up with this really interesting strategy for saying,
*  what if instead of just allowing all the, you know, the positions to connect to all the other
*  positions, you know, totally freely, what if we said that we're going to penalize the connections
*  by the length of the connection? Then could we encourage, you know, some sort of more sparse,
*  sparse meaning like a lot of the connections are zero, you know, just the weights go to zero.
*  That is what it means to be sparse. Can we encourage sparsity? Can we encourage modularity
*  by just making that very subtle tweak to the nature of the evaluation? Now we're saying,
*  we're not just evaluating you on the quality of your predictions. It's the quality of your
*  predictions and the length of all the connections in the neurons. So we're going to adjust the weights
*  so that we both reduce, we want to improve the prediction accuracy, but we also want to reduce
*  the length. And as you see that playing out over this process of prediction and improvement,
*  you know, back propagation, gradient descent, what you see is this kind of crystallization
*  into these highly modular and far more interpretable structures. So this gives me a lot of
*  optimism that like, hey, there's potentially a, first of all, this is way more efficient,
*  by the way, from the beginning. You know, if you run this, you've got to calculate a lot more stuff
*  than if you can just run something like this. So there are efficiency reasons also that you might
*  want to start to try to prefer these like very sparse modular structures, but certainly for
*  interpretability purposes, this is way easier to make sense of than, you know, the kind of
*  traditional spaghetti, everything connects to spaghetti.
*  All right, a couple more, and then I think we might have to pause for a part two.
*  So other angles on interpretability are, you know, can you figure out what an individual
*  position in the matrix corresponds to? In some cases you can. This is from our tiny stories episode
*  with the guys from Microsoft research. Here they use a relatively small model and they just,
*  as they feed data through, they say like, okay, what kind of stuff seems to cause this particular
*  position to have a high value, high activation. That's basically, again, like the same thing as,
*  you know, as in the earlier example. Here, what they see is, well, this layer seven neuron number
*  one, it pretty clearly corresponds to first person pronouns. The next one right over, it seems to be
*  maximized when there's some sort of like force verb, you know, or kind of movement force
*  application verb, push, ran, pull, whatever. Over here, unfortunately, I hate to tell you,
*  but it doesn't always make a lot of sense. So layer six neuron one, not an obvious pattern.
*  Delicious, mean, Ellie, that's like a token as part of smelly, new, big, scary, can't really make a
*  lot of sense out of that one. Sometimes it works, sometimes it doesn't. Again, we don't know really
*  why, you know, but we don't really know what that means, but it's doing something. And then this
*  final one, you know, obviously first names. So sometimes it's interpretable, sometimes it's not.
*  We're very much still working on it. This was just published, I think in the last six weeks.
*  Same thing also can work for images. This is a really cool technique where using a same type
*  of deal, what kind of input image maximizes the activation at a certain point in that broader
*  structure. They can synthesize these images to maximize certain activation. And what they find
*  is as you proceed through layers, you can see stuff like this, where you kind of squint at it
*  and you're like, what is that? Well, I guess it kind of looks like a car door. Yeah. And this
*  maybe kind of looks like a car body ish. I see some like grill there and headlight maybe, and
*  that's definitely a wheel. And then interestingly, when all of those are present, boy,
*  the next layer really lights up and that, you know, starting to look more like a semi recognizable
*  car detector. So it's weird that like, you know, these things, as much as they learn and they can
*  identify, you know, different kinds of images, they're actually maximized by these like very
*  trippy, you know, synthetic weird images. But it at least is recognizable enough to us. We can start
*  to say, okay, it seems like, you know, this particular position 4Z447, that does seem to
*  light up when it sees a car. And you can also verify that with real images, of course, but like
*  this is the sort of in the AI's mind's eye, this is the, you know, most car-y car there is. It doesn't
*  look like, you know, a familiar car, but all the different cars will light that up. But this is like
*  the canonical, almost like platonic idea of what a car is for this particular model.
*  So again, alien intelligence, you know, I mean, this is not, it's something we can begin to
*  understand, but it's definitely still pretty weird. Okay. Here is, I think, where we'll stop for today.
*  This is the, in my view, the most important content from the GPT-4 technical report.
*  We've set up this whole idea that we can predict what kind of performance a model will have
*  with these scaling laws. And indeed, they show that, yeah, we can start with some really small,
*  and again, this is orders of magnitude difference. This is like, you know, probably a billion X or
*  something. We start with these real small ones. We run them, same architecture, you know, just
*  less training. Let's then see what happens. We kind of draw, you know, do that times a bunch of
*  small ones. And then I believe this is the smallest one or the biggest one of the tests, I believe,
*  was only one 10,000th, if I remember correctly, of the final GPT-4 scale. So way, way smaller.
*  But sure enough, you follow that curve and GPT-4's performance is right on that curve. So
*  scaling laws not yet violated. So far, the scaling laws do seem to be holding. The more you scale,
*  the better the performance gets. And you can even kind of predict what that loss number is going to
*  be. But key point, that loss number is an aggregate measure. For all of the predictions
*  that you're doing for all of this different text, how right are you? It's an aggregate measure.
*  The number one sentence, certain capabilities remain hard to predict. We don't know, as that
*  performance improves, we don't know what is going to be grok'd when along the way. We're pretty sure
*  at this point that like a bunch of stuff is getting grok'd because we can see that, you know, that's
*  clearly happening in the small models. And it's, you know, you look at the behavior of the advanced
*  systems like GPT-4 and it certainly can do some sort of reasoning, you know, pretty well. So it
*  seems pretty clear that there's like a whole lot of grokking going on along the way. But a lot of
*  these things are probably very, you know, small kind of micro reasoning skills that are getting
*  grok'd bit by bit. And the key point is we don't know what will be grok'd when. And even more than
*  that, we don't know if something has in fact been grok'd until we actually do the reverse engineering
*  and look at the mechanism. Because you could always say, well, maybe it's just kind of learned
*  statistical correlations and it hasn't really learned a way, you know, to fully solve that
*  problem. Just seen enough data, you know, it's eventually kind of memorized and is making good
*  guesses. And the answer there is like, it's almost for sure both. Certain things are being grok'd,
*  other things are just kind of still in the, you know, statistical correlation paradigm.
*  But we don't know which are which. And sometimes it can be quite surprising. In this case, they show
*  this problem of the hindsight neglect problem, which is basically where, you know, you set up a
*  problem and say, okay, you had this opportunity to make a great bet, you know, make a great
*  investment. It was super positive expected value for you, whatever. You did it and then it didn't
*  work out well. So you actually, you know, you made a good bet, but you lost. Should you have actually
*  taken that bet? And the right answer is like, yeah, you should have taken the bet because it was
*  positive expected value. And, you know, you don't want to be, you don't want to overcorrect based
*  on the fact that you got unlucky and lost. Like you were right to take the bet in the first place.
*  The prior to GPT-4, as they scaled up the models, they were actually getting worse at this.
*  So it was like, oh, you're, it's, you're learning the wrong thing. You're kind of learning that like
*  the outcome was bad. And so it was bad, right? And, and not only was it not doing well, but the
*  bigger models were seemingly learning in the wrong direction. Like they were doing more memorizing
*  or more sort of association, but, you know, that association in general might, it might be useful
*  and might be predictive and might contribute to better loss. But in this particular thing,
*  it was leading the models astray. And then with GPT-4, boom, it's grok'd. So we don't know
*  what will be grok'd when, and we don't even use, somebody could still argue this isn't grok'd. I
*  mean, I would say, look, that's pretty grok'd to me when it's going worse, worse, worse, worse, worse.
*  And then all of a sudden it goes to perfect. I think some, some sort of phase change has happened
*  that is akin to what we saw in the modular edition, where, you know, you went long enough
*  and you saw enough of this stuff and you actually figured it out for real. Can't prove that yet,
*  but I'm pretty confident that that is happening. If not for this, then at least for a lot of things.
*  But again, we don't know what will be grok'd when. We don't know if something has been grok'd,
*  even by testing it, really, that requires the reverse engineering. And we have no idea
*  what the next generation of systems might grok if we scale them up to, you know, another hundred
*  or thousand or, you know, however many X, the current scale that we've reached. So I think we
*  pause it there. Perfect. Let's wrap here. Let's do a part two. I have a bunch of questions that I
*  held on to. I'll ask them as well in the next episode. Sounds good. Always a pleasure.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
