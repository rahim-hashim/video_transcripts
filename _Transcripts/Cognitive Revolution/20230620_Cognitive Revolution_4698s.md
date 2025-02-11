---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 4698s
Video Keywords: []
Video Views: 1001
Video Rating: None
---

# The Mind-Reading Revolution with Dr. Tanishq Mathew Abraham (Part 1 of 2)
**Cognitive Revolution "How AI Changes Everything":** [June 20, 2023](https://www.youtube.com/watch?v=JY7K-hoyqns)
*  I think this idea of mapping one latent space to another is a very powerful idea.
*  I think it's always best to try to take advantage of that as much as possible.
*  And the real, I guess, innovation these days is to be able to use these multimodal spaces as well.
*  And being able to map, you know, different things to these multimodal spaces.
*  That's kind of a really exciting area.
*  Hello, and welcome to The Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas, and together, we'll build a picture of how AI
*  technology will transform work, life, and society in the coming years.
*  I'm Nathan LeBenz, joined by my co-host, Eric Torenberg.
*  Hello, and welcome back to The Cognitive Revolution.
*  Our guest today, and also for our next episode, is Tanishq Matthew Abraham.
*  Tanishq is a remarkable talent.
*  He started college at seven years old, gave his first TED Talk shortly thereafter,
*  and has recently completed his PhD, just as he turned 20 years old.
*  He is also the CEO of MedArc, an organization he founded with the goal of translating AI progress
*  to real-world medical applications.
*  If you listen to this show, you know that much of the incredible AI progress we've recently seen
*  has been unlocked by a strikingly consistent recipe.
*  A clever, easy-to-score objective called a loss function allows the transformer architecture
*  to be scaled up and trained with unsupervised, often web-scale, data.
*  This approach has repeatedly advanced the state of the art in text generation,
*  image understanding, image generation, and so much more.
*  Against this backdrop, Tanishq has recently published two remarkable papers with two different
*  sets of co-authors, which show that there is still plenty of opportunity to produce breakthrough
*  results, even with relatively small datasets and modest compute budgets, by using more thoughtfully
*  designed, problem-specific architectures.
*  The first, called Reconstructing the Mind's Eye, which we'll cover in today's episode,
*  shows that AI can quite literally read minds.
*  Leveraging pre-trained clip and stable diffusion models, Tanishq and his collaborators are able to
*  take fMRI scan data collected while a person viewed a particular image and reconstruct that same image
*  with remarkably high fidelity.
*  Our conversation doesn't depend on visual aids, but to properly appreciate this result,
*  you absolutely must look at the headline graphic of this paper.
*  Follow the link in the show notes, and I promise you will be impressed.
*  For me, this conversation was not only a chance to learn about some of the latest techniques
*  that leverage the power of pre-trained foundation models in small data environments,
*  but also a chance to reflect on the big picture.
*  This result, like so many others we've seen recently, would have felt like science fiction
*  just a couple of years ago.
*  Now, with the pace of AI progress so relentless, they often seem to come and go with minimal fanfare.
*  And just as important, I think Tanishq's work demonstrates the potential
*  for AI to help advance neuroscience in general.
*  Decoding the brain's activity in a non-invasive way holds the promise of helping us understand our
*  own human cognition like never before, potentially bringing an entirely new meaning to the phrase,
*  cognitive revolution.
*  As always, if you're finding value in the show, I would really appreciate it if you'd take a moment
*  to share it with your friends.
*  We recently hit a new high as the number 15 rated show on Apple's Technology Podcast Chart.
*  And while I'll always prioritize depth over reach, it is extremely gratifying to know that
*  this project is helping others make sense of the rapidly evolving AI landscape.
*  So now, without further ado, I hope you enjoyed this conversation with Tanishq, Matthew Abraham.
*  Tanishq, Matthew Abraham, welcome to the cognitive revolution.
*  Thank you for having me.
*  Very excited to have you.
*  You are prolific all of a sudden, if not always.
*  For folks who don't know you, you are a child prodigy, I think fair to say, who's now
*  grown into a young adult AI researcher who is hitting on the level of,
*  from what I can tell, a tenure professor.
*  So extremely impressive young career that you have.
*  And a couple of papers that have come out in just the last week or so,
*  both of which are super interesting and for a whole bunch of reasons.
*  One about reading the state of the brain and translating what is detected in the brain
*  into a reconstruction of what the person saw, which is pretty amazing.
*  And there's some incredibly striking visuals there.
*  And then one also that is about taking raw images of tissues and predicting what those
*  would look like if they were treated in various ways to then allow a lab technician to read
*  what information they contain and make diagnoses.
*  So super fascinating stuff, really where the rubber hits the road kind of research.
*  This is not pie in the sky at all, but very sort of applied, practical, hands-on stuff.
*  And I think it's just fantastic.
*  So great work for starters.
*  And I'm looking forward to getting into all the details.
*  Yeah, sounds great.
*  So let's talk about the first paper first.
*  This is the one that has, I think, blown up a little bit more on social media.
*  It's called Reconstructing the Mind's Eye, fMRI to image with contrastive learning and
*  diffusion priors.
*  Maybe just for starters, I was surprised to learn, if I understand correctly, there is a
*  fMRI dataset that was already out there in the public for you to build on.
*  So maybe just start off by kind of telling us what you began with as you undertook this project.
*  It seems like I think the field of neuroscience also tends to have somewhat of a kind of open
*  approach to research in terms of releasing datasets.
*  And there are these sorts of databases with neuroscience datasets like EEG datasets,
*  fMRI datasets.
*  So luckily, there has been some of these datasets have been released where they take a subject,
*  ask them to look at some images and they measure the fMRI signal at the same time.
*  And so this was, so there have been a few datasets over the years that have done some
*  sorts of things.
*  The dataset that we used was released, I think maybe it was 2020, 2021, so pretty recently,
*  I think.
*  So it's a pretty recent dataset.
*  It's a very high resolution dataset.
*  So it uses a, so most of the datasets are using like, I think, magnet that is used for the
*  MRI.
*  It's I think like 1.5 Tesla, 3 Tesla, something around this range.
*  Whereas the one that this one is using is 7 Tesla.
*  So it's a much more powerful magnet.
*  So it actually results in a much more powerful and higher resolution fMRI signal.
*  And so you have a better signal that you can also measure as well.
*  So this was created by another team that conducted that research.
*  And they measured the signal for many different subjects, I think about eight subjects in total.
*  And the subjects went through hours of looking at images.
*  Maybe they look at each image for a few seconds and then the signal would be measured.
*  And then there'd be a break of another few seconds and then they measure again for another image.
*  So they have that sort of process.
*  And then, yeah, they collected all that data and they released it publicly.
*  And so, yeah, actually, I wasn't originally aware of this dataset.
*  It was only after meeting my collaborator here, who's the first author of the paper, who told me about this dataset.
*  Actually, we had started working on some similar ideas for this project about a year ago or so.
*  And we were actually looking at a different dataset at the time.
*  We were really happy to see this dataset, this new dataset, that is much higher resolution and much better signal quality.
*  And, yeah, it was really designed for these sorts of these sorts to research these sorts of questions.
*  So, yeah, it's really a great dataset.
*  And it's great to see that the neuroscience community also has a sort of open research spirit.
*  So I'm really happy about that.
*  And it just kind of makes me more excited to work in that field as well.
*  Yeah, well, the interaction between AI and many, if not all, aspects of biology is certainly going to be fascinating.
*  And this is one that people are just so struck by because you can look ultimately at this is what we showed the person.
*  And this is what we were able to reconstruct based on a reading of their brain.
*  And that first figure in this paper is incredibly striking where it's just like, wow, that is not a similar.
*  I mean, it is a similar image, but that's not just a somewhat similar image.
*  That is a very similar image that really looks like what you showed the person.
*  So we can put a link and we will put a link into the show notes to the paper.
*  But go check out that first visual pause right here and go look at it because it really does ground what we're talking about.
*  The striking resemblance of the reconstructions is just incredible.
*  The reason why it's doing so well is both because of a combination of this very high quality dataset,
*  as well as the latest AI advances that we're taking advantage of.
*  And I think these two, because of these two factors, that's why we're able to see such great results.
*  And so this isn't something that was possible before, but only because of these two factors now we're able to see such amazing results.
*  Cool. So let's talk just a little bit more about the fMRI side and kind of the nature of that dataset.
*  So reading through the paper, there's 15,000 voxels.
*  A voxel, as I understand, is a 3D space in and of itself.
*  So basically 15,000 little cubes, if you will, each corresponding to a physical region in the brain.
*  Is this all kind of like on the back of the head and the visual cortex?
*  Like how much of the brain is sort of under consideration here?
*  Yeah, that's approximately right.
*  The dataset actually has the fMRI signal of the entire brain, but we used a subset of the voxels that correspond to visual perception.
*  So yeah, and this was actually something that the original dataset folks actually prepared.
*  They actually prepared a subset of their data focused on visual perception.
*  And so that is the subset that we used in this study.
*  If we were to look at the sort of raw data of one voxel, what would that contain?
*  I think it's just be kind of a value associated with that particular voxel for that particular signal.
*  So the fMRI signal is actually measuring kind of, it's dependent on the blood oxygenation level.
*  So basically, as a particular region in the brain is using, there's a lot of activity,
*  it's going to be using up a lot of blood oxygen.
*  So you kind of see that sort of change in blood oxygenation level.
*  And so you have a value that's associated with that particular voxel that is indicative of the sort of blood oxygenation
*  and the usage of blood oxygen in that area of the brain.
*  Gotcha. Okay. So it's essentially activity or energy.
*  You know, it's just, it's a raw kind of scalar that says this is how intense activity was in this particular place.
*  Is there a time dimension to it as well, or are you kind of just staring as the user at an image,
*  until there's some sort of steady state or whatever that is then kind of average?
*  How does that work?
*  Yeah, kind of like that. There isn't much of a time dimension.
*  fMRI doesn't have as much high temporal resolution, especially because you do have this sort of blood oxygenation
*  and that process is a little bit slower.
*  And so it's much harder to get very kind of high accuracy in terms of the time resolution.
*  So it's more of kind of a single kind of steady state kind of value.
*  So that's why you have the patient looking at it for a few seconds first,
*  and then you take that measurement for over a course of a few seconds.
*  And then, yeah, that's kind of the measurement that you're using.
*  Yeah. So essentially, the input is, you know, when we think about an AI model that you're now going to develop on this data set,
*  as kind of an input-output device, you know, I always kind of fall back to that framework.
*  The input then is 15,000 numbers that correspond to intensity of activity in each, you know,
*  one of 15,000 little regions of the brain that are all kind of in that back visual cortex area.
*  That's strikingly not that much information.
*  You know, 15,000 numbers in the grand scheme of things feel small.
*  Does that feel small to you?
*  Yeah, it definitely is kind of striking in terms of how much information is present in the fMRI.
*  And again, like this isn't looking at individual neurons or anything like this.
*  This is kind of a region.
*  It's about one to two, like, I guess, two, maybe two millimeters, two by two by two millimeter cube kind of like basically,
*  like, yeah, it's a two by two by two millimeters kind of cube of area or volume that you're looking at for that particular voxel.
*  So it's not like a very, you know, it's not even that fine grained.
*  It's more fine grained than maybe some of the other technologies like EEG or some of these other technologies.
*  But like it's not like a lot of these sorts of systems where you have these sorts of invasive,
*  you know, measurements of specific neurons or things like this.
*  It's not looking at specific neurons.
*  So, you know, it's kind of interesting that, you know, you would expect you would need the actual neuron signal,
*  the actual electrical activity and, you know, at that very fine grade level to be able to get the, you know,
*  to be able to get that response, to be able to accurately predict the reconstruction.
*  But it turns out that's not absolutely necessary.
*  And I think a lot of it has to do with just the way the brain is organized.
*  And, you know, certain, you know, there are certain regions that respond to certain features in an image, for example.
*  So just being able to know, like, what regions are being activated and responding to the image,
*  that kind of gives you an overall idea of maybe the sorts of features that are there in an image already.
*  So I think, yeah, a lot of it has to do with kind of the organization of the brain and the visual perception of the brain.
*  And, yeah, that's also kind of partly why these sorts of approaches are interesting from my research perspective,
*  is to also better understand how that perception works as well.
*  And, you know, yeah, what's being activated, what's, yeah, what kind of signals are there.
*  So, yeah, overall, yeah, it sometimes can be, when you think about it, it's a little bit surprising.
*  I mean, I think it's just surprising overall that you can, you know, do this sort of reading of brain activity in the first place,
*  you know, whether or not it's with fMRI or any other thing, that's like, that's still kind of pretty impressive.
*  And doing it in a non-invasive manner, it's like, that's pretty surprising.
*  But, yeah, of course, you know, you still are getting very high, you still have to get that very high quality data.
*  And, you know, you have subjects that are, you know, in this MRI machine sitting there for an extended period of time.
*  And so it's still a very, you know, kind of involved process anyway.
*  But, you know, it's a great kind of first step and still useful for, hopefully, research applications.
*  Yeah.
*  I mean, the learning is going to go both ways here for sure.
*  I think that's another super key point and probably key theme is like the feedback cycles and dynamics here research wise.
*  You know, we're just scratching the surface of that.
*  Again, just grounding for a second.
*  So you said kind of two millimeter cube is one voxel.
*  So if I were to do a little, you know, mental math on that, I'm like, okay, five by five by five is 125.
*  So there's, there would be in a cubic centimeter, there would be 125 of these voxels.
*  And we're on our way to 15,000.
*  So that would be basically 100 cubic centimeters.
*  So if I'm thinking about that as like the cortex, it's maybe like a 10 by 10 by one deep kind of segment of tissue is what we're really looking at here.
*  Yeah, I think that sounds about right.
*  We've got that kind of slab of tissue.
*  We've divided it up into these two millimeter cube voxels.
*  Each one has a number that corresponds to its intensity.
*  That is again where we started.
*  And so that's the input now to the things that you are training AIs to do.
*  I guess there's a couple of big themes here that jump back to me.
*  One, the just the volume of data, not that high, right?
*  You've got only so many images, only a few patients.
*  And this is true of your other paper as well, right?
*  It's a low data environment and that creates some interesting challenges.
*  Tell me about the outputs.
*  You have multiple different approaches to create different outputs that you use for different purposes.
*  So maybe just run those down for us.
*  The final goal was to, of course, we construct the image.
*  We want a final image there.
*  The approach that we wanted to take was kind of how can we leverage sort of the existing
*  image generation models and image representation models that exist already to be able to
*  perform this reconstruction as well as this additional task that we talk about, which is retrieval.
*  And so in order to do that, the goal is to basically get some sort of clip embedding.
*  So this is again like sort of clip models that OpenAI has developed and released
*  where it's kind of a sort of joint representation of an image and text.
*  And so it's in this sort of, you have this sort of representation space.
*  And the idea is that lots of, a lot of these image generation models already taken some sort of
*  clip embedding.
*  So if we're able to predict the clip embedding from the fMRI signal, then we can use that clip
*  embedding for image generation and get a reconstruction that way.
*  So that's kind of at a high level of the approach.
*  There are a few different other aspects that allow this to work.
*  So the idea is that, okay, we have a sort of neural network, a basic MLP, multi-layer
*  perceptron.
*  That's like a basic neural network architecture.
*  And so we take this MLP to predict the embedding.
*  And the problem is that the embedding that we get at the beginning isn't aligned.
*  So it isn't, so basically when you have these embeddings, like you can get them so that the
*  sort of, I guess, some cosine similarities, the similarities between the embeddings kind of all
*  match up the way you want them to, but the actual representations aren't kind of aligned with the
*  other representations.
*  It's not just a problem with, you know, in this case, fMRI embeddings that we're working with,
*  but it's actually an issue that happens with even just within the regular clip where you have
*  image to text, image and text embeddings.
*  So for example, in the OpenAI Dali work that they have, they wanted to take text and then they
*  wanted to convert that, of course, to a nice image generation.
*  So the problem is that they did something similar where they actually took text and then they got
*  the clip embedding for the text.
*  And, you know, they just get that because that's how the clip model is already trained.
*  But then that clip text embedding isn't aligned again to the image embedding.
*  So, of course, the clip text embedding, you know, for example, if it's, let's say it's a picture of
*  a dog and that's the text, and then if it's the actual image of the dog, those embeddings have high
*  similarity to each other, the text embedding and the image embedding, but they're not of similar
*  values.
*  So that's the issue.
*  They're not really of similar values.
*  They're not really matching.
*  So you cannot take, like, for example, a clip text embedding and pass it in as a clip image
*  embedding to an image generation model that expects clip image embeddings.
*  You need to somehow convert from the clip text embedding to a clip image embedding.
*  So the Dali paper introduced this diffusion prior, which is another model that converts
*  the clip text embedding into a clip image embedding and aligns them.
*  And so that's what we did here, where we predicted our clip embedding from the fMRI signal.
*  And then we also had a diffusion prior that would take that predicted fMRI embedding and align it
*  with the clip image embedding.
*  And now we have a clip image embedding that's aligned, and that can be passed into a pre-trained
*  image generation model.
*  So that's the reconstruction pipeline.
*  And then we also have this retrieval pipeline, where in this case, you don't really need to have
*  the alignment because here all you're looking at is similarity.
*  So you can just say, OK, if you have some sort of fMRI embedding, what images are those similar
*  to based on, again, on cosine similarity of the clip embedding.
*  So you can get the similarity to a bunch of images, and you can say these are the ones that
*  are most similar to.
*  And we also did those experiments as well.
*  And we can see that if we used images from the data set that we worked with, then the ones that
*  are most similar to are the actual images that the subject actually saw in that case.
*  Or we can also extend it to a very large data set like Lion5b.
*  And you can do, again, some sort of similarity and get similar images.
*  And those similar images would look very similar to the actual image.
*  And you can kind of treat this as a generation pipeline without actually using a generation model
*  because you're getting these sorts of similar images that correspond very, very closely to the
*  original image.
*  And again, the nice thing about what we show in this paper is that you can get actually very
*  fine-grained information.
*  So if you had the example that we have in our paper, which we think is a really nice example,
*  is that there are actually a lot of zebra images in the data set that they were working with
*  to collect from some of the subjects.
*  And so if we have one zebra image that a subject looked at, and you try to predict the fMRI signal,
*  and you look at the retrieval of the images, you can actually retrieve the exact same
*  zebra image based on the fMRI embedding that we predict with our model.
*  And so this indicates that it's not just, oh, this is a zebra image.
*  You can get this is the exact zebra image that the patient was looking at.
*  So it's actually that fine-grained level of information that's also present.
*  So that's kind of the two sort of approaches that we have here.
*  We have the sort of reconstruction.
*  We have this retrieval.
*  There's one other aspect that is also worth pointing out, is that because with reconstruction,
*  you have this clip embedding, and that's being passed into this image generation model.
*  You get some nice image.
*  But it would be also nice if the sort of positions of the objects are similar,
*  or maybe the color is similar, these sorts of more low-level information.
*  So we also have a low-level pipeline that also kind of helps predict,
*  that can help with that low-level information.
*  And so the idea there is you actually just have a simple model that takes in the fMRI data and
*  predicts a signal in like a VAE representation.
*  So like with stable diffusion, it has this sort of VAE, which is a variational autoencoder.
*  So this is just kind of a lower dimensional representation of the image.
*  And so if we can predict that, and then we actually just
*  then decode that VAE representation that was predicted from the fMRI signal.
*  And that's kind of a very blurry image, but it has sort of some of the features that are important,
*  like some of the position of the objects or the colors, things like this.
*  And we can use that as a starting point for our diffusion process.
*  So because our standard pre-trained image generation is usually some sort of diffusion process,
*  we can use some of these sort of like image-to-image processes that people have been using
*  and use this low-level image as a starting point for the high-level image generation to occur.
*  And so that way you can get the high-level image generation with the low-level information.
*  So that's kind of this combination of this sort of low-level pipeline and this high-level pipeline.
*  And this allows us to get very high metrics also on the low-level metrics.
*  So people will do things like look at the, yeah, just kind of again, the comparison of the original image
*  and the output image.
*  And of course, if you have very similar semantic information in terms of like,
*  okay, this is a zebra, but the zebra is not in the same position.
*  If you're going to directly compare those images, it's not going to be very high.
*  The results won't be very good in terms of that sort of low-level comparison.
*  But here we can show that our low-level comparison actually is much better than previous approaches as well.
*  So yeah, that's a lot of information, I guess.
*  But those are the different pipelines.
*  And yeah, of course, feel free to ask questions about the specific pipelines and the specific details.
*  But yeah, hopefully that makes sense.
*  So am I right, first of all, to say that kind of the simplest first step
*  is taking a 15,000 voxels, each a number, and mapping that to a clip embedding.
*  And that's kind of the starting point, regardless of then whether you're going to go to the retrieval
*  or to the reconstruction.
*  Yes, that's correct.
*  Yes.
*  So I guess first of all, how big is that?
*  How big is a clip embedding?
*  Like how many numbers is that at the end of the prediction?
*  It depends.
*  I guess because we did try different clip models.
*  I don't remember which one we used finally.
*  But basically you have a sort of a vector for each.
*  In the case of text, it would be each kind of word or token, for example.
*  And then those would be concatenated together.
*  Or in the case of an image, for example, if you're using the sort of transformer,
*  you have like image tokens as well.
*  So you have this sort of array of vectors that you have for each image or each sentence or whatever.
*  And then typically what people will do is they like, for example,
*  like average across that and just get a single vector that they work with.
*  We don't actually do that because it turns out if you actually do average across all the
*  tokens, all the words in the sentence or the entire image or whatever,
*  you actually lose information that way.
*  And if you actually keep that information and try to predict, basically we're predicting
*  the clip embedding for the whole image and not just that kind of global representation,
*  but actually the different parts of the image as well.
*  Again, that allows you to get some more spatial information, some more kind of low-level,
*  accurate information that way too.
*  But it's basically some sort of a vector for each of these tokens.
*  And then you have that.
*  Overall, I can quickly look up the dimension.
*  It's probably mentioned in the diagram.
*  Yes.
*  257 by 768 if I'm reading the diagram.
*  Yeah. So to clarify what that means, basically you have for each token, you have a 768 vector.
*  So for example, if you had a clip...
*  So yeah, again, clip image embeddings are a little bit different because basically the image is
*  divided into multiple patches.
*  And then for each patch is treated as a sort of token.
*  So then you have a 768 vector for each patch in the image.
*  And then they have 256 patches.
*  So there's 256 patches.
*  So there's 256 of those 768 vectors.
*  And also there's one global patch, global representation for the entire image.
*  So that's another 768 vector.
*  So that's how you get 257 by 768.
*  And so instead of just predicting a single 1 by 768 vector for the entire image,
*  we actually predict that 257 by 768 for each patch plus the full global representation.
*  So maybe hopefully that makes more sense in terms of what's being predicted here
*  for the clip image embedding.
*  Yeah. Interesting.
*  So that's a dramatic increase in the number of numbers.
*  I mean, you're going from 15,000 to something like whatever, 150,000, maybe 200,000 numbers.
*  So that's always kind of interesting in itself.
*  Now, so you're predicting there the image embedding?
*  We're trying to predict the image embedding.
*  But again, when we predict it, we have these different losses,
*  like a contrast of loss and all these different losses.
*  So again, when we predict it, it's not necessarily aligned from the very beginning
*  to the image embedding.
*  So it's not going to have the exact same values as the image embedding from when we start out.
*  And so that's why there's this additional process for the reconstruction.
*  But you can use that predicted image embedding for retrieval,
*  because the similarities will work out perfectly fine anyway
*  without needing to do this alignment process.
*  So it's just we predict these image embedding.
*  So that's why in the paper, we don't call it necessarily image embedding,
*  the direct prediction from the MLP.
*  I think we call them fMRI embeddings or something like this.
*  But the direct output from the MLP isn't going to match exactly with the clip image embeddings.
*  But that's what we're trying to predict there.
*  And that's enough to do the retrieval out of the Lion 5 billion data set,
*  often down to even the single one image out of 5 billion, correct?
*  Yeah, that's basically correct.
*  Again, we have this contrast of loss that we're training the model,
*  the MLP with.
*  And so that allows, again, for the cosine similarities to work out,
*  because we're doing this contrast of learning,
*  similar to how the original clip models were trained.
*  And so then we can get the embeddings that work well with this retrieval task.
*  The next step is doing this aligning.
*  And I'm a little confused there as to,
*  was there something preventing you from doing that in an end-to-end training way?
*  Or was it just a matter of, we knew we wanted to do this in pieces anyway,
*  so this was an efficiency?
*  Why is that two steps instead of one end-to-end?
*  So that turns out to be a bit of actually a trade-off between
*  retrieval performance and reconstruction performance.
*  If you do end-to-end, it would be hard to get the best performance for both tasks.
*  Dividing up into these two processes, these two pipelines,
*  this allows us to get, we have something that we can do well for retrieval task,
*  and then we can get something that does well for image reconstruction.
*  So that's kind of the main motivating factor there for dividing it up.
*  And again, we have some ablation studies in the paper that kind of demonstrates this
*  concept of the sort of trade-off between reconstruction and retrieval.
*  Is there an intuition for that?
*  I'm a little drawing a blank as to why I would expect that they would,
*  I currently don't expect.
*  So you have to help me develop the intuition for why that would be the case.
*  I think it's potentially because there are some, yeah, like what may do,
*  in terms of getting that nice cosign similarity that sort of, again,
*  making sure these sorts of embeddings are similar to some images and different to others.
*  I guess that's kind of different, I guess maybe different information is needed or different sort
*  of representations may be needed for that approach versus if you want to just take
*  something to predict the final image.
*  I guess there may be some differences.
*  Yeah, I mean, even for us, I'm not sure if we have the best intuition as well for what's going on
*  there, but yeah, I guess there are some, there's different information that may be needed for these
*  two different tasks, I guess.
*  Yeah, it's an interesting question why the reconstruction and the retrieval
*  have this sort of trade-off.
*  So if I, again, understand correctly, it is a sequential process even in the inference step,
*  right?
*  Like maybe I have this wrong, but what I understood was voxel data comes in,
*  it's first then mapped onto the clip embedding space in such a way where it'll have this,
*  using the contrastive learning, so it'll have this high similarity so that you can perform
*  your database search with a vector database.
*  For folks who want to go deeper on that concept, we have a whole episode on vector databases
*  with Anton Trenikov, who is from Chroma, one of the founders of Chroma, and they have a
*  powerful demonstration of their technology built on this same data set that really flexes the
*  scalability of it.
*  So go listen to that if you want to think about, or want to learn more about the
*  nature of doing these vector database searches.
*  But okay, so you've got that, that's enough then to power the database search,
*  and then you're doing another transformation sequentially into the form that would then
*  feed into the diffusion model.
*  Yes, that's pretty much the case, yes.
*  So all the information is there the whole time, like that intermediate step,
*  it contains all the information by definition, right, that then gets kind of re-formulated.
*  So is it maybe the case that just like the constraints that you're working with are
*  different across these tasks?
*  Like maybe it's not sort of a fundamental thing and more like, well, what the diffusion model
*  needs is just different from what, you know, the sort of, you're training not necessarily
*  for informational content, but like for a specific representation that is required for
*  to use some frozen existing system.
*  Exactly, yeah, that was one of the things as I mentioned, because the idea is that you have
*  a diffusion model that's taking in, you know, specific clip embeddings.
*  And so the problem is that those embeddings that we produce again, they're trained with
*  this contrast of loss.
*  Basically, you can either train with the contrast of loss or you can train with like something
*  like an MSC loss, which is more like, yeah, you can directly compare, you know, you can get the
*  values to match exactly.
*  But so it's for the contrast of loss, that's good for that retrieval sort of task.
*  So when we train with the contrast of loss, it's good for that sort of retrieval stuff.
*  And so we're using that for the retrieval task.
*  But then the problem is, again, those representations may not necessarily match
*  a regular clip image embedding.
*  Again, it's useful for doing the sort of cosine similarity, getting similarities to existing
*  embeddings, but they don't match those sort of existing embeddings directly.
*  And yeah, again, there's actually, we have a good example of this sort of alignment process in the
*  appendix of our paper.
*  And so if there's this sort of U-map depiction of the clip image embeddings, as well as the
*  fmi embeddings, you can see that without our sort of alignment diffusion prior process,
*  you can see that the embeddings are kind of in two separate clusters almost.
*  And so, you know, they don't really line up together.
*  And then we need them to line up together in order for us to be able to pass it into
*  an image generation model that was trained with those clip image embeddings.
*  Because yeah, you want it to match those clip image embeddings,
*  because that's what the diffusion model knows to work with.
*  So we're just trying to make, yeah, the information is there, but we're just trying to
*  put it in a way that the model is used, that the pre-trained frozen models are used to.
*  And I guess that also has to do with the different objectives,
*  the sort of contrast objective that we're trading with.
*  It's easy to get, you can train that, you can get these good representations for the retrieval task,
*  but it doesn't give you representations that match exactly the clip image embeddings that we
*  need for passing into the pre-trained models.
*  So the final version that actually can be passed into the image generation model,
*  that is the thing that is directly analogous to the image embedding.
*  And I see how that's represented in the figure.
*  So is then maybe the surprising thing or the thing that needs understanding
*  is like, all that seems okay.
*  And now I'm like, well, wait.
*  So in addition to that, there's like a fact that if you want to maximize your retrieval performance,
*  you probably could just use those.
*  If you had trained the whole thing end to end, you could use the genuine aligned image embeddings
*  to power retrieval, but it doesn't work as well.
*  And what's revealed is there is actually a better way to represent these voxels for
*  retrieval purposes that is kind of its own thing.
*  It's like a, it's kind of a different subspace in this space that somehow it kind of just gradient
*  descends its way into.
*  And we really don't even know what that is.
*  That's like not really interpretable as of now.
*  Well, I think this is the same question for clip in general,
*  because this is a similar problem with clip image embeddings and text embeddings.
*  They are not lined up in the same way.
*  So I think this may be just kind of a general question in terms of, yeah, what's going on in
*  terms of the clip image embeddings and text embeddings.
*  Yeah.
*  It seems like when you train these sorts of models with contrast, this sort of contrast
*  objective, that doesn't really incentivize them to actually map to the same exact region,
*  the same exact space.
*  They map to kind of different spaces that have the appropriate, I guess, cosign
*  similarities and appropriate relationships, because the contrast of learning is just kind
*  of just, you know, trying to maximize similarity to similar things and, you know, minimize
*  similarity to things that are not similar.
*  But I guess that doesn't necessarily mean that they have to be in the exact same space,
*  I guess.
*  So I think there's sort of that question even in the case of clip image and text embeddings.
*  And again, that's why in the original Dali work, they did something similar where they took
*  the clip text embedding and then they had to incorporate this additional diffusion prior
*  to convert it into a clip image embedding.
*  They couldn't just pass in their text embedding into a diffusion model that took image embeddings.
*  So it's a similar sort of problem.
*  And I think it's just kind of a question for the contrast of learning community, I guess,
*  or something like this.
*  Yeah.
*  I think it also has to do with the sort of like when you work in these high dimensional
*  spaces, this is something that starts to show up.
*  So I think that's the other thing.
*  It's like, you know, we're working with this very high dimensionality data in terms of
*  the clip embeddings.
*  So that's something that there's something about working with this high dimension data
*  that leads to these sorts of properties.
*  If you had done the full end to end training, that would presumably be fine for the reconstruction.
*  Yeah. I mean, the goal was obviously to get best reconstructions.
*  We tried different things out.
*  I think we kind of stumbled upon this sort of retrieval task.
*  I think, yeah, because the issue is that if you want to go from, again, the problem is
*  like if you're going from the fMRI signal to the clip image embedding, I guess it has
*  to depend on the source of losses that use because we train it with a contrastive objective.
*  Like theoretically, it should work, but maybe more practically, it might be difficult to
*  just directly go to the clip image embedding.
*  I think that like because you can't so you can't train it necessarily maybe with a contrastive
*  objective because that is meant that that's going to cause it not to be it won't necessarily
*  be aligned that way.
*  But like theoretically, that should be a perfectly fine pipeline.
*  But I think practically there can be some difficulties getting such a model to train
*  well and to get an accurate model at the end.
*  So that would be the caveat I would mention.
*  Because one thing that's really interesting about both of these papers that you put out
*  in the last short period is again, the low data, but also kind of the non transformer
*  architecture.
*  Right. I mean, you've got something here that jumped out to me like if I understand
*  correctly, there's no attention mechanism in this architecture, at least in the models
*  you've created.
*  Yes. The model that we created is basically the MLP.
*  And so yeah, there isn't really.
*  Yeah, it's just the MLP.
*  And then of course, the clip will have, of course, attention in there.
*  And of course, the diffusion models could have as well.
*  But the MLP not really.
*  Yeah.
*  How big of a role then does the limited data set size play?
*  Because you have basically just under a thousand images per individual and you end up training
*  models for each individual.
*  So you're really just training on a thousand pairs of this is the image that the person
*  saw and the this is the fifteen thousand numbers for the fifteen thousand voxels as measured
*  for that image.
*  That's it.
*  Right.
*  Just a thousand of those pairs.
*  I don't know if you're talking about like the 982, if that's what you were referring
*  to in terms of under a thousand.
*  That was specifically a test set.
*  There are, I think, several thousand training samples that are used during training.
*  And that was with the retrieval.
*  I think that's the value you may be talking about.
*  I'm not 100% sure if that's what you were referring.
*  So yeah, that was just the retrieval experiments.
*  And so basically, we have multiple subjects, first of all.
*  So that's another thing worth mentioning.
*  Is that we have multiple subjects.
*  So that's multiple different people that are looking at these images and the FMI signal
*  is measured.
*  The FMI signal is different per subject.
*  And so we actually train separate models per subject.
*  So the way we do that is that we have the subject.
*  We have subject one and the data for subject one is divided into a training set and a test
*  set.
*  And so, you know, there may be a few several thousand samples from subject one that's used
*  for training and then you have a test set again.
*  And so, yeah, that's what we have.
*  And then we then you have to do similar process for subject two and all the remaining subjects.
*  And another thing to note is that, yeah, so we have subject one.
*  We did all the model development on just subject one.
*  And so, like, yeah, any sort of experiments were done.
*  They were all done with subject one.
*  And then for the rest of the subjects, we just did the same.
*  Whatever worked best for subject one, we did the same thing for the rest of the subjects.
*  And that's what we also reported.
*  And then the other thing, of course, is that when we're looking at the data sets,
*  the images that the subject looks at during the training in the training set is different
*  from the images that they look at that's present in the test set, of course.
*  So just again, to make sure that we are not overfitting or anything like this.
*  We want to make sure they're two separate sets.
*  But yeah, there are several thousand samples for the training set.
*  I think the exact data is or the exact information is in the appendix of the paper.
*  But yeah, I mean, it's still not that much, of course.
*  Yeah, it's small, right?
*  I mean, we're looking at five billion images in the in the Lion data set.
*  And now we're talking basically one millionth of that.
*  So it's surprising that you're able to get this much generalization out of
*  seemingly such a small set.
*  I mean, these images are just all kinds of different random scenes and subject matter.
*  And it's pretty diverse set of imagery that you're drawing from.
*  I think part of the reason is because we are leveraging these pre-trained models.
*  So of course, we're leveraging the representation space of the clip models.
*  And so the MLP just needs to learn how to map something that is similar to the clip image
*  embedding space.
*  So I mean, again, even with the sort of even before the diffusion prior alignment step,
*  it's still mapping to some space that should have kind of similar properties of the clip image
*  embedding space.
*  And in terms of how the images are laid out in that space, it should also be similar.
*  That's, you know, it should still have some sort of similar properties of the
*  clip image embedding space.
*  So I think that really helps.
*  It's just like you're kind of already mapping to something that is a very well established
*  representation.
*  So you have that sort of well established representation that you're mapping to.
*  But again, also, like, we don't know how well it's going to generalize out of natural scenes.
*  We know whatever we were training with.
*  And it's very much possible that it doesn't generalize out of those specific kind of
*  images.
*  And yeah, again, it also has to do with the sort of image reconstruction, the sort of image
*  generation models that we work with.
*  They also may have some particular data sets there that they are trained with.
*  And those are the sorts of images they're best able to produce.
*  So yeah, there are some sort of limitations in terms of the generalizability.
*  And I guess, yeah, we haven't studied that as much.
*  But the fact that we're able to train with such little data and get really good results
*  is also partly because I think of this really rich representation space that we're working with.
*  Yeah.
*  One of my prior Touchstone episodes that I always keep going back to was with the authors of Blip
*  out of Salesforce Research in Singapore.
*  And I use some of their models in my own product development work.
*  And that was kind of my first trip down the rabbit hole of these kind of bridging or mapping from
*  one high dimensional space to another.
*  And since then, it's like this just kind of comes up everywhere.
*  It seems that to a first approximation, it seems like every space is kind of
*  bridgeable or mappable to another space if you're clever enough to figure out where to put the
*  pylons.
*  Does that seem right to you?
*  It seems like all these things are kind of learning similar world models under the hood.
*  I think so.
*  I think there is some, yeah, I think this idea of mapping from one space to another,
*  one latent space to another is a very powerful idea.
*  And yeah, I think that it's always best to try to take advantage of that as much as possible.
*  And to also take advantage of these pre-existing latent spaces, especially in the cases that you
*  may not have enough data.
*  I think this is really a great opportunity.
*  Again, I mean, this has been true, I think, for a long time.
*  I think the more recent thing is the idea of these multimodal spaces.
*  Of course, the general idea of using pre-trained latent spaces isn't new.
*  I mean, that's kind of what transfer learning in a nutshell kind of is using the pre-existing
*  latent space of these pre-trained models.
*  But of course, a lot of them were focused for specific domains.
*  I think now the real advantage, the real, I guess, innovation these days is to be able
*  to use these multimodal spaces as well and being able to map different things to these
*  multimodal spaces.
*  I think that's kind of a really exciting area that, yeah, it's interesting to see lots of
*  developments in that.
*  I think there was some papers that recently it was like mapping anything to anything.
*  I think it's from Facebook, Meta, I think that they published a paper like this.
*  It's, again, a very, very powerful idea.
*  And yeah, I guess there is some sort of base representation of something that can be
*  utilized for various tasks.
*  But yeah, I guess it also depends.
*  There are representations that are useful for certain things, and that same representation
*  may not be useful for other things.
*  So it's also about there are different representations for a particular image, for example,
*  and maybe some representations are better than another depending on the task.
*  So there's also a lot to explore in the sorts of like how those representations trained and
*  what tasks are those useful for.
*  Again, it comes maybe different sort of clip models, blip models, all these different models
*  that are out there.
*  And they're trained with different objectives and they lead to different representations.
*  And that's something I think isn't fully explored yet.
*  And there's a lot of opportunity there to explore the differences between these different
*  representations and how they can be used for different applications.
*  So lots to explore there.
*  Yeah.
*  So we're not even fully done with the architecture.
*  We alluded to kind of the last part earlier, but since you mentioned like these, you know,
*  different pre-trained models and the different spaces that they have,
*  you've got another kind of clever dimension to this as well.
*  Right.
*  So that is the, and I'd love to maybe understand a little bit again, trying to develop some
*  intuition with the clip embeddings.
*  You know, that is originally a joint space of language and text.
*  And so you point this out in the paper that the image embeddings are kind of inherently
*  more about the captionable part of the image, if you will.
*  This is something I've explored in a lot of different ways too.
*  But what notably things that are not included in the captionable, you know, qualities of
*  an image would be like, how beautiful does the image look?
*  You know, is it appealing?
*  You know, those things are typically not represented in captions.
*  They're not really captured in this clip representation all that much.
*  So what you've really kind of communicated is some sort of semantic understanding at
*  that point that like, this is what the image would contain.
*  You also then have this other angle and then they converge at the end, but then you also
*  have the stable division VAE encoding.
*  And I want to develop a little bit more intuition for that as well.
*  But that has kind of the other half, which is like, what does this thing look like kind
*  of compositionally?
*  Like what colors are where?
*  And you have this kind of intermediate state that is like a blurry thing where it's like,
*  I don't necessarily know what that is, but I do kind of know where the color, you know,
*  what colors are where and like, there's some blobs here.
*  Yeah.
*  What more would you tell us about that side of the pipeline?
*  I mean, that's pretty much a pretty good summary of it.
*  I think, yeah, the idea is just to map the fMRI signal to some sort of VAE latent representation.
*  And that latent representation is coming from the stable diffusion autoencoder.
*  And that is able to contain a lot of this more low level information.
*  And we're able to then output some sort of blurry image.
*  And that is used as a starting point for the diffusion models that are then producing the
*  final image given the fMRI clip embedding, the clip embedding that was produced.
*  So yeah, this is doing this sort of image to image process.
*  You know, people have explored this for various AI art applications already where you can kind
*  of start out with some image, often like, for example, you can start with a sketch or
*  something like this. And then you take that sketch and then you can use like stable diffusion,
*  for example, to just produce this beautiful image based on the sketch.
*  But again, the idea is that, you know, the output image has a lot of that sort of the colors or the
*  structures, the positions, very similar to that original sketch.
*  And so that's a similar idea is that we have that starting image that's almost like a sketch of the
*  you know, the final image. And we are then of course taking our diffusion model, which is given
*  the semantic information coming from our clip embeddings. And it is producing a nice final result
*  that matches the sort of maybe colors or the sort of spatial position structures that was there in
*  the original very blurry kind of sketch of the image that was produced by our low level pipeline.
*  So, I mean, it's getting very blurry. So it just helps a bit. It helps a bit and gives you
*  better low level information, better low level results. But yeah, it's good to have additional
*  information where you can kind of see, you have to kind of look for it and you can see, you start
*  to see that it's kind of apparent that, okay, maybe that zebra is in the right place or that person is
*  kind of in the right place. And, you know, you see a little bit of that kind of matching up a bit
*  when you look compared to the original image. And so, yeah, it kind of just provides an extra
*  factor, that extra improvement in the final image, I'd say. Yeah. But again, it's not
*  completely necessary. Like if you just want, if you just cared about the semantic information,
*  you don't need to have a low level pipeline. It's not a necessary part of the-
*  You can just start from noise.
*  Yes, exactly. You just start your diffusion model, you know, the typical process is it starts from
*  noise and from noise, it does that sort of iterative process to produce the final image.
*  So instead of starting from the low level image, you could just start from noise and you can get
*  an image that matches the semantic content of the original, but may not necessarily have that
*  spatial information or colors or any of those things correct. So yeah, that's, it's not a
*  completely necessary part, but it just helps provide, sometimes it'll just help improve the
*  image a bit. You're definitely standing on the shoulders of, you know, a lot of recent giants
*  here where it's like, this work wouldn't even really have been possible in anything approaching
*  this way. Whatever was the most recently released, you know, pre, you know, kind of frozen model that
*  you're building on top of, I guess would be stable diffusion. So that's like, you know,
*  six, eight months ago that that thing first, you know-
*  We actually, yeah, we of course use stable diffusion. We actually tested a few different
*  pre-trained image generation models. We tested stable diffusion variations because we're taking
*  in clip image embeddings. So we're looking for the ones that other image generation models to
*  take clip image embeddings. We trained, started with like stable diffusion image variations.
*  I think it was Lafitte, I don't know how to pronounce it exactly, but it was like,
*  I'm on again, one of these other papers, Lafitte and then versatile diffusion. And that's the one
*  we actually went ahead and actually used for the final image generation. It gave the best performance
*  was this versatile diffusion model. And this is actually the one of the models that again takes
*  in, like I talked about the full clip embedding instead of the sort of global information, but
*  actually the very like the information for each of the tokens, each of the patches. So that full
*  257 by 768 tensor, some of the other models only take in the sort of global vector. That's just
*  like 768 vector, but this one takes in the full information. And again, I think that also really
*  contributes to much improved performance when you get that full information that the model's
*  predicting for the whole image and you're passing all that information into your pre-trained diffusion
*  models. And some of the fusions models don't take that. And those ones are not really necessarily
*  doing well for this task. But when you have a diffusion model that also takes all that full
*  information, then yeah, it can actually produce really nice results. And I think, yeah, versatile
*  diffusion is a paper that I think maybe went a little bit under the radar, but yeah, their models
*  are actually quite good for image generation as well. And so that's what we use and got the best
*  performance. Yeah, we can use any sort of future pre-trained image generation models that take in
*  these sorts of clip image embeddings. So yeah, we're really excited that, you know, if Stability AI
*  releases some other stable diffusion models that take in these clip image embeddings, these sorts
*  of like variation models or whatever, that is much better. That should hopefully also give us a better
*  reconstructions as well. But yeah, again, like you said, it's, you know, we're really building on top
*  of these sorts of existing models, but I think it's also worth highlighting that this, these
*  models, our approach can continue to work well for whatever future models also may come in the future.
*  So that's also really exciting about our approach. Yeah, that's cool. So, okay, let me try to play
*  this all back in kind of one description. And then I got a few other questions. Then we can go on to
*  the other paper if you have time. So the, I guess, you know, kind of working backwards, it's almost
*  like, all right, we have this raw data about the brain. And we know on the other end that there are
*  these image generation models that have recently been created. And they can work in various ways.
*  They could take text in, they could, you know, if we could somehow figure out when they take the text
*  in, they have to embed the text. And then we could figure out how to kind of bypass the text step and
*  like project directly into the text space. Then there's all these variations where it's like,
*  well, it could take an image in, it could take a, you know, it could take an image in and noise it
*  and then kind of take it in some guidance direction. And I think most of our audience will have at
*  least played with these various tools, right, where you start with text and make an image or we had
*  Suhail from Playground AI on actually our very first episode. And they have a really nice kind
*  of command based image editing tool now. And then of course, you've got your, you know,
*  image to image and all these different variations. People played with all these flavors.
*  So you kind of recognize that like, okay, that's out there as something we can tap into. And I know
*  that all the information I need is contained in these 15,000 voxel numbers. So then you're like,
*  all right, I'm going to take kind of a pincer movement at it. You identify one kind of blurry
*  representation space where it looks like I've basically just put, you know, a Coke bottle in
*  front of the image and I can just make out kind of color blotches and maybe some vague forms.
*  And you figure out how to project the voxels onto that space so that you have kind of a good
*  starting point for what the image qualitatively should look like. And then you separately say,
*  okay, and I also know that I can guide that toward something semantically meaningful
*  if I have the right representation to guide that, you know, the diffusion of that blurry image
*  towards something crisp. So then the other arm of the pincer movement is now we'll project those
*  15,000 voxel numbers onto this semantic representation, which is used to guide that
*  reconstruction process. You put both of those things into an existing model and now you're in
*  business with reconstructions coming out. Yep. That sounds about right to me.
*  All right. I love it. Well, I had to earn that one. There's some really, again, super interesting
*  things. Yeah. One thing I do really appreciate about the paper too is you have this just kind of
*  raw code architecture that's like, this is how the model is set up. And they're not that big,
*  right? So can you tell us a little bit about just kind of, I guess, the scale for one thing?
*  I'm also always really interested in how long does this take to train? Can you do it on
*  a machine overnight? What does your kind of cycle look like in terms of
*  actually training these things? So your iteration cycle obviously follows from that.
*  Yeah. In terms of training, I don't know exactly how long it took because I was in the one training
*  it. Again, the main authors who in this case is Dr. Paul Scotty and Amit Bannerjee. They were the
*  ones who were running a lot of the experiments. So I don't know how long exactly it takes to train.
*  It's probably on the order of several hours. It's not going to be like days and days of training.
*  That's not the case here. But yeah, I would have to confirm with them the exact timing of how long
*  it takes to train. I think in terms of how big the model is, it's mentioned in the paper somewhere.
*  I think it was on the order of a billion parameters. Part of it is also you see that if you use
*  larger models, they do tend to get better performance. So that's also definitely part of it.
*  Yeah. I'm just looking at the paper. I think the model that we finally used had 940 million
*  parameters. So yeah, close to a billion parameters that we used. In the paper,
*  they have different ablation studies. We have different ablation studies of the
*  different architectures that are used. So there are different things that we did try in terms of,
*  yeah, model depth, parameter count, all these different aspects that we've tried.
*  And we found the best model based on that. Yeah. So I guess maybe, yeah, it's not a too large
*  different model, but it's certainly sizable, I guess. Yeah, 940 million parameters. It's still
*  a decent size. Yes. GPT-2 scale in rough terms. So yeah, trained on a, just quoting the paper,
*  one A100 machine for 240 epochs with a batch size of 32. So yeah, just one machine. Pretty amazing.
*  Do you know how inference, I assume inference would be like quite fast on this, right? Like similarly,
*  it should take sub-second type of deal. Yeah, it's pretty fast. Yes. And how about on the topic of
*  the four individuals? So you train models specific to the individual. Can we say anything about
*  how similar or different we are as individuals based on, if I was doing this, maybe you did this,
*  I would be like, all right, I'm going to put subject A's data into subject B's model.
*  And if I do that, do I get total garbage noise out? Do I get something that's decent, but not as
*  good as it was on the actual person's model? How different are we under the hood?
*  That's a good question. Yeah. I don't know if we actually tried those experiments, to be honest,
*  but yeah, maybe they had, yeah, I'd have to ask them. But yeah, definitely there are some
*  differences in the sort of visual perception that different people will have. So that would
*  lead to different representations. Yeah. I mean, we are interested in seeing if, for example,
*  there is a way to somehow map them to some sort of shared space that can be used for anybody.
*  But yeah, there are these sorts of minor differences in the visual perception of
*  different people. So that's why we're required to train separate models for the time being.
*  But yeah, again, this is an open research question in terms of how we can, it'd be really nice if you
*  could have one model that just works for everyone. Part of it is also like, we're trying to think of
*  different approaches. We have different projects that we're working on right now to address this.
*  So again, if there, for example, people who are interested, people listening to this who are
*  interested in working in this further, feel free to check us out. And we have different projects,
*  like maybe some sort of foundation model for fMRI. Let's just train on all kinds of fMRI
*  datasets and then try to use that as something that we can map to. Or some form of like maybe
*  you have a sort of shared latent space for all these different subjects and for any sort of fMRI
*  data. And then maybe there are subjects that may need to do a few more image, some more data
*  collection to be able to kind of calibrate the model or something like this. So the different
*  approaches that we are considering to account for that sort of difference in visual perception of
*  the different people. But again, this is an open research question and there's lots of
*  interesting avenues of research there. And if people are interested in helping out,
*  feel free to join us. And yeah, so I think there's a lot to explore in that direction.
*  It sounds like if I understand you correctly, your expectation would be kind of like,
*  we should be able to get to a point where relatively fast calibration would be possible.
*  Maybe another, if we sort of extend, we said, okay, originally we had five billion images in
*  the datasets that trained the foundation models. It took a few thousand images to train something
*  that could kind of bridge the voxel space into the embedding space. And it sounds like you think
*  there's probably enough kind of similarity there that maybe you can bring it down another thousand
*  fold and have like a five image calibration step that could kind of fit your personal biology,
*  shape of your own head, whatever, to the kind of shared fMRI latent space. That's basically
*  where you think this is going. Yeah, I think that's the hope that we have that something like that
*  may be possible. And this is again, something that the main author, Dr. Paul Scottie, he's been really
*  kind of spearhead this effort in terms of trying to develop these sorts of approaches. And so he's
*  really excited about this and really thinks that something like this would be possible.
*  There's various questions that need to be answered. Like, what are those sorts of five, for example,
*  if it is just five images, what are those five images going to be? Are those different images
*  per subject? Maybe there are some images that, you know, maybe there, yeah, you may have to find
*  different optimal images. And then, yeah, how is that going to map appropriately? So there's lots
*  of open questions, but the general idea is that's kind of where we're hoping we can get to that kind
*  of stage in terms of image reconstruction. And that'd be pretty exciting, I think, if we can
*  get something like that working. Yeah, it's amazing. How much do you think this ultimately
*  feeds into better understanding of the brain, which seems like there's tremendous potential there,
*  versus, you know, the other direction would be like, you know, wearable devices, you know, sort
*  of more kind of, you know, well-personed consumer application. What's your kind of expectation for
*  how this research develops in that respect? In terms of like, yeah, let's start with the first
*  thing of like wearable devices and things like this. Of course, the fMRI is like, you know, you
*  have to go into this MRI machine. It's this very large machine, you know, and it's a very, you know,
*  involved and time consuming process. So to be able to use the fMRI for wearable, I think there's,
*  that would require a lot of development on, in terms of MRI technology and stuff like this.
*  Yeah, it's a strong magnet to be carried around, no doubt.
*  So it's like, that's more of like a hardware problem that, you know, I don't know when that would,
*  if something like that would be solved. And if so, when there are alternative like variable
*  approaches for measuring brain activity, things like EEG, I think FNIRS, different approaches.
*  But like, again, they have different sorts of trade-offs in terms of the signal that they
*  provide, you know, the sort of spatial resolution, temporal resolution. So like EEG is good in terms
*  of like, it's got a good temporal resolution, but its spatial resolution is less than fMRI.
*  And we already talked about how fMRI spatial resolution isn't already, isn't like actually
*  that great, to be honest. Like we talked about, it's like just this sort of millimeter by,
*  you know, two millimeters by two millimeters by two millimeters voxel. And, you know, EEG is even
*  more coarse grained than that. So it seems very unlikely that you can get a decent signal from EEG,
*  for example. There may be some other technologies that may be able to get some signal, but I'm not
*  entirely sure what other ones you can get signal from. So I think there's a lot more of like,
*  at this point, it's more like there's a need for better hardware that's able to actually get
*  high quality signal if you want this to work for variable applications. So I'm not sure if this is
*  like necessarily possible right now. And again, like even then it's like, okay, maybe if you don't
*  use fMRI, then if you're using some other technology, then you have to validate if a
*  similar approach would work well for these other technologies. I expect like if you have a high
*  quality dataset with high resolution and you get the relevant information, the approach,
*  the general approach should work well, but, you know, it still needs to be tested and validated.
*  So like for basically to summarize for variables, you need better, you basically need a better
*  hardware to be able to do this. And if you are using a different technology, then you need to
*  be able to validate that for that other technology. So that's why I'm not really like certain that,
*  you know, this is something that could be used for consumer applications, but it's not going to
*  happen within the next couple of years, I'd say. But, you know, maybe if there are some interesting
*  hardware developments, that could be something that may be possible in the future.
*  Because what I would imagine would be a fundamental challenge of like a consumer hardware
*  scenario would be what kind of resolution can you get? So I wonder if you could start to
*  anticipate what you might need by taking your current approach and being like, what if we just
*  make it four millimeters cubed instead, and we just, you know, average the, you know, that number
*  across, you know, if you take an eight, you know, bit, you know, go from eight voxels to one by,
*  you know, doubling the edge length, and then just take the average of those numbers. Now you just
*  have, you know, instead of 15,000, you have whatever about 2000, a little less than 2000,
*  a little less than 2000, right, numbers. Have you tried anything like that? Do you think that you
*  could just kind of be like, what if we just fuzz our data and like see how far we can fuzz it
*  before we can't read it anymore? Yeah, we haven't actually tried anything like that. But one thing
*  that I think we may investigate in the future is just also just some of the other data sets in
*  terms of, yeah, I mean, there are some of these other data sets that use less powerful magnets.
*  I mean, that's what's been used in the field so far, until maybe a couple years ago when this
*  new data set got released. So, you know, it could be worth just also trying those other data sets
*  as well and seeing what kind of performance people get with those data sets. Yeah, and then again,
*  your idea sounds like an interesting idea too. So there's definitely lots of different
*  approaches to test out that. Yeah, I mean, yeah, it's definitely an important question to think
*  about how much data or how much of the actual signal is needed and the sort of signal to noise
*  ratio needed. But yeah, I think even then like something like EEG or something like this is
*  still like significantly coarser than fMRI, even some of these less powerful fMRI machines. Yeah,
*  and then I guess the other question was about research sort of applications as well, right?
*  We mentioned this also a bit in the paper and, you know, there are some potentially interesting
*  applications. So for example, you could imagine just trying to study the image reconstructions
*  of different, you know, patients with different neurological diseases. You can see like how those
*  sorts of reconstructions change over time as degrees progresses. Or you can use them potentially
*  for some sort of diagnostic applications as well. So one example that, you know, we were thinking
*  of is like, if you had someone with depression, maybe their reconstructions, you know, look a
*  little bit different in terms of like, yeah, maybe a little bit more dull, maybe a little bit, yeah,
*  there may be some differences in the reconstructions that we'd be able to pick up on. There are various
*  studies that look at kind of these sorts of responses to images to or even just like mental
*  imagery, things like this. And a lot of those have been very coarse grained, just be like, imagine
*  some sort of object or like, it's very like, maybe imagine an animal or something. It's very coarse
*  grained. And so being able to also have this more fine grained information, there could be a lot of
*  really useful neurological studies that could be done if you're able to get that fine grained
*  information from a subject in terms of what they're imagining, what they're looking at,
*  and being able to reconstruct that. But yeah, I think there's a lot of interesting things in
*  terms of like, yeah, degrees, disease progression and diagnostics. And of course, you know, you have
*  more kind of basic applications of like, yeah, if you have locked in patients
*  or in coma or unable to communicate with the outside world, maybe some of these could be
*  useful, again, maybe with further development of variable technology and things like this,
*  you can use it for interesting medical applications. So yeah, I think there are lots of interesting
*  medical applications and research applications out there. And yeah, I think we're starting to
*  reach the point where maybe these sorts of image reconstructions can be used for
*  to research interesting clinical problems and neurological problems. So yeah, I think it's
*  quite exciting. So even if it's not necessarily being used for the mind reading for consumers,
*  I think there are still lots of interesting applications that we'll see in the short term
*  in clinical research. Yeah, I think one of my big takeaways from this
*  paper is just how many doors are opening. You know, so many different doors kind of recently
*  opened that enabled you to do this. And I think, you know, you're obviously going to be showing
*  the way to others. And it seems like as much as we have seen a lot of awesome stuff in the last
*  couple of years, something tells me, you know, we're not anywhere near, you know, kind of the end of
*  the, you know, the fruitful exploration of the current paradigm. And, you know, the fact that
*  you're able to do this kind of work with a single A100, you know, is pretty telling, you know, in
*  terms of how much value is already kind of, you know, embodied in these foundation models and just
*  waiting for, you know, a super, you know, clever person to come along and figure out how to,
*  you know, piece together the right architecture to kind of bridge different spaces and, you know,
*  make all these different things talk to each other. It's going to be wild, I think.
*  One of the interesting things about this project is kind of, you know, how it was done, how it was
*  conducted in terms of the sort of open research environment and organization that we had. So this
*  was again done as part of MedArc, which is the sort of research organization that I've founded.
*  The projects that we work on are done in the sort of collaborative and decentralized manner
*  and done in an open source manner. So of course, the GitHub repository was always open source for
*  people to look at and contribute. And, you know, there would be weekly meetings on Discord and,
*  you know, chatting on Discord, sharing research ideas, sharing progress. So all that was happening.
*  And then the compute was provided by Stability AI and, you know, they were able to support our
*  research. And yeah, I think this sort of approach was really great because we were able, and a lot
*  of interesting, smart and clever people were able to contribute to this project. So really was
*  grateful for the contributions, of course, of Dr. Paul Scotty, who's the lead author, and also
*  Ahmed Deep Banerjee, who's also really came up with, you know, really was working on this project
*  a lot and, you know, came up with some of these really interesting ideas that really pushed this
*  forward and really was able to help get this working. And then just so many other contributors
*  from around the world that was able to work on this. I think this is an interesting project
*  that kind of demonstrates the value of this sort of open collaboration as well. And, you know,
*  with this sort of open collaboration, we can do all kinds of incredible things as well. I think,
*  yeah, like you said, there's a lot of other interesting aspects in terms of being able to
*  use foundation models that enables new opportunities. And then, of course, this sort of collaboration
*  that is happening. So I think, you know, this is something that, you know, these sorts of things
*  wouldn't have been possible just a few years ago. And so it's quite incredible what's possible now.
*  And, you know, it can be done by people, you know, that are sitting somewhere halfway across the
*  world and, you know, working from their laptop. And it's kind of incredible what's possible these
*  days. So, yeah. Amnaki uses generative AI to enable you to launch hundreds of thousands of ad
*  iterations that actually work customized across all platforms with a click of a button. I believe
*  in Amnaki so much that I invested in it, and I recommend you use it too. Use CogRev to get a 10% discount.
