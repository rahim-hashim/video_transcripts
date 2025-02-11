---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3964s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 939
Video Rating: None
---

# BI 018 Dean Buonomano: Time in Brains and AI
**Brain Inspired:** [November 14, 2018](https://www.youtube.com/watch?v=t7n-4Paxvjs)
*  Certainly, our perception of subjective time is a product, a fabrication of the brain.
*  A wonderful fabrication, a wonderful illusion, if you will, in that it's created by the mind.
*  This is Brain Inspired.
*  Hello curious and ambitious people.
*  Well, in a couple of days, I'm packing up the car with my 3-year-old, my 6-year-old,
*  and my wife, and we're driving 18 hours over the course of two days to go see my family,
*  and then a week later we're turning around and doing it all again.
*  Why am I telling you this?
*  Because I may not make it.
*  If I don't make it, if you hear about a quadruple murder-suicide and you don't get a Brain Inspired
*  episode next week, let me just say it's been fun.
*  If you'd like to prevent the show ending in such an abrupt fashion, please overnight me
*  some MDMA, you know, Ecstasy, Molly, send me some shrooms, something, anything that lasts
*  a long time and forces unconditional love to emanate from me.
*  Another way that you could support the show and my burgeoning drug habit is through Patreon.
*  You can go to patreon.com slash Brain Inspired or you can go to my website braininspired.co
*  and click the red Patreon button there and you can support the show at either $2 or $4
*  per month.
*  That's a cheap cup of coffee or a latte per month respectively.
*  For those of you who have given your support recently, James, Katja, Camilo, Hester, thank
*  you so much.
*  Those coffees and lattes that I drink while I edit and prepare the show are the most delicious
*  I've ever tasted.
*  Okay, today's show I talk with Dean Buonomano, time researcher extraordinaire.
*  He's written two excellent books, his most recent of which we mostly focus on, called
*  Your Brain is a Time Machine, the Neuroscience and Physics of Time.
*  When I read this book, it not only taught me a great deal about what we know about how
*  time works in the brain and how physicists largely think about time, but it really scratched
*  my physics itch, which sounds awesome and terrible at the same time, I'm sure.
*  But it sent my mind reeling and soaring into wonderful places and that may sound effusive,
*  but it's true and I highly recommend the book.
*  So during the show we mostly talk about the neuroscience of time, but we also discuss
*  how this interacts with AI.
*  We talk about the nature of time in consciousness and a lot more, of course.
*  This is a fascinating topic and I hope to explore it more on future episodes.
*  You can find the show notes at braininspired.co.
*  slash podcast slash 18.
*  Alright please enjoy our discussion.
*  Welcome Dean Buonomano and thanks for being here.
*  It's my pleasure Paul.
*  Thank you for having me over.
*  Thanks for playing along.
*  And thank you for giving the listeners an example of our ability to understand speech
*  at different speeds.
*  Yeah, well, I've got to start right off the bat.
*  There's just so much that we could talk about.
*  So okay, I will have said a few words about you in the introduction, but by way of a short
*  introduction here, you run a lab at UCLA in which you study time.
*  You do neurophysiology experiments, psychophysics experiments, and you build models of how the
*  brain perceives time and durations and implements sequences over time.
*  But I'd like to rewind for just a second, if you will.
*  Is it true that in high school in the early 1980s that you programmed reaction time tests
*  into a computer and performed these tests on your family members?
*  I did.
*  I was fortunate to live in that very special window of computers where in the mid 80s, right,
*  where computers are just becoming available, but nobody knew what to do with them.
*  Right.
*  Unlike the new generation, right, where there's plenty to do with them even if you don't learn
*  how to program.
*  But back then, you knew they were cool, but you couldn't do anything unless you actually
*  programmed to do something.
*  And I did.
*  I did definitely ask my family and friends to do reaction time tests and lexical decision
*  tasks in terms of to measure and quantify how long the brain took to solve certain types
*  of problems like recognizing a word and that would take 600 milliseconds.
*  It's a lot of fun.
*  Yeah.
*  Do you still have any of your old data from those days?
*  You know, I probably do, but it's in those old floppy disks that I can't access.
*  Right.
*  Like the really, like the three, the bigger floppy disks.
*  Yeah, those guys.
*  Those guys.
*  No one will know what we're talking about.
*  No.
*  We're dating, you're dating yourself too, Paul.
*  Well, that's okay.
*  I'm out of it the field, so who knows, you know, it doesn't matter to me anymore.
*  So fast forward to graduate school and you studied neural plasticity in a plesia.
*  And of course you published in Science Magazine.
*  Where else would you publish?
*  And then while you're in graduate school, you attend a lecture by Michael Mach about
*  time encoding in the cerebellum and that big lobe in the back of our brains.
*  And this either reignites or adds fuel to your fire and your interest in time.
*  And to, as you know, to a man with a hammer, everything looks like a nail.
*  So you married your plasticity knowledge with time and you decided to test whether short-term
*  plasticity could be used to tell time.
*  And indeed you showed as much at the sub-second scale.
*  So timing below a second.
*  So you built computational models that showed this and you even showed this in vitro in
*  neuronal culture cells in petri dishes.
*  And I discovered you because of your work with recurrent neural networks and how their
*  intrinsic dynamics can be harnessed to tell time, which led me to your books, which we'll
*  talk about in the rest of your work.
*  So if you'll play along, let's spend a second just appreciating the nature of what you are
*  tasked with figuring out in the brain.
*  So you and I both agree that one of the most fundamental jobs of the brain is to predict
*  the...
*  The future.
*  Thank you.
*  And as humans, relative to other animals, we have perhaps a unique ability to mentally
*  time...
*  Speech.
*  Oh, really?
*  Travel, mentally time travel.
*  Okay, you're one for two.
*  And it might be a bit macabre actually.
*  So for example, Dean, do you ever think about when the day might come that you yourself
*  will...
*  Die
*  Two for three, not bad, sir.
*  Okay, so let's move on.
*  And this is a speech that you're predicting the ends of my sentences for me.
*  So thank you.
*  You're welcome.
*  So your brain is a time machine.
*  The neuroscience and physics of time is your most recent book.
*  Your first book called Brain Bugs, I hope to ask about show.
*  But your brain is a time machine.
*  I love this book.
*  It is about the neuroscience and physics of time, but it's also about the history of studying
*  and conceiving of time and how physics and neuroscience of time compare, whether they're
*  compatible, the different scales of time from circadian rhythms on the larger scale down
*  to the really tiny millisecond scales, the subjective nature of time, consciousness,
*  free will, relativity.
*  The word comprehensive comes to mind.
*  So this is a great work.
*  It's great storytelling, actually riddled with humor as well.
*  So thanks for running the book.
*  You're welcome.
*  Just a few fun facts and then I promise I'll let you I'll shut up and let you speak here.
*  I was an H.G. Wells fan.
*  So it was interesting for me to learn that H.G. Wells book, The Time Machine was the
*  first to mention time travel in that the time traveler is actually interacting with the
*  past and the future.
*  Is that really true?
*  You know, I think if you look hard enough in the literature, you can probably find something
*  that might be an exception.
*  So people who know a lot more about the literature than I tell me there's another book by a Spanish
*  author at the same time that also talks about what we might call true time travel.
*  And so for people to understand what we mean by true time travel, you and I are talking
*  about these cases where somebody can go back into the past and interact with people and
*  then come back to the quote present.
*  This is very different from the fact that we can all time travel into the future.
*  For example, if we just go into a meditative state or into a coma for that matter or travel
*  at the speed of light.
*  So it's easy to travel into the future relatively easy.
*  The hard part is going back and then coming back.
*  So that's what we mean by true time travel.
*  And I think it is true that H.G. Wells' book, if not the first, was certainly among the
*  first in that period.
*  It's certainly the most well known anyway among the first.
*  Sure.
*  Another fun fact.
*  So there are no known neurological disorders or conditions that result in people losing
*  the ability to tell time at the scale of around a second.
*  Well, I think it's fair to say that there's no neurological disorders in which people
*  totally lose their ability to tell time across all scales or completely lose their ability
*  to tell time.
*  There's certainly disorders that hamper or alter one's ability to tell time.
*  Maybe they have a tendency to perceive time as going a bit quicker or a bit slower or
*  The old cases in people with certain types of Parkinson's disease or dopaminergic diseases
*  have stories of people sort of moving in slow motion.
*  These are the types of stories in the movie and book Awakenings in which Oliver Sacks
*  talks about people moving in slow motion.
*  But nevertheless, those people could still sort of appreciate music or understand speech.
*  So they could still tell time.
*  So there's no, what we talk about is there's no centralized disease that's predominantly
*  characterized by an inability to tell time across all its shapes and forms.
*  But many diseases modulate timing on one time scale or in one form or
*  A little more fun one here.
*  So do you know what a Mondogreen is?
*  I do.
*  Excuse me while I kiss this guy.
*  Yeah, yeah.
*  Yeah.
*  So it's hearing alternate lyrics in a song, which has to do with the timing, among other
*  things of how fast or slow you're singing the lyrics, for instance.
*  And in fact, I happen to know or at least I believe because of Jimi Hendrix's album
*  Live at Winterland.
*  I believe it's on that one where he see he was aware that he was there that the
*  Mondogreen was prevalent in that song.
*  Excuse me while I kiss the sky is the lyric, of course, but people mishear it as excuse
*  me while I kiss this guy.
*  And I there's purple haze, I believe.
*  And in that rendition, he sings, excuse me while I kiss that policeman over there.
*  So so he was at least.
*  So although the term Mondogreen, I don't think had yet been coined, but he certainly knew
*  then that there was the ambivalent or ambiguous hearing of that.
*  That's very interesting.
*  Yeah.
*  Yeah.
*  Yeah.
*  I sense a humor about it, I think.
*  OK, last last fun fact.
*  Animals, including us, of course, develop spatial abilities before they develop timing
*  abilities, which is is an interesting thing.
*  And we might come back to that.
*  OK, so we can only scratch the surface today.
*  We'll see what we can get to.
*  And these concepts are going to overlap with the review paper in Neuron that we're going
*  to talk about in a couple of minutes here.
*  But maybe we can start with just the types of time to set it up being natural time,
*  clock time and subjective time.
*  Could you just kind of walk us through those?
*  Absolutely.
*  I think part of the challenge and part of the mystery in talking about time, if you
*  walk up to somebody on the street and say, please define time and their sort of look
*  of panic that inevitably develops is part of that challenge is just that time means
*  so many things.
*  And indeed, as you probably know by now, the word time is the most common noun in the English
*  language.
*  And that's because really it means many different things.
*  And especially and that's particularly so in English as English speakers.
*  When we want to know the time, we ask each other what time it is.
*  But in other languages, you don't use the word time for that purpose.
*  You say what hour is it in Portuguese?
*  You say, Kia horas são.
*  So we have to when we're having this debate about time, it's very useful to remind everybody
*  that we really use the word time to mean different things.
*  And I make an attempt to divide that up into three specific types of time, if you will,
*  or flavors of time.
*  Most of the time.
*  There we go again.
*  How often?
*  You must do this all the time.
*  I know.
*  I know.
*  And it becomes a bit annoying after a while.
*  But more often than not, I'll say more often than not than saying most of the time, more
*  often than not, when we're talking about time, we're referring to clock time.
*  Right.
*  We talk about when we're going to when we're going to meet.
*  We ask what time is the show on what time is the game on.
*  And that's clock time.
*  And so that leads to a fairly circular definition of time is what clocks measure.
*  And it's a bit circular because what is a clock?
*  It's something that measures time.
*  But nevertheless, it's very practical and very important.
*  And more often than not, that's what we really mean by time.
*  Time is a measure of change as quantified by a clock.
*  Now, in addition, we have our subjective sense of time, the time that you and I feel consciously
*  as elapsing.
*  The listeners might be feeling, oh, wow, this is going on forever.
*  These two guys talking here and they might have this dilation.
*  So it seems we might be talking for 10, 15 minutes, but they might feel it's been already
*  going on for 45 minutes.
*  So that's the subjective sense of time, which is normally correlated with clock time, of
*  course.
*  And that sort of subjective sense of time certainly goes away when we fall asleep or
*  when you you're an esthetized.
*  Everybody who has had that feeling of going under general anesthesia has that very surreal
*  notion of skipping time, like what happened in between.
*  And it's a very foreign notion that you don't have that subjective sense of time.
*  And then finally, we have natural time or what we might call physical time.
*  And this is the notion of time as the problem in physics of whether time is a dimension,
*  or sort of the fabric of the universe.
*  So in relativity, time means something more than just what a clock measures in many ways.
*  It's something that's seen as a fundamental part of the universe, a fabric of space and
*  time.
*  Now, if that's really true or not, it's still debated, but it's another way in which we
*  use the word time.
*  So I think it's useful to set the tone there in thinking between clock time, subjective
*  time and natural or physical time.
*  I mean, we can really go down the rabbit hole into the physics because it's really interesting
*  to me.
*  But we're going to try to stick toward the neuroscience today.
*  We'll see what happens.
*  Because you have me wondering what's going to happen to all those P's in all the physics
*  equations because it's symmetric and gosh, what are we going to do about it?
*  Okay, so those are the three types of times to start us off here.
*  And what is the multiple clock principle?
*  So I think it's a useful concept when we're talking about how the brain tells time.
*  So this relates to the brain as a device that can tell time, although not as accurately
*  as manmade devices.
*  So how does the brain do that?
*  Is there a central timer that times that's used for your ability to tell time in music,
*  to tell when you're hungry, to go to sleep, to determine your age or not?
*  And here it's useful to come up with an analogy here.
*  If you think about measuring quantities like weight, if you're going to measure a pound
*  of flour, you use one scale.
*  If you're going to measure yourself, you use another scale.
*  If you're going to measure a car, you need another scale.
*  These are different physical devices to measure weight or mass.
*  I'm dependent on the magnitude and clocks.
*  The clocks that we have made, manmade clocks are amazing devices in that the same atomic
*  clock or even the same clock on your wrist or in your smartphone is just a groundbreaking
*  device in that it can measure milliseconds, seconds, minutes, hours, days, weeks, months,
*  years.
*  There's not many physical devices that can measure a property across that vast range
*  of scales.
*  So that would be what we would call a single clock.
*  A single clock across the scales.
*  What I mean by the multiple clocks principle is the opposite.
*  So unlike our manmade clocks, which function incredibly well across scales, the brain has
*  scale-specific clocks.
*  We tell time on the order of microseconds.
*  Just to be clear there, you're not conscious of time on that scale.
*  But if you have a sound to your left, you know it's to your left because your brain
*  picked up the time difference it took to travel from your left ear to your right ear.
*  Interaural time.
*  Interaural time delays.
*  Exactly.
*  So that is done by one circuit in your brain.
*  But you also have a circadian clock that tells you when to go to bed or gives you jet lag.
*  That clock has absolutely nothing to do, absolutely independent of the clock that measures interaural
*  time delay.
*  So what I mean by multiple clock principle is your brain has fundamentally different
*  mechanisms to measure microseconds, seconds, hours, days, and so forth.
*  So we're about to dive deeper into the neural basis of time here.
*  In the book and in the review that you've written, it's clear that time is nearly ubiquitous.
*  It's a nearly ubiquitous feature of brain processing.
*  This is related to models of timing in the brain which distinguish between whether there
*  are centralized circuits dedicated to timing in the brain or whether timing is an intrinsic
*  property of brain circuits in general.
*  Your research strongly suggests, and you believe the latter, that it's an intrinsic property
*  of brain circuits in general.
*  So time is everywhere in the brain.
*  Now last week I had Jeff Hawkins on the show and he just came up with this framework.
*  His idea is that your entire neocortex, all throughout your neocortex, is encoding something
*  like grid cell location based things.
*  So in every cortical column it encodes a whole object actually.
*  This is kind of the theory.
*  So anyway, it's all over the cortex is the idea.
*  That makes me think, do we know of a neural circuit that cannot tell time?
*  I think so.
*  First let me just add something here.
*  So certainly the current hypothesis that's particularly that we favor is indeed that
*  because timing is so fundamental to everything that we do that most circuits should be able
*  to tell time.
*  But that's still a theory.
*  So you certainly find people that might disagree with that statement.
*  But I do think it's becoming more and more accepted.
*  And so we can record signals or neural activity patterns that can potentially encode time
*  in many areas of the brain.
*  Now that doesn't mean that those parts of the brain are necessarily the clock or telling
*  are being used by the animal to tell time.
*  It's just like they're correlated.
*  So you can look at a ball falling down a hill or a skier skiing downhill and you can
*  use that skier to tell time, right?
*  That doesn't mean that that's his or her function.
*  Because if you know that a downhill skier takes two minutes to go from top to the bottom,
*  you can see if they're half, it's probably around a minute that's gone by.
*  So we know that these many neural circuits have these neural signatures that can potentially
*  encode time.
*  But we still have to prove that that's what they're doing.
*  Now to answer your question, I think it's a bit early to say or to commit to the notion
*  that there's certainly some circuits that definitely do not tell time.
*  Because all circuits are sort of dynamic.
*  If they're always doing the same thing, if you have a neural circuit that's always doing
*  the same thing, it's really not doing much, right?
*  Because there's no information in it.
*  If the light is always on, you don't need a switch to control it.
*  You can just have it fixed.
*  So even things that we do every continuously like breathing, those neurons are still changing
*  in time.
*  They're oscillating.
*  They're changing the frequency.
*  So I think I'm hard pressed to come up with a circuit that doesn't change in time.
*  But let's say if it's timing or not, I think that's a tricky question.
*  So let's classify that as a trick question that I refuse to answer.
*  Yes.
*  All right.
*  Good enough.
*  Okay.
*  Well, so this book, it was just super engaging.
*  And I have to confess, I read it over maybe two weeks in my little time window from 530
*  a.m. to whenever my kids wake up.
*  Wow, that's impressive.
*  Well, you do what you have to do.
*  And we're not even touching on the physics unless we come back to it later or the philosophy
*  of time, which was, again, just as fun for me.
*  I'm going to link to the book, of course, in the show notes here.
*  But let's move on.
*  And these, of course, overlap.
*  You recently wrote a review in Neuron, the title of which is The Neurobasis of Timing,
*  Distributed Mechanisms for Diverse Functions.
*  And this covers the latest in the neuroscience of timing.
*  You begin with showing, you know, we understand pretty well some internal clocks.
*  So we talked about these different types of clocks.
*  Like we know a lot about the timing at the scale of the circadian rhythm and how it works
*  on the much larger scale.
*  And then the much smaller scale, like the interaural time delay, we know how those types
*  of clocks in the brain work at the few millisecond time scale.
*  But we still don't fully understand.
*  A lot of the open questions remaining have to do with the scale of 10 milliseconds or
*  so to about 10 seconds.
*  And that's what this review really focuses on.
*  You talk about the need to develop a taxonomy of time.
*  Can you just say what that means and why it's important?
*  So I think a lot of problems that scientists study generate a lot of confusion because
*  when we say we're going to study time or we're going to study memory, what does that mean?
*  If you ask, so let's say the most, one of the most studied and popular fields in neuroscience
*  is what is memory?
*  If you ask those people, please define memory, you know, you're going to get different answers.
*  So the truth is, most of them are not studying the same thing.
*  You think of memory in a computer, right?
*  Is memory the voltage of a transistor, whether you have a little dimple that's burned in
*  by a laser beam on the surface of a DVD?
*  Is that what you mean by memory or do you mean the sequence of zeros and ones that allow
*  us to rebuild a picture or rebuild the voices that you're recording for this show?
*  So memory means different things.
*  And I think one of the really perhaps underappreciated breakthroughs of the 20th century in neuroscience
*  was a taxonomy of memory.
*  So you may know and some of the listeners may know that we make an important distinction
*  between declarative memory or explicit memory, things that you can sort of verbalize and
*  declare the capital of France is Paris or implicit or non declarative memories such
*  as I can juggle and you know, it doesn't matter how well or how eloquent I am as a
*  speaker.
*  I'm not going to teach you how to juggle by just describing the process.
*  It's impressive that you've been juggling this whole time though.
*  And so those are distinct types of memory and it's very useful to neuroscience to make
*  that distinction and that really drove a lot of the progress in neuroscience in my opinion.
*  The field of timing I think has been hampered by the fact that as we were alluding to earlier,
*  timing really means different things and we need to define what we mean by time.
*  So if I talk about subjective sense of time, your ability to tell time in music, your ability
*  to tell time in speech as you were slowing down at the beginning of the program or speeding
*  up or circadian time.
*  So what we're struggling with as a field is to sort of understand how many different
*  types of timing we're all studying.
*  If it's at the sensory level, at the motor level, at the cognitive level, at the unconscious
*  level and so forth.
*  So that's what we mean.
*  That's what I mean by a taxonomy of time and I don't claim to have an answer or an
*  ideal taxonomy.
*  But you do, I mean, list some suggestions in the review.
*  But you got to start somewhere.
*  I mean, you know, it's interesting.
*  It's true that the study of time scientifically, neuroscientifically is so new still.
*  You make the point in some of your talks and in the book I believe that, you know, the
*  study of space started with Euclid who just ignored time because that is very convenient.
*  I think that is a point I think is important.
*  You know, if you think about what the first field of modern science is, I think it's
*  fair to say it's probably geometry as really formalized by Euclid around 2500 years ago.
*  And the question is why?
*  And I've made the argument that the reason is because science is a lot easier if you
*  can ignore time and that's what geometry is, right?
*  It's the study of a universe in which nothing ever changes.
*  And you know, from Euclid to the great scientists like Newton and Galileo who really started
*  bringing in time into physics and math, there was a gap of 2000 years.
*  And in neuroscience, I think it's really just beginning to fully blossom and embrace
*  the problem of the brain as a time machine or as a device that's inherently temporal.
*  Well and even the taxonomy of memory is really recent.
*  So it's a lesson to be learned I think.
*  So it's great that you're pushing to develop this taxonomy of time because it's generated
*  so much useful research, you know, so many more questions and answers.
*  So I talked a little bit about what you have done with plasticity and figuring out how
*  synaptic plasticity can implement timing in the range of 100 milliseconds or so.
*  Can you sort of at a high level description describe how that works?
*  So let's help listeners with what synaptic plasticity means.
*  Oh, you're not giving them the benefit of the doubt, okay.
*  I think that's wise.
*  In case my mom's listening.
*  So neurons of course connected by synapses.
*  These are these little structures in which allow one neuron to communicate to another.
*  And what Paul and I mean by synaptic plasticity is the fact that those connections, the ability
*  of one neuron to influence the other, is changes.
*  And that's what we refer to plasticity.
*  Some neurons can strongly influence another and that's a strong connection or a weak connection
*  in which the one neuron does not strongly influence another.
*  And we neuroscientists refer to plasticity.
*  Now plasticity can refer to long-term plasticity in which these changes take place on the level
*  of minutes and hours.
*  And the famous example is long-term potentiation and that's believed to be involved with memory.
*  Now what we're referring to here is called short-term synaptic plasticity in which the
*  weight of a synapse or the strength of a connection between two neurons changes continuously
*  on the scale of tens to hundreds of milliseconds.
*  This is a very ubiquitous synaptic property referred to as I said short-term synaptic
*  plasticity.
*  And what we had proposed is that one of the functions of this short-term synaptic plasticity
*  as opposed to long-term synaptic plasticity is to allow neurons to remember the past which
*  is another way of saying to tell time, to remember the recent past, the recent past
*  of what happened 100, 200, 300 milliseconds ago.
*  So if a synapse gets stronger over the course of 100 or 200 milliseconds that means that
*  neuron can in a sense be a bit selective to that interval.
*  So it's simply a way to inject dynamics into a system.
*  I mean ultimately we can also make the analogy with a memory.
*  So your ability to determine if a musical note is a half note or a quarter note, really
*  you're asking well what's the duration of that note which requires you to remember if
*  you will unconsciously how long ago it started except that memory only has to last 200, 500
*  seconds.
*  So we had proposed and have proposed that short-term synaptic plasticity is one way the brain can
*  do that.
*  And our experiment, our computational work suggests that that's true but it really does
*  still need to be further proven at the experimental level.
*  Well and this actually kind of leads into the idea of population clocks.
*  So you could implement population clocks through synaptic plasticity but maybe let's back up
*  and can you talk just a second about what a population clock is?
*  Okay, so this is an important concept.
*  When most of us think about clocks because they're so ubiquitous and telling time we
*  imagine something that's like an oscillator, something that's ticking like the pendulum
*  clock and having some gears and those count the oscillations of that pendulum.
*  So the gears are analog clocks are basically counting the oscillations and that counting
*  is changing with the angle of the minute hand and so forth.
*  So people might be saying okay well but how does the brain do that?
*  And the idea here is you don't need an oscillator to necessarily tell time.
*  Anything that's changing in a reproducible manner can potentially be used to tell time.
*  So now imagine a sequence of falling dominoes.
*  So if that sequence of a thousand dominoes always falls in the same way every time you
*  reset those you can use that to tell time.
*  Similarly the example I try to use in the book to describe an example of population
*  clock if you live in a big city and you look at a building at night which lights are on.
*  So at the beginning of the night maybe the upper floor lights are on or the lower floor
*  lights are on and then for some reason there's more residential areas on the top floor so
*  those lights go on after.
*  So together which lights are on give you an idea of the time of the evening.
*  And the same thing with neurons.
*  If the population of active neurons is changing in a reproducible manner we can use that to
*  tell time.
*  That's what I mean by population clock.
*  Using the changing patterns of neural activity to encode time.
*  So at time one maybe neuron 10 and 17 are active.
*  At time two maybe neuron 17 and 99 are active and so forth.
*  So that's what we mean by population clock.
*  So you've studied this a lot using recurrent neural networks.
*  And so we've talked about recurrent neural networks on the show before.
*  I've never said the phrase state dependent network.
*  Do you want to get us up to speed with what a state dependent network is and we can dive
*  in?
*  Yes.
*  So the brain is really characterized by neural circuits that are recurrent in nature.
*  That is they loop back on each other.
*  And what we mean by a state dependent network is intuitive in the sense that it's the idea
*  that any time you activate a network of neurons some neurons fire.
*  Two or three hundred milliseconds later that network will be in a different state even
*  if all the neurons have gone off because of properties, neural and synaptic properties
*  such as short term synaptic plasticity which we just discussed.
*  So the response to the network is always dependent on the current state of the network.
*  The other analogy we use is a liquid.
*  If you imagine throwing a pebble into a pond, a placid pond, that pebble will generate that
*  nice spatial temporal patterns of ripples.
*  But if you throw the same pebble in or identical pebble again briefly after it will produce
*  a totally different pattern because the second pattern will interact with the first.
*  So the response is state dependent and that state dependency allows networks to encode
*  once again time.
*  Now in a recurrent neural network you can use that dynamics which can be either relatively
*  simple or incredibly complex to encode time or to perform a computation and so forth.
*  Yeah, so I mean there has been kind of a resurgence in these recurrent neural networks being used
*  and I say that I mean you've been using them for years now and like I said we've talked
*  about them in the show but just to make the clear distinction what we normally think of
*  with deep learning networks are feed forward multilayer networks where one layer is usually
*  fully connected to the next meaning each unit in one layer connects to each unit in the
*  next layer and so on with forward progression.
*  And recurrent neural networks are wired more like the brain in that they have these recurrent
*  connections.
*  It's like this massive units sort of connected to each other so these recurrent loops form.
*  And in the past they've been really hard to train because they easily become chaotic.
*  Can you just talk about some of your work using these recurrent neural networks to tell
*  timing and sequences and how you tamed the chaos that can ensue and what it might mean
*  for how time is encoded in brain circuits?
*  Yeah that's a great summary of an important distinction between types of circuits and
*  a major distinction between deep learning machine learning and recurrent neural networks
*  which are also used in machine learning but are characteristic of the brain.
*  But as you eloquently said yeah so deep networks they're very sort of simplistic in a way in
*  that their information is flowing just from the input to the output and the brain certainly
*  doesn't work that way.
*  There's all these loops that are amplifying signals and what happens there is that this
*  feedback is the ideal recipe for chaos.
*  And that means what chaos means is simply that the system is incredibly sensitive to
*  noise so every time you do the same thing very small differences in state or noise will
*  generate different outcomes.
*  The classic example of course is in the weather in the study of meteorology a chaotic system
*  in which a butterfly beating its wing in the Amazon can alter the weather a week later
*  in New York.
*  So the field has struggled with this issue of chaos within these neural networks and
*  we and others and you've had David Sosillo on the show have come up with ways to try
*  to tame or control the chaos and what the field has struggled with is how to and this
*  is done this training when we say training just like in deep learning it's changing
*  the weights of the connections.
*  So this is quote again the synaptic plasticity but what would be considered long term synaptic
*  plasticity as opposed to short term synaptic plasticity.
*  So in the recurrent networks the challenge has been figuring out how to change the recurrent
*  connections.
*  So if you imagine a population of a hundred neurons each A is connected to B B is connected
*  to A and so forth so there's a lot of feedback within the circuit there's ways to tune those
*  connections to create these stable trajectories.
*  So what we mean by trajectories is the pattern of activity and those patterns of activity
*  can sort of become stable what I'll refer to as a dynamic attractor which is sort of
*  a amorphous term but what it just means is you can imagine a skier again going down a
*  hill and if he takes the same path because he's slowly grooving in some pathway that
*  pathway in the snow will become the tractor.
*  So it's not a fixed point attractor it's not he'll he always goes and stops at the
*  same place but he always converges back into that pathway in the snow.
*  Or he can fly off and hit a tree but yeah that's a good analogy.
*  And then it won't be a stable attractor.
*  Not stable yeah that's a good analogy though.
*  And then he so somehow the brain burns in those pathways and again the analogy here
*  is the pathway is the pattern of neural activity.
*  And they're on seven and 17 and 17 and 99 and so forth.
*  So there's ways to tune those weights and to create these stable attractors and what
*  we and others have proposed is that many of the computations the brain performs are encoded
*  not in the destination in state space but in the voyage through state space.
*  So the computation is not the arrival at the finish line if you will but the trajectory
*  taken to get to the finish line.
*  So if you think of something like how do you write your name or how do you play a song
*  on the piano the memory the information is not static it's dynamic.
*  So you need these trajectories to store information that's necessary for speech or writing or
*  walking and perhaps even thinking in most forms of cognition.
*  So the timing is inherent in that trajectory.
*  Does that overlap with the spatial abilities or is that a separate circuit in the brain?
*  I mean yeah what are your thoughts on that?
*  That's a great question and it's clear that in some times that those two things space and
*  distance if you will and time can be confounded.
*  So this is an important question.
*  If you people record from neurons in the hippocampus of mice or rats while they're on a treadmill
*  for example and they find some neurons go on at the beginning of their walk on the treadmill,
*  some in the middle, some at the end.
*  So what are those neurons encoding?
*  Are they encoding time or are they encoding distance walked?
*  And they're probably encoding both because those things are correlated.
*  So it seems clear that space and time are in the real world mostly correlated.
*  So this is something children learn very young.
*  If I'm going a long distance it's probably going to take a long time and we sort of use
*  space and time sometimes interchangeably.
*  This is something to digress a tad here in language.
*  We say it was a long day or the movie was very short.
*  So we use spatial metaphors to talk about time and sometimes we do the opposite.
*  We say well how far is your house?
*  And I might say well it's 10 minutes here from here by foot.
*  So it's clear that in many cases the neurons space and time are actually confounded.
*  So I'd be hesitant to say that these...so my point is this is a general computational
*  strategy and the brain is incredibly flexible.
*  And when the computation needs just time those neurons might be encoding time.
*  When it needs space it might just be encoding space or distance.
*  But when it's most of the time it might be very well encoding both and it might not be
*  a good idea to try to separate those things.
*  Well this is fascinating stuff.
*  There's a ton more in the review.
*  If it's okay with you let's move on and I'd like to ask you some sort of general broad
*  questions that will definitely overlap with all of these topics.
*  Of course.
*  So I was on a run the other day and I was actually listening to you on a different podcast
*  and thinking about timing and thinking about the eventual takeover of robots.
*  You know and I was imagining the processing speed of computers is such that these let's
*  say two robots could be talking essentially over each other anticipating what each other
*  is going to say and maybe that's okay.
*  But then if my personal assistant is talking over me that's not going to be cool with me
*  and they're going to misunderstand me and I'll misunderstand them.
*  And I'm wondering you know will it be important to explicitly encode time into like a general
*  AI robot creature.
*  And you know how would we do that.
*  You know it's hard for me to imagine if time is intrinsic to these computations do we actually
*  need to explicitly encode it.
*  Yeah.
*  That's a very hard question to address and you get to this issue of what's important
*  in a computation.
*  Is it ultimately the output that you've solved the task independent of how it was solved
*  or the manner in which it was solved.
*  So in a timing task AIs can encode time and process time in a totally different manner
*  from humans and that by the way happens.
*  So deep networks of course are actually pretty good at speech recognition now and speech
*  recognition of course requires some timing.
*  The pause between speech between syllables the example I already I often give although
*  AIs probably would be confused by it is something like they gave her cat food or they gave her
*  cat food.
*  So speech has many many examples in which you need to tell time.
*  So you say I screen or ice cream.
*  Now how do computers how do deep networks tell that difference.
*  So they tell time they're aware quote where if you will of the difference between or the
*  temporal delay between the different phonemes or different syllables but time is represented
*  in a very different way it's represented in space.
*  How a deep neural network tells time is by converting time into space.
*  So they have a buffer for time t for time t minus one for time t minus two time number
*  three.
*  Network is basically processing the present and the past as if it's one input in the present.
*  There's a buffer of what just happened that's being continuously fed into the network.
*  The brain doesn't work like that.
*  So any device that interacts with any other system of course is capable of telling time
*  or making decisions that are well timed or generating outputs that are well timed.
*  Now I think it is important to know that the way a computer then or most deep networks
*  solves speech is or represent time to solve speech is very different from how humans do
*  it.
*  Now there's other changes in machine learning that are changing that with recurrent neural
*  networks and things called long short term memory networks.
*  So that's one level.
*  So AIs already do that at some level but it's very different from the humans.
*  Now at this longer scale of being aware or having some sort of notion of time of the
*  past present and future this much higher level imagining planning something.
*  When you plan something you plan your trip or your jog you say well I want to bring my
*  smartphone so I can listen to this podcast.
*  So that's planning.
*  You're imagining the future.
*  Now the degree to which how AIs will achieve that or solve that problem there's many ways
*  to solve it.
*  Will they do it like humans?
*  I don't know.
*  They probably probably won't.
*  If you look at something like AlphaZero and the recent breakthroughs in chess, the AlphaZero
*  chess what I found just astounding is how future oriented many of the moves looked.
*  So some of those moves were just as Demi Hassabi said were just alien moves.
*  They were just like no human would have ever made that move but they were great moves.
*  So it's hard to look at that and say that in some sense it wasn't planning ahead or
*  quote and I'm going to use this quote here thinking of the future.
*  But obviously it's just the state of the system that's the best move.
*  So what I'm saying doesn't have to be true in any real sense but it certainly gives the
*  appearance of thinking about the future.
*  So when AIs become progressively more capable of flexible tasks and decision making little
*  by little I think the time will be represented in different ways but I suspect there's still
*  a lot to learn from how the brain tells time and I would argue that one of the things that
*  most machine learning approaches have not benefited from is learning lessons from neuroscience
*  in terms of representing time in these neural trajectories and these populations.
*  And one thing I think that one of the benefits of that is referred to what I would refer
*  to as temporal scaling.
*  The fact that as you eloquently pointed out at the beginning of the show is if you slow
*  down speech or speed speech up everybody can still understand it.
*  So that ability to slow something down or speed something up is very tricky but I think
*  that gives us some of the flexibility, some of our flexibility to appreciate music at
*  different tempos, to recognize music at different tempos, to distinguish people by their gait
*  presumably has a lot to do with the timing, the speed with which the arms and feet move
*  and so forth.
*  I think some of that will converge between AIs and neuroscience and others will be independent
*  because ultimately there will be many ways to solve similar problems.
*  I don't know, we'll have to ask the computers once they take over.
*  Well, okay, so my conscious experience is mostly of a world that's smoothly, continuously
*  flowing by.
*  So the stream of consciousness to quote William James can flow faster or slower but it seems
*  smooth.
*  But we know consciousness is discontinuous and bits and pieces build over time and appear
*  then as a whole in your subjective experience.
*  And the concept of now quote unquote can be any duration up to about 100 milliseconds or
*  so.
*  Time's not real, is it?
*  Is time just a construct of our brains that gets presented to our awareness as we subjectively
*  experience it?
*  The subjective time of the three types of time that we talked about?
*  I think so certainly our perception of subjective time is a product, a fabrication of the time
*  of the brain.
*  A wonderful fabrication, a wonderful illusion if you will in that it's created by the mind.
*  And this is a deep debate in physics.
*  Do we perceive time flowing, the past just slowly, slowly, slowly, slowly, slowly, slowly
*  debate in physics?
*  Do we perceive time flowing, the past just slowly evaporating into nothingness as it
*  opens the doors to the future?
*  Do we perceive that because it's real?
*  Meaning that that's happening in physics in the universe or because that's simply an illusion
*  in the deepest sense of the word created by the brain?
*  Now what we do know is that the perception of the now is indeed a construct that sort
*  of emerges in a very nonlinear fashion.
*  So of course we perceive things as flowing continuously and linearly and happening in
*  a clear order A, B, C, D.
*  But we know that that's not really the case and I think a good way to sort of grasp that
*  is if I say a sentence like the mouse was broken or the mouse was dead, you don't really
*  know what the mouse means until you hear the last word.
*  So it's pretty much impossible to be interpreting that sentence continuously because the meaning
*  of the word mouse can only be determined by the last word.
*  So clearly your brain is doing some backward editing in time.
*  So when you feel that you just understood that word as one continuous flow, clearly
*  that's probably not the case and there's many examples of that.
*  So this sense of the flow of time is your brain is continuously processing information
*  unconsciously and at some key points it delivers some narrative of the world, some convenient
*  narrative that's very comfort into your conscious experience and that's what we normally are
*  aware of obviously because that's consciousness.
*  But clearly the brain is continuously processing things in the background in a linear fashion
*  but waits to key points to deliver chunks of the story of the world around us into consciousness.
*  So in that sense it is an illusion and a very deep one.
*  So I think one of the deeper aspects to your question there is the interaction between
*  neuroscience and physics.
*  If what we perceive is a reflection, as I said before, of actual change of the world
*  around us or the universe as time flowing or that's something that's simply is a fabrication
*  of the human mind.
*  So many physicists and philosophers believe that the past, present and future are equally
*  real and that there's no sense of true flow of time.
*  Thus our sense of the flow of time would be an illusion.
*  On the other hand others might argue that no, time really is flowing and then the brain
*  is simply giving us a subjective experience of something that really is taking place in
*  the external world.
*  This is all confounding.
*  So actually this is, speaking of illusions, this is a pretty good time to ask you about
*  your first book.
*  So the first book that you wrote is called Brain Bugs.
*  I don't have the subtitle in front of me but tell us just a bit about what is a brain buck.
*  So here we're borrowing from the computer science, right?
*  I mean computational devices, whether that computational device is a standard von Neumann
*  architecture digital computer or that computational device is a biological neural computer, are
*  well suited for certain computations and poorly suited for others.
*  As a neuroscientist, I certainly went into neuroscience because I was fascinated by how
*  sophisticated the brain is as a computational device.
*  How is it that a neural biological computer gives me the ability to think, create, play
*  chess, understand language, to feel love and pleasure?
*  But as I grew older and grumpier, you know, I really began, you know, brains really suck
*  at many levels, right?
*  They don't do a lot of stuff good and we all have our pet peeves of what we want our
*  brain to do better but the trivial example is math, right?
*  So here you have what's the most complicated computational device in the known universe.
*  And yet we really suck at dividing 720 by 96, right?
*  Hang on, hang on, hang on. No, I'm just kidding.
*  So good luck with that. Bring up your calculator.
*  So why is that? Why is such a trivial numerical calculation so hard for the brain to do?
*  And it's because the brains in part didn't evolve to do that but it's deeper than that.
*  It's because the neural hardware in our brain is ill-suited for digital calculations.
*  So that's an example of what I would refer to as a limitation of the brain which sort
*  of figuratively I refer to brain bugs as those computations that the brain as a computational
*  device is poorly suited to do or the types of mistakes it often makes.
*  And there's many of those, right? We can't memorize long lists of numbers or random words
*  or sequences so we make a lot of errors and a lot of those errors are priming errors.
*  And if I say something like sweet and tooth and chocolate and pie and cake and then I
*  ask you if the word sugar was on that list, many people will think that the word sugar
*  was on that list because of the way the brain works, because of its architecture.
*  The computer would never make that mistake because these are fundamental computational
*  differences between how biological computer works and most digital computers work.
*  And we wouldn't really want a general AI to make that mistake either, right?
*  It's not clear. It's not clear. If it's the price to pay for flexibility then maybe you
*  would. But maybe a general AI can have the best of both worlds.
*  Maybe so.
*  And still have the flexibility and get the gist of a situation but not make those limited
*  mistakes. And the point I make in the book Brain Bugs is ultimately how our brains work.
*  The types of computations that it's inherently good at and inherently bad at have a profound
*  effect on the society in which we live. If we have societal problems, anything from
*  democracy and economics to drug use or cigarette related deaths, those societal problems are
*  a direct consequence of neuroscience, of how our brains work. And that really as a society
*  we need to pay more attention to the neuroscience because ultimately society is governed by
*  how we make decisions. And how we make decisions is fundamentally constrained by our neural
*  hardware. Yet I think most people don't think about it quite that mechanistically. And I
*  realize even most neuroscientists don't necessarily share that view. But I think it is undeniable
*  that until we have a better understanding of why we think one way or the types of mistakes
*  the brain makes, the best way to correct for those mistakes, the way we're manipulated
*  by advertising or politics, the best remedy for that is to be aware of how our own brains
*  work.
*  Do you think that in any way that's a price that we pay for creativity and generative
*  abilities?
*  I think there certainly can be a relationship between making non-optimal decisions and making
*  decisions.
*  Beautiful mistakes.
*  Beautiful mistakes and most like evolution, right? You say, well most of the mistakes
*  or the DNA mutations, the vast, vast majority of them are for the worst. But there's those
*  beautiful ones that drive evolution forward. And you might argue that there's something
*  along the same lines with neural function and that we make a lot of mistakes, but those
*  mistakes sometimes pan out and those sort of spurious responses are mostly mistake,
*  but sometimes can lead to great insights and breakthroughs. So I think that's certainly
*  a possibility. The question is again, is can we have the best of both worlds? And I think
*  with a certain degree of self-awareness, we can and recognize, okay, well that was
*  a output or that was a response that was probably generated by noise and that's not worthwhile,
*  but I recognize these other ones as potentially powerful insights.
*  Okay, we're hard pressed for time here. So I have two more questions and I think that
*  they'll be quick. Considering your knowledge of brain bugs and how we make mistakes, as
*  you've grown grumpier and grumpier, how has your thinking about time changed? I don't
*  know if you can sort of sum this up quickly because it's maybe a difficult question.
*  I think it's in part just being overwhelmed by the magnitude of the problem.
*  It's huge. That's one thing that comes across in your book and in your work is just how
*  big it is.
*  I think one thing I have changed a bit as I've become grumpier, but hopefully a bit
*  more mature is just to really recognize how fundamental time is to the brain and that
*  was the title of the book, Your Brain is a Time Machine and I mean that at multiple levels.
*  So the brain is a time machine because it's a machine that tells time. The brain is a
*  time machine because it allows us to remember the past to predict the future. The brain
*  is a time machine because it creates a subjective sense of the flow of time and finally the
*  brain is a time machine because it literally allows us to engage in mental time travel,
*  to predict and to practice what I want to do tomorrow. So in that sense the brain is
*  more literally a time machine.
*  So I think certainly my appreciation for how absolutely fundamental time is to the field
*  of neuroscience has certainly changed over time again.
*  Yeah, that's the way it works. Last question Dean, you've written two books now and that
*  takes a hell of a lot of time, I know. Do you recommend authorship?
*  Yeah I certainly recommend authorship in the sense that what it forces me to do is to do
*  a lot of reading and thinking hard about a topic and trying to practice how to read and
*  to best express that. So authorship if nothing else is a crash course in something you want
*  to learn. Now obviously academics, it's not something I think anybody should have as a
*  goal because it's going to be changed the world or be read by everybody because most
*  academic books probably don't. But I think it's something that should come out of a passion
*  to do so, a passion to learn. I think it's odd, sometimes I think people look at writing
*  a book as a way to transmit knowledge. But in a way writing a book is the best way to
*  acquire knowledge and I think it was Isaac Asimov who obviously was prolific and wrote
*  about everything who really enunciated that very clearly that any time he wanted to write
*  a book, I mean learn a new topic he would write a book on it which clearly he did and
*  maybe he over killed a bit. You're on your way, maybe you're on your way, who knows?
*  You have another one in the pipeline? Nothing loaded up yet, no.
*  Well you are at Dean Bono on Twitter, is that correct?
*  That's correct. Great and I'll link to your lab website
*  of course. So Dean in honor of spatializing time here, this has been too short for me,
*  maybe I'm sure it's been too long for you, but we can't push back the end of this episode
*  anymore. So this has been fun and thank you for your...
*  Time. Oh I was going to say knowledge, but I guess
*  we've said time enough. Thanks a lot Dean, I appreciate it.
*  Thank you Paul, it's been a pleasure.
*  As always there is so much more to talk about that we couldn't get to, but I hope that this
*  episode inspired a thought or two or three or more in you. If it did, don't let it go,
*  write it down, go figure out how to act on it, do it.
*  If you listened last week you heard me say that I would have Julie Grolier on the show
*  to talk about her spintronics neural networks. So there was a rescheduling because I'm a
*  derelict in a one man show and I messed up, but she will be here next week and it will
*  be a lot of fun. See you next time.
