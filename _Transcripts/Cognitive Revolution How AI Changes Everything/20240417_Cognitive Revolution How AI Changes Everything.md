---
Date Generated: April 18, 2024
Transcription Model: whisper medium 20231117
Length: 5651s
Video Keywords: ['Descript']
Video Views: 839
Video Rating: None
---

# Reading Minds from Shared Latent Space
**Cognitive Revolution How AI Changes Everything:** [April 17, 2024](https://www.youtube.com/watch?v=7_BS8tuUoZY)
*  The first step that we're going to is get these complicated machine learning things that are currently only able to be done in an academic setting with a huge data set to work with very limited data.
*  Hopefully do things in real time, be able to do things with very constrained data sets and still get high quality results and furthermore be able to generalize this to different kinds of outputs that are more relevant than just perception.
*  So, for instance, we are collaborating with the University of Minnesota to try to do mental imagery reconstruction, visualizing an image and recreate that.
*  You can imagine that there's a lot of different pipelines that would be relevant here, like memory decoding, stuff like that.
*  We're working, for instance, with Princeton to collect new data.
*  We're trying to have more collaborations with academic institutions and the broader open science community.
*  And in that sense, we are open for people to help out.
*  If you think you can help us with these projects, we have several projects going on right now on the Med Arc Discord.
*  It's an opportunity to work on some cutting edge research together.
*  Hello and welcome to the cognitive revolution, where we interview visionary researchers, entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas and together we'll build a picture of how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Thornburg.
*  Hello and welcome back to the cognitive revolution.
*  With everything in AI going exponential all at once, I'm often amazed at what manages to fly under the radar.
*  Last year, for example, we had Tunishk Matthew Abraham, founder of Med Arc, on the show to talk about MindEye, an AI system that literally reads minds in the form of FMRI brain scan data and reconstructs the image that the patients had seen at the time of the scans.
*  Of course, there were some limitations to this technology.
*  At the time, it took 30 to 40 hours worth of scans to create a new model for a single human observer.
*  Today, however, my guest is Paul Scotty, lead author on the recent follow-up MindEye 2, which advances this technique by creating shared subject models, still with remarkably little data and compute required, that can be fine-tuned to a new subject and deliver remarkably high-quality image reconstructions with just one hour of new scans.
*  In this conversation, Paul shares the details of how they pulled this off, helping me understand the nature of the FMRI data that they used, what the visual cortex is believed to understand, and how it can be used to create a new model for a single human observer.
*  How they overcame that anatomical variation to create a shared subject plate in space.
*  How improvements in foundation models like StableDiffusion XL are making everything easier, faster, and cheaper.
*  The opportunities that this creates for new clinical and scientific applications.
*  The prospects for a neuroscience foundation model trained on millions of hours of data spanning multiple scan modalities.
*  The current limits and future potential of brain reading technology more broadly.
*  And how to think about the risks and governance challenges that may arise as this technology matures.
*  While in the grand scheme of things we're still quite early in the development of neural decoding technology, and a general purpose consumer-grade brain-computer interface remains science fiction for now,
*  Paul's work, especially considering the very minimal incremental compute that was required to produce it,
*  shows not only that an AI-powered understanding of the brain is increasingly feasible,
*  but also that all the investments currently being poured into foundation model research and training are starting to pay off in all kinds of unexpected ways across the full range of human endeavor.
*  As always, if you find this sort of pioneering work as fascinating as I do, please take a moment to share this episode with a friend.
*  I think everyone deserves to know that AI can read human minds.
*  And as always, you're welcome to reach out with feedback either via our website, cognitiverevolution.ai, or by DMing me on your favorite social network.
*  With that, I hope you enjoy this deep dive into AI-powered decoding of human brain activity with Paul Scotty of MedArc and Stability AI.
*  Paul Scotty, welcome to the Cognitive Revolution.
*  Thanks for having me.
*  I'm excited for this conversation.
*  So you are the lead author on a recent paper called MindEye 2, shared subject models enable fMRI to image with one hour of data.
*  Longtime listeners will know that we had an earlier episode with your teammates and the author of the original MindEye paper just nine months ago.
*  And I thought this one was worth following up on because with multiple reasons.
*  In general, the fact that we have brain reading technology in the world today and that you can literally use a machine to see what somebody is seeing is a pretty striking reality that a lot of people are missing amidst all the other noise and developments that are happening.
*  Also, the techniques under the hood are really interesting.
*  So I'm excited to get into a lot of the technical details and learn how you made this modern marvel happen.
*  You want to maybe just set up briefly where the first one left off and what motivated the part two of this project?
*  Yeah, to give a bit of history to this back in 2022, I joined Lyon Discord server, and I joined basically to get better acquainted with machine learning methods, learn how they are publishing really high quality work as an open source machine.
*  As an open community, and I appreciated their open science approach to things.
*  And as I was scrolling through that discord, I found that there was a channel dedicated to reconstructing images from brain activity.
*  And the person who was leading that was Tanish.
*  So I basically introduced myself and said, Hey, I'm already kind of doing this.
*  So I was a postdoc at the time in Ken Norman's lab.
*  And this is the direction that we wanted to go more so regarding memory.
*  But to reconstruct memory, you first need to reconstruct vision.
*  Right. So that's the direction we were going.
*  And at the time, there was not as much work being done in this space.
*  At least the quality of the results were not the quality that now these papers are able to show.
*  And it was actually like a perfect timing because there is a new data set that came out.
*  The natural scenes data set.
*  And this was really high quality data from eight participants being scanned for 30 to 40 hours each.
*  A very intense data collection effort from the nasal arts and K labs.
*  And this was an amazing opportunity to use better data quality.
*  And there were new open source models being released.
*  For instance, clip and stable diffusion were very great open source models that you could tap into.
*  So everything was there.
*  The pieces were there to get a new pipeline working for state of the art results.
*  So we teamed up and made this an open science project with my night one.
*  And when we released my night one, it was a great reception.
*  And there were also many other papers that were doing the same sort of approaches.
*  For instance, Ferkin or Salik had a brain diffuser paper that was also showing really good results using similar approaches.
*  And the constraints with my night one and the similar papers was that all the models are being trained independently.
*  So you have 40 hours of data from one person and you train the entire pipeline on just that one person.
*  It's not being trained across multiple people.
*  So if you have a new person that you want to apply these models to, you would basically need to put them back into the MRI machine and scan them for 30 to 40 hours.
*  And it's like a thousand dollars an hour to scan somebody.
*  So it's really not realistic for follow up work.
*  So if you want to apply this kind of stuff to new directions like memory, mental imagery, dream reconstructions, biomarker diagnosis, have it usable by people in hospitals like clinicians, you're just not going to get the ability to apply these models.
*  So that's the focus we are working towards.
*  And my night two is that step in that direction that we now have output.
*  It basically allows you to with a totally new subject, collect one hour of data and get good, not as good as if you had 40 hours, but a lot better than you would have had with only one hour.
*  So it's like near the same level of quality with 2.5% the amount of data as before.
*  Yeah, there's a couple of really interesting things here about the relative magnitudes of data.
*  And there's a couple of interesting connections also to some recent like a recent episode we did on robotics.
*  So let me just try to highlight a couple of things and you can react to these.
*  One of the challenges, obviously, as you said, for this sort of problem is scarcity of data, right?
*  And that's again true in robotics as well.
*  There's just a limited amount of sort of how does a robot go about solving this problem?
*  In this case, there's like a very limited amount of fMRI data available to train models on.
*  So even in the first MindEye paper, one of the big ideas was we can combine this like relatively modest data set that we have with these foundation models in a clever way to tap into this kind of general purpose understanding of images that they have already learned from their web scale training.
*  And we're going to find a way to tap into this with a data set that's comparatively much smaller, but is still big in the fMRI sense.
*  And now you're taking another order of magnitude or close to two order of magnitude step in terms of how much incremental data is required to start to unlock this capability for a particular person.
*  That's really interesting because these sort of foundation models that embody a sort of a world model and obviously that topic is like hotly debated in terms of exactly how we should understand it.
*  But it is increasingly clear with all these different applications that it has a lot in there that if you figure out how to augment it in just the right way, you don't necessarily need to bring a ton of new data to the table to make really cool things happen.
*  That's just a really profound takeaway from this work.
*  Can we talk about the data set itself for a second?
*  First of all, do I understand quickly that the mind eye one and mind eye two papers are using the same data set?
*  Is that right? Yeah. Okay, cool.
*  Let me just run down a couple of things to make sure I understand it.
*  You can correct me if I have any misconceptions.
*  I believe there are eight patients that participated in this collection set.
*  They participated between 30 and 40 hours in an fMRI each.
*  And there's one table in the paper that I wasn't quite clear on, which is the in figure two, where there's this list of subjects and how many hours they were in there.
*  And then the number is that the number of input output pairs for each?
*  I think that's the number of voxels that get fed into the model to put them in a shared space.
*  Gotcha. Okay, let's go back to voxels in just one second.
*  So they're in there for 30 to 40 hours each.
*  Their experience during that time is what they're getting shown an image every how many seconds?
*  Every four seconds. So everyone was requested to be scanned for 40 hours.
*  Not everybody got through the full amount.
*  But for instance, for the subject one, they were there for 40 separate sessions, 40 visits to the MRI.
*  And they saw 750 images per visit. So per hour, basically.
*  So it's three seconds of looking at an image, then one second of blank period, and then another three seconds of a different image.
*  And the task is to press a button inside of the machine if they ever see an image again.
*  So every image was shown three times throughout the entirety of the 40 sessions.
*  Interesting. So they and they are identified.
*  It could be a total of like 40,000 images that a person sees. 30,000 to 40,000 images where every image gets shown three times.
*  Gotcha. Okay, interesting. And is there something that that sort of clicker data is used for?
*  Or is that primarily just to keep them engaged and make sure that they're actually still looking at thinking about the images that they're seeing?
*  Yeah, we didn't use it. But I think it could be used.
*  There's been some other papers that try to do the opposite of what we're doing.
*  Like you try to predict the brain data instead of predict the image.
*  And the state of the art for that is you use all the behavioral information that you have possible to better predict the brain data.
*  That shows that it can be useful. We tried to get that to work.
*  We weren't having much success, so we ultimately didn't use it.
*  Gotcha. Okay, cool. Then let's talk also about just what is measured.
*  So every four seconds, they get a three second view of an image, a one second blank during that time when eyes are on a particular image.
*  We're taking is it just one data point or multiple data points of the brain activity during that three second window?
*  Yeah, so I think it's taking a snapshot every second. I might be wrong.
*  This is the so-called repetition time of the MRI machine.
*  So you're taking a full picture of the entire 3D brain every X seconds where X is the repetition time of the machine.
*  So it's not a continuous measurement. It's like every second you get a full picture of the brain.
*  And then they use a general linear model to basically convert it from this time series, like every second measurement to a single measurement per image.
*  Gotcha. Okay, cool. Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omnike so much that I invested in it, and I recommend you use it to use Cogrev to get a 10% discount.
*  And then in terms of the actual biological function that is measured and sort of the space that is measured, the fMRI is measuring blood flow, if I understand correctly.
*  And I had to look back at my notes with Tanishka on this one, but he described it as a two millimeter cube resolution.
*  So the way I thought of that was if I kind of imagine my visual cortex being at the back of my brain and the number of voxels from this chart is like in the sort of the lowest number is 12,000 and some the highest number is 17,000 and some.
*  If a single voxel is two millimeters cubed, then you have five by five with a centimeter cubed, which should give you 125 voxels per cubic centimeter.
*  And then to get to those numbers, you'd need to have a 10 by 10, like layer. So it's 10 centimeters by 10 centimeters with these sort of rice grained two millimeter cube bits with a single number for each one that measures the blood flow to that small little region within the broader visual cortex.
*  That all sounds right?
*  Yeah, yeah, basically just kind of restate like with fMRI, you are processing these images and the parts of your brain that are more involved in processing the image are going to consume more resources.
*  And basically the brain needs to resupply those parts of the brain with more blood when it's been used. And the machine itself is measuring the oxygenation changes that are associated with increased blood flow to those parts of the brain.
*  And so we are measuring that oxygenation, blood level oxygenation change in the corresponding 1.8 millimeter cubes of the brain where every voxel is hundreds of thousands of individual neurons.
*  So you have a whole brain that's completely divided into all these voxels. We only take the voxels from the visual cortex specifically and feed those into the model.
*  Okay, first of all, that's remarkable that it's a pretty crude measure in some sense, right? It's like a it's both like at least one step conceptually removed from what you would presumably think of would be the ground truth of what neurons are firing.
*  It's aggregating also at you know, as you said, like the hundreds of thousands of neurons being compressed into one data point.
*  I'm also a little curious about how the different individuals end up with different numbers of voxels. Is that just a reflection of anatomy? Like people have different brain sizes and you're kind of segmenting?
*  Yeah, some people have bigger brains than others. Some people have differently shaped brains and also people have different topography of just how they represent things like the functional topography.
*  So you're looking for voxels that are receptive to visual processing, right? And so where you cut off where the visual cortex is going to be different for every person and it's going to be differently shaped.
*  And so you'll have different numbers of voxels that are corresponding to the visual cortex. But in addition to that, just in general, people will have different numbers of voxels and not every voxel has like a correspondence to the same voxel in somebody else's brain.
*  So that's why it's difficult to have shared subject modeling because there's all these variations in how people represent things and how the brain like the input data itself is a different dimensionality, right?
*  Yeah, interesting. So is that something that a clinician or a technician is doing based on their familiarity with fMRI scans? Is somebody actually like sitting there and drawing a line around it?
*  Or is there some automated process for determining what the region is that will be considered for an individual patient for kind of large scale, determining of where the different regions are.
*  You can use some automated software for that. There's parcellations that you can use that are based on large scale data sets where generally speaking, you can look at the different like psilocybin, gyri of the brain and figure out where it should be cut off.
*  For more specific brain regions, there's functional localizers. You can do retinotopic mapping. Basically, the occipital cortex has its own special way of representing where it should correspond to where in your visual field your inputs from the retina are coming from.
*  So there's some more nuanced stuff that you can do for it, but for just like visual cortex, you could rely on automated software. Yeah, it's not like you're subjectively looking at someone's brain and drawing where the different regions are.
*  So did I understand correctly that the one technique that you're describing there would basically amount to calibrating the system by showing a light in one corner of the visual field and then looking for where that lights up and creating a map of, okay, this is how this person seems to represent the visual field based on the fact that we know what we showed them and we know that there's going to be a surge of activity corresponding to that. Am I getting that right?
*  Yeah, pretty much. It's like you basically are just looking at where in the brain are you getting visual inputs and essentially you have these repeated images, right? You could directly quantify what parts of the brain are receptive to these visual images because you expect that if you have a repeat that the same, the brain regions responsible are going to look similar. They should look similar if you look at the same thing, right?
*  But if there's no sort of correlation between image repeats, then probably that information is not what you want for perception at least. So that's one way that you could quantitatively figure out the brain regions that you want. But also just we know that visual cortex is probably the most important part of the brain to use for this. We did try using the whole brain, but it didn't work out as well.
*  Interesting. So this data set actually contains a lot more voxels than are being specifically used for this project.
*  Yeah, yeah, you get the whole brain for every snapshot, but we only subset out the visual cortex.
*  Interesting. Okay, cool. So we've got something on the order of 10,000 ish images, each kind of shown three times. Each measurement of activity corresponds to essentially a vector of 12 to 17,000 numbers, which indicate activity in these tiny little regions 12 to 17,000 because everybody's anatomy is different.
*  And so you're on the order of 10,000 times 10,000, like 100 million numbers for an individual patient. And that's all drawn from this 30 to 40 hours in the fMRI machine. So that's not nothing, but unto itself, let's like still not enough to train this sort of image reconstruction.
*  So maybe give us a little bit of the kind of motivation for or maybe the intellectual history of how you guys realized that there was this opportunity to tap into even bigger scale, web scale foundation models that had already been pre-trained and were available to.
*  The key thing is that you don't want to map the voxels to pixels, right? It would just be an insane task. The number of parameters would explode and you're not relying on rich representational information like semantics of what is the image.
*  That's the kind of space that you want to map the brains into. You want to map from brain to some more compressed rich space. And that's why we mapped to clip space in particular.
*  And because clip has this kind of rich semantic information, if you use even better clip models, it even has basically low level information. You can exactly reconstruct the image from the latency.
*  So that was like the key insight map it to clip and that'll allow you to really allow yourself to get high quality reconstruction result. Passwork would do stuff like Gabor filters and CNN based approaches where the key insight here is just do whatever you can to map into this frozen pre-trained space.
*  Yeah, we recently covered units in a bit of depth on a recent episode, specifically a Mamba variation on a unit. And so I think of this as analogous to mapping onto the bottom of the unit.
*  You're mapping to the conceptual space where the image data has been convolved if it's a convolutional network and abstracted away from the lowest level raw pixel inputs and to a state where it is like fewer channels, but deeper dimensions, more meaning per channel.
*  And then as the unit kind of sweeps up the other side, it is gradually unpacking that into pixel level data again. And similarly, that's what the diffusion models are doing, right? They're starting with this like high meaning, but low precision and then unpacking that into something that you can actually render again as pixels and see what it looks like.
*  This is a really interesting point. And one of the big things I try to do with this show is help people develop their sort of conceptual intuition because there's so much technical stuff. There's so much notation. Is there anything else that you could offer about the nature of the space into which you are mapping the brain data?
*  Yeah, these are foundation models that have uses beyond just image and language. Clearly you're able to map brain data into clip and you could see that as like another modality that you're appending to a frozen model. Basically, my take on it is that as AI foundation models get better and better, the ability for medical applications will also get better and better.
*  For instance, we use stable diffusion Excel for this new paper, whereas we used versatile diffusion for MindEye 1. And the better the image generators get, the better we'll be able to tap into that. And the better the representations get for which we map the brain data into, the better the results will be.
*  Yeah, let's come back to that in a second. So it seems like there's two big drivers of why this project ultimately the end of the day, each project has a figure and the figure from MindEye 1 is here are the images that the people saw and here's what we are looking at.
*  It seems like there's two big drivers of why this project ultimately the end of the day, each project has a figure and the figure from MindEye 1 is here are the images that the people saw and here's what we are able to recreate.
*  And some of them are incredibly good where you're like, wow, that is crystal clear brain reading. And then as you get a little deeper into the data set, like some of them are not so good or uncanny valley.
*  And MindEye 2 at the simplest highest level analysis, like the images look even more like what the person saw and the reconstruction is at just a glance is obviously improved.
*  It seems like there's two main drivers of this improvement. One is that you've figured out a way to not have to train a single model for each individual person, but instead mix their data together.
*  This is conceptually super important as that as you mentioned at the top allows you to collect a lot less data for a person, which means like to the degree that there are going to be clinical applications for this, you can actually get there in a reasonable amount of time and effort and expense.
*  And then the other thing you're looking at just now is the image generation models themselves are getting a lot better. There's some of this stuff coming for free because rising tide of just general performance is lifting all of the different project boats toward your metaphor.
*  How would you break those down? What do you think is important? And what is the kind of relative contribution of those two conceptual advances to the overall headline view that like, oh my God, the reconstruction are looking really good.
*  Yeah, so there's two points to this. One is specifically if you isolate the shared subject part and discount the fact that we're using different models, like we're mapping to a different clip space, we're using a different image generation model.
*  So if you only look at the shared subject part, we do an ablation in the paper and show that is a notable increased performance. So just by that by itself using shared subject modeling, even if you're using the full data set, you know that you'll get state of the art results.
*  So we focus on the one hour use case here, but if you use the full amount of data, then you get state of the art reconstruction retrieval results. The second part, the clip model. So you can take out the shared subject part and use the new models and everything.
*  And that also gives you notable improvements in performance. So they're both giving obvious improvements for both of these. And also another part of the paper, it's not the focus of the paper, but we trained our own unclip model for this.
*  So it's actually state of the art unclip clip image embedding to image state of the art performance in that domain by itself. So we fine tune stable diffusion Excel to be able to reconstruct the image from ground truth clip image embeddings in a way that preserves both the high level meaning and the low level image details.
*  And that raises the possible ceiling of the quality of results you can get because the previous models that mostly these papers were using was versatile diffusion. And basically, if you give it an image, say people cooking in a kitchen or something, and you convert that to clip image embeddings, you can get a very good result.
*  And then you undo it back to the original image, you don't really get the original image, you'll get like something that maybe resembles a kitchen and a chef, but you're not going to get them in the right spot. They're not going to be wearing the right things. Lighting is going to be different and all that.
*  So we specifically had to train our own thing to raise the performance of that. And so we tap into the new space allowable by the ability to unclip better than before.
*  Okay, I want to break this down and get a little bit more into the performance of the paper. So we have a little bit of a
*  I'm looking at figure two, we can maybe overlay this on the YouTube version and maybe put this on the link to this image in the show notes as well. There's two main parts of the overall pipeline, right? There is the part that works on the brain data. And there the big advance is creating a single model that combines all of the data that's being used in the paper.
*  The part that works on the brain data and there the big advance is creating a single model that combines all of the individuals into a single shared latent brain space. And then the other side is, okay, now we're figuring out how to tap into the power of these foundation models by figuring out the best possible way to convert the latent into an actual good looking image.
*  This wasn't maybe entirely clear to me, but you're saying that the image portion in this figure, figure two in the paper, the brain side is shown as with fire emojis, which means that those parts are actively trained and then the image parts are shown with the snowflake indicating that they're frozen.
*  But you're saying that they were first fine tuned and then frozen for the purpose of doing each individual person's model. Is that right?
*  The difference between the flames and the snowflakes is basically like, ideally, all of these models that are in the snowflakes would already be out there. And we would just like tap into them during inference to get the final results. And like the actual mind eye to model itself is only training the parts that are indicated with the flames like the MLP and the diffusion prior stuff.
*  The nuance that I was talking about is that when you've converted the brain into clip image space, and then you want to undo it, aka use an unclip model, there didn't exist a good unclip model. So ideally, someone else would have done it already, and we would just use theirs. But since a good one didn't exist, we fine tuned SDXL to make a better unclip model. And then we use that.
*  Okay, cool. That's helpful.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The tech world turns to the Brave browser for its unbeatable privacy protections. But did you know that Brave also has a private ad platform? Brave ads offers first party targeting, and it's been cookie lists since day one, so you can relax while third party tracking cookies disappear from the web.
*  Today, millions of people turn to ad blockers to avoid being tracked and pestered online. But Brave's new ad model aligns incentives for users and advertisers. Users earn rewards for viewing ads, which they can save, spend or pass along to their favorite creators. And advertisers score points for respecting user privacy, generating ROI without invasive tracking.
*  So whether it's high impact announcements on the new tab page, or keyword targeted ads in Brave search, Brave offers diverse private future proof ad formats for all your business goals. Join the future of advertising at brave.com slash ads. Mention MOZ when signing up for a 25% discount on your first campaign.
*  Today's podcast is brought to you by Plum. It's 2024. Do you really need to be a staff engineer to understand how your AI feature works? Plum doesn't think so. That's why they've created a no code AI app builder that non-technical folks can understand at a glance. A drag, drop and configure visual pipeline for any AI feature you can imagine.
*  Plum gives product teams a place to go from prototype to prod together. Check out useplum.com. That's Plum with a B for early access.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable and do more with less, especially with engineering. Listen, I love your 30 year old ex-fang senior software engineer as much as the next guy. But honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale from sourcing to interviewing to on the ground operations and management. That's why I teamed up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high level for over five years to help you access global engineering without the headache.
*  Squat, Sean's new company, takes care of sourcing, legal compliance and local HR for global talent so you don't have to. With teams across Asia and South America, we can cover you no matter which time zone you operate in.
*  Their engineers follow your process and use your tools. They work with React, Next.js or your favorite front-end frameworks. And on the backend, they're experts at Node, Python, Java and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's doing two hours of work per week but billing you for 40. But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn. Head to choose Squat.com and mention Turpentine to skip the wait list.
*  Let's just go into a little bit more detail then on each half of this. Maybe start with the image one because it seems like that's the first part of the work. And once that's solid and working, then you can go over and do the brain to image mapping portion.
*  You said earlier that if you take a clip latent and try to unclip it, you get something that is semantically aligned with whatever the input was but may look quite different.
*  And this I would take to be a reflection of the original clip conceptually was aligning text and image space and driven by going back to your Lion project, the Lion 5B, right? It's like the 5 billion images pulled off the internet that are captioned with obviously a lot of noise in those captions, a lot of not super specific.
*  Typical web caption is not like describing in specific detail, like which elements are in which portion of the image. It's not containing all these sorts of layout type details. It's just saying high level. What is this at best? And it might even be worse than that.
*  And just off topic. So there's a lot of noise in the underlying data set for aligning text and image. The captions are not really meant to allow you to reconstruct. They're just meant to summarize and give a sense for what the image is.
*  So it makes sense that when you have this aligned space and you try to reverse out of the space into image space that you would have a fairly wide range of images.
*  All of which would correspond to the meaning. Like there is a tiger is it's a tiger. Be a tiger in a lot of poses, doing a lot of different stuff and with a lot of different backgrounds, whatever. So all of those are possible from this the diffusion prior or the latent that represents a tiger.
*  They can go in a lot of different directions of images. That's cool, right? Because that's why you can get different images every time from the same prompt out of a diffusion model. There's like just a lot of ways you can go. But you don't want that flexibility in this use case, right? You want to actually get back very specifically to the thing that the person saw.
*  So there's a complicated mix of techniques. You want to describe the mix of techniques that augment this semantic content with more low level visual detail. And there's also the captioning portion. I'm interested to hear how you conceive of all that working together.
*  Yeah, so basically to get back to the idea of like clip is semantic, right? So with unclip models going from clip back to image, the typical way that these models work is that you take the final output of basically the classification of the image.
*  So basically to get back to the idea of like clip is semantic, right? So with unclip models going from clip back to image, the typical way that these models work is that you take the final output of basically the classification token, the pooled output of the contrastively trained clip model, trying to align the image captions with the original image.
*  And then you feed that through some model that gets you back the pixel image. And that is going to be highly semantic. And people like that because it gave you this kind of creative flexibility. It was called image variations models.
*  So like you give the model an image and then it gives you a creative re-representation of that image. We didn't want that, like you said. We wanted exactly the original image, which at first glance might seem kind of contradictory.
*  Why do you want to be able to input an image and then output the same image? Like why, what's the point? But the point is that you're able to then cut off the beginning, just feed in the latent and then get back the original image.
*  And so that's the basis for training our own unclip model. We don't use the pooled output. We actually use the kind of like last hidden layer. So all of the outputs from each of the tokens that were represented in the vision transformer.
*  So it's a much higher dimensionality than just the final output of the clip model. And what's actually pretty interesting in its own right is that you can basically get back the exact original image from the clip latent if you take it from that point.
*  So even though it's only trained to contrastively match the captions with the image, the clip model somehow learns to represent the entirety of the image itself. So you can get back basically the original image from the clip latent.
*  Now this wasn't possible with MindEye 1, which meant that we needed to have a total low level pipeline where we are predicting a blurry representation of this image that doesn't care about semantics at all.
*  And then we use that as the initial starting point for the denoising diffusion process. So instead of starting from noise, we start from this kind of separately obtained blurry reconstruction and then go to the finished product from there.
*  And the blurry representation was not using a clip model. It was using other models like the VAE of stable diffusion.
*  And it had no semantics to it, but it was able to more or less have a darker region where the person should be. And maybe it has the sky is blue. And that's the extent of it. But at least it had this kind of low level representation to it.
*  So with MindEye 2, we consolidated that low level pipeline into the full pipeline. So we don't have to train two separate pipelines anymore. And also, we have a lot of different models that we can use to get back the image.
*  We don't have to train two separate pipelines anymore. And also, we realized that this new clip latent with the unclip basically does have the low level properties now.
*  It's not as important to have the low level pipeline at all. And the ablations that we use for the paper, like, we don't even need to start from the low level reconstruction and use that as a starting point.
*  It actually does worse when you do it like that. The low level, there are a couple of points to the figure 2, which we do, which kind of makes it look complicated, but you could actually remove and it doesn't really affect the performance that much.
*  So the low level stuff, getting this blurry reconstruction from MindEye 2, you really don't need it. It's more like it improved the low level statistics in the table to get the state of the art results.
*  But subjectively speaking, it didn't really do that much to it. We also have this kind of captioning module that is trying to predict from the brain the caption associated with the image to reconstruct.
*  And we use that to further guide the final output. So maybe the caption is a cat on a table. And so we feed that caption into the refinement process to get the final image.
*  That also didn't really matter that much. Like, it's cool to show that you can predict the caption from the brain. But honestly, the vast majority of the information here is contained in that clip.
*  You could throw out the captioning and the low level and it will do nearly as well.
*  Okay, that's fascinating. Let me try to restate some of that back to you and make sure that I understand it. In the earlier version, going back to MindEye 1, the foundation model that you were able to use was semantic but not structural in terms of what it represented.
*  This is why you would have this kind of like when you go use stable diffusion, you could say a tiger and it'll give you many different tigers because there's a lot of different ways to represent that.
*  So to get something that actually looked like the image that the person was using at that time, you had to start the diffusion process from essentially structural hint.
*  So you're combining two things saying here is what is represented. This is where we want to go. And here's the loose hint starting point of the regions of the image so that you can fill in appropriately.
*  And at that time, that was quite necessary to get things to work reasonably well. Now, if I understand correctly, it's largely because the.
*  This is really interesting and potentially quite subtle point. Maybe you have clarity on it, but I don't quite yet. It seems like it's because the foundation model is so much better that essentially now you can just take this diffusion prior, which is what the.
*  The second half, which we'll get to in a second, the mapping from the brain data to this space, what that outputs is now so rich in in meaning that it basically works straight away and you get images that look like the original image.
*  And then you also experimented with a couple of these other things to do that visual hint suggestion again. And then now you also have the caption hint suggestion.
*  And those sounds like kind of boost, let's say, yeah, it gives a slight boost to the metrics, but overall it doesn't actually make that big of a difference.
*  And yeah, we're able to get really good.
*  Caption predictions from the brain, but more or less the bulk of the model is explained by mapping brain into a frozen pre trained clip image embedding space.
*  So the very practical interpretation of that is if you remove these additional hints and just run this down the fairway, simplest version of this, then the images you get out still look like what you expect them to look like.
*  And as a human looking at them, you're like, this is working. And then you add these other things and it improves these scores, which are obviously more objective, but perhaps not necessarily super meaningful.
*  These are like pixel level comparison type. Yeah, it's like you can see the correlation of the original image and the reconstructed image at where you like feed them both through a frozen network and you compare how similar the intermediate parts of the networks are.
*  And honestly, we had some complaints about the metrics themselves, which we hinted throughout the paper saying that these metrics are not very good.
*  So like you can have reconstructions that to me are obviously better and they'll score worse on these metrics. And we actually did some human testing.
*  We showed people online human raiders the different images and had them pick the ones that they prefer better.
*  And it's like, clearly there's a disconnect between these quantitative metrics that are being used in all these papers and subjective preference for what people think is the better reconstruction from perception.
*  Yeah. Okay. We're hitting a lot of frontiers at the same time, generally across the whole vast field of AI.
*  So like that is becoming a very live issue. These sort of robotic scoring methods that we've used in the past are hitting their limits.
*  And all of a sudden it's like there's a lot of noise, obviously in human evaluations as well. Is there a just like human like how good is this score? Did you guys just try doing everybody rate this one to 10 or something?
*  We had an alternative forced choice. You show two things and then they pick the one that they think better resembles the original image, which could have its own problems.
*  It might be more biased towards looking like a naturalistic image rather than retaining low level properties. That was not perfect solution.
*  But yeah, I'm not quite sure what the best way is to measure the quality of these kind of results.
*  Because for instance, the low level modules, the blurry stuff, like we get really good results with the low level just by doing a simple averaging process with the blurry reconstruction.
*  It's very crude, but it works really well for the final evaluations. But subjectively, I think it looks worse. So I don't really know what to make of that.
*  But for these kind of papers, you have to show that you're able to get the state of the art tables with these metrics.
*  It's tough. One of the things that I've done that has informed my thinking about a lot of these metrics, perhaps more than anything else really, is trying to get a system together that would do an effective aesthetic evaluation of images.
*  This is something that in my company, which people have heard me talk about many times, Waymark, we make videos for small businesses, blah, blah, blah.
*  We need to choose from their image library images that both semantically correspond to what they're talking about in the videos that we're generating and also ideally the ones that look good.
*  And that looking good part is a real challenge. And part of the reason it's such a challenge is that people just have a lot of disagreement as to what looks good.
*  The AVA data set that came out six, seven years ago, maybe at this point, has about 100 data points per image.
*  Like they went on Mechanical Turk or whatever and just had people rate these images. But you would think, geez, why do you need 100 images or 100 ratings per image in this data set?
*  And the answer is that there's so much variation that they ultimately report a mean and a standard deviation for each image as opposed to a single score, because at the end of the day, it's just too much noise in how people think about these images.
*  And we can't really reduce that in for any practical purposes.
*  The evaluation is like across the board is becoming a very interesting topic where it's like we're hitting certain limits, if not the end of what robotic scoring can do for us.
*  But then when we look inward and say, what do we think about this, we're confronted by the fact that we often disagree.
*  I would also be really interested to see research as to how individuals disagree with themselves over time. There probably is some of that in other settings, but definitely across people disagree quite a bit.
*  And I would suspect even an individual will be subject to quite a bit of drift over time.
*  So, OK, here's one thing I don't really understand. And maybe you answer this in part with the description of more the FMRI side of this equation.
*  But where is the semantic information coming from?
*  I'm understanding that we have these voxels in the visual cortex. This corresponds to blood flow.
*  My sort of very naive version of what's going on in the brain is that the visual cortex is like a convolutional network and it's working up from like low level edge detection type stuff into higher order concepts.
*  But I'm not really sure how far that goes, and I'm not sure if in my visual cortex I get to the point where back there it's understanding that it's a tiger or if these high level concepts need to be sent forward to even higher order processing that would be like, OK, that's a tiger.
*  But you're mapping this stuff from the back of the brain to the latent space where you're saying that this both the what I would expect is that the like the visual, the structural data would be there.
*  If you just said, hey, we can get what colors people are seeing in what regions and from this noisy thing, we can back that out to an image.
*  I get that when it's I can also get a caption out of that.
*  I'm like, huh, is that because that semantic data is in the data pulled from the FMRI like it's represented by the blood flow?
*  Or is this something that the clip model is doing for us because it has done the work of doing the brain has both of these.
*  So like I'm including higher level processing areas of the brain in the visual cortex, right?
*  The very back of the brain, primary visual cortex, you'll get V1, V2.
*  These are just representing orientation lines, maybe colors as you continue the visual hierarchy.
*  But you get to the inferior temporal cortex and this area of the brain has specialized semantic processing.
*  One example would be the fusiform face area. It's very specific to processing human faces.
*  So there's a lot of rich semantic information in the brain that is being fed through the model.
*  Now, you could feed only the primate visual cortex into this model, in which case it's not going to have the semantic stuff and it's not going to do as well in mapping the clip space.
*  Gotcha. That sounds like something that you could do by segmenting.
*  Basically, you would have just fewer voxels to work with and you could say we have a good enough understanding of the regions of the brain to I apologize for being relatively ignorant of the biology and the neuroscience under this.
*  Would you say there's a general consensus as to what regions you would not include if you were going to try to just work with the lower level like content representations as opposed to the semantic understanding?
*  Yeah, if you only cared about low level, then you can just isolate to the V1234 primate visual cortex.
*  But part of the reason this is an exciting field of work is because you're tapping into someone's representation, like their cognitive representation of what they are looking at.
*  If you only cared about getting an exact reconstruction of the image, then just tap into your retina or put a camera in front of your eye.
*  Like where is the importance to these kind of works if you're just getting a one to one representation back of what you're looking at?
*  What you actually care about is the nuance behind what I am representing versus what somebody else is representing.
*  It's like looking into the brain and seeing specifically what is leading to your specific representation.
*  What is your like past history, your biases, all of the parts of your brain that have led to your current functional topography and how you represent things.
*  That is the thing that we care about and what will ultimately be relevant for follow up work like comparing clinical populations and stuff.
*  Yeah, OK. So this is another kind of key theme that comes up all the time where the space that we're ultimately mapping into was originally created by aligning text and image.
*  And with that initial work, you could get into that space either by giving it text or giving it an image, right?
*  You could get into this sort of shared aligned text image space either way.
*  But you couldn't necessarily get to the spaces that we're actually finding here with the brain data because this is essentially bringing both right.
*  It's bringing both the what did I see in the raw low level kind of data and also how did I conceptualize that and finding a space that you could presumably not access exclusively with text or exclusively with an image and representing both kinds of information there at the same time.
*  That's definitely really interesting.
*  One thing to highlight on this is that what people get away from this paper is we can get really high quality reconstructions of what you're looking at from the brain.
*  What I found that people, especially neuro imagers like the neuroscience community, seems to value more is actually the retrieval component.
*  So this is mapping brain space to basically a third modality of clip.
*  This is a retrieval module in the paper, trained with contrastive loss, and that allows you to do stuff like find the nearest neighbor in clip space.
*  It allows you to basically have a brain latent that you can compare to any other clip later than you want and see where you are along that axis, stuff like that.
*  And this is where we show that it has such fine grained representation.
*  One of the criticisms that I've been seeing is like, okay, it knows it's an elephant and whatever.
*  But you're like we show that you can you have a really fine grained nuance here.
*  You can determine that it is this exact zebra image out of like 20 zebra images.
*  Like you can get perfect matches with pretty high accuracy if you are relying on this retrieval submodule.
*  And there's a lot of applications that can be done from that, knowing that you're having such fine grained information.
*  It's not just like the overall category of the image.
*  It's not just a picture of an animal. Yeah.
*  Okay. Let's talk a little bit about the details of just the fireside of the figure two where the animal is.
*  Of the figure two where the voxels are being merged into the same space and then ultimately mapped in some ways that might be more intuitive for people.
*  I guess the basic strategy is just like we need a single latent space, but we have different dimensional data because people's brain sizes and that is different as we talked about.
*  So there is a per patient adapter that is trained to map each individual's data into this shared space.
*  And then from that shared space, everything is mapped into the diffusion prior space.
*  And then you systematically hold one out, train a model on the other seven patients from the original data set, get something that's shared across those seven and then see, okay, what if I just use a little bit of data from this eighth person?
*  So I now have rich enough representation, robust enough representation in the shared space that I can quickly map this new person onto that successfully.
*  How would you refine my description?
*  Yeah, that's all right.
*  Okay, cool. How big are those? How long do those take to train?
*  Obviously, this is a unique data set where there are these unusually long time spent in the fMRI for an individual person.
*  So if I instead said, hey, I don't want to do that again, but I went and got 240 or 1000 people to sign release for the one hour that they spent.
*  Would you expect that to work? How do you think this would work with a little bit of a different data set and how much compute, how many kind of parameters give us the specs on that kind of stuff?
*  Yeah, so you're referring to instead of having eight subjects scan for 40 hours, like hundreds of people scan for maybe an hour or something.
*  Yeah, I'm just thinking about what data is just already sitting out there that wouldn't take such a heroic effort.
*  I might take a legal heroic effort to unlock some of that stuff, but there's a ton of people that have spent one hour.
*  Two points on that. One is this is relating to the idea of precision neuroscience, which is the kind of trade off between shorter scanning sessions with a lot of people versus a lot of scanning with a single or just a few people.
*  And there are advantages to both. Obviously the natural scenes data set did the latter.
*  And the advantage you get is higher quality data, the ability to really get subject specific results.
*  And then the former is more so like you can really figure out how one person's brain is different from all the other people's brains.
*  But the overall quality of the data is worsened. So maybe you'll never really get the kind of high quality results that you would get with something like the natural scenes data set.
*  The point about like you have a lot of neuro imaging data sets currently out there that could potentially be tapped into to create like an overarching model space.
*  That is something we are actively working on.
*  So we're currently training a foundation model on fMRI, taking basically all possible data from the entirety of the publicly available data sets that we can get our hands on.
*  And the potential there I think is huge because you're essentially creating a new avenue towards getting the signal that you care about from a brain scan.
*  You're able to get a generalizable latent, convert the raw brain scans into a generalizable latent trained across hundreds of thousands of people's brains.
*  That's been imbued by the heuristics of how brain patterns typically work. So I'm really excited about that.
*  That is a definite potential that hopefully can work out.
*  Yeah, it seems like foundation models are coming to every modality and all modalities all pretty quickly.
*  So I asked Claude three to help me figure out how big the models were on the fMRI to diffusion prior side of this.
*  And it estimated 940 million parameters. I don't know if that was I didn't find that myself in the paper.
*  That was the parameter count from my day one.
*  Okay, so give me a sense of the order of magnitude of parameters and compute for this work.
*  And then I'm really interested to hear also like for your upcoming work, how much data is out there?
*  Like how many hours of fMRI data are you able to tap into? And what are the compute budgets you're going to need to do that sort of work?
*  Yeah, for my day two, the models that we trained were probably larger than they needed to be because if you're going to do everything for a deadline for a conference, just like maximize the compute that you currently have to just train it and get the results.
*  So that was like two billion parameter from my day two models.
*  But since then, I've looked into reducing the parameter count like more than half of that parameter count and still get basically the same quality of results.
*  Also, two billion sounds huge, but actually it's not that big because it's basically coming from a single and dot linear part of the model.
*  So basically over a billion of that is only coming through the residual MLP backbone and MLPs are a lot more computationally efficient than a diffusion model, for instance.
*  So it's actually not that slow, like computationally inefficient, even though the parameter count so big.
*  It's literally just this one linear layer that leads to this over a billion parameter count situation.
*  That is primarily the layer that is mapping the shared space to the diffusion prior.
*  Yeah, it's like in figure two, it's like this shared subject latent space where every person's brain gets compressed to 4096 and then going from 4096 to the clip latency dimensionality, which is 256 times 1664.
*  And that's flattened. So it's half a million, I think. So it's that and then dot linear 4000 to half a million.
*  That leads to the parameter account. Gotcha. That's really helpful.
*  So what happens next? How many orders of magnitude more FMRI data with the foundation model be trained on?
*  And what is the compute budget look like to make something like that happen?
*  Yeah, well, first I'll say the neuroscience community is amazing in the sense that there is a bit of a standard towards releasing your data that you collect as a lab, open source, according to standardized format.
*  Specifically, it's called bids, brain image data set specification, I think.
*  So that's amazing that there's already this push towards standardization and easily accessible data sets that is available publicly is also the huge challenge.
*  And then finally, there's also the human connectome project, which was a massive, large scale neuroimaging data set.
*  There is the UK biobank, which is another one, although you have to pay to get access to that one.
*  But basically, we're talking about millions of hours of people in machines and trying to use a foundation model to compress all of this data into some sort of generalizable purpose latent that can then be fed for downstream applications.
*  So I think that the goal would be better reconstructions, but it doesn't have to be that it could be anything. Right?
*  Yeah. Okay. So we're going from hundreds of hours to millions of hours, which is obviously quite a jump.
*  Yeah, we haven't fully gotten all the data sets out. So I don't know an exact number. Maybe it's less than a million, but it's a lot more data.
*  Everyone is talking about chat GPT right now. But are you actually using it to the max?
*  How do you use chat GPT is an interview show where the people at the forefront of technology show you how they use chat GPT in their work and their lives.
*  Host Dan shipper talks to programmers, writers, founders, academics, tech executives, and others to walk through all of their chat GPT use cases, including historical chats step by step.
*  They even use chat GPT together live on the show to build apps, analyze their leadership qualities, read more deeply and do the best work of their lives.
*  Listen to how do you use chat GPT from Dan shipper and the team at every wherever you get your podcasts.
*  So where do you think this is all going? You may have some interesting views of the future.
*  We're going to do another kind of somewhat companion episode to this, where we look at like all of the brain computer interface technologies that are out there for reading.
*  Increasingly, there's some that are attempting writing or at least steering the brain activity from the outside.
*  And there's like interesting progress across a lot of different hardware modalities and different kind of signals to try to pick up on and so on and so forth.
*  Where is this going in the big picture? Do you have a view of what is going to become possible?
*  Maybe in a medical setting is one question, but also in just a general daily consumer device like daily life view.
*  It seems like you guys are going to have your way with this foundation model.
*  I fully expect that you're going to come up with something that's going to be quite interesting.
*  But then what are we going to do with it? Yeah, ideally everything works out.
*  The foundation model allows us to have such rich latents and then follow up work to do multimodal stuff.
*  So like you could take inferior non-invasive imaging tech and map it to a better quality latent space.
*  And the dream would be that you can take smaller data sets that are higher quality, maybe even invasive data sets.
*  And you can just merge all these different modalities together to be able to make use of that kind of higher quality data.
*  FNRI right now is the best non-invasive tech.
*  But the downside, obviously, is that it's very expensive and it's also very difficult to use.
*  Like just from a patient's perspective, you can't move at all.
*  If you're someone who gets claustrophobic, then you can't get scanned, basically, especially for these kind of like hour long experiments.
*  So that's not ideal, but it is the best that we have in terms of invasive stuff.
*  Like you can get electrodes planted in your brain already.
*  If you're a seizure patient, then people will put electrodes across your brain and try to like deduce, localize where the seizures coming from.
*  And you can get really high quality data if you have invasive electrodes on your brain, like much better than fNRI even.
*  But the downside is that it's not spread out across the entirety of the brain.
*  Neuralink is specifically in the motor cortex, right?
*  So you're not going to be able to make use of the entirety of the brain.
*  Unless you've completely taken out your scalp and put these electrodes over the entirety of your cortex.
*  So you're going to be constrained in terms of localization, but you benefit from the higher quality data.
*  In terms of non-invasive stuff like EEG, you're not really able to localize at all.
*  So you don't get a 3D brain like you do with fNRI.
*  Basically, you put some electrodes in certain positions and then they bounce along the skull and eventually you get some changes in electrical activation.
*  And you deduce things based on that.
*  But you don't really know where the initial neurons that are leading to that change in electrical activation is coming from.
*  This is a localization problem.
*  Now, I think there's a lot of new tech that's coming out that's really promising.
*  So there's ultrasound.
*  There's near infrared proxies to what you would get with fNRI that seem very promising.
*  Currently, the tech is not there yet, but it's clear that it's in the right direction.
*  That something's going to come out in the foreseeable future that allows us to get, hopefully, close to fNRI quality results with non-invasive technology.
*  Or we figure out a way to get a multimodal thing working that can leverage higher quality data with worse inputs.
*  So then what's my life going to be like?
*  Do you have a vision for a Jetsons level future that you envision for the general public with brain reading technology on a daily basis?
*  Or what is your core reason why?
*  Is it medical? Is it daily life?
*  What do you think are the most exciting midterm applications, let's say?
*  Oh, yeah. I don't know about Jetsons.
*  The first step that we're going to is get these complicated machine learning things that are currently only able to be done in an academic setting with a huge data set to work with very limited data.
*  Hopefully do things in real time, be able to do things with very constrained data sets and still get high quality results.
*  And furthermore, be able to generalize this to different kinds of outputs that are more relevant than just perception.
*  So, for instance, we are collaborating with the University of Minnesota to try to do mental imagery reconstruction, visualizing an image and recreate that.
*  You can imagine that there's a lot of different pipelines that would be relevant here, like memory decoding, stuff like that.
*  Furthermore, something that we didn't really talk about was the shared subject space stuff shows the potential for this kind of approach to work where maybe you have some subjects that have a lot of data,
*  but you can tap into this shared space with very minimal data.
*  And that approach by itself is not specific to reconstructing images.
*  So basically, there is a lot of potential here in being able to get the cutting edge machine learning pipelines that are currently only reserved for kind of academic basic science research to more real settings that are actually feasible for clinicians to use,
*  for instance. Beyond that, when it comes to BCI tech, I would love to be involved in that space.
*  Obviously, I don't know what the potential is for consumer applications or things like that.
*  Yeah, I feel like in general, we're all groping. I asked these questions and in general, the answer is nobody really knows where this is going, which I find to be sort of fascinating and also, to be honest, somewhat disconcerting reality.
*  And that's a much broader statement than brain data reading and interpretation.
*  But just what is the sort of positive vision for where all this AI tech is taking us is one that I think everybody would do well to spend a little bit more time thinking about.
*  So the memory thing is really interesting. Are there any sort of surprising lessons from this work that people should know about?
*  I'm thinking, for example, like oftentimes bizarre failures of the model can be an interesting unpack.
*  I wonder if you've seen any examples where you're like, well, it got this wrong, but in a revealing way where we were able to learn something from it.
*  Or I wonder if you have any kind of updated theories of cognition or like how similar or different people's perception are.
*  These sorts of questions have been like age old philosophical questions.
*  Like when you see an apple and it's red, what does that look like to you versus me?
*  Yeah, I'm kind of curious as to if you feel like this work is informing the way you think about what once were sort of limited to philosophy questions, but now are maybe starting to be penetrated a little bit by science.
*  Yeah, kind of related to this. So the data set itself, right?
*  People were actually looking at totally different emissions.
*  So usually how people would approach shared subject modeling is everybody looks at the exact same emissions and then basically the correspondence between I saw this and you saw the same thing, but mine is different than yours.
*  And then you can look at that individual difference and help extract that out.
*  And then you have this sort of shared subject component and the individual component, right?
*  We didn't have that here. I mean, there was a small subset of images that everyone saw, but that was the test set.
*  We didn't have access to that at all for the training of the models.
*  And so it's pretty revealing that the approach that we used is literally it's a lot simpler than it seems.
*  It's just ridge regression. It's linear regression.
*  So you just take no matter what the input was, you take my brain, you take your brain.
*  We looked at different images.
*  You put them in the same batch and then you get your own linear mapping.
*  I get my own linear mapping. At least that just can get the dimensionalities to be the same and account for differences in our voxels, how we represent things.
*  Then everything else after the model is the same for both of us.
*  And the simplicity of this and the fact that it works so well is very interesting.
*  This was the first thing that we tried. It's like, OK, how do we do shared subject modeling?
*  And then the most obvious way, just do a linear mapping to a shared space and then everything else is the same.
*  And then the first try and it works great. And it's like, why is nobody else doing this?
*  Why is everyone doing fancier things of like manifolds and complicated neural networks that are shared between people?
*  Like the very easy solution of just linear mapping for my brain and your brain to the same space works so well.
*  So, I mean, there has to be some shared representations that can support that by one.
*  And you're able to extract that kind of variability in a pretty simple manner.
*  And so just the fact that it works so well tells us something about the similarities in how people's brains represent things.
*  Even though the inputs are different, you can get the same kind of underlying relevant signal out.
*  And the individual specifics of things can be further elaborated by fine tuning the complicated part of the model.
*  In terms of failure cases, there are some obvious failures when it comes to the reconstructions.
*  And that usually happens when the images are more complicated. If you are just looking at a simple image, it has maybe one object in it.
*  Then the reconstructions will typically be quite good. Like if it's a single giraffe, you can recreate the giraffe.
*  It'll look the right way in the image. It'll basically be in the right setting and it'll be great.
*  But if you have a complicated marketplace scene with multiple people and there's complications like that, it doesn't quite do as well.
*  And part of the reason for this is simply the data sets were collected in a way where the images come from Microsoft Cocoa.
*  And the majority of the images that people saw are simple scenes.
*  And so the farther away you get from that distribution of images, the less the model is going to be able to account for that.
*  Yeah, that sort of suggests that somebody like an open A.I. is in a really good position to do a version of this because reading their Dolly 3 technical report or whatever they officially called that, there was like a huge sort of data enrichment process where they were able to get much, much better results on the image generation, like much more control over the image.
*  By first doing super detailed captions of the images that they used for training and kind of getting past the bootstrapping process where these captions that have come off the Web are not meant for this purpose for one thing and just noisy and general as we've talked about.
*  But they were starting to caption these things in really granular ways, like detailed descriptions.
*  And then that allowed them to create that same corresponding level of control on the other side.
*  This sort of shows the way to potentially even way more powerful and high fidelity versions of this.
*  If you simply just had like better data, better foundation models.
*  One way that I'm thinking about that is like how much of the compute in this project was incremental to the original foundation model effort.
*  And if that ratio is really small, then that would suggest that these sort of mega projects potentially become even more valuable than we may be naively thinking, right?
*  Because then if it's just a little extra compute to do to unlock all these other use cases on top of these foundation models, then the best foundation model wins maybe.
*  So do you have a number? I again asked Cloud3 to analyze this and it guessed that the incremental compute was somewhere between 0.1% and even less than that.
*  At the high end of its range, it guessed that it was essentially one one thousandth additional compute relative to the stable diffusion Excel foundation model training.
*  For instance, we train the full thing of the pre-training and then the fine tuning.
*  It's like less than a day on one H100 node for the pre-training and then also less than one day for each fine tuning.
*  And then for the stable diffusion Excel unclip, we trained it for less than one epic, like fine tuned from the base SD Excel.
*  So, yeah, it's along that kind of scale in terms of GPU hours.
*  The foundation model is quite important.
*  It makes a big difference in terms of the starting point for which you can add all these other things.
*  And also the applications that you get out of it are potentially bigger than you would initially think.
*  For instance, back when we were trying to get the unclip to work, Tanish reached out to Robin, the head of stable diffusion team.
*  And Robin was like, yeah, if you want to get exactly the original image back from the clip image embedding, just use the open clip unpooled embeddings.
*  And yeah, you'll get it perfectly. Like, here's the kind of results that you can get.
*  And we were like, what? Why can't you release this? This is amazing.
*  There's a lot of applications for that, but I don't think that Robin understood the potential of having that.
*  So he was basically like, I don't see the potential in it.
*  So then we went and basically followed up and actually fully fine tune and got the thing working and everything.
*  But yeah, there's probably more of a scope than people initially think that is possible from foundation models.
*  I don't think that when people train clip, they would think that people would add a brain modality to clip.
*  Yeah, this is again, another kind of theme across a bunch of different topic areas that we've explored.
*  But the idea that a foundation model has like often with GPT-4 even just in prompting it better, we've gone like a year and change now and people still continue to come out with better ways just to prompt it to get better and better performance.
*  And then here with the foundation models being open source, you're able to come up with all these interesting, clever ways to map spaces to spaces and connect spaces to spaces that were never really intended and really don't actually end up requiring that.
*  All that much compute. I wonder if you have other areas in mind where you think that might work.
*  I was kind of trying to map this process onto something for like protein discovery or novel protein generation.
*  And it seemed like a lot of the parts kind of line up with obviously with different models and different data sets.
*  But this approach seems like something that I would expect to see a lot more of.
*  Do you have other things in mind that you think people should start to bring this like predict the diffusion prior approach to?
*  Yeah, I don't know about like specifically predict the diffusion prior approach.
*  I think there might be better ways to do these kind of things.
*  And the ability that we had to tap into the clip image space and image generation models was possible because our goal was to output an image.
*  When you're outputting like proteins or other kinds of things, it's probably a bit more difficult to get the alignment of using foundation models and we're trained for other purposes, although it's probably still possible.
*  And at that point, it's like the potential of foundation models is so apparent for other use cases that training medical foundation models is going to be very important.
*  That's why we're trying to do the FMRI foundation model, for instance, because it would unlock so many new applications even outside of FMRI, like with multimodal possibilities.
*  So how big of a project is this next one?
*  We covered the amount of data, is orders of magnitude more?
*  Presumably the compute would be orders of magnitude more. Orders of magnitude more than one day on one H100 still isn't necessarily that big.
*  Is this foundation model project something that is kind of moderate scale compute that you guys are getting interested to hear how because Tanishk is the founder of MedArc and you guys are both on the paper affiliated with MedArc and with stability.
*  So we're interested to hear a little bit about how that relationship works.
*  People are very curious for many reasons right now about how stability works.
*  But I'm curious, like, first of all, the nature of that relationship, but also is this next thing going to be the scale of compute that can easily come out of a stability budget or is it going to be big to the point where it becomes like either something that creates scarcity at stability or requires other resources to be brought to bear?
*  Just how big is it?
*  Yeah, first off, Tanishk, head of MedArc, he's been instrumental in helping to organize various projects, even outside of these neuroimaging projects where I'm the lead of the team for neuro AI.
*  And Ahmad was kind of like the instrumental person in supporting many different open source ecosystems.
*  He was very generous to basically allow us to use the compute that stability had for external teams and for open source projects in medical domain that I believe these projects do have profitability, but it's more of a longer term profitability to be aware of.
*  So it is a very generous use case of stability, employing me and Tanishk.
*  We're not getting paid through MedArc and stability giving access to compute, not just to the employees, but to the open lab team that we cultivate across both academic institutions and an open source, an open science discord community.
*  And I believe that's a very unique situation.
*  I'm not really aware of other places that have cultivated that kind of environment.
*  And it's also very crucial to being able to publish quickly and have a diversity of opinions and background to keep aware of the literature and what papers might be relevant to get ideas from.
*  So that's been great. And also, interestingly, you would think that that would be kind of prohibitively expensive of like onboarding multiple people that are not employees into a cluster and using all of this.
*  But honestly, so far, throughout everything, we've been able to get away with only using a few nodes across the whole team, which involves more projects than even the ones that we've talked about right now.
*  Basically, we're able to make use of large teams of people across multiple projects without that much compute, at least in relation to the amount of compute that like the stable diffusion team would use.
*  So that's been great.
*  But we haven't yet gotten to the scaling up period of the foundation model, for instance.
*  So I don't really know what kind of scale of compute we'd actually need and whether or not we would have access to that kind of compute as an external team like this is the sort of reality of things.
*  Hopefully, we're able to show more promising results and petition for more resources.
*  But yeah, so far, things have been good with little compute, honestly speaking, which is interesting.
*  And hopefully, we can petition to continue to grow the project out.
*  Yeah, the embodied compute, I sometimes think of it as that these models, you know, make kind of portable to other projects is again, and just another fascinating thing to ponder in the context of your work.
*  So this is a super interesting line of research, and it's going to be very interesting to see just how far the foundation models can go.
*  One of my theories right now is that I don't know how fast superhuman capabilities are coming in language models.
*  But I'm pretty sure they're coming quite quickly when it comes to all of these other things that are like non human modalities.
*  I mean, we have just no evolutionary basis for like interpreting the voxel level activity of the brain.
*  We have no evolutionary basis for reading DNA sequences that are super long and making connections across great distances in the genome and beginning to predict how those things are going to interact as they work up the layers of activity in a cell.
*  And so the foundation models in these areas are headed for superhuman status, like basically on the first go.
*  And then the question is going to be just how powerful are they?
*  But it seems like they're going to be quite powerful.
*  We're already decoding the brain on small data to think what might be possible with several orders of magnitude scale up on top of that is really quite remarkable.
*  Do you have any thoughts?
*  This is obviously a very complicated question, and there's like a both pros and cons to it.
*  But how do you think about open sourcing things that are so different than anything that's been out there in the past and that clearly have this ability for people to come along and add on a little bit to it and unlock something that you didn't even expect?
*  There's a lot of people who are super pro open sourcing and just say it's the only way.
*  And then there's a lot of people that are afraid of what somebody might do if you train something at 10 to the 20 whatever flops and then put it out there and people can do something with one one thousandth of that incremental.
*  How do you think about that?
*  Do you guys have like a framework for if you do train this next foundation model successfully?
*  Is there even a way to structure thinking on whether and how to create broader access to that?
*  The point of the foundation is to make it broadly accessible to allow new research to expand from it.
*  So the point of kind of sharing how this works is to improve science as a whole, right?
*  To allow this kind of progress to be made to make an actual difference, allow for novel clinical diagnosis approaches, allow for novel basic science advances that would be possible from a massive training of model.
*  Usually people are not going to have access to the kind of compute that might be necessary to train a foundation model.
*  But after it's trained, if you just use it for inference, yeah, you can get that to work probably.
*  And you can just map into that latent space and make use of that however you want.
*  You can fine tune it or do all sorts of things with it.
*  So I'm very pro in terms of making sure that it's broadly accessible and the open science component of getting people to collaborate with you to kind of expand the frontier of what's possible with these data sets.
*  There's just so many amazingly talented people that are not affiliated with an academic institution or have a PhD or are like actively working at Big Tech that there's just so much interest in the field.
*  And there's so many people who want to get involved and who are very talented that it's just such an untapped avenue in my opinion for creating fast paced, high impact work as a team.
*  Yeah, and open sourcing everything is great.
*  Like all the data that we're using is already public.
*  So it's not like there's a privacy thing.
*  People consent to share their data.
*  So I don't think that's an issue.
*  Like sharing how things were trained I think is really great.
*  If there are profitable avenues for applying downstream applications from foundation models, I think that that is very ripe.
*  And there would be a lot of interest after it's shown to be effective as basically the new way to process first fMRI, but then hopefully additional modalities after that.
*  Yeah, from what we've seen so far, all this activity has broadly been like very positive.
*  And I'd be pretty confident saying there's like a 10 to 1, maybe even 100 to 1 ratio of tapping into this talent that otherwise wouldn't have access and creating all these new things.
*  And the creativity and the fact that people will build things that you didn't think to build on top of the foundation, as you said, is the point.
*  And then I'm also like, man, some of this stuff is so wild in terms of what it might enable that I do wonder if we might one day wish that we had a more structured approach in the A.I. safety.
*  You may be aware of this kind of terminology, but in some corners of the A.I. safety world, there is the notion of structured access, which is like trying to find this middle space between open source services.
*  And you're processing everything in a way where you can't take it back if you ever wanted to, but still like trying to create the kind of access that people need to be able to do the good work that you want to enable.
*  Any, I wonder if you have any thoughts on a structured access approach to this kind of foundation model?
*  Yeah, to an extent, it depends on how well things work. If it's clear that it's working orders of magnitude better than anyone expects, then maybe there are reasons to be more diligent about how like what exactly you're sharing.
*  But for fMRI, there are so many limitations that I'm pretty confident there's not going to be like a huge problem with sharing these kind of foundation models.
*  As things get more invasive and the quality of data gets better and better, then there are going to be privacy concerns and then you need to be very careful about what is being released and who has access to it and like what companies are like maybe going to benefit from it.
*  You need to be very careful and make sure that people's brain data is not being taken advantage of.
*  Yeah, it doesn't seem like there's a major barrier to like there's a lot of little barriers, not to say it's not going to be a lot of work, but it seems like detection type of technology would pretty predictably get to the point over the next couple to few years where you could imagine the state like just putting a headset on people and being like, you're going to answer these questions and we're going to know if you're telling the truth or not.
*  And I would be a little concerned about that future.
*  It's like on the one hand, you can imagine a very positive version of that too, where people might voluntarily wear these things and demonstrate to others that they are being honest because look, my brain readout shows that I'm being honest and maybe that creates a high trust future that is really beautiful in a lot of ways.
*  But it's just always so striking how dual purpose a lot of these things are and especially when they are still noisy and it's we've seen these issues even with just face recognition sometimes where police like show up at somebody's door based on nothing but a face match.
*  It turns out it was a false match and now they're kicking somebody's door down who literally had nothing to do with whatever was the issue.
*  So it's very, I find, fraught. I personally am just like super excited about it and at the same time, yikes, what might happen here as this stuff gets really good. So at a minimum, it's good to hear that you are thinking very actively.
*  Actively, it's clear there's no way that, for instance, lie detection or applications by law enforcement would be relevant to the f m or I domain. The quality of the data is not good enough to do these kind of things.
*  You cannot access things that the person is not directly thinking about. If you move around more than a millimeter, the data gets distorted.
*  Like you're not going to be able to get the kind of signal to noise that would be at all relevant for practical applications that you're talking about, but it can get good enough for very important medical purposes of like comparing clinical groups, identifying biomarkers, trying to assess like mental imagery stuff.
*  You have to be concentrating on the task and be very still in a scanner to get any of these f m or I approaches to work. And I don't want to err on the side of being too careful in this current stage of knowing what the quality of the data looks like, because I know that we want to make advancements first that are going to practically make a difference in terms of helping people with their disorders, understanding basic science of how the brain works.
*  It would be much later on that there's the potential for the kind of technology you're talking about. There have to be some big innovation that happens where the quality of the data gets so good. You're able to access it even with the person not really wanting it to be like access.
*  This is much farther down the line. At which point, if that technology does become accessible, that would open new questions. Yeah. But at this stage, I don't think it's as important to really focus on the data.
*  I think it's important to really focus on like all the nuances around it. And I'm not even sure my concrete stances on everything. I'd have to think more about it.
*  Yeah, I think it's an important commentary. It seems like we're maybe at sort of a GPT one or GPT two phase of this line of research where it's like just entering into the zone where it can start to become useful, but it still takes a lot of effort to actually get real value from it.
*  And there are probably like at least a couple generations to go before it gets to the point where it's just really easy to use and broadly applicable. I often say about GPT four that we're in a sweet spot right now where it's on the one hand super useful and on the other hand, like not so powerful as to be like serious risk of becoming a destabilizing force in the world.
*  And I think maybe we have another generation to go before that happens. At some point, it does seem clear we're headed for something that's like quite powerful and potentially destabilizingly so. But it is good to calibrate on all these different lines of research.
*  Like, are we just entering that sweet spot? Are we getting like to the late stage of that sweet spot? So to say that we have a couple of years at least to really allow the research to mature and continue to figure out like what the plan is as it gets into that sweet spot of like easy broad use across a lot of use cases is a lot of work.
*  So I think that's a really good frame for us to all keep in mind. This has been an awesome conversation. I appreciate the technical depth and the philosophical engagement as well. Is there anything that we haven't covered that you want to make sure we touch on a little bit?
*  Sure, I want to give a shout out to the other people responsible for the work, right? So this clearly to me, she was the senior author on the paper, both for my night one and my night to hear Tripathi Caesar Tariqa Reese Neal and Ken Norman.
*  All very instrumental is even more co authors. There's like a dozen people involved, and you know who you are. But yeah, it's a very widespread effort. We're still working, for instance, with Princeton to collect new data. We're trying to have more collaborations with academic institutions and the broader open science community.
*  And in that sense, we are open for people to help out. If you think you can help us with these projects, we have several projects going on right now on the Med Arc Discord. So if you just go to MedArc.ai, you can find the Discord link. Join our server. We have weekly meetings for different projects. We just meet on Zoom once a week and work with public Git hubs for most of these projects. So it's an opportunity to work on some cutting edge research together and.
*  Yeah, I encourage anyone who's interested to look into it.
*  Cool. So that's MedArc.ai is the website. Definitely at a minimum, everybody's going to want to check out some of these figures and see just how high fidelity the reconstructions are of what the mind's eye is seeing. And I'll definitely join the Discord and lurk a little bit at least. I'm sure you'll get a couple other new entrants to the conversation as well.
*  For now, again, fantastic conversation. Thank you for sharing all this research and perspective with us. Paul Scotty, thank you for being part of the cognitive revolution.
*  Thank you so much.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the show. So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me on the social media platform of your choice.
*  Thank you.
