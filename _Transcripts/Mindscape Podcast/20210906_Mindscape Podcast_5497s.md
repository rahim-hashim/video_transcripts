---
Date Generated: June 08, 2024
Transcription Model: whisper medium 20231117
Length: 5497s
Video Keywords: []
Video Views: 19282
Video Rating: None
Video Description: Patreon: https://www.patreon.com/seanmcarroll
Blog post with audio player, show notes, and transcript: https://www.preposterousuniverse.com/podcast/2021/09/06/163-nigel-goldenfeld-on-phase-transitions-criticality-and-biology/

Physics is extremely good at describing simple systems with relatively few moving parts. Sadly, the world is not like that; many phenomena of interest are complex, with multiple interacting parts and interesting things happening at multiple scales of length and time. One area where the techniques of physics overlap with the multi-scale property of complex systems is in the study of phase transitions, when a composite system transitions from one phase to another. Nigel Goldenfeld has made important contributions to the study of phase transitions in their own right (and mathematical techniques for dealing with them), and has also been successful at leveraging that understanding to study biological systems, from the genetic code to the tree of life.

Nigel Goldenfeld received his Ph.D. in physics from the University of Cambridge. He currently holds the Chancellor's Distinguished Professorship in Physics at UC San Diego. Until recently he was a Swanlund Endowed Chair and Center for Advanced Study Professor in Physics at the University of Illinois at Urbana-Champaign. Among his awards are the Xerox Award for research, the A. Nordsieck award for excellence in graduate teaching, and the American Physical Society’s Leo P. Kadanoff Prize. He is the co-founder of NumeriX, a company that specializes in high-performance software for the derivatives marketplace.

Mindscape Podcast playlist: https://www.youtube.com/playlist?list=PLrxfgDEc2NxY_fRExpDXr87tzRbPCaA5x
Sean Carroll channel:  @Sean Carroll  

#podcast #ideas #science #philosophy #culture
---

