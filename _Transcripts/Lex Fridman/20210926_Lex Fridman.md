---
Date Generated: April 12, 2024
Transcription Model: whisper medium 20231117
Length: 10602s
Video Keywords: ['agi', 'ai', 'ai podcast', 'amd', 'artificial intelligence', 'artificial intelligence podcast', 'brain', 'computers', 'cpu', 'dojo', 'elecrtons', 'fiber optic', 'hippocampus', 'intel', 'jeffrey shainline', 'josephson junction', 'lattice site', 'lee smolin', 'lex ai', 'lex fridman', 'lex jre', 'lex mit', 'lex podcast', 'metaplasticity', 'mit ai', "moore's law", 'neurons', 'nist', 'optoelectronic intelligence', 'photolithography', 'physics', 'prefrontal cortex', 'processors', 'richard sutton', 'semiconductor', 'silicon', 'superconductor', 'synapses', 'titan', 'transistors', 'tsmc']
Video Views: 564333
Video Rating: None
---

# Jeffrey Shainline: Neuromorphic Computing and Optoelectronic Intelligence | Lex Fridman Podcast #225
**Lex Fridman:** [September 26, 2021](https://www.youtube.com/watch?v=EwueqdgIvq4)
*  The following is a conversation with Jeff Schoenlein, a scientist at NIST interested in optoelectronic intelligence.
*  We have a deep technical dive into computing hardware that will make Jim Keller proud.
*  I urge you to hop on to this rollercoaster ride through neuromorphic computing and superconducting electronics and hold on for dear life.
*  Jeff is a great communicator of technical information and so it was truly a pleasure to talk to him about some physics and engineering.
*  To support this podcast, please check out our sponsors in the description.
*  This is the Lex Friedman Podcast and here is my conversation with Jeff Schoenlein.
*  I got a chance to read a fascinating paper you authored called Optoelectronic Intelligence.
*  So maybe we can start by talking about this paper and start with the basic questions.
*  What is optoelectronic intelligence?
*  Yeah, so in that paper, the concept I was trying to describe is sort of an architecture for building brain inspired computing that leverages light for communication in conjunction with electronic circuits for computation.
*  In that particular paper, a lot of the work we're doing right now in our project at NIST is focused on superconducting electronics for computation.
*  I'll go into why that is, but that might make a little more sense in context if we first describe what that is in contrast to, which is semiconducting electronics.
*  So is it worth taking a couple minutes to describe semiconducting electronics?
*  It might even be worthwhile to step back and talk about electricity and circuits and how circuits work before we talk about superconductivity.
*  Right, okay.
*  How does a computer work, Jeff?
*  Well, I won't go into everything that makes a computer work, but let's talk about the basic building blocks, a transistor.
*  And even more basic than that, a semiconductor material, silicon, say.
*  So in silicon, silicon is a semiconductor.
*  And what that means is at low temperature, there are no free charges, no free electrons that can move around.
*  So when you talk about electricity, you're talking about predominantly electrons moving to establish electrical currents and they move under the influence of voltages.
*  So you apply voltages, electrons move around, those can be measured as currents, and you can represent information in that way.
*  So semiconductors are special in the sense that they are really malleable.
*  So if you have a semiconductor material, you can change the number of free electrons that can move around by putting different elements, different atoms in lattice sites.
*  So what is a lattice site?
*  Well, a semiconductor is a crystal, which means all the atoms that comprise the material are at exact locations that are perfectly periodic in space.
*  So if you start at any one atom and you go along what are called the lattice vectors, you get to another atom and another atom and another atom.
*  And for high quality devices, it's important that that is a perfect crystal with very few defects.
*  But you can intentionally replace a silicon atom with, say, a phosphorus atom, and then you can change the number of free electrons that are in a region of space that has that excess of what are called dopants.
*  So picture a device that has a left terminal and a right terminal.
*  And if you apply a voltage between those two, you can cause electrical current to flow between them.
*  Now we add a third terminal up on top there.
*  And depending on the voltage between the left and right terminal and that third voltage, you can change that current.
*  So what's commonly done in digital electronic circuits is to leave a fixed voltage from left to right and then change that voltage that's applied at what's called the gate, the gate of the transistor.
*  So what you do is you make it to where there's an excess of electrons on the left, excess of electrons on the right, and very few electrons in the middle.
*  And you do this by changing the concentration of different dopants in the lattice spatially.
*  And then when you apply a voltage to that gate, you can either cause current to flow or turn it off.
*  And so that's sort of your zero and one.
*  If you apply voltage, current can flow. That current is representing a digital one.
*  And from that, from that basic element, you can build up all the complexity of digital electronic circuits that have really had a profound influence on our society.
*  Now you're talking about electrons. Can you give a sense of what scale we're talking about when we're talking about in silicon being able to mass manufacture these kinds of gates?
*  Yeah, so scale in a number of different senses.
*  Well, at the scale of the silicon lattice, the distance between two atoms there is half a nanometer.
*  So people often like to compare these things to the width of a human hair.
*  I think it's some six orders of magnitude smaller than the width of a human hair, something on that order.
*  So remarkably small. We're talking about individual atoms here, and electrons are of that length scale when they're in that environment.
*  But there's another sense that scale matters in digital electronics. This is perhaps the more important sense, although they're related.
*  Scale refers to a number of things. It refers to the size of that transistor.
*  So for example, I said you have a left contact, a right contact, and some space between them where the gate electrode sits.
*  That's called the channel width or the channel length.
*  And what has enabled what we think of as Moore's law or the continued increased performance in silicon microelectronic circuits is the ability to make that size, that feature size, ever smaller, ever smaller at a really remarkable pace.
*  I mean, that feature size has decreased consistently every couple of years since the 1960s.
*  And that was what Moore predicted in the 1960s. He thought it would continue for at least two more decades, and it's been much longer than that.
*  And so that is why we've been able to fit ever more devices, ever more transistors, ever more computational power on essentially the same size of chip.
*  So a user sits back and does essentially nothing. You're running the same computer program, but those devices are getting smaller.
*  So they get faster. They get more energy efficient. And all of our computing performance just continues to improve.
*  And we don't have to think too hard about what we're what we're doing as, say, a software designer, something like that.
*  I absolutely don't mean to say that there's no innovation in software or the user side of things.
*  Of course, there is. But from the hardware perspective, we just have been given this gift of continued performance improvement through this scaling that is ever smaller feature sizes with very similar, say, power consumption.
*  That power consumption has not continued to scale in the most recent decades.
*  But nevertheless, we had a really good run there for a while. And now we're down to gates that are seven nanometers, which is state of the art right now.
*  Maybe Global Foundries is trying to push it even lower than that. I can't keep up with where the predictions are that it's going to end.
*  But seven nanometer, seven nanometer transistor has just just a few tens of atoms along the length of the conduction pathway.
*  So a naive semiconductor device physicists would think you can't go much further than that without some kind of revolution in the way we think about the physics of our devices.
*  Is there something to be said about the mass manufacture of these devices?
*  Right. Right. So that's another thing. So how have we been able to make those transistors smaller and smaller?
*  Well, companies like Intel, Global Foundries, they invest a lot of money in the lithography.
*  So how are these chips actually made? Well, one of the most important steps is this what's called ion implantation.
*  So you have you start with sort of a pristine silicon crystal and then using photolithography, which is a technique where you can pattern different shapes using light.
*  You can define which regions of space you're going to implant with different different species of ions that are going to change the local electrical properties right there.
*  So by using ever shorter wavelengths of light and different kinds of optical techniques and different kinds of lithographic techniques, things that go far beyond my knowledge base, you can just simply shrink that feature size down.
*  And you say you're at seven nanometers. Well, the wavelength of light that's being used is over 100 nanometers. That's already deep in the UV.
*  So how are those minute features patterned? Well, there's there's an extraordinary amount of innovation that has gone into that.
*  But nevertheless, it stayed very consistent in this ever shrinking feature size. And now the question is, can you make it smaller?
*  And even if you do, do you still continue to get performance improvements? But that's another kind of scaling where these these companies have been able to.
*  So, OK, you picture a chip that has a processor on it. Well, that chip is not made as a chip. It's made as a on a wafer and.
*  Using photolithography, you basically print the same pattern on different dyes all across the wafer, multiple layers, tens, probably probably 100 some layers in a mature foundry process.
*  And you do this on ever bigger wafers, too. That's another aspect of scaling that's occurred in the last several decades.
*  So now you have this 300 millimeter wafer. It's like as big as a pizza and it has maybe a thousand processors on it.
*  And then you dice that up using a saw. And now you can sell these things so cheap because the the manufacturing process was so streamlined.
*  I think a technology as revolutionary as silicon microelectronics has to have that kind of manufacturing scalability, which I will just emphasize, I believe, is enabled by physics.
*  It's not I mean, of course, there's human ingenuity that goes into it. But at least from my my side where I sit, it sure looks like the physics of our universe allows us to produce that.
*  And we've we've discovered how more so than we've invented it.
*  Although, of course, we have invented it. Humans have invented it. But it was it's almost as if it was there waiting for us to discover it.
*  You mean the entirety of it? Or are you specifically talking about the techniques of photolithography like the optics involved?
*  I mean, the entirety of the scaling down to the seven nanometers, you're able to have electrons not interfere with each other in such a way that you could still have gates like that's enabled to achieve that scale spatial and temporal.
*  It seems to be very special and is enabled by the physics of our world.
*  All of the things you just said. So starting with the silicon material itself, silicon is a unique semiconductor.
*  It has essentially ideal properties for making a specific kind of transistor that's extraordinarily useful.
*  So I mentioned that silicon has the well, when you make a transistor, you have this gate contact that sits on top of the conduction channel.
*  And depending on the voltage you apply there, you pull more carriers into the conduction channel or push them away so it becomes more or less conductive in order to have that work without just sucking those carriers right into that contact.
*  You need a very thin insulator. And and part of scaling has been to gradually decrease the thickness of that of that gate insulator so they can use a roughly similar voltage and still have the same current voltage characteristics.
*  So the material that's used to do that, or I should say was initially used to do that, was silicon dioxide, which just naturally grows on the silicon surface.
*  So you expose silicon to the atmosphere that we breathe. And well, if you're manufacturing, you're going to purify these gases.
*  But nevertheless, that that what's called a native oxide will grow there.
*  There are essentially no other materials on the entire periodic table that have as good of a gate insulator as as that silicon dioxide.
*  And that that has to do with nothing but the physics of the interaction between silicon and oxygen.
*  And if it wasn't that way, transistors could not they could not perform in nearly the degree of capability that they have.
*  And that that has to do with the way that the the oxide grows, the reduced density of defects there.
*  It's it's insulation, meaning essentially its energy gaps.
*  You can apply a very large voltage there without having current leak through it.
*  So that's physics right there. There are other things to silicon as a semiconductor in in an elemental sense.
*  You only need silicon atoms. A lot of other semiconductors you need to different kinds of atoms like a compound from Group 3 and a compound from Group 5.
*  That opens you up to lots of defects that can occur where one atom's not sitting quite at the lattice site.
*  It is. And it's switched with another one that degrades performance.
*  But then also on the side that you mentioned with the manufacturing.
*  We have access to light sources that can produce these very short wavelengths of light.
*  How does photolithography occur?
*  Well, you actually put this polymer on top of your wafer and you expose it to light.
*  And then you use aqueous chemical processing to dissolve away the regions that were exposed to light and leave the regions that were not.
*  And we are blessed with these polymers that have the right property where they can cause scission events where the polymer splits where a photon hits.
*  I mean, you know, maybe maybe that's not too surprising, but I don't know.
*  It all comes together to have this really complex, manufacturable ecosystem where very sophisticated technologies can be devised and it works quite well.
*  And amazingly, like you said, with a wavelength at like 100 nanometers or something like that, you're still able to achieve on this polymer precision of whatever.
*  Whatever we said, seven nanometers.
*  I think I've heard like four nanometers being talked about, something like that.
*  If we could just pause on this and we'll return to superconductivity.
*  But in this whole journey from a history perspective, what do you think is the most beautiful at the intersection of engineering and physics to you in this whole process that we talked about with silicon and photolithography?
*  Things that people were able to achieve in order to push the Moore's law forward?
*  Is it the early days?
*  The invention of the transistor itself?
*  Is it some particular cool little thing that maybe not many people know about?
*  Like, what do you think is most beautiful in this in this whole process journey?
*  The most beautiful is a little difficult to answer.
*  Let me let me try and sidestep it a little bit and just say what strikes me about looking at the history of silicon microelectronics is that.
*  So when quantum mechanics was developed, people quickly began applying it to semiconductors, and it was broadly understood that these are fascinating systems and people cared about them for their basic physics, but also their utility as devices.
*  And then the transistor was invented in the late 40s in a relatively crude experimental setup where you just crammed a metal electrode into the semiconductor.
*  And that was that was ingenious.
*  These people were able to make it work, you know, but so what I want to get to that that really strikes me is that in those early days there were a number of different semiconductors that were being considered.
*  They had different properties, different strengths, different weaknesses.
*  Most people thought germanium was the way to go.
*  It had some some nice properties related to things about how the electrons move inside the lattice.
*  But other people thought that compound semiconductors with Group 3 and Group 5 also had really, really extraordinary properties that might be conducive to to making the best devices.
*  So there were different groups exploring each of these, and that's great.
*  That's how science works.
*  You have to cast a broad net.
*  But then what I what I find striking is why why is it that silicon won?
*  Because it's not that it's not that germanium is a useless material and it's not present in technology or compound semiconductors.
*  They're both doing doing exciting and important things, slightly more niche applications, whereas silicon is the semiconductor material for microelectronics, which is the platform for digital computing, which has transformed our world.
*  Why did silicon win?
*  It's because of a remarkable assemblage of qualities that no one of them was the clear winner.
*  But it made these sort of compromises between a number of different influences.
*  It had that really excellent gate oxide that allowed it to that allowed us to make MOSFETs, these high performance transistors, so quickly and cheaply and easily without having to do a lot of materials development.
*  The band gap of silicon is actually so in a semiconductor, there's there's an important parameter, which is called the band gap, which tells you if you there, there are sort of electrons that fill up to one level in the energy diagram.
*  And then there's a gap where electrons aren't allowed to have an energy in a certain range.
*  And then there's another energy level above that.
*  And that that difference between the lower sort of filled level and the unoccupied level that tells you how much voltage you have to apply in order to induce a current flow.
*  So with germanium, that's about point seven five electron volts.
*  That means you have to apply point seven five volts to get a current moving.
*  And it turns out that if you compare that to the the thermal excitations that are induced just by the temperature of our environment, that gap's not quite big enough.
*  You start to use it to perform computations.
*  It gets a little hot and you get all these accidental carriers that are excited into the the conduction band and it causes errors in your computation.
*  Silicon's band gap is just a little higher, one point one electron volts, but you have an exponential dependence on the the number of carriers that are present that can induce those errors.
*  It decays exponentially with that voltage.
*  So just that that slight extra energy in that band gap really puts it in an ideal position to be operated in the in the conditions of our environment.
*  It's kind of fascinating that like you mentioned, errors decrease exponentially with the voltage.
*  So it's funny because the error thing comes up when you start talking about quantum computing.
*  It's kind of amazing that everything we've been talking about, the errors as we scale down, seems to be extremely low.
*  Yes. And like all of our quantum computing is based on the same thing.
*  It's extremely low. Yes.
*  And like all of our computation is based on the assumption that it's extremely low.
*  Yes. So it's not digital computation.
*  Digital. Sorry, digital computation.
*  So as opposed to our biological computation, our brain is like the assumption is stuff is going to fail all over the place and we somehow have to still be robust to that.
*  That's exactly right.
*  So this also this is going to be the most controversial part of our conversation where you're going to make some enemies.
*  So let me ask because we've been talking about physics and engineering.
*  Which group of people is smarter and more important for this?
*  Let me ask the question in a better way.
*  Some of the big innovations, some of the beautiful things that we've been talking about.
*  How much of it is physics? How much of it is engineering?
*  So, I think that is a physicist and he talks down to all the amazing engineering that we're doing in the artificial intelligence and the computer science and the robotics and all that space.
*  So we argue about this all the time.
*  So what do you think? Who gets more credit?
*  I'm genuinely not trying to just be politically correct here.
*  I don't see how you would have any of the what we consider sort of the great accomplishments of society without both.
*  You absolutely need both of those things.
*  Physics tends to play a key role earlier in the development and then engineering optimization.
*  These things take over.
*  And I mean, the invention of the transistor or actually even before that, the understanding of semiconductor physics that allowed the invention of the transistor.
*  That's all physics.
*  So if you didn't have that physics, you don't even get to get on the on the on the field.
*  But once you have understood and demonstrated that this is in principle possible, Moore's law is engineering.
*  Why we have computers more powerful than than old supercomputers in each of our phones is that's all engineering.
*  And I think I would be quite foolish to say that that's not valuable if it's not a great contribution.
*  It's a beautiful dance.
*  Would you put like silicon, the understanding of the material properties in the space of engineering?
*  Like, how does that whole process work to understand that it has all these nice properties or even the development of photolithography?
*  Is that basically would you put that in a category of engineering?
*  No, I would say that it is basic physics.
*  It is applied physics.
*  It's material science.
*  It's X-ray crystallography.
*  It's polymer chemistry.
*  It's everything.
*  I mean, chemistry even is thrown in there.
*  Absolutely. Yes.
*  Yes. Absolutely.
*  Just no biology.
*  We can get to biology.
*  Or the biology is in the humans that are engineering the system.
*  It's all integrated deeply.
*  OK, so let's return.
*  You mentioned this word superconductivity.
*  So what does that have to do with what we're talking about?
*  Right. OK.
*  So in a semiconductor, as I tried to describe a second ago, you can sort of induce currents by applying voltages.
*  And those have sort of typical properties that you would expect from some kind of a conductor.
*  Those electrons, they don't just flow perfectly without dissipation.
*  If an electron collides with an imperfection in the lattice or another electron, it's going to slow down.
*  It's going to lose its momentum.
*  So you have to keep applying that voltage in order to keep the current flowing.
*  In a superconductor, something different happens.
*  If you get a current to start flowing, it will continue to flow indefinitely.
*  There's no dissipation.
*  So that's crazy.
*  How does that happen?
*  Well, it happens at low temperature.
*  And this is crucial.
*  It has to be a quite low temperature.
*  And what I'm talking about there, for essentially all of our conversation,
*  I'm going to be talking about conventional superconductors, sometimes called low Tc superconductors, low critical temperature superconductors.
*  And so those materials have to be at a temperature around, say around 4 Kelvin.
*  I mean, their critical temperature might be 10 Kelvin, something like that.
*  But you want to operate them at around 4 Kelvin, 4 degrees above absolute zero.
*  And what happens at that temperature, at very low temperatures in certain materials, is that the noise of atoms moving around,
*  the lattice vibrating, electrons cladding with each other, that becomes sufficiently low that the electrons can settle into this very special state.
*  It's sometimes referred to as a macroscopic quantum state, because if I had a piece of superconducting material here,
*  let's say niobium is a very typical superconductor, if I had a block of niobium here and we cooled it below its critical temperature,
*  all of the electrons in that superconducting state would be in one coherent quantum state.
*  The wave function of that state is described in terms of all of the particles simultaneously.
*  But it extends across macroscopic dimensions, the size of whatever block of that material I have sitting here.
*  And the way this occurs is that, let's try to be a little bit light on the technical details,
*  but essentially the electrons coordinate with each other.
*  They are able to, in this macroscopic quantum state, they're able to sort of, one can quickly take the place of the other.
*  You can't tell electrons apart, they're what's known as identical particles.
*  So if this electron runs into a defect that would otherwise cause it to scatter,
*  it can just sort of almost miraculously avoid that defect, because it's not really in that location,
*  it's part of a macroscopic quantum state and the entire quantum state was not scattered by that defect.
*  So you can get a current that flows without dissipation, and that's called a supercurrent.
*  That's sort of just very much scratching the surface of superconductivity.
*  There's very deep and rich physics there, which is probably not the main subject we need to go into right now.
*  But it turns out that when you have this material, you can do usual things like make wires out of it,
*  so you can get current to flow in a straight line on a chip,
*  but you can also make other devices that perform different kinds of operations.
*  Some of them are kind of logic operations like you'd get in a transistor.
*  The most common or the most, I would say, diverse in its utility component is a Josephson junction.
*  It's not analogous to a transistor in the sense that if you apply a voltage here,
*  it changes how much current flows from left to right,
*  but it is analogous in sort of a sense of it's the go-to component that a circuit engineer is going to use to start to build up more complexity.
*  So these junctions serve as gates?
*  They can serve as gates.
*  So I'm not sure how concerned to be with semantics,
*  but let me just briefly say what a Josephson junction is and we can talk about different ways that they can be used.
*  Basically, if you have a superconducting wire and then a small gap of a different material that's not superconducting,
*  an insulator or normal metal, and then another superconducting wire on the other side, that's a Josephson junction.
*  So it's sometimes referred to as a superconducting weak link.
*  So you have this superconducting state on one side and on the other side,
*  and the superconducting wave function actually tunnels across that gap.
*  And when you create such a physical entity, it has very unusual current voltage characteristics.
*  Within that gap? Like weird stuff happens?
*  Through the entire circuit.
*  So you can imagine, suppose you had a loop setup that had one of those weak links in the loop.
*  Current would flow in that loop, independent, even if you hadn't applied a voltage to it, and that's called the Josephson effect.
*  So the fact that there's this phase difference in the quantum wave function from one side of the tunneling barrier to the other induces current to flow.
*  So how does he change state?
*  Right, exactly. So how do you change state?
*  Now picture if I have a current bias coming down this line of my circuit and there's a Josephson junction right in the middle of it.
*  And now I make another wire that goes around the Josephson junction.
*  So I have a loop here, a superconducting loop.
*  I can add current to that loop by exceeding the critical current of that Josephson junction.
*  So like any superconducting material, it can carry this supercurrent that I've described,
*  this current that can propagate without dissipation up to a certain level.
*  And if you try and pass more current than that through the material, it's going to become a resistive material, a normal material.
*  So in the Josephson junction, the same thing happens.
*  I can bias it above its critical current, and then what it's going to do, it's going to add a quantized amount of current into that loop.
*  And what I mean by quantized is it's going to come in discrete packets with a well-defined value of current.
*  So in the vernacular of some people working in this community, you would say you pop a fluxon into the loop.
*  So a fluxon.
*  You pop a fluxon into the loop.
*  Yeah.
*  Sounds like skateboarder talk. I love it.
*  Sorry, go ahead.
*  A fluxon is one of these quantized amounts of current that you can add to a loop.
*  And this is a cartoon picture, but I think it's sufficient for our purposes.
*  So which, maybe it's useful to say, what is the speed at which these discrete packets of current travel?
*  Because we'll be talking about light a little bit.
*  It seems like the speed is important.
*  The speed is important. That's an excellent question.
*  Sometimes I wonder how you became so astute.
*  Matrix 4 is coming out, so maybe that's related. I'm not sure.
*  I'm dressed for the job. I was trying to become an extra on Matrix 4. It didn't work out.
*  Anyway, so what's the speed of these packets?
*  You'll have to find another gig.
*  I know. I'm sorry.
*  So the speed of the pack is actually these fluxons, these sort of pulses of current that are generated by Joseph's injunctions,
*  they can actually propagate very close to the speed of light, maybe something like a third of the speed of light.
*  That's quite fast.
*  So one of the reasons why Joseph's injunctions are appealing is because their signals can propagate quite fast,
*  and they can also switch very fast.
*  What I mean by switch is perform that operation that I described where you add current to the loop.
*  That can happen within a few tens of picoseconds, so you can get devices that operate in the hundreds of gigahertz range.
*  And by comparison, most processors in our conventional computers operate closer to the one gigahertz range.
*  Maybe three gigahertz seems to be kind of where those speeds have leveled out.
*  The gamers listening to this are getting really excited that overclock their system to like, what is it, like four gigahertz or something?
*  A hundred sounds incredible.
*  Can I just, as a tiny tangent, is the physics of this understood well how to do this stably?
*  Oh, yes. The physics is understood well. The physics of Joseph's injunctions is understood well.
*  The technology is understood quite well, too.
*  The reasons why it hasn't displaced silicon microelectronics in conventional digital computing, I think, are more related to what I was alluding to before about the myriad practical, almost mundane aspects of silicon that make it so useful.
*  You can make a transistor ever smaller and smaller, and it will still perform its digital function quite well.
*  The same is not true of a Joseph's injunction.
*  You really, they don't, they just, it's not the same thing that there's this feature that you can keep making smaller and smaller and it'll keep performing the same operations.
*  This loop I described, any Joseph's in circuit, well, I want to be careful I shouldn't say any Joseph's in circuit, but many Joseph's in circuits, the way they process information or the way they perform whatever function it is they're trying to do, maybe it's sensing a weak magnetic field,
*  it depends on an interplay between the junction and that loop, and you can't make that loop much smaller.
*  And it's not for practical reasons that have to do with lithography.
*  It's for fundamental physical reasons about the way the magnetic field interacts with that superconducting material.
*  There are physical limits that no matter how good our technology got, those circuits would, I think, would never be able to be scaled down to the densities that silicon microelectronics can.
*  I don't know if we mentioned, is there something interesting about the various superconducting materials involved, or is it all?
*  There's a lot of stuff that's interesting.
*  And it's not silicon?
*  It's not silicon, no.
*  So, like, it's some materials that also require it to be super cold, 4K and so on.
*  Yes, yes, yes.
*  So let's dissect a couple of those different things.
*  The super cold part, let me just mention for your gamers out there that are trying to clock it at 4 GHz and would love to go to 400.
*  What kind of cooling system can it achieve for 4K?
*  Exactly. For 4K, you need liquid helium.
*  And so liquid helium is expensive, it's inconvenient, you need a cryostat that sits there,
*  and the energy consumption of that cryostat is impracticable for, it's not going in your cell phone.
*  So you can picture holding your cell phone like this and then something the size of a keg of beer or something on your back to cool it.
*  Like, that makes no sense.
*  So if you're trying to make this in consumer devices, electronics that are ubiquitous across society, superconductors are not in the race for that.
*  For now. But you're saying, so just to frame the conversation, maybe the thing we're focused on is computing systems that serve as servers, like large systems.
*  Yes, large systems. So then you can contrast what's going on in your cell phone with what's going on at one of the supercomputers.
*  Colleague Katie Schumann invited us out to Oak Ridge a few years ago, so we got to see Titan and that was when they were building Summit.
*  So these are some high performance supercomputers out in Tennessee, and those are filling entire rooms the size of warehouses.
*  So once you're at that level, okay, there you're already putting a lot of power into cooling.
*  You need cooling is part of your engineering task that you have to deal with.
*  So there it's not entirely obvious that cooling to 4 Kelvin is out of the question.
*  It has not happened yet, and I can speak to why that is in the digital domain if you're interested.
*  I think it's not going to happen. I don't think I don't think superconductors are going to replace semiconductors for digital computation.
*  There are a lot of reasons for that, but I think ultimately what it comes down to is all things considered cooling errors, scaling down to feature sizes, all that stuff.
*  Semiconductors work better at the system level.
*  Is there some aspect of just curious about the historical momentum of this?
*  Is there some power to the momentum of an industry that's mass manufacturing using a certain material?
*  Is this like a Titanic shifting? Like, what's your sense when a good idea comes along?
*  How good does that idea need to be for the Titanic to start shifting?
*  That's a that's an excellent question. That's an excellent way to frame it.
*  And, you know, I don't know the answer to that, but what I think is OK, so the history of the superconducting logic goes back to the 70s.
*  IBM made a big push to do superconducting digital computing in the 70s, and they made some choices about their devices and their architectures and things that in hindsight were kind of doomed to fail.
*  And I don't mean any disrespect for the people that did it. It was hard to see at the time.
*  But then another generation of superconducting logic was introduced.
*  I want to say the 90s, someone named Lykarev and Seminov.
*  They proposed an entire family of circuits based on Josephson junctions that are doing digital computing based on logic gates and or not these kinds of things.
*  And they showed how it could go hundreds of times faster than silicon microelectronics.
*  And it was it's extremely exciting. I wasn't working in the field at that time.
*  But later when I went back and read the literature, I was just like, wow, this is this is so awesome.
*  And so you might think, well, the reason why it didn't display silicon is because silicon already had so much momentum at that time.
*  But that was the 90s. Silicon kept that momentum because it had the simple way to keep getting better.
*  You just make features smaller and smaller. So, you know, it would have to be I don't think you would have to be that much better than silicon to displace it.
*  But the problem is, it's just not better than silicon.
*  It might be better than silicon in one metric speed of a switching operation or power consumption of a switching operation.
*  But building a digital computer is a lot more than just that elemental operation.
*  It's everything that goes into it, including the manufacturing, including the packaging, including the the various materials aspects of things.
*  So the reason why and even in even in some of those early papers, I can't remember which one it was.
*  Lykarev said something along the lines of you can see how we could build an entire family of digital electronic circuits based on these components.
*  They could go 100 or more times faster than semiconductor logic gates.
*  But I don't think that's the right way to use superconducting electronic circuits.
*  He didn't say what the right way was, but he basically said digital logic trying to steal the show from silicon is probably not what these circuits are most suited to accomplish.
*  So if we can just linger on use the word computation when you talk about computation, how do you think about it?
*  Do you think purely on just the get the switching or do you think something a little bit larger scale a circuit taken together performing the basic arithmetic operations that are then required to do the kind of computation that makes up a computer?
*  Because when we talk about the speed of computation, is it boiled down to the basic switching or is there some bigger picture that you're thinking about?
*  Well, all right. So maybe we should disambiguate. There are a variety of different kinds of computation.
*  I don't pretend to be an expert in the theory of computation or anything like that.
*  I guess it's important to differentiate though between digital logic, which represents information as a series of bits, binary digits, which you can think of them as zeros and ones or whatever.
*  Usually they correspond to a physical system that has two very well separated states and then other kinds of computation like we'll get into more the way your brain works, which it is, I think, indisputably processing information.
*  But where the computation begins and ends is not anywhere near as well defined.
*  It doesn't depend on these two levels. Here's a zero. Here's a one.
*  There's a lot of gray area that's usually referred to as analog computing.
*  Also in conventional digital computers or digital computers in general, you have a concept of what's called arithmetic depth, which is jargon that basically means how many sequential operations are performed to turn an input into an output.
*  And those kinds of computations in digital systems are highly serial, meaning that data streams, they don't branch off too far to the side.
*  You do. You have to pull some information over there and access memory from here and stuff like that.
*  But by and large, the computation proceeds in a serial manner. It's not that way in the brain. In the brain, you're always drawing information from different places.
*  It's much more network based computing. Neurons don't wait for their turn. They fire when they're ready to fire.
*  And so it's asynchronous. So one of the other things about a digital system is you're performing these operations on a clock.
*  And that's a crucial aspect of it. Get rid of a clock in a digital system. Nothing makes sense anymore.
*  The brain has no clock. It builds its own time scales based on its internal activity.
*  So you can think of the brain as kind of like this network computation where it's actually really trivial, simple computers, just a huge number of them, and they're networked.
*  I would say it is complex, sophisticated little processors. And there's a huge number of them. Neurons are not simple.
*  No offense. I don't mean to offend you. They're very complicated and beautiful. And yeah, but we often oversimplify them.
*  And yes, there's computation happening within a neuron.
*  Right. So I would say to think of a transistor as the building block of a digital computer is accurate.
*  You use a few transistors to make your logic gates. You build up processors from logic gates and things like that.
*  So you can think of a transistor as a fundamental building block. Or you can think of, as we get into more highly parallelized architectures, you can think of a processor as a fundamental building block.
*  To make the analogy to the neuro side of things, a neuron is not a transistor. A neuron is a processor.
*  It has synapses. Even synapses are not transistors, but they are lower on the information processing hierarchy in a sense.
*  They do a bulk of the computation. But neurons are entire processors in and of themselves that can take in many different kinds of inputs on many different spatial and temporal scales.
*  And produce many different kinds of outputs so that they can perform different computations in different contexts.
*  So this is where enters this distinction between computation and communication.
*  So you can think of neurons performing computation and the inter networking, the interconnectivity of neurons is communication between neurons.
*  And you see this with very large server systems. I mentioned offline, we're talking to Jim Keller, whose dream is to build giant computers that, you know, the bottleneck there is often the communication between the different pieces of computing.
*  So in this paper that we mentioned, Optoelectronic Intelligence, you say electrons excel at computation while light is excellent for communication.
*  Maybe you can linger and say in this context, what do you mean by computation and communication? What are electrons? What is light? And why do they excel at those two tasks?
*  Yeah, just to first speak to computation versus communication. I would say computation is essentially taking in some information, performing operations on that information and producing new, hopefully more useful information.
*  So for example, imagine you have a picture in front of you and there is a key in it and that's what you're looking for, for whatever reason. You want to find the key. We all want to find the key.
*  So the input is that entire picture and the output might be the coordinates where the key is. So you've reduced the total amount of information you have, but you found the useful information for you in that present moment. That's the useful information.
*  And you think about this computation as the controlled, synchronous, sequential?
*  Not necessarily. It could be. That could be how your system is performing the computation or it could be asynchronous. There are lots of ways to find the key. It depends on the nature of the data.
*  The nature of the data depends on... That's a very simplified example, a picture with a key in it. What about if you're in the world and you're trying to decide the best way to live your life?
*  It might be interactive. There might be some recurrence or some weird asynchrony. I got it. But there's an input and there's an output and you do some stuff in the middle that actually goes from the input to the output.
*  You've taken in information and output different information, hopefully reducing the total amount of information and extracting what's useful. Communication is then getting that information from the location in which it's stored because information is physical as Landauer emphasized.
*  It is in one place and you need to get that information to another place so that something else can use it for whatever computation it's working on. Maybe it's part of the same network and you're all trying to solve the same problem, but neuron A over here just deduced something based on its inputs.
*  It's now sending that information across the network to another location. That would be the act of communication.
*  Can you linger on Landauer and say information is physical?
*  It's Ralph Landauer, not to be confused with Lev Landau. He made huge contributions to our understanding of the reversibility of information and this concept that energy has to be dissipated in computing when the computation is irreversible.
*  But if you can manage to make it reversible, then you don't need to expend energy. But if you do expend energy to perform a computation, there's sort of a minimal amount that you have to do and it's KT log 2.
*  And it's all somehow related to the second law of thermodynamics and that the universe is an information process and then we're living in a simulation.
*  Okay, sorry for that tangent. So that's defining the distinction between computation and communication.
*  Let me say one more thing just to clarify. Communication ideally does not change the information. It moves it from one place to another, but it is preserved.
*  Got it. Okay. All right. That's beautiful. So then the electron versus light distinction and why are electrons good at computation and light good at communication?
*  Yes, this is a there's a lot that goes into it, I guess. But just try to speak to the simplest part of it. Electrons interact strongly with one another.
*  They're charged particles. So if I pile a bunch of them over here, they're feeling a certain amount of force and they want to they want to move somewhere else. They're strongly interactive.
*  You can also get them to sit still. You can an electron has a mass so you can you can cause it to be spatially localized.
*  So for computation, that's useful because now I can make these little devices that put a bunch of electrons over here and then I change the state of a gate like I've been describing, put a different voltage on this gate.
*  And now I move the electrons over here. Now they're sitting somewhere else. I have a physical mechanism with which I can represent information.
*  It's spatially localized and have knobs that I can adjust to change where those electrons are, what they're doing. Light by contrast, photons of light, which are the discrete packets of energy that were identified by Einstein, they do not interact with each other, especially at low light levels.
*  If you're in a medium and you have a high, a bright high light level, you can get them to interact with each other through the interaction with that medium that they're in.
*  But that's that's a little bit more exotic. And for the purposes of this conversation, we can assume that photons don't interact with each other.
*  So if you have a bunch of them all propagating in the same direction, they don't interfere with each other.
*  If I want to send, if I have a communication channel and I put one more photon on it, it doesn't screw up with those other. It doesn't change what those other ones were doing at all.
*  So that's really useful for communication because that means you can sort of allow a lot of these photons to flow without disruption of each other.
*  And they can they can branch really easily and things like that. But it's not good for computation because it's very hard for this packet of light to change what this packet of light is doing.
*  They pass right through each other. So in computation, you want to change information. And if photons don't interact with each other, it's difficult to get them to change the information represented by the others.
*  So that's the fundamental difference. Is there also something about the way they travel through different materials or is that just a particular engineering?
*  No, it's not. That's deep physics, I think. So this gets back to electrons interact with each other and photons don't.
*  So say say I'm trying to get a packet of information from me to you and we have a wire going between us in order for me to send electrons across that wire.
*  I first have to raise the voltage on my end of the wire, and that means putting a bunch of charges on it.
*  And then that that charge packet has to propagate along the wire and it has to get all the way over to you.
*  There's that wire is going to have something that's called capacitance, which basically tells you how much charge you need to put on the wire in order to raise the voltage on it.
*  And the capacitance is going to be proportional to the length of the wire.
*  So the longer the length of the wire is, the more charge I have to put on it.
*  And the energy required to charge up that line and move those electrons to you is also proportional to the capacitance and goes as the voltage squared.
*  So you get this huge penalty if you if you want to send electrons across a wire over appreciable distances.
*  So distance is an important thing here when you're doing communication.
*  Distance is an important thing. So is the number of connections I'm trying to make me to you.
*  OK, one, that's not so bad. If I want to now send it to ten thousand other friends, then then all of those wires are adding tons of extra capacitance.
*  Now, not only does it take forever to put the charge on that wire and raise the voltage on all those lines, but it takes a ton of power.
*  And the number ten thousand is not randomly chosen.
*  That's roughly how many connections each neuron in your brain makes.
*  So it a neuron in your brain needs to send ten thousand messages every time it has something to say.
*  You can't do that if you're trying to drive electrons from here to ten thousand different places.
*  The brain does it in a slightly different way, which we can discuss.
*  How can light achieve the ten thousand connections? And why is it?
*  In terms of like the energy use required to use light for the communication of the ten thousand.
*  Right, right. So now instead of trying to send electrons for me to you, I'm trying to send photons.
*  So I can make what's called a wave guide, which is just a simple piece of material.
*  It could be glass like an optical fiber or silicon on a chip.
*  And I just have to I just have to inject photons into that wave guide and independent of how long it is,
*  independent of how many different connections I'm making, it doesn't change the the voltage or anything like that that I have to raise up on the on the wire.
*  So if I have one more connection, if I add additional connections, I need to add more light to the wave guide because those photons need to split and go to different paths.
*  That makes sense. But I don't have a capacitive penalty.
*  Sometimes these are called wiring parasitics. There are no parasitics associated with light in that same sense.
*  So, well, just this might be a dumb question, but how do I catch a photon on the other end?
*  What is it material? Is it with the polymer stuff you were talking about for the for a different application for photolithography?
*  Like, how do you catch a photon? There's a lot of ways to catch a photon.
*  Catch a photon is not a dumb question. It's a it's a deep and important question that basically defines a lot of the work that goes on in our group at NIST.
*  One of my group leaders, Sayounam, has built his career around these superconducting single photon detectors.
*  So if you're going to try to sort of reach a lower limit and detect just one particle of light,
*  superconductors come back into our conversation and just picture a simple device where you have current flowing through a superconducting wire and a loop again or no?
*  Let's say yes, you have a loop. So you have a superconducting wire that goes straight down like this.
*  And on your loop branch, you have a little ammeter, something that measures current. There's a resistor up there to go with me here.
*  So your current biasing this so there's current flowing through that superconducting branch.
*  Since there's a resistor over here, all the current goes through the superconducting branch.
*  Now a photon comes in, strikes that superconductor. We talked about this superconducting macroscopic quantum state.
*  That's going to be destroyed by the energy of that photon. So now that branch of the circuit is resistive, too.
*  And you've properly designed your circuit so that the resistance on that superconducting branch is much greater than the other resistance.
*  Now all of your current is going to go that way. Your ammeter says, oh, I just got a pulse of current.
*  That must mean I detected a photon. Then where you broke that superconductivity in a matter of a few nanoseconds, it cools back off, dissipates that energy, and the current flows back through that superconducting branch.
*  This is a very powerful superconducting device that allows us to understand quantum states of light.
*  I didn't realize a loop like that could be sensitive to a single photon.
*  I mean, that seems strange to me.
*  Because, I mean, so what happens when you just barrage it with photons?
*  If you put a bunch of photons in there, essentially the same thing happens. You just drive it into the normal state. It becomes resistive.
*  And it's not particularly interesting.
*  So you have to be careful how many photons you send. Like, you have to be very precise with your communication.
*  Well, it depends. So I would say that that's actually in the application that we're trying to use these detectors for.
*  That's a feature, because what we want is for if a neuron sends one photon to a synaptic connection and one of these superconducting detectors is sitting there, you get this pulse of current.
*  And that synapse says, event, then I'm going to do what I do when there's a synapse event. I'm going to perform computations, that kind of thing.
*  But if accidentally you send two there or three or five, it does the exact same thing.
*  Got it.
*  And so this is how in the system that we're devising here, communication is entirely binary.
*  And that's what I tried to emphasize a second ago. Communication should not change the information.
*  You're not saying, oh, I got this kind of communication event for photons. No, we're not keeping track of that.
*  This neuron fired, this synapse says that neuron fired. That's it.
*  So that's a that's a noise filtering property of those detectors.
*  However, there are other applications where you'd rather know the exact number of photons that can be very useful in quantum computing with light.
*  And our group does a lot of work around another kind of superconducting sensor called a transition edge sensor that Adrian Alita in our group does a lot of work on that.
*  And that can tell you based on the amplitude of the current pulse you divert exactly how many photons were in that pulse.
*  So what's that useful for? Just one way that you can encode information in quantum states of light is in the number of photons.
*  You can have what are called number states and a number state will have a well defined number of photons.
*  And maybe the output of your quantum computation encodes its information in the number of photons that are generated.
*  So if you have a detector that is sensitive to that, it's extremely useful.
*  Can you achieve like a clock with photons or is that not important? Is there an asynchronicity here?
*  In general, it can be important. Clock distribution is a big challenge in especially large computational systems.
*  And so, yes, optical clocks, optical clock distribution is a very powerful technology.
*  I don't know the state of that field right now, but I imagine that if you're trying to distribute a clock across any appreciable size computational system, you want to use light.
*  Yeah, I wonder how these giant systems work, especially like supercomputers.
*  Do they need to do clock distribution or are they doing more ad hoc parallel like concurrent programming?
*  Like there's some kind of locking mechanisms or something.
*  That's a fascinating question. But the let's zoom in at this very particular question of computation on a processor and communication between processors.
*  So what does this system look like that you're envisioning?
*  One of the places you're envisioning it is in the paper on optoelectronic intelligence.
*  So what are we talking about? Are we talking about something that starts to look a lot like the human brain or does it still look a lot like a computer?
*  What are the size of this thing? Is it go inside a smartphone or as you said, does it go inside something that's more like a house?
*  Like what should we be imagining? What are you thinking about when you're thinking about these fundamental systems?
*  Let me introduce the word neuromorphic.
*  There's this concept of neuromorphic computing where what that broadly refers to is computing based on the information processing principles of the brain.
*  And as digital computing seems to be pushing towards some fundamental performance limits, people are considering architectural advances, drawing inspiration from the brain, more distributed parallel network kind of architectures and stuff.
*  And so there's this continuum of neuromorphic from things that are pretty similar to digital computers, but maybe there are more cores and the way they send messages is a little bit more like the way brain neurons send spikes.
*  But for the most part, it's still digital electronics.
*  And then you have some things in between where maybe you're using transistors, but now you're starting to use them instead of in a digital way, in an analog way.
*  And so you're trying to get those circuits to behave more like neurons.
*  And then that's quite a bit more on the neuromorphic side of things.
*  You're trying to get your circuits, although they're still based on silicon, you're trying to get them to perform operations that are highly analogous to the operations in the brain.
*  That's where a great deal of work is in neuromorphic computing.
*  People like Jakomo Indiveri and Gert Kaunberg, Jennifer Hasler, countless others.
*  It's a rich and exciting field going back to Carver Mead in the late 1980s.
*  And then all the way on the other extreme of the continuum is where you say, I'll give up anything related to transistors or semiconductors or anything like that.
*  I'm not starting with the assumption that I'm going to use any kind of conventional computing hardware.
*  And instead, what I want to do is try and understand what makes the brain powerful at the kind of information processing it does.
*  And I want to think from first principles about what hardware is best going to enable us to capture those information processing principles in an artificial system.
*  And that's where I live.
*  That's where I'm doing my exploration these days.
*  So what are the first principles of brain-like computation communication?
*  Right. Yeah, this is so important. And I'm glad we booked 14 hours for this because...
*  I only have 13. I'm sorry.
*  Okay, so the brain is notoriously complicated.
*  And I think that's an important part of why it can do what it does.
*  But okay, let me try to break it down.
*  Starting with the devices, neurons, as I said before, they're sophisticated devices in and of themselves.
*  And synapses are too. They can change their state based on the activity.
*  So they adapt over time. That's crucial to the way the brain works.
*  They don't just adapt on one time scale.
*  They can adapt on a myriad time scales from the spacing between pulses, the spacing between spikes that come from neurons all the way to the age of the organism.
*  Also relevant, perhaps I think the most important thing that's guided my thinking is the network structure of the brain.
*  Which can also be adjusted on different scales.
*  Absolutely. Yes. So you're changing the strength of contacts. You're changing the spatial distribution of them.
*  Although spatial distribution doesn't change that much once you're a mature organism.
*  But that network structure is really crucial. So let me dwell on that for a second.
*  You can't talk about the brain without emphasizing that most of the neurons in the neocortex or the prefrontal cortex,
*  the part of the brain that we think is most responsible for high level reasoning and things like that, those neurons make thousands of connections.
*  So you have this network that is highly interconnected.
*  And I think it's safe to say that one of the primary reasons that they make so many different connections is that allows information to be communicated very rapidly from any spot in the network to any other spot in the network.
*  So that's a sort of spatial aspect of it.
*  You can quantify this in terms of concepts that are related to fractals and scale invariants, which I think is a very beautiful concept.
*  So what I mean by that is kind of no matter what spatial scale you're looking at in the brain within certain bounds, you see the same general statistical pattern.
*  So if I draw a box around some region of my cortex, most of the connections that those neurons within that box make are going to be within the box to each other in their local neighborhood.
*  And that's sort of called clustering, loosely speaking. But a non-negligible fraction is going to go outside of that box.
*  And then if I draw a bigger box, the pattern is going to be exactly the same.
*  So you have this scale invariance and you also have a non-vanishing probability of a neuron making connection very far away.
*  So suppose you want to plot the probability of a neuron making a connection as a function of distance.
*  If that were an exponential function, it would go e to the minus radius over some characteristic radius, and it would drop off up to some certain radius.
*  So the probability would be reasonably close to one and then beyond that characteristic length r0, it would drop off sharply.
*  And so that would mean that the neurons in your brain are really localized. And that's not what we observe.
*  Instead, what you see is that the probability of making a longer distance connection, it does drop off, but it drops off as a power loss.
*  So the probability that you're going to have a connection at some radius r goes as r to the minus some power.
*  And that's more that's what we see with with forces in nature, like the electromagnetic force between two particles or gravity goes as one over the radius squared.
*  So you can see this in fractals. I love that there's a like a fractal dynamics of the brain that if you zoom out, you draw the box and you increase that box by certain step sizes,
*  you're going to see the same statistics. I think that's probably very important to the way the brain processes information.
*  It's not just in the spatial domain. It's also in the temporal domain. And what I mean by that is that's incredible that this emerged through the evolutionary process that potentially somehow connected to the way the physics of the universe works.
*  I couldn't agree more that it's a deep and fascinating subject that I hope to be able to spend the rest of my life studying.
*  You think you need to solve, understand this, this fractal nature in order to understand intelligence and communication?
*  I do think so. I think they are deeply intertwined. Yes, I think power laws are right at the heart of it.
*  So just to just to push that one through the same thing happens in the temporal domain.
*  Suppose your neurons in your brain were always oscillating at the same frequency, then the probability of finding a neuron oscillating as a function of frequency would be this narrowly peaked function around that certain characteristic frequency.
*  That's not at all what we see. The probability of finding neurons oscillating or pulsing, producing spikes at a certain frequency is again a power law, which means there's no defined scale of the temporal activity.
*  It's a temporal activity in the brain. It's you don't what at what speed do your thoughts occur?
*  Well, there's a there's a fastest speed they can occur, and that is limited by communication and other other things.
*  But there's not a characteristic scale. We have thoughts on all temporal scales from, you know, a few tens of milliseconds, which is physiologically limited by our devices.
*  Compare that to tens of picoseconds that I talked about in superconductors all the way up to the lifetime of the organism.
*  You can still think about things that happened to you when you were a kid.
*  If you want to be really trippy and across multiple organisms in the entirety of human civilization, you have thoughts that span organisms, right?
*  Yes, taking it to that level.
*  If you're willing to see the entirety of the human species as a single organism with a collective intelligence, and that too on a spatial and temporal scale, there's thoughts occurring.
*  And then if you look at not just the human species, but the entirety of life on Earth as an organism with thoughts that occurring that are greater and greater sophisticated thoughts, there's a different spatial and temporal scale there.
*  This is getting very suspicious.
*  Hold on, though. Before we're done, I just want to just tie the bow and say that the spatial and temporal aspects are intimately interrelated with each other.
*  So activity between neurons that are very close to each other is more likely to happen on this faster time scale, and information is going to propagate and encompass more of the brain, more of your cortices, different modules in the brain are going to be engaged in information processing on longer time scales.
*  So there's this concept of information integration where neurons are specialized. Any given neuron or any cluster of neuron has its specific purpose, but they're also very much integrated.
*  So you have neurons that specialize but share their information. And so that happens through these fractal nested oscillations that occur across spatial and temporal scales.
*  I think capturing those dynamics in hardware, to me, that's the goal of neuromorphic computing.
*  So does it need to look? So first of all, that's fascinating. We stated clear principles here. Now, does it have to look like the brain outside of those principles as well?
*  Like what other characteristics have to look like the human brain? Or can it be something very different?
*  Well, it depends on what you're trying to use it for. And so I think a lot of the community asks that question a lot. What are you going to do with it? And I completely get it. I think that's a very important question.
*  And it's also sometimes not the most helpful question. What if what you want to do with it is study it? What if you just want to see what do you have to build into your hardware in order to observe these dynamical principles?
*  And also, I ask sometimes I ask myself that question every day, and I'm not sure I'm able to answer that. It's like, what are you going to do with this particular neuromorphic machine?
*  So suppose what we're trying to do with it is build something that thinks we're not trying to get it to make us any money or drive a car. Maybe we'll be able to do that. But that's not our goal.
*  Our goal is to see if we can get the same types of behaviors that we observe in our own brain and by behaviors in this sense, what I mean the behaviors of the components, the neurons, the network, that kind of stuff.
*  I think there's another element that I didn't really hit on that that you also have to build into this. And those are architectural principles. They have to do with the hierarchical modular construction of the network.
*  And without getting too lost in jargon, the main point that I think is relevant there, let me try and illustrate it with a cartoon picture of the architecture of the brain.
*  So in the brain, you have the cortex, which is sort of this outer sheet. It's actually a layered structure. If you could take it out of your brain, you could unroll it on the table and it would be about the size of a pizza sitting there.
*  And that's a module. It does certain things. It processes as Yorgi Buzaki would say, it processes the what of what's going on around you.
*  But you have another really crucial module that's called the hippocampus. And that network is structured entirely differently. First of all, this cortex that had described 10 billion neurons in there.
*  So numbers matter here. And they're organized in that sort of power law distribution where the probability of making a connection drops off as a power law in space.
*  The hippocampus is another module that's important for understanding where you are, when you are, keeping track of your position in space and time.
*  And that network is very much random. So the probability of making a connection, it almost doesn't even drop off as a function of distance.
*  It's the same probability that you'll make it here to over there. But there are only about 100 million neurons there.
*  So you can have that huge, densely connected module because it's not so big. And then the neocortex or the cortex and the hippocampus, they talk to each other constantly.
*  And that communication is largely facilitated by what's called the thalamus. I'm not a neuroscientist here. I'm trying to do my best to recite things.
*  Cartoon picture of the brain. I gotcha.
*  Yeah, something like that. So this thalamus is coordinating the activity between the neocortex and the hippocampus and making sure that they talk to each other at the right time and send messages that will be useful to one another.
*  So this all taken together is called the thalamocortical complex. And it seems like building something like that is going to be crucial to capturing the types of activity we're looking for because those responsibilities, those separate modules, they do different things.
*  That's got to be central to achieving these states of efficient information integration across space and time.
*  By the way, I am able to achieve this state by watching simulations, visualizations of the thalamocortical complex. There's a few people I forget from where they've created these incredible visual illustrations of like visual stimulation from the eye or something like that.
*  It is in this image like flowing through the brain.
*  Wow. I haven't seen that. I got to check that out.
*  So it's one of those things you find this stuff in the world and you see like on YouTube it has like 1000 views these like these visualizations of the human brain processing information and like because there's this chemistry there.
*  Because this is act from actual human brains. I don't know how they're doing the coloring, but they're able to actually trace the like different the chemical and the electrical signals throughout the brain and the visual thing.
*  It's like, Whoa, because it looks kind of like the universe. I mean, the whole thing is just in cry. I recommend it highly. I'll probably post a link to it. But you can just look for one of the things they simulate is the thalamocortical complex and just visualization.
*  You can find that yourself on YouTube, but it's beautiful. The other question I have for you is how does memory play into all of this? Because all the signals sending back and forth. That's kind of like that's computation and communication.
*  But that's kind of like, you know, processing of inputs and outputs to produce outputs in the system. That's kind of like maybe reasoning. Maybe there's some kind of recurrence. But like, is there a storage mechanism that you think about in the context in neuromorphic computing?
*  Yeah, absolutely. So that's got to be central. You have to have a way that you can store memories and there are a lot of different kinds of memory in the brain. That's yet another example of how it's not a simple system. So there's one kind of memory.
*  One way of talking about memory usually starts in the context of Hopfield networks. You were lucky to talk to John Hopfield on this program. But the basic idea there is working memory is stored in the dynamical patterns of activity between neurons.
*  And you can think of a certain pattern of activity as an attractor, meaning if you put in some signal that's similar enough to other previously experienced signals like that, then you're going to converge to the same network dynamics and you will see these neurons
*  participate in the same network patterns of activity that they have in the past. So you can talk about the probability that different inputs will allow you to converge to different basins of attraction. And you might think of that as, oh, I saw this face and then I excited this network pattern of activity because last time I saw that face, I was at, you know, what some movie and that that's a famous person is on the screen or something like that. So so that's one memory storage mechanism. But that's one way of thinking about it.
*  So that's one memory storage mechanism. But crucial to the ability to imprint those memories in your brain is the ability to change the strength of connection between one neuron and another that synaptic connection between them. So synaptic weight update is a massive field of neuroscience and neuromorphic computing as well.
*  So there are two poles to that on that spectrum. One in OK, so in more in the language of machine learning, we would talk about supervised and unsupervised learning. And when I'm trying to tie that down to neuromorphic computing, I will use a definition of supervised learning, which basically means the external user, the person who's controlling this hardware has some knob that they can tune to change the way that they're
*  doing it. So you can change each of the synaptic weights depending on whether or not the network is doing what you want it to do. Whereas what I mean in this conversation when I say unsupervised learning is that those synaptic weights are are dynamically changing in your network based on nothing that the user is doing, nothing that there's no wire from the outside going into any of those synapses.
*  So the neural network itself is reconfiguring those synaptic weights based on physical properties that you've built into the devices. So if if the synapse receives a pulse from here and that causes the neuron to spike some circuit built in there with no help from me or anybody else, adjust the weight in a way that makes it more likely to store the useful information and excite the useful network patterns and makes it less likely that random noise useless information is going to be used.
*  So this communication events will have important effect on the network activity.
*  So there's memory encoded in the weights, the synaptic weights. What about the formation of something that's not often done in machine learning, the formation of new synaptic connections?
*  Right. Well, that seems to so again, not not a neuroscientist here, but my reading of the literature is that that's particularly crucial in early stages of brain development, where a newborn is born with tons of extra synaptic connections.
*  And it's actually pruned over time. So the number of synapses decreases as opposed to growing new long distance connections. It is possible in the brain to grow new neurons and assign new synaptic connections.
*  But it doesn't seem to be the primary mechanism by which the brain is learning. So, for example, like right now, sitting here talking to you, you say lots of interesting things and I learn what I learned from you and I can remember things that you just said.
*  And I didn't grow new axonal connections down to new synapses to to enable those. It's plasticity mechanisms in the between in the synaptic connections between neurons that enable me to learn on that time scale.
*  So at the very least that you can sufficiently approximate that with just weight updates, you don't need to form new connections.
*  I would say weight updates are a big part of it. I also think there's more because, broadly speaking, when we're doing machine learning, our networks, say we're talking about feed forward deep neural networks, the temporal domain is not really part of it.
*  Okay, you're going to put in an image and you're going to get out a classification and you're going to do that as fast as possible. So you care about time, but time is not part of the essence of this thing, really.
*  Whereas in spiking neural networks, what we see in the brain, time is as crucial a space and they're intimately intertwined, as I've tried to say.
*  And so adaptation on on different time scales is important, not not just in memory for formation, although it plays a key role there, but also in just keeping the activity in a useful dynamic range.
*  So you have other plasticity mechanisms, not just weight update, or at least not on the time scale of many action potentials, but even on the shorter time scale.
*  So a synapse can become much less efficacious. It can transmit a weaker signal after the second, third, fourth action potential to occur in a sequence.
*  So that's what's called short term synaptic plasticity, which is a form of learning. You're learning that I'm getting too much stimulus from looking at something bright right now, so I need to tone that down.
*  There's also another really important mechanism in learning. It's called meta plasticity.
*  What that seems to be is a way that you change not the weights themselves, but the rate at which the weights change.
*  So when I am in, say, a lecture hall and my this is a potentially terrible cartoon example, but let's say I'm in a lecture hall and it's time to learn, right?
*  So my brain will release more, perhaps dopamine or some neuromodulator that's going to change the rate at which synaptic plasticity occurs.
*  So that can make me more sensitive to learning at certain times, more sensitive to overriding previous information and less sensitive at other times.
*  And finally, as long as I'm rattling off the list, I think another concept that falls in the category of learning or memory adaptation is homeostasis or homeostatic adaptation where neurons have the ability to control their firing rate.
*  So if one neuron is just blasting way too much, it will naturally tone itself down.
*  Its threshold will adjust so that it stays in a useful dynamical range.
*  And we see that that's captured in deep neural networks where you don't just change the synaptic weights, but you can also move the thresholds of simple neurons in those models.
*  And so to achieve the spike in neural networks, you want to use like you want to implement the first principles that you mentioned of the temporal and the spatial fractal dynamics here.
*  So you can you can communicate locally, you can communicate across much greater distances and do the same thing in space and do the same thing in time.
*  Now you have like a chapter called Superconducting Hardware for Neuromorphic Computing.
*  So what are some ideas that integrate some of the things we've been talking about in terms of the first principles of neuromorphic computing and the ideas that you outline in optoelectronic intelligence?
*  Yeah, so let me start, I guess, on the communication side of things, because that's what led us down this track in the first place.
*  By us, I'm talking about my my team of colleagues at NIST, you know, Sayid Han, Bryce Brimavere, Sonia Buckley, Jeff Chiles, Adam McCaughan to name, Alex Tate to name a few, our group leaders, Sehwoon Nam and Rich Mirren.
*  We've all contributed to this. This is not this is not me saying necessarily just the things that that I've proposed, but sort of where our team's thinking has evolved over the years.
*  Can I can quickly ask what is NIST and where is this amazing group of people located?
*  NIST is the National Institute of Standards and Technology.
*  The larger facility is out in Gaithersburg, Maryland. Our team is located in Boulder, Colorado.
*  NIST is a federal agency under the Department of Commerce. We do a lot with by we, I mean other people at NIST, but do a lot with standards, you know, making sure that we understand the system of units, international system of units, precision measurements.
*  There's a lot going on in electrical engineering, material science.
*  And it's historic. I mean, I mean, it's like it's one of those it's like MIT or something like that.
*  It has a reputation over many decades of just being this really a place where there's a lot of really people have done a lot of amazing things.
*  But in terms of the people in your team, in this team of people involved in the concept we're talking about now, I'm just curious, what kind of disciplines are we talking about?
*  What is it?
*  Mostly physicists and electrical engineers, some material scientists.
*  But I would say, yeah, I think physicists and electrical engineers, my background is in photonics, the use of light for technology.
*  So coming from there, I tend to have found colleagues that are more from that background, although Adam McCaughan more of a superconducting electronics background.
*  We need a diversity of folks. This project is sort of cross disciplinary.
*  I would love to be working more with neuroscientists and things, but we haven't we haven't reached that scale yet.
*  But you're focused on the hardware side, which requires all the disciplines that you mentioned.
*  And then, of course, you know, science may be a source of inspiration for some of the long term vision.
*  I would actually call it more than inspiration. I would call it sort of a roadmap.
*  We're not trying to to build exactly the brain, but I don't think it's enough to just say, oh, neurons kind of work like that.
*  Let's kind of do that thing.
*  I mean, we're we're we're very much following the concepts that the cognitive sciences have laid out for us, which I believe is a really robust roadmap.
*  I mean, just on a little bit of a tangent, it's often stated that we just don't understand the brain.
*  And so it's really hard to replicate it because we just don't know what's going on there.
*  And I maybe five or seven years ago, I would have said that.
*  But as I got more interested in the subject, I read more of the neuroscience literature and I was just taken by the exact opposite sense.
*  I can't believe how much they know about this.
*  I can't believe how mathematically rigorous and sort of theoretically complete a lot of the concepts are.
*  That's not to say we understand consciousness or we understand the cell for anything like that.
*  But why is the brain what is the brain doing and why is it doing those things?
*  We have neuroscientists have a lot of answers to those questions.
*  So there's a lot if you're a hardware designer that just wants to get going.
*  Whoa, it's pretty clear which direction to go in, I think.
*  OK, so I love I love the optimism behind that.
*  But in the implementation of these systems that uses superconductivity, how do you make it happen?
*  So to me, it starts with thinking about the communication network.
*  You know for sure that the ability of each neuron to communicate to many thousands of colleagues across the network is indispensable.
*  I take that as a core principle of my my architecture, my thinking on the subject.
*  So coming from coming from a background in photonics, it was very natural to say, OK, we're going to use light for communication.
*  Just in case listeners may not know, light is often used in communication.
*  I mean, if you think about radio, that's light.
*  It's long wavelengths, but it's electromagnetic radiation.
*  It's the same. It's the same physical phenomenon obeying exactly the same Maxwell's equations.
*  And then all the way down to fiber fiber optics.
*  Now you're using visible or near infrared wavelengths of light.
*  But the way you send messages across the ocean is now contemporary over optical fibers.
*  So using light for communication is not a stretch.
*  It makes perfect sense.
*  So you might ask, well, why don't you use light for communication in a conventional microchip?
*  And the answer to that is, I believe, physical.
*  If we had a light source on a silicon chip that was as simple as a transistor,
*  we would there would not be a processor in the world that didn't use light for communication, at least above some distance.
*  How many light sources are needed? Oh, you need a light source at every single point.
*  A light source per neuron. Per neuron.
*  But then if you could have a really small and nice light source, you can your definition of neuron could be flexible.
*  Could be. Yes. Yes. Sometimes it's helpful to me to say in this hardware, a neuron is that entity which has a light source.
*  And then there was light.
*  I can explain more about that.
*  But somehow this like rhymes with consciousness because people often say the light of consciousness.
*  So that consciousness is that which is conscious.
*  I got it. That's not my quote.
*  That's me. That's my quote.
*  See, that quote comes from my background.
*  Yours is in optics, mine in light, mine's in darkness.
*  So go ahead.
*  So the point I was making there is that if it was easy to manufacture light sources along with transistors on a silicon chip, they would be everywhere.
*  And it's not easy.
*  People have been trying for decades and it's actually extremely difficult.
*  I think an important part of our research is dwelling right at that at that spot there.
*  So is it physics or engineering?
*  It's physics. So OK, so it's physics, I think.
*  So what I mean by that is as we discussed, silicon is the material of choice for transistors.
*  And it's very difficult to imagine that that's going to change anytime soon.
*  Silicon is notoriously bad at emitting light, and that has to do with the immutable properties of silicon itself, the way that the energy bands are structured in silicon.
*  You're never going to make silicon efficient as a light source at room temperature without doing very exotic things that degrade its ability to interface nicely with those transistors in the first place.
*  So that's like one of these things where it's why is nature dealing us that blow?
*  You give us these beautiful transistors and you give us all the motivation to use light for communication, but then you don't give us a light source.
*  So, well, OK, you do give us a light source, compound semiconductors, like we talked about back at the beginning, an element from group three and an element from group five from an alloy where every other lattice site switches which element it is.
*  Those have much better properties for generating light.
*  You put electrons in light comes out almost 100% of the electron hole.
*  It can be made efficient.
*  I'll take your offer.
*  OK. However, I say it's physics, not engineering, because it's very difficult to get those compound semiconductor light sources situated with your silicon in order to do that ion implantation that I talked about at the beginning.
*  So you've got to make all of your transistors first and then put the compound semiconductors on top of there.
*  You can't grow them afterwards because that requires high temperature.
*  It screws up all your transistors.
*  You try and stick them on there.
*  They don't have the same lattice constant.
*  The spacing between atoms is different enough that it just doesn't work.
*  Nature does not seem to be telling us that, hey, go ahead and combine light sources with your digital switches for conventional digital computing and conventional digital computing will often require smaller scale, I guess, in terms of like smartphone.
*  So in which kind of systems can does nature hint that we can use light and photons for communication?
*  Well, so let me just try and be clear.
*  You can use light for communication in digital systems.
*  Just the light sources are not intimately integrated with the silicon.
*  You manufacture all the silicon.
*  You have your microchip, plunk it down, and then you manufacture your light sources, separate chip, completely different parts of the silicon.
*  You have your microchip, completely different process made in a different foundry, and then you put those together at the package level.
*  So now you have some, I would say, a great deal of architectural limitations that are introduced by that sort of package level integration as opposed to monolithic on the same chip integration.
*  But it's still a very useful thing to do.
*  So that's where I had done some work previously before I came to NIST.
*  There's a project led by Vladimir Stoyanovich that now spun out into a company called IR Labs, led by Mark Wade and Chen Sun, where they're doing exactly that.
*  So you have your light source chip, your silicon chip, whatever it may be doing.
*  Maybe it's digital electronics.
*  Maybe it's some other control purpose, something.
*  And the silicon chip drives the light source chip and modulates the intensity of the light so you can get data out of the package on an optical fiber.
*  And that still gives you tremendous advantages in bandwidth as opposed to sending those signals out over electrical lines.
*  But it is somewhat peculiar to my eye that they have to be integrated at this package level.
*  And those people, I mean, they're so smart.
*  Those are my colleagues that I respect a great deal.
*  So it's very clear that it's not just they're making a bad choice.
*  This is what physics is telling us.
*  It just wouldn't make any sense to try to stick them together.
*  Yeah. So even if it's difficult, it's easier than the alternative, unfortunately.
*  I think so, yes.
*  And again, I need to go back and make sure that I'm not taking the wrong way.
*  I'm not saying that the pursuit of integrating compound semiconductors with silicon is fruitless and shouldn't be pursued.
*  It should.
*  People are doing great work.
*  Kai Mei Lau and John Bowers, others, they're doing it and they're making progress.
*  But to my eye, it doesn't look like that's ever going to be just the standard monolithic light source on silicon process.
*  I just don't see it.
*  Yeah. So nature kind of points the way usually.
*  And if you resist nature, you're going to have to do a lot more work.
*  And it's going to be expensive and not scalable.
*  Got it.
*  But OK, so let's go like far into the future.
*  Let's imagine this gigantic neuromorphic computing system that simulates all of our realities.
*  It currently is mentioned Matrix four.
*  So this thing, this powerful computer, how does it operate?
*  So what are the neurons?
*  What is the communication?
*  What's your sense?
*  All right. So let me let me now after spending 45 minutes trashing light source integration with silicon,
*  let me now say why I'm basing my entire life professional life on integrating light sources with electronics.
*  I think the game is completely different when you're talking about superconducting electronics for several reasons.
*  Let me try to go through them.
*  One is that, as I mentioned, it's difficult to integrate those compound semiconductor light sources with silicon.
*  With silicon is a requirement that is introduced by the fact that using semiconducting electronics in superconducting electronics,
*  you're still going to start with a silicon wafer, but it's just the bread for your sandwich.
*  And in a lot of ways, you're not using that silicon in precisely the same way for the electronics.
*  You're now depositing superconducting materials on top of that.
*  The prospects for integrating light sources with that kind of an electronic process are certainly less explored.
*  But I think much more promising because you don't need those light sources to be intimately integrated with the transistors.
*  That's where the problems come up.
*  They don't need to be lattice matched to the silicon, all that kind of stuff.
*  Instead, it seems possible that you can take those compound semiconductor light sources,
*  stick them on the silicon wafer, and then grow your superconducting electronics on the top of that.
*  It's at least not obviously going to fail.
*  So the computation would be done on the superconductive material as well?
*  Yes, the computation is done in the superconducting electronics.
*  And the light sources receive signals that say, hey, a neuron reach threshold, produce a pulse of light,
*  send it out to all your downstream synaptic connections.
*  Those are again superconducting electronics.
*  Perform your computation and you're off to the races. Your network works.
*  So then if we can rewind real quick.
*  So what are the limitations of the challenges of superconducting electronics
*  when we think about constructing these kinds of systems?
*  So actually, let me say one other thing about the light sources.
*  Yes, please.
*  And then I'll move on, I promise, because this is probably tedious for some.
*  This is super exciting.
*  OK, one other thing about the light sources.
*  I said that silicon is terrible at emitting photons.
*  It's just not what it's meant to do.
*  However, the game is different when you're at low temperature.
*  If you're working with superconductors, you have to be at low temperature because they don't work otherwise.
*  When you're at four Kelvin, silicon is not obviously a terrible light source.
*  It's still not as efficient as compound semiconductors, but it might be good enough for this application.
*  The final thing that I'll mention about that is, again, leveraging superconductors.
*  As I said, in a different context, superconducting detectors can receive one single photon.
*  In that conversation, I failed to mention that semiconductors can also receive photons.
*  That's the primary mechanism by which it's done.
*  A camera in your phone that's receptive to visible light is receiving photons.
*  It's based on silicon, or you can make it in different semiconductors for different wavelengths.
*  But it requires on the order of a thousand, a few thousand photons to receive a pulse.
*  Now, when you're using a superconducting detector, you need one photon, exactly one.
*  I mean, one or more.
*  So the fact that your synapses can now be based on superconducting detectors instead of semiconducting detectors
*  brings the light levels that are required down by some three orders of magnitude.
*  So now you don't need good light sources.
*  You can have the world's worst light sources.
*  As long as they spit out maybe a few thousand photons every time a neuron fires,
*  you have the hardware principles in place that you might be able to perform this optoelectronic integration.
*  To me, optoelectronic integration is just so enticing.
*  We want to be able to leverage electronics for computation, light for communication,
*  working with silicon microelectronics at room temperature that has been exceedingly difficult.
*  And I hope that when we move to the superconducting domain,
*  target a different application space that is neuromorphic instead of digital,
*  and use superconducting detectors, maybe optoelectronic integration comes to us.
*  Okay, so there's a bunch of questions.
*  So one is temperature.
*  So in these kind of hybrid heterogeneous systems, what's the temperature?
*  What are some of the constraints of the operation here?
*  Does it all have to be at 4 Kelvin as well?
*  4 Kelvin. Everything has to be at 4 Kelvin.
*  Okay, so what are the other engineering challenges of making this kind of optoelectronic systems?
*  Let me just dwell on that 4 Kelvin for a second, because some people hear 4 Kelvin and they just get up and leave.
*  They just say, I'm not doing it.
*  And to me, that's very earth-centric, species-centric.
*  We live in 300 Kelvin, so we want our technologies to operate there too.
*  I totally get it.
*  Yeah, what's zero Celsius?
*  Zero Celsius is 273 Kelvin.
*  So we're talking very, very cold here.
*  Not even Boston cold.
*  This is real cold.
*  This is Siberia cold.
*  Okay, so just for reference, the temperature of the cosmic microwave background is about 2.7 Kelvin.
*  So we're still warmer than deep space.
*  Yeah, good.
*  So that when the universe dies out, it'll be colder than 4K?
*  It's already colder than 4K.
*  In the expanses, you don't have to get that far away from the earth in order to drop down to not far from 4K.
*  So what you're saying is the aliens that live at the edge of the observable universe are using superconductive material for their computation.
*  They don't have to live at the edge of the universe.
*  The aliens that are more advanced than us in their solar system are doing this in their asteroid belt.
*  We can get to that.
*  Because they can get to that temperature easier there?
*  Sure. All you have to do is reflect the sunlight away and you have a huge head start.
*  So the sun is the problem here?
*  It's warm here on earth.
*  So how do we get to 4K?
*  It's a very different kind of 4K.
*  What I want to say about temperature is that if you can swallow that, if you can say,
*  all right, I give up applications that have to do with my cell phone and the convenience of a laptop on a train.
*  And you instead, for me, I'm very much in the scientific headspace.
*  I'm not looking at products.
*  I'm not looking at what this will be useful to sell to consumers.
*  Instead, I'm thinking about scientific questions.
*  Well, it's just not that bad to have to work at 4K.
*  We do it all the time in our labs at NIST.
*  For reference, the entire quantum computing sector usually has to work at something like 100 millikelvin, 50 millikelvin.
*  So now you're talking of another factor of 100 even colder than that, a fraction of a degree.
*  And everybody seems to think quantum computing is going to take over the world.
*  It's so much more expensive to have to get that extra factor of 10 or whatever colder.
*  And yet it's not stopping people from investing in that area.
*  And by investing, I mean putting their research into it as well as venture capital or whatever.
*  So based on the energy of what you're commenting on, I'm getting a sense that's one of the criticism of this approach is 4K, 4K is a big negative.
*  It is the showstopper for a lot of people.
*  Understandably, I'm not saying that that's not a consideration.
*  Of course it is.
*  Okay, so different motivations for different people.
*  In the academic world, suppose you spent your whole life learning about silicon microelectronic circuits.
*  You send a design to a foundry.
*  They send you back a chip and you go test it at your tabletop.
*  And now I'm saying, here, now learn how to use all these cryogenics so you can do that at 4K.
*  No, come on, man. I want to do that.
*  That sounds bad.
*  It's the old momentum, the Titanic of the turning.
*  Yeah, kind of.
*  But you're saying that's not too much of a...
*  When we're looking at large systems and the gain you can potentially get from them, that's not that much of a cost.
*  And when you want to answer the scientific question about what are the physical limits of cognition.
*  Well, the physical limits, they don't care if you're at 4K.
*  If you can perform cognition at a scale orders of magnitude beyond any room temperature technology,
*  but you got to get cold to do it, you're going to do it.
*  And to me, that's the interesting application space.
*  It's not even an application space.
*  That's the interesting scientific paradigm.
*  So I personally am not going to let low temperature stop me from realizing a technological domain or realm
*  that is achieving in most ways everything else that I'm looking for in my hardware.
*  So that's a big one. Is there other kind of engineering challenges that you envision?
*  Yeah, yeah, yeah.
*  So let me take a moment here because I haven't really described what I mean by a neuron or a network in this particular hardware.
*  Yeah, do you want to talk about loop neurons?
*  And there's so many fascinating ideas.
*  But you just have so many amazing papers that people should definitely check out.
*  And the titles alone are just killer. So anyway, go ahead.
*  Right. So let me say big picture based on optics, photonics for communication, superconducting electronics for computation.
*  How does this all work?
*  So a neuron in this hardware platform can be thought of as circuits that are based on Josephson junctions,
*  like we talked about before, where every time a photon comes in.
*  So let's start by talking about a synapse.
*  A synapse receives a photon, one or more, from a different neuron, and it converts that optical signal to an electrical signal.
*  The amount of current that that adds to a loop is controlled by the synaptic weight.
*  So as I said before, you're popping fluxons into a loop, right?
*  So a photon comes in, it hits a superconducting single photon detector, one photon.
*  The absolute physical minimum that you can communicate from one place to another with light.
*  And that detector then converts that into an electrical signal, and the amount of signal is correlated with some kind of weight.
*  Yeah. So the synaptic weight will tell you how many fluxons you pop into the loop.
*  It's an analog number. We're doing analog computation now.
*  Well, can you just linger on that? What the heck is a fluxon? Are we supposed to know this?
*  Or is this a funny, it's like the Big Bang. Is this a funny word for something deeply technical?
*  No, let's try to avoid using the word fluxon because it's not actually necessary.
*  It's fun to say though, so it's very necessary, I would say.
*  When a photon hits that superconducting single photon detector, current is added to a superconducting loop.
*  And the amount of current that you add is an analog value, can have 8-bit equivalent resolution, something like that. 10 bits, maybe.
*  That's amazing, by the way. This is starting to make a lot more sense.
*  When you're using superconductors for this, the energy of that circulating current is less than the energy of that photon.
*  So your energy budget is not destroyed by doing this analog computation.
*  So now in the language of a neuroscientist, you would say that's your postsynaptic signal.
*  You have this current being stored in a loop. You can decide what you want to do with it.
*  Most likely you're going to have it decay exponentially.
*  So every single synapse is going to have some given time constant.
*  And that's determined by putting some resistor in that superconducting loop.
*  So a synapse event occurs when a photon strikes a detector, adds current to that loop, it decays over time.
*  That's the postsynaptic signal. Then you can process that in a dendritic tree.
*  Bryce Primavera and I have a paper that we've submitted about that.
*  For the more neuroscience-oriented people, there's a lot of dendritic processing, a lot of plasticity mechanisms you can implement with essentially exactly the same circuits.
*  You have this one simple building block circuit that you can use for a synapse, for a dendrite, for the neuron cell body, for all the plasticity functions.
*  It's all based on the same building block, just tweaking a couple parameters.
*  So this basic building block has both an optical and an electrical component, and you can just build arbitrary large systems with that?
*  Close. You're not at fault for thinking that that's what I meant.
*  What I should say is that if you want it to be a synapse, you tack a superconducting detector onto the front of it.
*  And if you want it to be anything else, there's no optical component.
*  Got it. So at the front, optics in the front, electrical stuff in the back.
*  Electrical, yeah, in the processing and in the output signal that it sends to the next stage of processing further.
*  So the dendritic trees is electrical.
*  It's all electrical. It's all electrical in the superconducting domain.
*  For anybody who's up on their superconducting circuits, it's just based on a DC squid, the most ubiquitous, which is a circuit composed of two Josephson junctions.
*  So it's a very bread and butter kind of thing.
*  And then the only place where you go beyond that is the neuron cell body itself.
*  It's receiving all these electrical inputs from the synapses or dendrites or however you've structured that particular unique neuron.
*  And when it reaches its threshold, which occurs by driving a Josephson junction above its critical current, it produces a pulse of current, which starts an amplification sequence, voltage amplification, that produces light out of a transmitter.
*  So one of one of our colleagues, Adam McCaughan and Sonia Buckley as well, did a lot of work on the light sources and the amplifiers that drive the current and produce sufficient voltage to drive current through that now semiconducting part.
*  So that light source is the semiconducting part of a neuron.
*  And that so the neuron has reached threshold. It produces a pulse of light.
*  That light then fans out across a network of waveguides to reach all the downstream synaptic terminals that perform this process themselves.
*  So it's probably worth explaining what a network of waveguides is, because a lot of listeners aren't going to know that.
*  Look up the papers by Jeff Chiles on this one.
*  But basically, light can be guided in a simple, basically wire of usually an insulating material.
*  So silicon, silicon nitride, different kinds of glass, just like in a fiber optic, it's glass, silicon dioxide.
*  That makes it a little bit big. We want to bring these down.
*  So we use different materials like silicon nitride.
*  But basically, just imagine a rectangle of some material that just goes and branches, forms different different branch points that target different sub regions of the network.
*  You can transition between layers of these.
*  And now we're talking about building in the third dimension, which is absolutely crucial.
*  So that's what waveguides are.
*  Yeah, that's great. Why the third dimension is crucial?
*  Okay, so yes, you were talking about what are some of the technical limitations.
*  One of the things that I believe we have to grapple with is that our brains are miraculously compact.
*  For the number of neurons that are in our brain, it sure does fit in a small volume, as it would have to if we're going to be biological organisms that are resource limited and things like that.
*  Any kind of hardware neuron is almost certainly going to be much bigger than that.
*  If it is of comparable complexity, even whether it's based on silicon transistors.
*  Okay, a transistor seven nanometers.
*  That doesn't mean a semiconductor based neuron is seven nanometers.
*  They're big. They require many transistors, different other things like capacitors and things that store charge.
*  They end up being on the order of 100 microns by 100 microns.
*  And it's difficult to get them down any smaller than that.
*  The same is true for superconducting neurons.
*  And the same is true if we're trying to use light for communication.
*  Even if you're using electrons for communication, you have these wires where, okay, the size of an electron might be angstroms, but the size of a wire is not angstroms.
*  And if you try and make it narrower, the resistance just goes up.
*  So you don't actually win.
*  To communicate over long distances, you need your wires to be microns wide.
*  And it's the same thing for waveguides.
*  Waveguides are essentially limited by the wavelength of light, and that's going to be about a micron.
*  So whereas compare that to an axon, the analogous component in the brain, which is 10 nanometers in diameter, something like that, they're bigger when they need to communicate over long distances.
*  But grappling with the size of these structures is inevitable and crucial.
*  And so in order to make systems of comparable scale to the human brain, by scale here I mean number of interconnected neurons, you absolutely have to be using the third spatial dimension.
*  And that means on the wafer, you need multiple layers of both active and passive components.
*  Active, I mean superconducting electronic circuits that are performing computations.
*  And passive, I mean these waveguides that are routing the optical signals to different places, you have to be able to stack those.
*  If you can get to something like 10 planes of each of those, or maybe not even 10, maybe five, six, something like that, then you're in business.
*  Now you can get millions of neurons on a wafer.
*  But that's not anywhere close to the brain scale.
*  In order to get to the scale of the human brain, you're going to have to also use the third dimension in the sense that entire wafers need to be stacked on top of each other with fiber optic connections.
*  And that's where you need to have the communication between them.
*  And we need to be able to fill a space the size of this table with stacked wafers.
*  And that's when you can get to some 10 billion neurons like your human brain.
*  And I don't think that's specific to the optoelectronic approach that we're taking.
*  I think that applies to any hardware where you're trying to reach commensurate scale and complexity as the human brain.
*  So you need that fractal stacking.
*  Stacking on the wafer and stacking of the wafers and then whatever the system that combined this stacking of the tables with the wafers.
*  And it has to be fractal all the way. You're exactly right.
*  Because that's the only way that you can efficiently get information from a small point to across that whole network.
*  It has to have the power law connected.
*  And photons are like optics throughout.
*  Yeah, absolutely. Once you're at this scale, to me, it's just obvious. Of course you're using light for communication.
*  You have fiber optics given to us from nature so simple.
*  The thought of even trying to do any kind of electrical communication just doesn't make sense to me.
*  I'm not saying it's wrong. I don't know. But that's where I'm coming from.
*  So let's return to loop neurons. Why are they called loop neurons?
*  Yeah, the term loop neurons comes from the fact, like we've been talking about, that they rely heavily on these superconducting loops.
*  So even in a lot of forms of digital computing with superconductors, storing a signal in a superconducting loop is a primary technique.
*  In this particular case, it's just loops everywhere you look.
*  So the strength of a synaptic weight is going to be set by the amount of current circulating in a loop that is coupled to the synapse.
*  So memory is implemented as current circulating in a superconducting loop.
*  The coupling between, say, a synapse and a dendrite or a synapse in the neuron cell body occurs through loop coupling through transformers.
*  So current circulating in a synapse is going to induce current in a different loop, a receiving loop in the neuron cell body.
*  So since all of the computation is happening in these flux storage loops and they play such a central role in how the information is processed, how memories are formed, all that stuff,
*  I didn't think too much about it. I just called them loop neurons because it rolls off the tongue a little bit better than superconducting optoelectronic neurons.
*  OK, so how do you design circuits for these loop neurons?
*  That's a great question. There's a lot of different scales of design.
*  So at the level of just one synapse, you can use conventional methods.
*  They're not that complicated as far as superconducting electronics goes.
*  It's just four Josephson junctions or something like that, depending on how much complexity you want to add.
*  So you can just directly simulate each component in SPICE.
*  What's SPICE?
*  It's standard electrical simulation software.
*  So you're just explicitly solving the differential equations that describe the circuit elements.
*  And then you can stack these things together in that simulation software to then build circuits.
*  You can, but that becomes computationally expensive.
*  So one of the things when COVID hit, we knew we had to turn some attention to more things you can do at home in your basement or whatever.
*  And one of them was computational modeling.
*  So we started working on adapting, abstracting out the circuit performance so that you don't have to explicitly solve the circuit equations,
*  which for Josephson junctions usually needs to be done on like a picosecond timescale.
*  And you have a lot of nodes in your circuit.
*  So it results in a lot of differential equations that need to be solved simultaneously.
*  We were looking for a way to simulate these circuits that is scalable up to networks of millions or so neurons is sort of where we're targeting right now.
*  So we were able to analyze the behavior of these circuits.
*  And as I said, it's based on these simple building blocks.
*  So you really only need to understand this one building block.
*  And if you get a good model of that, boom, it tiles.
*  And you can change the parameters in there to get different behaviors and stuff.
*  But it's all based on now it's one differential equation that you need to solve.
*  So one differential equation for every synapse, dendrite or neuron in your in your system.
*  And for the neuroscientists out there, it's just a simple leaky integrated fire model, leaky integrator.
*  Basically, the synapse is a leaky integrator.
*  A dendrite is a leaky integrator.
*  So I'm really fascinated by how this one simple component can be used to achieve lots of different types of dynamical activity.
*  And to me, that's where scalability comes from.
*  And also complexity as well.
*  Complexity is often characterized by relatively simple building blocks connected in potentially simple or sometimes complicated ways.
*  And then emergent new behavior that was hard to predict from those simple simple elements.
*  And that's exactly what we're working with here.
*  So it's a very exciting platform, both from a modeling perspective and from a hardware manifestation perspective,
*  where we can hopefully start to have this test bed where we can explore things not just related to neuroscience,
*  but also related to other things that connected to other physics like critical phenomenon, Ising models, things like that.
*  So you were asking how we simulate these circuits.
*  It's at different levels.
*  And we've got the simple SPICE circuit stuff.
*  That's no problem.
*  And now we're building these network models based on this more efficient leaky integrator.
*  So we can actually reduce every element to one differential equation.
*  And then we can also step through it on a much coarser time grid.
*  So it ends up being something like a factor of a thousand to ten thousand speed improvement,
*  which allows us to simulate, but hopefully up to up to millions of neurons.
*  Whereas before we would have been limited to tens, a hundred, something like that.
*  And just like simulating quantum mechanical systems with a quantum computer.
*  So the goal here is to understand such systems.
*  For me, the goal is to study this as a scientific physical system.
*  I'm not drawn towards turning this into an enterprise at this point.
*  Short term applications that obviously make a lot of money is not necessarily a curiosity driver for you at the moment.
*  Absolutely not.
*  If you're interested in short term making money, go with deep learning.
*  Use silicon microelectronics.
*  If you want to understand things like the physics of a fascinating system,
*  or if you want to understand something more along the lines of the physical limits of what can be achieved,
*  then I think single photon communication, superconducting electronics is extremely exciting.
*  What if I want to use superconducting hardware at four Kelvin to mine Bitcoin?
*  That's my main interest.
*  That's the reason I wanted to talk to you today.
*  I want us not.
*  I don't know.
*  What's Bitcoin?
*  It's a look it up on the Internet.
*  Somebody somebody told me about it.
*  I'm not sure exactly what it is.
*  But let me ask nevertheless about applications to machine learning.
*  Okay.
*  So what like if you look at the scale of five, 10, 20 years, is it possible to before we understand the nature of human intelligence and general intelligence,
*  do you think we'll start falling out of this exploration of neuromorphic systems ability to solve some of the problems that the machine learning systems of today can't solve?
*  I'm I'm really hesitant to over promise.
*  So I really don't know.
*  I also I don't really understand machine learning in a lot of senses.
*  I mean, machine learning from my perspective appears to require that you know precisely what your input is and also what your goal is.
*  You usually have some objective function or something like that.
*  And that's just that's very limiting.
*  I mean, of course, a lot of times that that's the case.
*  You know, there's a there's a picture and there's a horse in it.
*  So you've done.
*  But that's not a very interesting problem.
*  I think when I when I think about intelligence, it's it's almost defined by the ability to handle problems where you don't know what your inputs are going to be.
*  And you don't even necessarily know what you're trying to accomplish.
*  I mean, I'm not sure what I'm trying to accomplish in this world.
*  But at all scales.
*  Yeah, at all scales.
*  Right.
*  I mean, so and sometimes so I'm more drawn to the underlying phenomena, the the critical dynamics of this of this system, trying to understand how elements that you build into your hardware result in emergent, fascinating activity that was very difficult to predict, things like that.
*  But but but I but I got to be really careful because I think a lot of other people who if they found themselves working on this project in my shoes, they would say, all right, what are what are all the different ways we can use this for machine learning?
*  Actually, let me let me just definitely mention colleague at NIST, Mike Schneider.
*  He's also very much interested, particularly in the superconducting side of things, using the incredible speed power efficiency.
*  Also, Ken Seagal at Colgate, other people working on specifically the superconducting side of this for machine learning and deep feed forward neural networks there.
*  The advantages are obvious.
*  It's extremely fast.
*  So that's less on the nature of intelligence and more on various characteristics of this hardware.
*  Right.
*  You can use for the basic computations we know today.
*  Yeah.
*  And communication.
*  One of the things that Mike Schneider is working on right now is an image classifier at a relatively small scale.
*  I think he's targeting that nine pixel problem where you can have three different characters and you just you put in a nine pixel image and you classify it as one of these three three categories.
*  And that's going to be really interesting to see what happens there, because if you can show that even at that scale, you just put these images in and you get it out and you can.
*  He thinks he can do it.
*  I forgot if it's a nanosecond or some extremely fast classification time.
*  It's probably less.
*  It's probably under picoseconds or something there.
*  You have challenges, though, because the Joseph's injunctions themselves, the electronic circuit is extremely power efficient.
*  Some orders of magnitude for something more than a than a transistor doing the same thing.
*  But when you have to cool it down to four Kelvin, you pay a huge overhead just for keeping it cold, even if it's not doing anything.
*  So.
*  It's you.
*  It has to work at big at large scale in order to overcome that power penalty.
*  But that's possible.
*  It's just it's going to have to get that performance.
*  And this is sort of what you're asking about before is like how much better than silicon would it need to be?
*  And the answer is, I don't know.
*  I think if it's if it's just overall better than silicon at a problem that a lot of people care about, maybe it's image classification, maybe it's facial recognition.
*  Maybe it's monitoring credit transactions.
*  I don't know.
*  Then I think it will have a place.
*  It's not going to be in your cell phone, but it could be in your data center.
*  So what about in terms of the data center?
*  I don't know if you're paying attention to the various systems like Tesla recently announced Dojo, which is a large scale machine learning training system that, again, the bottleneck there is probably going to be communication between those systems.
*  Is there something from your work on the everything we've been talking about in terms of superconductive hardware that could be useful there?
*  Oh, I mean, I OK.
*  Tomorrow? No.
*  In the long term, it could be the whole thing.
*  It could be nothing. I don't know.
*  But definitely, definitely.
*  When you look at the so I don't know that much about Dojo.
*  My understanding is that that's new, right?
*  That's just you just coming online.
*  Well, I don't even know where it hasn't come online.
*  And when you announce big sexy.
*  So let me explain to you the way things work in the world out there in the word of business and marketing.
*  It's not always clear where you are on the coming online part of that.
*  So I don't know where they are exactly.
*  But the vision is from ground up to build a very, very large scale modular machine learning basic basically hardware that's optimized for training neural networks.
*  And of course, there's a lot of companies that are small and big working on this kind of problem.
*  The question is how to do it in a modular way that has very fast communication.
*  The interesting aspect of Tesla is you have a company that at least at this time is so singularly focused on solving a particular machine learning problem and is making obviously a lot of money doing so because the machine learning problem happens to be involved with autonomous driving.
*  So you have a system that's driven by an application.
*  And that's really interesting because you know, you have maybe Google working on TPUs and so on.
*  You have all these other companies with ASICs.
*  They're usually more kind of always thinking general.
*  So I like it when it's driven by a particular application because then you can really get to the it's like.
*  It's somehow if you just talk broadly about intelligence, you may not always get to the right solutions.
*  It's nice to couple that sometimes a specific clear illustration of something that requires general intelligence, which for me driving is one such case.
*  I think you're exactly right.
*  Sometimes just having that focus on that application brings a lot of people focuses their energy and attention.
*  I think that so one of the things that's appealing about what you're saying is not just that the application is specific, but also that the scale is big, big, and that the benefit is is also huge.
*  So financial and humanity.
*  Right, right, right.
*  Yeah, so I guess let me just try to understand is the point of this dojo system to figure out the the parameters that then plug into neural networks and then you don't need to retrain you.
*  You just make copies of a certain chip that has all the other parameters established or no, it's straight up retraining a large neural network over and over and over.
*  So you have to do it once for every new car.
*  No, no, you have to.
*  So they do this interesting process, which I think is a process for machine learning supervised machine learning systems.
*  You're going to have to do, which is you have a system, you train your network once.
*  It takes a long time.
*  I don't know how long, but maybe a week.
*  Okay, the train.
*  And then you deploy it on, let's say, about a million cars.
*  I don't know what the numbers that part you just write software that updates some weights in a table.
*  And yeah, okay.
*  But there's a loop back.
*  Yeah, yeah.
*  Each of those cars run into trouble rarely.
*  But like they they they catch the edge cases of the performance of that particular system and then send that data back and either automatically or by humans.
*  That weird edge case data is annotated and then the network has to become smart enough to now be able to perform in those edge cases.
*  So it has to get retrained.
*  There's clever ways of retraining different parts of that network.
*  But for the most part, I think they prefer to retrain the entire thing.
*  So you have this giant monster that kind of has to be retrained regularly.
*  I think the vision with the dojo is to have a very large machine learning focused driving focused supercomputer that then is sufficiently modular.
*  That could be scaled to other machine learning applications.
*  But like so they're not limiting themselves completely to this particular application.
*  But this application is the way they kind of test this iterative process of machine learning is you make a system that's very dumb.
*  Deploy it. Get the edge cases where it fails.
*  Make it a little smarter.
*  It becomes a little less dumb.
*  And that where that iterative process achieved something that you can call intelligent or is smart enough to be able to solve this particular application.
*  So it has to do with training neural networks fast and training neural networks that are large.
*  But also based on an extraordinary amount of diverse input data.
*  And that's one of the things.
*  So this does seem like one of those spaces where the scale of superconducting optoelectronics, the way that you so when you talk about the weaknesses, like I said, OK, well, you have to cool it down at this scale.
*  That's fine. That's because that's not that's not an too much of an added cost.
*  Most of your power is being dissipated by the circuits themselves, not the cooling.
*  And also you have one centralized kind of cognitive hub, if you will.
*  And so when if we're talking about putting a superconducting system in a car, that's a that's questionable.
*  Do you really want to cryostat in the trunk of everyone in your car?
*  It'll fit. It's not that big of a deal.
*  But hopefully there's a better way. Right.
*  But since this is sort of a central supreme intelligence or something like that and it's it needs to really have this massive data acquisition, massive data integration, I would think that that's where large scale spiking neural networks with vast communication and all these things would would have something pretty tremendous to offer.
*  It's not going to happen tomorrow.
*  There's a lot of development that needs to be done.
*  But, you know, we have to be patient with self-driving cars for a lot of reasons.
*  We were all optimistic that they would be here by now.
*  And, OK, they are to some extent.
*  But if we're thinking five or ten years down the line, it's it's not unreasonable.
*  One other thing I'll just let me just mention that getting into self-driving cars and technologies that are using A.I. out in the world, this is something NIST cares a lot about.
*  Elham Tabassi is leading up a much larger effort in A.I. at NIST than than my my little project.
*  And really central to that mission is this concept of trustworthiness.
*  So when you're going to deploy this neural network in every single automobile with so much on the line, you have to be able to trust that.
*  So how do we know? How do we know that we can trust that?
*  How do we know that we can trust the self-driving car or the the supercomputer that that trained it?
*  There's a lot of work there and there's a lot of that going on at NIST and still early days.
*  I mean, you're familiar with the problem and all that.
*  But there's a fascinating dance in engineering with like safety critical systems.
*  There's a desire in computer science.
*  Just recently talked to Don Knuth to do, you know, for algorithms and for systems for them to be provably correct, provably safe.
*  And, you know, this is one other difference between humans and biological systems is we're not provably anything.
*  Right. Right. And so there's some aspect of imperfection.
*  Yes. That we need to have built in like robustness to imperfection be part of our systems.
*  Which is a difficult thing for engineers to contend with.
*  They're very uncomfortable with the idea that you have to be OK with failure and almost engineer failure into the system.
*  Mathematicians hate it, too.
*  But I think it was I think it was Turing who said something along the lines of I can give you an intelligent system or I can give you a flawless system, but I can't give you both.
*  And it's in sort of creativity and abstract thinking seem to rely somewhat on stochasticity and not having components that perform exactly the same way every time.
*  This is where like the disagreement I have with not disagreement, but a different view on the world.
*  I'm with Turing. When I talk to robotic robot colleagues, that sounds like I'm talking to robots, colleagues that are roboticists.
*  The goal is perfection. And to me is like, no, I think the goal should be imperfection that's communicated.
*  And through the interaction between humans and robots, that imperfection becomes a feature, not a bug.
*  Right. Like together as a scene as a system, the human and the robot together are better than either of them individually.
*  But the robot itself is not perfect in any way.
*  Of course, there's a bunch of disagreements, including with Mr.
*  Elon about to me, autonomous driving is fundamentally a human robot interaction problem, not a robotics problem.
*  To Elon, it's a robotics problem. That's actually an open and fascinating question, whether humans can be removed from the loop completely.
*  We've talked about a lot of fascinating chemistry and physics and engineering, and we're always running up against this issue that nature seems to dictate what's easy and what's hard.
*  So you have this cool little paper that I'd love to just ask you about.
*  It's titled Does Cosmological Evolution Select for Technology?
*  So in physics, there is parameters that seem to define the way our universe works, that physics works, that if it worked any differently, we would get a very different world.
*  So it seems like the parameters are very fine tuned to the kind of physics that we see.
*  All the beautiful equals MC squared that would get these nice, beautiful laws. It seems like very fine tune for that.
*  So what you argue in this article is it may be that the universe is also fine tuned its parameters that enable the kind of technological innovation that we see, that technology that we see.
*  Can you explain this idea?
*  Yeah, I think you've introduced it nicely. Let me just try to say a few things in my language.
*  Lay out what is this fine tuning problem. So physicists have spent centuries trying to understand the system of equations that govern the way nature behaves, the way particles move and interact with each other.
*  And as that understanding has become more clear over time, it became sort of evident that it's all well adjusted to allow a universe like we see, very complex, this large, long-lived universe.
*  And so one answer to that is, well, of course it is because we wouldn't be here otherwise. But I don't know, that's not very satisfying.
*  That's sort of that's what's known as the weak anthropic principle. It's a statement of selection bias. We can only observe a universe that is fit for us to live in.
*  So what does it mean for a universe to be fit for us to live in? Well, the pursuit of physics is based partially on coming up with equations that describe how things behave and interact with each other.
*  But in all those equations you have, so there's the form of the equation, sort of how different fields or particles move in space and time.
*  But then there are also the parameters that just tell you sort of the strength of different couplings, how strongly does a charged particle couple to the electromagnetic field or masses, how strongly does a particle couple to the Higgs field or something like that.
*  And those parameters that define not the general structure of the equations, but the relative importance of different terms, they seem to be every bit as important as the structure of the equations themselves.
*  And so I forget who it was, somebody when they were working through this and trying to see, okay, if I adjust the parameter, this parameter over here, call it the, say, the fine structure constant, which tells us the strength of the electromagnetic interaction.
*  Oh boy, I can't change it very much. Otherwise, nothing works. The universe sort of doesn't, it just pops into existence and goes away in a nanosecond or something like that.
*  And somebody had the phrase, this looks like a put up job, meaning every one of these parameters was dialed in.
*  It's arguable how precisely they have to be dialed in, but dialed in to some extent, not just in order to enable our existence. That's a very anthropocentric view, but to enable a universe like this one.
*  So, okay, maybe I think the majority position of working physicists in the field is it has to be that way in order for us to exist.
*  And so, if we're here, we shouldn't be surprised that that's the way the universe is. And I don't know, for a while that never sat well with me, but I just kind of moved on because there are things to do and a lot of exciting work.
*  It doesn't depend on resolving this puzzle, but as I started working more with technology, getting into the more recent years of my career, particularly when I started after having worked with silicon for a long time, which was kind of eerie on its own.
*  But then when I switched over to superconductors, just like this is crazy. It's just absolutely astonishing that our universe gives us superconductivity. It's one of the most beautiful physical phenomena, and it's also extraordinarily useful for technology.
*  So you can argue that the universe has to have the parameters it does for us to exist because we couldn't be here otherwise. But why does it give us technology? Why does it give us silicon that has this ideal oxide that allows us to make a transistor without trying that hard?
*  That can't be explained by the same anthropic reasoning.
*  Yeah, so it's asking the why question. I mean, a slight natural extension of that question is I wonder if the parameters were different, if we would simply have just another set of paint brushes to create totally other things that wouldn't look like anything like the technology of today, but would nevertheless have incredible complexity.
*  Which is if you sort of zoom out and start defining things, not by how many batteries it needs and whether it can make toast, but more like how much complexity is within the system or something like that.
*  Right. Well, yeah, you can start to quantify things. You're exactly right. So nowhere am I arguing that in all of the vast parameter space of everything that could conceivably exist in the multiverse of nature, there is this one point in parameter space where complexity arises.
*  I doubt it. That would be a shameful waste of resources.
*  Yeah.
*  But it might be that we reside at one place in parameter space that has been adapted through an evolutionary process to allow us to make certain technologies that allow our particular kind of universe to arise and sort of achieve the things it does.
*  See, I wonder if nature in this kind of discussion, if nature is a catalyst for innovation or if it's a ceiling for innovation. So like, is it going to always limit us? Like you're talking about silicon.
*  Is it just make it super easy to do awesome stuff in a certain dimension, but we could still do awesome stuff in other ways. It'll just be harder or is it doesn't really set like the maximum we can do.
*  That's a good thing. That's a good subject to discuss. I guess I feel like we need to lay a little bit more groundwork. So I want to make sure that I introduce this in the context of Lee Smolin's previous idea.
*  So who is Lee Smolin and what kind of ideas does he have?
*  Lee Smolin is a theoretical physicist who back in the late 1980s published a paper in the early 1990s introduced this idea of cosmological natural selection, which argues that the universe did evolve.
*  So his paper was called Did the Universe Evolve? And I gave myself the liberty of titling my paper, Does Cosmological Evolution Select for Technology in reference to that.
*  So he introduced that idea decades ago. Now he primarily works on quantum gravity, loop quantum gravity, other approaches to unifying quantum mechanics with general relativity, as you can read about in his most recent book, I believe, and he's been on your show as well.
*  So but I want to introduce this idea of cosmological natural selection because I think that is one of the core ideas that could change our understanding of how the universe got here, our role in it, what technology is doing here.
*  But there's a couple more pieces that need to be set up first. So the beginning of our universe is largely accepted to be the Big Bang.
*  And what that means is if you look back in time by looking far away in space, you see that everything used to be at one point, and it expanded away from there.
*  There was an era in the evolutionary process of our universe that was called inflation.
*  And this idea was developed primarily by Alan Guth and others, Andre Lindey and others in the 80s.
*  And this idea of inflation is basically that when a singularity begins this process of growth, there can be a temporary stage where it just accelerates incredibly rapidly.
*  And based on quantum field theory, this tells us that this should produce matter in precisely the proportions that we find of hydrogen and helium in the Big Bang, lithium-2, lithium also, and other things too.
*  So the predictions that come out of Big Bang inflationary cosmology have stood up extremely well to empirical verification, the cosmic microwave background, things like this.
*  So most scientists working in the field think that the origin of our universe is the Big Bang.
*  And I base all my thinking on that as well. I'm just laying this out there so that people understand that where I'm coming from is an extension, not a replacement of existing well-founded ideas.
*  In a paper, I believe it was 1986 with Alan Guth and another author Farhi, they wrote that a Big Bang, I don't remember the exact quote, a Big Bang is inextricably linked with a black hole.
*  This singularity that we call our origin is mathematically indistinguishable from a black hole. They're the same thing.
*  And Lee Smolin based his thinking on that idea, I believe, I don't mean to speak for him, but this is my reading of it.
*  So what Lee Smolin will say is that a black hole in one universe is a Big Bang in another universe.
*  And this allows us to have progeny, offspring. So a universe can be said to have come before another universe.
*  And very crucially, Smolin argues, I think this is potentially one of the great ideas of all time. That's my opinion.
*  That when a black hole forms, it's not a classical entity, it's a quantum gravitational entity.
*  So it is subject to the fluctuations that are inherent in quantum mechanics.
*  The properties, what we're calling the parameters that describe the physics of that system are subject to slight mutations.
*  So that the offspring universe does not have the exact same parameters defining its physics as its parent universe.
*  They're close, but they're a little bit different. And so now you have a mechanism for evolution, for natural selection.
*  So there's mutation. And then if you think about the DNA of the universe or the basic parameters that govern its laws.
*  Exactly. So what Smolin said is our universe results from an evolutionary process that can be traced back some, he estimated, 200 million generations.
*  Initially, there was something like a vacuum fluctuation that produced through random chance a universe that was able to reproduce just once.
*  So now it had one offspring. And then over time, it was able to make more and more until it evolved into a highly structured universe with a very long lifetime,
*  with a great deal of complexity. And importantly, especially importantly for Lee Smolin, stars.
*  Stars make black holes. Therefore, we should expect our universe to be optimized, have its physical parameters optimized to make very large numbers of stars.
*  Because that's how you make black holes and black holes make offspring.
*  So we expect the physics of our universe to have evolved to maximize fecundity, the number of offspring.
*  And the way Lee Smolin argues you do that is through stars that the biggest ones die in these core collapse supernova that make a black hole and a child.
*  OK, first of all, I agree with you that.
*  This is back to our fractal view of everything from intelligence to our universe that is very compelling and a very powerful idea that unites.
*  The origin of life and perhaps the origin of ideas and intelligence.
*  So from a Dawkins perspective here on Earth, the evolution of those and then the evolution of the laws of physics that led to us.
*  I mean, it's beautiful. And then you stacking on top of that, that maybe we are one of the offspring.
*  Right. OK, so before getting into where I'd like to take that idea, let me just a little bit more groundwork.
*  There is this concept of the multiverse and it can be confusing.
*  Different people use the word multiverse in different ways in the multiverse that I think is relevant to picture when trying to grasp Lee Smolin's idea.
*  Essentially, every every vacuum fluctuation can be referred to as a universe.
*  It occurs. It borrows energy from the vacuum for some finite amount of time and it evanesces back into the quantum vacuum.
*  And ideas of Gooth before that and and André Linde with eternal inflation aren't that different that you would expect nature due to the quantum properties of the vacuum, which we know exists.
*  They're measurable through things like the Casimir effect and others.
*  You know that there are these fluctuations that are occurring.
*  What what Smolin is arguing is that there is this extensive multiverse that we this universe, what we can measure and interact with is not unique in nature.
*  It's just our residence. It's where we reside.
*  And there are countless potentially infinity other universes, other entire evolutionary trajectories that have evolved into things like what you were mentioning a second ago with different parameters and different ways of achieving complexity.
*  And reproduction and all that stuff.
*  So it's not that the evolutionary process is a funnel towards this end point.
*  Not at all.
*  Just like the the biological evolutionary process that has occurred within our universe is not a unique route toward achieving one specific chosen kind of species.
*  No, we have extraordinary diversity around us.
*  That's what evolution does.
*  And for any one species like us, it might feel like we're at the center of this process.
*  We're the destination of this process, but we're just one of the many nearly infinite branches of this process.
*  And I suspect it is exactly infinite.
*  I mean, I just can't understand how with this idea you can ever draw a boundary around and say, no, the universe.
*  I mean, the multiverse has 10 to the one quadrillion components, but not infinity.
*  I don't know that.
*  Well, yeah, I have cognitively incapable, as I think all of us are, and truly understanding the concept of infinity and the concept of nothing as well.
*  And nothing.
*  But also the concept of a lot is pretty difficult.
*  I could just I can count.
*  I run out of fingers at a certain point and then you're screwed.
*  And when you're wearing shoes and you can't even get down to your toes, it's like it's like a thousand fine a million.
*  Is that what?
*  And then it gets crazier and crazier.
*  Right, right.
*  So this particular so when we say technology, by the way, I mean, there's some not to over romanticize the thing, but there is some aspect about this branch of ours that allows us to for the universe to know itself.
*  Yes, yes.
*  So to be to have like little conscious cognitive fingers that are able to feel like to scratch the head.
*  Right, right, right.
*  To be able to construct the equals on C squared and to introspect to have to start to gain some understanding of the laws that govern it.
*  Isn't that isn't that kind of amazing?
*  Amazing.
*  OK, I'm just human, but it feels like that if I were to build a system that does this kind of thing that evolves laws of physics, that evolves life, that evolves intelligence, that my goal would be to come up with things that are able to think about itself.
*  Right. Aren't we kind of close to this?
*  The design specs, the destination.
*  We're pretty close.
*  I don't know.
*  I mean, I'm spending my career designing things that I hope will think about themselves.
*  Exactly.
*  You and I aren't too far apart on that one.
*  But then maybe that problem is a lot harder than we imagine.
*  Maybe we need to.
*  Let's not get let's not get too far because I want to emphasize something that what you're saying is, isn't it fascinating that the universe evolved something that can be conscious, reflect on itself.
*  But Lee Smolin's idea didn't take us there.
*  Remember, it took us to stars.
*  Lee Smolin has argued, I think, right on almost every single way that cosmological natural selection could lead to a universe with rich structure.
*  And he argued that the structure, the physics of our universe is designed to make a lot of stars so that they can make black holes.
*  But that doesn't explain what we're doing in order to in order for that to be an explanation of us.
*  What you have to assume is that once you made that universe that was capable of producing stars, life, planets, all these other things were along for the ride.
*  They got lucky.
*  We're we're kind of arising growing up in the cracks.
*  But the universe isn't here for us.
*  We're still kind of a fluke in that picture.
*  And I can't I don't I don't necessarily have like a philosophical opposition to that stance.
*  It's just not OK.
*  So I don't think it's complete.
*  So it seems like whatever we got going on here to you, it seems like whatever we have here on Earth seems like a thing you might want to select for in this whole big process.
*  Exactly.
*  So if what you are truly if your entire evolutionary process only cares about fecundity, it only cares about making offspring universes, because then there's going to be the most of them in that local region of hyperspace, which is the set of all possible universes.
*  Let's let's say you don't care how those universes are made.
*  You know they have to be made by black holes.
*  This is what this is what inflationary theory tells us.
*  The Big Bang tells us that black holes make universes.
*  But what if there was a technological means to make universes?
*  Stars require a ton of matter because they're they're not thinking very carefully about how you make a black hole.
*  They're just using gravity.
*  But if we devise technologies that can efficiently compress matter into a singularity, it turns out that if you can compress about 10 kilograms into a very small volume, that will make a black hole that is likely highly probable to inflate into its own offspring universe.
*  This is according to calculations done by other people who are professional quantum theorists, quantum field theorists.
*  And I hope I am grasping what they're telling me correctly.
*  I'm somewhat of a translator here.
*  But so that's that's the position that is particularly intriguing to me, which is that what might have happened is that, OK, this particular branch on the vast tree of evolution, cosmological evolution that we're talking about, not biological evolution within our universe, but cosmological evolution went through exactly the process that at least Mullen described.
*  And so we got to the stage where stars were making lots of black holes, but then continued to evolve and somehow bridge that gap and made intelligence and intelligence capable of devising technologies because technologies.
*  So intelligent species working in conjunction with technologies could then produce even more more efficiently, more like faster and better and more different.
*  Then you start to have different kind of mechanisms and mutation, perhaps all that kind of stuff.
*  And so if you do a simple calculation that says, all right, if I want to, we know roughly how many core collapse supernova supernovae have resulted in black holes in our galaxy since the beginning of the universe.
*  And it's something like a billion.
*  So then you would have to estimate that it would be possible for a technological civilization to produce more than a billion black holes with the energy and matter at their disposal.
*  And so one of the calculations in that paper back of the envelope, but I think revealing nonetheless, is that if you take a relatively common asteroid, something that's about a kilometer in diameter, what I'm thinking of is just scrap material laying around in our solar system and break it up into 10 kilogram chunks and turn each of those into a universe.
*  Then you would have made at least a trillion black holes outpacing the star production rate by some three orders of magnitude.
*  That's one asteroid.
*  So now if you envision an intelligent species that would potentially have been devised initially by humans, but then based on superconducting optoelectronic networks, no doubt.
*  And they go out and populate.
*  They don't, they don't have to fill the galaxy.
*  They just have to get out to the asteroid belt.
*  They could potentially dramatically outpace the rate at which stars are producing offspring universes.
*  And then wouldn't you expect that that's where we came from instead of a star?
*  Yeah.
*  So you have to somehow become masters of gravity.
*  So like what or generally gravity.
*  So stars make black holes with gravity.
*  But any force that can make the energy density can compactify matter to produce a great enough energy density can form a singularity.
*  It doesn't, it would not likely be gravity.
*  It's the weakest force.
*  You're more likely to use something like the technologies that we're developing for fusion, for example.
*  So I don't know.
*  The large ignition facility recently blasted a pellet with a hundred really bright lasers and caused that to get dense enough to engage in nuclear fusion.
*  So something more like that or a tokamak with a really hot plasma.
*  I'm not sure something I don't know exactly how it would be done.
*  I do like the idea that especially just been reading a lot about gravitational waves and the fact that us humans with our technological capabilities,
*  one of the most impressive technological accomplishments of human history is LIGO being able to precisely detect gravitational waves.
*  I particularly find appealing the idea that other alien civilizations from very far distances communicate with gravity,
*  with gravitational waves, because as you become greater and greater master of gravity, which seems way out of reach for us right now,
*  maybe that seems like an effective way of sending signals, especially if your job is to manufacture black holes.
*  Right.
*  So that that so let me ask there.
*  Whatever I mean, broadly thinking, because we tend to think other alien civilizations would be very human like.
*  But if we think of alien civilizations out there as basically generators of black holes, however they do it, because they go stars.
*  Do you think there's a lot of them in our particular universe out there?
*  In our universe?
*  Well, OK, let me ask. OK, this is great.
*  Let me ask a very generic question and then let's see how you answer it, which is how many alien civilizations are out there?
*  If the hypothesis that I just described is on the right track,
*  it would mean that the parameters of our universe have been selected so that intelligent civilizations will occur in sufficient numbers,
*  so that if they reach something like supreme technological maturity, let's define that as the ability to produce black holes,
*  then that's not a highly improbable event.
*  It doesn't need to happen often because, as I just described, if you get one of them in a galaxy,
*  you're going to make more black holes than the stars in that galaxy.
*  But there's also not a super strong motivation.
*  Well, it's not obvious that you need them to be ubiquitous throughout the galaxy.
*  So one of the things that I try to emphasize in that paper is that given this idea of how our parameters might have been selected,
*  it's clear that it's a series of tradeoffs, right?
*  I mean, in order for intelligent life of our variety or anything resembling us to occur, you need a bunch of stuff.
*  You need stars. So that's right back to Smolin's roots of this idea.
*  But you also need water to have certain properties.
*  You need things like the rocky planets like the Earth to be within the habitable zone,
*  all these things that you start talking about in the field of astrobiology, trying to understand life in the universe.
*  But you can't over-emphasize, you can't tune the parameters so precisely to maximize the number of stars
*  or to give water exactly the properties or to make rocky planets like Earth the most numerous.
*  You have to compromise on all these things.
*  And so I think the way to test this idea is to look at what parameters are necessary for each of these different subsystems.
*  And I've laid out a few that I think are promising there could be countless others and see how changing the parameters makes it more or less likely
*  that stars would form and have long lifetimes or that rocky planets in the habitable zone are likely to form, all these different things.
*  So we can test how much these things are in a tug of war with each other.
*  And the prediction would be that we kind of sit at this central point where if you move the parameters too much,
*  stars aren't stable or life doesn't form or technology is infeasible.
*  Because life alone, at least the kind of life that we know of, cannot make black holes.
*  We don't have the – well, I'm speaking for myself.
*  You're a very fit and strong person.
*  But it might be possible for you, but not for me to compress matter.
*  So we need these technologies, but we don't know – we have not been able to quantify yet how finely adjusted the parameters would need to be in order for silicon to have the properties it does.
*  Okay, this is not directly speaking to what you're saying.
*  You're getting to the Fermi paradox, which is where are they?
*  Where are the life forms out there?
*  How numerous are they? That sort of thing.
*  What I'm trying to argue is that if this framework is on the right track, a potentially correct explanation for our existence,
*  it doesn't necessarily predict that intelligent civilizations are just everywhere.
*  Because even if you just get one of them in a galaxy, which is quite rare,
*  it could be enough to dramatically increase the fecundity of the universe as a whole.
*  Yeah, and I wonder, once you start generating the offspring for universes, black holes,
*  how that has effect on the – what kind of effect does it have on the other candidates, civilizations within that universe?
*  Maybe as a destructive aspect, or there could be some arguments about once you have a lot of offspring,
*  that that just quickly accelerates to where the other ones can't even catch up.
*  It could, but I guess if you want me to put my chips on the table or whatever,
*  I think I come down more on the side that intelligent life civilizations are rare.
*  I guess I follow Max Tegmark here.
*  Also, there's a lot of papers coming out recently in the field of astrobiology that are seeming to say,
*  all right, you just work through the numbers on some modified Drake equation or something like that.
*  It looks like it's not improbable.
*  You shouldn't be surprised that an intelligent species has arisen in our galaxy,
*  but if you think there's one the next solar system over, it's highly improbable.
*  I can see that the probability of finding a civilization in a galaxy,
*  maybe it's most likely that you're going to find one to a hundred or something.
*  But okay, now it's really important to put a time window on that, I think,
*  because does that mean in the entire lifetime of the galaxy before it – so for in our case, before we run into Andromeda?
*  I think it's highly probable – I shouldn't say I think.
*  It's tempting to believe that it's highly probable that in that entire lifetime of your galaxy,
*  you're going to get at least one intelligent species, maybe thousands or something like that.
*  But it's also, I think, a little bit naive to think that they're going to coincide in time and we'll be able to observe them.
*  And also, if you look at the span of life on Earth, the Earth history,
*  it was surprising to me to kind of look at the amount of time – first of all, the short amount of time there's no life is surprising.
*  Life sprang up pretty quickly.
*  Cellular, single cell –
*  But that's the point I'm trying to make is like so much of life on Earth was just like single cell organisms.
*  Like most of it. Most of it was like boring bacteria type of stuff.
*  Well, bacteria are fascinating, but I take your point.
*  No, I get it. I mean, no offense to them.
*  This kind of speaking from the perspective of your paper of something that's able to generate technology as we kind of understand it,
*  that's a very short moment in time relative to that full history of life on Earth.
*  And maybe our universe is just saturated with bacteria like humans,
*  but not the special extra AGI super humans.
*  That those are very rare. And once those spring up, everything just goes to like it accelerates very quickly.
*  Yeah, it's it's we just don't have enough data to really say, but I find this whole subject extremely engaging.
*  I mean, there's this concept I think it's called the rare Earth hypothesis, which is that basically stating that, okay,
*  microbes were here right away after the Hadean era where we were being bombarded.
*  Well, after yet bombarded by comets, asteroids, things like that, and also after the moon formed.
*  So once things settled down a little bit in a few hundred million years, you have microbes everywhere.
*  And it could have been we don't know exactly when it could have been remarkably brief that that took.
*  So it does indicate that, OK, life forms relatively easily.
*  I think that alone is sort of a checker on the scale for the argument that.
*  The parameters that allow even microbial life to form are not just a fluke.
*  But anyway, that aside, yes, then there was this long dormant period, not dormant.
*  Things were happening, but important things were happening for some two and a half billion years or something.
*  And then after the metabolic process that releases oxygen was developed,
*  then basically the planet is just sitting there getting more and more oxygenated, more and more oxygenated
*  until it's enough that you can build these large complex organisms.
*  And so the rare Earth hypothesis would argue that.
*  The microbes are common in everywhere in any planet that's like roughly in the habitable zone and has some water on it.
*  It's probably going to have those.
*  But then getting to this Cambrian explosion that happened some between five and six hundred million years ago, that's that's rare.
*  You know, and I buy that. I think that is rare.
*  So if you say how much life is in our galaxy, I think that's probably the right answer is that microbes are everywhere.
*  Cambrian explosion is extremely rare.
*  And then but the Cambrian explosion kind of went like that, where within a couple of tens or a hundred million years,
*  all of these body plans came into existence and basically all of the body plans that are now in existence on the planet were formed in that brief window.
*  And we've just been shuffling around since then.
*  So then what what caused humans to pop out of that?
*  I mean, that could be another extremely rare threshold that a planet roughly in the habitable zone with water is not guaranteed to cross.
*  You know, to me, it's fascinating for being humble, like the humans cannot possibly be the most amazing thing that such if you look at the entirety of the system,
*  that Lee Smolin you paint, that cannot possibly be the most amazing thing that process generates.
*  So like if you look at the evolution, what's the equivalent in the cosmological evolution and its selection for technology,
*  the equivalent of the human eye or the human brain, universes that are able to do some like they don't need the damn stars.
*  They dare able to just do some incredible generation of complexity fast on like much more than if you think about it.
*  If you think about it, it's like most of our universe is pretty freaking boring.
*  There's not much going on as a few rocks flying around and there's some like apes that are just like doing podcasts on some weird on some weird planet.
*  It just seems very inefficient.
*  If you think about like the amazing thing, the human eye, the visual cortex can do the the brain, the nervous, everything that makes us more powerful than single cell organisms.
*  There's an equivalent of that for universes.
*  They're like the richness of physics that could be that could be expressed through a particular set of parameters.
*  Like, I mean, that like for me, I'm so from a computer science perspective, huge fan of cellular automata,
*  is a nice sort of pretty visual way to illustrate how different laws can result in drastically different levels of complexity.
*  So like it's like, yeah, OK, so we're all like celebrating.
*  Look, our little cellular automata is able to generate pretty triangles and squares, and therefore we achieve general intelligence.
*  And then there'll be like some badass Chuck Norris type like universal Turing machine type of cellular automata.
*  They're able to generate other cellular automata that does any arbitrary level of computation off the bat.
*  It like those have to then exist.
*  And then we're just like this.
*  We're just we'll be forgotten is this story.
*  This is this podcast just entertains a few other apes for a few months.
*  Well, I'm kind of surprised to hear your cynicism.
*  No, I'm very I usually think of you as like one who celebrates humanity and all its forms and things like that.
*  And I guess I just I don't I see it the way you just described.
*  I mean, OK, we've been here for thirteen point seven billion years and you're saying, gosh, that's a long time.
*  Let's get on with the show already.
*  I mean, I think the universe could have kicked our butt by now.
*  But that's putting a characteristic time in.
*  Why is thirteen point seven billion a long time?
*  I mean, compared to compared to what I guess.
*  So when I look at our universe, I see this extraordinary hierarchy that has developed over that time.
*  So at the beginning, it was a chaotic mess of, you know, some plasma and nothing interesting going on there.
*  And even for the first stars to form that a lot of really interesting evolutionary processes had to occur by evolutionary.
*  In that sense, I just mean taking place over extended periods of time and structures are forming then.
*  And then it took that first generation of stars in order to produce the metals that that then can more efficiently produce another generation of stars.
*  We're only the third generation of stars, so we might still be pretty quick to the to the game here.
*  So but I don't think I don't.
*  OK, so then so then you have these stars and you have solar systems on those solar systems.
*  You have rocky worlds, you have gas giants, like all this complexity.
*  And then you start getting life and the the complexity that's evolved through the evolutionary process in life forms is just it's not a letdown to me.
*  No, no. And there's some of it is like some of some of the planets is like I see it's like different flavors of ice cream.
*  They're icy, but there might be water and all kinds of life forms, some volcanoes, all kinds of weird stuff.
*  No, no, I don't. I think it's beautiful. I think our life is beautiful.
*  And I think it was designed that by by design, the scarcity of the whole thing.
*  I think mortality, as terrifying as it is, is fundamental to the whole reason we enjoy everything.
*  No, I think it's beautiful. I just think that all of us conscious beings in the grand scheme of basically every at every scale will be completely forgotten.
*  Well, that's true. I think everything is transient.
*  And that would go back to maybe something more like Lao Tzu, the Tao Te Ching or something where it's like, yes, there is nothing but change.
*  There is nothing but emergence and dissolve. And that's it.
*  But I just in this picture, this hierarchy that's developed, I don't mean to say that now it gets to us and that's the pinnacle.
*  In fact, I think at a high level, the story I'm trying to tease out in my research is about, OK, well, so then what's the next level of hierarchy?
*  And if it's OK, we're we're kind of pretty smart.
*  I mean, talking about people like Lee Small and Alan Gooth, Max Tegmark.
*  OK, we're really smart talking about me. OK, we're kind of we can find our way to the grocery store or whatever.
*  But sometimes. But what's next?
*  You know, I mean, what if what if there's another level of hierarchy that grows on top of us that is even more profoundly capable?
*  And I mean, we've talked a lot about superconducting sensors.
*  Imagine these cognitive systems far more capable than us residing somewhere else in the solar system off of the surface of the Earth, where it's much darker, much colder, much more naturally suited to them.
*  And they have these sensors that can detect single photons of light from radio waves out to all across the spectrum to gamma rays and just see the whole universe.
*  And they just live in space with these massive collection optics so that they what what do they do?
*  They just look out and experience that that vast array of of what's being developed.
*  And if you're such a system, presumably you would do some things for fun.
*  And the kind of fun thing I would do as somebody who likes video games is I would create and maintain and observe something like Earth.
*  And so in some sense, we're like all what players on a stage for this superconducting cold computing system out there.
*  I mean, all of this is fascinating to think the fact that you're actually designing systems here on Earth, they're trying to push this technological at the very cutting edge and also thinking about how does the like the evolution of physical laws lead us to the way we are.
*  It's fascinating that that coupling is fascinating.
*  It's like the ultimate rigorous application of philosophy to the rigorous application of engineering.
*  So I Jeff, you're one of the most fascinating.
*  I'm so glad I did not know much about you except through your work.
*  And I'm so glad we got this chance to talk here.
*  You're one of the best explainers of exceptionally difficult concepts.
*  And you're also the speaking of like fractal, you're able to function intellectually at all levels of the stack, which I deeply appreciate.
*  This was really fun.
*  You're a great educator, a great scientist.
*  It's it's an honor that you spend your valuable time with me.
*  It's an honor that you would spend your time with me as well.
*  Thanks, Jeff.
*  Thanks for listening to this conversation with Jeff Shaneline to support this podcast.
*  Please check out our sponsors in the description.
*  And now let me leave you with some words from the great John Carmack, who surely will be a guest on this podcast soon.
*  Because of the nature of Moore's Law, anything that an extremely clever graphics programmer can do at one point can be replicated by a merely competent programmer some number of years later.
*  Thank you for listening and hope to see you next time.
*  Thank you.
