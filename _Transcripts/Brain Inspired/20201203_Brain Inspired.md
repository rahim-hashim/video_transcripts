---
Date Generated: April 20, 2024
Transcription Model: whisper medium 20231117
Length: 5300s
Video Keywords: ['Science', 'Technology', 'Education']
Video Views: 16747
Video Rating: None
---

# BI 091 Carsen Stringer: Understanding 40,000 Neurons
**Brain Inspired:** [December 03, 2020](https://www.youtube.com/watch?v=zWLxo4LRisA)
*  I see it as we partly as we're going to make these advances in AI potentially
*  faster and we already have because I think neuroscience isn't answering these
*  questions. Regardless it's going to help to be able to build these circuits in a
*  machine and see if we can learn some principles from them that we can then
*  So right now we're recording around 40,000 neurons simultaneously and so now the question becomes what do you do with that data?
*  Yeah, you're right. What you do is really quite simple, right?
*  Hey everyone, it's Paul. So there's been an explosion in the number of neurons that we can record simultaneously in animal brains as Matt Smith and I discussed a couple episodes ago.
*  Matt records the spiking activity of hundreds of neurons in awake monkeys performing tasks and he relates the population activity of those neurons to task-related behaviors and cognitive functions.
*  Today I have Carson Stringer on, a group leader who runs her lab at the Janelia Research Campus at the Howard Hughes Medical Institute.
*  Carson deals with neurons in the tens of thousands range. It's a little different though, whereas Matt records the precise timing of all of the spikes of neurons.
*  Carson can't tell precisely when spikes occur, but she can tell whether one or more spikes happened within a small window of many milliseconds.
*  She analyzes data collected using a technique called two-photon calcium imaging, where basically you shine a light onto the brain of an awake mouse.
*  In Carson's case, it's a mouse and that mouse has been genetically engineered so that its neurons, when they're active and the light is shining on them, will emit their own light that can then be seen and recorded through a microscope.
*  So you get a massive amount of data about large populations of neural activity.
*  And Carson spends her time developing tools to visualize and analyze the data, so we talk about that, and she spends time figuring out what information we can extract from such a large population of neurons and what it means.
*  One thing we discuss is what they found out about two properties you would want in a population of neurons that are responding to all the different things in the world.
*  One thing you would want is an efficient or orthogonal coding scheme, where neurons would collectively respond as differently as possible to different things in the world.
*  For example, you don't want overlap and confusion between a pet dog and an angry rhinoceros.
*  But you also want a robust or smooth coding scheme, where the collective response would smoothly overlap to things in the world that are more similar to each other, like a pet dog and a pet cat.
*  That's an insufficient explanation, of course, but I will leave it at that for now because we talk more about it.
*  And just say that Carson's team found a specific relationship between how much the neurons varied in their responses and the things in the world.
*  Although that too is an insufficient explanation. It's more subtle than that.
*  But we discuss what it means. We talk about how it relates to current AI and how their results may be inspiring improvements in deep neural networks and multiple other topics, of course, with a guest question today from the aforementioned Matt Smith.
*  I linked to stuff in the show notes at braininspired.co.uk slash podcast slash 91.
*  On a side note, I've been getting a ton of emails lately with requests for future guests, which is wonderful.
*  But I just want to say if you have suggested someone to me, just know I promise I've added them to my list of future guests.
*  But that list has grown close in size to the number of neurons that Carson analyzes at a time.
*  I will say if you're a Patreon supporter, the people you've suggested are way up at the top of that list or have already been on the podcast, as you know, because you deserve it for your support.
*  So thank you so much.
*  OK, last thing, Carson is looking to hire grad students and postdocs.
*  So good luck.
*  I was actually giving a talk at your institution just yesterday.
*  It was a little 15 minute spiel on my background about careers outside of academia in science communication.
*  So that was just a mere coincidence that you and I are had scheduled this for the same time.
*  So anyway, thanks for coming on the show, Carson.
*  Yeah, definitely. Thanks for giving a talk at Janelia for science communication.
*  That's awesome. Yeah, well, yeah, I don't know how it went over.
*  We'll see. It was it was pretty painful to revisit my past, to be honest.
*  But at least now I have a little presentation on it.
*  So Carson, I had Matt Smith on the podcast a couple episodes ago and he records he uses Utah arrays and he records tens to hundreds of neurons, single neurons at once.
*  And you record over 10,000.
*  So I really just want to start off by talking about the the fun issues of, you know, recording so many neurons.
*  Where do you see in the very broad zooming out like the very broad picture, where do you see we are and where are we in terms of how useful that data is to us?
*  Yeah, so that's a great question.
*  So in terms of what this kind of big data can give you relative to smaller data is first off, neural responses in general are noisy.
*  So you record 10 neurons and you there's there might be some noise, whether it's the behavior of the mouse or it's just noise in the circuit.
*  And you can't really tell what those neurons are doing on a single trial level.
*  If you record, you start recording 100 to 500 neurons, then you can start to say, what are the correlates between this neural activity and external things, behavior and stimuli?
*  And you can make these you can figure out these relationships much more easily and build models much more easily once you get into higher and higher numbers of neurons.
*  But we have I mean, what I was really wanting to know is just this is a very new thing that we're, you know, well, very not to you now.
*  It probably feels old. But in the field at large, it's a very new thing to have access to so many simultaneously recorded neurons and their activity.
*  And I'm just wondering, like how how you feel about how far along we are.
*  Are we just at the beginning of being able to get meaningful information from that data?
*  Or do you feel like we have the tools that we already need?
*  And and I know this kind of a trick question because this is part of what you do is is developing the tools to extract meaningful information from it.
*  So I'm just curious, like how you feel. Are you at the beginning? Are you in the middle?
*  Do we have are we are we ready for eighty six billion neuron recordings or what?
*  Yes, that's a good question. So I think so right now we're recording around forty thousand neurons simultaneously.
*  So that's sampling a good fraction. It could be anywhere from up to like 70 percent of the neurons in in a given area, depending on where we're recording.
*  So we're getting a very dense sampling. And so now the question becomes, what do you do with that data and what kind of stimuli do you show with that data?
*  And what kind of behaviors do you have the animal do?
*  So I think in terms of the recording techniques, those have been amazingly developed and we have these amazing proteins we use so that these neurons light up when they fire.
*  And that's how we capture this activity. So that all of that protein engineering and the microscopy is at a really great place for us to capture these large recordings.
*  And now the field needs to kind of explore different behavioral paradigms and think about the types of, for instance, visual stimuli you want to show to be able to understand what these patterns of activity mean.
*  So let's talk about the the two photon calcium imaging for just a second, because that's how you capture this really high neuron sample data.
*  So maybe you can just describe a little bit more what what two photon calcium imaging is and the kind of data that we actually get from it.
*  Right. Yeah. So it's a technique that allows you to basically take pictures of the brain across time.
*  And you're taking pictures of these neurons are are expressing this protein that lights up whenever the neurons fire.
*  So you're taking pictures of neural activity time point by time point.
*  And now you're you're able to from these recordings, you can extract each of these neurons and extract the neural activity across time.
*  And there's advantages on top of electrophysiology like you talked to Matt Smith about, which is that you're you're literally seeing the neurons.
*  So, you know, their spatial relationships, you can have genetic lines where certain neurons are different colors, depending on what kind of cell type they are, like if they're inhibitory, things like that are easy to do.
*  You're not seeing their connectivity, though, but you're but you're seeing their spatial relation to each other.
*  Yeah. So you can go even further. So so people also have started doing two photon stimulation.
*  So now you can see these neurons and you can also stimulate them with lasers.
*  You can focus on specific neurons and stimulate them.
*  And that can get you closer to having a kind of connectivity graph.
*  But it's not it's never going to be the perfect case where in electrophysiology, you're never going to be able to you don't have the temporal resolution to specifically say two neurons are connected in calcium imaging.
*  You mean? Yeah. Yeah. So that's that there's always this trade off. Right. So so the previous I don't know if it's still the gold standard of extra cellular electrophysiology recordings is that you have this super high temporal resolution and you can get every single spike.
*  If your if your electrode is right next to a neuron.
*  And on the other hand, the worst temporal resolution is with something like fMRI, right, where it's like seconds go by and pretty good spatial resolution, but really poor temporal resolution and calcium imaging is much closer to the temporal resolution of recording single electrodes.
*  But like you said, you're taking like little snapshots. So there what what is the bin of the window that you're looking at?
*  Right. Yeah. So to record so many neurons, we go even lower. So often people will take 30 millisecond bins. They'll record at 30 hertz and we go at around three hertz. So every 300 milliseconds, we get a sample from a neuron.
*  So we get three samples per second. OK, so you can kind of see whether it's spiked within that time within that window, essentially. Yeah, I think.
*  And even if you record at 30 hertz, you still can't really tell how many times a neuron spikes and calcium imaging. That's another downside.
*  Basically, different neurons have different size amplitudes of their calcium of these calcium spikes that we'll see.
*  And so a single spike in one neuron can correspond to a different size spike in a different neuron.
*  And then one spike even within the single neuron, that one spike can have a very variable size of calcium activation across across time.
*  So, yeah, yeah, we generally don't claim that we're recording spikes. Right. Yeah. OK. But but you're recording neural activity, I suppose.
*  Is that the claim? Yeah. Yeah. So one thing that I found frustrating throughout my little academic career is that, you know, I went into neuroscience in graduate school and wanted to ask these really big questions.
*  The brain, how does consciousness work? What is a mind and all this stuff?
*  And what I found was just a series of asking smaller and smaller questions and more so than that, troubleshooting technical issues in all the details.
*  And so I ended up focusing a lot more on methods and analyses and what they can tell us and which one's better and why they're better instead of.
*  And so you kind of like lose the big picture questions.
*  So I'm wondering, what are some of the challenges that you face when analyzing these sorts of really large recordings, first of all?
*  And do you have that same sort of I don't even I don't know why you got into neuroscience, but presumably you have some.
*  Well, I can just I can let you respond.
*  Do you have that same experience at all? Because what you a lot of what you seem to do is very technical.
*  Definitely. And if this happens, you want to answer some big question like I started being interested in kind of brain states and like how neural activity changes, whether you're, I mean, conscious or unconscious and anesthesia and stuff like this.
*  And then when you go in to record this data, I think one of the biggest confounds we see in calcium imaging that that people don't correct for is actually that the brain moves up and down parallel to the to the plane throughout the recording.
*  Yeah, physically is moving relative to the microscope. I mean, it's very small movements in microns.
*  Right. Well, that's huge when you're looking at this at the scale of microns.
*  But you should say that you're recording in mice.
*  Right. Yeah, yeah, sorry. Yeah, I apologize.
*  And just to back up, you have to you do this surgery where there's like a kind of a window onto the brain where you can point the microscope.
*  And and that's how you image the brain while the while the mouse is doing whatever it's doing.
*  Yeah, so and that's another advantage of calcium imaging is that we put these windows into the mice and they basically live their normal lives.
*  They go live with cage mates. Then then day after day we can come in and record their neurons.
*  And because we're taking these pictures of the brain, we can see are we taking pictures of the same neurons across days?
*  And so you can do this alignment across days and study learning in these circuits as well, which is something that's also harder to do with electrophysiology.
*  Yeah. OK, so so so what are some of the challenges?
*  I mean, there has to be a million challenges.
*  Yeah, so I work so there's a lot of challenges on the on the microscopy side that I don't deal with.
*  But on the software side, kind of we we've created pipelines to basically correct for move the microscope when the brain is moving to make sure that it's always in the same place relative to the cells in a closed loop.
*  So things like that are really improve our data quality.
*  How long did that take you to do? I'm going to guess I'll guess a year.
*  I spent a long time trying to correct the signals without moving the microscope.
*  So yes, so several resort to move the microscope to.
*  Yeah. Yeah. When we realized we weren't going to be able to correct the signals well enough.
*  So then we decided to move the microscope. Yeah.
*  I mean, so what about what about just recording like?
*  Well, we'll get into the analysis of all these things.
*  I had a listener question asking about how you manage the interplay between pursuing your own scientific questions and developing the tools and the software that you've you've had to develop to analyze the data.
*  So how do you manage that that balance? Or is there even a balance?
*  Yeah, that's a great question.
*  And I think I am in a I'll preface this all by saying I'm in a fortunate place.
*  So I'm a group leader at January Research Campus, which is a nonprofit institute.
*  And so I have funding for five years. So I'm basically able to continue to work on these projects as a group leader, whereas in other I mean, the the mechanism of funding in the U.S.
*  cannot is not always conducive to working on tools rather than working on science in terms of getting grants and so forth.
*  So I'll preface that by saying that that then the choice becomes how do I balance my time?
*  If that if that makes sense. Yeah. Yeah.
*  So so then I am able to choose how much time I want to spend doing tools and doing science.
*  And it's probably around maybe 20 to 30 percent of my time working on tools.
*  Oh, really? Wow. OK.
*  But and I think it's I think it's very useful for the community to to work on these tools like I and I enjoy working on this kind of software.
*  So I hope that rather than everyone having someone in their lab that spends 20 to 30 percent of their time working on this tool, we we've worked on this tool.
*  Other people contribute to this tool through pull requests on GitHub.
*  And we can all kind of work towards creating a better tool.
*  We get hundreds of user comments, whereas if an individual is making something in a single lab, they're not going to get this feedback and be able to improve the tool as well.
*  This particular listener says that you're a pro at both, but is curious sort of the dynamics of it.
*  Right. So do you usually think of and develop the tool first and then go on to apply the tool?
*  Or do you find yourself asking the scientific question and gathering the data and then think, oh, now I have to make a tool or software to analyze this?
*  Yeah, it's usually it's driven by the latter that we have a problem that requires a tool and will then develop a tool like the most recent tool that I developed was cell pose, which is for anatomical segmentation.
*  And that was we needed to segment. Actually, in this case, we were trying to segment calcium imaging data in an anatomical way rather than a functional way.
*  And so we we tried some of the out of the box tools that other people have developed.
*  They weren't working as well. So then we tried to develop our own tool.
*  How frustrating is that? It's like, I mean, you must find that at every step of the way.
*  Like, oh, is there something for this? No, we have to create it. I mean, that must happen over and over.
*  Yeah, I think the big problem is thinking about these questions and a small scale.
*  And that's that's the way that science has moved forward in general, that everyone's working in their own lab.
*  And they say there are great cell segmenters for certain types of data, like, for instance, for nuclear data there.
*  There are great pipelines in place, like, for instance, from Ann Carpenter's lab.
*  But then that they might not work for all the different types of cellular data you have.
*  And so thinking about things that are applicable for many people rather than a single use tool kind of is, I think, the difference between where I'm coming at with these problems rather than where several other people are coming at.
*  Yeah, when I was in graduate school and beyond, everyone was kind of in their own little individual bubble.
*  You wouldn't even like share stuff between lab members because everyone had their own very idiosyncratic specific problems that they were then developing things to deal with.
*  And that shift, I think, is a really that shift to more open source and collaborative and sharing these sorts of tools, I think, is obviously only a positive thing for the community.
*  This listener also goes on to ask whether there have been occasions where the the tool itself, you know, where we're building the tool or developing the software, developing the analysis has actually inspired you conceptually, inspired your science conceptually.
*  And if so, what's an example of that?
*  Yeah, so this is this is definitely still work in progress, but working on segmentation in terms of object segmentation, particularly we're looking at segmenting cells as kind of shaped the way I'm trying to think about how the brain does segmentation of images and thinking about images.
*  You can think of images as segmented objects or as textures, which are made of many objects and thinking about how the brain conceptualizes those different things and different the different types of architectures like for deep neural networks, for instance, that work well for segmentations and thinking about how those might be applied in the brain.
*  And is there insight that you've gained from it or is it just sort of the way that you approach the question has changed?
*  Yeah, so we've been so there's this kind of long line of work where people compare neural responses to responses in deep neural networks.
*  And those have been sort of confined to more of these feed forward models and not these models that are trained and that are trained on image recognition.
*  So it's kind of thinking about expanding this problem and thinking about what about a model that's trained on object segmentation and these models that do best on object segmentation actually have these these sorts of these skip connections, which you can think of as recurrent connections.
*  Which integrate local and global features.
*  So if you want to, for instance, segment an object, it's helpful.
*  You need these kind of global cues to know kind of around where the object is.
*  And then you also need this fine local information to say exactly where that edge is.
*  So you kind of would need to combine information from maybe high.
*  You could think of combining information from high order visual areas with low level primary visual areas and how that how that integration takes place is would be cool to figure out.
*  What is what is image segmentation?
*  Oh, yeah, sorry.
*  I clear. Yeah.
*  Yeah. So I'm talking about particularly what people often call instance segmentation.
*  So we have an image, for instance, of a bunch of you could think of cells.
*  We actually have rocks as well in our cell pose database.
*  We have circle.
*  You basically circle every rock in that image and you train the deep neural network to figure out where each of those rocks are.
*  OK, very good.
*  So we'll talk just a little bit more broadly about these sorts of data sets here before we get into the actual science that you've been producing.
*  Wayne on soon has asked if you could compare and contrast the pros and cons of your favorite unsupervised techniques for data analysis.
*  Yeah, that's an interesting question.
*  I would say we still don't have the best unsupervised algorithm for analyzing large scale neural data.
*  So I'll preface my answer with that.
*  But that being said, I think still kind of this state of the art for unsupervised dimensionality reduction, nonlinear dimensionality reduction would be T's knee.
*  OK, and so there's this big there's this problem with with dimensionality.
*  Sorry, sorry.
*  I should explain what TC is.
*  Yeah, what's what's T's knee?
*  Sorry.
*  I mean, yeah, yeah, sorry.
*  So you have this T distribution stochastic neighbor embedding algorithm.
*  That's what all those letters stand for.
*  But the idea of so these unsupervised dimensionality reduction techniques, particularly nonlinear ones, the idea is that you have this really high dimensional space we're recording from.
*  We have like forty thousand neurons and they have many thousands of time points.
*  But we can't visualize this really high dimensional space.
*  And so what these techniques do is they take this high dimensional space and they smush it into maybe a couple dimensions and they smush it in like a nonlinear way to kind of put neurons close to each other and kind of break some of the linear relationships between neurons to try to get a better to try to get a better picture that we can actually visualize in 2D.
*  He also asked if you could explain raster map because this is very related.
*  Yeah, so that's actually kind of what I was going to.
*  Yeah, so so T's knee has I think is still the state of the art in terms of getting kind of the global structure right of the manifold.
*  So you kind of want to globally capture how and how the activity change how neurons vary maybe across the recording.
*  And I think TC is still kind of the state of the art for getting this global picture.
*  And then in terms of there's always this trade off in these nonlinear dimensionality reduction techniques like however well you capture the global information you're going to lose information in the local structure like if I if I try to perfectly capture the global information I can't there will be neurons that will be moved around that should have been closer to each other but they just can't be smushed into the map.
*  And so there's there's always this trade off you're doing with these embedding algorithms that you're you're going to destroy some of this local structure while trying to get this global picture.
*  And so there's this trade off that that you do in these algorithms and and raster map is is an example of an algorithm which tries more to preserve this local structure.
*  This is something that you do that developed. Yeah, yeah. So it's just looking at the finer grain structure of the manifold.
*  Yeah, so it's it's it's also this embedding algorithm where it's this idea you have neurons in this high dimensional space and I'm going to put every neuron I'm going to define as having an XY position basically in 2D.
*  So that's what these algorithms do. So raster map is another way to kind of get XY positions for neurons and it has this way that it tries to more heavily weight these kind of high dimensional components of the neural activity rather than TC which is going to get more of this global more the global.
*  Why is it useful to rearrange things like this and and create images like this.
*  Yeah, so that's a that's a great question. So so once you rearrange things you can start to look at these maybe you'll get clusters out of it of neurons and then you can look at what these clusters of neurons are maybe correlated to in the external world.
*  So I might have a cluster of neurons that comes out in this low dimensional representation that maybe corresponds to the whisking of the mouse or maybe it corresponds to the confidence of the mouse and some decision making task.
*  So it could be something more abstract like that like the the advantage of having this representation is you're you're able to kind of average over neurons that are in that are noisy on a single trial but then look at single trial information once you've averaged over them because they're collected among other neurons that on average are coding for the same thing.
*  Which doesn't mean try to avoid the word coding but but yeah are similar in their responses to stimuli and cognitive manifestations I suppose.
*  Yeah exactly and that is that is really the big problem with neuroscience and what most of the field has done in the past is we study we study averages across many repeats of the same image for instance.
*  Right and we really if we want to understand the behavior of the mouse or any species we we want to know what it's thinking moment by moment and so ways to better be able to characterize this moment by moment information are really useful in the in these cases.
*  We've used the term you've used it once I believe and I've used it once manifold and I've been asked because that is a fairly manifolds are fairly new in neuroscience as well I guess they've been around a long time for high dimensional analysis but what is a manifold with respect to neural activity and why is it useful to think conceptually in terms of a manifold.
*  Good question so first I'll define what a manifold is mathematically so a manifold is it has this property that locally the points in the manifold resemble a Euclidean space.
*  So let's let's take that in the case of neural data so neural data we're going to we're going to think about every single point in this high dimensional 40,000 dimensional space every single point is a different response to maybe a visual stimulus like one could be a cat or a dog or a hawk or these other things.
*  And each of these points in this really high 40,000 dimensional space might create some kind of like wavy surface inside of this space so you're it's not going to explore this giant 40,000 dimensional space like there's many many places right that that activity could be but it's it's generally going to be constrained we think to sort of a subset of this space.
*  And we think of this subset as being a manifold that it is going to be curvy and complex but then if you zoom in if it is a manifold then the activity will be will change kind of linearly so maybe we zoom into a part of the of the manifold that codes for cats.
*  And maybe small changes in the cat nose or the cat ear pointiness maybe change the change the neural activity in small linear ways like you have these perturbations that change the neural activity in small ways rather than moving to a completely different part of the manifold.
*  So it's like just traveling along the surface of the manifold.
*  Yeah that that we would think of that small perturbations of an image space there will be perturbations in image space that travel along this manifold that that exist that change activity and in in such a way that it's it's small relative to the perturbations you're making in the image space.
*  So at heart is a manifold a way to reduce the super high dimensional dimensionality of your data in into like projections onto lower dimensions and that defines the manifold.
*  You can think of a manifold as a as a low dimensional representation but you can also think of the neural activity itself as a manifold.
*  So so what I'm trying to say is that we think that that the neural activity is constrained to this space which is generally lower dimensional and if you have I guess I wasn't totally clear right.
*  So so there will be small perturbations which will move you along what you think of as your neural manifold and then there might be perturbations you make that might jump you to other parts of this curvy manifold and like we don't know how curvy or smooth it is like if it if it's pretty if it's very smooth then lots of image perturbations will kind of keep you in the same place.
*  Whereas if it's really curvy then there will be some image perturbations that keep you in that space like I change the pointiness of the cat ears and the neural representation doesn't change that much but maybe I change the length of the nose and now all of a sudden it's a it's a dog or something and and I move a lot.
*  So yeah we don't really know how how smooth that that representation is and in what dimensions.
*  Am I wrong to think of a manifold then and I'm really pretty green about manifold so am I wrong to think of it as akin to an attractor in dynamical systems but just a like a surface attractor.
*  Yeah you can you can think of it that way and it might be the case that if you perturb neural activity for instance it will come back to the original manifold that we think is is of the of the responses that we see like that that consists of the responses to images and when you don't perturb it.
*  So there are those so there are places along the manifold that are more often visited or or you could think of as like having lower energy that it settles in this like lower energy area and then you perturb the system and it traverses parts of various parts of the man of along the manifold.
*  Yeah there definitely will be places that it sits more often but that's also another question there's also the manifold of neural activity with respect to behaviors and so this neural activity is also changing in this kind of orthogonal space in terms of what behavior the mouse is doing in addition to having this this manifold of responses to to visual stimuli.
*  Let's go ahead and jump in and let's talk about because we can revisit all these topics as we talk about what you've done so like I just I mentioned I had Matt Smith on the show and we talked about his recent finding what they call slow drift which is like this global fluctuation in the brain of actual neural activity over the course of minutes tens of minutes while an animal is performing a task that really tracks the also the internal cognitive state in the behavioral aspects of the brain.
*  So you know the animal like pupil size and various other behavioral measures and one of the recent things that you found this the 2019 science paper I suppose is that even when you're recording in visual cortex there is a signature that well much of the activity can be attributed to the spontaneous behavior of the mouse in this case.
*  So you guys had a mouse sitting in a dark room you weren't asking it to do anything but you were recording its pupil and its facial features its whiskers and so you would know when it's whiskering is it called whiskering?
*  Whisking.
*  Whisking, geez yeah and dilating for instance I know it's called dilating with a pupil but what you found is like there's all sorts of these spontaneous behaviors that the mouse was performing well was undergoing in acting in that dark room when it wasn't being asked to do anything that there was a lot of activity in visual cortex that correlated with these spontaneous behaviors.
*  And I'm going to pause here then and just so I so Matt has a question for you and then we can you can unpack it for us probably before maybe along with answering it.
*  Hi Carson thinking of your really impressive pair of papers last year in nature and science I had a question for you.
*  You find these really rich behavioral signatures embedded in visual cortex and you argued that having this kind of activity as early as visual cortex might help the brain integrate sensory inputs and motor actions.
*  So what I'm wondering is if you thought about drawbacks of this kind of system maybe particular actions or perceptual events that might be confounded by having these signals all sort of thrown together even in the early stages of visual processing.
*  All right.
*  That's a that's a great question. So so yeah I'll unpack it first with a kind of a simple example. So we have these signals for running in mouse visual cortex.
*  So whenever the mouse is running there's neurons that increase their activity.
*  And these neurons also code for for stimuli so they might also respond to cat stimuli.
*  And I'll just I'll just interrupt you and say that's actually just just off the bat. That's fairly surprising right because we think of visual cortex as just processing visual information sensory information.
*  But that's but so it's fairly surprising to just see all of this behavioral activity also in the visual cortex.
*  Right. Yeah. And I think I guess it's especially more surprising for people working on primate and human literature like the monk the mouse literature actually.
*  So this first finding was from 10 years ago now from Chris Neal.
*  So so there's a yeah I apologize I'm talking about it like it's it's pretty standard but yeah I guess it's 10 years a standard.
*  What makes it standard. Yeah but it's it's less it's definitely less well known how pervasive these signals are in in primate and humans.
*  Right. Well we're not doing calcium imaging in primates and that's that's one of the advantages of doing this in mice is that they're available for the calcium microscopy.
*  Right. Yeah. So we're able to get these many neurons and we're able to get these correlations with these behaviors and create models from from behavior to neural activity and predict the neural activity from these behaviors.
*  So yeah so the confound he's corresponding he's referring to is this fact that if a neuron is responding when the mouse is running and it's also this cat a response to cats then its response is going to be different when it sees a cat when it's running versus when it sees a cat when it's not running.
*  And so how does the brain then tell that it saw a cat if it can't use this neuron basically to tell it if I say I set some threshold then sometimes you'll think you'll see a cat sometimes you won't depending on whether or not for instance the mouse is running.
*  If you set a threshold on that neuron but you have the advantage that you have many thousands of neurons in cortex.
*  So you're not just going to be using a single neuron to figure out cat.
*  So say I have several hundred neurons that respond to cats and if as long as some of them respond to when as long as only some of them are modulated by running and maybe some of them are down modulated by running they decrease their activity with running.
*  Then on average if I take the average of those hundred neurons in response to a cat whether or not I'm running that that average response will be similar.
*  But I thought what you found was that the majority of the variance in the visual cortex could be explained by the behavior and therefore the minority was actually explained by incoming sensory stimulation and I'll just go ahead and say that and because you alluded to this earlier when we were talking about manifolds that what you found was that the majority of the neurons in the cat were modulated by running.
*  When we were talking about manifolds that what you found was that these the variance in these activities were orthogonal between behavior and the visual information so maybe you can touch on what that means as well.
*  So you bring up a good point so when we when we talk about a third of neural activity being explained were referring to a third of neural activity in the absence of visual stimuli.
*  there's this additional information in the neural population, which actually contains
*  around twice as much variance as the behavioral information.
*  That makes a lot of sense.
*  Yeah.
*  So then you have this information in there along with the behaviors.
*  And this idea of orthogonality is that the neurons that respond to cats have various
*  responses to different behaviors.
*  They're not all running neurons.
*  There's neurons correlated with running, anti-correlated with running, correlated with whisking, anti-correlated
*  with whisking.
*  So then on average, their responses to cats is going to be the same with whatever behavior
*  the mouse is doing.
*  But you can only tell that by looking at the population.
*  Yes.
*  So if you're looking at a single neuron, you're going to see you're not going to be able to
*  tell the image depending on the neuron.
*  So some neurons will be more or less modulated by behavior.
*  Gotcha.
*  So that's sort of the first pass at this when you had mice sitting in a dark room.
*  And like you said, you did start showing them visual stimuli eventually.
*  And then the question is how the images, the visual stimuli that you're showing to the
*  mouse, how they're processed in the population of visual cortex.
*  So I also recently had Chris Eliasmith on the show and we talked about his cognitive
*  architecture spawn.
*  One of the things that he uses, he developed what he calls a semantic pointer architecture.
*  The idea, and this is the way that information gets transformed from one area to another,
*  for instance.
*  But the idea is that in visual and in motor, so sort of like the input and output of the
*  brain in those areas, there are these really high dimensional states.
*  And then this semantic pointer processes the information from, let's say, visual in this
*  high dimensional state and reduces the dimension, reduces the dimension to whatever cognitive
*  process an animal is doing.
*  And then it has to be what he calls dereferenced to bring it back to another high dimensional
*  state to perform a motor action.
*  And you make the point that for visual information or really other sorts of sensory information
*  as well, it's actually coming in in a lower dimensional state than is possible in the
*  visual cortex.
*  Right?
*  So the retina goes through the thalamus and these are fairly low dimensional in that there
*  are lower numbers of neurons that it actually then it projects to back in V1, in early visual
*  cortex.
*  And there are two sort of classic theories, I suppose, about how the brain might usefully
*  process information within a population.
*  I don't know if they're officially called the efficiency versus the robustness theories,
*  but maybe you could just talk a little bit about the two different ways that it's thought
*  that information could be processed that would be useful.
*  Yeah.
*  So that's a great question.
*  So ideally, you have all this information from the visual world and you want to compute
*  as many features of it as possible and have as many of them in visual cortex in primary
*  areas.
*  So then you can do these complex tasks like object recognition.
*  So then the most efficient way to have all this information in your brain is to have
*  each of those features be orthogonal to each other.
*  That's how you're going to store as much information as possible about the visual world.
*  Completely separate.
*  Yeah.
*  But then you have this issue if there's any kind of noise or there's small changes in
*  the inputs, then your representation might change drastically.
*  Different neurons are going to be representing things even if you've just added a small amount
*  of noise.
*  And so you're not necessarily going to represent the visual world in a smooth way and you also
*  might not be...
*  You would be more sensitive to neural noise or maybe neurons dying or things like that.
*  And so the other far end of things is to be as robust as possible, which is to only represent
*  a few features but represent those with many hundreds of neurons.
*  And what we found was kind of more the in-between, that there are these features that many neurons
*  represent, that many neurons code for.
*  But then there's also these...
*  There's many hundreds of features that only a subset of neurons code for that kind of
*  have these finer features.
*  You found a specific relationship actually between the dimensional number, which I'll
*  ask you to unpack in a second, and the variance.
*  Maybe you can just explain what you found, I suppose, the power law relationship and
*  what it means.
*  Right.
*  Yeah.
*  So I can explain what we think it means.
*  Sure.
*  No, explain what it actually means.
*  So what we found empirically is that there's this decay in variance across dimensions.
*  And so you can think of the first few dimensions as maybe the contrast in the image, maybe
*  if there's edges somewhere or not.
*  And those are the kinds of dimensions that have the most variance in the neural population,
*  that drive the most neurons.
*  When you say dimension, maybe you can describe how you...
*  Not calculate, but how you come up with the different dimensions of what we're talking
*  about in terms of the variance, I suppose.
*  Yeah.
*  Yeah, sorry.
*  So when we're referring to dimensions, we're referring to linear dimensions.
*  And so we find these dimensions using principal components analysis.
*  And we have a special way to do it to ignore the noise that's coming from behaviors and
*  other things.
*  But it's basically principal components analysis to find directions with most variance in the
*  neural activity.
*  And then the result of that analysis is that there are dimensions with large amounts of
*  variance, but then there are many hundreds of dimensions that have significant variance
*  that create this power law decay of variances over these dimensions.
*  So it could be that there are...
*  And the way that you often frame this is, again, between the two hypotheses between
*  efficiency and robustness is that it could be that there are just a few dimensions of
*  variance and then nothing else.
*  And what would that entail?
*  Right.
*  Yeah.
*  If there were only a few dimensions and the rest were zero, it would mean that you have
*  this low dimensional code and that there's only...
*  Maybe you represent contrast in the image.
*  Maybe you represent red versus blue or green versus yellow.
*  And then you only have these few things you represent in the visual population.
*  And it means that you represent them very reliably.
*  You can kill a bunch of neurons and you'd still know what you're seeing with respect
*  to those features.
*  But then complex visual computations require these fine scale features of the image to
*  be computed.
*  If you want to do object recognition, there's much finer features of the image you might
*  have to pay attention to or object segmentation, for instance.
*  And then the other end of the spectrum there is if you had, I suppose, infinite dimensions,
*  if all of the variance was equal in all of the different dimensions, then that would
*  be a very different coding scheme.
*  Right.
*  Yeah.
*  So it would mean that every neuron is independent of every other neuron and that there aren't
*  these lower dimensions that we saw that are driving the whole population in these kind
*  of global ways.
*  And if every neuron is doing its own thing, you have a small perturbation of the stimulus
*  and a completely different neuron is going to start firing.
*  And so you're not able to...
*  It decreases your ability to be robust to noise.
*  It also decreases your potential to kind of generalize across stimuli.
*  So if you have a small change in your stimulus, you might think like...
*  If you say it's a small change in the cat, like I was talking about, like the ears get
*  pointier, you probably still want to think it's a cat.
*  But then if there's completely different neurons firing, it's going to be harder for downstream
*  decoders to be able to do this discrimination kind of in an easy way.
*  Are you a cat person or a dog person?
*  I'm kind of neutral on the question, but I'm more of a cat person.
*  Somewhere in between, but closer to cat.
*  Okay.
*  Well...
*  Yeah, I'm allergic to cats.
*  So I would be a cat person if I wasn't allergic to cats completely.
*  I'm much less allergic to cats these days than I used to be, but I still use that as
*  the reason why I deny my family getting a cat, because I'm more of a dog person.
*  But not shockingly then, what you guys found is that the quote unquote answer, at least
*  in visual cortex, is somewhere in between these two ends of the spectrum.
*  And not only that, that there is a mathematical relationship between the dimensionality number
*  and the variance.
*  So I guess that's the first question I asked.
*  So what is that relationship?
*  What is that power law relationship?
*  And what does it mean?
*  Not what might it mean.
*  What might it mean is the question.
*  Yeah.
*  So this is a little hard to do without pictures, but yeah.
*  Everything on this podcast is hard to do without pictures.
*  It's ridiculous, but so sorry, go ahead.
*  No, no.
*  Yeah.
*  So there's this idea of how quickly does this power law decay?
*  So a power law is like a straight line in a log log axis.
*  So you can think of a straight line that you're looking at that has a slope of minus one.
*  So that's our decay across dimensions.
*  And we have this slope of minus one is what we found in the neural data.
*  But this slope could decay more quickly, which would mean, say it has a slope of minus two,
*  then you start to have these higher dimensions have less variance.
*  So you have these kind of fine scale features have less and less variance, or you have fewer
*  fine scale features that are encoded in the population.
*  And so there's a question of like, if you for what we think is that this minus one is
*  kind of at the is as high dimensional as you can be, you have as much coding of these fine
*  scale features that you can possibly have before you kind of break.
*  If you go if you decay any more slowly, you're going to have too many of these fine scale
*  features and you're no longer going to have this manifold representation.
*  You're going to start breaking things and there's just this just everything is going
*  to be too high dimensional and you're going to you're no longer going to have this kind
*  of robustness.
*  At that point, you would stop calling it a manifold if it becomes too fine grained.
*  I didn't I realized I don't know what the threshold is to call something a manifold
*  because it does structure even though it's super fine grain, right?
*  Yeah, so it still has structure.
*  But then the the local neighborhoods are no longer equivalent to Euclidean spaces.
*  So they're just going to be basically these small changes we were talking about.
*  They're no longer going to result in small changes in neural activity.
*  There's going to be jumps and so forth in these small neighborhoods.
*  So that's where that's when things change.
*  Why would that be bad?
*  Right.
*  Yeah, so that will be bad because then you no longer are able to have a local neighborhood
*  that kind of smoothly potentially generalizes over stimuli.
*  Like you'd be jumping around whenever a stimulus with respect to small changes in the stimulus
*  space.
*  So like from pointy ears to less pointy ears, you could you would be in a totally different
*  neuronal space potentially.
*  Yeah, and it wouldn't quite it doesn't necessarily have to be a totally different place, but
*  it's still it would be moving much more than what you would then the stimulus is moving.
*  It would be larger jumps.
*  You could still think so.
*  You can think of an example of something that's not a manifold.
*  This is an example my advisor Kenneth Harris likes, which is the coast of England.
*  I don't know if you're familiar with that, but you have all these kind of little divots
*  and you have these kind of fine scale structures.
*  So you you you do have this you will have these kind of movements in the local space,
*  which will be disjoint, but you still might have an overall global structure that could
*  be preserved even in that case.
*  Well, I thought you're going to go into self-similarity and fractals there for a second.
*  But that is partially what you found also is that it has a fractal type structure, right?
*  Or is it close to it?
*  Yeah, so I okay.
*  So let's all right.
*  Wait, hold on.
*  There's another thing I want to unpack here because there's so many so many things going
*  on.
*  Yeah, yeah.
*  So backing up.
*  Yeah, so I so yeah, so this fractal idea.
*  So the power law if the power law is is minus one, if it decays at least as fast as minus
*  one, then it can be a manifold.
*  If it decays more slowly, then it will be a fractal.
*  But we don't know for sure that it's a manifold.
*  So it just suggests the math suggests that it could be a manifold, that it decays fast
*  enough to be a manifold.
*  But we don't know for sure that it's a manifold.
*  Do we want it to be a manifold?
*  What do we want it to be?
*  Yeah, I mean, we think that it would be ideal for it to be a manifold because then you'd
*  have local neighborhoods that kind of have this kind of smoothness property.
*  So a generalizability and yeah, that you'd be less like something people often think
*  of in machine learning.
*  It's it's kind of this equivalence to these adversarial images where you take a picture
*  of let's do an eel instead of a cat and you maybe change the color of the eel's eye.
*  And to us, the eel would be that would still be an eel.
*  But then that the neural network might completely think it's a different image.
*  Or you could think of even adding there's different types of Gaussian noise you can
*  add to those images and you'll get and these tiny amounts of noise you add can totally
*  change your the perception of the eel.
*  So that the neural network would then classify it as a cat, for instance, or let's bring
*  it back from a shark, let's say, you know, or something.
*  But yeah, but so I actually want to go back to what this tells us about AI and how it
*  might be helpful considering these adversarial examples.
*  But let's talk about the self-similarity a little bit more.
*  You were talking about the self-similarity and the nature of that.
*  Yeah.
*  It could be the case that the the idea of self-similarity is something like you could
*  think of a tree with branches.
*  And as you zoom into that tree, the branches look similar as they looked when you're further
*  away.
*  And so you could think maybe that the neural manifold has similar structure as you zoom
*  in further and further and that the global structure looks like the local structure.
*  And that is something that we're studying now.
*  And we're looking at these components of where we're basically doing local image perturbations
*  and seeing how the neural activity changes and seeing if those dimensions are similar
*  to these global dimensions that we found.
*  And we're not necessarily seeing this correspondence.
*  So we're not seeing this correspondence.
*  So it suggests that it's not it's not a self-similar structure.
*  Oh, okay.
*  And it's not necessarily so surprising.
*  I mean, there's so many different things that you might want to encode locally rather than
*  that that might be different than what you might want to code globally in terms of the
*  types of computations you want to do with local information versus global information.
*  I mean, what does this so this balance I mean, it seems like always in nature and through
*  evolution.
*  It's like walking this fine balance between local and global and efficiency and smoothness
*  or robustness.
*  In that sense, it's not a surprise.
*  But it's I don't know, it seems very impressive.
*  It is really incredible.
*  I think it's I and that no, I mean, I shouldn't use words like that in science.
*  But we were really surprised when we got this result of this power law that it is something
*  that we weren't expecting.
*  And it's what were you expecting?
*  We didn't really know what to expect.
*  Especially particularly in mice, we wouldn't think it would necessarily even be that high
*  dimensional.
*  We think maybe we have 10 or 100 dimensions and then we're good.
*  Let's fit a simple model and we'll be able to explain the neural responses.
*  Yeah.
*  So so what the what the power law shows is that it is very high dimensional and has this
*  really broad capacity then to yeah to code global and local features.
*  This same sort of relationship is also found in other networks like social networks.
*  And even when even images, right, they have this sort of balance between self similarity
*  and these kind of global features.
*  And there are these power law relationships, examples of them throughout lots of different
*  phenomena.
*  So in that respect, it's also not that surprising, I suppose.
*  Yeah, it's a question of if yeah, if it's inherited from the statistics of the natural
*  world that you experience that it is advantageous to represent things in a way that you that
*  that you're always going to have more power in these low frequencies versus these these
*  high frequencies.
*  I mean, I think that's kind of an open question in terms of the way that they learn these
*  representations.
*  And it could be that they are replicating the statistics to some degree, that there are
*  more of these that these global like low frequency representations in the images are more
*  frequent than high frequency things like small leaves and branches and that that's being
*  inherited by the by the neural activity and the neural representation.
*  So you don't think it's necessarily something inherent in the brain itself, but just a
*  capacity of the brain to put.
*  I mean, that's what you're saying, right, to potentially inherit the statistics of the
*  natural world isn't the way the brain is built per se, but it is allowed by the way that
*  the brain is built. Does that make sense?
*  Yeah. So that is totally an open question.
*  So I don't know how much of this architecture would have to be learned or if to some extent
*  it's already prewired in a way that allows for these kinds of that these global signals
*  are kind of innervating many neurons in this feed for in a feed forward way that allows
*  for this power law to exist.
*  It could be that it's it's from the architecture itself.
*  It could be that that to some extent it is learned.
*  What I guess it would be somewhat surprising to me if all of the high frequency features
*  are there to begin with, like I would think that maybe some of those might be learned
*  from experience, but we really don't know.
*  I mean, we're at the edge of what we know and what we don't know always, especially with
*  like data like this. This is just the newest kind of data.
*  No one's ever seen this kind of I mean, you know, for it's been a few years, I suppose.
*  But it's not like single neuron recordings that have been around for decades now.
*  Right. Yeah. And and it's also expanding the stimulus space and looking at natural images
*  and kind of doing these experiments where you you can do these experiments where you
*  have mice that are that grow up without any visual information.
*  They they grow up in the dark. You can raise them in the dark and see are their representations
*  different from representations in mice that have visual experiences.
*  And these are questions that would be really exciting to know the answers to.
*  Oh, I was going to ask if you guys were doing that.
*  Yeah, that's so my collaborator is is is working on some of that at Janelia.
*  But it's and there's people there's people at Carnegie Mellon working on it, too.
*  I think it's it's there are people working on it in the field.
*  So we'll have some answers soon.
*  Yeah, that's an interesting question.
*  Another thing that I know I'm sure you get asked this.
*  But so in this setup, right, you have a mouse and it is just being shown stimuli.
*  And then and what you found is this power law relationship between the dimensionality
*  and the variance.
*  Do you think that that it's the same relationship, first of all, like in different brain regions?
*  So, you know, classically, like like I was just saying with Chris Elias Smith,
*  the way that he set up spawn is to sort of reduce the dimension to like a lower dimensional space.
*  And one way one example you could think of this is forming a category, right,
*  of an image, right.
*  So you have like the dimensionality of eel.
*  Let's go eel is is very low compared to all of the visual features of an image of an eel
*  being processed in envy one.
*  Right. So you might think that that that the dimensionality law would change as a function of
*  where in the brain it's being processed.
*  Does that make sense? And yeah, would you think so?
*  Yeah, that is actually something.
*  So so the the motor cortex people, I'm just calling the motor cortex people,
*  but the people who study motor cortex are are very much there's there's a strong bias in that community
*  to think of those representations as low dimensional.
*  And I have discussed with them, they they think that their power law would be decay faster there than in
*  visual areas where basically that motor output is constrained to only so many dimensions.
*  And so that that might mean that there that the activity in that area is lower dimensional.
*  What do you think about? I mean, a related question is just cognitive functions, right?
*  So, you know, behave specific behaviors and specific cognitive functions.
*  Eventually, we have to think of them as low dimensional.
*  If, you know, if we call something working memory, for example, that is a low dimensional name given to a function.
*  And so do you think that the how do you think the dimensionality law would vary with respect to something like,
*  you know, image categorization, processing visual images versus something highfalutin like working memory or some of these higher function, higher cognitive functions?
*  Yeah, so that's a great question that we really don't really have enough data to answer.
*  So I think a lot of the working memory tasks have have been done with very few choices.
*  And so maybe you have two choices and then the activity ends up kind of being constrained to those kinds of the manifolds of those two choices,
*  like the responses to those two choices and the decision, which you might think of as decision signals telling the mouse to go left or right.
*  There's been slightly higher dimensional kinds of questions posed to monkeys decision making tasks,
*  post a monkeys like where there's multiple colors versus different motions of dots.
*  And so that becomes a little bit of a higher dimensional problem.
*  And then there they still see that kind of this activity gets gets sent to these lower dimensional modes.
*  And it's kind of I don't know if that's if that's always going to be the case.
*  Like, are there many of these low dimensional modes that you might find?
*  Right. Or like in the natural world, when you're going about your day, it's really hard for me to know if we can really generalize from the results from those studies to an animal in the real world.
*  I really don't have a good answer for that at all.
*  It's just it's still so early on.
*  I mean, part of the issue is obviously just how to deal with with data of such high dimension.
*  So so my next question is completely unfair, which is, you know, if you have plans for or vision for how to start introducing harder tasks for the animals to perform while recording these things and and looking at how that activity changes over time.
*  So sort of dynamics of it.
*  These are unfair questions, aren't they?
*  Yeah. So I personally I run a computational lab, so I won't be doing any of those experiments.
*  But but yeah, I think the field is moving towards more complex behaviors, more naturalistic behaviors.
*  And there's new it's not calcium imaging, but there are new probes called neuro pixels probes, which allow you to record many hundreds of neurons and freely moving mice.
*  So that will really open the doors in terms of the kinds of complex behaviors you can that you can look at while the mice are while you're recording many neurons.
*  And computationally, do you think that we're ready to meaningfully analyze such data?
*  That's a that's a great question.
*  So I am hoping that kind of the inferences we can make using calcium imaging data can help us analyze these kinds of smaller scale recording.
*  So so that's something that that I'm working on is trying to better understand what these behavioral representations are.
*  And then if you if you can figure out this mapping and in this large population of neurons, will that help you to figure out what the mapping should be?
*  And when you record maybe only a few tens of neurons in a single area.
*  So part of the in AI, at least in deep learning, you know, there's deep learning theory, right?
*  Which so the thing is, we have access to every single unit at any given moment.
*  Right. So in a in a deep neural network, for instance, so you can actually see the activity of any unit and know exactly what it's connected to and the exact strength between the connections.
*  And it's a big question right now.
*  It's an ongoing field of research to figure out what information you can extract from that, what it all means, like how how is the network in mass processing this?
*  And, you know, we're still not there yet with brains, obviously, but these high neural high high in recordings, many, many neurons that that you guys are doing using the calcium imaging, for instance, gets us a little bit closer to that.
*  So it's not like, you know, AI knows or neuroscience knows really what what it all means.
*  But I'm wondering if you think you were mentioning the adversarial images and how, like, if you take an image and then you can just add some Gaussian noise in a very particular way, add some Gaussian noise to it where and then the end result is an image.
*  Let's say let's say an eel.
*  Right. And then you add the Gaussian noise and the end result when you and I look at it still looks exactly like an eel.
*  But when a deep learning, a specific deep learning network looks at it, it might might classify it as a cat or whatever.
*  And this relates to the dimensionality finding that and the power that the specific power law that you guys have found with respect to how it's coded.
*  So I'm wondering, maybe you can just talk a little bit more about that and then whether what that means for like what how we might change deep neural networks moving forward to maybe be, I don't know, more general or what it means, what it means for AI.
*  If AI can learn anything from these results.
*  Well, I don't know what the right thing to do is, but I think one potential thing to do is is to try to change what you're trying to learn period that learning classes is not going to constrain the problem sufficiently to allow you to to create these kinds of smooth representations.
*  So, like in the in the natural world, we're constantly seeing images like of cats and the cats are in different locations on the image and we have to learn where the cats are.
*  We might have to to learn how the cats are moving, like optic flow information, and there's there's lots of different things we're extracting from these images, which are more things actually that.
*  Like you can think evolutionarily speaking that lower kind of animals that are earlier evolutionarily have to do that aren't just object recognition.
*  Like mice have to be able to track objects in the world and be able to turn around corners and things like that without bumping into things.
*  But they don't necessarily have to be like that's a car versus that's a cat.
*  I've thought about this a lot lately and I've really come to this idea that it's classically kind of backwards the way that we have approached, you know, even studying brains, right?
*  And ask image categorization.
*  It's such an unnatural thing to start with, right?
*  To start with, like, well, there are these categories in the world and that's what our brains do.
*  That's what that's what our intelligence is.
*  Figuring these things out.
*  But really, what what you perhaps would be better off starting with is the, you know, the behavior like the ecological functions, the needs of of organisms and stuff and building from that in that direction.
*  I don't know. What do you think about that?
*  Right. Yeah, that I think that's a that's a really crucial thing to try to understand is is what we're using vision for.
*  And what are what are like we need to understand what mice are using vision for and what kinds of tasks they can do.
*  And that's that's really kind of an underexplored space because we in mice and even in monkeys, too, we do these very constrained tasks.
*  And for instance, in a mouse, it's very hard for them to say, say, I show them to oriented gratings, one that's like horizontal and one that's at 45 degrees.
*  They have a lot of trouble with that task if they have to say which one's more horizontal.
*  But their their neurons code for those orientations with really high precision.
*  So the information is in their brain.
*  But those aren't the kinds of questions they need to answer on a day by day basis.
*  Yeah, that's kind of crazy to think about, actually, because that's one case where it's at odds with the story that evolution is chugging along and doing the best thing, you know, most efficient and all of that jazz.
*  Because to have all of the information there and then be unable to use it is an interesting thing or to not use it or to discard it or what you know, who knows if they could use it, I suppose.
*  But it's just not relevant.
*  Right. Yeah, that I guess it's it's been refined in a way that you have these many different features like you've made.
*  They it's it's been refined in such a way that it is high dimensional.
*  But then it's a question of what dimensions of that space do you use to drive behavior?
*  Yeah. And that's a really exciting question.
*  And it's a really hard question to answer.
*  Do you think that we are at a right next to really big advances in AI?
*  Or do you think that's a long way away still?
*  Because there was the deep learning revolution and everyone jumped out of their chairs.
*  And now we're all sitting back down in our chairs, realizing the limitations, all the many, many limitations and how really how far like deep neural networks are from.
*  So many of the things that we consider important cognitive functions.
*  So what what do you what do you see as the most important thing kind of missing from AI?
*  Like with deep learning? Yeah.
*  Oh, I would have to say, well, well, I don't know.
*  You know, I mean, it would just be a guess that that's part of the problem is that we don't know what the important thing is missing.
*  But I mean, for one thing, like you said, I would say embodiment and interaction with the world is just crucial.
*  But but there also needs to be something at stake for the for the AI agent.
*  Right. It needs to I don't know about if pain or emotion or death, you know, but there needs to be some something at stake to force the issue of
*  these same sorts of issues of layering on all of these different cognitive functions within this system.
*  But I don't think we understand the system well enough to begin with, to know how to to build it in.
*  And that's where you come in, because you're doing this great work really looking at this at such a high level, such a large population level.
*  This work, I think, is just it's really needed to to move our understanding forward of even what we even the right questions to ask, for instance.
*  Thanks. I think with AI, it's hard to say.
*  So if we add things like embodiment, though, and emotion, it might change what kinds of representations they learn.
*  But still, the I mean, at least in the case of computer vision, the AI is very good at these tasks, whether or not it has it has these representations.
*  So I think it will be a question of kind of if we if we make them more like the brain, I think at least in the case of computer vision, we might be getting closer to a place where they're going to be more efficient and have fewer parameters and maybe be more robust rather than necessarily
*  like solving new problems that they can't solve now.
*  Yeah, I mean, this also just goes back to the what the goal is in AI.
*  And I'm thinking less and less and less that the goal is to make human level AI, because I don't really I don't know what human level is.
*  And I think that humans are terrible at many things.
*  And that's just not what we would actually want AI to do.
*  Why would we want to replicate our terrible visual category systems relative to an AI or something?
*  Yeah, I think I think there is there are ideas of like, I think generalizing there there are instances of generalizability and there's AI has has trouble with with learning these many tasks and and things like that in terms of capacity.
*  And I think maybe we better understand how the brain represents kind of these lower level features.
*  It might help, at least in the case of computer vision in terms of having maybe a more universal model that can can solve all of these tasks.
*  But in terms of a universal model for how to to learn like a sequence of actions and these other more complex things that require memory and that sort of thing, I I don't think.
*  My work is going to necessarily help with that.
*  Do you do you think that it's unnecessary to look to the brain at all for building better AI?
*  Because it's an open question, right?
*  I mean, so what you're saying right now is that what we might should do instead is just look at the best way to do, for example, memory to do visual categorization and have these as a kind of separate components, expert separate components that then we can like put together in a system rather than build them all in the same.
*  Thing like a brain is right.
*  I I'm not sure I I see it as we partly as we're going to make these advances in AI potentially faster.
*  And we already have because I think neuroscience isn't answering these questions.
*  And so I think regardless, it's going to help to be able to build these circuits in a machine and see if we can learn some principles from them that we can then can use in the brain.
*  And it might be the case, like you're saying, that having these components as separate and learned separately is going to be the best way to do it rather than learning them in a holistic way, the way that a human learns in the world.
*  I just have this hunch that in the long run, so neuroscience is super slow, right?
*  And AI is super fast right now, but that in the long run, we're going to end up building principles into AI that we discover through the brain.
*  And we just won't be able to make something better necessarily, depending on what we want.
*  Obviously, like you're saying, if we want to categorize cats and eels, then we you know what we have is great.
*  You know, for example, although, you know, there is the adversarial examples.
*  I don't know. I mean, it's only really a feeling.
*  I have real I don't really have any principled reason for feeling this way.
*  But it's just a bet I have with myself in the world, I suppose, that that in the end, there will be contributions that the brain makes pretty fundamental contributions that the brain makes to AI.
*  And I'm just really blowing in the wind right now, but blowing hot air, right?
*  But I don't know. That's just my feeling.
*  You don't feel that way? I think it's going to be a lot further down the road is my concern.
*  I totally agree with that.
*  So I I am fascinated by the visual system.
*  And and it's also a really easy place, relatively easy place to study.
*  I can show images.
*  I can look at the responses.
*  Someone who's studying like hippocampus, for instance, they have they have so much more to worry about.
*  They don't. I just have this feed forward system from the relatively feed forward system from the thalamus to from the retina to the thalamus and so on.
*  You're looking at something like memory or and integrating these things in hippocampus.
*  There these these brain areas are getting inputs from everywhere.
*  Yeah. Yeah. And so really teasing apart exactly how they're doing this computation, I think, is going to take longer than it's going to take the visual field to have a better sense of of how these computations are taking visual computations are taking place.
*  Yeah, you're right. What you do is really quite simple, right?
*  Well, relatively speaking, I yeah, I am I think those problems are going to take a lot more experimental work as well to tease apart how those computations happen.
*  Well, that is a huge problem because experiments are so slow.
*  Yeah.
*  So Carson, what what what's going on in your lab?
*  What are you still hiring?
*  I know you're a pretty new faculty member and you I know you had been hiring for some time.
*  Are you still looking for people?
*  And and what's what's happening moving forward?
*  What are you guys doing?
*  Yeah, so I'm still looking to hire postdocs or grad students.
*  And we're we're working on these visual computations.
*  And we're also looking at these behavioral representations in visual cortex and in other areas.
*  And so I have a few people in my lab now who are really great that are working on some of these questions, like in particular, we're working on invariant texture recognition in mouse visual cortex.
*  So let's switch gears in the last few minutes here.
*  You know, so I have another listener question, and this is complete, completely orthogonal to our previous conversation.
*  But Gabriella, Gabriella, I imagine Gabriella asks.
*  Well, she said she knows that you're very pro diversity, equality, inclusivity.
*  And she's wondering how is a very big question.
*  How can we become a more diverse, equal and inclusive community?
*  Do you have ideas about this?
*  Yeah, I know that's a really I mean, that's a really hard problem to solve.
*  Can we start with like how much of a problem it is?
*  Because I think it's often just assumed these days it's assumed.
*  Oh, yeah, that's a that's a big problem.
*  But it's never asked, is it an actual problem?
*  And that's this where I get in trouble just asking the simple question if it actually is a problem.
*  And if so, then yeah, how do we move?
*  Yeah, so I can use the example of Janelia.
*  I think we're around 30 percent women group leaders or 25 percent women group leaders.
*  And we have one black group leader out of maybe 30 to 40.
*  So it's kind of where we're definitely not at the we're not equivalent to the population
*  distributions in terms of people in positions of power in science.
*  So that's one way to kind of gauge how how diverse the community is.
*  And then it's another question of how inclusive the community is, which is which is also can be which I mean,
*  if if the institute is more diverse than it may have a more inclusive community.
*  But that's also that's not necessarily the case either.
*  But most likely they probably do covary, I would imagine.
*  Yeah, yeah. And so so asking how inclusive it is, is kind of you you have to do more of these kinds of climate surveys.
*  And and these are done in the field and and consistently show that people from underrepresented groups
*  and women in science don't don't feel as welcome that they experience these microaggressions
*  from members of the dominant race and gender of white male and these sorts of things.
*  Is that how inclusivity is measured is through like surveys?
*  So that's one common way that I've I've heard of it being done.
*  But I don't know if there's a there's a better way to kind of measure kind of the the atmosphere of of an environment.
*  Yeah, yeah. I mean, I don't know if there would be there would be any other way.
*  I mean, I don't know. These are hard questions because they're also dependent on people's perceptions.
*  And this is a realm that I'm really not not familiar with or should really even be speaking my opinion.
*  I understand because I'm part of the privileged white male group that is a current target of all these things.
*  Right. And so it's hard for me to know how to think about these things.
*  So I should just stop talking, basically.
*  Well, it's not I mean, I wouldn't say that you're you're not a target.
*  It's more that it's it's that we as as white people in science have to acknowledge that we've had privilege going through our our education and that we're willing to step up and kind of get the training to be good mentors and support trainees from many different backgrounds and acknowledge that we have biases in the way that we hire and how we've been hired and that we've benefited from these systems.
*  And so it's getting it's getting kind of to that point of understanding.
*  So is the idea to going back to how to improve this and how to become more diverse?
*  Do privileged people need to then go against their biases?
*  I guess what you're saying is they just need to be trained better to be aware of their biases so that they can overcome them in making decisions like hiring and such.
*  Yeah. And in the way that they act in the community and how they interact with people.
*  I mean, one common thing is is like people like to hire people that they get along with, and it's often people that in your in group that you get along with better.
*  So if you're a white male, maybe you're more likely to hire postdocs that are white male.
*  And you have to have to acknowledge that that's not going to be beneficial for your lab, that you need many perspectives in your lab, and that just hiring someone that you kind of that you perceive as someone you get along with is not necessarily the even the best fit potentially for your lab.
*  Sure, of course. But do there need to be institutional rules that ensure some sort of equal outcome or do there just need to be policies that ensure equal opportunity?
*  I think both. So to get equal outcomes, you need to make sure that everyone has equal access to kind of mentoring once they're in in the program and that they're that they're all given the same kind of treatment.
*  And then equal opportunity as well in terms of of getting grants and that sort of thing. So one of the big so a recent study from from Kenneth Gibbs was was about this kind of that a big there are many underrepresented groups getting PhDs now that that has become better.
*  That that as a field, we've we've done better to some extent and on that front, but then many of them leave before they go on to get a postdoc or they leave after they get a postdoc.
*  And so it's a question of how to better advise students so that what they found in the study as well was that people from underrepresented groups were often less confident in their abilities.
*  And that's that's that comes down to an issue of mentoring 100% that the mentors were not giving adequate support to these trainees and not giving them the advice that they would need potentially to succeed in science.
*  I mean, these are really hard things, I think, moving forward.
*  But but I mean, it's a hard thing because the big problem is none of us get training in how to be good mentors.
*  Like many people, I mean, we become group leaders and and lab heads and we we aren't necessarily in the in a position to to be the best advisors that that we can be.
*  So I think it is a that is a is a step that every institute can kind of make.
*  But but is there is there an objective good mentor? I mean, isn't there some subjectivity in that as well?
*  Yeah, there are definitely like different mentoring styles.
*  But it also comes down to being able to read the kind of student you have and changing your mentoring style, depending on the student that you're working with.
*  And I think if if someone has training, maybe they'll recognize those those sorts of things and recognize how they how to better support the students they have.
*  Not that everyone has to be the same kind of mentor, obviously, but.
*  Yeah, do you think just personally, and maybe you do know the data on this, do you think that it is a few bad actors that are repeatedly, you know, I don't know, performing these microaggressions, making people feel excluded and stuff?
*  Or do you think it really is a much more systemic, low level thing that that many of us that the vast majority of us do without without knowing?
*  Um, so there's two aspects to that, like if there are bad actors that are then there are departments and there's lots of people in that department that are enabling them.
*  And they're not changing their behavior. So they're that already suggests that there is an acceptance there in some sense.
*  But the second point, yeah, I mean, I think unless we confront the fact that we have these unconscious biases, I think all of us can kind of.
*  My potentially be treating people differently without realizing it, and I think it is particularly in the US where we we often grow up in relatively segregated.
*  Societies, depending on what city you grow up in, it can often be the case that you mostly interact with people of your own race, and so you're you don't have the experience and kind of the perspective to to act as an inclusive person and you might not realize it.
*  How far do you think we have to go?
*  I mean, until until everyone feels like science is an inclusive environment.
*  Is that even possible for that to be fully manifests? Is that is that a possible future even?
*  I think that so people will always feel left out about it. Then it's a question of if people who feel left out, if there's a skew or a bias that people from.
*  From various groups feel more left out than other groups. That's a that's a big problem.
*  And so I think we have to if we can start to correct that, then we'll we'll be in a better place, but then we also need data on it like I think.
*  If Institute have done these surveys and they need to keep up kind of with checking in on are the policies and the changes that they're making actually working and making a difference.
*  And from studies that people do on these kinds of initiatives, they always say that kind of having numbers and keeping track of them kind of keeps departments accountable.
*  Right, yeah, I mean, there are there are initiatives like Neuro watch bias, I think it's called from Yale and there are some other metrics like that. And I think that sort of external viewable data is probably goes a long way toward correcting a wrong, I suppose.
*  Yeah, and I think that's something that that lots of places are starting to change to like for for tenure. There are certain institutes that require that a faculty member get recommendation letters from their graduate students.
*  So then that kind of raises the bar that they have to be good mentors to be able to progress in their career too.
*  So there's lots of ways to make sure that people are accountable, but they're not necessarily used in many institutions and can can often be neglected in some of our top institutions, even in the US.
*  Okay, so Gabrielle, I hope that that.
*  Do you have anything else to add Carson? This is, I mean, this is a it's not something that I talk about or ask about much on the podcast, knowing that it's a sensitive situation.
*  Also, way outside of my wheelhouse, my any sort of domain of expertise. So yeah, so is there something else to add before we move on?
*  Well, I should say one thing that like I don't consider myself an expert on this either. I've read about it, but I don't know the best solutions either. I just suggested some things that seem like kind of low hanging fruit that.
*  Sort of all departments can do and then I think the lowest hanging fruit I would say is that all of us can share our code and our data from our experiments.
*  And that allows, like, for instance, labs with less resources to use our data and do analyses and say, OK, I don't actually have to do another experiment for this paper. I can take data from someone else. I don't need the resources to do that.
*  People will hopefully then start to see things as in science as sort of like a collective pursuit rather than kind of a competition where we're pitting each other against each other.
*  Do you think that that I mean, we're on our way toward that toward these like really larger across lab collaborative efforts? I mean, that's that's just going to continue to happen, don't you think?
*  Yeah, I hope so. And I hope I think things will have to change in terms of the.
*  The incentive structure to some extent, too, in terms of of what kinds of papers are accepted and how grant money is is allocated.
*  So there are there are steps that still will need to be taken to help this problem of competition. But I think there are steps in the right direction.
*  Yeah, I mean, even when I was in graduate school, I was invited to give a talk at Yale and and I had collected all this experimental data.
*  And these were computational modelers that I was sitting around talking with, and they were saying they didn't understand why experimentalists wouldn't just readily give their data to them.
*  Right. So that they could then build models with. And to me, it was extremely clear because I'm trying to build my career.
*  And if I give you my data, you're you know, this is like a classic problem, right?
*  So this is a decades old maybe it was in the 90s. Someone wrote this famous paper.
*  I can't remember what it was, what it was about.
*  But it's a shame that I felt that way that, like, if I give that to you, it's going to vastly decrease my chances, chances at a good career, because this is my data that I could build a model on.
*  Of course, I never did.
*  But there is that feeling.
*  And that's the that's the kind of thing that hopefully is just going to disappear more and more.
*  Yeah. And I think as long as like if journals and people hold people accountable for sharing data, like I think the labs that have the most resources are the ones that can kind of that are the ones that should be doing it.
*  Like if you if you get a paper in a big journal, then you should be sharing your data then and you have the resources to share the data and to support your trainees.
*  And they're they're they're already more likely to get a job because they got that big paper out.
*  They cross that off the list. Yeah, that's true.
*  All right. So, Carson, thanks. And continued success and in your young but blossoming career.
*  And it's been great talking to you.
*  Thank you so much. Thanks for asking really interesting questions.
*  And you've clearly done your homework in terms of the questions that I'm working on.
*  So it's really fun to have an engaging conversation about them.
*  Brain inspired is a production of me and you.
*  I don't do advertisements.
*  You can support the show through Patreon for a trifling amount and get access to the full versions of all the episodes.
*  Plus bonus episodes that focus more on the cultural side but still have science.
*  Go to brandinspired.co and find the red Patreon button there.
*  To get in touch with me, email paul at brandinspired.co.
*  The music you hear is by the New Year.
*  Find them at the newyear.net.
*  Thank you for your support. See you next time.
