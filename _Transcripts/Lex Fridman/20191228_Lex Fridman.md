---
Date Generated: October 31, 2024
Transcription Model: whisper medium 20231117
Length: 6760s
Video Keywords: []
Video Views: 90914
Video Rating: None
Video Description: 
---

# Melanie Mitchell Concepts, Analogies, Common Sense & Future of AI  Lex Fridman Podcast #61
**Lex Fridman:** [December 28, 2019](https://www.youtube.com/watch?v=ImKkaeUx1MU)
*  The following is a conversation with Melanie Mitchell. She's a professor of computer science
*  at Portland State University and an external professor at Santa Fe Institute. She has worked
*  on and written about artificial intelligence from fascinating perspectives, including adaptive complex
*  systems, genetic algorithms, and the copycat cognitive architecture, which places the process
*  of analogy making at the core of human cognition. From her doctoral work with her advisors,
*  Douglas Huffstader and John Holland to today, she has contributed a lot of important ideas
*  to the field of AI, including her recent book, simply called Artificial Intelligence,
*  a Guide for Thinking Humans. This is the Artificial Intelligence Podcast. If you enjoy it,
*  subscribe on YouTube, give it five stars on Apple Podcast, support it on Patreon, or simply connect
*  with me on Twitter at Lex Friedman, spelled F-R-I-D-M-A-N. I recently started doing ads
*  at the end of the introduction. I'll do one or two minutes after introducing the episode,
*  and never any ads in the middle that can break the flow of the conversation. I hope that works
*  for you and doesn't hurt the listening experience. I provide timestamps for the start of the
*  conversation, but it helps if you listen to the ad and support this podcast by trying out the
*  product or service being advertised. This show is presented by Cash App, the number one finance
*  app in the App Store. I personally use Cash App to send money to friends, but you can also use it
*  to buy, sell, and deposit Bitcoin in just seconds. Cash App also has a new investing feature. You
*  can buy fractions of a stock, say $1 worth, no matter what the stock price is. Broker services
*  are provided by Cash App Investing, a subsidiary of Square, and a member of SIPC. I'm excited to
*  be working with Cash App to support one of my favorite organizations called FIRST, best known
*  for their FIRST Robotics and LEGO competitions. They educate and inspire hundreds of thousands of
*  students in over 110 countries and have a perfect rating on Charity Navigator, which means that
*  donated money is used to maximum effectiveness. When you get Cash App from the App Store or
*  Google Play and use code LEXPODCAST, you'll get $10, and Cash App will also donate $10 to FIRST,
*  which again is an organization that I've personally seen inspire girls and boys to dream of engineering
*  a better world. And now here's my conversation with Melanie Mitchell. The name of your new book
*  is Artificial Intelligence, subtitle, A Guide for Thinking Humans. The name of this podcast is
*  Artificial Intelligence. So let me take a step back and ask the old Shakespeare question about roses.
*  What do you think of the term artificial intelligence for our big and complicated
*  and interesting field? I'm not crazy about the term. I think it has a few problems
*  because it means so many different things to different people. And intelligence is one of
*  those words that isn't very clearly defined either. There's so many different kinds of
*  intelligence, degrees of intelligence, approaches to intelligence. John McCarthy was the one who
*  came up with the term artificial intelligence. And from what I read, he called it that to
*  differentiate it from cybernetics, which was another related movement at the time.
*  And he later regretted calling it artificial intelligence. Herbert Simon was pushing for
*  calling it complex information processing, which got mixed, but probably is equally vague, I guess.
*  Is it the intelligence or the artificial in terms of words that is most problematic,
*  would you say? Yeah, I think it's a little of both. But it has some good size because
*  I personally was attracted to the field because I was interested in phenomenon of intelligence.
*  And if it was called complex information processing, maybe I'd be doing something
*  wholly different now. What do you think of, I've heard that term used cognitive systems,
*  for example, so using cognitive. Yeah, I mean, cognitive has certain
*  associations with it. And people like to separate things like cognition and perception,
*  which I don't actually think are separate. But often people talk about
*  cognition as being different from sort of other aspects of intelligence. It's sort of higher level.
*  So to you, cognition is this broad, beautiful mess of things that encompasses the whole thing.
*  Memory, perception. Yeah, I think it's hard to draw lines like that. When I was coming out of grad
*  school in 1990, which is when I graduated, that was during one of the AI winters. And I was advised
*  to not put AI, artificial intelligence on my CV, but instead call it intelligence systems.
*  So that was kind of a euphemism, I guess. What about to stick briefly on terms and words,
*  the idea of artificial general intelligence, or like Jan LeCun prefers human level intelligence,
*  sort of starting to talk about ideas that achieve higher and higher levels of intelligence. And
*  somehow artificial intelligence seems to be a term used more for the narrow, very specific
*  applications of AI. What set of terms appeal to you to describe the thing that perhaps we strive
*  to create? People have been struggling with this for the whole history of the field
*  and defining exactly what it is that we're talking about. John Searle had this distinction
*  between strong AI and weak AI. And weak AI could be general AI, but his idea was strong AI was
*  the view that a machine is actually thinking that as opposed to simulating thinking or
*  carrying out processes that we would call intelligent.
*  At a high level, if you look at the founding of the field, McCarthy and Searle and so on,
*  are we closer to having a better sense of that line between narrow, weak AI and strong AI?
*  Yes, I think we're closer to having a better idea of what that line is. Early on, for example,
*  example, a lot of people thought that playing chess would be, you couldn't play chess if you
*  didn't have sort of general human level intelligence. And of course, once computers were able to play
*  chess better than humans, that revised that view. And people said, okay, well, maybe now we have to
*  revise what we think of intelligence as. And so that's kind of been a theme throughout the
*  history of the field is that once a machine can do some task, we then have to look back and say,
*  oh, well, that changes my understanding of what intelligence is because I don't think that machine
*  is intelligent. At least that's not what I want to call intelligence. Do you think that line moves
*  forever or will we eventually really feel as a civilization like we cross the line if it's possible?
*  It's hard to predict, but I don't see any reason why we couldn't, in principle, create something
*  that we would consider intelligent. I don't know how we will know for sure. Maybe our own view of
*  what intelligence is will be refined more and more until we finally figure out what we mean when we
*  talk about it. But I think eventually we will create machines in a sense that have intelligence.
*  They may not be the kinds of machines we have now. And one of the things that that's going to
*  produce is making us sort of understand our own machine-like qualities that we, in a sense,
*  are mechanical in the sense that cells are kind of mechanical. They have algorithms they
*  process information by. And somehow out of this mass of cells, we get this emergent property that
*  we call intelligence. But underlying it is really just cellular processing and lots and lots and
*  lots and lots and lots of it. Do you think it's possible to create intelligence without
*  understanding our own mind? You said in that process we'll understand more and more, but
*  do you think it's possible to create without really fully understanding
*  from a mechanistic perspective, from a functional perspective, how our mysterious mind works?
*  If I had to bet on it, I would say no, we do have to understand our own minds, at least to some
*  significant extent. But I think that's a really big open question. I've been very surprised at
*  how far brute force approaches based on, say, big data and huge networks can take us. I wouldn't
*  have expected that. And they have nothing to do with the way our minds work.
*  So that's been surprising to me, so it could be wrong. To explore the psychological and the
*  philosophical, do you think we're okay as a species with something that's more intelligent than us?
*  Do you think perhaps the reason we're pushing that line further and further is we're afraid of
*  acknowledging that there's something stronger, better, smarter than us humans?
*  Well, I'm not sure we can define intelligence that way because smarter than is with respect to
*  what... Computers are already smarter than us in some areas. They can multiply much better than we
*  can. They can figure out driving routes to take much faster and better than we can. They have a
*  lot more information to draw on. They know about traffic conditions and all that stuff. So for any
*  given particular task, sometimes computers are much better than we are. And we're totally happy
*  with that. I'm totally happy with that. It doesn't bother me at all. I guess the question is,
*  which things about our intelligence would we feel very sad or upset that machines had been able to
*  recreate? So in the book, I talk about my former PhD advisor, Douglas Hofstadter, who encountered
*  a music generation program. And that was really the line for him. If a machine could create
*  beautiful music, that would be terrifying for him because that is something he feels is really
*  at the core of what it is to be human, creating beautiful music, art, literature.
*  He doesn't like the fact that machines can recognize spoken language really well. He
*  personally doesn't like using speech recognition. But I don't think it bothers him to his core
*  because it's like, okay, that's not at the core of humanity. But it may be different for every person
*  what really they feel would usurp their humanity. And I think maybe it's a generational thing also.
*  Maybe our children or our children's children will be adapted. They'll adapt to these new
*  devices that can do all these tasks and say, yes, this thing is smarter than me in all these areas,
*  but that's great because it helps me. Looking at the broad history of our species,
*  why do you think so many humans have dreamed of creating artificial life and artificial intelligence
*  throughout the history of our civilization? So not just this century or the 20th century, but
*  really throughout many centuries that preceded it?
*  That's a really good question. And I have wondered about that because I myself was driven by curiosity
*  about my own thought processes and thought it would be fantastic to be able to get a computer to
*  mimic some of my thought processes. And I'm not sure why we're so driven. I think
*  we want to understand ourselves better. And we also want machines to do things for us.
*  But I don't know, there's something more to it because it's so deep in the kind of mythology
*  or the ethos of our species. And I don't think other species have this drive. So I don't know.
*  If you were to psychoanalyze yourself in your own interest in AI,
*  what excites you about creating intelligence? You said understanding our own cells?
*  Yeah, I think that's what drives me particularly. I'm really interested in human intelligence.
*  But I'm also interested in the phenomenon of intelligence more generally. And I don't
*  think humans are the only thing with intelligence or even animals. But I think intelligence
*  is a concept that encompasses a lot of complex systems. And if you think of things like insect
*  colonies or cellular processes or the immune system or all kinds of different biological
*  or even societal processes have as an emergent property some aspects of what we would call
*  intelligence. They have memory, they process information, they have memory,
*  they have goals, they accomplish their goals, etc. And to me, the question of what is this thing
*  we're talking about here was really fascinating to me. And exploring it using computers seemed to be
*  a good way to approach the question. So do you think kind of of intelligence,
*  do you think of our universe as a kind of hierarchy of complex systems and then intelligence is just
*  a property of any, you can look at any level and every level has some aspect of intelligence.
*  So we're just like one little speck in that giant hierarchy of complex systems.
*  I don't know if I would say any system like that has intelligence. But I guess what I want to,
*  I don't have a good enough definition of intelligence to say that.
*  So let me do sort of multiple choice I guess. So you said ant colonies. So are ant colonies
*  intelligent? Are the bacteria in our body intelligent? And then going to the physics world,
*  molecules and the behavior at the quantum level of electrons and so on. Are those kinds of systems,
*  do they possess intelligence? Where's the line that feels compelling to you?
*  I don't know. I mean, I think intelligence is a continuum. And I think that the ability to,
*  in some sense, have intention, have a goal, have some kind of self-awareness is part of it.
*  So I'm not sure if, it's hard to know where to draw that line. I think that's kind of a mystery.
*  But I wouldn't say that, say that the planets orbiting the sun is an intelligent system.
*  I mean, I would find that maybe not the right term to describe that. And there's all this debate in
*  the field of what's the right way to define intelligence? What's the right way to model
*  intelligence? Should we think about computation? Should we think about dynamics? And should we
*  think about free energy and all of that stuff? And I think that it's a fantastic time to be in
*  the field because there's so many questions and so much we don't understand. There's so much work to
*  do. So are we the most special kind of intelligence in this kind of, you said there's
*  a bunch of different elements and characteristics of intelligence systems and colonies.
*  Is human intelligence the thing in our brain? Is that the most interesting kind of intelligence
*  in this continuum? Well, it's interesting to us because it is us. I mean, interesting to me.
*  Yes. And because I'm part of the human. But to understanding the fundamentals of
*  intelligence, what I'm getting at is studying the human. It's sort of, if everything we've talked
*  about, what you talk about in your book, what just the AI field, this notion, yes, it's hard
*  to define, but it's usually talking about something that's very akin to human intelligence.
*  Yeah. To me, it is the most interesting because it's the most complex, I think. It's the most
*  self-aware. It's the only system, at least that I know of, that reflects on its own intelligence.
*  And you talk about the history of AI and us in terms of creating artificial intelligence,
*  being terrible at predicting the future with AI or with tech in general. So why do you think we're
*  so bad at predicting the future? Are we hopelessly bad? So no matter what, whether it's this decade
*  or the next few decades, every time we make a prediction, there's just no way of doing it well
*  or as the field matures, we'll be better and better at it. I believe as the field matures,
*  we will be better. And I think the reason that we've had so much trouble is that we have so little
*  understanding of our own intelligence. So there's the famous story about Marvin Minsky
*  assigning computer vision as a summer project to his undergrad students. And I believe that's
*  actually a true story. Yeah, there's a write-up on it that everyone should read. I think it's
*  like a proposal that describes everything that should be done in that project. It's hilarious
*  because it, I mean, you could explain it, but for my recollection, it describes basically all the
*  fundamental problems of computer vision, many of which still haven't been solved.
*  Yeah. And I don't know how far they really expect it to get, but I think that, and they're really,
*  Marvin Minsky is a super smart guy and very sophisticated thinker. But I think that no one
*  really understands or understood, still doesn't understand how complicated, how complex the things
*  that we do are because they're so invisible to us. To us, vision, being able to look out at the world
*  and describe what we see, that's just immediate. It feels like it's no work at all. So it didn't
*  seem like it would be that hard, but there's so much going on unconsciously, sort of invisible to
*  us that I think we overestimate how easy it will be to get computers to do it. And sort of, for me
*  to ask an unfair question, you've done research, you have thought about many different branches of
*  AI through this book, widespread looking at where AI has been and where it is today.
*  If you were to make a prediction, how many years from now would we as a society create something
*  that you would say achieved human level intelligence or superhuman level intelligence?
*  That is an unfair question.
*  A prediction that will most likely be wrong. But it's just your notion because-
*  Okay, I'll say more than a hundred years.
*  More than a hundred years.
*  And I quoted somebody in my book who said that human level intelligence is a hundred Nobel
*  prizes away, which I like because it's a nice way to sort of, it's a nice unit for prediction.
*  And it's like that many fantastic discoveries have to be made. And of course, there's no Nobel
*  prize in AI. Not yet, at least.
*  If we look at that hundred years, your sense is really the journey to intelligence has to go
*  through something more complicated that's akin to our own cognitive systems, understanding them,
*  being able to create them in the artificial systems as opposed to taking the machine learning
*  approaches of today and really scaling them and scaling them exponentially with both compute and
*  hardware and data.
*  That would be my guess. I think that in the sort of going along in the narrow AI,
*  that the current approaches will get better. I think there's some fundamental limits to how far
*  they're going to get. I might be wrong, but that's what I think. And there's some fundamental
*  weaknesses that they have that I talk about in the book that just comes from this approach of
*  supervised learning, requiring sort of feed forward networks and so on.
*  I don't think it's a sustainable approach to understanding the world.
*  Yeah, I'm personally torn on it. Everything you read about in the book and what we're talking
*  about now, I agree with you, but I'm more and more, depending on the day, first of all, I'm
*  deeply surprised by the success of machine learning and deep learning in general.
*  From the very beginning, it's really been my main focus of work. I'm just surprised how far it gets.
*  I also think we're really early on in these efforts of these narrow AI. I think there will
*  be a lot of surprises of how far it gets. I think we'll be extremely impressed. My sense is
*  everything I've seen so far, and we'll talk about autonomous driving and so on, I think we can get
*  really far. But I also have a sense that we will discover, just like you said, is that even though
*  we'll get really far in order to create something like our own intelligence, it's actually much
*  farther than we realize. I think these methods are a lot more powerful than people give them
*  credit for actually. Of course, there's the media hype, but I think there's a lot of researchers
*  in the community, especially not undergrads, but people who have been in AI, they're skeptical
*  about how far deep learning can get. I'm more and more thinking that it can actually get farther
*  than they'll realize. It's certainly possible. One thing that surprised me when I was writing
*  the book is how far apart different people are in the field are on their opinion of how far the
*  field has come and what is accomplished and what's going to happen next. What's your sense of the
*  different, who are the different people, groups, mindsets, thoughts in the community about where
*  AI is today? Yeah, they're all over the place. There's the singularity transhumanism group.
*  I don't know exactly how to characterize that approach.
*  The great first world. Yeah. The exponential progress. We're on the
*  almost at the hugely accelerating part of the exponential. In the next 30 years, we're going to
*  see super intelligent AI and all that, and we'll be able to upload our brains and that. There's that
*  kind of extreme view that most people who work in AI don't have. They disagree with that.
*  But there are people who are maybe aren't singularity people, but they do think that the
*  current approach of deep learning is going to scale and is going to go all the way basically
*  and take us to true AI or human level AI or whatever you want to call it.
*  There's quite a few of them. A lot of the people I've met who work at
*  big tech companies in AI groups have this view that we're really not that far.
*  Just to linger on that point, if I can take as an example, like Yann LeCun, I don't know if you know
*  about his work and so on. Yeah. I do. He believes that there's a bunch of breakthroughs,
*  Nobel prizes that are needed still. But I think he thinks those breakthroughs will be built on top of
*  deep learning. And then there's some people who think we need to kind of put deep learning to
*  the side a little bit as just one module that's helpful in the bigger cognitive framework.
*  Right. So I think from what I understand, Yann LeCun is
*  rightly saying supervised learning is not sustainable. We have to figure out how to
*  do unsupervised learning, that that's going to be the key. And I think that's probably true.
*  I think unsupervised learning is going to be harder than people think. I mean, the way that
*  we humans do it. Then there's the opposing view. There's the Gary Marcus kind of hybrid view where
*  deep learning is one part, but we need to bring back kind of these symbolic approaches and combine
*  them. Of course, no one knows how to do that very well.
*  Which is the more important part to emphasize. And how do they fit together? What's the foundation?
*  What's the thing that's on top? What's the cake? What's the icing?
*  Right. Then there's people pushing different things. There's the people, the causality people
*  who say, you know, deep learning as it's formulated today completely lacks any notion of causality.
*  Any notion of causality and that's dooms it. And therefore we have to somehow give it
*  some kind of notion of causality. There's a lot of push from the more cognitive science crowd saying,
*  we have to look at developmental learning. We have to look at how babies learn. We have to look at
*  intuitive physics, all these things we know about physics. And as somebody kind of quipped,
*  we also have to teach machines intuitive metaphysics, which means like objects exist.
*  Causality exists. You know, these things that maybe we're born with. I don't know.
*  That they don't have the machines don't have any of that. You know, they look at a group of pixels
*  and they, maybe they get 10 million examples, but they, they can't necessarily learn that there are
*  objects in the world. So there's just a lot of pieces of the puzzle that people are promoting.
*  And with different opinions of like how, how, how important they are and how close we are to
*  being able to put them all together to create general intelligence.
*  Looking at this broad field, what do you take away from it? Who's the most impressive?
*  Is it the cognitive folks, the Gary Marcus camp, the Yon camp, unsupervised,
*  and they're self supervised. There's the supervisors and then there's the engineers
*  who are actually building systems. You have sort of the Andre Carpathy at Tesla building actual,
*  you know, it's not philosophy. It's real systems that operate in the real world.
*  What, yeah, what do you take away from all this beautiful variety?
*  I don't know if, you know, these, these different views are not necessarily mutually exclusive. And
*  I think people like Jan LeCun agrees with the developmental psychology, causality, intuitive
*  physics, et cetera. But he still thinks that it's learning like end to end learning is the way to go.
*  Will take us perhaps all the way. Yeah. And that we don't need, there's no
*  sort of innate stuff that has to get built in. This is, you know, it's because it's a hard problem.
*  I personally, you know, I'm very sympathetic to the cognitive science side, because that's kind
*  of where I came in to the field. I've become more and more sort of an embodiment adherent saying
*  that, you know, without having a body, it's going to be very hard to learn what we need to learn
*  about the world. That's definitely something I'd love to talk about in a little bit. To step into
*  the cognitive world, then if you don't mind, because you've done so many interesting things.
*  If you look to copycat, taking a couple of decades, step back, you, Douglas Hofstadter and
*  others have created and developed copycat more than 30 years ago. That's painful to hear.
*  What is it? What is, what is copycat? It's a program that makes analogies in an idealized
*  domain, idealized world of letter strings. So as you say, 30 years ago, wow. So I started working
*  on it when I started grad school in 1984. Wow. Dates me. And it's based on Doug Hofstadter's
*  ideas that about, that analogy is really a core aspect of thinking. I remember he has a really
*  nice quote in the book by himself and Emmanuel Sander called surfaces and essences. I don't know
*  if you've seen that book, but it's about analogy. He says, without concepts, there can be no thought
*  and without analogies, there can be no concepts. So the view is that analogy is not just this kind
*  of reasoning technique where we go, shoe is to foot, glove is to what? These kinds of things
*  that we have on IQ tests or whatever. But that it's much deeper, it's much more pervasive in
*  everything we do, in our language, our thinking, our perception. So he had a view that was a very
*  active perception idea. So the idea was that instead of having a passive network in which you
*  have input that's being processed through these feed forward layers, and then there's an output
*  at the end, that perception is really a dynamic process where our eyes are moving around and
*  they're getting information. And that information is feeding back to what we look at next influences
*  what we look at next and how we look at it. And so CopyCat was trying to do that, kind of simulate
*  that kind of idea where you have these agents, it was kind of an agent based system and you have
*  these agents that are picking things to look at and deciding whether they were interesting or not
*  and whether they should be looked at more and that would influence other agents.
*  And how do they interact?
*  So they interacted through this global kind of what we call the workspace. So it's actually
*  inspired by the old blackboard systems where you would have agents that post information on a
*  blackboard, a common blackboard. This is like old, very old fashioned AI.
*  Is that, are we talking about like in physical space? Is this a computer program?
*  It's a computer program.
*  So agents posting concepts on a blackboard?
*  Yeah, we called it a workspace. And the workspace is a data structure. The agents are little pieces
*  of code that you could think of them as little detectors or little filters that say, I'm going
*  to pick this place to look and I'm going to look for a certain thing and is this the thing I
*  think is important? Is it there? So it's almost like a convolution in a way, except a little bit.
*  More general and saying, and then highlighting it in the workspace.
*  Once it's in the workspace, how do the things that are highlighted relate to each other?
*  Like what's this?
*  So there's different kinds of agents that can build connections between different things.
*  So just to give you a concrete example, what CopyCat did was it made analogies between strings of
*  letters. So here's an example. ABC changes to ABD. What does IJK change to? And the program had some
*  prior knowledge about the alphabet, knew the sequence of the alphabet. It had a concept of
*  letter, successor of letter. It had concepts of sameness. So it has some innate things programmed
*  in. But then it could do things like say, discover that ABC is a group of letters in succession.
*  And then an agent can mark that.
*  So the idea that there could be a sequence of letters, is that a new concept that's formed or
*  that's a concept that's innate?
*  That's a concept that's innate.
*  Sort of, can you form new concepts or are all concepts innate?
*  So in this program, all the concepts of the program were innate.
*  Obviously, that limits it quite a bit. But what we were trying to do is say, suppose you have some
*  innate concepts, how do you flexibly apply them to new situations? And how do you make analogies?
*  Let's step back for a second. So I really like that quote. That you said, without concepts,
*  there can be no thought. And without analogies, there can be no concepts. In a Santa Fe
*  presentation, you said that it should be one of the mantras of AI.
*  Yes.
*  And that you also yourself said, how to form and fluidly use concepts is the most important open
*  problem in AI.
*  Yes.
*  How to form and fluidly use concepts is the most important open problem in AI.
*  So what is a concept and what is an analogy?
*  A concept is in some sense a fundamental unit of thought. So say we have a concept of
*  a dog. And a concept is embedded in a whole space of concepts. So that there are certain
*  concepts that are closer to it or farther away from it.
*  Are these concepts, are they really fundamental, like we mentioned, innate, almost like axiomatic,
*  very basic, and then there's other stuff built on top of it? Or does this include everything?
*  Are there complicated...
*  You can certainly form new concepts.
*  Right. I guess that's the question I'm asking. Can you form new concepts that are
*  complex combinations of other concepts?
*  Yes, absolutely. And that's kind of what we do in learning.
*  And then what's the role of analogies in that?
*  So analogy is when you recognize that one situation is essentially the same as another
*  situation. And essentially is kind of the key word there, because it's not the same.
*  So if I say, last week I did a podcast interview, actually like three days ago,
*  in Washington, DC. And that situation was very similar to this situation, although it wasn't
*  exactly the same. It was a different person sitting across from me. We had different kinds
*  of microphones. The questions were different. The building was different. There's all kinds
*  of different things, but really it was analogous. Or I can say, so doing a podcast interview, that's
*  a new concept. I never had that concept before this year, essentially. And I can make an analogy
*  with it like being interviewed for a news article in a newspaper. And I can say, well, you play the
*  same role that the newspaper reporter played. It's not exactly the same, because maybe they
*  actually emailed me some written questions rather than talking. And the written questions
*  are analogous to your spoken questions. There's just all kinds of similarities.
*  And this somehow probably connects to conversations you have over Thanksgiving dinner,
*  just general conversations. There's a thread you can probably take that just stretches out
*  in all aspects of life that connect to this podcast. I mean, conversations between humans.
*  Sure. And if I go and tell a friend of mine about this podcast interview, my friend might say,
*  oh, the same thing happened to me. Let's say you ask me some really hard question
*  and I have trouble answering it. My friend could say, the same thing happened to me,
*  but it wasn't a podcast interview. It was a completely different situation.
*  And yet my friend is seeing essentially the same thing. We say that very fluidly,
*  the same thing happened to me. Essentially the same thing.
*  But we don't even say that, right? We just say the same thing.
*  We imply it, yes. Yeah. And the view that kind of went into,
*  say, copycat, that whole thing is that that act of saying the same thing happened to me is making an
*  analogy. And in some sense, that's what's underlies all of our concepts.
*  Why do you think analogy making that you're describing is so fundamental to cognition?
*  It seems like it's the main element action of what we think of as cognition.
*  Yeah. So it can be argued that all of this generalization we do of concepts
*  and recognizing concepts in different situations is done by analogy. Every time I'm recognizing
*  that, say, you're a person, that's by analogy because I have this concept of what person is
*  and I'm applying it to you. And every time I recognize a new situation, like one of the things
*  I talked about in the book was the concept of walking a dog, that that's actually making an
*  analogy because all of the details are very different. So reasoning could be reduced down
*  to sensory analogy making. So all the things we think of as like, yeah, like you said, perception.
*  So what's perception is taking raw sensory input and it's somehow integrating into our
*  understanding of the world, updating the understanding and all of that
*  as just this giant mess of analogies that are being made. I think so, yeah.
*  If you just linger on it a little bit, like what do you think it takes to engineer a process like
*  that for us in our artificial systems? We need to understand better, I think, how
*  we do it, how humans do it. And it comes down to internal models, I think. People talk a lot about
*  mental models, that concepts are mental models. In my head, I can do a simulation
*  of a situation like walking a dog. And there's some work in psychology that promotes this idea
*  that all of concepts are really mental simulations, that whenever you encounter a concept or situation
*  in the world or you read about it or whatever, you do some kind of mental simulation that
*  allows you to predict what's going to happen, to develop expectations of what's going to happen.
*  So that's the kind of structure I think we need, is that kind of mental model that
*  and in our brains, somehow these mental models are very much interconnected.
*  Again, so a lot of stuff we're talking about are essentially open problems, right? So if I ask a
*  question, I don't mean that you would know the answer, only just hypothesizing. But how big do
*  you think is the network graph data structure of concepts that's in our head? If we're trying to
*  build that ourselves, that's one of the things we take for granted. That's why we take common
*  sense for granted. We think common sense is trivial. But how big of a thing of concepts is
*  that underlies what we think of as common sense, for example?
*  Yeah, I don't know. And I don't even know what units to measure it in.
*  That's beautifully put, right?
*  But it's really hard to know. We have what, 100 billion neurons or something, I don't know.
*  And they're connected via trillions of synapses. And there's all this chemical processing going
*  on. There's just a lot of capacity for stuff. And their information's encoded in different
*  ways in the brain. It's encoded in chemical interactions. It's encoded in electric firing
*  and firing rates. And nobody really knows how it's encoded. But it just seems like there's
*  a huge amount of capacity. So I think it's huge. It's just enormous. And it's amazing how much stuff
*  we know.
*  But we know and not just know facts, but it's all integrated into this thing that we can make
*  analogies with. There's a dream of semantic web. There's a lot of dreams from expert systems of
*  building giant knowledge bases. Do you see a hope for these kinds of approaches of converting
*  Wikipedia into something that could be used in analogy making?
*  Sure. And I think people have made some progress along those lines. People have been working on
*  this for a long time. But the problem is, and this I think is the problem of common sense.
*  People have been trying to get these common sense networks. Here at MIT, there's this concept net
*  project. But the problem is that, as I said, most of the knowledge that we have is invisible to us.
*  It's not in Wikipedia. It's very basic things about intuitive physics, intuitive psychology,
*  intuitive metaphysics, all that stuff.
*  If you were to create a website that described intuitive physics, intuitive psychology,
*  would it be bigger or smaller than Wikipedia? What do you think?
*  I guess describe to whom? I'm sorry.
*  No, that's really good. That's exactly right.
*  That's a hard question because how do you represent that knowledge is the question.
*  I can certainly write down F equals MA and Newton's laws and a lot of physics can be deduced from that.
*  But that's probably not the best representation of that knowledge for doing
*  the kinds of reasoning we want a machine to do. So I don't know. It's impossible to say now.
*  And the projects like there's the famous psych project that Douglas Lenat did that was trying-
*  That's still going?
*  I think it's still going. And the idea was to try and encode all of common sense knowledge,
*  including all this invisible knowledge in some kind of logical representation.
*  And it just never, I think, could do any of the things that he was hoping it could do
*  because that's just the wrong approach.
*  Of course, that's what they always say. And then the history books will say, well,
*  the psych project finally found a breakthrough in 2058 or something.
*  So much progress has been made in just a few decades that who knows what the next breakthroughs
*  will be. It's certainly a compelling notion what the psych project stands for.
*  I think Lenat was one of the earliest people to say common sense is what we need. That's what we
*  need. All this expert system stuff, that is not going to get you to AI. You need common sense.
*  And he basically gave up his whole academic career to go pursue that. And I totally admire that. But
*  I think that the approach itself will not in 2020 or 2020 or whatever.
*  What do you think is wrong with the approach? What kind of approach might be successful?
*  Well, I knew that.
*  Nobody knows the answer, right?
*  If I knew that. One of my talks, one of the people in the audience, this is a public lecture,
*  one of the people in the audience said, what AI companies are you investing in?
*  I'm a college professor for one thing, so I don't have a lot of extra funds to invest. But also,
*  no one knows what's going to work in AI. That's the problem.
*  Let me ask another impossible question in case you have a sense. In terms of data structures that
*  will store this kind of information, do you think they've been invented yet,
*  both in hardware and software? Or is something else needs to be, are we totally, you know?
*  I think something else has to be invented. That's my guess.
*  Is the breakthroughs that's most promising, would that be in hardware or software?
*  Do you think we can get far with the current computers? Or do we need to do something?
*  I don't know if Turing computation is going to be sufficient. Probably.
*  I would guess it will. I don't see any reason why we need anything else. So in that sense,
*  we have invented the hardware we need, but we just need to make it faster and bigger.
*  We need to figure out the right algorithms and the right sort of architecture.
*  Turing, that's a very mathematical notion. When we have to build intelligence,
*  it's now an engineering notion where you throw all that stuff.
*  Well, I guess it is a question. People have brought up this question, you know,
*  when you asked about will our current hardware work? Well, Turing computation says that our
*  current hardware is in principle a Turing machine, right? So all we have to do is make it faster and
*  bigger. But there have been people like Roger Penrose, if you might remember, that he said
*  Turing machines cannot produce intelligence because intelligence requires continuous valued
*  numbers. I mean, that was sort of my reading of his argument and quantum mechanics and what else,
*  whatever. But I don't see any evidence for that, that we need new computation paradigms.
*  But I don't know if we're, you know, I don't think we're going to be able to
*  scale up our current approaches to programming these computers.
*  What is your hope for approaches like CopyCAD or other cognitive architectures? I've talked to the
*  creator of SOAR, for example. I've used Actar myself. I don't know if you're familiar with it.
*  Yeah, I am. What do you think is, what's your hope of approaches like that in helping develop
*  systems of greater and greater intelligence in the coming decades?
*  Well, that's what I'm working on now is trying to take some of those ideas and extending it. So I
*  think there are some really promising approaches that are going on now that have to do with more
*  active generative models. So this is the idea of this simulation in your head of a concept.
*  When you're perceiving a new situation, you have some simulations in your head. Those are generative
*  models. They're generating your expectations. They're generating predictions.
*  So that's part of a perception. You have a method model that generates a prediction,
*  then you compare it with, and then the difference in power forms.
*  And you also, that generative model is telling you where to look and what to look at and what
*  to pay attention to. And I think it affects your perception. It's not that just you compare it with
*  your perception. It becomes your perception in a way. It's kind of a mixture of the bottom-up
*  information coming from the world and your top-down
*  model being imposed on the world is what becomes your perception.
*  So your hope is something like that can improve perception systems and that they can understand
*  things better. Yes.
*  Understand things. Yes.
*  What's the analogy-making step there?
*  Well, there the idea is that you have this pretty complicated conceptual space. You can talk about a
*  semantic network or something like that with these different kinds of concept models in your brain
*  that are connected. So let's take the example of walking a dog. So we were talking about that.
*  Okay. Let's say I see someone out on the street walking a cat. Some people walk their cats,
*  I guess. It seems like a bad idea, but- Yeah.
*  Good thing. So my model, there's connections between my
*  model of a dog and model of a cat. And I can immediately see the analogy
*  that those are analogous situations, but I can also see the differences and that tells me what to
*  expect. Also, I have a new situation. So another example with the walking the dog thing is
*  sometimes I see people riding their bikes holding a leash and the dog's running alongside.
*  I know that I recognize that as a dog walking situation, even though the person's not
*  walking and the dog's not walking. Because I have these models that say, okay,
*  riding a bike is similar to walking or it's connected, it's a means of transportation,
*  but because they have their dog there, I assume they're not going to work, but they're going out
*  for exercise. These analogies help me to figure out what's going on, what's likely.
*  But these analogies are very human interpretable. So that's that kind of space. And then you look
*  at something like the current deep learning approaches, they help you to take raw
*  sensory information and to sort of automatically build up hierarchies of,
*  you can even call them concepts. They're just not human interpretable concepts.
*  What's the link here? Do you hope it's sort of the hybrid system question? How do you think
*  that two can start to meet each other? What's the value of learning in this systems of forming,
*  of analogy making? The original goal of deep learning in at least visual perception was that
*  you would get the system to learn to extract features at these different levels of complexity.
*  So maybe edge detection, and that would lead into learning simple combinations of edges and then
*  more complex shapes and then whole objects or faces. And this was based on the ideas of
*  the neuroscientists Hubel and Weasel who had seen laid out this kind of structure in brain.
*  And I think that's right to some extent. Of course, people have found that the whole story
*  is a little more complex than that. And the brain of course always is, and there's a lot of feedback.
*  So I see that as absolutely a good brain inspired approach to some aspects of perception.
*  But one thing that it's lacking, for example, is all of that feedback,
*  which is extremely important. The interactive element that you mentioned
*  the expectation, the conceptual level.
*  The expectation, the perception, and just going back and forth.
*  So that is extremely important. And one thing about deep neural networks is that in a given
*  situation, they're trained, they get these weights and everything, but then now I give them a new
*  a new image, let's say. They treat every part of the image in the same way. They apply the same
*  filters at each layer to all parts of the image. There's no feedback to say like,
*  oh, this part of the image is irrelevant. I shouldn't care about this part of the image.
*  Or this part of the image is the most important part. And that's kind of what we humans are able
*  to do because we have these conceptual expectations.
*  So there's, by the way, a little bit of work in that. There's certainly a lot more in
*  what's under the called attention in natural language processing knowledge.
*  That's exceptionally powerful. And it's a very, just as you say, it's a really powerful idea.
*  But again, in sort of machine learning, it all kind of operates in an automated way.
*  That's not human.
*  It's not also, okay. So that, yeah, right. It's not dynamic. I mean, in the sense that as
*  a perception of a new example is being processed, those attentions weights don't change.
*  Right. So, I mean, there's a kind of notion that there's not a memory.
*  So you're not aggregating the idea of like this mental model.
*  Yes.
*  That seems to be a fundamental idea. There's not a really powerful,
*  I mean, there's some stuff with memory, but there's not a powerful way to represent
*  the world in some sort of way that's deeper than, I mean, it's so difficult because,
*  you know, neural networks do represent the world. They do have a mental model.
*  Right. But it just seems to be shallow.
*  It's hard to criticize them at the fundamental level, to me at least. It's easy to criticize
*  and will look like exactly what you're saying. Mental models sort of almost from a put a
*  psychology hat on say, look, these networks are clearly not able to achieve what we humans do
*  with forming mental models, but the analogy making so on. But that doesn't mean that they
*  fundamentally cannot do that. It's very difficult to say that. I mean, at least to me,
*  do you have a notion that the learning approach is really, I mean, they're going to,
*  not only are they limited today, but they will forever be limited in being able to construct
*  such mental models.
*  I think the idea of the dynamic perception is key here. The idea that moving your eyes around
*  and getting feedback and that's something that, you know, there's been some models like that.
*  There's certainly recurrent neural networks that operate over several time steps. And,
*  the problem is that the actual, the recurrence is, you know, basically the feedback is
*  at the next time step is the entire hidden state of the network, which is,
*  it turns out that that doesn't work very well.
*  But see, the thing I'm saying is, mathematically speaking, it has the information
*  in that recurrence to capture everything. It just doesn't seem to work.
*  Yeah. Right.
*  So, you know, it's like, it's the same Turing machine question, right? Yeah, maybe theoretically,
*  computers, anything that's Turing, a universal Turing machine can be intelligent, but practically,
*  the architecture might be very specific kind of architecture to be able to create it. So,
*  I guess to sort of ask almost the same question again is, how big of a role
*  do you think deep learning needs, will play or needs to play in the future?
*  I think that deep learning as it currently exists, you know, will play,
*  that kind of thing will play some role. And, but I think that there's a lot more going on
*  in perception, but who knows, you know, the definition of deep learning, I mean,
*  that's another thing.
*  I think that deep learning is a lot more important than deep learning.
*  Perception, but who knows, you know, the definition of deep learning,
*  I mean, it's pretty broad. It's kind of an umbrella for a lot of different things.
*  What I mean is purely sort of neural networks.
*  Yeah, and a feed forward neural networks.
*  Essentially, or there could be recurrence, but yeah, sometimes it feels like, for example,
*  I talked to Gary Marcus, it feels like the criticism of deep learning is kind of like
*  birds criticizing airplanes for not flying well, or that they're not really flying.
*  Do you think deep learning, do you think it could go all the way like Yalda thinks?
*  Do you think that, yeah, the brute force learning approach can go all the way?
*  I don't think so. No. I mean, I think it's an open question, but I tend to be on the
*  innateness side that there's some things that we've been evolved to be able to learn,
*  and that learning just can't happen without them.
*  So one example, here's an example I had in the book that I think is useful to me,
*  at least, in thinking about this. So this has to do with the Deep Minds Atari game playing program,
*  and it learned to play these Atari video games just by getting input from the pixels of the screen,
*  and it learned to play the game Breakout 1000% better than humans. That was one of their results,
*  and it was great, and it learned this thing where it tunneled through the side of the bricks in the
*  Breakout game, and the ball could bounce off the ceiling and then just wipe out bricks.
*  Okay. So there was a group who did an experiment where they took the paddle that you move with
*  the joystick and moved it up two pixels or something like that, and then they looked at
*  a deep Q learning system that had been trained on Breakout and said, could it now transfer its
*  learning to this new version of the game? Of course, a human could, and it couldn't.
*  Maybe that's not surprising, but I guess the point is it hadn't learned the concept of a paddle.
*  It hadn't learned the concept of a ball or the concept of tunneling. It was learning something.
*  We, looking at it, anthropomorphized it and said, oh, here's what it's doing and the way
*  we describe it, but it actually didn't learn those concepts. And so because it didn't learn
*  those concepts, it couldn't make this transfer. Yes. So that's a beautiful statement, but at the
*  same time, by moving the paddle, we also anthropomorphize flaws to inject into the system
*  that will then flip how impressed we are by it. What I mean by that is, to me, the Atari games
*  were, to me, deeply impressive that that was possible at all. So I have to first pause on
*  that and people should look at that, just like the game of Go, which is fundamentally different
*  to me than what Deep Blue did. Even though there's still Monte Carlo, there's still Tree Search,
*  it's just everything DeepMind has done in terms of learning, however limited it is,
*  is still deeply surprising to me. Yeah, I'm not trying to say that what they
*  did wasn't impressive. I think it was incredibly impressive. To me, it's interesting.
*  Is moving the board just another thing that needs to be learned? So like we've been able to, maybe,
*  maybe, been able to, through the current neural networks, learn very basic concepts that are not
*  enough to do this general reasoning. And then maybe with more data, I mean, the data that,
*  you know, the interesting thing about the examples that you talk about beautifully is they,
*  it's often flaws of the data. Well, that's the question. I mean,
*  I think that is the key question, whether it's a flaw of the data or not.
*  The reason I brought up this example was because you were asking, do I think that,
*  you know, learning from data could go all the way? And this was why I brought up the example,
*  because I think, and this is not at all to take away from the impressive work that they did,
*  but it's to say that when we look at what these systems learn,
*  do they learn the human, the things that we humans consider to be the relevant concepts?
*  And in that example, it didn't. Sure, if you train it on moving, you know, the paddle being
*  in different places, maybe it could deal with, maybe it would learn that concept. I'm not totally
*  sure. But the question is, you know, scaling that up to more complicated worlds, to what extent
*  could a machine that only gets this very raw data learn to divide up the world into relevant concepts?
*  And I don't know the answer, but I would bet that without some innate notion that it can't do it.
*  Yeah. Ten years ago, I 100% agree with you as the most experts in AI system, but now I have
*  a glimmer of hope. Okay, that's fair enough.
*  And I think that's what deep learning did in the community is, no, no, if I had to bet all my money,
*  100% deep learning will not take us all the way. But there's still other, it's still,
*  I was so personally sort of surprised by the Atari games, by Go, by the power of self-play,
*  of just game playing against each other, that I was like many other times, just humbled of how
*  little I know about what's possible in science approaches. Yeah, I think fair enough. Self-play
*  is amazingly powerful. And that goes way back to Arthur Samuel with his checker plane program,
*  which was brilliant and surprising that it did so well.
*  So just for fun, let me ask you on the topic of autonomous vehicles. It's the area that I work
*  at least these days most closely on, and it's also area that I think is a good example that you use
*  as sort of an example of things we as humans don't always realize how hard it is to do. It's like the
*  constant trend in AI, or the different problems that we think are easy when we first try them
*  and then realize how hard it is. Okay. So why you've talked about this autonomous driving being a
*  difficult problem, more difficult than we realize humans give it credit for. Why is it so difficult?
*  What are the most difficult parts in your view?
*  I think it's difficult because of the world is so open-ended as to what kinds of things can happen.
*  So you have sort of what normally happens, which is just you drive along and nothing
*  surprising happens. And autonomous vehicles can do the ones we have now,
*  evidently can do really well on most normal situations as long as the weather is reasonably
*  good and everything. But if some, we have this notion of edge case or things in the tail of the
*  distribution called the long tail problem, which says that there's so many possible things that
*  can happen that was not in the training data of the machine that it won't be able to handle it
*  because it doesn't have common sense. It's the old, the paddle moved.
*  Yeah, it's the paddle moved problem. Right. And so my understanding, and you probably are more of
*  an expert than I am on this, is that current self-driving car vision systems have problems with
*  obstacles, meaning that they don't know which obstacles, which quote unquote obstacles they
*  should stop for and which ones they shouldn't stop for. And so a lot of times I read that they
*  tend to slam on the brakes quite a bit. And the most common accidents with self-driving cars are
*  people rear-ending them because they weren't expecting the car to stop.
*  Yeah. So there's a lot of interesting questions there. Because you mentioned two things. So one
*  is the problem of perception, of understanding, of interpreting the objects that are detected
*  correctly. And the other one is more like the policy, the action that you take, how you respond
*  to it. So a lot of the cars breaking is a kind of notion of, to clarify, there's a lot of different
*  kinds of things that are people calling autonomous vehicles. But the L4 vehicles with a safety driver
*  are the ones like Waymo and Cruze and all those companies, they tend to be very conservative and
*  cautious. So they tend to be very, very afraid of hurting anything or anyone and getting in any kind
*  of accidents. So their policy is very kind of, that results in being exceptionally responsive
*  to anything that could possibly be an obstacle, right? Right. Which the human drivers around it,
*  it behaves unpredictably. That's not a very human thing to do, caution. That's not the thing we're
*  good at, especially in driving. We're in a hurry, often angry, and et cetera, especially in Boston.
*  So, and then there's sort of another, and a lot of times that's, machine learning is not a huge part
*  of that. It's becoming more and more unclear to me how much, you know, sort of speaking to public
*  information, because a lot of companies say they're doing deep learning and machine learning just to
*  attract good candidates. The reality is, in many cases, it's still not a huge part of the perception.
*  There's lidar, there's other sensors that are much more reliable for optical detection. And then
*  there's Tesla approach, which is vision only. And there's, I think a few companies doing that,
*  but Tesla most sort of famously pushing that forward. And that's because the lidar is too
*  expensive, right? Well, I mean, yes, but I would say if you were to for free give to every Tesla
*  vehicle, Elon Musk fundamentally believes that lidar is a crutch, right? Fantasy said that.
*  If you want to solve the problem of machine learning, lidar should not be the primary sensor,
*  is the belief. The camera contains a lot more information. So if you want to learn,
*  you want that information. But if you want not to hit obstacles, you want lidar.
*  Right. It's sort of this weird trade off because, yeah, so what Tesla vehicles have a lot of,
*  which is really the thing, the primary fallback sensor is radar, which is a very crude version
*  of lidar. It's a good detector of obstacles, except when those things are standing, right?
*  The stopped vehicle. Right. That's why it had problems with crashing into stop fire trucks.
*  Stop fire trucks. That's right. So the hope there is that the vision sensor would somehow
*  catch that. And for, there's a lot of problems with perception. They are doing actually some
*  incredible stuff in the, almost like an active learning space where it's constantly taking edge
*  cases and pulling back in. There's this data pipeline. Another aspect that is really important
*  that people are studying now is called multitask learning, which is sort of breaking apart this
*  problem, whatever the problem is, in this case, driving into dozens or hundreds of little problems
*  that you can turn into learning problems. So this giant pipeline, it's kind of interesting. I've
*  been skeptical from the very beginning, but become less and less skeptical over time,
*  how much of driving can be learned. I still think it's much farther than the CEO of that
*  particular company thinks it will be, but it's constantly surprising that through good engineering
*  and data collection and active selection of data, how you can attack that long tail. And it's an
*  interesting open question that you're absolutely right. There's a much longer tail and all these
*  edge cases that we don't think about, but it's a fascinating question that applies to natural
*  language in all spaces. How big is that long tail? Right. And I mean, not to linger on the point,
*  but what's your sense in driving in these practical problems of the human experience?
*  Can it be learned? So the current, what are your thoughts on sort of Elon Musk's thought,
*  let's forget the thing that he says it'd be solved in a year, but can it be solved in
*  a reasonable timeline or do fundamentally other methods need to be invented?
*  So I don't, I think that ultimately driving, so it's a trade off in a way, being able to drive
*  and deal with any situation that comes up does require kind of full human intelligence. And even
*  in humans aren't intelligent enough to do it because humans, I mean, most human accidents
*  are because the human wasn't paying attention or the humans drunk or whatever.
*  And not because they weren't intelligent.
*  And not because they weren't intelligent enough, right. Whereas the human experience is
*  the accidents with autonomous vehicles is because they weren't intelligent enough.
*  They're always paying attention.
*  Yeah, they're always paying attention. So it's a trade off, you know, and I think
*  that it's a very fair thing to say that autonomous vehicles will be ultimately safer than humans
*  because humans are very unsafe. It's kind of a low bar.
*  But just like you said, I think humans got a better rap, right? Because we're really good at
*  the common sense thing. Yeah, we're great at the common sense thing. We're bad at the paying
*  attention thing, especially when we're, you know, driving is kind of boring and we have these phones
*  to play with and everything. But I think what's going to happen is that for many reasons, not just
*  AI reasons, but also like legal and other reasons that the definition of self-driving is going to
*  change or autonomous is going to change. It's not going to be just, I'm going to go to sleep in the
*  back and you just drive me anywhere. It's going to be more certain areas are going to be instrumented
*  to have the sensors and the mapping and all the stuff you need for that. That the autonomous cars
*  won't have to have full common sense and they'll do just fine in those areas as long as pedestrians
*  don't mess with them too much. That's another question. But I don't think we will have fully
*  autonomous self-driving in the way that like most the average person thinks of it for a very long
*  time. And just to reiterate, this is the interesting open question that I think I agree with you on is
*  to solve fully autonomous driving, you have to be able to engineer in common sense. Yes.
*  I think it's an important thing to hear and think about. I hope that's wrong, but I currently
*  agree with you that unfortunately you do have to have to be more specific, these
*  deep understandings of physics and of the way this world works and also human dynamics.
*  I can mention pedestrians and cyclists, actually that's whatever that nonverbal communication is,
*  some people call it, there's that dynamic that is also part of this common sense.
*  Right. We humans are pretty good at predicting what other humans are going to do.
*  And how our actions impact the behaviors of this weird game theoretic dance that we're good at
*  somehow. And the funny thing is, because I've watched countless hours of pedestrian video
*  and talked to people, we humans are also really bad at articulating the knowledge we have.
*  Right. Which has been a huge challenge.
*  Yes. So you've mentioned embodied intelligence. What do you think it takes to build a system of
*  human level intelligence? Does it need to have a body? I'm not sure, but I'm coming around to that
*  more and more. And what does it mean to be, I don't mean to keep bringing up Yalan Kun.
*  He looms very large.
*  He certainly has a large personality. Yes. He thinks that the system needs to be grounded,
*  meaning it needs to sort of be able to interact with reality, but doesn't think it necessarily
*  needs to have a body. So when you think of- So what's the difference?
*  I guess I want to ask, when you mean body, do you mean you have to be able to play with the world?
*  Or do you also mean like there's a body that you have to preserve?
*  That's a good question. I haven't really thought about that, but I think both, I would guess,
*  because I think intelligence, it's so hard to separate it from our desire for self-preservation,
*  our emotions, our all that non-rational stuff that kind of gets in the way of
*  logical thinking. Because the way, if we're talking about human intelligence or human level
*  intelligence, whatever that means, a huge part of it is social. We were evolved to be social
*  and to deal with other people. That's just so ingrained in us that it's hard to separate
*  intelligence from that. I think AI for the last 70 years, or however long it's been around,
*  it has largely been separated. There's this idea that it's kind of very Cartesian. There's this
*  thinking thing that we're trying to create, but we don't care about all this other stuff.
*  I think the other stuff is very fundamental.
*  There's an idea that things like emotion get in the way of intelligence.
*  As opposed to being an integral part of it.
*  Integral part of it. I'm Russian, so I romanticize the notions of emotion and suffering and all that
*  kind of fear of mortality, those kinds of things. In AI, especially...
*  By the way, did you see that there was this recent thing going around the internet?
*  I think he's a Russian or some Slavic that had written this thing,
*  the idea of super intelligence. I forgot, maybe he's Polish. Anyway, so he had all these arguments
*  and one was the argument from Slavic pessimism.
*  Do you remember what the argument is?
*  It's like nothing ever works. Everything sucks.
*  What do you think is the role? That's such a fascinating idea that what we perceive as
*  the limits of the human mind, which is emotion and fear and all those kinds of things,
*  are integral to intelligence. Could you elaborate on that? Why is that important, do you think,
*  for human level intelligence?
*  At least the way the humans work, it's a big part of how it affects how we perceive the world.
*  It affects how we make decisions about the world. It affects how we interact with other people.
*  It affects our understanding of other people. For me to understand
*  what you're likely to do, I need to have a theory of mind and that's very much a theory of emotions
*  and motivations and goals. To understand that, we have this whole system of
*  mirror neurons. I understand your motivations through simulating it myself. It's not something
*  that I can prove that's necessary, but it seems very likely.
*  You've written the op-ed in the New York Times titled,
*  We Shouldn't Be Scared by Superintelligent AI. It criticized a little bit Stuart Russell and Nick
*  Bostrom. Can you try to summarize that article's key ideas?
*  It was spurred by an earlier New York Times op-ed by Stuart Russell, which was summarizing his book
*  called Human Compatible. The article was saying, if we have superintelligent AI,
*  we need to have its values aligned with our values and it has to learn about what we really want.
*  He gave this example. What if we have a superintelligent AI and we
*  give it the problem of solving climate change and it decides that the best way to lower the carbon
*  in the atmosphere is to kill all the humans? To me, that just made no sense at all because
*  a superintelligent AI, first of all, trying to figure out what superintelligence means.
*  It seems that something that's superintelligent
*  can't just be intelligent along this one dimension of, okay, I'm going to figure out
*  all the steps, the best optimal path to solving climate change and not be intelligent enough to
*  figure out that humans don't want to be killed, that you could get to one without having the other.
*  And Bostrom in his book talks about the orthogonality hypothesis where he says he thinks
*  that a system's, I can't remember exactly what it is, but a system's goals and its
*  values don't have to be aligned. There's some orthogonality there, which didn't make any sense
*  to me. So you're saying in any system that's sufficiently, not even superintelligent, but
*  as it opposed greater and greater intelligence, there's a holistic nature that will sort of,
*  a tension that will naturally emerge that prevents it from any one dimension running away.
*  Yeah, yeah, exactly. So Bostrom had this example of the superintelligent AI that
*  turns the world into paper clips because its job is to make paper clips or something.
*  And that just as a thought experiment didn't make any sense to me.
*  Well, as a thought experiment or as a thing that could possibly be realized?
*  Either. So I think that what my op-ed was trying to do was say that intelligence is more complex
*  than these people are presenting it, that it's not so separable, the rationality,
*  the values, the emotions, all of that. That it's the view that you could separate all these
*  dimensions and build a machine that has one of these dimensions and it's superintelligent
*  in one dimension, but it doesn't have any of the other dimensions. That's what I was trying to
*  criticize that I don't believe that. So can I read a few sentences from
*  Yoshua Benjy who is always super eloquent? So he writes,
*  I have the same impression as Melanie that our cognitive biases are linked with our ability to
*  learn to solve many problems. They may also be a limiting factor for AI. However, this is a may,
*  in quotes. Things may also turn out differently and there's a lot of uncertainty about the
*  capabilities of future machines. But more importantly for me, the value alignment problem
*  is a problem well before we reach some hypothetical superintelligence. It is already posing a problem
*  in the form of super powerful companies whose objective function may not be sufficiently
*  aligned with humanity's general wellbeing, creating all kinds of harmful side effects.
*  He goes on to argue that the orthogonality and those kinds of things, the concerns of just
*  aligning values with the capabilities of the system is something that might come
*  long before we reach anything like superintelligence. So your criticism is kind
*  of really nice to saying this idea of superintelligence systems seem to be dismissing
*  fundamental parts of what intelligence would take. And then Yoshio kind of says, yes, but
*  if we look at systems that are much less intelligent, there might be these same kinds of
*  problems that emerge. Sure. But I guess the example that he gives there of these corporations,
*  that's people, right? Those are people's values. I mean, we're talking about people, the corporations
*  are their values are the values of the people who run those corporations. But the idea is the
*  algorithm. That's right. So the fundamental person, the fundamental element of what does
*  the bad thing is a human being. Yeah. But the algorithm kind of controls the behavior of this
*  mass of human beings. Which algorithm? For a company that's the, so for example, if it's
*  advertisement driven company that recommends certain things and encourages engagement,
*  so it sort of gets money by encouraging engagement and therefore the company more and more
*  is like the cycle that builds an algorithm that enforces more engagement and may perhaps more
*  division in the culture and so on, so on. I guess the question here is sort of who has the agency?
*  So you might say, for instance, we don't want our algorithms to be racist. Right.
*  And facial recognition, some people have criticized some facial recognition systems
*  as being racist because they're not as good on darker skin and lighter skin. That's right.
*  Okay. But the agency there, the actual facial recognition algorithm isn't what has the agency,
*  it's not the racist thing. Right? It's the, I don't know, the combination of the training data,
*  the cameras being used, whatever. But my understanding of, and I'll say I agree with
*  Benjio there that I think there are these value issues with our use of algorithms. But
*  my understanding of what Russell's argument was is more that the machine itself has the agency now.
*  It's the thing that's making the decisions and it's the thing that has what we would call values.
*  Yes. So whether that's just a matter of degree, it's hard to say, right? But I would say that's
*  sort of qualitatively different than a face recognition neural network.
*  And to broadly linger on that point, if you look at Elon Musk or Stuart Russell or
*  Bostrom, people who are worried about existential risks of AI, however far into the future,
*  their argument goes is it eventually happens. We don't know how far, but it eventually happens.
*  Do you share any of those concerns and what kind of concerns in general do you have about AI
*  that approach anything like existential threat to humanity?
*  So I would say, yes, it's possible, but I think there's a lot more closer in existential threats
*  to humanity. Because you said like a hundred years for, so your time-
*  It's more than a hundred years.
*  More than a hundred years.
*  Maybe even more than 500 years. I don't know.
*  So the existential threats are so far out that the future is, I mean, there'll be a million
*  different technologies that we can't even predict now that will fundamentally change the nature of
*  our behavior, reality, society and so on before then.
*  I think so. I think so. And we have so many other pressing existential threats going on right now.
*  Nuclear weapons even.
*  Nuclear weapons, climate problems, poverty, possible pandemics, you can go on and on.
*  And I think though worrying about existential threat from AI
*  is not the best priority for what we should be worrying about. That's kind of my view,
*  because we're so far away. But I'm not necessarily criticizing Russell or Bostrom or whoever for
*  worrying about that. And I think some people should be worried about it. It's certainly fine.
*  But I was more sort of getting at their view of what intelligence is. So I was more focusing on
*  their view of superintelligence than just the fact of them worrying. And the title of the article
*  was written by the New York Times editors. I wouldn't have called it that.
*  We shouldn't be scared by superintelligence.
*  No.
*  If you wrote it, it'd be like we should redefine what you mean by superintelligence.
*  I actually said something like superintelligence is not a sort of coherent idea.
*  That's not something the New York Times would put in.
*  And the follow-up argument that Yoshio makes also, not argument, but a statement, and I've
*  heard him say it before, and I think I agree. He kind of has a very friendly way of phrasing it as
*  it's good for a lot of people to believe different things.
*  He's such a nice guy.
*  It's also practically speaking, we shouldn't be like, while your article stands,
*  Stuart Russell does amazing work, Bostrom does amazing work, you do amazing work.
*  And even when you disagree about the definition of superintelligence or the usefulness of even the
*  term, it's still useful to have people that use that term and then argue.
*  Sure.
*  I absolutely agree with Benjo there. And I think it's great that the New York Times will publish
*  all this stuff.
*  It's an exciting time to be here. What do you think is a good test of intelligence?
*  Is natural language ultimately a test that you find the most compelling, like the original,
*  or the higher levels of the Turing test?
*  Yeah. I still think the original idea of the Turing test is a good test for intelligence.
*  I can't think of anything better. The Turing test, the way that it's been carried out so far,
*  has been very impoverished, if you will. But I think a real Turing test that really goes into
*  depth. Like the one that I mentioned, I talk about in the book, I talk about Ray Kurzweil and
*  Mitchell Kapoor have this bet that in 2029, I think is the date, a machine will pass the Turing
*  test. And they have a very specific, many hours, expert judges and all of that. And
*  Kurzweil says yes, Kapoor says no. We only have nine more years to go to see.
*  I, you know, if something, a machine could pass that, I would be willing to call it intelligent.
*  Of course, nobody will. They will say that's just the language model,
*  if it does. So you would be comfortable. So language, a long conversation that's,
*  well, yeah, you're right. Because I think probably to carry out that long conversation,
*  you would literally need to have deep common sense understanding of the world.
*  I think so. I think so.
*  And conversation is enough to reveal that. I think so.
*  And perhaps it is. So another super fun topic of complexity that you have worked on, written about.
*  Let me ask the basic question. What is complexity?
*  So complexity is another one of those terms, like intelligence. It's perhaps overused. But
*  my book about complexity was about this wide area of complex systems, studying different systems
*  in nature, in technology, in society, in which you have emergence. Like I was talking about with
*  intelligence. We have the brain, which has billions of neurons. And each neuron individually
*  could be said to be not very complex compared to the system as a whole. But the system, the
*  interactions of those neurons and the dynamics creates these phenomena that we call intelligence
*  or consciousness that we consider to be very complex. So the field of complexity is trying
*  to find general principles that underlie all these systems that have these kinds of emergent
*  properties. And the emergence occurs from like underlying the complex system is usually simple,
*  fundamental interactions. And the emergence happens when there's just a lot of these things
*  interacting. And then most of science to date, can you talk about what is reductionism?
*  Well, reductionism is when you try and take a system and divide it up into its elements,
*  whether those be cells or atoms or subatomic particles, whatever your field is, and then try
*  and understand those elements and then try and build up an understanding of the whole system by
*  looking at sort of the sum of all the elements. So what's your sense, whether we're talking about
*  intelligence or these kinds of interesting complex systems, is it possible to understand them in a
*  in a reductionist way? Which is probably the approach of most of science today, right?
*  I don't think it's always possible to understand the things we want to understand the most.
*  So I don't think it's possible to look at single neurons and understand what we call intelligence,
*  to look at summing up. And the summing up is the issue here. One example is the human genome.
*  So there was a lot of work on the excitement about sequencing the human genome because the idea would
*  be that we'd be able to find genes that underlies diseases. But it turns out that, and it was a very
*  reductionist idea, we figure out what all the parts are, and then we would be able to figure out
*  which parts cause which things. But it turns out that the parts don't cause the things that we're
*  interested in. It's like the interactions, it's the networks of these parts. And so that kind of
*  reductionist approach didn't yield the explanation that we wanted. What do you use the most beautiful
*  complex system that you've encountered? The most beautiful.
*  That you've been captivated by? Is it sort of, I mean, for me, it's the simplest to be cellular
*  automata. Oh, yeah. So I was very captivated by cellular automata and worked on cellular
*  automata for several years. Do you find it amazing or is it surprising that such simple systems,
*  such simple rules in cellular automata can create sort of seemingly unlimited complexity?
*  Yeah, that was very surprising to me. How do you make sense of it? How does that make you feel? Is
*  it just ultimately humbling or is there a hope to somehow leverage this into a deeper understanding
*  and even able to engineer things like intelligence? It's definitely humbling. How humbling in that,
*  well, also kind of awe-inspiring that. It's that awe-inspiring part of mathematics that these
*  incredibly simple rules can produce this very beautiful, complex, hard to understand behavior.
*  And that's, it's mysterious and surprising still. But it's exciting because it does give you kind
*  of the hope that you might be able to engineer complexity just from the simple rules.
*  From the simple rules from the beginnings. Can you briefly say what is the Santa Fe Institute?
*  Its history, its culture, its ideas, its future. So I've never, as I mentioned to you, I've never
*  been, but it's always been this, in my mind, this mystical place where brilliant people
*  study the edge of chaos. Yeah, exactly. So the Santa Fe Institute was started in 1984.
*  And it was created by a group of scientists, a lot of them from Los Alamos National Lab, which is
*  about a 40-minute drive from the Santa Fe Institute. They were mostly physicists and chemists.
*  But they were frustrated in their field because they felt that their field wasn't approaching
*  big interdisciplinary questions like the kinds we've been talking about.
*  And they wanted to have a place where people from different disciplines could work on these big
*  questions without being siloed into physics, chemistry, biology, whatever. So they started
*  this institute. And this was people like George Cowan, who was a chemist in the Manhattan Project.
*  And Nicholas Metropolis, who, a mathematician, physicist, Marie-Gail Mann, physicist, and some
*  really big names here. Ken Arrow, a Nobel Prize-winning economist. And they started
*  having these workshops. And this whole enterprise kind of grew into this research institute that's
*  itself has been kind of on the edge of chaos its whole life because it doesn't have a significant
*  endowment. And it's just been kind of living on whatever funding it can raise through donations
*  and grants and however it can, business associates and so on. But it's a great place. It's a really
*  fun place to go think about ideas that you wouldn't normally encounter.
*  So Sean Carroll, some physicists.
*  Yeah, he's on the external faculty.
*  And you mentioned that there's some external faculty and there's people that are-
*  A very small group of resident faculty, maybe about 10 who are there on five-year terms that
*  can sometimes get renewed. And then they have some post-docs and then they have this much larger,
*  on the order of 100, external faculty or people like me who come and visit
*  for various periods of time.
*  So what do you think is the future of the Santa Fe Institute? And if people are interested,
*  what's there in terms of the public interaction or students or so on that could be a possible
*  interaction with the Santa Fe Institute or its ideas?
*  Yeah, so there's a few different things they do. They have a complex system summer school for
*  graduate students and post-docs and sometimes faculty attend too. And that's a four-week,
*  very intensive residential program where you go and you listen to lectures and you do projects.
*  And people really like that. I mean, it's a lot of fun. They also have some specialty
*  summer schools. There's one on computational social science. There's one on
*  climate and sustainability, I think it's called. There's a few. And then they have short courses
*  where just a few days on different topics. They also have an online education platform
*  that offers a lot of different courses and tutorials from SFI faculty.
*  Including an introduction to complexity course that I taught.
*  Awesome. And there's a bunch of talks too online from those guest speakers and so on. They host a
*  lot of- Yeah, they have technical seminars and colloquia and they have a community lecture series
*  public lectures and they put everything on their YouTube channel so you can see it all.
*  Douglas Hofstadter, author of Ghetto Escherbach was your PhD advisor. He mentioned a couple of
*  times in collaborator. Do you have any favorite lessons or memories from your time working with
*  him that continues to this day, I guess, but just even looking back throughout your time working
*  with him? So one of the things he taught me was that when you're looking at
*  a complex problem, to idealize it as much as possible, to try and figure out what is the
*  essence of this problem. And this is how the CopyCat program came into being, was by taking
*  analogy making and saying, how can we make this as idealized as possible but still retain really
*  the important things we want to study? And he said, I think that's a great question.
*  That's really been a core theme of my research, I think. And I continue to try and do that.
*  And it's really very much physics inspired. Hofstadter was a PhD in physics. That was his
*  background. It's like first principles kind of thinking like you're reduced to the most fundamental
*  aspect of the problem so that you can focus on solving that fundamental aspect. Yeah. And in AI,
*  you know, that was people used to work in these micro worlds, right? Like the blocks world was
*  very early, important area in AI. And then that got criticized because they said, oh, you know,
*  you can't scale that to the real world. And so people started working on much like more real
*  world like problems. But now there's been kind of a return even to the blocks world itself. You know,
*  we've seen a lot of people who are trying to work on more of these very idealized problems
*  for things like natural language and common sense. So that's an interesting evolution of those ideas.
*  So the perhaps the blocks world represents the fundamental challenges of the problem of
*  intelligence more than people realize. It might. Yeah. Is there sort of when you look back at your
*  body of work and your life, you've worked in so many different fields. Is there something that
*  you're just really proud of in terms of ideas that you've gotten a chance to explore, create yourself?
*  So I am really proud of my work on the copycat project. I think it's really different from what
*  almost everyone has done in AI. I think there's a lot of ideas there to be explored. And I guess
*  one of the happiest days of my life, you know, aside from like the births of my children,
*  was the birth of copycat when it actually started to be able to make
*  really interesting analogies. And I remember that very clearly. It was a very exciting time.
*  Well, you kind of gave life. Yes, artificial. That's right. What in terms of what people can
*  interact. I saw there's like a, I think it's called meta copycat, medicat, and there's a Python 3
*  implementation. If people actually wanted to play around with it and actually get into it and study
*  it and maybe integrate into whether it's with deep learning or any other kind of work they're doing,
*  what would you suggest they do to learn more about it and to take it forward in different kinds of
*  directions? Yeah. So there's Douglas Hofstadter's book called Fluid Concepts and Creative Analogies
*  talks in great detail about copycat. I have a book called Analogy Making as Perception,
*  which is a version of my PhD thesis on it. There's also code that's available that you can get it to
*  run. I have some links on my webpage to where people can get the code for it. And I think that
*  that would really be the best way to get into it. Yeah. Play with it. Well, Melanie, it was
*  honor talking to you. I really enjoyed it. Thank you so much for your time today. Thanks. It's been
*  really great. Thanks for listening to this conversation with Melanie Mitchell and thank
*  you to our presenting sponsor, Cash App. Download it, use code LexPodcast, you'll get $10 and $10
*  will go to FIRST, a STEM education nonprofit that inspires hundreds of thousands of young minds
*  to learn and to dream of engineering our future. If you enjoy this podcast, subscribe on YouTube,
*  give it five stars on Apple Podcast, support it on Patreon, or connect with me on Twitter.
*  And now let me leave you with some words of wisdom from Douglas Hofstadter and Melanie Mitchell.
*  Without concepts, there can be no thought. And without analogies, there can be no concepts.
*  And Melanie adds, how to form and fluidly use concepts is the most important open problem
*  in AI. Thank you for listening and hope to see you next time.
