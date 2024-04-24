---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 2976s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 871
Video Rating: None
---

# BI 015 Terrence Sejnowski: How to Start a Deep Learning Revolution
**Brain Inspired:** [October 24, 2018](https://www.youtube.com/watch?v=l08QbgHIMOE)
*  This is all crazy.
*  This is not what's going to happen and the public is getting hoodwinked by people, extremists.
*  That's a good subtitle for the book, maybe, the public is getting hoodwinked.
*  That's good.
*  Well, a lot of books could go under that heading.
*  Not only is it an exciting time, but I think that many years from now, this era that we're
*  living through right now will be seen as the golden era.
*  This is Brain Inspired.
*  Welcome.
*  This is Paul Littlebrooks.
*  All right.
*  Well, I have now made it possible for you to support the podcast, should you choose.
*  I created a Patreon account, which you can access through the website, braininspired.co,
*  or go directly to the Patreon page, and that's at patreon.com forward slash braininspired.
*  And I got my first supporter, the man who actually strong-armed me into making this
*  Patreon page, Alex.
*  Thank you.
*  So you can support the show at two levels for now, either $2 or $4 per month.
*  That works out to 50 cents or $1 per episode.
*  I don't have any gifts or special offers for you at this time, but if you decide to
*  support the show, I will be able to share things exclusively with you when they become
*  available.
*  Maybe some toy code to play with, or if I write a book or want to release some bonus
*  or special footage and material.
*  Whatever the case, people who support the show on Patreon will be the first to get that
*  special stuff for free or at a discount, et cetera.
*  Plus, my wife will no longer be able to say, I bring home no bacon.
*  Okay, enough of that.
*  The voice you heard at the beginning was indeed the Terence Sienofsky.
*  Yes, that one.
*  I was flattered such a legend would agree to come on the show, so we all got lucky here.
*  Terry has written a book called The Deep Learning Revolution.
*  To say it's an insider's view is a major understatement.
*  Terry was one of a handful of people who basically created AI as we know it today.
*  Since then, the man has never stopped putting out great work in both neuroscience and artificial
*  intelligence.
*  We talk about his book, which I'm waiting for in my mailbox any day now.
*  Our chat made me even more excited to get my hands on the book.
*  We also talk about his online Coursera course with Barbara Oakley called Learning How to
*  Learn and it's the most popular online course ever.
*  Okay, you'll hear I try to trip him up and I ask him about his first published paper.
*  This was in the world of astrophysics, his first love, and it was published in 1969.
*  He immediately launches into a summary of the work like he had just released it yesterday.
*  It's amazing.
*  So I had so much left I didn't get to ask Terry because of time constraint, really so
*  much.
*  So apologies for that, but I think you'll still enjoy and get a lot out of our chat.
*  Lastly, Terry was an early influence on me.
*  Like his book, The Computational Brain with Patricia Churchlin literally helped alter
*  my life path and I tell him as much right at the beginning.
*  And guess what I do?
*  I flub the name of the book.
*  So you'll get to hear that.
*  Really ridiculous.
*  I seriously considered editing that out and splicing in a correction, but I decided to
*  leave in the embarrassing moment.
*  So hope you enjoy hearing my heart jump out of my chest there in a few seconds.
*  But Terry was gracious and he let me live and we had a great conversation.
*  A link to his book and all the other stuff that we talk about can be found in the show
*  notes at braininspired.co slash podcast slash 15.
*  Please enjoy Terence Sienowski.
*  I have a distinct memory I'd like to share.
*  So 20 years ago, I was in an undergraduate at UT Austin, University of Texas, and I was
*  in aerospace engineering major.
*  And that day I had gone to half price books and picked up a couple books and gone to the
*  laundromat and this I distinctly remember the low, the dim yellowish lights of the laundry.
*  And I read this book while my laundry was being done.
*  And the book was called Computational Neuroscience by Patricia Churchland and Terence Sienowski.
*  Actually actually it was the computational brain, but thank you.
*  The computational brain.
*  Yeah, that's right.
*  How can I mess that up?
*  The computational brain.
*  And so that was 20 years ago.
*  And it's actually recently celebrated its 25th anniversary.
*  So congratulations.
*  So that book, reading that book that day actually changed the course of my path toward neuroscience.
*  So I just want to say thank you, Terry, and welcome to the podcast.
*  Wonderful to be here.
*  And also thank you for remembering the book because 25 years is a long time.
*  But in fact, their seeds of the current book that's coming out next week is really contained
*  in that first book.
*  It was all about populations of neurons and how the early work that was being done by
*  with learning algorithms was giving us the ability to create distributed representations
*  in populations of neurons.
*  Very small at the time, like little toy problems.
*  But it was already clear back then that this was a kind of computing that the brain very
*  much looked like the kind of computing the brain could be doing.
*  Yeah, it was a great book and it really did change my path.
*  So I don't really need to introduce you, but just by way of a few tidbits here.
*  So your thesis advisor was John Hopfield of the famed Hopfield Network that helped usher
*  in neural networks from the very beginning.
*  And among a billion other things that you've done, you co-invented the Boltzmann machine
*  with Jeff Hinton, which is one of the earliest actually useful neural networks.
*  And your early work helped drive the transition from the good old fashioned type AI, the symbol-based
*  AI, to the modern statistical data-driven approach that underlies all of the modern
*  current successes of the deep learning networks.
*  You've published over 500 papers and written 12 books.
*  And now you're Francis Crick Professor at the Salk Institute for Biological Studies.
*  So you've done so much and there are so many different directions that we could go.
*  If you'll allow me to, I'd like to start in 1969 though, in the Astrophysical Journal
*  with a paper titled A Theoretical Analysis of Methods of Interpreting Radioline Data
*  for H2 Regions.
*  This was the first paper on your CV.
*  Do you remember the gist of that paper and the conclusions drawn?
*  Oh yes.
*  Oh yes.
*  This is bringing back memories.
*  This is as I was really just getting started at science.
*  I had spent a summer at the National Radio Astronomy Observatory working with an astrophysicist,
*  Robert Jelming.
*  And the problem that we worked on was these are lines from H2 regions.
*  These are hot balls of gas and there's something called the B sub N problem, which is transitions
*  between very high-lying states of hydrogen, like between 109 and 110.
*  Normally we think of the lines that you see in the visible coming from the transitions
*  from the lower orbitals.
*  But when you're up there at 109, it's in the radio region and you can see them in radio
*  telescopes.
*  So that actually was the beginning of my interest in astrophysics and in fact you mentioned
*  that John was my PhD advisor at Princeton.
*  In fact my master's degree was with John Wheeler, who is a black hole fame and general
*  relativity.
*  When I first went to Princeton, this is before any neural networks or the brain or anything,
*  my path was set.
*  I was going to work with John Wheeler and of course no one can predict where one's
*  career is going, but here I am.
*  I didn't predict 20 years ago when I was reading your book that I'd be interviewing you on
*  a podcast or that podcasts would exist.
*  This is nice for me.
*  I want to get to your new book in just a second that's coming out.
*  First I just want to talk briefly about your online course and the book Learning How to
*  Learn.
*  This is a Coursera course, the full title of which is Learning How to Learn, Powerful
*  Mental Tools to Help You Master Tough Subjects.
*  You do the course with Barbara Oakley and it's now the most popular massive online open
*  course to date, which is awesome.
*  I took it, it's great and it's accessible for everyone.
*  Really what it does, it talks about the neuroscience behind how we learn and how to use what we
*  know about neuroscience to learn more effectively.
*  Where did the idea come from to make this course and how did you connect with Barbara
*  Oakley to do it?
*  Well that's a really wonderful story.
*  The background is that I've been a co-director for 10 years of a science of learning center
*  sponsored by the NSF at UCSD, my sister institution.
*  My lab is at the Salk but I'm actually on the faculty also at the University of California
*  in San Diego.
*  Part of the science of learning center is to try to bring our understanding of how the
*  brain develops, how language emerges and there are six centers each looking at different
*  aspects of education and the brain.
*  Ours is the one that really focused more on learning mechanisms.
*  how the hippocampus is engaged when we're learning something, a new fact about the world.
*  The other thing that we tried to do was to interface with schools so we worked very closely
*  with the Price School on campus as a charter school.
*  Our experience was that we were very excited about the science, we wanted to bring them
*  into the classroom but it turned out to be incredibly difficult even with a school on
*  campus and the reason is that there's a tremendous amount of barriers that if you try to go into
*  a school you have to get permissions from all sorts of people.
*  Fortunately the principal Doris Alvarez of the Price School was very open but if you
*  go to a high school in the inner city, forget it.
*  For them it's just another complication.
*  What's worse, if you have the best solution to education, there are 12,000 school districts
*  in the US, you'd have to knock on 12,000 doors so immediately you realize it doesn't scale.
*  What we're trying to do doesn't scale, it might work in one classroom but how do you
*  go from that to hundreds of thousands of classrooms.
*  Here I was, and this is completely fortuitous, I was at a meeting that was taking place at
*  UC Irvine up the road and it was sponsored by the National Academy of Sciences, it's
*  a National Academy Keck Futures Initiative, NACFI, that I actually helped to organize
*  and one of the speakers that I introduced was Barbara and she was telling us the story
*  of her life.
*  It's fascinating, she's a remarkable woman.
*  She flunked her way through math in high school, she really wasn't very good at it.
*  This is chronicled in her book Mind Shift as well, right?
*  That's right.
*  There's another book and another MOOC that came afterwards and that's a follow-up.
*  What I came away understanding from her presentation is that after going off and learning Russian
*  and having adventures in the Arctic fishing trawlers and the army, she really wanted to
*  try to master math and she figured out how to do it on her own.
*  She went back and not just master of math but got a PhD in electrical engineering and
*  is now a professor of electrical engineering at Oakland University in Michigan.
*  What a career trajectory, wow.
*  Talk about being able to confront something that had been bothering her her whole life
*  and actually making a career out of it.
*  In any case, I was so impressed.
*  I had dinner with her and we hit it off.
*  I invited her to come give a talk at our Science of Learning Center which she did.
*  She came and flew in and we thought it would be a great opportunity to invite not just
*  the faculty but high school teachers and students.
*  We had a big auditorium filled with people of all ages and backgrounds and she was mesmerizing.
*  Unbelievable.
*  She had this talent for engaging the audience and she did things that I would have never
*  even thought of doing.
*  For example, to reach the high school students, she used metaphors like zombies.
*  I did notice that zombies are really big in high school these days.
*  She said, if you are having trouble with trying to understand something, you have this mental
*  block, don't beat your head against the wall over and over again.
*  Don't be a zombie.
*  That's what zombies do.
*  Get up, walk around, do something else.
*  Just free your mind up and your subconscious is going to work on it and you come back to
*  it a half hour later and it will be much clearer.
*  In any case, what became clear to me was that she was intuitive in terms of her understanding
*  of the learning process.
*  She was very good at communicating and what was missing was a scientific understanding
*  of the mechanisms underlying her experiences and the practical advice that she was giving
*  to the students.
*  It was all good but she really couldn't explain to them why it was good.
*  So over the period of the next six months or so, we put together this MOOC.
*  Here's another remarkable thing about Barbara.
*  If you go online, there are like 10,000 MOOCs now and the typical MOOC is a talking head.
*  This is a professor who has been giving the same course for the last 10 years and they're
*  an automatic pilot and it could be a very good lecture and I don't think we're
*  wrong with the material or anything, it's just that it really is soporific.
*  It doesn't grab your attention and in fact, much less so than if it was a classroom because
*  in the classroom at least, the person is walking around and they have the opportunity to interact
*  with the audience and with the students in the classroom.
*  But if you're doing a MOOC, it's like talking into a vacuum.
*  You don't have any feedback.
*  It's very difficult.
*  It's actually much more difficult than giving a classroom lecture in my experience.
*  For example, I was giving a taping, one of my MOOCs and I launched with this joke that
*  I thought would be in a regular lecture, get some reaction.
*  That's silence and you have no idea how frightening that is because you have no idea
*  did they get the joke, should I go on in the same direction, what's going on here.
*  That's the problem.
*  Here's what Barbara did which is really remarkable.
*  She realized that if you – and we were aiming at high school students by the way, the people
*  who are really in the business of learning, they go to work every day to learn.
*  She realized that we needed to engage them using all the tools that are available for
*  animating the concepts, the metaphors and she did something which really was brilliant.
*  It's called green screen and it's what weathermen use when they're pointing to
*  the hurricane in Florida.
*  There is actually a green screen behind them and it's being projected electronically
*  into the audience and that means you can put anything up.
*  You can put animations up, you can put pictures, movies, anything you want and so that's
*  what she did.
*  She did it in her basement.
*  Her husband was her film editor.
*  She bought a high-res camera, she bought a software to do some video editing and she
*  was the one who did all of the cuts and the animations and everything that you saw on
*  that MOOC, Learning How to Learn, was done in her basement for $6,000.
*  I had no idea.
*  What she realized again intuitively is that motion really captures your attention.
*  We injected humor and that is incredibly important for emotional engagement.
*  You need to get people to laugh, you need to get people to be interested in terms of
*  what they're thinking but what they're feeling.
*  She was a master at that and I think that those are all the reasons.
*  We don't know for sure but I think it really helps to get an audience that not only I think
*  benefited but actually was super enthusiastic.
*  I get fan mail every day.
*  You said that you guys created the course aimed at teens but the majority of your audience
*  has been professional adults, correct?
*  That's the shock.
*  This is true not just of our MOOC, it turns out to be all MOOCs.
*  Of the 3 million learners, only 1% were from that target audience, below 19.
*  The biggest demographic was 25 to 35 and half of them are college educated.
*  We're talking about a group that is in the workforce, they've left school, they probably
*  have families and mortgages but they're discovering that they need new skills in order to be able
*  to do their job because the day you graduate, basically what you've learned is obsolete
*  because what's going on right now is moving so quickly that the schools just can't keep
*  up with it.
*  The beauty of the MOOC is that it allows you to do that on your own time.
*  You don't have to go back to school, you don't have to interrupt your life, you can
*  take whatever course you need for whatever skill you need.
*  It's a perfect thing.
*  The MOOCs really aren't a replacement for schools.
*  They're basically I think going to evolve into a lifelong learning delivery system so
*  that people can continue to learn for their entire life as they need new skills.
*  That's right.
*  We failed to reach the audience we were aiming at and then someone pointed out the obvious
*  to us, look, these poor students, they spent all day in classrooms learning and what you
*  want them to do is to take another course?
*  That's the last thing they want to do.
*  At night?
*  Come on.
*  They're doing homework, they've got a life.
*  We realized that this was the wrong way to go about it.
*  We actually created a whole new MOOC that is in conjunction with the University of Arizona
*  that's going to go online very soon.
*  Is it zombie free?
*  No, they're zombies but it's filled with metaphors.
*  We made a huge effort to really create a metaphorical world that they could understand
*  things on their own terms and we actually wrote a book that just came out in August
*  learning how to learn for kids and it's already bestseller on Amazon.
*  It is aimed at the high school 12 to 14 by the way, middle school.
*  That's the key age at which a lot of students are turned away by math because they hit
*  algebra basically.
*  We really wanted to help those students and we're going to do it through the teachers.
*  The idea is that the teachers have this text that the students can read because it's written
*  for them.
*  By the way, we added another author who is a child book, a writer for children's books
*  which is a special talent I don't have.
*  What words are you going to use and how you pitch things?
*  We have a very talented artist who drew cartoons for us to make it come alive.
*  This book is I think is going to be our entrance to that age group.
*  Aside from all the techniques that you guys have developed and communicate in the course,
*  what is your secret to accomplishing so much?
*  Do you have a favorite productivity tool or strategy that you'd recommend to people?
*  Well, it helps to have a big lab and I have a fantastic lab manager.
*  I really depend a lot.
*  I expect a lot from people in my lab and they are tremendously supportive of me.
*  You can't do all that on your own.
*  I could never have done this MOOC without Barbara.
*  I'm also the president of the NIPS Foundation, Neural Information Processing Systems.
*  Last year in Long Beach, we had 8,000 people.
*  I couldn't have run that meeting on my own but Mary Ellen Perry, my lab manager who is very capable
*  and really works very closely with me and with the sponsors and the academics.
*  We really have a team.
*  That's the secret is to have a really first rate team for every project.
*  It's not just practical projects but it's also for scientific projects.
*  A lot of the research that we do in the lab is really working with people from different backgrounds.
*  That's important too by the way.
*  Everyone lives in a silo.
*  If you're a physicist in a physics department, you're in a silo.
*  The excitement these days isn't in the silos although some nice things are happening in physics.
*  If you really want to have breakthrough advances, then you need to bring together people who have different backgrounds.
*  People from mathematics, cognitive science, bioengineering, neuroscience.
*  The graduate students and post-doctoral students come from all those backgrounds.
*  It's fantastic. It's like having a little university.
*  We discuss things and everybody has a different perspective.
*  That's how you make the breakthroughs.
*  You get that synergy between the different people that have very different backgrounds.
*  Radical collaboration. That's good.
*  Your new book, which it's been a long time since you've written a book by yourself,
*  speaking of getting things done.
*  The book is called The Deep Learning Revolution.
*  By the time this podcast airs, I should have gotten my copy because I had pre-ordered it on Amazon.
*  I think the 23rd of October is when it's supposed to ship.
*  That is the date. It's actually in the warehouse already.
*  I have an advanced copy. It's a beautiful book.
*  You'll be pleased. I was incredibly proud to hold it.
*  It's just such a beautiful object. Full color.
*  The paper has a good feel to it.
*  They did a great design job. MIT Press is fantastic.
*  I have worked with them for over 30 years and I've always been happy with their product.
*  They're very, very good.
*  The book itself was a reaction a couple of years ago when, as you know, this deep learning hit the public press.
*  I said, wait a second now. This is just renaming something that I've been doing since the 1980s.
*  All the learning algorithms that are being used today were first pioneered by, you mentioned, the Bolesaw Machine.
*  Jeff Hinton and I worked on that back in 1983. Backpropagation came a few years after that.
*  This is basically taking what we had done back then and just scaling it up.
*  Creating more units. Back then, we had tiny networks with a few hundred units, a few thousand connections, one layer of hidden units.
*  Now we have millions of units, hundreds of millions of connections.
*  In the brain, there were 12 layers in the hierarchy in the visual system, but now people have 100 layers in some of the speech recognition networks.
*  This is really amping up what we had done by a million times.
*  I thought that they don't seem to understand the history here.
*  They think that it was all created full blown five years ago at a NIPS meeting.
*  That was part of my motivation.
*  The real motivation was I started reading articles in the newspaper about how, oh my God, this AI is going to put people out of work.
*  It's going to replace humans. We're going to become obsolete.
*  This is all crazy. This is not what's going to happen.
*  The public is getting hoodwinked by people, extremists.
*  That's a good subtitle for the book. The public is getting hoodwinked.
*  A lot of books could go under that heading.
*  This is another thing. I said, they should have access to something that is more sensible.
*  By the way, there is the other extreme, which is the people who said, oh, this is utopia.
*  We're going to be able to solve all the problems and humans are going to have this incredible new life that they won't have to do any hard work.
*  Everything will be beautiful and the medical diagnosis will happen automatically and blah, blah.
*  Those are the two extremes that people seem to gravitate toward and neither of them is the reality.
*  Here's an example of why that is.
*  The reason is that humans just cannot imagine the impact that a new technology will have.
*  I'll give you an example.
*  Back in the 1990s when the internet went from a way for academics to exchange information,
*  which was, they used to be called ARPANET back when I was at my first job at Johns Hopkins.
*  When it went commercial, suddenly you had web browsers, companies went online and started selling things.
*  Amazon was just fledgling back then.
*  Could anybody have imagined the impact that the internet was going to have on everybody's life today, 30 years later?
*  The reality is nobody could.
*  It's affected everything, every aspect of life.
*  It's music, commerce, taxis, social media, politics.
*  It's astonishing.
*  No science fiction writer I think was imaginative enough to figure this out.
*  I think that we're in a similar position here.
*  We have a mechanism now that can amplify human cognition in the same way back 250 years ago
*  in the industrial revolution, we created machines that can amplify physical power.
*  With a tractor, one human can plow 100 times more fields than a single human with a horse.
*  Now it's going to be the case that a single human is going to have much more impact through these cognitive appliances.
*  This is not a robot that's going to go around replacing you.
*  This is basically a way to amplify what you can do and how smart you can be.
*  The mantra in the book is AI will make you smarter.
*  Very good. You're obviously passionate about it.
*  I skimmed the table of contents and you can read some of the stuff when you look at the book online.
*  I came across that you had written the first draft of it within just a couple weeks. Is that right?
*  This was an epiphany I had.
*  I like to go hiking every year with friends to different parts of the world.
*  I just came back from Norway at the end of September, which was a fantastic Lofoten,
*  which are islands off the northwest coast of Norway, just fjords coming up from the ocean.
*  It's just spectacular.
*  I was hiking again in the fall in the Pacific Northwest in the Olympics.
*  A couple weeks clears your mind and you really begin to start thinking about the past and you start thinking about the future.
*  I realized that I have a story to tell.
*  I started just in my mind putting together some chapters and I said,
*  Hey, this could be fun.
*  When I got back, I had a lot of energy because after a couple weeks of hiking, you're in good physical shape and your mind is clear.
*  I just said, I'm just going to sit down and I'm just going to start writing.
*  Literally in two weeks, I had a first draft.
*  It's a completely different book from the one that I have now, but already I could see how it was going to play out.
*  It was going to have three parts.
*  The first part was about the past.
*  This is an artificial intelligence past.
*  The middle is going to be artificial intelligence today.
*  The third part is going to be artificial intelligence in the future.
*  This is the Christmas story.
*  It's also the classic three act play.
*  Exactly right.
*  In fact, as I started writing it, I found a voice which was very comfortable for me.
*  It's as if it was a personal narrative.
*  I'm there.
*  I tried to write it in such a way that a reader could put themselves there in the 1980s.
*  What was it like?
*  What was going on in the world?
*  Who was getting all of the publicity?
*  Who was working together?
*  How did they interact?
*  These are my friends.
*  I wrote about it the way I saw it.
*  I think that really put a different character.
*  It's not a book that's meant for the experts.
*  It's a book that's meant for a general audience.
*  I think experts can get a lot out of it too because of the fact that there's a lot of technical stuff in it.
*  That's not the heart of it.
*  The heart of it is a personal story.
*  It's about science.
*  How is science engineering done?
*  To the public, what's the image of science?
*  There's a mad scientist.
*  There's some genius, the Einstein.
*  It's all distorted.
*  Those are extreme metaphors for what's really going on.
*  Science is put together by humans just like everybody.
*  We have brilliant scientists and we have plotters and we have people who are really good at writing textbooks.
*  It's the whole range.
*  You need them all, but the creative part of science is ultimately it's a group activity.
*  It's not like you have one genius who creates it and everybody follows it.
*  That's not my experience.
*  I think that is very rare.
*  Occasionally it might happen like with Einstein, but I think that the traditional scientific enterprise is won by human beings with the same strengths and weaknesses of all human beings everywhere.
*  Somehow we manage to come together in teams.
*  This is the key.
*  It's a social enterprise.
*  What we're doing is through interactions with each other, sharing ideas, helping each other.
*  That's how breakthroughs are made.
*  That's what happened back in the 80s.
*  I was surprised actually.
*  I was recently reading Stephen Johnson's book, Where Good Ideas Come From.
*  He talked about some studies that were done in labs about how innovations take place.
*  The highest rate of innovation essentially took place during lab meetings where everyone's sharing ideas across the table, which was a little surprising to me.
*  Isn't that interesting?
*  That's my experience too.
*  I had no idea that he wrote about it.
*  Why is that?
*  Here's the reason.
*  My perspective is that it's like you're having a dialogue with a single collective of minds that are all focusing on a problem.
*  This is the other thing.
*  This comes across as another study that was done on creativity in industry.
*  In order for this to happen, this kind of groupthink, there has to be trust.
*  In other words, someone has to be willing to say what they think even though it may sound crazy or they can't be afraid that people are going to laugh at them.
*  When you come up with a new idea, it's always the case that it's not what anybody else thought of.
*  Therefore, people who don't know you might laugh at it or pooh-pooh it because it's hard to be open like that.
*  I think the idea of a lab meeting is that you have a lab that is working together and they trust each other.
*  If they don't, then you don't have a good lab.
*  Good.
*  I've watched you on a talk.
*  You've expressed how great it is right now that we have two things simultaneously going on.
*  We have the massive success in deep networks, in AI, and we have these new powerful tools being developed in neuroscience.
*  In your estimation, is this the most exciting time to be studying how brains work?
*  Not only is it an exciting time, but I think that many years from now, this era that we're living through right now will be seen as the golden era.
*  The golden era when we for the first time had the tools that we needed to make progress.
*  I'm not sure how we still haven't scratched the surface of the complexity of the brain.
*  At least we now have enough tools, and by tools I mean not just electrodes and optical recording,
*  but analytical algorithms that allow us to analyze the big data that's being generated.
*  Here's something that is a little bit of an interesting feedback loop here.
*  NIPs, Neural Information Processing System, was really born out of the neural network explosion that took place in the 80s,
*  and I've already alluded to the learning algorithms that we developed back then.
*  We didn't know it, but what we were really doing was creating a whole new field of machine learning.
*  That is to say, in statistics at the time, the way that you made progress was by working with very tiny models
*  with a few parameters and proving theorems about when it converged, some system for fitting the data.
*  Here we are naive. We're talking about let's try to understand how the brain with 100 billion neurons
*  and 10 to the 15th parameters, how are you going to deal with that amount of complexity?
*  It's only 84 billion neurons. Come on.
*  When I say 100, I mean plus or minus, 20%. Nobody has actually counted every neuron.
*  Actually, I get into arguments with my students about this. Actually, the number varies with the size of your brain.
*  Some people have bigger brains, some people have smaller brains. This is not a single number.
*  In any case, here we are. Who came to NIPS? This is really fascinating.
*  Those first few years, we only had 300 or 400 people show up, but they were people coming from areas that had never interacted before.
*  We were talking about physicists, neuroscientists, cognitive scientists, mathematicians, computer vision people,
*  speech recognition people, natural language people. What was common to all of them was that they were trying to tackle
*  really difficult problems, very high dimensional problems, and they weren't making much progress with the traditional tools that were available to them in statistics.
*  I remember in that era, the experts kept telling us that we were wasting our time. Why?
*  Number one, we don't have enough data. If you want to develop a statistical analysis tool that is going to learn from data,
*  then you only have 100 images. How are you going to constrain or overfit with your network that has 100,000 connections parameters?
*  Then the optimization experts, what they told us was that, oh, forget it. If you're crazy, you're going to get caught in local minima.
*  Everybody knows that you have to have convex optimization function, and otherwise, you're toast.
*  We were naive. We were young. We went ahead anyway. We just ran it, and it worked. We didn't understand why it worked.
*  We now know now that the reason is that when you're dealing with these high dimensional spaces, it looks very different than a one or two or three D space
*  where you have mountain valleys and local minima. If you're in a million dimensional space, they're all saddles.
*  You have a half a million going up and you have a half a million going down, so you always have an escape route.
*  No one understood this back then because no one had really tackled high dimensional problems before.
*  Interestingly, a couple of people from statistics did. Leo Breiman was one of our board of trustees very early on,
*  and he was an expert on trying to tackle these problems, but he was in the minority back then.
*  I really appreciated him very much because he gave us a real perspective that what we're trying to do wasn't completely crazy.
*  It's really interesting. He told me he felt more affinity with the NIPs group than with his own affinity group in statistics.
*  He really understood what we're trying to do, but back then, we just couldn't scale it up.
*  Computers were really slow by today's standards, and so the real discovery was that we were able to do it.
*  The real discovery that was made five years ago, and this is something nobody I think could have predicted 30 years ago,
*  is that of all the algorithms in AI, this is the only one that has scaled by a factor of a million.
*  Typical AI algorithm is combinatoric, which means that it blows up exponentially at some point and means you have a ceiling.
*  But if you have an algorithm like Backprop, which is linear in the parameters, basically it just scales beautifully.
*  It's all parallelized, so it goes beautifully on the GPUs.
*  Here's the real reason. The scaling and because of the fact that the architecture, once you've tuned it up and once you have optimized it,
*  which is what Jan LeCun did with convolutional neural networks over the period of 20 years,
*  the very same architecture could be applied to many problems. You don't have to be a domain expert.
*  That means that if you have something that works for speech, you have to adapt it, but it can be used for natural language processing.
*  It could be used for object recognition images, captioning images. All these difficult problems in AI could be attacked if you have enough data.
*  We're living in an era of big data, and that's really where I think everything comes together.
*  That's why it was a convergence. To go back to your other comment, isn't it ironic today that neuroscientists are now using the machine learning algorithms
*  that we developed in NIPS over the last 30 years? Not just deep learning, by the way, they're using it now, a few labs.
*  But support vector machines, which is really hot in the 90s, is now being used routinely by brain imaging people.
*  That's how they decode their brain data. All of these algorithms that were developed in the machine learning community are now helping neuroscientists
*  understand the brain that were originally inspired by the brain. I find it really...
*  You're back. You're back as well. Sorry. I think we had a dropout. Yeah, we did. Sorry, we got cut off there.
*  I was going to say that we were talking about this loop, the irony of the beautiful loop of the machine learning tools being used in neuroscience now.
*  Deep learning has had huge successes and in all these different fields, like you say.
*  But lately it's gotten some backlash, some criticism, because it's seemed to be such a small part of what we will eventually need to achieve general AI.
*  I'm just wondering your thoughts on general AI and getting there and the role of deep learning in that.
*  Right. Let's put things in perspective. I have a chapter on this, by the way.
*  If you take the biggest deep learning network today, it would fit into a cubic millimeter of cortex.
*  Each deep learning network is a domain expert in one problem. It's very narrow. It's called narrow AI.
*  But the beauty is though that in the brain, which has hundreds of thousands of such deep learning networks in it, you have to create a system.
*  It's another higher level of organization, which is in the computer is called an operating system.
*  The operating system has to keep track of all the subroutines that are going on, demons and scheduling.
*  It's an interface between the applications and the hardware, and it's invisible.
*  What we don't know yet is what is the operating system of the brain.
*  Ultimately, if you want human level intelligence, you're going to have to figure that out.
*  Ultimately, I think what will evolve in the world of AI is that all of these successes, which are very narrow, are going to eventually have to be integrated together into a broader system that is able to handle routing of information, decision making.
*  That's beginning to happen, by the way. For example, in AlphaGo, in addition to deep learning networks, there was also a basal ganglia, that is to say reinforcement learning algorithm, temporal differences, which was a loop with the cortex.
*  That's an algorithm that also goes back to the 80s, Rich Sutton.
*  We now know that dopamine neurons in vertebrate brains and also neurons even in insect brains that do conditioning, running on dopamine, are doing reward prediction error, which is the key to understanding how to develop a value function that allows you to make decisions, a sequence of decisions, to reach a reward, to reach your goal.
*  What I think is going to happen over the course of the next few decades is as we learn more about the brain and more learning algorithms that nature has developed, they're going to be integrated into an AI system that will become more and more autonomous and have higher capabilities.
*  Eventually, we might reach human level intelligence, but I don't think that's necessarily the ultimate goal.
*  I think the ultimate goal is to understand the human brain.
*  I think AI is going to help us do that.
*  That's the beauty.
*  Why do I say that?
*  Here's where NIPS is going and it's where everybody is going.
*  Everybody says, well, look, it's like a black box.
*  You have something that solves the problem, but you don't know how it solves it and how can you trust it if you can't solve it?
*  My immediate response is you have a brain, you use it.
*  Do you understand how it works?
*  No, but you trust it within limits.
*  That's where we are.
*  However, we can go much farther because it turns out these deep learning networks are not black boxes.
*  They're white boxes.
*  They're completely accessible.
*  We have access to every connection, every parameter, every input, every activity pattern of every input.
*  If we can't understand mathematically from an engineering and analytical perspective how these devices work, then we would never understand the brain.
*  What's happening now at NIPS is that we're getting the best mathematicians coming in using algebraic topology to understand the surfaces of the cost function.
*  There are these adversarial examples that show that by just tweaking a couple of inputs, by putting in small changes, you can hit a boundary.
*  Wow, what's that telling us about the geometry?
*  Now we're in this high dimensional space.
*  This is a completely new world now that mathematicians have jumped into.
*  I think what will come out at the end is a theory of learning in these very high dimensional systems of which the brain is one of many, many systems.
*  We know there are many learning algorithms that take you to the same place, so why not the brain?
*  That will give us a theory for learning in the brain.
*  That's great.
*  Well, I know that I'm stretching your time thin here.
*  I just want to say thanks for your contributions and I appreciate your time today.
*  Good luck and congratulations on the book.
*  I'm excited to get my copy.
*  I have one final question.
*  If you had to be cryogenically frozen today?
*  The minimum answer here is one day.
*  When would you want to be thawed?
*  Okay.
*  I haven't thought about that.
*  Let me think about it.
*  But I have to say that here's a heuristic that I've used, which is take the minimum amount of time that you would do it.
*  And I say the minimum would be 10 years.
*  Oh, okay.
*  And take the maximum that you would be willing to live with.
*  And let's say that's 100 years.
*  So take the geometric mean and that's a square root of 1000.
*  So we're talking about like 33 years.
*  So that's my answer.
*  33 and a third years.
*  All right.
*  So now he's heuristic.
*  I love it.
*  Thank you.
*  Thanks for your time.
*  I appreciate it.
*  You're welcome.
*  It was a lot of fun.
*  And I appreciate your letting me have this opportunity to be part of your podcast.
*  Okay.
*  Awesome stuff.
*  Remember, if you want to support the show, find my Patreon link on the website, braininspired.co.
*  You can find me on Twitter as well.
*  I am at PG Mid.
*  Next week, I'm talking with Ryota Kanai, who is working on creating artificial consciousness.
*  So no doubt that will be a fun conversation.
*  Until then, thanks for listening and thank you for your support.
*  See you next time.
