---
Date Generated: April 12, 2024
Transcription Model: whisper medium 20231117
Length: 8692s
Video Keywords: ['afghanistan robots', 'agi', 'ai', 'ai podcast', 'artificial intelligence', 'artificial intelligence podcast', 'baxter robot', 'domo robot', 'irobot', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'mit robotics', 'rethink robotics', 'robot deployment', 'robotics', 'robust.ai', 'rodney brooks', 'sawyer robot']
Video Views: 155508
Video Rating: None
---

# Rodney Brooks: Robotics | Lex Fridman Podcast #217
**Lex Fridman:** [September 03, 2021](https://www.youtube.com/watch?v=nre0QT9LN6w)
*  The following is a conversation with Rodney Brooks,
*  one of the greatest roboticists in history.
*  He led the Computer Science
*  and Artificial Intelligence Laboratory at MIT,
*  then co-founded iRobot,
*  which is one of the most successful robotics companies ever.
*  Then he co-founded Rethink Robotics
*  that created some amazing collaborative robots
*  like Baxter and Sawyer.
*  Finally, he co-founded Robust.ai,
*  whose mission is to teach robots common sense,
*  which is a lot harder than it sounds.
*  To support this podcast,
*  please check out our sponsors in the description.
*  As a side note, let me say that Rodney
*  is someone I've looked up to for many years
*  in my now over two decade journey in robotics
*  because one, he's a legit great engineer
*  of real world systems,
*  and two, he's not afraid to state controversial opinions
*  that challenge the way we see the AI world.
*  But of course, while I agree with him
*  on some of his critical views of AI,
*  I don't agree with some others,
*  and he's fully supportive of such disagreement.
*  Nobody ever built anything great by being fully agreeable.
*  There's always respect and love behind our interactions,
*  and when a conversation is recorded
*  like it was for this podcast,
*  I think a little bit of disagreement is fun.
*  This is the Lex Friedman Podcast,
*  and here is my conversation with Rodney Brooks.
*  What is the most amazing or beautiful robot
*  that you've ever had the chance to work with?
*  I think it was Domo,
*  which was made by one of my grad students, Aaron Edsinger.
*  It now sits in Daniela Rus' office, director of CSAIL,
*  and it was just a beautiful robot,
*  and Aaron was really clever.
*  He didn't give me a budget ahead of time.
*  He didn't tell me what he was gonna do.
*  He just started spending money.
*  He spent a lot of money.
*  He and Jeff Weber, who is a mechanical engineer,
*  who Aaron insisted he bring with him
*  when he became a grad student,
*  built this beautiful, gorgeous robot, Domo,
*  which is an upper torso humanoid, two arms,
*  with three-fingered hands,
*  and face eyeballs, all, not the eyeballs,
*  but everything else, series elastic actuators.
*  You can interact with it.
*  Cable-driven, all the motors are inside,
*  and it's just gorgeous.
*  The eyeballs are actuated, too, or no?
*  Oh, yeah, the eyeballs are actuated with cameras,
*  and so it had a visual attention mechanism,
*  looking when people came in,
*  and looking at their face and talking with them.
*  Wow, was it amazing?
*  The beauty of it.
*  You said what was the most beautiful.
*  What is the most beautiful?
*  It's just mechanically gorgeous.
*  As everything Aaron builds,
*  there's always been mechanically gorgeous.
*  It's just exquisite in the detail.
*  We're talking about mechanically,
*  literally the amount of actuators.
*  The actuators, the cables.
*  He anodizes different parts, different colors,
*  and it just looks like a work of art.
*  What about the face?
*  Do you find the face beautiful in robots?
*  When you make a robot,
*  it's making a promise for how well
*  it will be able to interact.
*  I always encourage my students not to over-promise.
*  Even with its essence, the thing it presents,
*  it should not over-promise.
*  Yeah, so the joke I make, which I think you'll get,
*  is if your robot looks like Albert Einstein,
*  it should be as smart as Albert Einstein.
*  So the only thing in Domo's face is the eyeballs,
*  because that's all it can do.
*  It can look at you and pay attention.
*  So there is no, it's not like one of those
*  Japanese robots that looks exactly like a person at all.
*  But see, the thing is, us humans and dogs too,
*  don't just use eyes as attentional mechanisms.
*  They also use it to communicate.
*  It's part of the communication.
*  Like a dog can look at you, look at another thing,
*  and look back at you, and that designates
*  that we're going to be looking at that thing together.
*  Or intent, you know, on both Baxter and Sawyer
*  at Rethink Robotics.
*  They had a screen with graphic eyes,
*  so it wasn't actually where the cameras were pointing.
*  But the eyes would look in the direction
*  it was about to move its arm,
*  so people in the factory nearby
*  were not surprised by its motions,
*  because it gave that intent away.
*  Before we talk about Baxter,
*  which I think is a beautiful robot,
*  let's go back to the beginning.
*  When did you first fall in love with robotics?
*  We're talking about beauty and love
*  to open the conversation.
*  This is great.
*  I've got these, I was born in the end of 1954,
*  and I grew up in Adelaide, South Australia.
*  And I have these two books that are dated 1961.
*  So I'm guessing my mother found them in a store
*  in 62 or 63, How and Why Wonder Books.
*  How and Why Wonder Book of Electricity,
*  and How and Why Wonder Book of Giant Brains and Robots.
*  And I learned how to build circuits,
*  you know, when I was eight or nine, simple circuits.
*  And I read, you know, I learned the binary system,
*  and saw all these drawings mostly of robots.
*  And then I tried to build them
*  for the rest of my childhood.
*  Wait, 61, you said?
*  This was when the two books, I've still got them at home.
*  What does the robot mean in that context?
*  No, they were, some of the robots that they had were
*  arms, you know, big arms to move nuclear material around,
*  but they had pictures of welding robots
*  that looked like humans under the sea,
*  welding stuff underwater.
*  So they weren't real robots,
*  but they were, you know, what people were thinking about
*  for robots.
*  What were you thinking about?
*  Were you thinking about humanoids?
*  Were you thinking about arms with fingers?
*  Were you thinking about faces or cars?
*  No, actually, to be honest, I realized my limitation
*  on building mechanical stuff.
*  So I just built the brains mostly,
*  out of different technologies as I got older.
*  I built a learning system, which was chemical-based,
*  and I had this ice cube tray, each well was a cell,
*  and by applying voltage to the two electrodes,
*  it would build up a copper bridge.
*  So over time, it would learn a simple network
*  so I could teach it stuff.
*  And that was, mostly things were driven by my budget,
*  and nails as electrodes and an ice cube tray
*  was about my budget at that stage.
*  Later, I managed to buy transistors,
*  and then I could build gates and flip-flops and stuff.
*  So one of your first robots was an ice cube tray?
*  Yeah.
*  And it was very cerebral, because it learned to add.
*  Very nice.
*  Well, just a decade or so before, in 1950,
*  Alan Turing wrote a paper that formulated the Turing test,
*  and he opened that paper with the question,
*  can machines think?
*  So let me ask you this question.
*  Can machines think?
*  Can your ice cube tray one day think?
*  Certainly machines can think,
*  because I believe you're a machine, and I'm a machine,
*  and I believe we both think.
*  I think any other philosophical position
*  is sort of a little ludicrous, what does think mean
*  if it's not something that we do, and we are machines.
*  So yes, machines can, but do we have a clue
*  how to build such machines?
*  That's a very different question.
*  Are we capable of building such machines?
*  Are we smart enough?
*  We think we're smart enough to do anything,
*  but maybe we're not.
*  Maybe we're just not smart enough to build stuff like us.
*  The kind of computer that Alan Turing was thinking about,
*  do you think there is something fundamentally
*  or significantly different between the computer
*  between our ears, the biological computer that humans use,
*  and the computer that he was thinking about
*  from a sort of high level philosophical?
*  Yeah, I believe that it's very wrong.
*  In fact, I'm halfway through a,
*  I think it'll be about a 480 page book,
*  titled, the working title is Not Even Wrong.
*  And if I may, I'll tell you a bit about that book.
*  So there's two, well, three thrusts to it.
*  One is the history of computation,
*  what we call computation.
*  Goes all the way back to some manuscripts in Latin
*  from 1614 and 1620 by Napier and Kepler
*  through Babbage and Lovelace.
*  And then Turing's 1936 paper is what we think of
*  as the invention of modern computation.
*  And that paper, by the way, did not set out to,
*  you know, invent computation.
*  It set out to negatively answer one of Hilbert's
*  three later set of problems.
*  He called it an effective way of getting answers.
*  And Hilbert really worked with rewriting rules,
*  as did Church, who also at the same time,
*  a month earlier than Turing, disproved Hilbert's,
*  one of these three hypotheses.
*  The other two had already been disproved by Gödel.
*  So Turing set out to disprove it,
*  because it's always easier to disprove these things
*  than to prove that there is an answer.
*  And so he needed, and it really came from his professor,
*  while I was an undergrad at Cambridge,
*  who turned it into, is there a mechanical process?
*  So he wanted to show a mechanical process
*  that could calculate numbers,
*  because that was a mechanical process
*  that people used to generate tables.
*  They were called computers, the people at the time.
*  And they followed a set of rules where they had paper,
*  and they would write numbers down,
*  and based on the numbers, they'd keep writing other numbers.
*  And they would produce numbers for these tables,
*  engineering tables,
*  that the more iterations they did,
*  the more significant digits came out.
*  And so Turing, in that paper,
*  set out to define what sort of machine
*  could do that mechanical machine,
*  where it could produce an arbitrary number of digits
*  in the same way a human computer did.
*  And he came up with a very simple set of constraints,
*  where there was an infinite supply of paper,
*  this is the tape of the Turing machine,
*  and each Turing machine had a set of,
*  came with a set of instructions
*  that as a person could do with pencil and paper,
*  write down things on the tape,
*  and erase them and put new things there.
*  And he was able to show that that system
*  was not able to do something that Hilbert had hypothesized.
*  So he disproved it.
*  But he had to show that this system was good enough
*  to do whatever could be done,
*  but couldn't do this other thing.
*  And there he said, and he says in the paper,
*  I don't have any real arguments for this,
*  but based on intuition.
*  So that's how he defined computation.
*  And then if you look over the next,
*  from 1936 up until really around 1975,
*  you see people struggling with,
*  is this really what computation is?
*  And so Marvin Minsky, very well known in AI,
*  but also a fantastic mathematician in his book,
*  Finite and Infinite Machines from the mid-60s,
*  which is a beautiful, beautiful mathematical book,
*  says at the start of the book, well, what is computation?
*  Turing says it's this, and yeah, I sort of think it's that.
*  It doesn't really matter whether the stuff's made of wood
*  or plastic, it's just, you know,
*  that relatively cheap stuff can do this stuff.
*  And so, yeah, it seems like computation.
*  And Donald Knuth in his first volume of his,
*  you know, Art of Computer Programming in around 1968,
*  says, well, what's computation?
*  It's this stuff like Turing says
*  that a person could do each step without too much trouble.
*  And so one of his examples
*  of what would be too much trouble was a step
*  which required knowing whether Fermat's Last Theorem
*  was true or not because it was not known at the time.
*  And that's too much trouble for a person to do as a step.
*  And Hopcroft and Ullman sort of said a similar thing
*  later that year, and by 1975,
*  in the A.H. Hopcroft and Ullman book, they're saying,
*  well, you know, we don't really know what computation is,
*  but intuition says this is sort of about right,
*  and this is what it is.
*  That's computation.
*  It's a sort of agreed upon thing
*  which happens to be really easy to implement in silicon.
*  And then we had Moore's Law, which took off,
*  and it's been an incredibly powerful tool.
*  I certainly wouldn't argue with that.
*  The version we have of computation, incredibly powerful.
*  Can we just take a pause?
*  So what we're talking about is there's an infinite tape
*  with some simple rules of how to write on that tape,
*  and that's what we're kind of thinking about.
*  This is computation.
*  Yeah, and it's modeled after humans,
*  how humans do stuff.
*  I think it's, Turing says in the 36th paper,
*  one of the critical facts here is that a human
*  has a limited amount of memory.
*  So that's what we're gonna put
*  onto our mechanical computers.
*  So, eh, eh, eh.
*  So, you know, unlike mass or charge or, you know.
*  It's not given by the universe.
*  It was, this is what we're gonna call computation.
*  And then it has this really, you know,
*  it had this really good implementation,
*  which has completely changed our technological world.
*  That's computation.
*  Second part of the book, or argument in the book,
*  I have this two by two matrix with science in the top row,
*  engineering in the bottom row, left column is intelligence,
*  right column is life.
*  So in the bottom row, the engineering,
*  there's artificial intelligence and there's artificial life.
*  In the top row, there's neuroscience and abiogenesis.
*  How does living matter turn in,
*  how does non-living matter become living matter?
*  Four disciplines.
*  These four disciplines all came into the current form
*  in the period 1945 to 1965.
*  That's interesting.
*  There was neuroscience before,
*  but it wasn't effective neuroscience.
*  It was, you know, there were these ganglia
*  and there's electrical charges,
*  but no one knows what to do with it.
*  And furthermore, there were a lot of players
*  who are common across them.
*  I've identified common players
*  except for artificial intelligence and abiogenesis.
*  I don't have, but for any other pair,
*  I can point to people who work them.
*  And a whole bunch of them, by the way,
*  were at the research lab for electronics at MIT,
*  where Warren McCulloch held forth.
*  And in fact, McCulloch, Pitts, Letvin, and Macerana
*  wrote the first paper on functional neuroscience
*  called What the Frog's Eye Tells the Frog's Brain,
*  where instead of it just being this bunch of nerves,
*  they sort of showed what different anatomical components
*  were doing and telling other anatomical components
*  and, you know, generating behavior in the frog.
*  Would you put them as basically the fathers
*  or one of the early pioneers
*  of what are now called artificial neural networks?
*  Yeah, I mean, McCulloch and Pitts,
*  Pitts was much younger than him, in 1943,
*  had written a paper inspired by Bertrand Russell
*  on a calculus for the ideas eminent in neural systems,
*  where they had tried to, without any real proof,
*  they had tried to give a formalism for neurons,
*  basically in terms of logic,
*  and gates, or gates, and not gates,
*  with no real evidence that that was what was going on,
*  but they talked about it.
*  And that was picked up by Minsky for his 1953 dissertation
*  on, which was a neural network, we would call it today.
*  It was picked up by John von Neumann
*  when he was designing the Edback computer in 1945.
*  He talked about its components being neurons based on,
*  and in references, he's only got three references,
*  and one of them is the McCulloch-Pitts paper.
*  So all these people, and then the AI people,
*  and the artificial life people,
*  which was John von Neumann originally,
*  as like overlap between all of them.
*  They're all going around at the same time.
*  And three of these four disciplines turned to computation
*  as their primary metaphor.
*  So I've got a couple of chapters in the book.
*  One is titled, wait, computers are people?
*  Because that's where our computers came from,
*  from people who were computing stuff.
*  And then I have another chapter, wait, people are computers?
*  Which is about computational neuroscience.
*  So there's this whole circle here.
*  That computation is it.
*  And I have talked to people about,
*  well, maybe it's not computation that goes on in the head.
*  Of course it is.
*  Okay, well, when Elon Musk's rocket goes up,
*  is it computing?
*  Is that how it gets into orbit?
*  By computing?
*  But we've got this idea, if you wanna build an AI system,
*  you write a computer program.
*  Yeah, so the word computation
*  very quickly starts doing a lot of work
*  that it was not initially intended to do.
*  Is that gonna say if you talk about the universe
*  as essentially performing a computation?
*  Yeah, right, Wolfram does this.
*  He turns it into computation.
*  You don't turn rockets into computation.
*  By the way, when you say computation in our conversation,
*  do you tend to think of computation narrowly
*  in the way Turing thought of computation?
*  It's gotten very squishy at the time.
*  But computation in the way Turing thinks about it
*  and the way most people think about it
*  actually fits very well with thinking like a hunter-gatherer.
*  There are places and there can be stuff in places
*  and the stuff in places can change
*  and it stays there until someone changes it.
*  And it's this metaphor of place and container,
*  which is a combination of the two.
*  Which is a combination of our place cells
*  in our hippocampus and our cortex.
*  But this is how we use metaphors mostly to think about.
*  And when we get outside of our metaphor range,
*  we have to invent tools which we can sort of
*  switch on to use.
*  So calculus is an example of a tool.
*  It can do stuff that our raw reasoning can't do
*  and we've got conventions of when you can use it or not.
*  But sometimes people try to, all the time,
*  we always try to get physical metaphors for things,
*  which is why quantum mechanics has been such a problem
*  for a hundred years.
*  Because it's a particle, no, it's a wave.
*  It's gotta be something we understand.
*  And I say, no, it's some weird mathematical logic
*  that's different from those, but we want that metaphor.
*  Well, I suspect that a hundred years or 200 years from now,
*  neither quantum mechanics nor dark matter
*  will be talked about in the same terms.
*  In the same way that Floggerton's theory
*  eventually went away,
*  because it just wasn't an adequate explanatory metaphor.
*  That metaphor was the stuff,
*  there is stuff in the burning,
*  the burning is in the matter.
*  Whereas it turns out the burning was outside the matter,
*  it was the oxygen.
*  So our desire for metaphor
*  and combined with our limited cognitive capabilities
*  gets us into trouble.
*  That's my argument in this book.
*  Now, and people say, well, what is it then?
*  And I say, well, I wish I knew that,
*  I tried to look about that, but I give some ideas.
*  But so there's the three things.
*  Computation is sort of a particular thing we use.
*  Oh, can I tell you one beautiful thing?
*  One beautiful thing I've found?
*  So I used an example of a thing
*  that's different from computation.
*  You hit a drum and it vibrates.
*  And there are some stationary points on the drum surface,
*  because the waves are going up and down
*  with stationary points.
*  Now, you could compute them to arbitrary precision,
*  but the drum just knows them.
*  The drum doesn't have to compute.
*  What was the very first computer program
*  ever written by Ada Lovelace?
*  To compute Bernoulli numbers.
*  And Bernoulli numbers are exactly what you need
*  to find those stable points in the drum surface.
*  Wow.
*  Anyway, and there was a bug in the program.
*  The arguments to divide were reversed in one place.
*  And it still worked.
*  Well, she never got to run it.
*  They never built the analytical engine.
*  She wrote the program without it.
*  So computation.
*  Computation is sort of a thing
*  that's become dominant as a metaphor,
*  but is it the right metaphor?
*  All three of these four fields adopted computation
*  and a lot of it swirls around Warren McCulloch
*  and all his students, and he funded a lot of people.
*  And our human metaphors,
*  our limitations to human thinking will play into this.
*  Those are the three themes of the book.
*  So I have a little to say about computation.
*  So you're saying that there is a gap between the computer
*  or the machine that performs computation
*  and this machine that appears to have consciousness
*  and intelligence.
*  Yeah.
*  Can we-
*  That piece of meat in your head.
*  Piece of meat.
*  And maybe it's not just the meat in your head.
*  It's the rest of you too.
*  I mean, you actually have a neural system in your gut.
*  I tend to also believe, not believe,
*  but we're now dancing around things we don't know.
*  But I tend to believe other humans are important.
*  So we're almost like,
*  I just don't think we would ever have achieved
*  the level of intelligence we have with other humans.
*  I'm not saying so confidently,
*  but I have an intuition that some of the intelligence
*  is in the interaction.
*  Yeah, and I think it seems to me very likely,
*  again, this is speculation,
*  but we, our species and probably Neanderthals to some extent
*  because you can find old bones
*  where they seem to be counting on them by putting notches
*  that were in Neanderthals.
*  We are able to put some of our stuff outside our body
*  into the world and then other people can share it.
*  And then we get these tools that become shared tools.
*  And so there's a whole coupling that would not occur in,
*  you know, the single deep learning network,
*  which was fed in a whole of literature or something.
*  Yeah, the neural network can't step outside of itself,
*  but is there some,
*  can we explore this dark room a little bit
*  and try to get at something?
*  What is the magic?
*  Where does the magic come from in the human brain
*  that creates the mind?
*  What's your sense?
*  As scientists that try to understand it
*  and try to build it,
*  what are the directions that if followed might be productive?
*  Is it creative interactive robots?
*  Is it creating large deep neural networks
*  that do like self-supervised learning?
*  And just like, we'll discover that
*  when you make something large enough,
*  some interesting things will emerge.
*  Is it through physics and chemistry and biology,
*  like artificial life angle,
*  like we'll sneak up in this four quadrant matrix
*  that you mentioned, is there anything you're most,
*  if you had to bet all your money, financial advice.
*  I wouldn't.
*  Okay.
*  So every intelligence we know,
*  I mean, animal intelligence, dog intelligence,
*  octopus intelligence,
*  which is a very different sort of architecture from us.
*  All the intelligences we know,
*  perceive the world in some way
*  and then have action in the world,
*  but they're able to perceive objects
*  in a way which is actually pretty damn phenomenal
*  and surprising.
*  We tend to think that the box over here between us,
*  which is a sound box, I think, is a blue box.
*  But blueness is something that we construct
*  with color constancy.
*  It's not a, it's not a, it's not,
*  the blueness is not a direct function
*  of the photons we're receiving.
*  It's actually context, you know, which is why
*  you can turn, you know, you may be seeing the examples
*  where someone turns a stop sign
*  into a, some other sort of sign
*  by just putting a couple of marks on them
*  and the deep learning system gets it wrong.
*  And everyone says, but the stop sign's red.
*  You know, why is it,
*  why is it thinking it's the other sort of sign?
*  Because redness is not intrinsic in just the photons.
*  It's actually a construction of an understanding
*  of the whole world and the relationship between objects
*  to get color constancy.
*  But our tendency in order that we get an archive paper
*  really quickly is you just show a lot of data
*  and give the labels and hope it figures it out.
*  But it's not figuring it out in the same way we do.
*  We have a very complex perceptual understanding
*  of the world.
*  Dogs have a very different perceptual understanding
*  based on smell.
*  They go smell a post, they can tell how many,
*  you know, different dogs have visited in the last 10 hours
*  and how long ago.
*  There's all sorts of stuff that we just don't perceive
*  about the world.
*  And just taking a single snapshot
*  is not perceiving about the world.
*  It's not perceiving the registration
*  between us and the object.
*  And registration is a philosophical concept.
*  Brian Cantwell-Smith talks about it a lot.
*  Very difficult squirmy thing to understand.
*  But I think none of our systems do that.
*  We've always talked in AI about the symbol grounding problem,
*  how our symbols that we talk about are grounded in the world.
*  And when deep learning came along
*  and started labeling images,
*  people said, ah, the grounding problem has been solved.
*  No, the labeling problem was solved
*  with some percentage accuracy,
*  which is different from the grounding problem.
*  So you agree with Hans Marvac
*  and what's called the Marvac's paradox
*  that highlights this counterintuitive notion
*  that reasoning is easy,
*  but perception and mobility are hard.
*  Yeah, we shared an office when I was working
*  on computer vision and he was working
*  on his first mobile robot.
*  What were those conversations like?
*  They were great.
*  So do you still kind of, maybe you can elaborate
*  and do you still believe this kind of notion
*  that perception is really hard?
*  And like, can you make sense of why we humans
*  have this poor intuition about what's hard and not?
*  Well, let me give us sort of another story.
*  Sure.
*  If you go back to the original teams working on AI,
*  from the late 50s into the 60s,
*  you know, and you go to the AI lab at MIT,
*  who was it that was doing that?
*  Was it a bunch of really smart kids who got into MIT
*  and they were intelligent.
*  So what's intelligence about?
*  Well, the stuff they were good at,
*  playing chess, doing integrals, that was hard stuff.
*  But you know, a baby could see stuff.
*  That wasn't intelligent.
*  Anyone could do that.
*  That's not intelligence.
*  And so, you know, there was this intuition
*  that the hard stuff is the things they were good at
*  and the easy stuff was the stuff that everyone could do.
*  Yeah.
*  And maybe I'm overplaying it a little bit,
*  but I think there's an element of that.
*  Yeah, I mean, I don't know how much truth there is to,
*  like chess, for example, was for the longest time
*  seen as the highest level of intellect, right?
*  Until we got computers that were better at it than people.
*  And then we realized, you know,
*  but if you go back to the 90s,
*  you'll see the stories in the press around
*  when Kasparov was beaten by Deep Blue.
*  Oh, this is the end of all sorts of things.
*  Computers are gonna be able to do anything from now on.
*  And we saw exactly the same stories with AlphaZero,
*  the go playing program.
*  Yeah, but still to me, reasoning is a special thing.
*  And perhaps-
*  Actually, we're really bad at reasoning.
*  We just use these analogies
*  based on our hunt-and-gather intuitions.
*  But why is that not,
*  don't you think the ability to construct metaphor
*  is a really powerful thing?
*  Oh yeah, it is.
*  Like tell stories.
*  It is.
*  It's the constructing the metaphor and registering that,
*  something constant in our brains.
*  Like isn't that what we're doing with vision too?
*  And we're telling our stories,
*  we're constructing good models of the world.
*  Yeah, yeah.
*  But I think we jumped between what we're capable of
*  and how we're doing it right there.
*  There was a little confusion that went on
*  as we were telling each other stories.
*  Yes, exactly.
*  Trying to delude each other.
*  No, I just think I'm not exactly,
*  so I'm trying to pull apart this Marvac's paradox.
*  I don't view it as a paradox.
*  What did evolution spend its time on?
*  It spent its time on getting us to perceive
*  and move in the world.
*  That was 600 million years
*  as multi-cell creatures doing that.
*  And then it was relatively recent
*  that we were able to hunt or gather,
*  even animals hunting.
*  That's much more recent.
*  And then anything that we,
*  speech, language, those things are
*  just a couple of hundred thousand years probably,
*  if that long.
*  And then agriculture, 10,000 years.
*  All that stuff was built on top of those earlier things,
*  which took a long time to develop.
*  So if you then look at the engineering of these things,
*  so building it into robots,
*  what's the hardest part of robotics, do you think?
*  As the decades that you worked on robots,
*  in the context of what we're talking about,
*  perception, the actual sort of the biomechanics of movement.
*  I'm kind of drawing parallels here
*  between humans and machines always.
*  Like what do you think is the hardest part of robotics?
*  I sort of think all of them.
*  There are no easy parts to do well.
*  We sort of go reductionist and we reduce it.
*  If only we had all the location of all the points in 3D,
*  things would be great.
*  If only we had labels on the images,
*  things would be great.
*  But as we see, that's not good enough.
*  Some deeper understanding.
*  But if I came to you and I could solve
*  one category of problems in robotics instantly,
*  what would give you the greatest pleasure?
*  I mean, you look at robots that manipulate objects.
*  What's hard about that?
*  Is it the perception?
*  Is it the reasoning about the world,
*  like common sense reasoning?
*  Is it the actual building of robot
*  that's able to interact with the world?
*  Is it like human aspects of a robot
*  that's interacting with human beings?
*  Is it like human aspects of a robot
*  that's interacting with humans
*  and that game theory of how they work well together?
*  Let's talk about manipulation for a second
*  because I had this really blinding moment.
*  I'm a grandfather, so grandfathers have blinding moments.
*  Just three or four miles from here,
*  last year, my 16-month-old grandson was in his new house
*  for the first time, right?
*  First time in this house.
*  He'd never been able to get to a window before,
*  but this had some low windows.
*  He goes up to this window with a handle on it
*  that he's never seen before.
*  He's got one hand pushing the window
*  and the other hand turning the handle to open the window.
*  He knew two different hands,
*  two different things he knew how to put together.
*  And he's 16 months old.
*  There you are watching in awe.
*  In an environment he'd never seen before,
*  a mechanism he'd never seen.
*  How did he do that?
*  Yes, that's a good question.
*  How did he do that?
*  That's why.
*  It's like, okay, you could see the leap of genius
*  from using one hand to perform a task to combining,
*  first of all, in manipulation, that's really difficult.
*  There's two hands, both necessary to complete the action.
*  Completely different,
*  and he'd never seen a window open before.
*  Huh.
*  But he inferred somehow a handle opened something.
*  Yeah.
*  There may have been a lot of
*  slightly different failure cases that you didn't see.
*  Not with a window, but with other objects
*  of turning and twisting and handles.
*  Well, there's a great counter to reinforcement learning.
*  We'll just give the robot,
*  or you'll give the robot plenty of time to try everything.
*  Yes.
*  Actually, can I tell a little side story here?
*  So I'm in DeepMind in London,
*  this is three, four years ago,
*  where there's a big Google building,
*  and then you go inside,
*  and then you go through this more security,
*  and then you get to DeepMind,
*  where the other Google employees can't go.
*  And I'm in a conference room,
*  a bare conference room with some of the people,
*  and they tell me about their reinforcement learning
*  experiment with robots,
*  which are just trying stuff out.
*  And they're my robots, they're Sawyer's, we sold them.
*  And they really like them because Sawyer's are compliant
*  and can sense forces, so they don't break
*  when they're bashing into walls,
*  they stop and they do all this stuff.
*  And so you just let the robot do stuff,
*  and eventually it figures stuff out.
*  By the way, Sawyer, we're talking about robot manipulation,
*  so robot arms and so on.
*  Yeah, Sawyer's a robot arm.
*  Just, what's Sawyer?
*  Sawyer's a robot arm that my company,
*  Rethink Robotics built.
*  Thank you for the context.
*  Sorry.
*  Okay, cool, so we're in DeepMind.
*  And it's in the next room,
*  these robots are just bashing around
*  to try and use reinforcement learning to learn how to act.
*  And can I go see them?
*  Oh no, they're secret.
*  They're all my robots that were secret.
*  That's hilarious, okay.
*  Anyway, the point is,
*  this idea that you just let reinforcement learning
*  figure everything out is so counter
*  to how a kid does stuff.
*  So again, story about my grandson,
*  I gave him this box that had lots
*  of different lock mechanisms.
*  He didn't randomly, and he was 18 months old,
*  he didn't randomly try to touch every surface
*  or push everything.
*  He found, he could see where the mechanism was,
*  and he started exploring the mechanism
*  for each of these different lock mechanisms.
*  And there was reinforcement, no doubt,
*  of some sort going on there.
*  But he applied a pre-filter,
*  which cut down the search space dramatically.
*  I wonder to what level we're able to introspect
*  what's going on.
*  Because what's also possible is you have something
*  like reinforcement learning going on in the mind
*  in the space of imagination.
*  So like you have a good model of the world
*  you're predicting, and you may be running those
*  tens of thousands of loops,
*  but as a human, you're just looking at yourself
*  trying to tell a story of what happened.
*  And it might seem simple, but maybe there's a lot
*  of computation going on.
*  Whatever it is, but there's also a mechanism
*  that's being built up.
*  It's not just random search.
*  That mechanism prunes it dramatically.
*  Yeah, that pruning step.
*  It doesn't, it's possible that that's,
*  so you don't think that's akin to a neural network
*  inside a reinforcement learning algorithm.
*  Is it possible?
*  It's, yeah, until it's possible.
*  But I, you know, I'll be incredibly surprised
*  if that happens.
*  I'll also be incredibly surprised that, you know,
*  after all the decades that I've been doing this,
*  where every few years someone thinks,
*  now we've got it, now we've got it.
*  You know, four or five years ago I was saying,
*  I don't think we've got it yet.
*  And everyone was saying,
*  oh, you don't understand how powerful AI is.
*  I had people tell me,
*  you don't understand how powerful it is.
*  You know, I sort of had a track record
*  of what the world had done to think,
*  well, this is no different from before.
*  Oh, we have bigger computers.
*  We had bigger computers in the 90s
*  and we could do more stuff.
*  But, okay, so let me push back.
*  I'm generally sort of optimistic
*  and try to find the beauty in things.
*  I think there's a lot of surprising and beautiful things
*  that neural networks, this new generation
*  of deep learning revolution has revealed to me
*  is continually been very surprising
*  the kind of things it's able to do.
*  Now, generalizing that over saying like this,
*  we've solved intelligence, that's another big leap.
*  But is there something surprising and beautiful
*  to you about neural networks
*  that where actually you said back and said,
*  I did not expect this?
*  Oh, I think their performance,
*  their performance on ImageNet was shocking.
*  So computer vision, those early days was just very like,
*  wow, okay.
*  That doesn't mean that they're solving everything
*  in computer vision we need to solve
*  in vision for robots.
*  What about AlphaZero and self-play mechanisms
*  and reinforcement learning?
*  Isn't that?
*  Yeah, that was all in Donald Mickey's 1961 paper.
*  Everything there was there,
*  which introduced reinforcement learning.
*  No, but come on.
*  So, no, you're talking about the actual techniques,
*  but isn't it surprising to you
*  the level it's able to achieve
*  with no human supervision of chess play?
*  Like, to me, there's a big, big difference in deep blue.
*  Maybe what that's saying
*  is how overblown our view of ourselves is.
*  That chess is easy.
*  Yeah, I mean, I came across this 1946 report that,
*  and I'd seen this as a kid in one of those books
*  that my mother had given me, actually.
*  1946 report, which pitted someone with an abacus
*  against an electronic calculator,
*  and he beat the electronic calculator.
*  So there, at that point was,
*  well, humans are still better than machines at calculating.
*  Are you surprised today that a machine can
*  do a billion floating point operations a second,
*  and you're puzzling for minutes through one?
*  So, you know.
*  I am, I mean, I don't know, but I am certainly surprised.
*  There's something, to me, different about learning.
*  So a system that's able to learn.
*  Learning, now, see, now you're getting
*  into one of the deadly sins.
*  Because of using terms overly broadly.
*  Yeah, I mean, there's so many different forms of learning.
*  Yeah.
*  There's so many different forms.
*  You know, I learned my way around the city.
*  I learned to play chess.
*  I learned Latin.
*  I learned to ride a bicycle.
*  All of those are very different capabilities.
*  And if someone has a,
*  in the old days, people would write a paper
*  about learning something.
*  Now, the corporate press office puts out a press release
*  about how Company X has,
*  has leading the world because they have a system that can.
*  Yeah, but here's the thing.
*  Okay, so what is learning?
*  When I refer to learning, there's many things.
*  But I-
*  It's a suitcase word.
*  It's a suitcase word, but loosely, there's a dumb system.
*  And over time, it becomes smart.
*  Well, it becomes less dumb at the thing that it's doing.
*  Yeah.
*  Smart is a loaded word.
*  Yes, less dumb at the thing it's doing.
*  And it gets better performance under some measure,
*  under some set of conditions at that thing.
*  And most of these learning algorithms,
*  learning systems, fail when you change the conditions
*  just a little bit in a way that humans don't.
*  So I was at DeepMind.
*  The AlphaGo had just come out.
*  And I said, what would have happened if you'd given it
*  a 21 by 21 board instead of a 19 by 19 board?
*  But a human player would actually, you know,
*  well, would actually be able to play a game.
*  And actually, funny enough, if you look at DeepMind's work
*  since then, they are presenting a lot of algorithms
*  that would do well at the bigger board.
*  So they're slowly expanding this generalization.
*  I mean, to me, there's a core element there.
*  It is very surprising to me that even in a constrained
*  game of chess or go, that through self play
*  by a system playing itself,
*  that it can achieve superhuman level performance
*  through learning alone.
*  So like-
*  Okay, so you know, you-
*  It's so fundamentally different in search of that.
*  You didn't like it when I referred to
*  Donald Mickey's 1961 paper.
*  There, in the second part of it, which came a year later,
*  they had self play on an electronic computer
*  at Tic Tac Toe, okay, it's not us,
*  but it learned to play Tic Tac Toe through self play.
*  That's not-
*  And it learned to play optimally.
*  What I'm saying is, I, okay, I have a little bit of a bias,
*  but I find ideas beautiful, but only when they actually
*  realize the promise, that's another level of beauty.
*  Like, for example, what Bezos and Elon Musk
*  are doing with rockets, we had rockets for a long time,
*  but doing reusable cheap rockets is very impressive.
*  In the same way, I, okay.
*  Yeah.
*  I would have not predicted, first of all,
*  when I was, started and fell in love with AI,
*  the game of Go was seen to be impossible to solve.
*  Okay, so I thought maybe, you know, I,
*  maybe it'd be possible to maybe have big leaps
*  in a Moore's law style of way,
*  in computation it'll be able to solve it.
*  But I would never have guessed that you could learn
*  your way, however, I mean, in the narrow sense of learning,
*  learn your way to beat the best people in the world
*  at the game of Go, without human supervision,
*  not studying the game of experts.
*  Okay, so-
*  That's surprising.
*  Using a different learning technique.
*  Yes.
*  Arthur Samuel, in the early 60s,
*  and he was the first person to use machine learning,
*  got, had a program that could beat
*  the world champion at checkers.
*  Now. Yes.
*  So, and that at the time was considered amazing.
*  By the way, Arthur Samuel had some fantastic advantages.
*  Do you want to hear Arthur Samuel's advantages?
*  Two things.
*  One, he was at the 1956 AI conference.
*  I knew Arthur later in life.
*  He was at Stanford when I was a grad student there.
*  He wore a tie and a jacket every day,
*  the rest of us didn't.
*  He's a delightful man, delightful man.
*  It turns out Claude Shannon,
*  in a 1950 Scientific American article,
*  outlined on chess playing,
*  outlined the learning mechanism that Arthur Samuel used,
*  and they had met in 1956.
*  I assume there was some communication,
*  but I don't know that for sure.
*  But Arthur Samuel had been a vacuum tube engineer,
*  on getting reliability of vacuum tubes,
*  and then had overseen
*  the first transistorized computers at IBM.
*  And in those days, before you shipped a computer,
*  you ran it for a week to seek to get early failures.
*  So he had this whole farm of computers running random code
*  for hours and hours,
*  a week for each computer, he had a whole bunch of them.
*  So he ran his chess learning program with self play
*  on IBM's production line.
*  He had more computation available to him
*  than anyone else in the world.
*  And then he was able to produce a chess playing program,
*  I mean, a checkers playing program
*  that could beat the world champion.
*  So that's amazing.
*  The question is, what I mean, surprise,
*  I don't just mean it's nice to have that accomplishment,
*  is there is a stepping towards something that feels
*  more intelligent than before?
*  And the question is-
*  That's in your view of the world.
*  Okay, well, let me then, doesn't mean I'm wrong.
*  No, no, it doesn't.
*  So the question is, if we keep taking steps like that,
*  how far that takes us?
*  Are we going to build a better recommender systems?
*  Are we going to build a better robot?
*  Or will we solve intelligence?
*  So, you know, I'm putting my bet on,
*  we're still missing a whole lot, a lot.
*  And why would I say that?
*  Well, in these games, they're all, you know,
*  100% information games.
*  But again, but each of these systems
*  is a very short description of the current state,
*  which is different from registering
*  and perception in the world.
*  Which gets back to Marovick's paradox.
*  I'm definitely not saying that
*  chess is somehow harder than perception
*  or any kind of even any kind of robotics
*  in the physical world, I definitely think is way harder
*  than the game of chess.
*  So I was always much more impressed by
*  like the workings of the human mind is incredible.
*  The human mind is incredible.
*  I believe that from the very beginning,
*  I wanted to be a psychiatrist for the longest time.
*  I always thought that's way more incredible
*  in the game of chess.
*  I think the game of chess is, I love the Olympics.
*  It's just another example of us humans picking a task
*  and then agreeing that a million humans
*  will dedicate their whole life to that task.
*  And that's the cool thing that the human mind
*  is able to focus on one task
*  and then compete against each other
*  and achieve like weirdly incredible levels of performance.
*  That's the aspect of chess that's super cool.
*  Not that chess in itself is really difficult.
*  It's like the Fermat's Last Theorem is not in itself
*  to me that interesting.
*  The fact that thousands of people have been struggling
*  to solve that particular problem is fascinating.
*  So can I tell you my disease in this way?
*  Sure.
*  Which actually is closer to what you're saying.
*  So as a child, I was building various,
*  I called them computers, they weren't general purpose
*  computers. Ice cube tray.
*  The ice cube tray was one.
*  But I built other machines and one I liked to build
*  was machines that could beat adults at a game.
*  And they couldn't, the adults couldn't beat my machine.
*  Yes.
*  So you were like, that's powerful.
*  Like that's a way to rebel.
*  Yeah.
*  By the way, when was the first time you built something
*  that outperformed you?
*  Do you remember?
*  Well, I knew how it worked.
*  I was probably nine years old and I built a thing
*  that was a game where you take turns
*  in taking matches from a pile.
*  And either the one who takes the last one
*  or the one who doesn't take the last one wins, I forget.
*  And so it was pretty easy to build that out of wires
*  and nails and little coils that were like plugging
*  in the number and a few light bulbs.
*  The one that I was proud of, I was 12 when I built
*  a thing out of old telephone switchboard switches
*  that could always win at tic-tac-toe.
*  And that was a much harder circuit to design.
*  But again, it was just, it was no active components.
*  It was just three position switches, empty X, zero,
*  and nine of them and a light bulb on which move it wanted next.
*  And then the human would go and move that.
*  See, there's magic in that creation.
*  There was, yeah.
*  I tend to see magic in robots that,
*  like I also think that intelligence
*  is a little bit overrated.
*  I think we can have deep connections
*  with robots very soon.
*  And we'll come back to connections with robots.
*  Sure.
*  But I do wanna say, I think too many people
*  make the mistake of seeing that magic
*  and thinking, well, we'll just continue.
*  But each one of those is a hard fought battle
*  for the next step, the next step.
*  Yes, the open question here is,
*  and this is why I'm playing devil's advocate,
*  but I often do when I read your blog post in my mind
*  because I have like this eternal optimism
*  is it's not clear to me.
*  So I don't do what obviously the journalists do
*  or like give into the hype,
*  but it's not obvious to me how many steps away we are
*  from a truly transformational understanding
*  of what it means to build intelligence systems
*  or how to build intelligence systems.
*  I'm also aware of the whole history
*  of artificial intelligence,
*  which is where your deep grounding of this is,
*  is there's been an optimism for decades.
*  And that optimism, just like reading old optimism
*  is absurd because people were like,
*  this is, they were saying things are trivial
*  for decades since the 60s.
*  They were saying everything is true.
*  Computer vision is trivial.
*  But I think my mind is working crisply enough to where,
*  I mean, we can dig into if you want.
*  I'm really surprised by the things DeepMind has done.
*  I don't think they're yet close to solving intelligence,
*  but I'm not sure it's not 10 years away.
*  What I'm referring to is interesting to see
*  when the engineering, it takes that idea to scale
*  and the idea works.
*  And no, it fools people.
*  Okay, honestly, Rodney, if it was you, me, and Demis
*  inside a room, forget the press, forget all those things,
*  just as a scientist, as a roboticist,
*  that wasn't surprising to you that at scale,
*  so we're talking about very large now,
*  okay, let's pick one that's the most surprising to you.
*  Please don't yell at me.
*  GPT-3, okay, hold on a second.
*  Hold on a second.
*  I was gonna bring that up.
*  Okay, thank you.
*  Alpha zero, alpha go, alpha go zero, alpha zero,
*  and then alpha fold one and two.
*  So are any of these kind of have this core
*  of, forget usefulness or application and so on,
*  which you could argue for alpha fold,
*  like as a scientist, was doors surprising to you
*  that it worked as well as it did?
*  Okay, so if we're gonna make the distinction
*  between surprise and usefulness,
*  and I have to explain this.
*  I would say alpha fold.
*  And one of the problems at the moment with alpha fold
*  is it gets a lot of them right,
*  which is a surprise to me
*  because they're a really complex thing.
*  But you don't know which ones it gets right,
*  which then is a bit of a problem.
*  Now they've come out with a reason.
*  You mean the structure of the protein
*  it gets a lot of those right?
*  Yeah, it's a surprising number of them right.
*  Yeah.
*  It's been a really hard problem.
*  So that was a surprise how many it gets right.
*  So far the usefulness is limited
*  because you don't know which ones are right or not.
*  And now they've come out with a thing
*  in the last few weeks,
*  which is trying to get a useful tool out of it,
*  and they may well do it.
*  In that sense at least alpha fold is different
*  because your alpha fold too is different.
*  Because now it's producing data sets
*  that are actually potentially revolutionizing
*  competition biology.
*  They will actually help a lot of people.
*  But you would say potentially revolutionizing.
*  We don't know yet.
*  But yeah.
*  That's true, yeah.
*  But I got you.
*  Okay, so you know what?
*  This is gonna be so fun.
*  So let's go right into it.
*  Speaking of robots that operate in the real world.
*  Let's talk about self-driving cars.
*  Oh.
*  Okay.
*  Because you have built robotics companies.
*  You're one of the greatest roboticists in history
*  and that's not just in the space of ideas.
*  We'll also probably talk about that.
*  But in the actual building and execution of businesses
*  that make robots that are useful for people
*  and that actually work in the real world and make money.
*  You also sometimes are critical of Mr. Elon Musk
*  or let's more specifically focus
*  on this particular technology,
*  which is autopilot inside Teslas.
*  What are your thoughts about Tesla autopilot
*  or more generally vision-based machine learning approach
*  to semi-autonomous driving?
*  These are robots that are being used in the real world
*  by hundreds of thousands of people.
*  And if you wanna go there, I can go there,
*  but that's not too much.
*  Which let's say they're on par safety-wise
*  as humans currently.
*  Meaning human alone versus human plus robot.
*  Okay, so first let me say I really like the car
*  I came in here today.
*  Which is?
*  2021 model, Mercedes E450.
*  I am impressed by the machine vision.
*  So are other things.
*  I'm impressed by what it can do.
*  I'm really impressed with many aspects of it.
*  It's able to stay in lane, is it?
*  It does the lane stuff.
*  It's looking on either side of me.
*  It's telling me about nearby cars.
*  For blind spots and so on.
*  Yeah, when I'm going in close to something in the park,
*  I get this beautiful, gorgeous, top-down view of the world.
*  I am impressed up the wazoo of how registered and metrical.
*  Oh, so it's like multiple cameras
*  and it's all ready to go to produce the 360 view kind of thing?
*  It's synthesized so it's above the car.
*  And it is unbelievable.
*  I got this car in January.
*  It's the longest I've ever owned a car without digging it.
*  So it's better than me.
*  It's me and it together better.
*  So I'm not saying technology's bad or not useful.
*  But here's my point.
*  Yes.
*  It's a replay of the same movie.
*  So maybe you've seen me ask this question before.
*  But when did the first car go over 55 miles an hour
*  for over 10 miles on a public freeway
*  with other traffic driving completely autonomously?
*  When did that happen?
*  Was it the MU in the 80s or something?
*  It was a long time ago.
*  It was actually in 1987 in Munich.
*  Munich, yeah.
*  At the Bundeswehr.
*  So they had it running in 1987.
*  When do you think, and Elon has said he's gonna do this,
*  when do you think we'll have the first car
*  drive coast to coast in the US, hands off the wheel,
*  hands off the wheel, feet off the pedals, coast to coast?
*  As far as I know, a few people have claimed to do it.
*  1995, that was the time of the year.
*  I didn't know, oh, that was the,
*  yeah, they didn't claim, did they claim 100%?
*  Not 100%, not 100%.
*  And then there's a few marketing people
*  who have claimed 100% since then.
*  But my point is that, you know,
*  what I see happening again is someone sees a demo
*  and they overgeneralize and say, we must be almost there.
*  Well, we've been working on it for 35 years.
*  So that's demos.
*  But this is gonna take us back to the same conversation
*  with AlphaZero.
*  Are you not, okay, I'll just say what I am.
*  Because I thought, okay, when I first started interacting
*  with the Mobileye implementation at Tesla Autopilot,
*  I've driven a lot of, you know,
*  I've been in Google stuff driving cars since the beginning.
*  I thought there was no way,
*  before I sat and used Mobileye,
*  I thought just knowing computer vision,
*  I thought there's no way it could work
*  as well as it was working.
*  So my model of the limits of computer vision
*  was way more limited
*  than the actual implementation of Mobileye.
*  So that's one example.
*  I was really surprised.
*  I was like, wow, that was incredible.
*  The second surprise came when Tesla threw away Mobileye
*  and started from scratch.
*  I thought there's no way they can catch up to Mobileye.
*  I thought what Mobileye was doing was kind of incredible,
*  like the amount of work and the annotation.
*  Yeah, well, Mobileye was started by Amnon Shresher
*  and used a lot of traditional, you know,
*  hard-fought computer vision techniques.
*  But they also did a lot of good sort of,
*  like non-research stuff, like actual,
*  just good, like what you do to make a successful product,
*  right, scale, all that kind of stuff.
*  And so I was very surprised when they, from scratch,
*  were able to catch up to that.
*  That's very impressive.
*  And I've talked to a lot of engineers that was involved.
*  This is, that was impressive.
*  And the recent progress, especially under,
*  well, with the involvement of Andre Kapathi,
*  what they were, what they're doing with the data engine,
*  which is converting into the driving task
*  into these multiple tasks,
*  and then doing this edge case discovery
*  when they're pulling back,
*  like the level of engineering
*  made me rethink what's possible.
*  I don't, I still, you know,
*  I don't know to that intensity,
*  but I always thought it was very difficult
*  to solve autonomous driving with all the sensors,
*  with all the computation.
*  I just thought it was a very difficult problem.
*  But I've been continuously surprised
*  how much you can engineer,
*  first of all, the data acquisition problem.
*  Because I thought, you know,
*  just because I worked with a lot of car companies,
*  they're so a little bit old school
*  to where I didn't think they could do this at scale,
*  like AWS style data collection.
*  So when Tesla was able to do that,
*  I started to think, okay, so what are the limits of this?
*  I still believe that driver,
*  like sensing and the interaction with the driver
*  and like studying the human factors psychology problem
*  is essential.
*  It's always going to be there.
*  It's always going to be there,
*  even with fully autonomous driving.
*  But I've been surprised, what is the limit,
*  especially a vision-based alone,
*  how far that can take us.
*  So that's my levels of surprise.
*  Now,
*  okay,
*  can you explain,
*  in the same way you said like AlphaZero,
*  that's a homework problem that scaled large in its chest,
*  like who cares, go with it.
*  Here's actual people using an actual car and driving,
*  many of them drive more than half their miles
*  using this system.
*  Right.
*  So yeah, they're doing well with pure vision.
*  Pure vision, yeah.
*  And you know, they...
*  And now no radar, which is...
*  I suspect that can't go all the way.
*  And one reason is,
*  without new cameras that have a dynamic range
*  closer to the human eye,
*  because human eye has incredible dynamic range,
*  and we make use of that dynamic range
*  in its 11 orders of magnitude
*  or some crazy number like that.
*  The cameras don't have that,
*  which is why you see the bad cases
*  where the sun on a white thing
*  and it blinds, in a way it wouldn't blind a person.
*  I think there's a bunch of things to think about
*  before you say, this is so good,
*  it's just gonna work.
*  Okay?
*  And I'll come at it from multiple angles.
*  And I know you've got a lot of time.
*  Yeah, okay, let's do this.
*  I have thought about these things.
*  Yeah, I know.
*  You've been writing a lot of great blog posts
*  about it for a while before Tesla had autopilot, right?
*  So you've been thinking about autonomous driving
*  for a while from every angle.
*  So a few things.
*  You know, in the US,
*  I think that the death rate from motor vehicle accidents
*  is about 35,000 a year,
*  which is an outrageous number.
*  Not outrageous compared to COVID deaths,
*  but there is no rationality.
*  And that's part of the thing.
*  People have said, engineers say to me,
*  well, if we cut down the number of deaths by 10%
*  by having autonomous driving,
*  that's gonna be great, everyone will love it.
*  And my prediction is that if autonomous vehicles
*  kill more than 10 people a year,
*  they'll be screaming and hollering,
*  even though 35,000 people a year
*  have been killed by human drivers.
*  It's not rational.
*  It's a different set of expectations.
*  And that will probably continue.
*  So there's that aspect of it.
*  The other aspect of it is that
*  when we introduce new technology,
*  we often change the rules of the game.
*  So when we introduced cars first,
*  you know, into our daily lives,
*  we completely rebuilt our cities
*  and we changed all the laws.
*  Jaywalking was not an offense.
*  That was pushed by the car companies
*  so that people would stay off the road
*  so there wouldn't be deaths from pedestrians getting hit.
*  We completely changed the structure of our cities
*  and had these foul smelling things, you know,
*  everywhere around us.
*  And now you see pushback in cities like Barcelona
*  is really trying to exclude cars, et cetera.
*  So I think that to get to self-driving,
*  we will, large adoption,
*  it's not gonna be just take the current situation
*  take out the driver and put the same car
*  doing the same stuff because the end case is too many.
*  Here's an interesting question.
*  How many fully autonomous train systems
*  do we have in the US?
*  I mean, do you count them as fully autonomous?
*  I don't know, because they're usually as a driver,
*  but they're kind of autonomous, right?
*  No, let's get rid of the driver.
*  Okay, I don't know.
*  It's either 15 or 16.
*  Most of them are in airports.
*  Okay.
*  There's a few that go about five,
*  two that go about five kilometers out of airports.
*  Yeah.
*  When is the first fully autonomous train system
*  for mass transit expected to operate fully autonomously
*  with no driver in a US city?
*  It's expected to operate in 2017 in Honolulu.
*  Oh, wow.
*  It's delayed, but they will get there.
*  Bart, by the way, was originally gonna be autonomous
*  here in the Bay Area.
*  I mean, they're all very close to fully autonomous, right?
*  Yeah, but getting the closest to think,
*  and I have often gone on a fully autonomous train in Japan,
*  one that goes out to that fake island
*  in the middle of Tokyo Bay, I forget the name of the,
*  and what do you see when you look at that?
*  What do you see when you go to a fully autonomous train
*  in an airport?
*  It's not like regular trains.
*  There's, at every station, there's a double set of doors,
*  so that there's a door of the train
*  and there's a door off the platform.
*  And it's really visible in this Japanese one
*  because it goes out in amongst buildings.
*  The whole track is built so that people
*  can't climb onto it.
*  Yeah.
*  So there's engineering that then makes the system safe
*  and makes them acceptable.
*  I think we'll see similar sorts of things happen in the US.
*  What surprised me, I thought, wrongly,
*  that we would have special purpose lanes on 101
*  in the Bay Area, the leftmost lane,
*  so that it would be normal for Teslas or other cars
*  to move into that lane and then say,
*  okay, now it's autonomous and have that dedicated lane.
*  I was expecting movement to that.
*  Five years ago, I was expecting we'd have a lot more
*  movement towards that.
*  We haven't.
*  And it may be because Tesla's been over-promising
*  by saying this, calling their system fully self-driving.
*  I think they may have gotten there quicker
*  by collaborating to change the infrastructure.
*  This is one of the problems with long-haul trucking
*  being autonomous.
*  I think it makes sense on freeways at night
*  for the trucks to go autonomously.
*  But then there's the how do you get onto and off
*  of the freeway?
*  What sort of infrastructure do you need for that?
*  Do you need to have the human in there to do that?
*  Or can you get rid of the human?
*  So I think there's ways to get there,
*  but it's an infrastructure argument
*  because the long tail of cases is very long
*  and the acceptance of it will not be at the same level
*  as human drivers.
*  So I'm with you still and I was with you for a long time,
*  but I am surprised how well, how many edge cases
*  machine learning and vision-based methods can cover.
*  This is what I'm trying to get at is,
*  I think there's something fundamentally different
*  with vision-based methods and Tesla Autopilot
*  and any company that's trying to do the same.
*  Okay, well, I'm not gonna argue with you
*  because we're speculating.
*  Yes.
*  And my gut feeling tells me it's gonna be
*  things will speed up when there is engineering
*  of the environment because that's what happened
*  with every other technology.
*  I'm a bit, I don't know about you,
*  but I'm a bit cynical that infrastructure
*  which relies on government to help out in these cases.
*  If you just look at infrastructure in all domains,
*  it's just a government always drags behind
*  on infrastructure.
*  There's like, there's so many just-
*  Well, in this country.
*  Sure, sorry, yes.
*  In this country, and of course there's many, many countries
*  that are actually much worse on infrastructure.
*  Oh yes, many of them are much worse
*  and there's some that, like high-speed rail,
*  the other countries have done much better.
*  I guess my question is like, which is at the core
*  of what I was trying to think through here and ask you
*  is like, how hard is the driving problem
*  as it currently stands?
*  So you mentioned like, we don't want to just take
*  the human out and duplicate whatever the human was doing,
*  but if we were to try to do that,
*  how hard is that problem?
*  Because I used to think is way harder.
*  Like I used to think it's, with vision alone,
*  it would be three decades, four decades.
*  Okay, so I don't know the answer to this thing
*  I'm about to pose, but I do notice that on highway 280
*  here in the Bay Area, which largely has concrete surface
*  rather than blacktop surface, the white lines
*  that are painted there now have black boundaries around them.
*  And my lane drift system in my car would not work
*  without those black boundaries.
*  Interesting.
*  So I don't know whether they've started doing it
*  to help the lane drift, whether it is an instance
*  of infrastructure following the technology,
*  but my car would not perform as well without that change
*  in the way they paint the line.
*  Unfortunately, really good lane keeping
*  is not as valuable, like it's orders of magnitude
*  more valuable to have a fully autonomous system.
*  Like.
*  Yeah, but for me, lane keeping is really helpful
*  because I'm healthy at it.
*  But you wouldn't pay 10 times, like,
*  the problem is there's not financial,
*  like it doesn't make sense to revamp the infrastructure
*  to make lane keeping easier.
*  It does make sense to revamp the infrastructure.
*  Oh, I see what you have a large fleet of autonomous vehicles.
*  Now you change what it means to own cars.
*  You change the nature of transportation.
*  That mean, but that for that, you need autonomous vehicles.
*  Let me ask you about Waymo then.
*  I've gotten a bunch of chances to ride
*  in a Waymo self-driving car and there,
*  I don't know if you'd call them self-driving, but.
*  Well, I mean, I rode in one before that called Waymo.
*  Yeah.
*  So at X.
*  So there's currently, it was a big leap,
*  another surprising leap, I didn't think it would happen,
*  which is they have no driver currently.
*  Yeah, in Chandler.
*  In Chandler, Arizona.
*  And I think they're thinking of doing that in Austin as well.
*  But they're expanding.
*  Although, and I do an annual checkup on this.
*  So as of late last year,
*  they were aiming for hundreds of rides a week,
*  not thousands.
*  And there is no one in the car,
*  but there's certainly safety people in the loop.
*  And it's not clear how many,
*  what the ratio of cars to safety people is.
*  It wasn't, obviously,
*  they're not 100% transparent about this.
*  No, none of them are 100% transparent.
*  They're very untransparent.
*  But at least the way they're,
*  I don't wanna make definitively,
*  but they're saying there's no teleoperation.
*  So like, they're, I mean, okay.
*  And that sort of fits with YouTube videos
*  I've seen of people being trapped in the car
*  by a red cone on the street.
*  And they do have rescue vehicles that come.
*  And then a person gets in and drives it.
*  Yeah.
*  But isn't it incredible to you,
*  it was to me to get in a car with no driver
*  and watch the steering wheel turn.
*  Like for somebody who has been studying,
*  at least certainly the human side
*  of autonomous vehicles for many years,
*  and you've been doing it for way longer.
*  Like it was incredible to me
*  that this was actually could happen.
*  I don't care if that scale is 100 cars.
*  This is not a demo.
*  This is me as a regular human.
*  No, the argument I have is that people
*  make interpolations from that.
*  Interpolations.
*  That it's here, it's done.
*  It's just, we've solved it.
*  No, we haven't yet.
*  And that's my argument.
*  Okay, so I'd like to go to,
*  you keep a list of predictions.
*  Yeah, okay.
*  On your amazing blog posts.
*  It'd be fun to go through them.
*  But before that, let me ask you about this.
*  You have,
*  you have a harshness to you sometimes
*  in your criticisms of what is perceived
*  as hype.
*  And so like, because people extrapolate,
*  like you said, and they kind of buy into the hype,
*  and then they kind of start to think that
*  the technology is way better than it is.
*  But let me ask you maybe a difficult question.
*  Do you think if you look at history of progress,
*  don't you think to achieve the quote impossible,
*  you have to believe that it's possible?
*  Absolutely, yeah.
*  Look, his two great runs.
*  Great, unbelievable.
*  1903, first human,
*  human heavier than air flight.
*  Yeah.
*  1969,
*  we land on the moon.
*  That's 66 years.
*  I'm 66 years old.
*  In my lifetime, that span of my lifetime,
*  barely flying, I don't know what it was,
*  50 feet, the length of the first flight or something,
*  to landing on the moon.
*  Unbelievable, fantastic.
*  But that requires, by the way,
*  one of the Wright brothers, both of them,
*  but one of them didn't believe it seemed impossible
*  like a year before, right?
*  So like, not just possible,
*  soon, but like ever.
*  So, you know.
*  How important is it to believe
*  and be optimistic is what I guess.
*  Oh yeah, it is important.
*  It's when it goes crazy.
*  When, you know, you said it.
*  What was the word you used for my bad?
*  Harshness.
*  Harshness, yes.
*  I just get so frustrated
*  when people make these leaps
*  and tell me that I'm not going to make it.
*  I'm not going to make it.
*  I'm not going to make it.
*  I'm not going to make it.
*  I'm going to make the leaps
*  and tell me that I don't understand.
*  Right.
*  Yeah.
*  There's just from iRobot,
*  which I was co-founder of.
*  I don't know the exact numbers now
*  because it's 10 years since I stepped off the board,
*  but I believe it's well over 30 million
*  robots cleaning houses from that one company.
*  And now there's lots of other companies.
*  Yes.
*  Was that a crazy idea that we had to believe
*  in 2002 when we released it?
*  Yeah.
*  That was, we had to, you know,
*  believe that it could be done.
*  Let me ask you about this.
*  So iRobot, one of the greatest robotics companies ever
*  in terms of creating a robot
*  that actually works in the real world
*  is probably the greatest robotics company ever.
*  You're the co-founder of it.
*  If the Rodney Brooks of today
*  talked to the Rodney of back then,
*  what would you tell them?
*  Because I have a sense that
*  would you pat them on the back and say,
*  what you're doing is going to fail,
*  but go at it anyway?
*  That's what I'm referring to with the harshness.
*  You've accomplished an incredible thing there.
*  One of the several things we'll talk about.
*  Like that's what I'm trying to get at that line.
*  No, it's when, my harshness is reserved
*  for people who are not doing it,
*  who claim it's just, well, this shows
*  that it's just gonna happen.
*  But here's the thing.
*  This shows.
*  But you have that harshness for Elon too.
*  Or no, it's a different harshness.
*  No, it's a different argument with Elon.
*  I think SpaceX is an amazing company.
*  On the other hand, in one of my blog posts,
*  I said, what's easy and what's hard?
*  I said, SpaceX vertical landing rockets,
*  it had been done before.
*  Grid fins had been done since the 60s.
*  Every Soyuz has them.
*  Reusable, SpaceX reused those rockets
*  that landed vertically.
*  There was a whole insurance industry in place
*  for rocket launches.
*  There were all sorts of infrastructure.
*  That was doable.
*  It took a great entrepreneur, a great personal expense.
*  He almost drove himself bankrupt doing it.
*  A great belief to do it.
*  Whereas Hyperloop, there's a whole bunch more stuff
*  that's never been thought about, never been demonstrated.
*  My estimation is Hyperloop is a long, long,
*  a lot further off.
*  If I've got a criticism of Elon,
*  it's that he doesn't make distinctions
*  between when the technology's coming along and ready,
*  and then he'll go off and mouth off about other things.
*  Which then people go and compete about and try and do.
*  This is where I understand what you're saying.
*  I tend to draw a different distinction.
*  I have a similar kind of harshness towards people
*  who are not telling the truth.
*  Who are basically fabricating stuff to make money or to...
*  Well, he believes what he says.
*  I just think he's wrong sometimes.
*  To me, that's a very important difference.
*  Yeah, I'm not food.
*  Because I think in order to fly,
*  in order to get to the moon, you have to believe
*  even when most people tell you you're wrong,
*  and most likely you're wrong, but sometimes you're right.
*  That's the same thing I have with Tesla Autopilot.
*  I think that's an interesting one.
*  Especially when I was at MIT,
*  and just the entire human factors in the robotics community
*  were very negative towards Elon.
*  It was very interesting for me to observe colleagues at MIT.
*  I wasn't sure what to make of that.
*  That was very upsetting to me
*  because I understood where that's coming from.
*  And I agreed with them,
*  and I kind of almost felt the same thing in the beginning
*  until I kind of opened my eyes
*  and realized there's a lot of interesting ideas here.
*  There might be overhype.
*  If you focus yourself on the idea that
*  you shouldn't call a system full self-driving
*  when it's obviously not fully autonomous,
*  you're going to miss the magic of progress.
*  You are gonna miss the magic, but at the same time,
*  there are people who buy it, literally pay money for it,
*  and take those words as given.
*  And that's...
*  But I haven't...
*  Take words as given as one thing.
*  I haven't actually seen people that use Autopilot
*  that believe that the behavior is really important,
*  like the actual action.
*  So to push back on the very thing
*  that you're frustrated about,
*  which is journalists and general people
*  buying all the hype and going out.
*  In the same way, I think there's a lot of hype
*  about the negatives of this too,
*  that people are buying without using.
*  People use the way...
*  This was...
*  This opened my eyes, actually.
*  The way people use a product is very different
*  than the way they talk about it.
*  This is true with robotics, with everything.
*  Everybody has dreams of how a particular product
*  might be used or so on.
*  And then when it meets reality,
*  there's a lot of fear of robotics, for example,
*  that robots are somehow dangerous
*  and all those kinds of things.
*  But when you actually have robots in your life,
*  whether it's in the factory or in the home,
*  making your life better, that's going to be...
*  That's way different.
*  Your perceptions of it are gonna be way different.
*  And so my just tension was, here's an innovator.
*  What is it?
*  Sorry, SuperCruise from Cadillac was super interesting too.
*  That's a really interesting system.
*  We should be excited by those innovations.
*  Okay, so can I tell you something
*  that's really annoyed me recently?
*  It's really annoyed me that the press
*  and friends of mine on Facebook are going,
*  these billionaires and their space games,
*  why are they doing that?
*  Yeah, that's been very frustrating.
*  That really pisses me off.
*  I must say, I applaud that.
*  I applaud it.
*  It's the taking and not necessarily the people
*  who are doing the things,
*  but that I keep having to push back against
*  unrealistic expectations
*  of when these things can become real.
*  Yeah, this was interesting
*  because there's been a particular focus for me
*  is autonomous driving.
*  Elon's prediction of when certain milestones will be hit.
*  There's several things to be said there
*  that I always, I thought about.
*  Whenever you said them, it was obvious
*  that's not going to me as a person
*  that kind of not inside the system.
*  It was obvious it's unlikely to hit those.
*  There's two comments I want to make.
*  One, he legitimately believes it.
*  And two, much more importantly,
*  I think that having ambitious deadlines
*  drives people to do the best work of their life,
*  even when the odds of those deadlines are very low.
*  To a point, and I'm not talking about it,
*  Elon, I'm just saying.
*  So there's a line there, right?
*  You have to have a line
*  because you over extend and it's demoralizing.
*  Yeah.
*  But I will say that there's an additional thing here
*  that those words also drive the stock market.
*  Yeah.
*  And we have because of the way that rich people in the past
*  have manipulated the rubes through investment.
*  We have developed rules about what you're allowed to say.
*  And I promise.
*  And there's an area here which is...
*  I tend to be, maybe I'm naive,
*  but I tend to believe that engineers, innovators,
*  people like that, they don't think like that,
*  like manipulating the stock price,
*  but it's possible that I'm wrong.
*  It's a very cynical view of the world
*  because I think most people that run companies,
*  especially original founders, they...
*  Yeah, I'm not saying that's the intent.
*  I'm saying it's a...
*  Eventually it's kind of you fall
*  into that kind of a behavior pattern.
*  I don't know.
*  I tend to...
*  I wasn't saying it's falling into that intent.
*  It's just you also have to protect investors in this market.
*  Yeah.
*  Okay, so you have...
*  First of all, you have an amazing blog
*  that people should check out,
*  but you also have in that blog a set of predictions.
*  Such a cool idea.
*  I don't know how long ago you started,
*  like three, four years ago.
*  It was January 1st, 2018.
*  18, yeah.
*  And I made these predictions
*  and I said that every January 1st,
*  I was gonna check back on how my predictions are.
*  That's such a great thought experiment.
*  For 32 years.
*  Oh, so you said 32 years.
*  I said 32 years
*  because I thought that would be January 1st, 2050.
*  I'll be...
*  I will just turn 95.
*  Nice.
*  And so people know that your predictions,
*  at least for now,
*  are in the space of artificial intelligence.
*  Yeah, I didn't say I was gonna make new predictions.
*  I was just gonna measure this set of predictions
*  that I made because I was sort of annoyed
*  that everyone could make predictions,
*  they didn't come true and everyone forgot.
*  So I said, I should hold myself to a high standard.
*  Yeah, but also just putting years
*  and date ranges on things,
*  it's a good thought exercise
*  and reasoning your thoughts out.
*  And so the topics are artificial intelligence,
*  autonomous vehicles, and space.
*  I was wondering if we could just go through some
*  that stand out maybe from memory,
*  I can just mention to you some.
*  Let's talk about self-driving cars.
*  Some predictions that you're particularly proud of
*  or are particularly interesting
*  from flying cars to the other element here
*  is how widespread the location,
*  where the deployment of the autonomous vehicles is.
*  And there's also just a few fun ones.
*  Is there something that jumps to mind
*  that you remember from the predictions?
*  Well, I think I did put in there
*  that there would be a dedicated self-driving lane on 101
*  by some year and I think I was over optimistic on that one.
*  Yeah, I actually do remember that.
*  But I think you were mentioning
*  difficulties at different cities.
*  Yeah.
*  Cambridge, Massachusetts, I think was an example.
*  Yeah, like in Cambridgeport.
*  I lived in Cambridgeport for a number of years
*  and the roads are narrow
*  and getting anywhere as a human driver
*  is incredibly frustrating when you start to put...
*  And people drive the wrong way on one-way streets there.
*  It's just...
*  So your prediction was driverless taxi services
*  operating on all streets in Cambridgeport, Massachusetts
*  in 2035.
*  Yeah, and that may have been too optimistic.
*  You think so?
*  You know, I've gotten a little more pessimistic
*  since I made these internally on some of these things.
*  So what...
*  Can you put a year to a major milestone
*  of deployment of a taxi service
*  in a few major cities?
*  Like something where you feel like...
*  Yeah, so...
*  Autonomous vehicles are here.
*  So let's take the grid streets of San Francisco
*  north of Market.
*  Okay.
*  Okay.
*  So, relatively benign environment.
*  The streets are wide.
*  The major problem is delivery trucks stopping everywhere,
*  which has made things more complicated.
*  A taxi system there
*  with somewhat designated pickup and drop-offs,
*  unlike with Uber and Lyft,
*  where you can sort of get to any place
*  and the drivers will figure out how to get in there.
*  We're still a few years away.
*  I live in that area.
*  So I see the self-driving car companies,
*  cars, multiple ones every day,
*  now if they drive a cruise.
*  Zooks less often, Waymo all the time,
*  different ones come and go.
*  And there's always a driver.
*  There's always a driver at the moment.
*  Although I have noticed that sometimes the driver
*  does not have the authority to take over
*  without talking to the home office
*  because they will sit there waiting for a long time.
*  And clearly something's going on
*  where the home office is making a decision.
*  That's fascinating.
*  So they're, you know,
*  and so you can see whether they've got their hands
*  or not and it's the incident resolution time
*  that tells you, gives you some clues.
*  So what year do you think, what's your intuition?
*  What date range are you currently thinking
*  San Francisco would be autonomous taxi service
*  from any point A to any point B without a driver?
*  Are you still, are you thinking 10 years from now,
*  20 years from now, 30 years from now?
*  Certainly not 10 years from now.
*  It's gonna be longer.
*  If you're allowed to go south of the market, way longer.
*  And unless it's re-engineering of roads.
*  By the way, what's the biggest challenge?
*  You mentioned a few.
*  Is it the delivery trucks?
*  Is it the edge cases, the computer perception,
*  computer vision problem?
*  Here's a case that I saw outside my house a few weeks ago
*  about 8 p.m. on a Friday night.
*  It was getting dark.
*  It was before the solstice.
*  It was a cruise vehicle come down the hill, turned right
*  and stopped dead covering the crosswalk.
*  Why did it stop dead?
*  Cause there was a human just two feet from it.
*  Now I just glanced, I knew what was happening.
*  The human was a woman was at the door of her car
*  trying to unlock it with one of those things
*  that you know, when you don't have a key.
*  Yes.
*  The car thought, oh, she could jump out
*  in front of me any second.
*  Yeah.
*  As a human, I could tell, no, she's not gonna jump out.
*  She's busy trying to unlock her.
*  She's lost her keys.
*  She's trying to get in the car.
*  And it stayed there for until I got bored.
*  Yeah.
*  And so the human driver in there did not take over.
*  But here's the kicker to me.
*  A guy comes down the hill with a stroller.
*  I assumed there was a baby in there.
*  And now the crosswalk's blocked by this cruise vehicle.
*  What's he gonna do?
*  Cleverly, I think he decided not to go in front of the car.
*  He went, but he had to go behind it.
*  He had to get off the crosswalk out into the intersection
*  to push his baby around this car, which was stopped there.
*  And no human driver would have stopped there
*  for that length of time.
*  They would have gotten out of the way.
*  And that's another one of my pet peeves
*  that safety has been compromised for individuals
*  who didn't sign up for having this happen
*  in their neighborhood.
*  Yeah, but-
*  Now you can say that's an edge case, but-
*  Yeah, well, I'm in general not a fan,
*  which of anecdotal evidence for stuff like,
*  this is one of my biggest problems
*  with the discussion of autonomous vehicles in general,
*  people that criticize them or support them are using edge cases.
*  Okay.
*  Are using anecdotal evidence.
*  So let me-
*  But I got you.
*  You know, your question is when is it gonna happen
*  in San Francisco?
*  I say not soon, but it's gonna be one of them.
*  But where it is gonna happen is in limited domains,
*  campuses of various sorts, gated communities,
*  where the other drivers are not arbitrary people.
*  They're people who know about these things.
*  They, you know, it's been warned about them.
*  And at velocities where it's always safe to stop dead.
*  Yeah.
*  You can't do that on the freeway.
*  That I think we're gonna start to see.
*  And they may not be shaped like, you know, current cars.
*  They may be, you know, things like, you know,
*  may mobility has those things.
*  And various companies have these.
*  Yeah, I wonder if that's a compelling experience.
*  To me, it's always important.
*  It's not just about automation.
*  It's about creating a product that like,
*  that makes your, it's not just cheaper,
*  but makes your, that's fun to ride.
*  One of the most, one of the least fun things
*  is for a car that stops and like waits.
*  There's something deeply frustrating for us humans,
*  for the rest of the world to take advantage of us
*  as we wait.
*  But think about, you know, not you as the customer,
*  but someone who's in their 80s in a retirement village.
*  Yes.
*  Kids have said, you're not driving anymore.
*  And this gives you the freedom to go to the market.
*  That's a hugely beneficial thing,
*  but it's a very few orders of magnitude,
*  less impact on the world.
*  It's not, it's just a few people in a small community
*  using cars as opposed to the entirety of the world.
*  I like that the first time that a car equipped
*  with some version of a solution to the trolley problem
*  is what's NIML stand for?
*  Not in my life.
*  Not in my life.
*  I define my lifetime as up to.
*  2050.
*  2050.
*  Yeah.
*  You know, I ask you, when have you had to decide
*  which person shall I kill?
*  No, you put the brakes on and you brake as hard as you can.
*  You're not making that decision.
*  It is, you know, I do think autonomous vehicles
*  or semi-autonomous vehicles do need to solve
*  the whole pedestrian problem that has elements
*  of the trolley problem within it, but it's not.
*  Yeah, well, so here's, and I talk about it
*  in one of my articles or blog posts that I wrote.
*  Here's, and people have told me,
*  one of my coworkers has told me he does this.
*  He tortures autonomously driven vehicles
*  and pedestrians will torture them.
*  Once they realize that putting one foot off the curb
*  makes the car think that they might walk into the road,
*  kids, teenagers will be doing that all the time.
*  They will.
*  I, by the way, one of my,
*  and this is a whole nother discussion,
*  because my main issue with robotics
*  is HRI, human-robot interaction.
*  I believe that robots that interact with humans
*  will have to push back.
*  Like, they can't just be bullied,
*  because that creates a very uncompelling experience
*  for the humans.
*  Yeah, well, Waymo, before it was called Waymo,
*  discovered that they had to do that
*  at four-way intersections.
*  They had to nudge forward to give the cue
*  that they were gonna go,
*  because otherwise the other drivers
*  would just beat them all the time.
*  So you co-founded iRobot, as we mentioned,
*  one of the most successful robotics companies ever.
*  What are you most proud of with that company
*  and the approach you took to robotics?
*  Well, there's something I'm quite proud of there,
*  which may be a surprise,
*  but I was still on the board when this happened.
*  It was March 2011,
*  and we sent robots to Japan,
*  and they were used to help shut down
*  the Fukushima Daiichi nuclear power plant.
*  Which was, everything was,
*  I've been there since, I was there in 2014,
*  and the robots, some of the robots were still there.
*  I was proud that we were able to do that.
*  Why were we able to do that?
*  And people have said,
*  well, Japan is so good at robotics.
*  It was because we had had about 6,500 robots deployed
*  in Iraq and Afghanistan, tele-opt,
*  but with intelligence, dealing with roadside bombs.
*  So we had, I think it was at that time,
*  nine years of in-field experience
*  with the robots in harsh conditions.
*  Whereas the Japanese robots, which were getting,
*  you know, this goes back to what?
*  Annoyed me so much.
*  Getting all the hype, look at that,
*  look at that Honda robot, it can walk,
*  wow, the future's here.
*  Couldn't do a thing, because they weren't deployed,
*  but we had deployed in really harsh conditions
*  for a long time.
*  And so we're able to do something very positive
*  in a very bad situation.
*  What about just the simple,
*  and for people who don't know,
*  one of the things that iRobot has created
*  is the Roomba vacuum cleaner.
*  What about the simple robot that is the Roomba,
*  quote unquote simple,
*  that's deployed in tens of millions of homes.
*  What do you think about that?
*  Well, I make the joke that I started out life
*  as a pure mathematician
*  and turned into a vacuum cleaner salesman.
*  So if you're gonna be an entrepreneur,
*  be ready to do anything.
*  But I was, you know,
*  there was a wacky lawsuit
*  that I got posed for not too many years ago.
*  And I was the only one who had emailed from the 1990s.
*  And no one in the company had it.
*  So I went and went through my email
*  and it reminded me of, you know,
*  the joy of what we were doing.
*  And what was I doing?
*  What was I doing at the time we were building
*  building the Roomba?
*  One of the things was we had this incredibly tight budget
*  because we wanted to put it on the shelves at $200.
*  There was another home cleaning robot at the time.
*  It was the Electrolux Trilobite,
*  which sold for 2000 euros.
*  And to us that was not gonna be a consumer product.
*  So we had reason to believe that $200
*  was a thing that people would buy at.
*  That was our aim.
*  But that meant we had, you know,
*  that's on the shelf making profit.
*  That means the cost of goods has to be minimal.
*  So I find all these emails of me going,
*  you know, I'd be in Taipei for a MIT meeting.
*  And I'd stay a few extra days.
*  I'd go down to Shenzhou
*  and talk to these little tiny companies,
*  lots of little tiny companies outside of TSMC,
*  Taiwan Semiconductor Manufacturing Corporation,
*  which let all these little companies be fabulous.
*  They didn't have to have their own fab so they could innovate.
*  And their innovations were to build stripped down 6802s.
*  6802 was what was in an Apple One.
*  Get rid of half the silicon, still have it be viable.
*  And I'd previously got some of those
*  for some earlier failed products of iRobot.
*  And then that was in Hong Kong,
*  going to all these companies that built,
*  you know, they weren't gaming in the current sense.
*  They were these handheld games that you would play
*  or birthday cards.
*  Because we had about a 50 cent budget for computation.
*  So I'm tracking from place to place,
*  looking at their chips, looking at what they'd removed.
*  Ah, their interrupt handling is too weak
*  for a general purpose.
*  So I was going deep technical detail.
*  And then I found this one from a company called Windbond,
*  which had, and I'd forgotten it had this much RAM.
*  It had 512 bytes of RAM and it was in our budget.
*  And it had all the capabilities we needed.
*  Yeah.
*  So you were excited.
*  Yeah, and I was reading all these emails,
*  Colin, I found this.
*  So did you think, did you ever think
*  that you guys could be so successful?
*  Like eventually this company would be so successful.
*  Did you, could you possibly have imagined?
*  No, we never did think that.
*  We'd had 14 failed business models up till 2002.
*  And then we had two winners the same year.
*  No, and then, you know, we, I remember the board,
*  because by this time we had some venture capital in.
*  The board went along with us building
*  some robots for, you know, aiming at the Christmas 2002
*  market.
*  And we went three times over what they authorized
*  and built 70,000 of them and sold them all in that first,
*  cause we released on September 18th
*  and they were all sold by Christmas.
*  So it was, so we were gutsy, but.
*  But yeah, you didn't think this would take over the world.
*  Well, this is, so a lot of amazing robotics companies
*  have gone under over the past few decades.
*  Why do you think it's so damn hard
*  to run a successful robotics company?
*  There's a few things.
*  One is expectations of capabilities by the founders
*  that are off base.
*  The founders, not the consumer, the founders.
*  Yeah, expectations of what can be delivered.
*  Sure.
*  Mispricing and what a customer thinks is a valid price
*  is not rational necessarily.
*  Yeah.
*  And expectations of customers.
*  And just the sheer hardness of getting people
*  to adopt a new technology.
*  And I've suffered from all three of these.
*  I've had more failures than successes in terms of companies.
*  I've suffered from all three.
*  Do you think one day there will be a robotics company,
*  and by robotics company I mean,
*  where your primary source of income is from robots,
*  that will be a trillion plus dollar company.
*  And so what would that company do?
*  I can't, because I'm still starting robot companies.
*  Yeah.
*  I'm not making any such predictions in my own mind.
*  I'm not thinking about a trillion dollar company.
*  And by the way, I don't think in the 90s
*  anyone was thinking that Apple
*  would ever be a trillion dollar company.
*  So these are very hard to predict.
*  But sorry to interrupt,
*  because I kind of have a vision in a small way,
*  a big vision in a small way,
*  that I see that there would be robots in the home
*  at scale, like Roomba, but more.
*  And that's a trillion dollar.
*  Right.
*  And I think there's a real market pull for them
*  because of the demographic inversion.
*  Who's gonna do all the stuff for the older people?
*  There's too many.
*  You know, I'm leading here.
*  There's gonna be too many of us.
*  But we don't have capable enough robots
*  to make that economic argument at this point.
*  Do I expect that that will happen?
*  Yes, I expect it will happen.
*  But I gotta tell you, we introduced the Roomba in 2002,
*  and I stayed another nine years.
*  We were always trying to find
*  what the next home robot would be.
*  And still today, the primary product of 20 years later,
*  almost 20 years later, 19 years later,
*  the primary product is still the Roomba.
*  So iRobot hasn't found the next one.
*  Do you think it's possible for one person in the garage
*  to build it versus like Google launching
*  Google self-driving car that turns into Waymo?
*  Do you think this is almost like what it takes
*  to build a successful robotics company?
*  Do you think it's possible to go from the ground up
*  or is it just too much capital investment?
*  Yeah, so it's very hard to get there
*  without a lot of capital.
*  And we're starting to see, you know,
*  fair chunks of capital for some robotics companies.
*  You know, Series Bs, I just saw one yesterday
*  for $80 million, I think it was, for Covariant.
*  But it can take real money to get into these things.
*  And you may fail along the way.
*  I certainly failed at Rethink Robotics.
*  And we lost $150 million in capital there.
*  Okay, so Rethink Robotics is another amazing robotics
*  company you co-founded.
*  So what was the vision there?
*  What was the dream?
*  And what are you most proud of with Rethink Robotics?
*  I'm most proud of the fact that we got robots
*  out of the cage in factories that was safe.
*  Absolutely safe for people and robots
*  to be next to each other.
*  So these are robotic arms.
*  Robotics arms for the factory.
*  They're able to pick up stuff and interact with humans.
*  Yeah, and that humans could retask them
*  without writing code.
*  Right.
*  And now that's sort of become an expectation
*  for a lot of other little companies
*  and big companies are advertising they're doing.
*  That's both an interface problem and also a safety problem.
*  Yeah, yeah.
*  So I'm most proud of that.
*  I completely, I let myself be talked out of what I wanted to do.
*  And you know, you've always got, you know,
*  I can't replay the tape.
*  You know, I can't replay it.
*  Maybe, maybe, you know, if I'd been stronger on,
*  and I remember the day, I remember the exact meeting.
*  Can you take me through that meeting?
*  Yeah.
*  So I'd said that I'd set as a target for the company
*  that we were going to build $3,000 robots with force feedback
*  that were safe for people to be around.
*  Wow.
*  That was my goal.
*  And we built, so we started in 2008,
*  and we had prototypes built of plastic, plastic gearboxes.
*  And at a $3,000, you know, lifetime, or $3,000,
*  I was saying we're going to go after not the people
*  who already have robot arms in factories,
*  the people who would never have a robot arm.
*  We're going to go after a different market.
*  So we don't have to meet their expectations.
*  And so we're going to build it out of plastic.
*  It doesn't have to have a $35,000 lifetime.
*  It's going to be so cheap that it's OPEX, not CAPEX.
*  And so we had a prototype that worked reasonably well,
*  but the control engineers were complaining
*  about these plastic gearboxes,
*  the beautiful little planetary gearbox,
*  but we could use something called serious elastic actuators.
*  We embedded them in there.
*  We could measure forces.
*  We knew when we hit something, et cetera.
*  The control engineers were saying,
*  yeah, but this is torque ripple
*  because these plastic gears, they're not great gears.
*  And there's this ripple, and trying to do force control
*  around this ripple is so hard.
*  And I'm not going to name names,
*  but I remember one of the mechanical engineers saying,
*  we'll just build a metal gearbox with spur gears,
*  and it'll take six weeks.
*  We'll be done. Problem solved.
*  Two years later, we got the spur gearbox working.
*  We cost-reduced it every possible way we could.
*  But now the price went up to, and then the CEO at the time said,
*  well, we have to have two arms, not one arm.
*  So our first robot product, Baxter, now cost $25,000.
*  And the only people who were going to look at that
*  were people who had arms in factories
*  because that was somewhat cheaper for two arms
*  than arms in factories.
*  But they were used to 0.1-millimeter reproducibility of motion
*  and certain velocities.
*  And I kept thinking, but that's not what we're giving you.
*  You don't need position repeatability.
*  You use force control like a human does.
*  No, but we want that repeatability.
*  We want that repeatability.
*  All the other robots have that repeatability.
*  Why don't you have that repeatability?
*  So can you clarify, force control is you can grab the arm,
*  and you can move it?
*  Yeah, well, you can move it around.
*  But suppose you... Can you see that?
*  Yes.
*  Suppose you want to...
*  Yes.
*  Suppose this thing is a precise thing that's got to fit here
*  in this right angle.
*  Under position control, you have fixtured where this is.
*  You know where this is precisely, and you just move it.
*  And it goes there.
*  In force control, you would do something like
*  slide it over here until we feel that, and slide it in there.
*  And that's how a human gets precision.
*  They use force feedback and get the things to mate
*  rather than just go straight to it.
*  Couldn't convince our customers who are in factories
*  and were used to thinking about things a certain way.
*  And they wondered, so then we said,
*  okay, we're going to build an arm that gives you that.
*  So now we ended up building a $35,000 robot with one arm with...
*  Oh, what are they called?
*  A certain sort of gearbox made by a company whose name
*  I can't remember right now, but it's the name of the gearbox.
*  But it's got torque ripple in it.
*  So now there was an extra two years of solving the problem
*  of doing the force with the torque ripple.
*  So we had to do the thing we had avoided for the plastic gearboxes.
*  We ended up having to do the brake system,
*  and for the plastic gearboxes, we ended up having to do...
*  The robot was now overpriced.
*  And that was your intuition from the very beginning, kind of,
*  that this is not...
*  You're opening a door to solve a lot of problems.
*  You're eventually going to have to solve this problem anyway.
*  Yeah, and also I was aiming at a low price to go into a different market.
*  A low price.
*  $3,000 would be amazing.
*  Yeah, I think we could have done it for five.
*  But you talked about setting the goal a little too far for the engineers.
*  Yeah, exactly.
*  So why would you say that company not failed, but went under?
*  We had buyers, and there's this thing called the Committee on Foreign Investment in the US,
*  CFIUS, and that had previously been invoked twice around where the government could stop
*  foreign money coming into a US company based on defense requirements.
*  We went through judge diligence multiple times.
*  We were going to get acquired, but every consortium had Chinese money in it,
*  and all the bankers would say at the last minute, you know, this isn't going to get past CFIUS,
*  and the investors would go away.
*  And then we had two buyers, once we were about to run out of money, two buyers,
*  and one used heavy-handed legal stuff with the other one, said they were going to take it and pay more,
*  dropped out when we were out of cash, and then bought the assets at one-thirtieth of the price
*  they had offered a week before.
*  It was a tough week.
*  Does it hurt to think about an amazing company that didn't, like iRobot, didn't find a way?
*  Yeah, it was tough. I said I was never going to start another company.
*  I was pleased that everyone liked what we did so much, that the team was hired by
*  three companies within a week. Everyone had a job in one of these three companies.
*  Some stayed in their same desks because another company came in and rented the space.
*  So I felt good about people not being out on the street.
*  So Backstress is a screen with a face.
*  That's a revolutionary idea for a robotic arm.
*  How much opposition did you get?
*  Well, first, the screen was also used during codeless programming,
*  where you taught by demonstration, it showed you what its understanding of the task was.
*  So it had two roles.
*  Some customers hated it, and so we made it so that when the robot was running,
*  it could be showing graphs of what was happening and not show the eyes.
*  Other people, and some of them surprised me, who they were, were saying,
*  this one doesn't look as human as the old one. We like the human looking.
*  So there was a mixed bag.
*  I'm kind of disappointed whenever I talk to roboticists,
*  the best robotics people in the world, they seem to not want to do the eyes type of thing.
*  They seem to see it as a machine, as opposed to a machine that can also have a human connection.
*  I'm not sure what to do with that. It seems like a lost opportunity.
*  I think the trillion dollar company will have to do the human connection very well, no matter what it does.
*  Yeah, I agree.
*  Can I ask you a ridiculous question?
*  Sure.
*  I'm not giving a ridiculous answer.
*  Do you think, well, maybe by way of asking the question, let me first mention that
*  you're kind of critical of the idea of the Turing test as a test of intelligence.
*  Let me first ask this question.
*  Do you think we'll be able to build an AI system that humans fall in love with
*  and it falls in love with the human, like romantic love?
*  Well, we've had that with humans falling in love with cars, even back in the 50s.
*  It's a different love, right?
*  Well, I think there's a lifelong partnership where you can communicate and grow
*  I think we're a long way from that. I think we're a long way.
*  I think Blade Runner had the time scale totally wrong.
*  Yeah. To me, honestly, the most difficult part is the thing you said with the Marv X Paradox
*  is to create a human form that interacts and perceives the world.
*  But if we just look at a voice, like the movie Herb,
*  I tend to think we're not that far away.
*  Well, for some people, maybe not.
*  But as humans, as we think about the future, we always try to,
*  and this is the premise of most science fiction movies,
*  you've got the world just as it is today and you can't just go to the movies
*  and you can't just go to the movies and you can't just go to the movies.
*  But that's not how, and it's the same with the self-driving car.
*  You change one thing.
*  No, everything changes. Everything grows together.
*  So surprisingly, it might be surprising to you or it might not,
*  I think the best movie about this stuff was Bicentennial Man.
*  And what was happening there?
*  It was Schmaltzy and, you know, the movie was called The Man of the Moon.
*  And what was happening there?
*  It was Schmaltzy and, you know, but what was happening there?
*  As the robot was trying to become more human,
*  the humans were adopting the technology of the robot and changing their bodies.
*  So there was a convergence happening in a sense.
*  So we will not be the same.
*  You know, we're already talking about genetically modifying our babies.
*  You know, there's more and more stuff happening around that.
*  We will want to modify ourselves even more for all sorts of things.
*  We put all sorts of technology in our bodies to improve it.
*  You know, I've got things in my ear so that I can sort of hear you.
*  Yeah.
*  So we're always modifying our bodies.
*  So, you know, I think it's hard to imagine exactly what it will be like in the future.
*  But on the touring test side, do you think...
*  So forget about love for a second.
*  Let's talk about just like the Alexa Prize.
*  Actually, I was invited to be a...
*  What is it?
*  An interviewer for the Alexa Prize or whatever that's in two days.
*  Their idea is success looks like a person wanting to talk to an AI system
*  for a prolonged period of time, like 20 minutes.
*  How far away are we?
*  And why is it difficult to build an AI system with which you'd want to have a beer
*  and talk for an hour or two hours?
*  Like, not for to check the weather or to check music, but just like to talk as friends.
*  Yeah, well, you know, we saw Weissenbaum back in the 60s with his program Eliza
*  being shocked at how much people would talk to Eliza.
*  I remember, you know, in the 70s, typing, you know, stuff to Eliza to see what it would come back with.
*  You know, I think right now, and this is a thing that Amazon's been trying to improve with Alexa.
*  There is no continuity of topic.
*  There's not...
*  You can't refer to what we talked about yesterday.
*  It's not the same as talking to a person where there seems to be an ongoing existence, which changes.
*  We share moments together and they last in our memory together.
*  Yeah, but there's none of that.
*  And there's no sort of intention of these systems that they have any goal in life,
*  even if it's to be happy, you know, they don't even have a semblance of that.
*  Now, I'm not saying this can't be done.
*  I'm just saying I think this is why we don't feel that way about them.
*  That's a sort of a minimal requirement.
*  If you want the sort of interaction you're talking about, it's a minimal requirement.
*  Whether it's going to be sufficient, I don't know.
*  We haven't seen it yet.
*  We don't know what it feels like.
*  I tend to think it's not as difficult as solving intelligence, for example.
*  And I think it's achievable in the near term.
*  But on the Turing test, why don't you think the Turing test is a good test of intelligence?
*  Oh, because, you know, again, the Turing, if you read the paper, Turing wasn't saying this is a good test.
*  He was using it as a rhetorical device to argue that if you can't tell the difference between a computer and a person,
*  you must say that the computer's thinking because you can't tell the difference when it's thinking.
*  You can't say something different.
*  What it has become is this sort of weird game of fooling people.
*  So back at the AI lab in the late 80s, we had this thing that still goes on called the AI Olympics.
*  And one of the events we had one year was the original imitation game as Turing talked about,
*  because he starts by saying, can you tell whether it's a man or a woman?
*  So we did that at the lab.
*  We had, you know, you'd go and type and the thing would come back and you had to tell whether it was a man or a woman.
*  And one man came up with a question that he could ask, which was always a dead giveaway
*  of whether the other person was really a man or a woman.
*  He would ask them, did you have green plastic toy soldiers as a kid?
*  Yeah. What did you do with them?
*  And a woman trying to be a man would say, oh, I lined them up.
*  We had wars, we had battles.
*  And the man just being an answer, I stomped on them.
*  I burned them.
*  So, you know, that's what the Turing test with computers has become.
*  What's the trick question?
*  That's why I say it sort of devolved into this weirdness.
*  Nevertheless, conversation not formulated as a test is a pretty fascinatingly challenging dance.
*  That's a really hard problem.
*  To me, conversation when non poses a test is a more intuitive illustration how far away we are from solving intelligence than computer vision.
*  It's hard.
*  Computer vision is harder for me to pull apart.
*  But with language, with conversation, you could see.
*  Because language is so human.
*  We can so clearly see it.
*  Shit, you mentioned something I was going to go off on.
*  OK.
*  I mean, I have to ask you because you were the head of CSAIL AI lab for a long time.
*  I don't know.
*  To me, when I came to MIT, you're like one of the greats at MIT.
*  So what was that time like?
*  And plus you were friends with, but you knew Minsky and all the folks there, all the legendary AI people of which you're one.
*  So what was that time like?
*  What are memories that stand out to you from that time?
*  From your time at MIT, from the AI lab, from the dreams that the AI lab represented to the actual revolutionary work?
*  Let me tell you first the disappointment in myself.
*  As I've been researching this book and so many of the players were active in the 50s and 60s, I knew many of them when they were older.
*  And I didn't ask them all the questions now I wish I had asked.
*  I'd sit with them at our Thursday lunches, which we had a faculty lunch, and I didn't ask them so many questions that now I wish I had.
*  Can I ask you that question?
*  Because you wrote that.
*  You wrote that you were fortunate to know and rub shoulders with many of the greats, those who founded AI robotics and computer science and the World Wide Web.
*  And you wrote that your big regret nowadays is that often I have questions for those who have passed on.
*  And I didn't think to ask them any of these questions, even as I saw them and said hello to them on a daily basis.
*  So maybe also another question I want to ask, if you could talk to them today, what question would you ask?
*  What questions would you ask?
*  Well, Rick Leiter, I would ask him, you know, he had the vision for humans and computers working together and he really founded that at DARPA.
*  And he gave the money to MIT, which started Project MAC in 1963.
*  And I would have talked to him about what the successes were, what the failures were, what he saw as progress, etc.
*  I would have asked him more questions about that because now I could use it in my book.
*  But I think it's lost. It's lost forever.
*  A lot of the motivations are lost.
*  I should have asked Marvin why he and Seymour Pappitt came down so hard on neural networks in 1968 in their book Perceptrons, because Marvin's PhD thesis was on neural networks.
*  How do you make sense of that?
*  That book destroyed the field.
*  He probably, do you think he knew the effect that book would have?
*  All the theorems and negative theorems.
*  Yeah.
*  Yeah.
*  So, yeah.
*  That's just the way of life.
*  Yeah.
*  But still, it's kind of tragic that he was both the proponent and the destroyer of neural networks.
*  Yeah.
*  Is there other memories stand out from the robotics and the AI work at MIT?
*  Well, yeah, but you have to be more specific.
*  Well, I mean, like it's such a magical place.
*  I mean, to me, it's a little bit also heartbreaking that, you know, with Google and Facebook, like DeepMind and so on, so much of the talent, you know, doesn't stay necessarily for prolonged periods of time in these universities.
*  Oh, yeah.
*  Yeah.
*  I mean, some of the companies are more guilty than others of paying fabulous salaries to some of the highest, you know, producers and then just, you never hear from them again.
*  They're not allowed to give public talks.
*  They're sort of locked away.
*  And it's sort of like collecting, you know, Hollywood stars or something and not allowed to make movies anymore.
*  I heard them.
*  Yeah.
*  That's tragic because I mean, there's an openness to the university setting where you do research to both in the space of ideas and space like publication, all those kinds of things.
*  Yeah, you know, and, you know, there's the publication and all that and often, you know, although these places say they publish.
*  There's pressure.
*  And but I think, for instance, you know, NetNet, I think Google buying those eight or nine robotics company was bad for the field because it locked those people away.
*  They didn't have to make the company succeed anymore.
*  Lock them away for years and then sort of all fretted away.
*  Yeah.
*  So do you have hope for MIT?
*  For MIT?
*  Yeah. Why shouldn't I?
*  Well, I could be harsh and say that I'm not sure I would say MIT is leading the world in AI or even Stanford or Berkeley.
*  I would say I would say deep mind, Google AI, Facebook AI.
*  I would take a slightly different approach, a different answer.
*  I'll come back to Facebook in a minute.
*  But I think there's other places are following a dream of one of the founders.
*  And I'm not sure that it's well founded, the dream.
*  And I'm not sure that it's going to have the impact that he believes it is.
*  You're talking about Facebook and Google and so on.
*  I'm talking about Google.
*  Google. But the thing is, those research labs aren't, there's the big dream.
*  And I'm usually a fan of no matter what the dream is, a big dream is a unifier.
*  Because what happens is you have a lot of bright minds working together on a dream.
*  What results is a lot of like adjacent ideas.
*  Yeah.
*  So much progress is made.
*  Yeah. So I'm not saying they're actually leading.
*  I'm not saying that the universities are leading.
*  But I don't think those companies are leading in general because they're, you know,
*  we saw this incredible spike in attendees at NeurIPS.
*  And as I said in my January 1st review this year for 2020,
*  2020 will not be remembered as a watershed year for machine learning or AI.
*  You know, there was nothing surprising happened anyway,
*  unlike when deep learning hit ImageNet.
*  That was a, that was a shake.
*  And there's a lot more people writing papers,
*  but the papers are fundamentally boring and uninteresting.
*  And incremental work.
*  Yeah.
*  Is there particular memories you have with Minsky or somebody else at MIT that stand out?
*  Funny stories.
*  I mean, unfortunately, he's another one that's passed away.
*  You've known some of the biggest minds in AI.
*  Yeah. And, you know, they did amazing things and sometimes they were grumpy.
*  Well, he was, he was interesting because he was very grumpy,
*  but that, that was, I remember him saying in an interview that the key to success
*  or being, to keep being productive is to hate everything you've ever done in the past.
*  Maybe that explains the Perceptron book.
*  There it was. He told you exactly what.
*  But he, meaning like, just like, I mean,
*  maybe that's the way to not treat yourself too seriously.
*  Just always be moving away from the world.
*  I mean, that's the idea.
*  I mean, that crankiness, I mean, there's a,
*  yeah, that's the character.
*  So let me, let me, let me tell you, you know, what really,
*  you know, the joy memories are about having access to technology before anyone else has seen it.
*  So, so, you know, I got to Stanford in 1977 and we had, you know,
*  we had terminals that could show live video on them.
*  Digital, digital sound system.
*  We had a Xerox graphics printer.
*  We could print, it wasn't, you know,
*  wasn't like a typewriter ball hitting in characters that you print arbitrary things.
*  So only in, you know, one bit, you know, black or white, but arbitrary pictures.
*  This was science fiction.
*  At MIT, the list machines, which, you know,
*  they were the first personal computers and, you know,
*  they cost $100,000 each and I could, you know,
*  I got there early enough in the day.
*  I got one for the day.
*  Couldn't, couldn't stand up.
*  Let's keep working.
*  So having that like direct glimpse into the future.
*  Yeah.
*  And, you know, I've had email every day since 1977.
*  And, you know, the, the host field was only eight bits, you know,
*  places, but we, I could send email to other people at a few places.
*  So that was, that was pretty exciting to be in that world.
*  So different from what the rest of the world knew.
*  And,
*  let me ask you,
*  I think you mentioned that you were a very, very, very,
*  very, very, very, very, very, very, very, very,
*  very, very good.
*  Let me ask you probably edit this out, but just in case you have a story,
*  I'm hanging out with Don Knuth for a while tomorrow.
*  Did you ever get a chance to such a different world than yours?
*  He's a very kind of theoretical computer science,
*  the puzzle of computer science, and mathematics,
*  and you're so much about the magic of robotics, like the practice of it.
*  Did you mention him earlier for like,
*  about computation. Did your worlds cross?
*  They did. I know him now, we talked.
*  But let me tell you my Donald Knuth story.
*  So besides analysis of algorithms,
*  he's well known for writing tech,
*  which is in LaTeX, which is the academic publishing system.
*  So he did that at the AI lab and he would work overnight at the AI lab.
*  One night, the mainframe computer went down.
*  A guy named Robert Paul was there.
*  He did his PhD at the Media Lab at MIT.
*  He was an engineer.
*  So he and I tracked down what the problem was.
*  It was one of this big refrigerator size or washing machine size disk drives had
*  failed and that's what brought the whole system down.
*  So we got panels pulled off and we're pulling circuit cards out.
*  Donald Knuth, who's a really tall guy,
*  walks in and he's looking down and says,
*  when will it be fixed?
*  Because he wanted to get back to writing his tech system.
*  We're like, it's Donald Knuth.
*  So we figured out it was a particular chip,
*  7400 series chip, which was socketed.
*  We popped it out,
*  we put a replacement in, put it back in,
*  smoke comes out because we put it in backwards because we were so
*  nervous that Donald Knuth was standing over us.
*  Anyway, we eventually got it fixed and got the mainframe running again.
*  So that was your little, when was that again?
*  Well, that must have been before October 79 because we moved out of that building then.
*  So probably 78, sometime early 79.
*  Yeah, all those figures are just fascinating.
*  All the people who have passed through MIT,
*  it's really fascinating.
*  Is there, let me ask you to put on your big wise man hat.
*  Is there advice that you can give to young people today,
*  whether in high school or college, who are thinking about their career,
*  who are thinking about life,
*  how to live a life they're proud of, a successful life?
*  Yeah, so many people ask me for advice and have asked for it.
*  I talk to a lot of people all the time.
*  And there is no one way.
*  You know, there's a lot of pressure to produce papers
*  that will be acceptable and be published.
*  Maybe I come from an age where I could be a rebel against that
*  and still succeed.
*  Maybe it's harder today.
*  But I think it's important not to get too caught up
*  with what everyone else is doing.
*  And if you, well, it depends on what you want of life.
*  If you want to have real impact, you have to be ready to fail a lot of times.
*  So you have to make a lot of unsafe decisions.
*  And the only way to make that work is to keep doing it for a long time.
*  And then one of them will be work out.
*  And so that will make something successful.
*  Or not.
*  Or you just may end up not having a lousy career.
*  I mean, it's certainly possible.
*  Taking the risk is the thing.
*  Yeah.
*  But there's no way to make all safe decisions and actually really contribute.
*  Do you think about your death, about your mortality?
*  I got to say when COVID hit, I did.
*  Because in the early days, we didn't know how bad it was going to be.
*  And that made me work on my book harder for a while.
*  And I'd started this company and now I'm doing more than full time at the company.
*  So the book's on hold.
*  But I do want to finish this book.
*  When you think about it, are you afraid of it?
*  I'm afraid of dribbling.
*  You know, of losing it.
*  The details of, OK.
*  Yeah.
*  But the fact that the ride ends.
*  I've known that for a long time.
*  So that's.
*  Yeah, but there's knowing and knowing.
*  It's such a.
*  Yeah, and it really sucks.
*  It feels it feels a lot closer.
*  So my in my my blog with my predictions, my sort of push back against that was I said,
*  I'm going to review these every year for 32 years.
*  And that puts me into my mid 90s.
*  So, you know, it's my.
*  That puts the whole every every time you write the blog post, you're getting closer
*  to your own prediction.
*  That's that's true.
*  Of your death.
*  Yeah.
*  Yeah. What do you hope your legacy is?
*  You're one of the greatest roboticists, researchers of all time.
*  What I hope is that I actually finish writing this book.
*  And that.
*  There was one person who reads it.
*  And see something about changing the way they're thinking.
*  And that leads to the next big.
*  And then they'll be on a podcast 100 years from now saying I once read that book
*  and that changed everything.
*  What do you think is the meaning of life?
*  This whole thing, the existence, the all the hurried things we do on this planet.
*  What do you think is the meaning of it all?
*  Well, you know, I think we're all really bad at it.
*  Life or finding meaning or both?
*  Yeah, we get caught up in in the it's easier to get easier to do the stuff
*  that's immediate and not through the stuff that's not immediate.
*  So the big picture or bad.
*  Yeah. Yeah.
*  Do you have a sense of what that big picture is?
*  Like, why ever look up to the stars and ask why the hell are we here?
*  You know, my my my my atheism tells me it's just random.
*  But, you know, I want to understand the way random in the
*  in what I talk about in this book, how order comes from disorder.
*  Yeah. But it kind of sprung up like most of the whole thing is random,
*  but this little pocket of complexity they will call Earth that like,
*  why the hell does that happen?
*  And what we don't know is how common that
*  those pockets of complexity are or how often
*  because they may not last forever.
*  Which is more exciting, sad to you if we're alone
*  or if there's infinite number of.
*  Oh, I think it's impossible for me to believe that we're alone.
*  That was just too horrible, too cruel.
*  Could be like the sad thing.
*  It could be like a graveyard of intelligent civilizations.
*  Oh, everywhere. Yeah.
*  That may be the most likely outcome.
*  And for us, too. Yeah, exactly.
*  Yeah. And all of this will be forgotten. Yeah.
*  Including all the robots you build.
*  Everything forgotten.
*  Well, on average, everyone has been forgotten in history.
*  Yeah. Right. Yeah.
*  Most people are not remembered beyond the generation or two.
*  I mean, yeah, not just on average, basically.
*  Very close to 100 percent of people who have ever lived are forgotten.
*  Yeah. I mean, no long arc.
*  I don't know anyone alive who remembers my great grandparents
*  because we didn't meet them. So.
*  Still, this fun.
*  This this life is pretty fun somehow. Yeah.
*  Even the immense absurdity and at times,
*  meaninglessness of it all is pretty fun.
*  And one of the for me, one of the most fun things is robots.
*  And I've looked up to your work.
*  I've looked up to you for a long time.
*  That's right. Rod.
*  It's an honor that you would spend your valuable time with me today
*  talking. It was an amazing conversation.
*  Thank you so much for being here.
*  Well, thanks for thanks for talking with me. I enjoyed it.
*  Thanks for listening to this conversation with Rodney Brooks.
*  To support this podcast, please check out our sponsors in the description.
*  And now let me leave you with the three laws of robotics from Isaac Asimov.
*  One, a robot may not injure a human being or through inaction,
*  allow a human being to come to harm.
*  Two, a robot must obey the orders given to it by human beings,
*  except when such orders would conflict with the first law.
*  And three, a robot must protect its own existence
*  as long as such protection does not conflict with the first or the second laws.
*  Thank you for listening.
*  I hope to see you next time.
