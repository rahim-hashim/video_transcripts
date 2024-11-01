---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 3715s
Video Keywords: []
Video Views: 2036
Video Rating: None
Video Description: Tune in to this special episode of the Cognitive Revolution for AI scouting report. We cover the state of the art in AI applications for medicine, key AI concepts, and how these technologies could influence society. 

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

RECOMMENDED PODCAST -The Riff with Byrne Hobart
Byrne Hobart, the writer of The Diff, is revered in Silicon Valley. You can get an hour with him each week. See for yourself how his thinking can upgrade yours.
Spotify: https://open.spotify.com/show/6rANlV54GCARLgMOtpkzKt
Apple: https://podcasts.apple.com/us/podcast/the-riff-with-byrne-hobart-and-erik-torenberg/id1716646486

CHAPTERS:
(00:00:00) Introduction
(00:06:13) Current State of the Art
(00:08:34) Medicine
(00:13:49) AI limitations
(00:17:01) AI capabilities
(00:17:02) Sponsors: Oracle | Brave
(00:19:09) How AI works
(00:24:05) Information processing
(00:28:51) Curated data sets
(00:32:52) Sponsors: Squad | Omneky
(00:34:38) Transformer
(00:37:11) Scaling
(00:39:59) Emergence
(00:44:03) Grokking
(00:50:30) Best practices for business
(00:53:38) Live Players
(00:58:33) What to Watch
(01:00:35) Final Thoughts
---

