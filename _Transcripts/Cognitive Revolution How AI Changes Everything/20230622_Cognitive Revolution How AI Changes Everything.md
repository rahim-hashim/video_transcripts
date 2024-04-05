---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 3777s
Video Keywords: []
Video Views: 575
Video Rating: None
---

# The Virtual Biopsy Revolution with Dr. Tanishq Mathew Abraham (Part 2 of 2)
**Cognitive Revolution "How AI Changes Everything":** [June 22, 2023](https://www.youtube.com/watch?v=Vpt9z3XwoFc)
*  And I'd be very excited about medical applications of AI and using AI to improve patient care.
*  I'm excited about using AI for education, being able to learn whatever we want to learn.
*  There may be concerns of AI being used for polarization of society, but I also think that AI
*  could be used for bringing society together and being able to connect with each other.
*  Hello, and welcome to The Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas, and together we'll build a picture of how AI
*  technology will transform work, life, and society in the coming years. I'm Nathan LeBenz, joined by
*  my co-host Eric Torenberg. Hello, and welcome back to Tenishk Week on The Cognitive Revolution.
*  Today's episode is part two of my conversation with Tenishk Matthew Abraham. If you missed part
*  one in which Tenishk and I discuss his fMRI to image project, which uses visual cortex activity
*  data to reconstruct images that patients saw during an fMRI scan, I highly recommend checking
*  that out. But today's portion of the conversation is quite self-contained, so you can definitely
*  feel free to choose your own adventure. Today we're covering the other paper that Tenishk
*  recently published, which introduces an AI-powered technique to support medical diagnosis based on
*  clinical assessment of tissues. In practical terms, in today's world, cancer screens are often
*  invasive, expensive, and slow. To determine whether a particular tissue contains cancerous growth,
*  the usual workflow is to biopsy the tissue, prepare thin slices of the tissue, stain the
*  tissue with dyes to improve visibility of key structures, and then examine the stained tissue
*  under a microscope, a process that often takes more than eight hours from end to end.
*  The new technique, in contrast, is far faster and cheaper and can even be less invasive.
*  Using 3D image data collected with a new technology called quantitative oblique back
*  illumination microscopy, Tenishk and co-authors were able to use a technique called CycleGAN,
*  which, interestingly, was introduced in 2017, making it a relatively old approach by today's
*  AI standards, to take this entire process down to just one second. A virtual slice of the 3D
*  tissue image is virtually stained and then can be immediately examined, even in the context of
*  ongoing surgery. While this technique is new and will, of course, take time to work its way into
*  general practice, the promise of more effective surgeries based on more effective diagnosis
*  with less unnecessary damage is clear. Again, a picture is worth a thousand words, and I
*  definitely encourage you to follow the link in the show notes to get a sense for the raw
*  inputs and outputs before going on to listen to this episode in full.
*  Special thanks to Tenishk for spending three full hours with me for these two episodes,
*  and thanks also to all of you for listening. If you're finding value in the show, I'd very
*  much appreciate a review on Apple Podcasts, Spotify, or the platform of your choice.
*  And with that, I hope you enjoy part two of my conversation with Tenishk, Matthew Abraham.
*  You've got a second paper, and these two came out within like three or four days of each other.
*  Second one is called Label and Slide-Free Tissue Histology Using 3D EpiMode Quantitative Phase
*  Imaging and Virtual HNE Staining. That is a mouthful, but in the end, there's one diagram
*  in the paper that I think kind of describes the before and after extremely well, and it definitely
*  touches on, or at least alludes to some themes that are kind of outside of your research,
*  but definitely still of interest to our podcast audience, which is like,
*  how are things going to be done in the future? What is work going to look like? What's going
*  to happen with jobs and all these things? So just the kind of before and after is like,
*  how is it done today? You guys have a diagram where it's an eight-hour process for somebody to
*  take a piece of tissue that is biopsied out of a patient, perhaps, and do these real thin slices
*  of it. Now we plate that on a slide. Now we put these chemical reagents on them to dye them colors.
*  That is notably a destructive process where you really can't undo that, and for a lot of them,
*  you can't go use that tissue for something else now that it's been kind of stained the one way.
*  That's kind of used up, right? So then you plate a few of these things and stain them a few different
*  ways. Then ultimately somebody looks at it under a microscope and looks for different
*  indicators, and all of this adds up to diagnostic. The after, one second,
*  you don't even have to with the new method, you don't even have to slice the tissue.
*  I want to hear a little bit more about this, but you instead use this new 3D imaging technology
*  that can image a whole tissue. So in this sense, it's kind of similar to the voxel fMRI thing from
*  before where it's non-invasive against a certain piece of tissue, it doesn't have to destroy it.
*  Then you can pull out these slices from this 3D imaging. You can apply the model that you've
*  developed, which does a virtual staining of the image to convert it to what it would look like
*  if you actually sliced it and stained it. And then a person can look at that, or you could
*  potentially even train a classifier model, as certainly people have done prior to this as well,
*  to automatically process these images. And we're probably going to need one,
*  because it sounds like a lot more of this might end up happening if you are virtually
*  doing all these stains instead of actually slicing and manually staining.
*  Upshot of this is at least, I would say, probably more like two orders of magnitude
*  time reduction in what it takes to get a stained image out. And again, that just means
*  explosion likely of how much of this imaging work and diagnostic stuff can be done.
*  What did I miss in my high-level summary before we dig into some of the details about
*  how you made it all happen? Yeah, I think a high-level that's all
*  sounds pretty accurate to me. The other thing worth noting is this eight-hour process,
*  you can imagine, is very impractical for some applications. So in a typical diagnostic workflow,
*  that's used, but there are some applications where it doesn't work. So for example,
*  during surgery, which is one of the examples that we are really interested in, where a patient may
*  undergo some sort of tumor removal surgery. So the surgeon is going there, for example,
*  if it's a brain tumor, which is again, we're really interested in brain tumors. So if it's
*  a brain tumor, the surgeon is in the surgical site within the brain and trying to remove as much of
*  the brain tumor as possible. And it's often useful to provide some form of guidance to the surgeon,
*  so they know, okay, this is a tumor or there's no more tumor here, we're done. A similar form of
*  we take some sort of biopsy and then we try to image it and tell, okay, if there is still tumor,
*  then maybe that means there's still tumor remaining in the patient as well. So there needs to be some
*  sort of similar guidance, and this is again, using a similar sort of process, but you can imagine
*  that eight hours is way too long to be able to do this in a surgery. So there are some alternative
*  processes that are like 30 minutes. So that's like still like kind of slow, but like it's still
*  much better than eight hours. But that process also provides really low quality images and like
*  very hard to interpret slides and images. So it's not ideal either. So like, yeah, people have been
*  developing some of these alternatives that some of them are, you know, widely used in the clinic,
*  but they're still very, yeah, they're still kind of difficult to interpret and hard to use. So yeah,
*  overall people have been developing these, what are known as slide-free microscopy methods that
*  they try to speed up that process altogether and don't require all that processing like you talked
*  about and can do the sort of, you know, imaging in just a couple minutes or in the case of this
*  particular technology, it's not even the, you know, it's like you can even image directly and
*  it can just take just like a second to image. So it's like, there are very slide-free microscopy
*  technologies, but this one that has been developed as well is actually a very unique technology as
*  well that is quite promising. And this was actually developed by a lab at Georgia Tech.
*  And so this paper was in collaboration with their lab at Georgia Tech.
*  And that is the QOBM, the quantitative oblique back elimination microscopy?
*  That's right. That's the slide-free technology and it's also label-free. So what that means is
*  it doesn't require the staining. So there are some slide-free technologies that do utilize some
*  form of staining. Yeah, itself, the staining isn't necessarily destructive. The most destructive
*  parts are the sort of processing to get down to that single slice. So that's including the
*  sort of formalin fixation, which basically makes it so that these structures are, you know, intact,
*  like they just kind of stay in place. So the structure stay in place, but you know, that's
*  still some form of like, you're basically applying formalin, you know, formaldehyde,
*  which of course can be, you can imagine that can also be destructive. And then there's also
*  this embedding in paraffin vacs. So that allows you to section it into thin slices. So all that
*  sort of processing, that can be damaging to the tissue and it can take quite some time to be able
*  to do all that processing as well. The staining itself can be a little bit damaging, but isn't
*  necessarily the worst part of it, I would say. You can technically, if you wanted to, you could
*  actually like remove the stain in some cases, but you know, it may not be perfect. But because of
*  that, like there are some slide-free microscopy methods that don't require all of these sorts of
*  formalin fixation, paraffin vacs, embedding and all those steps, but still do require staining.
*  So there are some technologies like that that use some sort of dyes that label for specific
*  structures and things like this. But the unique advantage of technologies like QoBM is that it
*  doesn't even require that. And so you can imagine that allows, that's why it's called label-free,
*  it doesn't require any sort of labels, any sort of staining, any sort of dyes. So it's called
*  a label-free technology. And because it's label-free, that allows for in vivo applications.
*  Because you can imagine if you wanted to stain something, you would actually have to remove it.
*  You cannot like apply your stain. It'd be kind of difficult to do that. And you wouldn't want to
*  label functioning tissue in your body. I don't think that's the most ideal thing to be doing.
*  So instead, with label-free technology that's able to image also in a sort of slide-free manner,
*  you could also do in vivo imaging. And that's actually made more practical by the use of
*  handheld probe. So the QoBM technology has been miniaturized into a handheld probe as well
*  by this lab in Georgia Tech. So then they can use this handheld probe to, for example, image in vivo.
*  So yeah, there's a lot of interesting advantages of this QoBM technology compared to even other
*  slide-free microscopy technologies that may exist out there. So that's why we really think that QoBM
*  is a quite promising and unique technology. And then in combination with these sorts of AI tools,
*  it can become a very powerful system for diagnostic and in the case of these sorts
*  of surgical applications as well. So yeah, it's very powerful, I think.
*  Yeah. The vision of being, I mean, everybody has had somebody in their life who's been through one
*  of these tumor removal surgeries. And then it's like, well, how'd it go? And well, the doctor
*  thinks that they got the whole thing, so that's good. And it's like, well, how exactly did they
*  determine that and how confident are they on thinks? And it sounds like, without jumping to
*  the conclusion that I understand the current state of the art, which I certainly don't, it sounds like
*  there's a lot of room for improvement in terms of being able to take a probe directly into the
*  surgical site and be like, zap, okay, cool. Now we got a 3D image of this that we can virtually slice,
*  virtually stain, virtually classify and see, is there any more tumor if it's detected in this
*  process? We could do that right in line. Yep. That's the hope. Yes, that's the goal.
*  So let's talk about then how you did it. Again, a small data regime here by comparison, certainly,
*  to what folks are used to hearing about with trillions of tokens. So yeah, tell you, I was
*  reading the paper and I copied down 2358 QOBM and 1737 H&E tiles. Is that basically like,
*  you have that many thousand of the new kind of image and then 1700 of the like,
*  actually stained tissue samples that correspond to it? Yeah. So these are actually 512 by 512
*  pixel tiles. So they're very small tiles that we're working with. And yeah, that's pretty much
*  correct. And they're only actually coming from a few actual subjects. Or like in this case,
*  we started out with a rat brain model. So there were maybe a few rats that we were working with.
*  And then again, with the human, we had some human examples as well, some human specimens that we were
*  working with, again, just from a few patients. So they're just from a few patients and then we
*  were able to get several images from each of these patients or subjects or whatever. But yeah,
*  even with all that considered, it's still a quite small data set that we are working with here.
*  So 1737 H&E tiles, that essentially corresponds to some smaller number of actual tissue samples,
*  sliced, plated, stained, imaged. And then the tiles are just little sub bits of that larger
*  tissue sample. So like a handful of tissue samples, a handful of actual things, and then just
*  zoomed in 512 by 512 squares from those samples. That's correct. Yes. So that's like really small
*  data. Yes, exactly. Yes. Yeah, it's not much data at all. Hey, we'll continue our interview in a
*  moment after a word from our sponsors. Omniki uses generative AI to enable you to launch hundreds of
*  thousands of ad iterations that actually work customized across all platforms with a click of
*  a button. I believe in Omniki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount. If you had said to me, go build something like this,
*  my knee-jerk reaction would be like, all right, I need to go find how am I going to get 100 million
*  input-output pairs. And then I'm like, well, shit, I'm going to be cutting a lot of tissue
*  to get there. Probably not feasible. Or maybe not. Certainly would take a lot more effort on the
*  actual slicer than you've managed to get away with. So you use a GAN-based approach, which I think
*  folks will probably have some familiarity with. Certainly I've seen GANs used it in the image
*  generation days before the current crop of image generators. That was kind of the way.
*  So I think folks will maybe have passing familiarity. But how did you decide to use
*  that approach? Was it a direct consequence of not having that much data? Or were there other
*  factors that went into it? Where did the inspiration from the architecture come from?
*  First of all, going back to the concept of datasets, of course, I just wanted to point out,
*  of course, with the case of these sorts of medical datasets, these biological datasets,
*  it's of course very hard to collect a lot of specimens, as you can imagine, to be able to...
*  In the case of the rats, that means that if you wanted to collect a lot of rats, you're going to
*  have to sacrifice a lot of rats. And then you have to grow the tumors in the rats, and you sacrifice
*  all those rats. It's a very long and involved process. The same with the humans. It's like you
*  have to wait for enough humans to have brain tumor surgeries, I guess, and then hope there's
*  enough excess tissue around that can be used for research purposes. And it's going to be very hard
*  to collect a lot of specimens. So it's overall just not feasible to do that unless you have...
*  I guess if you were going into a clinical trial or something. By then, you should already have
*  somewhat of an established method anyway. So overall, these are the sorts of issues that you
*  have to worry about when applying AI to medical applications, is that you do have to sometimes
*  worry about the lack of enough data. And especially if you're trying to use AI in
*  a medical application that's using novel technology. If you had something like you want to use AI just
*  for histology, we can get thousands of H&E slides, like the regular slides that is already being used.
*  That's not hard to get because people are already doing that in the regular process,
*  and they're already saving those and storing them. And so if that's something that you're working
*  with and trying to apply AI for diagnosis or something like that, for example, then you can
*  do that. But the problem here is that we're also working with a novel technology and we want to
*  apply this novel technology for all these different applications. And trying to bring a novel technology
*  into the clinic is going to be a little bit harder. And so there's a lot of different
*  challenges around that as well. So these are the different, I guess, considerations that maybe
*  people don't necessarily think about when it comes to applying AI to medicine, and especially in this
*  case of a novel technology. Then specifically for these slide-free microscopy systems, one of the
*  difficult things in terms of doing this virtual staining task is the idea is that, okay, these
*  slide-free microscopy images that we get don't look like standard H&E, which is the standard
*  images, the standard visualization. The H&E represent is the sort of hemotoxin ESN. It
*  stands for hemotoxin ESN, which are the exact stains that are often used for the tissue slides.
*  And that's what the doctors are typically used to seeing. And so this cut typically got this
*  purple and pink color sometimes. It typically has this purple and pink color. That's what the
*  doctors are used to. And so my task is to take those slide-free microscopy images where they may
*  not have any color. So in the case of the QoBM, they're like grayscale images, or in some cases,
*  they may have very different colors. So there's various different slide-free microscopy technologies.
*  Actually, in my PhD research, I was working with QoBM, but I was also working with a couple other
*  slide-free microscopy technologies as well, and trying to do a similar sort of virtual staining
*  task of converting those images to look more like standard H&E so that it can be easier to
*  interpret. So the issue in terms of collecting data for this is when you take your slide-free
*  microscopy system and image a piece of tissue, you're imaging like a fresh piece of tissue,
*  for example. This tissue isn't processed in any way, because that's the whole point of the
*  methodology is to take a fresh piece of tissue and image it. But then in order to get your ground
*  truth, you have to process it. So you have to do the sort of formal infixation, embed it in paraffin,
*  slice it into thin slices, put it on the slide, and then stain it with your stains. And then
*  finally, you can look under the microscope, image it with some sort of scanner, whatever you have,
*  and you get a final image. The problem is all that processing causes significant changes to the
*  tissue. So the tissue that you see at the beginning isn't going to be looking exactly the same as the
*  tissue at the end. You're going to have different changes in these sort of spatial positions, maybe
*  changes in some of the structures, maybe a little bit different. You won't be able to get a pixel
*  match between the original slide-free microscopy image and the final H&E image. A typical process
*  you'd be like, you have your input and you have your output, and you can just kind of like learn
*  to transform that. But you don't necessarily have the output that corresponds to the exact same input
*  now. They look, they're slightly different. So this is what is known as an unpaired image-to-image
*  translation, because you want to translate from the slide-free microscopy image, like this QOBM
*  image, for example. You want to translate from the QOBM image to the H&E, but you don't have exact
*  pairs of the QOBM and the H&E. So this is why it's called unpaired image-to-image translation.
*  So there are a few approaches for this, the most common approach being the CycleGAN approach. So
*  that's the GAN-based approach for doing this translation. There have been some other novel
*  approaches that have been developed in the past few years that I've also attempted,
*  but they haven't worked as well. CycleGAN is actually a very old approach. It actually was
*  developed back in maybe 2016, 2017. It's actually very old. I guess for AI, it's old. Maybe in other
*  fields, it's not as old. And I think AI is one of that unique fields where if something's
*  six months old, it's already ancient. So in other fields, that's not the case. In the field
*  of medicine, for example, something in 2017, that's still pretty new. So in that field,
*  people think, oh, CycleGAN is actually quite new technology. But in the context of AI,
*  CycleGAN is actually quite an old method. But it seems to work really well for these tasks.
*  And in addition, I've tried some of the newer techniques. So there was another approach that
*  was actually based on contrastive learning, which is kind of funny, you know, connecting to the
*  previous stuff that we talked about. I tried that contrastive learning approach. It didn't work as
*  well. I've also tried diffusion model approaches and hasn't worked as well. So I've actually tried
*  a few different other approaches. And maybe it's possible with those other approaches that you can
*  maybe design appropriate loss functions or maybe change the architecture or something and get them
*  to work better. But CycleGAN seemed to work very well, like right out of the box and also with
*  limited data. I'm not 100% sure why that's the case. But that's something I've observed
*  throughout my research is that you can actually train these models with very limited data. They
*  don't seem to overfit. They don't seem to have any issues. They seem to generalize fairly decently.
*  Yeah, as long as you're passing in high quality data into the models, they seem to be
*  that you can train them quite well. And they work well for these virtual sitting tasks. So,
*  I mean, that's kind of one of the first models I've tried. Most of the models I've tried
*  afterwards seem to not be as good as this baseline. And so that's why I've kind of stuck
*  to this CycleGAN approach. So sometimes, yeah, sometimes the newest things are not always the
*  best for at least the specific tasks that you're working with. I think there are some different
*  properties of histology images that make them unique. And some of these newer methods make
*  different assumptions, implicit assumptions that many people don't realize that they do.
*  And those sorts of assumptions don't work well. They don't correspond well to histology images.
*  So some of these newer methods don't seem to work well from what I've observed. But in our case,
*  the CycleGAN seems to work really well, which, you know, yeah, I'm still kind of surprised that
*  this really old technology, I mean, we thought that, oh, you know, we, and I thought that, oh,
*  we'd be working with diffusion models already. But like, I've tried diffusion models and they
*  haven't worked as well either. And it's like kind of surprising to me. Sometimes, yeah, it's worth
*  even exploring some of these older techniques and seeing if they still may be applicable and
*  may be even better in some cases. And that seems to be the case here. So, yeah.
*  Yeah. So how does it help you get over the lack of unpaired images? Because at the end of this,
*  right, your kind of end state is we now have a technology where we can use this new kind of
*  microscopy, you know, even that can be used during surgery on a live tissue.
*  It does like a 3D kind of imaging. Then you can take slices out of that 3D space as 2D images.
*  And then you can kind of apply this mask, so to speak. You know, it's almost like if I went to,
*  you know, Playground AI and said, make this an H&E image, except, you know, with a lot more
*  rigor and actual, you know, usefulness behind it. But that's kind of the, you know, you're sort of
*  painting it over as if it had been stained. But I'm missing the trick that the CycleGAN
*  architecture performs that allows you to do that without having the paired images in the first
*  place. Okay. So maybe it's worth talking about GANs in general, because like you said, maybe
*  it's kind of an old technology at this point. Maybe some people are less familiar with it
*  nowadays. But basically, a GAN is the sort of dual neural network framework. So you have a
*  generator neural network and you have a discriminator neural network. The generator neural network is
*  trying to produce, trying to generate your images, whatever data that you have, trying to generate
*  images that look like they came from that data set. And then you have a discriminator neural network
*  that tries to determine which images are real and which images are generated. So it's being past
*  some random image. That random image could be from the original data set, or it could be an
*  image that was generated by the generator neural network. And the discriminator is going to try to
*  figure out if this is a fake image or a real image. So basically what you're trying to do is you're
*  actually trying to train the generator to generate images that fool this discriminator. So you're
*  training your generator to just try to make images that are more and more realistic such that it
*  fools the discriminator. And the discriminator is trying to tell, it's being trained to try to
*  improve, it's trained to try to tell the difference between the generated image and the
*  original image. So there's sort of like back and forth that's going between the two models. The
*  generator is trying to fool the discriminator and the discriminator is trying to determine which one
*  is generated. And it's just kind of going back and forth. And the idea is that eventually your
*  generator is going to keep in, it's going to, through this process, it's going to improve and
*  improve and improve and finally give you really realistic images that look like they came from
*  the original data set. So that's just a general idea of GAN. And this was used very frequently
*  for all kinds of applications. It was kind of like, I'd say the first primitive form of
*  generative AI, I would say. I mean, these were being used for things like generating faces and
*  we had all these sorts of different GAN architectures, like style GAN was very common at the time.
*  So this was being used quite commonly, I guess before 2020 or like, yeah, up to 2020 or so.
*  So the additional thing that the cycle GAN itself provides in addition to this general GAN framework
*  is that the cycle GAN adds, it actually has two generators and two discriminators. So the idea is
*  that you have one generator that is taking in the original image. So in our case, that is the QOBM
*  image. It's taking the QOBM image and it's trying to produce the H&E image. So it's going to produce
*  some sort of fake H&E image. And we also have a discriminator that is going to try to figure out
*  if it's a real image, a real H&E image or a fake H&E image. It just sees the H&E image from the
*  descriptor, from the generator, or it sees some real H&E image. So it's trying to learn how to,
*  you know, classify between real and fake. That signal is going to the generator and the generator
*  is trying to improve itself and produce more real H&E images. So it's able to produce really nice,
*  realistic H&E images. But that doesn't mean that it has to produce H&E images that correspond to
*  the original QOBM image. It can produce any H&E image. It doesn't matter. As long as it's real,
*  it will fool the discriminator. As long as it looks real, it will fool the discriminator.
*  So that's why we have an additional generator that takes in the H&E image produced by the first
*  generator and it produces a QOBM image. And again, we can have another discriminator that,
*  you know, can take in that generated QOBM image, you know, that is classifying and makes that
*  second generator. It's able to now produce really realistic QOBM images. But what's unique now is
*  that we can compare that last QOBM image to the first original QOBM image. And basically,
*  you want those QOBM images to be the same. You have your starting input QOBM image. It's going
*  to that first generator to produce an H&E image. Then it's going to the second generator to produce
*  a reconstructed QOBM image. And you can map those two together, you know, do some sort of like some,
*  like MSE loss or some sort of direct comparison of these two images now. And you can say, okay,
*  those have to be as close as possible to each other. They should be exactly the same.
*  And the idea now is that in order to be able to reconstruct that QOBM image at the very end,
*  the content has to be maintained throughout the entire process. The content has to be maintained
*  throughout the entire process. So that means the QOBM image is being converted to an intermediate
*  H&E image. And that H&E image should hopefully now maintain the content of the original QOBM image.
*  So now you're able to get a realistic H&E image that maintains the content of the original QOBM
*  image. And that's what you actually want. And so that's the general idea of CycleGAN. It's not
*  perfect. Like you're just kind of hoping that it does maintain the content, but it seems to work
*  most of the case. Like, you know, I guess it turns like there are some cases where people see like,
*  oh, it doesn't actually maintain the content. And it actually there are some cases where it doesn't
*  work perfectly. I won't go too much into that. But in most cases, if you also if you have really
*  high quality data that you're working with, a good data set that you're working with, it seems to work
*  quite well. And again, that's basically in a nutshell, how CycleGAN works. It's this idea
*  of having the cycle where you're going from QOBM to H&E back to QOBM. And now you have something
*  that you can compare directly because it's comparing basically to itself. So it's this sort
*  of idea. It's called cycle consistency. So that's why the CycleGAN actually stands for
*  Cycle Consistent Generative Adversarial Network. So that's why it's called CycleGAN. So that's the
*  general idea of a CycleGAN. And it's surprisingly powerful, even though I'd say, you know, it's not
*  the most sophisticated architecture, but it works. So, yeah. So you've ultimately got four
*  models, right? Yes. But at the end, you only need that one first generator that's used for inference.
*  So it's actually you do have like basically three models that you actually don't necessarily use
*  anymore afterwards. So, you know, it feels like, okay, maybe there's like, yeah, it's like maybe
*  you're using extra computation. But again, I've tried some of these other methods that seem to be
*  simpler, only use a single model, but they don't seem to work as well. It seems to work, but like,
*  it's not ideal. You do have these four models that you're training with. And then at the end,
*  you just use that first generator for your desired virtual staining task.
*  Still in there, there's not a conceptual guarantee that virtual stain will have like exactly the
*  same structure, whatever. The thing that is keeping it on the rails is the fact that
*  you're then enforcing that it must be able to be converted back. So if it was like
*  too divergent, you'd lose that ability to convert back.
*  The issue can be sometimes like, so for example, it's mentioned in this paper a bit, and it's
*  actually discussed in another paper, a workshop where I wrote for another Slyfee microscopy
*  virtual staining. It's that sometimes, basically the idea is you want to make your task as easy
*  as possible for the cyclogand in order for it to be able to do this. You want it to be
*  as easy as possible, so the easiest possible solution is basically to maintain the content.
*  That's what it's just kind of naturally, you want it to be the easiest thing to do.
*  Because what we've seen are some examples where, again, in the case of the QoBM, and for some of
*  the other Slyfee microscopy images that I've worked with, you can have sometimes in the H&E,
*  the nuclei are dark because they're labeled with this absorbent dye known as hematoxin,
*  and the nuclei, the cell nuclei, kind of show up as this dark purple color.
*  But the problem is that in QoBM, they're kind of bright in the QoBM. The cell nuclei are kind
*  of bright, especially mostly for like the tumor cell nuclei, actually. They're like kind of pretty
*  bright. So this can cause issues because the cyclogand is confused that in the H&E, the
*  nuclei are dark, but in the QoBM, the nuclei are bright. So it may make some sort of like
*  H&E image, but that H&E image has the dark regions in the QoBM as nuclei,
*  but they're actually not nuclei. They're just like other parts of, like they're like maybe the
*  cytoplasm of the cell or some other region of the cell, because the nuclei in the quim are actually
*  bright. But it's able to do that whole cycle consistency because, you know, it can still know
*  how that maps. Then it has its own way of mapping that to a regular QoBM image, that incorrect H&E.
*  It's probably better to see this visually, and we do have, there's a figure in the paper in the
*  supplementary material where you can actually see that really visually. It's harder to describe
*  this sort of thing, but there are some cases like, yeah, because like there's this difference between
*  the QoBM images and the Asian images. So you have these issues. So the solution that we take is we
*  simply invert the QoBM image. And so now in the inverted image, the nuclei are now dark.
*  And so now the cyclogannous like, okay, they're dark nuclei in the QoBM, they're dark nuclei in
*  the H&E. The simplest possible thing to do in order to make H&E images while keeping the cycle
*  consistency and the consistency going on is just to take those dark nuclei in the QoBM and convert
*  them to dark nuclei in the H&E. So you got to make it as simple as possible for the cyclogann.
*  So that was kind of one of the key insights that we had when working with the cyclogannous. It's
*  a bit of like trying to understand what's going on, the sort of psychology of these sorts of models
*  in a way. It's like, what are the things to get this to work? So one of the things we noticed is
*  try to make it as simple as possible for the model. And there's different things like this that we
*  have to play around with in order to work with these models. So actually a lot of the work that
*  we did was on the data side, data processing, data cleaning. And it turns out there's a lot you can
*  actually do on the data side that can really improve the quality of the models. So I think this has a
*  lot to do with what is known as data-centric AI, where it's like you're focusing on the data
*  development rather than the model development and trying better and better models, but you try to
*  improve your data. And I'm a huge believer of that sort of practice in terms of like, yeah,
*  the data is one of the most important things you should be focusing on. You can actually get
*  really basic models to work really well if you've got really good data sets. And knowing how those
*  data sets are processed by the models and how the models work with those data sets and having all
*  that and understanding that can help you to get good results with even really basic models.
*  I was interested to see that to the degree that there are any points of confusion, it seemed to be
*  that the system was flagging things as potential tumors even when they weren't. It did not miss
*  any of the actual tumors. Yeah, it wasn't something that we explicitly designed for. So again,
*  I think this has to do with slide-free microscopy being different from regular HD images and how to
*  get an exact match. So we went to the errors, the ones that it failed with, and we noticed a few
*  common factors. One of the factors was these sorts of blood vessels. You have these small blood
*  vessels, these sorts of capillaries as they're called. In H&E images, you don't get continuous
*  capillaries because you have these very thin slices. It's hard to get like, if a capillary is
*  going up and down or something, you may just get like a... Think about a 3D, if it's going a little
*  bit up and down and you just cut a very thin slice, you're not going to see the full capillary.
*  So you just get a very thin slice. You're going to get very small segments that you'll see.
*  We don't see full continuous capillaries. That was one thing that we do see though in the QOBM
*  because it's an intact tissue. It's not necessarily sliced. You can see more the full capillaries.
*  And not only that, like during, again, some of the processing with the H&E, some of these
*  red blood cells in these blood vessels may fall out and all sorts of issues. So yeah, basically,
*  you're not going to see... Some of these structures are intact in the original QOBM images, but not
*  intact in the H&E. So sometimes that confuses the cycle again. It doesn't know what to do with those
*  sorts of structures. Sometimes it's able to deal with it, sometimes not. And in this case, we had
*  those capillaries in those sorts of images. Another thing is that we have these sorts of what I call
*  white matter bundles, which are specific structures, again, in the brain. And again,
*  they look quite different in the QOBM compared to standard H&E. And so because they look different,
*  maybe in a more intact manner, that this is maybe actually how they are supposed to look like within
*  the H&E with some of the processing and some of these extra steps and the staining, it looks
*  kind of different. Again, the cycle again is getting a little bit confused about the differences
*  between the QOBM and the H&E. So those are some of the kind of features that we see that happen.
*  And because of these differences between QOBM and H&E, it can be a little bit hard sometimes to
*  map them. And so sometimes occasionally the cycle again will get a little bit confused about this.
*  So it's not necessarily ideal, but it's a very difficult problem. And you have things that
*  look different like this and it's hard to get an exact match. So it is what it is. But it's possible
*  that with collecting more data and different data sets, it may be possible to improve this further.
*  And ideally, you would want no false positives and no false negatives. So there's still room
*  for improvement, obviously, especially if you're working in something like with BrainTumer.
*  You also don't want false positives because that means that you'd be removing perfectly healthy
*  functioning brain tissue. And that's also a very difficult and something you'd like to avoid,
*  potentially. So there's still room to improve, but it's still quite good right now. But in the future,
*  there may be better approaches, maybe larger data sets or something like this that may be able to
*  help solve some of these issues. What is the training process on this look like? How compute
*  intensive is this? Yeah, it's also trained on a single A100. Each of the models are just
*  trained on a single A100. And it takes just a few hours. It's not particularly long again.
*  So yeah, I can just put an experiment for running and after two or three hours, I can come back and
*  see. So yeah, it's again, partly because the data sets are not very large. So also it's like, yeah,
*  it takes quite quickly to go through the data sets. But also, yeah, I mean, I tried doing these
*  experiments though earlier, even with like a V100 and things like that. And of course, it used to
*  take much longer back then. So also, part of it is also like, now the GPUs are getting better too,
*  so it's much faster too. But yeah, it's pretty fast and it's doable on pretty simple, yeah,
*  pretty limited hardware compared to, of course, a lot of these larger trading runs.
*  What do you think is kind of the path to this sort of thing being actually used in a clinical
*  setting and like what are the bottlenecks? So of course, there are certain like,
*  potential model developments, improvements that could be made to the virtual staining. So you
*  can of course try to improve that further. But also, it's very important to further validate
*  this technology. We only train, we only play around with, you know, a few human specimens.
*  So, you know, for example, we only got like one, a single human healthy image, which you can imagine
*  you wouldn't want to be like, there's obviously going to be very little human healthy images
*  available. Because, you know, you wouldn't be wanting to take out healthy tissue from a patient
*  anyway. So there weren't many human healthy images that we could play around with. So we weren't able
*  to validate how well the model works with, like if it saw a healthy image, how well it would do.
*  For the one single healthy image that we did use, it actually worked perfectly fine, even though the
*  model was trained mostly on tumor images. That was actually kind of interesting and kind of surprising.
*  It's like, okay, kind of generalizes to this healthy image, which I thought was kind of neat.
*  But, you know, again, those are examples of things that need to be validated more carefully. Again,
*  we used only a subset of types of tumors. So we use these sorts of great,
*  great two and three astrocytomas. But there are various other types of brain tumors that
*  would undergo the same sort of tumor removal surgery and would benefit from the same technology.
*  But we didn't get a chance to image and utilize and train our models on those sorts of images and
*  validate our technology for those sorts of tumors. So, you know, just trying to make it more broad
*  for other types of brain tumors, for example. So there's a lot there that just kind of scaling
*  this up, basically getting more specimens, getting more images, training them on these
*  different images and specimens, validating them, and, you know, just trying to do some sort of
*  like clinical trial at the end. That's going to obviously be necessary if you wanted to actually
*  get this into the clinic. So you would have to, yeah, there's a lot of kind of scaling up of this
*  research that would need to be done before you can, you know, properly validate it and have
*  confidence that this is something that would be safe to use and accurate and, you know, for
*  clinical applications. And then in terms of, yeah, in terms of the actual hardware, you know,
*  there, you know, it's still kind of in the research stage. There is a handhold probe that is,
*  that has been developed, but, you know, there may need to be more work in terms of just ensuring
*  that it's reliable and things like this. And then I guess once that's developed, again, it probably
*  have to go through its own form of clinical validation. And the medical side of things,
*  it can be quite intensive in terms of the sorts of testing that needs to be done in order to
*  validate the technologies, which of course is important because, you know, you're using this,
*  you know, in life and death scenarios. So, you know, you want to make sure it's working properly.
*  So, you know, it would take a while for it to be able to be finally utilized in the clinic. But,
*  you know, the eventual promise is definitely very, very appealing. And, you know, the eventual
*  benefits that it could have in terms of really speeding up the workflow and improving
*  the patient care is really, really exciting. So, yeah. One of the main takeaways for me during my
*  entire PhD has been the importance of data, of high quality data and the focus of data-centric AI.
*  And that's something that I think people haven't been focusing on as much. I think we're now
*  starting to see that become a focus these days, even in the context of trading large language
*  models or some of these other fields. I know that, you know, there have been some recent papers that
*  have talked about the importance of data filtering and large for, you know, trading large language
*  models and things like this. So, I'm really glad to see that sort of focus of high quality data.
*  And that's something that, you know, I've learned from my time as a PhD student and something that
*  I will continue to focus on throughout any of these sorts of ML projects that I will work on.
*  Yeah, I think that's kind of the key takeaway for me. Having the most advanced models is not going
*  to do you any good if you don't have high quality data. My PI, my advisor liked to say garbage in,
*  garbage out. So, you know, that's a common saying that people have. So, that's, I think, a very
*  important point to make, I feel. You have these affiliations with Eleuther and with Stability.
*  Anything you would just tell us about those organizations that may not be obvious from
*  kind of a public viewpoint? Yeah, I mean, my affiliation with Eleuther is just being kind of
*  part of the general research community. And I think it's definitely a very, very, again,
*  a great research community in terms of like, again, focusing on that sort of open, collaborative
*  nature. And I think MedArk took a lot of inspiration from communities like Eleuther AI,
*  some of the other communities, Lyon, ML Collective. There's so many, nowadays there are lots of great
*  open source research communities and all those have really inspired MedArk. And now I think we're
*  seeing that this seems to be like, this is a really promising approach for medical AI research as
*  well. So, yeah, and I'm just really happy to be part of some of these communities and be involved.
*  And yeah, that kind of is the extent of, I guess, my Eleuther AI affiliation. And then in terms of
*  Stability AI, I'm a part-time employee of Stability, and they are basically supporting my work at MedArk
*  and the research that I'm doing there. And yeah, you know, they've been really great support for
*  the community and providing compute to run all these experiments and to support this research.
*  That's been really appreciated. Yeah, they've also supported my PhD as well. So like, they provided a
*  fellowship for my PhD as well. So they were supporting my PhD research as well. So yeah, but
*  yeah, this lots of interesting research has been going on at Stability. And so I'm really
*  excited that I've been part of that. And yeah, I'm excited to, of course, continue the research at
*  MedArk in these directions. I think why Stability is interested in these sorts of,
*  in this area is to, of course, see how these sorts of advances in generative AI that Stability AI
*  is making and other, of course, other companies and other research institutes are making, how these
*  can be applied to medicine. And that's kind of the focus of MedArk is, and the focus of my research
*  is to see how can generative AI be applied to medical applications. Because yeah, I don't
*  think many people realize that that's something that, you know, even worth looking into. It's
*  like, you know, you think like, oh, it's like AI art, how's AI art going to be any useful in
*  medicine? It's like, what's the point of that? But it turns out, you know, these sorts of models
*  can be used for all kinds of interesting applications in medicine. And similarly with
*  language models, it's like, I guess that may be a little bit more kind of a little bit more obvious
*  why that might be useful for medicine, but you know, it's still lots of unexplored opportunities
*  there. So that's kind of what we're focusing on at MedArk and really glad that Stability is
*  supporting me to be able to do that as well and supporting the research at MedArk.
*  You're not returning anything in an exclusive way to Stability, it sounds like.
*  Yeah, that's correct. There isn't anything necessarily exclusive to Stability. And you're
*  just willing to provide their compute resources. And of course, I mean, they're providing this not
*  just to MedArk, but to other academic research projects and yeah, all kinds of research projects.
*  But I think also being part of Stability also enables us to kind of take advantage of some of
*  the research that Stability is actually doing. So there are some like projects that we're working
*  on that is able to take advantage of the stuff that Stability is working on, collaborating with
*  Stability AI researchers. So that is also enabled by being part of Stability. But yeah, apart from
*  that, I mean, it's just kind of a research organization. There's nothing necessarily that
*  Stability is gaining out of this. And again, this is something that Stability has been doing for
*  various different academic research projects. It's possible, of course, that some of the
*  developments that we see in the medical AI field may help out for other potential applications.
*  Have you seen this happen in the past, for example? For example, the original U-net
*  architecture was developed for cell segmentation, actually. That was the original application. And
*  now we're seeing it being used for all kinds of segmentation, but also any sort of image to image
*  thing, any sort of even for diffusion. It's used in the diffusion models all the time.
*  And then another great example is the CLIP model. So actually the CLIP model was originally
*  developed by Stanford for medical AI applications, but it was then scaled up by OpenAI for CLIP. So
*  CLIP was actually, I think the original paper was called CONVERT or something like this. It was
*  actually developed for looking at image text representations of radiology reports and these
*  sorts of data sets. And then I think some researchers at OpenAI discovered that and decided
*  to scale it up. And that's how we got CLIP. So I think there's lots of interesting opportunities
*  in the medical AI space because the research that comes out of that space could be utilized
*  for other applications too. So I think it's kind of that, again, going both ways in terms of the
*  research in generative AI may be useful for medical AI, but it's also possible that the research in
*  medical AI may be useful for more general AI applications as well. So that's the sort of
*  kind of feedback that's going on there that I think is really exciting to potentially explore
*  further. And so that's why I think that maybe some of these organizations like Stability have
*  picked up on that and are willing to support some of this research as well.
*  What do you think is kind of the future of radiology work? Is the stuff that you're developing
*  going to change that in a fundamental way? Is it all just a tool?
*  In the short time, it definitely seems like it's just going to be a tool for various applications.
*  There's so many ways that AI can help in medical applications and even specifically in radiology.
*  There are various questions of how reliable AI systems are currently. And I think we see this,
*  of course, with systems like chat GPT and these sorts of large language models that are known for
*  hallucinating and they have these issues, but they're still extremely useful if you
*  view them as a starting point. And so I think the question is if we can make these systems more
*  reliable. And right now it's unclear if that is, what is the status of that? The sort of current
*  systems, I can see these sort of current systems being used for various applications that still
*  require the doctors to be in the loop. So the sort of human in the loop process. I think that's still
*  going to be extremely valuable. I mean, there have been like the general applications include
*  just like maybe having AI systems provide some sort of diagnosis that the doctors can
*  see that this is a potential diagnosis that the AI provided, for example. And I've seen some papers
*  that have described the sort of combined AI doctor system as actually outperforming even the
*  AIs themselves. So this is something that's possible because the AIs may pick up on certain
*  things and the doctors, based on their years of experience, may pick up on other things as well.
*  And then in addition, I think the AIs could also be, there are various applications for AI to be
*  used in clinical education settings as well. So even using AI to better educate doctors as well
*  is a very interesting scenario that I think will be really promising in terms of, for example,
*  one of the interesting things that we worked on recently was the sort of fine tuning stable
*  diffusion on chest x-rays. So using generative AI tools to generate medical images, and you can use
*  that to, for example, train doctors on certain images or something like this. Maybe there are
*  some images that the doctors are less familiar with. They can utilize these tools to generate
*  some images and use that to help train them better. So there are various applications like that.
*  One application I'm also very interested in how AI can be used would be actually discovering things
*  that doctors didn't know were originally there in images, for example. So that's something that I
*  think is really exciting is that there are actually a lot of interesting biomarkers that are hard for
*  people to actually pick up on, but that information is actually there in the images.
*  So I'm coming from this, like I was working a lot in pathology and my PhD research is
*  microscopy and pathology, applying AI to these applications. So one of the interesting applications
*  that I read about, that there's a lot of research in, is actually picking up on molecular biomarkers
*  from H&E images. So these sorts of molecular signals, like maybe if cells are presenting
*  specific receptors, specific proteins or things like this, you wouldn't think that that kind of
*  information would be available from an image. You think that you have to actually go and do those
*  molecular tests in order to get that information, but the cells show certain different morphology
*  and different shapes and sizes, very minute differences, but those differences are still
*  there that AI systems can pick up on that. So being able to use AI systems to actually
*  pick up on information that regular humans cannot, that I think is also a very interesting
*  application. And again, that's something that the AI systems can provide that information to
*  doctors and they can use that for clinical decision making. So overall, there's lots of
*  interesting applications, but again, the question comes down to how reliable are these systems?
*  They can be used to supplement what's already going on and kind of maybe alleviate the burden
*  of existing doctors, but if the systems are not reliable enough, I don't see them fully replacing
*  the doctors. But it depends on how this research goes and we'll see how the field goes. And it's
*  very hard to predict the developments. I mean, I don't think any of us would have been able to
*  predict where we would be now five years ago. So it's very hard to predict these developments,
*  but based on what I've seen right now, this is where I see things going in the future.
*  But I wonder if there was any sort of interesting elements to your early childhood education
*  that maybe were like not scalable or not very repeatable that you think
*  AI could start to make more broadly available to more kids.
*  I mean, I think part of it is just like, yeah, a lot of why I was able to do what I was able to do
*  is of course the availability of resources and online. I think there's a lot of great
*  online resources. Like I don't think this would have been possible 20, 30 years ago.
*  And I think also, yeah, it's part of it is like people learn at different rates.
*  And I think AI, that's something that AI could definitely help with is because, yeah, like going
*  back to what's scalable and what's not scalable is that there's this sort of assumption that
*  everyone's learning at the same rate. That's kind of the implicit assumption of most education
*  systems. And this is something that has caused a lot of problem for me, is the idea of like,
*  I learn at a faster rate compared to most people. And then of course there are people who learn
*  maybe at a slower rate than other people. So it's like there are people learning at different rates
*  and giving the same homogenous education for everyone doesn't make much sense.
*  So I think that's something where AI could help with is trying to provide more personalized
*  education for people, providing this sort of personalized education programs that
*  meets them at the level that they are at and allows them to progress at the rate that they
*  are comfortable with, whether or not it's a slow rate or at a fast rate. It doesn't, it shouldn't
*  matter. And so that's kind of, in my case, I had to do a lot of, I guess, trying to get through
*  the system to be able to go at the rate that I was interested in going at and was comfortable
*  with going at, so that I wasn't bored out of my mind, I guess. And so that was, I think that
*  there's definitely some interesting potential for AI to help with that. But I also think a lot of
*  it has to do with how people are, how much people are willing to implement those sorts of systems.
*  It feels like that's again, kind of a complete overhaul of the education system. It's like
*  this idea of like, oh, personalized education, you mean we're not going to just have regular
*  classrooms or how does that work or, there's lots of these sorts of things that I think there's also
*  that kind of societal aspect that is definitely hard to solve. So there's a lot of, again, lots
*  of interesting AI applications. And I mean, this is true for any field. There's like, there could
*  be lots of interesting AI applications, but the sort of societal reaction and how society implements
*  it, that's itself kind of a different question and something that's also worth thinking about and
*  worth trying to solve as well. So Neuralink just got initial approval for a FDA approval for a
*  human trial. Let's imagine a future state where they've gone through all that, they're approved
*  and a million people have a Neuralink device implanted. Would you be interested in getting
*  one at that point? It's a good question. In theory, that sounds like I would love to get one, but I
*  would be more concerned about the security issues. So I guess it would, assuming security is not an
*  issue, I would definitely get one. But I think it has a lot to do with, I don't want people hacking
*  my brain. So that's definitely an important concern. But yeah, I guess as part of your
*  hypothetical scenario, if that's not a concern, security, I would love the idea of being able to
*  connect to, have these sorts of brain and computer interfaces, being able to augment myself in that
*  way. That sounds amazing. So I would definitely do that if that was in the hypothetical scenario.
*  So yes, but of course, in reality, it's a little bit more messy than that. So we'll see how this
*  technology progresses. But yeah, I mean, it's still very interesting and I look forward to seeing how
*  all that kind of progresses. What are your big hopes for and fears for society at large as AI
*  permeates society at large and begins to touch everything?
*  Yeah, I guess let's start with fears. With the types of fears, of course, I think my fear in terms
*  of AI in society is just maybe how much polarized our society may become because of AI. That seems
*  to be a big concern. The concern of biases as well being made worse because of AI technology.
*  There's a lot of concerns like this and just overall concerns of the reliability of AI tools
*  and what kinds of dangerous circumstances that could lead to. In terms of what I'm excited about
*  AI, I think I'm really excited. Well, of course, as you can imagine, I'd be very excited about
*  is the medical applications of AI and using AI to improve patient care. I'm really excited about all
*  kinds of applications there. Of course, I'm excited about using AI for education, being able
*  to learn whatever we want to learn. I think AI is going to be extremely valuable for that.
*  Yeah, I mean, I think AI can be used in various different ways. I think there may be concerns of
*  AI being used for polarization of society, but I also think that AI could be used for bringing
*  society together and being able to connect with each other. I mean, there's so many ways that it
*  could be able to... I mean, it's happening even now with very primitive forms of AI, things like
*  we have social networks, we have things like, for example, translation that's able to connect
*  us with people from other cultures. There's so many forms of even primitive AI tools that are
*  being used nowadays that are helping us to connect with other people. I'm hoping that that kind of
*  trend continues even with the current AI tools. I'm also really interested in how AI will help
*  enable people's creativity. I think we're starting to see this already with some of these
*  AI art tools. I think there's lots of interesting creative applications of AI and just being able
*  to bring ideas that people have into the real world with AI. I think that's really exciting.
*  Of course, maybe that will soon happen with mind reading and things like this that will then
*  immediately take it from the idea stage to something that's physical, something that's
*  happening right in front of you. But yeah, I'm really excited about just how AI can
*  enable people to bring their ideas and actually augment their creativity.
*  So yeah, I think there's a lot of really interesting applications, but yeah, it can go
*  both ways. It's a very nuanced topic in terms of both the benefits and the opportunities of AI,
*  as well as the risks and concerns. So,
*  Tanishk, Matthew, Abraham, happy 20th birthday in just a few days.
*  Thank you for being part of the cognitive revolution.
*  Thank you for having me. It's been really fun.
*  Amnaki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button.
*  I believe in Amnaki so much that I invested in it, and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
