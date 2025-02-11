---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 6223s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 9441
Video Rating: None
---

# BI 085 Ida Momennejad: Learning Representations
**Brain Inspired:** [September 30, 2020](https://www.youtube.com/watch?v=LH1dlpagF1U)
*  Life felt precious, like learning felt precious.
*  Reading fiction, watching certain movies, listening to certain music, creating certain
*  things, it felt precious.
*  Does it still feel that way?
*  For me it does.
*  There is a sense in which there are particular parts, newer, evolutionarily newer parts of
*  the human brain that enables the hardware to transcend the limits of the algorithms
*  you are born with.
*  This is why meaning and philosophy matter so much.
*  I think we can change that ultimate value function you are talking about or determine
*  it on the basis of a particular meaning or philosophy that we have about our lives.
*  And I think that is profoundly human.
*  What kind of reinforcement learning algorithms do our brains run?
*  What kind will the future robots and AI run?
*  Hey, it's Paul.
*  It's Brain Inspired.
*  I'm Amin Najat and I answer those questions and more on today's episode.
*  Taking it up a notch there.
*  Ida studies reinforcement learning and collective memory, especially as they pertain to the
*  structure of the environment and how individuals interact with that structure.
*  And she's done that for years in the academic world, but she's recently started a job at
*  Microsoft Research where she'll continue that work and beyond.
*  So deep reinforcement learning has dominated the AI headlines for the past few years with
*  the successes of DeepMind's AlphaGo beating the world champion at Go, the networks that
*  learn to play Atari games so well and the list goes on.
*  And reinforcement learning in general has been one of the major success stories in neuroscience
*  in terms of spanning all of David Maher's levels of understanding from the computational
*  level goal of maximizing reward to the algorithmic solutions like temporal difference learning,
*  etc.
*  To the neural implementation in brain circuits involving the basal ganglia and dopamine.
*  The reinforcement learning story has traditionally been divided into two families of learning
*  strategies.
*  Model free learning, which is learning surely by experience, which is computationally efficient
*  but can't easily adapt to new situations.
*  It isn't very flexible.
*  And model based learning, which is learning by simulating lots of potential outcomes,
*  which is more adaptable and flexible, but is computationally more expensive than model
*  free learning, having to run all those simulations.
*  Behaviorally, model free and model based reinforcement learning roughly map onto habitual behaviors,
*  those you do without thinking about it, and goal directed behaviors, those that require
*  more thought or planning.
*  Also traditionally, there are roughly two brain circuits that model free and model based
*  reinforcement learning map onto.
*  And there's a continuing story about how dopamine underlies the updates required in those brain
*  circuits.
*  But that's the old view.
*  The new view is that model free and model based reinforcement learning algorithms and
*  their neural underpinnings interact all the time.
*  And that there are in between types of algorithms that span the spectrum of computational efficiency
*  and flexibility.
*  One of those in between type of algorithms that Ida studies is called the successor representation,
*  which she describes in much more detail.
*  But basically, it allows you or an AI agent to remember some distant connections between
*  things.
*  So it can skip steps along the way and thereby not need to run full on simulations of a whole
*  situation.
*  And thus the successor representation framework has a nice balance of computational efficiency,
*  along with pretty good flexibility.
*  So we talk about all of that, but it's been the first part of our conversation talking
*  about her background and how it's shaped her approach to science and life and the role
*  philosophy has played and continues to play in her life.
*  Visit the show notes at brain inspired co slash podcast slash 85 to dive deeper and
*  learn more about Ida to always hear the full version of each episode of brain inspired.
*  And to get some bonus episodes, you can always support the show through Patreon.
*  Thank you as always to you beautiful souls who value the show enough to spend a couple
*  of bucks a month on it.
*  Speaking of beautiful souls.
*  This is how I imagine it went down and you can correct me, but there'll be no need because
*  it's accurate.
*  I'm sure a young Ida in Tehran was sitting around pondering her future and basically
*  in an afternoon planned it all out and thought, you know, what I need to do first is some
*  computer science and some software engineering.
*  Gosh, that's going to help me, but I really need to learn about philosophy before I go
*  on to get a PhD in psychology, which will I can translate into neuroscience and computational
*  means and eventually land a job at Microsoft, which I can parlay into appearing on a podcast
*  with a super intelligent and charming podcast host.
*  That's how it went right?
*  You got it right.
*  Yeah, it was all on my vision board, including the podcast.
*  It does seem like your trajectory has been one series of deliberate, well thought out
*  steps.
*  So I just want to spend a few moments pondering that because mine was super messy and I didn't
*  know what I was doing at almost any step.
*  But yours from the outside looks like you knew exactly what you're doing.
*  Is that is that accurate?
*  That's not how I felt while it was happening.
*  So what it seems to me was that I was chasing certain questions or certain aspirations and
*  the best approach at the time to me at each stage seemed like a particular discipline
*  or other.
*  And to so it to a lot of other people, it actually seems like a very messy trajectory.
*  But you know, the very young I actually when I was very young, I very genuinely wanted
*  to be an astronaut and I was thinking about it in a very rational way.
*  And at some point, so I was doing track and being good in math and everything.
*  But at some point I realized I don't like to be confined in small spaces.
*  And that's the time that I realized, oh, no, I probably can never be an astronaut.
*  Oh, so physically small spaces.
*  Exactly.
*  Yeah.
*  So anyway, so at that time I realized, all right, next thing.
*  Interesting.
*  I actually have in my notes here, because the question is like how to start out, right?
*  Because everyone has a different messy series of steps.
*  And in my notes, I have should we just start out in space camp?
*  What's the right way to start out to give us some grounding?
*  You know, well, as a as a young child in growing up in Tehran, while there was a war for the
*  first sort of seven years of my life, I think that I would have really appreciated going
*  to a space camp.
*  My space camp was our balcony where I used to sit for hours and look at the sky and then
*  chart the stars and then make up names for stars and connect them in random ways.
*  Because I had seen it in books that people connected them and they have names.
*  But I didn't know that you can't rename constellations.
*  I thought that I thought the rule is you just connect the dots and name it something.
*  So I kept doing that.
*  I thought that's astronomy.
*  You just imagine things in the sky and then name them.
*  And my mom kept those notes actually until I was older.
*  Wow.
*  So when you say you charted, do you mean night after night?
*  You Yeah.
*  Wow.
*  So you've been I was very young.
*  Obviously, it wasn't precise.
*  Well, I mean, that's that's more than more effort than most put into, you know, something
*  like that, keeping track of things and learning about things.
*  So I think that that's something that I can say is in the what I perceive to be as kind
*  of a messier trajectory than perhaps it seems to you.
*  I think the thing that has always been consistent is a certain appetite for learning and for
*  having new ways of understanding things.
*  Every time an art piece or a piece of science in any discipline or a talk or a movie or
*  a piece of music gives me a way of perceiving differently or gives me an understanding or
*  connects the dots in a different way.
*  I really appreciate it.
*  So I think this idea of connecting the dots and naming it so that you have a concept to
*  refer to something that's, you know, larger than one moment is something that I've been
*  just naturally attracted to since I was probably five or something.
*  But how important is knowing what you want along the entire trajectory?
*  It sounds like it's it has been with you.
*  Well, I mean, that what keeps changing.
*  I think the thing that doesn't change much is the practice as how do you approach whatever
*  it is.
*  And I think that the what is determined really by how we go about things or the kinds of
*  practices that we find ourselves comfortable doing, which is why, for instance, I realized
*  the what of being an astronaut is not going to work out for me because the practice of
*  being in a confined space for a very long time seemed like it might not be in my sort
*  of wheelhouse, which the pandemic has shown me.
*  I'm not bad at it, actually.
*  I'm not sure that your apartment is nearly as closed off as like a space station or something.
*  That's true.
*  But you do have so so your curiosity and your drive to learn has taken you through many
*  different subjects.
*  And is there a way to rank the importance of the different subjects that continue, I
*  assume, to inform everything that you do?
*  Sure.
*  So I think something that is underlying pretty much every single scientific study or philosophical
*  work that I have ever undertaken or have been attracted to is the idea of temporally extended
*  agency, and not just temporally extended agency, but also collective agency.
*  So there are ways in which humans can I can decide right now that I'm going to raise my
*  hand and I can do this.
*  And this is a very sort of proximal intention or a sort of a very immediate intention.
*  But then there is the idea of, oh, I plan to go to Iran to visit my family.
*  And that's a much more challenging sort of plan or intention, because there are a lot
*  of uncertainties, for instance, in the world, even if before COVID there were.
*  It's a more long term undertaking.
*  It needs a lot of coordination and planning.
*  And then there is a further one, which is in 10 years, I want to somehow have contributed,
*  let's say, to, you know, somehow helping with reducing our negative impact on climate change,
*  let's say. Or let's say the goal is I'm going to in 10 years time, I want to have created
*  something that assists people for mental health management.
*  So these kinds of things are sort of longer term agency.
*  They require a different scale of thinking about things.
*  And I'm profoundly interested in this capacity in humans, whether it's from philosophical
*  stance, whether it's from a collective stance, what kind of organization, what kind of
*  graph structure between people enables these kinds of things, what kind of things shrinks
*  agency. And if you I think what you were asking is how does it tie back to some kind of
*  episode or moment in my personal history?
*  I mean, I grew up during the war and then I was in a country where a lot of things were
*  banned. And so it's surprisingly not unlike sort of where everywhere in the world is
*  currently heading. So there was a sense where you couldn't plan things in advance because
*  things could change.
*  And if all of a sudden the bombing changed in one city, you should be ready to pick up
*  and go somewhere else to make sure your family is safe.
*  And then there were bunkers and then every day there were sirens and you had to run down
*  to some bunkers at school, at anywhere else.
*  And if there were no bunkers, you had to run to some basement somewhere just to stay safe.
*  So this kind of thing, when you're very young, it doesn't sound traumatic.
*  It doesn't feel like that.
*  It just my dad made it feel like a game, but a very serious one that we really need to
*  do it right.
*  And so so but but what it taught me is that we couldn't plan long term during that time,
*  obviously. But then we somehow did.
*  So there was a mortgage and we discussed as a family things about that.
*  Or when we got when my mom was writing her master thesis at the time.
*  So there was discussions of those things.
*  And then we grew up again, some plans, plans about this.
*  And it started to seem to me how important the structure of the environment around you
*  is for shrinking or expanding your agency.
*  And I think that that really got interesting to me.
*  And I noticed that a lot of work in philosophy or I saw a kind of a division between
*  works that focus on individuals and cultures that focus on individuals and cultures that
*  enforce certain kinds of collective attitudes versus a kind of a critical approach in
*  between that acknowledges the collective forces that shape the individual and expand or
*  diminish what it can want the scope of its agency, what kind of being it can be, what
*  kind of questions it can ask, etc.
*  And so that idea, I guess, very closely linked with a sense, a certain sense of freedom and
*  not just freedom in the sense of free will, which I think is a very almost like a
*  distraction in all of this.
*  The metaphysical question is almost like a distraction to the things that matter the most,
*  which is somehow in the control of human societies.
*  We decide on them together.
*  I think that those kinds of questions became sort of central to me.
*  So it sounds like you have been thinking in graphs since a very young age.
*  You know, you might be the first person to say this, but I do like to think that because of my
*  drawings of fake constellations I was making up.
*  Yeah.
*  So, yeah, some of my early drawings are basically I would call them graphs now, but back then I
*  thought I'm just making up new constellations.
*  But but now you'd call everything a graph, right?
*  You can think of almost anything as a graph.
*  Interesting.
*  I haven't done that in my scientific work, but I in all of my work, I have definitely done it in my
*  collective memory work.
*  And when I think about how we learn a cognitive map of the environment, I mean, there are people way
*  before me 20 years ago, people who have called it cognitive graphs.
*  So definitely not the first person to call anything a graph by any means.
*  And do I think everything is a graph?
*  I mean, I'm not sure.
*  It depends on the level of analysis or level of whether it's helpful for that level of analysis or not.
*  Well, a cognitive map, a la Tolman, whom I know is one of your intellectual heroes, I guess, for lack
*  of a better term.
*  But a map is a graph.
*  That's right.
*  That's right.
*  So, I mean, anyway, we'll come back to this later.
*  Yeah, of course.
*  As an aside, do you feel grateful at all that you grew up during a war in the midst of a war?
*  I'm again positively surprised by that question.
*  And to be honest, I can't say that I'm grateful, but I do have a sense that I'm content with the
*  trajectory of my life in spite of its difficulties, because I have a sense that I got to
*  experience a range of human possibilities and experiences that a lot of people will not be able to
*  experience it in multiple generations even.
*  Yeah.
*  So this your trajectory, I'm so intrigued by this because the way that you grew up in your
*  trajectory is so different than mine because at many steps along the way, I just had no idea what
*  I wanted.
*  Right.
*  And that is a huge impediment to making progress in anything.
*  Because I was just largely unfocused because I grew up in a, you know, suburban, fairly wealthy
*  family and had total freedom, like to do many things.
*  And the challenges would only have to come through self-challenge or through sports or there was
*  school, but everything in school came easy until I kind of quit trying in school, you know.
*  And so I wonder if one needs some sort of challenging environment to propel one forward.
*  You know, some people are born with that internal intrinsic motivation, which you may also have had.
*  You might have had the right combination.
*  I'm not trying to deconstruct your being here, although we can.
*  It'll be fun.
*  I think that, so if you look at regions that are war-torn, what you observe is not that all of a
*  sudden everybody is progressing and unfolding their best potential.
*  So I think that something that happens is a huge number of people lose their capacity to realize any
*  potential at all.
*  And not just because of losing physically something, but because of the psychological impact that the
*  shrinking of agency has on them.
*  Now, there are people who form some kind of resilience through trial and error, through a support
*  system or whatnot.
*  What I do get interested in is if you read post-war literature and philosophy in most cultures, it
*  tends to be turning point.
*  And or around the time or just pre around the time of catastrophes, there is a sense in which people
*  start to talk about narratives.
*  People start to rethink things.
*  You find a lot of very good philosophy in post-World War II in Europe.
*  You mean personal philosophy or cultural?
*  No, cultural products.
*  Yeah.
*  Okay.
*  Yeah.
*  There are those kinds of turning points that happen after periods of war sometimes.
*  And I think that that's interesting.
*  So I'm only focusing on this because of your specific question.
*  Do wars make people realize potential?
*  I mean for you.
*  Oh, I see.
*  I see.
*  And really I'm just talking about the broader context of growing up with and without these
*  challenging constraints and structures that force you into different scenarios and make you
*  experience different things rather than being up to just Saturday morning cartoons or, you
*  know, something like that where there's really no grounding with the external world and how
*  to proceed.
*  And I'm not sure how to compare those two forms of life because it seems to me that there
*  are so many other factors that I have.
*  I'm not an expert in analyzing those.
*  What I can say is I do certainly think that I could have probably done a lot more if I
*  wasn't facing as much obstacles.
*  Oh, come on.
*  You've done quite a bit already.
*  That's not my perception.
*  But that's part of who you are as well, I think.
*  So I want to ask more about philosophy.
*  But before I do that, have there been moments throughout your career?
*  Because the other thing it looks like is that every step has been a success and you've been
*  here's my question.
*  I'm going to go in this field and answer it.
*  And this leads to a new question.
*  And then, oh, I now need to learn a new field and then I'll get a good position there.
*  Have you ever felt disillusioned in your career?
*  And if so, like how, you know, how did you move forward?
*  Yes, multiple times.
*  I think that the first time that I felt profoundly disillusioned was when I migrated to Europe
*  around the age of 23.
*  We were a group of people in Tehran.
*  We were, you know, learning multiple languages, reading as much philosophy as we could,
*  reading fiction from everywhere in the world, history of cinema, watching sort of
*  taped versions of good plays everywhere in the world, going to the theater all the time.
*  Tehran had amazing theater.
*  And my sense was that if I go to Europe because they just haven't had all the restrictions
*  that we've had, things are going to be even a lot more, you know, everybody has exactly.
*  And then I arrived there and I realized, oh, actually, they don't care as much about the
*  meaning of life or, you know, what is a better way to govern or what are the different
*  political systems that have existed for the last 2000 years and which ones survived and why.
*  So I had a culture shock when I arrived to Europe.
*  Why don't these people care?
*  Yeah. And then I realized the fact that everything that we were doing was kind of somehow
*  in some sense, illegal almost made every moment and every every activity driven towards
*  knowledge more significant.
*  What do you mean illegal?
*  So, for instance, certain movies, you weren't supposed to have them.
*  Music was illegal.
*  Certain kinds of music and books.
*  Yeah. Certain books during different times were illegal.
*  As I was growing up, things changed, of course, because there was a revolution in 1979
*  before I was born. And then there were a lot of restrictions afterwards and they sort of
*  slowly changed over time.
*  And there was a time that even chess got illegal banned, which was a very surprising thing.
*  So there were various moments where it seemed like every activity that we were doing had a
*  certain significance to it.
*  It wasn't as much how perfect you were doing something as it was the fact that you were
*  doing something. You were maintaining that.
*  And, you know, in the history of our culture, there are many times that Iran had been sort of
*  attacked by another culture who tried to, for instance, change the language or something.
*  And people kept the language alive via poetry, for instance, when it wasn't allowed to be
*  the written dominant language.
*  So there was there is a kind of culture of resistance that was, I guess, I grew up with.
*  There were poetry that I grew up with.
*  There was this thing that it's a value to learn from anything in the world as much as you
*  can learn as many languages as you can.
*  And so these things were real values.
*  Because the opportunity might be taken away from you otherwise.
*  Is that part of it?
*  I'm not sure.
*  But maybe. Yeah, maybe.
*  Yeah, I'm not entirely sure whether it's that the opportunity might be taken away, but it
*  felt precious. Life felt precious.
*  Like learning felt precious.
*  Reading fiction, read, watching certain movies, listening to certain music, creating
*  certain things. It felt precious.
*  Does it still feel that way?
*  For me, it does, because I because there is a lot more resistance to buy.
*  I mean, currently, I think the world is a little more comfortable with the term systemic
*  injustice or systemic bias.
*  And I think that you feel it.
*  It's almost like it's as felt as gravity.
*  If you are a person who's migrating alone, a woman of color, migrating alone from country
*  to country, trying to acquire knowledge, you feel that resistance to your presence almost
*  the same way you feel gravity when you're looking down a cliff.
*  It's very real.
*  It's it's it's so tangible.
*  And I've been fortunate to have fantastic allies from privileged backgrounds here and
*  then who have helped me out.
*  And one of them was telling me one of the situations where they first tried to change
*  something about somebody being on a panel.
*  And they told me how much they felt that.
*  And we had a long discussion about that feeling when you feel that resistance towards
*  some activity that you want to do that you think is just and it's going to improve things
*  and that you've sensed that resistance.
*  So I think that that sense of the importance, the kind of almost urgency of engaging in
*  big picture thinking, engaging in philosophical thought, it kept getting reinforced by the
*  fact that it's kind of it's I don't know.
*  It's almost.
*  It almost is as if you're you're tagged as a dangerous being, and it's unclear why,
*  because you haven't done anything that's dangerous at all.
*  And it's the unknown that you haven't done any you haven't you haven't done anything
*  that someone has observed.
*  Right. So it's different.
*  Right. There's a difference is fear of breathing.
*  What is it now?
*  We're really going off the deep end.
*  But we might need to take out some of this.
*  That's OK. I don't mind.
*  But so are we in the United States on the right track?
*  Have we course corrected at all?
*  Is this a time of are we improving or is this this is a huge question?
*  I'm sorry. What I can say is that I am a huge fan.
*  Of political philosophy, poetry and science fiction produced by African-American authors
*  on this topic, I'm a very huge fan of the American civil rights movement.
*  I'm a very huge fan of the BLM movement in general.
*  And I think that something that is extremely unique about the United States is the
*  practices and cultures of resistance that particularly the African-American
*  community here has developed.
*  And it almost is unique in the world.
*  And I think it can teach the world a lot.
*  So in that sense, I am I feel very indebted to the authors that I have read over the years
*  and I keep reading. I feel indebted to the conversations that I've had with people who
*  have taught me how to view the culture of resistance from different angles.
*  So, again, coming from a culture of resistance and being very deeply motivated by it,
*  I recognize it in others and I profoundly have respect and extreme reverence for it.
*  And I think that it's particularly been going very strong and profoundly creative in the
*  United States in spite of the increasing and kind of scary sort of I'm not even sure where
*  it's going to go. But let's say counter wave that is that they are facing.
*  So, OK, at risk for, you know, at the risk of going really off the rails to political
*  topics. I know we'll we can continue this after we stop recording, which would be fun.
*  But OK, so let's talk a little bit of philosophy and yeah.
*  And its role in your life and career before we move on to talking about reinforcement
*  learning and your particular role in that.
*  And maybe we'll come back to this collective memory and collective learning that you're
*  also interested in because it's all related.
*  So I sort of zeroed in on your I think it was a master's in philosophy.
*  I don't remember exactly what degree you got, but philosophy of science, philosophy of
*  mind. Has that continued to shape your current thoughts?
*  Do you do you refer back onto it or is it just a key part of a history that has shaped
*  you or is it a continued ingredient?
*  Yeah, that's a great question.
*  Very often do I refer back to it, not just in my own thinking, but also in discussions
*  with others. Very often do I reread things that I've read in the past.
*  And it's interesting how it changes the way that you think about it.
*  I guess for me, philosophy is first and foremost an activity.
*  It's a part of your way of life.
*  It's an activity.
*  It's not something that is a static thing that you read and then you apply.
*  It's something that you do.
*  Another point of disillusionment for me was when I realized that philosophy is one of
*  the worst fields in terms of gender ratio.
*  I think it's even worse than math.
*  And I realized that a lot of writing philosophy would mean that you would need to publish
*  in journals that people like you are not going to be the ones who are reviewing or reading
*  or assessing it.
*  And so at some point I realized that maybe as a career, as a vocation, this might be
*  not the way for me to practice philosophy, so to speak.
*  So I have a sense that a lot of the kinds of science that I practice is a form of, you
*  know, doing philosophy in some ways.
*  And there was a time where natural science was called natural philosophy.
*  And it was, in fact, in the 19th century that the term science started to emerge and
*  separate from the notion of natural philosophy.
*  Looking back at my own culture, there have been so many Iranian scientists.
*  There is Abissena, there's Hayyam, there's people who built calendars or advanced
*  medicine or created different kinds of math.
*  And they were always doing multiple things.
*  They always were doing philosophy, science, poetry, a bunch of these things.
*  So I almost feel like there's nothing original in that way of looking at it.
*  It's basically like my cultural heritage to some extent.
*  And in that way, philosophy does shape, to be honest with you, almost my everyday
*  conversations as much as my scientific work in Twitter discussions.
*  It comes up a lot. And recently we started this sort of salon called the Learning Salon.
*  And we're hosting it together with John Krakauer, who has been on your show before.
*  Friend of the show. Yeah.
*  And Joshua Vogelstein.
*  And it's interesting because some of the people's feedback for our discussions on
*  Twitter was that, oh, neuroscientists have discovered philosophy.
*  Like, no, we were we were using it.
*  It's always been there.
*  Yeah. Yeah.
*  So I think it's very ingrained in how I think about things and in how it helps to
*  step back and look from a different angle and not get too lost in details and also to
*  dissociate things in certain ways, to to to test a particular hypothesis and to be able
*  to recognize, I guess, the slower movement of ideas as opposed to get too excited about
*  everyday advances.
*  So how many things have we really advanced over the past 20 years, over the past 30
*  years, over the past 60 years?
*  I think it's easier to look at that if you keep zooming out, so to speak.
*  And I think that that is a very valuable thing for science, because at some point we
*  need to realize we've been holding the same court for too long.
*  Yeah, we hit the wall.
*  But do you do you use philosophy?
*  It sounds like you use philosophy more as a way to think about how to move forward in
*  sort of a prescriptive manner.
*  Well, it kind of sounds like you use them both, because one way you can use it is to
*  develop rules and in a prescriptive way of of how to achieve some scientific results
*  or something. Right.
*  And another way is you can use that background to evaluate and to to judge the validity of
*  some results that someone else has published or whatever.
*  Do you use them both equally that way or is there a certain?
*  I think that that's a great question.
*  And I think that I use it to evaluate some existing fields and then develop some new
*  idea by by developing it in a kind of a philosophical sphere and then testing it in
*  with with models or empirical work.
*  For instance, when I went to do my Ph.D.
*  in Berlin after my master's in philosophy, I was working on this distal agency and
*  distal intentions, long term intentions.
*  And then I went and started using fMRI to study how does the brain represent future
*  intentions when we are paying attention to something else.
*  And that's my first encounter with Brahman Area 10, which ended up happening,
*  reoccurring again and again, pretty much in every study that I've done ever since
*  that I've used fMRI, I have somehow again uncovered Brahman Area 10.
*  It's the largest site architectonic area of the prefrontal cortex, and it's the region
*  in which we have the largest difference between humans and other mammals, including
*  our evolutionary cousins.
*  So it was an interesting interconnectivity between them.
*  And then when it came to the collective memory ideas, this idea, the philosophical idea
*  of not individualism, but acknowledging the sort of embeddedness of humans in a larger
*  structure and acknowledging that some of my memories are not my memories.
*  The majority of the things that I remember right now are actually not exactly my own
*  memories. And I have read about them or learned about them or heard about them,
*  implicitly acquired them through culture, but they're not really mine.
*  And a lot of my memories of individual experiences that I've had are not my own
*  memories only because I have rewritten them and updated them on the basis of
*  conversations with others.
*  This interpersonal aspect and relational aspect is prominent in philosophical
*  traditions, and some of them go back to Hegel and some of them are more contemporary
*  in feminist and race philosophy.
*  So there is a lot of interesting places where these different sort of philosophical
*  ways of thinking leads to what kind of experiments do we want to do now?
*  So, for instance, that relational idea of memory leads to, OK, what kind of graphs
*  leads to memories converging or diverging?
*  Or in the same graph, what order of conversations would make them diverge or converge?
*  Which sounds like a much more empirical thing to do.
*  But really, I think it's very much ingrained in these kinds of philosophical ways.
*  You mentioned going back and rereading multiple times different passages, different
*  works. What I would love to figure out is just the exact right sequence of when to go
*  back, how often to go back to a work.
*  And because I think that there's this huge value in just cycling.
*  Right. And it's not just a circle, it's a messy scribble that moves forward in time
*  and how to know when to revisit a certain work.
*  Because every time you revisit it, you do revisit it with new knowledge.
*  And then, you know, like I read a lot of high school philosophy in high school and it
*  was basically a complete waste of time because then I, you know, and so I started off
*  my academic career or whatever with this really broad and very shallow knowledge base.
*  And then I sort of dove in and, you know, in the PhD, you do the specialized work.
*  And then I became very specialized, but very narrow.
*  Right. And through my postdoc.
*  And now what I'm doing through the podcast and just my own readings is now I'm
*  expanding back and getting really broad again, but with much more depth in certain areas,
*  which color everything else I read.
*  So revisiting philosophy, revisiting even old neuroscience works, everything is colored
*  by the new knowledge. And so there must be some perfect optimal trajectory through that
*  graph. Maybe that could be a side project for you to figure out what the right trajectory
*  is. But do you have a sense of like what, just when to visit and what?
*  I never thought about it like that.
*  You know, in in the memory works that I've done on prospective memory with Ken Norman
*  and John Cohen, something that is very interesting to me is a kind of a bottom up
*  spontaneous retrieval that happens in episodic memory, for instance, which is very
*  different from the top down way of determining when to retrieve what, for instance, or
*  maintaining something in your mind all the time.
*  And I have a sense that there is a way in which these things just resurface every now
*  and then in case they are really on the trajectory that you're on.
*  There are things that don't resurface again.
*  And you realize that, OK, maybe, you know, that that would be a little forced to force
*  yourself to read some things.
*  But for me, it's a sense of some things happen, some context, some train of thought
*  happens. And then you find yourself all of a sudden back where you were before.
*  And you all of a sudden realize that you see it in a very different light now.
*  I think that the one example of this, I guess, a tangible example of this was in the
*  movie Big Fish, where this guy arrives at the same village twice.
*  The first time he sees it as this amazing place.
*  And the second time it's just kind of a broken down place.
*  And it's it's unclear.
*  It seems like the second time might be reality and the first time might have been the
*  kind of projected idealism or something.
*  But at the same time, both of them felt as real.
*  I think that I've had that experience with some work that the first time you see it,
*  it's this magical land that opens up all doors.
*  And then the second time you read it 10 years later, you're like, oh, it's actually,
*  you know, that window is broken over there and this door doesn't work.
*  Yeah. But my favorite is the opposite.
*  When the first time that's right, maybe you don't get it or it doesn't seem
*  interesting. And then you come back and then all of a sudden it's well, it's
*  repainted and the windows are fixed and all of that jazz.
*  Absolutely. I absolutely agree with you.
*  And that definitely happens, especially with work that you underestimate the first
*  time that you read it, because someone that you respected or valued had devalued
*  this work. And later on, you encounter the work again on your own and you all of a
*  sudden discover some value to it that you might have overlooked because perhaps it
*  was not as much valued in the particular contingent circle you were in at the time.
*  Yeah. Yeah. As we're talking, I realize I think reinforcement learning was one of
*  those that was originally like to me, you know, and the whole neuroeconomics and
*  subjective value and action value, state value, action value pair policy.
*  And, you know, at the time when I was reading really early on, one, it was above my
*  head. Two, I thought, oh, this is all so mechanical.
*  And, you know, what I'm really interested in is our awareness and subjective
*  experience. So you kind of pass it on.
*  But everything comes back full circle.
*  So so let's move on and get into reinforcement learning because you have a long
*  history now of studying reinforcement learning in academia.
*  But recently you've moved to Microsoft.
*  Are you in a situation at Microsoft?
*  First of all, congratulations on the job.
*  Yeah. Are you is it a Bell Labs kind of situation there or are you do you feel
*  fledged in industry there because it seems like these Bell Lab type situations are
*  just cropping up everywhere now?
*  Yeah, I do think it's a very from what I understand about Bell Labs.
*  Your memory of someone else's memory of Bell Labs.
*  Exactly. My memory of somebody else's memory of Bell Labs.
*  From what I understand, yes, it's very similar to that.
*  And I think it's not an exaggeration if I say that I have a sense of and that the
*  promise of 100 percent freedom of research is true at Microsoft in the industry
*  setting. So it's Microsoft research, which is a part of Microsoft that's exclusively
*  focusing on research, obviously, and any interest in working with the product teams
*  would depend on your research interests, which is a fantastic position to be in, to
*  be honest with you. You know, Microsoft owns Xbox and Minecraft.
*  And for a lot of people, especially during the pandemic, that's the real world right
*  now. So if you want to observe human behavior, if you're somebody who wants to study
*  human behavior, there are opportunities there.
*  I'm trying to get Katja Hoffman to come on the show, who does a lot of the Minecraft
*  work. Yeah, she's she's she her team is doing incredible work and they have actually a
*  lot of ongoing recent work that I think you would be very interested in as well.
*  OK, so you're not writing grants. You don't have that burden.
*  You don't do you have the publish burden?
*  I mean, it's it's it's not a burden.
*  It's a it's a desire.
*  I don't want to not publish.
*  I want to publish as much as I can.
*  And in probably the same journals, too, in the same I will be in the same academic
*  circles, but also a little bit more involved in sort of CS circles than I have been in
*  the past, although I used to go to those conferences.
*  Well, is that just because you're not going to be running experiments yourself now?
*  I mean, or is experimentation part of the OK.
*  Yeah, yeah, no, absolutely.
*  I will be running experiments.
*  I will continue collaborating with a lot of academic institutions, be it with grad
*  students, postdocs, professors in different directions of my research, in fact.
*  So there wasn't a lot of convincing that had to be done for you to to join soul
*  searching. Well, I well, there was a lot of soul searching and part of it was I had
*  sort of this idea of starting my own lab for a very long time.
*  But at the same time, the my I do take a lot of joy and energy in mentoring and
*  working with grad students over a long period of time.
*  And there are situations at Microsoft where you can do that.
*  There there is opportunities to not only have what we call interns, which happens
*  a lot in the CS field, which is that somebody who's doing a grad who's in grad
*  school basically joins for three months and works with someone on a project and
*  they might return for another one or for a postdoc or something.
*  And then there is just co advising students.
*  There is a lot of different ways that I was people sort of clarified for me that
*  this is how they are sort of pursuing research.
*  So there was always a priority of research and a priority of some advancing
*  some vision, getting to a point where you can finally have the sense that you can
*  advance something.
*  And I think that was what was while mentoring others.
*  So having, you know, your academic baby, so to speak.
*  So that was the kind of thing that had always been on my mind.
*  And so as I move forward, I will always that's my North Star.
*  I will always go towards a direction that I can have the situations where I can
*  mentor people, work with other people and hopefully grow together and at the same
*  time have the ability to advance my research in directions that I haven't
*  before.
*  And I have a sense that currently Microsoft research is indeed a place that
*  I get to do both.
*  You feel more freedom to explore right now than you have or than you projected
*  you would as a faculty member?
*  I can't say because I haven't seen the other option.
*  As of right now, I have the sense that the projects that I'm getting involved
*  with right now are very much in the trajectory of expanding in a way that I
*  have always wanted.
*  And I have a sense that it might be in directions that might not have been
*  entirely available to me in academia.
*  And that's very exciting, to be honest with you.
*  But it's very early.
*  So I can't so, you know, you can't you can't count your papers before they have
*  hatched.
*  Yeah.
*  Well, I feel I just had this internal sense.
*  I feel excited for you.
*  So thank you.
*  Thank you.
*  It's just great.
*  So we're going to talk reinforcement learning here.
*  But before I ask you about it, it feels like reinforcement learning is a super
*  crowded field.
*  Is that true?
*  Does it feel crowded to you?
*  Or is it just because it's exploded?
*  Is there just are the pieces flying so many pieces flying everywhere that there's
*  just room for unlimited growth?
*  Could you explain to me what that means?
*  So everyone studies reinforcement learning.
*  It just seems like half of the academic world.
*  And I have my own bias because I talk to people about these topics.
*  You know, does it feel very competitive or are there literally so many new
*  developments, new results that leading to new experiments and new computational
*  principles occurring that it feels like there's enough room for everyone to be
*  studying their own little niche.
*  So I'm trying to categorize where are these explosions that you're perceiving?
*  Well, so we're going to talk about successor representation, right?
*  Which is between model free and model based essentially reinforcement learning.
*  So there are new algorithms being developed all the time.
*  There are new ways of updating policy of, you know, revaluating things, etc, etc.
*  I'm curious why it's not my question isn't clear.
*  Because I don't feel OK.
*  Great question.
*  So because I meet a lot of people, especially in cognitive science or in NLP or
*  other fields that don't know much about either reinforcement learning or that
*  there are experiments on reinforcement learning in humans that are or in animals
*  that are beyond just, you know, model free values.
*  And it has been quite clear to me that a lot of the directions of reinforcement
*  learning that we see right now, a lot of it has been, you know, rewrite of things
*  that have been around since the 90s.
*  That's also what deep reinforcement learning is, well, what it began as.
*  But that's what I'm saying.
*  You know, deep reinforcement learning has is the darling of the AI world right now.
*  Correct?
*  So I think that that is the way that we see it.
*  I think that that is that might be true in some sort of aspects, for instance.
*  There are a lot of deep RL approaches that seem to get better scores on specific
*  task sets or specific measures.
*  But if you look at the bigger picture, the field of, for instance, theoretical
*  reinforcement learning that a lot of my colleagues at Microsoft Research are
*  involved with, that's I feel like I feel like it's an underappreciated field so far.
*  And I think that as we explore all of the things that GPUs can allow us to explore,
*  we are going to all go back to the whiteboard at some point in kind of theoretical
*  ways at some point.
*  And I have a sense that there is a lot of value to that.
*  And if anything, that seems underrepresented to me as opposed to over crowded.
*  It's not something that I have done so far, but it's something that I'm very
*  excited to collaborate with people on.
*  Another thing is the kinds of things that I'm doing, I know pretty much it's not
*  too hard to keep track of the papers that are coming out that are directly related
*  to yours, because although there is a lot of them and they're very interesting,
*  it's not as overcrowded as you would think.
*  OK, so my sense is actually that.
*  Especially if you're doing reinforcement learning in humans and you're doing
*  reinforcement learning in humans as pertaining to representation learning and how
*  it influences human planning or decision making or memory, it's not a very huge
*  field, in fact.
*  And to be honest, people have been most people, at least that I'm mostly in touch
*  with are pretty good with citing each other and collaborating.
*  And so I have a sense that it's a healthy field.
*  That's my experience.
*  And I have a sense that there is a lot of untapped potential and potential for
*  growth there.
*  Well, see, that's all I was asking is whether there's still do you think that?
*  So you mentioned the deep reinforcement learning stuff is occurring and it
*  exploded. But eventually we're going to go to the whiteboards and consider the
*  theoretical reinforcement learning moving forward.
*  Is that going to happen sooner rather than later?
*  Are we up against the limits or are we is it going to be 10 years from now?
*  I think especially the last couple of years, people have gotten a lot more
*  excited about aspects of cognition that are higher level.
*  And that requires compositionality, for instance, that requires an ability to
*  factor certain aspects of the stimuli that are related or most useful for
*  certain tasks.
*  There is meta learning of what are these features that are more related.
*  There is a need to understand how we could have agents that might, for
*  instance, learn objects without a kind of a symbolic approach or without a lot of
*  inherited inbuilt designer algorithms, but with just based on rooted in learning
*  principles.
*  And I think that the idea of approaching reasoning and compositionality and
*  objects and schema from a perspective of learning as opposed to the kind of, I
*  guess I could say, last century MIT approach, which was kind of symbolic inbuilt
*  sort of approach, very, very language oriented, very top down, very designed.
*  And it actually sort of historically and culturally, it stopped the growth of
*  connectionist approaches successfully for something like two decades, at least.
*  Yeah.
*  And I think that what we are seeing right now is that more and more learning
*  approaches are trying to approach those problems from a perspective of learning
*  principles out of which these can arise and minimal architectures out of which
*  these learning minimal architectures for and learning principles out of which these
*  can emerge without having hard coded them.
*  How do you reconcile that with the recent pushback on tabula rasa,
*  connectionism, deep learning from people who don't necessarily want people like
*  Gary Marcus, you know, who doesn't don't necessarily want to bring back symbolic AI,
*  a la MIT a century ago, but who want more priors, more structures built in and a
*  where the architecture plays a larger role moving forward.
*  And they don't want to get rid of learning, but maybe reduce the all encompassing
*  reliance on learning.
*  So I think that when I talk about learning principles and minimal architectures, there
*  are things that we can think about in terms of not tabula rasa machines.
*  However, I think there is a difference in what is the extent to which we think certain
*  architectures are innate.
*  And that is the kind of a, I guess, 30, 40 year old disagreement in the field before
*  I was a person or I was alive.
*  But Paul Smolenski gave a fantastic talk actually at Microsoft Research and talking
*  about the kind of East Pole, what he calls East Pole, which is again, the MIT sort of
*  Pinker Chomsky.
*  East Pole.
*  East Pole as in not he doesn't say East Coast, he calls it East Pole because there's a
*  yeah. And then West Coast, which is the sort of connectionism of I guess, 80s 90s.
*  Does he call it West Pole?
*  I think he calls that one West Coast.
*  I don't. Yeah.
*  And then the difference between these two and kind of in a cartoonish way, he
*  characterizes the two of them.
*  His own approach, of course, with the whole tensors and everything is to kind of bridge
*  between them.
*  And but again, he has a particular angle to it.
*  So there's a number of people who have tried to bridge them.
*  Gary Marcus is one of them.
*  Paul Smolenski is another.
*  And there are other people.
*  John Cohen has made some attempts at this.
*  But at the same time, I guess everybody has their own idea of what is the approach that
*  will work and what are the limits of every approach.
*  My understanding is that minimal architecture and minimal principles of learning, giving
*  rise to all of these is the way to go.
*  And I think that that would be something that's special because and here is, I think,
*  perhaps where I would differ, for instance, with someone like Gary Marcus, who we are
*  going to have on the learning salon.
*  So I will fortunately get the chance to talk to him in November about this.
*  Is this idea of, I guess, algorithms versus hardware?
*  You can have hardware that can enable a couple of algorithms.
*  And I think in many animals, it's like that.
*  You can barely teach them too many variations of other algorithms.
*  And even if you do, they don't teach it to their offspring.
*  So we haven't still managed to teach language to any other creature.
*  And in the sense that it has both systematicity and compositionality, we haven't observed it
*  in other creatures, although there are particular types of crows that have particular, sort
*  of more sophisticated versions.
*  There are calls that animals make.
*  They can learn new calls, but it's not at that level quite.
*  And they also don't teach it to their offspring when, for instance, when they learn
*  language, when they learn something language like or pseudo language like from humans.
*  But humans seem to have a kind of an architecture that enables varieties of algorithms on it.
*  It seems like the interconnectedness of our algorithm and our hardware is much less
*  strict and much more loose than it is for other mammals.
*  And which is part of the reason I'm fascinated by prefrontal cortex and its connection to
*  posterior medial cortex, to medial temporal lobe, because there is a sense in which there
*  are particular parts, newer, evolutionarily newer parts of the human brain that enables
*  the hardware to transcend the limits of the algorithms you're born with.
*  And it's completely correlated with how long it takes for you to develop.
*  How long does your learning process take?
*  And you mean it transcends it in terms of you start off with the hardware and a set of
*  algorithms and then through development, your hardware is able to combinatorially or
*  well, maybe not combinatorially, but transcend the number of algorithms it's then producing
*  through development. So it's a matter of producing more algorithms.
*  It could produce a lot more than what you would develop if I just left you to your own
*  devices with like a family.
*  Sure. But minimal levels of training.
*  There are so many directions of algorithm development that can happen in humans.
*  And in that sense, we need a kind of a flexible architecture that can generate new algorithms
*  for new problems.
*  And it doesn't need a new set of inbuilt biases every time it faces a new problem or
*  every time we need to we needed to solve a new task.
*  The number of tasks that humans can solve and the types of varieties that they use the
*  transfer for.
*  They're also not all in line with, I guess, like some kind of evolutionary survival
*  reproductive objective either.
*  It seems like there's a lot more room for just generating a lot of different types of
*  algorithms, generating completely made up structures and then inhabiting those.
*  We just are very good at making new tasks for ourselves, making new objectives and
*  creating very intricate structures that sustain for 2000 years or more and maintain
*  that as a part of our objective function, which you wouldn't get if this called if
*  one of one or two cultures get lost.
*  You will just not have those algorithms anymore.
*  You'll develop something else.
*  I think that that is a fascinating aspect of human cognition.
*  And I think that it gets lost in anything that is in between the innate versus
*  tabula rasa, anything that's making everything inbuilt in order to solve different
*  tasks completely misses the opportunity of even thinking about this more important
*  aspect, in my opinion, of human hardware software relation.
*  And I think that the biggest sort of maybe and I don't know, but for me, I think that
*  something that would be a huge advance is, first of all, theoretically understanding
*  this capacity for generating new algorithms to fit new problems.
*  Sorry.
*  And second, just theoretically understanding how simple organisms start to develop, start
*  to evolve architectures that enable more algorithms.
*  It doesn't mean that we need to.
*  So some people's reaction to these kinds of arguments is, oh, well, we don't have
*  millions of years to have a single cell and allow it to to to evolve into a human.
*  And the answer to that is, yes, it's not that we're simulating the entire evolution.
*  The idea is, can we figure out very theoretical, basic principles of evolving a more
*  complex hardware or changing your hardware, changing your architecture such that it might
*  enable more complex algorithms to increase your fitness?
*  You don't need to do the whole you don't need to sort of work on the entire evolutionary
*  trajectory up to humans.
*  It's sufficient if we can show it at least at some level.
*  And I think that if we did that, we create machines that can change their own architecture
*  and change their own algorithms according to situations.
*  I think that's that that would be a bigger breakthrough than the next one.
*  The next collage of tricks that is going to solve something with 98 as opposed to 97
*  percent. You know, man, so so much of what you just said, we're going to just keep coming
*  back to throughout the episode here throughout our conversation here.
*  And what you just ended on is kind of perfect because it's related to open endedness.
*  And I'll be talking with Ken Stanley, Kenneth Stanley next week.
*  And so hopefully I'll bring this back in to the conversation with him as well, because he
*  would delight in what you just said.
*  I think one of the things that you talked about is the modern landscape of reinforcement
*  learning starting to incorporate higher level, higher level cognitive operations and
*  compositionality and so on.
*  And that's happening in neuroscience as well.
*  And I'm not sure if you're referring to A.I. or neuroscience, but at least in the neuroscience
*  world, you see working memory being incorporated in reinforcement learning, episodic
*  memory, executive functions.
*  And it seems like we're starting to go beyond studying cognitive processes in isolation
*  and really starting to kind of put the system together.
*  I kind of winced when I said that because I don't totally believe it.
*  But learning how all these different parts interact in a more holistic manner.
*  And it makes me wonder, do you feel like this sort of progress is pushing towards some
*  sort of fundamental change, some fundamental advance in our understanding of intelligence?
*  Sorry, what kind of or if it's more incremental?
*  Well, so traditionally we've studied the brain in a modular fashion.
*  Right. And now, you know, thinking about reinforcement learning and I don't know if
*  we'll talk about this later, but you have the model free system, quote unquote system
*  where there's, you know, dopamine projects to habitual related brain regions.
*  I just rolling her eyes when I said to which is great.
*  But, you know, there's traditional dichotomy and then there's goal directed behavior,
*  which is related to a different system and projections in the brain.
*  And one of the things that you're doing, successor representations, is talking about
*  how these systems both interact and how there's different sorts of algorithms like you were
*  just talking about.
*  But then but then it seems like it's silly to talk about just reinforcement learning
*  systems on their own because working memory interacts with it.
*  And so does episodic memory and executive function.
*  And it seems like we're getting a more holistic picture.
*  I think I'm just repeating myself now, so I apologize about what it means to interact
*  and be intelligent. And I'm wondering if you feel like is that changing our conception
*  of intelligence? Are we really on the verge of moving, really taking a big step forward?
*  So I'm going to acknowledge a couple of sort of advances that we're already around,
*  at least in neural networks, the idea of working memory, episodic memory and within the
*  neural networks field has been around since the 90s in the works of someone, for instance,
*  like John Cohen or Randy O'Reilly.
*  The idea of because of the prefrontal cortex hippocampus and then lateral temporal lobe
*  sort of natural ways and also earlier theoretical work that we have from Andel Tolving
*  or Moskovich and others, there is a natural way in which different kinds of memory have
*  always been a part of the idea of learning.
*  And I think that you're totally right that reinforcement learning was a little sort of
*  later to incorporating either the idea of external memory, which would be sort of a
*  long term storage or the idea of working memory.
*  And I think that there has been some beautiful work by Anne Collins and others, especially
*  with regards to dissociating the contributions of reinforcement learning versus working
*  memory to things. The inclusion of various sorts of cognitive functions is definitely
*  for me. Also, I think that that's reflected in the question that you're asking is quite
*  important in the models that we develop.
*  And I think that I would like to acknowledge that this is in contrast to the idea of some
*  folks who think that we need to first understand entirely a fly before we can talk about
*  human cognition. And I think that this kind of a bottom up approach versus the kind of
*  let's focus on the capacities that happen in humans, for instance.
*  I think these are two other kind of distinctions and they are particularly pertinent and
*  important in neuroscience, but they're also important in the ways that we start to
*  approach these different capacities in modeling.
*  And so I think that it would be a very interesting time if we are both sort of trying to
*  look at minimal architectural requirements to have these capacities and have the
*  functions that these capacities have at the end of the day, but also have some sense of
*  perhaps what happens when we start to need to develop memory.
*  What are the evolutionary pressures that would require a creature to remember things?
*  I think that they are both very interesting questions, but I don't think that we need to
*  understand one first to understand the other so they can happen in parallel.
*  And I think that reinforcement learning has been contributing here and then, but can has a
*  lot more to contribute also in the future.
*  AI work that I would like to sort of highlight.
*  Well, there is sort of some work that Greg Wayne and others have done at DeepMind that I
*  think are very interesting.
*  And they tried to incorporate sort of external memory.
*  And we had some discussions about this.
*  We were both talking at a workshop at Cosine, which was the last conference in person that I
*  just just when the pandemic hit.
*  Cosine 2020, right?
*  That's right. That's right.
*  And so we had conversations about this.
*  So there are particular ways in which the kinds of external memory that our models are
*  currently incorporating are not very efficient.
*  And John Langford, for instance, my colleague at Microsoft Research has some has done some
*  work, not just on contextual bandits, but also on contextual memory trees and various kinds of
*  approaches that will have a more efficient memory.
*  And what do I mean by that is when you're inserting new memories or finding them, how do
*  you scale with regard to the how does your search or your insertion scale compared to the
*  number of memories per se?
*  Is it N squared?
*  Is it log?
*  Is it order N?
*  And this makes a huge difference how useful your memory is.
*  And it makes a huge difference, puts a kind of a pressure of what things you need to prune or
*  you need to delete and what needs you need to abstract together, for instance.
*  So these kinds of considerations on memory, I think it goes way beyond the idea of, oh, let's
*  have memory. I think that that's where we are.
*  I think we are way I think that we are in a good spot now to use our models of memory.
*  And I'm a very big fan of computational models of memory.
*  I've I've been sort of going to specific conferences for this one is context and episodic
*  memory that Ken Norman and Mike Kahana have been organizing for, I think, 10 years now or more,
*  15 years. I'm not sure.
*  A long time. I've been going to it for seven years myself.
*  And just every year seeing senior and more junior scientists share their computational
*  models of memory and discuss it.
*  And some people focus on working memory.
*  Some people focus on recognition memory.
*  Some people focus on episodic memory.
*  Some people focus on conjunctive representations and how they lead to, let's say, schema or
*  associative statistical learning.
*  And others say, oh, no, it's a recurrent neural net that just unfolds things and makes
*  inferences every time you need to know.
*  So the differences between all of these camps might seem subtle from the outside, but it's a
*  beautiful space to think about memory and develop new models of memory in ways that would
*  encompass all of the different parts of the state space, offline and online memory
*  processes. If you thought so.
*  In one of my talks, that was a commentary of someone else's talk.
*  I used the kind of sort of a 3D space.
*  And so there were different access and I could then place their work and my work and the
*  ancestor of their work.
*  And so how things are moving in my models of memory space.
*  I think that there are a lot of exciting, many different exciting new directions for not
*  just memory, computational models of memory development, but also experiments that would
*  test them and associate them, that would cover and span across different spaces of memory.
*  I do think we are at an exciting point for that.
*  And I think the next 10 years are going to be hopefully more creative than the last.
*  One of the things that you mentioned when talking about the uniqueness of humans and the
*  explosion of potential algorithms is that it doesn't necessarily need to be related to our
*  evolutionary fitness or our evolutionary goal.
*  And I was going to ask you if ultimately we're going to have equations that relate the value
*  function, you know, the trying to maximize, quote unquote, our value, our reward over time, if
*  we're going to be able to relate that in equations to, you know, something like the ultimate end of
*  value, which is self-replication, some sort of evolutionary objective function, fitness
*  function. Right.
*  But what you said suggests otherwise that maybe we're beyond that.
*  But I would counter and say some sort of political structural cultural structure that
*  lasted two thousand years is probably great for self-replication.
*  So I just want to get your thoughts on that, on on, you know, how whether we're going to tie
*  reinforcement learning to evolution mathematically.
*  Yeah, that's a great question.
*  It's actually something that I'm working with currently with two of my wonderful colleagues at
*  Microsoft Research, but it's in early stages.
*  So I don't want to say too much about that.
*  What I do want to say to the comment that you were making earlier is that.
*  So, yeah, hopefully once we have those works, we can talk again.
*  But just going back to the comment that you mentioned, I think this is why meaning and
*  philosophy matters so much.
*  I think we can change the that ultimate value function you're talking about or determine it
*  on the basis of a particular meaning or philosophy that we have about our lives.
*  And I think that is profoundly human.
*  And it is, of course, every every fascist system has been very interested in discarding
*  this as error, as noise.
*  I'm not sure if I can ever agree with that.
*  At the same time, is the goal the sustainability of the species or is it every single person's
*  genes? Because if it is the latter, we are doing terribly at it.
*  We are really doing terribly at it.
*  We're destroying our habitats as well as our chances on it by overpopulating Earth.
*  So I'm not sure if I agree with you that even from what we are seeing, we are going in that
*  direction so far. I think there is.
*  Yeah. But do you think that we have a good grasp on what the evolutionary goal is?
*  Because that is a computational level question, which are hypotheses that we think we
*  understand. But yeah, how would how would we know?
*  I think a lot of us think about this a lot, including my astrophysicist friends who think a lot
*  about Big Bang and the entropy increasing and all that.
*  And I am comfortable saying that I don't have a good answer to that.
*  And I'm not convinced that the ideas of evolutionary fitness that we currently have are
*  entirely accurate when it comes to humans.
*  That doesn't mean, oh, I don't want this to turn into somebody thinking I'm questioning
*  evolution. Absolutely not.
*  It's not that. I'm just thinking that there it might be limited the way that we are currently
*  thinking about what is the notion of fitness for humans.
*  This is what I was going toward.
*  Yeah, exactly. Yeah.
*  So I'm very comfortable saying that I am not confident about the answers we have so
*  far. And I'm not confident whether we are on the right track to even give the answers to
*  that. And as a species, I think it's a question that we will keep asking and asking until
*  the last day that we exist, because there's going to be a last day at some point.
*  The big crunch or heat death.
*  One of the two.
*  At some point. Yeah.
*  That's why astrophysicists are interested in this question, too, because at some point you
*  need to think about what happens after humans.
*  Right. AI happens after humans.
*  OK, Ida, it's been I'm sorry I've taken you so long without talking about successor
*  representations. Let's talk about your work a little bit, shall we?
*  So we talked about reinforcement learning at large, and I mentioned this classical dichotomy
*  between model free reinforcement learning and model based reinforcement learning.
*  And these days, there's a lot of work being done on how those two systems interact in the
*  brain, you know, and whether they're competitive or cooperative.
*  But there's also a lot of work like your work on successor representations that suggest
*  there are in betweens in between algorithms.
*  So maybe you can just start off by telling us what is the successor representation mapping,
*  I suppose, framework and maybe how it relates to model free and model based.
*  Of course. So imagine if I need to go outside of my apartment and then go outside the house and
*  then go right.
*  And then there is a bakery around the corner that I really like it.
*  Maybe I need to just like walk two blocks towards right.
*  And my model free, if I was a model free agent, I would just say right good.
*  And that good is a little bit more quantifiable in terms of discounted expected future value of
*  the action go right, which means what is the the reward that I expect to get discounted by how far
*  away it is from me if I go right.
*  And it has no information about how many blocks away it is.
*  It has no information about what are the streets in between or how many houses there are in
*  between.
*  Now, a model based reinforcement learner would have some idea of abstraction of the states into
*  discrete states.
*  Let's say that the world was such that there were some kind of states in the tabular case, there's,
*  of course, continuous situations.
*  I'm going to make it in the most simple scenario.
*  Let's say that this was a grid world.
*  And again, I was supposed to go and go to the bakery.
*  It will have a vector of rewards that tells me what is the reward that I will get for every state
*  that I might occupy.
*  And also it tells me what is the probability of transitioning from every state to another on the
*  way to the bakery on the way to the bakery.
*  So at the moment when I want to plan to go and buy bread, my model free will say right good.
*  And my model base would say, well, I go downstairs and take a step right and then take a step right
*  and then take a step right.
*  And it just does that.
*  And then at the end of it, it figures out that, oh, and then there is the bakery.
*  Therefore, this is good.
*  So it takes me longer.
*  It's going to take me longer to make the plan.
*  It's going to take me longer to get there.
*  But at the same time, if all of a sudden one of the streets in between is blocked, model free,
*  if somebody says, hey, that street is blocked, model free is still going to go outside and say,
*  right, good.
*  Habitually, one might say.
*  Exactly. Model based is going to say, OK.
*  I need to take the right, right, right.
*  Oh, I hit a boundary.
*  So I take left, left, left and right, right.
*  So you found the detour or something else, but it takes also a lot of time.
*  However, it takes exactly the same amount of time than it took last time to find your way to the bakery
*  because it's kind of unfolding all the probabilities one step at a time, unrolling them in order to
*  compute the expected value before it makes that decision.
*  There are, of course, approaches like the Dynah approach, where a model based is training the model free
*  offline. So when I hear that the street to the right is actually blocked, so I cannot get to the bakery
*  that is two blocks away, then model based starts to replay one step at a time the steps to take when I'm
*  not making the decision and then retrains the model free so that it takes left and it takes the other
*  path instead.
*  So by the time that I go downstairs, even though model free didn't have the chance to learn and it
*  couldn't do it on its own, it goes downstairs and he thinks, oh, left.
*  Good. And so some people confuse this idea and they say, oh, no, but if you let it let the model free
*  train itself, it will learn.
*  It's like, yes, but it needs to actively go to that location, see that it's not getting a reward and
*  then go the other way.
*  And that's a very powerful distinction between, I guess, what Tolman thought in terms of a cognitive
*  map based approach as opposed to the behaviorist dogma of the time that Tolman was the cognitive
*  revolution or part of the cognitive revolution against.
*  And in his case, the example was latent learning.
*  He observed that if rodents just run around a maze for a while, for a couple of days without any
*  rewards at all, later when he introduces a reward somewhere in the maze, the rodents are going to be
*  faster at learning the policy to reward than rodents who had never been in the maze.
*  This is against the behaviorist dogma that you need the reward in order to be able to learn something
*  about the world.
*  Right.
*  So in the case of the model based, it could have been learning the probability of transitions and
*  storing them in its sort of model of the world or what some call the dynamics of the environment
*  without having to independently of whether there were rewards or not.
*  Now, there are certain kinds of predictions.
*  Like I said, it does take the same amount of time for the model based or it is equally good at going
*  right and left, whether there is a detour or not, as long as it knows or as long as it has learned that
*  like little change in the world, because it's unfolding.
*  It's all of its probabilities in order to decide what to do.
*  And that was the sort of the key distinction between any approach that is combining model based,
*  model free or is model based.
*  And this other approach that I will talk about in a second, which is somewhere in between.
*  So what is that approach?
*  We said that model free caches the value of actions, but doesn't care about states and model based has
*  the one step by one step dynamics of the environment and separately stores rewards.
*  The successor representation caches multi-step dependencies and separately stores rewards and
*  then combines the two of them.
*  The difference that it has with model free is that it doesn't cache value of actions.
*  It has some information about the map of the world.
*  And because of that, if you just move the reward around, it's going to be still very good at finding
*  the optimal location of reward.
*  And we are very often in environments where the reward moves around, but the environment dynamics
*  change less often than that.
*  However, there are times that the environment's dynamics change.
*  For instance, if you live in New York City, the A train and the F train, they sometimes run in each other's
*  lanes and one train and two train do the same thing.
*  So if you want to go to Brooklyn from Columbia University, you might be careful because you might end up
*  at World Train Center if you fall asleep on a train and it was actually running on the one.
*  So that did not happen to me, but it's the thing that has happened to us very specific, I know, because
*  it has happened to someone else.
*  So what happens in the case of the successor representation when transition structures change?
*  In that case, if it's just a successor representation alone, the way that Peter Diane introduced it in the
*  early 90s, what happens is that the successor representation has inherited this multi-step map that
*  from here there is a path to the bakery and it combines it sort of with the location of the reward,
*  which is in this case, I'm going to the bakery, but if I wanted to go, I don't know, to a cafe, then it
*  would have been, the reward would have been a different location.
*  The map would have been similar.
*  But if there is a detour or something that maybe I have learned because I was going from another
*  direction and I found that that street is closed, the successor representation still has
*  grandfathered that old multi-step relationship between where I am and the location of the bakery.
*  So in the absence of some kind of replay that would piece things together, it's not capable of
*  updating that, but it is capable of updating going to another place for value.
*  So for instance, if the bakery moved somewhere else, so it just moved the reward, Model 3 still
*  can't solve it. It would still think right, good, unless it experiences that it goes left.
*  But the successor representation can because we just changed the reward value,
*  sorry, the reward vector, but not the map of the environment.
*  Now the one that the algorithm that I proposed is SR-Dynite combines replay together with
*  successor representation. We have another variation of this that combines model-based and the
*  successor representation. Why is this so different? Because the idea of this conjunctive representation
*  predicts a certain kind of asymmetry in performance on certain kinds of tasks compared to others.
*  Remember we talked about the importance of AI making errors or artificial agents making errors
*  similar to errors that humans make. And so that was the origin of designing a task that
*  asymmetry will come to be, where a model-based would be expected to perform equally well on
*  all of the conditions, model-free would be expected to perform equally bad on all of the conditions,
*  and the successor representation would be very asymmetric, while the successor representation for
*  us replay would have this kind of asymmetry, but would be able to do something still as long as it
*  got enough replay. Some sort of compensatory mechanism? I would say updating mechanism. So
*  it's capable of updating its own representations offline, as opposed to either relying entirely
*  on online computations at the moment of decision, like the model-based, which will not be rational
*  in case you want to run away from an animal to a shelter, because you might get eaten before you
*  have the time to process one step at a time all of the things. So if you're time constrained at
*  the moment of decision, there would be a pressure that you have a system that can make a decision
*  fast. You want a mechanism for decision making that's fast. Now the trade-off between model-based
*  and successor representation learning is one is very slow at the moment of decision making,
*  the other takes a lot of memory. Its representations occupy a lot of space,
*  and that's when you can see how this relates to this idea of depends on the kinds of environments
*  you live in, depends on what kind of decisions you need to make in order to, I guess the word is
*  survive, something else we've discussed. And so, or solve the task or whatever the sort of
*  intermediate goal is towards that survival. Find your mating partner. For instance. So all of these
*  are interesting algorithms. To the best of my knowledge, we don't have any evidence of
*  exclusively model-free anything in the brain, and we don't have an evidence of exclusively
*  model-based anything in the brain. And in fact, if you look at even the dopamine system,
*  there are situations where you see things you don't expect to see in model-based in the brain,
*  which is something that we discussed in a paper in 2017 in Plus Computational Biology
*  with my very talented colleague, Evan Rusek, and together with also Nathaniel Dahl, Sam Gershman,
*  and Matt Botvinnik. And in that paper, we discussed the successor representation DINA approach
*  as a middle ground between model-based and model-free. And it's a computational paper,
*  but we simulate examples that are the detour task and some other tasks that in our other paper with
*  that nature of human behavior, where we had the tasks that are asymmetric, we sort of show them.
*  And the asymmetry is exactly in the examples I've already given you. What happens if my favorite
*  restaurant or bakery moves somewhere else, which is just the change in the vector of rewards as
*  opposed to change in the environment, but what happens when the dynamics or transition structure
*  changes, like train two runs on train one, then I need to sort of change my plan because of a
*  different reason. It's not that my goal location or the reward has changed, it's that the transition
*  structures in between to get there has changed. So I need to change my map or update my map
*  adequately in order to be able to still get to the same location. And the prediction is that
*  success representation alone would not be able to perform the transition revaluation condition
*  where you have to or transition transfer, whereas it can be very good at solving the
*  reward evaluation where the location of the bakery changes. Model-free is not good at any of them,
*  and model-based is equally good at both. And SRDINA is better at reward evaluation,
*  can solve the other one, but it's a little worse because it depends on this extra computation to
*  update its maps. So if you take an average of a hundred times an agent doing it or different
*  agents doing it, it would be on average worse than how good they are at doing the reward evaluation,
*  even given noise and everything else. By the extra computation, you mean the offline replay?
*  That's right. So that's what I can say about the basic sort of principles of it.
*  You know, you started off by mentioning that there isn't really good evidence for a strictly
*  model-free or a strictly model-based system in our brains, but our brains, speaking of the hardware,
*  there's a ton of it. And the capability to implement many algorithms is inherent in the
*  hardware. And this relates to what we were discussing earlier, but do you think that we are just
*  running all of the possible reinforcement learning algorithms all the time in parallel
*  and didn't switching the outputs, or are there a set of four standard RL algorithms in our brain
*  that we switch among? What's the granularity of the sheer volume of
*  types of reinforcement algorithms we're running? That's a great question. And I can
*  I'm comfortable saying that while I have some speculative ideas in this domain, I don't think
*  that we are at a place where we know the answer to that. There are some people who would like to
*  think, oh, it's cognitive maps all the way down, or some people might want to think, oh, it's
*  success representations all the way down, or if it's model-based all the way down, or it's model-free
*  and model-based, and then the combination. And I understand the appeal of those ideas,
*  but I genuinely think we are not at a place to know all the different kinds of algorithms that
*  are happening at different cognitive domains and different parts of the brain. And even the same
*  part of the brain could have very different kinds of algorithms. Again, especially in humans, this
*  is very much the case. So I'm comfortable saying that while I might have some ideas or theories
*  for the next steps to take, I don't have the final answer. There is this spectrum of needing
*  to know what you need to do at the very next step versus super long-term planning. And a lot of what
*  you do is related to how our memory relates to our future planning. But as I was learning about
*  successor representations, what jumped out at me was thinking, because you can skip connections,
*  and you don't have to run, like in model-based learning, you have to run the entire simulation
*  to get from point A to point Z. You have to go through all the letters. Whereas in successor,
*  you can skip over them because you cache the various stages in between. And it jumped out
*  at me that that might be a way for us to develop heuristics or intuitions about what to do without
*  necessarily running the entire model in our head. You just kind of know what to do in a given
*  situation, and a successor representation like structure might underlie that kind of
*  process. Is there anything to that? I think I share your intuition, especially when we are
*  speaking about... Yeah, see what I did there? I saw what you did there. Especially when it's
*  multi-scale successor representations that we are talking about. And at different scales,
*  you can have certain kinds of hunches because you have lumped together a bunch of different things,
*  so you can actually go to the next step more freely. This is something that I'm quite excited.
*  I've been having conversations with some folks about this, and hopefully this will lead to some
*  future work. And there have been other people who've tried this out, which is this idea that
*  there are particular structures also that we start to learn after having these kinds of
*  multi-step things. And later on, not only are we more likely to perhaps have these kinds of multi-step
*  AC, AD, AF hunches, which is different from the re-merge model, because it will need to do the
*  recurrence every time. And their argument to us would be that, hey, you could get the same intuitions
*  with just very fast recurrence. So just to be fair to them, I'm going to voice that position as well.
*  But there is also a way in which if you have these kinds of multi-step landscapes, you might be able
*  to abstract the relational structure. And then if you have a memory for those structures, next time
*  that I'm testing a hypothesis, I can just think in terms of evidence I can look for to search which
*  of the underlying structures might be the case. And this is very similar to the idea of schema,
*  for instance. I am capable, very comfortably capable of going to infinite number of airports,
*  as long as they have the same structure in terms of the larger scale graphs. I mean, if they let me
*  in, I'm Iranian, so I should remember that. Oh, come on. It's true. I'm sorry. Yeah.
*  I don't know why you're protesting, but yeah. No, no, I'm just saying,
*  yeah, no, I'm not protesting your statement. You just slipped it in. That's what I was reacting to.
*  Yeah. It's my life. So there is an interesting way in which I'm capable of going to infinite
*  number of airports. And as long as there are the same similar number of steps in them,
*  and there is not something out of the blue, the colors might be different, the location, the size,
*  the buildings, how many floors, which floor something is, so many things can be different.
*  And the same schema will apply to the idea of airport, or I can go to a lot of different
*  restaurants. Sure. As long as it's not some seven course meal that has too many forks and knives,
*  I think I can manage to apply it and to subscribe to the same schema across them.
*  One of the famous examples is just ordering the structure of back and forth with the waiter. Hello,
*  how are you? Drinks, menu, et cetera. And that sort of, I don't remember who it was,
*  where that example comes from, but that's in my head, one of the classic examples of this sort of
*  schema. Yeah. So I think that there is a way that there might be a link between these multi-step
*  ADAF approaches and the extraction of structures that are more abstract, like schema, that don't
*  need to be very detailed in terms of the implementations. So the re-merge idea might not work well for that
*  kind of an idea of sort of schema or testing different structures. I'm sure that they can come
*  up with something a deep mind that would solve it, but that's not what I'm, I'm not suggesting that
*  that's not possible, but I wonder whether in principle it just simple principles of
*  conjunctive learning might naturally give rise to this without us needing to inject a lot of extra
*  inbuilt constraints or rules or architecture. So we're just about out of time. I want to just bring
*  it way back out and end on just a broad reinforcement learning type questions. Yeah,
*  of course. So one of the things that reinforcement learning is famous for is that it spans all of
*  Mars famous levels, computational level, algorithmic level, and implementation level, that there's
*  evidence, you know, and we can make sense of it at all those different levels. If you were going to
*  be known on your, you know, to have to headstone for discovering something, you know, if you had
*  to choose between being known for discovering something at the implementation level, at the
*  mechanistic level, that changed the shape of our understanding of the, of a computational level
*  process, or of discovering or describing a new computational level process that then we could use
*  to constrain our knowledge and move forward and discover new things about the implementation level,
*  which which would you choose? Does that make sense? And which would you? Yeah, I think I'm,
*  I think implementation level is not the one that makes my heartbeat or wakes me up in the morning
*  with a sense of joy or motivation to do things. Not to discount it, I'm very happy that there are
*  a lot of colleagues that are doing a great job at it. But I think that the computational algorithmic
*  sort of levels are sort of more, I hope that I can contribute something there. Yeah. And even maybe
*  even scoping out of it, because if we're then thinking about multi agent settings, we might even
*  need to go even a step higher. So I think that if there was something to be that that would
*  outlive me, if there was an idea, we all hope that some ideas outlive us. Yeah. I hope that it's
*  at multiple levels, but I definitely hope that it's at a higher level enough so that it can
*  inspire a lot more work. Well, I wasn't trying to isolate the levels. But so, so, traditionally,
*  the way that science seems to work is that you have some computational level hypothesis, right?
*  And then, and then a lot of people say, well, the only thing the implementation level is good for
*  is just confirming the what you thought to be the computational level process, right? After you name
*  the computational level process. And very, very rarely, if at all, if ever does, does work in at
*  the implementation level, then translate up, let's say, if you're going if you have to give a direction
*  up to the computational level to change a computational level description or framework of
*  thinking. And so that's why I was wondering, because it'd be pretty rare and pretty powerful
*  to be able to do that, I think. I think the interesting thing is that implementation level
*  can sometimes help us if our goal is for all of them to be, let's say, human oriented or biologically
*  plausible. The implementation level can sometimes help us choose between different computational
*  sort of theories. So there is a, you know, at the meta level, when you're deciding between different
*  theories, it might be helpful to think about a kind of a recurrence at different levels that are
*  going on. And so all that I want to say is while I will always look at the implementation level for
*  correcting the theoretical level, it's just that the thing that I hope that will outlive me is
*  something that is at a higher level. Oh, it's so much more fun to just to think about in terms of,
*  you know, in terms of thinking theoretical is so much more fun. Final question, I can't let you
*  get away before I ask you this. It seems like the reinforcement learning world is a world of cold
*  mechanical processes that could all go on under the hood of our awareness, of our consciousness,
*  of our subjective experience. And I'm wondering if you think that these algorithms and related
*  computational level processes, if reinforcement learning work will contribute to our knowledge
*  of how subjective awareness comes about, be careful with your words when you talk about this stuff.
*  Yeah, emerges. That's a bad word. You know, things like that.
*  Yeah, you got to also be careful when you're responding to it. Of course.
*  So in response to the cold idea, I have to say that, sorry about the pun, but reinforcement
*  learning is rewarding. But well, I don't mean that people are cold. But the idea of like learning a
*  structure, learning a map, and it just seems very unconscious. Yeah. Yeah.
*  So I have thought about this. What would be a theory? I mean, I wonder what even would be,
*  no matter how fuzzy and warm, what would be an approach to this idea of subjective experience?
*  So there's a lot of work on subjective value, right in the neuroeconomics world. I thought
*  you might tie it back into that. That's the way I see in for a potential answer from someone of your
*  ilk. I think that there are two directions about this. One thing is,
*  I think it gets similar to what I guess
*  Yasha Bengio works on these days. So there is a sense in which if you have different inner
*  mechanism, and one is just like doing things, and one is just trying to understand this thing and
*  connect it to other things. And it goes back to Bernard Barr's idea of global workspace and what
*  he thought was the emergence of, I'm using it in a colloquial term, as a colloquial term,
*  emergence of subjective experience or sort of qualia, if you want. So there is that kind of
*  approach to it, which is this idea of there's going to be some need to constrain which information
*  from all of these parallel streams that are coming in to choose from and which wants to pay
*  internal attention to. So there is a mental action, there is a requirement to coordinate them.
*  And one idea is that that seemingly cold mechanism is actually what's giving rise to this sense,
*  and potentially mixed with a cocktail of various kinds of neurotransmitters that happen in order to
*  center everything in one direction. And I guess the Edelman-Tononi idea was that,
*  well, that's linked to some notion of complexity, and you need some sense of high complexity,
*  but their notion of phi is kind of is good for smaller scale, but it's unclear how we can think
*  of it in terms of large number of neurons. So yes, we need large enough number of neurons and
*  parallel processing so that there is a need to somehow take mental actions to choose between them.
*  And then so there is a whole long history of it, and I'm not going to get into it. But depending
*  on which you subscribe to, reinforcement learning could potentially contribute. But the reason I'm
*  mentioning all of them is to highlight that at the end of the date would depend on the philosophy
*  that you subscribe to when you want to approach the question of subjective experience. When it
*  comes to the subjective value and the different things that might be of value to you, I think the
*  work in proto-value function and some work that hopefully we will sort of advance on how do we
*  evolve certain sort of different dimensions of value. All of these things could speak to that
*  in ways that perhaps is not the way that economics is looking at it, but it's a little bit more
*  towards the way that is closer to how us neuroscientists might think about. So I think
*  that some parts of your question, there might be already existing RL approaches that are answering
*  and other parts of your question will completely depend on the philosophical stance that we are
*  taking in order to model, understand, and approach a particular human capacity.
*  That's great. Bringing it back to philosophy as always. Thank you so much for taking the time.
*  This has been really fun. I wish we had a lot more time to talk and maybe in the future we can,
*  but continued success and thanks. Thank you so much. I really appreciate it.
*  Brain Inspired is a production of me and you. I don't do advertisements. You can support the
*  show through Patreon for a trifling amount and get access to the full versions of all the episodes,
*  plus bonus episodes that focus more on the cultural side but still have science. Go to
*  braininspired.co and find the red Patreon button there. To get in touch with me, email paul at
*  braininspired.co. The music you hear is by The New Year. Find them at thenewyear.net.
*  Thank you for your support. See you next time.
