---
Date Generated: December 14, 2024
Transcription Model: whisper medium 20231117
Length: 6355s
Video Keywords: []
Video Views: 429
Video Rating: None
Video Description: Nathan welcomes back computational biochemist Amelie Schreiber for a fascinating update on AI's revolutionary impact in biology. In this episode of The Cognitive Revolution, we explore recent breakthroughs including AlphaFold3, ESM3, and new diffusion models transforming protein engineering and drug discovery. Join us for an insightful discussion about how AI is reshaping our understanding of molecular biology and making complex protein engineering tasks more accessible than ever before.
Help shape our show by taking our quick listener survey at https://bit.ly/TurpentinePulse

SPONSORS:
Shopify: Shopify is the world's leading e-commerce platform, offering a market-leading checkout system and exclusive AI apps like Quikly. Nobody does selling better than Shopify. Get a $1 per month trial at https://shopify.com/cognitive

SelectQuote: Finding the right life insurance shouldn't be another task you put off. SelectQuote compares top-rated policies to get you the best coverage at the right price. Even in our AI-driven world, protecting your family's future remains essential. Get your personalized quote at https://selectquote.com/cognitive

Oracle Cloud Infrastructure (OCI): Oracle's next-generation cloud platform delivers blazing-fast AI and ML performance with 50% less for compute and 80% less for outbound networking compared to other cloud providers13. OCI powers industry leaders with secure infrastructure and application development capabilities. New U.S. customers can get their cloud bill cut in half by switching to OCI before December 31, 2024 at https://oracle.com/cognitive

Weights & Biases RAG++: Advanced training for building production-ready RAG applications. Learn from experts to overcome LLM challenges, evaluate systematically, and integrate advanced features. Includes free Cohere credits. Visit https://wandb.me/cr to start the RAG++ course today.

