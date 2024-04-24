---
Date Generated: April 19, 2024
Transcription Model: whisper medium 20231117
Length: 5731s
Video Keywords: []
Video Views: 1048
Video Rating: None
---

# BI 178 Eric Shea-Brown: Neural Dynamics and Dimensions
**Brain Inspired:** [November 13, 2023](https://www.youtube.com/watch?v=92dCOE36gh0)
*  That sounds nuts, right? If somebody would have asked me whether that is likely to be true, and I was responsible for this field of research, I wouldn't have even started. I would have thought it was hopeless.
*  I think we really need to probe this question of when structure matters and when it doesn't, right? And so sometimes we might write down a bunch of different model architectures, one with a bottleneck, one without a bottleneck, one with some sort of propensity to produce oscillations or attractors, one without that propensity, one with cell types, one without cell types, and try to understand when it makes a difference.
*  If Paul is completely in charge, and maybe Paul is in charge of all of the ten neurons, then you'd say that that system is just one degree of freedom. It's whatever Paul feels like doing. And one degree of freedom means one dimension, right? It's a one dimensional brain. Paul is really our only neuron effectively.
*  I'm fine with that brain.
*  You're fine with that, right?
*  This is Brain Inspired. Hey everyone, I'm Paul. Eric Shay Brown is my guest today. Eric's a theoretical neuroscientist and principal investigator of the Working Group on Neural Dynamics at the University of Washington.
*  In this episode, we talk a lot about dynamics and dimensionality in neural networks, how to think about them, why they matter, how Eric's perspectives have changed throughout his career.
*  We discuss a handful of his specific research findings about dynamics and dimensionality, like how dimensionality changes when one is performing a task versus when you're just sort of going about your day.
*  What we can say about dynamics just by looking at different structural connection motifs, how different modes of learning can rely on different dimensionalities, and more.
*  We also talk about how he goes about choosing what to work on and how to work on it.
*  You'll hear in our discussion how much credit Eric gives to those surrounding him, his colleagues and peers, and also those who came before him.
*  He drops tons of references throughout the discussion, so get ready if you want to follow up on some of the many lines of research that he mentions.
*  You'll find links to Eric's website and some of his relevant work in the show notes at braininspired.co.uk slash podcast slash 178.
*  You'll also find there a link to Patreon to support this here podcast. If you're feeling generous, huge gratitude to all of you who already support Brain Inspired. I really appreciate it. Thank you.
*  And thanks to Eric for this lovely conversation.
*  Eric, when's the last time you went mountain climbing?
*  Ah, let's see. Well, it depends what you define as a mountain. But my son Milo is now 11. And so my whole experience in the mountains, as most things in life as everybody who's a parent knows, revolves around him now.
*  So just on the weekend, we went out rock climbing together and completely awesome.
*  That's what I meant rock climbing. Did you guys like belay each other or what?
*  We did. Yeah. So we climbed as a team of three. So me and my beautiful wife Colleen and my 11 year old. And so I go up first and then the two of them climb up together.
*  And we did this incredibly beautiful climb called Black Solar Supreme or something like that. Just overlooking Mount Rainier on a perfect sunny day. It was enchanted.
*  And did you go offline just a moment ago? We were talking about RVs and Volkswagens. Did you go in the VW and the newer VW?
*  You know, we wanted to drive our bus up there, but Milo had business in town that he needed to attend to the next day. He's also an insane carnivorous plant lover.
*  And he had the opportunity to get another species to add to his list if he cleaned up his carnivorous plant chaos, which is our living room.
*  And so that was the top priority. And for once, as a parent, I actually managed to listen to him.
*  So we just rolled down the mountain in the evening under the full moon and got to work on his interest in botany. Oh, nice. OK, so we talk some science. Let's do it.
*  I mean, you've been a dynamical systems enthusiast for a long time now.
*  And it seems from my limited viewpoint that that the dynamical systems approach, dimensionality approach has really exploded in the neurosciences the past handful of years.
*  And I wonder what that's like from your point of view, kind of historically when you were first getting into these things and just seeing it.
*  Am I accurate in that it has kind of exploded or have I just not been in your world and it's OK?
*  Yeah, I think you're right on target. I think there are threads that use dynamical systems in incredibly beautiful ways to understand neural computation that I think, as you know,
*  very well go back to the fifties with milestone events closer to neural computation in the in the 80s as well.
*  But I think maybe people like me who originally came from outside the field of neurobiology have gotten to know of those beautiful historical developments better.
*  And so that thread or those bubbles perhaps have have have surfaced or those flowers really have blossomed in an amazing way in recent times.
*  There have also been a really new pair of perspectives.
*  The first is, I think, very new, which is to pursue dynamical systems from a top down perspective.
*  Again, we have to be humble in our claim of newness because the techniques which enable one to do this, right, observe a system and then try to extract from it the rules Newton's equations, if you will,
*  the rules that map the state of that system into the future, the dynamical rules of the system.
*  Those techniques have also been around since the 60s or before, right, by the name of Kalman filters and others.
*  And there have been people like Steve Schiff close to you in Pennsylvania, the University of Pennsylvania, who have since the 90s and early 2000s explore the application of those dynamical systems from data extraction tools to neuroscience.
*  But I do believe that it's really been in the last decade, maybe decade and a half, that the idea of just looking at fabulous and large scale brain data, a fresh and from that trying to extract dynamical rules, really dynamical systems has become maybe a third way, a third path to study neural systems.
*  And that is a new explosion. So I think you're right. I think there's growth in the field. But we always have to remember that some of that comes from brand new innovations.
*  But a lot of it also comes from realizing right that the giants that step before us in other fields or or even within our own field and perhaps when unrecognized had great ideas that it's our turn now to try to develop.
*  But I would say that you're on the early leading edge of that right back in, you know, if you go back, you know, 1015 years, I mean, are you are you are you just a sage? Did you know that your time was coming and you needed to get in at that point? Or were you just following what you thought was beautiful and right?
*  Yeah, I think that's too generous and kind of you. I think that, you know, at the time in which I began working in dynamical systems in in neuroscience, I was very much following existing dynamical systems approaches to neuroscience from from my mentors.
*  I fell in love with dynamics, as many of us do in in a freshman physics class. Do you remember it? Actually, it wasn't really a freshman class, was it for me? Maybe a sophomore or junior or something. But anyway, you've got a pendulum swinging back and forth like this. Here's my coffee.
*  And then what's the usual way to approach this? Right. You write down some set of equations again, they're the dynamical laws for a system that map the state of the pendulum, where it's at, how tilted it is, how fast it's going into where it's going.
*  And then you unfold those dynamical laws over time and you're able to predict the future. Right. The miracle of dynamics. But usually when you see that it's posed in terms of differential equations. Right. We all remember this second derivative of X is equal to force or something like that.
*  And then you work and work and do the right substitutions and a bunch of calculations on the forum on the page. And then suddenly you get the trace versus time of where your pendulum is. Right. That's our usual exposure.
*  And for me, when I was doing that, I honestly maybe I got a minus in the class or something, but I had no idea really what was going on. I didn't have a feel for it. It didn't feel that appealing. It felt sort of like magic. And then like many of us, do you remember Paul when in that class suddenly somebody instead drew a picture, right?
*  Took a geometrical approach to the dynamics. It's actually the position goes in this direction and the velocity in that direction or the other way around.
*  And this path is back and forth. Oscillation of this pendulum can be understood by some property that causes that dynamical law, which tells you how the state changes to complete the circle.
*  So if you can have a theory of how forces push you around in a circle that you can feel that you can draw, that you can shape and that you can generalize, you understand what makes an oscillation.
*  So many of us saw that right in a physics class about a pendulum or something else like that. Then I had this professor at Berkeley named Harold LaCarre, who taught a class on biophysical neuroscience.
*  I was very fortunate by just good luck and kind support of others to sit in on. And then suddenly Harold LaCarre was drawing the same picture on the blackboard with the same type of circle that described the motion of something that was moving.
*  But in this case, it was the periodic firing of a neuron. And for me, this was just a watershed because it indicated that these same wonderful tools linking geometry and the ability to predict the future, see into the future by seeing geometrically what these laws really mean could be applied to neural systems as well.
*  And so in that sense, I was absolutely not a sage. I was just lucky and just happened to stumble into these classes where people like Harold LaCarre were pushing a very interesting theory of how forces push you around in a circle that you can feel that you can draw, that you can shape and that you can generalize.
*  Then I went to work, I learned more about the work, Harold LaCarre, John Renzell at NYU, Marty Golubitsky, who was a professor at the University of New York, and I was very fortunate to have him as my mentor.
*  And I was very fortunate to have him as my mentor. And I was very fortunate to have him as my mentor. And I was very fortunate to have him as my mentor.
*  And so I studied with these amazing individuals, and that's how I got into the field. And I was very fortunate to have him as my mentor. And I was very fortunate to have him as my mentor.
*  And so I studied with these amazing individuals, and that's how I got into the field.
*  And so I studied with these amazing individuals, and that's how I got into the field.
*  And so I studied with these amazing individuals, and that's how I got into the field.
*  Just good luck in getting piped in through a pendulum.
*  Well, and hard work, of course, I'm sure.
*  But now we're talking about these like giant populations of neurons, and to look at a single neuron and model it as a dynamical system is one thing, right?
*  But then and we'll come back to this because I want to ask you about looking at dimensionality across scales, which you've recently written about.
*  But, you know, how do you think that in terms of this more recent explosion?
*  I mean, how do you think it has changed in the field?
*  And then what I'm really curious to know is how your own, you know, going from like seeing that early example of a neuron, right?
*  The graph of a neuron, the cycles of a neuron, going from that to then applying it to like these larger populations of neurons, how that has affected how you think about applying this to brains and how you think about brains in general.
*  Yeah, yeah, absolutely.
*  So just to do with a proper homage to history, right, Wilson and Cowan, as you know, in the 70s, right, a famous paper in 1972, were already thinking about population level equations and that bridge from single cells to entire groups of cells that would then be described by their firing rate or average levels of activity.
*  And believe it or not, one of the famous early results that they had also was how populations as a whole excitatory and inhibitory cells can produce oscillations.
*  So once again, funneled in through the pendulum and geometry to the understanding of large scale populations.
*  But I think you're right to finally take the bait.
*  These days it is different and things are different for multiple reasons, one of which, of course, is that some of the large scale population dynamical equations that are under study are not those that come from ground up models that start with physical laws or biophysical laws that you can roughly
*  interpret and approximate from understanding how individual neurons work as machines and then scaling up to populations, right, the approach of Renzel and Lacar and Cowan and others that we were just discussing, also very importantly, Nancy Coppell, then at Boston University and still there.
*  These days it does seem to be a little bit more complicated.
*  These days it does seem different in that there are observations of the brain literally in action and there are techniques then to write down the systems of equations that describe the brain's motion over time.
*  And sometimes that's an oscillation once again, but oftentimes it's something much richer.
*  So that's a whole new domain of study.
*  The other thing that does trace a thread that's historical, at least back to Oya and Oya's rule and also, of course, to the work of Steven Grossberg and perhaps a year before John Hopfield in the late 80s is the idea of associative memory models.
*  So what are these? So these are both dynamical systems that actually implement computations.
*  And that's the second big thread I want to talk about.
*  So what's new? Thing one, dynamical systems that come straight from observations of large scale brain data.
*  Thing two is really an explosion in the study of dynamical systems that once again do not arise from strict biophysical considerations, but do arise from the performance of an algorithm.
*  In the case of Oya's rule, the extraction of principal directions that efficiently summarize large and complex scenes or sets of data, principal component analysis, as called.
*  And of course, in the case of Hopfield and Grossberg, the idea of pattern completion and memory.
*  And so those are, you know, hey, I want to extract what's important about the world or hey, I want to remember something.
*  That's not biophysics, right? That's computation.
*  But those scholars, as well as many others, historically, maybe 40, 50 years ago, were starting to formulate algorithms to learn or to perform those types of computations.
*  And lo and behold, those were dynamical systems and understanding the algorithms could then be done through the lens of dynamical systems.
*  And that line of work through, for example, the endeavors of Sophie Deneve at E&S Paris is one exemplar and role model for that type of work.
*  That type of work also, Chris Rozelle, Georgia Tech and many others has totally exploded.
*  So now we have the dynamics of algorithms and the dynamics of computation starting from the dizzera data of actually doing something cool in the world.
*  And that is a really new I think that field is really been elevated in the last years as well.
*  You've been applying theory to artificial nets a lot and in a lot of different manners.
*  And we're going to step through like some of the things that you've done, but just in a broad sense, has working with some of these, you know, I'll call them toy models sometimes and stripping things away and applying assumptions.
*  But has working with artificial nets changed your intuitions at all and or perspective on the way that the brain operates or has it or does it just kind of fit the way you've always pictured it?
*  Yeah, I would say definitely not. Again, I describe my background, which is more of a ground up biophysics style approach.
*  I was not aware myself. I was extra unaware of the power of artificial networks to do amazing computation.
*  I think the whole world was unaware of this as well. Right.
*  But except for some godfathers out there. Well, perhaps. But did they really know they thought it would work? But where were the examples? Right.
*  Until 2006 or whatever.
*  Anyway, so maybe I had two corners to turn, you know, being aware of the amazing connectionist and PDP theory, right, from the 80s.
*  And other colleagues largely at Carnegie Mellon, Jonathan Cohen, too. Right. That work was developed in the in the in the 80s and 90s and was absolutely pioneering.
*  I didn't know enough about it. But then, like the rest of us, right.
*  Many people didn't know how well it would work.
*  And so, you know, all of us have experienced this transition in terms of dealing with artificial neural networks.
*  These are systems that are potentially tractable. Right. We have the whole parts list. We have all the dynamical equations written down before us. Right.
*  And the gigantic perspective shift for the whole world, really, is that this parts list is sufficient to drive really, really interesting computation.
*  So the change in perspective is that we can apply techniques to a known set of equations.
*  And this dynamical system has almost as much power, it seems, as as as we do. That's amazing. Right. What a time to be alive.
*  Yeah. But that's a very just to push back slightly. Right. So that's kind of coming at it from the perspective of the artificial systems. Right.
*  So if you kind of like step back and think of the biological system that we're studying, do you think any differently about that or do you think about the way that we're studying?
*  Yeah. Do you think any differently about that or do you just see it as that computational kind of dynamical system?
*  Yeah. Thanks so much for asking that. What a wonderful question. And lots of us are struggling with this now. Right.
*  Like, is the computation the same or the different or different in an artificial network that's, you know, recognizing brownies and and and cheesecakes or whatever I love to eat.
*  So no cats and dogs for me. You're speaking to me as a hungry person today, by the way. So these are going to be right. This is going to be your downfall mentioning food.
*  Yeah. So your question is great. So what are you doing right when you're studying these artificial nets? Are you developing a theory of computation with a known parts list?
*  A right. It's going to be completely different from the theory of computation with sort of known parts list B, which is that that arrived from evolution. Right.
*  And you do a whole podcast on this and you're a professional at understanding this distinction. So I'm not going to tell you or your listeners anything new here. Right.
*  But that is the question. Right. And as you also know very well, there have been a number of studies which I really think are remarkable in terms of showing a commonality, right.
*  In the sense that there is a universal point to which any learning algorithm working with a parts list that's that's close enough will converge to write many people.
*  Let's see. Matt Gala, many others. I just want to make it very clear that these are not my own ideas.
*  I think that the ideas argue that the dynamics that appear out of this evolution, David Susio, also colleagues at Google, that the type of processing that occurs across wide varieties of different parts list based networks that are that are seeking to learn a computation.
*  So the processing that occurs will be best described by universality, a commonality that's expressed in terms of dynamics. That's cool. Right.
*  So to say that the evolution equations that describe how it is that information is going to be swirling around a network are going to be qualitatively similar, roughly similar, no matter what you build that network out of once it has solved the task.
*  That's the idea, right. Not my idea, but the idea of many. That sounds nuts. Right. If somebody would have asked me whether that is likely to be true and I was responsible for this field of research, I wouldn't have even started.
*  I would have thought it was hopeless. Luckily, other people were in charge or the other people took the steps and you and your listeners, we can discuss some of them if you want, but have seen many examples in which it really does seem like way beyond chance, way beyond what you would expected.
*  So the types of features that arise in a artificial neural network and that can be observed through these data driven dynamical systems methods in the real brain seem to be really quite similar.
*  Right. It's not going to be the same all the time, but but the fact that those two things can, at least in some cases, talk to one another and perhaps be revealing the same underlying ideas, the same underlying principles opens the door.
*  So if you ask the question, do I feel like it's artificial neural networks on Monday and biological neural networks on Friday?
*  In some sense, yes. Right. But the question is, you know, on Wednesday, you know, do those two things meet and when do they when do they meet and why? And that is basically an amazing question for anybody from neurobiology to mathematical theory to be thinking about.
*  And many are, as you know, but you spend most of your time thinking or you tell me this. This is a question. I'm not going to tell you what you spend most of your time thinking about.
*  But from my perspective, I would guess you spend most of your time thinking from a principled theoretical perspective and thinking in terms of how can I build a model that has particular features with a particular set of input data in a way that I can learn something about how the dynamics are structured within that model.
*  Instead of how can I build a model that does something like the cerebellum does or something like that? Right. So you're after you're after these higher level principles that should be a to say the word universal, universal feature of whatever areas you're studying and different brain areas under different cognitive functions and different cognitive loads and different cognition will behave differently.
*  But some of those principles can be applied in those separate situations. Sorry, that's not full.
*  No, not at all. I think I think that's right. And so so I think I think that one way I would hear that question is, you know, how much about the brain, how much structure do you build into a network that you might study?
*  Right. One approach, as you indicated, might be to go for universality.
*  And that would say that you might try putting in different types of structure initially into a system and seeing when they when they wash away and when they stick around and impact the computation.
*  Another approach might be to follow right the landmark approaches of Hopfield and Grossberg, right? And to say, you know, what is the minimal neural network that can store memories, right? That has stable attracting basins into which close by patterns of activity will fall and recall a common memory.
*  So what do I do? A mix, right? I think we really need to probe this question of when structure matters and when it doesn't. Right.
*  And so sometimes we might write down a bunch of different model architectures, one with a bottleneck, one without a bottleneck, one with some sort of propensity to produce oscillations or attractors, one without that propensity, one with cell types, one without cell types, one with a bottleneck.
*  And try to understand when it makes when it makes a difference.
*  I think when we try to maybe we're not as we haven't been as inspired as let's go back to Hopfield and Grossberg with really being able to think of a deep computation like like memory and from the ground up, think about a minimal architecture that can perform that.
*  You can think about us maybe more as flailing and experimenting with the same kind of data.
*  And then post facto trying to generate a minimal model of what we of what we saw.
*  So that requires that requires luck, perhaps more more than more than genius.
*  And that requires the notion that there is something universal to be discovered to be correct.
*  Right. Otherwise, we can't do that.
*  If you want to be charitable approach, we're never going to come upon common and meaningful principles.
*  But it seems in some cases, you know, in other people's groups and in mine as well, that that approach has some potential for for some successes.
*  Well, I was going to ask you how you think about this.
*  You want to study because it seems so varied the types of questions that you're asking.
*  And is it is it really just throw a bunch of stuff at the wall and and then the thing that makes you go, huh?
*  That's that's funny. And then and then think like, well, why is that interesting?
*  I mean, you know, I'm I'm a really interesting person and I'm just kind of a, you know, I'm kind of a great person.
*  and then think like, well, why is that interesting? I mean, you know, now I'm putting words in your
*  mouth again, like, how do you decide on these 14 different things that you're currently studying?
*  Yeah. I mean, there are cases where it's let's go against the wall, right? But in these cases,
*  you would be starting with a very generic model, right? Sorry about that. That was jargon, but you'd
*  be starting with the simplest possible setup. What is the end? And it does come from the brain. It is
*  brain inspired in that sense. Like, what have I got? I've got a lot of neurons, right? They serve
*  up spikes and maybe they fall into two categories, excitatory and inhibitory. That's all I got.
*  Right. And then let's connect these things up randomly, right? And you know, they're connected
*  together with some probabilities, say every 10th neuron pair is connected, something like that,
*  whatever. Cook that together, right? And see what it does, right? There's a long history of this
*  type of work. And it turns out to do super, super interesting things, like really interesting and
*  surprising things out of the gate, right? It's been known since the work of Van Vriesch and
*  Sampolinsky, right? 94, 96, that this type of a system will produce very irregular activity.
*  And sometimes people call this chaotic activity. But the point is that if you at least record from
*  the brain, it does too, right? This is one of the persistent mysteries of the brain. There's a very,
*  we're working someone in this kind of area as well now. And it's very controversial whether or not
*  this sort of just big random soup generating irregular activity is really an explanation
*  for the irregularity that we see in the brain. But we've all got to admit that that is super
*  interesting, right? Just mix these ingredients in a pot and they come alive sort of like radioactive
*  soup emitting pulses like a Geiger counter, right? Literally as a Poisson or totally irregular
*  process record from a brain. And although there are lots of deviations, many people will tell you
*  that one of the foundational things that it looks like is that cells are firing more like a Geiger
*  counter than not. That type of similarity is amazing. Something that we worked on maybe 10
*  years ago or so, more than that actually, Guillaume LeJoy, Kevin Lin, Lysanne Young at NYU,
*  and others leading the way was to look more in more detail at that soup, right? At that Geiger
*  counter sort of looks super irregular bath of activity and make the observation that yeah,
*  it looks super irregular if you look at one neuron at a time. But if you start to look at dozens or
*  hundreds of cells, the activity patterns are super structured and actually they become incredibly
*  irregular in that the irregularity is only expressed in particular directions or for
*  particular combinations of neurons. But let me try and put it another way. That wasn't clear. If
*  you look at a single cell, it looks irregular, but there are many other cells that are doing
*  something that's very closely related to what every individual irregular cell is doing. So if
*  you can record from bunches of cells at once, you can crack the code and see a consistent,
*  predictable pattern of activity occurring. So anyway, your big picture question is like,
*  what do we do? Just like randomly guess and like do stuff and like, how do you actually have a job
*  doing that? Which is a pretty good question. That was not my question. Yeah, well, that's how I
*  would phrase it. And one, and I think one reason is that if you take even minimal sets of these
*  components, right, like excitatory inhibitory cells, big network, more or less, sparsely connected
*  together, it turns out maybe this is universality working from the bottom up that those types of
*  ingredients produce features that are worth studying in terms of the essence of what the
*  brain's dynamics might be. And then you could imagine following from that, like, okay, that was
*  fun. We had two cell types, as you know, very well. There are many more than that, distinguished by
*  their anatomy, distinguished by their dynamics. How did these additional ingredients change the
*  picture? That's all bottom up, right, in terms of what ingredients you put in your soup and then
*  how you, you know, arrange things, structures of connections, maybe that make it less of a soup and
*  more of a more of a cake or more of a lattice work. The top down field works the same, right? Let me
*  understand how learning works in a neural network with basically no structure. Let me understand how
*  neural network works in a system with excitation and inhibition. Let me acknowledge that learning
*  has particular constraints and let me see how these shape the patterns. And as I add these
*  different assumptions, which ones make the resulting activity patterns in the brain look,
*  sorry, in the simulated brain look more like the real brain? Which ones have a systematic effect
*  that you can then seek to try to categorize? And which ones, which is going to be most of them,
*  just lead you to confusion and those results. And so that's where the throwing at the wall
*  goes from. But it tends to be starting from a point of the simplest possible and minimal
*  biological assumptions and layering on additional features that more or less come from the biology.
*  I won't claim that we're that organized, but that's the philosophy.
*  Are you, this may seem like a non sequitur, but are you more or less in awe of the biological
*  brain after all these years? I think that,
*  right, you could, one answer could be like, why is this guy more in awe of this if he's saying that
*  you just like write down a soup and that does the same thing as the brain, like whatever, right?
*  Then it's this soup that came out, 700 million years of multicellular complex life, like whatever,
*  it's just some soup that somebody can write down and like find equations. Like that doesn't sound
*  awesome at all, or that doesn't sound like you should be that impressed by the biology.
*  But I think there are twin aspects which are cool, right? Like one is that still, right,
*  you need to achieve this universal, super powerful computation within biological constraints, right?
*  And that means you have to not die, you have to provide energy, you have to consume not even
*  more energy than the brain actually does. You have to be robust to turnover. You have to be able to
*  learn from many fewer examples than most modern AI systems can learn from. And you have to be able
*  to, as Tony Zador emphasized to us recently at a meeting, stuff whatever the key ingredients are
*  for driving this biologically plausible computation into a genome that can be read out and reproduced
*  from one generation to the next. So that's cool, right, implementing the universal stuff in a way
*  that actually works as a machine. But there's a super awesome thing, honestly, I guess our
*  conversation hasn't gone to this yet, is that there are aspects of computing systems, many,
*  many ones that are also not generic or not universal, right? And you've probably maybe
*  even interviewed or talked with individuals who have been inspired by Michael Graziano's,
*  let's see here, attention schema theory of consciousness. This is absolutely a computational,
*  almost dynamical theory of where it is that the sense of awareness, the sort of tactile
*  feel of awareness arises from. And it is absolutely from a large neural system that needs to
*  exert control over its information routing and information exploring properties.
*  And as Graziano emphasizes, right, you could build a system that solves a lot of tasks
*  where there are details in the quantitative and qualitative ways that information is routed and
*  information is managed. And the model of that process of information management that perhaps
*  becomes the model, again, that underlies awareness is very different and very absent.
*  So my awe comes from believing that, well, as Graziano certainly admits, the details of any
*  early and bold theory like that will not all be correct, that there probably is a theory like
*  that out there that will make sense and that will describe how this specific version of biology and
*  computation that evolved in this planet creates some of the more nuanced features or some of the
*  features that are layered on top of computation that Graziano's and others' worlds make life so
*  special and so lovely. And so to actually believe that, I never thought, it's the work of other
*  people that I just read, but I never thought that those types of questions would be accessible
*  through anything that really looked like neuroscience, computational or otherwise.
*  And I feel very differently now. And so, yeah, more and all having more fun.
*  Oh, and more optimistic.
*  Yeah. Well, I guess, is that optimistic? It's interesting also. I mean, this is
*  going straight to consciousness. So here we've done it before lunch already. Some people would
*  say it's not optimistic in that it takes the magic away. But others would say maybe it helps you
*  appreciate and believe in the magic and savor it more. Yeah, that's more philosophical.
*  There is the consciousness. Yeah.
*  Yeah. Well, I was going to ask you if you like, oh, okay, are you saying that you buy the attention
*  schema theory? But what I meant, I didn't mean optimistic in terms of solving consciousness or
*  something. Just optimistic in terms of your daily. Okay, right. So when I got into neuroscience,
*  well, the brain is impossible to understand because it's so complex. That's a very pessimistic
*  viewpoint, right? But there's so many open questions. You can work on almost anything.
*  Yeah, you can have a career.
*  So I'll get into this. Right. And now I still feel, God, so there are these new tools like
*  dimensionality reduction, like what we'll talk about in a moment. I'll bring us to that.
*  And then, you know, and these dynamical trajectories in state spaces. And I start
*  to feel like, okay, like, and you know, principles of universality. Oh, this is like getting us
*  toward a different kind of understanding than I appreciated we would be able to have or that I
*  would be able to absorb anyway. And now that they've sat with me for a little while now,
*  I'm questioning, oh, man, is this what does this really buy us? So I kind of have this back and
*  forth with optimism and pessimism in terms of making progress. And what you were just saying
*  sounded like your optimism has increased with your sense of awe.
*  Yeah, mega completely. And I think that, you know, a I'm sure I'm being naive in many ways.
*  And there are lots of features of anatomy and neurophysiology that I don't know. I mean, like
*  shocking level gaps in my knowledge. So some of this is probably naive. But the trajectory that
*  you mentioned, Paul, is one that I absolutely share. Right. Like, you know, I've loved and
*  felt really lucky to be doing the work that I've done and tried to do and work with the people I
*  have from day one in this field. Right. In day one, we were looking at very simple computations.
*  They were still like incredibly interesting and still study today integration, summation of
*  information over time. Right. How does that work in neural circuits? Again, building on the work of
*  many other people as well. And I thought that that and like basic studies of, you know,
*  is there a code that breaks the chaos in the brain and makes it look like it's less irregular
*  than you thought? You know, what does this type of coupling do to make things more or less irregular?
*  That those types of questions is where I would have a very satisfied at the time and happy career.
*  And that has totally changed. I think that it is possible for people like me and our group to take
*  a shot at questions that at any level, and we're going to do all sorts of stuff that's ridiculous
*  and wrong. But I think that it's a serious endeavor now. And it's an endeavor that, you know, is
*  incredibly inviting. And so, yeah, I'm optimistic that, you know, there'll be 100 years of work in
*  these directions and there'll be incremental lots of wrong turns. But it really feels like the
*  questions are on the same road that we're traveling now. Whereas before I was like,
*  that's another time. That's 300 years down the line. And that's for people who can think
*  completely differently. So yes, optimistic and happy. Okay. Okay. All right. Thanks for
*  answering those. I want to talk about some of your specific work a little bit if you're up for it.
*  Let's give it a shot. Yeah. So a lot of what you do is study the dimensionality of systems.
*  And just give us a little bit, you know, kind of a high level. Why is dimensionality important
*  to study? Yeah. Yeah, no problem. So one way to think about that is just the number of degrees
*  of freedom that a system has. And so we can go straight to neurons, right? Think about a
*  a brain that's just a line of one, two, three, four, five, six, seven, eight, nine, ten, ten
*  neurons. The question, does every single neuron get to do its own thing? Right? Is it fine? Let's
*  give our neurons names, neuron Eric, neuron Paul. Can I do whatever I want completely independent
*  of you? Right? Can I? Or are you so strongly connected to me that whenever in your inhibitory,
*  you've had enough of this interview, as soon as you get really active, you make my activity go
*  down. So we are absolutely not independent of one another. Right? What you do, I do. We might as
*  well just be one thing. We got one degree of freedom. Paul's in charge and then I just follow
*  him around. Right? So if Paul's completely in charge and maybe Paul's in charge of all of the
*  ten neurons, then you'd say that that system is just one degree of freedom. It's whatever Paul
*  feels like doing. And one degree of freedom means one dimension, right? It's a one dimensional brain.
*  Paul is really our only neuron effectively. I'm fine with that brain. That's a great thing.
*  You're fine with that. Right. Okay. And brains, weirdly, might be sort of fine with some version
*  of that as well. But if instead everybody can do their own thing, then they can do a lot more
*  stuff. Right? Obviously. Okay. So the first reason people care about dimensionality,
*  right? It's degree of freedoms and simply how many different states a system can be in. If every
*  state of a system results from thinking about something or representing some particular piece
*  of sensory information, then if you can do more stuff, right, you can think about more stuff.
*  You have more degrees of freedom or represent more independent pieces of information. And I think
*  most people will see quickly that that is a very, very, very dramatic explosion in what we can call
*  capacity of the number of things that can be represented in a system that has full dimensionality,
*  that doesn't have Paul ruling everybody. Neuron number one, say it can be high or low state of
*  activity, right? Or maybe 10 different states of activity in between. Okay. Then it can do 10 things.
*  Neuron number two can do 10 things as well. Right. But what is the combination? Well,
*  let's say neuron number one changes its 10 different levels of activity in one direction.
*  Neuron number two changes its 10 levels of activity in another direction. Each of them can do
*  whatever they want. Then the space of possible states of the brain is one direction plus another
*  direction makes for a square, right? 10 square different possible states. Fill in the blanks
*  right in between my fingers for the number of possible things that the brain can do.
*  Add on a third neuron. Well, that forms a cube in another direction, 10 cubed, a thousand different
*  states of activity. By the time you get up to a hundred neurons, right, which is a billionth,
*  the number of neurons that we have in the brain, you have 10 to the hundred different possible
*  states of activity, which is more than the number of atoms in the universe you see it, right?
*  So dimensionality, right? You always have to go to the more than the number of atoms in the universe.
*  Right. We can end the interview at this point, right? So dimensionality controls whether you
*  don't do anything except for what Paul says in one extreme version of one dimensional brain.
*  But if you, you know, take off that tight lid of control, the capacity of a system can rapidly
*  explode, right? And so that's a basic reason why people are super interested in dimensionality,
*  is it's very closely related to the capacity of a system. And our brains seem to be, you know,
*  incredibly capable. So maybe one of the reasons is they have some sort of an efficient code or a
*  maximum entropy, sometimes people would call code, that exploits that capacity. And dimensionality
*  is a direct window into that. Is it a square? Is it a cube? Or is it just Paul's, you know,
*  one dimensional line of activity that's entirely slaved? But the interesting thing about dimensionality
*  is that you might think like more is better, right? Is that there are many reasons to think
*  that less is more as well from a computational point of view. I was thinking about this,
*  one of the ways that people often talk about this is in terms of navigation. So let's try that
*  experiment super quickly. So you are walking home from or you're walking to the pastry shop
*  in Paris on sabbatical or something like that. And as you look around, you're going to see samples
*  of the world, which are obviously images, right? A classic way that people represent images,
*  obviously, CCD camera or something like that is a bunch of pixels, line up those pixels into a big,
*  tall list, and you have a huge list of numbers, right? So the number of different possible images
*  that you can see is drawn from a very high dimensional set, right? So say with me here,
*  if you want a brain that can represent all those different images and details, right? Recall,
*  you know, is it raining? Is it not? Am I about to get flattened by a car? Am I homing in on
*  boulangerie number one or two or whatever? You want to keep all that detail. But what if you
*  actually want to navigate, right? What if you actually want to know where you are in the maze
*  of the streets or more generally in a two dimensional landscape that you're cruising around?
*  Do you really want all that detail, right? Do you want this insane, super complicated,
*  impossible to envision representation of all these different images scattered around randomly?
*  I turn my head to the left and okay, it looks sort of similar, but not really,
*  because now I'm looking at a car instead of a bakery. And suddenly, you know, my image is
*  somewhere else in this huge dimensional space. And that's what I'm seeing. I have no idea where I'm
*  at. Obviously not, right? You want a representation that's more like Google Maps that takes the super
*  complex image, right? Street view or whatever, and actually locates it somewhere that's useful
*  in terms of performing the task of navigation. And that would be like somehow squeezing this
*  super high dimensional street view, forgetting all the details and representing the point as the blue
*  dot or whatever it is on your smartphone screen, right? So that feels like an example in which you
*  want a very low dimensional representation. Somehow you want a neural network that is
*  squeezed out most of the dimensionality in the world and presented an actual usable two dimensional
*  map, right? So those are the kind of extremes, you know, more is better or less is better
*  that the concept of, you know, higher or low dimensional representation invite. And that's
*  a starting point for why a lot of people think that in a computing system, it's something that's
*  worth talking about. Well, let's take that example, right? So I like that example because to do
*  something useful in the world, like our motor output is like low dimensional, right? And our
*  behavior essentially is low dimensional because there's constraints on the affordances and
*  navigation. So we can just stay with that. So if I perform that low dimensional or that
*  dimensionality reduction to make it useful, so I can navigate to the pastry shop,
*  while I'm walking, I'm thinking and what I want is for so I have this, so to use the word capacity
*  earlier, and we have, you know, potentially this really large capacity. And what I want is for my
*  thoughts to be able to visit all of those spaces within that state space. And I don't want low
*  dimensional thought necessarily, even though it's useful for behaving in the world, right?
*  Wonderful. You nailed it. And they're wonderful. So you want the continuum, right? And I think you
*  said it beautifully. And that's where brain structure may and maybe brain dynamics may play
*  a role. So let's think about those two desired features, right? Like you certainly don't want
*  to become blind to the or unsighted to the visions of the complexities of the world around you as
*  you're navigating, right? And that doesn't happen, right? If you're a sighted person,
*  you're going to be able to write if I ask you, right, read the menu on the boulangerie or whatever.
*  But you don't want to always be operating in that super complicated space, right? And so as you know
*  very well, right, in many of your listeners and followers as well, right, you have the first
*  outgrowth of the brain, right? The first part of the visual system that's part of the brain,
*  which is the retina. And that probably represents things somewhat veridically, right? It is
*  absolutely not like a CCD camera. It has almost miraculous properties of dynamical transformation
*  and adaptation, but it still has a spatial array and a spatial representation of what you're seeing,
*  way higher dimensional than a 2D map. You get deeper into the brain, right? Where is it? Is
*  it hippocampus? Is it enter rhino cortex, right? And you have these structures, grid cells, right,
*  very famous, Nobel Prize 2014, which may be actually representing in some ways the map itself.
*  And then do you have a hierarchy in between, right? Nicole Rust and Jim DiCarlo, right,
*  maybe 2008 talked about visual representations in terms of disentangling, having details early on,
*  and then having representations. I'm not exactly sure if they were talking about
*  low dimensional representations, but representations deeper in that are easier to compute on, easier to
*  categorize, for example, deeper into the brain. So does this happen, right? Probably, I think,
*  right? So we're working on this from a theory perspective, but many people, including us,
*  have seen that you have a hierarchy of dimensionalities that emerge either in deep
*  neural networks, or my favorite example, actually, John Mounsell at Chicago pointed this out to us
*  when I was giving a talk about it. He's like, you've missed the coolest thing about your own talk,
*  which is that if you have a recurrent neural network, which means a system that's connected
*  to itself, that's doing processing of originally high dimensional and complicated inputs, right,
*  like these snapshots from the street that we're talking about, it turns out that once it's
*  trained to do something, categorize or help you navigate or help you predict the future or some
*  sort of task, that when an input image comes in, right, that initially that input image, well,
*  it comes in, it's copied into the neural network. And this transformation into a lower dimensional
*  map-like space is gradual, it occurs over time, maybe over, right, who knows what the time steps
*  are, or whatever, let's say, just throw out a number over 200 or 300 or 400 milliseconds,
*  something like that. So if you had a system that's looking even at just one brain area,
*  right, then it could titrate the level of specificity that it wanted by tapping into that
*  single brain area early versus late in a stimulus presentation. And when you couple that
*  with a hierarchical, you know, early visual system or whatever, to late visual system,
*  to hippocampal representations that we're talking about, I think we see that there's going to be an
*  opportunity for the brain to tap into the right level of dimensionality for the right computation,
*  and it may be organized in really cool ways over space and time.
*  So, you know, how do I phrase this? Hierarchy is a step, steps of abstraction, let's say,
*  especially, you know, the classic example is the visual, ventral visual stream, where things become
*  more and more abstract. And you're just talking about Nicole Rust and Jim DiCarlo and, yeah,
*  these untangling effects, and then you need these more and more abstract slash low dimensional
*  representations. But it seems, what am I trying to say here? It seems limiting. So
*  it seems like you should be able to have your cake and eat it too, to have
*  abstract, low dimensional structures, but then all of a sudden embed them in a very
*  high dimensional space. You nailed it. Oh, I nailed it. You totally nailed it because there is a very
*  important line of work that at least in my reading is coming from the laboratory of Stefano
*  Fusi at Columbia that is doing exactly what you're saying. It really is. Actually, I was thinking
*  about this a little bit last night. It really is the have your cake and eat it too theory
*  of abstract representations. It's exactly right, right? You could have a paper with,
*  I don't know, 10,000 citations or whatever the fundamental papers from the Fusi lab have based on,
*  you know, development of that idea. If you would have had it 10 years ago, that's exactly right.
*  So, so Fusi and colleagues have an alternate look at this, I believe. And we've talked a
*  bunch and I think the mechanisms may be very related. But what you really need, right, for
*  this Google Maps awesome representation that I'm talking about, isn't exactly a squashing. It's
*  closer to what you said, Paul, which is that you need a consistent arrangement, right? Let's have
*  my hand be the two dimensional landscape that you're navigating as you're going to the bakery,
*  right? But what about what's going on in the third direction, right? And in the brain, right,
*  if we're going to be literally, you have 100 billion minus two other directions that you
*  could be traversing out of the page if you wish or out of my hand. What's happening in this direction,
*  that could be completely flexible and it doesn't have to be squashed onto the plane.
*  What matters is that an image of bakery number one and a gigantic sign of an eclair, my dream
*  over here and the streetlight over there, these can be all over the place, right, in maintaining
*  their full information and all these other directions just so long as you have an operation
*  which could just look at where they are in the plane. That's sometimes called a projection,
*  but that's really, really easy to do in neuroscience. You just have to read out the
*  right, as you know very well, the right combination with the right strengths of all
*  the different neural activities. So as I read it, and I'm sure I'm oversimplifying it, the theory,
*  I think there's a paper, what is it called? It's like the neuroscience, like the best paper title
*  ever, neuroscience of abstraction or something like that from the Fusi lab. You'll see that
*  easily if you look it up, F-U-S-I. I think the essence of the idea is that what needs to be
*  consistent is a consistent direction of the meaningful low-dimensional coordinates
*  so that they can be consistently read out and interpreted. And squashing, running over everything
*  else with a steamroller, even if that's later in the brain or later in time, as I was mentioning,
*  is not strictly necessary. It's a great idea. And so I honestly don't know what happens, right? It's
*  a mechanistic question. I think Fusi and you yourself, Paul, have laid out the minimal
*  requirement, which is a consistent decodability, right? So that you can actually, with some
*  generality and some ability to learn from one situation and apply it to the next, you have to
*  be able to read out the key navigation, the key low-dimensional information, right? And is it true
*  that you just keep everything, right, and read that out? Or is it true that in certain brain areas,
*  you go ahead and squash everything down and make it even easier for yourself so you don't have to
*  look in just the right directions to read out the map information? I think, as usual, probably
*  both will be true in different brain areas, at different stages of learning, and in different
*  task scenarios as well, and different plasticity mechanisms. Thanks for asking that right on target.
*  It's a very important question. Well, I mean, this is, you know, it just goes back to my own
*  struggle and thinking about, you know, what do I gain from saying something is high-dimensional,
*  low-dimensional? Because if you could, like a projection, right, is like a low-dimensional
*  structure, but if it's embedded in high-dimension, like if you measure it one way, it's going to be
*  low-dimensional, but it could actually be high-dimensional if it's used in a different
*  way. Or if it, you know, that's right. So then, so like, for instance, let's talk about your work
*  on motifs, right? So you're interested in, and I don't know how you came to this, and you can tell
*  me the backstory here, but you came to be interested in asking whether by looking at very
*  local structure, local connections between units and their directionality and the patterns of those
*  connections, if you could see like a percentage of local connections that was two by two, and that
*  was, you know, one to another neuron, etc., those kinds of patterns, then you could predict the
*  dimension, at least to some degree. So how did you come to ask that question? And then,
*  and then how far have we gotten? Yeah, that is such a wonderful
*  line of work in my own life, and that it was just so enjoyable and so surprising.
*  And I'm so glad that you asked about it. So the answer really does start with, with, with dynamic,
*  sort of where we started our conversation with the basic principles about how it is
*  that a law, right, a dynamical law that tells you what neural activity is going to be tomorrow or
*  the next time step based on the neural activity today, what that dynamical system, how that
*  dynamical system is unfolded over time to actually make its prediction. So again, you've got a law
*  that says, you know, given how everything is now, what's it going to be the next time step,
*  and you unfold that over multiple time steps to predict the future, right, the magic of dynamics.
*  Now apply that concept to a network. And imagine that we have you and me or two neurons again in
*  that network, Eric and Paul, right, with some chance we're going to be connected to one another.
*  Let's say we are, there's a direct synaptic connection between the two of us. What's going
*  to happen to you on the next time step? Well, you're going to take your state of affairs,
*  right, your level of activity or voltage, and you're going to update it based on your own
*  dynamics, but also based on the influences that you're getting from other cells that are one step
*  away in the network. In other words, everybody who's connected to you is going to influence you.
*  Seems as simple as pie, right? What's going to happen the next time step? Okay, well, on the next
*  time step, right, let's say there's another individual, my son Milo, who's connected to me
*  as a neuron, right? Well, in the meantime, while I was influencing you, he's going to influence me,
*  right? So on the next time step, right, I'm going to influence you based on what Milo did to me,
*  and you're going to feel the impact of something two time steps away. Okay, so this process
*  continues. And as you look further and further into the future, if you wish, your activity as
*  a neuron Paul is influenced by other cells or other neurons in the activity in the network that
*  are more and more steps away. One step after one time step or one connection after one time step,
*  path length two after two time steps, so on and so forth. Now warp all the way to some steady state
*  of the system, right? You weren't born yesterday, right? Your brain's been doing whatever it's been
*  doing for some period of time. And it is at the state of activity that it is when I measure from
*  it and estimate the dimensionality of your brain, right? How many different path lengths have
*  contributed to the activity of all the cells? It's been a lot of steps. So it's been a lot of paths,
*  right? So basically any quantity that you want to look at in a network dynamical system can be
*  decomposed into the influence of steps or paths through the network of gradually increasing length,
*  right? Every path of what's a motif, a motif is some sort of structure in a network that has some
*  length. It's a path of a particular length. The simplest motif for just me and Paul is a connection,
*  an arrow between the two of us. That's it, right? But if we have me and Paul and Milo over here,
*  just envision this for a second, connected in, right? Then you could have a chain, right? That
*  connects Milo to me to Paul as it did in our example, or you could not have that chain. And
*  if you have a fourth member, you can start to imagine cool diamond-shaped patterns and many
*  other things. These are the motifs. So these are different paths that could enter. And you can
*  immediately see from this discussion how basically any quantity that you want to write down in a
*  system that's evolved for a long time can be expressed somehow about the activity in terms
*  of the activity that reverberates along these paths of different lengths. Somehow. Right. And
*  somehow is the key, right? Because when you start to write down these quantities, you see, right,
*  we went into infinite time that there are lots of these paths, right? And if you, so infinite time,
*  sorry, into a steady state, right, it's not going to be limited to like paths of length three, path
*  of length five or whatever. And this sounds like it's more of a mathematical commentary than a tool
*  that you can use in practice. And to be honest with you, this is why I like this sort of
*  intellectual history or whatever, this subject, at least in our working group, is that's as far
*  as we could get these ideas ourselves. And me and my peer level collaborators like Krusha Josick
*  in University of Houston and Brent Duanrond now in Chicago, we got to this point where like,
*  that's pretty interesting. There was another group in Germany, Rodder, Stefan Rodder, who got to about
*  the same point independently as well. Anyway, so are my colleagues and I and other groups independently
*  got to this point, which you said somehow, right? That's fun. The big expansion of basically any
*  network dynamical property in terms of paths of different lengths from the network, which you
*  can identify with different patterns or connectivity motifs somehow. And the list is long and it seems
*  intractable. This is where we looked at the somehow thing and couldn't do anything ourselves.
*  But this amazing second year, I think at the time, applied math PhD student named Yu Hu, who's now a
*  professor, sometimes Hu Yu or Yu Hu, depending on the continent that you're on at HKUST, Hong Kong
*  University of Science and Technology. Yu Hu looked at this huge sum over all these or this big
*  combination of our paths of different lengths and saw how to tame that giant list of paths of gradually
*  increasing length, which again is somehow impossible to deal with, saw how to reorganize that.
*  So we could build up and predict the influence of these very long paths from the short paths.
*  So the entire theory in the end would be predicted by what is happening or what the short paths were
*  that were present in the network. So we can do any of this. This was hopeless. But then Yu Hu came
*  and when he was a second year student, figured out how to tame this zoo of different paths into
*  an organized theory. And that's how it happened. And so this is a case where it's like pure.
*  So forgive me if I'm missing some of the other work that you've done. But I'm thinking of in
*  terms of applying it to actual brain structure and testing it against a connectome, for example.
*  Is this a place where we have where neuroscience is limiting what we can infer about these theory
*  based approaches? Because you do some averaging and there are some tricks and assumptions that
*  you make to infer. And then you can measure it in the network. But then if you applied it,
*  is there experimental data from the brain? And I think so. So this is work. There's a long story.
*  It's a 10 year story. So Yu Hu figured out how to do this computation in 2013 and now it's 2023.
*  And I think we have done the best possible job and maybe in our hands for the first time and
*  actually convincing in real job of testing these theories based on living brain data and vivo brain
*  data. And so the lead contributors are David Daumann at ULIC in Germany, J-U-L-I-C-H and
*  Stefano Rattanatese here at the University of Washington at the Allen Institute. And what these
*  colleagues did was thing one, right? Let's try to see, right? We said these motifs or these paths in
*  a network are supposed to be predictive of any statistical quantity that, as you rightly said,
*  can be averaged across the network. One of those quantities is dimension, right? So let's write
*  down some formula for how strongly basically Paul is controlling Eric and everything else to the
*  number of degrees of freedom in the system. And it turns out that that once again can be written
*  in terms of these paths. Okay. Then you use the ideas of Yu Hu or new versions of them that are
*  computed using different mathematical techniques by David Daumann and Stefano Rattanatese.
*  And those things tell you that, again, depending on how many short types of connection patterns
*  you have in the network, how many connections there are between Eric and Paul, but also how many
*  diamonds, how many triangles, how many whatevers in the network, you should be able to predict the
*  dimensionality of the activity. So how do you actually do that, right? Well, let's just take
*  the Allen Brain Observatory right here at the Allen Institute. That's where I'm sitting right now.
*  I'm proud to be here on sabbatical. Right? So stupid of me to ask that question knowing
*  where you're sitting. Yeah, yeah, no problem. But anyway, it's a gigantic, totally open source.
*  It's actually amazing. It's something to talk about later. Selflessly shared resource, which
*  is very large scale recording. Look at it, count the number of degrees of freedom one way or another,
*  figure out what it is. Right? And then the Allen Brain Observatory led by Stephanie Seaman,
*  Tim Jarsky, Luke Campagnola and others also have a massive, also open source resource called the
*  Synaptic Physiology Resource or Synaptic Physiology Database. And from that, you have
*  the motifs that are present statistically among neurons of different types in these same brain
*  areas from which the recordings are done. Right? So it sounds kind of good, right? You've got the
*  parts list in terms of the connection patterns. You know what the dimensionality is. The question
*  is, does that parts list predict the dimensionality? Right? And you can probably see the problem.
*  Do you have absolutely everything that you need in that parts list to get to a number that the
*  dimensionality is? And the answer is no. There's going to be something else like the overall
*  input to the network or some sort of overall scaling factor on how strong, something like that,
*  that is going to keep you from being able to make a quantitative conclusion. So you could
*  be stuck or you could be Stefano Ricanatessi, who had the idea to break up this ongoing
*  brain recording into different discrete states of activity, which he discovered, following ideas
*  that are also prevalent in other groups via some sort of partitioning method. And then
*  that was the key because you had dimension number one and dimension number two at different points
*  in time. And the question is, can you predict the direction of this change from the direction,
*  from the motifs or from the structure of the network? And you might be saying, what are you
*  talking about? Right? This is one network. This is one set of neurons at different points in time.
*  Why are you telling me there's a different network? There's not a different network. It's
*  the same brain. That sounds like garbage. But the point is that the effective network that's present,
*  that's actually driving activity in the network, is going to have to do with which neurons in the
*  network are actually active at a given point in time. And that switches across time. And that
*  seems to switch in a discrete way. And that also switches in a way that corresponds to genetic
*  and anatomical labels for different types of neurons. So you could really say in this period
*  of time, it looks like it's network A composed of this dominance of one type of cell type.
*  In this window of time, it's kind of like network B. Go back to the synaptic physiology database
*  and construct networks made mostly out of neurons of type A or mostly neurons of type B. Of course,
*  it's much more complicated than that. They're just different mixtures of neuron types in the
*  two cases and see if the motifs point in the right direction in that case. And it seems like they do.
*  So that's a little bit convoluted, but it looks like you're able to follow. It's not convoluted,
*  actually. But it shows you that it took a decade and it took the right approach to be able to
*  have an experimental setting which controlled for things that you could not measure and got
*  to the heart of the matter. And it took this cell type specificity, years of work with genetic and
*  anatomical work. It took these very large scale recordings, which would actually enable you to
*  identify different periods of times where it's likely that different sub networks of cells were
*  active to be able to design an experiment or really enact post facto, we can say, the beauty
*  of these large scale databases and their great utility. But to design an experiment, let us say,
*  are enact an experiment which would actually enable you to test the theory. So it took 10
*  years, but I think it's doable. And there will be other clever approaches. There are many being
*  taken now that actually try to make the connection with living or in vivo data to the underlying
*  network structures. It's a blessing and a curse. And you can disagree with me to have these
*  huge databases, experimental, but also these huge models. And I say, so it's a blessing
*  because then you can model almost anything you want. And it's kind of a curse because it's
*  somewhat disappointing to think, oh, I have to consider the 100 different cell types that are
*  in the network to get a grasp on what the network is doing. What can I really say about what I
*  understand about how it's operating? And I guess that's where these kind of principles,
*  these theoretical principles maybe is what you're going to say, come back. And that's what we need
*  to feel comfortable understanding. Well, I think that there are two aspects to that. I think you're
*  right that the theory is the sort of cheese in the sandwich there. But the bread really is the
*  question that you're asking. So we started out early on talking about what you could learn from
*  networks with only two types. And it turns out you mix those two types into the pot and you get this
*  amazing activity, which looks irregular, but which also can carry very strong or repeatable signals
*  if you combine the cells together, right? The balanced state theory. In our case, what we wanted
*  to do was understand whether there seemed to be evidence for a structural relationship in the
*  shape of connectivity patterns in a brain in terms of constraining the activity, how much Paul was in
*  charge, how much the dimensionality was being changed. And in this case, we had maybe three to
*  five different cell types that we were able to resolve in the synaptic physiology database,
*  right? Which means, right, it's five cell types, which means that, you know, as you said, maybe
*  there are a hundred different cell types who knows every one of those cell types maybe has a subset
*  of 15 or 20 different cell, whatever. But that level of granularity was enough to be able to
*  identify, at least according to our hypotheses, what the different sub network, what the different
*  networks were, network A, network B in that case. And it turned out that that included enough
*  information to provide with whatever caveats probably still remain, but a test of the question
*  that we had, right? Which is once again, you know, do these local connectivity structures actually
*  control dimensionality or not, or is it something else? So I think that what's cool, right,
*  is the role of theory. And that was the point of your question. And the theory will, I think,
*  be key in letting us know what the level of detail is that we need to answer a question,
*  which comes from general neuroscience, which doesn't really come from math. It comes from
*  just thinking about the brain. Yeah, so it's super daunting. I agree. But, you know, just like,
*  as you know, as I was trying to mention in the historical examples, we can titrate the level of
*  complexity that we need to answer the questions, right? And we did have to turn up the dial,
*  right? If we would have just looked at excitatory, inhibitory, or just like homogenize all this
*  activity together over time, we would have been nowhere in terms of being able to actually test
*  the theory, or really, who cares about testing the theory, testing a concept. Yeah. Yeah. I mean,
*  you know, going back to like the early days of connectionism, and you were mentioning earlier,
*  you know, who, no one who thought that that would work, right? Except a handful of people.
*  But then, you know, looking back on it, well, it's the obvious thing to do. You know, if you,
*  our brains are kind of structured like that. And you're taking like what we know about our brains,
*  it was just neurons connected, right? And but looking at it from here, we have all this
*  biophysical detail, all this knowledge, right? And it's we're not just point neurons connected.
*  Exactly. And so, like you mentioned before, it's amazing how well it works.
*  Exactly. But in some sense, I can look at it, conceptualize a connectionist model and think,
*  okay, there's a transformation. But then you add these biophysical details, these types of neurons,
*  we're going to talk about neuromodulation in a little bit, hopefully, and astrocytes and,
*  you know, recurrence and all these different organizational nested hierarchical structures.
*  And then all of a sudden, I can't understand it anymore. And so I guess that's why I was asking if
*  you know, these theoretical principles are going to be the key to the understanding part.
*  Yeah, I think maybe right. So there are two aspects, right? Again, once this this motif
*  theory and again, you whose way of cracking the expansion and developing the simplified theory,
*  that's helpful, right? Because it tells you that all you need is to summarize this incredibly
*  complicated connectivity. What you need to sort of excuse me, summarize a very complicated
*  connectome of all kinds of different connections among hundreds of different cell types or whatever
*  is you need to count, right? How many different structures of this square and diamond and triangle
*  shape and whatever happens. Now, it would still be pretty stressful if you had to deal with all
*  100 different cell types, right? That's a lot of triangles to try to do. But then you can do
*  collapsing, right? You can say, well, in terms of the dynamics, right, if this is an inhibitory cell,
*  it's going to serve me up this many triangles that are involved in sorry, inhibitory cell type
*  that involve inhibition. Here's another inhibitory cell type that's going to serve me up this many
*  triangles. You know, when you unroll the dynamics in the system, right, the genetic labels of cells
*  are not speaking directly to the fast time scale kind of, you know, activity patterns that are
*  produced. You can group those two things together, right? So your ingredients list can become simpler.
*  And I think that the theory, you know, you start with a question in many cases. And again, the
*  theory tells you what types of groupings you can possibly make or you seem justified in making.
*  And in the end, right, in terms of knowing whether you actually understood anything about the brain,
*  like anything, we can't escape the scientific method, right? This is very complicated or very
*  complex, very beautiful and interesting. Also, I think hypothesis building, right? And so finally,
*  after all this, right, you build a hypothesis that in state A versus state B, the dimension should
*  be higher or lower controlling for these different factors and you have to go in and test it. But I
*  shouldn't be that glib, Paul, because the quality, you know, you say you get the answer, yes, right,
*  still in interpreting that answer and what you really learned about the brain, right, you do
*  have to unwind that theory and ask yourself how much you believe it and test that theory. And so
*  that's my job, I think, as a theorist and a modeler is to, you know, always be there in winding up
*  the concepts in order to make an actual testable prediction, but be there also to,
*  in collaboration with others, unwind and challenge those, the high, the assumptions that went into
*  forming that hypothesis and see where they break so that the thread that we thought
*  may not actually lead from point A to point B in terms of the conclusions that we're trying to make.
*  Yeah, so it's not as simple as we can try and simplify, but if we're screwing it up,
*  we're going to be misleading ourselves and so we better stay engaged, we better stay humble.
*  Isn't it tempting though to just, because the work that you're doing is beautiful for its own sake,
*  right? So then I can see how it would be tempting to not worry about tying it back to the brain,
*  because it's interesting on its own in principle. But you seemed hell bent on applying this
*  to the brain. Yeah, it's an interesting comment actually, you know. Yeah, well, I am because it's
*  deeply enjoyable and it gives extra layers of meaning, you know, and as we were talking about
*  earlier, right, if it's we actually believe, who called it the astonishing hypothesis?
*  That's Crick.
*  Right, Crick or something. I didn't read the book, so I may be misquoting, but if we actually
*  believe, right, that this incredible feeling of being ourselves and this human experience arrives
*  and really non-human experience as well, no question in my mind,
*  right, arises from this biological machinery, then that's motivation in itself. If you can be
*  a part of explaining that and celebrating that and having that influence, maybe the way that we live
*  that is well worth doing. But I think your point is very well taken and I think there's,
*  it is really fun to just like get on a blackboard and if you're at least you who, which I'm not,
*  you know, derive a blackboard full of what he called motif cumulant theory, you know, pose what
*  is a new take on a, I think a branch of mathematical theory, of subgraph theory, write awesome papers
*  about it, state it as theorems. These theorems are beautiful, right, if you're mathematicians,
*  which I'm not, but who I admire, right, have been, you know, celebrating the sheer beauty of
*  mathematics for millennia, why not just do that, right? And I think what's important for us is,
*  a field is to make space for people who want to just do that, right, to be able to bring in these
*  ideas and people who feel the way I do or we do, to be able to act as interpreters and conduits
*  of information and let everybody do the science and do the mathematics that they want to do.
*  And some of us will try to serve, right, I didn't come up with this idea of motif cumulants, I
*  couldn't, I was stuck, right, but somebody else who had a stronger math background and abilities
*  than me could get it, right, even though they were half my age or whatever. And so let's just do that,
*  right. We see the same thing, I'm sure you see with many of the issues that you follow in society
*  and many of the younger people that you follow right now with sort of brain inspired, I wouldn't
*  say sort of brain inspired, I'm gonna say totally brain inspired computation. I'll put myself
*  on that lens, you know, playing out in industry and very important applications and government
*  and society, everything else. Can I just do this, right? Do I really have to always refer to some,
*  you know, genetic database and try to understand whether this matches up with real cell types?
*  So my students say this too, and I respect it, right, like this is so much work to try this,
*  you know, try to tie this rigorously to the brain. There's so much development to be done in terms
*  of the engineering side, the application side of this. Can I just do this? And the answer that
*  I have to give if I'm a reasonable mentor, you know, and follow the philosophy that I applied
*  to applied math on the engineering side, right, is to say, yes, you can just do that. That's great,
*  and I'll be here as a conduit, you know, if I can, or if I have the time still at midnight or
*  whatever to try to pipe some of these insights back in and some will come in and some won't. But
*  yeah, it's, it depends, it is tempting. And I think that we need to let people as they wish,
*  you know, yield to that temptation, just as we get to yield to the temptation, you know,
*  in many flawed ways, probably to, to try to, you know, be the ones building the connections.
*  Okay, all right. Are you do you have a rich brain or a lazy brain?
*  Yeah, I don't know. But I do know that, like, not knowing the answer to this question,
*  you know, led us to, I don't know, maybe mistakes, but but definitely a lot of confusion
*  in our own research trajectory. So I think, you know, we're talking about so well unpacked
*  those concepts in a second. But we were talking about universality, right? You know, you might
*  learn dimension might collapse to make your awesome Google Map or whatever, like, does that
*  actually happen or not? Right. So when we saw this happening, it was through simulations that were
*  done by Stephanie, we're kind of Tessie also in Matt Farrell and many other colleagues,
*  others involved with the university. Actually, Merav Stern had the first key insights perhaps
*  in our group in this direction as well, Merav Stern, and the first results in some ways.
*  Anyway, so these very bright individuals, you know, would see a collapse in dimensionality
*  across stages of learning. Okay, who does that always happen, right? And they were like, we're
*  gonna go nuts on this. I start giving talks about this is so interesting. This is mechanism
*  for building the Google Map or whatever, let's go nuts on it. And then suddenly, you know,
*  we're editing the proofs for the paper or something like that. And Matt is like, Eric,
*  this doesn't really happen that much. Like, what are you talking about? This is a theory. I just
*  get talking from 1000 people celebrating this. And it turns out that that he's absolutely right,
*  right. And there's a theory that he was aware of this rich and lazy learning theory that predicts
*  this and other phenomena, which is saying that there are two different ways that you can learn,
*  right? You can learn by basically having to is I see it, which may be inaccurate, but this is my
*  best shot at it, you can have a very complex brain that's doing all kinds of awesome transformations
*  on inputs. So that based on this wonderfully transformed input with all sorts of different
*  pre computations applied to the input, all you got to do is reach in and pick out the quantities
*  that you need to perform the task at hand, leave the big brain processor. Sometimes people might
*  even in older literature, call it a reservoir alone and pluck out what you need from it, right?
*  People would call that lazy learning. You still do the task, but without really shaping in a strong
*  way what the brain or the main body or whatever the brain is actually doing. Or you can have a
*  rich regime and what you learn a task and that changes the computations more or less all the way
*  through. We were working in the rich regime, which is where all kinds of stuff happens, right,
*  which is where you really see the signatures of learning throughout the brain. But it's also
*  possible to initialize the system or put other constraints on the system so that most of the
*  learning happens without you actually being able to see the signatures of that. So I don't know
*  what kind of brain I have, but I have a brain that's richer to go for a quip to answer your
*  quip like question for actually knowing that there are two different possible regimes. And
*  and we're we again, another example of needing to be humble. You think a phenomenon is universal
*  and it's not, but here's again, just a hopeful message at the end, right? How come, you know,
*  Merave Stern independently, Matt Farrell, other people, and then other people around the world,
*  Donahoe Group and also the late Neftali Tishby were seeing very similar things.
*  Donahoe Group at Stanford, how come all these people were seeing this sort of squash of
*  dimensionality, right? That indicates, right, we're all operating, we must have been in the rich
*  regime there, right? But that means the rich regime also has to be a big regime, right? It's
*  not like there are like 80 billion different regimes in which different quantitative things
*  or qualitative things happen. There's probably a continuum between rich and lazy and the rich
*  kingdom where you would see reasonably systematic changes is fairly large. So again, you know,
*  my brain's richer because it needs it means it needs to be a huddle, a humbler and more,
*  you know, systematic. But it's not hopeless in that, you know, it's a if we wish a single
*  navigable continuum between these two states, perhaps, at least from the perspective of
*  dimensionality. Let's so and I don't know if I'm gonna ask this in the right way. I want to bring
*  in the concept of latent variables and apply it to rich versus lazy. So if in a rich regime,
*  where there's all sorts of changes and learning going on in the network, presumably you're
*  learning these latent variables that have some meaning in that they represent well, the structure
*  of let's say the task that you're doing or the bakery that you're looking at, right? And so you
*  can say you can map on some there's some structure in the quote unquote latent variables in the
*  representation in the network that has formed over time, let's say, or takes on a form.
*  What so and presumably in a lazy network, which doesn't need to change doesn't change,
*  right? Just input in it's like chaotic. Anything can go in, you can pull it out
*  with some readout weights, like a reservoir computer or whatever. Then presumably, you'd
*  still call whatever that was happening inside the hidden units, a latent variable, but it
*  loses some meaning. Am I describing this in a way that makes any sense?
*  Yeah, you're doing a great job. And I think the you're absolutely right, right? If you're able
*  to do the computation, you're able to extract the latent variable. And in that sense, it is there.
*  And I think the question is, is it immediately present right in the neural activity in the area
*  in which you're studying? Or does it require a linear transformation just sorry for the jargon?
*  Does it require just finding particular weights or directions that you should look in that space
*  to identify that that latent variable? Or does it require a very complex nonlinear transformation,
*  right? Which says that, my those latent variables are in there somewhere, just like they are,
*  by the way, in the images of the bakery and the images of the street scene in Paris, right? The
*  latent variables must be there somewhere because that's all the data there is, right? These
*  different pictures, right? There is some path that connects these different complex images together
*  in a two dimensional space or in the space of latent variables that's of interest. The question
*  is, how much work has a given brain area done for you in extracting and presenting those latent
*  variables to you on a platter, right? And how much work remains for you to do yourself? And
*  that's a really interesting question about brain areas and segregation of function that I think is
*  far from resolved. Okay. Yeah. And different brain areas will be on the different areas of the
*  spectrum of rich versus lazy. And it's just another dimension we're going to have to consider,
*  like in terms of studying the brain. Right. Right. But again, I think the hopeful point
*  is that you're right that these are all dimensions and you're right also that,
*  like we were saying before, you add more dimensions and then you explode in terms
*  of the number of possibilities that you need to study overall. So we shouldn't take this lightly.
*  But the hopeful perspective is that the list of considerations that you're mentioning here
*  is going to be a handful of different general principles. And as the theory develops further,
*  we'll see, oh, rich and lazy is the same thing that somebody else meant by fast and slow or
*  something like that, or like, oh my gosh, it seems like there are lots of different factors that
*  control whether you're rich and lazy. But actually they can be grouped together. Helen Olu and our
*  group is working on this somewhat by the effective rank or some sort of other mathematical property.
*  So I think there's going to be a gradual expansion in growth in terms of the dimensions
*  of subtlety in terms of building a theory of learning and dynamics in the brain,
*  in the brain. But there's also going to be work by theorists like Helena and others to try to
*  tame that. And we'll see if it grows out of control and causes us despair before
*  bright young people manage to tame it. Okay. Very good. So maybe in these final
*  few moments, I can ask you some just kind of broader questions. So we've talked about
*  all the assumptions that go into the modeling and how you have to, at the end, you have to unpack it
*  and think about what it all means in terms of how brains function. Are there assumptions that worry
*  you more and assumptions that worry you less like linearizing a non-linearity, stripping,
*  what assumptions give you the most pause or worry? Yeah. Yeah, many. I would say maybe my top
*  two would be that the learning objectives, right, which we're applying to our network models,
*  that's classified stuff, let's learn how to navigate in some fixed arena and otherwise
*  stationary conditions are just way too simple, right? They're simple minded in terms of their
*  construction and they're also simple in terms of assuming that the whole teaching environment,
*  right, people would call the supervised learning or whatever is constant over time. You always
*  have somebody giving you ideal exemplars against which you can compare your outcome.
*  I think another major concern, so I'd say the whole learning environment is too simple or it's
*  misconstrued in much of our work. I think ignorance of anatomy is particularly catastrophic
*  in my world given my background and is a big area of weakness in our work. That's really thinking
*  about what to a real biologist, which I strive to be, but I'm still in beginning student mode in
*  many ways, what to a real biologist would be obvious features of brain anatomy. You have a
*  thalamus, right, that is a bottleneck for thalamic cortical computer interactions.
*  You're doing well with the anatomy here. Right, but thank you very much, but there are also
*  direct pathways that bypass the bottleneck. So actually you don't have one pathway between
*  them two brain areas. You have two and one's a bottleneck. Those must be doing different things.
*  Why is it in none of your models after 25 years of calling yourself a computational
*  neuroscientist? That's kind of ridiculous. I think that while we may be excited from a theory point
*  of view about some of the concepts that we have about cell types or whatever, we may be skipping
*  the first five chapters in a textbook and missing really key features of brain anatomy and missing
*  the point in many ways. So those are two of many weaknesses, I think, in our approaches.
*  Is there something that you would love to have from experimental neuroscience that doesn't exist
*  yet? And or you could answer just what's currently holding you back in general?
*  Yeah. Great. Let me take the latter because it does feel like from an experimental neuroscience
*  point of view, right? There are so many things we could ask for, longitudinal recordings with
*  single cell resolution across stages of learning. A lot of that is happening, but I want it on a
*  fast time scale. So I want it from whatever. But I feel like the tables have turned so fast. You've
*  seen this in your career too, Paul, where it used to be that the theorists were always dreaming of
*  different ways of testing their ideas. And maybe this experiment will come about in 50 years,
*  but I'm going to do the math anyway. As you know, many people have said this,
*  in the last decade and a half, everything's switched, right? And the data is now running
*  ahead of the theory. And so I think I feel like I want to try to take advantage of the experimental
*  results that are there. And I'm so obsessed and feel so inadequate perhaps with doing that,
*  that I'm hesitant to answer the former question. In terms of what's holding me back, I mean,
*  it's lack of knowledge of all these things that I mentioned. I mentioned anatomy. Another one that
*  I wanted to mention is cognitive psychology. Man, again, I'm at the popular science level with a lot
*  of this stuff. I'm just reading or listening to some of the work of Kahneman. And it's so intimidating.
*  I mean, it's amazing, but it's also intimidating to know that there's like a century, right,
*  of quantitative experimentation with very detailed, very systematic behavioral features
*  that are large and that they're consistent. And I don't know them, right? And especially as we go
*  maybe towards some more complex decision-making tasks that are closer to reinforcement learning
*  and some of our future work, trying to proceed on like theories of mechanistic theories of
*  decision-making, mechanistic theories of neural circuits in that context without knowing a hundred
*  years of psychology feels to me like it is either dangerous in terms of missing the point or just
*  perhaps missing the opportunity to really ask the right and the big questions. So there are just so
*  many different fields and I need to build, you're never going to learn them, right? So you have to
*  build collaborations and connections and I need to reconnect with psychology and cognitive psychology
*  and get mentors and collaborators and students and people who are willing to work in that area. And
*  there are so many things that are holding me back, but that one that I'm really realizing recently
*  is at a crisis level. It doesn't feel like, so you just listed a ton of things holding you back.
*  Doesn't feel like anything is holding you back because you have your fingers in a lot of pots.
*  Is that the phrase? You're like a dog in a... I'm not sure what the right expression is, but
*  you are doing lots of amazing work. I really appreciate all your time here.
*  And your humility is also just, I just admire it and I could go on. And just your memory for all of
*  the references. Jeez, man. Do you have an internal... Do you have a prosthesis,
*  like a machine learning prosthesis helping you there?
*  Well, I don't think so, but we talked about this a little bit just as we were getting set up
*  before the interview. Science is like, this is fun, a circular thing. We can say, okay, this is
*  a scientific community made up of a bunch of interconnected brains, which are human beings
*  talking about their own brains and talk about fun circular stuff. But even if you're doing
*  pure mathematics or physics or whatever, science is a super personal endeavor. And I've been lucky
*  enough to get to go to meetings and put names to faces and other things. And so in that process,
*  I think that it's fun to reference points and memories for many of these concepts,
*  whether they're biological or mathematical, often do come back to people. And it's a wonderful way
*  to organize thinking about the science, but it's also a wonderful way to think about what it all
*  means and what it will all continue to mean with the next generation of people when we're all gone.
*  That's a great way to end it. Thank you so much for your time,
*  Eric, and continued success to you. My pleasure. Great.
*  I alone produce Brain Inspired. If you value this podcast, consider supporting it through Patreon
*  to access full versions of all the episodes and to join our Discord community. Or if you want to
*  learn more about the intersection of neuroscience and AI, consider signing up for my online course,
*  Neuro AI, the quest to explain intelligence. Go to braininspired.co to learn more. To get in touch
*  with me, email paul at braininspired.co. You're hearing music by the new year.
*  Find them at thenewyear.net. Thank you, thank you for your support. See you next time.
*  Bye.
