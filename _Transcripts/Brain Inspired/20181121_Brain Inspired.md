---
Date Generated: April 21, 2024
Transcription Model: whisper medium 20231117
Length: 3196s
Video Keywords: ['Science & Medicine', 'Technology', 'episodes']
Video Views: 808
Video Rating: None
---

# BI 019 Julie Grollier: Spintronic Neuromorphic Nano-Oscillators!
**Brain Inspired:** [November 21, 2018](https://www.youtube.com/watch?v=9lP6yQhvtSU)
*  Instead of coding everything in zeros and ones and sending it to a CPU or a GPU, why
*  not make physical neurons, you know, layers of physical artificial neurons and interconnect
*  them directly with some kind of synapses that are really in between the neurons.
*  This is Brain Inspired.
*  Hello, good people.
*  Welcome to the Spintronic Neuromorphic Nano Oscillator Spectacular!
*  Actually, I am excited because it's the first Brain Inspired episode about neuromorphics,
*  and I hope it's the first of many because I really enjoyed it.
*  So we have talked plenty on this show about neural networks, deep learning, recurrent neural
*  networks, and sundries.
*  So the current way of running neural networks is you fire up your digital computer, you
*  open your favorite statistics software program like Python, and you spend what seems like
*  10 days figuring out which of the newest hot machine learning packages to use, and you
*  spend another 10 days learning how to code for that package, and then four years or so
*  coding your particular network with your particular data.
*  And of course, by then, you learn that your new hot machine learning package is now the
*  senile guy in the room, and there's another new hot one to learn.
*  Anyway, you run your network on a digital computer, and that's fine, but it has some
*  drawbacks like it's energetically inefficient.
*  And as neural networks continue to scale up in size and parameters, their energy consumption
*  will become problematic.
*  So a solution to this is to change the hardware that we run neural nets on, change the computer
*  chips themselves to resemble a more brain-like architecture.
*  Enter folks like Julie Grolier, with whom I speak today.
*  So Julie is a research director in a lab under both TALIS, which is a large French electronic
*  company, and the National Center for Scientific Research, also a huge institution that sponsors
*  a lot of research.
*  Julie and I talk about neuromorphics in general and how they differ from current computer
*  chips.
*  We dive into her nanoscale hardware implementation of a neural network that uses the properties
*  of electron spin, magnetic materials.
*  I think there's some magic in there.
*  Anyway, we talk about how it all works and how the network learns, as well as current
*  neural networks, at least thus far on a small scale that we talk about.
*  So you can follow Julie on Twitter.
*  She is at Julie underscore Grolier, G-R-O-L-L-I-E-R.
*  Her website has lots of nice introductions to the concepts and terms that we use, and
*  she's given a TED talk on this topic, and I'll link to all that and the rest of what
*  we discuss in the show notes at braininspired.co slash podcast slash 19.
*  If you would like to help keep this show running and ad free, I despise advertisements on podcasts.
*  Consider supporting it for a measly two or four dollars per month.
*  Go to braininspired.co and click the red Patreon button there.
*  All right.
*  Thank you for listening.
*  Thank you for your support.
*  And here is our conversation.
*  Julie Grolier, welcome.
*  Thank you for being on the show.
*  Hi.
*  Thank you very much.
*  I enjoy your podcast very much.
*  I was very happy when you invited me.
*  Oh, thank you.
*  That's very kind of you.
*  Well, this is cause for celebration because you, this rather is the first episode in which
*  we're going to talk about neuromorphics.
*  So let's celebrate.
*  Cheers.
*  Cheers.
*  Yeah.
*  All the way across the continent.
*  So Julie, you are in France right now and you are, I think you're in France, right?
*  Yeah, yeah, yeah, I am.
*  Okay.
*  So you're a research researcher director in the CNRS Talis lab in France.
*  Is that how you pronounce Talis?
*  Yeah, perfect.
*  Oh, great.
*  So you do work on bio-inspired computing among other things and you seem to be interested
*  in saving the world.
*  Is that right?
*  Well, if I can contribute a little bit.
*  Oh, that's modest as well.
*  Very nice.
*  Okay.
*  So the first neural networks that were created really were perceptrons from Frank Rosenblatt
*  and they were built out of hardware.
*  And I recently had Terry Sanofsky on the show and he was telling me that he actually built
*  one of those original perceptrons just by reading that original perceptron paper.
*  He went and got the supplies and built himself one using his own hardware.
*  But these days we run deep neural networks and machine learning algorithms on software
*  on digital computers.
*  We build these networks now using Python, right?
*  Machine learning packages.
*  Yeah, yeah, yeah, absolutely.
*  But you are back to working on building these things out of hardware.
*  So let's just kind of kick things off real broadly and talk about neuromorphics in general,
*  if that's okay.
*  And then we'll work our way to your most recent work here.
*  So what are neuromorphic chips and how do they compare to the CPU chips that are in
*  computers these days?
*  Right.
*  So yeah, as you were saying, neural networks are inspired from the brain.
*  I mean, they are inspired by biological neurons and biological synapses, which are all wired
*  together by axons and dendrites.
*  And it's true that today neural networks are basically running software.
*  So there are, you know, lines of code in pythons or whatever.
*  And then they are binarized in a series of zeros and ones.
*  And then they are sent into digital processors, right?
*  So these are things like CPUs or GPUs or even the new ones that have been fabricated by
*  Google that are called TPUs.
*  And so this may seem all very good, but actually there are some limitations to doing that.
*  And in fact, there are several problems.
*  And the most clear one is the problem of energy consumption.
*  So, yeah, so if we see neural networks as a huge fit functions, where you have all these
*  parameters, which are the synaptic weights, you see that when you want to have better
*  performance, it's good to have more parameters, right?
*  So people are to scale up these neural networks.
*  Yeah, a lot of these things are like hundreds of layers deep these days.
*  Yeah, exactly.
*  So when you want to do image recognition, for example, you need about to have 10 to
*  the 8 parameters.
*  And this already is going to consume like kilowatts or even more.
*  So if you want to scale these things up, which people are trying to do now, when you get
*  to a number of parameters like 10 to the 14, then this is going to consume megawatts.
*  It's going to be super slow to learn.
*  And I mean, it's going to be impossible to manage basically.
*  So it's a real barrier to progress, I suppose.
*  Yeah, that's a real barrier to progress.
*  And well, we could say, OK, maybe there's nothing to do.
*  But actually, when we look at the brain, you can say that the brain is a big neural
*  network and actually it's really huge.
*  There are 10 to the 11 neurons in the brain and about these are orders of magnitude,
*  right?
*  But 10 to the 15 synapses.
*  And so and it consumes only 20 watts.
*  So like a light bulb, basically.
*  And it can really learn in real time.
*  It's quite fast, even if the individual elements are slow.
*  So it means that we should be able to do better than what we do now with our CPUs or GPUs,
*  right?
*  So that's why it really makes sense to try to look at what is different in the brain
*  and can we try to copy it to improve the way we compute basically.
*  You have a physics background and you did your PhD on what's called the spin torque
*  transfer effect, which we'll talk we'll get to.
*  But how did you come to be?
*  Did you originally have a concern with energy consumption or was it through working in this
*  field that you learned that this could be a benefit to using these techniques?
*  Yeah, it's by working in the field actually that I started to get really interested and
*  understand how really the energy consumption was a huge problem and that well, maybe we'll
*  come to that later.
*  But that really physics and new nanotechnologies could help in the field.
*  What I wanted to say first is that so you know in a CPU, there are many, many differences
*  between the processor and the brain.
*  Right, right.
*  And so there are many different aspects or something are quite evident, you know.
*  So for example, in a CPU, everything is coded in binary.
*  Whereas in the brain, you have some you can consider that the neural spikes are binary,
*  but you also have analog coding because the synapses seem to be analog.
*  CPU is 2D, but the brain is 3D.
*  Also, in a CPU, everything is rather sequential internally and very synchronous.
*  So you have a big clock, whereas in the brain, you have a lot of dynamics.
*  You have dynamics, you don't have a central clock.
*  Everything has its own rhythm and is fully parallel.
*  That's good because I just interviewed Dean Buonamano about all the clocks in the brain
*  and how that all works.
*  So that's good.
*  Right.
*  Yeah, yeah, yeah.
*  Absolutely.
*  Okay, so that's one thing.
*  But there are two other points that are very important when we want to think how we could
*  make these neuromorphic chips and that we could benefit from.
*  The first one is that you see in a computer today, every component is very high precision.
*  Everything has to be perfect because you cannot tolerate any error.
*  Right.
*  Because if you have a switch between a zero and a one, it can really affect the final
*  number that is coded.
*  So you cannot, and this to allow this precision and this lack of error requires a lot of energy
*  consumption.
*  Whereas the brain seems to be working in a completely different lead regime, maybe at
*  the thermal limit, where in fact neurons and synapses seem to be highly stochastic and
*  still they seem to be able to function, right, through the, probably through the algorithm.
*  So it's already one thing that can be, you know, taken inspiration from in order to build
*  chips that doesn't consume too much energy, trying to allow for this stochasticity to
*  reduce the energy that we need to bring to compute.
*  But there is something that is even more important is that another really big difference and
*  where the energy consumption is very important is that in the CPU you have really two different
*  blocks.
*  You have the memory block and then you have the place where you do the processing and
*  they are, you know, they are specially separated, right?
*  This is like the von Neumann kind of architecture, right?
*  Yeah, yeah, exactly.
*  And so this von Neumann architecture is really a problem for running your networks because
*  you need, you have all these huge number of parameters that you have to fetch in the memory
*  and then you have to bring them to the processing part where you do all this huge matrix vector
*  multiplication and then you have to put them, the result back into the memory and so you
*  need to do all this transfer of data back and forth and this consumes really enormous
*  amounts of energy.
*  I like your analogy to cooking in the kitchen and having your supplies.
*  Right, exactly.
*  It's like a badly built kitchen, right?
*  Where you have a table where you have your ingredients and this is the memory and you
*  have to do the processing on another table that is like meters away so that would be
*  very inconvenient.
*  Yeah.
*  And it's very different in the brain because in the brain you have the synapses and neurons
*  that are completely entangled and it's really like the synapses are holding the memory for
*  neurons, they are very close and they are giving the memory to neurons and like that
*  you avoid this data transfer and this is really where the economy of energy comes from.
*  So having this massively parallel architecture where you have memory and processing in very
*  close proximity.
*  And so, sorry, I wanted to say that because for neuromorphic chips the idea is actually
*  the following is to say, OK, but then if we want to have this memory and processing close
*  together, why not, you know, make instead of coding everything in zeros and one and
*  sending it to a CPU or GPU, why not make physical neurons, you know, layers of physical
*  artificial neurons and interconnect them directly with some kind of synapses that are really
*  in between the neurons.
*  So that's the main idea for building neuromorphic chips today.
*  You mentioned also the stochasticity and that's, you know, in the brain we still don't really
*  understand what could, what stochasticity could be useful for.
*  So it's really still an active area of research.
*  But yeah, to build that into the chip could be an important benefit as well.
*  So you'll have to forgive me for my naivete in a lot of these areas because I don't have
*  that strong of a physics background.
*  So you're going to be carrying me through this.
*  So I appreciate it in advance.
*  OK, I will try.
*  So let's talk a little bit about just the different types of neuromorphic chips that
*  have been tried and are being created today.
*  Sort of the landscape of what this all looks like because I'm very, I'm ignorant of it.
*  So educate me, please.
*  OK, so let's try.
*  So as you said in the beginning, as soon as the brain has been, let's say modeled as some
*  computer or some logic network, as soon as this has been done, I mean, people have been
*  trying to build these kind of things, right, to make machines.
*  So I mean, very, yeah, you talk about Frank Rosenblatt and Terry Sejnowski at times, but
*  even in the 50s, Marvin Minsky started to make some kind of machine.
*  And so, but of course, at this time, they were using the technology that was available
*  to them.
*  And so I mean, they were using this huge, big element.
*  So I mean, for example, the machine of Minsky had only 40 synapses and it was a big, big
*  thing already.
*  And then after that, in the 50s, transistors appeared.
*  So it was the beginning of our current electronics, basically, because this is a building block
*  of the electronics today.
*  The digital age, I guess you could say.
*  Yeah, the digital age, if you want.
*  And so this on one side gave rise to our computers today.
*  But on the other side, it was a new building block for trying to make neuromorphic chips.
*  And so already in the 80s, there is a very famous scientist called Carver Mead, who
*  proposed to use transistors to make chips that are really directly inspired from the
*  brain.
*  And so his idea was to use transistors, not as a switch, but in a regime where there are
*  sub-thresholds and where they have this non-linear behavior as a function of the input voltage.
*  And he thought he could use that to imitate biology, because this is something that you
*  see a lot in biology.
*  And so he proposed and he built very beautiful and sophisticated neuromorphic systems like
*  artificial cochlea, artificial retina.
*  And these kind of chips, I mean, today are still developed.
*  So of course, they are more and more sophisticated and it's a trend that is going on.
*  And so people who are working in this area, their goal is really to model and to imitate
*  and understand the brain by building these chips.
*  Well, so that's in the 80s.
*  But before that, so you've done some work with what are called memristors, which are
*  these little nanoresistors.
*  But they were invented in 1971.
*  Yeah, absolutely.
*  There is this beautiful neural network by WeDraw and Of, right?
*  So I think it's called Adeline.
*  And they used in this, it was a kind of perceptron, I think.
*  They used a device that they called, at the time it was called memisto, not memristor.
*  Yeah, the idea was to say, okay, the information we propagate is the electrical current, right?
*  And synapses need to be valves, analog valves for the information.
*  So a good valve, a good way to modulate an electrical current is to use resistance, basically.
*  And so they used some device that was big at that time.
*  It was a huge thing also called a memristor that was doing exactly that.
*  So yeah, it was the first artificial synapse based on some modulated resistance.
*  Okay, and then sort of it's gone on from there and developed.
*  Yes.
*  You've touched on this just a little bit already, but what are the current challenges to developing
*  these bio-inspired neuromorphic chips that can run in parallel?
*  So I would say there are two huge challenges.
*  So if you want to make a very small chip, let's say really like one centimeter square,
*  like approximately, and you want to fit in a lot of neurons and synapses,
*  which is necessary to run some very useful computation,
*  then when you make the calculation, you see that if you want to fit in,
*  for example, more than 10 to the 8 neurons and synapses,
*  you need every device, every neuron, every synapse to be really small.
*  I mean, the lacerol dimension has to be less than one micrometer.
*  It means that you need to make nano-synapses and nano-neurons.
*  So you need to give them the important functionality at the nanoscale,
*  which is already difficult, but you need to do it with a very good performance
*  because as you were saying, yeah, the brain is stochastic,
*  but we don't really know how to use that in today's algorithms.
*  So we might want a little bit of noise, but not too much.
*  And we want to have limited variability and to have devices that are persistent,
*  that are not going to drift or degrade too much,
*  and all this at the nanoscale.
*  So this is really the first challenge.
*  And the second challenge actually is once you have all these devices,
*  you need to connect them together.
*  And maybe this is the biggest challenge of neuromorphic computing
*  because as you know, the more interconnected the neural network,
*  the smarter it can be.
*  In the brains, there are 10,000 synapses per neuron, so it's enormous.
*  Yeah.
*  It means that every neuron has to be connected to other ones
*  by 10,000 little wires in a chip.
*  So this is really extremely complicated.
*  And so, I mean, we need to find smart ways to do this.
*  One thing that I am just completely ignorant of is how these,
*  I guess we'll get into it,
*  but how these chips are built at such a fine scale.
*  You know, I picture little tweezers, but that's not how it happens.
*  So, you know.
*  Okay.
*  I see.
*  Yeah, yeah.
*  Well, maybe we can talk about the actual manufacturing later,
*  but let's get into your paper and sort of the science that led up to this.
*  So you recently published in Nature, of course,
*  because that's the only place you seem to publish,
*  you seem to publish,
*  All right, I love that title.
*  So you set up this neural network physically,
*  that is using the hardware that we'll discuss,
*  and you trained it to recognize distinct vowel sounds.
*  And these were sounds from recordings of people saying different vowel sounds.
*  So this is sort of a proof of principle
*  because it's kind of a small network,
*  but you successfully trained a nano-scale spin-torque oscillator network
*  to recognize vowels.
*  So this is cool stuff.
*  So we got to back way up though.
*  So what are spintronics and why use spintronics for bio-inspired computing?
*  So spintronics is short for electronics using the spin of the electrons, basically.
*  Yeah, so the idea is that you can get additional functionality by doing that.
*  To use the spin, what we do is that we combine,
*  let's say, okay, we send currents through multilayers
*  that are made of magnetic materials and non-magnetic materials basically.
*  So the basic element component of spintronics is called a magnetic tunnel junction.
*  And you can see it has two very little magnets piled on top of each other
*  and separated by a very, very thin insulating layer
*  that is a magnetic tunnel junction.
*  Yeah, a little sandwich with magnetic layer in between.
*  Yes, exactly.
*  And why these devices are interesting?
*  Well, first, they are today developed for making novel types of non-volatile memories.
*  So they are used in a binary mode.
*  So what happens is that these little magnets can be seen as little compass, right?
*  And when the needle points to the left or to the right, this end calls the zero or one.
*  At some threshold, I guess, right?
*  There has to be a readout of the actual angle.
*  Actually, yes, so you can switch between these two modes
*  by sending short pulses of current through the device.
*  And then you can read easily because when the needle switches,
*  the resistance changes between two different levels.
*  So that's how it works.
*  So it's computing based on the spin of the electrons
*  and being able to manipulate those.
*  Yes, and these devices can be made really, really small,
*  like with a diameter of 10 nanometer.
*  And so you can already prototypes of memories using these devices,
*  gigabit prototypes.
*  And they are on top of a layer of transistors,
*  so they are compatible with current electronics.
*  So, for example, why they are interesting in themselves like that,
*  in this binary mode, they are already very interesting
*  because they could be used to store a huge number of synaptic weights
*  coded in the floating number, for example.
*  You see what I mean?
*  Yeah, so we talked about the memristors before
*  and those can be used as well, but I guess the issue is
*  that the memristors are too large to really fit enough onto the chip
*  and that's an advantage of these spintronic components?
*  No, I mean, memristors are really very similar in a sense
*  because they can be made very small also
*  and so they can store multilevel resistance.
*  One memristor can be a synapse in itself.
*  You don't need to use several memristors to code for the synaptic weights.
*  I see.
*  What spintronics bring in addition, in fact,
*  more than that is that it's very multifunctional.
*  For example, this magnetic tunnel junction that I was describing
*  can be more than just a memory.
*  So, as I was saying, when you send a small pulse of current
*  through the device, the needle can switch
*  but if you send the current constantly
*  the needle can start to rotate in a permanent way.
*  Ah.
*  Yeah, and it rotates at like, it can go from megahertz to gigahertz
*  and then when you measure the voltage across this junction
*  you get some kind of sinusoidal oscillation
*  that is very fast and the amplitude of this oscillation
*  and the frequency of the oscillation is very non-linear.
*  So, our idea was to say, okay, you know, in deep networks today
*  a neuron has to perform some kind of non-linearity
*  and here it means that we have some device
*  that takes as input a current
*  that outputs an oscillation that is
*  with an amplitude that is non-linear
*  as a function of the input.
*  So, it performs some computation,
*  this non-linear function.
*  Since it emits a wave at gigahertz
*  this neuron can broadcast its results.
*  So, you call this, well, you call it a nano-oscillator.
*  Yeah.
*  So, we haven't talked about the torque yet.
*  So, let's build in the final piece here.
*  So, we talked about spintronics
*  and you just described how they oscillate
*  and can be read out.
*  The full thing is called a spin-torque nano-oscillator.
*  So, what's the torque?
*  Ah, yes, I forgot to talk.
*  Thank you for pointing it out.
*  So, when you send this electrical current
*  through this little sandwich, little magnetic sandwich
*  so the current comes from a normal metal
*  so it doesn't, in average, it does not carry a spin
*  but when the electrons go through the first magnetic layer
*  they are going to get some spin.
*  You say it's some kind of polarizer,
*  so it gets spin polarized.
*  So, the electrons that go out, they are going to carry a spin
*  and this spin, they are going to transfer it
*  to the next magnetic layer.
*  And by transferring the spin,
*  they make the magnet spin, right?
*  So, it exerts a torque on the other magnet.
*  So, it transfers the torque between...
*  Yes, it transfers the torque, exactly.
*  Alright, so we are all caught up here,
*  so we all know how these things work now.
*  And what you did in this paper,
*  you set up a neural network, like I said.
*  But actually, so you had work leading up to this
*  and if I understand this correctly,
*  you have, in the past, you have used
*  a single nano-oscillator.
*  It was able to function as a neural network itself,
*  one unit.
*  Is that right?
*  And if so, how did that work?
*  Yes, so we wanted to first show
*  that one oscillator was good enough
*  to be used as a neuron
*  and able to do some neuromorphic tasks.
*  And since we had only one to start with,
*  we used a trick that is called time multiplexing.
*  And so, in fact, this oscillator plays
*  the role of all the neurons in the network
*  one after the other.
*  That's what happens.
*  Oh, so it's in sequence. I see.
*  Yes, so you go back to sequential computing,
*  but this allowed us to benchmark
*  our device on some kind of database.
*  So we could do spoken digit recognition
*  and show that we obtained very good results.
*  So it proved that even if our neuron is very small,
*  it can do good things.
*  That was the idea.
*  Okay, great.
*  So, yeah, and those were on spoken digits,
*  0 through 9, I guess. Is that right?
*  Yes, 0 through 9, yeah.
*  Okay, so fast forward to this most recent work.
*  Let's talk about how the network was set up.
*  How many units and what was the input and output
*  and all that jazz?
*  Can you set us up here?
*  Yes, as I just said,
*  you see these spin-torque oscillators
*  can emit waves.
*  And what is interesting also is that
*  you can see them as some kind of radio emitters.
*  Yeah, okay.
*  But they also can act as radio receivers.
*  So because the oscillation frequency
*  and amplitude is highly non-linear
*  as a function of the electrical current
*  or the magnetic field that is applied,
*  they are extremely sensitive to
*  incoming electromagnetic waves.
*  And they are so sensitive that
*  if you imagine you have two oscillators
*  that run at different frequencies,
*  but you put them close enough,
*  they can synchronize.
*  So they can mutually influence each other
*  and end up in a state where they share the same frequency,
*  even if originally they were autonomous.
*  So in a sense, it means that they are radio receivers
*  because they have their own wave,
*  but when they receive another wave,
*  they are going to modify the way they oscillate.
*  And so we thought that we could use
*  this non-linear dynamical process for computing.
*  Our idea was to say,
*  okay, imagine you have some...
*  The concept is the following.
*  Imagine you have different layers of neurons
*  and that we want to make them communicate through waves.
*  So the first layer of neurons is going to do a computation,
*  emit a wave,
*  and the next layer is going to receive this wave
*  and modify its output as a result.
*  And we thought, okay, how could we compute with that?
*  And of course, there are probably many, many ways.
*  I mean, all this needs to be invented,
*  but what we propose in this paper is to say,
*  okay, if the two neurons get synchronized,
*  this is equivalent to having good communication
*  between them.
*  So it's like having a very strong synapse.
*  And if they don't influence each other,
*  it's like a weak synapse.
*  So in the parlance of neural networks,
*  it'd be like weak and strong weights
*  between units as well.
*  Yes, exactly.
*  So I mean, what is nice with these oscillators
*  is in principle, you can have billions on the chip,
*  but in a lab, we cannot control so many of them
*  because of our equipment.
*  So we started with only, we had four of them.
*  So with four of these oscillators,
*  we emulated the second layer of neurons
*  and we imitated the first layer of neurons
*  using some microwave source that emitted waves.
*  So we have two of these sources.
*  They emitted a wave of different frequency
*  and then sent it to this layer of neurons
*  with four oscillators.
*  Okay, so two microwave inputs
*  at different frequencies
*  going into four nano-oscillating units
*  that are fully connected by way of their waves.
*  Yes, exactly.
*  And so these two microwave sources,
*  the two frequencies, the two incoming frequencies
*  were coding for the vowels that we wanted to classify.
*  And did you, I can't remember,
*  so you have this audio of the vowel sound
*  was that transformed into the frequencies
*  or are the frequencies directly from the vowels?
*  Yes, it was transformed and accelerated
*  because our oscillators, they work at,
*  in that case, it was 300 megahertz.
*  Oh, right, sure.
*  The frequencies of vowels are much lower.
*  So yeah, so it was,
*  we did some linear combination
*  of the formants of the vowels.
*  Gotcha.
*  And then how was the signal read out?
*  How are the outputs read out?
*  Yeah, so what we did in that experiment
*  is that in our lab, we plugged the spectrum analyzer
*  at the output of our four oscillators
*  and we looked at the emissions.
*  And so the way we wanted to compute,
*  we, as I said just a little bit earlier on,
*  we wanted to use a synchronization.
*  So our idea was to use
*  the different synchronized states of the oscillators,
*  the synchronization to the input.
*  So for example, when a given vowel was sent,
*  even if different speakers
*  with different accents were pronouncing it,
*  we wanted to have always
*  the same synchronization configuration.
*  So that, I don't know,
*  I can give you an example.
*  For example, we have these four oscillators
*  and let's say if you have the vowel O,
*  you want always oscillator one
*  to be synchronized to source B,
*  to, yeah, source A and B
*  and we always want to have oscillator one
*  synchronized to source A.
*  I see.
*  You see, and for another vowel,
*  we would use another synchronization configuration.
*  I see. So yeah, and combinations
*  between these, between all of them as well.
*  Yeah.
*  Okay, so in, well, what people of my ilk think of
*  when they think of supervised machine learning networks,
*  they use backpropagation to train the network
*  and that basically takes the errors
*  that the network makes and then sends them
*  backwards through the network
*  and tweaks the weights
*  between all of the connections
*  between the units in the network
*  in a way that nudges them closer
*  to the correct answer
*  and you do that over and over and over
*  and that's the training regimen.
*  So how does this nano-oscillatory network learn?
*  Yeah, so in that particular case,
*  because we are just starting,
*  so we did not really have synapses.
*  The synapse is the coupling
*  between the input sources
*  and the oscillators.
*  And so in order to allow learning nevertheless,
*  we modified the frequency
*  of the oscillators to learn
*  because this modified the way they would
*  respond to the input sources.
*  So if you want to make an analogy
*  with classical neural networks,
*  it would be quite similar
*  to trying to learn by just changing
*  the threshold of the activation functions
*  or something like that.
*  Oh, I see.
*  So what are the advantages of this network?
*  I mean, this is going to be kind of reiterating
*  what we already talked about.
*  So I know that one advantage of using
*  a network like this is
*  just the energy efficiency.
*  What are some of the other advantages?
*  Yeah, so of course, we are starting very small.
*  And here we don't want to say
*  that the algorithm we used here
*  is very interesting.
*  I mean, it was just a proof
*  that this was working.
*  And now we are much more ambitious.
*  So we have all these.
*  So potentially, you see,
*  because you can make gigabits,
*  I mean, sorry, you can make arrays
*  with billions of these elements.
*  First, we are going to try to make synapses
*  so we have ideas to do that.
*  And we would like really to make huge arrays
*  of these oscillators
*  followed by synapses, followed by oscillators.
*  So we want to do two things.
*  We would like to show that we can run
*  very classical deep learning
*  like using backprop on these networks.
*  That's something we are going to try to do.
*  But also, because they are,
*  as we said, you see, they are oscillators.
*  They can synchronize.
*  So, you know,
*  we are trying to make a very big
*  synchronization process.
*  So we would like to see
*  if we can, by using
*  these features,
*  we could compute more efficiently.
*  We would like to see
*  if by using nonlinear dynamics,
*  which is something that happens in the brain,
*  the synchronization process happens
*  in the brain, neurons can synchronize in the brain.
*  And so my belief
*  that somehow it's useful
*  for computation.
*  And we would like to think how we could
*  you see, enhance deep learning
*  through this nonlinear dynamics.
*  But for now it's completely speculative.
*  It's something that we need to figure out.
*  We are going to study this.
*  Yeah, so much in the future
*  to do. That's awesome. So, you know,
*  I jumped the gun a little bit. But what happened with the network?
*  Did it learn the vowel recognition sounds?
*  Or did it fail completely and you got into nature?
*  Yeah, no, actually it did good.
*  It did good.
*  It could learn the vowels quite well.
*  Even, I mean, for such a
*  small network, we could achieve like
*  recognition rates of
*  85 percent.
*  And I mean,
*  a multilayer perceptron
*  with the same number of parameters
*  would do approximately the same.
*  So, I mean, once again,
*  we are okay.
*  Good.
*  And there's a nice video online as well
*  to sort of illustrate
*  the network learning while the
*  vocalizations are happening,
*  the vowel sound vocalizations. So, I'll link to that
*  in the show notes.
*  One of the advantages
*  also of these nano-oscillatory
*  neural networks, if I remember correctly,
*  is that it reduces the number of parameters
*  needed to perform at the same level.
*  Do I have that right?
*  Yes, yes. We found
*  that indeed, I mean,
*  our network for the same
*  number of parameters was doing a little bit
*  better than a multilayer
*  perceptron with the same number of
*  parameters. And we think that's because
*  the way we
*  built this network, the neurons
*  in one layer are
*  coupled to each other.
*  And so, when
*  they synchronize to the inputs,
*  they influence each other.
*  And it's a bit like saying that
*  they collectively
*  take the decision, you see.
*  And so, what we showed
*  through simulation
*  that this coupling is indeed important
*  to get a good result.
*  Yes, that's something we want also to think
*  more in the future, is
*  how to use these couplings
*  inside one layer
*  to enhance the computation.
*  It's got to be expensive to
*  make these chips right now.
*  I mean, how long does it
*  – so, I'm wondering what you're going to be
*  doing next, right? So, you had a four
*  unit network here, and now you
*  think, well, now I want to put, I don't know,
*  you know, a hundred or something, let's say, on a chip.
*  And how long do you have to wait for the
*  manufacturing to take place?
*  Yeah, yeah, yeah. So, for us, it's going to be a big step.
*  So, what we are going to do first
*  is to make networks
*  with hundreds of these devices.
*  So, this can be done by
*  doing
*  some homemade
*  circuits, if you want, but
*  integrating many of these devices. So, this we can
*  do. You mean – sorry,
*  you mean like many of the, like, four
*  unit networks, like
*  connecting them together, or is that what you mean?
*  I'm thinking of, yeah,
*  the next step we will do, for example,
*  try to put, have layers
*  of ten neurons, and
*  some, like, one hundred synapses,
*  and something like that.
*  This, I think we can still do by
*  ourselves in the lab by using a printed
*  circuit board and things like that.
*  But then, of course, we,
*  if we want to go to millions
*  of devices, we need to,
*  we will need support from industry, because this is
*  extremely costly, as you say.
*  And so, yeah, we are starting to
*  talk with
*  people who can manufacture these devices,
*  because there are now many foundries
*  who are starting to
*  integrate magnetic tunnel
*  junctions in their process
*  for building a really, you know, big
*  wafers. And so, yeah, so
*  we are starting to see what is possible.
*  Yeah, that's kind of frustrating
*  that you're having to sort of wait for manufacturing
*  to catch up, you know?
*  Yes, but there's so much to think in between.
*  You see the algorithm, how to connect
*  it.
*  It's okay, we have things to do in between.
*  Yeah, yeah, you're not suffering
*  from lack of anything to do.
*  Well, so, this is great, it's awesome work.
*  So, I mean, sort of the summary is that
*  you built this neural network using
*  these spin-torque nano-oscillators,
*  and successfully
*  trained the network
*  using a few tweaks and
*  trickery here and there, to
*  transform sound into frequencies
*  to inject in the network. But
*  you built a neural network,
*  a hardware implementation of a neural network.
*  And, oh, and I should
*  say, it's extremely stable.
*  Isn't that another advantage of this
*  type of network? Yes, yes.
*  I mean, for nano-devices, magnetic
*  materials are very stable.
*  So, yes, that's important for
*  learning, because if there is some drift
*  of the properties, then
*  the learning cannot be achieved.
*  And here it was OK.
*  Great, this is awesome. I'll point people
*  to the paper, of course.
*  So, in our remaining time,
*  do you want to just kind of open it up and talk a little bit
*  more broadly? Can I ask you a few kind of
*  broad questions? Yes, of course.
*  So, I'm curious
*  how, if you communicate
*  much with the machine learning community
*  and the neuroscience community,
*  and what their take is on this?
*  Are people excited? Do they not want to hear
*  about it, etc.?
*  So, yes, we are starting to
*  talk with people from
*  machine learning
*  and the computational
*  neuroscience community.
*  So, let's say, of course, for now, what we are doing
*  right now is not really, it's too small
*  for them to be interested.
*  I mean, now the machine learning
*  community has really turned
*  to try to adapt
*  backprop and
*  deep learning to hardware.
*  They are trying to reduce the precision
*  of the weights.
*  I mean, there are all these papers that
*  you, in fact,
*  you talked in your podcast about
*  how deep learning could be implemented
*  in the brain, which is some type of hardware.
*  So, there is some
*  link here
*  to talk with people from machine learning.
*  And also, computational
*  neuroscientists have always been very interested
*  in neuromorphic chips
*  because their models are very
*  complex and they know they cannot run very well
*  on CPUs
*  and GPUs. And so, they are very
*  eagerly waiting for these kind of systems
*  to scale up to run
*  their models, right?
*  Speaking of that, the current trend,
*  it seems to be the current trend
*  in deep learning network,
*  is to continue building more
*  brain-like features into these models.
*  So, there are people trying to
*  build dendrites, for instance,
*  into the units, like Blake Richards,
*  the person I spoke with. And
*  the further we progress,
*  it seems like the more neuron-like
*  features are being built into that.
*  And I'm wondering if that's relevant
*  for these nano-oscillators
*  and how much,
*  how brain-like you can get or even
*  want to get with them.
*  Yes, that's very, I mean,
*  these brain-like
*  deep models that are being
*  developed are for us extremely
*  interesting because
*  they are bringing deep learning
*  closer to the
*  hardware that is the brain. And so,
*  they are getting easier to run on
*  our devices, closer to what we could
*  run. So,
*  we are reading all these
*  papers and trying to understand and see
*  how we could
*  maybe augment the functionalities
*  of our artificial neurons
*  and synapses also to look more
*  like what these models
*  need. So, yes, there is some kind of bridge
*  here that we are
*  working on making
*  this connection. Yeah, I'm curious
*  to see how brain-like,
*  you know, when does it stop?
*  Because eventually you just model the entire brain
*  and that doesn't seem
*  necessary. But who knows
*  what features are really
*  important and what aren't? I guess we'll find out.
*  Yeah, absolutely.
*  But I must say that on our
*  one of our objectives, of course,
*  I think everybody in this community
*  is fascinated by the brain, but we
*  would be happy already if we
*  are able to build a small chip
*  that can do something useful with
*  very low energy consumption. That would be
*  good already. Oh, that would be great.
*  Yeah, that's why
*  I said you're saving the world. How to save
*  the world here. Right, not yet.
*  Not yet. Well, hey,
*  but you still have plenty to do in the meantime before you
*  save the world. So, these
*  units, you talk about
*  how they last a long time
*  you write the paper. So,
*  they're stable and they're hardy.
*  Eventually in a,
*  let's say, an AI system,
*  you're going to have to replace a unit, right?
*  And these units respond differently
*  to different current
*  injections. And then,
*  but when you have to replace
*  a unit that wears out,
*  is it possible because this unit has been trained,
*  right, with the essentially
*  training weights,
*  analogous to training weights,
*  over time, can you then
*  replace that unit with a new one
*  that holds the same
*  learning, training?
*  Does that make sense?
*  Yes, yes, but that would be complicated
*  because indeed we do it in hardware
*  so we cannot replace
*  a device. So,
*  but what has been shown is that
*  what is very nice with
*  neural network is there is some kind of
*  a bit of redundance. So, you can lose
*  neurons
*  up to a few percent
*  and synapses even more
*  without degrading too much result.
*  Right. And if
*  we want to avoid that, what we need to do
*  is to build in this redundance.
*  So, have more neurons than
*  necessary at the start.
*  So that we can rewire if we need to.
*  But then you will need to retrain a bit, of course.
*  Oh, so more
*  and more brain-like, indeed. Yeah.
*  So, you know, so far we've talked about
*  using what's known kind of in
*  neuroscience and you
*  derive inspiration also, I guess, from
*  artificial neural networks when you guys are
*  considering how to proceed.
*  I'm wondering if there's anything that we
*  if you've thought about
*  how
*  these nano-oscillators, if they can
*  transfer any knowledge
*  into neuroscience, can we learn anything about the
*  brain using this technology?
*  Yeah, that's a good question.
*  I would love to say yes, but
*  I'm not sure.
*  I would, it would be great if, because
*  of course,
*  when you, by trying to
*  build something, you always
*  learn, right?
*  So, I hope we will learn something. What we try to
*  do is each time we make
*  a small prototype like we did
*  is to get some lessons from it.
*  So, for example, when we
*  made our first experiment with
*  time-multiplexing with only one neuron,
*  we found out that
*  I mean, people always say
*  in neural networks,
*  they are very noise tolerant, so noise
*  is okay, but in fact,
*  in a nano-device, noise can be
*  very high, and in fact,
*  we learned that it's okay to have
*  a little bit of noise, but not too much
*  for it to work. So, that's something
*  we understood at that point.
*  And so, each time we try to learn something,
*  right? And I don't know if what we
*  learn for these oscillators could be
*  applied to the brain, but
*  maybe there are some links.
*  Yeah. Well,
*  when we were talking earlier, and you were talking
*  about how sensitive they are to
*  fluctuations,
*  I was kind of picturing
*  my mind just goes straight to a robot
*  for some reason, but if I just
*  have my microwave
*  gun, can I just deactivate
*  the robot? But I guess they'd
*  be built into little black boxes
*  and shielded from the radiation.
*  Yeah, absolutely. Yeah. Okay.
*  Okay, so this seems like hard
*  work, Julie.
*  Can you tell me about
*  something that you failed at or
*  got rejected from or
*  were just wrong about sometime
*  and how you moved on from it?
*  Yeah, I don't know. I've been
*  like everybody. I had so many
*  failures and did things wrong.
*  I was...
*  One thing that happened
*  to me is that
*  when I wanted
*  to get this project funded, and
*  I tried to get a European grant,
*  so I wrote a project and it went out to
*  many referees, and then it
*  was rejected and I got the referee
*  report, and one of them was
*  saying, oh, okay, this
*  Julie Gourlier, she has all
*  this idea, but she never does anything,
*  you know?
*  You know, I was really
*  angry at
*  that, but at the same time,
*  sometimes it's a bit true. I tend to
*  dream and figure it in my
*  head and then maybe don't do it enough, so I said,
*  okay, this time I'm going to do it, right?
*  So, yeah, that's what I've been doing these
*  last years, and yeah, it worked out in the end.
*  You've become a woman of action.
*  That's actually one of the reasons
*  why I decided to go to
*  graduate school because my
*  sort of default is to be a dreamer
*  and not do, and I've only...
*  So I kind of forced myself into action
*  by going into graduate school, you know.
*  Yeah, I know what you mean.
*  Yeah.
*  And, you know, I've
*  learned how important action is, and
*  sometimes I preach a little bit on the show,
*  you know, trying to prod
*  people into action, and I think my audience
*  doesn't need any prodding, so I don't really need to preach.
*  But, so, oh, but
*  that must have felt terrible.
*  Yeah, yeah, a bit.
*  But then, yeah, you see,
*  I could overcome it.
*  Yeah, well, so
*  you're doing stuff, but you are a dreamer,
*  and I'm wondering if there's
*  something that you believe,
*  because it's just impossible
*  to predict the future. We're terrible at it.
*  But is there something that you believe
*  that will come out of the interface of
*  neuroscience and artificial intelligence
*  and maybe physics
*  that might be a little out there?
*  My dream is really to see, you know,
*  one of these big artificial
*  neural networks that produce something
*  really, you know, amazing,
*  like, yeah, computing
*  through
*  nonlinear dynamics
*  with very low energy consumption, and
*  yeah, that would be really great.
*  I like how you often
*  start your talks
*  with this, the energy consumption, and
*  it really is a huge problem
*  that I think goes under the radar,
*  mostly. Yeah, yeah, because
*  there's been all this progress, so GPUs are
*  doing better and better, so
*  people might have the feeling
*  that it's going to go on, but actually
*  there are really some limitations
*  that we are going to hit soon, and
*  so we need to think about that now,
*  I think.
*  Julie, je vous remercie.
*  Merci beaucoup.
*  Thanks for talking with me today,
*  and this is really fascinating work.
*  Keep up the good work and keep up that
*  action so that you don't get those reviews again.
*  Yeah, thank you.
*  Thanks for the advice.
*  Brain Inspired is a production of
*  me. You can support the show
*  through Patreon for a trifling
*  $2 or $4 per month.
*  Go to patreon.com
*  slash Brain Inspired, or go to
*  the website, braininspired.co, and
*  find the red Patreon button there.
*  Your contribution will help keep this show
*  going without any annoying
*  advertisements like you hear on other shows.
*  To get in touch with me, email
*  paul at braininspired.co.
*  The music you hear is by The New Year.
*  Find them at the newyear.net.
*  Thank you for your support.
*  See you next time.
