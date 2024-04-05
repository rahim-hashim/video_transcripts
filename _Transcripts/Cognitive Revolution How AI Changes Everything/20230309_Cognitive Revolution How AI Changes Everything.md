---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 4880s
Video Keywords: []
Video Views: 1046
Video Rating: None
---

# The AI Multimodal Revolution with Junnan Li and Dongxu Li of BLIP & BLIP2
**Cognitive Revolution "How AI Changes Everything":** [March 09, 2023](https://www.youtube.com/watch?v=zTr5vDjEy2I)
*  But in a way, it's not that dissimilar from how we see, right?
*  Like we have our eyes, the eyes kind of take in raw light and turn that into a signal.
*  And that signal goes through the nerve and finally gets back to the back of the brain.
*  And by that point, it's not that interpretable either, right?
*  It doesn't necessarily correspond to language.
*  But then there's some further connector that like turns that visual data into something
*  that I can understand as language or at least understand and then articulate as language.
*  So it feels like there is something kind of analogous taking shape in the AI world.
*  Imagine you are human, you grow up learning only knowledge.
*  And now one day you open your eyes, you don't really know how to interpret what you see.
*  So that's what we are going to do here to kind of build this bridge between these two modalities.
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers, entrepreneurs,
*  and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz joined by my co-host Eric Thornburg.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work,
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  Today's episode was a fun one for me.
*  Researchers Junan Li and Dongshu Li, both of Salesforce Research's Singapore office,
*  have co-authored some of the most practically useful computer vision papers of the last year.
*  As recently as January 2021, the challenge of using AI to interpret what is going on in a photograph was considered to be nowhere near solved.
*  But just a year later, Junan and Dongshu changed all that by publishing and open sourcing Blip,
*  a family of pre-trained models that delivered state-of-the-art performance on image captioning, visual question answering, and image text matching.
*  For Waymark, my company, Blip was a godsend.
*  Suddenly, we had a reliable way to understand the contents of users' images, allowing us to make useful image suggestions for the very first time.
*  This was something we had worked toward for years.
*  Unusually in today's AI landscape, Blip has held the title of Best Image Captioner for over a year,
*  ultimately becoming the 18th most cited AI paper of 2022.
*  And more recently, just as worthy rivals to Blip started to come online, Junan and Dongshu changed the game again with Blip 2.
*  As an aside, for a funny moment in Cognitive Revolution history, you can listen back to episode 1,
*  in which Suhail tells me about the release of Blip 2 live on the show, forcing me to clear my calendar for the rest of the afternoon to go check it out.
*  Now, Blip 2 uses a different approach, which I think may ultimately prove even more influential.
*  Rather than training a large model end-to-end, this time they trained a much smaller model that connects a frozen vision model to a frozen language model.
*  This strategy has several benefits.
*  First, because it injects semantic visual information into the language model's latent space,
*  you can now have an open-ended dialogue about an image in which the language model shows remarkably detailed and nuanced understanding.
*  Second, because the connector model is so much smaller, training time and cost are dramatically reduced.
*  Blip 2 was trained on just a single A100 machine in less than 10 days,
*  making it easy to upgrade the system as new and more powerful language models become available.
*  You can even use your own fine-tuned language models as well.
*  Small connector models like Blip 2 show just how much potential remains to be drawn out of today's large language models,
*  and seem likely to play an important role in the great implementation of multimodal AI across society.
*  One note for listeners, both Junan and Dongshu are native Chinese speakers,
*  and while both are perfectly fluent in English, audience members listening at 2x speed might benefit from watching this episode on YouTube,
*  where we've also included subtitles for your convenience.
*  Now enjoy our conversation with Junan Li and Dongshu Li.
*  Junan Li and Dongshu Li, welcome to the Cognitive Revolution.
*  Thanks. Excited to be here.
*  Thanks for having us.
*  So you guys have really done some outstanding work in the subdomain of AI known as computer vision.
*  I guess I would even ask you guys right off the bat, like, do you think of yourselves as computer vision specialists,
*  or now with Blip 2 and your work kind of branching into multimodal and models being involved,
*  do you think of yourselves even as kind of beyond computer vision?
*  I'd love to hear how you think about where you fit into the broader AI landscape.
*  Yeah, I think with how AI has been developing, I think the boundary between different fields is kind of blurring out.
*  So I think both Dongshu and I, we started as computer vision people during our PhD,
*  but gradually, like, it doesn't require too many expertise really to move to another domain.
*  But that's why we started to explore other language domain and also other domains,
*  and try to see how can we also be involved to build better AI models.
*  You know, he's just trying to be humble if he actually has a lot of expertise.
*  But there is definitely this kind of great convergence phenomenon.
*  Transformers kind of increasingly working for everything.
*  It is amazing to see how quickly people can move from what used to be one subfield to another
*  and just how much the same techniques are really starting to work across these domains.
*  So I find that super fascinating.
*  You guys have also done something that is pretty rare in today's AI landscape,
*  which is that you put out a model almost a year ago now, right?
*  If not, maybe a full year ago was the original release of Blip.
*  And that continued to be state of the art or really neck and neck
*  with one or two other models for state of the art captioning, image captioning model,
*  all the way up until you released your most recent paper, which is Blip 2,
*  which obviously supersedes Blip 1 and I think now is safe to say is kind of the state of the art,
*  both captioning model, question answering model as it pertains to images,
*  and really starting to unlock like longer dialogues and true understanding of images
*  beyond kind of bite-sized captions that we've seen in the past.
*  So I think that's really an amazing accomplishment in today's AI world.
*  We don't see too many things that can hold the top of the leaderboard for a year.
*  Typically, it's more like a month.
*  Sometimes it's more like a week.
*  But you guys put something out there that really in today's AI context, a year I would call enduring work.
*  So I want to compliment you on that.
*  But I also want to dig into both kind of the original Blip and Blip 2 and understand like,
*  how you guys got into these projects, how they work, how you train them.
*  And we really do want to go pretty deep on that.
*  So maybe let's start with the original Blip.
*  Tell us about kind of the origin of that project and how it all came together.
*  Sure, sure. Thanks for the compliment, by the way.
*  So I think actually before Blip, we have a previous one or two paper in this VJLounge domain.
*  So for me, actually, my first paper is this LBEP.
*  I'm not sure if you have heard, but it's also been accepted at New Reaps.
*  And that is kind of when we started to explore this field and feel like there's something we can do here.
*  So in LBEP, it's kind of at the same time as Clip from Open here.
*  We published LBEP shortly after that.
*  And in that paper, we found out that the idea was that we want to build this kind of multi-model encoder that can understand both image and text.
*  So Clip is kind of a unimodal encoder.
*  You have the image encoder, you have the text encoder, and you can build a similarity.
*  And what we found is that we can build on top of that kind of contrasted learning approach to have another kind of this fusion encoder.
*  We encode both image and text together.
*  We find that achieves quite good performance on some parts that require understanding of both image and text because of this fusion mechanism.
*  So that's actually where we started.
*  And then we found out that this kind of encoder architecture is good at some understanding parts,
*  but it's not really that good at generation parts, in particular text generation parts,
*  captioning or VQA that requires an open-ended generation.
*  So in the paper, actually, the architecture, we heavily inherit our LBEP architecture.
*  We made some changes such that the encoder can also function as a decoder.
*  So we propose what we call a mixture of encoder and decoder model, which basically like a single model with shared parameter by the switch from either encoder or decoder.
*  So that's where the architecture kind of comes from.
*  And then we also find out that in order to train this model, you need a lot of data from this web domain, like image text pairs.
*  And for previous methods like CLIP, you just want to do contrasted learning, you want to learn encoder, then it's fine that you have a lot of noise.
*  If you just want to do contrasted learning, the noise is fine most of the time.
*  But if you want to do image captioning, this noise can really be quite harmful because this language model is more like a finer grain version than the contrasted model.
*  So that's where another kind of contribution of our LBEP was that we kind of boost-dragged this data set.
*  So that it has synthetic generated captions.
*  And also we use this filter to remove the noisy captions.
*  And that's basically these two pieces, the architecture perspective and the data set perspective together makes LBEP work.
*  You filtered or did you, how did you remove the noise from the data set?
*  Some of the captions that actually describe the image have a high similarity score with their corresponding text encoding.
*  But then it's just such a big data set. There's so much noise in there.
*  Got a lot of things that are just like, what an awesome day.
*  And that doesn't really line up with what's in the image.
*  So that can add noise to the system.
*  It sounds like in your case to create a captioner, this was working against you.
*  So did you just go through the giant data set and just kind of filter out things with low similarity score and work from that?
*  Yeah, exactly. Like what you described, we just go through all the examples and filter out those that are not aligned with the image.
*  And I think it's this perfect point that in some cases that noise would be good.
*  Like I mentioned, in contrast to learning stage, noise would be good because really you are just learning one single vector.
*  You are not really trying to generate the text.
*  But in the model captioning space, let's say you give an image you want to generate text,
*  if the text is totally irrelevant to the image, then the model could learn something that we are not trying to learn.
*  It doesn't capture anything from the image. It tries to hallucinate some stuff out of the...
*  Basically, there's no context. So I think that's something we try to avoid.
*  Remind me, how big is the original blip model?
*  It's like one to two gigabytes downloaded, if I recall correctly. It's not huge, but it's...
*  So, yeah, tell me about the size and kind of the training dynamics.
*  I want to contrast that ultimately to the blip2 successor.
*  Yeah, I think that's actually a beauty part about blip2 is that if you compare the number of trainable parameters,
*  so this trainable meaning that you are using vibration to optimize the gradient during this pre-train.
*  Actually, blip is larger than blip2 in that trainable parameter, the count for that.
*  Blip has a few hundred meanings, but blip2 only has less than 200 meanings.
*  So the reason is, I think in blip, we are training everything end-to-end,
*  including this vision encoder, this language model, everything we train end-to-end.
*  But in blip2, we have this frozen image encoder, which we don't update at all.
*  And then we have this frozen, this large language model, which is very large.
*  It can be a few billion per meter.
*  But because we keep it frozen during pre-training, it actually impairs very little computation cost.
*  So if you just compare how much time and GPU we need to take during this pre-training,
*  blip2 is actually cheaper than blip, because we use this already off the shelf,
*  all the available models that are built by other amazing research teams.
*  On the original blip, what are you optimizing for there?
*  Are you just optimizing for generating the exact caption, like token by token?
*  Or is there some more abstracted or semantic loss function that you're optimizing against?
*  So actually, this blip is the inheritor of this LBAC paper.
*  So our optimization function, actually, if you look at LBAC blip and blip2,
*  we have kind of the foundational laws, which are very similar.
*  So there are basically three laws that we use.
*  One is contrastive learning.
*  It's the same as what clip used to learn better adaptations and align this image and text with others.
*  Can you unpack the contrastive learning a little bit better?
*  I think most people will be familiar with clip,
*  and I think they'll understand it largely as kind of the thing that somehow,
*  someway, stable diffusion somehow is downstream of, and so it's important.
*  I don't think people have a great sense in general of what exactly the insight there was that created that possibility.
*  So give us a little bit more on that before we go on to the next two papers.
*  Sure. So this term contrastive learning actually already is before clip is from online computer vision field.
*  I would say that. So basically, the idea is that you want to learn some kind of adaptations for your data,
*  such that if your data is similar, like in semantic meanings, they should have similar adaptations.
*  And what we consider this for image and text domain,
*  what it does is that you have these positive pairs.
*  So-called positive pairs is what you're collecting from the web is you have an image and text and they are correlated.
*  And you want to train the model such that their adaptations for this positive pair is more similar to each other compared to the similarity for negative pairs.
*  So this negative pairs are basically random sample image and text pair that don't correlate to each other.
*  And so what this loss does is it trains this image and text encoder.
*  They don't interact with each other until the last stage.
*  So they will extract this image and text feature individually.
*  That's why we also call them like uni-model encoders, because they don't interact with each other.
*  After you extract the features, the final stage is you compute their similarity.
*  So that's where they interact. And this very simple mechanism, you just use the dot product,
*  which measures the cosine similarity of this normalized invariance.
*  And you try to maximize the invariance, the similarity of the invariance from this positive pair.
*  So this kind of contrastive learning works. It's quite a simple mechanism.
*  And in the end, what you get is you get this very good image and text encoder that can produce good representations that represent what their semantic meanings are.
*  That's why the VIT of Clib and text encoder of Clib has been really successful applied to different data tasks, because it captured the semantic meanings of those data.
*  Cool. Let's go back to the history then.
*  Yeah, so the first loss is this contrastive loss that gives you a good uni-model encoder.
*  But then if you want to do more finer grained interaction between the image and text, you'll need more than just a dot product.
*  You'll need some parameterized mechanism to interact.
*  So that's where we have this cross-attention, where you have the text encoder that can cross-attend to the image encoder.
*  So it's kind of like consider T5 encoder-decoder architecture, where the encoder is your VIT and your decoder is your text model.
*  So in the term, when we consider image captioning loss, basically this text encoder will cross-attend to the image encoder and generate the text tokens.
*  So that's basically our second loss, which is the standard image captioning loss.
*  It's just a language model loss, but conditioned on the image.
*  And our third loss is what we call image text matching loss.
*  So the purpose of this loss is that we want to learn even finer grained similarity or kind of matching between the image and text.
*  Through this cross-attention mechanism.
*  So you can't really expect a single vector to capture all the finer grained details of one image, right?
*  Because the image is worth something worth, so there are too many ways to describe this image.
*  So this single vector is very concentrated and good for imitation.
*  But if you really want to find a grain, you need this cross-attention.
*  So for this image text matching loss is kind of a binary classification task where we give the model an image and text pair.
*  And we ask the model through this cross-attention after this computation to tell me whether this is a matched pair or not matched pair.
*  So by doing this, we can further enhance this alignment between these two modalities.
*  So this is basically what the image text matching loss does.
*  And in our experiment, we find that these three loss complement each other,
*  meaning that they have this multitask learning objective will enhance the final performance of each individual loss and objective.
*  So this through different experiment, that's why we fix those three loss as kind of the standard loss losing.
*  And I think many other papers also kind of now adopt this three loss or something similar.
*  One of the things that I think Blip has notably done better than any other model that I've tried is handling logos.
*  Like can almost read the logos. A lot of times it like kind of fudges the words from the logo.
*  So help us understand that. Like as a you know, just as a user, I see this really interesting behavior.
*  Other captioning models really struggle with logos. You may know that.
*  Blip does quite well. How did you manage to do that?
*  Was that a matter of like the training data or was there is there a technical reason that that happens?
*  And then also when I do see something, if it's like the Coca-Cola logo, it'll just know, OK, that's the Salesforce logo.
*  It's going to know that's the Salesforce logo.
*  But when I have these long tail small business logos, it's like probably never seen them before.
*  I imagine most of them are not in the training set.
*  And then you'll see these things where it might be like Torenberg plumbing.
*  And instead, it'll say like Torrenstein plumbing, right?
*  It'll be like almost the right name, but it'll kind of just flip it a little bit on like the last couple letters and the last token.
*  And I've always kind of wondered, like, what is happening there?
*  Where it clearly can sort of recognize the letters, but it's not doing like exactly an OCR type mechanism, obviously.
*  And so I'm always kind of confused as to how it ends up just being a little bit off in those scenarios.
*  But I'd love to understand that.
*  Yeah, I think that's quite a fascinating phenomenon.
*  I really didn't really observe this before.
*  I think in terms of why BLEAP can understand logos, I would say it's mostly from the training data that we use.
*  And we are one of the first to scale up to this AI and data set.
*  Yeah, I think we once after 9 released this 400 million data set, we started to use it to train the captioning model.
*  So there are a lot of logos in that data.
*  So I would imagine BLEAP can learn such information, web-scale data.
*  And of course, this data is quite noisy.
*  So it's likely that some spelling error can lead to a wrong recognition of the logo.
*  But I would still say that it is not a perfect OCR model because it's not really designed to do OCR.
*  The VIT itself, even though powerful, it's not really at least compared to the best OCR architecture, it's not the same mechanism.
*  So OCR has this detect first and then you really zoom in to each individual letter and you recognize.
*  But VIT is more like a holistic view of the image and you're trying to recognize maybe the most salient part of the text.
*  So that's why the text is small.
*  It may fail.
*  And another reason like you mentioned is if it's not a common name that appears frequently in training data, the model may not really know that name.
*  So it lacks the prior information to spell the correct name.
*  And I'm not sure, maybe BLEAP 2 will be better at this because we are using an order language model that has more knowledge about words.
*  So maybe it knows more companies.
*  So there's stronger prior to give you the correct information.
*  Yeah, I mean, I want to add something to that.
*  Like, I think that's the emerging advantage of this contrastive learning in the context of multi-modal data.
*  If you look at some of the earlier models, I mean, before Alibi and the GLEAP,
*  many models are actually using some off-the-shelf detectors to provide object level labels.
*  But because of the usage of these object detectors, they won't be able to necessarily take into account this logo information.
*  Because if you look at these detectors, they usually don't turn to detect the logos.
*  Like the boxes, tables, and not the logos.
*  I think one emerging property since ever the contrastive learning was introduced by BLEAP and LBF is that you don't need these off-the-shelf detectors anymore.
*  These contrastive laws really very well align the captions, each text tokens in the caption to the corresponding region in the image.
*  And because of that, this text, if you see some text in the logo, that really aligns to the text appearing in the caption.
*  So that gives kind of the alignment on this logo thing, the text words.
*  And I think there is no OCR loss for that.
*  But we also have some other team members who try to adapt BLEAP to the OCR context, which turns out to work pretty well.
*  And that really demonstrates this foundation model is critical to serve for general purposes for the model understanding without too much task-specific designs or tasks specific.
*  So it's just a little bit adjustment.
*  This foundation model could be used for different scenarios, which is quite nice.
*  So with the original BLEAP, you said it's end-to-end training.
*  Is it correct to say that there is no knowledge before that end-to-end training?
*  Like the only text that BLEAP ever has seen is the image captions that are associated with the images.
*  There's no other text pre-training or anything like that that's being built on top of.
*  Do I have that right?
*  Actually, we do use a pre-trained BERT model to initialize this text encoder.
*  So of course, BERT is not considered to be the best language model.
*  But still, if you consider its size, it has some decent text understanding capabilities.
*  So that allows us to initialize with a model that already knows text.
*  Then we start to train it on this caption to enhance its capability.
*  What was the total training time like for the original BLEAP model?
*  Yeah, so if I recall correctly, we used 32, 800 GPUs.
*  And the training takes about, for the largest model, it takes about a week to finish.
*  I was under the impression it was even longer.
*  So that's actually pretty reasonably efficient.
*  How many cycles did you guys go through in the process of doing that research?
*  Like, did you run that week-long training process five times, 50 times, 500 times?
*  We all see the one end product, but how many earlier versions of it were there that ultimately got tossed out?
*  Yeah, so actually, during the research, we really started with not the largest model
*  and relatively smaller size and smaller training data.
*  So we can iterate faster.
*  Maybe within a few days, we know how the training is going and we can adjust.
*  And because we already have this LBEP work, it kind of gave us a solid, this per-training loss.
*  We didn't really make any adjustments about the losses because we are quite certain it would work well.
*  And we made some adjustments to the model architecture because we have this one model that can do both decoder and encoder.
*  So we do some ablations on that.
*  I think in total, maybe less than 100 trials, maybe 10 or 20 trials until we finalized
*  the final model architecture and the per-training strategy.
*  What would you say were the biggest things that you learned or adjusted during that process?
*  Is it like a sort of learning rate schedule or other hyperparameters or something else?
*  Yeah, actually, we didn't really have a single thing that gave us a significant boost.
*  So I would say mostly the model is robust with different changes.
*  We do observe some kind of instability in training if we increase the learning rate too much.
*  So the loss may go to none sometimes for mysterious reasons.
*  So that's why we decided to kind of keep the learning rate a bit lower.
*  And in terms of other hyperparameters, like the batch size, we just feed in the largest batch size
*  we can feed within the 32 GPUs. And also the data and the per-training loss, we didn't really make
*  too much changes. We like to tweak the architecture a little bit, but it's more like there is a trade-off
*  between your efficiency and your performance and we find a sweet point that gives us the best
*  performance while still being efficient. So it's 32 GPUs and like seven days.
*  So that is essentially whatever 200-ish GPU days. That's a significant amount of compute.
*  Yeah, just to jump in. So like if there are I think tons of models that
*  transfer way longer hours than that. So even some of the earlier models,
*  although they are not as flexible, they require way longer hours. I think that also shows that
*  the architecture is quite efficient to capture this model.
*  These 200 GPU days is indeed a lot.
*  If you just think about it, it's awesome. If you look at KEEP and Align, especially these ones from Google,
*  they maybe transfer like tens of thousands of GPU hours, I would say, at least. And I think
*  at least tens of times more running data than BLEEP. While saying that, BLEEP is still able to
*  achieve comparable, I would say in most cases, even better performance. I think that really
*  demonstrates that it's important to make good choices on architecture and training strategies
*  in addition to proper scaling in terms of data sets.
*  I don't know if you guys know the answer to this question, but I looked it up just today.
*  How, if you don't know, I'd love to hear what you would guess is the number of times that the
*  original BLEEP model has been downloaded from Hugging Face in the last month, just the last month.
*  I'm not too sure. Because I think BLEEP was uploaded to Transformer not long ago,
*  right? Transformer, the Hugging Face team, I think they're great. I think half a year or maybe less.
*  I would guess 1,000, maybe 3,000, I would say. From just the last month, mind you, just under
*  20,000 downloads of the original. Which model was that? Action model?
*  That's a good question. Let me see. Yeah, I just want to say that sometimes also take a look at
*  the statistics and we feel quite excited about it. We also learn quite a lot from how people
*  use it, how people are using it. We see a lot of different application scenarios that we
*  wasn't actually expecting, but it was amazing. And yeah, it is really appreciated the community
*  effort and feedback. I think that really also helped us a lot in developing a better idea of
*  what the model is doing and where we are going to in the future.
*  Just to answer your question, it is the BLEEP image captioning base model that has been downloaded
*  exactly, according to Hugging Face, 18,976 times in the last month.
*  That's amazing. I'd love to hear some of those stories of unexpected use cases.
*  And maybe you could also just tell, give us like a little bit of guidelines for anyone who's
*  thinking, okay, how do I get in on this action? I would say, by the way, too, for Waymark, we do
*  not fine tune the model. We just use the base with the kind of web scale data that you trained it on.
*  Base works really well for us. I'd love to help the audience understand, like, what would it take
*  for them to do a fine tuning in terms of data set, any gotchas that you guys have observed,
*  compute resources that they would need to go into that?
*  Yeah, I think that's definitely something I also want to say is that if you want to fine tune BLEEP,
*  we have the support in our NavVis library. And so we spent a lot of time and effort last year
*  to build this library that really offers you not only the very convenient inference using our models,
*  but also training and benchmarking. So we set up this framework where you can do training of our
*  machine models, fine tune them quite easily using your custom data set. So all you need to do is
*  maybe you prepare the data set in a certain format, and then you write some configuration files.
*  I follow the default ones, but if you want to change some hyperparameters, you can also override
*  them. And then you call our trainer master to train the model. And in terms of compute, I think
*  it depends. Of course, you have a lot of GPUs of that grade, but if not, it takes longer to train.
*  But for the base model, one or two GPUs can still run the training. It just may take longer. You
*  need to do some grading and stuff. And I think any size of data set would work. Of course,
*  if you have only tens or hundreds of captions, maybe I'm not sure how much effect it will have,
*  but I say if I have hundreds of captions, I will say that's worth a try to fine tune.
*  So that's kind of the strategy that I would suggest to do the BLEEP fine tuning.
*  And for BLEEP2, we also provide this fine tuning in the same library. But that would
*  make it require a bit more computing resource because we use these large-range models.
*  But even if we keep them frozen, I think for our smallest, this OPT 2.7 billion,
*  you still need a decent amount of GPU memory. I think a V100 should be enough to run this
*  fine tuning using the smallest BLEEP2 model that we provide. But for BLEEP2, I think most of the
*  time you don't really need fine tuning because it's quite generalizable to different scenarios.
*  I've seen several use cases for using this captioning. Last year we saw this quite
*  interesting use case where they generate captions for these Pokemon images and fine
*  tune a stable diffusion to generate the Pokemon based on the text. So that's one interesting use
*  case I've seen before. And recently I find there's another demo that uses captions to do this image
*  search. So that's also something we have been exploring is these texts are kind of a
*  concentrated representation of your image and it's human-interpretable. And if you just translate
*  every image to text, the amount of information is concentrated to these very small text tokens.
*  They occupy a very small space compared to the original image. And you can use all these existing
*  techniques like sentence invariance to do very fast similarity search across a wide database.
*  And that gives you an alternative way to do this image search and also even image to text search.
*  If I were to add something to how you want to use the Blip captioning model, I would say first I
*  strongly recommend to take a look at the Blip2 model. We have tried that one in some of our
*  recent experiments and we found that the captions from Blip2
*  significantly better than the Blip. What's happening there, I think it also depends kind of
*  on your use case. For Blip, the captioning model released there was fine tuned on Coco caption.
*  And the effect of that, you kind of observe that the description sometimes tends to be a little bit
*  generic in the sense that it kind of loses the very specific namings kind of stuff.
*  If you look at the Blip2, we have multiple versions of the captioning model released.
*  Some of them are just retuned on the Lyon and the other web data set. And if you use that model,
*  that actually gives you very concrete and, I would say, customized the namings of the object.
*  It can recognize, for example, the car makes, all these logos and kind of stuff, which could
*  provide more useful information if you want to have a really finer ground of information
*  there. And really try the web retuned Blip2 version first before you actually go into the
*  fine tuning phase, which is more expensive. And usually, I would say the Blip2 retuned version
*  is probably strong enough for a lot of this application.
*  You kind of anticipated another question I had with the car makes. So I'm in Detroit, Michigan.
*  The auto industry here is in our blood. One of the challenges that car makers have a lot of times
*  is identifying their cars down to the model. And then they've got the trim, which is the specific
*  package that they have. So do you think it would be, and they have lots of data, right?
*  Plenty of shots of all these cars. Do you think it's feasible to get to the point if you had a
*  significant scale data set where you could get accurate down to the model of the car and even
*  the details of the car? Have you seen people push the performance to that very high level in a narrow
*  range with Blip? I think it's definitely possible if you have good enough and large data set.
*  I don't see any reason that you cannot do it. I think currently in terms of more like research
*  perspective, we don't really have access to those finer-grained data set. But we are trying to
*  improve the tool on certain domains that could be more widely applicable. Like Doshi mentioned,
*  we try to improve our OCR, we try to improve some other capabilities by specific tuning on
*  the individual domains. So I would say that's definitely a good way to improve the performance
*  on specific downstream tasks. Cool. Well, let's, I mean, we've kind of gone back and forth a little
*  bit between Blip and Blip2. And it's funny because I'm just such a Blip stan that I want to talk
*  about it from all these different angles. But your new thing is Blip2. And that has superseded,
*  as you said, even the original as more general and has this, I think the most fascinating part
*  about it is the fact that it uses and really connects these pre-trained vision or image and
*  then pre-trained language models and kind of helps them to work together. My gut says that this is going
*  to be a big trend, right? Because we're seeing the proliferation of the language models and
*  as well as the image models, but especially language models are really going wild right now.
*  And yet, the 200 days, as much as that's not the biggest thing that's ever been done,
*  it's prohibitive for most projects, right? Most people cannot get to that if only because the
*  cycle time is just going to be too slow and they just don't have the calendar time to figure all
*  that out, right? That's a lot of research. Now, Blip2 also a lot of research, but the training time,
*  because it's a connector model, because it's so many fewer parameters, I believe is down to
*  10 days on a single machine. And I assume that could be parallelized down to even shorter
*  run times. So I really want to unpack a little bit this connector model. Tell us,
*  where did the idea for the connection style model come from? I really want to get your
*  vision for what that's going to look like over the next couple of years.
*  Yeah, I think what you mentioned is a very insightful point. And that's something actually
*  we try to push in the Blip2 paper, because initially we find that there's all this amazing
*  vision models, right? You have people just dedicated to pre-training better vision models
*  with self-supervised learning or contrasting learning. And you have another group of NLP
*  researchers trying to push the boundary of these language models, right? You have instruction
*  tuning and all these GPT style models. But for vision-oriented domain, people are still
*  doing pre-training from scratch. So that's kind of puzzling for me. That is why can't you just bring
*  the available progress together and you do some kind of connection that can have a very flexible
*  way to combine different models and efficient ways so that you can harvest from this progress from
*  the individual field. So that's kind of our motivation. I think in terms of the connector
*  model itself, the architecture, we are heavily inspired from a few previous work because we use
*  this kind of curie technique to extract features. We have this cross-attention. So a part is inherited
*  from Blip's previous architecture. We also inspired from the data, which is kind of the first
*  model that uses curie, one of the first to use curie to extract features. And also Flamingo is
*  one of the previous work that also uses this kind of curie mechanism. But I think what we find
*  different is not really the architecture itself. So this connector model, there are different ways
*  to build it. I think we choose one of the most efficient ways so that you don't need to change
*  anything about the language model. You just plug in as kind of prompt tuning. But I would like to
*  highlight that the reason we make it work is because of our pre-training strategy.
*  And this is really something unique from Blip to I think because we have this two-stage pre-training
*  strategy. So what we did is that we first connect this connector to the vision model
*  and do pre-training so that this connector is very well aligned with the vision model. So we
*  can understand the vision information very well in terms of how the text can correlate to the
*  image features. And then only after this stage, we plug in the language model and adapt this
*  connector so that it can work as a bridge between this vision model and language model.
*  And what we find in our paper is that if you remove the first stage, you just do a connection
*  between these two models and you do this kind of image captioning loss, then the performance
*  becomes much, much worse. And there will be a catastrophic forgetting, which was widely observed
*  in previous papers like Domingo that just uses this kind of generation loss of the start. So I
*  think the reason is that we need this connector to have a good understanding first before it learns
*  how to teach the language model to generate. Because these language models are really large,
*  they are prone to overfitting, and they don't really have any understanding about the image.
*  So that's why this pre-training strategy, I would say, is the most useful technique that we try to
*  propose. And this is also applicable to other multi-modal domains. You just need this connector,
*  you connect to the first module first, you do some pre-training, then you connect to the second
*  module and you do some pre-training. I think that's quite a generic way to do it. And we do hope that
*  this can be applicable to other domains and power other applications.
*  So one of the things I think is most fascinating about it is your connector model, which really,
*  I mean, blip2 when you use it is an ensemble, right? You have the image part, which is frozen,
*  you have language part frozen, then you have the connection in the middle, which is what you've
*  trained. It is predicting embeddings that get injected directly into the language model,
*  correct? It's bypassing the text encoding and just going straight to the embedded
*  text layer of the language model. So that in and of itself is kind of like an eye-opening thing for me.
*  It also creates some discomfort for me in the sense that obviously in February of 2023,
*  I don't think we're facing imminent danger from models like blip2. But I sort of extrapolate this
*  trend out a little bit and I start to think, boy, you could really connect a lot of different sensors
*  to language models in this way. And then you could really start to cobble together,
*  not just let's say bimodal, but like a truly multimodal systems. And those can start to do
*  all kinds of things. But what is a little bit concerning to me is the lack of understanding
*  of exactly what is being injected into the language model. Like how is this understanding
*  happening? It becomes ultimately pretty inscrutable. So I wonder what you think about that.
*  And also was curious about whether you have any way to figure out if those
*  embeddings that it is predicting are like, can you backport those to text? Is there a way to sort of
*  understand in a human legible way what exactly is being injected into the language model?
*  Yeah, yeah. That's a great question. I think this kind of injecting embeddings has been there for a
*  while from this prompt tuning kind of technique. In NLP, you have this soft prompt, which are
*  basically embeddings. And you learn those prompts and you prepare them to your text input and give
*  this to a language model. And somehow they can guide the language model to predict certain things
*  like you can fine tune the prompts to guide the language model for certain downstream tasks.
*  And they can give you better performance. And people have tried to interpret what this prompt
*  learns. And I think so far the conclusion is not really interpretable. It's kind of like a black box
*  what this soft prompt really captures. Because like I said, the language model is so big, right?
*  There are so many hidden kind of limitations that can guide it towards certain things.
*  So in terms of this soft prompt, I would say Bluetooth is similar, that we are trying to
*  provide prompts that can embed vision information. So we don't really know what exactly are these
*  vision information, but they are limitations of the image that the language model can make use of.
*  And I think why we are sure that there must be repetition of the image comes back to our first
*  stage pre-training. Because in our first stage pre-training, we are using these contrasting
*  laws, we are using these image text matching laws. So that from this pre-training objective,
*  we can be certain that this connector, like we call it a QFormer, is learning the most
*  representative feature from the image. So it's kind of like a feature extractor. You extract
*  good features from a frozen image encoder. So we are certain of that because we know these are
*  good features that represent the image well. Then that's why we are confident that if you put this
*  to a language model, then it's most likely we'll teach the language model about the image rather
*  than something else. Yeah. I wonder if we can give folks even a little bit better intuition for this.
*  I mean, as you said earlier, a picture's worth a thousand words. And it is fascinating to me that,
*  especially with relatively little compute, right? One machine for 10 days is kind of the total
*  thing that you can figure out a way to predict these injectable embeddings into this space,
*  which was originally created by embedding text and which is interpreted as if it were text
*  by the language model. And the loss is ultimately based on what comes out the other end of the
*  language model and that that all still works. It's like there is this sort of invisible
*  kind of dark space within the language embedding space that language itself cannot access,
*  but which this model can learn to access in such a way that it is still immediately
*  interpretable by the language model itself. It's definitely worth more research to really
*  find out the working mechanism. I just want to mention some of our previous efforts.
*  So we do have some previous paper where we tried to directly map the image to text,
*  like human-interpreterable text focus. And we give this text as input to the language model and see
*  what it can do. We find out it's quite good. Let's say we generate captions and then we give these
*  captions to the language model as context to answer questions or do some other tasks. It can
*  perform well, but there are some limitations. And the major limitation is that those captions,
*  they are hard to represent everything about the image. So we need to first find relevant captions,
*  relevant meaning that is relevant to my task. If I want to ask a specific question,
*  then I need this caption to be relevant to this specific question so that I know the language
*  model can make use of this. Secondly, we need to generate a lot of captions. One caption is not
*  enough. We need to maybe generate 20, 30 or even more to hopefully capture more information about
*  the image. So that's why we changed to this paradigm where we inject embeddings, because each
*  embedding is itself a vector. I think it's 768 dimensional vector. And we have 32 of these vectors.
*  This actually can capture quite a lot of information, because if you consider images
*  itself, it's just 200 by 200 pixels. And now we transfer the knowledge into these embedding
*  vectors. How do we make sure these are interpretable by the language model? If we just
*  randomly generate these vectors and we give the language model and we ask the language model to
*  generate the text, it's likely there are a thousand ways the language model can interpret image and
*  generate some text. So that's the most previous approach we are using. They just train with this
*  language model at the end. So the training signal is truly coming from the language model's output
*  and back-propagate to this connector. There are a lot of ways for this connector to basically cheat.
*  So it can cheat, such that during training it can guide the language model to produce certain output,
*  but it cannot really generalize. It doesn't really understand the image. It's just cheating because
*  it can change its own output and adapt to the language model. So again, that's why we need this
*  first stage to make sure this connector itself has really good understanding of the image.
*  And that's why during our two-stage pre-training, our first stage actually takes a longer time. So
*  we take maybe six days to pre-train the first stage. And the second stage, while we plug in
*  the language model, we only need maybe two days. So that's a drastic difference from the previous
*  approach. And this also means that after we pre-train this connector first, we can plug in
*  different language models, and it doesn't take much time to adapt. So because the connector itself
*  already has good understanding of the image, it's hard for itself to... Because it tries to find the
*  shortcut. So deep learning models always try to learn the most easy solutions to certain problems.
*  If there's a shortcut, it will find it. So by making it to understand the image first,
*  its shortcut, its obvious solutions will disappear because it cannot really
*  overfeed. Basically, the easier solution for the connector is not, I need to understand the image,
*  because it already knows the image. So that's become easier solution. So that's why I think it
*  works well in our case. And we don't really just rely on the language model to teach the connector.
*  I would kind of pre-teach it first so that it can teach the language model instead.
*  That's really interesting and definitely gives me a better understanding than I had just from
*  reading the paper. So thank you. Have you gone as far as to try to find... Because you might think,
*  okay, what's the closest I could get if I just had text to the embeddings that are predicted by the
*  connector model? Have you tried to figure that out? And if so, are you able to get at all close?
*  Or is it just kind of like a totally different universe that the connector... Or let's probably
*  better analogy would be, totally different language that the connector model is speaking.
*  Yeah, I would say it's quite difficult to map the output of the connector to certain text tokens,
*  because like you said, this language model space, input space is so huge.
*  I don't think it's really interpretable by human language, but I do think there's a lot of
*  information there. Maybe not in the form of human interpretable, but definitely interpretable by the
*  language model. And I do see a lot of research work can be done in that space to try to make it
*  less of a black box for us. I kind of think of language models increasingly, especially with
*  the rise of these connector models, as kind of like the executive function of these kind of expanding
*  ensembles that increasingly are going to be fairly general, I think, and can kind of do a lot of
*  different things. In a way, it's not that dissimilar from how we see, right? Like we have
*  our eyes, the eyes kind of take in raw light and turn that into a signal. And that signal
*  goes through the nerve and finally gets back to the back of the brain. And by that point,
*  it's not that interpretable either, right? It doesn't necessarily correspond to language,
*  but then there's some further connector that like turns that visual data into something that I can
*  understand as language, or at least understand and then articulate as language. So it feels like there
*  is something kind of analogous taking shape in the AI world right now, where the language model
*  feels like kind of a center. I'm not big on analogies. I honestly am very suspicious of
*  analogies. So tell me, I want to hear why you think this analogy is wrong or where you think
*  it falls short. But it feels intuitively like there's this kind of analogy between kind of
*  myself or my kind of conscious awareness and my narrative center. And then obviously the eyes and
*  the image models are analogous and you've kind of now created the circuits that connect the two.
*  Do you like that analogy? Do you think that that is missing the mark? How is that falling short?
*  I think that's a very good analogy, to be honest. I think the reason why this knowledge model are
*  so powerful now is because they are trained basically on the entire web, right? So the amount
*  of knowledge and information is so much on the web. And in particular, these texts, they are
*  very concentrated information. I would say with the current kind of deep learning model and
*  transformers, it's easy to learn from texts and images because the images are raw pixels. It takes
*  some processing to really understand what's going on. But these texts, they are very, like one word
*  can encompass a lot of information in that. I think that's why the knowledge model have been
*  very successful in learning this kind of word knowledge and have conversations, right? Answer
*  questions and do all these kind of amazing tasks. So I do see that this is kind of a brain. In the
*  current status, at least this knowledge model can be considered as the central piece that holds all
*  the knowledge. And then what we are trying to do is that we bridge this knowledge to some other
*  modalities and make her process other modalities information. This could be hard because these
*  language models, they have never seen those data, right? Like imagine you are human, you grow up
*  learning only knowledge and now one day you open your eyes, you don't really know how to
*  interpret what you see. So that's what we are trying to do here to kind of build this bridge
*  between these two modalities. And I do see there is a potential that by adding additional
*  region or other modalities, this knowledge model itself can also improve. So we are giving it more
*  information to learn from. And for now we are keeping the knowledge model frozen because mostly
*  our data, this image and text data is not so great that in the sense that the image is good
*  but the text corresponding to this data are limited. So let's say we have better quality
*  text, even better paired image and text. But actually I do see there is a way we can teach
*  the language model to further improve from this additional data as kind of a new knowledge.
*  And I can see a pretty direct path to that. I mean you already have,
*  just combining a couple ideas from your last few papers, slicing, one thing we are going to try,
*  we haven't done this quite yet because you just sent me the paper the other day, but with Waymark
*  we are going to at least start to experiment a little bit with slicing images into just pieces,
*  like slice them into four square, four rectangles or nine rectangles or whatever, caption each of
*  those, then maybe use a language model to try to synthesize all those captions into kind of one
*  overarching caption. I have seen some of that stuff with video as well where you take a frame
*  every second or whatever and then caption all of those and then use a language model on top of that
*  and you can kind of synthesize the narrative. And again, this is all just frozen stuff, right?
*  I'm talking like I think I did that with TextaVinci 2. Here's a bunch of captions,
*  tell me what must be going on in this video. And that works off the shelf. So it seems like
*  we're now entering kind of a phase two where it would probably take a significant amount of
*  compute to do this, but I would expect that if you went back through like the Lion data set,
*  for example, and revisited either some of those noisy images or even some of the better ones,
*  that just may have short captions and kind of ran a process like that, you could probably enrich
*  the data set quite a bit and end up with a data set that you could then do go back to the end to
*  end training with. So is that kind of the direction that you guys are headed next? Am I picking up
*  where you're going? Exactly. I think actually this has been done, not exactly like what you
*  described, but it has been done. So like I said in our previous paper, we already kind of generated
*  synthetic captions on these lion images. We didn't really slice them into different crops,
*  right? That's definitely something we would have done, but I think due to this efficiency and speed
*  concern, like lion data set is so huge, right? We just randomly sample captions for each image.
*  But after the paper, the lion team themselves, they actually have this version called lion
*  synthetic captions or Coco caption data set, right? Where they use this big model to generate
*  captions and they make sure the captions are higher quality. So they do some random sampling
*  and they even do some paraphrasing. And that data set, in my opinion, is quite good in terms
*  of the quality. It may lack some diversity because it's generated by just one model,
*  one blip model. So if you compare it to the web data, it may lack some diversity, but
*  that's definitely a much higher quality that the texts are more aligned with what the image is about.
*  Yeah. Do you think that these techniques will work for other modalities? Like when I think of
*  video, for example, or sound, the one thing that jumps out immediately is like there's a time
*  dimension to those that complicate things quite a bit. With video, I can more easily imagine just
*  like down sampling and kind of running things that way. With sound, it feels like it would be a bit
*  of a bigger leap, but ultimately I also kind of imagine that it would be going to be smart enough
*  to figure that out. Do you anticipate that similar techniques will work across all these
*  different modalities? I would say so. For videos, like I said, it's actually quite straightforward
*  to just adapt blip to video input. You just down sample certain frames to add a time step
*  position encoding to each frame and keep this to the encoder so that it can encode all the frames
*  and keep track of their relative positions in the time dimension. For sound, I'm not really
*  expert in sound, but I would say you can do a similar thing. You have these
*  sound encoders that can encode these wave signals and then you have this knowledge model that can
*  understand language. You try to bridge those two using some of our technique. I would say it would
*  definitely work. Ultimately, this feels like kind of one path to something like AGI. I think
*  obviously people have very different things in their mind when they talk about AGI, but take a
*  chat GPT or a Claude and maybe a next generation of those and equip them with all of these
*  connector models where they have the ability now to understand visual data and the ability to
*  understand sound data. Then you can also imagine potentially connector models coming out the other
*  side too. If you strip off that last layer that turns all the logits into token into a single token
*  prediction and you take that last probability distribution and feed that into another connector
*  model, it doesn't seem like a huge stretch that you could get action or motion predictions out of
*  that. Is that like the macro vision that you guys are working toward? Do you see yourselves
*  as building toward this giant, ultimately like this colossus of a giant ensemble that ultimately
*  can be a super powerful system? Yeah, our vision is to build this kind of ultimate multi-modal
*  kind of system where you can do a lot of things, not only image, you can also maybe do coding
*  and do actions and understand other modalities data. I think that's something we are trying to
*  build and I would definitely love to have a larger chat GPT model to train with, but unfortunately
*  that's not available. So I think as Salesforce research, what we are trying to push is we want
*  first of all open source all the models we have. So I think almost 100% of our research will be
*  delivered to the community with open source code and models. And we are also trying to kind of
*  democratize this AI and the pre-training in particular because they are so costly,
*  in particular those language models, right? They are so costly to train. I think most practitioners
*  won't have the resource to train them. So that's why we're trying to propose these techniques that
*  is more like a methodology rather than a model that you can in a more convenient way, an efficient
*  way to make use of these available models. And you can add on top of our method, you add some other
*  strategies that you have this efficient adapter module that you may want to try. So I think it
*  opens up a door for others to really make use of these large models because we can really adapt
*  them but keep them frozen during our training. What should we be on the lookout for from you
*  guys next? Yeah, we got some exciting news. Dongxu will have a new model coming out soon.
*  It's about text to image generation. So yeah, I feel that could be quite exciting. And also on
*  this tool, we are working on the next version, which hopefully will be stronger than the current
*  model. It is amazing the pace of research right now. Do you guys feel like everything you do is
*  working? Like, are there a lot of failures that you're like not publishing or is it basically
*  like all the projects are working? They are definitely failures. So I think our kind of
*  strategy is we focus on a direction first. So a topic and direction that we feel like
*  it will be impactful to the community. And then we work on that. So we can meet some
*  failures in the way, but because we are confident that this will work in the end,
*  we will continue to push forward. And most of the time eventually we will meet our target.
*  I think a lot of these failures in research, they are not necessarily just failures. They
*  succeed at different degrees. So like if you want to get AGI, you don't get it immediately after one
*  grand research project, but it takes a lot of iterative efforts. So we
*  succeed in the sense that we believe we are making steady progress towards that goal.
*  And we also want to take some risks, you know, meanwhile, so that we can always explore something
*  that we are curious about and not just, and also to tell people something we discover.
*  Notice to pushing up the metrics and benchmarking results. We just really want to share the
*  insights and discoveries so that ours can also benefit from our findings. And to do that is also
*  important that we ensure our methods and codes and install are all open source. And I think we
*  are, we really benefit a lot from the open source community from others,
*  especially this flip phone model. We leverage this open source vision and language models.
*  And we really want to say that this community feedback and community efforts are really important
*  to pushing the development of AGI. And we are also quite committed to that.
*  What are your guys' first languages and what do you speak in the office environment? Is it all
*  English at work or is it a mix of things? Yeah, our team comes from quite diverse countries.
*  Like Dongxuan and I, we are from China. We also have team members here from Singapore,
*  Vietnam, India. So at office we speak English as kind of the official language. But personally,
*  Dongxuan and I, we speak Chinese. Being able to speak at a high level on technical topics in
*  another language, I think is impressive. I guess before too long, we might have some AI babblefish
*  that could sort everything out in real time. But for now, I'm relying on your English ability,
*  obviously. How has AI affected how you guys work on a day-to-day basis? Are there any tools
*  that have made an impact on your daily workflow? Yeah, Dongxuan maybe can speak to that. He's a
*  heavy co-pilot user. I think there are a lot of things happening behind the scene that we may not
*  be directly aware of. I'm not sure that this search results. For example, Google, a lot of AI
*  is going on behind. So I think I Google a lot of things every day on Stack Overflow. That's the
*  main thing I rely on, coding. I think in terms of that, having improved the search efficiency
*  using this AI is probably efficient. Recently, I also gave $8 to Microsoft every month for the
*  co-pilot subscription. Sometimes it gave me a bug, but it was taking some days to figure out.
*  It's very good for machine learning experience. But for most of the time, for example, one of them
*  is this boilerplate code. It really helps a lot. It's code comments, testing cases, unit tests.
*  It really saves me a lot of time. Sometimes I don't just... I may not feel
*  anything of it, but if I disable that plugin, I feel like my lab quality has worsened a lot.
*  I really have to keep paying for the subscription. I want to look at this because I'm right now
*  working on this TechSuite image generation project. I keep an eye on this forum,
*  all this infest community. There are a lot of these very surprising and
*  impressive image generation results every day. That really blows my mind. I also learned a lot
*  from there. It's not just about entertaining. Sometimes I also get to know people. What are the
*  most interesting things to people? That's also amazing. Cool. Thank you. I'm also a big
*  co-pilot fan, so I can totally relate to that. And a big hugging face fan.
*  So we're definitely sharing tools from 12 time zones away.
*  Yeah. We have some in-house code generation models and hopefully I don't need to pay that subscription
*  soon. I'm sure you're aware of how Replet used their Ghostwriter model was a distillation,
*  I believe, from the Salesforce code gen method. I don't know if you've used the Replet Ghostwriter,
*  but it's also very good. And they also now have a chat mode. Hard to say. I would both co-pilot and
*  Replet, I think, are advancing pretty quickly. It's amazing that Replet's not that big of a company
*  and they are, I would say, keeping pace with co-pilot, but certainly got a big jump out of the
*  gate by being able to build on the Salesforce code gen. So if you haven't checked that out already,
*  I definitely recommend it as well. You guys are doing, I think, some really
*  useful work with the blip set of models. As I said at the top, much more enduring than almost
*  anything else that we see in AI right now. So that's awesome. You have this kind of understanding
*  of how this work fits into a bigger picture of kind of an ensemble strategy for AGI. But zooming
*  out even a little bit further, kind of thinking about society, thinking about the change that
*  we're all about to see over the next however many years as AI kind of goes from a research agenda to
*  an applied reality in life. What are your biggest hopes and also what are your biggest fears for
*  what AI could mean for all of us? That's a big question. I think my biggest hope is,
*  I think it's getting close. I'm surprised by the advancement every day.
*  So I think the progress is even beyond what I can hope for now. It's developing so fast
*  with all this journey to AI. I think this year or for the past two years, it has been really
*  growing fast. I don't really fear it in the term because like in
*  literally speaking, because we are the one fundamentally who build these models.
*  So I would say maybe there is the public has a different opinion on this AGI. But as a researcher,
*  I would still consider them to be quite artificial and even stupid a lot of times.
*  And I know it's not as far from like sentient or perfect as it's been. Fundamentally,
*  it's just a big neural network. It is far from what we expect from humans. So I was
*  looking forward to that day to come in the future.
*  In the meantime, while we are innovating, we also pay attention to kind of related
*  ethics issues on these foundational models. And we have an ethical team who have us to review
*  our use cases, especially on some of the demos we are making.
*  And I think we have seen a couple of examples of this kind of threatening user-large language
*  model interactions in some of these recent large language chatbots. And we want to make sure that
*  eventually we are responsible with our model is responsible for what it is actually producing,
*  understanding what it is doing, not just to abuse it to the cases that are harmful
*  in innocence to the human. And we do have a sense that a lot and our ethics teams,
*  they work very hard to ensure that our delivery and development is safe and also production ready
*  when we want to deploy that. And then just to add on top of that,
*  this external AI is also one of our major focus. And we do have a library called OmniXAI that is
*  all about how do you interpret models predictions to make really safe and
*  interpretable decisions based on those AI models.
*  Awesome. Well, Junan Li, Dongchul Li, thank you guys very much for joining us on the Cognitive Revolution.
*  Thank you. Thanks a lot.
*  OmniQI uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in OmniQI so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
