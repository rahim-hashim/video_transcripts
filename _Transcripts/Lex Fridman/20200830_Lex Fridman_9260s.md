---
Date Generated: April 14, 2024
Transcription Model: whisper medium 20231117
Length: 9260s
Video Keywords: ['françois chollet', 'artificial intelligence', 'agi', 'ai', 'ai podcast', 'artificial intelligence podcast', 'lex fridman', 'lex podcast', 'lex mit', 'lex ai', 'lex jre', 'mit ai']
Video Views: 235651
Video Rating: None
---

# François Chollet: Measures of Intelligence | Lex Fridman Podcast #120
**Lex Fridman:** [August 30, 2020](https://www.youtube.com/watch?v=PUAdj3w3wO4)
*  The following is a conversation with Francois Chalet, his second time on the podcast.
*  He is both a world-class engineer and a philosopher in the realm of deep learning
*  and artificial intelligence. This time, we talk a lot about his paper titled
*  On the Measure of Intelligence that discusses how we might define and measure general intelligence
*  in our computing machinery. Quick summary of the sponsors. Babel, Masterclass, and Cash App.
*  Click the sponsor links in the description to get a discount and to support this podcast.
*  As a side note, let me say that the serious, rigorous,
*  scientific study of artificial general intelligence is a rare thing. The mainstream
*  machine learning community works on very narrow AI with very narrow benchmarks. This is very good
*  for incremental and sometimes big incremental progress. On the other hand, the outside the
*  mainstream, renegade, you could say, AGI community works on approaches that verge on the philosophical
*  and even the literary without big public benchmarks. Walking the line between the two worlds is a rare
*  breed, but it doesn't have to be. I ran the AGI series at MIT as an attempt to inspire more people
*  to walk this line. DeepMind and OpenAI for a time and still on occasion walk this line.
*  Francois Chollet does as well. I hope to also. It's a beautiful dream to work towards
*  and to make real one day. If you enjoy this thing, subscribe on YouTube, review it with 5
*  stars on Apple Podcasts, follow on Spotify, support on Patreon, or connect with me on Twitter
*  at Lex Friedman. As usual, I'll do a few minutes of ads now and no ads in the middle. I try to make
*  these interesting, but I give you timestamps so you can skip. But still, please do check out
*  the sponsors by clicking the links in the description. It's the best way to support this
*  podcast. This show is sponsored by Babbel, an app and website that gets you speaking in a new
*  language within weeks. Go to babbel.com and use Colex to get three months free. They offer 14
*  languages, including Spanish, French, Italian, German, and yes, Russian. Daily lessons are 10
*  to 15 minutes, super easy, effective, designed by over 100 language experts. Let me read a few
*  lines from the Russian poem Noch, Ulitsa, Fanar, Apteka by Alexander Block that you'll start to
*  understand if you sign up to Babbel. Noch, Ulitsa, Fanar, Apteka, Vesmyslinyi i tuskliy svet,
*  zhivi eschyo, khot chetvirtveko, vse budet tak, ishoda net.
*  Now, I say that you'll start to understand this poem because Russian starts with a language
*  and ends with vodka. Now, the latter part is definitely not endorsed or provided by Babbel
*  and will probably lose me this sponsorship, although it hasn't yet. But once you graduate
*  with Babbel, you can enroll in my advanced course of late night Russian conversation over vodka.
*  No app for that yet. So get started by visiting babbel.com and use Colex to get three months free.
*  This show is also sponsored by Masterclass. Sign up at masterclass.com slash lex to get a discount
*  and to support this podcast. When I first heard about Masterclass, I thought it was too good to
*  be true. I still think it's too good to be true. For $180 a year, you get an all access pass to
*  watch courses from to list some of my favorites. Chris Hatfield on space exploration. Hope to have
*  him in this podcast one day. Neil deGrasse Tyson on scientific thinking and communication. Neil too.
*  Will Wright, creator of SimCity and Sims on game design. Carlos Santana on guitar.
*  Kary Kasparov on chess. Daniel Lagrano on poker and many more. Chris Hatfield explaining how
*  rockets work and the experience of being launched at the space alone is worth the money.
*  By the way, you can watch it on basically any device. Once again, sign up at masterclass.com
*  slash lex to get a discount and to support this podcast. This show finally is presented by Cash
*  App, the number one finance app in the app store. When you get it, use Colex podcast. Cash App lets
*  you send money to friends, buy Bitcoin and invest in the stock market with as little as $1. Since
*  Cash App allows you to send and receive money digitally, let me mention a surprising fact
*  related to physical money. Of all the currency in the world, roughly 8% of it is actually physical
*  money. The other 92% of the money only exists digitally and that's only going to increase.
*  So again, if you get Cash App from the app store, Google play and use Colex podcast, you get 10 bucks
*  and Cash App will also donate $10 to FIRST, an organization that is helping to advance robotics
*  and STEM education for young people around the world. And now here's my conversation with Francois
*  Chalet. What philosophers, thinkers or ideas had a big impact on you growing up and today?
*  So one author that had a big impact on me when I read his books as a teenager was Jean Piaget,
*  who is a Swiss psychologist, is considered to be the father of developmental psychology.
*  And he has a large body of work about basically how intelligence develops in children. And so
*  it's really old work, like most of it is from the 1930s, 1940s. So it's not quite up to date.
*  It's actually superseded by many newer developments in developmental psychology.
*  But to me, it was very, very interesting, very striking and actually shaped the early ways in
*  which I started thinking about the mind and development of intelligence as a teenager.
*  Whose actual ideas or the way he thought about it, or just the fact that you could think about
*  the developing mind at all? I guess both. Jean Piaget is the author that really introduced me to the
*  notion that intelligence and the mind is something that you construct throughout your life and that
*  children construct it in stages. And I thought that was a very interesting idea, which is,
*  of course, very relevant to AI, to building artificial minds.
*  Another book that I read around the same time that had a big impact on me,
*  and there was actually a little bit of overlap with Jean Piaget as well, and I read it around
*  the same time, is Jeff Harkin's On Intelligence, which is a classic. And he has this vision of
*  the mind as a multi-scale hierarchy of temporal prediction modules. And these ideas really
*  resonated with me, like the notion of modular hierarchy of compression functions or prediction
*  functions. I thought it was really, really interesting, and it shaped the way I started
*  thinking about how to build minds. The hierarchical nature, which aspect?
*  Also, he's a neuroscientist, so he was basically talking about how our mind works.
*  Yeah, the notion that cognition is prediction was an idea that was kind of new to me at the time,
*  and that I really loved at the time. And yeah, and the notion that there are multiple scales
*  of processing in the brain. The hierarchy.
*  Yes. This was before deep learning. These ideas of hierarchies. In AI,
*  I've been around for a long time, even before On Intelligence. They've been around since the 1980s.
*  And yeah, that was before deep learning. But of course, I think these ideas really found
*  their practical implementation in deep learning. What about the memory side of things? I think he
*  is talking about knowledge representation. Do you think about memory a lot? One way you can
*  think of neural networks as a kind of memory. You're memorizing things, but it doesn't seem to be
*  the kind of memory that's in our brains, or it doesn't have the same rich complexity,
*  long-term nature that's in our brains. Yes. The brain is more of a sparse access
*  memory so that you can actually retrieve very precisely bits of your experience.
*  The retrieval aspect, you can introspect. You can ask yourself questions.
*  You can program your own memory. And language is actually the tool you use to do that. I think
*  language is a kind of operating system for the mind. And use language. Well, one of the uses of
*  language is as a query that you run over your own memory. Use words as keys to retrieve specific
*  experiences or specific concepts, specific thoughts. Language is a way you store thoughts,
*  not just in writing, in the physical world, but also in your own mind. And it's also how you
*  retrieve them. Imagine if you didn't have language, then you would not really have a self-
*  internally triggered way of retrieving past thoughts. You would have to rely on external
*  experiences. For instance, you see a specific sight, you smell a specific smell, and that brings up
*  memories. But you would not really have a way to deliberately access these memories without
*  language. Well, the interesting thing you mentioned is you can also program the memory. You can change
*  it probably with language. Yeah, using language. Yes. Well, let me ask you a Chomsky question,
*  which is like, first of all, do you think language is like fundamental? Like,
*  uh, there's turtles. What's at the bottom of the turtles? They don't go, it can't be turtles all
*  the way down. Is language at the bottom of cognition of everything is like language, the fundamental
*  aspect of like what it means to be a thinking thing? No, I don't think so. I think language,
*  you disagree with Noam Chomsky? Yes. I think language is a layer on top of cognition. So
*  it is fundamental to cognition in the sense that to use a computing metaphor, I see language as
*  the operating system of the brain, of the human mind. And the operating system is a layer on top
*  of the computer. The computer exists before the operating system, but the operating system is how
*  you make it truly useful. And the operating system is most likely Windows, not Linux, because
*  language is messy. Yeah, it's messy and it's pretty difficult to inspect it,
*  introspect it. How do you think about language? Like we use actually sort of human interpretable
*  language, but is there something like deeper, closer to like, like logical type of statements?
*  Like, yeah, what is the nature of language? Do you think? Is there something deeper than like the
*  syntactic rules we construct? Is there something that doesn't require utterances or writing or so
*  on? Oh, you're asking about the possibility that there could exist languages for thinking that are
*  not made of words. Yeah, yeah, I think so. I think so. The most important thing is that
*  the mind is layers, right? And language is almost like the outer most, the upper most layer.
*  But before we think in words, I think we think in terms of emotion in space and we think in terms of
*  physical actions. And I think babies in particular probably express these thoughts in terms of
*  the actions that they've seen of that or that they can perform. And in terms of the,
*  in terms of motions of objects in the environment before they start thinking in terms of words.
*  It's amazing to think about that as the building blocks of language. So like the kind of actions
*  and ways the babies see the world as like more fundamental than the beautiful Shakespearean
*  language you construct on top of it. And we probably don't have any idea what that looks
*  like, right? Like what, because it's important for them trying to engineer it into AI systems.
*  I think visual analogies and motion is a fundamental building block of the mind. And you
*  actually see it reflected in language. Like language is full of special metaphors. And when
*  you think about things, I consider myself very much as a visual thinker. You often express these
*  thoughts by using things like visualizing concepts in 2D space or like you solve problems by
*  imagining yourself navigating a concept space. I don't know if you have this sort of experience.
*  You said visualizing concept space. So like, so I certainly think about,
*  I certainly math, I certainly visualize mathematical concepts, but you mean like in concept space,
*  visually you're embedding ideas into some, into three dimensional space. You can explore
*  with your mind essentially. It's really more like 2D, but yeah. 2D. You're a flat lander. You're,
*  okay. No, I do not. I always have to, before I jump from concept to concept, I have to
*  put it back down on paper. It has to be on paper. I can only travel on 2D paper, not inside my mind.
*  You're able to move inside your mind. But even if you're writing like a paper, for instance,
*  don't you have like a spatial representation of your paper? Like you visualize where ideas lie
*  topologically in relationship to other ideas, kind of like a subway map of the ideas in your paper.
*  Yeah, that's true. I mean, there is, in papers, I don't know about you, but there feels like
*  there's a destination. There's a key idea that you want to arrive at and a lot of it is in the fog
*  and you're trying to kind of, it's almost like, what's that called when you do a path planning
*  search from both directions, from the start and from the end. And then you find, you do like
*  shortest path, but like, you know, in game playing, you do this with like a star from both sides.
*  And you see where they join.
*  Yeah. So you kind of do, at least for me, I think like, first of all, just exploring from the start,
*  from like first principles, what do I know? What can I start proving from that? Right. And then
*  from the destination, if I use their backtracking, like if I want to show some kind of sets of ideas,
*  what would it take to show them? And you kind of backtrack, but like, yeah, I don't think I'm doing
*  all that in my mind though. Like I'm putting it down on paper. Do you use mind maps to organize
*  your ideas? No. Yeah. I like mind maps. Let's get into this because it's, I've been so jealous of
*  people. I haven't really tried it. I've been jealous of people that seem to like, they get like
*  this fire of passion in their eyes because everything starts making sense. It's like Tom
*  Cruz in the movie was like moving stuff around. Some of the most brilliant people I know use mind
*  maps. I haven't tried really. Can you explain what the hell a mind map is? I guess the mind map is
*  a way to make kind of like the mess inside your mind to just put it on paper so that you gain more
*  control over it. It's a way to organize things on paper. And as kind of like a consequence of
*  organizing things on paper, they start being more organized inside your own mind.
*  So what does that look like? You put, like, do you have an example? Like what do you, what's the
*  first thing you write on paper? What's the second thing you write? I mean, typically you draw a
*  mind map to organize the way you think about a topic. So you would start by writing down like
*  the key concept about that topic. Like you will write intelligence or something, and then you
*  would start adding associative connections. Like what do you think about when you think about
*  intelligence? What do you think are the key elements of intelligence? So maybe we'd have
*  language, for instance, and you'd have motion. And so you would start drawing notes with these things,
*  and then you would see what do you think about when you think about motion and so on. And you
*  would go like that, like a tree. It's a tree or a tree mostly, or is it a graph too? Like a tree.
*  It's more of a graph than a tree. And it's not limited to just writing down words. You can also
*  draw things. And it's not supposed to be purely hierarchical. The point is that you can start,
*  once you start writing it down, you can start reorganizing it so that it makes more sense,
*  so that it's connected in a more effective way. See, but I'm so OCD that you just mentioned
*  intelligence and language and motion. I would start becoming paranoid that the categorization
*  is imperfect. Like that I would become paralyzed with the mind map that like this may not be.
*  So like the, even though you're just doing associative kind of connections, there's an
*  implied hierarchy that's emerging. And I would start becoming paranoid that it's not the proper
*  hierarchy. So you're not just one way to see mind maps is you're putting thoughts on paper.
*  It's like a stream of consciousness, but then you can also start getting paranoid. Well,
*  is this the right hierarchy? Sure. Like it's mind maps, your mind map. You're free to draw
*  anything you want. You're free to draw any connection you want, and you can just make a
*  different mind map if you think the central node is not the right node. So I suppose there's a fear
*  of being wrong. If you want to organize your ideas by writing down what you think, which I think is
*  very effective, like how do you know what you think about something if you don't write it down?
*  Right. If you do that, the thing is that it imposes a much more syntactic structure over your ideas,
*  which is not required with a mind map. So mind map is kind of like a lower level,
*  more freehand way of organizing your thoughts. And once you've drawn it, then you can start
*  actually voicing your thoughts in terms of, you know, paragraphs.
*  It's a two dimensional aspect of layout too, right? Yeah. It's a kind of flower, I guess,
*  you start. There's usually, you want to start with a central concept?
*  Yes. Typically it ends up more like a subway map. So it ends up more like a graph,
*  a topological graph. Without a root node.
*  Yeah. So like in a subway map, there are some nodes that are more connected than others,
*  and there are some nodes that are more important than others. Right. So there are destinations,
*  but it's not going to be purely like a tree, for instance.
*  Yeah. It's fascinating to think that if there's something to that about the way our mind thinks.
*  By the way, I just kind of remembered, obvious thing that I have probably thousands of documents
*  in Google doc at this point, their bullet point lists, which is, you can probably map a mind map
*  to a bullet point list. It's the same. It's a, no, it's not. It's a tree. It's a tree. Yeah.
*  So I create trees, but also they don't have the visual element. Like, I guess I'm comfortable
*  with the structure. It feels like it, the narrowness, the constraints feel more comforting.
*  If you have thousands of documents with your own thoughts in Google docs, why don't you write
*  some kind of search engine, like maybe a mind map, a piece of software, mind mapping software,
*  where you write down a concept and then it gives you sentences or paragraphs from your thousand
*  Google docs document that match this concept. The problem is it's so deeply, unlike mind maps,
*  so deeply rooted in natural language. So it's not, it's not semantically searchable. I would say,
*  because the categories are very, you kind of mentioned intelligence, language, and
*  motion. They're very strong, semantic. Like it feels like the mind map forces you to be
*  semantically clear and specific. The bullet points list I have are, are it's sparse, disparate
*  thoughts that poetically represent a category like motion, as opposed to saying motion. So
*  unfortunately, that's the same problem with the internet. That's why the idea of semantic web is
*  difficult to get. It's, most language on the internet is a giant mess of natural language
*  that's hard to interpret. Which, so do you think, do you think there's something to mind maps as,
*  you actually originally brought it up as what we're talking about,
*  kind of cognition and language. Do you think there's something to mind maps about how our brain
*  actually deals, like think reasons about things? It's possible. I think it's reasonable to assume
*  that there is some level of topological processing in the brain, that the brain is
*  very associative in nature. And I also believe that a topological space is a better medium
*  to encode thoughts than a geometric space. Then so I think-
*  What's the difference in a topological and geometric space?
*  Well, if you're talking about topologies, then points are either connected or not. So topology
*  is more like a subway map. And geometry is when you're interested in the distance between things.
*  And in subway maps, you don't really have the concept of distance. You only have the concept
*  of whether there is a train going from station A to station B. And what we do in deep learning
*  is that we're actually dealing with geometric spaces. We are dealing with concept vectors,
*  word vectors that have a distance between them expressed in terms of dot product.
*  We are not really building topological models usually.
*  I think you're absolutely right. Like distance is a fundamental importance in deep learning.
*  It's the continuous aspect of it.
*  Yes, because everything is a vector. And everything has to be a vector because
*  everything has to be differentiable. If your space is discrete, it's no longer differentiable.
*  You cannot do deep learning in it anymore. Well, you could, but you could only do it by embedding
*  it in a bigger continuous space. So if you do topology in the context of deep learning,
*  you have to do it by embedding your topology in a geometry.
*  Well, let me zoom out for a second. Let's get into your paper on the measure of intelligence
*  that you put out in 2019.
*  Yes.
*  Okay. Yeah.
*  November.
*  November. Yeah. Remember 2019? That was a different time.
*  Yeah, I remember. I still remember.
*  It feels like a different world.
*  You could travel, you can actually go outside and see friends.
*  Yeah. Let me ask the most absurd question. I think there's some non-zero probability
*  there'll be a textbook one day, like 200 years from now, on artificial intelligence,
*  or it'll be called like just intelligence because humans will already be gone.
*  It'll be your picture with a quote. This is one of the early biological systems would
*  consider the nature of intelligence and there'll be like a definition of how they
*  thought about intelligence, which is one of the things you do in your paper on measure
*  of intelligence is to ask like, well, what is intelligence and how to test for intelligence
*  and so on. So is there a spiffy quote about what is intelligence? What is the definition
*  of intelligence according to Francois Chollet?
*  Yeah. So do you think the super intelligent AIs of the future will want to remember us
*  the way we remember humans from the past? And do you think they won't be ashamed of
*  having a biological origin?
*  No, I think it would be a niche topic. It won't be that interesting, but it'll be
*  like the people that study in certain contexts, like historical civilization that no longer
*  exist, the Aztecs and so on. That's how it'll be seen. And it'll be study in the also the
*  context on social media. There'll be hashtags about the atrocity committed to human beings
*  when the robots finally got rid of them. Like it was a mistake. It'll be seen as a giant mistake,
*  but ultimately in the name of progress and it created a better world because humans were
*  over consuming the resources and they were not very rational and were destructive in the end in
*  terms of productivity and putting more love in the world. And so within that context, there'll
*  be a chapter about these biological systems.
*  Seems to have a very detailed vision of that hit here. You should write a sci-fi novel about it.
*  I'm working on a sci-fi novel currently, yes. Self-published.
*  The definition of intelligence. So intelligence is the efficiency with which
*  you acquire new skills at tasks that you did not previously know about, that you did not prepare
*  for. So intelligence is not skill itself. It's not what you know. It's not what you can do.
*  It's how well and how efficiently you can learn new things.
*  New things. The idea of newness there seems to be fundamentally important.
*  Yes. So you would see intelligence on display, for instance, whenever you see a human being or
*  an AI creature adapt to a new environment that it has not seen before, that its creators did
*  not anticipate. When you see adaptation, when you see improvisation, when you see generalization,
*  that's intelligence. In reverse, if you have a system that when you put it in a slightly
*  new environment, it cannot adapt, it cannot improvise, it cannot deviate from what it's
*  hard-coded to do or what it has been trained to do. That is a system that is not intelligent.
*  There's actually a quote from Einstein that captures this idea, which is,
*  the measure of intelligence is the ability to change. I like that quote. I think it captures
*  at least part of this idea. There might be something interesting about the difference
*  between your definition and Einstein's. I mean, he's just being Einstein and clever, but acquisition
*  of new ability to deal with new things versus ability to just change. What's the difference
*  between those two things? So just change in itself. Do you think there's something to that?
*  Just being able to change. Yes, being able to adapt. So not change, but certainly a change
*  is direction. Being able to adapt yourself to your environment. Whatever the environment is.
*  That's a big part of intelligence. Intelligence is more precisely how efficiently you're able
*  to adapt, how efficiently you're able to basically master your environment, how efficiently
*  you can acquire new skills. I think there's a big distinction to be drawn between intelligence,
*  which is a process and the output of that process, which is skill.
*  For instance, if you have a very smart human programmer that considers the game of chess
*  and that writes down a static program that can play chess, then the intelligence is the process
*  of developing that program. But the program itself is just encoding the output artifact
*  of that process. The program itself is not intelligent. And the way you tell it's not
*  intelligent is that if you put it in a different context, you ask it to play Go or something,
*  it's not going to be able to perform well with that human involvement because the source of
*  intelligence, the entity that is capable of that process is the human programmer. So we should
*  be able to tell the difference between the process and its output. We should not confuse
*  the output and the process. It's the same as do not confuse a road building company
*  and one specific road because one specific road takes you from point A to point B,
*  but a road building company can take you from, can make a path from anywhere to anywhere else.
*  Yeah, that's beautifully put. But it's also, to play devil's advocate a little bit,
*  you know, it's possible that there is something more fundamental than us humans. So
*  you kind of said the programmer creates the difference between the choir of the skill and
*  the skill itself. There could be something like you could argue the universe is more intelligent,
*  like the deep, the base intelligence of that we should be trying to measure is something that
*  created humans, we should be measuring God or the source of the universe as opposed to
*  like there's, there could be a deeper intelligence. There's always deeper intelligence.
*  You can argue that, but that does not take anything away from the fact that humans are
*  intelligence. And you can tell that because they are capable of adaptation and generality.
*  And you see that in particular in the fact that
*  humans are capable of handling situations and tasks that are quite different from anything that
*  any of our evolutionary ancestors has ever encountered. So we are capable of generalizing
*  very much out of distribution, if you consider our evolutionary history as being in a way,
*  altering data. Of course, evolutionary biologists would argue that we're not going too far out
*  of the distribution or like mapping the skills we've learned previously, desperately trying to
*  jam them into these new situations. I mean, there's definitely a little bit of that,
*  but it's pretty clear to me that we're able to, most of the things we do any given day in our
*  modern civilization are things that are very, very different from what our ancestors a million years
*  ago would have been doing in a given day. And our environment is very different. So I agree that
*  everything we do, we do it with cognitive building blocks that we acquired over the
*  course of evolution. And that anchors our cognition to certain contexts, which is
*  the human condition very much. But still, our mind is capable of a pretty remarkable degree of
*  generality, far beyond anything we can create in artificial systems today. The degree in which
*  the mind can generalize from its evolutionary history, can generalize away from its evolutionary
*  history is much greater than the degree to which a deep learning system today can generalize away
*  from its trained data. And the key point you're making, which I think is quite beautiful, is
*  we shouldn't measure, if we're talking about measurement, we shouldn't measure the skill.
*  We should measure the creation of the new skill, the ability to create that new skill.
*  But it's tempting. It's weird because the skill is a little bit of a small window into the
*  system. So whenever you have a lot of skills, it's tempting to measure the skills.
*  I mean, the skill is the only thing you can objectively measure. But yeah, so the thing
*  to keep in mind is that when you see skill in the human, it gives you a strong signal that that
*  human is intelligent because you know they weren't born with that skill, typically. Like you see a
*  very strong chess player, maybe you're a very strong chess player yourself.
*  I think you're saying that because I'm Russian and now you're prejudiced. You assume all Russians
*  are going to just... I'm biased. Well, you're...
*  Very short bias. So if you see a very strong chess player, you know they weren't born
*  knowing how to play chess. So they had to acquire that skill with their limited resources,
*  with their limited lifetime. And they did that because they are generally intelligent. And so
*  they may as well have acquired any other skill. You know they have this potential.
*  And on the other hand, if you see a computer playing chess, you cannot make the same assumptions
*  because you cannot just assume the computer is generally intelligent. The computer may be born
*  knowing how to play chess in the sense that it may have been programmed by a human that has
*  understood chess for the computer and that has just encoded the output of that understanding and
*  aesthetic program. And that program is not intelligent. So let's zoom out just for a second
*  and say like, what is the goal on the Measure of Intelligence paper? Like what do you hope to
*  achieve with it? So the goal of the paper is to clear up some long-standing misunderstandings
*  about the way we've been conceptualizing intelligence in the AI community and in the
*  way we've been evaluating progress in AI. There's been a lot of progress recently in
*  machine learning and people are extrapolating from that progress that we are about to solve
*  general intelligence. And if you want to be able to evaluate these statements, you need
*  to precisely define what you're talking about when you're talking about general intelligence.
*  And you need a formal way, a reliable way to measure how much intelligence, how much general
*  intelligence a system processes. And ideally, this measure of intelligence should be actionable. So
*  it should not just describe what intelligence is. It should not just be a binary indicator that
*  tells you the system is intelligent or it isn't. It should be actionable. It should have explanatory
*  power. So you could use it as a feedback signal. It would show you the way the world's building
*  more intelligent systems. So at the first level, you draw a distinction between two divergent views
*  of intelligence. As we just talked about, intelligence is a collection of tasks, specific
*  skills, and a general learning ability. So what's the difference between
*  this memorization of skills and a general learning ability? We've talked about it a
*  little bit, but can you try to linger on this topic for a bit?
*  Yeah. So the first part of the paper is an assessment of the different ways we've been
*  thinking about intelligence and the different ways we've been evaluating progress in AI. And
*  the history of cognitive sciences has been shaped by two views of the human mind. And one view is
*  the evolutionary psychology view, in which the mind is a collection of fairly static,
*  special purpose, ad hoc mechanisms that have been hard-coded by evolution over our history as a
*  species for a very long time. And early AI researchers, people like Marvin Minsky, for
*  instance, they clearly subscribed to this view. And they saw the mind as a collection of static
*  programs similar to the programs they would run on mainframe computers. And in fact, I think they
*  very much understood the mind through the metaphor of the mainframe computer, because that was the
*  tool they were working with. And so you had this static program, this collection of very different
*  static programs operating over a database like memory. And in this picture, learning was not
*  very important. Learning was considered to be just memorization. And in fact, learning is basically
*  not featured in AI textbooks until the 1980s with the rise of machine learning.
*  It's kind of fun to think about that learning was the outcast. Like the weird people working on
*  learning, like the mainstream AI world was, I mean, I don't know what the best term is,
*  but it's non-learning. It was seen as like reasoning would not be learning-based.
*  Yes, it was considered that the mind was a collection of programs that were primarily
*  logical in nature. And that's all you needed to do to create a mind was to write down these programs.
*  And they would operate over knowledge, which would be stored in some kind of database. And as long as
*  your database would encompass everything about the world and your logical rules were comprehensive,
*  then you would have a mind. So the other view of the mind is the brain as a sort of blank slate.
*  This is a very old idea. You find it in John Locke's writings. This is the tabula rasa.
*  And this is this idea that the mind is some kind of information sponge that starts empty,
*  that starts blank, and that absorbs knowledge and skills from experience. So it's a sponge that
*  reflects the complexity of the world, the complexity of your life experience, essentially.
*  That everything you know and everything you can do is a reflection of something you found
*  in the outside world, essentially. So this is an idea that's very old, that was not very popular,
*  for instance, in the 1970s. But that gained a lot of vitality recently with the rise of
*  connectionism in particular deep learning. And so today, deep learning is the dominant paradigm in AI.
*  And I feel like lots of AI researchers are conceptualizing the mind via a deep learning
*  metaphor. They see the mind as a kind of randomly initialized neural network that starts blank when
*  you're born and then that gets trained via exposure to training data that requires knowledge
*  and skills for exposure to training data. By the way, it's a small tangent. I feel like
*  people who are thinking about intelligence are not conceptualizing it that way. I actually haven't
*  met too many people who believe that a neural network will be able to reason, who seriously
*  think that, rigorously. Because I think it's an actually interesting worldview. And we'll talk
*  about it more, but it's been impressive what neural networks have been able to accomplish.
*  And it's an eye to me, I don't know, you might disagree, but it's an open question whether
*  scaling size eventually might lead to incredible results to us mere humans will appear as if it's
*  general. I mean, if you ask people who are seriously thinking about intelligence, they will
*  definitely not say that all you need to do is like the mind is just a neural network.
*  However, it's actually a view that's very popular, I think, in the deep learning community that
*  many people are kind of conceptually intellectually lazy about it.
*  But I guess what I'm saying exactly right is I haven't met many people and I think it would be
*  interesting to meet a person who is not intellectually lazy about this particular topic
*  and still believes that neural networks will go all the way. I think Yann LeCun is probably
*  closest to that with self-supervised. There are definitely people who argue that
*  current deep learning techniques are already the way to general artificial intelligence.
*  That all you need to do is to scale it up to all the available training data.
*  And that's if you look at the waves that open their eyes, GPT-3 model has made, you see echoes
*  of this idea. So on that topic, GPT-3, similar to GPT-2 actually, have captivated some part of the
*  imagination of the public. There's just a bunch of hype of different kind. I would say it's emergent.
*  It's not artificially manufactured. It's just like people just get excited for some strange
*  reason. In the case of GPT-3, which is funny, that there's, I believe, a couple of months delay
*  from a release to hype. Maybe I'm not historically correct on that, but it feels like there was a
*  little bit of a lack of hype and then there's a phase shift into hype. But nevertheless,
*  there's a bunch of cool applications that seem to captivate the imagination of the public about
*  what this language model that's trained in unsupervised way without any fine tuning is
*  able to achieve. So what do you make of that? What are your thoughts about GPT-3?
*  Yeah. So I think what's interesting about GPT-3 is the idea that it may be able to learn new tasks
*  after just being shown a few examples. So I think if it's actually capable of doing that,
*  novel and that's interesting and that's something we should investigate.
*  That said, I must say I'm not entirely convinced that we have shown it's capable of doing that.
*  It's very likely, given the amount of data that the model is trained on, that what it's actually
*  doing is pattern matching a new task you give it with a task that it's been exposed to in its training
*  data. It's just recognizing the task instead of just developing a model of the task.
*  Sorry to interrupt, there's a parallel to what you said before, which is it's possible to see GPT-3
*  as like the prompts it's given as a kind of SQL query into this thing that it's learned,
*  similar to what you said before, which is languages used to query the memory.
*  Yes. So is it possible that neural network is a giant memorization thing, but then if it gets
*  sufficiently giant, it'll memorize sufficiently large amounts of things in the world where it
*  intelligence becomes a querying machine. I think it's possible that a significant
*  chunk of intelligence is this giant associative memory. I definitely don't believe that intelligence
*  is just a giant associative memory, but it may well be a big component.
*  So do you think GPT-3, 4, 5, GPT-10 will eventually... Where's the ceiling? Do you think you'll be able to
*  reason? No, that's a bad question. What is the ceiling is the better question.
*  How well is it going to scale? How good is GPT-N going to be?
*  I believe GPT-N is going to improve on the strength of GPT-2 and 3, which is it will be able to generate
*  ever more plausible text in context. Just monotonically increasing performance.
*  Yes. If you train a bigger model on more data, then your text will be increasingly more
*  context aware and increasingly more plausible in the same way that GPT-3 is much better
*  generating plausible text compared to GPT-2. But that said, I don't think just scaling up
*  the model to more transformer layers and more training data is going to address the flaws
*  of GPT-3, which is that it can generate plausible text, but that text is not constrained by
*  anything else other than plausibility. In particular, it's not constrained by factualness
*  or even consistency, which is why it's very easy to get GPT-3 to generate statements that are
*  factually untrue or to generate statements that are even self-contradictory.
*  Because its only goal is plausibility and it has no other constraints. It's not constrained to be
*  self-consistent. For this reason, one thing that I thought was very interesting with GPT-3 is that
*  you can put in mind the answer it will give you by asking the question in a specific way,
*  because it's very responsive to the way you ask the question since it has
*  no understanding of the content of the question. If you have the same question
*  in two different ways that are adversely engineered to produce certain answers,
*  you will get two different answers, two contradictory answers.
*  It's very susceptible to adversarial attacks essentially.
*  Potentially, yes. In general, the problem with these models, these generative models, is that
*  they are very good at generating plausible text, but that's just not enough.
*  One avenue that would be very interesting to make progress is to make it possible
*  to write programs over the latent space that these models operate on, that you would rely on these
*  self-supervised models to generate a sort of flag pool of knowledge and concepts and common sense.
*  Then you would be able to write explicit,
*  reasoning programs over it. Because the current problem with GPT-3 is that it can be quite
*  difficult to get it to do what you want to do. If you want to turn GPT-3 into products, you need to
*  put constraints on it. You need to force it to obey certain rules. You need a way to program it
*  explicitly. If you look at the data, you can see that
*  you need a way to program it explicitly. If you look at its ability to do program synthesis,
*  it generates something that's plausible. If you try to make it generate programs,
*  it will perform well for any program that it has seen in its training data. But because
*  program space is not interpretive, it's not going to be able to generalize to problems it hasn't
*  seen before. Now that's currently, do you think, sort of an absurd, but I think useful,
*  I guess intuition builder is the GPT-3 has 175 billion parameters.
*  Human brain has about a thousand times that or more in terms of number of synapses.
*  Do you think, obviously, very different kinds of things, but there is some degree of similarity.
*  Do you think, what do you think GPT will look like when it has 100 trillion parameters?
*  You think our conversation might be in nature different? Because you've criticized GPT-3 very
*  effectively now. Do you think? No, I don't think so. To begin with, the bottleneck with scaling up
*  GPT-3, GPT models, generative pre-trained transformer models, is not going to be the size of the model
*  or how long it takes to train it. The bottleneck is going to be the training data because OpenAI
*  is already training GPT-3 on a crawl of basically the entire web. That's a lot of data. You could
*  imagine training on more data than that. Google could train on more data than that, but it would
*  still be only incrementally more data. I don't recall exactly how much more data GPT-3 was
*  trained on compared to GPT-2, but it's probably at least like 100 or maybe even 1000x. I don't
*  have the exact number. You're not going to be able to train the model on 100 more data than what
*  you're already doing. That's brilliant. It's easier to think of compute as a bottleneck
*  and then arguing that we can remove that bottleneck. We can remove the compute bottleneck.
*  I don't think it's a big problem. If you look at the pace at which we've improved the efficiency
*  of deep learning models in the past few years, I'm not worried about
*  train time bottlenecks or model size bottlenecks. The bottleneck in the case of these generative
*  transformer models is absolutely the training data. What about the quality of the data?
*  So, yeah, the quality of the data is an interesting point. The thing is,
*  if you're going to want to use these models in real products, then you want to feed them
*  data that's as high quality as factual, I would say as unbiased as possible. But there's not really
*  such a thing as unbiased data in the first place. But you probably don't want to train it on Reddit,
*  for instance. It sounds like a bad plan. From my personal experience working with
*  large scale deep learning models, at some point I was working on a model at Google that's trained
*  on 350 million labeled images. It's an image classification model. That's a lot of images.
*  That's probably the most publicly available images on the web at the time.
*  And it was a very noisy data set because the labels were not originally annotated by hand,
*  by humans. They were automatically derived from tags on social media or just keywords
*  in the same page as the image was found and so on. So it was very noisy. And it turned out
*  that you could easily get a better model, not just by training. If you train on more of the noisy
*  data, you get an incrementally better model, but you very quickly hit diminishing returns. On the
*  other hand, if you train on smaller data set with higher quality annotations, annotations that are
*  actually made by humans, you get a better model. And it also takes less time to train it.
*  Yeah, that's fascinating. It's the self-supervised learning. There's a way to get better
*  doing the automated labeling. Yeah. So you can enrich or refine your labels
*  in an automated way. That's correct. Do you have a hope for, I don't know if you're familiar with
*  the idea of a semantic web. Is this a semantic web just for people who are not familiar?
*  And is the idea of being able to convert the internet or be able to attach semantic meaning
*  to the words on the internet, the sentences, the paragraphs, to be able to convert information on
*  the internet or some fraction of the internet into something that's interpretable by machines.
*  I was kind of a dream for, I think the semantic web papers in the 90s. It's kind of the dream that
*  the internet is full of rich, exciting information. Even just looking at Wikipedia, we should be able
*  to use that as data for machines. And so far- Yeah, the information is not really in a format
*  that's available to machines. So no, I don't think the semantic web will ever work simply because it
*  would be enough work to provide that information in structured form. And there is not really any
*  incentive for anyone to provide that work. So I think the way forward to make the knowledge on
*  the web available to machines is actually something closer to unsupervised deep learning.
*  Yeah. So GBT3 is actually a bigger step in the direction of making the knowledge available to
*  machines than the semantic web was. Yeah, perhaps in a human centric sense, it feels like
*  GBT3 hasn't learned anything that could be used to reason. But that might be just the early days.
*  Yeah, I think that's correct. I think the forms of reasoning that you see perform are basically just
*  reproducing patterns that it has seen in string data. So of course, if you're trained on the entire
*  web, then you can produce an illusion of reasoning in many different situations, but it will break
*  down if it's presented with a novel situation. That's the open question between the illusion of
*  reasoning and actual reasoning. Yes. The power to adapt to something that is genuinely new.
*  The power to adapt to something that is genuinely new. Because the thing is, even imagine you had,
*  you could train on every bit of data ever generated in this sphere of humanity.
*  That model would be capable of anticipating many different possible situations, but it remains that
*  the future is going to be something different. For instance, if you train a GBT3 model
*  on data from the year 2002, for instance, and then use it today, it's going to be missing
*  many things. It's going to be missing many common sense facts about the world. It's even going to be
*  missing vocabulary and so on. Yeah, it's interesting that GBT3 even doesn't have, I think, any information
*  about the coronavirus. Yes. Which is why a system that's... You tell that the system is intelligent
*  when it's capable to adapt. Intelligence is going to require some amount of continuous learning.
*  It's also going to require some amount of improvisation. It's not enough to assume that
*  what you're going to be asked to do is something that you've seen before,
*  or something that is a simple interpolation of things you've seen before.
*  Yeah. In fact, that model breaks down for
*  even very tasks that look relatively simple from a distance, like L5 self-driving, for instance.
*  Google had a paper a couple of years back showing that something like 30 million
*  different road situations were actually completely insufficient to train a driving model.
*  It wasn't even L2. That's a lot of data. That's a lot more data than the 20 or 30 hours of driving
*  that a human needs to learn to drive, given the knowledge they've already accumulated.
*  Well, let me ask you on that topic. Elon Musk, Tesla Autopilot, it's one of the only companies
*  I believe is really pushing for a learning-based approach.
*  You're skeptical that that kind of network can achieve level four?
*  L4 is probably achievable. L5 is probably not.
*  What's the distinction there? L5 is completely, you can just fall asleep.
*  Yeah, L5 is basically human level.
*  Well, with driving, we have to be careful saying human level because that's the most-
*  Yeah, they're all kinds of drivers.
*  Yeah, that's the clearest example of like, cars will most likely be much safer than humans
*  in many situations where humans fail. It's the vice versa question.
*  I'll tell you, the thing is the amounts of training data you would need to anticipate
*  for pretty much every possible situation you learn content in the real world is such that it's not
*  entirely unrealistic to think that at some point in the future, we'll develop a system
*  that's trained on enough data, especially provided that we can simulate a lot of that data.
*  We don't necessarily need actual cars on the road for everything, but it's a massive effort.
*  In turns out, you can create a system that's much more adaptive,
*  that can generalize much better if you just add explicit models of the surroundings of the car.
*  If you use deep learning for what it's good at, which is to provide perceptive information.
*  In general, deep learning is a way to encode perception and a way to encode intuition,
*  but it is not a good medium for any sort of explicit reasoning. In AI systems today,
*  strong generalization tends to come from explicit models, tend to come from abstractions in the
*  human mind that are encoded in program form by a human engineer. These are the abstractions
*  you can actually generalize, not the sort of weak abstraction that is learned by a neural network.
*  The question is how much reasoning, how much strong abstractions are required to solve
*  particular tasks like driving? That's the question. Or human life, existence. How much strong
*  abstractions does existence require? But more specifically, driving, that seems to be a coupled
*  question about intelligence. How much intelligence, how do you build an intelligence system?
*  The coupled problem, how hard is this problem? How much intelligence does this problem actually
*  require? We get to cheat, right? Because we get to look at the problem. It's not like you get to
*  close our eyes and completely new to driving. We get to do what we do as human beings, which is
*  for the majority of our life, before we ever learn, quote unquote, to drive, we get to watch other
*  cars and other people drive. We get to be in cars. We get to watch. We get to see movies about cars.
*  We get to observe all that stuff. That's similar to what neural networks are doing.
*  It's getting a lot of data. The question is, yeah, how many leaps of reasoning genius is required?
*  To be able to actually effectively drive. I think it's an example of driving. Sure,
*  you've seen a lot of cars in your life before you learned to drive. But let's say you've learned to
*  drive in Silicon Valley and now you rent a car in Tokyo. Well, now everyone is driving on the other
*  side of the road and the signs are different and the roads are more narrow and so on. So it's a very,
*  different environment. And a smart human, even an average human, should be able to just zero shot it
*  to just be operational in this very different environment right away, despite having had new
*  contact with the novel complexity that is contained in this environment. And that novel
*  complexity is not just interpolation over the situations that you've encountered previously,
*  like learning to drive in the US. I would say the reason I ask is one of the most interesting
*  tests of intelligence we have today actively, which is driving in terms of having an impact
*  on the world. When do you think we'll pass that test of intelligence? I don't think driving is
*  that much of a test of intelligence because again, there is no task for which skill at that task
*  demonstrates intelligence unless it's a kind of meta task that involves acquiring new skills.
*  So I think you can actually solve driving without having any real amount of intelligence. For
*  instance, if you really did have infinite trained data, you could just literally train an end to
*  end deep learning model that does driving, provided infinite trained data. The only problem
*  with the whole idea is collecting a data set that's sufficiently comprehensive, that covers the very
*  long tail of possible situations you might encounter. And it's really just a scale problem.
*  So I think there's nothing fundamentally wrong with this plan, with this idea. It's just that
*  it strikes me as a fairly inefficient thing to do because you run into this scaling issue with
*  diminishing returns. Whereas if instead you took a more manual engineering approach where you
*  use deep learning modules in combination with engineering an explicit model of the surrounding
*  of the cars and you bridge the two in a clever way, your model will actually start generalizing
*  much earlier and more effectively than the end to end deep learning model. So why would you not
*  go with the more manual engineering oriented approach? Even if you created that system,
*  either the end to end deep learning model system that's infinite data or the slightly
*  more human system. I don't think achieving L5 would demonstrate general intelligence or
*  intelligence of any generality at all. Again, the only possible test of generality in AI
*  would be a test that looks at skill acquisition over unknown tasks. For instance, you could take
*  your L5 driver and ask it to learn to pilot a commercial airplane, for instance,
*  and then you would look at how much human involvement is required and how much strength
*  data is required for the system to learn to pilot an airplane. That gives you a measure of how
*  intelligent that system really is. Yeah. Well, I mean, that's a big leap. I get you, but
*  I'm more interested as a problem. I would see, to me, driving is a black box
*  that can generate novel situations at some rate, what people call edge cases. So it does have
*  newness that keeps being like we're confronted, let's say once a month.
*  It is a very long tail. Yes. That doesn't mean you cannot solve it
*  just by training a statistical model amount of data. Huge amount of data. It's really a matter
*  of scale. But I guess what I'm saying is if you have a vehicle that achieves L5, it is going to be
*  able to deal with new situations. Or, I mean, the data is so large that the rate of new situations
*  is very low. Yes. That's not intelligent. So if we go back to your kind of definition of
*  intelligence, it's the efficiency. With which you can adapt to new situations,
*  to truly new situations, not situations you've seen before, right? Not situations that could
*  be anticipated by your creators, by the creators of the system, but truly new situations.
*  The efficiency with which you acquire new skills. If you require, in order to pick up a new skill,
*  you require a very extensive training data set of most possible situations that can occur
*  in the practice of that skill, then the system is not intelligent. It is mostly just a lookup table.
*  Yeah. Likewise, if in order to acquire a skill, you need a human engineer to write down
*  a bunch of rules that cover most or every possible situation, likewise, the system is not
*  intelligent. The system is merely the output artifact of a process that happens in the minds
*  of the engineers that are creating it. It is encoding an abstraction that's produced by the
*  human mind. And intelligence would actually be the process of autonomously producing this abstraction.
*  If you take an abstraction and you encode it on a piece of paper or in a computer program,
*  the abstraction itself is not intelligent. What's intelligent is the agent that's capable of
*  producing these abstractions. Right? Yeah. It feels like there's a little bit of a gray area.
*  Like, because you're basically saying that deep learning forms abstractions too.
*  But those abstractions do not seem to be effective for generalizing far outside of the
*  things that's already seen. But generalize a little bit. Yeah, absolutely. No, deep learning
*  does generalize a little bit. Like, generalization is not a binary. It's more like a spectrum. Yeah.
*  And there's a certain point, it's a gray area, but there's a certain point where there's an impressive
*  degree of generalization that happens. No, like I guess exactly what you were saying is
*  intelligence is how efficiently you're able to generalize far outside of the distribution of
*  things you've seen already. Yes. So it's both like the distance of how far you can, like how new,
*  how radically new something is and how efficiently you're able to deal with that.
*  You can think of intelligence as a measure of an information conversion ratio. Like, imagine
*  a space of possible situations and you've covered some of them. So you have some amount of information
*  about your space of possible situations that's provided by the situations you already know.
*  And that's on the other hand also provided by the prior knowledge that the system brings
*  to the table of the prior knowledge that's embedded in the system. So the system starts
*  with some information about the problem, about the task. And it's about going from that information
*  to a program, what you would call a skill program, a behavioral program that can cover
*  a large area of possible situation space. And essentially the ratio between that area and
*  the amount of information you start with is intelligence. So a very smart agent can make
*  efficient use of very little information about a new problem and very little prior knowledge as well
*  to cover a very large area of potential situations in that problem without knowing what these future
*  new situations are going to be. So one of the other big things you talk about in the paper
*  we've talked about a little bit already, but let's talk about it some more as actual tests
*  of intelligence. So if we look at like human and machine intelligence, do you think tests of
*  intelligence should be different for humans and machines or how we think about testing of intelligence?
*  Are these fundamentally the same kind of intelligence that we're after and therefore
*  the tests should be similar? So if your goal is to create AIs that are more human-like,
*  then it will be super valuable obviously to have a test that's universal that applies to both
*  AIs and humans so that you could establish a comparison between the two that you could tell
*  exactly how intelligent in terms of human intelligence a given system is. So that said,
*  the constraints that apply to artificial intelligence and to human intelligence are
*  very different and your test should account for this difference because if you get artificial
*  systems it's always possible for an experimenter to buy arbitrary levels of skill at arbitrary
*  tasks either by injecting hard-coded prior knowledge into the system via rules and so on
*  that come from the human mind, from the minds of the programmers and also buying higher levels of
*  skill just by training on more data. For instance, you could generate an infinity of different Go
*  games and you could train a Go playing system that way but you could not directly compare it
*  to human Go playing skills because a human that plays Go had to develop that skill in a very
*  constrained environment. They had a limited amount of time, they had a limited amount of energy
*  and of course this started from a different set of priors, this started from innate human priors.
*  So I think if you want to compare the intelligence of two systems like the intelligence of an AI
*  and the intelligence of a human you have to control for priors, you have to
*  start from the same set of knowledge priors about the task and you have to control for
*  experience that is to say for training data. So what's priors? So prior is whatever information
*  you have about a given task before you start learning about this task. And how's that
*  different from experience? Well experience is acquired, right? So for instance if you're
*  trying to play Go, your experience with Go is all the Go games you've played or you've seen
*  or you've simulated in your mind let's say and your priors are things like well Go is a game on
*  a 2D grid and we have lots of hard-coded priors about the organization of 2D space.
*  And so rules of how the dynamics of this, the physics of this game in the studio space. Yes.
*  And the idea that you have what winning is. Yes exactly. And all other board games can also share
*  some similarities to Go and if you've played these board games then with respect to the game of Go
*  that would be part of your priors about the game. Well it's interesting to think about the game of
*  Go is how many priors are actually brought to the table. When you look at self-play reinforcement
*  learning-based mechanisms that do learning it seems like the number of priors is pretty low.
*  Yes. But you're saying you should be... There is a 2D spatial priors in the covenant. Right. But you
*  should be clear at making those priors explicit. Yes. So in particular I think if your goal is to
*  measure a human-like form of intelligence then you should clearly establish that you want the AI you're
*  testing to start from the same set of priors that humans start with. Right. So I mean to me personally
*  but I think to a lot of people the human side of things is very interesting. So testing intelligence
*  for humans. What do you think is a good test of human intelligence? Well that's the question that
*  psychometrics is interested in. There's an entire subfield of psychology that deals with this question.
*  So what's psychometrics? The psychometrics is the subfield of psychology that tries to measure,
*  quantify aspects of the human mind. So in particular community abilities, intelligence
*  and personality traits as well. So like what are, it might be a weird question, but what are like the
*  first principles of psychometrics that operates on what are the priors it brings to the table?
*  So it's a field with a fairly long history. So you know psychology sometimes gets a bad reputation
*  for not having very reproducible results and some psychometrics has actually some fairly
*  solidly reproducible results. So the ideal goals of the field is a test should be reliable, which
*  is a notion tied to reproducibility. It should be valid, meaning that it should actually measure
*  what you say it measures. So for instance, if you're saying that you're measuring intelligence,
*  then your test results should be correlated with things that you expect to be correlated with
*  intelligence like success in school or success in the workplace and so on, should be standardized,
*  meaning that you can administer your test to many different people in the same conditions.
*  And it should be free from bias, meaning that for instance, if your test involves the English
*  language, then you have to be aware that this creates a bias against people who have English
*  as their second language or people who can't speak English at all. So of course, this
*  principles for creating psychometric tests are very much night y'all. I don't think every
*  psychometric test is really either reliable, valid or free from bias, but at least the field is aware
*  of these weaknesses and is trying to address them. So it's kind of interesting.
*  Ultimately, you're only able to measure, like you said previously, the skill,
*  but you're trying to do a bunch of measures of different skills that correlate.
*  You mentioned strongly with some general concept of cognitive ability.
*  Yes. Yes.
*  What's the G factor?
*  So right, there are many different kinds of tests of intelligence and each of them is interested
*  in different aspects of intelligence. Some of them will deal with language, some of them
*  will deal with spatial vision, maybe mental rotations, numbers and so on. When you run
*  these very different tests at scale, what you start seeing is that there are clusters of
*  correlations among test results. So for instance, if you look at homework at school, you will see
*  that people who do well at math are also likely statistically to do well in physics. And what's
*  more, there are also people who do well at math and physics are also statistically likely to do
*  well in things that sound completely unrelated, like writing an English essay, for instance.
*  So when you see clusters of correlations in statistical terms, you would explain them with
*  a latent variable. And the latent variable that would, for instance, explain the relationship
*  between being good at math and being good at physics would be cognitive ability. And the G
*  factor is the latent variable that explains the fact that every test of intelligence that you can
*  come up with results on this test end up being correlated. So there is some single unique variable
*  that explains these correlations. That's the G factor. So it's a statistical construct. It's
*  not really something you can directly measure, for instance, in a person.
*  But it's there.
*  But it's there. It's there. It's there at scale. And that's also one thing I want to mention about
*  psychometrics. When you talk about measuring intelligence in humans, for instance, some people
*  get a little bit worried. They will say, that sounds dangerous. Maybe that's not potentially
*  discriminatory and so on. And they're not wrong. And the thing is, personally, I'm not interested
*  in psychometrics as a way to characterize one individual person. Like if I get your
*  psychometric personality assessment or your IQ, I don't think that actually tells me much
*  about you as a person. I think psychometrics is most useful as a statistical tool. So it's
*  most useful at scale. It's most useful when you start getting test results for a large number of
*  people and you start cross-correlating these test results. Because that gives you information about
*  the structure of the human mind, in particular about the structure of human cognitive abilities.
*  So at scale, psychometrics paints a certain picture of the human mind. And that's interesting.
*  And that's what's relevant to AI, the structure of human cognitive abilities.
*  Yeah. It gives you an insight into it. I mean, to me, I remember when I learned about G factor,
*  it seemed like it would be impossible for it to be real, even as a statistical variable. It felt
*  kind of like astrology. It's like wishful thinking among psychologists. But the more I learned,
*  I realized that there's some... I mean, I'm not sure what to make about human beings, the fact that
*  the G factor is a thing. There's a commonality across all of human species, that there does seem
*  to be a strong correlation between cognitive abilities. That's kind of fascinating.
*  So human cognitive abilities have a structure, like the most mainstream theory of the structure
*  of cognitive abilities is called CHC theory. So Cattle, Horn, Carol, it's the name of the three
*  psychologists who contributed key pieces of it. And it describes cognitive abilities as a hierarchy
*  with three levels. And at the top, you have the G factor, then you have broad cognitive abilities,
*  for instance, fluid intelligence, right? That encompass a broad set of possible kinds of tasks
*  that are all related. And then you have narrow cognitive abilities at the last level, which is
*  closer to task specific skill. And there are actually different theories of the structure
*  of cognitive abilities that just emerge from different statistical analysis of IQ test results.
*  But they all describe a hierarchy with a kind of G factor at the top. And you're right that the G
*  factor is... It's not quite real in the sense that it's not something you can observe and measure,
*  like your height, for instance. But it's really in the sense that you see it in a statistical
*  analysis of the data. One thing I want to mention is that the fact that there is a G factor does
*  not really mean that human intelligence is general in a strong sense. It does not mean human intelligence
*  can be applied to any problem at all. And that someone who has a high IQ is going to be able to
*  solve any problem at all. That's not quite what it means. I think one popular analogy to understand
*  it is the sports analogy. If you consider the concept of physical fitness, it's a concept that's
*  very similar to intelligence because it's a useful concept. It's something you can intuitively
*  understand. Some people are fit, maybe like you. Some people are not as fit, maybe like me.
*  But none of us can fly. Absolutely. Even if you're very fit, that doesn't mean you can do
*  anything at all in any environment. You obviously cannot fly. You cannot survive at the bottom of
*  the ocean and so on. And if you were a scientist and you wanted to precisely define and measure
*  a physical fitness in humans, then you would come up with a battery of tests. You would have running
*  100 meters, playing soccer, playing table tennis, swimming, and so on. And if you run these tests
*  over many different people, you would start seeing correlations in test results. For instance,
*  people who are good at soccer are also good at sprinting. And you would explain these correlations
*  with physical abilities that are strictly analogous to cognitive abilities. And then you would start
*  also observing correlations between biological characteristics, like maybe lung volume is
*  correlated with being a fast runner, for instance. In the same way that there are
*  neurophysical correlates of cognitive abilities. And at the top of the hierarchy of physical
*  abilities that you would be able to observe, you would have a physical G factor, which would map
*  to physical fitness. And as you just said, that doesn't mean that people with high physical
*  fitness can fly. It doesn't mean human morphology and human physiology is universal. It's actually
*  super specialized. We can only do the things that we were evolved to do. You could not exist on
*  Venus or Mars or in the void of space, but on the ocean. So that said, one thing that's really
*  striking and remarkable is that our morphology generalizes far beyond the environments that we
*  evolved for. Like in a way you could say we evolved to run after prey in the savanna, right? That's
*  very much where our human morphology comes from. And that said, we can do a lot of things that are
*  completely unrelated to that. We can climb mountains. We can swim across lakes. We can
*  play table tennis. Table tennis is very different from what we were evolved to do. So our morphology,
*  our bodies, our sense and motor affordances have a degree of generality that is absolutely remarkable.
*  And I think cognition is very similar to that. Our cognitive abilities have a degree of generality
*  that goes far beyond what the mind was initially supposed to do, which is why we can play music
*  and write novels and go to Mars and do all kinds of crazy things. But it's not universal in the same
*  way that human morphology and our body is not appropriate for actually most of the universe by
*  volume. In the same way you could say that the human mind is naturally appropriate for most of
*  problem space, potential problem space by volume. So we have very strong cognitive biases, actually,
*  that mean that there are certain types of problems that we handle very well and certain types of
*  problems that we are completely inelipted for. So that's really how we interpret the G factor.
*  It's not a sign of strong generality. It's really just the broadest cognitive ability.
*  But our abilities, whether we are talking about sensory motor abilities, our cognitive abilities,
*  they still remain very specialized in the human condition.
*  Within the constraints of the human cognition, they're general.
*  Yes, absolutely.
*  But the constraints, as you're saying, are very limited.
*  We evolved our cognition and our body evolved in very specific environments
*  because our environment was so variable, fast changing, and so unpredictable. Part of the
*  constraints that drove our evolution is generality itself. So we were in a way evolved to be able to
*  improvise in all kinds of physical or cognitive environments. And for this reason, it turns out
*  that the minds and bodies that we ended up with can be applied to much, much broader scope than
*  what they were evolved for. And that's truly remarkable. And that's a degree of generalization
*  that is far beyond anything you can see in artificial systems today. It does not mean that
*  human intelligence is anywhere universal.
*  Yes, it's not general. It's a kind of exciting topic for people even outside of artificial
*  intelligence, IQ tests. I think it's Mensa, whatever. There's different degrees of difficulty
*  for questions. We talked about this offline a little bit too about difficult questions.
*  What makes a question on an IQ test more difficult or less difficult, do you think?
*  So the thing to keep in mind is that there's no such thing as a question that's intrinsically
*  difficult. It has to be difficult to suspect to the things you already know and the things you
*  can already do. So in terms of an IQ test question, typically it will be structured, for instance,
*  as a set of demonstration input and output pairs. And then you would be given a test input, a prompt,
*  and you would need to recognize or produce the corresponding output. And in that narrow context,
*  you could say a difficult question is a question where the input prompt is very surprising and
*  unexpected given the training examples. Just even the nature of the patterns that you're observing
*  in the input prompt. For instance, let's say you have a rotation problem. You must write it a shape
*  by 90 degrees. If I give you two examples and then I give you one prompt, which is actually one of
*  the two training examples, then there is zero generalization difficulty for the task. It's
*  actually a trivial task. You just recognize that it's one of the training examples and you produce
*  the same answer. Now, if it's a more complex shape, there is a little bit more generalization,
*  but it remains that you are still doing the same thing at test time as you were being demonstrated
*  at training time. A difficult task is a task that will require some amount of test time adaptation,
*  some amount of improvisation. Consider, I don't know, you're teaching a class on quantum physics
*  or something. If you wanted to test the understanding that students have of the material,
*  you would come up with an exam that's very different from anything they've seen
*  on the internet when they were cramming. On the other hand, if you wanted to make it easy,
*  you would just give them something that's very similar to the mock exams that they've taken,
*  something that's just a simple interpolation of questions that they've already seen.
*  And so that would be an easy exam. It's very similar to what you've been trained on.
*  And a difficult exam is one that really probes your understanding because it forces you
*  to improvise. It forces you to do things that are different from what you were exposed to before.
*  So that said, it doesn't mean that the exam that requires improvisation is intrinsically hard,
*  because maybe you're a quantum physics expert, so when you take the exam, this is actually stuff
*  that despite being new to the students, it's not new to you. So it can only be difficult with
*  respect to what the test taker already knows and with respect to the information that the test
*  taker has about the task. So that's what I mean by controlling for priors, what the information
*  brings to the table and the experience, which is the training data. So in the case of the quantum
*  physics exam, that would be all the course material itself and all the mock exams that students
*  might have taken online. Yeah, it's interesting because I've also, I sent you an email, I asked
*  you, I've been, this is just this curious question of what's a really hard IQ test question. And I've
*  been talking to also people who have designed IQ tests. There's a few folks on the internet,
*  it's like a thing, people are really curious about it. First of all, most of the IQ tests they designed,
*  they like religiously protect against the correct answers. Like you can't find the correct answers
*  anywhere. In fact, the question is ruined once you know, even like the approach you're supposed to
*  take. So they're very- That said, the approach is implicit in the training examples. So if you
*  release the training examples, it's over. Which is why in Arc, for instance, there is a test set that
*  is private and no one has seen it. No, for really tough IQ questions, it's not obvious. It's not
*  because the ambiguity. Like it's, I mean, we'll have to look to them, but like some number
*  sequences and so on, it's not completely clear. So like you can get a sense, but there's like some,
*  when you look at a number sequence, I don't know, like you've had a number sequence,
*  if you look at the first few numbers, that sequence could be completed in a lot of different ways.
*  And some are, if you think deeply, are more correct than others. Like there's a kind of intuitive
*  simplicity and elegance to the correct solution. Yes. I am personally not a fan of ambiguity
*  in test questions actually, but I think you can have difficulty without requiring ambiguity
*  simply by making the test require a lot of extrapolation over the training examples.
*  But the beautiful question is difficult, but gives away everything when you give the training
*  example. Basically, yes. Meaning that, so the tests I'm interested in creating are not necessarily
*  difficult for humans because human intelligence is the benchmark. They're supposed to be difficult
*  for machines in ways that are easy for humans. Like I think an ideal test of human and machine
*  intelligence is a test that is actionable, that highlights the need for progress and that
*  highlights the direction in which you should be making progress. I think we'll talk about
*  the RARC challenge and the test you've constructed and you have these elegant examples.
*  I think that highlight, like this is really easy for us humans, but it's really hard for machines.
*  But on the designing an IQ test for IQs of like higher than 160 and so on,
*  you have to take that and put it on a stairways. You have to think like what is hard for humans.
*  That's a fascinating exercise in itself, I think. It was an interesting question of what it takes
*  to create a really hard question for humans because you again have to do the same process
*  as you mentioned, which is something basically where the experience that you have likely to
*  have encountered throughout your whole life, even if you've prepared for IQ tests, which is a big
*  challenge, that this will still be novel for you. Yeah. Novelty is a requirement. You should not
*  be able to practice for the questions that you're going to be tested on. That's important because
*  otherwise what you're doing is not exhibiting intelligence. What you're doing is just retrieving
*  what you've been exposed before. It's the same thing as deep learning model. If you train a deep
*  learning model on all the possible answers, then it will ace your test in the same way that
*  a stupid student can still ace the test if they cram for it. They memorize a hundred different
*  possible mock exams and then they hope that the actual exam will be a very simple interpolation
*  of the mock exams. That student could just be a deep learning model at that point, but you can
*  actually do that without any understanding of the material. In fact, many students pass the exams
*  exactly this way. If you want to avoid that, you need an exam that's unlike anything they've seen,
*  that re-probes their understanding. How do we design an IQ test for machines,
*  an intelligent test for machines? In the paper, I outline a number of requirements
*  that you expect of such a test. In particular, we should start by acknowledging
*  the priors that we expect to be required in order to perform the test. We should be explicit about
*  the priors. If the goal is to compare machine intelligence and human intelligence, then we
*  should assume human cognitive priors. Secondly, we should make sure that we are testing for skill
*  acquisition ability, skill acquisition efficiency in particular, and not for skill itself, meaning
*  that every task featured in your test should be novel and should not be something that you can
*  anticipate. For instance, it should not be possible to brute force the space of possible questions,
*  to pre-generate every possible question and answer. It should be tasks that cannot be anticipated
*  not just by the system itself, but by the creators of the system.
*  Yeah. You know what's fascinating? One of my favorite aspects of the paper and the work you
*  do with the ARC challenge is the process of making priors explicit. Just even that act alone
*  is a really powerful one. It's a really powerful question to ask of us humans. What are the priors
*  that we bring to the table? The next step is once you have those priors, how do you use them to
*  solve a novel task? Just even making the priors explicit is a really difficult and really powerful
*  step. That's visually beautiful and conceptually, philosophically beautiful part of the work you
*  did with, and I guess continue to do probably with the paper and the ARC challenge. Can you
*  talk about some of the priors that we're talking about here? Yes. A researcher that has done a lot
*  of work on what exactly are the knowledge priors that are innate to humans is Elizabeth Spalke
*  from Harvard. She developed the core knowledge theory, which outlines four different core
*  knowledge systems. Systems of knowledge that we are basically either born with or that we are
*  hardwired to acquire very early on in our development. There's no strong
*  distinction between the two. If you are primed to acquire a certain type of knowledge in just a few
*  weeks, you might as well just be born with it. It's just part of who you are. There are four
*  different core knowledge systems. The first one is the notion of objectness and basic physics.
*  You recognize that something that moves currently, for instance, is an object.
*  We intuitively, naturally, innately divide the world into objects based on this notion of
*  physical coherence. In terms of filamentary physics, there's the fact that objects can bump
*  against each other and the fact that they can occlude each other. These are things that we are
*  essentially born with or at least that we are going to be acquiring extremely
*  early because we're really hardwired to acquire them. A bunch of points, pixels that move together
*  are an object. I'm partly the same object. I don't smoke weed, but if I did,
*  that's something I could sit all night and just think about. I remember writing in your paper,
*  just objectness. I wasn't self-aware, I guess, of that particular prior. That's such a fascinating
*  prior. That's the most basic one. But objectness, just identity. Yeah, objectness. It's very basic,
*  I suppose, but it's so fundamental. It is fundamental to human cognition.
*  The second prior that's also fundamental is agentness, which is not a real world.
*  A real world. Agentness. The fact that some of these objects that you segment your environment
*  into, some of these objects are agents. What's an agent? Basically, it's an object that has goals.
*  That has what? That has goals. There's a table of person goals. For instance, if you see two dots
*  moving in a roughly synchronized fashion, you will intuitively infer that one of the dots
*  is pursuing the other. One of the dots is an agent, and its goal is to avoid the other dot.
*  And one of the dots, the other dot, is also an agent, and its goal is to catch the first dot.
*  Pellky has shown that babies as young as three months identify agentness and goal
*  directedness in their environment. Another prior is basic geometry and topology,
*  like the notion of distance, the ability to navigate in your environment, and so on.
*  This is something that is fundamentally hardwired into our brain. It's in fact backed by
*  very specific neural mechanisms, like for instance, grid cells and plate cells.
*  It's something that's literally hardcoded at the neural level in our hippocampus.
*  The last prior would be the notion of numbers. Numbers are not actually cultural constructs.
*  We are intuitively, innately able to do some basic counting and to compare quantities.
*  It doesn't mean we can do arbitrary arithmetic.
*  Counting, the act of counting.
*  That's counting, like counting one, two, three, then maybe more than three.
*  You can also compare quantities. If I give you three dots and five dots, you can tell
*  the side with five dots as more dots. This is actually an innate prior.
*  That said, the list may not be exhaustive. Spelky is still pursuing
*  the potential existence of new knowledge systems, for instance,
*  knowledge systems that would deal with social relationships.
*  Which is much less relevant to something like ARC or IQ tests.
*  There could be stuff like rotation or symmetry. Is it really interesting?
*  It's very likely that there is, speaking about rotation, that there is in the brain
*  a hard-coded system that is capable of performing rotations. One famous experiment that people did
*  in the 70s was that people found that if you asked people, if you give them two different shapes,
*  and one of the shapes is a rotated version of the first shape, and you ask them,
*  is that shape a rotated version of the first shape or not? What you see is that the time it takes
*  people to answer is the time it takes them to answer the question, is that shape a rotated
*  version of the first shape or not? What you see is that the time it takes people to answer
*  is linearly proportional to the angle of rotation. It's almost like you have it somewhere in your
*  brain, like a turntable with a fixed speed. If you want to know if two objects are rotated
*  versions of each other, you put the object on the turntable, you let it move around a little bit,
*  and then you stop when you have a match. That's really interesting.
*  What's the arc challenge?
*  In the paper, I outline all these principles that a good test of machine intelligence and
*  human intelligence should follow. The arc challenge is one attempt to embody as many of these principles
*  as possible. I don't think it's anywhere near a perfect attempt. It does not actually follow
*  every principle, but it is what I was able to do given the constraints. The format of arc is very
*  similar to classic IQ tests, in particular Raven's progressive matrices. If you've done IQ tests in
*  the past, you know what that is probably, or at least you've seen it, even if you don't know
*  what it's called. You have a set of tasks, that's what they're called, and for each task you have
*  training data, which is a set of input and output pairs. An input or output pair is a grid
*  of colors, basically. The size of the grid is variable. You're given an input and you must
*  transform it into the proper output. You're shown a few demonstrations of a task in the form of
*  existing input-output pairs, and then you're given a new input. You must produce the correct output.
*  The assumptions in arc is that every task should only require
*  core knowledge priors, should not require any outside knowledge. For instance, no language,
*  no English, nothing like this. No concepts taken from all human experience like trees, dogs, cats,
*  and so on. Only reasoning tasks that are built on top of core knowledge priors. Some of the tasks are
*  actually explicitly trying to probe specific forms of abstraction. Part of the reason why I wanted to
*  create arc is I'm a big believer in when you're faced with a problem as murky as understanding
*  how to autonomously generate abstraction in a machine, you have to co-evolve the solution
*  and the problem. Part of the reason why I designed arc was to clarify my ideas about the nature of
*  abstraction. Some of the tasks are actually designed to probe bits of that theory. There are
*  things that turn out to be very easy for humans to perform, including young kids,
*  but turn out to be near impossible for machines. What have you learned from the nature of abstraction
*  from designing that? Can you clarify what you mean one of the things you wanted to try to understand
*  was this idea of abstraction? Yes. Clarifying my own ideas about abstraction by forcing myself
*  to produce tasks that would require the ability to produce that form of abstraction in order to
*  solve them. Got it. By the way, people should check out, I'll probably overlay if you're watching
*  the video part, but the grid input output with the different colors on the grid, that's it.
*  It's a very simple world, but it's kind of beautiful. It's very similar to classic IQ
*  tests. It's not very original in that sense. The main difference with IQ tests is that
*  we make the priors explicit, which is not usually the case in IQ tests.
*  So you make it explicit that everything should only be built on top of core knowledge priors.
*  I also think it's generally more diverse than IQ tests in general. It perhaps requires a bit more
*  manual work to produce solutions because you have to click around on a grid for a while. Sometimes
*  the grids can be as large as study by study cells. How did you come up, if you can reveal,
*  with the questions? What's the process of the questions? Was it mostly you that came up with
*  the questions? How difficult is it to come up with a question? Is this scalable to a much larger
*  number? With IQ tests, you might not necessarily want it to or need it to be scalable. With machines,
*  it's possible you could argue that it needs to be scalable.
*  So there are a thousand questions, a thousand tasks in the Lord, including the test set,
*  the prior test set. I think it's fairly difficult in the sense that a big requirement
*  is that every task should be novel and unique and unpredictable. You don't want to create
*  your own little world that is simple enough that it would be possible for a human to
*  reverse and generate and write down an algorithm that could generate every possible hard task and
*  their solutions, for instance, that would completely invalidate the test.
*  You're constantly coming up with new stuff.
*  Yeah, you need a source of novelty, of infacable novelty. One thing I found is that as a human,
*  you are not a very good source of infacable novelty. You have to pace the creation of these
*  tasks quite a bit. There are only so many unique tasks that you can do in a given day.
*  So that means coming up with truly original new ideas. Did psychedelics help you at all?
*  But that's fascinating to think about. So you would be walking or something like that.
*  Are you constantly thinking of something totally new?
*  Yes.
*  I mean, this is hard.
*  Yeah, I mean, I'm not saying you've done anywhere near a perfect job at it. There is some
*  amount of redundancy and there are many imperfections in ARC. So that said, you should
*  consider ARC as a work in progress. It is not the definitive state. The ARC tasks today are not
*  definitive states of the test. I want to keep refining it in the future. I also think it should
*  be possible to open up the creation of tasks to a broad audience to do crowdsourcing. That would
*  involve several levels of filtering, obviously, but I think it's possible to apply crowdsourcing
*  to develop a much bigger and much more diverse ARC data set. That would also be free of potentially
*  some of my own personal biases.
*  Does there always need to be a part of ARC that the test is hidden?
*  Yes, absolutely. It is imperative that the tests that you're using to actually
*  benchmark algorithms is not accessible to the people developing these algorithms.
*  Because otherwise, what's going to happen is that the human engineers are just going to
*  solve the tasks themselves and encode their solution in program form. But that, again,
*  what you're seeing here is the process of intelligence happening in the mind of the
*  human and then you're just capturing its crystallized output. But that crystallized output
*  is not the same thing as the process that's generated. It's not intelligent.
*  By the way, the idea of crowdsourcing it is fascinating. I think the creation of questions
*  is really exciting for people. I think there's a lot of really brilliant people out there that
*  love to create these kinds of stuff.
*  Yeah. One thing that kind of surprised me that I wasn't expecting is that
*  lots of people seem to actually enjoy ARC as a kind of game. And I was really seeing it as a test,
*  as a benchmark of fluid general intelligence. And lots of people, including kids,
*  just started enjoying it as a game. So I think that's encouraging.
*  Yeah, I'm fascinated by it. There's a world of people who create IQ questions.
*  I think that's a cool activity for machines and for humans. Humans are themselves fascinated by
*  taking the questions, like measuring their own intelligence. That's just really compelling.
*  It's really interesting to me, too. One of the cool things about ARC, you said, is it's kind of
*  inspired by IQ tests or whatever, it follows a similar process. But because of its nature,
*  because of the context in which it lives, it immediately forces you to think about the nature
*  of intelligence as opposed to just the test of your own. It forces you to really think. I don't
*  know if it's within the question, inherent in the question, or just the fact that it lives in a test
*  that's supposed to be a test of machine intelligence.
*  Absolutely. As you solve ARC tasks as a human, you will be forced to basically introspect
*  how you come up with solutions. And that forces you to reflect on the human problem-solving process
*  and the way your own mind generates abstract representations of the problems it's exposed to.
*  I think it's due to the fact that the set of core knowledge priors that ARC is built upon is so
*  small. It's all a recombination of a very, very small set of assumptions.
*  Okay. So what's the future of ARC? You held ARC as a challenge, as part of a Kaggle competition.
*  Kaggle competition. Do you think this is something that continues for
*  five years, 10 years, just continues growing?
*  Yes, absolutely. ARC itself will keep evolving. I've talked about crowdsourcing. I think that's a
*  good avenue. Another thing I'm studying is I'll be collaborating with folks from the psychology
*  department at NYU to do human testing on ARC. And I think there are lots of interesting questions
*  you can start asking, especially as you start correlating machine solutions to ARC tasks and
*  the human characteristics of solutions. For instance, you can try to see if there's a
*  relationship between the human perceived difficulty of a task and-
*  Machine perceived.
*  Yes, and exactly some measure of machine perceived difficulty.
*  Yeah. It's a nice playground in which to explore this very difference. It's the same thing as we
*  talked about with autonomous vehicles. The things that could be difficult for humans might be very
*  different than the things that are difficult. And formalizing or making explicit that difference
*  in difficulty may teach us something fundamental about intelligence.
*  One thing I think we did well with ARC is that it's proving to be a very actionable test in the
*  sense that machine performance on ARC started at very much zero initially, while humans found
*  actually the tasks very easy. And that alone was like a big red flashing light saying that
*  something is going on and that we are missing something. And at the same time, machine performance
*  did not stay at zero for very long actually within two weeks of the Kaggle competition,
*  we started having a non-zero number and now the state of the art is around 20% of the test set
*  solved. And so ARC is actually a challenge where our capabilities start at zero, which
*  indicates the need for progress, but it's also not an impossible challenge. It's not accessible.
*  You can start making progress basically right away. At the same time, we are still very far from having
*  solved it. And that's actually a very positive outcome of the competition is that the competition
*  has proven that there was no obvious shortcuts to solve these tasks.
*  Yeah. So the test held up.
*  Yeah, exactly. That was the primary reason to the Kaggle competition is to check if some clever
*  person was going to hack the benchmark. That did not happen. People who are solving the tasks are
*  essentially doing it... Well, in a way, they're actually exploring some flaws of ARC that we will
*  need to address in the future, especially they're essentially anticipating what sort of tasks may
*  be contained in the test set. Right. Which is kind of... Yeah, that's the kind of hacking.
*  It's human hacking of the test. Yes. That said, with the state of the art, it's like 20%. We're
*  still very, very far from human level, which is closer to 100%. And I do believe that it will
*  take a while until we reach human parity on ARC. And that by the time we have human parity,
*  we will have AI systems that are probably pretty close to human level in terms of
*  general fluid intelligence, which is... I mean, they're not going to be necessarily human-like.
*  They're not necessarily... You would not necessarily recognize them as being an AI,
*  but they would be capable of a degree of generalization that matches the generalization
*  performed by human fluid intelligence. Sure. I mean, this is a good point in terms of
*  general fluid intelligence to mention. In your paper, you describe different kinds of generalizations,
*  local, broad, extreme, and there's a kind of hierarchy that you form. So when we say
*  generalizations, what are we talking about? What kinds are there?
*  Right. So generalization is a very old idea. I mean, it's even older than machine learning.
*  In the context of machine learning, you say a system generalizes if it can make sense
*  of an input it has not yet seen. And that's what I would call a system-centric
*  generalization. It's generalization with respect to novelty for the specific system you're
*  considering. So I think a good test of intelligence should actually deal with
*  developer-aware generalization, which is slightly stronger than system-centric
*  generalization. So developer-aware generalization would be the ability to generalize to novelty or
*  uncertainty that not only the system itself has not access to, but the developer of the system
*  could not have access to either. That's a fascinating meta definition. So like the system
*  is basically the edge case thing we're talking about with autonomous vehicles.
*  Neither the developer nor the system know about the edge cases it may encounter. So it's up to
*  the system to be able to generalize the thing that nobody expected. Neither the designer of
*  the training data nor obviously the contents of the training data. That's a fascinating definition.
*  You can see degrees of generalization as a spectrum. And the lowest level is what machine
*  learning is trying to do, is the assumption that any new situation is going to be sampled
*  from a static distribution of possible situations and that you already have
*  a representative sample of that distribution. That's your training data. And so in machine
*  learning, you generalize to a new sample from a known distribution. And the ways in which your
*  new sample will be new or different are ways that are already understood by the developers
*  of the system. So you are generalizing to known unknowns for one specific task. That's what you
*  would call robustness. You are robust to things like noise, small variations and so on. For one,
*  a fixed known distribution that you know through your training data. And a higher degree would be
*  flexibility in machine intelligence. So flexibility would be something like an L5 cell driving car,
*  or maybe a robot that can pass the coffee cup test, which is the notion that you would be given a
*  random kitchen somewhere in the country and you would have to go make a cup of coffee in that
*  kitchen. So flexibility would be the ability to deal with unknown unknowns. Dimensions of variability
*  that could not have been possibly foreseen by the creators of the system within one specific task.
*  So generalizing to the long tail of situations in self-driving, for instance, would be flexibility.
*  So you have robustness, flexibility, and finally, we'd have extreme generalization, which is
*  basically flexibility. But instead of just considering one specific domain like driving
*  or domestic robotics, you're considering an open-ended range of possible domains. So
*  a robot would be capable of extreme generalization if, let's say, it's designed and trained
*  to cook, for cooking, for instance. And if I buy the robot and if it's able to teach itself
*  gardening in a couple of weeks, it would be capable of extreme generalization, for instance.
*  So the ultimate goal is extreme generalization.
*  Yes. So creating a system that is so general that it could essentially achieve a human skill parity
*  over arbitrary tasks and arbitrary domains with the same level of improvisation and adaptation
*  power as humans when it encounters new situations. And it would do so over basically the same range
*  of possible domains and tasks as humans and using essentially the same amount of training
*  experience, of practice, as humans would require. That would be human-level extreme generalization.
*  I don't actually think humans are anywhere near the optimal intelligence bound,
*  if there is such a thing. So I think...
*  For humans or in general?
*  In general. I think it's quite likely that there is a hard limit to how intelligent
*  any system can be. But at the same time, I don't think humans are anywhere near that limit.
*  Yeah. Last time I think we talked, I think you had this idea that we're only as intelligent as the
*  problems we face. Sort of...
*  Yes. Intelligence.
*  We are upper bounded by the problems.
*  In a way, yes. We are bounded by our environments and we are bounded by the problems we try to solve.
*  Yeah. What do you make of Neuralink and outsourcing some of the brain power,
*  like brain-computer interfaces? Do you think we can expand our, augment our intelligence?
*  I am fairly skeptical of neural interfaces because they are trying to fix one specific bottleneck
*  in human-machine cognition, which is the bandwidth bottleneck, input and output of information
*  in the brain. And my perception of the problem is that bandwidth is not at this time a bottleneck
*  at all. Meaning that we already have senses that enable us to take in
*  far more information than what we can actually process.
*  Well, to push back on that a little bit, to sort of play devil's advocate a little bit,
*  is if you look at the internet, the Wikipedia, let's say Wikipedia,
*  I would say that humans, after the advent of Wikipedia, are much more intelligent.
*  Yes. I think that's a good one. But that's also not about, that's about externalizing
*  our intelligence via information processing systems, the external information processing
*  system, which is very different from brain-computer interfaces.
*  Right. But the question is whether if we have direct access, if our brain has direct access
*  to Wikipedia without having...
*  Your brain already has direct access to Wikipedia. It's on your phone and you have your hands and
*  your eyes and your ears and so on to access that information. And the speed at which you can access
*  it is...
*  Is bottlenecked by the cognition.
*  I think it's already close, fairly close to optimal, which is why speed reading, for instance,
*  does not work. The faster you read, the less you understand.
*  But maybe it's because it uses the eyes. So maybe...
*  So I don't believe so. I think the brain is very slow. It typically operates at the fastest things
*  that happen in the brain at the level of 50 milliseconds. Forming a conscious thought
*  can potentially take entire seconds. And you can already read pretty fast. So I think the speed
*  at which you can take information in and even the speed at which you can add with information
*  can only be very incrementally improved.
*  If you're a very fast typer, if you're a very trained typer, the speed at which you can
*  express your thoughts is already the speed at which you can form your thoughts.
*  Right. So that's kind of an idea that there are fundamental bottlenecks to the human mind,
*  but it's possible that everything we have in the human mind is just to be able to survive in the
*  environment. And there's a lot more to expand. Maybe, you said the speed of the thought.
*  So I think augmenting human intelligence is a very valid and very powerful avenue.
*  And that's what computers are about. In fact, that's what all of culture and civilization is
*  about. Culture is externalized cognition and we rely on culture to think constantly.
*  Not just computers, not just phones and the internet. All of culture, like language,
*  for instance, is a form of externalized cognition. Books are obviously externalized cognition.
*  Yeah, that's a good point.
*  And you can scale that externalized cognition far beyond the capability of the human brain.
*  And you could see civilization itself has capabilities that are far beyond any individual
*  brain. And we'll keep scaling it because it's not rebounded by individual brains.
*  It's a different kind of system.
*  Yeah. And that system includes non-humans. First of all, it includes all the other biological
*  systems, which are probably contributing to the overall intelligence of the organism.
*  And then computers are part of it.
*  Non-human systems probably not contributing much, but
*  AIs are definitely contributing to that. Like Google search, for instance, is a big part of it.
*  Yeah. Yeah. A huge part. A part that we can't probably introspect.
*  How the world has changed in the past 20 years is probably very difficult for us to be able to
*  understand until, of course, whoever created the simulation wherein is probably doing metrics,
*  measuring the progress. There was probably a big spike in performance. They're enjoying this.
*  So what are your thoughts on the Turing test and the Lobner prize, which is one of the most famous
*  attempts at the test of artificial intelligence by doing a natural language open dialogue
*  test that's judged by humans as far as how well the machine did.
*  So I'm not a fan of the Turing test itself or any of its variants for two reasons.
*  So first of all, it's really copping out of trying to define and measure intelligence
*  because it's entirely outsourcing that to a panel of human judges. And these human judges,
*  they may not themselves have any proper methodology. They may not themselves have
*  any proper definition of intelligence. They may not be reliable. So the Turing test is already
*  failing one of the core psychometric principles, which is reliability because you have biased
*  human judges. It's also violating the standardization requirement and the freedom from
*  bias requirement. And so it's really a cop out because you are outsourcing everything that
*  matters, which is precisely describing intelligence and finding a standalone test
*  to measure it. You're outsourcing everything to people. So it's really a cop out. And by the way,
*  we should keep in mind that when Turing proposed the imitation game, it was not meaning for the
*  imitation game to be an actual goal for the field of AI, an actual test of intelligence.
*  He was using the imitation game as a thought experiment in a philosophical discussion
*  in his 1950 paper. He was trying to argue that theoretically it should be possible
*  for something very much like the human mind, indistinguishable from the human mind, to be
*  encoded in a Turing machine. And at the time, that was a very daring idea. It was stretching
*  credulity. But nowadays, I think it's fairly well accepted that the mind is an information
*  processing system and that you could probably encode it into a computer. So another reason why
*  I'm not a fan of this type of test is that the incentives that it creates are incentives that
*  are not conducive to proper scientific research. If your goal is to trick, to convince a panel
*  of human judges that they're talking to a human, then you have an incentive to rely on tricks and
*  prestidigitation. In the same way that let's say you're doing physics and you want to solve
*  teleportation. And what if the test that you set out to pass is you need to convince a panel of
*  judges that teleportation took place and they're just sitting there and watching what you're doing.
*  That is something that you can achieve with, David Copperfield could achieve it in his show at Vegas.
*  But what he's doing is very elaborate, but it's not actually, it's not physics. It's not making
*  any progress in our understanding of the universe. To push back on that as possible. That's the hope
*  with these kinds of subjective evaluations is that it's easier to solve it generally than it is to
*  come up with tricks that convince a large number of judges. That's the hope. In practice, when it
*  turns out that it's very easy to deceive people in the same way that you can do magic in Vegas,
*  you can actually very easily convince people that they're talking to a human when they're actually
*  talking to an algorithm. I disagree with that. I think it's easy. I would push, it's not easy.
*  It's doable. It's very easy because- I wouldn't say it's very easy though.
*  We are biased. We have theory of mind. We are constantly projecting emotions, intentions.
*  Agent-ness. Agent-ness is one of our core, innate priors. We are projecting these things on
*  everything around us. If you paint a smiley on a rock, the rock becomes happy in our eyes.
*  Because we have this extreme bias that permits everything we see around us,
*  it's actually pretty easy to trick people. I totally disagree with that. You brilliantly
*  put the anthropomorphization that we naturally do, the agent-ness of that word. Is that a real
*  word? No, it's not a real word. I like it. But it's a useful word. It's a useful word. Let's make it
*  real. It's a huge help. But I still think it's really difficult to convince. If you do like the
*  Alexa Prize formulation where you talk for an hour, there's formulations of the test you can create
*  where it's very difficult. I like the Alexa Prize better because it's more pragmatic. It's
*  more practical. It's actually incentivizing developers to create something that's useful
*  as a human machine interface. That's slightly better than just the imitation.
*  Your ideas like a test would hopefully help us in creating intelligent systems as a result. If you
*  create a system that passes it, it'll be useful for creating further intelligent systems.
*  Yes, at least.
*  Yeah. I mean, just to comment, I'm a little bit surprised how little inspiration people draw from
*  the Turing test today. The media and the popular press might write about it every once in a while.
*  The philosophers might talk about it. But most engineers are not really inspired by it.
*  And I know you don't like the Turing test, but we'll have this argument another time.
*  There's something inspiring about it, I think.
*  As a philosophical device in a philosophical discussion, I think there's something very
*  interesting about it. I don't think it is, in practical terms, conducive to progress.
*  And one of the reasons why is that I think being very human-like, being indistinguishable from a
*  human is actually the very last step in the creation of machine intelligence. That the first
*  AI that will show strong generalization, that will actually implement human-like broad cognitive
*  abilities, they will not actually behave or look anything like humans. Human-likeness is the very
*  last step in that process. And so a good test is a test that points you towards the first step
*  on the ladder, not towards the top of the ladder.
*  Right. So to push back on that, I usually agree with you on most things. I remember you, I think,
*  at some point tweeting something about the Turing test not being counterproductive or something like
*  that. And I think a lot of very smart people agree with that. A computation speaking, not very smart
*  person, disagree with that because I think there's some magic to the interactivity with other humans.
*  So to play devil's advocate on your statement, it's possible that in order to demonstrate the
*  generalization abilities of a system, you have to show your ability in conversation, show your
*  ability to adjust, adapt to the conversation through not just like as a standalone system,
*  but through the process of like the interaction, the game theoretic, where you really are changing
*  the environment by your actions. So in the ARC challenge, for example, you're an observer.
*  You can't scare the test into changing. You can't talk to the test. You can't play with it.
*  So there's some aspect of that interactivity that becomes highly subjective, but it feels like it
*  could be conducive to generalize. You make a great point. The interactivity is a very good setting
*  to force a system to show adaptation, to show generalization. That said, at the same time,
*  it's not something very scalable because you rely on human judges. It's not something reliable
*  because the human judges may not. So you don't like human judges.
*  Basically, yes. And I think so. I love the idea of interactivity. I initially wanted an ARC test
*  that had some amount of interactivity where your score on a task would not be one or zero,
*  if you can solve it or not, but would be the number of attempts that you can make before you
*  hit the right solution, which means that now you can start applying the scientific method
*  as you solve ARC tasks, that you can start formulating hypothesis and probing the system
*  to see whether the observation will match the hypothesis or not.
*  It would be amazing if you could also, even higher level than that, measure the quality
*  of your attempts, which of course is impossible, but again, that gets subjective. How good was
*  your thinking? How efficient was... So one thing that's interesting about this notion of
*  scoring you as how many attempts you need is that you can start producing tasks that are way more
*  ambiguous. Because with the different attempts, you can actually probe that ambiguity.
*  So that's in a sense, which is how good can you adapt to the uncertainty and reduce the uncertainty?
*  Yes. It's half fast. It's the efficiency with which to reduce uncertainty in program space.
*  Exactly. Very difficult to come up with that kind of test though.
*  Yeah. So I would love to be able to create something like this. In practice,
*  it would be very, very difficult, but yes. What you're doing, what you've done with
*  the ARC challenge is brilliant. I'm also surprised that it's not more popular,
*  but I think it's picking up. It has its niche.
*  It has its niche. Yeah. What are your thoughts about another test that I talked with Marcus
*  Hodder? He has the Hodder Prize for compression of human knowledge and the idea is really sort of
*  quantify and reduce the test of intelligence purely to just the ability to compress.
*  What's your thoughts about this intelligence as compression?
*  I mean, it's a very fun test because it's such a simple idea. You're given Wikipedia,
*  basically English Wikipedia, and you must compress it. And so it stems from the idea that
*  cognition is compression, that the brain is basically a compression algorithm. This is a very
*  old idea. It's a very, I think, striking and beautiful idea. I used to believe it. I eventually
*  had realized that it was very much a flawed idea, so I no longer believe that cognition is compression.
*  But I can tell you what's the difference. It's very easy to believe that cognition and compression
*  are the same thing. Jeff Hockens, for instance, says that cognition is prediction. And of course,
*  prediction is basically the same thing as compression, including the temporal axis.
*  It's very easy to believe this because compression is something that we do all the time,
*  very naturally. We are constantly compressing information. We have this bias towards simplicity.
*  We're constantly trying to organize things in our mind and around us to be more regular.
*  So it's a beautiful idea. It's very easy to believe. There is a big difference between
*  what we do with our brains and compression. So compression is actually a tool in the human
*  cognitive toolkit that is used in many ways, but it's just a tool. It is a tool for cognition. It
*  is not cognition itself. And the big fundamental difference is that cognition is about being able
*  to operate in future situations that include fundamental uncertainty and novelty. So for instance,
*  consider a child at age 10. And so they have 10 years of life experience. They've gotten pain,
*  pleasure, rewards, and punishment in that period of time. If you were to generate the shortest
*  behavioral program that would have basically run that child over these 10 years in an optimal way,
*  the shortest optimal behavioral program, given the experience of that child so far.
*  Well, that program, that compressed program, this is what you would get if the mind of the child
*  was a compression algorithm essentially, would be utterly unable, inappropriate to process the next
*  70 years in the life of that child. So in the models we build of the world, we are not trying
*  to make them actually optimally compressed. We are using compression as a tool to promote simplicity
*  and efficiency in our models, but they are not perfectly compressed because they need to include
*  things that are seemingly useless today, that have seemingly been useless so far. But that may
*  turn out to be useful in the future because you just don't know the future. And that's the
*  fundamental principle that intelligence arises from is that you need to be able to run appropriate
*  behavioral programs, except you have absolutely no idea what sort of context, environment,
*  situation they're going to be running in. And you have to deal with that uncertainty,
*  with that future novelty. So an analogy that you can make is with investing, for instance.
*  If I look at the past 20 years of stock market data and I use a compression algorithm to figure
*  out the best trading strategy, it's going to be, you know, if you buy Apple stock, then maybe the
*  past few years you buy Tesla stock or something. But is that strategy still going to be true for
*  the next 20 years? Well, actually, probably not. Which is why if you're a smart investor,
*  you're not just going to be following the strategy that corresponds to compression of the past.
*  You're going to have a balanced portfolio, right? Because you just don't know what's going to happen
*  in your things. I mean, I guess in that same sense, the compression is analogous to what you
*  talked about, which is like local or robust generalization versus extreme generalization.
*  It's much closer to that side of being able to generalize in the local sense.
*  That's why, you know, as humans, when we are children, in our education,
*  so a lot of it is driven by place, driven by curiosity. We are not efficiently
*  compressing things. We're actually exploring. We are retaining all kinds of
*  things from our environment that seem to be completely useless because they might
*  turn out to be eventually useful, right? And that's what cognition is really about and
*  what makes it antagonistic to compression is that it is about hedging for future uncertainty.
*  And that's antagonistic to compression. Cognition leverages compression as a tool
*  to promote efficiency, right? And so in that sense, in our models.
*  It's like Einstein said, make it simpler, but not, however that quote goes, but not too simple.
*  So you want to, compression simplifies things, but you don't want to make it too simple.
*  Yes. So a good model of the world is going to include all kinds of things that are completely
*  useless actually, just in case. Because you need diversity in the same way that in your portfolio,
*  you need all kinds of stocks that may not have performed well so far, but you need diversity.
*  And the reason you need diversity is because fundamentally you don't know what you're doing.
*  And the same is true of the human mind is that it needs to behave appropriately in a future.
*  And it has no idea what the future is going to be like. It's a bit, it's not going to be like the
*  past. So compressing the past is not appropriate because the past is not, is not productive in the
*  future. Yeah. History repeats itself, but not perfectly. I don't think I asked you last time
*  the most inappropriately absurd question. We've talked a lot about intelligence,
*  but the bigger question from intelligence is of meaning.
*  Intelligence systems are kind of goal oriented. They're always optimizing for goal.
*  If you look at the Hodder Prize actually, I mean, there's always a clean formulation of a goal.
*  But the natural question is for us humans, since we don't know our objective function
*  is what is the meaning of it all? So the absurd question is what Francois Chollet
*  do you think is the meaning of life? What's the meaning of life? Yeah, that's a big question.
*  And I think I can give you my answer, at least one of my answers. And
*  so, you know, the one thing that's very important in understanding who we are is that
*  everything that makes up, that makes up ourselves, that makes up who we are,
*  even your most personal thoughts is not actually your own. Right? Like even your most personal
*  thoughts are expressed in words that you did not invent and are built on concepts and images
*  that you did not invent. We are very much cultural beings. Right? We are made of culture.
*  We are not what makes us different from animals, for instance. Right? So we are,
*  everything about ourselves is an echo of the past, an echo of people who lived before us.
*  Right? That's who we are. And in the same way, if we manage to contribute something,
*  something to the collective edifice of culture, a new idea, maybe a beautiful piece of music,
*  a work of art, a grand theory, a new words, maybe, that something is going to become a part
*  of the minds of future humans essentially forever. So everything we do creates
*  repulse that propagates into the future. And that's in a way, this is our path to immortality,
*  is that as we contribute things to culture, culture in turn becomes future humans. And
*  we keep influencing people thousands of years from now. So our actions today create repulse. And
*  these repulse, I think, basically sum up the meaning of life. Like in the same way that we are,
*  the sum of the interactions between many different repulse that came from our past,
*  we are ourselves creating repulse that will propagate into the future. And that's why
*  we should be, this seems like perhaps an naive thing to say, but we should be kind to others
*  during our time on earth, because every act of kindness creates repulse. And in reverse,
*  every act of violence also creates repulse. And you want to carefully choose which kind of repulse
*  you want to create, and you want to propagate into the future. And in your case, first of all,
*  beautifully put, but in your case, creating repulse into the future human and future AGI systems.
*  Yes.
*  It's fascinating.
*  All six of us.
*  I don't think there's a better way to end it, Francois, as always for a second time, and I'm
*  sure many times in the future, it's been a huge honor. You're one of the most brilliant people in
*  the machine learning, computer science, science world. Again, it's a huge honor. Thanks for talking
*  today.
*  It's been a pleasure. Thanks a lot for having me. We appreciate it.
*  Thanks for listening to this conversation with Francois Chollet.
*  And thank you to our sponsors, Babel, Masterclass, and Cash App. Click the sponsor links in the
*  description to get a discount and to support this podcast. If you enjoy this thing, subscribe on
*  YouTube, review it with five stars on Apple Podcasts, follow on Spotify, support on Patreon,
*  or connect with me on Twitter at Lex Friedman.
*  And now let me leave you with some words from René Descartes in 1668, an excerpt of which Francois
*  includes and is on the Measure of Intelligence paper.
*  If there were machines which bore a resemblance to our bodies and imitated our actions as closely as
*  possible for all practical purposes, we should still have two very certain means of recognizing
*  that they were not real men. The first is that they could never use words or put together signs,
*  as we do in order to declare our thoughts to others. For we can certainly conceive of a
*  machine so constructed that it utters words and even utters words that correspond to bodily
*  actions causing a change in its organs. But it is not conceivable that such a machine should produce
*  different arrangements of words so as to give an appropriately meaningful answer to whatever is
*  said in its presence as the dullest of men can do. Here Descartes is anticipating the Turing test,
*  and the argument still continues to this day. Secondly, he continues, even though some
*  machines might do some things as well as we do them, or perhaps even better, they would
*  inevitably fail in others, which would reveal that they are acting not from understanding,
*  but only from the disposition of their organs. This is an incredible quote. For, whereas reason
*  is a universal instrument which can be used in all kinds of situations, these organs need some
*  particular action. Hence, it is for all practical purposes impossible for a machine to have enough
*  different organs to make it act in all the contingencies of life in the way in which our
*  reason makes us act. That's the debate between mimicry memorization versus understanding.
*  So, thank you for listening and hope to see you next time.
*  you