# AI Scouting Report NOT Investment Advice Edition
**Cognitive Revolution:** [June 01, 2024](https://www.youtube.com/watch?v=FUbqQmVVabQ)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution. In today's episode, I'm excited to share an AI
*  scouting report that I recently presented to a group of retail investors. This fast-paced,
*  high-level overview is obviously quite different from our usual deep dive format, but I definitely
*  think it's worthwhile for all of us to occasionally take a step back to review the fundamentals and
*  survey the current AI landscape. I also hope that this can be a compelling introduction for
*  intellectually curious people who haven't been tracking the field and who need a fast on-ramp to
*  understand where we are with AI today. Because I was told that the group was made up primarily
*  of doctors and lawyers, I opened this presentation with a walkthrough of the
*  current state of the art in medicine. After that, I gave a brief overview of what I consider to be
*  the most important concepts in AI, including what goes into these systems, how they learn,
*  and what we can say about what they really understand, their strengths and weaknesses
*  relative to humans on a practical level, how one might think about investing in this space,
*  though of course this is not investment advice, and most importantly, how these developments
*  might affect society at large. Before we dive in, I wanted to mention a few other things as well.
*  First, I am available for more speaking engagements along these lines. So if you have
*  a sophisticated audience that could use some help catching up on AI in general, or on a certain
*  focus area in particular, drop me a line and I'll see if I can help. With three little boys at home,
*  I will be far more able to accept remote invitations, but for the right audiences,
*  I am open to occasional travel as well. Second, in addition to my ongoing work at Waymark and as
*  an AI advisor to Athena, I recently got involved with a new AI advisory and implementation firm
*  called Stellis AI. This company aims to serve small and medium-sized businesses,
*  you can think 50 to 1,000 employees, with a mix of guidance and solutions that drive AI adoption,
*  efficiency and productivity gains, and ultimately business growth.
*  I love that we're really getting into the weeds with this work. One of our very first projects is
*  for a plumbing parts supply company that has decades worth of old part catalogs currently
*  sitting on a giant bookshelf and is really struggling to help people find what they need.
*  We're working on an AI solution to make this information far more accessible, and that could
*  create major new opportunities for them as a business. If you would like to explore being
*  an early customer of Stellis AI, please be in touch. Finally, I'm considering starting a very
*  niche cognitive revolution job board where past guests and other companies I believe in can post
*  their open positions. Right now, for example, Elicit is looking for seasoned software engineers
*  to join their team and help scale their systems. Athena will soon be ramping up a hiring process
*  for a number of AI and other technology roles, and Stellis will be hiring both AI engineers
*  and AI advisors, whose responsibility it will be to translate AI technology into practical
*  results for businesses. If you're interested in any of those roles, please contact me and I'll
*  help you get connected. I am super curious to see how many audience members are interested in such
*  opportunities, and obviously your response will help me determine whether or not this is a
*  worthwhile project. If you have any roles that you'd like to advertise, you can ping me about
*  that as well. As always, we appreciate it when folks share the show. This episode is more
*  accessible than most and could be a great starting point for any friends of yours who've been
*  sleeping on AI, so if you know someone who fits that description, please consider sharing this
*  episode with them. And of course, we invite your feedback. You can contact us anytime at our website,
*  cognitiverevolut.ai, and I do read all my DMs on all of the social networks. With that, I hope this
*  AI Scouting Report provides a solid foundation for understanding the exciting and at least somewhat
*  terrifying AI developments that are unfolding around us every single day. I'm excited and look
*  forward to sharing what I hope will be an interesting and super fast-paced journey through
*  the modern AI landscape. I call this the AI Scouting Report, the Not Investment Advice Edition.
*  I'm going to really not pull any punches in terms of being very in the weeds about some of the
*  important details of what is happening in AI now. We're going to start off with just a quick
*  rundown. Obviously, I can't cover anywhere close to everything, but a couple of key points,
*  specifically from the field of medicine, to describe the current state of the art when you
*  see SOTA in AI. That refers to state of the art. We'll talk a little bit about how that's already
*  impacting the economy, what the limitations are of the current systems. Then I'll get a little bit
*  theoretical for a bit and talk about the inputs to how AIs are made and some of the science that
*  actually goes into making them work as well as they do. Then toward the end, we'll get into
*  the true not investment advice section where I try to, and my crystal ball gets very foggy after
*  just a pretty short time into the future, but where I at least have a little bit of a sense for how
*  I'm thinking about investing and what companies are in the best position. I can close it with a
*  few key questions that I think will really be super important to watch as we try to get a sense
*  for where this whole AI thing is headed. I'm not going to use analogies. I often call my content
*  an analogy-free zone because I think that the AI phenomenon is something that is really worth
*  the time and effort to understand on its own terms. I think it is as important of a phenomenon
*  and as fundamental to understanding the world as understanding DNA and natural selection. To walk
*  around the world without those concepts just leaves so much unexplained and puts you in a
*  position of confusion. I think there are some core concepts in AI that are really becoming
*  similarly important. I don't use analogies to describe them. I'm going to try to describe them
*  in very literal terms. Simple as possible, but very literal without being wrong is what I try to do.
*  And then I won't do any big predictions, although I do have a few thoughts toward the end on
*  at least how I'm thinking about allocating capital. I guess I'll break my no predictions rule
*  just ever so slightly. Here is a little tap dance through the current state of the art,
*  specifically with a focus on medicine. Where are we in AI today? I think it's really important just
*  to try to keep tabs on that. It's a big part of what I do is try to have an up-to-date
*  sense of what our current AI systems capable of. It's really remarkable, but it is undeniably true
*  at this point that since the middle of 2022, the best AI systems have been better than the average
*  human at the average task. That is to say, if you go find some random task that might be typical of
*  white collar computer work, and you take a typical intern or young employee and ask the AI to do it
*  and ask the employee to do it, you're going to get better results from the AI. That's been true for
*  almost two years now. In addition to that, the best AI systems are really now closing in on expert
*  performance for routine tasks. And the word routine there is really important. Routine means
*  it's obviously common and that we know what good looks like. In medicine, you might think of something
*  the standard of care, something that is well established. So that's a really remarkable
*  phenomenon and it's happening super quick. GPT-2 was released in 2019. I read about that at the
*  hospital when I was there with my wife as she was about to deliver our son. And he's just turned five.
*  Five years later, we've gone through a series of different generations of the models. So now the
*  current one, GPT-4, is closing in on human expert performance on really demanding tests of cognitive
*  ability. This test, the MMLU test, is comprised of undergrad and graduate school exams across a super
*  wide range of topics. And the average GPT-4 score at this 86 compares to the human expert in their
*  domain. So it's coming close to matching what human experts can do in domain, but it's beating
*  the humans. If you were to have one human try to answer all the questions across all the domains,
*  then the GPT-4 result would be notably stronger. So that is pretty crazy and it's happened in a
*  pretty short period of time. Now, to get more specific in terms of how this is playing out in
*  medicine, here is a similar curve focused on a US medical licensing exam. To pass is somewhere in
*  the range of 60, low 60s. So the first system that pretty clearly passed the medical licensing exam
*  was Medpalm. That is one from Google. Not too long after that, really just a few months. Look at this
*  scale. December 2022 and March 2023, they came out with Medpalm 2 and it hit 86%. And again,
*  that is closing in on expert performance on the medical licensing exam. It goes further in medical
*  question answering. Here are nine different dimensions on which they evaluated. This is,
*  again, out of Google. They evaluated an AI and a human doctor head to head. And they asked human
*  doctors to evaluate both the AI and the human doctor participants. The top section here are
*  the good things, the things that you want to see in your answers to your medical questions. Things
*  like reflecting the consensus of the medical establishment, reading comprehension, knowledge
*  recall, better reasoning. The orange is how often the AI was judged to have done a better job. And
*  the blue is how often the human doctor was judged by other doctors to have done a better job. The
*  gray was in between is when it was considered to be a tie. So you can see that the AIs are dominating
*  on the good things. And then here are the bad things. This is the one of nine categories on
*  which the AI was judged to be worse. It did more of bringing up inaccurate or irrelevant information.
*  Not a ton more than the human, but a bit more. The humans did all the other bad things more than the
*  AI did. So we're again, getting into this strange zone where state of the art AIs are closing in
*  on the performance of experts, even in cognitively demanding areas like medicine.
*  Here's another study. Again, this is medicine. This is differential diagnosis. On the left is
*  the AI. On the right is the human. There are four bars here that refer to whether they had the exact
*  match on the proper diagnosis or some increasingly permissive definition of accuracy. And then the
*  top K is how many guesses they got before they got to the right one. So again, you see the AI is at a
*  significantly higher accuracy percentage across the board as compared to the human doctor. These
*  are primary care physicians specifically in this study. So I tell people in all seriousness these
*  days that if I had a medical condition that genuinely worried me, I would not be without my
*  AI doctor. I would also of course want to have a human doctor. I wouldn't put all my trust into
*  the AI, but I would absolutely be cross-referencing their answers and checking them against one another
*  to try to get the best of both worlds. But I would not be without my AI doctor with a serious medical
*  condition in today's world. A lot of other interesting applications just in medicine as well.
*  This is a project on virtual tissue staining. I don't know a lot about the traditional way that
*  this is done, but biopsy and slicing tissue and staining it and looking at it under a microscope,
*  I'm told that this can take hours and that it's too slow to be done while the patient is in surgery.
*  Now there's a new technique that includes this in situ imaging and then they add this virtual stain
*  to it and now they can get these sorts of images out of patients in just seconds while they're
*  still in the operating room. So if you're doing some sort of procedure to try to remove a tumor,
*  you can get a lot of these images in real time as you're going and that of course can lead to
*  better patient outcomes. So the creativity that people are bringing to all these different
*  applications of AI is super, super interesting. Here's one that flies under the radar and always
*  blows my mind. This is literal mind reading. I have a full episode actually two on this project,
*  but what they've done here is taken fMRI scan data and taught an AI to reconstruct the image
*  that the patient was looking at when the scan was captured. So you're in an fMRI, you're shown
*  these images, they captured the data and they record what you were looking at the time and then
*  you do a bunch of that and then after that the AI can take the brain data, the fMRI data, and
*  reconstruct the image that you see here on the right where the original one was the one on the
*  left. So you can literally decode brain activity and reconstruct images with this level of fidelity
*  and I often think, man, I feel like when I was a kid this would have been major news.
*  And somehow today we live in a world where it just crosses over and gets a few retweets or
*  whatever, but most people don't even realize that this kind of thing is out there. So literal mind
*  reading is happening and with this original one it took 30 to 40 hours of scan data to train the AI
*  to decode one person's brain. With the latest update, they're now down to one hour of scan
*  data required. So it is actually starting to get feasible where you could put somebody into the
*  thing for an hour and get this type of process up and running without it being a huge undertaking.
*  So obviously we do a lot of things. I think one thing that's important to keep in mind,
*  and I'll get into a little bit more detail in just a second, comparing what the AIs are best at and
*  what the humans are best at, but they can't do everything of course. So this is a study of
*  what they can do and how that breaks down by different kinds of jobs. Interestingly,
*  and this is definitely a surprise and I think this has become common knowledge at this point,
*  the AIs that we're getting are not really the AIs that we expected. We expected that they would
*  automate relatively low wage and low status labor first, but on the contrary they seem to be impacting
*  high wage and high status labor first. Your proverbial plumber or custodian of a building
*  is not feeling much impact yet from the current wave of AI, but your doctors and lawyers are
*  definitely seeing significant impact. So this study broke jobs down into five different categories.
*  The green here is the lowest, let's say, status, wages and lowest impact. As you go out,
*  it's the fourth quintile that's the highest one out. So the most impacted are the fourth
*  quintile and then the fifth quintile comes in a little bit again. And to read this, you can
*  basically think of all the area under the curve is amount of work that AIs seem to be poised to
*  be able to do. Everything outside of the curve they would not be able to do. So if you're, again,
*  a plumber or custodian, there's a relatively small amount of your overall work that is likely to be
*  impacted by the current wave of AIs, whereas if you're a doctor or lawyer or maybe out here
*  somewhere, this is to say about half of people have about half of their tasks such that AI
*  could impact them, plausibly do a significant part of them. I think that's really something
*  that we are going to be adjusting to for quite some time. And again, we're just getting started
*  in this AI era. Here's one thing that was really just announced and is coming to market right now.
*  This is AI nursing. This company, Hippocratic AI, has a pretty interesting go-to-market proposition
*  where they are charging by the hour for their AI system. So you're starting to see AIs that
*  are actually competing in essentially a labor market, not by API calls, not by number of tokens
*  generated, but literally by the hour that they're working for you and doing stuff.
*  Of course, they're scalable and clonable in the way that software systems are,
*  but they're actually starting to charge an hourly rate. They charge $9 for their AI nurses.
*  And this company specifically is trying to be very cautious, very safety-focused, even though
*  you saw the result above on the relative strength of AI systems on diagnosis. This company is taking
*  a strong... We're not trying to even get into diagnosis, but we do think that we can get AI
*  to do a very reliable job on a lot of these follow-up tasks that either nurses do or that,
*  frankly, today, nobody does because there's just no time in the day to do them. So they have all
*  sorts of things where they'll call you and work through your pre-op thing or follow up on your
*  discharge instructions or make sure you're taking your medicine or checking on how you're feeling,
*  all that kind of stuff. And $9 an hour is the going rate for an AI nurse in today's world.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  AI might be the most important new computer technology ever. It's storming every industry,
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of control?
*  It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing, and of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive of OCI at oracle.com
*  slash cognitive. That's oracle.com slash cognitive. Oracle.com slash cognitive.
*  The Brave Search API brings affordable developer access to the Brave Search index,
*  an independent index of the web with over 20 billion web pages.
*  So what makes the Brave Search index stand out? One, it's entirely independent and built from
*  scratch. That means no big tech biases or extortionate prices. Two, it's built on real
*  page visits from actual humans, collected anonymously of course, which filters out tons of junk data.
*  And three, the index is refreshed with tens of millions of pages daily, so it always has
*  accurate up-to-date information. The Brave Search API can be used to assemble a data set to train
*  your AI models and help with retrieval augmentation at the time of inference,
*  all while remaining affordable with developer-first pricing. Integrating the Brave Search API into
*  your workflow translates to more ethical data sourcing and more human representative data sets.
*  Try the Brave Search API for free for up to 2,000 queries per month at brave.com slash API.
*  Okay, so where does it stop? This is where we get to limitations.
*  Where it stops is things that are not routine. So can AI do new science? In general, the answer
*  today is no. There are a few very engineered and purpose-built systems like your Alpha Folds that
*  I'm sure people have heard of that are specifically designed and highly tailored to do a narrow task
*  in science, and those are high-impact systems as well. But the general purpose systems,
*  you're like chat GPT-like things that you can talk to and just have do whatever you want.
*  Those things today cannot do new science, and that basically extends to general, novel,
*  unfamiliar, somebody really has to figure something out for the first time situations
*  across the board. They are not good at those. I used to say actually no eureka moments. That
*  was one of my summary bottom lines for the state of AI. Now I have to say precious few eureka moments
*  because this is actually one instance where GPT-4 was doing a better job on some pretty novel stuff
*  compared to even human experts. I'll just try to play this video. And the scenario here is
*  they're trying to train a robot hand to do various tasks. The task in this case is twirling a pencil,
*  and they use a technique called reinforcement learning. So this gets a little meta because
*  it's AI training other AIs. But to do these sorts of reinforcement learning programs, you have to
*  have what's called a reward function. When the AI is just beginning, just starting to learn what's what,
*  it doesn't do very well. And so it needs some score to learn like, when am I doing better? When
*  am I doing worse? I can do more of the stuff that's getting me the high score and gradually
*  find my way to figuring out how to do the task. So the reward function, you could imagine sitting
*  down and trying to come up with, okay, if I'm looking at this, how would I score it so that I
*  could give the AI a signal from which to learn how to get better at this task? And you might think,
*  okay, maybe I could measure the angular momentum of the pencil and turn that into a score somehow,
*  something along those lines. There are people that do this, right? This is an expert task to write
*  reward functions for robot reinforcement learning. Turns out that GPT-4 is significantly better
*  at writing these reward functions for robot reinforcement learning, even then the people
*  who did it. And this is not like you're a person on the street sort of task, right? You often just,
*  again, step back and think, you go talk to somebody on the street and say, hey, could you write me a
*  reward function for this robotics reinforcement learning project that I have? They will not even
*  parse that sentence, let alone give you a serviceable reward function. So you're by definition
*  in expert territory here, and yet GPT-4 still able to significantly outperform the human reward
*  function writers. That doesn't happen very often. This is the exception, not the rule, but I have had
*  to update my summary position from no eureka moments to precious few eureka moments because
*  of a number of little projects like this. Here's one other one that kind of, I'm still wrapping
*  my head around. This is a example of essentially a chat GPT-like model trained on just tons of
*  DNA sequences, 300 billion base pairs worth of DNA sequences, all drawn from bacteria and phage DNA
*  data. And what they find is that now they can use this thing to generate new stuff. So they've found
*  that they are able to generate a variety of CRISPR like complexes. These are all complexes generated
*  by the DNA generating AI. And the other thing that they can do that's really interesting is they can
*  start to perturb the AI and see how confused it gets and use that to determine how essential
*  different genes are to the survival of the cell. They call this in silico gene essentiality
*  experiments. And apparently this is, again, quite a cumbersome process to do if you're doing it in
*  an actual traditional lab context. But now they can run it in just like a couple seconds
*  because they can obviously do it in the computer. And this is just from the last few weeks. So this
*  is really some of the latest and greatest. And I think we're, again, just beginning to see the impact
*  of all these advances across a wide range of fields. So hopefully that has you motivated to
*  understand a little bit better how it all works under the hood. The core inputs to AI systems are
*  data, compute, and algorithms. That's like your Trinity, your three-legged stool. Without any of
*  these three, it's not going to work. You need data from which to learn. You need compute to crunch
*  the numbers. And you need an algorithm that actually translates that data and that number
*  crunching into something that actually works. So I'll take you through each of the three.
*  For starters, all these systems are really just information processing systems. You might call
*  them circuits. They are inspired by human neuroanatomy, but they're definitely not
*  much like human neuroanatomy. One thing that they all have in common is that they are all
*  unidirectional. They are all differentiable, which means there's no cyclicality. In the human brain,
*  you have different parts regulating one another and a lot of crosstalk. In the AI systems that we
*  have today, they proceed very linearly from one layer to the next. So this is just an example of
*  a really simple thing where you might have a number and your goal is to classify this image as what
*  number is this image. This one is obviously a seven. You can break this up into pixels. You can
*  feed raw pixel data in here and it progresses through the layers. And then your goal is to get
*  a seven to be the one that lights up. And if that happens and it's working effectively, then you have
*  an AI now that can identify which number it is. So that's a very simple system. I strongly recommend,
*  if you want to go see great visualizations of this, the YouTube channel ThreeBlueOneBrown does
*  some of the best visualizations, not just on this, but on all sorts of different mathematical things.
*  But this short clip is drawn from a longer series that is really good for building intuition if you
*  want to go check something like that out. Okay. So there are these information circuits, but let's
*  get a little deeper now on how do you actually get it to learn? A super important concept sitting
*  at the heart of this is the loss function. The loss function is the way that you score
*  the output from the AI. So let's imagine you are at the beginning of a training process.
*  And by the way, they usually just randomly assign the numbers at the beginning. There are some
*  tricks, but traditionally the numbers in all these different positions are just randomly assigned.
*  So what happens at first is basically garbage in, garbage out. You have your kind of matrices that
*  are crunching all these numbers. It starts in a very random position. Let's say you go ahead and
*  put a two in, you crunch all the way through the thing and you get this kind of result out.
*  And it gave a high rating to a three and also a high rating to a six, very strangely, and a high
*  rating to a one and the actual two was a very low rating. Okay. That's a bad prediction from the
*  ads. It's not able to do the task at this point, but you can score it. So you can say, Hey, your
*  score on two should have been higher and everything else should have been lower. And now you have a
*  score. You can put that into a single number and you can say, this is your score. And then you can
*  do what is called back propagation, which is saying, if I go back through all the different
*  parts of this system, all the different numbers in the matrix, and I look at each one and I ask,
*  if I tweaked this one, should I tweak it up or should I tweak it down to make the overall score
*  a bit better or a bit worse? This is ultimately chain rule from calculus for each number in the
*  thing. And if you're talking about a GPT three scale system with famously 175 billion parameters,
*  then you're doing this literally 175 billion times in these small systems. It can happen very
*  quickly, but it does take a lot of number crunching as the systems get big. But for
*  literally every single parameter in the system, you're just saying, okay, I can either move this
*  up a little bit or down a little bit. And I want to just do that in such a way that makes the final
*  score a bit better. It's a really simple concept. Actually, you have a loss function, which gives
*  you a score, you use back propagation to work your way using the chain rule of calculus from the end
*  all the way back to the beginning of the network, tweaking every single little parameter along the
*  way. And then you do that in a loop. And that loop is called gradient descent. So I'm sure you've
*  heard some of these terms flying around. Gradient descent is the process of just through all these
*  little incremental changes, gradually finding your way to something that works. So this is a
*  visualization of what's called a loss landscape, which is like at any given point in the vast space
*  of all the possibilities for the numbers in this information processing network, you're going to
*  have some loss value. And as you work your way down to the lowest possible loss, that is the
*  process of gradient descent. And this gets complicated. You've got all sorts of different
*  strategies for how to find your way down the hill. And you can imagine people have been working on
*  this for a long time. So there's lots of different little complications to it. But this is basically
*  the core thing. You have to have something that is differentiable so that you can do this back
*  propagation. You have to have a score so that you have the loss function. And if you have those and
*  you run this in a loop, you are doing gradient descent and you are on your way to training in AI.
*  What you'll typically see are these loss curves where as you go step by step, the loss gets better
*  and better. You're finding your way to the best possible solution. Traditionally, this was done
*  with curated data sets. So this is like a classic data set, a data set of just nothing but small
*  images of hand drawn numbers. I think it's called MNIST, but that's all it is, right? Small images
*  of hand drawn numbers. And there are some that you're meant to train on. And then there are some
*  that are meant to test how well you did from the learning process. And typically what people
*  would notice is that the more you would train, your training loss would go down. You would continue
*  to see better and better scores. But then when you actually tried it on the test set, or also
*  sometimes that's known as the validation set, you would see that at some point the validation
*  results would get worse. And this was typically considered to be the point at which the model is
*  overfitting. That's another term that you'll potentially hear if you spend more time in this
*  area. When it's overfitting, it is learning now idiosyncrasies of the data set that don't actually
*  mean anything for the general case. So essentially you can imagine memorizing a bunch of strange
*  weird cases and getting really good on the test, but this is teaching to the test. Now you go and
*  show other handwritten numbers, it's actually getting worse because it's learning the wrong stuff.
*  So past this line where the validation gets worse, that is known as overfitting.
*  Here's where the paradigm has changed. That was the traditional thing. You'd have a data set,
*  the data set was finite, you train on a certain amount, and then you test on a different amount,
*  and the game was like, who can come up with the best algorithms, the best architectures
*  to get the highest validation score? That was the pinnacle of the field. Now things have changed
*  very significantly and the big unlock has been figuring out clever loss functions that allow you
*  to tap into huge amounts of unstructured data. There's only so much labeled data in the world.
*  The key thing about these data sets is that, again, you know what the number is. The data
*  set includes the image, but it also has the label, so you can check your answers against the actual
*  answer key. But what they've done now with what's called unsupervised learning is they've come up
*  with clever formulations to allow the world's web scale data to serve as training data. And there's
*  two big things that have been really popular recently. One is called next word or next token
*  prediction, and the other is image denoising. So in next word prediction, and this is how we're
*  now getting to chat GPT and that sort of model, the whole body of all human text becomes available
*  because your job is now just predict the next word. So you take all of the all possible text,
*  you cast that into a vocabulary. There are like 50,000, sometimes 100,000 possible outputs in
*  these text generation systems, and you do something very similar to what we showed here, except
*  instead of 10 numbers to choose from, there's now 50,000 possible next tokens that you could
*  output, and you get a very similar score and you can do backpropagation. But the key is that the
*  text itself provides the answer. So now you can just crunch all available text, and for every
*  single bit of text, you have the opportunity to score yourself with a loss function and to do that
*  backpropagation. So this is how the data sets have become huge. A similar thing has happened with
*  images where somebody came up with a very clever idea of what if we first added a bunch of noise
*  to existing images? What if we degraded the images purposefully with noise, and then we train an AI
*  to denoise the image? That would allow us to use all of the images that are out there for training
*  data. So this is, I can't overstate the importance of this paradigm shift from small curated labeled
*  data sets to web scale, unlabeled, but self-documenting data sets that is known as
*  unsupervised learning. And this is how all the main scale systems in today's world are trained.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable
*  and do more with less, especially with engineering. Listen, I love your 30 year old ex-fang senior
*  software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale,
*  from sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high level
*  for over five years to help you access global engineering without the headache. SQUAD, Sean's
*  new company, takes care of sourcing, legal compliance, and local HR for global talent so
*  you don't have to. With teams across Asia and South America, we can cover you no matter which
*  time zone you operate in. Their engineers follow your process and use your tools. They work with
*  React, Next.js, or your favorite front end frameworks. And on the back end, they're experts at
*  Node, Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week, but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted
*  top 1% talent and actually working hard for you every day. Increase your velocity without
*  amping up burn. Head to choose squad.com and mention Turpentine to skip the wait list.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omniki
*  so much that I invested in it, and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Okay. So that was all data, right? Where's the data coming from? What is the nature of the data?
*  How are we using the data? You also need compute. Of course, there's been massive amounts of
*  investment in computing infrastructure. NVIDIA's stock price has gone up tremendously because they
*  are the leading company that is providing the GPUs that are doing all the compute. The key thing
*  about GPUs as opposed to CPUs that you need to know is just that they allow for massive
*  parallelization of the calculation. You can imagine that if you're going to ask a question
*  about 175 billion numbers, do I tweak it up or down? You don't want to have to do that sequentially
*  because it'll take a really long time, even if you have a really fast computer. So you need to come
*  up with some way to ask that in parallel for as many of those different numbers as you can,
*  and then batch the results together and then make the updates. So that's part of where the
*  algorithm progress comes in. And that takes you to the transformer. Transformer is the number one
*  pretty much dominant approach to AI today in the world. I'm trying to not use too many advanced
*  vocabulary terms because I know that people get lost in the jargon. So here's a quick glossary
*  of terms. The transformer is just a type of information processing circuit. The tokens
*  is another word for the words, or it could be like a little part of an image.
*  When you embed something, that is the process of converting that text or image input to numbers.
*  The neurons are the nodes in the network. They're generally organized into layers. As I said earlier,
*  everything has to be sequential. You can't have loops in there. Sometimes these are also called
*  activations or the values at the particular neuron places are called activations.
*  There are three different parts of the transformer that are important. The attention mechanism is the
*  one that gets all the attention because it was one of the big breakthroughs. The MLP is the
*  multi-layer perceptron. And then you have these things called non-linearities. Typically each
*  layer will have all three of these. Then you finally get to the parameters and weights. These
*  are the numbers that are actually in the thing sitting there that were trained, that were learned,
*  that are going to do the number crunching. You'll also hear words like logits. These are the final
*  numbers that get output before they're finally converted back into actual text. The forward pass
*  is the process of actually running the thing once. And the model is the thing that is actually run.
*  I'd just like to go through these real quick because there's so much jargon and it's very
*  easy to get lost in all the jargon. I mentioned that the transition to unsupervised learning and
*  the massive amount of data that comes available when you switch to that paradigm has been super
*  important. So let's talk about scaling and then a couple of really interesting observations as
*  people have started to scale up these systems. They're getting really big. There has been a
*  whole study of what are known as scaling laws, which is to say, how good are these things going
*  to get if we put a certain amount of resources into them? And what you'll notice across the board
*  in these sorts of system designs is that there's always a Pareto curve. There's always some optimum
*  point where you can make the model bigger in terms of parameters, but then it takes more compute to
*  do each process. So for a given compute budget, then you can't process as much text. If you make
*  it smaller, then you can do more loops, but the smaller models don't tend to learn as fast. So
*  there's always this optimum point where you're choosing the right balance between how big you
*  want the model to be and how much data you're going to run through it in the training process
*  for a given budget. So each of these different colors represents a given compute budget.
*  We're here at six times 10 to the 18. That's big, but it's still eight orders of magnitude below
*  the White House threshold for reporting large training runs, which they set at 10 to the 26
*  flops. A flop is a floating point operation. It's literally just a small unit of compute.
*  You're actually doing a thing with a number. You're doing that 10 to the 26 times to trigger
*  the White House reporting requirements. And here they're going from like eight to five orders of
*  magnitude less than that. But what's key about this is these small studies have allowed them to
*  then draw these lines, which allows them to project out into the future as they're really scaling these
*  systems. How good do we think they're going to get? We can predict the loss based on this scaling
*  law for a given compute budget. And this is how people are starting to back into these things like,
*  okay, we should have this many billion parameters and we should have this many
*  tokens that we want to run through it. And it's going to cost us this much money.
*  So how big is this getting today? The big systems, GPT-4 was trained on 10 trillion
*  tokens. That's essentially 10 trillion words. And it cost reportedly some tens of millions of dollars
*  just to run the compute. That does not include like the salaries of the researchers or collecting
*  all the data, but literally just to run the servers to do the work. GPT-5, allegedly in training or
*  getting close to the end of training is expected to be trained on 10 times more than that,
*  100 trillion tokens and is expected to cost a few billion in compute. So that's pretty crazy.
*  It is bringing also some crazy results. So one of the things that is most remarkable to me about
*  these systems is that they seem to learn things that they were not explicitly told to learn.
*  The first sign of emergence, this is a story from the OpenAI team from back in 2000. So this is way
*  smaller. They didn't have all the compute, all the resources they have now, but they trained a model
*  just to predict the next character in Amazon reviews. And then as they were looking inside,
*  and looking at the activations, which parts, which nodes in the architecture had high values
*  and under what situations did those positions have high values? What they found is that there was one
*  little neuron that was lighting up strong if it was a positive review and was like very strongly
*  negative if it was a negative review. And people have been trying to do sentiment classification
*  for a long time. This is like a pretty well established thing. And people had all sorts of
*  techniques. What they were amazed to see is that this system, which they had only trained with a
*  loss function of predicting the next token, internally had this neuron that if it was on its
*  own, a sentiment classifier would have been the state of the art sentiment classifier at the time.
*  So this is like a really profound observation because it's like, wait a second, we just trained
*  this thing to predict the next token and yet internally without us ever giving it any signal
*  or information about the sentiment, even the concept of sentiment, it knows nothing about that.
*  Or at least we didn't tell it to know anything about that. Somehow it has come to represent sentiment
*  as a means to do what it is ultimately doing, which is predicting the next token. So somehow
*  representing or understanding what the sentiment is helps you predict the next token, which
*  that intuitively makes sense that it could help. But what's remarkable is that it is learning that.
*  So as Greg Brockman, the president of OpenAI put it, semantics emerged from a syntactic process,
*  even though it was only trained to predict the next token, it learned a higher order human
*  recognizable concept, which is sentiment. That is really the sort of breakthrough that is at the
*  heart of the advances now that we're seeing that make these systems so general and powerful.
*  There's been a lot of other study. I'll go quickly over this because I don't have a ton of time for
*  it, but similar phenomena have been observed when you train a model to play a game and you maybe
*  just train it to predict the next move. And all it gets to see is a sequence of moves like this,
*  like F4, this is a fellow, F4, F3, D2, F5, that's all it ever sees. And yet they can look inside the
*  model and begin to decode that it is actually representing a two dimensional board state
*  and updating that board state with each move as pieces get captured and territory switches hands.
*  So all it ever saw was this, but it learns to develop its own conception that looks more like
*  this. This is also happening in image understanding of computer vision models, where you have these
*  different neurons that seem to respond to a particular concept. And then people figured out
*  how to reverse engineer what would be an image that would maximize that and what would that look
*  like. And you'd see these sort of trippy things where it's okay, that's a window and that's a
*  something and that's a wheel. And that's what maximizes these neurons. And then as they feed
*  forward to the next layer, these sort of window and car body and wheel detectors all send a strong
*  signal to what appears to be a car detector. And this is the image that would maximize the
*  response from the car detector neuron. Now, there was no engineering to say this should be the car
*  detector neuron. All of this is an emergent process that just results from this definition
*  of a loss function, the process of gradient descent, and the massive scale at which these
*  things are now operating. These models are learning these high order human recognizable
*  semantic concepts from this purely syntactic process. That is something that I think way more
*  people should understand. And if there's one takeaway that I would want you to leave from
*  today with, it would be that. Okay, so this is really another kind of profound example of it.
*  Here's a task called modular addition. You may remember this from your MCAT studying days or
*  whatever. The idea here is to take two numbers, add them together, then modulo divide by a third
*  number and take the remainder. So five plus 12, modulo 12, it's 12 divided by 12, remainder is zero.
*  17 plus eight is 25, divide by 10 is two, remainder is five. So they train a model to do that.
*  It learns to do the task. But right in here is the process where you would traditionally call
*  overfitting because it learns some, but then the validation performance falls off. The test
*  performance continues to get better and eventually memorizes the whole training set, but the
*  validation is bad. So for the longest time, people have just said, this is useless. You've just trained
*  a model and memorized things, but it didn't actually learn the real task. And so they would
*  have stopped long before you notice this is a log scale, right? So this happens at like hundreds of
*  optimization steps. Finally, somebody said, what if we just run this a really long time? What if we
*  give it like 10,000 optimization steps? What they find is they get out toward a million optimization
*  steps is that it actually jizes and learns a real solution. They call this grokking generalization
*  beyond overfitting. So it's overfitting here. Traditionally, people would have stopped here
*  because, okay, the validation loss never gets better once it starts to get worse,
*  except that it actually does. It just takes a lot longer for it to finally learn to do this task.
*  And now at the end of this, it can actually do modular addition, even on examples that it hasn't
*  seen. It learns the examples that it sees in the training early, but it takes a long time for it to
*  grok the general concept of modular addition and do it for unseen examples. But that's really
*  profound, right? That it's able to make this shift from memorizing the examples to learning an
*  underlying algorithm. The algorithm that it learns is like quite weird. I'll show that in just a
*  second. But this is a really key point that we don't know in the process of training these things
*  when something will be grokked, when the model will go from just predicting whatever next token
*  might seem plausible to actually figuring out the underlying concepts and being able to use them
*  across the board. So for my money in the GPT-4 technical report, which is the paper that they
*  put out, this is the most important sentence. Certain capabilities remain hard to predict.
*  We showed the scaling loss that show how they can predict what the loss is going to be. That is the
*  aggregate score. But what's really still a mystery is how does that aggregate score
*  translate to particular behaviors, to particular abilities, to which kinds of problems it's going
*  to be able to solve and which kinds of problems it's not going to be able to solve. And here you
*  see one where as they got models bigger and bigger, this was from a paper called the inverse scaling.
*  There's actually a contest to find, are there certain tasks where as things get bigger and
*  bigger, the performance gets worse? And they found some of these tasks. One was called the hindsight
*  neglect problem. I won't bore you with the details, but basically across several generations, the
*  models got worse at this task with increasing scale. And then with the next generation,
*  it seems to have grok'd that concept. And now it's perfect from being bad to worse to good
*  in a surprising way. So capabilities remain hard to predict. We know that we can scale things up.
*  We know that the loss will get predictably better, but we don't know for any given task
*  when this process of generalization will kick in. It's a surprise for all of the different tasks
*  that we might be interested in. So this is a really profound challenge in terms of understanding
*  what these systems are doing and also how to control them. Okay. So I said that they're human
*  level. They're definitely not human-like. Here's just a quick, I won't even go into the details of
*  this, but somebody went in and reverse engineered. How is it learning to do modular addition? And it
*  turns out it's doing it in a very weird way. It's like learning sine and cosine functions,
*  and it's essentially rotating around the circle. No human would really do this way. It involves
*  Fourier transform math. So it's a very alien process, but it does add up to a reliable algorithm.
*  And now that this has been reverse engineered, you can actually see how it is doing it.
*  You don't have to like it. I think you should probably be a little bit scared of the fact that
*  it's learning such alien solutions to these problems. But nevertheless, this is what it does
*  for this particular thing. So I really emphasize how while they are very human-like in their
*  abilities in some ways, they are also not at all human-like in their underlying mechanism. And we
*  should not think of them as human-like where it really counts. Okay. So here's the tale of the
*  tape. This is important. What are AIs good at? What are humans good at? AIs are much better at
*  breadth. They've read all the information on the internet. They can speak all the languages. Even
*  human experts don't have anywhere the breadth of a modern AI. But the human experts do still have
*  better depth, especially in their area of expertise. Breakthrough insight is humanity's biggest edge
*  right now. As I said earlier, few eureka moments, precious few eureka moments. The AIs are a lot
*  faster and they are a lot cheaper. Typically, I would tell people that you can expect they'll
*  be like at least 10 times faster and usually 90% cheaper if they can do what you need them to do.
*  They're also like super parallelizable, super clonable. They're ready whenever you are.
*  You can pick up where you left off 24-7. So they have lots of availability advantages.
*  Memory is something that I've really come to appreciate in myself. My memory is certainly
*  not perfect, but it does give me a coherent sense of who I am, what I'm trying to do.
*  And the AIs don't have that in the same way. They have a very limited and brittle memory as it stands
*  today. They do have great technology diffusion speed. A paper that I think should give everyone
*  a little pause is natural selection favors AIs over humans. The key thing there is that when an
*  advance is made, it can often be ported to all the different architectures, all the different
*  models very quickly. Whereas we struggle to learn new things, especially as we get a little older.
*  Bedside manner is another one too that AIs are actually beating humans on in evaluations,
*  but they're really not good at adversarial robustness, meaning they're quite easy to
*  trick. You can confuse them. You can trick them. This is sometimes known as jailbreaking. If you
*  go on AI Twitter, you'll see lots of examples of people getting the AIs to make fools of themselves
*  in ways that humans would never do. This is one of their main weaknesses is that they're quite
*  brittle and not really robust to being tricked. Okay. I know I'm going super long. I'm skipping
*  over best practices for business. And you might be able to check that out on my podcast feed,
*  if you're interested in that. But just to cash this out a little bit to some investment advice,
*  or I should say not investment advice. The question that a friend of mine poses is,
*  are we approaching a big tech singularity? The way that he defines that is a moment at which
*  the big tech companies have such advantage because of their dominance in the core inputs to AI.
*  Those are, again, data, compute, and algorithms. Are we reaching a point where they might be able
*  to enter into all sorts of different industries and dominate those new industries because of
*  their core strength in AI and in the inputs to AI? And I would say that's looking increasingly
*  plausible. And certainly the stock prices of the big tech companies would seem to reflect that.
*  This is a chart of how much compute different companies in the world have. This is Google,
*  Microsoft, Amazon, Metta across the top. Apple comes in at number five. Alibaba is the top
*  entrance out of China. And then things get relatively small. And this is Oracle down here,
*  by the way, which is a multi-hundred billion dollar company. But these are the dominant
*  players in compute. The big four in compute today, Google, Microsoft, Amazon, Metta.
*  Nobody else is on their level. And there's really no path for any company that's not already on this
*  list to get into the compute game at anything approaching similar scale to what the big guys
*  already have. If you're prepared and able to spend billions to train a single AI model,
*  it's going to be very hard for anyone to enter into that market and rival you.
*  So I don't pick stocks. I genuinely don't pick stocks, but I do have a little investment club
*  with some friends of mine. And I've literally made one individual stock recommendation to the group
*  all of history. And that was Nvidia about two years ago, because I could just see where this
*  was going, where everybody's saying, man, look at these scaling laws, right? To compete, we're going
*  to need to hit this compute budget at this given time. We're going to need to collect this amount
*  of data. Of course, we're going to have to do a lot of research on the algorithms too, but
*  you're not... The algorithms right now are like incremental improvements. Nobody has recently come
*  up with an algorithm that just blows everything out of the water. You got to have all three elements.
*  You got to have the data. You got to have the compute and you got to have the algorithms.
*  And so everybody's buying compute from the same place. That's Nvidia. I think all the chip makers
*  are probably going to be doing pretty well. People are interested. Nvidia is making insane
*  margins. So people are very interested in like AMD and Intel as well. And obviously the government
*  is getting involved and saying, hey, maybe it's not such a good thing that this is all getting
*  manufactured in Taiwan. Maybe we should bring some of it back to the United States. But I would say
*  probably the safest bet in the space is the fundamental compute providers, both at the
*  layer of manufacturing the chips and then also at the big tech layer, because they have all three.
*  They have the data, the compute and the AI researchers that are constantly working on
*  new algorithms. This is my list of like live players. That is to say, who are the companies
*  that really have a chance at shaping the future? And these are pretty familiar names at this point.
*  OpenAI is the leader. Google still has the deepest bench in terms of the most researchers,
*  the broadest research agenda. Anthropic is a real dark horse. They're not very big,
*  but they're partnered with both Amazon and Google. And there are a bunch of people that left OpenAI
*  to found this new company. Meta is certainly a big one. They're putting out a big open source
*  model you'll hear a lot about called Llama 3 right now and over the next few weeks.
*  Microsoft is not quite as cutting edge in terms of research, but they've got it where it counts
*  in terms of data centers and they're partnered with OpenAI. Never count out Elon. I think Tesla
*  and X will be interesting. A dark horse that is not a public company, you can't invest in it,
*  but definitely one to watch is called Character AI. They basically make AI girlfriends and people
*  are spending a lot of time talking to their AI girlfriends. So that's a whole other dimension
*  of sort of societal impact. What's going to happen to the birth rate is I think a very
*  interesting long-term question. Mistral is the European champion. They're based in France.
*  I would say they probably wouldn't have a chance at really competing except for the fact that the
*  European Union may say, you know what, here's a few billion dollars because we want to have one
*  of these leaders on our soil. And the geopolitics of this are going to be very interesting to watch.
*  Obviously, what's going on in China is a big deal as well. They're not at the same level as
*  the United States, but they're not too far behind. If you were to go to the big AI conference in New
*  Orleans called NeurIPS a few months ago, I didn't personally attend, but I was told you heard a lot
*  of Mandarin conversations on the floor. There are tons of talented Chinese researchers. A lot of
*  them are here in the US, but also obviously a lot are in China. The chip ban though may be a big
*  deal for them because they don't have their own domestic chip industry. And if they can't import
*  the chips, they may have a hard time reaching those next levels of scale. Apple hopefully is
*  going to make Siri good at some point, but I would say they're currently behind. But you can't count
*  them out too much because they are, you look here on the list, they are the number five on compute.
*  And certainly they have more money than anybody could possibly know what to do with. And that
*  can pay a lot of researchers. So, all right, I'm going to land the plane here in the next two
*  minutes and then I'll be happy to take a few questions. So are we all going to die is obviously
*  a question that people are asking. I think that really depends on what happens next in terms of
*  how much things scale and whether the scaling laws hold. They're called scaling laws, but they're not
*  fundamental laws of nature that we, at least it doesn't, we don't have that level of justification
*  for them. They would be better maybe described as scaling trends. And so the trend could break.
*  So are we going to see something where the sort of capabilities level off at a human expert level,
*  or do they just blow past human expert? I think that's probably the single biggest question.
*  It's hotly debated. There's not really a clear answer there. My guess is that we're going to
*  get something ailing in that'll be superhuman in some ways, but it'll still be weird and weak in
*  other ways. And how that plays out was ultimately going to be weird and very hard to predict.
*  One thing that I do think is strange though, is that we're racing into this without a real plan.
*  Nobody really has a sense for how these systems are going to be controlled. If they do become
*  superhumanly powerful, even the leading developers are specifically saying that it could lead to
*  human extinction. Sam Altman, the CEO of OpenAI has said the worst case scenario is lights out
*  for all of us. So it's bizarre that they're chasing this goal with seemingly as much speed
*  as they can muster while they don't really have a plan to make sure that things don't go totally
*  awry. The best I can say is at least they know that they're playing with fire. This is a survey
*  of AI researchers that just goes to show how much radical uncertainty there is in the field.
*  48% of the respondents, these are people that had published in top journals in AI in the last few
*  years, 48% of them gave at least a 10% chance of human extinction from AI. So half gave a 10% chance.
*  For my money, that is very much worth taking seriously. Tons of, this is another thing,
*  mitigating the risk of human extinction. This was signed by all the leaders, Sam Altman,
*  the CEO of OpenAI, the CEO of Anthropic, Bill Gates is on there, the chief scientist from OpenAI,
*  the chief scientist from Google DeepMind, the CEO of Google DeepMind. These two are Turing Award
*  winners, which is basically like the Nobel Prize in computer science. So it's really a who's who
*  of people signing on to the idea that mitigating the risk of extinction from AI should be a global
*  priority. There's just really radical uncertainty and all bets are really off, I think, for how the
*  future is going to shape up. How fast is this going to happen? It's not that long of a time.
*  The average, there's a couple different ways you can ask the question, but the average among
*  forecasters is maybe in the next few years, maybe it's closer to eight to 10 years, who knows? But
*  that's the range in which the field is expecting these breakthroughs. Of course, it may never happen,
*  but the consensus view is like a few to a handful of years from now. And so what will we be watching
*  to figure out where we're going from here? Will this raw scaling continue to work? Will the scaling
*  laws hold all the way to superhuman systems? That is very hotly debated. Will a new architecture
*  come along and be even better than the transformer? Recent results suggest that yes, actually there
*  will even be better architectures than the one that has taken us this far. Will mechanistic
*  interpretability catch up? That's like the reverse engineering and figuring out what's actually going
*  on inside. That was one thing that the survey of the 2000 AI researchers did ask. And the consensus
*  was no, that we're not close enough to being able to understand what's going on inside to be able
*  to count on that to save us, even though great progress is being made. What new modalities will
*  matter? You saw the DNA one earlier. I think there's going to be a lot of kind of immediately
*  superhuman capabilities coming out of AI when it comes to things like modeling cells, reading brains,
*  predicting the weather. This is the kind of stuff that humans just can't do, but we're already
*  starting to see that AI systems can do it. And as soon as they can do it, they're pretty much
*  immediately superhuman at it. Will these things start to become agentic? That means will they be
*  able to have their own goals and pursue their plans over medium time horizons? That seems likely,
*  and a lot of people are working on it. That's like, you might think, gee, that's crazy. We
*  wouldn't want to turn these things into independent agents. I could point you to a hundred startups
*  that are doing exactly that for all kinds of different use cases. Are these frontier labs,
*  like your OpenAI's, your Google's, Anthropics, are they going to pause their research or stop
*  scaling if things start to get scary? They say they are. They've signed that statement.
*  They have other various policies they've put in place, but will they follow through on that?
*  Obviously, we'll see. When will the government get involved? It's already starting to. I would
*  expect a lot more focus on AI among not just the US government, but all sorts of governments around
*  the world. And what's going to go on in China is another big one because people are really concerned
*  that we might end up in a sort of AI arms race vis-a-vis China. And if it were to go that way,
*  that would definitely be really bad. So my final thought is I love AI. I feel like I sound a note
*  of caution here, but I love building apps. What AI has done for Weimark has been transformative.
*  Our product is literally 10 times better than it used to be. I use CHAT GPT tons of times every
*  single day, and I love having these AI servants at my disposal. But I would just suggest that while
*  we should all be figuring out how to use the current systems in our lives and in our work,
*  the hyper scaling, the scaling up of 10x and 100x past where we've gone already is something that I
*  think society would be wise to slow down on. Let's figure out what we have. Let's figure out how best
*  to use it before we try to make something that is a superhuman AI scientist, because I don't think
*  we have the strategies that we will ultimately need to keep that under control and to make sure
*  it goes well for us. If you want to find more from me elsewhere, all these different places
*  are good places to find more. So thank you. It is both energizing and enlightening to hear why
*  people listen and learn what they value about the show. So please don't hesitate to reach out via
*  email at tcr at turpentine.co or you can DM me on the social media platform of your choice.
