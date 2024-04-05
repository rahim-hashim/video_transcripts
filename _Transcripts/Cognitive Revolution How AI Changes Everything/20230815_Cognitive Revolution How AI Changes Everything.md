---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 5020s
Video Keywords: []
Video Views: 1141
Video Rating: None
---

# The AI Revolution in Education with Shawn Jansepar, Director of Engineering at Khan Academy
**Cognitive Revolution "How AI Changes Everything":** [August 15, 2023](https://www.youtube.com/watch?v=ati_ACj1Dic)
*  In 10 years from now, I don't think there'll be any kid who's learning without a personal tutor next to them on demand available all the time that knows everything about their learning history.
*  If they give permission to also understand their interests so that they can kind of motivate them more.
*  If you make a problem based on the Avengers or soccer or something like that, it could be a lot more motivating than whatever generic problem that the student is given.
*  So I think in 10 years, my prediction is that everyone will have this available.
*  Hello and welcome to the cognitive revolution where we interview visionary researchers, entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz joined by my co-host Eric Torenberg.
*  Hello and welcome back to the cognitive revolution.
*  Today's episode is an extremely positive and fun one.
*  My guest is Sean Jantzapar, director of engineering and AI product lead at Khan Academy.
*  For years, Khan Academy's mission has been to provide a free world class education for anyone, anywhere.
*  And they've made incredible progress toward this goal.
*  What started as just one man making personal tutoring videos for his cousin has now grown to over 150 people with expertise in all facets of education.
*  From learning science and instructional design to software delivery.
*  But still, the promise of a truly world class education for all has been limited by the impossibility of scaling personal one to one attention for each student.
*  That's recently changed, of course, with the release of GPT-4 when suddenly the notion of an AI personal tutor went from a distant dream to a practical product problem.
*  And in this conversation, Sean takes us behind the scenes into Khan Academy's early access partnership with OpenAI.
*  Describing the magical experience of chatting with GPT-4 for the first time and how quickly he realized its potential for education.
*  He also tells the story of how his team mobilized to build and launch the first version of their AI tutor, Khanmigo, just in time for the GPT-4 launch event in March.
*  We dig into the details of how Khanmigo works and Sean explains how they're using a mix of prompting techniques and other system level strategies to ensure that Khanmigo is always focused, encouraging, relevant, and critically in command of core academic material.
*  He also discusses Khan Academy's intense focus on safety, including how they minimize the risks of jail breaks and generally monitor for other problems.
*  And also how they're partnering with school districts and teachers to deploy Khanmigo effectively into classroom setting.
*  While the reactions from students and teachers have already been overwhelmingly positive, as Sean puts it, they've only scratched the surface of personalized AI assisted education.
*  He paints an inspiring picture of a future where Khan Academy's educational expertise and GPT-4's capacity for interactive conversation combine to dramatically accelerate learning for students worldwide.
*  And he envisions just how much this could mean for humanity as a whole.
*  If you're finding value in the show, we would appreciate it if you'd share it with friends and or post a review to Apple Podcasts, Spotify, or YouTube.
*  We've had a few great comments over the last week, including one Apple Podcast reviewer who said that this is a sorely needed show with how quickly AI is coming at us.
*  Incredible value each episode.
*  A YouTube commenter also said,
*  And a third said,
*  I really appreciate all these comments and especially appreciate you sharing the show with friends.
*  Of course, your feedback is always welcome.
*  You can email us at tcr at turpentine.co or DM me on Twitter where I am at Labens.
*  Now, without further ado, I hope you enjoy this conversation with Sean Jantzapar of Khan Academy.
*  Sean Jantzapar, welcome to the cognitive revolution.
*  Thanks for having me.
*  So you are leading AI development and productization at Khan Academy and the new product is Khanmigo.
*  I am excited to get into all aspects of this.
*  But for starters, you know, because I feel like we are so quickly acclimating to the pace of progress in AI, I wonder if you could just take me back not too long to your GPT-4 story.
*  If I understand correctly, Khan Academy partnered with OpenAI before things were released to the public.
*  And so you were in this kind of small set of people that had this glimpse of the future.
*  I'd love to hear about that.
*  Yes, it's an interesting story.
*  So I think actually it kind of goes all the way back to around October is when I first got access to GPT-4.
*  Basically, what happened was I suddenly in the evening got access to GPT-4 via Slackbot.
*  I just randomly was added to a channel where you could interact with this AI and an email was sent to just a few folks, key folks at Khan Academy who were given access.
*  And I was like, yep, we're chatting with OpenAI about their new model, GPT-4.
*  I hadn't really played too much with any of the other models that they had available via API or anything, because this is prior to chat GPT being launched.
*  And I remember getting access to this thing.
*  And the initial impressions were that I'm interacting essentially with like an omnipotent being, like this thing that just knew everything.
*  Obviously, over time, you've started to understand the limitations of it.
*  But in the beginning, it was just like, wow, I cannot believe what I have just experienced after talking with it for 30 minutes.
*  And I literally had to go for a walk and walk around the block and just like take it all in thinking about what this is going to change for the world.
*  And it is going to change a lot for the world.
*  Obviously, it's not quite as like, you know, we don't have AGI yet.
*  I felt like when I initially tried it for the first 30 minutes, we had AGI, we don't have AGI, but that's when we got access in around October.
*  And then we shortly after that had a company on site where we were having a hackathon.
*  And the few of us who were or who had access to it decided that we were going to do some some hackathon projects with it, basically.
*  And in the beginning, we were pretty hesitant about the idea of building something that was directly accessible by a learner.
*  We were more interested in the idea of using this to help us build content or use this to do maybe some things for teachers to generate them lesson plans or whatnot.
*  But we were worried about the idea just from a safety standpoint around giving access to students.
*  But over time, we did try a few different ideas, but we thought, you know, what if there's ways we can mitigate some of the concerns we have for students?
*  Things like if we can have ways of monitoring what the student is doing, we found out about OpenAI's moderation API, which we leverage in Konmigo as ways of mitigating some of the risks.
*  And so in around December, we started working with OpenAI a little bit more closely and directly.
*  Actually, somebody on the team, Jessica, created us this quick demo of like, well, hey, what if one idea that you could use this for is really help guide students to the right content?
*  Kind of like almost a more advanced search functionality.
*  And that kind of opened up our eyes to what this could be.
*  Like we kind of initially thought about it as like a concierge, and we tried that and it was it was a pretty cool interaction.
*  So we said, hey, why don't we just do some rapid prototyping together?
*  We were we were engaged with them in like weekly meetings, but they were kind of going nowhere really until Jessica at OpenAI created this this little prototype for us.
*  And that's when we said, you know, rather than just meeting every week being like, hey, so what's your update?
*  Hey, so what's your update? We said, let's just sit down together virtually sit down and just engage in like rapid prototyping.
*  So like, let's check in in the morning and let's check in in the evening.
*  And we decided like, let's actually try to build what would it feel like to have this large language model available as this guide on the side experience next to you in Khan Academy?
*  It was very scrappy. We built it with a few members of the team and initially it just started out as a Chrome extension.
*  And that's how we integrated into the site.
*  And so, you know, we just we made it such that the the AI had access of the context on on any content page of Khan Academy and being able to just say,
*  I don't really get this. And for it to know what this meant, it felt really magical.
*  And we were like, wow, I think there's I think there's something here.
*  And we were we were a bunch of us were experimenting with it, including a lot of the members of our leadership team.
*  And we were just really impressed at the level of how good it could be at a tutor.
*  Of course, it was still making a lot of math mistakes and whatnot, but we felt like there was promise.
*  So what we ended up deciding was, let's get a little bit more serious about this.
*  What if we fly down to Mountain View and do some rapid prototyping together directly with OpenAI in their offices and also in that one?
*  Our offices are just actually above a school that's kind of a related to Khan Academy, but it's a separate organization called Khan Lab School.
*  And we said, like, let's just let's test it out with them and get some student reactions.
*  So we flew down the next week, built out this prototype and tested it with some students and they loved it.
*  One of the things I think that was the most exciting for them was the ability to click this button that says, why should I care about this?
*  That was like by far the most interesting thing that they wanted to try, which goes to show you how good of a job we do in education to help kids understand why they should be learning this stuff.
*  And they were just so shocked at the quality of this thing in general, because Chad GPT at this point in time hadn't been launched.
*  And we did, you know, we also did a bunch of stuff in advance, got consent from parents and whatnot to try it out with them.
*  But they they just they thought they were going to get some sort of like basic, you know, not very good chat bot experience.
*  And and they were blown away at how much it was able to help them.
*  And so from there, we also started we went to the opening offices, did a lot of red teaming with them, talked about our roadmap, talked about, you know, what are ways to make the math more accurate?
*  That worked out really well. That was kind of towards late December.
*  In January, we decided, hey, you know, this is promising.
*  Let's consider building a feature here to launch alongside of the GPT-4 announcement.
*  And by by this point, you know, most people at that point knew about the product, but they didn't know about GPT-4 and the power of GPT-4.
*  And we knew specifically that GPT-4 was was much more powerful, especially from the context of being able to kind of like give it very clear directions and it followed those directions.
*  So, for instance, the tutoring example, when you tell GPT-3.5 to be more Socratic and not give way the answer, it doesn't follow those instructions very well.
*  Whereas GPT-4 does. And that was critical for us because we really wanted to build something that wasn't just going to be something that could help students cheat.
*  But that's something that could really guide them towards the answer and act like as much of a tutor as possible.
*  We decided we wanted to launch alongside of GPT-4 and we engaged the whole company into a kind of a company wide hackathon in January.
*  We decided we're going to let the whole team know, bring them into this NDA.
*  We got generative with the ideas.
*  A bunch of people built some really cool stuff.
*  And then we had to make some decisions about what things would we like to fit into the launch on March 14th.
*  And so from there, we converged the ideas into a few.
*  And then we kind of basically had a huge portion of the engineering design and product team continuing working on this thing right up until March 14th,
*  which is when we launched alongside of OpenAI.
*  And then the launch at the end was a bit of a fun story.
*  We, you know, at the end of the day, you know, OpenAI only had one model they could release and they were working with a lot of customers and a lot of partners,
*  not just Khan Academy and certain customers really liked a certain model that was better at storytelling and whatnot,
*  but maybe not so good at math.
*  But that was the model we weren't interested in because obviously math is the most important for us.
*  There was a very specific model that they released because they were doing weekly releases of these models.
*  And we were hoping like we want the capabilities of this to be the production GPT-4.
*  And we got access to that model pretty late.
*  And once we got access to that model, it was over a weekend and we got a whole bunch of our few folks on our leadership team,
*  a few of our key engineers and design folks, and we just tested the heck out of it.
*  And it worked really well.
*  Turns out this model kind of ended up having the best of both worlds, which is what they were expecting.
*  But they had kind of a backup model that we weren't as happy with.
*  And we tested that model out, worked really well.
*  And thankfully, the launch went really smoothly.
*  So I'll stop there because that's a lot of me talking,
*  but that's kind of what led from like initial trying things out to the launch on March 14th.
*  That's phenomenal story.
*  Takes me down a little bit of my own, you know, walk down memory lane.
*  I was, you know, also kind of as a customer able to get early access and then ended up joining the Red Team project
*  that they had just as kind of a community Red Team.
*  My experience was much less, you know, handheld by the organization,
*  which I kind of envy, you know, the opportunity to sit down and work more closely with them.
*  I was very much just kind of trying to figure it out on my own and didn't know how many other people were also doing it.
*  So in some ways, that was like one of the better things that has happened to me because it really motivated me to figure out what was going on.
*  But I was also a little nervous.
*  Like how many people know that this is out there and what's really happening?
*  You know, as you said, you had to go for a walk.
*  I definitely had a few moments where I was like, man, this thing is a big deal.
*  And nobody, you know, I'm like one of I don't even know how few people know about it.
*  It was crazy experience.
*  So speaking of big deal, it's been out now for a handful of months.
*  You've certainly had a chance to kind of calibrate on the model performance and, you know,
*  probably also to start to get grounded in like where the rubber hits the road with this thing,
*  which for you is with students as they're actually learning stuff.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  If you're a startup founder or executive running a growing business,
*  you know that as you scale your systems break down and the cracks start to show.
*  If this resonates with you, there are three numbers you need to know.
*  Thirty six thousand, twenty five and one.
*  Thirty six thousand.
*  That's the number of businesses which have upgraded to NetSuite by Oracle.
*  NetSuite is the number one cloud financial system,
*  streamline accounting, financial management, inventory, HR and more.
*  Twenty five.
*  NetSuite turns twenty five this year.
*  That's twenty five years of helping businesses do more with less,
*  close their books in days, not weeks and drive down costs.
*  One, because your business is one of a kind.
*  So you get a customized solution for all your KPIs in one efficient system
*  with one source of truth, manage risk, get reliable forecasts and improve margins.
*  Everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist designed to give you
*  consistently excellent performance absolutely free and NetSuite.com slash cognitive.
*  That's NetSuite.com slash cognitive to get your own KPI checklist.
*  NetSuite.com slash cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations
*  that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it to use Cogrev
*  to get a 10% discount.
*  It's you know, it's been said for a long time, right?
*  That like the personal AI tutor, it's for us for far longer than the technology has been able to support it.
*  You know, the personal AI tutor for each kid is going to change everything.
*  And that was a very like hand wavy, you know, notion.
*  But now all of a sudden it really does seem to be either here or like very closely within reach.
*  I'm interested to hear, you know, whether you think it's here or in reach.
*  But how big of a deal do you think this is?
*  You know, people talk about the two standard deviation effect, which is basically the idea that like
*  if I understand the literature correctly and if perplexity is helping me synthesize the literature effectively,
*  basically the most effective thing ever found in education is one on one tutoring.
*  Is that kind of the premise, you know, that you're working with as you build these products and, you know,
*  with a few months now in market, you know, do you still believe that two standard deviation effect theory?
*  And where do you think Omnigo is on that, you know, on that curve?
*  What you're referencing is Benjamin, Benjamin Bloom's two Sigma study,
*  which is something that we have that's been part of our essential pedagogy at Khan Academy really since the very beginning.
*  The idea of using technology as a way of personalizing the experience for every single learner, right?
*  That like we have this one size fits all in the classroom.
*  But how could we imagine a world where you can build something that's personalized to each student?
*  And, you know, in that study, there's something that shows that even in this setting where there's one teacher to 30 students,
*  if you do mastery based learning, that can also be a significant increase.
*  I think there's at least one standard deviation improvement over over a normal classroom to do mastery based learning,
*  even in a 30 to one setting. And then there's the, you know, one on one is with mastery based learning is the ideal.
*  Define for me, mastery based learning. Is that like demonstrating I can do it?
*  It's not moving on to the next concept until you've mastered the previous one.
*  Whereas today in our in our system, students kind of move from the fifth grade to the sixth grade to the seventh grade, regardless of how well they've done.
*  Right. So if you get a C in Algebra 1, you're still moving on to Algebra 2.
*  What are the chances that you're going to be able to be successful with Algebra 2 when you clearly have significant gaps and these gaps form over time?
*  If you're getting lower grades earlier on in your in your school year.
*  And so the idea with mastery based learning is you really shouldn't move on to the next concept until you've mastered the previous one.
*  At the very least, gotten to proficient on the previous one.
*  There's an interesting distinction between those two terms.
*  But really, it's like you should have a good understanding of it rather than moving on to the next concept.
*  Yeah, the old I miss that day in school joke.
*  Except you're you're not allowing people to kind of fall through the cracks by, you know, having missed a day in school or a concept.
*  Yeah, exactly. And tons of kids these, you know, I remember being in school.
*  You miss a day. You don't catch up.
*  You don't remember what you learned or, you know, and that's the idea with, you know, I even remember being in university.
*  If you're in the lecture, don't have a great teacher, you daydream, you're tired, whatever you miss a section, you're confused about the about the next part of the lecture.
*  And now you can't even listen to the lecture because everything was built on that.
*  And the idea with Khan Academy with videos was you could pause it, you could rewind it.
*  There's no judgment. And so that enables you to kind of do that personalized experience and really just like focus on what it is that you're learning.
*  And now with with AI and large language models, we see the ability to emulate even further down the kind of that that that study in getting into that one on one tutoring.
*  My opinion is that in 10 years from now, I don't I don't think there'll be any kid who's learning without a personal tutor next to them on demand available all the time that knows everything about their, you know, their learning history, which can help them identify where someone might be struggling right away.
*  If they give permission to also understand their interests so that they can kind of motivate them more if you if you make a problem based on, I don't know, the Avengers or soccer or something like that to be a lot more motivating than, you know,
*  whatever generic problem that the student is given.
*  So I think in 10 years, my prediction is that everyone will have this available, whether or not it's going to going to achieve the same results as the study of a human tutor.
*  I think that still remains to be seen.
*  It's interesting because I think that, like, emulating the tutor in some ways, you don't want to emulate the tutor exactly because tutors, if you're getting help from a tutor, unless that tutor is built like a long history and a long
*  relationship like a parent tutoring a kid, that's different.
*  But if you're working with a tutor that you just met, you know, if you're a kid, you're maybe hesitant to share the tutor doesn't really know what motivates you doesn't know what you've been struggling with.
*  And so if you're if you're using AI and you have that as a kind of a tutor on the side, since, you know, in the early days of you learning, it's going to know everything about what you've been doing up until that point.
*  And if it knows your interests, it's going to be able to be more personal to you.
*  And it's on demand and it doesn't judge you.
*  Right. Not to say that tutors judge you, but, you know, everybody's different in the way they teach.
*  At the same time, the difference is that a tutor is still, especially in the more advanced areas of of learning, is still going to be better if they're experts in that field.
*  So, kind of go still sometimes, you know, and obviously powered by GPT four.
*  It still makes math mistakes. Right. Or if you get into some of the more advanced concepts, it sometimes gets confused.
*  And so I think that is most likely going to get solved.
*  That's a problem that is getting getting math perfect.
*  It's still a it's a research problem that is not solved yet in the in the world of large language models and I if we can solve those problems with large language models, and I believe we will be able to.
*  Then I could imagine that it could be just as powerful of a really, really great tutor.
*  Yeah, it's fascinating. So are you guys still using exclusively GPT four with kind of instructions or have you made a leap into fine tuning it as well or like starting to use different models in combination?
*  How has the sort of model stack evolved for us?
*  Well, I guess we're a small organization, and I think that if GPT four hadn't kind of landed in our lap that allowed us to do something with zero shot and few shot.
*  It would have been a lot harder for us to I think have built this because fine tuning a model is this or building a model based on your own information your own data is a pretty huge effort.
*  So when we tried this with GPT four and like I mentioned such a huge aspect of this of the success of this is being able to be Socratic not give you the answer.
*  And so the like the power of GPT four being able to do that was kind of essential for us now in terms of the mix today.
*  There's still vast majority GPT four, there are certain activities that we've experimented with. So within Convigo, there's, you know, you can try you can get tutor on the side when you're working on content like getting doing a quiz or, you know, reading an article or watching video.
*  But there's also a collection of activities. Right now we're kind of talking about them like a they're like a demo disk that you'd get when buying a game console. It's like, there's a few of these things that you can try out like craft a story with the AI or talk to a historical figure like these are it exists in this user interface that you can imagine over time will get embedded within our content.
*  So if you're doing history lesson and you're reading about Isaac Newton, then maybe directly from there you can ask Isaac Newton a question. But right now it's just kind of confined in this activities, activities area and so some of those activities are fine with something like GPT 3.5, because it doesn't matter as much whether or not the model can kind of follow very specific instructions, but it's basically a no go when it comes to doing any of the tutoring activities or doing tutoring with a computer.
*  So it's like tutoring within the content to use anything other than GPT 4 so far. I think there's other models that are coming out that are looking promising llama to we haven't tried that yet. But those are things that you know we want to explore. It's really just the challenge right now is just the opportunity cost of doing that relative to so many other things that we have on the road map.
*  Makes a lot of sense to me. I mean, I kind of always explore this question of how people think about cost and it sounds like you think about it pretty similarly to how I think about it. And you may also have, you know, I don't know if there's any sort of special, you know, nonprofit kind of status that helps you ease the cost burden.
*  But in most business context, I kind of tell people just use GPT 4, you know, get your thing working first and then you know, kind of think about shaving some cost off later opportunistically. Sounds like that's basically how you're thinking about it too.
*  Exactly. Yeah, I mean, I think it's kind of the classic like startup go from zero to one like build something amazing and sort out the monetization later. Right. You want to like, you want to get it to the point where it's better that 10 people absolutely love your product than trying to build something mediocre for 10,000 people.
*  Right. And so I think like for us our goal, the expression that I've been using with my team is like, let's just focus on finding the magic, because there's magic here. And I think we've only even scratched the surface like a lot of the experiences that, you know, I know you've tried to cut me go out and a huge portion of that experience has just been like a lot of back and forth chat conversations, but we think there's so much that we can do that that goes beyond just like that back and forth interaction.
*  Right now we're building an essay writing tool where, you know, you write an essay, and can be go well, you can ask it for feedback on in a series of dimensions and you might say, Okay, give me a feedback on grammar and spelling, and then it'll kind of like highlight a bunch of the areas where you've kind of, you know, you can improve your grammar and improve your spelling.
*  And it can do that in a number of ways. And so, doing that as a back and forth is painful, right, you've probably tried to use chat GPT, or you like pasted an essay or an article you're writing, and then say, give me some feedback, but it's hard because it can't just comment directly on like the parts of the UI.
*  I think the most obvious thing for a lot of people was let's just jump into kind of a chat based interface, but I think a lot of people are going to start to, to find ways of integrating this in in in more unique ways and I think we're really well positioned to kind of figure that out because,
*  A, I mean, we have a really strong engineering and product organization, but we have amazing learning scientists and content creators too. And we embed them within kind of the process of creation and, and I think actually that was one of the key things for us in the development of
*  Condigo was we actually took a pretty different approach of building Condigo at Khan Academy relative to how we've built products in the past. It was a bit more waterfall before like PM defined some requirements, design makes some designs, passes it along to engineering.
*  It was definitely not ideal, but we said we think that this could emulate this tutor like experience, but there's no perfect set of requirements we can define upfront. We just need to get the people who are experts cross functionally in a room and hash this out.
*  Get designers, engineers, product managers and learning science folks, lock them in a room, build a prototype, demo it, get feedback and made it right, which was actually inspired by a book that I read.
*  It was called Creative Selection and it was a story about how the iPhone was built. And so we tried to emulate kind of a demo driven development process and that I think that worked really well for us.
*  There are elements where we are using say GPT 3.5. So for instance, we're like extracting insights from the conversation. Some of those are for available for teachers to know like our students going off topic are, you know, where are they struggling?
*  And then there's also an area of extracting interest from students who opt into that experience. This is not happening yet. This isn't launched. This is something we're working on, but extracting interest from students if they decide to opt into it so that when someone asks, why should I care about learning this?
*  We don't have to ask, well, what are you interested in? We can just say, oh, we know you like soccer, so we'll relate this to soccer somehow or whatnot.
*  And when you have that content, it can feel pretty magical. But a lot of that stuff is fine with GPT 3.5. And so we are definitely, when we can use GPT 3.5, like that's definitely the goal because 4 is obviously a lot more expensive.
*  Yeah, 3.5 so fast as well. So several follow up points there. One just kind of note or suggestion, I guess on the writing side, I have found Claude too to be really quite successful as a writing assistant recently, specifically actually for the podcast.
*  I always, you know, we record the episode, we get an edit and then kind of my last step is I'll write this little introductory essay that I put up front. And, you know, I end up kind of losing track of time sometimes, and really wordsmithing these things.
*  And it takes me a while. So I was like, you know, I'm the AI guy, right? I got to have AI help me with this. I wasn't really able to get GPT 4 to like match my style or kind of vibe with me in the way that I wanted it to, but kind of a few writing samples of what I have written in the past that I like.
*  And then today's transcript actually does get me like a pretty decent starting point. So I've been, I'm still very much GPT 4 for the most like demanding analytical things, but Claude 2 is coming on pretty strong for things that are, you know, where I want like an elevated writing beyond what 3.5 can do, you know, kind of needs to be closer to GPT 4, but it seems to just whatever have a better kind of style aspect to it.
*  So, so my questions, I started using this term cognitive diversity, which came to mind when you're describing, you know, getting everybody into the room and trying to kind of figure it out altogether. I think that's so important because, you know, typically you have three people working on a project like this.
*  And it's like one person will be the subject matter expert. I'm often like the AI, you know, prompting expert that's supposed to be able to make the thing work. And then other people will kind of come in with like just random sort of idiosyncratic style suggestions or whatever. And they all seem very additive to me most of the time.
*  But then the flip side of that discussion is like, what exactly is good? Like, what are we looking for? So how would you describe the process now that you have all those people in the room of saying like, okay, how do we want this thing to act? You know, I mean, we've got like the general notion of Socratic tutor, but you know, a lot of details left. So how did you guys approach that kind of effort to sculpt the behavior of the model?
*  Well, one thing actually, I think you met you asked the question, like, are we using doing any fine tuning? And the answer is no, which means we do end up using a lot of tokens, but also fine tuning has its cost as well. And I don't think fine tuning is yet available for four. I think it's just available for 3.5 turbo. So, you know, we're always passing in the context of like the article that you're working on or whatever. And each every time there's like you're getting help on an article, we don't fine tune. But we did do some fine tuning.
*  Before GPT four launched, actually. So open AI gave us kind of direct access to their fine tuning tool. You know, we actually had Sal go in there. So, you know, CEO Khan Academy, as well as a few folks on our content team. And they did a bunch of fine tuning on making it better at being a math tutor. Because one of the one of the things we actually found with with GPT four was like, yes, sometimes it'll just make general mistakes at math. But one of the things that we found was that we did a bunch of fine tuning on how to make it better at being a math tutor.
*  And one of the things that we found was that it was actually more so one of the bigger challenges was that it was it was getting lost in the conversation. So if like, if you were working on something with the AI, and you gave it an equation as a response to a question that it asked you like, oh, what do you think the next step is?
*  And sometimes it'll kind of get confused. It won't be like it won't recognize that equation is the answer to the question that the AI asked. It'll be like, oh, you just gave me an equation. Let's work on that equation now. Right. And so it'll like, continue on helping you with this like new equation that you entered. And that was very common. But once we once we did the fine tuning in the GPT four model, which again was was not launched yet. This is pretty much 14th. That significantly improved the performance of the
*  of it. So I guess like to answer your question, like how, how did we determine like what what it is that we are looking for? How do we determine what we're looking for? It's based on the experts that we have at Khan Academy. Like we have an understanding of what kids might say to the AI and like what mistakes that they would make, they might make. And we would enter that and we would tell the model these are bad responses. And these are great responses and kind of everything in between. And we did that for I think roughly 100 questions. But each question, there's a ton of variation.
*  With that within that. And so I would say, I guess, like going back to my point about it's important to bring the experts in the room. They're the ones who, you know, they have their PhDs in learning science or education. And they've worked in classrooms for years.
*  We have so much educational experience at Khan Academy with with our content creators and also, you know, the fun fact about Khan Academy, given that it's this nonprofit mission based company.
*  So many people outside of even our content team have educational experience.
*  And I came to Khan Academy because I was teaching a university level course on building web applications.
*  And so much of our team is like people who are just interested in education or have done teaching themselves.
*  So that's one thing that's just really awesome about Khan Academy is that wealth of educational knowledge and experience.
*  And I think being able to leverage that as a way of kind of making some assumptions about what works well, I think previously as well, going back to my point about us moving a little bit too slowly.
*  I think we were often way too data driven. And I think that can be a mistake.
*  I think it's important to be data informed, but data driven means your feedback loops are very long.
*  You have to like make a decision based on being assured about something in the data that you see.
*  And that's fine. But iterating in that way can be very, very slow.
*  We didn't have the time to iterate in that way. And so by leveraging the experts, you kind of you end up getting to short circuit that.
*  And obviously, the data informs our decisions, but we don't wait to make decisions based on data.
*  In certain cases, we do like if we're doing an efficacy study that asserts whether or not like something in our product is efficacious, that's obviously where we need to be very data driven.
*  And so there's a time and place for data driven. But when it came to rapidly iterating on product, leveraging the expertise of our team was really important.
*  Just in terms of how things actually went down, am I understanding correctly that basically OpenAI said, hey, this thing, you're telling us this is not that great at math?
*  And then they kind of gave you guys a role in the reinforcement learning process, if I understand correctly.
*  Like, so you guys were I don't know if they use at one point, I think they were a scale AI customer.
*  Maybe I don't know if they still are have their own. But you're using kind of an interface to go in and be like this one or that one or like what's a good response look like.
*  So you guys didn't ultimately you didn't fine tune the model, but you contributed to the reinforcement learning of the of the model.
*  Yes, exactly. I mean, I know they've done that a lot, probably with a lot of different partners.
*  But it's cool to be, you know, sell and teams voices kind of, you know, encoded in the the great tutor now.
*  It is. And and it makes sense when you think about, like, for instance, like, how is this thing?
*  Sometimes I wonder, it's like, it's so good at writing code, right?
*  It's so good at being logical when it's code. But it's like sometimes just so bad at math.
*  Like, why is that? Well, it can train on, you know, millions and millions of lines of great coding GitHub is my assumption about where it's getting its data.
*  And then when it comes to math, where is it getting that training data?
*  There isn't a ton of like widely available online data about like the steps a student would take and like which what would be a good response and what would be a bad response.
*  So I think that's why it was so important for us to kind of take part in that in that training process.
*  And just to be clear, I don't think that necessarily made it better at math, like if it was ever get two plus two wrong or whatever, but it made it better at tutoring you at math.
*  That's the key thing that we trained it on.
*  There's other things that we did to kind of make the math better using kind of like an internal AI thoughts process chain of thought prompting, which I can talk about.
*  But that's a bit different. That's not something that we like did to improve the model.
*  That's a technique that we learned about and implemented.
*  That is all really fascinating. The other thing you said that's super interesting to me is being data informed, but not data driven.
*  And I think I might have to steal that because I find so many examples now where people are and there was just a real famous one in the last two weeks.
*  Right. The GPT four is getting worse phenomenon where all of a sudden it's like, oh, this thing, you know, used to get 25 of these 50 coding problems right.
*  And now it's down to five. And I looked at that and I was like, this is somebody who needs to read the raw transcripts because there's no way, you know, that they've let it get that much worse from one release to the other.
*  And like, you know, sure enough, that turned out to be misunderstanding, I would say.
*  But how do you think about your can you give us a little more color and how you think about striking that balance?
*  Is there a practice that you guys have, you know, where I think some simple heuristics, I wonder if you have any could be really useful in a lot of cases like render no judgment until you read five, you know, transcripts or something.
*  You know, just these like very basic making sure you're in touch with these things because the surface area is so big and mismeasurement is so easy.
*  So how do you guys kind of make that a practice for yourselves?
*  Yeah. And again, just to be clear, like when I mentioned data being data informed, what I mean is like when we're when we're building that initial prototype or getting something in the hands of users, you know, we're not like we want to be able to develop rapidly.
*  But we are we're still looking at the data. Right.
*  So like we're doing we have like a labeling infrastructure where we're going in and trying to label as many of these interactions as possible to get a sense of the performance of this.
*  How much are how much is it actually helping students?
*  How much is that, you know, not helping students?
*  And so data is data still really important.
*  But I think that for us, one one framework that we started using internally at Khan Academy is this notion of trying to really get crisp on like what are one way door decisions versus two way door decisions.
*  So if a decision is something where you can walk through that door, but you can walk out of it easily, then it probably makes more sense to try to move quickly, shorten feedback loops and leverage intuition, because it's not so consequential that if you make that decision that you can that you're stuck with that decision forever.
*  And that's with with Conmigo, especially initially early on when we when we launched it, we we didn't know how well is this going to be received.
*  We launched it under kind of a of this banner called Con Labs.
*  So this this feature set that's experimental, you should only try this if you're willing to to be a tester with us on this journey.
*  And even when we're when we're doing it in in districts today, that's still the framing.
*  It's we're working with with with districts in classrooms that are willing to kind of pilot this technology because there's there's still a ton of unknowns.
*  But there's a lot of decisions that are, you know, if you make that decision, you can't walk backwards.
*  So an example of that at Khan Academy would be before Conmigo, we were actually doing this big project where we shifted our entire back end from a Python modelist to a series of Go services.
*  And we had to decide which language did we want to use because Python two is being end of life on Google Cloud.
*  And we did not transition early enough, and so we decided we're going to shift that whole back end and we had to make a decision which language do we want to go with?
*  And that's an important decision.
*  We spent a lot of time crunching the numbers, finding out the best balance between developer productivity and and and server costs and everything.
*  And so we spent a lot of time being data driven in that decision.
*  But when it comes to decisions that are two way doors, we actually just recently launched something we call or decision records at Khan Academy.
*  So when we make a big strategic shift, we share a decision record with the entire organization.
*  And one of the decision records was formally changing how we work.
*  And one of those was introducing this one way versus two way door framework, which we didn't invent, by the way, it comes from Amazon.
*  But copying, customize always.
*  I think that all makes a lot of sense.
*  So you can be flexible.
*  You can be intuition driven.
*  You can quit, you know, certainly when you're prompting, you can kind of revert a prompt change pretty quickly.
*  It sounds like you built a lot of your own stuff to kind of instrument this and whatnot.
*  I don't know if you have any reflections on that, but I kind of went through a similar thing where for just being a little bit ahead of the curve, you know, we were punished.
*  You and I probably both with there not being a lot of tools that now exist.
*  If you, you know, if you could go back in time and like bring a couple of tools with you, are there any things that you're like, oh God, I wish I were using that.
*  But we've kind of, you know, did this other thing because it didn't exist, you know, when we had to make something happen.
*  Yeah.
*  I mean, I think one would just be Lang chain as a tool.
*  Like right now we're going in and rewriting a ton of our code to be able to use Lang chain so that we can do things like easily swap in models or easily be able to do things like get things in a JSON formatted response.
*  So that would be one.
*  One, another example might be our labeling infrastructure.
*  We did, we built it initially as a custom Google spreadsheet.
*  And there's a few tools out there that we're transitioning to now that do that at scale with like a really great user interface and everything.
*  So maybe that would be another one.
*  It's also hard because we were moving so fast.
*  And so we did have this deadline and like, sometimes it's sometimes tech debt is good, right?
*  Sometimes it's okay to incur tech debt in order to make a launch so that you can be first to market.
*  Because the reality is what happened to us when we got to first to market was there were so many people out there because opening, I really only partnered with us as like one of the key organizations for education.
*  A lot of people, when they saw it, they were like, well, why would I even bother entering this space?
*  You already have done a great job with it.
*  You've executed well and you have the brand and you have the trust.
*  And so it was essential that we did incur a significant amount of tech debt in order to get to that launch.
*  Even if it meant in the overall sense that like in aggregate, had we made a few decisions around not incurring tech debt, maybe the overall development is shorter, but the launch deadline is later resulting in a bunch of other competitors in the space.
*  Joining because, you know, we weren't there first to market and people get excited about GPT-4.
*  And so I don't necessarily think I regret any of the decisions that we made, but over time, there's definitely a lot of things that we're doing where I'm like, this is infrastructure that everyone needs.
*  Right.
*  So for instance, we have an interface for prompt engineers and our prompt engineers are a few, like he, there's some engineers, there's some PMs, there's some content folks.
*  But we built a user interface to allow them to make changes really quickly, test them really quickly.
*  Soon we're looking into building regression testing into that so that we can kind of have a bit more confidence and not have to do a ton of manual testing.
*  But that's a tool that like everyone's going to need.
*  And maybe there's five products out there that are already, that already exists that we can hot swap.
*  But, you know, that's another area where I think there's a ton of infrastructure here that every company, every tech company, everyone in Silicon Valley is going to want.
*  And we're having to write that now because we need it for our needs that maybe we're then going to swap to at a later date.
*  Very similar experiences there where I can remember us building, you know, kind of our own little playground type of thing.
*  And, you know, is this good or not good?
*  And it's like, oh my God.
*  If, you know, but it is tough because you want it, I do, you know, the exact same, the exact same reasons to, right.
*  Wanting to get to market first and wanting to be ahead of the curve.
*  And that's kind of the price you pay to get ahead of the curve, you know, like it or not.
*  So I have to come back and clean up sometimes, but what else are you going to do?
*  When it comes to the capability of the model today, and you understand it's mostly GPT-4, one thing I think a lot about is the, I call it the can-can't boundary.
*  And it's obviously, you know, as the capabilities continue to grow, you know, this boundary continues to get pushed out and out and out.
*  And now, you know, there's a whole lot that it can do, but obviously, you know, you push hard enough in any direction, you eventually kind of found, find the limits of it.
*  How do you think about those limits?
*  Do you have a sense for, you know, just I was doing it this morning and just going like friend Jimmy Cople, who's a outstanding programmer and affiliated with MIT,
*  suggested this task to me of just saying you have a boat sitting in the water and you start to add, you know, mass to it.
*  And what happens to the water line?
*  There's a lot of little subtleties in the reasoning there.
*  And I would say that was that felt like it was right on the boundary to me, like it was very close.
*  I had to give it a couple of hints.
*  It kind of got distracted a couple of times.
*  I, you know, it was close enough that I got confused a couple of times as to exactly what I was, you know, what the right answer was.
*  I even, you know, I was starting to lose confidence in my own understanding.
*  So I guess, you know, how do you think about kind of determining where that boundary is?
*  And I'm also curious as to, you know, whether you consider like just not making the tool available beyond, you know, a certain point, like it probably can't handle string theory at all.
*  Right now, I don't know if you guys have a string theory module, but like as a sort of funny example, there might be areas where it just makes sense to say, hey, like it where I was just not there for this yet.
*  You got to just, you know, it's you and the lecture still.
*  Sorry. So anyway, a lot there.
*  But how do you think about that?
*  We made the decision early on to enable it everywhere because our focus was learning.
*  Right. Like we really wanted to understand the boundaries of this and and see what what people thought about it and be very clear with people up front that like it does make mistakes.
*  It's not perfect.
*  I think we in a lot of ways, because we were building especially something for for students who either get it access, you know, either you're over 18, you get it for yourself or your your parent who gives it to your child or you're in a your teacher gives it to a student.
*  We were really focused on the safety aspect of it.
*  And so like, you know, one of the things that we're really focused on early on in the process was making kind of this like extra moderation layer to prevent the AI from doing things like, you know, going really off topic or talking about inappropriate things and like alerting alerting teachers.
*  When those when those students were, you know, doing things that they weren't intending with the platform, I think when it comes to things like string theory, a I mean, a we teach up to second year university.
*  Courses so I don't I don't think we teach string theory, but maybe we do.
*  But I mean, it would probably be basic intermediate stuff.
*  But I think ultimately, we want to put it out there for students and for them to give us feedback on how well is it going?
*  And I think like over time, we would iterate, right?
*  I think that's an example of a two way door decision.
*  If if we get a bunch of feedback that like, hey, this is just horrible for string theory, then we can turn it off.
*  And we learned and we iterated, but to kind of close the door from learning, I think I think it was the right approach for us in the speed we were moving.
*  I think ultimately for us, one of the big things is like, are we is this harming anyone?
*  How do we reduce that harm as much as possible?
*  And I think for us, you know, it does really well, especially at the lower level, like lower level concepts for math and and whatnot.
*  And I think the older students who are trying it for first year, second year course, university courses are going to be able to have the understanding of like, oh, this isn't working so well.
*  It's not causing me to like get worse at my grades.
*  I can give Khan Academy feedback.
*  I know I opted into an experimental feature.
*  How do you think about the special case?
*  This is one that I've also kind of identified as a frontier capability.
*  And I would say really, in my experience, only GPT-4 does this very much at all.
*  And that is identifying when the user is confused and doing something, you know, being willing to kind of challenge the user's assumption.
*  That can take like, obviously a lot of there's a lot of different flavors of confusion.
*  So, you know, people obviously think a lot about hallucination where the model makes something up outright.
*  And that's bad.
*  But in kind of a, I think it's even subtler and trickier in some ways to figure out when is the user working from some sort of confusion or false premise?
*  And, you know, when should I kind of push back on their assumptions?
*  In my testing this morning, it did pretty well at that.
*  I just did a few, you know, balancing chemistry equations sort of exercises and kind of confidently asserted some wrong stuff.
*  And I got the response of like, I see where you're coming from, but that's not quite right.
*  You know, that was that stuck out to me because I was like, do you really see where I'm coming from?
*  I don't know.
*  You know, but it said it's all where I was coming from.
*  And it did, you know, effectively, you know, avoid getting confused based on my confusion.
*  But I mentioned that I wonder if that or other things are kind of like special scenarios that you guys think a lot about given the the teaching purpose.
*  I mean, I would say we thought a lot about it from the sense of, again, kind of doing a good job at being a good tutor.
*  And what I would say, like one of the key things that probably enables this to be really good and probably even better than chat, because I think chat is really just a direct interface to talking to the model.
*  But ours in particular, we'll do things like, if we detect that you're talking about math, then we will do like chain of thought prompting where it's like.
*  First question, is it math?
*  Yes or no?
*  If it's yeah, if it's yes, then, you know, submit this to the AI to say, you know, think through this out loud to yourself.
*  Like, look at what the student said.
*  Look at the context of the question.
*  Did they get it right or wrong and why?
*  And it will kind of explain it via text.
*  But we don't want to show that to the student.
*  That's almost like when if you're if a tutor is helping a student before just answering a student, they're like thinking about it like, oh, where was this misconception?
*  That's kind of like the AI private thoughts.
*  And then we feed that response into the next call to the AI to say, hey, tutor the student now based on the thoughts that you had.
*  And that significantly improved the math.
*  And I would imagine that it's doing that same thing in the scenario that you're describing with chemistry.
*  I think it's probably like the ability for it to really like think through its thoughts out loud before it gives you the answer is probably key to what made it do such a good job.
*  You know, a lot of these little self critique techniques that are being developed, I find really fascinating.
*  You've probably seen the tree of thought approach that kind of combines chain of thought with essentially like a tree search and allows the model.
*  This I think came out of I think deep mind, actually.
*  It may foreshadow some big things that they're working on, but as presented in this initial paper, it's not like that crazy of a concept, but it basically just allows kind of extends what you're describing with chain of thought, but allows it to go down multiple different tree, you know, paths of a tree.
*  And then look at itself and kind of figure out, you know, which of these appears to be the best path and then continue to go down that path.
*  So it leverages this ability for self critique, which again, I saw this morning, you know, with my Archimedes principle thing, there was these, there were a couple points of confusion where I was like, wait, is that equation for that?
*  And sure enough, it would say, oh, nope, sorry, you know, that I, that the actual equation for that is whatever.
*  And then it would get it right.
*  And I think that whole thing could have maybe happened behind the scenes, though.
*  Your token count, you know, goes, you know, kind of multiplicative potentially as well.
*  So that's definitely something still to, to keep in mind.
*  Yeah.
*  I mean, that sounds like it's almost like a combination between chain of thought and few shot, like give it a few shots of chain of thought prompting and it, you know, it's more likely to.
*  To do the right thing.
*  So that's interesting, but we wouldn't even bother checking is it math if it wasn't more expensive, like we might just do that for, for everything, for every response or every input that the user sends you.
*  Think of think out loud about what you want to say first before you say it.
*  And I think that would probably improve the experience across the board, but that's too expensive.
*  And so we really like reserve that for the places where it's like really important for things to be accurate.
*  What other things are you using behind the scenes?
*  You've got the chain of thought, you know, other common development patterns would be like.
*  Doing some sort of embedding backed, you know, database of examples.
*  It doesn't sound like you really need that because you have like just the article context there.
*  It can kind of curate things in a designed way, as opposed to a retrieval way.
*  That's something we've been talking a lot about.
*  Like I'll give you actually an example of where we might leverage that, which is for students are two most used areas of Convigo are one is in an exercise.
*  So if you're getting tutored on an exercise on an exercise, it has the full context of the question, the multiple choice or whatever the question is as the answer.
*  It has hints. It has like the full written hints from our content team.
*  And so that's actually where it does the best job.
*  But there's also another activity called Tutor Me STEM and Tutor Me STEM is a place where you can ask it any math question.
*  Now, it doesn't have the answer to that math question, at least right now in the current implementation.
*  And so it's not quite as accurate.
*  You could imagine a world where not not an embedding search, but like maybe we solve that with Wolfram first or we solve that with just a Python back end thing and then inject that into the conversation.
*  Like, give it the answer first, give it the step by step before talking to the student to make it equivalent to the exercise experience.
*  So that's I think like an area that we're exploring in terms of like places where we do use embeddings.
*  One of it is to reduce hallucinations.
*  So we just embarked on this project that we launched recently just called Expand Conmigo Knowledge Base.
*  So like a lot of a lot of people were writing into us saying like, hey, this thing doesn't even know about itself.
*  Like if you ask it, what is AI power?
*  And AI power and Conmigo is this notion of like you have a certain amount of tokens a day.
*  The limit is very high because it's not about, you know, reducing costs.
*  It is, but it's about like making sure no one just abuses it.
*  So there's like a 200,000 token limit.
*  People were saying like, why, why doesn't it know what AI power is?
*  And so now it knows like, if there's a, if there's a question that results in a similarity match above a certain score, then, you know, we inject that information into the prompt.
*  So that when the AI is going to respond to the user, it has that context and it works really, really well.
*  Previously, we were also doing things like every time you sent a message, we would do related links.
*  But sometimes it would just be off.
*  Like you'd ask a question about algebra two and it would send you to an MCAT course.
*  And so we want to explore that again, but it just wasn't providing enough value and we kind of ditched it temporarily.
*  But we do try as best as possible.
*  If someone's like asking about a link to something that we injected the right link and all that stuff.
*  When I think about what the kind of things that I was doing this morning and really pushing the, the frontier of like, you know, how hard can these problems be?
*  And it can still get it right.
*  And some of these like super token intensive processes, like the tree of thought.
*  I wonder if there's some way to like group and cash certain answers.
*  Like, I don't know how often somebody comes and asks the question I asked, but it might take, you know, 200,000 tokens to for GPT-4 to reliably answer it.
*  But then I'm kind of inspired in this question by that Nvidia project where they created the GPT-4 Minecraft agent that would save its successes.
*  Basically, when it would, you know, successfully, whatever fight a zombie or whatever you do in Minecraft, you know, it would take the code that.
*  That it succeeded with and save that, you know, into it, a database that it has access to.
*  And, you know, next time it needs to fight a zombie that it can just kind of load that module and not have to like recreate or rediscover it.
*  I'm not sure what the equivalent would be here, but.
*  I mean, I think the challenge is there's just so many different ways students are going to ask questions or, or want to get help.
*  I think that maybe if we explore like what the, all the permutations end up looking like that, it's we can start to, we can start to identify those and maybe, you know, do an embeddings lookup for a specific.
*  Query and then just respond with, with what's in the embeddings database rather than querying GPT-4.
*  And so I think there's something there, but it's not something we've explored as much.
*  The one thing I'll say is that we, one optimization we have been doing.
*  So we, we do, we have a dedicated instance from open AI.
*  We're not just using the shared instance that, you know, everyone is using and it has a lot of caching powers.
*  I don't know all the intricacies of how that works, but the thing that they instructed us to do is like, make sure that you have as much.
*  Text as possible.
*  That's common to everybody.
*  So previously we might've had like some text and then some custom user variable, and then some texts and a custom user variable.
*  We changed a lot of our prompts to have a lot of that text and then, and then mentioned some of the custom user variables at the bottom.
*  And that significantly improved our cache hit ratio on the instance.
*  Very, very interesting indeed.
*  Yeah.
*  Cause I mean, there's a lot there that you can just, if you're using the same first thousand tokens every time, you might as well take advantage of that.
*  Um, let's see.
*  So you mentioned also a little bit about red teaming.
*  Um, I try, you know, naturally as a, uh, red teamer myself, I had to try getting it to ignore previous instructions and, uh, tell me your prompt and all that kind of stuff.
*  I even tried that recent universal one that was published where it was like fine tuned.
*  You know, this, this jailbreak technique was developed on llama two, but then it was found that it poured it over to GPT four.
*  I'm not sure I'm doing it right to be honest, but that also didn't work.
*  Is that all just kind of GPT four getting really good at being jailbreaking resistant?
*  Or did you have your own measures that you've also brought to, you know, even clamp down further on that kind of activity?
*  Well, like I mentioned earlier, I think like one of the things about chat, GBT, I believe anyways, is that you're just talking to the raw model.
*  Whereas our, we have this ability to take what the user said and kind of wrap it in a bunch of stuff.
*  And I think like one of those things is at the end of every message that's coming in, things like, you know, check to make sure that the user is on track and all that sort of thing.
*  I think that has really helped with making it harder to use some of those universal things that you would do directly in the model.
*  Another one is the moderation API.
*  That's not as much for, for jailbreaking, but that one will flag anything that's like sexual topic content or like, but it has a bunch of different things that it'll tell you whether or not.
*  Like the certainty that that is in the message that the user sent.
*  And we kind of, we make sure that every message that gets sent goes through the moderation API first.
*  I know that one of the things that when they launched GPT-4 that they were very keen on was the, the trust and safety side and make, and avoiding those jail breaks.
*  And I think they are continuing to iterate on it.
*  So I think it is also the power of GPT-4.
*  The model that we ended up using, I'm sure they did a huge amount of iteration on the June model, but that one, that was a big kind of sticking point for them of that being really, really done really well.
*  Yeah, I really respect.
*  I mean, it's, it's a huge problem and I don't think they are, you know, anywhere yet super close to having it fully solved, but definitely a ton of respect for how much work has gone into that.
*  Relative to what we saw earlier, I don't know if you went off the beaten path in your early experimentation, but the early version compared to now is definitely a night and day difference.
*  Oh, it's yeah, it's absolutely huge.
*  We were super impressed with the progress they were making as we were getting these new weekly models.
*  Is it personalized today?
*  It seems like not super much, but that seems to be part of the future vision is to know the user's full history and all that kind of stuff.
*  Yeah, I mean, to the extent right now and the current, you know, what's released in production right now, it's not very personalized beyond.
*  You can do things like customizing the reading style, so you can do like simple, complex and maybe professorial.
*  And when you're working on an exercise, it'll know like, are you already unfamiliar or familiar or proficient or mastered, but nothing beyond just the one thing that you're working on.
*  So the plan over time is for it to be able to collect your interests again, as on an opt in basis for it to know more about the kind of the history of your educational experience.
*  Like an example that we're looking to solve, for instance, was one student gave us the feedback that like, hey, you know, I asked it about sign and then it asked me like, well, what do you know about sign?
*  But then I went on to tan and then it was like, well, before I talked to you about tan, let me like, what do you know about sign?
*  And she was like, I already told you about sign like 10 minutes ago, but because it was a different conversation or a different question.
*  And every time we go to a different question, we kind of start a new conversation.
*  She was really feeling like, how did you not know that?
*  Like we just talked about this.
*  And even though from a back end perspective, this is like a new thread, it's a new conversation.
*  Users expect that that journey to feel continuous.
*  And so that's also on the roadmap.
*  Cool.
*  Yeah, it's interesting.
*  The, the disconnect between what people.
*  Intuit the AI to be doing or capable of, or whatever, and what it's actually doing, you know, is often, I think super, you know, super interesting place to, to study.
*  What do you, how do you think about kind of educating the.
*  Users slash the students right now, they're both users and students.
*  About AI and kind of the nature of AI, like I could imagine that being in product, you know, messages like, Hey, FYI, this thing only knows, you know, each chat is a new day or whatever.
*  It has no, you know, memory and kind of just, just trying to shape expectations that way.
*  But I can also imagine like a whole AI course, you know, which could be, you know, potentially a best seller on the platform.
*  So what are you guys thinking right now about AI education?
*  I don't think my memory is serving me wrong.
*  We do have a AI course already that we, you know, give us something that teachers can read or they can assign to their students.
*  So that's something we actually, I think launched in March.
*  So we do have a lot of stuff in our support article area, which a few of those key ones is available also in our embeddings database.
*  If so, if a student asks a question about how certain things about how AI works, if the match is there, then it'll provide the student with that answer directly in the user interface.
*  There's a few key things that we wanted to make it very apparent to the learners and teachers and parents.
*  One is that it does say right at the bottom, Conmigo makes mistakes sometimes.
*  Here's why. And you can click it and it'll link you out to a Zendesk article to help you understand why that's the case.
*  And another one is just making it very clear to students and children of parents who've granted access that the logs are all available by their teachers and by their parents for safety reasons,
*  because it's important that parents have trust in this platform and they want to be able to know what their kids are talking about.
*  How about the future of multimodal functionality?
*  That's something that a lot of people are kind of highly anticipating.
*  And GPT-4 obviously has a version that will bring some of that online.
*  But I also could imagine that your multimodal plans might be quite different than others.
*  Like GPT-4 is going to allow us to understand images.
*  But is that something that you're super excited about, or would you be more like going toward speaking in voice to the user as kind of the next?
*  Because I can imagine that might be really helpful for a lot of folks to be able to hear and not merely just read off the screen.
*  So as you get beyond text, what do you think are the most exciting text plus sort of experiences?
*  Yeah, we've been doing experiments with a few things.
*  So one is text to speech is something we've been trying a bunch of different text to speech providers,
*  mainly because ultimately, I think one of the biggest issues with especially going back to the fact that a lot of this is a back and forth conversation.
*  It's reading a lot of text. And even if we tell the AI, like write it as simple as possible, right, like the explain it like M5 kind of notion,
*  it's still a lot of text to read. And there's a lot of learners out there who may be in the seventh grade,
*  but they have a fifth grade or a second grade reading comprehension. And that can make tutoring a really big challenge.
*  So text to speech is really high on our roadmap. We are experimenting with a lot of things.
*  And I think I think students are going to love it.
*  I think our hope is that we can give students a number of different voices and whatnot to try out and test.
*  And maybe there's even ways they can unlock cool voices is like an engagement mechanic.
*  I'm not sure. But those are all things that we're experimenting with right now.
*  When it comes to, I guess, like the vision side of things, we haven't spent much time there,
*  but it is something we're very interested in, like the notion of maybe you eventually might have right now.
*  It's not available, say, on our mobile app, but maybe one day,
*  Conmigo is available on our mobile app and you can open up the mobile app and scan your homework and get step by step help through that.
*  Another one is within the user interface, you can actually draw at any point when you're working on an exercise.
*  So if you have a Chromebook with a touch screen or if you want to just use your mouse, obviously,
*  mouse is awkward for doing math equations, but like that's a pretty heavily used feature.
*  And we're thinking about the notion of like, well, what if a student is doing their math and they're drawing it on the screen and they're about to make a mistake?
*  And the AI maybe could I mean, we haven't thought through this deeply because obviously you want to let students make mistakes
*  sometimes. And I'm not saying we would do this every time, but like you can imagine it notices when you're about to make a mistake.
*  Is there ways it can kind of give you hints, especially if you made the same mistake a couple of times or something?
*  Maybe it can intervene and and kind of say, hey, like I noticed that you're you've been doing this a few times.
*  Like, why do you like why are you why are you making why are you doing that specific step?
*  Can you describe why you're doing that to me? And I think something like that could be really engaging.
*  So those those are things that we are super interested in, but there's a lot in a roadmap and sometimes you have to make tough choices about what to prioritize.
*  What is the state of like evaluation of this? You mentioned, you know, kind of toward the top of the conversation that if we're going to try to do a real assessment and demonstrate efficacy,
*  then we need to be obviously more careful about numbers. It sounds like you might be working on something like that.
*  Do you know how far you are from being able to put a stake in the ground that you're confident in on the results?
*  Yeah, I don't know if I have a timeline specifically, but I'll tell you kind of like the way we've been thinking about it.
*  So one is that we are just trying to see, like, you know, are people a spending more time on Khan Academy?
*  Just engagement regardless is still good, even though, you know, it might be more time on.
*  Well, if they're spending it all just crafting stories or whatever, but that's still good for kids reading comprehension.
*  So one is just are you spending more time learning? That's interesting.
*  The other one is like, are you working on are you just working on more stuff than you were before?
*  But ultimately, the thing that we're looking towards is having a standardized assessment where a student, you know, for instance, there's the there's a test called the map growth test.
*  And we are we actually partnered with a company who many years ago who administers that test and we.
*  They recently acquired, I don't remember their their new name, but they have this test called the map growth test.
*  And what we did was we partnered with them to, you know, when a student would do that test, we would ingest those tests.
*  Then the teacher could kind of assign whatever they wanted to each individual student, depending on the results of those tests, to really bring this personalized experience into the classroom on a per student basis.
*  And then the student would work on those four goals.
*  They would have like one goal for measurement and another goal for geometry and like in like four different categories.
*  And then they would work kind of in a self paced mode on Khan Academy, using it like X X number of times per week, depending on how that teacher decided to implement it.
*  And then they would do the map growth test again.
*  And we had some students who who were using that and then some students who weren't.
*  And we have an amazing research and efficacy team who could go into the details in depths that I could never.
*  But, you know, that we we saw that we had a statistically significant improvement in the learning outcomes of those learners who were using who were doing the map growth test with Khan Academy versus without.
*  Now, that's not with Conigo, but the hope would be that we could do a similar test where students who are using Khan Academy.
*  And who are taking the growth, the map growth test once a quarter are then compared to a cohort of students who are using Conigo alongside of Khan Academy content.
*  And then we'll compare what are the gains in the map growth test.
*  So that's kind of like where we want to go long term, really, like testing this against the standardized assessment is kind of the holy grail of determining it, determining the efficacy.
*  But we're a little ways away from from getting there.
*  There's a lot of logistics to set up.
*  How widely are you deployed today?
*  And I guess also, you know, big pictures you think about the future and just the, you know, the original vision of Khan Academy.
*  What would it take or what is the outlook for some sort of universal public access?
*  I mean, obviously, tokens are expensive.
*  It doesn't sound trivial to get there, but I imagine that's the long term North Star.
*  So how do you see that possibly happening?
*  Our mission is a free world class education for anyone anywhere.
*  And the challenge with that is like a mission statement is all about where you want to be many, many years from now.
*  And I think the way we kind of think about it is because we can't do it for free, it's still significantly cheaper than, say, someone paying for a real tutor, right?
*  Folks who have more privileged position, they can hire tutors and they can get that help directly.
*  And there are some kids who just don't have that access.
*  And so we still think for independent learners signing up, it's still there's still a lot of value there.
*  But where we've really been focused and kind of trying to level the playing field as much as possible in the interim,
*  while we just can't give it to the entire world for free, is we sell Khan Academy to school districts.
*  And now there's like an extra premium if a school district wants to get access to Khan Academy.
*  But because we're a nonprofit, we don't have to, you know, we don't have to focus on like, how do we sell to them?
*  The school districts with the most money instead, what we do is we really focus on who are the school districts who have a higher percentage of historically under resource learners.
*  And we do that via a proxy of like schools that have a higher percentage of what's called free and reduced lunch.
*  So those are the schools that we generally try to target to sell to.
*  And if those schools can't afford it, we tend to partner with corporate sponsors, especially the ones who are local.
*  Like if a corporation from Kansas wants to help in their local community, they can sponsor per student and work with us to kind of offset the costs that the districts can't afford.
*  And so that's what we've been really focused on is working closely with the districts who we believe could use us the most.
*  And this is kind of a long term aspiration.
*  But as part of what we're doing with Conigo is, you know, a lot of nonprofits like museums have this notion of a membership.
*  And so we want to create this tiered system of membership where if you do want to pay more, then we will take the offset costs, at least is what we're talking about,
*  taking some of those offset costs and giving them to students who can't afford it.
*  So maybe we work with another nonprofit who has direct access already to many kids who are historically under resource and we give them a bunch of licenses.
*  Those are the things that we're exploring.
*  But I think right now our main focus is getting it into the hands of students and districts who we think can benefit from it the most.
*  And again, right now, it's very much like on a trial basis as well.
*  But we want to build this and get the feedback from the students who aren't just the ones who have all the most resources and all that stuff.
*  We want to get it in the hands of the kids who, you know, maybe who don't love math, who think they hate math or they're not good at math.
*  We want to help want to get it into those hands and help kind of create growth mindsets and create a love of learning.
*  So, you know, if we if we don't get into those classrooms, then it's really hard to get that feedback.
*  And it's really important for us to do that.
*  You know, I think about the technology, I think about the student.
*  But obviously, there's you're alluding to here.
*  There's the distribution through the districts and the teachers and a lot of stakeholders in this game.
*  So how has that gone so far?
*  Yeah, I mean, one thing we haven't talked much about, and this is mainly because I'm actually more I'm the director of engineering for the learner experience.
*  And there's another director who drives the teacher experience, although we own the core platform.
*  But, you know, there's a whole teacher side of this equation as well, creating creating custom lesson plans,
*  getting insights into where your students are struggling, creating differentiated learning plans based on that using the large language model.
*  So there's a there's a whole thing in there.
*  But, you know, I think teachers have really taken to it.
*  A lot of teachers are feeling like it's saving them a significant amount of time.
*  And then the students really like it. They love that.
*  It's some of the assumptions that we made around having a tutor that can do a pretty good job at tutoring you that occasionally makes mistakes.
*  But is there 24 7 and it's not judging you students really responded very positively.
*  And then there's other examples to say, for instance, one of the biggest things that some students love who were English isn't their first language is being able to speak to Conmigo in their native language.
*  And Conmigo to be able to interact in that way has been huge because there's just some areas where the language is too difficult in English.
*  And they've and folks have responded very positively to that.
*  So the reception has been quite positive, which is why we're continuing to invest so much in this product line.
*  I've been surprised by this, how positive reaction has been in a couple of places in medicine.
*  Is another one where I had sort of if you'd asked me a year or when I was first trying GPT-4, like, how is the medical establishment going to react to this?
*  I would have forecast, you know, probably quite defensively.
*  And I might have said the same about the education establishment, if that's a term that makes sense.
*  But certainly on the medical side and it sounds like also on the education side from your account, maybe just because folks are actually just super overloaded and really need help and want relief.
*  I've been surprised on the positive side as to how eager people are to get the best out of these tools.
*  We were worried that there would be teachers who would view this as this replacing their jobs.
*  And that's like the last thing that we would ever want.
*  We don't envision a world where, you know, there's no more classrooms and kids are just like learning next to a computer their entire life from first grade to 12th grade.
*  Like school is a social experience and building those relationships with your teachers and your classmates is such an important part of it.
*  And really, this is all about just freeing up the teacher to be able to to do more of the personalized approach and help.
*  And ultimately, you know, if Kanmigo can't help with something, then the teacher can go over to them and help them directly.
*  But, you know, previously, maybe there would be 10 hands raised while the teachers helping, I hope I can get to all these kids.
*  Now, maybe there's only two hands raised or the teacher can really work towards building more like project based experiences rather than having to do like one on one help with as many students as possible and struggling.
*  So really, we're trying to just supercharge the classroom and unlock things for teachers in ways that they would never be able to do before.
*  We would never our intent is not to replace teachers by any stretch of the imagination.
*  Is there like a standard price that is publicly known?
*  Is it a per student per month sort of deal? Or how does the business side of it work?
*  It is a per student per month. And again, there's a lot of, you know, offset costs with with corporate sponsors or sometimes not just corporate sponsors.
*  But even ourselves discounting it to be able to get it in the hands of users who you think need it the most.
*  Yeah. So I got access with the recurring monthly donation of nine dollars a month, which I signed up for with my PayPal account.
*  So, you know, that's under half the price of chat GPT pro.
*  And, you know, presumably that's kind of order of magnitude. Same same deal that you're offering to schools.
*  I have one final question. Anything else that we didn't talk about that you wanted to make sure we touched on today?
*  One of the things that we're really excited about potentially doing in the future that's on our eventual roadmap is things like multi user activity.
*  So right now it's this it's this very like one on one thing between a student and an and an AI.
*  But you can imagine a world where the AI is doing things like differentiated learning and then making a recommendation to a teacher that says, like, hey,
*  I'm noticing that these five kids are struggling with this concept.
*  These 10 kids are struggling with this other concept and these two kids are struggling with this other concept.
*  Would you like to create a breakout? And maybe the teacher just says yes, or they can adjust it.
*  And then there's like this experience where maybe the students are actually grouped, where the same students are struggling with that concept.
*  They're getting grouped and kind of tutor with the AI and they can all chat with the AI.
*  Or you can imagine a world where there's engaging classroom mechanics where you're crafting a story one on one with the AI.
*  But imagine, like within the classroom, the different students are taking turns contributing to the story and they create this collective story together,
*  kind of like Mad Libs, but I don't know, or an AI facilitating debates and grading between students.
*  I think there's just a lot of things that we're really excited about when it comes to classroom interactions that go beyond just this one on one experience.
*  And those were just a few examples I gave you. But I think we again, I just I think we've really only scratched the surface of of what we can do with education.
*  Obviously, obviously, when the new technology comes out, you just the initial propensity is just to emulate what is already happening in the real world.
*  But I think there's a lot of magic to discover. And I'm just really looking forward to to finding that magic.
*  I think you guys are off to a phenomenal start. And that's a great forward looking product vision.
*  My final question for you is just going to be what is the story you tell yourself about the impact that this can ultimately have as it does reach global scale?
*  Like, how do you think it changes the world at large?
*  Yeah, I mean, even the question just gave me goosebumps. It's it's funny when I joined Khan Academy, I remember, you know, I'd watched a lot of Sal's TED Talks.
*  And as a big part of why I joined, one of the things he always talked about was how, you know, he he believes it's so important that students kind of are able to find their gaps and fill those gaps.
*  And when I joined in 2017, I kind of assumed that the software already did that. And I was surprised that it didn't like you can go and, you know, in a lot of ways, figure out what the gaps are.
*  Like, if you're struggling, you get to work on things that you're on time and pace.
*  But the way I kind of see it is finding gaps on Khan Academy when I joined was really like, at best, O of log N, like you could go in the middle if it was too hard, chop that list in half, go in the middle, chop it in half, or, you know, O of N, but work backwards or something like that.
*  But there was nothing that really like was able to kind of notice where you were struggling, really pinpoint that and and help you with that specific skill so that you could get back to your grade level work and be unblocked and not develop these gaps over time.
*  I think, like, preventing the Swiss cheese gap for students is just such a huge opportunity with what we are building with having this AI based tutor.
*  I just feel like we have the opportunity to dramatically accelerate that at scale.
*  And I think ultimately, that's what I'm just so excited about.
*  I think, like, not everyone has access to a smaller classroom where they can get all that personal help.
*  A lot of students don't have, you know, parents who can help them with every subject.
*  And it's kind of like with the way I think about the amazing stuff about Khan Academy was with Sal creating all these videos for all these different subjects.
*  Maybe he's not the best at teaching a specific subject.
*  Maybe there's one person who's the best at teaching that one very specific subject.
*  But we really kind of like leveled the playing field with with those videos by saying everyone in the world has access to Sal as the world's teacher.
*  And I think with Commigo, we're just taking that one step forward and going back to the whole thing about the potential effect sizes of having one on one tutoring.
*  I can't wait to see those efficacy studies because I think they're going to show that this thing can really help students.
*  And I think it can really help change the world.
*  We'll see. Brilliant. Sean Jantzapar, thank you for being part of the cognitive revolution.
*  Thanks, Nathan. It's a pleasure.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work, customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it, and I recommend you use it to use Cogrev to get a 10 percent discount.