CHAPTERS:
(00:00:00) Teaser
(00:00:46) About the Episode
(00:04:30) AI for Biology
(00:07:14) David Baker's Impact
(00:11:49) AlphaFold 3 & ESM3
(00:16:40) Protein Interaction Prediction (Part 1)
(00:16:44) Sponsors: Shopify | SelectQuote
(00:19:18) Protein Interaction Prediction (Part 2)
(00:31:12) MSAs & Embeddings (Part 1)
(00:32:32) Sponsors: Oracle Cloud Infrastructure (OCI) | Weights & Biases RAG++
(00:34:49) MSAs & Embeddings (Part 2)
(00:35:57) Beyond Structure Prediction
(00:51:13) Dynamics vs. Statics
(00:57:24) In-Painting & Use Cases
(00:59:48) Workflow & Platforms
(01:06:45) Design Process & Success Rates
(01:13:23) Ambition & Task Definition
(01:19:25) New Models: PepFlow & GeoAB
(01:28:23) Flow Matching vs. Diffusion
(01:30:42) ESM3 & Multimodality
(01:37:10) Summary & Future Directions
(01:45:34) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Scouting Frontiers in AI for Biology Dynamics, Diffusion, and Design, with Amelie Schreiber
**Cognitive Revolution:** [December 14, 2024](https://www.youtube.com/watch?v=enNrsTrf2ck)
*  I saw people designing mechanical degraders that pulled apart like the needle complex of bacteria
*  so that the bacteria couldn't infect the cell and they were actually able to like pull apart
*  the needle complex of the proteins that they designed and prevent infection. If you can scale
*  that process and have an agent drive a big complicated workflow and solve a task
*  and you can just like churn out molecules, that changes things a lot. If you're interested in
*  biochem and you're interested in AI, I would highly suggest getting into it as soon as possible
*  because it's very fast moving, very fast paced, but also just really beautiful and the things
*  that we can accomplish with this are going to be great. Hello and welcome back to the cognitive
*  revolution. Before getting started today, I want to take a moment to invite all of you to submit
*  questions for an Ask Me Anything episode that we'll be producing in the next couple of weeks.
*  From practical application to galaxy brain philosophy to parenting and career choices in
*  the age of AI, I may not have all the answers, but it's all fair game to ask. And while you're there,
*  we'd appreciate it if you'd complete a short survey so that we can learn more about the audience
*  and how we can serve you better. All of the questions are optional. It's fine if you want
*  to be anonymous and we do have a few thank you gifts planned as a token of our appreciation.
*  That said, today I'm excited to welcome Amelie Schreiber, computational biochemist and AI
*  researcher back to the show for our second deep dive into frontier developments in AI for biology.
*  Our first conversation just over six months ago now offered a fascinating glimpse into how AI is
*  transforming humanity's ongoing quest to understand life at the molecular level and to harness that
*  knowledge for everything from medicine to industrial process. And it prompted perhaps the
*  single biggest update to my personal worldview of any episode we'd done up to that point.
*  Since then, the pace of progress in AI for biology has, if anything,
*  accelerated. We now have Alpha Fold 3, which extends the structure prediction paradigm to
*  include RNA, DNA, small molecules, metallic ions, and critically ensembles of all of these.
*  ESM3, a new multimodal model that combines sequence, structure, and function. And an
*  ever-growing library of specialist models as well. Of course, no single podcast could hope
*  to be comprehensive in such a fast-moving and expanding space, but Amelie does an amazing job
*  of keeping up with the literature and in this conversation serves as an incredible guide to
*  recent advances and current challenges. She helps me understand why modeling dynamics,
*  not just static structures, is the new frontier. How molecular dynamic simulation models like MDGen
*  are dramatically accelerating what traditional computational methods can achieve. And the recent
*  introduction of diffusion models that specialize in shorter sequences of amino acids called
*  peptides, which are often less structured than larger proteins and thus generally much harder
*  to model. Now a big part of what makes Amelie's perspective so valuable is her unique understanding
*  of how all these tools relate to one another and can ultimately be used together. As researchers
*  explore ways to chain these specialized models together to orchestrate the entire protein design
*  workflow, what emerges is a new paradigm of increasingly AI-assisted and even AI-driven
*  protein engineering and drug discovery that promises to be dramatically more efficient,
*  more creative, and more tuned to the nuances of biology than anything we've seen before.
*  Big picture, these workflows could make even the most complex protein engineering tasks,
*  like designing enzymes that catalyze entirely new reactions, which would have seemed like
*  pure science fiction not long ago. Not just achievable, but perhaps even accessible and
*  affordable over the next few years. As always, if you're finding value in the show, please share it
*  with a friend, post about it on social media, or leave us a review on Apple or Spotify.
*  I sincerely believe that many more people should be paying attention to the developments happening
*  right now in AI for biology. I plan to do a lot more episodes in this area, and I appreciate you
*  helping to spread the word. Of course, we always welcome your feedback and suggestions too. You
*  can contact us via our website, cognitiverevolution.ai, and there you'll find a link to the AMA form and
*  the survey right at the top. And of course, you can feel free to DM me on your favorite social
*  network as well. For now, I hope you enjoyed this update on recent advances in AI for biology with
*  computational biochemist and researcher, Amelie Schreiber. Amelie Schreiber, computational
*  biochemist and AI researcher. Welcome back to the cognitive revolution.
*  Hey, nice to be here. I'm excited about this. It has been about six months since our last deep dive
*  into developments in AI for biology. And the pace is accelerating in that subfield of AI,
*  obviously probably one of the most consequential ones, if not the most consequential one long term,
*  just as it is everywhere else. So I'm excited to have this opportunity to catch up.
*  Last episode we did was really well received. I think there's a ton of hunger among a general
*  audience that hears a lot about large language models and a lot about image generation to
*  understand, okay, sure, but how is all this stuff going to impact science and biology and ultimately
*  medicine and ultimately quality of life and maybe even longevity? Last time we kind of,
*  and I would definitely recommend for folks if they haven't seen it already, go back and check that
*  episode out. But we basically covered the two main challenges as I kind of came away understanding it
*  in biomedicine broadly, one being, can we understand what is going on? What causes what?
*  What interacts with what? What promotes what? What inhibits what? All that sort of stuff,
*  obviously super complicated. We've got a lot of work left to do on that. And then the other thing
*  which really surprised me was just how far we have already come when it comes to a situation
*  where given a target where we know what we want to affect the ability to actually design new
*  proteins to introduce into cells and make the desired changes and actually interact effectively
*  with the proteins and the other molecules of life. So pretty fascinating stuff. I kind of
*  recall that we talked about predicting structures as kind of static structures with different levels
*  of resolution. And we also talked about the ground truth being the Boltzmann distribution,
*  which is not a single structure, but like a range of structures where some of them are,
*  the way that these big molecules spend a lot of their time and then others are kind of
*  in between states where they don't spend so much time. And you can do that at kind of a general
*  shape level or a sequence level or even down to like the all atom level where you're even trying
*  to get to where each hydrogen atom is. All that to tee up, a lot has happened in just the last
*  six months. We've got some Nobel prizes given out. We've got a bunch of new models. You've
*  drawn my attention to some new models specifically focusing on peptides. We'll get into why that's
*  important. And then I want to try to dive into your actual work a little bit better and understand,
*  because we got kind of the general way of the land last time, but didn't come away with a great
*  sense of like what you actually do during the day and what the practice of designing proteins
*  actually looks like today if I were to come watch over somebody's shoulder. So let's start off maybe
*  with a little discussion of David Baker, because I know you're a huge fan and he recently shared a
*  Nobel prize and that's a big deal. I think he was obviously the less famous recipient of the prize,
*  but maybe it shouldn't be that way. It shouldn't be that way. No, I have a few things to say there.
*  Yeah, definitely a huge David Baker fan for sure. He runs a solid lab. The work they put out is
*  really good stuff. And from what I hear, he's a very good advisor too. A lot of his students
*  and coworkers have a lot of good things to say about him. So yeah, I definitely love to follow
*  their work, Baker Labs work. So I guess like something that is a little maybe annoying to me
*  in particular is the fanfare that Alpha Fold got over some of the stuff that David Baker got in
*  some of the more simple mainstream videos that are maybe not digging into the history as much
*  as you could. Because I mean, David Baker's been doing this for a while. He's been doing
*  protein engineering for longer than Alpha Fold has been around for sure. And I would say the
*  approaches that they were using pre-Alpha Folds were very physics-based sort of methods.
*  And I mean, they had some reasonable results with some of that in some systems, but I think things
*  really started to change when they started adopting AI. And that happened right around when Alpha
*  Fold happened. I think like Baker Lab have been using AI methods even before Alpha Fold came out.
*  They also built their own structure prediction model similar to Alpha Fold 2. They built Rosetta
*  Fold 2, which is a very similar model, does the exact same thing, predicts the structure given
*  a protein sequence. And they actually did something really interesting, right? They took it a step
*  further. They didn't stop at structure prediction. They decided they wanted to bring in someone to do
*  generative modeling. And so they brought in people to do generative modeling, and they fine-tuned
*  Rosetta Fold 2 into a diffusion model that they called RF diffusion, right? And we talked about
*  this some last time when we met. I think it's a very important model to know. It's very useful,
*  even still. I mean, in AI terms, it's been out forever. It's been out for like two or two and
*  a half years, but it's still very useful, even though it's an older model, so to speak.
*  And I would say that that work in a lot of the YouTube videos and things that I was seeing
*  floating around that were more oriented towards like kind of hyping AI, they kind of brushed over
*  some of the contributions that David Baker has made. But I have found a few good ones that
*  actually went into the history a little bit and talked about like Rosetta and what David Baker was
*  doing before Alpha Fold and what his lab did after Alpha Fold. And I think they've come up with a lot
*  of different AI models too. It's not just structure prediction and generating binders or doing motif
*  scaffolding with RF diffusion. They also had to develop a sequence design model so that they could
*  design the protein sequences that fold into the design structures that they have. And they've also
*  developed several other models for various other things that we'll talk about today probably. And
*  yeah, I think it was well deserved. The Nobel was definitely well deserved for sure. I think as these
*  things always go, there are always a few people that maybe also deserved it that didn't get it
*  or that contributed similar things but didn't get put in the spotlight. And I can maybe give some
*  links to some info about that towards the end if people want to look into that a little more. But
*  yeah, I mean really cool stuff. I think it says a lot too that if you break it down into the physics
*  and the chemistry Nobel category, I guess there were five total Nobel laureates this year that won
*  Nobel's in large part because of their AI techniques, which I think is really cool. And that's saying a
*  lot about the kind of impact that AI is having. And I think there is plenty of hype, but there's a
*  lot of signal there too. It's not all noise. There's plenty of signal and I think it's still coming
*  through. And in biochemistry in particular, it just hasn't even popped off yet in my opinion.
*  We're still at the very beginning of the curve there in a lot of ways. So yeah, a lot of exciting
*  stuff to look forward to. Yeah, so there were two things that you mentioned that you wanted to talk
*  about that I thought would be good to address up front. Alpha Fold 3 and ESM3. I think both of those
*  are good things to mention because those both came out since we talked last. And those are
*  pretty big foundational models, whatever that term means anymore. But they're pretty central,
*  important models that do some pretty important things. And the new Alpha Fold 3, it predicts
*  complexes of not just proteins now, but also RNA and DNA and small molecules and even ions,
*  which is pretty cool. I think especially the ions, I haven't spent a lot of time testing how accurate
*  that is. So I won't speak to the quality of the predictions that involve ions, but assuming that
*  your predictions are high quality and the ion predictions are good, that's actually like,
*  it's really useful for several things that I'm interested in. So that's pretty cool.
*  Unfortunately, not open source, so I can't really use it. But hopefully, you know, we'll have some
*  open source versions pretty soon. Can't say for sure when, but I do know there are at least a couple
*  of groups working on it. And there are a couple of open source versions that have come out that
*  are like kind of approximations of Alpha Fold 3, but nothing that's really satisfied me yet.
*  I think they each have their own merits, but I haven't seen something that I feel like is just
*  like a really good faithful reproduction of Alpha Fold 3 yet. And that's still in the works by a
*  couple of groups. Hopefully, that'll come out sometime by the end of the year, first of next year.
*  And I think that having something that will predict the structure of complexes involving
*  all the different biomolecules and ions included is super useful, right? Because then you can start
*  predicting things like protein-protein interactions or protein-nucleic acid interactions,
*  and start building out these interaction networks, which is really important for understanding
*  different disease mechanisms or, you know, like how, like, if I want to treat some particular
*  disease, do I need to, like, design a binder here? Do I need to design some kind of inhibitor? Do I
*  need to design, like, an allosteric modulator? You get the idea. So it's useful for building out
*  these interaction networks and understanding how things are interacting with each other and where
*  you need to design your molecules and for what purposes you need to design them for.
*  A couple questions on Alpha Fold. I guess there is an API, right? Just to be, to go back to the
*  open source bit for a second. There is, yeah. You can definitely use the API. I guess it's not open
*  source on GitHub. The other thing, too, is, like, the restrictions on it are pretty limiting. So,
*  like, if I wanted to use their API in some kind of drug design process, I wouldn't actually be able
*  to do that because of their licensing and stuff. So it can't really be used for, like, drug design,
*  unless maybe you're, like, an academic and you're doing it completely outside of the whole capitalist
*  profit sort of machine and you're just doing it for academic research purposes and it's all
*  completely, like, public domain, open source sort of research that's coming out of it. I think that's
*  fine. But if you're doing anything that you want to have, like, any kind of IP for, or if you wanted
*  to, like, patent your molecule or sell it or get it into the whole drug discovery pipeline and have
*  it go to market or something one day, like, you couldn't really do that. They have restrictions
*  on it so that you can't really do that. Yeah. Gotcha. You also mentioned sort of the fact that,
*  like, one of the qualitative differences between Alpha Fold 3 and what has come before is that it
*  now works with all of life's molecules, I think was the language that they used in the original
*  blog post, if I remember correctly. And your comment there sort of suggested that you might
*  be able to use this to kind of almost brute force your way through exploring what interacts with what
*  in a cell. Like, I've come to sort of an estimate that we have maybe 5 to 10% of all of the
*  interactions in a given cell mapped and understood. And, you know, that obviously means that the
*  majority of it, like, we don't know exactly what's interacting with what yet. Right. This sounds like
*  you almost think it could be the basis for just put a few things together, throw them into Alpha
*  Fold 3. If they seem to interact in a very, like, natural or close fitting way, then you would maybe
*  infer that, hey, this probably happens for real and that's like a real interaction. And if you
*  put them together and they, like, don't seem to form a good fit together, then you would think
*  that's maybe something that doesn't have a lot of actual impact in how cells behave. Is that the
*  right intuition for that? Yeah, that's roughly- Are people just like brute forcing through this now?
*  Well, kind of. Hey, we'll continue our interview in a moment after we're with our sponsors.
*  The Cognitive Revolution is brought to you by Shopify. I've known Shopify as the world's
*  leading e-commerce platform for years, but it was only recently when I started a project with my
*  friends at Quikly that I realized just how dominant Shopify really is. Quikly is an urgency
*  marketing platform that's been running innovative time-limited marketing activations for major
*  brands for years. Now we're working together to build an AI layer, which will use generative AI
*  to scale their service to long-tail e-commerce businesses. And since Shopify has the largest
*  market share, the most robust APIs, and the most thriving application ecosystem, we are building
*  exclusively for the Shopify platform. So if you're building an e-commerce business, upgrade to Shopify
*  and you'll enjoy not only their market-leading checkout system, but also an increasingly robust
*  library of cutting-edge AI apps like Quikly, many of which will be exclusive to Shopify on launch.
*  Cognitive Revolution listeners can sign up for a $1 per month trial period at Shopify.com
*  slash Cognitive, where Cognitive is all lowercase. Nobody does selling better than Shopify,
*  so visit Shopify.com slash Cognitive to upgrade your selling today. That's Shopify.com slash Cognitive.
*  There are so many things in life we just never get around to. Taking up that hobby,
*  cleaning out the garage, you know, little things that don't really make huge differences in our
*  lives. Yet there's one thing that most of us have probably been neglecting that can have a huge
*  impact on our family's future. It's life insurance. And with Select Quote, getting covered with the
*  right policy for you is easier and more affordable than you might think. As someone who tracks AI
*  progress on a full-time basis and obsesses about its potential impact nonstop, I know how tempting
*  it can be to ignore more mundane, familiar risks. There's always another paper to read,
*  podcast to listen to, or product to try. And yet the smartest people that I know in the AI space
*  continue to save and invest money for the future, carve out time for their relationships,
*  maintain their physical and mental health, and yes, protect their family with life insurance,
*  just in case anything should happen before the singularity. If nothing else, it's one less thing
*  to worry about in a time of unprecedented change. So get the right life insurance for you,
*  for less, at selectquote.com slash cognitive. Go to selectquote.com slash cognitive today to get
*  started. That's selectquote.com slash cognitive. So let's talk about a use case of structure
*  prediction first, and then we'll talk about like the interaction prediction and building out
*  interactomes or interaction networks. So one thing that AlphaFold2 was used for by Baker Lab
*  was in this workflow where they design a backbone with RF diffusion. They design a binder backbone
*  with RF diffusion, and then they use protein MPNN or ligand MPNN or something like that to design
*  multiple sequences really, and all of which are supposed to fold into the backbone that you just
*  designed with RF diffusion. And then the final step is validating that, right, and predicting
*  the structure of those sequences that you designed and making sure that they actually do fold into
*  the right structure that you designed with RF diffusion. And when you do this, sometimes you
*  have to do it in kind of a high throughput way. So like sometimes people will generate 10,000,
*  50,000, even 100,000 potential binder candidates, and they'll design, you know, sometimes multiple
*  sequences for each one, and then they'll do structure prediction, right? And the structure
*  prediction step, there's a technique that was shown to help in screening for protein-protein
*  interactions for this binder design pipeline. And basically what it amounts to is you give AlphaFold2
*  a template that just has the target. You remove the MSA part of the prediction process, so it
*  doesn't generate the MSA, it just uses a single sequence. And you predict that, and then at the
*  end, once it's done a few recycles and predicted the structure, you then take the PAE map and use
*  the PAE map to compute like a mean PAE score over the interface. And once you have this mean PAE
*  score over the interface, you can use that to sort of filter out binders that maybe aren't going to
*  interact very well. And this has been used by BakerLab for a while now, and if it's done in a
*  very particular way, it is useful for screening. But they ended up training a different model
*  to do this that was lighter weight and smaller so that they could do it faster. Because when
*  you're having to do this in a really high throughput way, you need to be able to do it kind of fast
*  because you're doing lots and lots and lots of predictions with lots of proteins. And so
*  they stripped it down, made it lighter weight, pulled out some of the layers, and simplified
*  the architecture, and used that for their screening. And it turns out like you don't need to be
*  particularly good at structure prediction to screen for protein-protein interactions. The model
*  that they fine-tuned actually does better at predicting protein-protein interactions, even
*  though it does slightly worse at predicting the structure. And so I do think structure prediction
*  models like Rosettafold or Alphafold in their various incarnations is going to be a very key
*  central thing to high-quality protein-protein interaction prediction. I think any method that's
*  going to involve predicting interaction between two proteins, not binding affinity, just whether
*  or not the two are going to interact at all. And having that as more of a binary sort of
*  classifier, not so much like a ranking sort of thing. So having structure be a part of your
*  protein-protein interaction prediction model seems very fundamental to me in a lot of ways. You need
*  that geometry, you need that awareness of the geometry to really have a high-quality prediction
*  of a protein-protein interaction. And I think this would transfer over to other types of
*  interactions as well. This should work for if I design a protein to bind to DNA or something,
*  maybe I'm designing a CRISPR analog or something like that. The same sort of method or some
*  variation on it should still work for those kinds of complexes as well. So I personally don't see
*  any getting around having structure as part of your protein-protein interaction prediction.
*  I don't know that sequence alone is enough. That's just an opinion based on what I've seen
*  in what I've read and just kind of some vibe checks, I guess, and what has been working and
*  what has not been working so far. And it seems like structure is pretty key. So I think something
*  like AlphaFold3, maybe not AlphaFold3 itself, maybe it's some kind of stripped down,
*  streamlined sort of version of it, or maybe they use flow matching instead of diffusion so that
*  they can speed up the inference or something like that. There's different things that you could do
*  to kind of modify AlphaFold3 to make it a little better for protein-protein interaction screening.
*  But I think something like that is going to be the right way. If you need a high-quality
*  prediction, that's going to be the way to go.
*  So just to try to recap, make sure I kind of understand the general progression. If you're
*  designing something, you start with a target, you have a sequence of a target, you may or may not
*  have a shape of a target, I guess. And then you would design first with, and we covered a little
*  bit of this last time, different models for different parts of this process. First, you're
*  designing the shape of the thing, the general shape of the thing that would bind. Then you're
*  filling in the actual sequence of amino acids that would hopefully fold into that shape.
*  And then you're validating that with an AlphaFold2, or now obviously you've got an AlphaFold3 as well,
*  and kind of using that to confirm that these other models came up with this, and now we can say,
*  yes, it actually does look like it would work. And so that can be used when you have a single
*  target or now it's maybe getting good enough, and potentially with inference efficiency improvements
*  in particular, that you could begin to just brute force. We obviously know the genome,
*  we know lots more protein sequences than we know what actually interacts with what.
*  So we could, in theory, I don't know if this is practical, how much compute
*  would it take? Could we just say, hey, what do we have? Tens of thousands of proteins ourselves?
*  I guess that wouldn't be that crazy to just start to go 10,000 squared is only, what, 100 million?
*  LESLIE KENDRICK Yeah. I mean, they actually did this. So when they fine-tuned this model
*  for predicting protein-protein interactions, this stripped down version of RosettaFold,
*  they actually did it for the human proteome, and they predicted all the possible pairwise
*  interactions for the human proteome, and discovered quite a lot of new interactions that weren't known
*  before that were high-quality predictions, and got a good precision recall curve.
*  Like the area under the precision recall curve was pretty good.
*  Can you unpack that concept? That's basically just saying, for a given confidence level,
*  how much do you actually capture versus how much false positives you're bringing in?
*  LESLIE KENDRICK Right. Yeah. So the precision is about false positives, and the recall is about
*  how much you remember out of how much is actually there. And then you've got a curve. If you put
*  precision on one axis and recall on the other axis, and then plot a curve, and then look at
*  the area under that curve, that gives you a metric of how well the model is doing.
*  So the slow part of this protein-protein interaction screening process is really
*  generating the MSAs. So if you need to generate an MSA to predict a protein-protein interaction,
*  it takes a while. It's not a very quick process. And so if you can somehow find a way around that,
*  that would speed up the screening step for picking out which pairs actually do interact.
*  And I have some ideas on how one might go about doing that. I am in the process of testing some
*  of them out. And I also have some other ideas that may help improve the MSAs, especially for
*  sequences that are considered like Twilight Zone proteins, if you've ever heard of that.
*  So a Twilight Zone protein is a sequence that has very low sequence identity to other sequences.
*  And so it's really hard to build a nice deep MSA for them. So when you're trying to build
*  multiple sequence alignments and you're computing sequence similarity to find your homologs,
*  you can't find very many of them. And the ones that you do find are pretty low sequence identity
*  to your reference protein. And so there's a method that came out maybe two years ago where
*  they use a protein language model to do homology search inside of a database of embeddings. So
*  they convert like UniREF 100, for example, into a bunch of embeddings. So each protein sequence
*  has some embeddings associated to it using something like ESM2 or ESM3 or whatever.
*  Then you use like cosine similarity or something like that and compute similarity between the
*  embeddings to find your homologs instead of computing sequence similarity. So you're
*  looking at similarity inside of embedding space instead of inside of sequence space.
*  And it turns out you can capture similarities that aren't encoded. Let me put it this way.
*  So structure is more conserved than sequences. And so you can have two proteins that have similar
*  structures but that don't have similar sequences. And so this method would pick up on such things.
*  And if you use this to construct your MSAs, you can get better results for proteins that have
*  this property that they're really hard to construct MSAs for. So I'm in the process of testing that
*  out and using another method to construct the MSAs itself. So once you have your homologs,
*  you have all your similar sequences in a big list, I think you want to actually perform the
*  alignment. And you don't perform the alignment in sequence space. Again, you perform the alignment
*  inside of embedding space. And so you're aligning vectors in embedding space that represent the
*  amino acids at each residue. And again, using like cosine similarity or something like that to figure
*  out which vectors in embedding space are the most similar to each other so that you can align those.
*  And you end up getting some alignments that often look very much like traditional multiple
*  sequence alignments. But sometimes you'll get funny alignments where like residues get lined up in a
*  way that's a little bit strange because you're aligning in embedding space instead of in sequence
*  space. But hopefully that ends up working a bit better. And if it's fast enough, I think that might
*  be a really good way to go for protein-protein interaction screening because the MSA process,
*  if it's fast enough, would be I think higher quality. And then you could use something
*  lightweight to predict the protein-protein interaction. You wouldn't have to actually use
*  alpha fold three per se. You could use some stripped down version of Rosetta fold or something
*  like that, for example. And that's actually pretty fast. So the actual step where you run
*  the fine-tuned version of Rosetta folds to predict the protein-protein interaction,
*  that's actually a pretty fast step, not very slow. It's the MSAs that are really slow.
*  And so as long as you have a way around MSAs, you're fine.
*  **Matt Stauffer** Yeah. Let's revisit MSA for a second. This is a way of identifying what is
*  highly conserved and therefore like critical to function versus what is not so highly conserved
*  and therefore not so critical. And that is fed into a lot of these structure prediction models.
*  But you're saying that that calculation itself is what is slow.
*  **Samantha Niedra-Morris** Calculating the MSA, yeah, is very slow.
*  **Matt Stauffer** So the alternative is to then do it in embedding space,
*  which I don't have an intuition for why that would be faster, but I take your word that it is.
*  **Samantha Niedra-Morris** Yeah. So I guess the idea would be like, convert everything into vectors
*  and then maybe have something like an indexed vector database or something like that.
*  I guess that would be the ideal setup for this. And yeah, I don't know that it's going to be a
*  lot faster. That's still kind of iffy. Still trying to figure out how fast it is exactly.
*  I think actually computing the alignment itself will be fast when you're aligning in embedding
*  space. Actually computing all the homologues, I'm not sure about. I think that's going to come
*  down to like how good you query your database. But yeah, to be determined.
*  **Matt Stauffer** Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Even if you think it's a bit overhyped, AI is suddenly everywhere from self-driving cars,
*  to molecular medicine, to business efficiency. If it's not in your industry yet, it's coming
*  and fast. But AI needs a lot of speed and computing power. So how do you compete without
*  costs spiraling out of control? Time to upgrade to the next generation of the cloud,
*  Oracle Cloud Infrastructure, or OCI. OCI is a blazing fast and secure platform for your
*  infrastructure, database, application development, plus all your AI and machine learning workloads.
*  OCI costs 50% less for compute and 80% less for networking. So you're saving a pile of money.
*  Thousands of businesses have already upgraded to OCI, including MGM resorts, specialized bikes,
*  and fireworks AI. Right now, Oracle is offering to cut your current cloud bill in half if you
*  move to OCI for new US customers with minimum financial commitment. Offer ends 12-31-24. So
*  see if your company qualifies for this special offer at oracle.com slash cognitive. That's
*  oracle.com slash cognitive. As a developer, the journey from concept to production-ready
*  large language model apps is fraught with challenges. Dealing with unpredictable language
*  model outputs, hallucinations, and ballooning API costs can all be blockers to shipping your next
*  AI-powered feature. That's where advanced RAG comes in. With the new RAG++ course from Weights
*  and Biases, you can overcome these hurdles and build reliable production-ready RAG applications.
*  Go beyond proof of concept and learn how to evaluate systematically. Use hybrid search
*  correctly and give your RAG system access to tool calling. Based on 21 months of running a customer
*  support bot in production, industry experts at Weights and Biases, Cohere, and Weaviate show you
*  how to get to a deployment-grade RAG application. This offer includes free credits from Cohere to
*  get you started. Make real progress on your large language model development and visit
*  wnb.me slash cr to get started with their RAG++ course today. That's wnb.me slash cr to get
*  started with their RAG++ course today. So I'm going to ask some dumb questions.
*  Okay. If there's a hundred million possible interactions and people already have done the
*  whole thing. To take the really, really naive question, I think a lot of people, myself included,
*  heard, oh my God, Alpha Fold, now we can predict all the proteins. This is amazing. Does this mean
*  everything is solved? And it was like, well, evidently not because there was an Alpha Fold 2.
*  And it could do more stuff. And now we have Alpha Fold 3. And it can do all of life's molecules. So
*  that's pretty intuitive. Okay, the original one predicted structures of proteins. Now this can
*  predict the way that different kinds of, not just proteins, but RNA and DNA, whatever they can all
*  interact with each other. But if we've already gone and run all that and have identified lots of new
*  interactions, where does that put us on the process of mapping out all these interactions?
*  Did that find just a small percentage of what remains to be found? Or do you think it may be
*  found a large percentage of what remains to be found? And what can Alpha Fold 3 not do
*  still yet that we, you know, like what remains unsolved?
*  Yeah, so a lot, actually. And I will say, like, any static structure prediction model is not going to
*  get you everything that you need in all circumstances. It's like, if you're going
*  to do a protein engineering task that amounts to something like binder design or motif scaffolding,
*  you're probably fine not worrying about molecular dynamics too much. But if you like, for example,
*  let's say you wanted to build a new enzyme, and you want it to catalyze some new reaction,
*  maybe even a completely new reaction that nobody's ever seen in an enzyme before, maybe it's completely
*  new to nature, and you want to catalyze this reaction, that's a tricky process. That's
*  trickier than binder design, because there's work showing that there are multiple things that are
*  important to catalysis that are not immediately obvious. So when you have a binding pocket inside
*  of an enzyme, there are sites inside of the binding pocket called catalytic sites, or catalytic
*  residues, or sometimes people call them active sites. These are the important residues inside
*  the binding pocket that actually perform the catalytic reaction or that cause the catalytic
*  reaction and perform catalysis. So catalysis is like, basically, you know, an enzyme eats some kind
*  of small molecule and then converts it into some products. You can think of it as like a cleaving
*  process where you're like pulling apart the molecule into products of the reaction. And
*  the process is inherently dynamic, like catalysis is a dynamic process. And to really design an
*  enzyme that performs the catalysis that you want, and has a good turnover, you have to take into
*  account not just the catalytic sites and where they're placed in relation to the substrate,
*  the small molecule that's getting converted into products. You also need to consider all the binding
*  sites, you need to consider the side chains around the binding pocket. And it's also been shown that
*  even the dynamics up to about 20 angstroms away from the catalytic sites is actually important
*  for catalysis. And if you want to design a new enzyme that performs this catalysis, you need to
*  take into account all of these things, you need to take into account all the binding sites and active
*  sites, but also the side chain confirmations that they have, not just the backbone configuration.
*  And then also the dynamics of the protein itself within about a 20 angstrom radius of the active
*  sites. So when you're going to design a new enzyme, one way that you could do it is start with a known
*  enzyme, pull out the active sites, the catalytic sites, and then run motif scaffolding with RF
*  diffusion to build a protein around the active sites. And this kind of works, but you have to
*  do a few special things to get it to work well. So one thing that you need is you need some way of
*  modeling the conformational ensemble between the ligands, the substrate, and the enzyme.
*  And if you have some way of modeling the conformational ensemble of the complex,
*  you can compare your designs and show the dynamics within a 20 angstrom radius and the side chain
*  confirmations and the active site arrangements are all favorable, they're all matching up within
*  some error thresholds. And so probably what's going to happen is catalysis is going to be preserved
*  and we're going to have a new protein that performs catalysis that we can hopefully then
*  optimize for higher turnover. And then you go to optimizing once you've scaffolded in your active
*  sites and such and analyze your dynamics and your side chains and whatnot. But there's a new model
*  out now that allows you to generate de novo catalytic pockets called enzyme flow. So it's
*  a flow matching model, which we'll probably get into a little bit, talk a little bit about like
*  the relation between flow matching and diffusion, but it's a generative flow matching model and it
*  generates catalytic pockets. And then you can take those catalytic pockets and scaffold them into a
*  full protein with RF diffusion. And then you can analyze the side chain confirmations and the
*  conformational ensembles using another model that Baker Lab came out with called ChemNet.
*  What ChemNet does is it allows you to dock the substrate to the enzyme and get out an analysis
*  of a conformational ensemble of that complex. And using ChemNet, you can tell, okay, are like all
*  these side chain confirmations right? Am I getting the right confirmations? And you can use that as a
*  ranking step when you're designing the enzymes. And so that ends up going in the middle of that
*  pipeline that I was describing before. So you would have enzyme flow first to generate your
*  catalytic pocket. Then you would go into RF diffusion to scaffold that into a full protein.
*  Then you would go into like protein, well, ligand and PNN in this case, because ligand and PNN
*  understands the substrate molecule. And once you've designed your sequence with ligand and PNN,
*  then you want to use ChemNet to get those conformational ensembles and analyze those
*  side chains and figure out how to rank your designs in terms of how favorable the side
*  chain confirmations and such are. And then, you know, there's also some structure validation
*  and stuff to make sure that the design structure that you have predicted matches up with the
*  structure that you generated in the beginning. And that whole workflow gets you to new enzymes.
*  And then you can turn that into an iterative setup where you feed it back into itself and
*  iterate on the sequence design step and get an optimization loop for these things. And sometimes
*  this will boost your turnover and you get higher catalysis. So I guess like, you know, what is
*  needed beyond the structure prediction, beyond AlphaFold 3, for example, would be something like
*  modeling conformational ensembles. So like using tools like ChemNet from Baker Lab, or another tool
*  that we should definitely talk about that I think will be useful for this, potentially after some
*  fine tuning, maybe as is, but maybe some fine tuning is needed, is MDGen. So MDGen is a generative
*  flow matching model that is very much like a Sora for molecules. And you can generate molecular
*  dynamics trajectories with it. And it was shown to have better performance than AlphaFlo.
*  So that's very encouraging because it was trained on the same data set. So it was trained on Atlas.
*  And that's a kind of a smallish dynamics data set, but it's a reasonable sort of benchmarking
*  sort of data set. They trained MDGen on Atlas and showed that it had noticeably better performance
*  than AlphaFlo. And I'm of the opinion that if we train such a model further on more high quality
*  molecular dynamics simulations, we will have something incredibly useful. Because MDGen doesn't
*  just generate molecular dynamics trajectories. Like I can give it a static structure of a protein,
*  like a predicted structure or a structure from the PDB or whatever, and have it generate my
*  trajectory of whatever length I want. And it also is able to do several other things that you just
*  you can't do with molecular dynamics. Molecular dynamics just will not do this. Let me just go
*  through all the things it does. So it generates trajectories, it upsamples. So if I have a coarse
*  grained molecular dynamic simulation, or if I have something that's coarser than I would like,
*  I can upsample it with MDGen and kind of like fill in the missing frames and make it a higher
*  resolution. I can also interpolate between two states, which is really helpful for as long as
*  it's reversible, could be really useful for like binding free energy calculations. Because if I
*  have a reversible interpolation between two metastable states or something like that,
*  I can use that to calculate binding free energies. And so it will interpolate between two
*  metastable states or two conformations. And it also will do inpainting. And the inpainting
*  is really interesting to me for multiple reasons. So it was originally trained on monomers. So it
*  just understands single proteins. It doesn't understand complexes. It doesn't understand
*  a protein like an enzyme eating a substrate. It doesn't understand DNA or RNA or anything like
*  that. It just understands single proteins by themselves, right? But if you were to train it
*  on complexes, you might have something coupled with the inpainting functionality, where you could
*  design really interesting like new binders, because the binders would have like dynamics
*  that are favorable to the interaction that you want. So when you do the inpainting with MDGen,
*  basically what you're doing is masking out some part of the trajectory, some part of the molecule,
*  and having it fill in the molecule inside the trajectory so that the generated part has dynamics
*  that match up with the rest of the part that you didn't mask out, which is pretty wild to me. I
*  think that's really wild, being able to inpaint in a molecular dynamics trajectory and have it generate
*  a new molecule for me that matches the trajectory around it, right? Like that's pretty wild.
*  And that's not something that we've seen before. That's new. That's a completely new sort of thing
*  that I don't... And that just came out. That's like fresh off the press. So
*  that hasn't even had time to digest in the community yet. People haven't even had time to
*  really comprehend what does that mean to be able to do inpainting inside of trajectories. That's
*  a pretty new thing that I don't think anybody really saw coming. I mean, maybe some people who
*  are really deep into the AI stuff and knew about Sora, but also were interested in biochemistry
*  stuff, maybe. Some people saw it six or eight months ago. Inpainting in molecular dynamics
*  trajectories is pretty interesting, pretty useful potentially. So I'm excited to see where that goes
*  and what people do with that. And I think that's kind of... To really get back to answer your
*  question, put a period at the end of my tome that I just wrote, I think what's missing is dynamics,
*  right? We need to understand the function of the protein. To understand the function of the protein,
*  sometimes you need to understand more than just a static structure. Sometimes you need to understand
*  the dynamics. And there are lots of properties of proteins that we might want to predict that
*  require some kind of dynamics. Like I was saying before, binding free energy calculations and
*  things like that. Having the ability to interpolate between two states, that's also a really useful
*  capability. And I think these pieces are starting to get filled in. So we're moving away from static
*  structure prediction and into Boltzmann distribution sampling, basically, or generating trajectories.
*  And I don't think it's going to be that much longer before we have something like MDGEN that
*  is comparable in quality. Maybe it's not quite as good because it's being trained on molecular
*  dynamics. So it can't technically ever be better than molecular dynamics in terms of accuracy,
*  whatever that means in this case. But you can certainly approach the quality of MD, right?
*  Like you can asymptotically approach that and get really close. And if we have a model that
*  will generate trajectories for us a thousand times faster than molecular dynamics will generate
*  trajectories for us, and we have these additional capabilities to do inpainting and interpolation
*  and upsampling, that seems really, really valuable to me. Like we go from having a month-long
*  simulation down to having something that happens in a few hours. Like you might have a really
*  complicated system that takes a month to simulate so that you can get a long enough trajectory.
*  But now because of MDGEN, it's a thousand times faster. It takes me a few hours,
*  which means I can generate a huge volume of trajectories for a lot of different kinds of
*  molecules and do high throughput things that I couldn't do before. It just fundamentally
*  changes the way that you're doing things because all of a sudden things that were not high throughput
*  before are now high throughput. And so like maybe you lose a little bit of accuracy because you're
*  training on molecular dynamics and you're using a neural network instead of the molecular dynamics
*  itself or some other approximation of ground truth. But the little bit that you lose in accuracy
*  is going to be just more than made up for in how high throughput things become. Because all of a
*  sudden you're able to do a thousand times more than you were able to do before. You're able to
*  test a thousand more hypotheses than you were able to test before. And the accuracy hit that
*  you're going to take is negligible. I mean at the moment I wouldn't say it's negligible, but I think
*  like in the very near future it will be. We have enough molecular dynamics data that's good enough
*  quality to push MDGEN I think close enough to molecular dynamics that it will be useful.
*  And you know there may still be like situations where I need the accuracy of molecular dynamics
*  or I need some other specialized method that has their accuracy or something like that. But
*  you know as a general rule like I would think for average situations that aren't really
*  difficult tricky ones like MDGEN is probably or something like MDGEN maybe not MDGEN as it is
*  right now today. But something in the very near future like MDGEN maybe even MDGEN trained a
*  little more on a better data set I think will be incredibly useful. I don't want to say that it's
*  going to come and replace molecular dynamics right because one the molecular dynamics people will not
*  be very happy with me if I say that. And two I'm not really 100 sure that it's entirely true. But
*  I do think it's probably going to eat a chunk of molecular dynamics and that is something that I
*  think people are going to have to kind of try to live with a little bit because maybe it doesn't do
*  everything as accurate as molecular dynamics and it doesn't do all the same things that molecular
*  dynamics does. But it's still going to be really useful. Like it doesn't need to replace molecular
*  dynamics to impact molecular dynamics and like maybe take a chunk out of it and offer a new way
*  to do things that's more effective in some ways. Let me try to rebuild up some of these
*  intuitions and make sure I'm kind of getting the right takeaways.
*  What is the current frontier is one question and the answer there is dynamics versus statics.
*  Jared Ranere I think so, yeah.
*  Kyle Sosnowski And when I think about kind of these giant enzymes, proteins, catalyzing reactions,
*  I sort of visualize kind of an assembly line honestly, which is I don't like analogies,
*  but that is kind of the picture that's coming to mind where it's like it's not only that you have
*  to have the shape of the machinery, right, but it also has to move in the right ways and kind of
*  go in the right sequence or it's not going to work because these things do have to happen in
*  an order, right, or they fall apart. So the sort of one shape to another shape to a third shape,
*  whatever, these multiple shapes are important and the way that they move from one to another
*  is also important. So you can now do something where you start by designing this active pocket
*  and this is like really very sort of, it sounds like pretty mechanical almost, right, where you're
*  like, if I want this, I guess to even zoom out one step further, this takes me back to my early
*  chemistry days, it's like a lot of reactions that you might want to do you cannot do at room
*  temperature or they would be prohibitively slow or they just won't happen at all or and if you
*  did turn up the temperature, you might be able to do them, but then you would like kill the cell or
*  whatever, right? So you have these transformations that are maybe possible in some other way, but
*  for them to happen within the limitations of like what life can survive in, they have to have this
*  guided process where the enzyme is actually bringing things together or pulling them apart
*  or doing like physical spatial manipulation in order to promote the chemical changes that
*  need to happen. So you now say, okay, I want to do some reaction, I want to design an enzyme that
*  can do this particular reaction. You start with designing that active site, which is like the
*  sort of, and in a way, this kind of recalls some of my best practices as far afield as this is from
*  regular old app development with AI models. One of my mantras is do the hard part first. It's like,
*  make sure that your AI can actually do the task that you want it to do before you build all the
*  surrounding stuff. Sometimes I call that the plumbing and that is how is data going to come
*  in from here and there and whatever. This is, again, I don't trust analogies too much, but
*  just trying to grasp onto things because this is such a nuanced field that I know so little about.
*  In a way, it's like do the hard part first. Figure out what is the shape at the kind of core of this
*  reaction that is going to do the manipulation that is needed to make the reaction happen
*  under the conditions that life can handle. Once we have that kind of core shape, now take a different
*  model and figure out how to scaffold that with some larger protein superstructure. My understanding
*  is that's like orders of magnitude bigger often than the active site. The active site might be
*  quite small. The protein that surrounds that and brings it together might be comparatively huge.
*  I guess the hugeness of that is really just a function of we only have so many,
*  there's only what, 20 amino acids and they can only be put together in a chain. You end up with
*  weird shapes because these are the building blocks that you have and sometimes you have to
*  get convoluted, I guess, to basically come all the way back around and assemble this active site
*  together. You do that at a structural level, you do that at a sequence level, you start to then simulate
*  I guess even then down to the side chain level and the super fine grain stuff.
*  Then with these MD molecular dynamics models, I did an episode with a guy named Tim Dagnan out of
*  Australia who is doing something very similar for modeling ionic solutions. Literally, we're just
*  talking about salt water in a lot of that episode. But a similar thing where he was saying, I can take
*  a supercomputer and go simulate this stuff, but it's super, super slow. He was working at femto
*  second scale and then the big, why go to a model as opposed to doing that calculation?
*  Well, because the numerical methods that we have for solving the wave equation to propagate
*  one time step in the molecular dynamics process are really slow and the model can
*  learn to guess or intuit the solution to the wave equation orders of magnitude faster,
*  which allows you to do much more time steps with the same amount of compute.
*  In his case, the big reveal was that they saw crystallization happening in a salt solution,
*  even though they hadn't trained on that. It was just like that is what, obviously,
*  physics does include that. As they were able to run these things longer, they were able to see,
*  like, hey, look at this. We do see actually crystallization that we know happens happening
*  in the simulation. We couldn't have simulated it this long with the traditional numerical methods,
*  but with the model filling in for the numerical solution to the wave equation, then it becomes
*  like something that is within the computational budget to get to. That's kind of similar here
*  and probably even a more challenging thing because you got crazy huge molecules.
*  Help me with the... When we do these molecular dynamic simulations, we're now,
*  or models that imitate that, we're now able to see these trajectories are the actual
*  movement of the proteins, right? The thing folds and the active site comes together,
*  and then it folds some other way and the other part of the active site or whatever.
*  I think I got all that. How does the in-painting work or what questions does that
*  help us answer there? Maybe it would help in other workflows more because I feel like we're so
*  deep down the rabbit hole of simulation here that I'm not sure what I'm masking and in-painting.
*  Maybe I need to come at it from a different task and imagine how that would be useful given
*  a different story of why I'm using that thing. I can think of two example use cases. One is binder
*  design. This could be a new way to do binder design. If I in-paint a binder, basically,
*  once I've trained on complexes and that maybe that's a protein binder. Maybe you train on small
*  molecules too and you have small molecule binders. The possibilities are really interesting.
*  And then the other use case that I could think of is enzyme design. Again, here again, if you had a
*  catalytic pocket either generated from enzyme flow or pulled out of a known protein, you could then
*  in-paint around that and generate an enzyme around your catalytic pocket. So that's two
*  applications I could think of immediately. And I could see it being useful for those two in cases
*  where the dynamics are important. So maybe you need some kind of control over how transient the
*  interaction is. Maybe I want to design a binder that has an interaction that lasts for a certain
*  amount of time or has a certain probability of dissociating after a certain amount of time.
*  And if I want to have some fine-grained control over what that probability distribution looks like,
*  I need some kind of fine-grained control over the dynamics and MDGEN would be the way to do that.
*  And similarly for proteins, because the dynamics are important and you don't just want to preserve
*  the dynamics around the active sites, you also want the dynamics away from the active sites to
*  be compatible with the dynamics around the active sites. And so doing in-painting of stuff to generate
*  more of the enzyme or to generate a new enzyme, that would be another use case that I could think of.
*  So let's zoom out a little bit from this workflow and kind of maybe try to help me understand better
*  the context that it happens in. And there's maybe multiple different angles we could take on that.
*  One is what sort of software platforms are people doing this stuff in? Another would be
*  what sort of value chain, how does this fit into the overall value chain?
*  Also be really interested to know what is the success rate? So if we were to
*  say, kind of again, working from the inside out, we've got this sort of workflow where
*  given a target, we can sort of work through this design process. In what companies are people
*  kind of doing this work? How are the targets coming to them? How long does it take them to
*  work on a problem like this? What do they come out with in terms of how many candidates? How often
*  are they able to be successful versus not successful? What are they handing off to the
*  people that are then going to go do the actual real world experiments?
*  I would divide it into two categories. I would divide it into industrial versus medical.
*  So if you're designing proteins for industrial applications, you're going to have a faster
*  process than if you're designing proteins for medical applications. For just the very obvious
*  reason that if you're doing medical applications, you have a whole process to go through to make
*  sure that it's safe for humans. And then for industrial applications, it's a little less
*  tricky because you're not putting it into a human. I mean, in some cases, you still need to worry
*  about safety and things, of course, but it's not as hard as I think medical applications are.
*  And as far as the ecosystem, the demand, what kinds of software is being developed, I think
*  open source right now is very disjointed in a lot of ways. A lot of the heavy duty software
*  and workflows are closed source at the moment. They're inside of big drug companies who are
*  collaborating with these smaller AI labs. And there is one exception to that though, I will say.
*  So Nvidia is looking into making a lot of open source endpoints available,
*  APIs, they're using these things called NIMS, and they are sort of like orienting themselves
*  towards designing useful workflows that don't just run a single model, but run a whole workflow of
*  models, a whole chain of them or a whole loop or whatever kind of graph you want. So there's
*  definitely movement, but a lot of the movement is happening in closed source places. And so I think
*  open source in a lot of ways is still very much like, okay, I need to pick out the models I want
*  to use, I need to go and set up the conda environments or the dockers or whatever, I need to
*  download all the model weights and set everything up and maybe even do a fine tuning run or a training
*  run or something. And it's still very much like rolling up your sleeves, getting your hands dirty
*  and doing things by hand in a lot of ways. Like there aren't a lot of open source solutions for
*  designing these workflows and implementing them and using them with a few small exceptions.
*  And I will say, you know, that is changing. Obviously, people are starting to think about
*  these things, but there, I think a lot of the movement that could be happening in the open
*  source space is getting scooped up. And so it's happening in closed source areas more.
*  It's interesting that what I'm taking away from your answer there is just that these things are
*  all so new that nobody much outside of maybe a few companies that are right on the edge and
*  investing heavily in it have anything that kind of ties this all together. Like there's no zappier
*  for this. There's just a bunch of labs have put out their models and now they're out there.
*  But the work of understanding like what is the constellation that we have,
*  how would that be assembled into productive workflows that has not been finished or people
*  are kind of ad hocing it themselves and not working on any sort of standard program at this point.
*  Do you think that there are, you know, when I said like what's missing from Alpha Fold 3,
*  the dynamics versus static was the big answer. But then obviously we've gone on to talk about
*  lots of different things that seem to add up to an overall workflow that can do the dynamics.
*  So I guess would it be accurate to say that like Alpha Fold 3 is kind of doing a really
*  good job of one generation of the tech and all these other things are like pushing into the next
*  generation, but they're not as big a data set, not as big a compute, whatever, but they're kind of all
*  chipping away at the problem and showing pieces. And maybe what you would expect from Alpha Fold
*  4 would be like a lot of that stuff coming into a single system with even more kind of refinement,
*  bigger data and ultimately higher performance. Yeah. So I guess one thing I want to say is like,
*  the way it is now, you still need a static structure to start with to feed into your MDGEN
*  or your distributional graph former or whatever AI model you're using to generate something like a
*  Boltzmann distribution or a trajectory. You still need to feed in a static structure. And so if you
*  don't have a PDB structure, you'll need to predict it with something like Alpha Folds. So for the
*  time being, at least those two aren't integrated into a single model. You could certainly do that
*  and I'm sure somebody will eventually, but at the moment it's like a two-step thing. I need to
*  predict structure first and then I need to feed that into my trajectory model or Boltzmann
*  distribution model or whatever to get the dynamics. So I wouldn't say that it's the next stage or like
*  it's replacing or like a new phase of evolution or something. I think maybe once somebody has
*  integrated those two into the same model and it's like structure prediction and dynamics all at the
*  same time in one model, then I would say, yeah, that's the next generation. That's replacing Alpha
*  Fold and that's what's coming next. And this is the new paradigm now for functions. Yeah.
*  So what would you say is the like, this is sort of in a medical context, this is all upstream of
*  creating a drug candidate that would eventually go through clinical trials, right? And so people
*  are sort of familiar with thinking of the pipeline there of phase one, phase two, and there's fall
*  out at each stage, right? Is that a productive way to think about what the design process looks
*  like today? If somebody says, hey, here's a challenge, we need something that binds to this
*  thing. And you're going through this workflow that has kind of tacked together all these
*  different models. For any given challenge, is it like, how likely is it that you'll ultimately be
*  able to get something that actually works out of this workflow? And where are the drop offs? Like,
*  what are the pain points in a very practical sense between sitting down to do this and coming out
*  with something on the other end? Yeah, for like success rates, I guess, like there again, I
*  like hesitate to give like a black and white answer, because it's really going to depend on
*  the design task and the target. So, you know, like, motif scaffolding, like if I have two binding
*  domains to two different proteins that I want to scaffold into a new protein, so that I have a
*  protein that's by specific and binds to two different things at the same time, like, that
*  is not so bad. Like the success rate of something like that would be relatively high, like,
*  and depending on the proteins, like I might have like a success rate of like one in 50 or something
*  like that. On the other hand, one in 50 means like one in 50. What one in 50 times you can succeed at
*  all or like one in 50 attempts work? So like, let's say I have a bunch of designs and I rank
*  them using some kind of ranking metrics, and I send 50 of them into the wet lab to see which
*  ones of them actually ended up being by specific and had a good binding affinity to the two targets.
*  That would be a hit in this case. Gotcha. Okay, so the way to think about it is how many
*  designs do I need to generate to get one that actually works? Right. Yeah, in the wet lab,
*  like initial wet lab testing for like binders. Now, for something more complicated like an enzyme,
*  your success rate might be lower because the design challenge is harder. You have to take
*  into account more things. You have to take into account the active site arrangement,
*  the side chain confirmations, and the dynamics up to about 20 angstroms away from the active sites.
*  And so having to take all that extra stuff into account, you need some extra models so that you
*  can model all those things. And like what the success rate in that case might be with these
*  newer models is to be determined, but still a lot higher than I think it was before,
*  like significantly higher than pre-AI methods for such a challenge for designing an enzyme.
*  But yeah, the success rate is going to go down for something like that for sure, because
*  the different things you have to take into account are just a lot more complicated.
*  And so I would expect, oh my God, I don't know if I even want to give a number for something like
*  that, but it might be something more like one in a thousand or something. I don't know. It really
*  just depends on the target, depends on the models that you're using, and it depends on the task that
*  you're going after for the design challenge that you're doing. And these would be all things that
*  passed the, like the one in 50, those 50 all passed all of the digital validations that you could
*  throw at them. Right, exactly. And the success rate could even be higher than one in 50. I mean,
*  there are some cases where they, like in the new Alpha Prodeo model that DeepMind and Insilico or
*  Isomorphic released, or they didn't really release it, but they trained it. Their success
*  rate for some of their targets were really high. Like I know one of them was like an 80 something
*  percent success rate. And then for others, it was like 9%. So it could be a whole range of things,
*  and it really just depends on the design task. How is the initial target specified? I keep falling
*  back to this like binder notion, because it's pretty intuitive for me to think, okay, we have
*  this molecule. We need something to bind to it. Relatively simple. If you are trying to design
*  an enzyme and you're trying to catalyze a reaction, presumably you have less of a, maybe not,
*  but it intuitively feels to me like you would have less of a well-defined starting point,
*  because there's presumably much bigger space of ways that you could catalyze something.
*  How does that starting task definition look in the first place for something like that?
*  Can you reword that maybe? I think I had trouble following that.
*  Yeah, well, I'm groping around a little bit. Okay, so going back to the binding. When there is a,
*  here's a protein, we need to bind this protein. Okay, well, we know what the protein is, so we
*  know what shape we need to bind to. That seems like reasonably well-defined. But if you are trying to
*  do some new industrial process, catalyze some reaction in vivo, whatever, ultimately,
*  it seems like you have less of a well-defined task in the first place. How to catalyze this reaction?
*  When you start with this active site prediction thing at the heart of it, I don't even have a
*  really good intuition for what would be the definition of the task there. We want to do
*  this reaction, but presumably there's just a lot of ways you could catalyze any
*  given reaction, as opposed to a single thing that you want to bind to.
*  I would say that when I think of the catalytic process, actually the reaction that's happening
*  itself and the movement of the protein, it's very precise and very conserved in my mind. That seems
*  almost too defined because it has to be so precise in order to function. And any deviation from that
*  destroys the catalysis. It's a very fragile geometry, really. You have to get the geometry
*  just right so that it fits with the substrate and then pulls it apart or something.
*  I guess that is the task definition is a geometry. It's like we need to have something that can
*  put these two molecules into this geometry so that they react, and that is known.
*  Yeah, so I guess enzyme flow, for example, is conditioned on reactions and enzyme commission
*  classes. So I would give it a reaction that I want it to catalyze, and I would give it an EC number
*  and condition it on those, and then it would generate the catalytic pocket for me, which is
*  the geometry that I need. It arranges the catalytic sites the way that they need to be arranged
*  for you.
*  Gotcha. Okay. How far can you push this? I was recently reading a little bit about
*  even better DNA editing technique that's been discovered. My understanding is that this
*  evolved. It wasn't engineered, but the technique is bridge editing. And I guess I'm wondering,
*  if you had something that ambitious laid out as a protein design task, are we anywhere close to
*  being able to take on something so crazy, or is that... Like designing a new enzyme, like a
*  CRISPR analog or something? Is that what you're saying? Yeah, this thing is like... Yeah. Although
*  I'm imagining in a way where you couldn't condition on existing CRISPRs, not to say
*  variation on something, but take a job like that, like a big complicated job in a cell,
*  and try to generate a new way of doing it. Right. Is that totally impossible still? And
*  how do we know where the boundary is for how ambitious we can be with today's tools?
*  I think we can get pretty ambitious. I've seen a lot of weird stuff happening over the past year.
*  I saw a lot of really interesting engineering projects, or I don't know, protein engineering
*  projects that people did at RosettaCon, for example, this year were very inspiring,
*  to say the least. I would say I saw a lot of people doing some really interesting things.
*  I saw people designing stereo selective enzymes that select for a left-handed version instead of
*  a right-handed version of a molecule or something like that. I saw people designing
*  mechanical degraders that pulled apart the needle complex of bacteria so that the bacteria couldn't
*  infect the cell. And they were actually able to pull apart the needle complex of the proteins
*  that they designed and prevent infection. I saw so many things that I was very inspired by. I was
*  like, okay, this could get really wild really soon. Because if you just have a little creativity
*  and you're a little persistent about it and you're mechanically minded, a lot of these problems
*  do translate into mechanical engineering problems. Not all of them. There are plenty of cases where
*  you need to understand something deeper than just the geometry and the mechanics of it. But
*  a lot of very valuable, useful cases, you can actually boil a lot of this down to a very
*  mechanistic engineering problem that doesn't involve a lot of traditional drug design techniques.
*  As far as what is possible in the near future, I would say don't expect a miracle, but certainly
*  some interesting and surprising things are going to be happening. I'm trying to think of some other
*  good examples that I could pull from RosettaCon because there were a lot of really good ones.
*  They designed multi-step enzymes that had four steps in the catalytic process. There were multiple
*  examples of people designing functional enzymes that performed some kind of catalysis that was
*  really important for the problem they were working on. Designing a multi-step enzyme has four
*  complicated steps in the catalysis process. I would say that's a pretty big one, and they did it.
*  They were able to actually do it. It just required a little bit of determination and
*  being a little bit clever about the mechanics of the problem and thinking about it in terms of
*  an engineering problem. Is this something that people are looking at with 3D
*  visualizations? Is there good software to help with that? Or how are they, in very procedural,
*  practical terms, turning all this sequence and related data into something that they can have
*  mechanical engineering intuitions about? Just visualizing a PDB file can give you a
*  lot of intuition. That's pretty simple. Just pulling up a PDB file in MolStar or something
*  like that on the PDB itself. I think just spending some time analyzing how things fit together,
*  what kinds of motions things could have based on their geometry. That's getting a little bit
*  contentious because you don't really know the dynamics a priori from just the structure. You
*  need to understand more than that. That's interesting. Basically, people are looking at
*  3D shapes and making guesses. Educated guesses.
*  For example, let's say I don't need dynamics to have an open and a closed confirmation.
*  I don't need to necessarily have the full dynamics to have an open confirmation and a close
*  confirmation of an enzyme or something. If I have some way of just getting an open and a
*  close confirmation, I don't necessarily need to run MD to get that. Once I have an open and a
*  closed, and let's say I want to design something that locks my protein open, whereas it naturally
*  wants to be closed, then that very much is an engineering problem at that point. As soon as you
*  have the open state, you don't need really any dynamics to design a binder that locks it into
*  that open state. It really is a very structural sort of problem. I think in a lot of cases,
*  it does end up just... I'm not really needing MD at all. I feel like I'm going to step on
*  some people's toes or hurt some people's feelings saying that. A lot of these problems, they just
*  don't require it. You don't need to understand the full dynamics of the protein to solve the problem.
*  It can be helpful, and in some cases, it definitely is required. In a lot of cases,
*  in a lot of very useful cases, it's not. Fascinating stuff. Well, let's talk about
*  some of the other new models that have come out and what difference they are making. You mentioned
*  ESM-3 toward the top, we didn't get into that one. Then you've sent me these peptide ones,
*  which I have used Notebook LM to help me develop some intuition for, a very analogy,
*  heavy understanding coming out of Notebook LM as it stands today. It's great, isn't it? I love
*  Notebook LM. Yeah, I really like it though. My one request so far is I would like to have a
*  low analogy or no analogy version because I'm always trying to be literal and I'm always like,
*  I just feel myself being sucked into these sort of convenient metaphors. I'm just like,
*  I'm not really sure how much this really maps on to the reality. I don't trust the language
*  models quite that much to be really apt with the analogies. I definitely am getting my butt out of
*  my chair more because I can throw these papers into something like that and go take a walk and
*  listen to it. I'm very bullish on the form, but I want a better analogy dialed down.
*  I read the one that you generated for MDGen. It was actually pretty good. I was actually
*  really impressed by it. Yeah, the models are definitely, Gemini is probably smarter than me,
*  so I can't give it too much rock. I think it is a settings thing or just when they created this
*  product, and obviously that's early too, right? They just looked at what popular podcasters are
*  doing to explain this sort of stuff. I'm just a weird person who doesn't want too much analogy
*  driven explanation, but it definitely works well. I have to say it has me questioning how long
*  humans will be needed in the podcasting game for sure, which, hey, I'll have to move on and
*  find something else maybe. Going back to these models, we got EM3, we get the peptide ones,
*  we've got GOAB, and there might even be others, but give us a walkthrough of these big highlights
*  in terms of new releases. I'll start with PepFlo and GOAB. I think those are, in a way,
*  very similar models. One is for generating antibodies. It's very much like an RF diffusion
*  for antibodies in particular. The other is for peptides. It turns out relatively small,
*  especially disordered peptides are very similar to CDR loops on antibodies. They behave in a very
*  similar way. Something that I was kind of questioning is why no one's trained on both
*  of those at the same time, because PepFlo is just trained on peptide data and GOAB was just trained
*  on antibody data. They could have easily trained on both and probably would have gotten better
*  performance from it. So I think it would be interesting to see someone retrain either PepFlo
*  or GOAB on a bigger data set that involves both peptides and antibodies, because you could use
*  them interchangeably. Well, I don't know if I would use the antibody to design peptides,
*  but I would definitely use the peptide model to design CDR loops that I could then scaffold into
*  an antibody. I would totally do that. So the PepFlo model is useful for CDR loops as well,
*  not just for peptides. And I think they're interesting. So like PepFlo in particular,
*  I find really interesting because it has four different kinds of flow matching.
*  And the mathematics behind that are just really beautiful to me. When I saw the math that they
*  used to construct PepFlo, I was just like, wow, that's beautiful. They use multiple different
*  kinds of flow matching for different parts of the problem. So like for rotations, they have an SO3
*  flow matching. For the torsion angles, they have the toric flow matching. For translations in
*  Euclidean space, they had Euclidean flow matching. And then they also had the probability simplex
*  flow matching as well for designing the sequence. So it's a structure and sequence co-design model,
*  actually. So you don't need two separate models to design the structure and then the sequence.
*  You do it at the same time, all in one model. And I find these really interesting because
*  like CDR loops and small disordered peptides are hard. Like those are actually like pretty hard
*  to learn on and pretty hard to get good performance with. And so if you have a model that does well on
*  those, that will generate CDR loops or peptides for you really well. That's really useful. And
*  I think it's also like saying a lot because a few months ago we didn't have an antibody model.
*  And I think a lot of people were a little disappointed by the antibody models that were
*  available. And in the past six months, we have some models that are viable for antibodies. Now,
*  I will say this for GOAB and PEPFLO, there isn't really wet lab validation. And so without the wet
*  lab validation, I don't 100% buy that these are really good hard-tested methods yet because
*  they haven't been run through the wringer and have all this extra wet lab validation like RF
*  diffusion has. So I think the people who trained the models are going to have to pair up with the
*  wet lab people and get some wet lab validation going because I think a lot of people are going
*  to be reluctant to adopt the model if there isn't any wet lab validation. No matter how good your
*  in silico metrics are and how good your predictions are, if you don't have a wet lab validation,
*  it kind of feels like it just isn't complete. Okay. A couple of simpleton questions again.
*  Is there a clean division between a peptide and a protein? I mean, I understand like a peptide is
*  a short sequence, shortish sequence of amino acids and a protein is a longer one. When you talk about
*  disordered, that basically I understand to mean like doesn't have confirmations that it spends
*  a lot of time in but is kind of more generally just free-floating and free-folding in kind of
*  whatever way. And also it doesn't have like a stable secondary structure. Like you see these
*  helices, the alpha helices and these protein structures and these like sheets that are parallel
*  to each other called beta sheets. And then there are like little regions that look more kind of
*  disordered. Right? So what I'm talking about is the regions that aren't alpha helices or beta sheets
*  and that aren't structured loops. They're just kind of wobbly and they don't spend a lot of time
*  in a single confirmation, just like you said. Yeah. And these loops are sort of the active site.
*  I mean, that's why they're important on the antibody and that's why we need so many different
*  ones because we're going to encounter all these different intruders into our bodies. So we've got
*  these little, yeah, I remember this does take me way back, but studying how the immune system
*  evolves these antibody chains is like quite a fascinating detour unto itself. But I guess
*  those like the sheets and the sort of main structural elements, those don't do
*  the critical interactions. Those are like the scaffolding pieces by and large.
*  In antibodies, yes, but in general proteins, no. So in more general proteins, you have interfaces
*  of all different kinds. And I will also say like you can sometimes get better binding affinity
*  with peptides than you can with antibodies, which I think is not intuitive necessarily,
*  especially considering the history behind getting antibodies to bind to different things and
*  that sort of being the wet lab approach being the traditional way that people do these things.
*  But yeah. Yeah. So I understand these peptides are like easier to make, easier to like distribute
*  in the body versus giant proteins, but have just been traditionally kind of elusive to understand
*  because they don't have the same level of stability in their structure.
*  That's right. Yeah, exactly. And I think, yeah. So yeah, that's another thing too. So for like
*  the drug development with peptides, I think the manufacturing process with peptides, if the
*  peptides are small enough, the manufacturing processes could potentially be the same manufacturing
*  processes for small molecules, if the peptide is small enough. And if it's not small enough,
*  it could still be easier than general proteins. But once you get past a certain size, it starts
*  to get harder. So and yeah, like you said, like I don't know that there's a clear defining line
*  between peptides and proteins. It's a very fuzzy sort of boundary between the two, I would say.
*  But for the peptides in these two models, like we're looking at things that are less than 30
*  residues, if that gives you a better idea of how many. Yeah. Can you help me understand
*  flow matching better as it compares to diffusion? I have studied like image diffusion models in some
*  detail and I sort of have the sense of like the noising process and the denoising process.
*  I don't really have as much of an understanding of flow matching. I also noticed in preparing for
*  this and looking at these papers that there isn't a new noising method for proteins that one of
*  the papers introduced. And I was like, oh yeah, it hadn't even really occurred to me that like,
*  you would have to noise a protein differently than you would noise an image. But
*  now that it's brought to my attention, it does make sense. So but yeah, help us small minded people
*  better understand what's going on there. Yeah. So I guess like something that I, let me find it.
*  Oh, here we go. Yeah, I'm going to drop this in the chat. This will be a great thing for you to
*  share with people. So this is a little notebook that shows you the relationship between diffusion
*  and auto regression and how diffusion is like auto regression after you do like a Fourier transform,
*  basically. So the relationship between diffusion and flow matching, I don't know, in some ways is
*  kind of similar because flow matching is actually like a generalization of diffusion. So like
*  diffusion is a special case of flow matching. And there are different advantages to flow matching
*  over diffusion. So I think the two main ones that I remember the most are the training stability,
*  data efficiency, and inference speed. So flow matching tends to be more stable during training,
*  it tends to be less data hungry, and the inference speed is significantly faster. So like,
*  when it comes to, for example, the protein-protein interaction prediction problem,
*  having a flow matching version of something like alpha fold could be really useful because the
*  inference speed would be a lot faster. And so predicting a higher volume of protein-protein
*  interactions would be more possible with flow matching than it would be with diffusion.
*  Let's talk about ESM3. You know, I'm always really interested when I see things that seem to
*  model multiple different modalities. This includes not just sequence and structure,
*  but also function. That seems like a really interesting kind of trend that I'm observing
*  in a couple different places. So yeah, I mean, what's your understanding of ESM3? Why is it a
*  big deal? What does it say about the future? Well, I think the multimodality is definitely
*  interesting. As far as the function aspect of it. So I have mixed feelings about the function
*  modality. And the reason being is I'm very partial to like an open vocabulary sort of
*  setup, instead of having something that has like a very finite restricted vocabulary
*  for the function. To do an open vocabulary, you need a good high quality
*  text-based data set, right? Which I would argue that we probably have, but ESM3 kind of condenses
*  that by making it a finite vocabulary and giving you like a finite number of choices. And I don't
*  remember exactly how many, but it was like a few hundred or something like that. And compressing
*  protein function down so much that you have it encoded in, you know, a few hundred tokens
*  seems very limiting to me. So like, if you look back at a model like protein DT, okay, protein DT
*  was open vocabulary and it was text to protein. And so you could type in a text prompt in natural
*  English language and get out a protein, right? I would prefer something like that over the finite
*  vocabulary version of the function, just because I think it's more generalizable. I think you can
*  get outside of your distribution a little bit better that way. And having that open vocabulary
*  also gives you more flexibility to kind of like blend functions, I think. And I would think if
*  you're allowing for like open vocabulary, it kind of implies like an infinite number of functions,
*  right? And to me that seems more useful. And so like, I'm really hoping that eventually someone
*  trains something like ESM3, but with an open vocabulary instead of the finite vocabulary that
*  they chose for the function modality. That said, I mean, it is as good as Alpha Fold 2 at structure
*  prediction now. You have the ability to work with sequences or structures or some functions of
*  proteins. And, you know, they did successfully design a functional protein that fluoresced, right?
*  Which is, I mean, it's pretty cool. I would be ecstatic if it were a functional enzyme,
*  or even just a functional binder of some kind. I think that would be really cool. But at the same
*  time, like being able to show that you've generated something that's very evolutionarily dissimilar
*  from all the known stuff that you trained on, I think is a good argument for, you know,
*  at least in some cases, we can actually kind of push things out of distribution and generalize a bit.
*  Yeah.
*  Yeah. How do you, I mean, the title of the paper is Simulating 500 Million Years of Evolution with
*  a Language Model, which is that 500 million years is measured, as I understand it, by an analysis of
*  like how different the protein that they designed is from things that are actually observed in
*  nature and then kind of comparing that to how far back a common ancestor is between things that are
*  similarly different. So it's like a two hop kind of analysis. That's odd.
*  Why is that odd?
*  I don't know. Well, it doesn't seem like we've simulated 500 million years of evolution, I guess.
*  It seems like we picked a random, not random, of course, but it seems like we picked a point
*  out of protein space. And yeah, so just the language of simulating just seems weird as I
*  try to understand like what I think they actually did.
*  So yeah, I would say simulating evolution is, I don't know, in my mind, simulating evolution would
*  be something akin to like directed evolution, like in silico directed evolution, right?
*  Which is not at all what they did. So I think the language is a little misleading saying that you
*  simulated 500 million years of evolution. Yes, I think that is a little bit, maybe you have a
*  misnomer, but at the same time, I think, so I guess here, let me drop this page, because I want to talk
*  about this a little bit. So this is a fine tune of ESM3. So Joshua Benjio and some other people
*  from like Miele and National Research Council of Canada, CFAR, they fine tuned ESM3 and they were
*  able to fine tune it and get conformational ensembles out of it. So dynamics to some degree.
*  So not necessarily like the transitions between them or trajectories or anything like that, but
*  conformational ensembles at least. So they fine tuned ESM3 and I think they fine tuned it as a
*  diffusion model, actually, and were able to get it to generate conformational ensembles. So there's
*  now a new version of ESM3. It's open source and you can generate conformational ensembles with it,
*  which is really cool. And like I wouldn't be able to get into exactly how they did that because the
*  paper just came out a week ago, but it's worth mentioning that you, you know, fine tuning ESM3
*  might be very, very fruitful. So if we zoom out on all of this, can we attempt a summary of
*  what has happened in the last six or so months? It seems like we've made real progress on
*  peptides, which are hard because they are not so structurally stable and are described as
*  disordered. There's been notable progress on moving toward dynamics as opposed to
*  static structures. You've been to a conference where people are creating things that can eat
*  key parts of bacteria and that have like multiple different active sites and are able to kind of
*  choreograph all that together. What is sort of the practical upshot of this? Like how would you say
*  the frontier has moved and what are you looking for next as you obviously just continue to,
*  you know, keep tabs and look for difference makers in this field?
*  Yeah. So as far as what I'm looking for next, I think two things. One would be some obvious
*  improvements to the dynamics models. So like training MDGen on a bigger data set, a better data
*  set, for example, and getting models that are not just structure prediction, but also trajectory or
*  Boltzmann distribution samplers. But beyond that, I think having multiple models chained together in
*  a way so that when one runs, it feeds into the next one and solves a task. And then all together,
*  having all of them orchestrated in some cohesive workflow and then maybe run by an agent,
*  having an agent like tuning hyperparameters and assessing the outputs and coming up with hypotheses
*  and things like that. I think that is where we're headed and that's already popping up
*  in multiple different places. And it's proving effective. And I think it's very, very promising
*  because I think if you can scale that process and have an agent drive a big complicated workflow
*  and solve a task and you can just like churn out molecules, that changes things a lot. And I think
*  like both for industrial applications and medical applications, we are going to see like better
*  molecules being designed that are more specific, more tuned to the function that you really want
*  them to perform, less of a guess and test brute force sort of procedure and more of a carefully
*  considering things and designing for a specific purpose sort of procedure. So I definitely expect
*  like agents driving these workflows to be the next thing to be looking out for. And that's already
*  happening. I mean, you can already find examples of that that I think are really interesting.
*  Are people using like GPT-4 to...?
*  Yeah, language models. Yeah, or vision language models. So like, for example, you might have
*  an agent do some kind of literature search and help you develop hypotheses. You might have an
*  agent assessing outputs of a model and tuning hyperparameters. You might have another agent
*  that's looking at the results and iterating or something like that. Like you might have multiple
*  agents in your workflow that are each doing different things and talking to each other and
*  stuff. And I've seen people using really small models for some of this and like tuning like
*  little 8 billion parameter models to do some of the more specialized tasks and just having like
*  multiple 8 billion parameter models scattered around. And then also sometimes there's a bigger
*  one that's in there doing something a little more complicated in general or like orchestrating the
*  simpler ones. I think that's definitely the thing to look out for in the coming months. Like by
*  early next year, I'd be surprised if somebody didn't have a real banger in terms of like
*  workflows being driven by agents. Like I've already seen some good examples that I can send you that
*  I think are really interesting. How much, how high are the quality of the results? I mean, in the
*  case of like the AI scientist paper that made the rounds out of Sakana AI and we just did an episode
*  not too long ago on this other paper that asked the question, can large language models generate
*  novel research ideas and did an experiment where they asked human PhDs and postdocs for ideas,
*  notably in the context of prompting language models. That was like the subject of the research
*  was a little bit kind of meta and people were sort of wondering like to what degree does it
*  generalize from there out to other things. But I would say those systems, they feel like a sign of
*  things to come to me, but they don't seem to be producing like great results yet. How would you
*  characterize the results? Like the AI scientist, when people actually went and read those papers,
*  they were like, well, yeah, I don't think my job is at risk just yet. Although yes, I do think
*  we may only be like one turn of the scaling laws from that happening, but at least for now,
*  the actual papers that the AI scientist spits out is like mid. Yeah, I mean, it's not even the
*  scaling laws. Like I am less interested in having a full publication that's well written at the end
*  and more interested in like hypothesis development or like target identification, right? Like that,
*  that's way more interesting to me than having it write my publication for me. I mean,
*  having the publication wrap up at the end gives you a nice way to kind of interface with the whole
*  thing and see in like a test driven development sort of way, like, oh, did the thing that I built
*  produce the output that I expected? But having something that can help you generate hypotheses
*  or help you generate targets to go after, I think that is way more interesting. Or having a model
*  that can tune your workflow and tune the different, you know, like knobs and hyperparameters that there
*  might be based on the output that it's getting so that the design process itself comes out well.
*  Like, I don't think the measure of success is a well written paper. I think the measure of success
*  is a well designed molecule. And so like my success measure would be measured in the wet lab,
*  not on the computer screen. And I think like that's coming sooner. Like that'll be happening sooner
*  than having an AI that'll just write a fully fledged publication really well for you. Yeah,
*  does that answer the question? Have you seen anything already where you would say that that is
*  I have and I didn't have it pulled up. I want to share it with you though. It's something that I
*  just started looking into like yesterday and it looked really good. So I'll find that and I'll
*  send it to you because it looked like something that you would be interested in. I actually
*  thought of you when I saw it. So always looking for these eureka moments. That's for sure. Yeah,
*  cool. I'll find that. Well, you've again been very generous with your time and perspective on all
*  this. Any other thoughts you want to share before we break? It's really awesome that I got to hang
*  out with you today. I had a really good time. Yeah, likewise. As usual. You're awesome to talk
*  to you. You're really good at interviewing. Like you're good at kind of pretending like you don't
*  know. So that the person like you're saying that hard, especially not in this area. So yeah, it's
*  been a lot of fun. But I would say like my takeaway is this machine is moving real fast
*  and new things are coming out at a really fast rate. Like we're looking at like six months and
*  things are already very different than they were six months prior. And so I would say like,
*  what we really need at this point is just more people in the area, because we're going to have
*  to build agents to scale this at the moment, because there's not enough people doing it. So
*  if you're interested in biochem, and you're interested in AI, I would highly suggest getting
*  into it as soon as possible, because it's very fast moving very fast paced, but also just really
*  beautiful and the things that we can accomplish with this are going to be great. So yeah, let's
*  go. It's a great place to leave it. I'm only Schreiber. Thank you for being part of the cognitive
*  revolution. It is both energizing and enlightening to hear why people listen and learn what they
*  value about the show. So please don't hesitate to reach out via email at tcr at turpentine.co
*  or you can DM me on the social media platform of your choice.