# Mindscape 163 | Nigel Goldenfeld on Phase Transitions, Criticality, and Biology
**Mindscape Podcast:** [September 06, 2021](https://www.youtube.com/watch?v=P_lM898S8_U)
*  Hello everyone, welcome to the Mindscape podcast. I'm your host Sean Carroll. Today we're going to have Nigel Goldenfeld on the podcast. Nigel is a leading condensed matter physicist.
*  Now we have physics all the time here on Mindscape, but we don't really do condensed matter that much. It's not my personal area and I really don't want to neglect it.
*  So why not start at the top? Nigel is an amazingly prolific and influential condensed matter physicist who works in lots of different areas.
*  But the number of ideas that are going to get discussed in this podcast and the way in which they fit together, there's a lot of ideas and they're tricky and they fit together in an interesting way.
*  So I wanted to do more of a little extended introduction here than I would usually do because the forest really matters.
*  And we're going to talk a lot about the trees. So I figured if I could sort of lay out the roadmap for the entire discussion, it will help people follow along when we actually get into it.
*  Not because Nigel is not clear. He's actually a brilliant expositor of some of these really difficult ideas.
*  But this is the kind of area where being told what you're going to be told before you're told it doesn't hurt any. Let's put it that way.
*  So here's how I think about what is going on in this conversation. Physics is great, right? Physics is very, very good at describing certain features of the world.
*  But its natural home, where it's most comfortable, most effective, is actually in quite simple systems, right?
*  The spherical cow philosophy, ignore air resistance and all that.
*  So if you have just a few particles bumping into each other, do some Feynman diagrams, or even if you have two black holes in spiraling or the universe expanding, these might be beyond our intuition or everyday experience.
*  But there's a small number of moving parts, OK? Whereas the real world of our everyday experience actually is very complex.
*  There are many, many moving parts in a biological system or a sociological or economic system or something like that.
*  And in some sense, you know, that's a shame because physics is really good at what it does.
*  And it's kind of a shame that we can't readily transport the techniques and things that we learn from doing physics into these messy, complicated systems.
*  But it turns out there are some physical systems that are in some sense pretty simple and yet show features that are closely related to those that we see in the real world.
*  So think about a fractal. Get in your mind the famous images of fractals with all these little sharp edges and so forth.
*  What makes a fractal a fractal? Well, that you can look at it at any magnification and it looks more or less the same, maybe not exactly the same, but sort of the similar statistical properties.
*  So if you zoom in on a fractal, you see just as much going on as you do if you zoom out and look at it from very, very far away.
*  Physicists or other kind of scientists call this scale free behavior at every scale over every distance that you examine the system.
*  Something is going on, often called self similar behavior or sometimes power law behavior, because if you quantify what's going on, you can show that in these self similar systems or fractal systems,
*  the amount of stuff that's going on goes as the length scale you're looking at to some exponent, to some power.
*  OK, so power law behavior, very different than a simple physical system like two particles bumping into each other or even a typical condensed matter system.
*  If you think about water, right, you can have a glass of water. If you zoom in on it, nothing's going on. It's still water.
*  There's no difference, it's true, from looking at it one scale to the other, but that's because nothing interesting is going on.
*  There's the scale of the glass and then nothing going on at the scale beneath the glass.
*  If you have a black hole, two black holes, let's say spinning into each other, if you look at it far away, it's just a dot.
*  If you look at it at the scale of the black holes, there's all these black holes. You can see two black holes spiraling into each other.
*  If you zoom in even further, you don't even see the black holes. So it's very different from scale to scale.
*  There is a characteristic scale there. However, go back to the water.
*  Water is something that, as you know, has different phases, right? You can take liquid water, you can freeze it to make ice, you can boil it to make water vapor.
*  So there are phase transitions. And when physicists study phase transitions, they often sometimes they think about water or something like that.
*  But very often they think about magnets. We'll talk right from the start in this podcast about the Ising model collection of little spins
*  that are next to each other. Well, there's a whole bunch of spins. So if you look at two spins that are next to each other, they want to align with each other because the little spins are magnets.
*  So if you have nothing but these spins, then either they'll all be pointing up and you'll get a magnet that way or they'll all be pointing down and they'll get a magnet pointing the other direction because the spins want to be aligned.
*  But if you put that in a hot room or a hot oven or something like that, if you heat up the system, give it a temperature, well, then the system, the spins start jiggling around.
*  Even though by themselves they want to be lined up, the thermal motions want to disorder them. And there turns out to be a phase transition.
*  If you heat it up high enough, who cares about the attraction between the individual spins lining them up? They're all going to be pointing in different directions at very high temperatures.
*  So there's some critical temperature at which you go from being a magnet being mostly lined up to not being a magnet at all to everything being disordered.
*  And this study of phase transitions is more deep than that. And here's why. Because if you go right to the point of the phase transition, if you go right to the temperature at the boundary of it's a magnet and it's completely disordered,
*  what you see is scale free behavior. What you see is if you looked at the spins, they would make little domains.
*  We call it a domain if all the spins are in the same pointing in the same direction in some region.
*  So there are small domains with just a few spins pointing in the same direction surrounded by other spins doing something different.
*  There are large domains where you get a whole bunch of spins even at this critical temperature, which are all lined up in the same direction.
*  And you can show mathematically that the distribution of sizes of the domains of spins at the critical temperature is scale free.
*  It looks more or less the same no matter what scale you look at the Ising model at.
*  So here's an example where physics methods that study things like phase transitions and spins and magnets can be used to quantify and rigorously understand the behavior of a system that exhibits scale free behavior.
*  Just like biological systems like the brain exhibits scale free behavior, the tree of life that you get from evolution exhibits scale free behavior.
*  Things in the economy or in politics or in social networks exhibit scale free behavior.
*  So this one example of critical phenomena, phenomena at the critical point where a phase transition happens,
*  is a way for physicists to get their hands and their quantitative way of thinking about things on things happening at different scales like the real world has.
*  And so if you're good at this, like Nigel Goldenfeld is, you study phase transitions and the mathematical tools needed to think about them,
*  like the renormalization group is something that we will talk about, and then you apply it to other areas like biology and like finance, as he has done very, very successfully.
*  So we'll talk about phase transitions and scale free behavior, and then we'll talk about biology all the way from the genetic code to the tree of life.
*  That's, of course, you know, candy for my brain.
*  This is a very mindscapie kind of thing where we can connect these ideas from different areas.
*  And Nigel Goldenfeld is a master of this kind of stuff.
*  I can't think of a better person to connect these big ideas for us.
*  So let's go.
*  Nigel Goldenfeld, welcome to the Mindscape Podcast.
*  Well, thank you. I'm happy to be here.
*  So this is one of the challenging interviews that I sometimes do with a person who is more senior and accomplished, and there's just too many things to talk about.
*  But maybe we can start more or less gently with the idea of phase transitions, because I know that people on the street, they may have heard of the idea of a phase transition, and they're thinking of water boiling or ice melting or something like that.
*  But the set of connotations that pops up in a physicist's mind when you say phase transitions is a little bit different and richer.
*  So, you know, how do you define phase transition and what are the things that you think of immediately when someone says a phrase like that?
*  Well, as a physicist, you can't talk about phase transitions without talking about Ising models.
*  And so most people think about liquids and gases and things like this, which is perfectly correct.
*  But the way that physicists always use to think about phase transitions is little spins on the lattice that either point up or point down.
*  And the thing about them is this, the spins of it represents the electronic dipole moments of atoms on a crystal, and they interact with their nearest neighbors.
*  But otherwise, there is no global coercion for them to do anything.
*  But what people like about phase transitions is that just because you're interacting with your nearest neighbor and if your neighbor is pointing up, you might feel slightly more likely to point up.
*  If your neighbor is pointing down, you might feel slightly more likely to point down.
*  But, you know, what can happen is that the tendency can, below a certain temperature, can actually propagate throughout the whole system.
*  And so everybody gets a point up or points down as a result of an interaction which is just from your nearest neighbors.
*  So it is a conspiracy. A phase transition is a conspiracy. It's a cooperative phenomenon.
*  You're not interacting with everybody in the world, but just by interacting with your neighbors, everybody ends up doing the same thing.
*  And that's what a phase transition is.
*  And physicists like to use that simple model because it's mathematically one where you can actually really understand in detail what's going on.
*  And in particular, people talk about a phase transition happening as a function of some parameter.
*  So in the Ising model, presumably it's the temperature that we're imagining changing?
*  Yes, because you can sort of understand it very qualitatively.
*  If something is at a very high temperature, that means that they sort of get excited by the temperature.
*  The more temperature you have, the more you move around and so on.
*  That's like an atom in a gas. Same thing turns out to be true for spins going up and down.
*  So the higher the temperature, they flip up and down like this.
*  And so what you'd expect is that at very high temperatures, they're all flipping up and down like crazy.
*  And so on average, there's going to be as many pointing up as pointing down.
*  But then as you take the temperature to be much lower, then the temperature really doesn't make much difference.
*  And basically, if they can lower their energy by just lining up with their neighbors, they will do that.
*  And so what you always have is this interplay between energy trying to minimize the energy by doing the same thing as your neighbors.
*  And then these sort of crazy fluctuations induced by temperature, which causes some kind of disorder.
*  And people think of that disorder using the word entropy.
*  And so the phase transition is a trade off between energy and entropy.
*  And the higher the temperature, the more the entropic effect, the lower the temperature, the more the energetic effect.
*  And so then as you dial up the temperature from a low temperature, you will eventually go from being in a state where there is order to a state with disorder.
*  And this search for order and disorder in the natural universe is something incredibly fundamental.
*  And physicists call it a phase diagram.
*  They really want to understand the first question you want to understand about matter is what is its phase diagram?
*  If you have stuff that does this, how does how does it behave overall?
*  And this is a question that relates to physical systems like electrons in a material or spins in a material.
*  It relates to phenomena like epidemic spreading.
*  It relates to phenomena in ecology and in biology.
*  So the applications are incredible.
*  Yeah. And but I think the part that makes sense, I'm imagining that I know nothing about this now.
*  Right. So I'm playing dumb. It's my job.
*  So the part that makes sense is, you know, the spins want to line up, but then you heat them up so they become disordered.
*  And there's some there's some point at which there's a transition, right.
*  The phase transition point, some temperature of which that happens.
*  So, OK, I figure out what that temperature is, either theoretically or experimentally.
*  Is that it? Am I done? Or is there still more to learn about how this actually happens?
*  Well, that's a great question. So you're leading the witness there.
*  Yeah. Because you do actually have a PhD in physics.
*  But the interesting thing is this.
*  What can happen is as you raise the temperature, you might think or let's say even lower the temperature.
*  So you're going from a very high temperature to a low temperature.
*  You're going from disordered state to an ordered state.
*  You might ask, how does that order emerge?
*  Does it emerge bang suddenly or do you just get into that order gradually?
*  And the the something like a liquid gas transition is something that occurs just suddenly.
*  You know, you go below the melting temperature.
*  In reality, you have to go a little bit below that if you want to.
*  If you don't want to wait forever.
*  But once you go there, then your stuff, your water turns into ice and it doesn't just turn into a little bit of ice.
*  It all goes into ice.
*  In other kinds of transitions, like a magnet, like a superconductor and things like this, many other things,
*  that transition occurs gradually.
*  And the reason why this is so interesting is because the way that the order emerges as you lower the temperature,
*  you might think that you could calculate how much order there is as you go below the critical temperature.
*  But it turns out to be an incredibly hard problem.
*  When you do the calculation, you get one answer and then you go and do the experiments and the answer is completely different from that.
*  So that's something that happens all the time in physics.
*  You have a model of something. It doesn't quite describe things.
*  And you say, well, what do you expect? It was just a simple model to begin with.
*  But the thing that was really shocking was that if you look at the model, the way you described the physical system,
*  and it doesn't agree with the experiment, actually, there is nothing you can think of in your description.
*  That is responsible for this discrepancy.
*  It's not like, well, you just sort of change this parameter just a little bit and then you get the third decimal place correct.
*  It's like you can't even understand in principle how this discrepancy can occur.
*  And when this was solved and it took 50 years for people to solve it,
*  it completely changed the way that scientists and physicists think about modeling nature.
*  It revolutionized not just the study of phase transitions and say material science or solid state physics.
*  It changed the way we think about elementary particle physics, cosmology, high energy physics, quantum mechanics.
*  Everything changed because we realized that there was fundamental assumptions that had gone into our thinking that made everything get turned on its head.
*  And so the person who ended up putting finishing touches to the theory that we now have today,
*  won the Nobel Prize quite rightly for this work.
*  Every year, U.S. businesses waste over $400 billion because of bad writing.
*  Bad writing causes confusion, misses the mark, or just takes too long to get to the point.
*  Whereas better, faster writing means better business, which is why your team needs WordTune for Teams.
*  Going way beyond simple spelling and grammar correction,
*  WordTune is the only AI-powered writing tool that understands meaning,
*  offering writing suggestions that help anyone achieve clear and compelling writing.
*  WordTune will improve performance on any project, from internal emails to press releases,
*  sales outreach to customer services support, and so much more.
*  And you can use WordTune anywhere you're writing online, like Google Docs, Slack, Outlook Web, and WhatsApp.
*  So now try WordTune for free at wordtune.com slash mindscape.
*  If you're looking to elevate your entire team's writing, get a discount today at wordtune.com slash mindscape.
*  WordTune improves writing efficiency up to four times, and that means better business.
*  So start writing with WordTune at wordtune.com slash mindscape.
*  I think that, you know, one of the things about the audience for mindscape is they're not experts in things,
*  but they like to hear some of the details.
*  So I think we can say out loud that the person you're talking about is Ken Wilson,
*  and the idea is the renormalization group. Is that more or less right?
*  Yeah.
*  So how do we tell our non-expert audience what the renormalization group is,
*  and how it solves this really interesting problem?
*  I mean, you're leaving us on tenterhooks here. You have this huge problem that we can't solve.
*  I can tell you in a simple way.
*  So let's suppose that I'm doing an experiment looking at some phase transition, let's say a magnetic transition.
*  I've got a piece of metal in my lab, and I'm doing an experiment to measure how the magnetization,
*  the number of spins pointing up minus the number of spins pointing down,
*  how that number changes as I go below the critical temperature.
*  And you might say, well, what could the answer depend upon?
*  And so one of the things you might say is, well, my experimental apparatus is foot in diameter, let's say,
*  and perhaps you have some reason to think, well, maybe it should also depend on the radius of the Earth.
*  So then you think, well, by dimensional analysis, the one foot divided by the radius of the Earth,
*  it's a pretty small number, I should just be able to throw that away.
*  It shouldn't matter in my theory for this.
*  And that's a sort of common sense thinking that everybody would relate to.
*  But that step turns out to be wrong.
*  That step turns out to be the thing that messes everything up.
*  In fact, it's not really the radius of the apparatus divided by the radius of the Earth.
*  It's something slightly different.
*  It's actually the range over which these spins start to communicate.
*  They start to feel cooperation divided by the lattice spacing of the spins on, say, a crystal lattice, which might be a few axons.
*  And as you get closer to that transition, the range over which the cooperative effects take place goes as large as you like.
*  It can be 100 miles, a thousand miles, a million miles if you have a big enough material.
*  And you would think that range, physicists call it the correlation length, that range is much, much bigger than the atomic spacing, which is angstroms.
*  So we can just neglect the atomic scale in making a model of this.
*  And it makes perfect sense.
*  And everything we teach our undergraduates in physics by using, say, dimensional analysis uses that argument.
*  But it's completely wrong.
*  Just because something is small doesn't mean it's negligible.
*  And in the phase transition problem, this fact that you cannot lose sight of the small scale, if you do, you cannot possibly explain the experiment.
*  You have to include that in there.
*  That fact is something I like to call scale interference.
*  Because scales that should have by no means have anything to do with what happens macroscopically, nevertheless, do show up in the critical behavior.
*  And that is a real shock.
*  And just to drum home how big a shock it is, you know, people know that the existence of atoms was only really established about 100 years or so ago.
*  In fact, it really was Einstein whose work on Brownian motion really convinced people that atoms actually exist.
*  And so the question that you might want to ask yourself is, why did it take so long to discover that matter is made out of atoms?
*  Well, the answer is you can explain pretty much everything that you see in the world around you, mechanical properties, thermal properties and so on, without having to assume the existence of atoms.
*  Everything happens in a way that looks just like some continuum.
*  Matter is just some blob of stuff.
*  And nothing seems to depend on the fact that if you really look at it very closely, it's made out of atoms.
*  All of that gets washed away.
*  So we're used to this idea that on large scales, all the microstructure all gets washed away.
*  You never have to worry about it.
*  That's how people in the 19th century were able to work out the theory of elasticity and fluid mechanics and all this kind of stuff.
*  It makes perfect sense that it should happen like this.
*  But at phase transitions, all of this goes out the window.
*  And so this was why this was such a shock to physicists.
*  OK, that's a very good way of putting it.
*  And it's interesting just because I've learned renormalization group things from the quantum field theory particle physics perspective.
*  And even though the ideas are the same, the sort of things you care about are a little bit different in condensed matter.
*  But this is it's an excellent point that we don't care how big atoms are or how far away they are if what we care about is macroscopic properties unless you're at a phase transition.
*  And so how what do we do about that?
*  I'm a little bit scared even asking the question.
*  But, you know, there are these ideas of renormalization.
*  And we I think that in many people's minds, if they hear that word at all, they're thinking of Feynman and Schwinger and Tomonaga and QED.
*  But it's really in this broader context that it's applicable to, you know, fluids and materials and everything we care about that makes up the world around us.
*  Right. So the name renormalization group is related to renormalization that Feynman and Schwinger and Tomonaga developed to try to solve a completely different problem, at least on the face of it.
*  So the problem that certainly I just mentioned it to your listeners.
*  So the problem that they were concerned with was people tried to work out properties of how quantum mechanical systems like atoms interacted with electromagnetic radiation, which we've known about since the middle of the 19th century.
*  And when people tried to do these calculations, they found that when you when you try to calculate, there is a naturally small number that comes out of the middle of the 19th century.
*  It's a dimensionless number.
*  I'm not going to explain what it is.
*  It's made up of things like the electronic charge and Planck's constant and things like that.
*  And it's a very small number.
*  It's about one, you know, one over one hundred and thirty seven, something like this.
*  So you think, well, OK, so I can do that.
*  I can't solve this problem exactly.
*  At least I can solve it in an approximation scheme that is principled and works like that.
*  And so when people tried to do that, they discovered that all their calculations blew up.
*  And the answer you got was, you know, the thing you want to calculate is something plus infinity plus infinity squared and so on and so forth.
*  And so that was the big shock.
*  Where does all this come from?
*  And then, you know, what, you know, what Feynman, Tomahawk and Schwinger did was they figured out a way to say, well, OK, it's only infinities if you if you think about it the wrong way.
*  But you assume that the mass of the electron is the actual mass of the electron that we see.
*  But suppose that mass is something different.
*  It's not the one that we see.
*  It's something else.
*  And the one we see is something that has taken into account these infinities as it were.
*  Then they came up with some mathematical mumbo jumbo that basically absorbed all these infinities into these into these unknown quantities that could not be observed.
*  And they were able to get finite results out of it.
*  And Feynman himself didn't believe this was a good strategy.
*  He spoke many times.
*  It's sort of, you know, it's some leisure demand.
*  It's a mathematical trick.
*  And, you know, why the heck this works?
*  I have no idea.
*  And so it was treated with suspicion for a very long time.
*  But the fact of the matter is that what people believed was that the only physical theory is that made any sense at all were theories where you could do this trick.
*  So called renormalizable theories.
*  OK, so now what does that have to do with phase transitions?
*  When you when you look at phase transitions and you try to also do calculations in a small parameter, the small parameter in phase transitions doesn't turn out to be some number to do electrical calculations.
*  Or charge or something like that.
*  It's typically something like a small a small number that counts how how how high you are in dimension.
*  So there's an expansion that physicists do where you expand in dimensions below four dimensions.
*  OK, turns out that that's a thing that you can do.
*  And I'm not going to go into details why.
*  So you can say, well, I live in three dimensions, but three dimensions is one less than four dimension.
*  So why don't I just think, let's suppose my dimension was actually three point nine.
*  OK, so if I if my dimension was just slightly less than four dimensions, could I do a calculation?
*  And in fact, Ken Wilson wrote a famous paper, Critique of the Novelian in the three point nine nine dimensions.
*  OK, so so you can do things like that.
*  But what you find is that you again get infinitives in in these calculations.
*  And so you have to use the same sort of mathematical tricks to get rid of them.
*  But this time you actually understand what where they come from.
*  And that's the thing that is different.
*  What's happening? And maybe it wasn't really clear when Wilson did it.
*  But, you know, many years later in the in the late 1980s and 90s, I applied the same things just to looking at regular differential equations that you learn about in high school.
*  You can get these things happening there.
*  And, you know, what do you find is the when you do these calculations, the calculation breaks down because it's fundamentally making a wrong assumption.
*  It's making the wrong assumption that the scale you don't have scale interference, that the cooperative phenomena is so large you don't have to worry about the atomic spacing.
*  And that is wrong. And the failure of that common sense assumption shows up in the mathematics as infinities in the theory.
*  And so now that you understand that, so then you can actually put that small scale back into the problem and actually see that that solves the infinities problem.
*  And so that's the connection between these things.
*  And so a couple of times now you use the word critical or criticality.
*  And I want to dig into that because it's part of the fact that at or near this phase transition, it's not just everything happens everywhere in space, for example.
*  Right. There are fluctuations and you can sort of characterize them.
*  So what do you mean by the word critical in this context?
*  Right. So so so people talk about the point where order first starts to appear.
*  So below that temperature, in the case of, say, a magnet, that temperature is called the critical temperature and all the phenomena, the epiphenomenon, if you will, that are associated with this weird scale interference.
*  All of those epiphenomenon happen in a small temperature interval around that temperature.
*  And and and the things that you see there are like a total breakdown of the usual physical assumptions.
*  And and so that's why there is a critical phenomenon.
*  Now, this only happens in the cases where you have this gradual increase in the in the order.
*  It doesn't really happen in, say, ice turning, melting and turning into liquid.
*  But physicists call that critical phenomena.
*  And the reason why it's so important is not just that it undermines it undermines the way we think about physics.
*  We have to start thinking about physics on different lengths and time scales, looking at fluctuations, looking at scale invariant phenomena and so on.
*  But it turns out that some of these effects show up in systems like biological systems or ecological systems or the brain and things like this.
*  And so people started to realize that when you look at complex systems, they also show some of the same epiphenomenon associated with critical phenomena.
*  And so this question of trying to understand critical phenomena then cause physics to leak into other disciplines and infect them with this with this sort of thing.
*  And so in neuroscience, we know now that there are neural avalanches in the brain which behave very much like critical phenomena and so on and so forth.
*  So so so so that's another reason why it became so important.
*  Well, I want to pin this down exactly because this connection between something that even though a phase transition is a little bit more rich than a small number of particles interacting with each other,
*  that the typical particle physicists might care about, it still seems pretty simple, right?
*  A bunch of spins at a temperature.
*  And yet you get these these phenomena that then are reminiscent of what happened in the brain or in evolutionary biology or something like that.
*  And that's that's something worth teasing out.
*  So you also use the phrase scale free at least once or twice.
*  And so it what does that mean?
*  And is it the same as critical?
*  I want to get not only the dictionary definitions but sort of all the connotations of these words in our brains.
*  Well, I don't know.
*  I don't know if I'd say it's the same thing because.
*  Because.
*  You would you I mean, when you when you have critical phenomena, so you so you have this lattice scale which you're forced to include in your calculations.
*  You have this large scale which is telling you about the scale over which degrees of freedom spins or creatures or whatever happens to be that you're describing neurons in the brain are cooperating.
*  And then in between, there's a wide range of scales.
*  And and when you look on in the in an intermediate range of scales, there is nothing that tells you in particular which scale you're at.
*  You wouldn't know what scale you're looking at if I showed you a picture of say spins in a magnet very close to the critical point.
*  What you would see is eventually you would see the latter spacing and that would then tell you about there's a micron.
*  There's a micron.
*  You know, you'd know what the scale is.
*  But if I didn't put the scale bar on the picture, you wouldn't know what scale you're at.
*  And so we call that scale invariance.
*  And it leads to very particular mathematical consequences.
*  So another area which I take the opportunity to talk about is fluid turbulence, where also you get fluid fluid motion.
*  It is swirly worthy stuff that swirls and swirls and whirls on all scales from the large scale like a hurricane down to very small scales like the mean free path or gases and so on.
*  Not quite that scale, but close to that.
*  And so again, there's a phenomenon where you're not essentially doing anything to tune the system to a critical temperature, but the system behaves naturally as if it is.
*  Like a critical system.
*  And so that's why the phase transition metaphor has become so powerful because we are starting to see.
*  We've seen in many systems which are not phase transitions where you see the same phenomena and people really want to understand why.
*  Right, right, right.
*  Right, so for, so we go back to the spins.
*  What you're saying is I can just repeat it in words I think I understand.
*  We're zooming in and we're imagining measuring the spins in some region of space and or the average amount of spin in some little box or something like that.
*  And the scale freeness says that if we look at a big box or a small box, a big region or small region, we see the same statistical pattern which sounds like a fractal to me right.
*  It's exactly like a fractal. Exactly like a fractal.
*  We also see similar patterns in turbulence or something like that but now that raises a huge question because for the icing model for the spins, the whole thing seemed pretty delicate right like you had to tune it to the right temperature to make this thing happen
*  whereas turbulence happens all the time it seems pretty darn robust. Is that a real puzzle or just a fake puzzle.
*  It's a fake puzzle. So the analog of tuning the temperature to the critical temperature is the analog of making the fluid as turbulent as it possibly can be.
*  And if you want to think about how you would do that, think about this. Suppose I had a very viscous fluid like honey.
*  Have you ever seen honey be turbulent? Not really.
*  No. If you made the viscosity really really small, then of course it would be really easy to just put your fingers into it and swirl it around.
*  And so as you make the viscosity going to zero of whatever fluid you're talking about, that tunes you towards the point at which you would see complete scale invariance in a turbulent fluid.
*  Okay, so there are fluids. So the fluids if they're less viscous, it's easier to get turbulence in them and sort of that limit, the limit where turbulence is easy is kind of like the critical point in the.
*  That's right. And so if the viscosity is some number that is small but not too large or not too small, you'll see turbulence over a range of scales, but not over the complete range of scales.
*  You'll be able to see where its turbulence stops above and below some scale, for example, as you go closer to, you know, more less and less viscous fluids that range of scales will in where you see turbulent behavior will increase.
*  And it's the same thing as what happens in a magnet as you get closer and closer to the critical temperature, the range of scales over which you see fractal behavior in the sort of configurations of the spins that range of scales gets larger and larger.
*  But this is only somewhat reassuring because isn't turbulence, famously the most difficult problem in classical physics, you know, how close are we to saying that we truly understand what's going on in turbulent flows?
*  Well, I think it's a great thing that it's an unsolved problem because it means that you can write grant proposals to try to solve it.
*  So, in fact, I lead and am part of a very exciting collaboration of people actually trying to understand turbulence.
*  And of course, there's many, many ways that people have tried to understand this.
*  You know, what's new from our perspective is that we're trying to understand it using the conceptual framework of statistical physics, the phase transition framework, as opposed to the more traditional fluid mechanics framework.
*  It's not that they're at odds with each other, but one way of thinking of it allows you to guess that certain phenomena might happen, even if you don't really know how to explain how to solve the equations exactly.
*  And indeed, that's what we have found.
*  For example, how does a fluid that is flowing through a pipe as you increase the speed at which the fluid flows, it should become turbulent.
*  You intuitively would understand that.
*  And when you actually do the experiments, you find that it has all sorts of really rich behavior, which is can be understood and predicted by the same sort of physics that we use in phase transitions.
*  Some things are just better from home. A home cooked meal, the ability to pause a movie whenever you want.
*  And now with Peloton, you can add working out to that list.
*  When you purchase the Peloton bike, you get access to live classes and thousands on demand, plus access to the app to get you moving anytime, anywhere.
*  With a boot camp between nap times or a ride before brunch, you can seamlessly fit Peloton into your life.
*  What I personally like about Peloton is the flexibility in the different kinds of classes you can take.
*  It's not just being on the bike. You could do cardio classes, there are strength classes, even yoga and Pilates.
*  And with epic artist collaborations and instructor curated playlists, Peloton's music experience is unlike any other.
*  With the Peloton bike, there's nothing like working out from home.
*  Learn more at onepeloton.com. New members can try Peloton classes free for 30 days at onepeloton.com slash app.
*  Terms apply. That's O-N-E-P-E-L-O-T-O-N dot com.
*  So you just said there we are flowing liquid through a pipe, which is a very real world problem, by the way.
*  I'm glad that we're doing physics, but one that really has applications beyond thinking about the multiverse or something like that, right?
*  You have fluid flowing through a pipe and you increase the velocity.
*  Is there a sense in which there is a phase transition from non turbulent to turbulent flow?
*  Yes, it's not a sense. It's an exact prediction.
*  Prediction is that it's a non equilibrium phase transition because the fluid is definitely not in equilibrium.
*  It is being pushed through the pipe as it were.
*  So it's what's called a non equilibrium phase transition in the universality class of directed percolation.
*  And I'll tell you what I mean.
*  You're going to have to elaborate a little bit on what that means.
*  I will. But so that's the prediction.
*  And that has been verified experimentally in at least one system experimentally and in another in work that we are in the process of finishing writing up in literally in pipes.
*  Now, what is directed percolation?
*  OK, here's a story.
*  So I get up in the morning. I like to make coffee.
*  So I make myself a colical filter.
*  I pour in the coffee grounds, put it under the drip and it drips through.
*  So this is what happens.
*  So you just put the coffee in and start the drip filter and you get a cup of coffee at the end.
*  And it's like petrol station coffee.
*  When you get it, it's weak and disgusting and you wouldn't want to drink it.
*  So then you say, fine, OK, throw it away.
*  Let's try it again.
*  But this time, let's push the grains of coffee much closer together because you've got the idea that if the water trickles through slowly, it will absorb some of the good stuff from the coffee grains.
*  And you'll get a better cup of coffee.
*  So you go and do that.
*  But what happens then is the water can't find its way through because the grains are packed too tightly.
*  So the water backs up and then it spills all over the counter.
*  And then everybody who's in the breakfast room at that moment starts yelling at you and and you have a nice peaceful day started rather unfortunate manner.
*  So then you think to yourself, OK, that didn't work.
*  So maybe I can just get the balance just right.
*  Get the grains packed together just enough that the fluid can still manage to get through.
*  But but it takes as long as possible to get through.
*  So it doesn't back up.
*  It manages to get through and absorbs the most possible good stuff from the coffee grains.
*  And so you can imagine that there's some packing threshold where you can manage to get that where it's not loosely packed and it's not densely packed.
*  It's just somewhere in between.
*  And that's and then the water will go through.
*  It is called percolation.
*  And and that percolation point is a second order phase transition.
*  And it behaves in the way that I've told you.
*  It turns out that it really mathematically exhibits the same phenomena as say a magnet, you know, becoming magnetic at the critical temperature.
*  But this, of course, is not an equilibrium.
*  The water is going through under gravity.
*  So it's a non-equilibrium process.
*  And it's called percolation because it's percolating through and it's called directed.
*  But generally speaking, when water goes down, it doesn't then start to come up.
*  So it is under the influence of gravity.
*  So it's called directed percolation.
*  And you can make a mathematical model of that.
*  And the mathematical model, you'd say, well, let's make a lattice.
*  Let's have sites on the lattice, which are you're not allowed to go to.
*  That means there's a grain in the way.
*  And then the fluid can go through in between them.
*  And then you can ask, as I vary how many grains there are, how many sites there are that you can't go to, how will the particles diffuse through?
*  And you can solve that.
*  And so it's a model of particles hopping on a lattice, going all the way through and trying to tune the probability of being able to hop from one site to another, which is related to how closely the grains are packed.
*  And you can solve that problem in a mathematical model.
*  So there's a description of something that has nothing to do with turbulence.
*  Right.
*  It's just coffee pouring through, water pouring through a bunch of coffee grains.
*  And yet that transition, the mathematical problems of that transition are exactly what happens when a fluid becomes turbulent.
*  And so this is one of the this is one of the astounding things that came from these insights that came from phase transition physics is that systems which are totally disconnected from each other, they seem apparently different, nevertheless have exactly the same mathematical properties.
*  And here's a great example.
*  Coffee going through a percolator, water going through a percolator and fluid becoming turbulent.
*  One is a discrete model of something hopping on a lattice.
*  One is just fluid just sloshing around.
*  And yet the two things behave mathematically exactly identical at this transition point.
*  And this is the idea, I mean, you just sort of explained in words the idea of a universality class, which is a phrase you use that these very different physical systems can obey the same equations under the right circumstances.
*  Well, it's not just different.
*  So there's two things to universality.
*  So you could say, let's take a magnet and let's suppose it's, you know, some some alloy or some some some sort of atoms in it.
*  And I take another magnet, which is made out of completely different atoms, different interactions, different magnetic, different electronic properties and so on.
*  What the first kind of universality says that regardless of what atoms it is, the phase transition happens in exactly the same way.
*  So that's universality number one.
*  Universality number two is actually, it's not it doesn't even have to be a magnet.
*  Let's suppose I take the liquid gas transition, which is literally a liquid and gas.
*  OK, that's translocation can be mathematically related at the right temperature to the magnetic transition.
*  One hand you've got a magnet, one hand you've got, you know, what's called a lattice gas atoms that are either there or not.
*  And if they're there, you know, if there's more of them there than it's dense, like a liquid, if there's only a few of them there, it's like a gas.
*  And those two systems are very different, but they can be mapped into each other.
*  And so that's the universality that you were talking about.
*  And then, of course, the example I gave, you know, turbulent fluid and the water percolating through coffee granules, obviously very different, different things.
*  I mean, here's another thing that's really interesting.
*  So this transition also happens in ecology.
*  In other words, we have predator and prey in an ecosystem.
*  There is a there is a I can explain it to more if you want to go into this direction.
*  But it turns out that depending on how voraciously the prey are eaten, so how voraciously the predators eat the prey, prey doesn't want to be voraciously eaten.
*  The predators eat the prey, you can get a coexistence where there's always predator and prey in the ecosystem, always sheep, always wolves, the population never goes to zero.
*  And there's a point where they just coexist.
*  And at that point, it's like a phase transition as well.
*  And it also is misdirected percolation transition.
*  Well, good. I think I do actually explain more about that.
*  What exactly is it about those dynamics that maps on to percolation in some interesting way?
*  Well, you would never know it just by looking at it.
*  Okay, you would just say, I have no idea.
*  You know, if you ask if you just walk down the street, you know, found a physicist and asked her, you know, what do you think this transition is going to be?
*  There's no way she would say, oh, it's going to be directed percolation in the ecosystem.
*  So you have to you have to study it with statistical physics techniques.
*  But really, what it ends up being is that you have to have what's called an absorbing state, a state that once you get into it, then you can't get out of it again.
*  And so that really is one of the key factors that turns out to tell you that you're going to be able to get out of it.
*  And so so that it really is is is one of the key factors that turns out to tell you what something is is is in such a state.
*  So, for example, in an ecosystem, if you know, if you eat all the prey, then then the predators, the prey are dead.
*  The predators have now got nothing to eat. So they die.
*  Everything dies and the ecosystem is then just dead forever.
*  So that's that's that's an example of an absorbing state.
*  In the fluid turbulence case, it turns out that if you're looking at, say, a flow in a pipe, you know, if you make the flow just be laminar and then you increase the speed at which you make the fluid flow through the pipe and you do it really, really carefully,
*  you can actually as high as you want to go in speed, if you do it really, really carefully and a very smooth pipe, there's no vibration, nothing like that.
*  The fluid will always stay laminar.
*  And then, you know, you could be, you know, have a very high velocity fluid going through the pipe and you say, how can this not be turbulent?
*  You click your fingers like that. All of a sudden, that amount of vibration is enough to cause the fluid to move.
*  It is turbulent. OK, good.
*  So there's a kind of gap, you know, mathematically it's called a subcritical transition.
*  And it's that that that gap that means that if you're in the laminar state, you can literally stay there forever in principle, unless something comes along and perturbs it.
*  So in this is I just want to get as explicitly as possible the relationships between these very different physical systems.
*  So in one, the critical point is where the flow is at a certain rate where it could stay laminar or it could become turbulent.
*  In the other, the rate at which the prey is being eaten, the rate at which the sheep are being eaten by the wolves is such that both populations stay exactly the same.
*  Is that right?
*  Yes. And it's not really unique how you do that.
*  You could say it's a characteristic speed at which the fluid flows through the pipe, given that you know the viscosity of the fluid.
*  Or you could say, never mind the speed, just vary the viscosity or, you know, or the diameter of the pipe.
*  Or in the case of the predator and prey, the birth rate of the prey, for example.
*  Think about this. I've got some wolves, they can eat at a certain rate.
*  They're eating sheep. Let's suppose the sheep are like rabbits and they reproduce every 100 years.
*  Not like rabbits, the opposite. They reproduce every 100 years.
*  And what's going to happen is the wolves are going to eat all the sheep and then they're gone.
*  Then the wolves will die and that's the end of it.
*  If on the other hand, the sheep can reproduce every one minute, of course they really can't.
*  But suppose they could, then the wolves wouldn't be able to keep up.
*  They're trying to eat deep and meanwhile the sheep are making new baby sheep and so on and so forth.
*  And so then you'd say, well then they keep up. And so there's now coexistence of the two things.
*  And so then you can ask, well what birth rate do I need? Somewhere between once a minute and once every 100 years.
*  There's going to be some critical birth rate where the sheep, you know, pretty much eat all the, all the wolves eat all of the sheep.
*  But the sheep just manage to make enough babies that the system doesn't die out completely.
*  So again, it's this balance in this particular example. That's what it would be.
*  Maybe someday in the future we'll live in a post-scarcity world.
*  And then your company can waste money on inefficient hiring if it wants to.
*  Until then, save your time and only pay for quality candidates that meet your must-have requirements by going to Indeed.
*  Indeed is the job site that makes hiring incredibly simple. Just attract, interview and hire.
*  In fact, with Indeed, you can do all of your hiring in one place, including the interviewing.
*  So don't just hope your perfect candidate will find you.
*  Indeed's hiring tools help you cut through the noise to hire faster and smarter.
*  In fact, Indeed Instant Match provides a list of quality candidates whose resumes are on Indeed the moment you post a sponsored job.
*  With Indeed, you save time and money by setting your must-have qualifications and only paying for the quality candidates that meet them.
*  So get started right now with a $75 sponsored job credit to upgrade your job post at Indeed.com slash Mindscape.
*  That's a $75 credit at Indeed.com slash Mindscape.
*  Indeed.com slash Mindscape offer valid through September 30th. Terms and conditions apply.
*  And do we expect that I honestly don't know the answer to this question, although I can guess it.
*  Do we expect that at that critical point where the rate of wolves eating sheep and sheep reproducing is just right to keep it long-term balance, is there scale-free behavior?
*  If we had a really, really big ecosystem and sort of zoomed in, is it sort of similar fluctuations?
*  Yes, it's scale-free. In fact, it's mathematically identical to what happens in high-energy hadron scattering.
*  So you may remember from grad school, you probably studied Reggie poles and Reggie on field theory.
*  Yeah. Okay. So Reggie on field theory, you can explain that better than I can, but Reggie on field theory was an attempt to understand high-energy scattering.
*  And it turns out mathematically to be the same as this process of directed percolation.
*  And it is a scale invariant, except it's an allyspropic scale invariant.
*  So you think of scale invariants as being every direction you look looks the same. In these problems, things look different in different directions.
*  So, for example, think about the water dribbling through the coffee in your percolator.
*  So obviously the vertical direction is very different from the horizontal direction.
*  And so when you get the critical phenomenon in that process, the way that you get scale invariants in the vertical direction is different from the way you get scale invariants in the horizontal direction.
*  And that's because the system is out of equilibrium. It's being driven. The water has to follow the gravity and go down.
*  But it can go sideways as much as it likes. You just can't go back up.
*  And so that process is an anisotropic. And again, that's something that's very special to these non-equilibrium phase transitions.
*  And I'm going to return to my question about the delicateness here.
*  So we see or maybe maybe the right way to ask it is when we see other scale free behavior in nature, is there what is it about it that is phrase transition II.
*  In other words, when we see critical behavior in the brain or in a hurricane or whatever, why is it approximately scale invariant rather than just having a scale that dominates everything?
*  Is there is there even though it's not tuned to some critical point, as far as I know?
*  Yeah, so that's right. So I think that's the sort of million dollar question.
*  I mean, I think people people don't really know. Is it really true that there was nothing tuned in that or, you know, it's not really understood.
*  Let me give you an example of how you can fool yourself into thinking that there was no tuning.
*  So many years ago, maybe 20 or 30 years ago, people led by Park Bak, for example, in Denmark, made models of sand piles.
*  You know, you take a take a you take some sand grains and you put them on a pile and beach and you make a sand sand pile out of it.
*  And then, of course, as the sand pile gets bigger and bigger, when you put the last grain on, what will happen is it will cause a little avalanche.
*  And and so people started to realize that if you made models of this, this process, this avalanche process in sand piles exhibited this the scale free behavior that you're talking about.
*  And so this seemed like, well, this is a really, you know, nobody tuned anything.
*  You're just putting sand grains, stacking them up, making a making a making a pyramid of the beach, you know, nothing's being tuned there.
*  So so it was sort of thought that maybe somehow the system self organizes itself and it became known as self organized criticality.
*  So then Sid Maigle, one of my colleagues at the University of Chicago, said, well, I'm going to test this experimentally.
*  So he went and got sand grains and built a nice apparatus and some really clever measurements, which is sort of what what Sid does and and what he discovered that in the real real sand piles, they're not scale invariant.
*  And what had happened was that in making the models, people had neglected the inertia of the grains.
*  And so the real the real one doesn't show that because of because of this.
*  And so by making the mathematical models, you actually had inadvertently tuned it to a critical point by saying, well, I don't need to worry about inertia.
*  So I'll just set that equal to zero. Ignoring something is the same as setting it equal to zero and setting it equal to zero is the same as tuning it.
*  So so so, you know, so we know that we can easily fool ourselves into thinking that there is a self organization that's really not there.
*  It's just an artifact of the way we've been talking about the form.
*  That makes perfect sense that in our attempts to mathematically model something, we simplify, we find ourselves at a special point due to those simplifications.
*  But then there's also the the opposite of that, where I think that in something like evolution, I think that it's somewhere in the many talks you've given on many subjects.
*  You mentioned that phylogenetic trees, the way that we trace down speciation in biological evolution, can be thought of in some sense, which maybe you'll explain as scale free, where I don't think anyone tuned it there unless we want to believe intelligent design.
*  I think that it just sort of happened. So is there scale freeness in evolution? And why is that?
*  Well, there is, but there is a there is a hidden tuning.
*  So so so so let me just explain what you're what you're talking about.
*  So you can. So the thing is this. You can.
*  Everybody knows about what a family tree is.
*  So you know your family tree is, you know, who is descended from you and who do they marry and make children and stuff like that.
*  So people make make family trees. So then you can say, well, all right, can we make a family tree?
*  But now we're talking about species rather than human human beings.
*  And we're seeing, you know, what species, you know, humans descended from and what species were they descended from and so on and so forth, you know, all the way back.
*  And try to figure out what was the evolutionary history of all life on Earth.
*  And the first person who who really answered that question, I mean, the question was posed a long time ago.
*  Even Darwin drew a picture of us on the family tree of life.
*  And my my my colleague and friend, Carl Woese, was the really the first person to come up with a way to answer this question empirically.
*  And in fact, did that and discovered how to make five different trees of all life on Earth.
*  He discovered the evolutionary history and what he he did it using a sort of molecular sequencing technique, which is the forerunner of today's genomics.
*  And what he discovered was that life is actually in three parts.
*  People knew that there were bacteria, which are little round blobby things.
*  People knew that there are eukaryotic cells like humans or plants where the cell is much more complicated internal structure.
*  Biologists would say it has a nucleus.
*  And then what he discovered was, hey, guess what?
*  There's another set of round blobby things that look just like bacteria.
*  If you don't look at them closely enough and yet they have a totally different evolutionary history.
*  And so that was this discovery of the what's called the third domain of life.
*  And then once he discovered and shown that he had totally different evolutionary history from humans and plants and things like this and bacteria,
*  you know, then people discovered, you know, other differences to do the cell wars and so on.
*  So so so now you can make these phylogenetic trees by doing genome sequencing.
*  And when you when you do that, you discover that the trees that you make where the length of the branches tells you how many mutations that have been in the DNA,
*  those trees turn out to be mathematically fractal.
*  If you draw them out, they look fractal.
*  And if you study them topologically and actually how you do that is really too involved to talk about.
*  But it's easy to talk about, roughly speaking, how many clays or branches emanate from one particular species.
*  And you can sort of count that up and and then sort of count how many in total are connected from it.
*  And the mathematical relationship between those tells you about how symmetrical the branching pattern is.
*  You know, if you have people who then make babies and then they each make two babies and make two babies or that you get a tree that bifurcates into two at each generation.
*  On the other hand, it could be that one one branch bifurcates into three.
*  One branch bifurcates, doesn't bifurcate at all.
*  And so you can get asymmetric trees.
*  And it turns out that the way the characterization of that asymmetry of the trees turns out to follow a scale invariant behavior.
*  And that's what that's all was discovered about about 10, 10 years or so ago by us and also independently and a bit earlier by another group.
*  And and what we discovered was that actually this could be an outcome of the interplay between ecology and evolution.
*  And and the idea being that that when organisms change their environment by their activity, think the usual example is beavers eating trees,
*  damming rivers, causing lakes that then get invaded by plants and fish and things like this.
*  So so the activity of an organism in its environment can literally change the evolutionary history of that entire ecosystem.
*  And so when you try to model that effect in a very in a very crude way, what do you find is that it also it can produce the scale invariant behavior.
*  So then to your question, your question was, well, what does it have to do with tuning?
*  So remember that we talked about the scale interference in the magnetic system, that there's a range over which there is a time, a spatial scale where things are correlated.
*  There's a range where the atoms sit on the lattice, which is angstroms.
*  And it's the scale interference between a very small scale in space and a very large scale in space for the correlations.
*  That scale interference, the fact that you can't neglect the smallness of the lattice is what causes the critical phenomena.
*  So in the evolution problem, it's an it's a normalization effect like that is scale interference, but it's a time rather than a space.
*  So when you think about ecosystems, you think there's a time scale which the ecosystem adjusts.
*  When you think about evolution, you think there's a time scale over which evolution occurs in millions and millions of years.
*  And you would think, well, I can neglect the time scale of beavers eating over here trees and chopping them down and causing a mess in the ecosystem and damning rivers.
*  I can ignore that time scale compared to millions of years.
*  Well, it turns out you can't.
*  And if you if you make that if you ask what happens if you don't make that common sense assumption, then you can explain the fractal behavior, the scaling laws that you see in the evolutionary history of of.
*  So it is an interesting kind of tuning in some sense.
*  I mean, the the Ising model example gives us the impression that, you know, we're an external actor and we have to carefully tune it.
*  Whereas in examples like this, I think probably both turbulence and in evolution, there's some internal dynamics that naturally takes you to that critical point.
*  Is that a fair thing to say?
*  That's right.
*  In other words, in the limit, if you just look at the evolutionary time scale as being just a little bit bigger than the ecological time scale, you will not see this scale and then behavior.
*  So just like in the fluid, if the viscosity is small but not zero, but not tending towards zero, you'll see turbulence over some range, but you won't see a full scale.
*  So the same thing is true in the in the ecological evolutionary time scales that the the time scale of evolution is so much larger than the time scale of physical processes in the environment.
*  That's the that's the hidden tuning parameter that has caused this to happen.
*  It does seem like there is a potential worry for scientists here because we see approximately scale free behavior in many different kinds of systems.
*  You already mentioned the brain.
*  There's also things like the Internet or the economy as well as evolution and turbulence.
*  And so is there a worry that if the phenomenon is too universal, it's hard to explain because almost any kind of dynamics gives rise to it.
*  I mean, how do we go backwards from what we observe about the system to why it is like that?
*  Yeah, it's a really great question.
*  And the answer is you can't.
*  So universality is a double edged sword.
*  On the one hand, it means you can explain a phenomena without having to know very much about it.
*  Mathematically, for physicists, I want to understand a phase transition.
*  I just need to understand the symmetry group and the dimension of the dimensions, spatial dimensional system.
*  And once I know those things, I can predict what the critical phenomena are going to be.
*  And as you as we've already talked about, those can be independent of what the actual system really is, you know, whether it's a magnet or it's, you know, a liquid gas transition or people in the city or something like this.
*  So you have this great universality.
*  So you have this huge explanatory power within.
*  If you want to ask, well, what's really going on at the microscopic level?
*  Why is it like that?
*  You don't really you don't really know.
*  So let me give you a concrete example of where this is.
*  This turned out to be a huge problem.
*  And that is ecology.
*  So you can ask a very simple question about an ecosystem.
*  You can ask how how how what's going to be the most abundant organism in the ecosystem and what's going to be the next most abundant and what's going to be the next next most abundant.
*  And so you can calculate, you know, measure a species abundance diagram.
*  How many species are there which have this sort of abundance?
*  How many species are there which have this sort of abundance and so on?
*  And you can pull that distribution out and you can you can measure it.
*  And the place where it's really been measured is in a place called Colorado Island, which is near Panama, where there's every tree and shrub and weed has been analyzed by by biologists and researchers.
*  And they can identify these things.
*  So we have extremely good ecological data for that for that system.
*  And so you can say, well, OK, so let me try to make a theory for how this species abundance distribution, you know, I'm going to take into account how things grow and they compete for light and the soil nutrition.
*  All these sort of things that you might imagine are really important.
*  So you can do that and you'll get some distribution.
*  Then you can say, well, I don't really care about that because you know, I don't really care about that.
*  Well, I don't really care about that because, you know, here's what I know as a statistical scientist.
*  I know that something has to be more more abundant than something else.
*  So so and then the next thing is going to be more abundant than the third thing and so on.
*  So let me ask, let's suppose that the the organisms were completely independent.
*  They never saw each other.
*  They behaved exactly the same.
*  Functional equivalence is what an ecologist would call it.
*  And so you make a theory for how things interact in an ecosystem, which is like the ideal gas theory of atoms bouncing around in the box.
*  In other words, there's no interactions.
*  They just bounce out in the box and they obey statistical laws and those statistical laws end up giving you the laws of thermodynamics and the ideal gas law that you learned in high school and things like that.
*  So you say, let's try to do that species in the ecosystem and you go ahead and you do that.
*  So that's called the neutral model of ecology.
*  And and it was really, really propagated extensively by brilliant work by Hubble and many other people, you know, about 20, 25 years ago.
*  And so now you look at what you predict from that and you look at what you predict from actually understanding the biology of the organisms.
*  And you get two distributions and they're virtually exactly the same.
*  So when I look at the Baira Colorado Island, I ask, well, was this just this curve just a statistical thing like the central limit theorem, which is, of course, the first example of universality in science that I know about?
*  Or is it does it reflect something about the actual processes by which this community was formed?
*  And there has been a huge debate in the ecological literature about this.
*  And of course, the right answer is it's a mixture of the two things.
*  Well, how how does one go backwards?
*  Well, the answer is that you can't really.
*  What it tells you is that asking for species abundance distributions is a question that is nice to know, may be useful for some things.
*  But it's not going to answer the question about process.
*  So just because you see a pattern doesn't mean you understand what is the process that gave rise to that.
*  Exactly. But OK, this this sparks another question, which you'll tell me whether or not it's related.
*  The use of the word universality in all of these examples gives a feeling of robustness for the kinds of phenomena that we're talking about.
*  So given that we're talking about life and its relationship to physics, an obvious question is how robust is life itself?
*  I mean, are you someone who thinks that we're going to find life ubiquitous in different hospitable environments in the universe?
*  Or is this something where we need to know extra information about some miraculous fluctuation that started at all?
*  No, I my prejudice is, is that life is a generic consequence of the laws of physics and that matter can self-organize out of equilibrium hierarchically into into structures that are then evolvable.
*  And it's the evolvability that, in my view, defines living systems, not that they can reproduce, not that they can metabolize things, but that they are capable of evolving into what is called open ended growth of complexity.
*  I mean, you could say, well, OK, so life started some mother of all faith transitions three point eight billion years ago.
*  OK, so now you've got self replicating RNA molecules, if you believe the RNA world, but I don't suppose you believe that.
*  So then the question is, OK, so once once you've got self replicating RNA molecules, why doesn't it just stop?
*  Why why why does it have to go and produce, you know, walruses and elephants and humans and dinosaurs?
*  OK, so that question of how the growth of complexity arises is really, I think, one of the frontier frontier questions in evolutionary biology.
*  So so, yes, I do think that life that there is an inevitability about life.
*  I don't know about robustness. I think the inevitability is the way the word I would use.
*  Well, one of the points that is often mentioned in this context is that life seemed to begin relatively quickly after the formation of the Earth.
*  But it but it didn't, as far as we know, seem to start many different times.
*  Or is that something we don't know? I would say it's something we don't know.
*  So I think the the speed at which life evolved is really an important question.
*  And it's actually one that I worked on in understanding the genetic code because, you know, the world is about four point six billion years.
*  We know from fossil evidence and genomics that really the last universal common ancestral state of life from which we are seemingly all descended was about three point eight billion years ago.
*  Maybe even earlier, but certainly three point eight. So, you know, you know, the Earth was pretty inhospitable to life for a large part of its early history.
*  But yet within less than a billion years, you essentially evolved the complexity, more or less the complexity of the modern cell.
*  And then after that, evolution didn't really do much. I mean, you made dinosaurs and humans and things like that.
*  But from the point of view of the architecture of the cell, from the point of view of the information that is transmitted and so on, you know, there wasn't really very, very significant changes from the point of view, the qualitative point of view.
*  And so that's always been an important, an important question.
*  And if you're interested, we can talk into how that paradox is resolved.
*  But, you know, I do think that there is going back to the inevitability.
*  I think the thing that you really want, I'd like your listeners to take away is that, you know, what life is, is a process by which a planet approaches equilibrium.
*  So the purpose, if you want to know, you know, what is the meaning of life? What is the purpose of life?
*  The purpose of life is to help planets approach equilibrium, because what life does is it takes chemical potential differences in the environment.
*  When a planet first forms, there's lots of metastable states. There's lots of, it's far from equilibrium.
*  There's chemical processes that will eventually, you know, cause chemical reactions to occur.
*  And what life is able to do is short circuit those reactions and basically suck up that energy difference.
*  And that energy difference, that free energy difference, as you should say it, is then what is used to power living systems.
*  And so living systems are always involved in a competition with just regular chemical processes.
*  But living systems have an advantage because they can exchange information.
*  And so they can swap information through swapping genes.
*  They can, they can, you know, by evolution, they're able to adapt to environments, change the way in which they operate in ways that purely chemical systems don't do.
*  And so living systems are the things that really exploit these environmental free energy differences and suck up every last bit of free energy.
*  And that's the purpose of life. Kind of humbling.
*  I like to quote, Michael Russell taught me that the purpose of life is to hydrogenate carbon dioxide.
*  And I think that that's just sort of a cheeky way of saying exactly the same thing you're saying. It's part of that.
*  Exactly. And just for the record, I've been heavily influenced by Michael Russell.
*  So we work together. And so, yes, this point of view is not solely my own point of view, of course, but it's one that has emerged from the community of scientists trying to understand the emergence of life.
*  Okay, but you left us hanging with a paradox that I think the paradox was why things happen really, really quickly and then slow down and nothing interesting has happened in evolution for the past four billion years.
*  So help us out. Why is that?
*  Well, it's a phase transition.
*  Oh, there you go.
*  So they should have guessed.
*  So the thing is this.
*  The way Carl Woese and Colin Fitzsiguen and I turned this question into something that is a scientifically answerable question, which is not very easy.
*  I have to add because these things are so speculative and they occurred so long ago.
*  So you would think that this isn't a scientifically well-defined question, but it turns out that it really is.
*  And the way we approached it was building off on work that looked at the structure of the genetic code.
*  So the genetic code, just to make sure everybody knows what I'm talking about here, it's not your genome.
*  If you look at the newspapers, they'll say, you know, somebody's genetic code and they just mean the sequence of nucleotide bases on somebody's genome.
*  The genetic code is the thing that tells the ribosome to machine inside your cells and it makes proteins.
*  And the way it makes proteins is it reads messenger RNA in groups of three nucleotide bases and those are called codons.
*  And each group of three then tells the ribosome, oh, you need this particular amino acid, go and grab it and stick it onto the protein that you're just making.
*  And this machine called the ribosome, that's all it does.
*  And the code, the genetic code is the thing that tells you from a space of nucleotide bases and triplets to the space of amino acids.
*  It's that map. Now, there's four nucleotide bases, they occur in triplets.
*  So there's four times four times four, which is 64 different combinations.
*  And yet there's only 20 amino acids of life.
*  And so there's a non-unique, another one to one map that goes from one space to another.
*  And that's the thing called the genetic code.
*  And so when you when you study the genetic code in detail, what you find is, of course, everybody knows that every organism on planet has the same genetic code.
*  It's not quite true. There's small variations, but it's more or less true.
*  So maybe we shouldn't say the genetic code is universal. Maybe we should just say it's canonical.
*  OK, so now you've got the genetic code. So then you ask, well, if I had to ask you, you mentioned intelligent design.
*  So let's do some intelligent design. How would I design the genetic code?
*  Well, the way I would do it is this. I'd say, well, look, this ribosome machine that goes around making proteins in your cells, you know, it's going to make lots and lots of mistakes.
*  There's all sorts of fluctuations on scales. The molecules have to move around inside the cell.
*  What happens if you can't get the one you want and stuff like this?
*  There's all sorts of bad things that can happen. And so it could very well be the case that this machine stitches together the wrong amino acids into the protein that you're supposed to make.
*  And then you get a protein that's really bad for you. And then you'll die and so on.
*  So then you might say, OK, well, suppose I had to design the genetic code in such a way that if I get the wrong amino acid,
*  I'm still going to get one that is more or less chemically like the one I should have got so that the protein has some chance of folding up in just the way it's supposed to fold up so they can do the stuff that is biologically supposed to do.
*  OK, so if you were really clever, you could sit down and design a genetic code that does that.
*  OK, or you could just wait for a million years or actually half a billion years and evolution will do it for you.
*  And so the genetic code has this structure. It is pretty much not quite, but pretty much optimal in the sense of having a structure so it will minimize the most frequent errors that you're going to get in this gene expression process.
*  And that was discovered by people like Hagenhurst in the 1990s and elaborated on by many others, including myself, over the following 10 years or so.
*  But then what we discovered was actually, you know, how does this process happen dynamically?
*  And you might say, well, it can't happen dynamically because we're all descended from one organism or one group of organisms.
*  We can't really tell. We know that from Carl Wos' work and the subsequent elaborations.
*  So there was a last universal common ancestor. Well, whatever genetic code that organism had or that group of organisms had, we must have that as well.
*  And so you would say, OK, it's an accident, but it's also a frozen accident because let's suppose that you say halfway through the course of evolution, I'm going to change the genetic code table.
*  I can put this genetic code table on the T-shirt. I'm going to just change it, swap things around, put some amino acids in a different place.
*  Well, then you'd make proteins that would be all completely wrong and the organism would be suboptimal or it would die.
*  So Francis Crick realized this in 1968. And so, you know, basically the idea is the genetic code is a frozen accident.
*  It can't evolve. It's just what it is. And that's the way it is. No point in trying to analyze it.
*  OK, so we know that that was wrong. And so how did it evolve?
*  And I'm not going to go into a huge amount of detail about this.
*  But, you know, the story is that actually what happened is since about 3.8 billion years ago, life has evolved in a tree like structure, like a family tree, just like we've been talking about for the last half an hour or so.
*  Before that, the only way you can get a unique genetic code, an optimal genetic code and a fast genetic code, meaning one that evolves fast, is if the process of evolution is not tree like.
*  So you think of, you know, you have a family tree. It's got to be a tree, right? But it's not true at the biological level.
*  And the reason is this. When you're tracking a family tree of organisms, what you're tracking actually are genes that are involved in the code for parts of the ribosome.
*  Because it's such an essential ingredient of life. And this was one of Karl Boies' brilliant insights.
*  So, you know, that's the same in organisms. So that's what you accept for small differences.
*  And that's what you use to trace the family tree.
*  So what we realized was that before 3.8 billion years ago, actually organisms could swap genes collectively, not just transmit them to their offspring, to their daughter cells, but actually transmit the genes to an organism to which they're not related.
*  Just like I'm teaching my class on renormalization group, like going back to what we talked about at the beginning of this podcast.
*  All right. Well, you know, I could tell people, go and read my book, come to my lectures. And after several months of torture, you'll know how to do these things.
*  On the other hand, wouldn't it be great if I could just sort of pop out a little loop of DNA, throw it into the audience, everybody absorbs that loop of DNA, and then bingo, they can do renormalization group calculations.
*  Well, we can't do that, obviously, but bacteria can, and they do it all the time.
*  And that process that happens today is called horizontal gene transfer.
*  Horizontal meaning to organisms they are not related to, vertical being giving genes to your own children.
*  So that's vertical, horizontal.
*  And that process is a very, very fast way for an evolving system to discover solutions to problems, to be able to evolve because it's now utilizing a network effect rather than just making copies of itself with small variations.
*  And so when you model that and work out what happens, you find it, you get hugely accelerated evolution rates.
*  You go to a unique and an optimal genetic code.
*  And there's even evidence now when you start looking at your phylogenetic trees for the molecules that are involved in the gene expression process, the so-called amino acid TMA synthetases, for example, you could see evidence of these horizontal gene transfers way back in early time.
*  And you can even see it in recent X-ray data of high resolution X-ray data showing you the structure of the ribosome, showing you that it evolved in the kind of successive series of onion layers that evolved.
*  So in the middle, you've got a thing called a peptidine transfer center, which does translation, but it does it really, really rapidly.
*  And then later on, it gets more and more accurate.
*  And this crappy translational procedure that's at the core of the ribosome is essential for its ability to evolve.
*  Because if it's a very malleable process, then it's one that can evolve over time.
*  And we worked out what kind of dynamical system would do that, and we modeled that and simulated it and so on.
*  And that's how one tries to understand this fact.
*  Well, it's another example of something that appears accidental or tuned.
*  But in fact, there's a dynamical explanation.
*  The genetic code is the thing that you would naturally evolve to under these kinds of constraints.
*  That's right. And it's more than that, because the system eventually goes from a state where you're having a lot of horizontal gene transfer to a point where it cuts off the horizontal gene transfer.
*  And the only thing that is left, at least for the core cellular machinery, is vertical evolution.
*  Because once you've got a really good ribosome, you don't want to start messing around with it.
*  And also anything you get from another organism is very unlikely to improve the thing you've got.
*  And so this process naturally self-limits.
*  So this has been fantastic.
*  Let's, to wrap up, get a little bit more meta, because we've traversed a lot of fields implicitly, right?
*  From kinest matter physics, there was some particle physics in there, you know, biology, evolutionary biology, cellular biology, complex systems.
*  Yeah, we did a really poor job of staying in that lane.
*  I know we're dead. Well, which is bad. But, you know, is it good?
*  No, it's good. It's good.
*  Exactly. So, I mean, what is the...
*  I guess my question is, how conscious is this of a choice on your part in terms of the research you do?
*  Is it that you just led to interesting problems and they end up being all over the map?
*  Or do you place value on being all over the map in some sense?
*  I place value on being all over the map in the following sense.
*  I like to work on problems that if I didn't work on them, nobody else would have done them.
*  And my theory of impact in science is that your impact is the ratio of what you can do in the numerator to what everybody else does in the denominator.
*  And what you do in the numerator is bounded above by how lucky you are, by how much funding you have, by how smart you are, you know, all sorts of things like that.
*  So, and, you know, I'm not really very smart. So I know that my numerator is bounded.
*  So I'm not going to try to make that big. But what I can do is make the denominator as small as possible.
*  And so I try to work on problems that other people aren't working on.
*  I try to look for things, you know, intellectual arbitrages where I can see something I know in one field is similar to what happens in another field.
*  One of those fields will be ahead of the other. So whatever which falls ahead, take what it knows and apply it to the other field and things like that.
*  And physicists, I'm not the first person to do this, by any means, physicists do this all the time.
*  And so that's sort of a way why these things, why my work is definitely wandered all over the map.
*  There is a similarity and a coherence to it. There are connections between these things that my students and I see.
*  And it drives us to see these and say, well, we can do this. You know, we should do that.
*  Right now I'm working on something to do with time crystals.
*  Yes, I'm not going to tell you what the analogy is because the idea is the main thing in physics, as you know.
*  But you see these connections and then once you see the connections, then it percolates through to other fields.
*  I know we didn't even get to Turing patterns or hallucinations or the visual cortex or anything like that.
*  But I will point people to your web pages and your articles.
*  I have point people to wonderful articles written by Jennifer Ouellette on exactly those topics.
*  Exactly. I should do that also. By the way, are you ever going to write a popular book? Is that an ambition?
*  Yes, it is an ambition. And it's one that I've talked with publishers about for some time, for actually about nearly 20 years.
*  And I will do it when I have a bit of time because nobody has written the trade book that describes what condensed matter physics is.
*  Nobody even knows the field exists, yet it's so fundamentally important.
*  So that's one thing. But there's also other things that I think are interesting to talk about.
*  So, yes, I definitely have ideas about that. But I don't have the time to do it right now. But I will do it.
*  We'll be waiting for it. Nigel Goldenfeld, thanks so much for being on the Mindscape podcast.
*  It's been my pleasure and thanks for your awesome questions.
*  Thank you.
