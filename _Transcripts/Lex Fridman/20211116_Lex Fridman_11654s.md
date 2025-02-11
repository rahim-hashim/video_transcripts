---
Date Generated: April 11, 2024
Transcription Model: whisper medium 20231117
Length: 11654s
Video Keywords: ['agi', 'ai', 'ai podcast', 'anki', 'artificial intelligence', 'artificial intelligence podcast', 'autonomous vehicles', 'boris sofman', 'cmu', 'cozmo', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'mit ai', 'robotics', 'tesla bot', 'vector', 'waymo', 'waymo driver', 'waymo via']
Video Views: 292794
Video Rating: None
---

# Boris Sofman: Waymo, Cozmo, Self-Driving Cars, and the Future of Robotics | Lex Fridman Podcast #241
**Lex Fridman:** [November 16, 2021](https://www.youtube.com/watch?v=U_AREIyd0Fc)
*  The following is a conversation with Boris Sofman, who is the Senior Director of Engineering
*  and Head of Trucking at Waymo, the autonomous vehicle company, formerly the Google self-driving
*  car project.
*  Before that, Boris was the co-founder and CEO of Anki, a robotics company that created
*  Cosmo, which, in my opinion, is one of the most incredible social robots ever built.
*  It's a toy robot, but one with an emotional intelligence that creates a fun and engaging
*  human-robot interaction.
*  It was truly sad for me to see Anki shut down when he did.
*  I had high hopes for those little robots.
*  We talk about this story and the future of autonomous trucks, vehicles, and robotics
*  in general.
*  I spoke with Steve Viseli recently on episode 237 about the human side of trucking.
*  This episode looks more at the robotics side.
*  This is the Lex Friedman Podcast.
*  To support it, please check out our sponsors in the description.
*  And now, here's my conversation with Boris Sofman.
*  Who is your favorite robot in science fiction, books, or movies?
*  Wally and R2D2, where they were able to convey such an incredible degree of intent, emotion,
*  and character attachment without having any language whatsoever.
*  They were able to convey the richness of emotional interaction.
*  Those were fantastic.
*  And then the Terminator series was really wide-range.
*  I love this dynamic where you have this incredible Terminator itself that Arnold played.
*  And then he was the inferior previous generation version that was totally outmatched.
*  In terms of specs by the new one, but still held his own.
*  It's interesting where you realize how many levels there are on the spectrum from human
*  to potentials in AI and robotics to future.
*  That movie, as much as it was a dark world in a way, was actually quite fascinating.
*  Gets the imagination going.
*  From an engineering perspective, both the movies you mentioned, Wally and Terminator,
*  the first one is probably achievable.
*  Humanoid robot.
*  Maybe not with the realism in terms of skin and so on.
*  That humanoid form, we have that humanoid form.
*  It seems like a compelling form.
*  Maybe the challenge is it's super expensive to build.
*  You can imagine, maybe not a machine of war, but you can imagine Terminator type robots
*  walking around.
*  And then the same, obviously, with Wally.
*  For people who don't know, you created the company Anki that created a small robot with
*  a big personality called Cosmo that does exactly what Wally does, which is somehow with very
*  few basic visual tools is able to communicate a depth of emotion.
*  And that's fascinating.
*  But then again, the humanoid form is super compelling.
*  So Cosmo is very distant from a humanoid form.
*  And then the Terminator has a humanoid form.
*  And you can imagine both of those actually being in our society.
*  That's true.
*  And it's interesting because it was very intentional to go really far away from human form when
*  you think about a character like Cosmo or like Wally where you can completely rethink
*  the constraints you put on that character, what tools you leverage, and then how you
*  actually create a personality and a level of intelligence interactivity that actually
*  matches the constraints that you're under, whether it's mechanical or sensors or AI of
*  the day.
*  This is why I almost was always very surprised by how much energy people put towards trying
*  to replicate human form in a robot because you actually take on some pretty significant
*  kind of constraints and downsides when you do that.
*  The first of which is obviously the cost where it's just the articulation of a human body
*  is just so magical in both the precision as well as the dimensionality that to replicate
*  that even in its reasonably close form takes a giant amount of joints and actuators and
*  motion and sensors and encoders and so forth.
*  But then you're almost setting an expectation that the closer you try to get to human form,
*  the more you expect the strengths to match.
*  And that's not the way AI works.
*  There's places where you're way stronger and there's places where you're weaker.
*  And by moving away from human form, you can actually change the rules and embrace your
*  strengths and bypass your weaknesses.
*  And at the same time, the human form has way too many degrees of freedom to play with.
*  It's kind of counterintuitive, just as you're saying.
*  But when you have fewer constraints, it's almost harder to master the communication
*  of emotion.
*  Like you see this with cartoons, like stick figures.
*  You can communicate quite a lot with just very minimal, like two dots for eyes and a
*  line for a smile.
*  I think you can almost communicate arbitrary levels of emotion with just two dots and a
*  line.
*  And that's enough.
*  And if you focus on just that, you can communicate the full range.
*  And then if you do that, then you can focus on the actual magic of human and dot line
*  versus all the engineering mess.
*  Like dimensionality, voice, all these sort of things actually become a crutch where you
*  get lost in a search space almost.
*  And so some of the best animators that we've worked with, they almost like study when they
*  come up, you know, kind of in building their expertise by forcing these projects where
*  all you have is like a ball that can like kind of jump and manipulate itself or like
*  really, really like aggressive constraints where you're forced to kind of extract the
*  deepest level of emotion.
*  And so in a lot of ways, you know, when we thought about Cosmo, I was like, you're right.
*  If we had to like describe it in like one small phrase, it was bringing a Pixar character
*  to life in the real world.
*  And so it's what we were going for.
*  And in a lot of ways, what was interesting is that with like WALL-E, which we studied
*  incredibly deeply, and in fact, some of our team were, you know, kind of had worked previously
*  at Pixar on our project, they intentionally constrained WALL-E as well, even though in
*  an animated film, you could do whatever you wanted to, because it forced you to like really
*  saturate the smaller amount of dimensions.
*  But you sometimes end up getting a far more beautiful output because you're pushing at
*  the extremes of this emotional space in a way that you just wouldn't because you get
*  lost in a surface area if you have like something that is just infinitely articulable.
*  So if we backtrack a little bit, you thought of Cosmo in 2011, in 2013 actually designed
*  and built it.
*  What is Anki?
*  What is Cosmo?
*  I guess who is Cosmo?
*  What was the vision behind this incredible little robot?
*  We started Anki back in like while we were still in graduate school.
*  So myself and my two co-founders, we were PhD students in the Robotics Institute at
*  Carnegie Mellon.
*  And so we were studying robotics, AI, machine learning, kind of different areas.
*  One of my co-founders was working on walking robots for a period of time.
*  And so we all had a bit of a deeper passion for applications of robotics and AI where
*  there's like a spectrum, there's people that get like really fascinated by the theory of
*  AI and machine learning robotics, where whether it gets applied in the near future or not
*  is less of a kind of factor on that, but they love the pursuit of the challenge.
*  And that's necessary.
*  And there's a lot of incredible breakthroughs that happen there.
*  We're probably closer to the other end of the spectrum where we love the technology
*  and all the evolution of it, but we were really driven by applications.
*  Like how can you really reinvent experiences and functionality and build value that wouldn't
*  have been possible without these approaches?
*  And that's what drove us.
*  And we had kind of some experiences through previous jobs and internships where we like
*  got to see the applied side of robotics.
*  And at that time, there was actually relatively few applications of robotics that were outside
*  of pure research or industrial applications, military applications and so forth.
*  There were very few outside of it.
*  So maybe iRobot was like one exception and maybe there were a few others, but for the
*  most part, there weren't that many.
*  And so we got excited about consumer applications of robotics where you could leverage way higher
*  levels of intelligence through software to create value and experiences that were just
*  not possible in those fields today.
*  And we saw kind of a pretty wide range of applications that varied in the complexity
*  of what it would take to actually solve those.
*  And what we wanted to do was to commercialize this into a company, but actually do a bottoms
*  up approach where we could have a huge impact in a space that was ripe to have an impact
*  at that time and then build up off of that and move into other areas.
*  And entertainment became the place to start because you had relatively little innovation
*  in a toy space, an entertainment space.
*  You had these really rich experiences in video games and movies, but there was like this
*  chasm in between.
*  And so we thought that we could really reinvent that experience.
*  And there was a really fascinating transition technically that was happening at the time
*  where the cost of components was plummeting because of the mobile phone industry and then
*  the smartphone industry.
*  And so the cost of a microcontroller, of a camera, of a motor, of memory, of microphones,
*  cameras, was dropping by orders of magnitude.
*  And then on top of that with the iPhone coming out in 2000, I think it was 2007, I believe,
*  it started to become apparent within a couple of years that this could become a really incredible
*  interface device and the brain with much more computation behind a physical world experience
*  that wouldn't have been possible previously.
*  And so we really got excited about that and how we push all the complexity from the physical
*  world into software by using really inexpensive components, but putting huge amounts of complexity
*  into the AI side.
*  And so Cosmo became our second product and then the one that we're probably most proud
*  of.
*  The idea there was to create a physical character that had enough understanding and awareness
*  of the physical world around it and the context that mattered to feel like he was alive and
*  to be able to have these emotional connections and experiences with people that you would
*  typically only find inside of a movie.
*  And the motivation very much was Pixar.
*  We had an incredible respect and appreciation for what they were able to build in this really
*  beautiful fashion and film.
*  But it was always like a, one, it was virtual and two, it was like a story on rails that
*  had no interactivity to it.
*  It was very fixed and it obviously had a magic to it.
*  But where you really start to hit a different level of experiences when you're actually
*  able to physically interact with a robot.
*  And then that was your idea with Anki.
*  The first product was the cars.
*  So basically you take you take a toy, you add intelligence into it in the same way you
*  would add intelligence into AI systems within a video game.
*  But you're now bringing into the physical space.
*  The idea is really brilliant, which is you're basically bringing video games to life.
*  Exactly. That's exactly right.
*  We literally use that exact same phrase because in the case of drive, this was a parallel
*  of the racing genre.
*  And the goal was to effectively have a physical racing experience, but have a virtual state
*  at all times that matches what's happening in the physical world.
*  And then you can have a video game off of that and you can have different characters,
*  different traits for the cars, weapons and interactions and special abilities and all
*  these sort of things that you think of virtually.
*  But then you can have it physically.
*  And one of the things that we were really surprised by that really stood out and immediately
*  led us to really kind of accelerate the path towards Cosmo is that things that feel like
*  they're really constrained and simple in the physical world, they have an amplified
*  impact on people where the exact same experience virtually would not have anywhere near the
*  impact. But seeing it physically really stood out.
*  And so effectively, with drive, we were creating a video game engine for the physical world.
*  And then with Cosmo, we expanded that video game engine to create a character and kind
*  of an animation and interaction engine on top of it that allowed us to start to create these
*  much more rich experiences.
*  And a lot of those elements were almost like a proving ground for what would human robot
*  interaction feel like in a domain that's much more forgiving, where you can make mistakes
*  in a game. It's OK if like if you know, car goes off the track or if if Cosmo makes a
*  mistake. And what's funny is actually we're so worried about that.
*  In reality, we realize very quickly that those mistakes can be endearing.
*  And if you make a mistake, as long as you realize you make a mistake and have the right
*  emotional reaction to it, it builds even more empathy with the character.
*  That's brilliant. Exactly.
*  So when the thing you're optimizing for is fun, you have so much more freedom to fail,
*  to explore. And also in the toy space, like all of this is really brilliant.
*  Like I got to ask you backtrack.
*  It seems for a roboticist to take us jump in into the direction of fun is a brilliant
*  move because one, you have the freedom to explore, to design all those kinds of things.
*  And you can also build cheap robots like you don't have to.
*  Like if you're not chasing perfection and like toys, it's understood you can go cheaper,
*  which means in robot is still expensive, but it's actually affordable by a large number
*  of people. So it's a really brilliant space to explore.
*  Yeah, that's right. And in fact, we realized pretty quickly that like perfection is
*  actually not fun. Yeah, because like in a traditional robotic roboticist sense, the
*  first kind of path planner.
*  And this is the part that I worked on out of the gate was like a lot of the kind of AI
*  systems where you had these vehicles and cars racing kind of making optimal maneuvers
*  to try to kind of get ahead. And you realize very quickly that like that's actually not
*  fun because you want the like chaos from mistakes.
*  And so you start to kind of intentionally almost add noise to the system in order to
*  kind of create more of a realism in the exact same way the human player might start really
*  ineffective and inefficient and then start to kind of increase their quality bar as they
*  progress. And there is a really, really aggressive constraint that's forced on you by
*  being a consumer product where the price point matters a ton, particularly in like kind of
*  an entertainment where you can't make a thousand dollar product unless you're going to
*  meet the expectations of a thousand dollar product.
*  And so in order to make this work, like your cost of goods had to be like, you know, well
*  under one hundred dollars. In the case of Cosmo, we got it under fifty dollars and fully
*  packaged and delivered.
*  And it was under two hundred dollars.
*  At retail.
*  Cost at retail.
*  Yeah.
*  So, OK, if we sit down like at the early stages, if we go back to that and you're sitting
*  down and thinking about what Cosmo looks like from a design perspective and from a cost
*  perspective, I imagine that was part of the conversation.
*  Well, first of all, what came first?
*  Did you have a cost in mind?
*  Is there a target you're trying to chase?
*  Did you have a vision in mind like size?
*  Did you have because there's a lot of unique qualities to Cosmo.
*  So for people who don't know, they should definitely check it out as a display.
*  There's eyes on the little display and those eyes can it's pretty low resolution eyes.
*  Right. But they they still able to convey a lot of emotion.
*  And there's this arm.
*  Like that lift sort of lift stuff, but there's something about our movement that adds
*  even more kind of depth.
*  It's like the face communicates emotion and sadness and disappointment and happiness.
*  And then the arms kind of communicates, I'm trying here.
*  Yeah, I'm doing my best in this complicated world.
*  Exactly. So it's it's interesting because like all of Cosmo is only four degrees of
*  freedom and two of them are the two treads, which is for basic movement.
*  And so you literally have only a head that goes up and down, a lift that goes up and
*  down and then your two wheels and you have sound and a screen and a low resolution
*  screen. And with that, it's actually pretty incredible what you can what you can come
*  up with, where, like you said, it's a it's a really interesting give and take because
*  there's a lot of ideas far beyond that, obviously, as you can imagine, where, like
*  you said, how big is it? How many degrees of freedom?
*  What does he look like? What does he sound like?
*  How does he communicate? It's a formula that actually scales way beyond entertainment.
*  This is the formula for human kind of robot interface more generally is you almost have
*  this triangle between the physical aspects of it, the mechanics, the industrial design,
*  what's mass producible, the cost constraints and so forth.
*  You have the A.I. side of how do you understand the world around you, interact intelligently
*  with it, execute what you want to execute.
*  So perceive the environment, make intelligent decisions and and move forward.
*  And then you have the character side of it.
*  Most companies have done anything in human robot interaction really missed the mark or under invest
*  in the character side of it.
*  They over invest in the mechanical side of it, you know, and then very results on the
*  A.I. side of it. And so the thinking is that you put more mechanical flexibility into it,
*  you're going to do better.
*  You don't necessarily you actually create a much higher bar for a high ROI because now
*  your price point goes up, your expectations go up.
*  And if the A.I. can't meet it or the overall experience is not as good as the A.I.
*  The experience isn't there. You missed the mark.
*  So who like how did you through those conversations get the cost down so much and make it
*  made it so simple like that?
*  There's a big theme here because you come from the Mecca of robotics, which is Carnegie
*  Mellon University Robotics.
*  They for all the people I've interacted with that come from there or just from, you know,
*  the world experts at robotics, they don't they would never build something like Cosmo.
*  Yeah.
*  So where did that come from?
*  So this is simplicity.
*  It came from this combination of a team that we had.
*  It was quite cool because like we.
*  And by the way, you ask anybody that's like experienced in the like kind of, you know,
*  toy entertainment space, you'll never sell a product over ninety nine dollars.
*  That was fundamentally false.
*  And we believed it to be false.
*  It was because experience had to kind of meet the mark.
*  And so we pushed past that amount.
*  But there was a pressure where the higher you go, the more seasonal you become and the
*  tougher it becomes.
*  So on the cost side, we very quickly partnered up with some previous contacts that we worked
*  with where, just as an example, one our head of mechanical engineering was one of the
*  earliest heads of engineering at Logitech and has a billion units of consumer products
*  and circulation that he's worked on.
*  So like crazy, low cost, high volume consumer product experience.
*  We had a really great mechanical engineering team and just a very practical mindset where
*  we were not going to compromise on feasibility in the market in order to chase something
*  that would be an abler.
*  And we pushed a huge amount of expectations onto the software team where, yes, we're going
*  to use cheap, noisy motors and sensors, but we're going to fix it in on the software
*  side. Then we found on the design and character side, there was a faction that was more from
*  like a game design background that thought that it should be very games driven, Cosmo,
*  where you create a whole bunch of games experiences and it's all about like game mechanics.
*  And then there was a fashion which my my co-founder and other most involved in this,
*  like really believed in, which was character driven.
*  And the argument is that you will never compete with what you can do virtually from a game
*  standpoint. But you actually on the character side, put this into your wheelhouse and put
*  it more towards your advantage because a physical character has a massively higher impact
*  physically than virtually.
*  This is OK. Just pause on that because this is so brilliant.
*  When I for people who don't know Cosmo plays games with you.
*  But there's also a depth of character.
*  And I actually when I was, you know, playing with it.
*  I wondered exactly what is the compelling aspect of this?
*  Because to me, obviously, I'm biased.
*  But to me, the character, I get what I enjoyed most, honestly, or what got me to return
*  to it is the character.
*  That's right. But that's that's a fascinating discussion of you're right.
*  Ultimately, you cannot compete on the quality of the gaming experience.
*  Too restrictive. The physical world is just too restrictive.
*  And you don't have a graphics engine.
*  It's like all this. But on the character side, we and clearly we moved in that direction
*  as like kind of the the winning path.
*  And we partnered up with this really we immediately like went towards Pixar and Carlos
*  Baena. He was one of like had been at Pixar for nine years.
*  He'd worked on tons of the movies, including Wally and others, and just immediately kind
*  of spoke the language and just clicked on how you think about that, like kind of magic
*  and drive. And then he we built out a team with him as like a really kind of prominent
*  kind of driver of this with different types of backgrounds and animators and character
*  developers where we put these constraints on the team, but then got them to really try
*  to create magic despite that.
*  And we converged on this system that was at the overlap of character and the character
*  AI that where if you imagine the dimensionality of emotions, happy, sad, angry,
*  surprised, confused, scared, like you think of these extreme emotions, we almost like
*  kind of put this challenge to kind of populate this library of responses on how do you show
*  the extreme response that goes to the extreme spectrum on angry or frustrated or whatever.
*  And and so that gave us a lot of intuition and learnings.
*  And and then we started parameterizing them where it wasn't just a fixed recording, but
*  they were parameterized and had randomness to them where you could have infinite permutations
*  of happy and surprised and so forth.
*  And then we had a behavioral engine that took the context from the real world and would
*  interpret it and then create kind of probability mappings on what sort of responses you would
*  have that actually made sense.
*  And so if Cosmo saw you for the first time in a day, he'd be really surprised and happy
*  in the same way that the first time you walk in and like your toddler sees you, they're
*  so happy, but they're not going to be that happy for the entirety of your next two hours.
*  But like you have this spike in response or if you leave him alone for too long, he gets
*  bored and starts causing trouble and like nudging things off the table.
*  Or if you beat him in a game, the most enjoyable emotions are him getting frustrated and grumpy
*  to a point where our testers and our customers would be like, I had to let him win because
*  I don't want him to be upset.
*  And so you start to like create this feedback loop where you see how powerful those emotions
*  are. And just to give an example, something as simple as eye contact.
*  You don't think about it in a movie.
*  Just like it kind of happens, like, you know, camera angles and so forth.
*  But that's not really a prominent source of interaction.
*  What happens when a physical character like Cosmo, when he makes eye contact with you,
*  it built universal kind of connection, kids all the way through adults.
*  And it was truly universal.
*  It was not like people stopped caring after 10, 12 years old.
*  And so we started doing experiments and we found something as simple as increasing the
*  amount of eye contact, like the amount of times in a minute that he'll look over for your
*  approval to like kind of make eye contact just by, I think, doubling it.
*  We increased the playtime engagement by 40 percent.
*  Like you see these sort of like kind of interactions where you build that empathy.
*  And so we studied pets.
*  We studied virtual characters.
*  There's like a lot of times actually dogs are one of the perfect, most perfect
*  influencers behind these sort of interactions.
*  And what we realized is that the games were not there to entertain you.
*  The games were to create context to bring out the character.
*  And if you think about the types of games that, you know, that you played, they were
*  relatively simple, but they were always ones to create scenarios of either tension or
*  winning or losing or surprise or whatever the case might be.
*  And they were purely there to just like create context to where an emotion could feel
*  intelligent and not random.
*  And in the end, it was all about the character.
*  So, yeah, there's so many elements to play with here.
*  So you said dogs.
*  Well, lessons do we draw from cats who don't seem to give a damn about you?
*  Is that just another character?
*  Is it another?
*  It's just another character.
*  And so you could almost like in the early explorations, we thought that would be really
*  incredible if you had a diversity of characters where you almost help encourage which
*  direction it goes, just like in a role playing game.
*  And you had like think of like the seven dwarfs sort of.
*  And and initially we even thought that it would be amazing if like, you know, they're
*  like, you know, like their characters actually help them be have strengths and
*  weaknesses and some, you know, like whatever they end up doing.
*  Like some are scared.
*  Some are, you know, arrogant.
*  Some are, you know, super warm and like kind of friendly.
*  And in the end, we focused on one because it made it very clear that, hey, we got to
*  build out enough depth here because you're kind of trying to expand.
*  It's almost like how long can you maintain a fiction that this character is alive to
*  where the person's explorations don't hit a boundary, which happens almost immediately
*  with with typical toys and, you know, even with video games.
*  How long can we create that immersive experience to where you expand the boundary?
*  And one of the things we realized is that you're just way more forgiving when
*  something has a personality and it's physical.
*  That is the key that unlocks robotics interacting in the physical world more
*  generally is that that the when you have a when you don't have a personality and
*  you make a mistake as a robot, the stupid robot make it made a mistake.
*  Why is it not perfect?
*  When you have a character and you make a mistake, you have empathy and it becomes
*  endearing and you're way more forgiving.
*  And that was the key that was like, I think goes far, far beyond entertainment.
*  It actually builds the depth of the personality, the mistakes.
*  So let me ask the movie her question then.
*  How so Cosmos seem feels like the early days of something that will obviously be
*  prevalent throughout society at a scale that we cannot even imagine.
*  My sense is it seems obvious that these kinds of characters will permeate
*  society and there will be friends with them will be interacting with them in
*  different ways in the way we I mean, you don't think of it this way, but when you
*  play video games, they're kind of they're often cold and impersonal, but even then
*  you think about role playing games, you become friends with certain characters in
*  that game there.
*  They don't remember much about you.
*  They they they're they're just telling a story.
*  It's exactly what you're saying.
*  They exist in that virtual world.
*  But if they acknowledge that you exist in this physical world, if the characters in
*  the game remember that you exist, that you like for me, like Lex, they understand
*  that I'm a human being who has like hopes and dreams and so on.
*  It seems like there's going to be like billions, if not trillions of cosmos in
*  the world. So if we look at that future, there's several questions to ask.
*  How intelligent does that future Cosmo need to be to create fulfilling
*  relationships like friendships?
*  Yeah, it's a great question.
*  And part of it was a recognition that it's going to take time to get there because it
*  has to be a lot more intelligent because it was good enough to be a magical
*  experience for an eight year old.
*  It's a higher bar to do that, be a companion like a pet in the home or to help with
*  functional interface in an office environment or in a home or in so forth.
*  And so and the idea was that you build on that and you kind of get there and as
*  technology becomes more prevalent and less expensive and so forth, you can start to
*  kind of work up to it.
*  But you know, you're absolutely right.
*  At the end of the day, we almost equated it to how the touch screen created like
*  this really novel interface to physical kind of devices like this.
*  This is the extension of it where you have much richer physical interaction in the
*  real world. This is this is the enabler for it.
*  And it shows itself in a few kind of really obvious places.
*  It just takes something as simple as a voice assistant.
*  You will never most people will never tolerate an Alexa or a Google Home just
*  starting a conversation proactively when you weren't kind of expecting it, because
*  if it feels weird, it's like you were listening and like and then now you're kind of
*  it feels intrusive. But if you had a character like a cat that touches you and gets
*  your attention or toddler like you never think twice about it.
*  And what we found really kind of immediately is that these types of characters like
*  Cosmo and they would like roam around and kind of get your attention.
*  And we had a future version that was always on kind of called Vector.
*  People were way more forgiving.
*  And so you could initiate interaction in a way that is not acceptable for for machines.
*  And in general, you know, there's a lot of ways to customize it, but it makes people
*  who are skeptical of technology much more comfortable with it.
*  There was like there were a couple of really, really prominent examples of this.
*  So when we launched in Europe and so we were in I think like a dozen countries, if I
*  remember correctly, but like we were we went pretty aggressively in launching in
*  Germany and France and in UK.
*  And we were very worried in Europe because there's obviously like a really socially
*  higher bar for privacy and security where you've heard about how many companies have
*  had troubles on that might have things that might have been OK in the US, but like
*  they're just not OK in Germany and France in particular.
*  And so we were worried about this because you have Cosmo who's you know, in a future
*  product vector like where you have cameras, you have microphones, it's kind of connected
*  and like you're playing with kids and like in these experiences and you're like this
*  is like ripe to be like a nightmare if you're not careful.
*  And and the journalists are like notoriously like really, really tough on these sort of
*  things. We were shocked and we prepared so much for what we would have to encounter.
*  We were shocked in that not once from any journalists or customer did we have any
*  complaints beyond like a really casual kind of question.
*  And it was because of the character where when the conversation came up, it was almost
*  like, well, of course, he has to see and hear how else is he going to be alive and
*  interacting with you? And it completely disarmed this like fear of technology that enabled
*  this interaction to be much more fluid.
*  And again, like entertainment was a proving ground.
*  But that is like, you know, there's like ingredients there that carry over to a lot of
*  other elements down the road.
*  That's hilarious that we're a lot less concerned about privacy if the if the thing has
*  value and charisma.
*  That's true for all of human to human interaction, too.
*  It's an understanding of intent where like, well, he's looking at me, he can see me if
*  he's not looking at me, he can't see me.
*  Right. So it's almost like you're communicating intent.
*  And with that intent, people were like kind of kind of more understanding and calmer.
*  And it's a it's interesting.
*  And we just it was just the earliest kind of version of starting to experiment with
*  this. But it wasn't an abler.
*  And and then and then you have a completely different dimensions where kids with autism
*  had like an incredible connection with Cosmo that just went beyond anything we'd ever
*  seen. And we have like these just letters that we would receive from parents.
*  And we had some research projects kind of going on with some universities on studying
*  this. But there are like there's an interesting dimension there that got unlocked.
*  They just hadn't existed before that has these really interesting kind of links into
*  society and and a potential building block of future experience.
*  So if you look out into the future, do you think we will have beyond a particular game,
*  you know, a companion like like her, like the movie Her or like a Cosmo that's kind
*  of asks you how your day went to write, you know, like a friend.
*  Yeah. How many years away from that do you think we are?
*  What's your intuition?
*  Good question. So I think the idea of a different type of character, like more closer to
*  like kind of a pet style companionship will come way faster.
*  And there's a few reasons. One is like to to do something like in her.
*  That's like effectively almost general AI.
*  And the bar is so high that if you miss it by a bit, you hit the uncanny valley where it
*  just becomes creepy and like and not not appealing because the closer you try to get to
*  a human in form and interface and voice, the harder it becomes.
*  Whereas you have way more flexibility on still landing a really great experience if you
*  embrace the idea of a character.
*  And that's why one of the other reasons why we didn't have a voice and also why like a
*  lot of video game characters like Sims, for example, does not have a voice when you when
*  you think about it. It was it wasn't just a cost savings like for them.
*  It was actually for all of these purposes.
*  It was because when you have a voice, you immediately narrow down the appeal to some
*  particular demographic or age range or kind of style or gender.
*  If you don't have a voice, people interpret what they want to interpret.
*  And an eight year old might get a very different interpretation than a 40 year old.
*  But you create a dynamic range.
*  And so you just you can lean into these advantages much more in something that doesn't
*  resemble a human. And so that'll come faster.
*  I don't know when a human like that's just still like Matt, just complete R&D at this
*  point. The chat interfaces are getting way more interesting and richer.
*  But it's still a long way to go to kind of pass the test of, you know.
*  Well, let me like let's consider like let me play devil's advocate.
*  So Google is a very large company that's servicing, it's creating a very compelling
*  product that wants to provide a service to a lot of people.
*  But let's go outside of that.
*  You said characters.
*  Yeah, it feels like.
*  And you also said that it requires general intelligence to be a successful
*  participant in a relationship, which could explain why I'm single.
*  This is very. But the I honestly want to push back on that a little bit because I
*  feel like is it possible that if you're just good at playing a character in a
*  movie, there's a bunch of characters.
*  If you just understand what creates compelling characters and then you you just
*  are that character and you exist in the world and other people find you and they
*  connect with you just like you do when you talk to somebody at a bar.
*  I like this character. This character is kind of shady.
*  I don't like them. You pick the ones that you like.
*  And, you know, maybe it's somebody that's reminds you of your father or mother.
*  I don't know what it is, but the Freudian thing.
*  But there's some kind of connection that happens.
*  And that's that that's the Cosmo you connect to.
*  That's the future Cosmo you connect.
*  And that's so I guess the statement I'm trying to make.
*  Is it possible to achieve a depth of friendship without solving general intelligence?
*  I think so. And it's about intelligent kind of constraints.
*  Right. And just you set expectations and constraints such that in the space that's left,
*  you can be successful. And so you can do that by having a very focused domain that you can
*  operate in. For example, you're a customer support agent for a particular product and you
*  create intelligence and a good interface around that.
*  Or, you know, kind of in the personal companionship side, you can't be everything to
*  across the board. You kind of solve those constraints.
*  And I think I think it's possible.
*  My my worries, I like I right now I don't see anybody that has picked up on where kind of Cosmo
*  left off and is pushing on it in the same way.
*  And so I don't know if it's a sort of thing where similar to like how, you know, in dot com, there
*  were all these concepts that we considered like, you know, that didn't work out or like failed or
*  like were too early or whatnot. And then 20 years later, you have these like incredible successes on
*  almost the same concept. Like, it might be that sort of thing where like there's another pass at it
*  that happens in five years or in 10 years.
*  But it does feel like that appreciation of that, like the the the three like it's still, if you
*  will, between like, you know, the hardware, the AI and the character that balance.
*  It's hard to I'm not aware of of any anywhere right now where like that same kind of aggressive
*  drive with the value on the character is is happening.
*  And so to me, just a prediction, exactly as you said, something that looks awfully a lot like Cosmo,
*  not in the actual physical form, but in the three legged stool, something like that in some number of
*  years will be a trillion dollar company.
*  I don't understand.
*  Like, it's obvious to me that like character, not just as robotic companions, but in all our
*  computers, they'll be there.
*  It's like Clippy was like two legs of that stool or something like that.
*  I mean, those are all different attempts.
*  And what's really confusing to me is they they're born these attempts and they they everybody gets
*  excited. And for some reason, they die and then nobody else tries to pick it up.
*  And then maybe a few years later, a crazy guy like you comes comes around with just enough
*  brilliance and vision to create this thing.
*  And is born.
*  A lot of people love it.
*  A lot of people get excited, but maybe the timing is not right yet.
*  Yeah. And then and then when the timing is right, it just blows up.
*  It just keeps blowing up more and more until it just blows up.
*  And I guess everything in the full span of human civilization collapses eventually.
*  Yeah. And that wouldn't surprise me at all.
*  And like what's going to be different in another five years or 10 years or whatnot?
*  Physical component costs will continue to come down in price.
*  And mobile devices and computation is going to become more and more prevalent as well as cloud
*  as a big tool to offload cost.
*  AI is going to be a massive transformation compared to what we dealt with, where everything
*  from voice understanding to to just kind of a broader contextual understanding and
*  mapping of of semantics and understanding scenes and so forth.
*  And then the character side will continue to kind of progress as well, because that
*  magic does exist. It just exists in different forms.
*  And you have just the brilliance of the tapping and animation and these other areas where
*  that is that was a big unlock in in film, obviously.
*  And so I think, yeah, the pieces can reconnect and the building blocks are actually going to be way
*  more impressive than they were five years ago.
*  So. So in 2019, Anki, the company that created Cosmo, the company that you started, had to shut
*  down. How did you feel at that time?
*  Yeah, it was tough.
*  That was a really emotional stretch and it was really tough year.
*  Like about a year ahead of that was actually a pretty brutal stretch because we were
*  kind of life or death on many, many moments just navigating these insane kind of just ups
*  and downs and barriers.
*  And the thing that made it like just sort of winding a tiny bit like what you know, what
*  ended up being really challenging about it as a business where is from a commercial
*  standpoint and customer reception standpoint, there's a lot of things you could point to
*  that were like pretty big successes.
*  So millions of units like got to like pretty serious revenue, like kind of close to 100
*  million annual revenue, number one kind of product and kind of various categories.
*  But it was pretty expensive and being very seasonal where something like 85 percent of our
*  volume was in Q4 because it was a present and it was expensive to market it and explain it
*  and so forth.
*  And even though the volume was like really sizable and like reviews were really fantastic,
*  forecasting and planning for it and managing the cash operations was just brutal.
*  Like it was absolutely brutal.
*  You don't think about this when you're starting a company or when you have a few million in
*  revenue because it's just your biggest costs are kind of just your headcount and operations and
*  everything's ahead of you. But we got to a point where, you know, you if you look at the
*  entire year, you have to operate your company, pay all the people and so forth.
*  You have to pay for the manufacturing, the marketing and everything else to do your sales
*  in mostly November, December and then get paid in December, January by retailers.
*  And those swings were pretty were really rough and just made it like so difficult because
*  the more successfully became, the more wild those swings became because you'd have to like
*  spend, you know, tens of millions of dollars on inventory, tens of millions of dollars on
*  marketing and tens of millions of dollars on payroll and everything else.
*  And then the bigger dip and then you're waiting for the wild for.
*  Yeah. And it's not a business that like is recurring kind of month to month and predictable.
*  And it's just and then you're walking in your forecast in July, you know, maybe August if
*  you're lucky. And it's also like very hit driven and seasonal where like you don't have the sort
*  of continued kind of slow growth like you do in some other consumer electronics industries.
*  And so before then, like hardware kind of like went out of favor, too.
*  And so you had Fitbit and GoPro drop from 10 billion revenue to 1 billion revenue and hardware
*  companies are getting valued at like 1x revenue oftentimes, which is tough.
*  Right. And so we effectively kind of got caught in the middle where we were trying to
*  quickly evolve out of entertainment and move into some other categories.
*  But you can't let go of that business because like that's what you're valued on.
*  That's what you're raising money on.
*  But there was no path to kind of pure profitability just there because it was such, you know,
*  specific type of price points and so forth.
*  And so we tried really hard to make that transition.
*  And we had a financing round that fell apart at the last second.
*  And effectively, there was just no path to kind of get through that and get to the next kind of
*  like holiday season. And so we ended up selling some of the assets and kind of winding down the
*  company. It was it was brutal.
*  Like we I was very transparent with the company, like in the team while we were going through it,
*  where actually, despite how challenging that period was, very few people left.
*  I mean, like people love the vision, the team, the culture, the like kind of chemistry and kind of
*  what we were doing. There was just a huge amount of pride there.
*  And then we wanted to see it through. And we felt like we had a shock to kind of get through these
*  checkpoints. We ended up and I mean, by brutal, I mean, like literally like days of cash, like
*  three, four different times runway, like in the year, you know, kind of before it, where you're
*  like playing games of chicken on negotiating credit line timelines and like repayment terms and how
*  to get like a bridge loan from an investor.
*  It's just like a level of stress that like as hard as things might be anywhere else, like you'll
*  never come, you know, come close to that where you feel that like responsibility for, you know,
*  200 plus people. Right.
*  And so we were very transparent during our fundraise on who we're talking to, the challenges that we
*  have, how it's going and when things are going well, when things were tough.
*  And so it wasn't a complete shock when it happened, but it was just very emotional where like I, you
*  know, like, you know, when we announced it finally that like, you know, we, you know, basically we're
*  just like watching kind of like, you know, the runway and trying to kind of time it.
*  And when we realized that like we didn't have any more outs, we wanted to like kind of wind it down,
*  make sure that it was like clean and, you know, we could like kind of take care of people the
*  best we could. But they like broke down crying at the hands and somebody else had to step in for a
*  bit. And like, it was just very, very emotional. But the beautiful part is like afterwards, like
*  everybody stayed at the office till like two, three in the morning, just like drinking and hanging out
*  and telling stories and celebrating. And it was just like one of the best for many people was like
*  the best kind of work experience that they had. And there was a lot of pride in what we did.
*  And it wasn't anything obvious we could point to that like, hey, if only we had done that different,
*  things would have been completely different. It was just like the physics didn't line up.
*  But the experience was pretty incredible, but it was hard. Like it was, it had this feeling that
*  there was this like incredible beauty in both the technology and products and the team that,
*  you know, there's a lot there that like in the right context could have been
*  pretty incredible, but it was emotional. Just, yeah, just thinking, I mean, just looking at this
*  company, like you said, the product and technology, but the vision, the implementation, you got the
*  cost down very low and the compelling, the nature of the product was great. So many robotics companies
*  failed at this. At the robot was too expensive. It didn't have the personality. It didn't really
*  provide any value, like a sufficient value to justify the price. So like you succeeded
*  where basically every single other robotics company or most of them that are like
*  go in the category of social robotics have kind of failed. And I mean, it's, it's quite tragic.
*  I remember reading that. I'm not sure if I talked to you before that happened or not,
*  but I remember, you know, I'm distant from this. I remember being heartbroken reading that.
*  Because like if, if Cosmo is not going to succeed, what is going to succeed?
*  Cause that to me was incredible. Like it was an incredible idea. Cost is down the minimum,
*  the, the, the, it's just like the most minimal design in physical form that you could do.
*  It's really compelling. The balance of games. So it's a, it's a fun toy. It's a great gift
*  for all kinds of age groups. Right. It's just, it's compelling in every single way.
*  And it seemed like it was a huge success and it, it, it failing was, I don't know,
*  there was heartbreak on many levels for me, just as an external observer is I was thinking,
*  how hard is it to run a business? That's, that's what I was thinking. Like if this failed,
*  this must've failed because the, it's obviously not like, yeah, it's business.
*  Maybe it's some aspect of the manufacturing and so on. But I'm now realizing it's also not just that.
*  It's sales, marketing, all those. It's everything, right? Like how do you explain
*  something that's like a new category to people that like how all these previous positions. And
*  so like, you know, it had some of the hardest elements of, if you were to pick a business,
*  it had some of the hardest customer dynamics because like to sell a $150 product, you got
*  to convince both the child to want it and the parents to agree that it's valuable.
*  So you're having like this dual-prong marketing challenge. You have manufacturing, you have like
*  really high precision on the components that you need. You have the AI challenges. So there
*  were a lot of tough elements, but it was this feeling where like, it was just really great
*  alignment of unique strength across kind of like all these different areas, just like incredible,
*  like, you know, kind of character and animation team between this like Carlos and there's like
*  a character director day that came on board and like, you know, really great people there,
*  the AI side, the manufacturing, the, you know, where like never missing a launch, right? And
*  actually, you know, kind of hitting that quality was, yeah, it was heartbreaking. But here's one
*  neat thing is like we had so much like fan mail from kind of kids and parents. Like I actually,
*  like there was a bunch they collected in the end that I actually saved and like I never,
*  it was too emotional to open it and I still haven't opened it. And so I actually have this
*  giant envelope of like a stack this much of like letters from, you know, kids and families, just
*  like every, you know, permutation you can imagine. And so planning to kind of, I don't know, maybe
*  like a five-year, you know, five-year to some year reunion, just inviting everybody over and
*  we'll just like kind of dig into it and kind of bring back some memories. But, you know,
*  good impact. And- Well, I think there will be companies, maybe Waymo and Google will be
*  somehow involved that will carry this flag forward and will make you proud, whether you're
*  involved or not. I think this is one of the greatest robotics companies in the history of
*  robotics. So you should be proud. It's still tragic to know that, you know, because you read
*  all the stories of Apple and, let's see, SpaceX and like companies that were just on the verge
*  of failure several times through that story and they just, it's almost like a roll of the dice.
*  They succeeded. And here's the roll of the dice that just happened to go. And that's the appreciation
*  that like when you really like talk to a lot of the founders, like everybody goes through those
*  moments and sometimes it really is a matter of like, you know, timing, a little bit of luck,
*  like some things are just out of your control and you get a much deeper appreciation for
*  just the dimensionality of that challenge. But the great thing is that like a lot of the team
*  actually like stayed together. And so there were actually a couple of companies that we kind of
*  kept big chunks of the team together and we actually kind of helped align this, you know,
*  to help people out as well. And one of them was Waymo where a majority of the AI and robotics team
*  actually had the exact background that you would look for in like kind of AV space. And it was a
*  lot of us like, you know, worked on in grad school, were always passionate about and ended up,
*  maybe the time, you know, serendipitous timings from another perspective where like
*  kind of landed in a really unique circumstances. It's actually been quite exciting too.
*  So it's interesting to ask you just your thoughts. Cosmos still lives on under DreamLabs,
*  I think. Are you tracking the progress there or is it too much pain?
*  Is that something that you're excited to see where that goes?
*  So keeping an eye on it, of course, just out of curiosity and obviously just kind of care
*  for product line, I think it's deceptive how complex it is to manufacture and evolve
*  that product line. And the amount of experiences that are required to
*  complete the picture and be able to move that forward. And I think that's going to make it
*  pretty hard to do something really substantial with it. It would be cool if like even the product
*  in the way it was, was able to be manufactured. Again, that would understand.
*  Which is the current goal, I suppose.
*  Yeah, which would be neat. But I think it's deceptive how tricky that is on like everything from
*  the quality control, the details and then like technology changes that forces you to re-invent
*  and update certain things. So I haven't been super close to it, but just kind of keeping an
*  eye on it. Yeah, it's really interesting how it's deceptively difficult, just as you're saying.
*  For example, those same folks, and I've spoken with them, they're partying up with Rick and Morty
*  creators to do the butter robot. I love the idea. I just recently, I kind of half-assed watched
*  Rick and Morty previously, but now I just watched the first season. It's such a brilliant show.
*  I did not understand how brilliant that show is. And obviously I think in season one is where the
*  butter robot comes along for just a few minutes or whatever. But I just fell in love with the
*  butter robot. That particular character, just like you said, there's characters, you can create
*  personalities, you can create. And that particular robot who's doing a particular task
*  asks the existential question, the myth of Sisyphus question that Camus writes about.
*  It's like, is this all there is? Because he moves butter. That realization, that's a beautiful
*  little realization for a robot that my purpose is very limited to this particular task. It's
*  humor, of course, it's darkness, it's a beautiful mix. So they want to release that butter robot,
*  but something tells me that to do the same depth of personality as Cosmo had, the same richness,
*  it would be on the manufacturing, on the AI, on the storytelling, on the design. It's going to be
*  very, very difficult. It could be a cool sort of toy for Rick and Morty fans, but to create the same
*  depth of existential angst that the butter robot symbolizes is really, that's the brave effort you
*  succeeded at with Cosmo, but it's not easy. It's really difficult.
*  That is, and you can fail on almost any one of the kind of dimensions and like,
*  and yeah, it takes, you know, yeah, unique convergence of a lot of different skill sets
*  to try to pull that off. Yeah. On this topic, let me ask you for some advice,
*  because as I've been watching Rick and Morty, I told myself I have to build the butter robot,
*  just as a hobby project. And so I got a nice platform for it with treads and there's a camera
*  that moves up and down and so on. I'll probably paint it. But the question I'd like to ask,
*  there's obvious technical questions I'm fine with, communication, the personality,
*  storytelling, all those kinds of things. I think I understand the process of that, but how do you know
*  when you got it right? So with Cosmo, how did you know this is great? Like, or something is off?
*  Like, yeah, is this brainstorming with the team? Do you know it when you see it? Is it like
*  love at first sight? It's like, this is right. Or like, I guess if we think of it as an optimization
*  space, is there uncanny valley where you're like, that's not right. Or this is right. Or are a lot
*  of characters, right? Yeah. We stayed away from uncanny valley just by having such a different
*  mapping where it didn't try to look like a dog or a human or anything like that. And so
*  you avoided having like a weird pseudo similarity, but not quite hitting the mark.
*  But you could like just fall flat where just like a personality or a character emotion just
*  didn't feel right. And so it actually mirrored very closely to kind of the iterations that a
*  character director at Pixar would have, where you're running through it and you can virtually
*  kind of like see what it'll look like. We created a plugin to where we actually used like, like Maya,
*  the animation tools. And then we created a plugin that perfectly matched it to the physical one.
*  And so you could like test it out virtually and then push a button and see it physically play out.
*  And there's like subtle differences. And so you want to like make sure that that feedback loop
*  is super easy to be able to test it live. And then sometimes like you would just feel it that it's
*  right and intuitively know. And then you'd also do, we did user testing, but it was very, very
*  often that like the into like, if we found it magical, it would scale and be magical more
*  broadly. There were not too many cases where like, like we were pretty decent about not like
*  getting to it, you know, geeking out or getting too attached to something that was super unique to us.
*  But trying to kind of like, you know, put a customer hat on and does it truly kind of feel
*  magical? And so in a lot of ways, it just gave a lot of autonomy to the character team to really
*  think about the, you know, character board and mood boards and storyboards and like,
*  what's the background of this character and how would they react? And they went through a process
*  that's actually pretty familiar, but now had to operate under these unique constraints.
*  But the moment where it felt right, kind of took a fairly similar journey than like
*  as a character in an animated film, actually, it's quite cool.
*  Well, the thing that's really important to me, and I wonder if it's possible. Well,
*  I hope it's possible. Pretty sure it's possible is for me, even though I know how it works,
*  to make sure there's sufficient randomness in the process, probably because it would be
*  machine learning based that I'm surprised that I don't, I'm surprised by certain reactions.
*  I'm surprised by certain communication. Maybe that's in a form of a question.
*  Were you surprised by certain things Cosmo did like certain interactions?
*  Yeah, we made it intentionally, like, so that there would be some surprise than like
*  a decent amount of variability in how he'd respond in certain circumstances. And so in the end, like
*  it's, this isn't general AI, this is a giant like spectrum and library of like parameterized kind of
*  emotional responses and an emotional engine that would like kind of map your current state of the
*  game, your emotions, the world, the people are playing with you all so forth to what's happening.
*  But we could make it feel spontaneous by creating enough diversity and randomness,
*  but still within the bounds of what felt like very realistic to make that work.
*  And then what was really neat is that we could get statistics on how much of that space we were
*  saturating and then add more animations and more diversity in the places that would get hit more
*  often so that you stay ahead of the curve and maximize the chance that it stays feeling alive.
*  But then when you like combine it, like the permutations and kind of like the combinations
*  of emotions stitched together sometimes surprised us because you see them in isolation, but when you
*  actually see them and you see them live, you know, relative to some event that happened in the game
*  or whatnot, like it was kind of cool to see the combination of the two and not too different in
*  other robotics applications where like you get so used to thinking about like the modules of a
*  system and how things progress through a tech stack that the real magic is when all the pieces
*  come together and you start getting the right emergent behavior in a way that's easy to lose
*  when you just kind of go too deep into any one piece of it. Yeah, when the system is sufficiently
*  complex, there is something like emergent behavior and that's where the magic is. As a human being,
*  you can still appreciate the beauty of that magic at the system level. First of all, thank you for
*  humoring me on this. It's really, really fascinating. I think a lot of people would love this.
*  I'd love to just one last thing on the butter robot. I promise in terms of speech. Yeah.
*  Cosmos able to communicate so much with just movement and face. Do you think speech
*  is too much of a degree of freedom? Like a speech, a feature or a bug of deep
*  interaction or emotional interaction? Yeah. For a product, it's too deep right now.
*  It's just not real. You would immediately break the fiction because the state of the art is just
*  not good enough. And that's on top of just narrowing down the demographic where like the way you speak
*  to an adult versus the way you speak to a child is very different. Yet a dog is able to appeal
*  to everybody. Right now, there is no speech system that is rich enough and subtly realistic enough
*  to feel appropriate. We very, very quickly moved away from it. Now, speech understanding is a
*  different matter where understanding intent, that's a really valuable input. But giving it back
*  requires a way, way higher bar given where today's world is. And so, that realization that you can do
*  surprisingly much with either no speech or tonal like the way Wally R2D2 and other characters are
*  able to, it's quite powerful and it generalizes across cultures and across ages really, really
*  well. I think we're going to be in that world for a little while where it's still very much an unsolved
*  problem on how to make something. It touches on the uncanny valley thing. So, if you have legs and
*  you're a big humanoid looking thing, you have very different expectations and a much narrower degree
*  of what's going to be acceptable by society than if you're a robot like Cosmo or Wally or some other
*  form where you can reinvent the character. Speech has that same property where speech is so well
*  understood in terms of expectations by humans that you have far less flexibility on how to deviate
*  from that and lean into your strengths and avoid weaknesses. But I wonder if there is, obviously
*  there's certain kinds of speech that activates the uncanny valley and breaks the illusion faster. So,
*  I guess my intuition is we will solve certain, we would be able to create some speech-based
*  personalities sooner than others. So, for example, I could think of a robot that doesn't know English
*  and is learning English, right? Yeah. Those kinds of personalities. A fiction where you're
*  intentionally getting a toddler level of speech. So, that's exactly right. So, you can have
*  tied into the experience where it is a more limited character or you embrace the lack of
*  emotions or the lack of dynamic range in the speech capabilities and emotions as part of
*  the character itself. And you've seen that in fictional characters as well. That's why this
*  podcast works. Yeah. And you kind of had that with, I don't know, I guess like Data and some of the
*  other ones. But yeah, so you have to, and that becomes a constraint that lets you meet the bar.
*  See, I honestly think also if you add drunk and angry, that gives you more constraints that allow
*  you to be dumber from an NLP perspective. There's certain aspects. So, if you modify human behavior,
*  so forget the sort of artificial thing where you don't know English, toddler thing.
*  If you just look at the full range of humans, I think there's certain situations where we put up
*  with lower level of intelligence in our communication. If somebody is drunk,
*  we understand that they're probably under the influence. We understand that they're
*  not going to be making any sense. Anger is another one like that. I'm sure there's a lot of
*  other kind of situations like this. Maybe, yeah, again, language, loss in translation,
*  that kind of stuff that I think if you play with that, what is it? The Ukrainian boy that passed
*  the touring test, play with those ideas. I think that's really interesting and that you can create
*  compelling characters. But you're right, that's a dangerous sort of road to walk because you're
*  adding degrees of freedom that can get you in trouble. Yeah. That's why you have these
*  big pushes that for most of the last decade plus where you'd have full human replicas of robots,
*  being down to skin and in some places. My personal feeling is like, man, that's not the
*  direction that's most fruitful right now. Beautiful art. It's not in terms of a
*  rich, deep, fulfilling experience. Yeah, you're right. Yeah. And you're creating a minefield of
*  potential places to feel off. And then you're sidestepping where the biggest kind of functional
*  AI challenges are to actually have really rich productivity that actually justifies the higher
*  price points. And that's part of the challenges. Yeah, robots are going to get to thousands of
*  dollars, tens of thousands of dollars and so forth, but you can imagine what sort of expectation of
*  value that comes with it. And so that's where you want to be able to invest the time and depth.
*  And so going down the full human replica route creates a gigantic distraction and really,
*  really high bar that can end up sucking up so much of your resources.
*  So it's weird to say, but you happen to be one of the greatest at this point,
*  roboticists ever because you created this little guy, your part obviously of a great team that
*  created the little guy with a deep personality and are now switching to an entirely, well,
*  maybe not entirely, but a different, fascinating, impactful robotics problem,
*  which is autonomous driving and more specifically the biggest version of autonomous driving,
*  which is autonomous trucking. So you are at Waymo now. Can you give us a big picture overview?
*  What is Waymo? What is Waymo driver? What is Waymo one? What is Waymo via? Can you give an
*  overview of the company and the vision behind the company?
*  For sure. Waymo, by the way, has been eye opening on just how incredible the people and the talent
*  is and how in one company you almost have to create 30 companies worth of technology and
*  capability to solve the full spectrum of it. So I've been at Waymo since 2019, so about two
*  and a half years. So Waymo is focused on building what we call a driver, which is creating the
*  ability to have autonomous driving across different environments, vehicle platforms,
*  domains, and use cases. As you know, it got started in 2009. It was almost like an immediate
*  successor to the Grand Challenge and Urban Challenges that were incredible catalysts for
*  this whole space. And so Google started this project and then eventually Waymo spun out.
*  What Waymo is doing is creating the systems, both hardware, software, infrastructure,
*  everything that goes into it to enable and to commercialize autonomous driving. This hits on
*  consumer transportation and ride sharing and kind of vehicles in urban environments. And as you
*  mentioned, it hits on autonomous trucking to transport goods. So in a lot of ways, it's
*  transporting people and transporting goods. But at the end of the day, the underlying capabilities
*  required to do that are surprisingly better aligned than one might expect, where it's the
*  fundamentals of being able to understand the world around you, process it, make intelligent
*  decisions, and prove that we are at a level of safety that enables large-scale autonomy.
*  So from a branding perspective, Waymo driver is the system that's irrespective of a particular
*  vehicle it's operating in. You have a set of sensors that perceive the world, can act in that
*  world, and move whatever the vehicle is through the world. That's right. And so in the same way
*  that you have a driver's license and your ability to drive isn't tied to a particular make and model
*  of a car. And of course, there are special licenses for other types of vehicles, but the
*  fundamentals of a human driver very, very largely carry over. And then there's uniquenesses related
*  to a particular environment or domain or a particular vehicle type that kind of add some
*  extra additive challenges. But that's exactly right. It's the underlying systems that enable
*  a physical vehicle without a human driver to very successfully accomplish a task that previously
*  wasn't possible without 100% human driving. And then there's Waymo 1, which is the transporting
*  people from a brand perspective, in case we refer to it so people know. And then there's Waymo Via,
*  which is the trucking component. Why Via, by the way? Is it just a cool sounding name?
*  Is there an interesting story there? It is a pretty cool sounding name.
*  It's a cool sounding name. When you think about it, it's just like, well, we're going to transport
*  it via this and that. So it's just kind of like an allusion to the mechanics of transporting
*  something. And it is a pretty good grouping. And the interesting thing is that even the groupings
*  kind of blur where Waymo 1 is like human transportation and there's a fully autonomous
*  service in the Phoenix area that every day is transporting people. And it's pretty incredible
*  to see that operate at reasonably large scale and just kind of happen. And then on the Via side,
*  it doesn't even have to be like long haul trucking is a major focus of ours, but down the road,
*  you can stitch together the vehicle transportation as well for local delivery. Also,
*  and a lot of the requirements for local delivery overlap very heavily with consumer transportation,
*  obviously, given that you're operating on a lot of the same roads and navigating the same
*  safety challenges. And so, yeah, and Waymo very much is a multi-product company that has
*  ambitions in both. They have different challenges and both are tremendous opportunities.
*  But the cool thing is that there's a huge amount of leverage and this kind of core technology stack
*  now gets pushed on by both sides. And that adds its own unique challenges, but the success case is
*  that the challenges that you push on, they get leveraged across all platforms and all domains.
*  From an engineer perspective, the teams are integrated.
*  It's a mix. So there's a huge amount of centralized core teams that support all applications. And so,
*  you think of something like the hardware team that develops the lasers, the compute, integrates into
*  vehicle platforms. This is an experience that carries over across any application that we'd
*  have and they have been full of both. Then there's really unique perception challenges,
*  planning challenges, other types of challenges where there's a huge amount of leverage on a core
*  tech stack, but then there's dedicated teams that think of how do you deal with a unique challenge?
*  For example, an articulated trailer with varying loads that completely changes the physical dynamics
*  of a vehicle that doesn't exist on a car, but becomes one of the most important
*  unique new challenges on a truck. So what's the long-term dream of Waymovia,
*  the autonomous trucking effort that Waymo's doing? Yeah. So we're starting with developing
*  L4 autonomy for class eight trucks. These are 53-foot trailers that capture a pretty sizable
*  percentage of the goods transportation in the country. Long-term, the opportunity is obviously
*  to expand a much more diverse types of vehicles, types of goods transportation, and start to really
*  expand in both the volume and the route feasibility that's possible. And so just like we did on the
*  car side, you start with a single route with a very specific operating kind of domain and
*  constraints that allow you to solve the problem. But then over time, you start to really try to push
*  against those boundaries and open up deeper feasibility across routes, across surface
*  streets, across environmental conditions, across the type of goods that you carry,
*  the versatility of those goods, and how little supervision is necessary to just start to scale
*  this network. And long-term, it's a pretty incredible enabler where today you have already
*  a giant shortage of truck drivers. It's over 80,000 truck driver shortage that's expected to grow to
*  hundreds of thousands in the years ahead. You have really, really quickly increasing demand from
*  e-commerce and just distribution of where people are located. You have one of the deepest safety
*  challenges of any profession in the US where there's a huge, huge, huge challenge around
*  fatigue and around the long routes that are driven. And even beyond the cost and necessity of it,
*  there are fundamental constraints built into our logistics network that are tied to the type of
*  human constraints and regulatory constraints that are tied to trucking today. For example,
*  our limits on how long a driver can be driving in a single day before they're not allowed to
*  drive anymore, which is a very important safety constraint. What that does is it enforces
*  limitations on how far jumps with a single driver could be and makes you very subject to availability
*  of drivers, which influences where warehouses are built, which influences how goods are transported,
*  which influences costs. And so you start to have an opportunity on everything from plugging into
*  existing fleets and brokerages and the existing logistics network and just immediately start to
*  have a huge opportunity to add value from a cost and driving fuel insurance and safety standpoint,
*  all the way to completely reinventing the logistics network across the United States
*  and enabling something completely different than what it looks like today.
*  Yeah, I had to be published before this, had a great conversation with Steve Vichelli, who
*  we talked about the manual driving. He echoed many of the same things that you were talking about,
*  but we talked about much of the fascinating human stories of truck drivers. He was also
*  was a truck driver for a bit as a grad student to try to understand the depth of the problem.
*  It's fascinating lives. We have some drivers that have 4 million miles of lifetime driving
*  experience. It's pretty incredible. And yeah, it's learning from them. Some of them are on the road
*  for 300 days a year. It's a very unique type of lifestyle. So there's fascinating stuff there.
*  Just like you said, there's a shortage of actually people, truck drivers taking the job counter to
*  what this I think is publicly believed. So there's an excess of jobs and a shortage of people to take
*  up those jobs. And just like you said, it's such a difficult problem. And these are experts at
*  driving, at solving this particular problem. And it's fascinating to learn from them to understand
*  how hard is this problem. And that's the question I want to ask you from a perception,
*  from a robotics perspective, what's your sense of how difficult is autonomous trucking? Maybe
*  you can comment on which scenarios are super difficult, which are more manageable. Is there
*  a way to kind of convert into words how difficult the problem is? Yeah, it's a good question.
*  So there's, and as you can expect, it's a mix. Some things become a lot easier or at least more
*  flexible. Some things are harder. And so on the things that are like the tailwinds, the benefits,
*  a big focus of automating trucking, especially initially, is really focusing on the long haul
*  freeway stretch of it, where that's where a majority of the value is captured. On a freeway,
*  you have a lot more structure and a lot more consistency across freeways across the US,
*  compared to surface streets where you have a way higher dimensionality of what can happen,
*  lack of structure, lack of consistency and variability across cities. So you can leverage
*  that consistency to tackle, at least in that respect, a more constrained AI problem, which
*  has some benefits to it. You can itemize much more of the sort of things you might encounter
*  and so forth. And so those are benefits. Is there a canonical freeway and city we should
*  be thinking about? Is there a standard thing that's brought up in conversation often? Here's a
*  stretch of road. What is it? When people talk about traveling across country, they'll talk about
*  New York, San Francisco. Is that the route? Is there a stretch of road that's nice and clean?
*  And then there's cities with difficulties in them that you think of as the canonical
*  problems to solve here. Right. So starting with the car side,
*  Waymo very intentionally picked the Phoenix area and the San Francisco area as a follow once we
*  hit driverless, where when you think of consumer transportation and ride sharing kind of economy,
*  a big percentage of that market is captured in the densest cities in the United States. And so
*  really pushing out and solving San Francisco becomes a really huge opportunity and importance
*  and places one dot on kind of like the spectrum of like kind of complexity.
*  The Phoenix area, starting with Chandler and then like kind of expanding more broadly in the Phoenix
*  metropolitan area, it's I believe the fastest growing city in the US. It's a kind of a higher
*  medium sized city, but growing quickly and still captures a really wide range of kind of like
*  complexities. And so getting to driverless there actually exposes you to a lot of the building
*  blocks you need for the more complicated environments. And so in a lot of ways,
*  there's a thesis that if you start to kind of place a few of these kind of dots where
*  San Francisco has these types of unique challenges, dense pedestrians, all this like complexity,
*  especially when you get into the downtown areas and so forth, and Phoenix has like
*  a really interesting kind of spectrum of challenges, maybe other ones like LA kind
*  of add freeway focus and so forth, you start to kind of cover the full set of features that you
*  might expect and it becomes faster and faster if you have the right systems and the right
*  organization to then open up the fifth city and the tenth city and the twentieth city.
*  On trucking, there's similar properties where obviously there's uniquenesses in freeways when
*  you get into really dense environments and then the real opportunity to then get even more
*  value is to think about how you expand with like some of the service challenges. But for
*  example, right now we're looking, we have a big facility that we're finishing building in Q1
*  in Dallas area. That'll allow us to do testing from the Dallas area on routes like Dallas to
*  Houston, Dallas to Phoenix, going out east and- Dallas to Austin.
*  Austin, so that triangle- Waymo should come to Austin.
*  Well, Waymo, the car side was in Austin for a while.
*  Yes, I know. Come back.
*  Yeah. But trucking is actually, Texas is one of the best places to start because of both volume,
*  regulatory, weather, there's a lot of benefits. On trucking, a huge opportunity is Port of LA
*  going east. So in a lot of ways, a lot of the work is to start to stitch together a network
*  and converge to Port of LA where you have the biggest port in the United States.
*  And the amount of goods going east from there is pretty tremendous. And then obviously there's
*  channels everywhere and then you have extra complexities as you get into like snow and
*  inclement weather and so forth. But what's interesting about trucking is every single
*  route segment that you add increases the value of the whole network. And so it has this kind of
*  network effect and cumulative effect that's very unique. And so there's all these dimensions that
*  we think about. And so in a lot of ways, Dallas has a really unique hub that opens up a lot of
*  options has become a really valuable lever. So the million questions I could ask you. First of all,
*  you mentioned level four. For people who totally don't know, there's these levels of automation
*  that level four refers to kind of the first step that you could recognize as fully autonomous
*  driving. Level five is really fully autonomous driving. Level four is kind of fully autonomous
*  driving. And then there are specific definitions, depending on who you ask what that actually means.
*  But for you, what does the level four mean? And you mentioned freeway. Let's say like there's three
*  parts of long haul trucking. Maybe I'm wrong in this, but there's freeway driving. There's like
*  truck stop. And then there's more urban type of area. So which of those do you want to tackle?
*  Which of them do you include under level four? Like, well, how do you think about this problem?
*  What do you focus on? Where's the biggest impact to be had in the short term?
*  So the goal is that we got to get to market as fast as we can, because the moment you get to market,
*  you just learn so much and it influences everything that you do. And it is,
*  one of the experiences I carried over from before is that you add constraints,
*  you figure out the right compromises, you do whatever it takes because getting to market
*  is so critical. Right? And here with autonomous driving, you can get to market in so many different
*  ways. That's right. And so one of the simplifications that we intentionally have put on is using what we
*  call transfer hubs, where you can imagine depots that are at the entry points to metropolitan areas,
*  like let's say Dallas, like the hub that we're building, which does a few things that are very
*  valuable. So from a first product standpoint, you can automate transfer hub to transfer hub.
*  And that path from the transfer hub to the full freeway route can be a very intentional single
*  route that you can select for the features that you feel you want to handle at that point in time.
*  And you build the hub specifically designed for autonomous trucking.
*  And that's what's going to happen actually. You need to come out in January and check it out
*  because it's going to be really cool. Not only is it our main operating headquarters for our fleet
*  there, but it will be the first fully ground up design driverless hub for autonomous trucks in
*  terms of where do they enter, where do they depart, how do you think about the flow of people,
*  goods, everything. It's quite cool and it's really beautiful on how it's thought through.
*  And so early on, it is totally reasonable to do the last five miles manually to get to the final
*  kind of depot to avoid having to solve the general surface street problem,
*  which is obviously very complex. Now, when the time comes and we are increasingly,
*  already we're pushing on some of this, but we will increasingly be pushing on surface
*  street capabilities to build out the value chain to go all the way depot to depot instead of
*  transfer hub to transfer hub. And we have probably the best advantages in the world because of all
*  the Waymo experience on surface streets, but that's not the highest ROI right now where the
*  highest ROI is hub to hub and get the routes going. And so when you ask what's L4,
*  L4 can be applied to any domain, operating domain or scope, but it's effectively for the places where
*  we say we're ready for autonomous operation. We are 100% operating as a self-driving truck with no
*  human behind the wheel. That is L4 autonomy. And it doesn't mean that you operate in every condition.
*  It doesn't mean you operate on every road, but for a particularly well-defined area,
*  operating conditions, routes kind of domain, you are fully autonomous. And that's the difference
*  between L4 and L5. And most people would agree that at least anytime in the foreseeable future,
*  L5 is just not even really worth thinking about because there's always going to be these extremes.
*  And so it's a race and almost like a game where you think of what is the sequence of expanded
*  capabilities that create the most value and teach us the most and create this feedback loop
*  where we're building out and unlocking more and more capability over time.
*  I got to ask you, just curious. So first of all, I have to, when I'm allowed,
*  visit the Dallas facility because it's super cool. It's like robot on the giving and the receiving
*  end. It's the truck is a robot and the hub is a robot. Yeah. It's got to be very robot friendly.
*  So that's great. I will feel at home. What's the sensor suite like on the hub? If you can
*  just high level mention it is that does the hub have like lidars and like, is the truck doing
*  most of the intelligence or is the hub also intelligent? Yeah. So most of it will be the
*  truck and everything is like connected. So we have our servers where we know exactly where every
*  truck is. We know exactly what's happening at a hub. And so you can imagine like a large backend
*  system that over time starts to manage timings, goods, delivery windows, all these sorts of things.
*  And so you don't actually need to, there might be special cases where that is valuable to equip
*  some sensors in the hub, but a majority of the intelligence is going to be on the truck
*  because whatever's relevant to the truck, relevant should be seen by the truck and can be relayed
*  remotely for any sort of kind of cognizance or decision making. But there's a distinct type of
*  workflow where do you check trucks? Where do you want them to enter? What if there's many operating
*  at once? Where's the staging area to depart? How do you set up the flow of humans and human cars
*  and traffic so that you minimize the interaction between humans and kind of self-driving trucks?
*  And then how do you even intelligently select the locations of these transfer hubs that are both
*  really great service locations for a metropolitan area? And there could be over time, many of them
*  for a metropolitan area, while at the same time leaning into the path of least resistance to lean
*  into your current capabilities and strengths so that you minimize the amount of work that's
*  necessary to unlock the next kind of big bar. I have a million questions. So first, is the goal
*  to have no human in the truck? The goal is to have no human in the truck. Now, of course,
*  right now we're testing with expert operators and so forth, but the goal is to... Now, there might
*  be circumstances where it makes sense to have a human and obviously these trucks can also be
*  manually driven. So sometimes we talk with our fleet partners about how you can buy Waymo-equipped
*  Diemore truck down the road and on the routes that are autonomous, it's autonomous. On the routes
*  that are not, it's human driven. Maybe there's L2 functionality that add safety systems and so
*  forth. But as soon as they become... As soon as we expand in software, the availability of driverless
*  routes, the hardware is forward compatible to just now start using them in real time. And so
*  you can imagine this mixed use, but at the end of the day, the largest value proposition is where
*  you're able to have no constraints on how you can operate this truck and it's 100% autonomous with
*  nobody inside. That's amazing. So let me ask on the logistics front, because you mentioned that
*  also opportunity to revamp or for builds from scratch some of the ideas around logistics.
*  I don't want to throw too much shade, but from talking to Steve, my understanding is
*  logistics is not perhaps as great as it could be in the current trucking environment.
*  I'm not... Maybe you can break down why, but there's probably competing companies. There's just a
*  mess. Maybe some of it is literally just it's old school. It's not computerized.
*  Truckers are almost like contractors. There's an independence and there's not a nice interface
*  where they can communicate where they're going, where they're at, all those kinds of things.
*  And so it just feels like there's so much opportunity to digitize everything
*  to where you could optimize the use of human time, optimize the use of all kinds of resources.
*  How much are you thinking about that problem? How fascinating is that problem?
*  How difficult is it? How much opportunity is there to revolutionize the space of logistics
*  in autonomous trucking, in trucking period? It's pretty fascinating. This is one of the most
*  motivating aspects of all this where yes, there's a mountain of problems that you have to solve to
*  get to the first checkpoints and first drivers and so forth. And inevitably in a space like this,
*  you plug in initially into the existing system and start to learn and iterate. But
*  that opportunity is massive. And so a couple of the factors that play into it. So first of all,
*  there's obviously just the physical constraints of driving time, driver availability.
*  Some fleets have a 95% attrition rate right now because of just
*  this demands and gaps in competition and so forth. And then it's also incredibly fragmented where
*  you would be shocked at when you look at industries and you think of the top 10 players,
*  the biggest fleets like the Walmarts and FedExes and so forth. The percentage of the overall
*  trucking market that's captured by the top 10 or 50 fleets is surprisingly small.
*  The average truck operation is like a one to five truck family business. And so there's just a huge
*  amount of fragmentation which makes for really interesting challenges in stitching together
*  through bulletin boards and brokerages and some people run their own fleets. And this world's
*  evolving, but it is one of the less digitized and optimized worlds that there is. And the part that
*  is optimized is optimized to the constraints of today. And even within the constraints of today,
*  this is a $900 billion industry in the US and it's continuing to grow.
*  It feels like from a business perspective, if I were to predict that whilst trying to solve
*  the autonomous trucking problem, Waymo might solve first the logistics problem. Because that
*  would already be a huge impact. So on the way to solving autonomous trucking, the human driven,
*  there's so much opportunity to significantly improve the human driven trucking, the timing,
*  the logistics. So you use humans optimally. The handoffs, the like. Well, even that you get
*  really ambitious, you start to expand this beyond how does the fulfillment center work and how does
*  the transfer hub work? How does the warehouse work? There's a lot of opportunities to start
*  to automate these chains. And a lot of the inefficiency today is because you have a delay.
*  Port of LA has a bunch of ships right now waiting outside of it because they can't dock because
*  there's not enough labor inside of the port of LA. That means there's a big backlog of trucks,
*  which means there's a big backlog of deliveries, which means the drivers aren't where they need
*  to be. And so you have this huge chain reaction and your feasibility of readjusting in this
*  network is low because everything's tied to humans and manual processes or distributed processes
*  across a whole bunch of players. And so one of the biggest enablers is yes, we have to solve
*  autonomous trucking first. And by the way, that's not like an overnight thing. That's decades of
*  continued kind of expansion and work. But the first checkpoint and the first route is not that
*  far off. But once you start enabling and you start to learn about how the constraints of
*  autonomous trucking, which are very, very different than the constraints of human trucking,
*  and again, strengths and weaknesses, how do you then start to leverage that and rethink a flow of
*  goods more broadly? And this is where the learnings of really partnering with some of the largest
*  fleets in the US and the sort of learnings that they have about the industry and the sort of needs
*  that they have and what would change if you just really broke this one constraint that holds up the
*  whole network? Or what if you enabled this other constraint? That actually drives the roadmap in a
*  lot of ways, because this is not like an all or nothing problem. You start to kind of unlock more
*  and more functionality over time, which functionality most enables this optimization ends up being kind
*  of part of the discussion. But you're totally right. You fast forward to five years, 10 years,
*  15 years, and you think about very generalized capability of automation and logistics,
*  as well as the ability to poke into how those handoffs work. The efficiency goes far beyond
*  just direct cost of today's unit economics of a truck. They go towards reinventing the entire
*  system in the same way that you see these other industries that when you get to enough scale,
*  you can really rethink how you build around your new set of capabilities, not the old set of
*  capabilities. Yeah, use the analogy metaphor or whatever that autonomous trucking is like email
*  versus mail. And then with email, you're still doing the communication, but it opens up all
*  kinds of varieties of communication that you didn't anticipate. That's right. Constraints are just
*  completely different. And yeah, there's definitely a property of that here. And we're also still
*  learning about it because there is a lot of really fascinating and sometimes really elegant
*  things that the industry has done where there's companies whose entire existence is around,
*  despite the constraints, optimizing as much as they can out of it. And those lessons do carry over,
*  but it's an interesting kind of merger of worlds to think about like, well, what if this was
*  completely different? How would we approach it? And the interesting thing is that for a really,
*  really, really long time, it's actually going to be the merger between how to use autonomy and how
*  to use humans that leans into each of their strengths. Yeah. And then we're back to Cosmo,
*  human robot interaction. So in the interesting thing about Waymo is because there's the passenger
*  vehicle, the human, the transportation of humans and transportation of goods, you can see over time
*  they may kind of meld together more because you'll probably have like zero occupancy vehicles moving
*  around. So you have transportation of goods for short distances and then for slightly longer
*  distances and then slightly longer. And then there'll be this, then you just see the difference
*  between a passenger vehicle and a truck is just size and you can have different sizes and all that
*  kind of stuff. And at the core, you can have a Waymo driver that doesn't, as long as you have
*  the same sensor suite, you can just think of it as one problem. And that's why over time these do
*  kind of converge where in a lot of ways, a lot of the challenges we're solving are freeway driving,
*  which are going to carry over very well to the vehicles, to the car side. But there are like then
*  unique challenges like you have a very different dynamics in your vehicle where you have to see
*  much further out in order to have the proper response time because you have an 80,000 pound
*  fully loaded truck. That's a very, very different type of braking profile than a car. You have
*  really interesting kind of dynamic limits because of the trailer where you actually,
*  it's very, very hard to physically flip a car or do something physically. Most risk in a car is from
*  just collisions. It's very hard in any normal operation to do something other than unless you
*  hit something to actually kind of like roll over or something. On a truck, you actually have to
*  drive much closer to the physical bounds of the safety limits, but you actually have real
*  constraints because you could have really interesting interactions between the cabin
*  and the trailer. There's something called jackknifing if you turn too quickly, you have
*  roll risks and so forth. And so we spent a huge amount of time understanding those boundaries.
*  And those boundaries change based on the load that you have, which is also an interesting
*  difference. You have to propagate that through the algorithm so that you're leveraging your dynamic
*  range, but always staying within a safety balance, but understanding what those safety bounds are.
*  We have this really cool test facility where we take it to the max and actually
*  imagine a truck with these giant training wheels on the back of the trailer, and you're pushing
*  it past the safety limits in order to try to actually see where it rolls. And so you define
*  this high dimensional boundary, which then gets captured in software to stay safe and actually do
*  the right thing. But it's fascinating the challenges you have there. But then all of
*  these things drive really interesting challenges from perception to unique behavior prediction
*  challenges. And obviously in planner where you have to think about merging and creating gaps with a 53
*  foot trailer and so forth. And then obviously the platform itself is very different where you have
*  different numbers of sensors, sometimes types of sensors, and you also have unique blind spots
*  that you have because of the trailer, which you have to think about. And so it's a really interesting
*  spectrum. And in the end, you try to capture these special cases in a way that is cleanly
*  augmentations of the existing tech stack because a majority of what we're solving is actually
*  generalizable, the freeway driving and different platforms. And over time, they all start to kind
*  of merge ideally where the things that are unique are as minimal as possible. And that's where you
*  get the most leverage. And that's why Waymo can do take on $2 trillion opportunities and
*  be nowhere near 2X the cost or investment or size. In fact, it's much, much smaller than that
*  because of the high degree of leverage. So what kind of sensors they can speak to that
*  a long haul truck needs to have? Lidar, vision, how many, what are we talking about here?
*  Yeah, so it's more than the car. So very loosely you can think of as like 2X, but it varies
*  depending on the sensor. And so we have like dozens of cameras, radar, and then multiple
*  Lidar as well. You'll see one difference where the cars have a central main sensor pod on the
*  roof in the middle, and then some kind of hood sensors for blind spots. The truck moves to two
*  main sensor pods on the outsides where you would typically see how the mirrors next to the driver.
*  They effectively go as far out as possible kind of up to the front, kind of on the cabin, not all
*  the way in the front, but like kind of where the mirrors for the driver would be. And so those are
*  the main sensor pods. And the reason they're there is because if you had one in the middle,
*  the trailer is higher than the cabin and you would be occluded with this like awkward wedge.
*  Too much occlusion.
*  Too much occlusion. And so then you would add a lot of complexity to the software to make up for
*  that and just unnecessary complexity.
*  There's so many probably fascinating designs you have to see.
*  It's really cool.
*  Because you can probably bring up a Lidar higher and have it in the center or something. You can
*  have all kinds of choices to make the decisions here that ultimately probably will define the
*  industry.
*  Right. But by having two on the side, there's actually multiple benefits. So one is like
*  you're just beyond the trailer so you can see fully flush with the trailer. And so you eliminate
*  most of your blind spot except for right behind the trailer, which is great because now the
*  software carries over really well. And the same perception system you use on the car side,
*  largely that architecture can carry over and you can retrain some models and so forth.
*  But you leverage it a lot. It also actually helps with redundancy where there's a really
*  nice built-in redundancy for all the Lidar cameras and radar where you can afford to have any one of
*  them fail and you're still okay. And at scale, every one of them will fail.
*  And you will be able to detect when one of them fails because they don't, because the redundancy
*  that they're giving you the data that's inconsistent with the rest of it.
*  That's right. And it's not just like they no longer give data. It could be like they're
*  fouled or they stop giving data where some electrical thing gets cut or part of your
*  compute goes down. So what's neat is that you have way more sensors, part of it is field of
*  view and occlusions, part of it is redundancy, and then part of it is new use cases. So there's
*  new types of sensors to optimize for long range and the sensing horizon that we look for
*  on our vehicles that is unique to trucks because it actually is like kind of much
*  like further out than a car. But a majority are actually we used across both cars and trucks.
*  And so we use the same compute, the same fundamental baseline sensors, cameras,
*  radar, IMUs. And so you get a great leverage from all of the infrastructure and the hardware
*  development as a result. So what about cameras? What role does... So Lidar is this rich
*  server information as its strengths has some weaknesses. Camera is this rich source of
*  information that has some strengths as its weaknesses. What role does Lidar play? What
*  role does vision cameras play in this beautiful problem of autonomous trucking?
*  Oh, it is beautiful. There's like so much that comes together.
*  And how much... At which point do they come together?
*  Yeah. So let's start with Lidar. So Lidar has been like one of Waymo's big strengths and
*  advantages where we developed our own Lidar in-house where many generations in both in
*  cost and functionality, it is the best in the space.
*  Which generation? Because I know there's this cool, I mean, I would love versions that are
*  increasing. Which version of the hardware stack is it currently? Officially, publicly?
*  So some parts iterate more than others. I'm trying to remember on the sensor side. So
*  the entire self-driving system, which includes sensors and compute, is fifth generation.
*  I can't wait until there's like iPhone style announcements for new versions of the Waymo
*  hardware. Well, we try to be careful because, man, when you change the hardware, it takes a lot to
*  retrain the models and everything. So we just went through that and going from the Pacifica to the
*  Jaguars. And so the Jaguars and then the trucks have the same generation now. But yeah, the
*  Lidar is incredible. And so Waymo has leaned into that as a strength. And so a lot of the near range
*  perception system that obviously carries over a lot from the car side uses Lidar as a very
*  prominent primary sensor. But then obviously everything has its strengths and weaknesses.
*  So in the near range, Lidar is a gigantic advantage. And it has its weaknesses when it
*  comes to occlusions in certain areas, rain and weather, things like that. But it's an incredible
*  sensor and it gives you incredible density, perfect location precision and consistency,
*  which is a very valuable property to be able to apply a male approach.
*  Can you elaborate consistency?
*  When you have a camera, the position of the sun, the time of the day, various of the properties
*  can have a big impact, whether there's glare, the field of view, things like that.
*  So consistent in the face of a changing external environment, the signal.
*  Yeah, daytime, nighttime. It's about 3D physical existence. In fact, you're seeing
*  beams of light that physically bounce off of something and come back. And so whatever the
*  conditional conditions are, the shape of a human sensor reading from a human or from a car or from
*  an animal, you have a reliability there, which ends up being valuable for the long tail of
*  challenges. Now, Lidar is the first sensor to drop off in terms of range. And ours has a really good
*  range, but at the end of the day, it drops off. And so particularly for trucks, on top of the
*  general redundancy that you want for near range and complements through cameras and radar for
*  occlusions and for complimentary information and so forth, when you get to long range,
*  you have to be radar and camera primary because your Lidar data will fundamentally drop off after
*  a period of time and you have to be able to see objects further out. Now, cameras have the
*  incredible range where you get a high density, high resolution camera. You can get data well
*  past a kilometer and it's really potentially a huge value. Now, the signal drops off, the
*  noise is higher, detecting is harder, classifying is harder. And one that you may not think about
*  localizing is harder because you can be off by two meters in where something's located a kilometer
*  away. And that's the difference between being on the shoulder and being in your lane. And so you
*  have interesting challenges there that you have to solve, which have a bunch of approaches that
*  come into it. Radar is interesting because it also has longer range than Lidar and it gives you
*  speed information. So it becomes very, very useful for dynamic information of traffic flow,
*  vehicle motions, animals, pedestrians, just things that might be useful signals.
*  And it helps with weather conditions where radar actually penetrates weather conditions in a better
*  way than other sensors. And so it's kind of interesting where we've kind of started to
*  converge towards not thinking about a problem as a Lidar problem or a camera problem or radar
*  problem, but it's a fusion problem where these are all like large scale ML problems where you
*  put data into the system. And in many cases, you just look for the signals that might be present
*  in the union of all of these and leave it to the system as much as possible to start to really
*  identify how to extract that. And then there's places we have to intervene and actually
*  include more, but no single sensor is in a great position to really solve this problem and end
*  without a huge extra challenge. That's fascinating. There's a question that's
*  probably still an open question is at which point do you fuse them? Do you solve the perception
*  problem for each sensor suite individually, the Lidar suite and the camera suite, or do you
*  do some kind of heterogeneous fusion or do you fuse at the very beginning?
*  Is there a good answer or at least an inkling of intuitions you can come?
*  Yeah. So people refer to this as early fusion or late fusion. So late fusion might be that you have
*  the camera pipeline, the Lidar pipeline, and then you fuse them and when it gets to final semantics
*  and classification and tracking, you fuse them together and figure out which one's best.
*  There's more and more evidence that early fusion is important and that is because
*  late fusion does not allow you to pick up on the complementary strengths and weaknesses of the
*  sensors. Weather is a great example where if you do early fusion, you have an incredibly hard
*  problem for any single sensor in rain to solve that problem because you have reflections from
*  the Lidar. You have weird kind of noise from the camera, blah, blah, blah, right? But the
*  combination of all of them can help you filter and help you get to the real signal that then gets you
*  as close as possible to the original stack and be much more fluid about the strengths and weaknesses
*  where your camera is much more susceptible to fouling on the actual lens from rain or random stuff,
*  whereas you might be a little bit more resilient in other sensors. And so there's an element of
*  logic that always happens late in the game, but that fusion early on actually, especially as you
*  move towards ML and large-scale data-driven approaches, just maximizes your ability to pull
*  out the best signal you can out of each modality before you start making constraining decisions
*  that end up being hard to unwind late in the stack. So how much of this is a machine learning
*  problem? What role does ML, machine learning, play in this whole problem of autonomous driving,
*  autonomous trucking? It's massive, and it's increasing over time. If you go back to
*  the grand challenge days and the early days of AV development, there was ML, but it was not in the
*  mass-scale data style of ML. It was like learning models, but in a more structured way, and it was
*  a lot of heuristic and search-based approaches and planning and so forth. You can make a lot of
*  progress with these types of approaches across the board, an almost deceptive amount of progress.
*  We can get pretty far, but then you start to really grind the further you get in some parts of the
*  stack if you don't have an ability to absorb a massive amount of experience in a way that
*  scales very subliminally in terms of human labor and human attention. And so when you look at the
*  stack, the perception side is probably the first to get really revolutionized by ML, and it goes
*  back many years because ML for computer vision and these types of approaches took off with a lot of
*  the early push in deep learning. And so there's always a debate on the spectrum between end-to-end
*  ML, which is a little bit too far to how you architect it to where you have modules but enough
*  ability to think about long-tail problems and so forth. But at the end of the day, you have big
*  parts of the system that are very ML and data-driven, and we're increasingly moving
*  in that direction all the way across the board, including behavior where even when it's not like
*  a gigantic ML problem that covers a giant swath end-to-end, more and more parts of the system
*  have this property where you want to be able to put more data into it, and it gets better.
*  And that has been one of the realizations as you drive tens of millions of miles and
*  try to solve new expansions of domains without regressing your old ones, it becomes intractable
*  for a human to approach that in the way that traditionally robotics has approached some
*  elements of the tech stack. So are you trying to create a data pipeline specifically for the
*  trucking problem? How much leveraging of the autonomous driving is there in terms of data
*  collection? And how unique is the data required for the trucking problem?
*  So we reuse all the same infrastructure, so labeling workflows, ML workflows, everything,
*  so that actually carries over quite well. We heavily reuse the data even, where almost every
*  model that we have on a truck, we started with the latest car model. So it's almost like a good
*  back-car model. Yeah, it's like you can think of like, despite the different domain and different
*  numbers of sensors and position of sensors, there's a lot of signals that carry over across
*  driving. And so it's almost like pre-training and getting a big boost out of the gate where
*  you can reduce the amount of data you need by a lot. And it goes both ways actually. And so we're
*  increasingly thinking about our data strategy on how we leverage both of these. So you think about
*  how other agents react to a truck. Yeah, it's a little bit different, but the fundamentals are
*  actually like, what will other vehicles in the road do? There's a lot of carryover that's possible.
*  And in fact, just to give you an example, we're constantly adding more data from the trucking
*  side. But as of right now, when we think of one of our models, behavior prediction for other
*  agents on the road, like vehicles, 85% of that data comes from cars. And a lot of that 85% comes
*  from surface streets because we just had so much of it and it was really valuable. And so we're
*  adding in more and more, particularly in the areas where we need more data, but you get a
*  huge boost out of the gate. Just all different visual characteristics of roads, lane markings,
*  pedestrians, all that, that's still relevant. It's all still relevant. And then just the
*  fundamentals of how you detect the car, does it really change that much, whether you're detecting
*  it from a car or a truck? The fundamentals of how a person will walk around your vehicle,
*  is it'll change a little bit, but the basics, there's a lot of signal in there that as a
*  starting point to a network can actually be very valuable. Now, we do have some very unique
*  challenges where there's a sparsity of events on a freeway. The frequency of events happening on a
*  freeway, whether it's interesting objects in the road or incidents, or even from a human benchmark,
*  how often does a human have an accident on a freeway, is far more sparse than on a surface
*  street. And so that leads to really interesting data problems where you can't just drive infinitely
*  encounter all the different permutations of things you might encounter. And so there you get into
*  interesting tools like structured testing and data collection, data augmentation, and so forth. And so
*  there's really interesting kind of technical challenges that push some of the research
*  that enables these new suites of approaches. What role does simulation play? Really good question.
*  So Waymo simulates about a thousand miles for every mile it drives. So you think of- In both,
*  so across the board. Across the board, yeah. So you think of, for example, well, if we've driven
*  over 20 million miles, that's over 20 billion miles in simulation. Now, how do you use simulation?
*  It's multi-purpose. So you use it for basic development. So you want to make sure you have
*  regression prevention and protection of everything you're doing. That's an easy one. When you
*  encounter something interesting in the world, let's say there was an issue with how the vehicle
*  behaved versus an ideal human. You can play that back in simulation and start augmenting your system
*  and seeing how you would have reacted to that scenario with this improvement or this new area.
*  You can create scenarios that become part of your regression set after that point. Then you start
*  getting into really, really high kind of hill climbing where you say, hey, I need to improve
*  this system. I have these metrics that are really correlated with final performance. How do I know
*  how well I'm doing? The actual physical driving is the least efficient form of testing. It is
*  expensive. It's time consuming. So grabbing a large scale batch of historical data and simulating it
*  to get a signal of over these last or just random sample of a hundred thousand miles, how has this
*  metric changed versus where we are today? You can do that far more efficiently in simulation than
*  just driving with that new system on board. And then you go all the way to the validation phase
*  where to actually see your human relative safety of how well you're performing on the car side or
*  the trucking side relative to a human. A lot of that safety case is actually driven by
*  taking all of the physical operational driving, which probably includes a lot of interventions
*  where the driver took over just in case. And then you simulate those forward and see if
*  would anything have happened. And in most cases, the answer is no, but you can simulate it forward.
*  And you can even start to do really interesting things where you add virtual agents to create
*  harder environments. You can fuzz the locations of physical agents. You can muck with the scene
*  and stress test the scenario from a whole bunch of different dimensions. And effectively,
*  you're trying to more efficiently sample this infinite dimensional space, but try to encounter
*  the problems as fast as possible. Because what most people don't realize is the hardest problem
*  in autonomous driving is actually the evaluation problem in many ways, not the actual autonomy
*  problem. And so if you could in theory evaluate perfectly and instantaneously, you can solve that
*  problem in a really fast feedback loop quite well. But the hardest part is being really smart about
*  this suite of approaches on how can you get an accurate signal on how well you're doing as quickly
*  as possible in a way that correlates to physical driving. Can you explain the evaluation problem?
*  Which metric are you evaluating towards? We're talking about safety. What are the performance
*  metrics that we're talking about? So in the end, you care about end safety. That's in the end what
*  keeps you... That's what's deceptive where there's a lot of companies that have a great demo.
*  The path from a really great demo to being able to go driverless can be deceptively long, even when
*  that demo looks like it's driverless quality. And the difference is that the thing that keeps
*  you from going driverless is not the stuff you encounter on a demo. It's the stuff that you
*  encounter once in a 100,000 miles or 500,000 miles. And so that is at the root of what is most
*  challenging about going driverless because any issue you encounter, you can go and fix it,
*  but how do you know you didn't create five other issues that you haven't encountered yet?
*  So those were painful learnings in Waymo's history that Waymo went through and led to us then finally
*  being able to go driverless in Phoenix and now are at the heart of how we develop. Evaluation
*  is simultaneously evaluating final kind of end safety of how ready are you to go driverless,
*  which may be as direct as what is your human relative kind of collision rate for all these
*  types of scenarios and severities to make sure that you're better than a human bar by a good amount.
*  But that's actually the most useful for development. For development, it's much more
*  kind of analog metrics that are part of the art of finding what are the properties of driving
*  that give you a way quicker signal that's more sensitive than a collision that can correlate to
*  the quality you care about and push the feedback loop to all of your development.
*  A lot of these are, for example, comparisons to human drivers, like manual drivers. How do you do
*  relative to a human driver in various dimensions or various circumstances?
*  Can I ask you a tricky question? So if I brought you a truck, how would you test it?
*  Okay. Alan Turing came along and you said- This one's, can't tell if it's a human driver or
*  an autonomous driver. Yeah. But not the human because humans are flawed.
*  It's different, but yeah. How do you actually know you're ready basically? How do you know
*  it's good enough? Yeah. And by the way, this is the reason why Waymo released a safety framework
*  for the car side because one, it sets the bar so nobody cuts below it and does something bad for
*  the field that causes an accident. Two, it's to start the conversation on framing what does
*  this need to look like. Same thing we'll end up doing for the trucking side. It ends up being
*  different portfolio of approaches. There's easy things like, are you compliant with all these
*  fundamental rules of the road? You never drive above the speed limit. That's actually pretty easy.
*  You can fundamentally prove that it's either impossible to violate that rule or that in these,
*  you can itemize the scenarios where that comes up and you can do a test and show that you pass that
*  test and therefore you can handle that scenario. And so those are traditional structured testing
*  system engineering approaches where you can just, fault rates is another example where
*  when something fails, how do you deal with it? You're not going to drive and randomly wait for
*  it to fail. You're going to force a failure and make sure that you can handle it and close courses
*  and simulation or on the road and run through all the permutations of failures, which you can
*  oftentimes for some parts of system itemize like hardware. The hardest part is behavioral where
*  you have just infinite situations that could in theory happen and you want to figure out the
*  combinations of approaches that can work there. You can probably pass the Turing test pretty
*  quickly even if you're not completely ready for driverless because the events that are really
*  hard will not happen that often. Just to give you a perspective, a human has a serious accident on a
*  freeway, like a truck driver on a freeway has, there's a serious event happens once every 1.3
*  million miles and something that actually has like a really serious injury is 28 million miles. And
*  so those are really rare and so you could have a driver that looks like it's ready to go, but you
*  have no signal on what happens there. And so that's where you start to get creative on combinations
*  of sampling and statistical arguments, focused structured arguments where you can kind of
*  simulate those scenarios and show that you can handle them and metrics that are correlated with
*  what you care about, but you can measure much more quickly and get to a right answer. And that's what
*  makes it pretty hard. And in the end, you end up borrowing a lot of properties from aerospace and
*  space shuttles and so forth where you don't get the chance to launch it a million times just to
*  say you're ready because it's too expensive to fail. And so you go through a huge amount of
*  structured approaches in order to validate it. And then by thoroughness, you can make a strong
*  argument that you're ready to go. This is actually a harder problem in a lot of ways though, because
*  you can think of a space shuttle as getting to a fixed point or an airplane and you freeze the
*  software and then you prove it and you're good to go. Here you have to get to a driverless quality
*  bar, but then continue to aggressively change the software even while you're driverless.
*  And so- And also the full range of environment that there's an external environment with a shuttle,
*  you're basically testing the systems, the internal stuff. And you have a lot of control in the
*  external stuff. Yeah. And the hard part is how do you know you didn't get worse in something that
*  you just changed? Yes, sure. And so in a lot of ways, the Turing test starts to fail pretty
*  quickly because you start to feel driverless quality pretty early in that curve. If you think
*  about it, in most really good AV demos, maybe you'll sit there for 30 minutes, right? So you've
*  driven 15 miles or something like that. To go driverless, what's the rate of issues that you
*  need to have you won't even encounter? So let's try something different then. Let's try a different
*  version of the Turing test, which is an IQ test. So there's these difficult questions of increasing
*  difficulty. They're designed, you don't know them ahead of time. Nobody knows the answer to them.
*  And so is it possible to in the future orchestrate basically really difficult course almost of like,
*  yeah, that maybe change every year and that represent if you can pass these,
*  they don't necessarily represent the full spectrum. That's it. Yeah. They won't be conclusive,
*  but you can at least get a really quick read and filter. Yeah. Like you're able to,
*  because you didn't know them ahead of time. Like, I don't know, probably like construction zones,
*  failures. Or driving anywhere in Russia. Yeah. Yeah, exactly. Snow. Weather, cut-ins,
*  dense traffic, kind of merging, lane closures, animal foreign objects on a road that pop out
*  on short notice, mechanical failures, sensor breaking, tire popped, weird behaviors by other
*  vehicles like a hard brake, something reckless that they've done, fouling of sensors like bugs or birds,
*  you know, poop or something. But yeah, like you have these like kind of like extreme conditions
*  where like you have a nasty construction zone where everything shuts down and you have to like
*  get pulled to the other side of the freeway with a temporary lane like that. Those are sort of
*  conditions where we do that to ourselves. We itemize everything that could possibly happen
*  to give you a starting point to how to think about what you need to develop. And at the end
*  of the day, there's no substitute for real miles. If you think of traditional ML, like you know how
*  there's like a validation set where you hold out some data and like real world driving is
*  the ultimate validation set. That's the, in the end, like the cleanest signal. But you can do
*  a really good job on creating an obstacle course. And you're absolutely right. Like at the end,
*  if there was such a thing as automating and kind of a readiness, it would be these extreme
*  conditions like a red light runner, right? A really reckless pedestrian that's jaywalking,
*  a cyclist that makes like a really awkward maneuver. That's actually what keeps you from
*  going driverless. Like in the end, that is the long tail. Yeah. And it's interesting to think
*  about that. That to me is the touring test. Touring test means a lot of things, but to me,
*  in driving the touring test is exactly this validation set that is handcrafted. I don't know
*  if you know him. There's a guy named Francois Chalet. He designed, he thinks about like how
*  to design a test for general intelligence. He designs these IQ tests for machines and the
*  validation set for him is handcrafted. And that it requires like human genius or ingenuity to
*  create a really good test. And you hold, you truly hold it out. It's an interesting perspective on
*  the validation set, which is like, make that as hard as possible, not a generic representation
*  of the data, but this is the hardest. The hardest. Yeah. It's like go. You'll never
*  out fully itemize all the world states that you'll expand. And so you have to come up with
*  different approaches. And this is where you start hitting the struggles of ML, where ML is fantastic
*  at optimizing the average case. It's a really unique craft to think about how you deal with
*  the worst case, which is what we care about in the AV space when using an ML system on something
*  that occurs like super infrequently. So like, you don't care about the worst case really on ads,
*  because if you miss a few, it's not a big deal, but you do care about it on the driving side.
*  And so typically like you'll never fully enumerate the world. And so you have to take
*  a step back and abstract away. What are the signals that you care about and the properties
*  of a driver that correlate to defensive driving and avoiding nasty situations that even though
*  you'll always be surprised by things you'll encounter, you feel good about your ability
*  to generalize from what you've learned. All right. Let me ask you a tricky question.
*  So to me, the two companies that are building at scale, some of the most incredible robots ever
*  built is Waymo and Tesla. So there's very distinct approaches, technically, philosophically,
*  in these two systems. Let me ask you to play sort of devil's advocate and then the devil's advocate
*  to the devil's advocate. It's a bit of a race. Of course, everyone can win. But if Waymo wins this
*  race to level four, which why would they win? What aspect of the approach do you think would be the
*  winning aspect? And if Tesla wins, why would they win? And which aspect of their approach would be
*  the reason? Just building some intuition, almost not from a business perspective, for many of that,
*  just technically. Yeah. Yeah. And we could summarize, I think maybe you can correct me,
*  one of the more distinct aspects is Waymo has a richer suite of sensors as LiDAR and Vision.
*  Tesla now removed radar. They do Vision only. Tesla has a larger fleet of vehicles operated
*  by humans. So it's already deployed out in the field and it's a larger, what do you call it,
*  operational domain. And then Waymo is more focused on a specific domain and growing it
*  with fewer vehicles. So both are fascinating approaches. I think there's a lot of brilliant
*  ideas. Nobody knows the answer. So I'd love to get your comments on this lay of the land.
*  Yeah, for sure. So maybe I'll start with Waymo. And you're right, both incredible companies and
*  just a gigantic respect to everything Tesla's accomplished and how they pushed the field forward
*  as well. So on the Waymo side, there is a fundamental advantage in the fact that it is
*  focused and geared towards L4 from the very beginning. We've customized the sensor suite
*  for it, the hardware, the compute, the infrastructure, the tech stack, and all of the
*  investment inside the company. That's deceptively important because there's a giant spectrum of
*  problems you have to solve in order to really do this from infrastructure to hardware to autonomy
*  stack to the safety framework. And that's an advantage because there's a reason why it's the
*  fifth generation hardware and why all of those learnings went into the DIMEware program.
*  It becomes such an advantage because you learn a lot as you drive and you optimize for the best
*  information you have. But fundamentally, there's a big, big jump, like every order of magnitude
*  that you drive in numbers of miles in what you learn. And the gap from really decent progress
*  for L2 and so forth to what it takes to actually go L4. And at the end of the day,
*  there's a feeling that Waymo has, there's a long way to go. Nobody's won, but there's a lot of
*  advantages in all of these buckets where it's the only company that has shipped a fully driverless
*  service. We can go and you can use it and it's at a decently sizable scale. And those learnings
*  can feed forward how to solve the more general problems. And you see this process, you've deployed
*  in Chandler. You don't know the timeline exactly, but you could see the steps.
*  They seem almost incremental. The steps become more engineering than totally blind R&D.
*  Because it works in one place and then you move to another place and you grow it this way.
*  And just to give you an example, we fundamentally changed our hardware and our software stack
*  almost entirely from what when driverless in Phoenix to what is the current generation of
*  the system on both sides. Because the things that got us to driverless, even though it got
*  to driverless way beyond human relative safety, it is fundamentally not well set up to scale
*  in an exponential fashion without getting into huge scaling pains. And so those learnings,
*  you just can't shortcut. And so that's an advantage. And so there's a lot of open challenges
*  to get through, technical, organizational, how do you solve problems that are increasingly
*  broad and complex like this work on multiple products. But there's a few in that, okay,
*  balls in our court. There's a head start there. Now we got to go and solve it.
*  And I think that focus on L4, it's a fundamentally different problem. If you think about it,
*  let's say we were designing an L2 truck that was meant to be safer and help a human.
*  You could do that with far less sensors, far less complexity and provide value very quickly,
*  arguably with what we already have today, just packaged up in a good product. But
*  you would take a huge risk in having a gap from even the like compute and sensors,
*  not to mention the software to then jump from that system to an L4 system. So it's a huge risk,
*  basically. So I can, let me allow me to be the person that plays the devil's advocate
*  on the argue for the Tesla approach. So that the what you just laid out makes perfect sense.
*  And it's exactly right. There are some open questions here, which is it's possible that
*  investing more in faster data collection, which is essentially what Tesla is doing,
*  will get us there faster if the sensor suite doesn't matter as much and machine learning can
*  do a lot of the work. This is the open question is how much is the thing you mentioned before,
*  how much of driving can be end to end learned? That's the open question. Obviously, the Waymo
*  and the vision only machine learning approach will solve driving eventually, both.
*  The question is of timeline, what's faster? That's right. And what you mentioned, if I were
*  to make the opposite argument, like what puts Tesla in the strongest position, it's data. That
*  is their superpower where they have an access to real world data effectively with a safety driver.
*  Yes. They found a way to get paid by safety drivers versus safer safety drivers. It's brilliant.
*  But all joking aside, one, it is incredible that they've built a business that's incredibly
*  successful that can now be a foundation and bootstrap really aggressive investment in
*  the autonomy space. If you can do it, that's always an incredible advantage. And then the data
*  aspect of it, it is a giant amount of data if you can use it the right way to then solve the problem.
*  But the ability to collect and filter through the things to the things that matter at real world
*  scale at a large distribution, that is huge. It's a big advantage. And so then the question becomes,
*  can you use it in the right way? And do you have the right software systems and hardware systems
*  in order to solve the problem? And you're right that in the long term, there's no reason to believe
*  that pure camera systems can't solve the problem that humans obviously are solving with vision
*  systems. But it's a risk. So there's no argument that it's not a risk. And it's already such a
*  hard problem. And so much of that problem, by the way, is even beyond the perception side,
*  some of the hardest elements of the problem are on the behavioral side and decision making and
*  the long tail safety case. If you are adding risk and complexity on the input side from perception,
*  you're now making a really, really hard problem, which on its own is still almost
*  insurmountably hard, even harder. And so the question is just how much. And this is where
*  you can easily get into a little bit of a trap where, similar to how do you evaluate how good
*  an AV company's product is, you go and you do a trial, kind of a test run with them, a demo run,
*  which they've kind of optimized like crazy and so forth. And it feels good. Do you put any weight
*  in that? You know that that gap is kind of pretty large still. Same thing on the perception case.
*  The long tail of computer vision is really, really hard. And there's a lot of ways that
*  that can come up. And even if it doesn't happen that often at all, when you think about the safety
*  bar and what it takes to actually go full driverless, not like incredible assistance driverless,
*  but full driverless, that bar gets crazy high. And not only do you have to solve it on the
*  behavioral side, but now you have to push computer vision beyond arguably where it's ever been pushed.
*  And so you now on top of the broader AV challenge, you have a really hard perception challenge as
*  well. So there's perception, there's planning, there's human robot interaction. To me, what's
*  fascinating about what Tesla is doing is in this march towards level four, because it's in the
*  hands of so many humans, you get to see video, you get to see humans. I mean, forget, forget
*  companies, forget businesses. It's fascinating for humans to be interacting with robots.
*  That's incredible. And they're actually helping kind of push it forward. And that is valuable,
*  by the way, where even for us, a decent percentage of our data is human driving. We intentionally
*  have humans drive higher percentage than you might expect, because that creates some of the best
*  signals to train the autonomy. And so that is on its own value. So together, we're kind of learning
*  about this problem in an applied sense, just like you had with Cosmo. When you're chasing an actual
*  product that people are going to use, robot based product that people are going to use, you have to
*  contend with the reality of what it takes to build a robot that successfully perceives the world and
*  operates in the world. And what it takes to have a robot that interacts with other humans in the
*  world. And that's like, to me, one of the most interesting problems humans have ever undertaken,
*  because you're in trying to create an intelligent agent that operates in a human world.
*  You're also understanding the nature of intelligence itself. How hard is driving? It's still
*  not answered to me. I still don't understand.
*  Yeah. And all the subtle cues, even little things like your interaction with a pedestrian
*  where you look at each other and just go, okay, go. That's hard to do without a human driver,
*  and you're missing that dimension. How do you communicate that? So there's really,
*  really interesting elements here. Now, here's what's beautiful. Can you imagine that when
*  autonomous driving is solved, how much of the technology foundation of that space can go and
*  have tremendous, just transformative impacts on other problem areas and other spaces that have
*  subsets of these same problems? It's just incredible to think about that.
*  It's both a pro and a con is with autonomous driving is so safety critical.
*  So once you solve it, it's beautiful because there's so many applications that are a lot
*  less safety critical. But it's also the con of that is it's so safety. It's so hard to solve.
*  And the same journalists that you mentioned to get excited for a demo are the ones who
*  who write long articles about the failure of your company if there's one accident
*  that's based on a robot. And it's just society is so tense and waiting for failure of robots.
*  You're in such a high-stake environment. Failure has such a high cost.
*  And it slows down development. It's hard.
*  It slows down development.
*  Yeah. The team definitely noticed that once you go driverless, we were driverless in Phoenix and
*  you continue to iterate, your iteration pace slows down because your fear of regression
*  forces so much more rigor that obviously you have to find a compromise on like,
*  okay, well, how often do we release driverless builds? Because every time you release a driverless
*  build, you have to go through this validation process, which is very expensive and so forth.
*  So it is interesting. It is one of the hardest things. There's no other industry where
*  you would not like you wouldn't release products way, way quicker when you start to kind of provide
*  even portions of the value that you provide. Healthcare maybe is the other one.
*  Yeah, that's right.
*  But at the same time, we've gotten there where you think of like surgery, right? You have surgery,
*  there's always a risk, but it's really, really bounded. You know that there's an accident rate
*  when you go out and drive your car today, right? And you know what the fatality rate in the US is
*  per year. We're not banning driving because there was a car accident, but the bar for us is way
*  higher and we hold ourselves very serious to it where you have to not only be better than a human,
*  but you probably have to like at scale be far better than a human by a big margin.
*  And you have to be able to like really, really thoughtfully explain all of the ways that we
*  validate that becomes very comfortable for humans to understand because a bunch of jargon that we
*  use internally just doesn't compute. At the end of the day, we have to be able to explain to society,
*  how do we quantify the risk and acknowledge that there is some non-zero risk, but it's far above a
*  human relative safety. See, here's the thing to push back a little bit and bring Cosmo back in
*  the conversation. You said something quite brilliant at the beginning of this conversation,
*  I think probably applies for autonomous driving, which is, you know, there's this desire to make
*  autonomous cars much safer than human driven cars. But if you create a product that's really
*  compelling and is able to explain both the leadership and the engineers and the product
*  itself can communicate intent, then I think people may be able to be willing to put up with a thing
*  that might be even riskier than humans because they understand the value of taking risks.
*  You mentioned the speed limit. Humans understand the value of going over the speed limit. Humans
*  understand the value of going fast through a yellow light. When you're in Manhattan streets,
*  pushing through crossing pedestrians, they understand that. I mean, this is a much more
*  tense topic of discussion, so this is just me talking. So in Cosmo's case, there was something
*  about the way this particular robot communicated, the energy it brought, the intent it was able to
*  communicate to the humans that you understood that of course it needs to have a camera.
*  Of course it needs to have this information. And in that same way, to me, of course a car needs
*  to take risks. Of course there's going to be accidents. That's what, like that's, you know,
*  if you want a car that never has an accident, have a car that just doesn't go anywhere.
*  And so that, but that's tricky because that's not a robotics problem.
*  Many accidents are not even due to you, right? Obviously it's, so there's a big difference though.
*  You are, that's not a personal decision. You're also impacting obviously kind of the rest of the
*  road and we're facilitating it, right? And so there's a higher kind of ethical and moral bar,
*  which obviously then translates into as a society and from a regulatory standpoint,
*  kind of like what comes out of it where it's hard for us to ever see this even being a
*  debate in the sense that like you have to be beyond reproach from a safety standpoint,
*  because if you're wrong about this, you could set the entire field back a decade, right?
*  See, I, this is me speaking. I think if we look into the future, there will be,
*  I personally believe this is me speaking, that there will be less and less focus on safety.
*  It's still very, very high.
*  Yeah. Meaning like after autonomy is very common and accepted.
*  Yeah. It's not so common as everywhere, but there has to be a transition because I think
*  for innovation, just like you were saying, to explore ideas, you have to take risks.
*  And I think if autonomy in the near term is to become prevalent in society,
*  I think people need to be more willing to understand the nature of risk, the value of risk.
*  It's very difficult, you're right, of course, with driving, but that's the fascinating nature
*  of it. It's a life and death situation that brings value to millions of people. So you have to figure
*  out what do we value about this world? How much do we value? How deeply do we want to avoid
*  hurting other humans?
*  That's right. And there is a point where like, you can imagine a scenario where Waymo has a system
*  that is, even when it's like kind of beyond human relative safety and provably statistically will
*  save lives, there is a thoughtful navigation of that fact versus just kind of society readiness
*  and perception and education of society and regulators and everything else where like,
*  it's multi-dimensional and it's not a purely logical argument, but ironically, the logic
*  can actually help with the emotions. And just like any technology, there's early adopters and
*  then there's kind of like a curve that happens after it.
*  And eventually celebrities, you get The Rock in a Waymo vehicle and then everybody just comes.
*  And then everybody calms down because The Rock likes it.
*  If you post the...
*  Yeah. And it's an open question on how this plays out. Maybe we're pleasantly surprised and
*  it's just like people just realize that this is such a neighbor of life and efficiency and cost
*  and everything that there's a pull. At some point, I should fully believe that this will go from a
*  thoughtful kind of movement and tiptoeing and kind of like a push to society realizes how
*  wonderful of an enabler this could become and it becomes more of a pull.
*  And hard to know exactly how that will play out, but at the end of the day, both
*  the goods transportation and the people transportation side of it has that property
*  where it's not easy. There's a lot of open questions and challenges to navigate. And there's
*  obviously the technical problems to solve as a kind of prerequisite, but they have such an
*  opportunity that is on a scale that very few industries in the last 20, 30 years have even
*  had a chance to tackle that maybe we're pleasantly surprised by how much that tipping point in a
*  really short amount of time actually turns into a societal pull to kind of embrace the benefits of
*  this. Yeah, I hope so. It seems like in the recent few decades, there's been tipping points
*  of technologies where like overnight things change. It's like from taxis to ride sharing
*  services, all that, that shift. I mean, there's just shift after shift after shift that requires
*  digitization and technology. I hope we're pleasantly surprised in this. So there's millions of long
*  haul trucks now in the United States. Do you see a future where there's millions of Waymo trucks
*  and maybe just broadly speaking, Waymo vehicles, just like ants running around United States
*  freeways and local roads? Yeah, and other countries too. You look back decades from now
*  and it might be one of those things that just feels so natural and then it becomes almost like
*  this kind of interesting kind of oddity that we had none of it like decades earlier. And
*  it'll take a long time to grow and scale. Very different challenges appear at every stage,
*  but over time, like this is one of the most enabling technologies that we have in the world
*  today. It'll feel like, you know, how was the world before the internet? How was the world
*  before mobile phones? Like it's going to have that sort of a feeling to it on both sides.
*  It's hard to predict the future, but do you sometimes think about weird ways it might change
*  the world? Like surprising ways. So obviously there's more direct ways where like there's
*  increases efficiency. It will enable a lot of kind of logistics optimizations kind of things.
*  It will change our probably our roadways and all that kind of stuff, but it could also change
*  society in some kind of interesting ways. Do you ever think about how might change cities? How
*  might change your lives? All that kind of stuff. Yeah. You can imagine city where people live
*  versus work becoming more distributed because the pain of commuting becomes different, just easier.
*  And I don't know, there's a lot of options that open up the way out of cities themselves
*  and how you think about car storage and parking obviously just enables a completely different type
*  of experience in urban environments. I think there was like a statistic that something like
*  30 percent of the traffic in cities during rush hour is caused by a pursuit of parking or some
*  like some really high stats. So those obviously kind of open up a lot of options.
*  Flexibility on goods will enable new industries and businesses that never existed before because
*  now the efficiency becomes more palatable. Good delivery timing, consistency and flexibility is
*  going to change. The way we distribute the logistics network will change. The way we then
*  can integrate with warehousing, with shipping ports, you can start to think about greater
*  automation through the whole kind of stack and how that supply chain, the ripples become much more
*  agile versus like very grindy the way they are today where just the adaptation is like very
*  tough and there's like a lot of constraints that we have. I think it'll be great for the environment.
*  It'll be great for safety where like probably about 95 percent of accidents today statistically
*  are due to just attention or things that are preventable with the strengths of automation.
*  Yeah and it'll be one of those things where like industries will shift but the net creation is
*  going to be massively positive and then we just have to be thoughtful about the negative implications
*  that will happen in local places and adjust for those. But I'm an optimist in general for
*  the technology where you could argue a negative on any new technology but you start to kind of
*  see that if there is a big demand for something like this, in almost all cases, it's an enabling
*  factor that's going to propagate through society and particularly as life expectancies get longer
*  and so forth, there's just a lot more need for a greater percentage of the population to kind of
*  just be serviced with a high level of efficiency because otherwise we're going to have a really
*  hard time kind of scaling to what's ahead in the next 50 years. Yeah and you're absolutely right.
*  Every technology has negative consequences or positive consequences and we tend to focus on
*  the negative a little bit too much. In fact, autonomous trucks are often brought up as an
*  example of artificial intelligence and robots in general taking our jobs and as we've talked about
*  briefly here, we talk a lot with Steve, it is a concern that automation will take away certain jobs,
*  it'll create other jobs, so there's temporary pain, hopefully temporary, but pain is pain and
*  people suffer and that human suffering is really important to think about. But trucking is,
*  there's a lot written on this, is I would say far from the thing that would cause the most
*  pain. Yeah, there's even more positive properties about trucking where not only is there just a
*  huge shortage which is going to increase, the average age of truck drivers is getting closer
*  to 50 because the younger people aren't wanting to come into it, they're trying to incentivize,
*  lower the age limit, all these sort of things and the demand is just going to increase and the least
*  favorable, I mean it depends on the person, but in most cases the least favorable types of routes
*  are the massive long-haul routes where you're on the road away from your family 300 plus days a year.
*  Steve talked about the pain of those kind of routes from a family perspective, you're
*  basically away from family, it's not just hours, you work insane hours, but it's also just time
*  away from family. It's rough. Obesity rate is through the roof because you're just sitting all day,
*  it's really, really tough and that's also where the biggest safety risk is because of fatigue and
*  so when you think of the gradual evolution of how trucking comes in, first of all,
*  it's not overnight, it's going to take decades to kind of phase in all the, like there's just a long,
*  long, long road ahead, but the routes and the portions of trucking that are going to require
*  humans the longest and benefit the most from humans are the short haul and most complicated
*  kind of more urban routes which are also the more pleasant ones which are less continual driving time,
*  more flexibility on geography and location and you get to kind of sleep at your own home.
*  And very importantly, if you optimize the logistics, you're going to use humans much better
*  and thereby pay them much better because one of the biggest problems is truck drivers currently
*  are paid by how much they drive so they really feel the pain of inefficient logistics because
*  if they're just sitting around for hours which they often do not driving, waiting,
*  they're not getting paid for that time and that logistics has a significant impact on the quality
*  of life of a truck driver. And a high percentage of trucks are empty because of inefficiencies in the
*  system. Yeah, it's one of those things where, and the other thing is when you increase the
*  efficiency of a system like this, the overall net volume of the system tends to increase,
*  the entire market cap of trucking is going to go up when the efficiency improves and facilitates
*  both growth in industries and better utilization of trucking. And so that on its own just creates
*  more and more demand which of all the places where AI comes in and starts to really kind of reshape
*  an industry, this is one of those where there's just a lot of positives that for at least any
*  time in the foreseeable future seem really lined up in a good way to kind of come in and help with
*  the shortage and start to kind of optimize for the routes that are most dangerous and most painful.
*  Yeah, so this is true for trucking but if we zoom out broader, automation and AI does technology
*  broadly I would say but automation is a thing that has a potential in the next couple of decades to
*  shift the kind of jobs available to humans. Yes. And so that results in, like I said,
*  human suffering because people lose their jobs, there's economic pain there, and there's also a
*  pain of meaning. So for a lot of people, work is a source of meaning, it's a source of identity,
*  of pride, of pride in getting good at the job, pride in craftsmanship and excellence,
*  which is what truck drivers talk about. But this is true for a lot of jobs. And is that something
*  you think about as a sort of a roboticist zooming out from the trucking thing? Like where do you
*  think it would be harder to find activity and work that's a source of identity, a source of
*  meaning in the future? I do think about it because you want to make sure that you worry
*  about the entire system, not just the part of autonomy plays in it but what are the ripple
*  effects of it down the road. And on enough of a time window, there's a lot of opportunity to put in
*  the right policies, the right opportunities to kind of reshape and retrain and find those openings.
*  And so just to give you a few examples, both trucking and cars, we have remote assistance
*  facilities that are there to interface with customers and monitor vehicles and provide
*  very focused kind of assistance on areas where the vehicle may want to request help
*  in understanding an environment. So those are jobs that get created and supported.
*  I remember taking a tour of one of the Amazon facilities where you've probably seen the Kiva
*  systems robots, where you have these orange robots that have automated the warehouse,
*  kind of picking and collecting of items in this really elegant and beautiful way.
*  It's actually one of my favorite applications of robotics of all time.
*  I think it kind of came across a company like 2006, it was just amazing.
*  It's warehouse robots that transport little things.
*  So basically, instead of a person going and walking around and picking the seven items in your order,
*  these robots go and pick up a shelf and move it over in a row where the seven shelves that
*  contain the seven items are lined up in a laser or whatever points to what you need to get.
*  And you go and pick it and you place it to fill the order. And so the people are fulfilling the
*  final orders. What was interesting about that is that when I was asking them about the impact on
*  labor, when they transitioned that warehouse, the throughput increased so much that the jobs
*  shifted towards the final fulfillment, even though the robots took over entirely the search of the
*  items themselves. And the labor, the job stayed, it was actually the same amount of jobs, roughly
*  they were necessary, but the throughput increased by I think over 2X or some amount. So you have
*  these situations that are not zero sum games in this really interesting way. And the optimist to
*  me thinks that there's these types of solutions in almost any industry where the growth that's
*  enabled creates opportunities that you can then leverage. But you've got to be intentional about
*  finding those and really helping make those links because even if you make the argument that
*  there's a net positive, locally there's always tough hits that you've got to be very careful
*  about. That's right. You have to have an understanding of that link because there's
*  a short period of time, whether training is required or just mental transition or physical
*  or whatever is acquired, that's still going to be short term pain. The uncertainty of it, there's
*  families involved. It exceptionally is difficult on a human level and you have to really think
*  about that. You can't just look at economic metrics always, it's human beings. That's right.
*  And you can't even just take it as like, okay, well we need to subsidize or whatever because
*  there is an element of just personal pride where majority of people don't want to just be okay,
*  but they want to actually have a craft like you said and have a mission and feel like they're
*  having a really positive impact. And so my personal belief is that there's a lot of
*  transferability and skill set that is possible, especially if you create a bridge and an investment
*  to enable it. And to some degree that's our responsibility as well in this process.
*  You mentioned Kiva robots, Amazon. Let me ask you about the Astro robot, which is, I don't know if
*  you've seen it, it's Amazon has announced that it's a home robot that they have a screen looks
*  awfully a lot like Cosmo has, I think different vision probably. What are your thoughts about
*  like home robotics in this kind of space? There's been quite a bunch of home robots,
*  social robots that very unfortunately have closed their doors that for various reasons,
*  perhaps they were too expensive. There's been the manufacturing challenges, all that kind of stuff.
*  What are your thoughts about Amazon getting into the space?
*  Yeah, we had some signs that they're getting into like long, long, long, long ago. Maybe they were
*  too interested in Cosmo and I turned our conversations, but they're also very good
*  partners actually for us as we kind of just integrated a lot of shared technology. But
*  if I could also get your thoughts on, you could think of Alexa as a robot as well, Echo.
*  Do you see those as fundamentally different just because you can move and look around?
*  Is that fundamentally different than the thing that just sits in place?
*  It opens up options. But my first reaction is I think like, I have my doubts that this one's
*  going to hit the mark because I think for the price point that it's at and the kind of functionality
*  and value propositions that they're trying to put out, it's still searching for the killer
*  application that justifies, I think it was like a $1,500 price point or kind of somewhere on there.
*  That's a really high bar. So there's enthusiasts and early adopters will obviously kind of pursue
*  it, but you have to really, really hit a high mark at that price point, which we always tried to,
*  we were always very cautious about jumping too quickly to the more advanced systems that we
*  really wanted to make, but would have raised the bar so much that you have to be able to hit it.
*  In today's cost structures and technologies, the mobility is an angle that hasn't been utilized,
*  but it has to be utilized in the right way. And so that's going to be the biggest challenge is like,
*  can you meet the bar of what the mass market consumer like, think like our neighbors,
*  our friends, parents, like would they find a deep, deep value like in this at a mass scale
*  that justifies the price point? I think that's in the end, one of the biggest challenges for
*  robotics, especially consumer robotics, where you have to kind of meet that bar,
*  it becomes very, very hard. And there's also the higher bar,
*  just like you were saying with Cosmo of, you know, a thing that can look one way and then turn around
*  and look at you. There's that's either a super desirable quality or super undesirable quality,
*  depending on how much you trust the thing. That's right. And so there's a, there's a
*  problem of trust to solve there. There's a problem of personality. It's the thing that is the
*  quote unquote problem that Cosmo solved so well is that there you trust the thing. And that has to
*  do with the company, with the leadership, with the intent that's communicated by the device and the
*  company and everything together. Yeah, exactly right. And so, and I think they also have to
*  retrace some of the like warnings on the character side where like, as usual, I think that's the place
*  where it's a lot of companies are great at the hardware side of it and can think about those
*  elements. And then there's like, you know, the thinking about the AI challenges, particularly
*  with the advantage of Alexa is a pretty huge boost for them. The character side of it for technology
*  companies is pretty novel territory. And so that will take some iterations. But yeah, I mean, I
*  hope, I hope this continued progress in the space and that thread doesn't kind of go dormant for too
*  long. And it's not, you know, it's going to take a while to kind of evolve into like the ideal
*  applications. But, you know, this is one of Amazon's, I guess like you could call it,
*  it's definitely like part of their DNA. But in many cases, it's also strength where they're very
*  willing to like iterate kind of aggressively and, and move quickly. Take risks. You have deep pockets
*  so you can get. Yeah. And then maybe have more misfires than an apple would. But, you know,
*  it's different styles and different approaches. And, you know, at the end of the day, it's like
*  there's a few familiar kind of elements there for sure, which was, you know, kind of, you know,
*  homage. There's one way to put it. So why is it so hard at a high level to build a robotics company,
*  a robotics company that lives for a long time? So if you look at, so I thought Cosmo for sure would
*  for a very long time that to me was exceptionally successful vision and idea and implementation.
*  iRobot is an example of a company that has pivoted in all the right ways to survive
*  and arguably thrive by focusing on the having like a, have a driver that constantly provides profit,
*  which is the vacuum cleaner. And of course there's like Amazon, what they're, what they're doing is
*  they're almost like taking risks so they can afford it because they have other sources of revenue.
*  Right. But outside of those examples, most robotics companies fail. Yeah. Why, why do they fail? Why
*  is it so hard to run a robotics company? iRobot's impressive because they found a really, really
*  great fit of where the technology could satisfy a really clear use case and need. And they did it
*  well and they didn't try to overshoot from a cost to benefit standpoint. Robotics is hard because
*  it like tends to be more expensive. It combines way more technologies than a lot of other types
*  of companies do. If I were to like say one thing that is maybe the biggest risk in like a robotics
*  company failing is that it can be either a technology in search of an application or they
*  try to fight off a kind of an offering that has a mismatch in kind of price to function. And
*  just the mass market appeal isn't there. And consumer products are just hard. It's just,
*  I mean, after all the years in it, like definitely kind of feel a lot of the battle scars because
*  you have, you know, you not only do you have to like hit the function, but you have to educate
*  and explain, get awareness up, deal with different types of consumers. Like, you know, there's a
*  reason why a lot of technologies sometimes start in the enterprise space and then kind of continue
*  forward in the consumer space. Even like, you know, you see AR like starting to kind of make
*  that shift with HoloLens and so forth in some ways. Consumers and price points that they're
*  willing to kind of be attracted in a mass market way. And I don't mean like, you know, 10,000
*  enthusiasts bought it, but I mean like, you know, 2 million, 10 million, 50 million, like mass market
*  kind of interest, you know, have bought it. That bar is very, very high. And typically robotics
*  is novel enough and non-standardized enough to where it pushes on price points so much
*  that you can easily get out of range where the capabilities and today's technology or just a
*  function that was picked just doesn't line up. And so that product market fit is very important.
*  So the space of killer apps or rather super compelling apps is much smaller because it's
*  easy to get outside of the price range. Yeah. And it's not constant, right? Like,
*  that's why like we picked off entertainment because the quality was just so low in physical
*  entertainment that we could, we felt we could leapfrog that and still create a really compelling
*  offering at a price point that was defensible. And we like that proved out to be true.
*  And over time, that same opportunity opens up in healthcare, in home applications, in, you know,
*  commercial applications, in kind of broader, more generalized interface, but there's missing pieces
*  in order for that to happen. And all of those have to be present for it to line up. And we see these
*  sort of trends in technology where, you know, kind of technologies that start in one place evolve and
*  kind of grow to another, some things start in gaming, some things start in space or aerospace,
*  and then kind of move into the consumer market. And sometimes it's just a timing thing, right?
*  Where how many stabs at what became the iPhone were there over the 20 years before that just
*  weren't quite ready in the function relative to the kind of price point and complexity.
*  And sometimes it's a small detail of the implementation that makes all the difference,
*  which is design is so important.
*  Something like the new generation UX, right? And that's tough. And oftentimes all of them
*  have to be there and it has to be like a perfect storm. But yeah, history repeats itself in a lot
*  of ways in a lot of these trends, which is pretty fascinating. Well, let me ask you about the
*  humanoid form. What do you think about the Tesla bot and humanoid robotics in general?
*  So obviously to me, autonomous driving, Waymo and the other companies working in the space,
*  that seems to be a great place to invest in potentially revolutionary application of robotics
*  application, folks application. What's the role of humanoid robotics? Do you think Tesla bot is
*  ridiculous? Do you think it's super promising? Do you think it's interesting, full of mystery?
*  Nobody knows. What do you think about this thing? Yeah, I think today humanoid form
*  robotics is research. There's very few situations where you actually need a humanoid form to solve
*  a problem. If you think about it, right? Like wheels are more efficient than legs. There's
*  joints and degrees of freedom beyond a certain point, just add a lot of complexity and cost.
*  If you're doing a humanoid robot, oftentimes it's in the pursuit of a humanoid robot,
*  not in the pursuit of an application for the time being. Especially when you have the gaps
*  and interface and AI that we talk about today. So anything you want does, I'm interested in
*  following. So there's an element of that. No matter how crazy it is, I just like,
*  I'll pay attention. I'm curious to see what comes out of it. So it's like you can't ever
*  ignore it, but it's definitely far afield from their core business, obviously.
*  What was interesting to me is I've disagreed with Elon a lot about this,
*  is to me the compelling aspect of the humanoid form and a lot of kind of robots, Cosmo for
*  example, is a human robot interaction part. From Elon Musk's perspective, Tesla bot has nothing to
*  do with the human. It's a form that's effective for the factory because the factory is designed
*  for humans. But to me, the reason you might want to argue for the humanoid form is because,
*  at a party, it's a nice way to fit into the party. The humanoid form has a compelling notion to it
*  in the same way that Cosmo is compelling. I would argue if we were arguing about this,
*  that it's cheaper to build a Cosmo like that form. But if you wanted to make an argument,
*  which I have with Jim Keller about, you could actually make a humanoid robot for pretty cheap.
*  It's possible. And then the question is, all right, if you're using an application where it
*  can be flawed, it can have a personality and be flawed in the same way that Cosmo is,
*  then maybe it's interesting for integration into human society. That's to me is an interesting
*  application of a humanoid form because humans are drawn, like I mentioned to you, legged robots.
*  We're drawn to legs and limbs and body language and all that kind of stuff. And even a face,
*  even if you don't have the facial features, which you might not want to have to reduce the creepiness
*  factor, all that kind of stuff. But yeah, that to me, the humanoid form is compelling. But in
*  terms of that being the right form for the factory environment, I'm not so sure.
*  Yeah. For the factory environment, right off the bat, what are you optimizing for? Is it strength?
*  Is it mobility? Is it versatility? That changes completely the look and feel of the robot that
*  you create. And almost certainly the human form is overdesigned for some dimensions and constrained
*  for some dimensions. And so what are you grasping? Is it big? Is it little? So you would customize it
*  and make it customizable for the different needs if that was the optimization. And then for the
*  other one, I could totally be wrong. I still feel that the closer you try to get to a human,
*  the more you're subject to the biases of what a human should be and you lose flexibility to shift
*  away from your weaknesses and towards your strengths. And that changes over time,
*  but there's ways to make really approachable and natural interfaces for robotic characters and
*  deployments in these applications that do not at all look like a human directly,
*  but that actually creates way more flexibility and capability and role and forgiveness and
*  interface and everything else. Yeah, it's interesting. But I'm still confused by the magic
*  I see in legged robots. Yeah. So there is a magic. So I'm absolutely amazed at it from a
*  technical curiosity standpoint and the magic that the Boston Dynamics team can do from walking and
*  jumping and so forth. Now, there's been a long journey to try to find an application for that
*  technology, but wow, that's incredible technology, right? So then you go towards, okay,
*  are you working back from a goal of what you're trying to solve or are you working
*  forward from a technology and then looking for a solution? And I think that's where
*  it's a bidirectional search oftentimes, but the two have to meet. And that's where humanoid robots
*  is kind of close to that in that it is a decision about a form factor and a technology that it
*  forces that doesn't have a clear justification on why that's the killer app from the other end.
*  But I think the core fascinating idea with the Tesla bot is the one that's carried by Waymo
*  as well, is when you're solving the general robotics problem of perception control, where
*  there's the very clear applications of driving, as you get better and better at it, when you have
*  Waymo driver, the whole world starts to kind of start to look like a robotics problem. So
*  it's very interesting for now. Detection, cost-plication, segmentation, tracking,
*  planning, like it's carried. So there's no reason, I mean, I'm not speaking for Waymo here, but
*  moving goods, there's no reason transformer like this thing couldn't take the goods up an elevator.
*  Like slowly expand what it means to move goods and expand more and more of the world
*  into a robotics problem. Well, that's right. And you start to like
*  think of it as an end-to-end robotics problem from like loading from everything. And even like the
*  truck itself, today's generation is integrating into today's understanding of what a vehicle is,
*  right? A Pacifica, Jaguar, the Freightliners from Daimler, there's nothing that stops
*  these us from like down the road after like starting to get to scale to like expand these
*  partnerships to really rethink what would the next generation of a truck look like
*  that is actually optimized for autonomy, not for today's world. And maybe that means a very
*  different type of trailer. Maybe that like there's a lot of things you could rethink on that front,
*  which is on its own, very, very exciting. Let me ask you, like I said, you went to the
*  Mecca of robotics, which is CMU, Carnegie Mellon University. You got a PhD there.
*  Maybe by way of advice and maybe by way of story and memories, what does it take to get a PhD
*  in robotics at CMU? And maybe you can throw in there some advice for people who are thinking about
*  doing work in artificial intelligence and robotics and are thinking about whether to get a PhD.
*  I was at CMU for undergrad as well and didn't know anything about robotics coming in and was
*  doing electrical computer engineering, computer science, and really got more and more into kind
*  of AI and then fell in love with autonomous driving. And at that point, like that was just
*  by a big margin, like such an incredible like central spot of development of investment in that
*  area. And so what I would say is that like robotics, like for all the progress that's
*  happened is still a really young field. There's a huge amount of opportunity. Now that opportunity
*  shifted where something like autonomous driving has moved from being very research and academics
*  driven to being commercial driven, where you see the investments happening in commercial.
*  Now there's other areas that are much younger and you see like kind of grasping at an impalation,
*  making kind of the same sort of journey that like autonomy made and there's other areas as well.
*  What I would say is the space moves very quickly. Anything you do a PhD in, like it is in most areas,
*  will evolve and change as technology changes and constraints change and hardware changes and the
*  world changes. And so the beautiful thing about robotics is it's super broad. It's not a narrow
*  space at all and it could be a million different things in a million different industries. And so
*  it's a great opportunity to come in and get a broad foundation on AI, machine learning,
*  computer vision, systems, hardware, sensors, all these separate things. You do need to like go deep
*  and find something that you're like really, really passionate about. Obviously, like just like any PhD,
*  this is like a five, six year kind of endeavor and you have to love it enough to go super deep
*  to learn all the things necessary to be super deeply functioning in that area and then contribute
*  to it in a way that hasn't been done before. And in robotics, that probably means more breadth
*  because robotics is rarely kind of like one particular kind of narrow technology.
*  And it means being able to collaborate with teams where like one of the coolest aspects of like
*  the experience that I kind of cherish in our PhD is that we actually had a pretty large
*  AV project that for that time was like a pretty serious initiative where you got to like partner
*  with a larger team and you had the experts in perception and the experts in planning and the
*  staff and the mechanical engineers. For the DARPA challenge. So I was working on a project called
*  UPI back then, which was basically the off-road version of the DARPA challenge. It was a DARPA
*  funded project for basically like a large off-road vehicle that you would like drop and then give it
*  a waypoint 10 kilometers away and it would have to navigate a completely unstructured environment.
*  In an off-road environment. Yeah. So like forests, ditches, rocks, vegetation. And so it was like a
*  really, really interesting kind of a hard problem where like wheels would be up to my shoulders.
*  It's like gigantic, right? Yeah. By the way, AV for people stands for autonomous vehicles.
*  Autonomous vehicles, yeah. Sorry. And so what I think is like the beauty of robotics, but also
*  kind of like the expectation is that there's spaces in computer science where you can be very, very
*  narrow and deep. Robotics, the necessity, but also the beauty of it is that it forces you to be
*  excited about that breadth and that partnership across different disciplines that enable it.
*  But that also opens up so many more doors where you can go and you can do robotics in almost any
*  category where robotics isn't really an industry. It's like AI, right? It's like the application of
*  physical automation to all these other worlds. And so you can do robotic surgery, you can do
*  vehicles, you can do factory automation, you can do healthcare, you can do like
*  leverage the AI around the sensing to think about static sensors and scene understanding.
*  So I think that's got to be the expectation and the excitement. And it breeds people that are
*  probably a little bit more collaborative and more excited about working in teams.
*  If I could briefly comment on the fact that the robotics people I've met in my life
*  from CMU and MIT, they're really happy people. Yeah. Because I think it's the collaborative thing.
*  I think you don't... You're not like sitting in the fourth basement.
*  Yes, exactly. Which when you're doing machine learning purely software, it's very tempting
*  to just disappear into your own hole and never collaborate. And that breeds a little bit more
*  of the silo mentality of like, I have a problem. It's almost like negative to talk to somebody
*  else or something like that. But robotics folks are just very collaborative, very friendly.
*  And there's also an energy of like, you get to confront the physics of reality often, which is
*  humbling and also exciting. So it's humbling when it fails and exciting when it finally works.
*  It's like a purity of the passion. You got to remember that like right now,
*  robotics and AI is like just all the rage and autonomous vehicles and all this. Like 15 years
*  ago and 20 years ago, it wasn't that deeply lucrative. People that went into robotics,
*  they did it because they thought it was just the coolest thing in the world to make physical
*  things intelligent in the real world. And so there's a raw passion where they went into it
*  for the right reasons and so forth. And so it's really great space. And that organizational
*  challenge, by the way, when you think about the challenges in AV, we talk a lot about the technical
*  challenges, the organizational challenges through the roof where you think about what it takes to
*  build an AV system and you have companies that are now thousands of people.
*  And you look at other really hard technical problems like an operating system,
*  it's pretty well established. You kind of know that there's a file system, there's virtual memory,
*  there's this, there's that, there's like caching and there's like a really reasonably well
*  established modularity and APIs and so forth. And so you can kind of like scale it in an efficient
*  fashion. That doesn't exist anywhere near to that level of maturity in autonomous driving right now.
*  And tech stacks are being reinvented, organizational structures are being reinvented.
*  You have problems like pedestrians that are not isolated problems. They're part sensing,
*  part behavior prediction, part planning, part evaluation. And like one of the biggest challenges
*  is actually how do you solve these problems where the mental capacity of a human is starting to get
*  strained on how do you organize it and think about it where you have this multi-dimensional
*  matrix that needs to all work together. And so that makes it kind of cool as well because it's
*  not solved at all from what does it take to actually scale this? And then you look at other
*  gigantic challenges that have been successful and are way more mature, there's a stability to it.
*  And like maybe the autonomous vehicle space will get there, but right now just as many
*  technical challenges as they are, they're like organizational challenges. And how do you like
*  solve these problems that touch on so many different areas and efficiently tackle them
*  while maintaining progress among all these constraints while scaling?
*  By way of advice, what advice would you give to somebody thinking about doing a robotic startup?
*  You mentioned Cosmo, somebody that wanted to carry the Cosmo flag forward, the Anki flag forward,
*  looking back at your experience, looking forward at a future that will obviously have such robots.
*  What advice would you give to that person? Yeah. It was the greatest experience ever. And it's like,
*  there are things you learn navigating a startup that you'll never... It was very hard to encounter
*  that in a typical kind of work environment. And it's wonderful. You got to be ready for it.
*  It's not as good... The glamour of a startup, there's just brutal emotional swings up and down.
*  And so having co-founders actually helps a ton. I could not imagine doing it solo, but having
*  at least somebody where on your darkest days, you can really openly just have that conversation
*  wean onto somebody that's in the thick of it with you helps a lot. What I would say...
*  What was the nature of darkest days and the emotional swings? Is it worried about the funding?
*  Is it worried about whether any of your ideas are any good or ever were good? Is it the self-doubt?
*  Is it facing new challenges that have nothing to do with the technology, like organizational,
*  human resources, that kind of stuff? Yeah. You come from a world in school
*  where you feel that you put in a lot of effort and you'll get the right result and input translates
*  proportional to output and you need to solve the set or do whatever and just kind of get it done.
*  Now, PhD tests out a little bit, but at the end of the day, you put in the effort, you tend to
*  come out with enough results to get a PhD. In the startup space, you could talk to 50 investors and
*  they just don't see your vision and it doesn't matter how hard you tried and pitched. You could
*  work incredibly hard and you have a manufacturing defect and if you don't fix it, you're out of
*  business. You need to raise money by a certain date and you got to have this milestone in order
*  to have a good pitch and you do it. You have to have this talent and you just don't have it
*  inside the company or you have to get 200 people or however many people kind of along with you and
*  buy in the journey. You're like disagreeing with an investor and they're your investors.
*  So it's just like there's no walking away from it. It tends to be like those things where you just
*  kind of get clobbered in so many different ways that things end up being harder than you expect
*  and it's such a gauntlet, but you learn so much in the process and there's a lot of people that
*  actually end up rooting for you and helping you from the outside and you get great mentors and
*  you find fantastic people that step up in the company and you have this magical period where
*  everybody's like it's life or death for the company, but you're all fighting for the same
*  thing and it's the most satisfying kind of journey ever. The things that make it easier
*  and that I would recommend is be really, really thoughtful about the application. There's a saying
*  of team and execution and market and how important are each of those and oftentimes the market wins
*  and you come out of thinking that if you're smart enough and you work hard enough and you're like
*  have the right talented team and so forth, you'll always kind of find a way through.
*  It's surprising how much dynamics are driven by the industry you're in and the timing of
*  you entering that industry. Waymo is a great example of it. I don't know if there'll ever
*  be another company or suite of companies that has raised and continues to spend so much money
*  at such an early phase of revenue generation and productization from a P&L standpoint.
*  It's an anomaly by any measure of any industry that's ever existed,
*  except for maybe the US space program. But it's like multiple trillion dollar opportunities,
*  which is so unusual to find outside of a market that just the progress that shows the de-risking
*  of it. You could apply whatever discounts you want off of that trillion dollar market and it
*  still justifies the investment that is happening because being successful in that space makes all
*  the investment feel trivial. Now, by the same consequence, the size of the market, the size
*  of the target audience, the ability to capture that market share, how hard that's going to be,
*  who the incumbent is, that's probably one of the lessons I appreciate more than anything else where
*  those things really, really do matter and oftentimes can dominate the quality of the team
*  or execution because if you miss the timing or you do it in the wrong space or you run into
*  the institutional headwinds of a particular environment, let's say you have the greatest
*  idea in the world but you barrel into healthcare but it takes 10 years to innovate in healthcare
*  because of a lot of challenges. There's fundamental laws of physics that you have to think about.
*  The combination of Anki and Waymo drives that point home for me where you can do a ton if you
*  have the right market, the right opportunity, the right way to explain it and you show the
*  progress in the right sequence. It actually can really significantly change the course of your
*  journey and startup. How much of is understanding the market and how much of is creating a new
*  market? How do you think about, like space robotics is really interesting. You said exactly right,
*  the space of applications is small. Yeah. Relative to the cost involved. How much is
*  truly revolutionary thinking about what is the application? Then yeah, creating something that-
*  Didn't exist.
*  This is pretty obvious to me. The whole space of home robotics, everything that Cosmo did,
*  I guess you could talk to it as a toy and people will understand it because it was much more than
*  a toy. I don't think people fully understand the value of that. You have to create it and the
*  product will communicate it. Just like the iPhone, nobody understood the value of no keyboard and a
*  thing that can do web browsing. I don't think they understood the value of that until you create it.
*  Having a foot in the door and an entry point still helps because at the end of the day,
*  an iPhone replaced your phone. It had a fundamental purpose and it's all these things that it did
*  better. Then you could do ABC on top of it. Then you even remember the early commercials where
*  there's always one application of what it could do and then you get a phone call.
*  That was intentionally sending a message, something familiar, but then you can send a
*  text message, you can listen to music, you can surf the web. Autonomous driving obviously anchors
*  on that as well. You don't have to explain to somebody the functionality of an autonomous
*  truck. There's nuances around it, but the functionality makes sense. In the home,
*  you have a fundamental advantage. We always thought about this because it was so painful
*  to explain to people what our products did and how to communicate that super cleanly,
*  especially when something was so experiential. You compare Anki to Nest, Nest had some beautiful
*  products where they started scaling and actually found really great success. They had really clean
*  and beautiful marketing messaging because they anchored on reinventing existing categories where
*  it was a smart thermostat. You are able to take what's familiar, anchor that understanding,
*  and then explain what's better about it. That's funny. You're right, Cosmos is a totally new
*  thing. What is this thing? We struggle. We spent a lot of money on marketing. We actually had far
*  greater efficiency on Cosmos than anything else because we found a way to capture the emotion in
*  some little shorts to kind of lean into the personality in our marketing. It became viral
*  where we had these kind of videos that would go and get hundreds of thousands of views and get
*  spread and sometimes millions of views. It was really, really hard. Finding a way to
*  anchor on something that's familiar but then grow into something that's not is an advantage.
*  Then again, there are successes otherwise. Alexa never had a comp. You could argue that that's
*  very novel and very new. There's a lot of other examples that created a category out of Kiva
*  systems. They came in and they like, enterprise is a little easier because it's less susceptible
*  to this because if you can argue a clear value proposition, it's a more logical conversation
*  that you can have with customers. It's a little bit less emotional and kind of subjective.
*  In the home, you have to- Yeah. A home robot is like, what does that mean?
*  Then you really have to be crisp about the value proposition and what really makes it worth it.
*  We, by the way, went through that same one. We almost hit a wall coming out of 2013 where
*  we were so big on explaining why our stuff was so high tech and all the great technology in it and
*  how cool it is and so forth to having to make a super hard pivot on why is it fun and why does
*  the random family of four need this? It's learnings but that's the challenge. I think robotics tends
*  to sometimes fall into the new category problem but then you got to be really crisp about why
*  it needs to exist. I think some of robotics, depending on the application,
*  is a little bit of a marketing challenge. I don't mean, it's the kind of marketing that
*  Waymo is doing, that Tesla is doing, is showing off incredible engineering, incredible technology
*  but convincing, like you said, a family of four that this is transformative for your life.
*  This is fun. They don't care how much tech is in your thing. They really don't care.
*  They need to know why they want it. Some of that is just marketing.
*  Yeah. That's why Roomba, yes, they didn't go and have this huge ramp into the entirety of
*  AI robotics and so forth but they built a really great business in the vacuum cleaner world and
*  everybody understands where a vacuum cleaner is. Most people are annoyed by doing it and now you
*  have one that does it itself in various degrees of quality but that is so compelling that it's
*  easy to understand and they had a very, and I think they have 15% of the vacuum cleaner market
*  so it's pretty successful. I think we need more of those types of thoughtful stepping stones in
*  robotics but the opportunities are becoming bigger because hardware is cheaper, compute is cheaper,
*  cloud is cheaper and AI is better so there's a lot of opportunity. If we zoom out from specifically
*  startups and robotics, what advice do you have to high school students, college students about
*  career and living a life that you'd be proud of? You lived one heck of a life. You're very successful
*  in several domains. If you can convert that into a generalizable potion, what advice would you give?
*  Yeah, that's a very good question. It's very hard to go into a space that you're not passionate
*  about and push hard enough to maximize your potential in it and so there's always the saying
*  follow your passion. Try to find the overlap of where your passion overlaps with a growing
*  opportunity and need in the world where it's not too different than the startup argument that we
*  talked about where if you are- Where your passion meets the market.
*  That's a beautiful thing where you can do what you love but it also just opens up tons of
*  opportunities because the world's ready for it. If you're interested in technology,
*  that might point to go and study machine learning because you don't have to decide what career you're
*  going to go into but it's going to be such a versatile space that's going to be at the root
*  of everything that's going to be in front of us that you can have eight different careers in
*  different industries and be an absolute expert in this tool set that you wield that can go and be
*  applied. By the way, that doesn't apply to just technology. It could be the exact same thing if
*  you want the same thought process of price to design, to marketing, to sales, to anything but
*  that versatility where you like when you're in a space that's going to continue to grow.
*  It's just like what company do you join? One that just is going to grow and the growth creates
*  opportunities where the surface area is just going to increase and the problems will never get stale
*  and you can have many- And so you go into a career where you have that growth in the world that
*  you're in. You end up having so much more opportunity that organically just appears
*  and you can then have more shots on goal to find that killer overlap of timing and passion and
*  skill set and point in life where you can just really be motivated and fall in love with something.
*  And then at the same time, find a balance. There's been times in my life where I worked
*  a little bit too obsessively and crazy and I think we tried to correct the right opportunities. But
*  I think I probably appreciate a lot more now, friendships that go way back, family and things
*  like that. And I have the personality where I have so much desire to really try to optimize.
*  When I'm working on that, I can easily go to an extreme. And now I'm trying to find that balance
*  and make sure that I have the friendships, the family, relationship with the kids, everything
*  that I don't. I push really, really hard, but it find a balance. And I think people can be happy on
*  actually many extremes on that spectrum, but it's easy to inadvertently make a choice
*  by how you approach it that then becomes really hard to unwind. And so being very thoughtful about
*  all of those dimensions makes a lot of sense. And so those are all interrelated. But at the end of
*  the day- Oh, love, passion and love. Love towards, you said-
*  Yeah, family, friends. Family. And hopefully one day,
*  if your work pans out, Boris, is love towards robots.
*  Love towards robots. Not the creepy kind, the good kind.
*  Not the good kind. Just friendship and fun.
*  Yeah. It's like another dimension to just how we interface with the world.
*  Yeah. Boris, you're one of my favorite human beings, roboticists. You've created some incredible
*  robots and I think inspired countless people. And like I said, I hope Cosmo, I hope you work with
*  Anki Lizan, and I can't wait to see what you do with Waymo. I mean, if we're talking about
*  artificial intelligence technology, there's the potential to revolutionize so much of our world.
*  That's it right there. So thank you so much for the work you've done and thank you for spending
*  your valuable time talking with me. Thanks, Alex.
*  Thanks for listening to this conversation with Boris Hoffman. To support this podcast,
*  please check out our sponsors in the description. And now let me leave you with some words from
*  Isaac Asimov. If you were to insist I was a robot, you might not consider me capable of love
*  in some mystic human sense. Thank you for listening and hope to see you next time.
