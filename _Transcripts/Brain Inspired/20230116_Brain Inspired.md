---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5712s
Video Keywords: []
Video Views: 3368
Video Rating: None
---

# BI 158 Paul Rosenbloom: Cognitive Architectures
**Brain Inspired:** [January 16, 2023](https://www.youtube.com/watch?v=I36y3YJLFU0)
*  It has unfortunately always been somewhat of a fringe activity both in psychology or
*  cognitive science and AI, although it captures kind of the original motivation for AI as
*  it was started back in the 1950s.
*  I want to look for the deep underlying generalities and see how to get this wide range of phenomena
*  out of the combinations of a small number of ideas.
*  I mean, if you look over the history of AI or probably in science in general, there are
*  always booms when something interesting happens.
*  And they always asymptote out.
*  But you can never tell when or why or how high.
*  This is Brain Inspired.
*  In the early 1980s, Paul Rosenblum, along with John Laird and the early AI pioneer Alan
*  Newell, developed one of the earliest and best known cognitive architectures called
*  SOAR.
*  A cognitive architecture, as Paul defines it, is a model of the fixed structures and
*  processes underlying minds.
*  And SOAR was aimed at generating general intelligence.
*  It's been 40 years since then, and Paul is now Professor Emeritus of Computer Science
*  at the University of Southern California.
*  And he doesn't work on SOAR anymore, although SOAR is still alive and well in the hands
*  of his old partner, John Laird.
*  He did go on to develop another cognitive architecture called Sigma.
*  And in the intervening years between those projects, among other things, Paul stepped
*  back and explored how our various scientific domains are related and how computing itself
*  should be considered a great scientific domain.
*  And that's in his book On Computing, The Fourth Great Scientific Domain.
*  He also has helped develop the common model of cognition, which is not a cognitive architecture,
*  but instead a theoretical model meant to bring together what everyone in the field agrees
*  are the minimal components for a human-like mind.
*  The idea is roughly to create a consensus within the cognitive architecture community
*  for a shared language and framework, so that whatever cognitive architecture you work on,
*  you have a basis to compare it to and can communicate effectively among your peers.
*  So all of what I just said and much of what we discuss in this episode can be found in
*  Paul's memoir called From Designing Minds to Mapping Disciplines, My Life as an Architectural
*  Explorer.
*  And that can be found online, and I link to it in the show notes at braininspired.co
*  slash podcast slash 158.
*  And I will say the memoir is an excellent read to learn a lot of science and history,
*  but also to learn about a very self-aware and self-reflective scientist.
*  And that would be Paul Rosenblum.
*  For our kids, only you can prevent forest fires.
*  And only you can keep this podcast alive by supporting it on Patreon, where you'll get
*  full episodes and you can join our Brain Inspired community.
*  Go to braininspired.co to learn more about that.
*  And thank you to my Patreon supporters.
*  All right, here's Paul.
*  I thought we might start with a quote from your, is it a living memoir?
*  Is that how you refer to it?
*  Yes, it is living in the sense that I'm constantly updating as I think of more things.
*  It's actually been submitted to a journal, in which case if it's published, then it will
*  get frozen at that point.
*  But so far, I keep updating it.
*  The memoir, unless because on the one hand, I see the title From Designing Minds to Mapping
*  Disciplines, My Life as an Architectural Explorer, but then it seems like an alternative title
*  might be, oh, I forget, something.
*  Oh, yeah, the Search for Insight.
*  Which one are we going with?
*  I actually started with that.
*  Oh, you did?
*  But decided that was a bit too generic.
*  And I had to be a little more explicit about the nature of what I've been doing in terms
*  of the kind of topics I've worked on and in my research methodology.
*  Well, I really enjoyed the memoir.
*  It reads very easily.
*  And I guess as a memoir does, it explores both your scientific career, but also some
*  very personal reflections and personality, parts of your personality that have shaped
*  your career and your thought process.
*  So I highly recommend it to people.
*  Let me start with this quote here.
*  One of the things I've realized about myself over the span of my career is that I am attracted
*  much more to thought provoking novelty than to rigorous methodology.
*  Perhaps this makes me inherently pre-scientific or non-scientific, but I get little thrill
*  from either formalization or precision.
*  So that's the quote.
*  And you know, you characterize yourself, as is in the title, as an explorer.
*  And that essentially is what you have been doing throughout your career.
*  And you also state in the book how throughout your career, you've kind of been slightly
*  outside the mainstream areas of like, you're slightly outside of artificial intelligence,
*  you're slightly outside of cognitive science, and that you've always been more or less part
*  of a smaller research community.
*  So I wanted to ask you about that first.
*  I mean, do you think all these things are related, the exploration aspect and your inherent
*  pre-scientific or non-scientific approach?
*  Well, that approach fits fairly well with the area in which I have kind of been driven
*  to work, which is to look at architectures of mind or what we call cognitive architectures.
*  It is, unfortunately, always been somewhat of a fringe activity, both in psychology or
*  cognitive science and AI, although it captures kind of the original motivation for AI, as
*  it was started back in the 1950s.
*  But most people quickly backed off to studying parts of minds where they could study them
*  carefully and where they could measure things and make progress in knowable ways.
*  But I've always cared about the big problem.
*  And to me, that's been more of an exploration activity than it has been kind of careful
*  experimental activity.
*  Though you certainly do experiments at times when you're looking at various parts of it
*  and when you're looking at how parts fit together and so on.
*  So I think both kind of the way I think and the problem I chose to work on fit together
*  quite naturally.
*  One of the people that you were influenced by and worked with and under is Alan Newell.
*  And he wrote the book Unified Theories of Cognition.
*  He was at the beginning, like you just mentioned, of artificial intelligence.
*  But then he went on to get interested in these kinds of cognitive architecture problems.
*  And I wanted to ask you, you know, just how I mean, you write about him in the book.
*  And so people can always read the memoir, or I guess it's a journal article.
*  I thought it would be a book.
*  Right now.
*  Well, it's about 80 pages, a little short for a book.
*  But we'll see how it ends up.
*  Anyway, my philosophy was to write what you want to write and then figure out how to publish
*  it afterwards.
*  That's right.
*  And actually, at the end of the book, I think that's one of your is that one of your 28
*  maxims?
*  I'd have to it is.
*  Yeah.
*  Okay.
*  Yeah.
*  So that was really cool, too.
*  That's a lot of maxims, by the way.
*  And Alan Newell had three maxims.
*  Right.
*  So so it might have been more of those for the ones I captured.
*  Oh, right.
*  Okay.
*  Well, his weren't formalized.
*  You kind of captured those in your own words, right?
*  Yeah.
*  Yeah.
*  So what kind of influence did Alan Newell have on you?
*  I mean, professionally, but also personally?
*  Um, so Alan was kind of an amazing guy.
*  So he was clearly one of the founders about AI and cognitive science.
*  But he was also one of the founding figures in computer architecture and in human computer
*  interaction.
*  He had major books that helped found both of those fields.
*  I first got to know him a bit when I was visiting various universities to try to figure out
*  where to go for graduate school.
*  And so I then visited Carnegie Mellon.
*  I had a chance to meet with him.
*  And I was just kind of impressed with his whole vision and enthusiasm for for the path.
*  That's one of the main reasons I ended up going to CMU and trying to work with him.
*  But in AI, he had this he had this grand vision of how to build, how to go about building
*  mines.
*  It started with a number of principles that he was heavily involved in in kind of defining.
*  One of them was the notion of physical symbol systems, where a symbol is a pattern that
*  can be combined into expressions.
*  So you get this combinatoric nature.
*  They can designate or represent things and they can be interpreted so you can use them
*  as basis for programs and things like that.
*  So symbol systems are one way of viewing general purpose computing.
*  Computers are, in fact, in general, simple systems of a particular sort.
*  So that's one of the kinds of ideas.
*  There is the notion of production or rule based systems, which are these local reactive
*  bits of memory, which can add incrementally and that can execute when the situation is
*  appropriate. And so that was kind of a model for memory.
*  Then there's notion of problem spaces or searches as a way of structuring both kind of
*  decision making and how one thinks about the consequences of decisions.
*  So projects into the future and looks at alternatives.
*  And then there was also this notion of unified theories of cognition or cognitive
*  architectures, a way of putting these together.
*  And the earliest kind of major architecture I worked on was so I'd worked on one of my
*  own a little bit earlier than that that I mentioned in the memoir.
*  Zaps, XZaps, Zaps.
*  Zaps, yeah, XAPS.
*  Which I got started when I was visiting grad student psychology at UC San Diego.
*  That's a whole other story.
*  But in the early years of SOAR, we we essentially found ways of putting these ideas of
*  symbol systems and problem spaces and rule systems and kind of learning by practice
*  mechanism that I developed to my thesis into an architecture that could combine those
*  in all sorts of interesting ways and produce a range of phenomena people hadn't been able
*  to do before within a single system.
*  So that was the kind of thing that excites me about going after these kinds of
*  architectures. How can you find a small set of very general mechanisms that when you put
*  them together can produce kind of the range of human like intelligent behavior?
*  And before we move on, we're going to talk about more about SOAR and then later your
*  cognitive architecture, Sigma.
*  But, you know, how did Alan affect you personally?
*  Was he kind of a playful personality, it seems like?
*  Um, I think you'd say he was.
*  He was not an overly serious person, though he was totally committed to his work.
*  He worked incredible hours.
*  He worked like 60, 70, 80 hours a week on the research, and then he'd spend another 30 to 40
*  hours working on the communities around him.
*  So both the research community and the community at Carnegie Mellon.
*  So he was kind of totally committed to the stuff he was doing, but was always cheerful.
*  He was a happy person.
*  To me, he was kind of an ideal of a researcher in terms of how to work with people, how to
*  work with your communities, how to do your research, how to set large problems and be
*  committed to them over the long term, how to support everyone around him.
*  So to me, he was kind of an inspiration, an ideal kind of second father figure.
*  He clearly got me started on kind of the research path that influenced most of my career.
*  So he was a huge influence on my life and first kind of an advisor and mentor and then a
*  collaborator and friend over a number of years afterwards when we continued working on the
*  SOAR project after both John Laird and I had graduated.
*  Was he an explorer like yourself or would you consider him more of a well, I'll let you
*  describe it?
*  I think so. I don't know if he would describe himself that way.
*  He was clearly an innovator.
*  He invented a whole bunch of things that have influenced many scientific fields.
*  He believed certainly in the scientific method and we certainly did experiments.
*  But much to your chagrin.
*  No, not really. I mean, I was happy to do them.
*  I just realized they didn't give me the joy that certain of the things did.
*  But much of the early phases of Aon Cognor science were exploratory.
*  And even if we didn't say that explicitly, I think it was a very interesting idea.
*  I didn't say that explicitly.
*  They were the fields were wide open and there were so many important problems to tackle
*  that there often wasn't time to tie down every loose end in something before you went out to
*  something else.
*  So you're often thinking, trying to think big and thinking about problems no one had thought
*  about before.
*  So it was kind of inherently exploratory.
*  And I picked up that as part of the culture, even though by the time I got to the field in
*  the mid 70s, I guess the field had been around for 20 years or so.
*  But A.I. cognitive science was still not quite invented.
*  But but there still was this notion of there's this huge world of intelligence to go out
*  there and discover and what can we find out about it?
*  What can we formalize?
*  And at least to the extent of being able to create programs that behave that way.
*  So the kind of formalism we tend to think about was a procedural notion, not creating
*  theorems and proofs, but creating programs that would actually embody the ideas that we
*  were considering.
*  So you had I think it's about a 10 year hiatus where you had been working on SOAR, one of
*  the cognitive architectures that we'll discuss here in a second.
*  And then later you came back to begin and work on what became known as Sigma, which was
*  is your newest and ongoing cognitive architecture.
*  But during your 10 year hiatus, you kind of went even grander picture and almost meta
*  science and looked at theories of computing and how computing relates to other disciplines.
*  And then you came up with something called dichotomic, dichotomic maps.
*  Is that right?
*  I think that's dichotomic.
*  But I'm not sure.
*  Dichotomic. Oh, man.
*  Let me say that over.
*  Yeah, like dichotomic.
*  Dichotomic maps.
*  All right. So maybe we'll come back to those.
*  But but the interesting thing to me is that cognitive architecture in your little it's
*  not a Venn diagram, it's kind of a nested diagram is like the most minute part of the
*  way that you view what you have worked on through your career.
*  And yet, you know, this is a kind of a unified picture of cognition.
*  So you start from a pretty large scale there.
*  Yeah. So when I started that 10 year digression, I certainly didn't have any attempt of
*  trying to re-understand computer science or computing more broadly.
*  But I had gotten burned out.
*  I didn't see how to make further progress on SOAR the way I wanted to.
*  And we had been working for a number of years on a military simulation, basically
*  applying SOAR to model pilots and commanders in military simulation.
*  Which was highly successful, but it took me away from the kind of research that I like to do.
*  And one of the things I found out about myself is that I'm really not applications oriented, even
*  though payoff for that is very high.
*  I've never started a company.
*  I've always avoided doing anything beyond a toy application unless I kind of had to.
*  But we as a group decided that was the right thing to do with SOAR, and I think it was the
*  right thing to do with SOAR.
*  But after that, Herb Shor, who was the executive director of ISI, saw that Mr. Bernhardt invited me to work
*  with him on new directions for the Institute.
*  This is the University of Southern California Information Sciences Institute, which essentially
*  involved going across the breadth of computer science and related fields and looking at what
*  the future was to bring and what kind of new areas we ought to get the Institute into.
*  So that had me working in many different areas, everything from technology and the arts to
*  sensor networks to automated building construction.
*  And there was just this wide range of things I was working on and with many different partners.
*  And to me, it felt incoherent in the sense that I couldn't figure out, at least to me, it didn't
*  feel like what brought all this together?
*  Why? Why was this so coherent subject of study?
*  And that got me thinking a little bit during those 10 years as to what did they all have in common and
*  how did they fit together?
*  There was actually near the end of those 10 years and going on that I started to come up with this notion of
*  at that point, it wasn't a dichotomous analysis.
*  It was more what I call the relational model, where I started to look at the relationships between
*  computing and the physical sciences and the life sciences and the social sciences and to itself
*  and started to understand that there was a core to computing, which had to do with this transformation of
*  information. But that when you related that core to itself in various ways and to these other
*  scientific and engineering disciplines, you could start to understand how the different how the
*  different kinds of activities I was involved in and ultimately how all of computing fit together in kind
*  of a neat way. And that's sort of what led to to the book
*  on computing, the fourth great scientific domain.
*  It happened later on as part of that, it was something inspired by Peter Denning, a computer
*  scientist up at the Naval Postgraduate School in Monterey.
*  But it's come to the notion that, OK, I was looking at the relationship between computing and these
*  other domains. I was thinking of them as great scientific domains.
*  They didn't really have a name that there was standard use.
*  Everybody knew that the physical life and social sciences.
*  But there wasn't a term people used for those kinds of things.
*  But I was using computing in the relational model just as I was using those.
*  I said, perhaps computing is one of those.
*  And so that sent me out thinking, OK, what is a great scientific domain and is computing one of those?
*  And that then took me into philosophy of science.
*  And it's an area in which I've continued to work, though I can't ever quite claim myself as being a
*  professional in that area. But the question of what is a scientific domain and what is and what isn't
*  and and why consider computing.
*  And so I came up with the definition of one and which, of course, fits computing because it had to
*  fit these other domains as well.
*  And then I started to look at the relationships among these.
*  And that's what led to that particular book and has continued with a work in
*  these dichotomous approaches to understanding
*  and kind of AI and cognitive science and
*  and complex systems within those fields.
*  So in a sense, you mentioned this nesting of.
*  Of kinds of models I've worked on, the cognitive architecture is the biggest piece of my life.
*  It's part of AI and cognitive science.
*  Those are bigger than that.
*  And computing is bigger than that.
*  And all of science and engineering is bigger than that.
*  So it's the smallest part of the figure, though, has been the biggest part of my career.
*  So did the I know that we're all over the place, but that's OK.
*  But did your stint in philosophy of science and then thinking about these bigger pictures
*  these bigger picture things, did that have something to do with you reformulating and getting interested again
*  into cognitive architectures?
*  Not directly. So those 10 years actually led to two efforts that I thought of as being
*  completely distinct at the time.
*  One of them was Sigma, this new cognitive architecture, and this other was the attempt to understand
*  computing via the relational model.
*  Both came out of that period.
*  The Sigma came out of, again, looking more broadly at AI and looking at all the advances at that time they made in
*  this area called probabilistic graphical models.
*  We were missing something in the world, cognitive architectures, but not understanding this world of probabilistic reasoning,
*  reasoning under uncertainty, the kinds of learning you can do and the kinds of reasoning you can do.
*  So Sigma came out of that period by that.
*  Although one of the things I understood while doing the book was that I really cared about these deep fundamental
*  understanding about things.
*  And part of what is to Sigma was understanding that I didn't feel like I was making progress in cognitive architectures
*  unless I was bringing that same insight to those.
*  So the early years of SOAR had that.
*  There was kind of one form of memory, one form of learning, one way of making decisions.
*  And there's no sort of problem spaces for search and one way of doing the reflection.
*  And through that small number of fairly general ideas, you got this huge variety of intelligent behaviors coming out.
*  When you couldn't push SOAR any farther, at least I couldn't forget to push SOAR any farther, in that same paradigm,
*  that's kind of when I burned out.
*  Now, John Laird, who along with Alan Newell and me was working, it was John's regional thesis.
*  And then I joined with him and Alan.
*  Alan was the advisor, both of us.
*  John continued working on SOAR after I stopped.
*  And he added more memories and learning mechanisms and other mechanisms, which is something I hadn't been
*  willing to consider at the time, partly because even without realizing it, I had this mental framework saying you
*  can't do that. Whereas John didn't have that framework and so very successfully has improved SOAR in many ways
*  since that point. When I started to think and it took quite a while to figure out how to do this, how to bring the
*  probabilistic graphical models and SOAR like architecture together, I realized this was sort of the second period
*  like the early days of SOAR, that all of a sudden I could see how to bring, again, a small set of ideas together that would be
*  even more prolific in terms of the range of things it would provide than the original SOAR did.
*  So both the book and Sigma have this common notion of I want to look for the deep underlying generalities and see how to
*  get this wide range of phenomena out of the combinations of a small number of ideas.
*  That ended up being common to both. And I wouldn't have realized that if I hadn't worked on the book.
*  And that really helped Sigma.
*  Oh, let's back up and just state what a cognitive architecture is, because I don't think that I had ever seen a
*  definition of a cognitive, of what a cognitive architecture is.
*  But I just kind of loosely held it in my mind that I kind of know what it is.
*  But there's a pretty clear definition.
*  Well, I don't know if there's a generally accepted definition, actually, that I keep in mind.
*  I consider it a hypothesis concerning the fixed structures and processes that define a mind.
*  And for me, it's a mind, whether it's a natural mind or an artificial mind.
*  To most people, cognitive architecture focuses on natural, in fact, human minds.
*  So most of the field will tell you that.
*  And then there'll be AGI and AI architectures, which are focused on artificial systems.
*  To me, it's about a mind in general.
*  In fact, that's something that's characterized my thinking all along.
*  I haven't been focused on either human or artificial.
*  I cared about mind in general and human and AI are two kinds.
*  And so I look at all the different kinds.
*  I can't haven't looked at animal minds.
*  OK, so I was going to ask is, but it is a human level.
*  Yeah. Human human level.
*  Or I guess the term we use now is human like human level is
*  emphasized as a different aspect of it.
*  So, yeah, that's what a cognitive architecture is.
*  We're looking for what are the basic mechanisms and processes?
*  How do you fit them together so that you get the range of intelligent
*  behavior coming out of that combination?
*  It's that phrase fixed structure.
*  I for some reason that helped me solidify
*  what a cognitive architecture is and be more at ease with it.
*  So is that the part that you think maybe is not commonly accepted as the definition?
*  So for me, that's the key part of it.
*  Fixed structure and minds to other people.
*  To most people in the field, fixed is important,
*  though people will say, well, there's development as well as learning.
*  Right. And development might slowly change the mind,
*  as opposed to evolution, which creates it fixed within an individual.
*  There's another notion, which is that
*  I knew one of the things he did in the unified theories of cognition
*  is come up with this notion of scale counts in cognition.
*  Right. Yeah. And so he looked at different time scales
*  from a micro milliseconds to seconds to hours,
*  days, weeks, months and so on, and developed a set of bands, time scales.
*  So he had what we call the biological band that ended, I think,
*  that around 100 milliseconds and then a cognitive band
*  that went from like 100 milliseconds up to a few seconds.
*  And then there was a rational and social band.
*  I may not have maybe remembering that.
*  That's close. Yeah.
*  But so for him, I think the cognitive architecture
*  was at the base of the cognitive band.
*  It's kind of things that happened at around 50 to 100 milliseconds.
*  There's a notion that is also probably due to him,
*  the others may have come up with it early as well,
*  that there's a basic cognitive cycle time that's in the range.
*  For him, originally, it was around 70 milliseconds in something
*  he called the model human processor, which actually came out of his work
*  in human computer interaction.
*  And for us, it's turned into more of a 50 millisecond
*  cycle time for cognitive architectures.
*  So there's a way to think of cognitive architectures
*  at providing the mechanism that happened at roughly the tens of milliseconds level.
*  Below that, you get into neural networks and other aspects of brain modeling.
*  Above that, you might get into rational things like logic
*  and other kinds of things which take more time in human cognition.
*  But the cognitive band is sort of the tens of milliseconds up to a few seconds.
*  So you can think of a cognitive architecture as the stuff
*  that supports that particular band.
*  So it's a different way of thinking about it.
*  We tend to think of those as kind of the same
*  because we talk about the mind, we're talking about the cognitive band
*  as opposed to the brain, which is more the biological band.
*  So SOAR started off
*  aimed at that cognitive band, that 70 or, you know,
*  Alan 70 millisecond kind of time scale.
*  Well, I just want you to talk about SOAR a little bit.
*  I can't, you know, back in the at Dartmouth, right?
*  And at the birth of AI, they were going to solve AI within a summer.
*  What was the feeling of, you know,
*  looking back, it's almost like right now is the right time for cognitive
*  architectures to be coming back because AI has made so much progress.
*  We've made a lot of progress in cognitive science and neuroscience.
*  But then, you know, looking back, it almost looks overly ambitious
*  to try to bring this unified
*  architecture to explain and implement cognition.
*  What was the feeling like back then when SOAR was being developed?
*  So most of the field, most of the time considers it overambitious.
*  But those of us who are kind of committed to it are always looking at
*  what's the best we can do at this point in time.
*  And the field goes up and down.
*  Most of the time, the field spends looking at particular mechanisms,
*  particular planning or learning or memory or reasoning systems.
*  And they do a lot of very careful
*  development and understanding of all these specialized techniques.
*  And then there are times they get dissatisfied and say,
*  oh, it's time we got to think about putting those together.
*  So there's a time in the 80s, I think it was maybe early 90s
*  when the field felt that was important.
*  And so there was a high point for the field then.
*  When we started in the mid to late 70s,
*  there wasn't that much interest in it at that point in the field.
*  There was, I guess you could say, early in the 50s.
*  So where SOAR kind of came from, I mean,
*  so there had been some ideas that Alan and Simon and others had developed earlier.
*  By the mid 70s, there was a project at CMU
*  called the Instructable Production System Project,
*  and it was wildly ambitious.
*  The notion is you should be able to take production systems or real systems
*  and build millions of rules into them, capturing much of human expertise.
*  But you can't do that by hand. It has to be learned.
*  And so how do you do that?
*  So what you do is you build a natural language and you talk to the system
*  and it learns from that.
*  So the Instructable Production System was this production system
*  based on what at that point was the highly efficient
*  version of how you do rule match, which was the most expensive part of the systems.
*  And there was this task environment, which was a model job shop.
*  Very simple for the day.
*  But think of it as an early predecessor of game environments
*  back in the mid 70s.
*  And the idea is that the system IPS would try to solve problems in this domain
*  and you would give it advice and interact with it.
*  It was doing it. And from that, it would learn the rules.
*  It was entirely too ambitious.
*  Act as Alan Newell said in his Sire and Diversions talk,
*  it was a classic failure.
*  There was a prospective paper and a retrospective paper and nothing in between.
*  Soar turned out to be kind of the revenge of IPS.
*  Oh, in John's later thesis, they understood
*  John and he John and Al understand
*  so it had to bring together rule systems and problem spaces.
*  So you could get decision making and rules going together.
*  And then my thesis, I understood how to bring together
*  rule systems and learning from experience.
*  And then we were able to put all of that together
*  in a version of Soar that combined them.
*  And all of a sudden, it didn't have language yet.
*  We started working on that a little later.
*  But all of a sudden, it started to have the kinds of capabilities
*  we wanted in IPS, but we had no clue how to do an IPS.
*  And so that was kind of how that occurred at that point in time.
*  I think to Alan, the notion of the unified systems was always important.
*  To me, it was always important.
*  But the field went hot and cold on the idea.
*  I do agree with you that I believe and at least I hope
*  that we're getting into an era when we'll see interest in them again.
*  We're starting to see that out of the neural network community.
*  The deep learning community where they realize some of the limitations
*  just having a single neural network and for example, systems like Alpha Zero,
*  which are an AlphaGo before it, which beat the human world champion
*  to a bunch of other games that combines the neural network as a form of memory,
*  along with problem space search of a particular sort.
*  And so there are other examples of what they call neural
*  turing machines where people are trying to combine neural networks
*  with other of the kinds of capabilities we've been looking at for a long time in AI.
*  Jan LeConde has come out with some recent editorials and papers about his ideas.
*  He doesn't call it a cognitive architecture, but that's really what it is.
*  Why wouldn't why wouldn't he call it cognitive architecture?
*  I don't want to speculate, but OK.
*  I mean, so people like Jeff Hinton know
*  exactly what cognitive architectures are.
*  He was on my thesis committee, actually.
*  I knew him since my days as a graduate student at UC San Diego.
*  Jan LeConde I've only met once, I think, very briefly at a workshop in Zurich.
*  But I don't think I read our papers.
*  I think the neural network world,
*  new fields often try to create space for themselves by separating themselves
*  from earlier ones, and they try not to understand what was going on there.
*  AI did that when it got started, it separated itself from cybernetics
*  and double E and pattern recognition.
*  It only became decades later that we started to bring them back together.
*  So at some point, we'll bring them all back together.
*  And then you'll and then your legacy will be sealed.
*  Right. How frustrating has that been?
*  That was all that was all wrong.
*  So, yeah, it was history, but it was all wrong.
*  Here's the right.
*  I mean, for Jan, for example, if it's not all differentiable, then it doesn't count.
*  And the kinds of stuff we do.
*  I mean, Sigma has some neural network aspects that are differentiable,
*  but not all of it is.
*  And so, Tim, it doesn't count.
*  I mean, it's obvious that eventually,
*  you know, like the specialized deep learning systems are going to need
*  to be put together in an integrated cognitive architecture.
*  Is that am I missing something or is that obvious?
*  That's obvious to me. OK.
*  And I think it's more obvious to some of the players in neural networks.
*  But most of them still work on individual applications. Yeah.
*  Maybe they will be inspired
*  by the recent success of the generative models,
*  which are showing just the huge ability to do all sorts of things. Yeah.
*  To me, they're kind of
*  the latest best approximation to the subconscious,
*  which is one part of the full system.
*  And they will understand that and say, oh, we've done such a good job on this.
*  But if we have this, this and this, we can get to full.
*  I mean, they're all talking about sentience and consciousness now and so on.
*  So they'll start to realize, oh, if we have these other capabilities,
*  maybe we'll get there.
*  OK, all right. So let's go back to SOAR, I suppose,
*  before we go down the rabbit hole there, because I want to come back
*  to the deep learning eventually as well.
*  So so SOAR was a solution
*  that was the sort of a oh, what did you call it?
*  Not a revenge. It was not you didn't use the word revenge.
*  It was it was yeah, revenge on the on the previous
*  classical failure, as Alan Newell put it.
*  And then you worked on that for a long time with John Laird.
*  And yeah, but for years without until he died.
*  You developed something called chunking, which you have left off in Sigma.
*  And so I don't maybe I don't know if you want to describe what chunking is.
*  But anyway, you and both John Laird
*  worked on that and Alan until until he passed.
*  So what else is there to say?
*  How far did you get with SOAR that you got so
*  so to the point that you thought you couldn't make any more progress on it?
*  Was it just because the limitation of the single memory function, et cetera?
*  So let me start with chunking since then.
*  Sure. So that came out of some work I did with
*  with Alan Newell after I returned from UC San Diego.
*  He had signed up to write a paper for a for a
*  a chapter in a book, and he wanted to do it on the parallel practice,
*  which was kind of known implicitly, but hadn't been made explicit
*  as far as I know before that.
*  It's a general phenomena which says that
*  if you graph the amount of time it takes you to perform a task
*  versus the number of times you've done it, that you get a parallel curve.
*  Now, parallel in the simplest form is the time equals the number of trials to some power.
*  And generally, it's a negative power, small power.
*  So you get a curve that goes like this.
*  It's it's like an exponential curve, but slower.
*  So we started by doing a bunch of work, trying to establish that
*  you found power law curves everywhere.
*  Whenever you measure human performance, you got a power law curve.
*  And then we started to come up with a theory for what could produce power law curves.
*  And it was Alan's intuition to start with the notion of chunking,
*  which traditionally came out of psychology as a way of talking about short term memory.
*  As being chunks of items.
*  Seven plus or minus two was George Miller's classical paper on the topic.
*  The way we eventually developed it and I developed my thesis
*  was as a notion of.
*  Combining experiences, essentially.
*  So the idea was if you're going along fine
*  and you have enough knowledge to do what you want to do,
*  you're just applying the rules you already have to help make decisions.
*  If you run into what we call an impasse,
*  you would step back and reflect.
*  This is one form of what you might think of as part of consciousness.
*  But you step back and think about the problems in your own behavior
*  and you solve those problems.
*  And from that, the idea is you can learn new rules
*  that in the future you could just fire and continue on without having to think
*  hard about it again.
*  That's what chunking became, essentially a means of learning new rules.
*  By.
*  Essentially summarizing this reflective processing you do
*  did when you ran impasses.
*  And so it turned out that applied sort of all over the place.
*  And so are there a number of different kinds of impasses
*  it can run into.
*  And so you could learn rules that control search.
*  You could learn rules that implemented operations of various sorts.
*  You could learn all different kinds of rules.
*  And that was, again, part of the early excitement.
*  As time went on, we we found more and more things for it to do.
*  And we were doing wider and wider ranges of applications from knowledge,
*  intensive systems and search oriented systems to real time robotic control
*  and control of simulated entities.
*  So all of that was going along fine.
*  But I didn't feel like with the architecture itself was improving.
*  I didn't know what was missing, so that was part of the frustration.
*  I knew I couldn't.
*  I knew we weren't there yet, but I didn't know what was missing.
*  I did a I had a sabbatical just before I stopped working on
*  soar and I tried to work on emotion.
*  And I realized it was very difficult in soar.
*  The only thing I came up with was a bit of a model,
*  a bit of a model of frustration, which kind of be extremely appropriate.
*  Sure. It was essentially you'd you start reflecting
*  and you'd keep reflecting down to arbitrary levels.
*  You never make any progress.
*  And that was the notion you start getting frustrated.
*  And then that was kind of kind of when I stopped working on soar.
*  It wasn't until then
*  with Sigma, where I started to bring together the probabilistic ideas
*  and the kinds of learning you can get out of that
*  and the kinds of reasoning you can get out of that
*  and how that gave you ideas about how to do perception and motor control.
*  And how to do visual imagery and all these other kinds of things
*  that they felt like they could make progress again.
*  Now, you mentioned the chunking is not in soar, and that's
*  perhaps my biggest failure with Sigma to this point.
*  I've tried any number of times over the years to put chunking into soar.
*  Sometimes I've tried to look at very narrowly just as way of combining
*  rule based processing, times times very broadly as ways of summarizing
*  all of the kinds of things going on when Sigma reflects.
*  But I've never managed to pull it off. It's interesting.
*  Is that is that is the is the challenge because you use probabilistic
*  graphical networks as the sort of ground level implementation beneath Sigma?
*  I haven't been able to articulate exactly what the issue is, but
*  I know that the
*  the core problem is finding a way to summarize
*  the processing that goes on when you reflect in in Sigma
*  as sets of knowledge structures within Sigma.
*  I mean, generalizations of the rules in soar, which include things like
*  probabilistic graphical models and and things that are hybrids
*  between them and all these other things.
*  So there's a particular way that the summarization process happened in soar.
*  And I've been trying to mimic or mimic that in some ways in Sigma.
*  And it's just never quite worked out for all sorts of very subtle reasons.
*  Unfortunately, I probably finished with Sigma since I've retired.
*  I just don't have what it takes to go back and and pursue that further.
*  So, but yeah, but Sigma itself is not finished.
*  Sigma may be finished.
*  There are some students who may continue doing things on it.
*  But as far as what I can do, it's kind of finished, unfortunately.
*  So there may be an inspiration that hits me or hit someone else.
*  And I just can't resist or someone can't resist going back and trying to make it happen.
*  But but yeah, that's that's a key kind of learning that I've never managed to get into.
*  Maybe you need to go to DARPA for another 10 years or something.
*  And then that'll do it.
*  But it's a different kind of learning in which did all sorts of additional things
*  which we couldn't do in soar, although John has found various
*  has added multiple new mechanisms to deal with with those kinds of
*  some of those kinds of learning.
*  So we didn't really talk about and I don't know.
*  We don't need to get in the weeds about it, but we didn't really illustrate
*  the actual architecture of soar and then what how Sigma, you know,
*  how how different it is and how similar it is.
*  OK, so the original sort of the way I think about it still,
*  I mean, the way it was sort of until I left the project in the late 90s.
*  It's fairly simple conceptually.
*  There's a single long term memory consisting of rules.
*  There's a working memory, which is short term memory.
*  And the way things work is that the each rule is a set of conditions
*  and set of actions.
*  The conditions match to patterns in working memory,
*  which are these little simple structures or trees of symbols.
*  And they generate new structures in working memory.
*  And so the there's a basic memory retrieval cycle of matching
*  and executing rules in parallel, which augment what's in working memory.
*  So perception comes into working memory.
*  And then you can view this memory as elaborating
*  what you know about what you're seeing.
*  So that's a core part of the memory or what we call the knowledge cycle.
*  And that's happening in small numbers of mic
*  milliseconds in human time.
*  Then, so that's kind of the innermost loop.
*  Outside of that is the cognitive cycle, which, as you say, in humans
*  is running at approximately 50 milliseconds.
*  What happens there is you run the whole memory till exhaustion,
*  till there are no more rules that can fire.
*  So they're firing waves of parallel rules
*  until you've kind of exhausted what you know about the current situation.
*  Part of what you retrieve or what called preferences in the original sword,
*  they were little symbol structures.
*  They say prefer this operation over that one.
*  Or this operation is best in the situation.
*  Later versions of sword, there were numerical references as well.
*  You could then make a decision.
*  If you could make a decision based on these preferences,
*  you would choose an action to execute or you'd
*  execute the action or do things like that.
*  If you couldn't choose an action or apply it, that's when you reach an impasse
*  and you'd step back and reflect and you'd give yourself a whole new space
*  in which to think about that problem of why couldn't you make a decision?
*  And so and out of sequences of those kinds of things,
*  you'd go off in kinds of search and reasoning.
*  And then once you figured it out, you'd return a result,
*  which meant the impasse, you could make a decision.
*  The impasse would go away and new rules would be learned.
*  So that was kind of the essence of of SOAR, the way I thought about it.
*  John has since added two additional long term memories.
*  He's added a visual imagery memory.
*  He's added multiple learning mechanisms for reinforcement
*  learning and for declarative learning and episodic learning.
*  And so it's a much more complex beast than it was back then.
*  But that was kind of the essence of SOAR as I thought about it.
*  And then Sigma has a lot of similarities to SOAR.
*  And then, you know, eventually we're going to talk about what you what
*  is being called the common model of cognition that kind of brings
*  all these principles together in an abstract way.
*  But but what do you see?
*  How is Sigma different and similar to SOAR?
*  What's the main main differences?
*  So in some sense, the inspiration is similar.
*  I was trying to kind of get by with one or a small number of everything.
*  But the kinds of things it has are more general.
*  So the way I think about Sigma is that it's at least a two layered architecture.
*  So there's a cognitive architecture, which in some ways is like SOAR.
*  Below that is a graphical architecture, which is based on a generalization
*  of what are called factor graphs, which is a form of these probabilistic
*  graphical models.
*  They're all kind of ultimately due to to you to Pearl and his work on on Bayesian
*  networks of factor graphs are a very, very general form of these.
*  I got inspired by reading
*  a paper out of Double E, which was normally about things like
*  error correction, coding theory and stuff.
*  But it showed to me, forget it, unfortunately, at the moment,
*  that the three authors on it, but the breadth of what you could do with factor
*  graphs. And so I started to think about, OK, can I start with a level like those,
*  but use them not only for probabilistic reasoning, but for rule based reasoning.
*  And ultimately, we got to points where we're using them for neural network
*  like reasoning and other kinds of things.
*  So I built this generalized factor graph representation
*  as a graphical model and then started to look, OK, how can I build rules?
*  How can I build decision making?
*  How can I build search
*  and learning all on the basis of these factor graphs
*  and get things that were not only like source rule memory,
*  but were like the later source.
*  Semantic memory or memory for facts,
*  where you can give a pattern and retrieve facts that are similar to it.
*  It's episodic memory where it records experiences
*  that you can retrieve in various ways, as well as things that were much more
*  probabilistic and things that were hybrids between those,
*  because you had a kind of a deeper understanding of how they all related
*  to each other. So Sigma was kind of built on that intuition.
*  So it is a much more general unified memory model,
*  which can do all three kinds of memory.
*  So it can do plus in the neural network memories and other kinds of memories
*  as well. But it still has a decision cycle, though it's now based on
*  all these numbers floating around in these graphs.
*  And it has a sort like reflection capability,
*  but again, not a sort like chunking capability.
*  And we found we can use it for perception.
*  You can do both neural network like perception as well as
*  as probabilistic graphical model types of perception.
*  I did certain generalizations that generalize sort of over symbols
*  and numbers where I start with a real number line
*  and then allow discretization of it so that you can get integers
*  and then allow assigning symbols to discrete regions.
*  You can get symbol processing.
*  And so I could get a range of things from symbols to numeric processing.
*  And that made it fairly easy to do things like visual imagery,
*  because I have this underlying
*  in dimensional numeric space that I could tap into because you can get.
*  There's essentially a single number line, but you could get cross products
*  of them, so you can get arbitrary numbers and dimensions.
*  So there are all sorts of things I could now do that I couldn't do
*  with with SOAR originally.
*  And that's again, kind of had me excited and drove me for the next 10 plus years.
*  This, you know, all that detail that you're just talking about
*  reminds me of a of a couple of your maxims.
*  One is that implementation is important to actually, you know, implement the
*  the architecture, the ideas that you're thinking of.
*  But then I think the one just before that,
*  which you mentioned might be in somewhat a conflict
*  with the implementation is important is to keep the the insight is important,
*  which is kind of the big picture is important.
*  Right. I mean, how have you done that?
*  Sorry, this is a bit of a diversion, but how have you done that
*  when you have to work on these problems of how we're going to implement it,
*  which inevitably must shape how you think about the the process itself as well?
*  So fortunately, I seem to be able to work at both those levels at once.
*  Yeah, that is fortunate.
*  Any people that are one level, one level or the other,
*  and they to me are somewhat limited in what they can accomplish.
*  I mean, they can be very good at all.
*  The details are very good at high level thinking.
*  But I've always been able to kind of maintain both in mind at the same time,
*  which let me accomplish what I've been able to do.
*  And it's multiple levels.
*  So there was kind of the grand idea of Sigma.
*  But within that, there are a bunch of smaller ideas, which are
*  visionary in some sense also.
*  But then there's the hard slogging of how to make all this work.
*  And.
*  I do get a lot.
*  I have gotten a lot of my insights out of out of doing that.
*  Some of the original ideas about how this works simply didn't work out.
*  And if I just stuck at a high level, I would not have realized it.
*  And my insights would not have been as deep.
*  But when you go down and actually forget how to all make work
*  and how to make it all work together, that's sort of to me, the key
*  challenging part in architectures, not the individual mechanisms,
*  but how do they all smoothly work together to yield through their combination?
*  What you're looking for.
*  It's always possible to slap together a bunch of modules and get something.
*  But to get them going generally and elegantly,
*  is kind of the key challenge for me.
*  So not to belittle any other cognitive architectures,
*  because there's this review paper and there's like,
*  I don't know how many cognitive architectures there are in the 80s now.
*  That are like, yeah, around 100 or so.
*  I mean, plus or minus 100.
*  Yeah. And I've had Chris Eliasmith on the podcast
*  and we've talked about his cognitive architecture spawn.
*  I've had Randy O'Reilly and his cognitive architecture, Libra.
*  And those are more on the neural side of things generally.
*  But I would imagine the big three that often get mentioned in the same breath
*  are SOAR, Sigma and then ACT-R, which was John Anderson's
*  psychological cognitive architecture.
*  Almost right.
*  Oh, is it? Oh, how's it?
*  Tell me I'm wrong. How am I?
*  What's wrong about it?
*  There's only a big two.
*  SOAR and ACT-R.
*  And SOAR is kind of the leading one in the AI focus
*  and ACT-R with the cognitive science focus.
*  Sigma is in the common model because I was one of the leading
*  developers of the common model.
*  Otherwise, in some of the later papers, they don't always talk about Sigma.
*  To me, Sigma is a synthesis of much of the rest of it.
*  But if you talk, there's really a big two, not a big three.
*  OK, well, there's a big three, but not for everyone.
*  OK, well, we'll get to talking about the common model.
*  But what is the since, quote unquote, cognitive architectures
*  are outside the mainstream somehow.
*  What is the sense of community within, you know, between people
*  working on their version of the cognitive architectures?
*  Is it competition? Is it, you know, are people trying to synthesize things?
*  Do they get along? You know, I'll hate each other, you know.
*  So like any community or any research community, the complex are dynamics.
*  I mean, it's full of people with with egos and ambitions and
*  and things they're trying to accomplish.
*  And it ranges from, I mean, so the big two architectures
*  have had large communities working on them.
*  There are some where it's just a single individual working on their own.
*  Sometimes even individuals that's not even in any of the core fields.
*  They just feel they they understand what intelligence is about.
*  And there's kind of everything in between.
*  And there are good relationships and sometimes hard feelings.
*  There are jealousies.
*  I mean, there's everything you can think of that you expect from from a community.
*  The common model is is a bit different
*  in that it's trying to bring people together
*  to get them to agree, at least find out where they do agree.
*  So we'd call it a consensus model.
*  It's trying to to at least go out initially to folks
*  who work on cognitive architectures and that, OK, what do we as a community
*  agree is true of a human like cognitive architecture,
*  where human like means either human or an architecture
*  that adheres somewhat closely to how humans work.
*  So there are some very widely different architectures in AI and HDI.
*  There's universal AI, which says there's a single equation
*  that produces all of intelligence.
*  But for human like AI, we thought there was a chance for conjunction
*  rather than just disjunction.
*  And we've been surprised to find out we can get fairly far with that.
*  I mean, it's going kind of slowly at the moment, where at the moment
*  we're working on topics like emotion and metacognition or reflection,
*  trying to add those to them because the original common model
*  is fairly minimal in a variety of ways.
*  But we were surprised we could get that much agreement across that community.
*  So it works kind of across the cognitive science
*  and AI people who care about cognitive science community
*  and those interested in architecture.
*  It's not something that the world that looks at individual mechanisms cares about.
*  The neuroscience community doesn't care about it.
*  AGI, we've gotten some rapport with the AGI community on it.
*  People like Ben Gertzell and so on.
*  But philosophy has philosophy embraced it or have they had anything to say about it?
*  Philosophy of mind people.
*  We haven't had a lot of contact with philosophy of mind folks about
*  specifically things like the common model.
*  I know there's there's a history.
*  People like Daniel Dennett, for example, and so on.
*  And there is an interesting philosophy of mind community.
*  But not so far the common model hasn't really made much contact
*  with philosophy of mind.
*  Well, it is pretty minimal.
*  And I'd love to hear the story in a moment of just
*  because it kind of arose out of a a meeting or a conference.
*  But let me just I'm going to list off the five parts of it.
*  And then we can go from there.
*  So in the center of the hub of it all, the center of it all is
*  is a working memory company.
*  And this is not a working cognitive architecture.
*  This is an abstract theoretical proposal for how minds are structured and functioned.
*  Yeah. So OK, so there's this core working memory component.
*  There are two types of long term memories, one
*  that builds in your knowledge, your semantic kind of memory or your knowledge.
*  And another is more procedural based in which skills.
*  Yeah, you learn skills.
*  And then there's perception and there's action.
*  And those the four things are kind of coming out on spokes from the
*  working memory and where everything is bound or comes together, I suppose.
*  And then perception and action are connected themselves as well.
*  But that's a pretty minimalistic model.
*  But even you were surprised that among the cognitive architecture
*  community that this that this model is fairly accepted as a theoretical abstract entity.
*  Right. So there's a bit more to there's decisions which don't make it into the figure.
*  We can tension this.
*  That's whether, for example, they're just part of the skill memory
*  or whether it's a separate module that should be shown there.
*  There are a number of assumptions that goes that go along with this,
*  that try to make it a bit more specific and concrete.
*  But yeah, it's minimal, but still surprising
*  that we could achieve consensus, because if you look at that paper,
*  for example, that you mentioned, which I think there were 80 something active
*  architectures, but there were over 100 that had been developed over the last four decades.
*  And you look at all those architectures,
*  described very few of them follow that model. Oh, really?
*  Um, so but if you look deeply at them,
*  you can see them in terms of this model for many of them.
*  So for a number of other architectures, we have mappings of them onto the common model.
*  I see. But the way the common model is expressed came about because I mean,
*  so the three of us who did the first version of it were in John and me
*  and Christian Labierre, who has worked for many years with John Anderson on an act are.
*  So it was highly influenced by the way we we thought about Sorin, Actar and Sigma
*  with me was assuming a sigma often pushing them in ways that were uncomfortable,
*  because I saw the these things in a fundamentally different way.
*  So, for example, it doesn't have two long term memories. Right.
*  But you build both of those on top of singles of source.
*  Sorry, a sigma single long term memory, because it's general.
*  So regions of memory rather than distinct memories themselves.
*  So there were things like that we had to work out.
*  But it started.
*  I mean, the first step was actually Christian and I,
*  who I didn't know very well at that point, the moaning at a meeting
*  that was discussing the next
*  international conference on cognitive modeling.
*  And we were both saying, there's all these small specialized conferences,
*  each which captures a small bit of what goes on in cognitive architectures.
*  So ICCM, this conference we were just talking about, really focused on cognitive
*  modeling, human like things. There was AGI.
*  There's Bicca, which is biologically inspired cognitive architectures.
*  There's advances in cognitive systems, which is high level, symbolic cognitive
*  architectures. But there wasn't any venue
*  where you could interchange all these different perspectives on the topic.
*  So out of that, we created a what was called a triple AI symposium
*  on integrated cognition, which Christian and I led.
*  And he I kind of I think I probably opened the symposium.
*  He closed it and he summarized his thoughts from it.
*  And his summary was in terms of what he called a standard model
*  of what he saw was common to at that at the symposium.
*  We did have people from neural approaches and AGI approaches
*  and cognitive approaches and AI approaches.
*  You remember we had if we had new from philosophy or other things.
*  But from what we saw, we had a lot of people from the
*  but from what Christian saw, there's a smaller number of things
*  he thought were in common.
*  And so he put it up on a slide as the standard model of the mind.
*  And the thing that shocked us was everyone in the room at the time said,
*  Yeah, that seems right.
*  That totally surprised us and gave us the
*  kernel of hope that we could build on that to do something more substantial.
*  John, who was at the workshop and worked closely with me and you,
*  saying Christian well, joined us early on.
*  And that led to that paper on the standard model of the mind
*  that appeared in the magazine, which later got
*  re termed as the common model of cognition.
*  Because so we held to further symposia on this common model idea.
*  The first one was on the standard model of the mind.
*  One of the kinds of pushbacks we got was there was fear
*  because of the notion of the standard model and in linguistics
*  that we were going to drop down and pose something on the field.
*  So there are folks who are feeling quite threatened by the whole thing.
*  There's some who still feel threatened and feel like we've left them out.
*  But so one of the things we did as a community was hold a pole and renamed it.
*  We did individual pieces, so standard, common, different alternatives.
*  Model of mind, whatever.
*  And we did polls and we ended up with the common model of cognition.
*  That's the name for what we were doing. Nice.
*  You know, my sort of knee jerk reaction
*  in reading about the common model and learning about this story
*  and how everyone more or less agreed is wondering whether that's due to a bias
*  in the cognitive architecture community that, of course, everyone agrees
*  because we all have the same kind of constructs of what psychologically
*  we're supposed to be doing because we all use the same words for psychology.
*  But it doesn't necessarily mean that we have the ontological
*  psychological categories correct anyway, but that's our common language.
*  So do you think any of it has to do with our bias as or sorry,
*  the, you know, the cognitive architecture community's bias in thinking in those terms?
*  So that's certainly a possibility.
*  And particularly with respect to the terminology,
*  I would hope that the ideas transcend the terminology.
*  Yeah. And even if you say we're biased in the terminology,
*  that some of the core ideas hold.
*  But we've been trying to challenge it by
*  mapping additional architectures onto it.
*  So we started with sort of the three and what we knew more broadly.
*  But if a wider range of people map on and say, here's what it's missing
*  or here's how you think about it wrong, that provides proof of thought.
*  The something we haven't talked about yet, but I know you wanted to talk about
*  was the mapping of the common model onto the brain.
*  Another one that is showing us that to some extent, we're thinking right about it,
*  whether or not the terminology is the best way of thinking about it.
*  So we're hoping to challenge it.
*  Ultimately, we hope that anything that's humanlike.
*  And again, you have to be careful that you don't say, OK, that didn't map onto it.
*  So it's not humanlike.
*  And therefore, we don't have to worry about it.
*  So you've got to be careful about these kinds of things. But.
*  If we can get the wider community of folks working on humanlike
*  architectures to map their architectures onto it.
*  And so we understand how all these things relate.
*  That's part of the hope for the common knowledge provides
*  kind of an interlingual for understanding the relationships among these models.
*  We'll get beyond the kind of the initial starting point
*  and concerns about whether it's biased because of where it started.
*  But we'll see how it goes.
*  So with that whole effort, we're trying to serve as facilitators rather than leaders.
*  So we started eight working groups and assigned a leader.
*  We got leaders for each of them, which weren't the three of us.
*  Unfortunately, they got far enough to produce some papers
*  for the second common model workshop, but they each had their own.
*  Things are working on, so it kind of died out.
*  So the three of us are taking it back on
*  working with Andrea Stocco as well and seeing if we can push some things
*  behind the scenes and then bring the community back on
*  to see if we can get them kind of reenergized.
*  Well, I read through a bunch of the papers that
*  that you guys, I guess, commissioned, you know.
*  So so you put out this common model of cognition bulletin
*  where basically you're asking other cognitive architecture folks,
*  like you were just saying, to reflect on their own cognitive architectures
*  and offer what they think might be missing to the common model of cognition.
*  But a lot of them seemed just like advertisements
*  for their own cognitive architectures.
*  I'm wondering, like, what you got out of reading those papers of that input.
*  And then maybe we can talk about some of the things that may or may not be missing,
*  because a lot of those papers said, well, this is missing
*  and my cognitive architecture has it, you know.
*  Right. So a lot of it is.
*  It shouldn't be surprising.
*  So I know I do be accepting the bulletin, actually.
*  The common model bulletin is an interesting case in point.
*  So Rob West, who I think is the University of Waterloo in Canada,
*  he's been one of the more active figures in the common model community
*  and cognitive architecture community, and generally traditionally come out
*  of the act our world.
*  He stepped up and volunteered to do that on his own.
*  Oh, so we said, sounds great. Please do it.
*  And so it's trying to be repository for the papers
*  that can publish wherever they are on that are related to the common model.
*  Papers that came out of those working groups.
*  What we hoped were that they would take a look.
*  So they were on topics like emotion and metacognition and language
*  and neural neuroscience basis.
*  We hope they kind of do a summary of what the issues were
*  for the common model in those particular areas.
*  And some of it ends up being advertisements for individual architectures.
*  Some of what you were talking about, the architecture.
*  And here's what's missing. My architecture.
*  That's actually a good thing, because that was mapping architectures
*  onto the common model. Right.
*  And it was saying what they thought the problems were.
*  And that's some of the kind of feedback we needed to hear.
*  It was from their perspective, but that's perfectly natural
*  and where they have expertise.
*  So, I mean, it's a mindset to work on the common model
*  and for people working on their individual architectures.
*  It's hard to shift perspective, of course.
*  And so we're trying to help the field
*  get the perspective and to be able to combine that.
*  I mean, they're not going to shift away from working on individual architecture.
*  But we're hoping is, again, they can combine that perspective
*  with the perspective of thinking about the common model
*  and kind of essentially do those two kinds of things in parallel.
*  That would be kind of an ideal world.
*  But again, you know, just I was kind of frustrated
*  reading a lot of the papers because it felt like a lot of people
*  weren't willing to play that game. Right.
*  They only wanted to stay in their own world and talk about their own thing.
*  So I can use one example, because I've had them on the podcast.
*  Like Steven Grossberg and his adaptive resonance theory.
*  You know, his entry read like any of his other entries.
*  He's been largely influential and and adaptive resonance theory
*  has is really old and it's done a lot of really cool stuff.
*  But there was no connection to the common model of cognition that I could see.
*  And that was the the case for a lot of the different
*  entries, I suppose, or papers.
*  But did you you know, what did you gain from reading those?
*  Was there a common theme that you've you're thinking,
*  oh, maybe this is one of the important things like affect motivation, etc.
*  That we should add.
*  It would be nice if we could get more people.
*  I mean, so in today's talk, it's a good example.
*  He's someone else who grew up to some extent in the act, our community.
*  He's got more of the neuroscience perspective.
*  He's at the University of Washington.
*  But he's totally bought into the common model perspective.
*  And so we invited him to join us to bring additional perspective in
*  and to bring a smart kind of younger person into kind of the core people,
*  a group of people thinking about this.
*  And it just was completely natural for him to think in this fashion.
*  And for some people, it is another for other people.
*  It just isn't. And it may excuse me.
*  It may never be.
*  So what we try to get from people is what we can.
*  We try to enculturate them as possible
*  and hope that things will grow in some in some kind of natural fashion.
*  I won't say it's not frustrating at times, but to me, it's just
*  the natural order of things.
*  And so you do your best, given the nature of everyone you're working with.
*  I'll highlight that you said, enculturate and not indoctrinate there.
*  So which is a major distinction.
*  Well, I'll just ask, you know, because because, you know,
*  there are a bunch of things thrown out that the common model must be missing.
*  What what are your thoughts on consciousness,
*  subjective experience is that, you know, is that an important part?
*  Well, so the problem with consciousness is no one knows what you're talking about.
*  The one problem with consciousness.
*  Right. Right.
*  There's one of the consciousness.
*  No one knows what they're talking about. Yeah.
*  When you read the literature that mentions consciousness
*  or metacognition or reflection, there are many different kinds of things
*  people are talking about.
*  And so I say one of the things we are talking about among the four of us
*  is metacognition and reflection, which is one aspect of
*  I think of the full world of people talk about with consciousness.
*  It's it's not
*  the notion of phenomena.
*  It's not quite the right word. Phenomenology.
*  Yeah.
*  Because to me, that's still mysticism, much of that.
*  But it is this notion of
*  including the sense of self model of self, the ability to reflect on what you're thinking.
*  So it's a set of concrete capabilities that we think are part of what goes
*  by the term consciousness that we think are, in fact, missing from the common model
*  at this point, but exist in some of the architectures, both
*  soar and Sigma have aspects of it.
*  Other architectures certainly have aspects of it as well.
*  So we know it's missing.
*  We know it was missing at the beginning.
*  We just didn't think there was a a consensus.
*  So, as you said, the common model's abstract was also the deliberately incomplete
*  as we're looking to include parts that there is a consensus.
*  And so we erred on the on the side of incompleteness
*  rather than trying to force
*  consensus where there wasn't any.
*  But absolutely that emotion.
*  A lot of people in AI think emotion is this epiphenomenal thing
*  you don't need to worry about.
*  The folks in psychology thinks it's the center of everything. Right.
*  I think those of us working on the common model
*  actually believe it is terribly important for cognition.
*  I mean, I've referred to it as the wisdom of evolution.
*  It provides forcing functions for us to do things in certain ways
*  that we don't want to necessarily do.
*  But evolution is decided is wise for us.
*  Now, that wisdom is very coarse.
*  And so it often steers us wrong, but often, but sometimes.
*  But to me, it's.
*  I mean, it involves physiology, it involves thought,
*  involves the architecture.
*  Emotions change how we think, they change how we behave.
*  Most of the work on emotion in AI is what I call cold emotion.
*  It's all reading about emotion.
*  So it works just as fine thinking about other persons,
*  people's emotion as it does about yourself.
*  It's all reasoning about it.
*  And then there's emotional, I mean, physiological stuff
*  where clearly things are changing in how your body works.
*  But again, as an architectural person, the part I care about most is
*  how does the architecture sense emotional states
*  and how does its functionality change as a function of that?
*  So when you're angry, you think differently.
*  It's not just a symbol in your working memory that you're angry.
*  And it's not just chemicals.
*  It actually changes how you think.
*  So how does your architecture understand that state?
*  And what does that actually change about how it operates?
*  Those, to me, are kind of like the central things about emotion.
*  Not everyone agrees with me about that, of course.
*  But that's the kind of stuff I'm pushing when we talk about emotion in the
*  in the common model.
*  We actually held up an on a virtual workshop on the topic,
*  got a lot of good input and got some consensus at the end of that,
*  which, again, was surprising, but the fun.
*  And right now, we're trying to just build on that consensus
*  to come up with a more concrete and more elaborated proposal
*  that we can go back to the community to talk about.
*  This is kind of an aside, but I was going to ask you,
*  given your interest in computing as the fourth great discipline,
*  or scientific domain,
*  domain, sorry, you know, since just just going off of what you were talking
*  about with emotion and physiology, do you think of the mind as
*  all computational or is there something else to minds?
*  It depends on what you mean by computational.
*  OK, we can say Turing computable.
*  Well, let's say, well, I'll let you I'll let you actually,
*  instead of pin you into a corner.
*  Is it all computations all the way down?
*  So there are people have very
*  narrow notions of what it means for them to be computational.
*  So, for example, they limit to that to simple processing.
*  And when you talk about numeric stuff,
*  they think you're not talking about computation any longer,
*  even though computers, of course, do computation.
*  And in fact, it's all grounded in digital processing on computers.
*  There are theories like digital physics, which hypothesize
*  that the whole universe is is basically a giant computer.
*  Of course, terribly controversial and not at all established.
*  So there's the possibility that everything is is computational at its base.
*  I don't rule out analog computation as part of the world of computation as well.
*  When you're talking about human minds and human bodies,
*  there's clearly an electrical and chemical and
*  there may be quantum things from people.
*  There are folks who want to
*  always push intelligence into the things we don't understand.
*  Quantum is one of the favorite aspects of that right now.
*  Yeah. But of course, there's quantum computation.
*  So maybe we'll understand that in terms of the form of computation.
*  So I almost don't care what you call chemical processing computation.
*  OK. I mean, it's an interesting scientific question as to whether
*  ultimately that's grounded in computation.
*  I do believe that chemical signals matter in thinking.
*  They're at a pretty low level, but pervasive level,
*  whether they're all captured by the kinds of things.
*  And we can do pervasive things computationally as well.
*  Whether we captured the effects of those chemical signals is a whole separate question.
*  My guess is we haven't.
*  And that when you talk about emotions, that's part of clearly what's going on.
*  You have to understand how to capture the kind of pervasive, low level
*  effects that happen from that kind of thing.
*  Let me see how to phrase this.
*  So on the one hand, in real brains, we've learned
*  that it's a really highly integrative system
*  and there's a lot of recurrence and interaction.
*  We've also learned that due to sort of a systems neuroscience effect
*  using neuromodulators, it can switch these circuits
*  into different regimes of behavior.
*  And we've also learned that cognitive functions are multiply realizable.
*  But are these kinds of principles that are coming out of neuroscience
*  and computer science, are those part of the common model,
*  sort of the backbone and infrastructure?
*  And sorry to ask another question on top of it.
*  How do you think about the modularity of both cognitive architectures
*  and the common model with respect to what we see as the
*  common model with respect to what we what we, quote unquote,
*  are discovering more and more about brains, that it's more integrative
*  and interactive than the strict modularity that we used to think.
*  So in some sense, I'm the wrong person to answer that question,
*  because neuroscience is a fairly large blind spot for me.
*  The brain, I've never you think I would be interested in the brain,
*  but I was never the answer.
*  I would think so.
*  Mind the memory was messy biological thing.
*  And I never looked by how.
*  So it's always been a large blind spot for me.
*  And just something I've had to accept it was for Alan also.
*  And it actually made more sense for him than for me, because in the early days
*  of AI was going into symbolic, it was so far from what people were understanding
*  neuroscience that there was just not a lot of room to talk.
*  Yeah. Now, with cognitive neuroscience, the world is it's a very different world.
*  But Christian and more so Andrea in the common model world are much more up
*  on that kind of thing than I am.
*  So they bring a general background.
*  I mean, so act are earlier been mapped on the brain and it worked with
*  with Randall Riley on cell, which is a combination of act are and Libra.
*  So there was those kinds of connections and Andreas is more deeply rooted in that world.
*  Many of the kinds of general things you are talking about from neuroscience
*  where I can't say are explicitly in the common model.
*  To some extent, Sigma might reflect them more than than the common model
*  because of the generality. Yeah.
*  Of the different. Yeah.
*  It says the module boundaries in the common model aren't quite as real
*  as we make them seem in the common model, that they are just different regimes
*  or different portions of a broader, more general memory that made.
*  So the graphical architecture might be more like the brain.
*  And then even Sigma's cognitive architecture is still more like it
*  because it only effectively has one long term memory.
*  The divergence into two in a common model and three in a sore
*  happen kind of above the level of the cognitive model of cognitive architecture in Sigma.
*  So some of that may be reflected, and hopefully we'll see more
*  that coming out as time goes on.
*  I'm really hoping that the stuff that Andreas Stalko is doing
*  in mapping Sigma onto.
*  I'd say the macro level of
*  functional circuits in the brain and the communication patterns among those circuits.
*  That will intrigue some of the neuroscience community.
*  And so we'll be able to see more interaction of that sort.
*  Can you let's let's before we move on, can you describe that?
*  This is the first author is Andreas Stalko, and it's comparing predictions
*  made from the common model to predictions made from other types of kind of connective
*  connectome and functional network models that are sort of popular.
*  I mean, it tested against like a few different versions of that.
*  Maybe you can just describe a little bit more what happened and
*  and where the common model fares, of course.
*  Sure, I'll I'll try.
*  But again, Andreas, you're an expert on all of this.
*  So you mentioned kind of the basic components in the common model.
*  There's a long term memory, a working memory and.
*  Perception and motor modules, and they all kind of connect through that working memory.
*  So hypothesis in particular, you could say connectome between those modules.
*  So what Andrea did, and you could say it's built on earlier, what had been done with Actar.
*  He mapped the modules in the common model onto functional circuits in the brain.
*  They're not quite brain regions, but there are functional circuits.
*  And then looked at the human connectome data to ask, OK, how do those different
*  functional circuits communicate and how does that compare to the connections
*  we have in the common model?
*  And what he turned up was that, in fact,
*  the common model approach provided a much better model, at least for the seven or so
*  domains of the human connectome tasks that he looked at.
*  Then you got from the traditional hub and spoke and hierarchical models from neuroscience.
*  And that was kind of really it was completely unexpected for us.
*  We didn't think the common model is abstract and incomplete.
*  They've been necessarily anything to do with the brain.
*  He showed that, in fact, there was this really neat macro level connection.
*  And then it might tell neuroscience some, then it might be able to provide
*  feedback to the common model for more of what's being learned in neuroscience.
*  So that's essentially what's going on.
*  And he applied some kind of interesting techniques for being able to establish
*  that these kinds of connections were a better model than what people
*  were traditionally looking at.
*  Not not to beat a dead horse at all, but going back to the question of bias,
*  right, the kinds of tasks that we run in labs to come up with these functional
*  circuits using the psychological terms that we use.
*  Do you think there's any particular issue with, you know, testing
*  working memory, you know, a very specific kind of working memory task in the lab?
*  And then, voila, there's a working memory circuit.
*  And since the common model has a working memory module, it maps really well onto this.
*  But it's it's it's in some sense could be putting the carrot before the whole
*  cart. I don't remember the phrase eating its own a snake eating its own tail.
*  Right. Because it defined the things to test in the lab that it is purporting to explain.
*  Right. I mean, so you've raised the whole humongous issue of ecological
*  validity of psychological experimentation.
*  Thank you. I could have said it much faster, but thank you.
*  Thanks for doing that for me.
*  And I can't say we have any additional solution than the in the field as a whole
*  lab. But yes, it is potentially vulnerable to those same kinds of critiques.
*  OK, fair enough. What do you think of the current boom of deep learning?
*  I know that some of the cognitive architectures are incorporating deep learning networks.
*  But as you're talking just earlier, the deep learning world is sort of taking this
*  cognitive architecture. I don't know if it's inspiration, but approach in some sense
*  and starting to piece together these various narrow networks and to work towards
*  something more general. So what is your broad overview or thoughts?
*  OK, so as an older person, I'm viewing as entertainment to some extent.
*  I mean, I try to I mean, as is the person as the kind of person they're often
*  railing against, I could get very defensive about it.
*  And there are some folks in our community who do.
*  But to me, it's it's par for the course.
*  It's the standard operating procedure.
*  So very community that for many years felt suppressed.
*  There's the Minsky Papert book and early results, which kind of showed that the
*  simplest versions of these models couldn't do what people thought they could.
*  And that effectively killed off the field for a decade, except for people like
*  Grossberg and others who stuck with and check in and others.
*  So they have a large chip on their shoulder about Jeff has even talked about
*  how Alan Newell and Herb Simon misdirected the field for a long time.
*  I think he's completely inappropriate in what he's saying and those kinds of things.
*  But but I understand the chip they have on their shoulder.
*  So I'm watching it from this perspective, seeing I was like that in its infancy.
*  It was separating itself out from everything else, and it was wildly ambitious
*  and completely overoptimistic.
*  And and that's just completely natural when all of a sudden you're at the point
*  where there's stuff you've been working on, you see, oh, it can do all this stuff.
*  And so they're pushed on by their success, which is completely natural.
*  So all the criticisms and they're accurate, but they're completely
*  understandable as far as I'm concerned.
*  And they have gotten way beyond.
*  I thought they would be able to with their current set of very simple
*  stacking technology.
*  I mean, if you look over the history of AI or probably in science in general,
*  there are always booms when something interesting happens.
*  And they always ask them to it out.
*  But you can never tell when.
*  Or why or how high.
*  And so those when people ask me, I say, yeah, it's going to ask them to it.
*  I just can't tell. I can't answer those questions.
*  And it turns out they've asked him to do a much higher level than I ever
*  would have expected.
*  I mean, they might not have even reached an asymptote.
*  Right. Right. General models are doing right now.
*  It's just I don't understand how they could possibly do what they're doing,
*  even though I understand what the technology is actually doing.
*  You don't think just with such compute and such huge volumes of data that it
*  and it's just making those statistical correlations and going for it.
*  I understand all of that.
*  But I wouldn't have thought that just doing that would you.
*  So I played with chat, you know, many people have.
*  It just shouldn't be my model of of large amounts of data
*  and statistical correlations and prediction and transformers
*  and whatever else they use.
*  I just don't see how it accomplishes it.
*  So there's this big gap in my mind
*  where it's just doing too good a job, even with all the limitations.
*  You know, it's getting things wrong and I know and you know,
*  it doesn't know when it's getting things wrong. Right.
*  And you know, it's I mean, it's shallow and it's all these other limitations.
*  But it's still incredible.
*  And I just it's like magic.
*  Um, do you think that in any of our like
*  one interpretation of that is that, wow, it is, you know,
*  let's say a large language model that generates, you know, really rich text
*  and is very impressive.
*  One interpretation is, wow, it's like almost as great as us.
*  But another interpretation is, well, maybe our language is not
*  that impressive after all, like that it's not the height of cognition or something.
*  So I mean, I think the secret really is that, I mean, in generating a language
*  model, they're looking at text describing everything we know.
*  And so implicitly in the language model includes aspects of everything we know
*  or almost everything.
*  And so there's a way it's a summary of all knowledge
*  and the way the web is, but in a different form.
*  But the fact that it coherent, I can coherently
*  at a larger scale than individual sentences produce
*  useful answers is just kind of incredible.
*  But still, as I said, I think it's a it's the next great model of the subconscious,
*  which means it's missing whole aspects
*  that are required for for full intelligence.
*  And in order to counteract the weaknesses to have, which the subconscious has as well.
*  And I think there are a variety of members of the community
*  that are coming to realize that and they're looking for alternatives,
*  whether they will find a fully distrational version like Jan wants
*  or there will be something else is an open question.
*  But I'm sure they will be pushed in the direction of adding more
*  of the capabilities as time goes by, because even though I'm sure they are
*  are enjoying and pushing as hard as they can on all the applications of what they've got,
*  they're also looking at what the limitations are and how to overcome them.
*  Yeah.
*  You wrote in your memoir, I believe you wrote about that in your memoir,
*  unless I'm misremembering and I saw it in an interview or something,
*  that you get a lot more satisfaction and intellectual inspiration
*  out of going to AGI conferences rather than psychology or computer science
*  or any of those other fields that you're kind of a part of.
*  I just want to ask you about that, and maybe you can just reflect on why that has.
*  Well, so they're clearly quite different.
*  I mean, for people who don't know them, the AGI conferences, at least traditionally,
*  were kind of all over the place.
*  Lots of people spouting big ideas, often with a little support.
*  That's different than these days?
*  I haven't been recently because I'm, I mean, the pandemic and I'm limited,
*  but my guess is that there's a bit more rigor now,
*  but I don't know if that's actually true.
*  It's supposed to be a traditional conference, which matters most is the rigor
*  and much less whether you're saying anything interesting.
*  So if you've done your experiments properly and it's something new,
*  even though it doesn't matter, you can get accepted usually.
*  And to me, as I mentioned, what I care most about are ideas that give me
*  thinking in new ways and the next incremental idea just leaves me flat.
*  And the next incremental idea just leaves me flat.
*  So that's why I've often enjoyed the AGI conferences.
*  There are people thinking big.
*  They may, of course, be totally wrong,
*  but they get me thinking.
*  And that's really what I care about.
*  And at a conference, I'm going to go to some place and get me
*  where people will get me thinking in a different way than I normally do.
*  You think other people go to happen in regular conferences?
*  There are ground making were published in regular conferences.
*  But the vast majority is just incremental progress on existing topics.
*  So it's really suited to your personality and desire as an explorer,
*  I suppose, to to seek that sort of inspiration rather than necessarily
*  the answer to the next question that you're asking or something.
*  As most of my colleagues in the academic cognitive science world
*  consider AGI abhorrent.
*  Right. That's why I was asking.
*  Lose cannons that have no methodology whatsoever and just spout off
*  whatever they want to say.
*  I said, yeah, it's true, but I still find them interesting.
*  And they dress different. A lot of them.
*  Yes.
*  You know, before I let you go, I just want I would be amused
*  if I didn't mention one of the things I really appreciated that you wrote about.
*  And I don't need to ask you a question about it.
*  I just appreciated your self-realization
*  that at different points in your life, you have come to
*  appreciate other facets of science and being able to take on board
*  different ways of thinking.
*  And I think that that is an underappreciated
*  realization that more people should be
*  should take on in their own lives and kind of more accept
*  who they are at the time in that part of their life.
*  I completely agree with that.
*  I made a road down partly because it seems like I've never seen that mentioned anywhere.
*  Yeah. And it clearly describes my life and I assume it describes most people's lives.
*  I think so.
*  But it's never kind of articulated.
*  And it helps people understand themselves and to accept how they are at that point.
*  And think about, well, I might be different in the future
*  and sort of just look forward to see what happens.
*  Yeah. So it's a beautiful way to think about it.
*  OK, Paul, I've taken you long enough.
*  I really appreciate your time. Thanks for being on.
*  OK. Thank you again. OK, bye.
*  I alone produce Brain Inspired.
*  If you value this podcast, consider supporting it through Patreon
*  to access full versions of all the episodes and to join our Discord community.
*  Or if you want to learn more about the intersection of neuroscience and AI,
*  consider signing up for my online course, Neuro AI, the quest to explain intelligence.
*  Go to braininspired.co to learn more.
*  To get in touch with me, email Paul at braininspired.co.
*  You're hearing music by the New Year.
*  Find them at the new year dot net.
*  Thank you. Thank you for your support.
*  See you next time.
