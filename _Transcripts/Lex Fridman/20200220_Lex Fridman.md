---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 5350s
Video Keywords: ['andrew ng', 'deep learning', 'machine learning', 'coursera', 'deeplearning.ai', 'landing.ai', 'stanford', 'introducation to machine learning', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 545336
Video Rating: None
---

# Andrew Ng: Deep Learning, Education, and Real-World AI | Lex Fridman Podcast #73
**Lex Fridman:** [February 20, 2020](https://www.youtube.com/watch?v=0jspaMLxBig)
*  The following is a conversation with Andrew Eng, one of the most impactful educators,
*  researchers, innovators, and leaders in artificial intelligence and technology space in general.
*  He co-founded Coursera and Google Brain, launched Deep Learning AI, Landing AI,
*  and the AI Fund, and was the chief scientist at Baidu. As a Stanford professor and with Coursera
*  and Deep Learning AI, he has helped educate and inspire millions of students, including me.
*  This is the Artificial Intelligence Podcast. If you enjoy it, subscribe on YouTube,
*  give it five stars on Apple Podcasts, support it on Patreon, or simply connect with me on Twitter
*  at Lex Friedman, spelled F-R-I-D-M-A-N. As usual, I'll do one or two minutes of ads now,
*  and never any ads in the middle that can break the flow of the conversation.
*  I hope that works for you and doesn't hurt the listening experience.
*  This show is presented by Cash App, the number one finance app in the App Store. When you get it,
*  use code LEXPODCAST. Cash App lets you send money to friends, buy bitcoin, and invest in the stock
*  market with as little as $1. Broker services are provided by Cash App Investing, a subsidiary
*  of Square, a member SIPC. Since Cash App allows you to buy bitcoin, let me mention that cryptocurrency
*  in the context of the history of money is fascinating. I recommend Ascent of Money
*  as a great book on this history. Debits and credits on ledgers started over 30,000 years ago.
*  The US dollar was created over 200 years ago, and bitcoin, the first decentralized cryptocurrency,
*  released just over 10 years ago. Given that history, cryptocurrency is still very much in
*  its early days of development, but it's still aiming to, and just might, redefine the nature of
*  money. Again, if you get Cash App from the App Store or Google Play and use the code LEXPODCAST,
*  you'll get $10, and Cash App will also donate $10 to First, one of my favorite organizations
*  that is helping to advance robotics and STEM education for young people around the world.
*  And now, here's my conversation with Andrew Eng. The courses you taught on machine learning
*  at Stanford, and later on Coursera that you co-founded, have educated and inspired millions
*  of people. So let me ask you, what people or ideas inspired you to get into computer science
*  and machine learning when you were young? When did you first fall in love with the field?
*  Is another way to put it. During up in Hong Kong and Singapore, I started learning to code when I
*  was five or six years old. At that time, I was learning the basic programming language, and I
*  would take these books and they'll tell you, type this program into your computer. So I'd type that
*  program into my computer. And as a result of all that typing, I would get to play these very simple,
*  shoot them up games that I had implemented on my little computer. So I thought it was fascinating,
*  as a young kid, that I could write this code. I was really just copying code from a book into
*  my computer to then play these cool little video games. Another moment for me was when I was a
*  teenager and my father, because the doctor was reading about expert systems and about neural
*  networks. So he got me to read some of these books, and I thought it was really cool. You
*  could write a computer that started to exhibit intelligence. Then I remember doing an internship
*  while I was in high school. This was in Singapore, where I remember doing a lot of photocopying and
*  office assistants. And the highlight of my job was when I got to use the shredder.
*  So the teenager, me, remember thinking, boy, this is a lot of photocopying. If only we could write
*  software, build a robot, something to automate this, maybe I could do something else. So I think a
*  lot of my work since then has centered on the theme of automation. Even the way I think about
*  machine learning today, we're very good at writing learning algorithms that can automate
*  things that people can do. Or even launching the first MOOCs, Mass Open Online Courses,
*  that later led to Coursera. I was trying to automate what could be automatable in how I
*  was teaching on campus. The process of education tried to automate parts of that to make it more,
*  sort of to have more impact from a single teacher, single educator.
*  Yeah. I felt teaching at Stanford, I was teaching machine learning to about 400 students a year at
*  the time. And I found myself filming the exact same video every year, telling the same jokes
*  in the same room. And I thought, why am I doing this? Why don't we just take last year's video,
*  and then I can spend my time building a deeper relationship with students. So that process of
*  thinking through how to do that, that led to the first MOOCs that we launched.
*  And then you have more time to write new jokes. Are there favorite memories from your early days
*  at Stanford teaching thousands of people in person and then millions of people online?
*  You know, teaching online, what not many people know was that a lot of those videos were shot
*  between the hours of 10 PM and 3 AM. A lot of times, launching the first MOOCs at Stanford,
*  we'd already announced the course, about 100,000 people had signed up. We just started to write
*  the code and we had not yet actually filmed the video. So we had a lot of pressure, 100,000 people
*  waiting for us to produce the content. So many Fridays, Saturdays, I would go out, have dinner
*  with my friends. And then I would think, okay, do you want to go home now or do you want to go
*  to the office to film videos? And the thought of being able to help 100,000 people potentially
*  learn machine learning, fortunately, that made me think, okay, I'm going to go to my office,
*  go to my tiny little recording studio. I would adjust my logic webcam, adjust my Wacom tablet,
*  make sure my lapel mic was on. And then I would start recording often until 2 AM or 3 AM. I think
*  unfortunately, that doesn't show that it was recorded that late at night, but it was really
*  inspiring the thought that we could create content to help so many people learn about machine learning.
*  How did that feel? The fact that you're probably somewhat alone, maybe a couple of friends
*  recording with a Logitech webcam and kind of going home alone at 1 or 2 AM at night and knowing that
*  that's going to reach sort of thousands of people, eventually millions of people.
*  What's that feeling like? I mean, is there a feeling of just satisfaction of pushing through?
*  I think it's humbling. And I wasn't thinking about what I was feeling. I think one thing we,
*  I'm proud to say we got right from the early days was I told my whole team back then that the
*  number one priority is to do what's best for learners, do what's best for students. And so
*  when I went to the recording studio, the only thing on my mind was what can I say? How can I
*  design my slides? What I need to draw right to make these concepts as clear as possible for learners?
*  I think, you know, I've seen sometimes instructors is tempting to, hey, let's talk about my work.
*  Maybe if I teach you about my research, someone will cite my papers a couple more times. And I
*  think one of the things we got right, launched the first few MOOCs and later building Coursera was
*  putting in place that bedrock principle of let's just do what's best for learners and forget about
*  everything else. And I think that that is a guiding principle turned out to be really important to
*  the rise of the MOOC movement. And the kind of learner you imagined in your mind is as broad as
*  possible, as global as possible. So really try to reach as many people interested in machine learning
*  and AI as possible. I really want to help anyone that had an interest in machine learning to break
*  into the field. And I think sometimes I've actually had people ask me, hey, why are you
*  spending so much time explaining gradient descent? And then my answer was, if I look at what I think
*  the learner needs and what benefit from, I felt that having that a good understanding of the
*  foundations coming back to the basics would put them in a better stead to then build on a long term
*  career. So try to consistently make decisions on that principle. So one of the things you actually
*  revealed to the narrow AI community at the time and to the world is that the amount of people who
*  are actually interested in AI is much larger than we imagined. By you teaching the class and how
*  popular it became, it showed that, wow, this isn't just a small community of sort of people who go to
*  NeurIPS and it's much bigger. It's developers, it's people from all over the world. I mean,
*  I'm Russian, so everybody in Russia is really interested. There's a huge number of programmers
*  who are interested in machine learning, India, China, South America, everywhere. There's just
*  millions of people who are interested in machine learning. So how big do you get a sense that this,
*  the number of people is that are interested from your perspective?
*  I think the number has grown over time. I think one of those things that maybe it feels like it
*  came out of nowhere, but it's an insider building it. It took years. It's one of those overnight
*  successes that took years to get there. My first foray into this type of online education was when
*  we're filming my Stanford class and sticking the videos on YouTube and some other things. We had
*  uploaded the whole works and so on, but it's basically the one hour, 15 minute video that
*  we put on YouTube. And then we had four or five other versions of websites that had built,
*  most of which you would never have heard of because they reached small audiences, but that
*  allowed me to iterate, allow my team and me to iterate, to learn what the ideas that work and
*  what doesn't. For example, one of the features I was really excited about and really proud of was
*  build this website where multiple people could be logged into the website at the same time.
*  So today, if you go to a website, if you are logged in and then I want to log in,
*  you need to log out. It was the same browser, the same computer. But I thought, well, what if two
*  people say you and me were watching a video together in front of a computer? What if a website
*  could have you type your name and password, have me type my name and password, and then now the
*  computer knows both of us are watching together and it gives both of us credit for anything we do
*  as a group. Infantist feature rolled it out in a high school in San Francisco. We had about 20
*  something users. Where's the teacher there? Sacred Heart Cathedral Prep, the teacher is great.
*  Guess what? Zero people use this feature. Turns out people studying online, they want to watch the
*  videos by themselves so you can play back, pause at your own speed rather than in groups. So that
*  was one example of a tiny lesson learned out of many that allowed us to hone into the set of
*  features. And it sounds like a brilliant feature. So I guess the lesson to take from that is,
*  there's something that looks amazing on paper and then nobody uses it. It doesn't actually have the
*  impact that you think it might have. So yeah, I saw that you really went through a lot of different
*  features and a lot of ideas to arrive at the final, at Coursera, the final kind of powerful
*  thing that showed the world that MOOCs can educate millions. And I think with the whole machine
*  learning movement as well, I think it didn't come out of nowhere. Instead what happened was
*  as more people learned about machine learning, they would tell their friends and their friends
*  would see how it's applicable to their work. And then the community kept on growing. And I think
*  we're still growing. I don't know in the future what percentage of all developers will be AI
*  developers. I could easily see it being north of 50%, right? Because so many AI developers broadly
*  construed, not just people doing the machine learning modeling, but the people building
*  infrastructure, data pipelines, all the software surrounding the core machine learning model.
*  Maybe it's even bigger. I feel like today, almost every software engineer has some understanding of
*  the cloud. Not all, but maybe it's my microcontroller developer doesn't need to do the
*  cloud. But I feel like the vast majority of software engineers today are sort of having
*  the patience to cloud. I think in the future, maybe we'll approach nearly 100% of all developers
*  being in some way an AI developer, at least having an appreciation of machine learning.
*  My hope is that there's this kind of effect that there's people who are not really interested in
*  being a programmer or being into software engineering, like biologists, chemists,
*  and physicists, even mechanical engineers, all these disciplines that are now more and more
*  sitting on large data sets. And here, they didn't think they're interested in programming until they
*  have this data set and they realize there's this set of machine learning tools that allow you to
*  use the data set. So they actually become, they learn to program and they become new programmers.
*  Not just because you've mentioned a larger percentage of developers become machine learning
*  people, it seems like more and more the kinds of people who are becoming developers is also
*  growing significantly. Yeah. I think once upon a time, only a small part of humanity was literate,
*  could read and write. And maybe you thought, maybe not everyone needs to learn to read and write.
*  Go listen to a few monks, right? Read to you. And maybe that was enough. Or maybe we just need a few
*  handful of authors to write the best sellers and then no one else needs to write. But what we found
*  was that by giving as many people, in some countries, almost everyone basic literacy,
*  it dramatically enhanced human to human communications. And we can now write for
*  an audience of one, such as if I send you an email or you send me an email. I think in computing,
*  we're still in that phase where so few people know how to code that the coders mostly have to
*  code for relatively large audiences. But if everyone, or most people became developers
*  at some level, similar to how most people in developed economies are somewhat literate,
*  I would love to see the owners of a mom and pop store be able to write a little bit of code to
*  customize the TV display for their special this week. And I think it will enhance human to computer
*  communications, which is becoming more and more important today as well.
*  So you think you think it's possible that machine learning becomes kind of similar to literacy where
*  where, yeah, like you said, the owners of a mom and pop shop is basically everybody in all walks
*  of life would have some degree of programming capability. I could see society getting there.
*  There's one other interesting thing, you know, if I go talk to the mom and pop store, if I talk to a
*  lot of people in their daily professions, I previously didn't have a good story for why they
*  should learn to code. You know, we could give them some reasons. But what I found with the rise of
*  machine learning and data science is that I think the number of people with a concrete use for data
*  science in their daily lives in their jobs, maybe even larger than the number of people
*  with concrete use for software engineering. For example, if you actually if you run a small mom
*  and pop store, I think if you can analyze the data about your sales, your customers,
*  I think there's actually real value there, maybe even more than traditional software engineering.
*  So I find that for a lot of my friends in various professions, be it recruiters or accountants or,
*  you know, people that work in the factories, which I do with more and more these days,
*  I feel if they were data scientists at some level, they could immediately use that in their work.
*  So I think that data science and machine learning may be an even easier entree into the developer
*  world for a lot of people than the software engineering. That's interesting. And I agree
*  with that. But that's beautifully put. We live in a world where most courses and talks have slides,
*  PowerPoint, keynote, and yet you famously often still use a marker and a whiteboard.
*  The simplicity of that is compelling and for me, at least fun to watch. So let me ask, why do you
*  like using a marker and whiteboard even on the biggest of stages? I think it depends on the
*  concepts you want to explain. For mathematical concepts, it's nice to build up the equation one
*  piece at a time. And the whiteboard marker or the pen and stylus is a very easy way to build up an
*  equation, build up a complex concept one piece at a time while you're talking about it. And
*  sometimes that enhances understandability. The downside of writing is that it's slow. And so
*  if you want a long sentence, it's very hard to write that. So I think there are pros and cons.
*  Sometimes I use slides and sometimes I use a whiteboard or a stylus.
*  The slowness of a whiteboard is also its upside because it forces you to reduce everything to
*  the basics. So some of your talks involve the whiteboard. I mean, it's really not what you go
*  very slowly and you really focus on the most simple principles. And that's a beautiful,
*  that enforces a kind of a minimalism of ideas that I think is surprising at least for me is
*  great for education. Like a great talk, I think is not one that has a lot of content. A great talk
*  is one that just clearly says a few simple ideas. And I think the whiteboard somehow enforces that.
*  Peter Abil, who is now one of the top roboticists and reinforcement learning experts in the world,
*  was your first PhD student. So I bring him up just because I kind of imagine this is,
*  must have been an interesting time in your life. Do you have any favorite memories of working with
*  Peter, your first student in those uncertain times, especially before deep learning really
*  sort of blew up any favorite memories from those times?
*  Yeah, I was really fortunate to have had Peter Abil as my first PhD student. And I think even
*  my long-term professional success builds on early foundations or early work that Peter was so
*  critical to. So I was really grateful to him for working with me. What not a lot of people know
*  is just how hard research was and still is. Peter's PhD thesis was using reinforcement
*  learning to fly helicopters. And so, you know, actually even today the website heli.stanford.edu,
*  h-e-l-i.stanford.edu is still up. You can watch videos of us using reinforcement learning to make
*  a helicopter fly upside down, fly loops, rolls. It's just cool. It's one of the most incredible
*  robotics videos ever. So people should watch it. It's inspiring. That's from like 2008 or seven
*  or six, like that range. Something like that. It was like, yeah, it was over 10 years old.
*  That was really inspiring to a lot of people. Yeah. What not many people see is how hard it was.
*  So Peter and Adam Coase and Morgan Quigley and I were working on various versions of the helicopter
*  and a lot of things did not work. For example, turns out one of the hardest problems we had was
*  when a helicopter is flying around upside down doing stunts, how do you figure out the position?
*  How do you localize a helicopter? So we want to try all sorts of things. Having one GPS unit
*  doesn't work because you're flying upside down, GPS units facing down, so you can't see the
*  satellite. So we tried, we experimented trying to have two GPS units, one facing up, one facing
*  down. So if you flip over, that didn't work because the downward facing one couldn't synchronize if
*  you're flipping quickly. Morgan Quigley was exploring this crazy complicated configuration
*  of specialized hardware to interpret GPS signals. Looking at FPG is completely insane. Spent about
*  a year working on that, didn't work. So I remember Peter, great guy, him and me, sitting down in my
*  office looking at some of the latest things we had tried that didn't work and saying, done it.
*  What now? Because we tried so many things and it just didn't work. In the end, what we did
*  and Adam Colts was crucial to this was put cameras on the ground and use cameras on the ground to
*  localize the helicopter. And that solved the localization problem so that we could then focus
*  on the reinforcement learning and inverse reinforcement learning techniques to then
*  actually make the helicopter fly. And I'm reminded when I was doing this work at Stanford,
*  around that time, there was a lot of reinforcement learning theoretical papers, but not a lot of
*  practical applications. So the autonomous helicopter work for flying helicopters was one of
*  the few practical applications of reinforcement learning at the time, which caused it to become
*  pretty well known. I feel like we might've almost come full circle with today. There's so much buzz,
*  so much hype, so much excitement about reinforcement learning. But again, we're hunting
*  for more applications of all of these great ideas that the communities come up with.
*  What was the drive in the face of the fact that most people are doing theoretical work?
*  What motivate you in the uncertainty and the challenges to get the helicopter to do the
*  applied work, to get the actual system to work? Yeah, in the face of fear, uncertainty,
*  the setbacks that you mentioned for localization. I like stuff that works.
*  In the physical world. So it's back to the shredder.
*  I like theory, but when I work on theory myself, and this is personal taste, I'm not saying anyone
*  else should do what I do. But when I work on theory, I personally enjoy it more if I feel that
*  the work I do will influence people, have positive impact, will help someone.
*  I remember when many years ago, I was speaking with a mathematics professor,
*  and it kind of just said, hey, why do you do what you do? And then he said, he had stars in his
*  eyes when he answered. And this mathematician, not from Stanford, different university, he said,
*  I do what I do because it helps me to discover truth and beauty in the universe. He had stars
*  in his eyes when he said that. And I thought that's great. I don't want to do that. I think
*  it's great that someone does that, fully support the people that do it, a lot of respect for people
*  that, but I am more motivated when I can see a line to how the work that my teams and I are doing
*  helps people. The world needs all sorts of people. I'm just one type. I don't think everyone should
*  do things the same way as I do. But when I delve into either theory or practice, if I personally
*  have conviction that here's a pathway to help people, I find that more satisfying to have that
*  conviction. That's your path. You were a proponent of deep learning before it gained widespread
*  acceptance. What did you see in this field that gave you confidence? What was your thinking
*  process like in that first decade of the, I don't know what that's called, 2000s, the aughts?
*  Yeah. I can tell you the thing we got wrong and the thing we got right. The thing we really got
*  wrong was the early importance of unsupervised learning. So early days of Google Brain, we put
*  a lot of effort into unsupervised learning rather than supervised learning. And there was this
*  argument, I think it was around 2005 after NeurIPS at that time called NIPS, but now NeurIPS had ended
*  and Jeff Hinton and I were sitting in the cafeteria outside the conference. We had lunch
*  with us chatting and Jeff pulled up this napkin. He started sketching this argument on a napkin.
*  It was very compelling as I repeated. Human brain has about a hundred trillion. So there's 10 to the
*  14 synaptic connections. You will live for about 10 to the nine seconds. That's 30 years. You
*  actually live for two by 10 to the nine, maybe three by 10 to the nine seconds. So let's say 10
*  to the nine. So if each synaptic connection, each weight in your brain's neural network
*  has just a one bit parameter, that's 10 to the 14 bits you need to learn in up to 10 to the nine
*  seconds of your life. So via this simple argument, which is a lot of problems, it's very simplified.
*  That's 10 to the five bits per second you need to learn in your life. And I have a one year old
*  daughter. I am not pointing out 10 to five bits per second of labels to her.
*  And I think I'm a very loving parent, but I'm just not going to do that. So from this very crude,
*  definitely problematic argument, there's just no way that most of what we know is through supervised
*  learning. But where you get so many bits of information is from sucking in images, audio,
*  just experiences in the world. And so that argument, and there are a lot of known forces
*  argument, you know, we should go into, really convinced me that there's a lot of power to
*  unsupervised learning. So that was the part that we actually maybe got wrong. I still think unsupervised
*  learning is really important, but in the early days, you know, 10, 15 years ago, a lot of us thought
*  that was the path forward. Oh, so you're saying that that perhaps was the wrong intuition for
*  the time for the time that that was the part we got wrong. The part we got right was the importance
*  of scale. So Adam Coates, another wonderful person, fortunate to have worked with him.
*  He was in my group at Stanford at the time, and Adam had run these experiments at Stanford,
*  showing that the bigger we train a learning algorithm, the better his performance. And
*  it was based on that. There was a graph that Adam generated, you know, where the x axis, y axis,
*  lines going up into the right. So big, it may make the thing the bestest performance accuracy
*  is the vertical axis. So it's really based on that chart that Adam generated that gave me the
*  conviction that it could scale these models way bigger than what we could on a few CPUs, which is
*  what we had a Stanford that we could get even better results. And it was really based on that
*  one figure that Adam generated that gave me the conviction to go with Sebastian Thrun to pitch,
*  you know, starting a project at Google, which became the Google Brain project.
*  Brain, you go find Google Brain. And there the intuition was scale will bring performance for
*  the system. So we should chase larger and larger scale. And I think people don't realize how
*  groundbreaking of a simple, but it's a groundbreaking idea that bigger data
*  sets will result in better performance. It was controversial at the time. Some
*  of my well-meaning friends, you know, senior people in the machine learning community,
*  I won't name, but who's people, some of whom we know, my well-meaning friends came and were
*  trying to give me friendly as a, Hey, Andrew, why are you doing this? This is crazy. It's in
*  the near and dear architecture. Look at these architectures of building. You just want to go
*  for scale. Like this is a bad career move. So my well-meaning friends, you know, we're trying to,
*  some of them were trying to talk me out of it. But I find that if you want to make a breakthrough,
*  you sometimes have to have conviction and do something before it's popular. Since that lets
*  you have a bigger impact. Let me ask you just in a small attention on that topic. I find myself
*  arguing with people saying that greater scale, especially in the context of active learning, so
*  very carefully selecting the data set, but growing the scale of the data set is going to lead to
*  even further breakthroughs in deep learning. And there's currently pushback at that idea
*  that larger data sets are no longer that. So you want to increase the efficiency of learning. You
*  want to make better learning mechanisms. And I personally believe that just bigger data sets
*  will still with the same learning methods we have now will result in better performance.
*  What's your intuition at this time on those, on the, this dual side is do we need to come up with
*  better architectures for learning or can we just get bigger, better data sets that will improve
*  performance? I think both are important and it's also problem dependent. So for a few data sets,
*  we may be approaching, you know, a base error rate or approaching or surpassing human level
*  performance. And then there's that theoretical ceiling that we will never surpass a base error
*  rate. But then I think there are plenty of problems where, where we're still quite far
*  from either human level performance or from base error rate and bigger data sets with new networks
*  without further effort innovation will be sufficient to take us further.
*  But on the flip side, if we look at the recent breakthroughs using, you know,
*  transforming networks or language models, it was a combination of novel architecture,
*  but also scale had a lot to do with it. If we look at what happened with, you know,
*  GP2 and BERT, I think scale was a large part of the story.
*  Yeah, that's, that's not often talked about is the scale of the data set it was trained on
*  and the quality of the data set, because there's some, so it was like redded threads that had,
*  they were operated highly. So there's already some weak supervision on a very large data set
*  that people don't often talk about, right? I find that today we have
*  maturing processes to managing code, things like get right version control. It took us a long time
*  to evolve the good processes. I remember when my friends and I were emailing each other C++ files
*  and email, you know, but then we had, was it CVS subversion, get maybe something else in the future.
*  We're very immature in terms of tools for managing data and think about the clean data
*  and how to solve very hot, messy data problems. I think there's a lot of innovation there
*  to be had still. I love the idea that you were versioning through email.
*  I'll give you one example. When we work with manufacturing companies, it's not at all uncommon
*  for there to be multiple labels that disagree with each other, right? And so we would do the work in
*  visual inspection. We will, you know, take say a plastic part and show it to one inspector.
*  And the inspector sometimes very opinionated to go, clearly that's a defect, this trash, unacceptable,
*  gotta reject this part. Take the same part to different inspector, different, very opinionated,
*  clearly this trash is small, it's fine. Don't throw it away. You're going to make us, you know,
*  and then sometimes you take the same plastic part, show it to the same inspector in the afternoon,
*  and I suppose in the morning, and very opinionated to go in the morning to say, clearly this is okay.
*  In the afternoon, equally confident, clearly this is a defect. And so what is the AI team supposed
*  to do if sometimes even one person doesn't agree with himself or herself in the span of a day?
*  So I think these are the types of very practical, very messy data problems that my teams wrestle
*  with. In the case of large consumer internet companies, where you have a billion users,
*  you have a lot of data, you don't worry about it, just take the average, it kind of works.
*  But in a case of other industry settings, we don't have big data, it's just a small data,
*  very small data sets, maybe around 100 defective parts or 100 examples of a defect. If you have
*  only 100 examples, these little labeling errors, you know, if 10 of your 100 labels are wrong,
*  that actually is 10% of your data set has a big impact. So how do you clean this up? What are you
*  supposed to do? This is an example of the types of things that my teams, this is a landing AI example,
*  are wrestling with to deal with small data, which comes up all the time once you're outside consumer
*  internet. Yeah, that's fascinating. So then you invest more effort and time in thinking about the
*  actual labeling process. What are the labels? What are the how are disagreements resolved and all
*  those kinds of like pragmatic real world problems? That's a fascinating space. Yeah, I find that
*  actually when I'm teaching at Stanford, I increasingly encourage students at Stanford to
*  try to find their own project for the end of term project rather than just downloading someone else's
*  nicely clean data set. It's actually much harder if you need to go and define your own problem and
*  find your own data set rather than you go to one of the several good websites, very good websites
*  with with cleans scoped data sets that you could just work on. You're not running three efforts,
*  the AI fund, landing AI and deep learning dot AI. As you've said, the AI fund is involved in creating
*  new companies from scratch, landing AI is involved in helping already established companies do AI,
*  and deep learning AI is for education of everyone else, or of individuals interested
*  of getting into the field and excelling in it. So let's perhaps talk about each of these areas.
*  First, deep learning dot AI. How the basic question, how does a person interested in deep learning
*  get started in the field? Deep learning AI is working to create causes to help people break into
*  AI. So my machine learning course that I taught through Stanford is one of the most popular
*  courses on Coursera. To this day, it's probably one of the courses, sort of if I asked somebody,
*  how did you get into machine learning? Or how did you fall in love with machine learning? Or
*  would get you interested? It always goes back to engineering at some point. So you've been
*  fluent, the amount of people you've influenced is ridiculous. So for that, I'm sure I speak for a
*  lot of people say big thank you. Yeah, thank you. I was once reading a news article. I think it was
*  tech review, and I'm going to mess up the statistic. But I remember reading an article that said
*  something like one third of all programmers are self-taught. I may have the number one
*  third wrong, it was two thirds. But when I read that article, I thought, this doesn't make sense.
*  Everyone is self-taught. So because you teach yourself, I don't teach people. That's well put.
*  So yeah, so how does one get started in deep learning? And where does deep learning.ai fit
*  into that? So the deep learning specialization offered by deep learning.ai is, I think,
*  was Coursera's top specialization, it might still be. So it's a very popular way for people
*  to take that specialization, to learn about everything from neural networks to how to
*  tune in your network to what does a confnet do, what is a RNN or a sequence model, or what is an
*  attention model. And so the deep learning specialization steps everyone through those
*  algorithms. So you deeply understand it and can implement it and use it for whatever application.
*  From the very beginning. So what would you say are the prerequisites for somebody to take the
*  deep learning specialization in terms of maybe math or programming background?
*  Need to understand basic programming since there are programming exercises in Python.
*  And the math prereq is quite basic. So no calculus is needed. If you know calculus is great,
*  you get better intuitions. But deliberately try to teach that specialization without requiring
*  calculus. So I think high school math would be sufficient. If you know how to multiply two
*  matrices, I think that's great. So a little basic linear algebra is great.
*  Basically linear algebra, even very, very basic linear algebra in some programming.
*  I think that people that have done the machine learning course will find the deep learning
*  specialization a bit easier. But it's also possible to jump into the deep learning
*  specialization directly, but it will be a little bit harder since we tend to go over faster
*  concepts like how does gradient descent work and what is the objective function,
*  which is covered more slowly in the machine learning course.
*  Could you briefly mention some of the key concepts in deep learning that students
*  should learn that you envision them learning in the first few months, in the first year or so?
*  So if you take the deep learning specialization, you learn the foundations of what is a neural
*  network. How do you build up a neural network from a single logistic unit to a stack of layers to
*  different activation functions. You learn how to train the neural networks.
*  One thing I'm very proud of in that specialization is we go through a lot of practical know-how of how
*  to actually make these things work. So what are the differences between different optimization
*  algorithms? What do you do if the algorithm overfits? How do you tell if the algorithm is
*  overfitting? When do you collect more data? When should you not bother to collect more data?
*  I find that even today, unfortunately, there are engineers that will spend six months trying
*  to pursue a particular direction, such as collect more data because we heard more data is valuable.
*  Sometimes you could run some tests and could have figured out six months earlier that for this
*  problem, collecting more data isn't going to cut it. So just don't spend six months collecting more
*  data. Spend your time modifying the architecture or trying something else. So go through a lot of
*  practical know-how so that when someone, when you take the deep learning specialization,
*  you have those skills to be very efficient in how you build these networks.
*  So dive right in to play with the network, to train it, to do the inference on a particular
*  data set, to build intuition about it without building it up too big to where you spend,
*  like you said, six months learning, building up your big project without building any intuition
*  of a small aspect of the data that could already tell you everything you need to know about that
*  data. Yes. And also the systematic frameworks of thinking for how to go about building practical
*  machine learning. Maybe to make an analogy, when we learn to code, we have to learn the syntax of
*  some programming language, right? Be it Python or C++ or Octave or whatever. But that equally
*  important or maybe even more important part of coding is to understand how to string together
*  these lines of code into coherent things. So when should you put something in the function column?
*  When should you not? How do you think about abstraction? So those frameworks are what makes
*  a programmer efficient, even more than understanding the syntax. I remember when I was an undergrad at
*  Carnegie Mellon, one of my friends would debug their code by first trying to compile it and then
*  it was C++ code. And then every line did a syntax error. They want to get rid of the syntax errors
*  as quickly as possible. So how do you do that? Well, they would delete every single line of code
*  with a syntax error. So really efficient for getting rid of syntax errors for horrible debugging
*  service. So we learned how to debug. And I think in machine learning, the way you debug a machine
*  learning program is very different than the way you do binary search or whatever, or use a debugger,
*  trace through the code in traditional software engineering. So it's an evolving discipline,
*  but I find that the people that are really good at debugging machine learning algorithms
*  are easily 10x, maybe 100x faster at getting something to work.
*  And the basic process of debugging is, so the bug in this case, why isn't this thing learning,
*  improving, sort of going into the questions of overfitting and all those kinds of things.
*  That's the logical space that the debugging is happening in with neural networks.
*  Yeah, the often question is, why doesn't it work yet? Or can I expect it to eventually work?
*  And what are the things I could try? Change the architecture, more data, more regularization,
*  different optimization algorithm, different types of data. So to answer those questions systematically,
*  so that you don't spend six months heading down the blind alley before someone comes and says,
*  why did you spend six months doing this? What concepts in deep learning do you think
*  students struggle the most with? Or is the biggest challenge for them was to get over that hill?
*  It hooks them and it inspires them and they really get it.
*  Similar to learning mathematics, I think one of the challenges of deep learning is that
*  there are a lot of concepts that build on top of each other. If you ask me what's hard about
*  mathematics, I have a hard time pinpointing one thing. Is it addition, subtraction? Is it a
*  carry? Is it multiplication? There's just a lot of stuff. I think one of the challenges of learning
*  math and of learning certain technical fields is that there are a lot of concepts and if you
*  miss a concept, then you're kind of missing the prerequisite for something that comes later.
*  So in the deep learning specialization, try to break down the concepts to maximize the arts of
*  each component being understandable. So when you move on to the more advanced thing, we learn
*  confidence, hopefully you have enough intuitions from the earlier sections to then understand why
*  we structure confidence in a certain way and then eventually why we build RNNs and LSTMs or
*  attention models in a certain way, building on top of the earlier concepts. Actually, I'm curious,
*  you do a lot of teaching as well. Do you have a favorite, this is the hard concept moment in
*  your teaching? Well, I don't think anyone's ever turned the interview on me. I'm glad to be the
*  first. I think that's a really good question. Yeah, it's really hard to capture the moment when
*  they struggle. I think you put it really eloquently. I do think there's moments that are like aha
*  moments that really inspire people. I think for some reason, reinforcement learning, especially
*  deep reinforcement learning is a really great way to really inspire people and get what the use of
*  neural networks can do. Even though neural networks really are just a part of the deep RL framework,
*  but it's a really nice way to paint the entirety of the picture of a neural network being able
*  to learn from scratch, knowing nothing and explore the world and pick up lessons. I find that a lot
*  of the aha moments happen when you use deep RL to teach people about neural networks, which is
*  counterintuitive. I find like a lot of the inspired sort of fire in people's passion,
*  people's eyes, it comes from the RL world. Do you find reinforcement learning to be a useful part
*  of the teaching process or no? I still teach reinforcement learning in one of my Stanford
*  classes. And my PhD thesis was on reinforcement learning. So I clearly love the field. I find that
*  if I'm trying to teach students the most useful techniques for them to use today, I end up
*  shrinking the amount of time I talk about reinforcement learning. It's not what's
*  working today. Now our world changes so fast. Maybe it does be totally different in a couple of years.
*  But I think we need a couple more things for reinforcement learning to get there.
*  One of my teams is looking to reinforcement learning for some robotic control tasks. So I
*  see the applications, but if you look at it as a percentage of all of the impact of the types of
*  things we do, at least today, outside of playing video games, right? In a few other games, the
*  scope. Actually at Neuro, a bunch of us were standing around saying, hey, what's your best
*  example of an actual deploy reinforcement learning application among senior machine
*  learning researchers? And again, there are some emerging ones, but there are not that many great
*  examples. I think you're absolutely right. The sad thing is there hasn't been a big
*  application impact for real world application reinforcement learning. I think its biggest impact
*  to me has been in the toy domain, in the game domain, in the small example. That's what I mean
*  for educational purpose. It seems to be a fun thing to explore neural networks with. But I think
*  from your perspective, and I think that might be the best perspective is if you're trying to educate
*  with a simple example in order to illustrate how this can actually be grown to scale and have a real
*  world impact, then perhaps focusing on the fundamentals of supervised learning in the
*  context of a simple data set, even like an MNIST data set is the right way, is the right path to
*  take. The amount of fun I've seen people have with reinforcement learning has been great, but not in
*  the applied impact on the real world setting. So it's a trade off. How much impact you want to have
*  versus how much fun you want to have. Yeah, that's really cool. And I feel like the world
*  actually needs all sorts. Even within machine learning, I feel like deep learning is so exciting,
*  but the AI team shouldn't just use deep learning. I find that my teams use a portfolio of tools.
*  And maybe that's not the exciting thing to say, but some days we use a neural net, some days
*  we use a PCA. Actually, the other day I was sitting down with my team looking at PCA residuals,
*  trying to figure out what's going on with PCA applied to manufacturing problem. And some days
*  we use a prophecy graphical model. Some days we use a knowledge draft, which is one of the things
*  that has tremendous industry impact, but the amount of chatter about knowledge drafts in
*  academia is really thin compared to the actual role impact. So I think reinforcement learning
*  should be in that portfolio. And then it's about balancing how much we teach all of these things.
*  The world should have diverse skills. It'd be sad if everyone just learned one narrow thing.
*  Yeah. The diverse skill help you discover the right tool for the job. What is the most beautiful,
*  surprising or inspiring idea in deep learning to you? Something that captivated your imagination?
*  Is it the scale that could be, the performance that could be achieved with scale, or is there
*  other ideas? I think that if my only job was being an academic researcher, if an unlimited budget,
*  and didn't have to worry about short-term impact and only focus on long-term impact,
*  I probably spent all my time doing research on unsupervised learning.
*  I still think unsupervised learning is a beautiful idea. At both this past New York and
*  ICML, I was attending workshops or listening to various talks about self-supervised learning,
*  which is one vertical segment maybe of unsupervised learning that I'm excited about.
*  Maybe just to summarize the idea, I guess you know the idea well described.
*  No, please.
*  Here's an example of self-supervised learning. Let's say we grab a lot of unlabeled images off
*  the internet. So with infinite amounts of this type of data, I'm going to take each image and
*  rotate it by a random multiple of 90 degrees. Then I'm going to train a supervised neural
*  network to predict what was the original orientation. So it has to be rotated 90 degrees,
*  180 degrees, 270 degrees, or zero degrees. You can generate an infinite amount of labeled data
*  because you rotated the image so you know what's the ground truth label. Various researchers have
*  found that by taking unlabeled data and making up labeled datasets and training a large neural
*  network on these tasks, you can then take the hidden layer representation and transfer it to
*  a different task very powerfully. Learning word embeddings where we take a sentence,
*  delete a word, predict the missing word, which is how we learn. One of the ways we learn word
*  embeddings is another example. I think there's now this portfolio of techniques for generating
*  these made up tasks. Another one called jigsaw would be if you take an image, cut it up into a
*  three by three grid, so like a nine, three by three puzzle piece, jump out the nine pieces,
*  and have a neural network predict which of the nine factorial possible permutations it came from.
*  So many groups, including OpenAI, Peter B has been doing some work on this too, Facebook,
*  Google Brain, I think DeepMind, actually Aaron Vendor-Ault has great work on the CPC objective.
*  So many teams are doing exciting work and I think this is a way to generate infinite labeled data
*  and I find this a very exciting piece of unsupervised learning.
*  So long term you think that's going to unlock a lot of power in machine learning systems?
*  Is this kind of unsupervised learning?
*  I don't think there's a whole enchilada. I think it's just a piece of it. And I think this one
*  piece unsupervised self supervised learning is starting to get traction. We're very close to it
*  being useful. Well, web embeddings are really useful. I think we're getting closer and closer
*  to just having a significant real world impact maybe in computer vision and video. But I think
*  this concept and I think there'll be other concepts around it. Other unsupervised learning things that
*  I worked on, I've been excited about. I was really excited about sparse coding and ICA,
*  slow feature analysis. I think all of these are ideas that various of us were working on
*  about a decade ago before we all got distracted by how well supervised learning was doing.
*  Supervised learning work, yeah. So we would return to the fundamentals of representation learning
*  that really started this movement of deep learning. I think there's a lot more work that one could
*  explore around the steam of ideas and other ideas to come with better algorithms.
*  So if we could return to maybe talk quickly about the specifics of deep learning that AI,
*  the deep learning specialization perhaps, how long does it take to complete the course would you say?
*  The official length of the deep learning specialization is I think 16 weeks, so about
*  four months, but it's go at your own pace. So if you subscribe to the deep learning specialization,
*  there are people that finished it in less than a month by working more intensely and studying
*  more intensely. So it really depends on the individual. When we created the deep learning
*  specialization, we wanted to make it very accessible and very affordable. And with Coursera and
*  deep learning AI's education mission, one of the things that's really important to me is that
*  if there's someone for whom paying anything is a financial hardship, then just apply for financial
*  aid and get it for free. If you were to recommend a daily schedule for people in learning, whether
*  it's through the deep learning data, AI specialization or just learning in the world of deep learning,
*  what would you recommend? How do they go about day to day specific advice about learning,
*  about their journey in the world of deep learning, machine learning?
*  I think getting the habit of learning is key, and that means regularity. So for example, we send out
*  our weekly newsletter, The Batch, every Wednesday. So people know it's coming Wednesday, you can
*  spend a little bit of time on Wednesday catching up on the latest news through The Batch on Wednesday.
*  And for myself, I've picked up a habit of spending some time every Saturday and every Sunday reading
*  or studying. And so I don't wake up on a Saturday and have to make a decision. Do I feel like reading
*  or studying today or not? It's just what I do. And the fact is a habit makes it easier. So I think if
*  someone can get into that habit, it's like, just like we brush our teeth every morning,
*  I don't think about it. If I thought about it, it's a little bit annoying to have to spend two minutes
*  doing that. But it's a habit that it takes no cognitive load. But this would be so much harder
*  if we have to make a decision every morning. And actually, that's the reason why I wear the same
*  thing every day as well. It's just one less decision. I just get up and then wear my shirt.
*  So I think if you can get that habit, that consistency of studying, then it actually
*  feels easier. So yeah, it's kind of amazing. In my own life, I play guitar every day for,
*  I force myself to at least for five minutes play guitar. It's a ridiculously short period of time.
*  But because I've gotten into that habit, it's incredible what you can accomplish in a period of
*  a year or two years. You can become exceptionally good at certain aspects of a thing by just doing
*  it every day for a very short period of time. It's kind of a miracle that that's how it works.
*  It adds up over time. Yeah. And I think it's often not about the birth of sustained efforts
*  and the all-nighters because you could only do that a limited number of times. It's the
*  sustained effort over a long time. I think reading two research papers is a nice thing to do,
*  but the power is not reading two research papers. It's reading two research papers
*  a week for a year. Then you've read a hundred papers and you actually learn a lot when you
*  read a hundred papers. So regularity and making learning a habit. Do you have
*  general other study tips for particularly deep learning that people should, in their process of
*  learning, is there some kind of recommendations or tips you have as they learn? One thing I still do
*  when I'm trying to study something really deeply is take handwritten notes. It varies. I know there
*  are a lot of people that take the deep learning courses during a commute or something where maybe
*  more awkward to take notes. So I know it may not work for everyone, but when I'm taking courses on
*  Coursera, and I still take some every now and then, the most recent one I took was a course on
*  clinical trials because I was interested in that. I got out my little Moleskine notebook and I was
*  sitting in my desk just taking down notes of what the instructor was saying. We know that that act
*  of taking notes, preferably handwritten notes, increases retention. So as you're watching the
*  video, just kind of pausing maybe, and then taking the basic insights down on paper.
*  Yeah. So there have been a few studies. If you search online, you find some of these studies that
*  taking handwritten notes, because handwriting is slower as we're saying just now, it causes you to
*  recode the knowledge in your own words more. And that process of recoding promotes long-term
*  retention. This is as opposed to typing, which is fine. Again, typing is better than nothing.
*  Taking a class and not taking notes is better than not taking any classes at all. But comparing
*  handwritten notes and typing, you can usually type faster for a lot of people than you can handwrite
*  notes. And so when people type, they're more likely to just try to strive verbatim what they heard.
*  And that reduces the amount of recoding. And that actually results in less long-term retention.
*  I don't know what the psychological effect there is, but it's so true. There's something
*  fundamentally different about handwriting. I wonder what that is. I wonder if it is
*  as simple as just the time it takes to write it slower.
*  And because you can't write as many words, you have to take whatever they said and summarize it
*  into fewer words. And that summarization process requires deeper processing of the meaning,
*  which then results in better retention. That's fascinating.
*  Oh, and I think because of Coursera, I spent so much time studying pedagogy.
*  It's actually one of my passions. I really love learning how to more efficiently help others learn.
*  One of the things I do both when creating videos or when we write the batch is I try to think,
*  is one minute spent with us going to be a more efficient learning experience than one minute
*  spent anywhere else? And we really try to make it time efficient for the learners because everyone's
*  busy. So when we're editing, I often tell my teams every word needs to fight for its life.
*  And if we can delete a word, let's just delete it and not waste the learners' time.
*  It's so amazing that you think that way because there is millions of people that are impacted
*  by your teaching and that one minute spent has a ripple effect through years of time,
*  which is fascinating to think about. How does one make a career out of an interest in deep learning?
*  Do you have advice for people? We just talked about sort of the beginning, early steps,
*  but if you want to make it an entire life's journey or at least a journey of a decade or two,
*  how do you do it? So most important thing is to get started.
*  And I think in the early parts of a career, coursework, like the deep learning specialization,
*  or it's a very efficient way to master this material. So because instructors, be it me or
*  someone else or Lawrence Maroney teaches our intensive law specialization or other things
*  we're working on, spend effort to try to make it time efficient for you to learn a new concept.
*  So coursework is actually a very efficient way for people to learn concepts in the beginning
*  parts of breaking into new fields. In fact, one thing I see at Stanford, some of my PhD students
*  want to jump into research right away. And I actually tend to say, look, in your first couple
*  years of PhD student, spend time taking courses because it lays the foundation. It's fine if you
*  are less productive in your first couple of years, you'll be better off in the long term.
*  Beyond a certain point, there's materials that doesn't exist in courses because it's too cutting
*  edge. The courses haven't been created yet. There's some practical experience that were not
*  that good as teaching in a course. And I think after exhausting the efficient coursework,
*  then most people need to go on to either ideally work on projects and then maybe also continue
*  their learning by reading blog posts and research papers and things like that. Doing projects is
*  really important. And again, I think it's important to start small and just do something. Today you
*  read about deep learning, if you say, oh, all these people are doing such exciting things,
*  what if I'm not building a neural network that changes the world? And what's the point? Well,
*  the point is sometimes building that tiny neural network, be it MNIST or upgrade to fashion MNIST,
*  doing your own fun hobby project. That's how you gain the skills to let you do bigger and bigger
*  projects. I find this to be true at the individual level and also at the organizational level. For
*  a company to become good at machine learning, sometimes the right thing to do is not to
*  tackle the giant project, is instead to do the small project that lets the organization learn
*  and then build out from there. But this is true both for individuals and for companies.
*  Taking the first step and then taking small steps is the key. Should students pursue a PhD? Do you
*  think you can do so much? That's one of the fascinating things in machine learning. You
*  can have so much impact without ever getting a PhD. So what are your thoughts? Should people go
*  to grad school? Should people get a PhD? I think that there are multiple good options of which
*  doing a PhD could be one of them. I think that if someone's admitted to a top PhD program,
*  you know, at MIT, Stanford, top schools, I think that's a very good experience. Or if someone gets
*  a job at a top organization, at the top AI team, I think that's also a very good experience.
*  There are some things you still need a PhD to do. If someone's aspiration is to be a professor,
*  you know, at the top academic university, you just need a PhD to do that. But if it goes to,
*  you know, start a company, build a company, do great technical work, I think a PhD is a good
*  experience. But I would look at the different options available to someone, you know, where
*  the place is where you can get a job, where the place is and get into the PhD program, and kind
*  of weigh the pros and cons of those. So just to linger on that for a little bit longer, what final
*  dreams and goals do you think people should have? So what options should they explore? So you can
*  work in industry. So for a large company, like Google, Facebook, Baidu, all these large sort of
*  companies that already have huge teams of machine learning engineers. You can also do within industry
*  sort of more research groups that kind of like Google research, Google brain. Then you can also
*  do, like we said, a professor in academia. And what else? Oh, you can build your own company.
*  You can do a startup. Is there anything that stands out between those options? Or are they
*  all beautiful different journeys that people should consider? I think the thing that affects
*  your experience more is less are you in this company versus that company or academia versus
*  industry. I think the thing that affects your experience most is who are the people you're
*  interacting with in a daily basis. So even if you look at some of the large companies,
*  the experience of individuals in different teams is very different. And what matters most is not
*  the logo above the door when you walk into the giant building every day. What matters most is
*  who are the 10 people, who are the 30 people you interact with every day. So I actually tend to
*  advise people, if you get a job from a company, ask who is your manager? Who are your peers? Who
*  are you actually going to talk to? We're all social creatures. We tend to become more like
*  the people around us. And if you're working with great people, you will learn faster. Or if you get
*  admitted, if you get a job at a great company or a great university, maybe the logo you walk in
*  is great, but you're actually stuck on some team doing really work that doesn't excite you. And
*  then that's actually a really bad experience. So this is true both for universities and for
*  large companies. For small companies, you can kind of figure out who you'd be working with
*  quite quickly. And I tend to advise people if a company refuses to tell you who you work with,
*  someone say, Oh, join us. We have a rotation system. We'll figure it out. I think that's a
*  worrying answer because it means you may not get sent to, you may not actually get to a team with
*  great peers and great people to work with. It's actually a really profound advice that we kind of
*  sometimes sweep. We don't consider too rigorously or carefully. The people around you are really
*  often, especially when you accomplish great things, it seems that great things are accomplished
*  because of the people around you. So that's a, it's not about the, the, whether you learn this thing
*  or that thing, or like you said, the logo that hangs up top, it's the people that's a fascinating
*  and it's such a hard search process of finding, just like finding the right friends and
*  somebody to get married with and that kind of thing. It's a very hard search. It's a
*  people search problem. Yeah. But I think when someone interviews, you know, at a university
*  or the research lab or the large corporation, it's good to insist on just asking who are the people,
*  who is my manager? And if you refuse to tell me, I'm going to think, well, maybe that's cause you
*  don't have a good answer. It may not be someone I like. And if you don't particularly connect,
*  if something feels off with the people, then don't stick to it. You know, that's a really
*  important signal to consider. Yeah. Yeah. And actually, I actually, in my Stanford class, CS230,
*  as well as an ACM talk, I think I gave like a hour long talk on career advice, including on the job
*  search process and some of these. So, so you, so if you can find those videos online. Awesome.
*  I'll point people to them. Beautiful. So the AI fund helps AI startups get off the ground,
*  or perhaps you can elaborate on all the fun things it's involved with. What's your advice
*  on how does one build a successful AI startup? You know, in Silicon Valley, a lot of starts
*  at failures come from building our products that no one wanted. So when, you know, cool technology,
*  but who's going to use it? So I think I tend to be very outcome driven and customer obsessed.
*  Ultimately, we don't get to vote if we succeed or fail. It's only the customer that they're the
*  only one that gets a thumbs up or thumbs down votes in the long term. In the short term,
*  you know, there are various people that get various votes, but in the long term,
*  that's what really matters. So as you build a startup, you have to constantly ask the question,
*  will the customer gives a, give a thumbs up on this? I think so. I think startups that are very
*  customer focused customer says deeply understand the customer and are oriented to serve the customer
*  are more likely to succeed with a provisional that I think all of us should only do things that we
*  think create social good and move the world forward. So I personally don't want to build
*  addictive digital products, just to sell a lot of ads. Well, you know, there are things that that
*  could be lucrative that I won't do. But if we can find ways to serve people in meaningful ways,
*  I think those can be, those can be great things to do, either in the academic setting or in a
*  corporate setting or a startup setting. So can you give me the idea of why you started the AI fund?
*  I remember when I was leading the AI group at Baidu, I had two jobs, two parts of my job. One
*  was to build an AI engine to support the existing businesses. And that was running,
*  just ran, just performed by itself. The second part of my job at the time, which was to try to
*  systematically initiate new lines of businesses using the company's AI capabilities. So, you know,
*  the self-driving car team came out of my group, the smart speaker team, similar to what is Amazon
*  Echo or Alexa in the US. But we actually announced it before Amazon did. So Baidu wasn't
*  following Amazon. That came out of my group. And I found that to be actually the most fun part of
*  my job. So what I wanted to do was to build AI fund as a startup studio to systematically create
*  new startups from scratch. With all the things we can now do with AI, I think the ability to build
*  new teams to go after this rich space of opportunities is a very important mechanism
*  to get these projects done that I think will move the world forward. So I've been fortunate to
*  build a few teams that had a meaningful positive impact. And I felt that we might be able to do
*  this in a more systematic, repeatable way. So a startup studio is a relatively new concept.
*  There are maybe dozens of startup studios right now, but I feel like all of us, many teams are
*  still trying to figure out how do you systematically build companies with a high success rate. So I
*  think even a lot of my venture capital friends seem to be more and more building companies rather
*  than investing in companies. But I find it a fascinating thing to do to figure out the
*  mechanisms by which we could systematically build successful teams, successful businesses
*  in areas that we find meaningful. So a startup studio is something, is a place and a mechanism
*  for startups to go from zero to success, to try to develop a blueprint. It's actually a place for us
*  to build startups from scratch. So we often bring in founders and work with them or maybe even have
*  existing ideas that we match founders with. And then this launches, hopefully into successful
*  companies. So how close are you to figuring out a way to automate the process of starting from
*  scratch and building a successful AI startup? Yeah, I think we've been constantly improving
*  and iterating on our processes, how we do that. So things like, how many customer calls do we need
*  to make in order to get customer validation? How do we make sure that the technology can be built?
*  Quite a lot of our businesses need cutting edge machine learning algorithms. So what kind of
*  algorithms have developed in the last one or two years? And even if it works in a research paper,
*  it turns out taking the production is really hard. There are a lot of issues for making these things
*  work in the real life that are not widely addressed in the academia. So how do we validate that this
*  is actually doable? How do we build a team, get the specialized domain knowledge, be it in education
*  or healthcare, whatever sector we're focusing on. So I think we've actually been getting much better
*  at giving the entrepreneurs a high success rate. But I think the whole world is still
*  in the early phases of picking this out. But do you think there are some aspects of that
*  process that are transferable from one startup to another, to another, to another? Yeah, very much so.
*  You know, starting a company to most entrepreneurs is a really lonely thing. And I've seen so many
*  entrepreneurs not know how to make certain decisions. Like, when do you need to,
*  how do you do B2B sales? Right? If you don't know that, it's really hard. Or how do you market
*  this efficiently other than, you know, buying ads, which is really expensive. Are there more efficient
*  tactics to that? Or for machine learning project, you know, basic decisions can change the course
*  of whether machine learning product works or not. And so there are so many hundreds of decisions
*  that entrepreneurs need to make. And making a mistake in a couple key decisions can have a huge
*  impact on the fate of the company. So I think a startup studio provides a support structure
*  that makes starting a company much less of a lonely experience. And also, when facing with these key
*  decisions, like trying to hire your first VP of engineering, what's a good selection criteria? How
*  do you solve? Should I hire this person or not? By helping, by having an ecosystem around the
*  entrepreneurs, the founders to help, I think we help them at the key moments and hopefully
*  significantly make them more enjoyable and then higher success rate. So they have somebody to
*  brainstorm with in these very difficult decision points. And also to help them recognize what they
*  may not even realize is a key decision point. That's the first and probably the most important
*  part. Yeah. Actually, I can say one other thing. You know, I think building companies is one thing,
*  but I feel like it's really important that we build companies that move the world forward. For example,
*  within the AI Fund team, there was once an idea for a new company that if it had succeeded,
*  would have resulted in people watching a lot more videos in a certain narrow vertical type of video.
*  I looked at it, the business case was fine, the revenue case was fine, but I looked and just said,
*  I don't want to do this. I don't actually just want to have a lot more people watch this type
*  of video. It wasn't educational. It's an educational heavy. And so I code the idea on the basis that I
*  didn't think it would actually help people. So whether building companies or work of enterprises
*  or doing personal projects, I think it's up to each of us to figure out what's the difference
*  we want to make in the world. With lending AI, you help already established companies grow their AI
*  and machine learning efforts. How does a large company integrate machine learning into their
*  efforts? AI is a general purpose technology. And I think it will transform every industry.
*  Our community has already transformed to a large extent the software internet sector.
*  Most software internet companies outside the top five or six or three or four already have reasonable
*  machine learning capabilities or getting there. There's still room for improvement. But when I
*  look outside the software internet sector, everything from manufacturing, agriculture,
*  healthcare, logistics transportation, there's so many opportunities that very few people are
*  working on. So I think the next wave for AI is for us to also transform all of those other industries.
*  There was a McKinsey study estimating $13 trillion of global economic growth. US GDP is $19 trillion.
*  So $13 trillion is a big number. Or PWC estimates $16 trillion. So whatever number is large. But the
*  interesting thing to me was a lot of that impact would be outside the software internet sector.
*  So we need more teams to work with these companies to help them adopt AI. And I think this is one
*  thing that will help drive global economic growth and make humanity more powerful.
*  And like you said, the impact is there. So what are the best industries, the biggest industries
*  where AI can help perhaps outside the software tech sector?
*  Frankly, I think it's all of them. Some of the ones I'm spending a lot of time on are manufacturing,
*  agriculture, looking to healthcare. For example, in manufacturing, we do a lot of work in visual
*  inspection, where today there are people standing around using the human eye to check if this plastic
*  pod or the smartphone or this thing has a scratch or a dent or something in it. We can use a camera
*  to take a picture, use a algorithm, deep learning and other things to check if it's defective or not
*  and does help factories improve yield and improve quality and improve throughput.
*  It turns out the practical problems we run into are very different than the ones you might read
*  about in most research papers. The data sets are really small, so we face small data problems.
*  The factories keep on changing the environment, so it works well on your test set. But guess what?
*  Something changes in the factory, the lights go on or off. Recently, there was a factory in which
*  a bird flew through the factory and pooped on something. That changed stuff. Increasing our
*  algorithmic robustness to all the changes that happen in the factory, I find that we run into a
*  lot of practical problems that are not as widely discussed in academia. It's really fun being on
*  the cutting edge solving these problems before many people are even aware that there is a problem.
*  That's such a fascinating space. You're absolutely right. But what is the first
*  step that a company should take? It's just a scary leap into this new world of going from the human
*  eye inspecting to digitizing that process, having a camera, having an algorithm. What's the first
*  step? What's the early journey that you recommend that you see these companies taking?
*  I published a document called the AI Transformation Playbook that's online and taught briefly in the
*  everyone calls on Coursera about the long-term journey that companies should take. But the first
*  step is actually to start small. I've seen a lot more companies fail by starting too big than by
*  starting too small. Take even Google. Most people don't realize how hard it was and how controversial
*  it was in the early days. When I started Google Brain, it was controversial. People thought
*  deep learning near the net tried it, didn't work. Why would you want to do deep learning?
*  My first internal customer within Google was the Google speech team, which is not the most
*  lucrative project in Google, not the most important. It's not web search or advertising.
*  But by starting small, my team helped the speech team build a more accurate speech recognition
*  system. This caused their peers, other teams to start to have more faith in deep learning.
*  My second internal customer was the Google Maps team where we used computer vision to read house
*  numbers from basically street view images to more accurately locate houses within Google Maps to
*  improve the quality of geo data. And it was only after those two successes that I then started the
*  most serious conversation with the Google Ads team. So there's a ripple effect that you showed
*  that it works in these cases and it just propagates through the entire company that this thing has a
*  lot of value and use for us. I think the early small scale projects, it helps the teams gain
*  faith, but also helps the teams learn what these technologies do. I still remember when our first
*  GPU server, it was a server under some guy's desk. And that taught us early important lessons about
*  how do you have multiple users share a set of GPUs, which is really not obvious at the time.
*  But those early lessons were important. We learned a lot from that first GPU server that later helped
*  the teams think through how to scale it up to much larger deployments. Are there concrete challenges
*  that companies face that you see is important for them to solve? I think building and deploying
*  machine learning systems is hard. There's a huge gulf between something that works in a Jupiter
*  notebook on your laptop versus something that runs in a production deployment setting in a factory or
*  agriculture plant or whatever. So I see a lot of people get something to work on your laptop and
*  say, wow, look what I've done. And that's great. That's hard. That's a very important first step.
*  But a lot of teams underestimate the rest of the steps needed. So for example, I've heard this
*  exact same conversation between a lot of machine learning people and business people. The machine
*  learning person says, look, my algorithm does well on the test set. And it's a clean test set.
*  I didn't peek. And the business person says, thank you very much, but your algorithm sucks.
*  It doesn't work. And the machine learning person says, no, wait, I did well on the test set.
*  And I think there is a gulf between what it takes to do well on a test set on your hard drive versus
*  what it takes to work well in a deployment setting. Some common problems, robustness
*  and generalization. You deploy something in the factory, maybe they chop down a tree outside the
*  factory so the tree no longer covers the window and the lighting is different. So the test set
*  changes. And in machine learning, and especially in academia, we don't know how to deal with test
*  set distributions that are dramatically different than the training set distribution. There's
*  research, there's stuff like domain annotation, transfer learning. There are people working on it,
*  but we're really not good at this. So how do you actually get this to work? Because your test set
*  distribution is going to change. And I think also, if you look at the number of lines of code in the
*  software system, the machine learning model is maybe 5% or even fewer relative to the entire
*  software system you need to build. So how do you get all that work done and make it reliable and
*  systematic? So good software engineering work is fundamental here to building a successful
*  small machine learning system. Yes. And the software system needs to interface with people's
*  workloads. So machine learning is automation on steroids. If we take one task out of many tasks
*  that are done in the factory. So the factory does lots of things. One task is vision inspection.
*  If we automate that one task, it can be really valuable, but you may need to redesign a lot of
*  other tasks around that one task. For example, say the machine learning algorithm says this is
*  defective. What are you supposed to do? Do you throw it away? Do you get a human to double check?
*  Do you want to rework it or fix it? So you need to redesign a lot of tasks around that thing you've
*  now automated. So planning for the change management and making sure that the software
*  you write is consistent with the new workflow. And you take the time to explain to people what
*  needs to happen. So I think what landing AI has become good at, and I think we learned by making
*  the steps and painful experiences, what we've become good at is working with our partners to
*  think through all the things beyond just the machine learning model that you put in the notebook,
*  but to build the entire system, manage the change process and figure out how to deploy this in a way
*  that has an actual impact. The processes that the large software tech companies use for deploying
*  don't work for a lot of other scenarios. For example, when I was leading large speech teams,
*  if the speech recognition system goes down, what happens? Well, allowance goes off. And then
*  someone like me would say, hey, you 20 engineers, please fix this. But if you have a system go down
*  in the factory, there are not 20 machine learning engineers sitting around. You can pay your duty
*  and have them fix it. So how do you deal with the maintenance or the DevOps or the MLOps or
*  the other aspects of this? So these are concepts that I think landing AI and a few other teams
*  on the cutting edge, but we don't even have systematic terminology yet to describe some
*  of the stuff we do because I think we're inventing it on the fly. So you mentioned some people are
*  interested in discovering mathematical beauty and truth in the universe, and you're interested in
*  having a big positive impact in the world. So let me ask-
*  The two are not inconsistent.
*  No, they're all together. I'm only half joking because you're probably interested a little bit
*  in both. But let me ask a romanticized question. So much of the work, your work and our discussion
*  today has been on applied AI. Maybe you can even call narrow AI, where the goal is to create
*  systems that automate some specific process that adds a lot of value to the world. But there's
*  another branch of AI, starting with Alan Turing, that kind of dreams of creating human level or
*  superhuman level intelligence. Is this something you dream of as well? Do you think we human
*  beings will ever build a human level intelligence or superhuman level intelligence system?
*  I would love to get to AGI, and I think humanity will, but whether it takes a hundred years or
*  500 or 5000, I find hard to estimate.
*  Do you have- Some folks have worries about the different trajectories that path would take,
*  even existential threats of an AGI system. Do you have such concerns,
*  whether in the short term or the long term?
*  I do worry about the long term fate of humanity. I do wonder as well. I do worry about over
*  population on the planet Mars, just not today. I think there will be a day when maybe someday
*  in the future Mars will be polluted, there are all these children dying. And someone will look back
*  at this video and say, Andrew, how was Andrew so heartless? He didn't care about all these children
*  dying on the planet Mars. And I apologize to the future viewer. I do care about the children,
*  but I just don't know how to productively work on that today.
*  Your picture will be in the dictionary for the people who are ignorant about the over
*  population on Mars. Yes. So it's a long-term problem. Is there something in the short term
*  we should be thinking about in terms of aligning the values of our AI systems with the values
*  of us humans? Sort of something that Stuart Russell and other folks are thinking about
*  as this system develops more and more, we want to make sure that it represents the better angels of
*  our nature, the ethics, the values of our society.
*  You know, if you take self-driving cars, the biggest problem with self-driving cars is not
*  that there's some trolley dilemma and you teach this. So, you know, how many times when you're
*  driving your car, did you face this moral dilemma? Who do I crash into? So I think self-driving cars
*  will run into that problem roughly as often as we do when we drive our cars. The biggest problem
*  with self-driving cars is when there's a big white truck across the road and what you should do is
*  brake and not crash into it and the self-driving car fails and it crashes into it. So I think we
*  need to solve that problem for us. I think the problem with some of these discussions about
*  AGI, you know, alignment, the paperclip problem is that is a huge distraction from the much harder
*  problems that we actually need to address today. Some of the hard problems we need to address today,
*  I think bias is a huge issue. I worry about wealth and equality. The AI and internet are
*  causing an acceleration of concentration of power because we can now centralize data,
*  use AI to process it. And so industry after industry, we've affected every industry.
*  So the internet industry has a lot of win and take most of win and take all dynamics,
*  but we've infected all these other industries. So also giving these other industries win and
*  take most of win and take all flavors. So look at what Uber and Lyft did to the taxi industry.
*  So we're doing this type of thing to a lot of them. So we're creating tremendous wealth,
*  but how do we make sure that the wealth is fairly shared? I think that's, and then how do we help
*  people whose jobs are displaced? I think education is part of it. There may be even more that we need
*  to do than education. I think bias is a serious issue. There are adverse uses of AI, like deep
*  fakes being used for various and fairer purposes. So I worry about some teams, maybe accidentally,
*  and I hope not deliberately, making a lot of noise about things that problems in the distant future,
*  rather than focusing on some of the much harder problems.
*  Yeah, the overshadow of the problems that we have already today. They're exceptionally
*  challenging, like those you said, and even the silly ones, but the ones that have a huge impact,
*  which is the lighting variation outside of your factory window. That ultimately is what makes the
*  difference between, like you said, the Jupiter notebook and something that actually transforms
*  an entire industry potentially. Yeah. And I think, and then just to some companies,
*  when a regulator comes to you and says, look, your product is messing things up,
*  fixing it may have a revenue impact. Well, it's much more fun to talk to them about how you
*  promise not to wipe out humanity than to face the actually really hard problems we face.
*  So your life has been a great journey from teaching to research to entrepreneurship.
*  Two questions. One, are there regrets, moments that if you went back, you would do differently?
*  And two, are there moments you're especially proud of, moments that made you truly happy?
*  You know, I've made so many mistakes. It feels like every time I discover something,
*  I go, why didn't I think of this, you know, five years earlier or even 10 years earlier?
*  And as we see, and then sometimes I read a book and I go, I wish I read this book 10 years ago,
*  my life would have been so different. Although that happened recently. And then I was thinking,
*  if only I read this book when we're starting up Coursera, it could have been so much better.
*  But I discovered the book had not yet been written or starting Coursera. So that made me feel better.
*  But I find that the process of discovery, we keep on finding out things that seem so obvious
*  in hindsight, but it always takes us so much longer than I wish to figure it out.
*  So on the second question, are there moments in your life that if you look back that you're
*  especially proud of or you're especially happy, that filled you with happiness and fulfillment?
*  Well, two answers. One, does my daughter know her?
*  Yes, of course.
*  Because I know how much time I spend with her. I just can't spend enough time with her.
*  Congratulations, by the way.
*  Thank you. And then second is helping other people. I think to me, I think the meaning of life
*  is helping others achieve whatever are their dreams. And then also, to try to move the world
*  forward by making humanity more powerful as a whole. So the times that I felt most happy,
*  most proud was when I felt someone else allowed me the good fortune of helping them a little bit
*  on the path to their dreams.
*  I think there's no better way to end it than talking about happiness and the meaning of life.
*  It's a huge honor, me and millions of people. Thank you for all the work you've done. Thank you
*  for talking today.
*  Thank you so much. Thanks.
*  Give it five stars on Apple Podcasts, support it on Patreon, or simply connect with me on Twitter
*  at Lex Friedman. And now let me leave you with some words of wisdom from Andrew Ng.
*  Ask yourself if what you're working on succeeds beyond your wildest dreams, which have significantly
*  helped other people. If not, then keep searching for something else to work on. Otherwise, you're
*  not living up to your full potential.
*  Thank you for listening and hope to see you next time.
