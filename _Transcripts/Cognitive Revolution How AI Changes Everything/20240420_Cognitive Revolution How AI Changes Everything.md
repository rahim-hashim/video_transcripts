---
Date Generated: April 22, 2024
Transcription Model: whisper medium 20231117
Length: 6137s
Video Keywords: []
Video Views: 969
Video Rating: None
---

# AI Inference: Good, Fast, and Cheap, with Lin Qiao & Dmytro Ivchenko of Fireworks AI
**Cognitive Revolution How AI Changes Everything:** [April 20, 2024](https://www.youtube.com/watch?v=KVlEYLULbss)
*  That is a complexity. All application product developers, as they are doing things, fun stuff themselves or in enterprises, they're all facing this challenge.
*  So that's where we come in and say, you don't worry about it. We handle it all for you. So you just focus on your product application development.
*  I'm going to just directly apply the techniques we learned from text models on the image model because it has quality application.
*  So you need to do some extra work to make sure the quality is progressing. So that is quite a bit different.
*  Over time, all these database management systems become smarter and smarter because they all have a layer called optimizer.
*  Those optimizer observe the workload and they start to create, oh, you're doing a lot of filter on this particular column.
*  So I'm going to create index. I'm going to partition those columns based on your future criteria. So it's much better search, much faster search.
*  Everyone is talking about chat GPT right now, but are you actually using it to the max?
*  How do you use chat GPT is an interview show where the people at the forefront of technology show you how they use chat GPT in their work and their lives.
*  Host Dan Schipper talks to programmers, writers, founders, academics, tech executives, and others to walk through all of their chat GPT use cases, including historical chats step by step.
*  They even use chat GPT together live on the show to build apps, analyze their leadership qualities, read more deeply and do the best work of their lives.
*  Listen to how do you use chat GPT from Dan Schipper and the team at every wherever you get your podcasts.
*  Hello and welcome to the cognitive revolution where we interview visionary researchers, entrepreneurs and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of how AI technology will transform work, life and society in the coming years.
*  I'm Nathan Labenz joined by my co-host Eric Torenberg.
*  Hello and welcome back to the cognitive revolution.
*  Today my guests are Lynn Chow and Dmitry Ivchenko, co-founders of Fireworks AI, a company that specializes in inference compute, partnering with the world's leading generative AI researchers to serve the best models at the fastest speeds.
*  Lynn and Dmitry both previously worked on PyTorch at Meta, which is today the default go-to AI framework powering applications used by billions.
*  There they gained first hand experience with the immense challenges of running large language models at a massive scale and the many trade offs between latency, cost and scalability that are always involved.
*  With Fireworks, they're building an end to end platform to make it radically easier and more cost effective for any company to put generative AI into production.
*  This spans the full technology stack, including providing simple tools for executing parameter efficient fine tuning techniques like LoRa that help developers iterate quickly toward product market fit.
*  Also developing highly optimized deployments, leveraging multiple layers of abstraction, including custom CUDA kernels to deliver consistently low latency and managing and scaling hardware across major cloud compute providers in a way that's seamless to their customers.
*  This is a wide ranging discussion. Lynn and Dmitry share their hard earned expertise on the intricacies of AI inference and we dive deep into the weeds on topics including the different priorities that their customers have, such as minimizing time to first token, which is particularly important for voice applications.
*  How some inference compute providers today are using Uber style subsidized pricing to win business and why Lynn thinks developers should be cautious about building on these platforms.
*  Also why she considers open AI and Anthropic to be Fireworks real long term competition.
*  Why Fireworks is betting that all small models, whether open or closed source, will ultimately converge in capabilities.
*  The main parallelization techniques, including tensor and pipeline parallelism that they're using to spread models across GPUs in different ways with different benefits.
*  Why software is struggling to keep up with the pace of advances in hardware and how Fireworks is working toward an automated optimizer that will eventually allow even non technical customers to choose the best configurations for their use cases.
*  Finally, at the end, we brought Dmitry back for a short bonus discussion to cover their recently announced partnership with Stability AI, which has them powering stable diffusion three generation on an exclusive basis.
*  We talked a bit about some of the subtle differences between the image and text generation use cases, and overall I came away with the sense that this partnership makes a ton of sense and might become a new pattern in the industry as research groups look to make their work widely and effectively available while also finding ways to earn a return on their investment.
*  Whether you are an AI engineer wrestling with model deployment or an executive evaluating AI platforms, Lin and Dmitry offer a rare peek behind the curtain of the infrastructure layer, which may not get as much hype as the latest state of the art model, but is obviously critical to realizing the potential of this technology.
*  If you like me default to high speed podcast listening, I might suggest slowing this one down a little bit.
*  Lin is originally from China and Dmitry is originally from Ukraine, and this conversation does get quite technical at times, so when I listened back, I found that 1.5x speed was as fast as I could comfortably go.
*  As always, if you find value in the show, we'd appreciate an online share or review, and we always welcome your feedback via our website, cognitiverevolution.ai, or by DMing me on your favorite social network.
*  Finally for today, if you're an AI engineer looking for a new opportunity or a business owner thinking about investing in AI tools or custom applications, I especially encourage you to get in touch.
*  A number of companies that I'm connected with, including the executive assistant company Athena, which I've mentioned many times, and Elicit, where I'm a small-time investor, plus a number of previous guests, are looking for AI engineering talent.
*  And I'm also helping to start a boutique AI advisory and custom application studio, which will serve small and medium-sized businesses.
*  That company is still in stealth mode for now, but the founder is offering free one-on-one consultations to business owners who have a practical problem that AI might be able to help solve.
*  If any of this sounds interesting, send me a DM and I can connect you with the right people behind the scenes.
*  Now, here's my conversation on AI inference optimized for scale, speed, and efficiency with Lin Chau and Dmitry Ivchenko of Fireworks AI.
*  Lin Chau and Dmitry Ivchenko, co-founders of Fireworks AI, welcome to the Cognitive Revolution.
*  Thanks for having us.
*  Yeah, I'm excited for this conversation. You guys are in a super interesting business, which I will confess to not knowing a ton about.
*  You provide primarily inference compute, and people broadly are well aware of the fact that compute is one of the hottest commodities in the world today and don't need to look any farther than Nvidia's stock price to get a sense for how high the demand is for compute.
*  I also hear speculation that it's a tough business to be in because commodity businesses long-term can be tough.
*  And then I also know that there's a lot of low-level execution details that really matter in businesses like these, and I'm super interested to learn more about some of the close to the metal work that you're doing.
*  So maybe to start off, just give us a quick intro to Fireworks AI, how you guys got the idea to start the business and what your big picture vision is for it.
*  Yeah, definitely. So I think this is a very interesting question about, hey, is inference optimized for scale, speed, and efficiency?
*  So I think this is a very interesting question about, hey, is inference support provider a low margin commodity?
*  So a different way to answer these questions. First of all, reselling hardware is a low margin business.
*  I still remember when we just started, we were brainstorming all kinds of different ideas, and we did notice a demand that because of GPU shortage, GPU arbitration could be an interesting problem to solve.
*  And I think that's a good point to start because indeed, as you said, it's low margin and it's not a sustainable business.
*  I have also seen artificially manufactured pricing from highly competitive landscape, and there's no way those providers can build a sustainable long-term business.
*  And at least at the minimum, people need to take caution building on top of such that as when these companies or startups run out of funding, they will disappear.
*  So one of the important things we want to build fireworks on top of is like focus on our specialty based on our experience.
*  And here, when we think about GNI, so it is going to empower a whole slew of application and product disruption, particularly being consumer, prosumer, and developer facing.
*  The fundamental reason is this is a new revolutionary technology that didn't exist before that can generate content emulating what human can generate.
*  And by definition, the receiving part of this content are by and large human.
*  And for those B2C application, latency is a very important part of product experience because it has to be hyper interactive.
*  Without that interactiveness, it's not a viable product.
*  So many of our customers come to us for extremely low latency requirements.
*  At the same time, the content generated from those providers has to be high quality.
*  And we provide high quality through automated loop across fine tuning and inference.
*  And last but not least, we provide low TCO in a highly sustainable way.
*  And here low TCO is very important because it's a different business from traditional application development where built on top of commodity CPUs.
*  The gross margin is very high because CPUs are cheap and now shift towards GPUs and GPUs not just the hardware expensive.
*  It is very power hungry. It consumes a lot of power and the general other heat and traditional air cooling doesn't work.
*  People have to use liquid cooling or immersed immersion cooling.
*  That means put the GPU inside oil and fully immersed.
*  And those are all costs of operating and GNI inference.
*  So that very high cost make it very challenging to justify business impact.
*  And we specialize in reducing total cost ownership.
*  So if you have a viable product, it can turn that into a viable business.
*  So that's the value add. We have been focused on delivering from fireworks side in terms of product.
*  Quick overview. We provide the general AI platform to do fast experiment iteration and inference production scaling.
*  So here there are two development loops we're optimizing for in the loop product experimentation.
*  We optimize for iteration speed and auto loop production.
*  We optimize for hard system metrics, including latency, TCO, scalability, reliability.
*  I just mentioned the specific product feature on these two loops are fine tuning and inference with on demand serving and automation.
*  This is for inner loop fast iteration of experimentation.
*  And we provide the fastest inference at scale for the auto loop.
*  When you have product market fit, you want to scale your business and this auto loop of production will help you to get the best seed and best TCO.
*  So that's a very high level summary of fireworks product.
*  Cool. OK. Several threads there that I want to follow up on.
*  And interestingly, it sounds like you're saying that a lot of products on the market today are in an Uber moment where you think they're essentially being offered below cost and in a fundamentally unsustainable way.
*  And by contrast, I understand that you are operating your business without doing that. You're not radically subsidizing the customer. Do I have that correct?
*  That's correct. But also, I just want to call out our value add is not extremely low cost.
*  Our value add is low latency, high quality and low TCO.
*  So I'm saying low TCO is a byproduct of our high performance.
*  Yeah, this is a real I've experienced this in my own application development where TCO is not the natural way that a lot of engineers think of things.
*  Things and they specifically don't tend to factor in the cost of their own salaries as they start to build out infrastructure.
*  I am a big believer in certainly the specialization of dedicated infrastructure providers just because I've seen how hard it is to create a reasonably reliable stack when you're doing it on your own.
*  But where are we in this market development cycle and where are things headed?
*  It's an interesting observation off the bat that some of these bargain the cheapest options that are out there are subsidized in an unsustainable way.
*  I know that's happening a lot at the application layer, because certainly people are offering free demos.
*  That's obviously subsidized, right? Because all the tokens are costing money and people are certainly giving away a lot of free accounts and a lot of free inference to their end users.
*  But I hadn't really considered how much that might be happening at the inference compute layer.
*  So it's really interesting to consider that is also a reality in today's world.
*  A lot of our customers, whether they are developers or enterprises come to us not because we are the lowest pricing provider at all.
*  They come to us because again, they are building consumer, personal developer facing applications that requires very low latency and they cannot get it by themselves.
*  They cannot get it from any other providers, even from OpenAI and Topic.
*  They didn't get the right latency or latency is not stable and they are seeking solution from our side.
*  And getting to low latency is actually not easy.
*  And Dimitri can speak a lot to it today.
*  But the high level challenging is GenAI model is among the largest model sizing and complexity in the whole spectrum of machine learning.
*  In early days of machine learning, the algorithm is extremely simple.
*  It's tens of megabytes.
*  And now we're talking about tens of billions of parameters.
*  But that complexity, it doesn't change the nature of all these B2C applications, whether built on traditional machine learning or built on top of GenAI.
*  It doesn't change the latency requirements.
*  It has to be extremely interactive.
*  And that put a lot of back pressure on the inference serving tier to do even more aggressive optimization.
*  And that's the challenge we are.
*  We are really good at addressing and that's our biggest value add.
*  In addition to pricing, I don't think pricing in the long run is a sustainable value add.
*  Yeah, makes sense.
*  OK, cool. So I want to get into then how you're doing it to the greatest degree that you can share and that I can comprehend because I do think this stuff is going to get very into the weeds as we get close to the metal.
*  Do I understand correctly that you are managing your own servers on racks?
*  You're talking about cooling and all this sort of stuff.
*  So are you vertically integrated to that level?
*  Yeah. So that's a good segue to talk about our compute stack.
*  And we currently build on top of CSPs.
*  We're running on top of AWS, GCP and Oracle, OCI.
*  The reason is when we grow bigger, there are various different ways to be more efficient.
*  And right now we are optimizing for velocity of our product development.
*  And those CSPs have been battle tested.
*  So that's why we build on top of them.
*  And we also as a company aspire to run on top of the best hardware across the whole entire industry.
*  And of course, it's the easiest to build on top of NVIDIA GPUs.
*  And that's how we started.
*  But at the same time, we see a lot of emerging hardware coming to this hardware landscape for JDI, including MD, including Intel, including custom ASICs.
*  So there are various different interesting trade-offs.
*  We'd love to pass on to Dimitri to talk about the trade-offs across those different hardware providers.
*  Sure. Yeah.
*  So as Lin mentioned, historically, we've been primarily dominated by NVIDIA in the overall AI landscape.
*  And the reason for NVIDIA domination is twofold.
*  First is they have pretty good hardware.
*  And if you look at the latest H100, it has two petaflops.
*  This is pretty high.
*  And they are pushing with a new Blackwell to double that.
*  And then you can go to 10 petaflops for the superchips.
*  And they also are doubling, quadrupling memory bandwidth along the way.
*  They are also improving on their cross-host interconnect.
*  And the most welcome development there is the actual inter-connect, which in turn will allow us to reduce the latencies of our generation speed.
*  That's one.
*  But the second thing is NVIDIA historically has had a very robust developer stack.
*  And because of these two reasons, I think NVIDIA has been dominating.
*  But lately, I would say NVIDIA's arrival, AMD is coming back.
*  And then now with the new MI300, which has better hardware specs than NVIDIA.
*  And they are also working, I'm sure, day and night on their software stack and the new welcome open source development on the Oracle stack.
*  They are catching up basically in all aspects to NVIDIA as well.
*  You see other newcomers with other developments from Intel, the Gaudi 2, Gaudi 3 release, which is actually even more powerful than MI300.
*  So it's in between H100 and B100, B200.
*  So that's like on the more programmable side of things.
*  And now we look at the different spectrums, the less programmable, more specialized hardware, namely ASICs.
*  So here I would probably just select one is Rock, which has been making a bit of waves lately on Reddit because of their nice demo, the high generation speeds.
*  But the thing is that ASICs are always compromising something.
*  So here is that if you look at Rock, and surprisingly, there is very little detail.
*  And sometimes you need to guess what these guys do because they're not as open as NVIDIA.
*  But what they're fundamentally doing, they're compromising on the fact that they want to remove the shared memory, this HBM in GPUs, and they want to put it as close to units as possible.
*  They want to put it on the die.
*  But then they are compromising on the processing units.
*  So they are achievable for a sub-lover.
*  They also, this memory is very expensive because putting anything on die is way more expensive than having a memory shared across the units.
*  And now what the result is that they have much lower achievable flops.
*  What they can do faster, they can run the generations faster because they don't need to copy memory from the shared memory to the memory which is on die.
*  So this is like a fundamental compromise.
*  They also way more expensive to operate because if you want to host a single model, you need to have a humongous setup which costs millions of dollars.
*  So these are compromising.
*  Although it's very interesting and creates cool demos, but you see limited application of this in the real world.
*  And so the limited disruption, although it does solve some interesting cases, but there seem to be more edge cases right now.
*  Where it wins over traditional programmable GPU hardware.
*  There's also TPUs of course.
*  There has been a case where they have been around and they are sitting out from programmability between ASICs and GPUs.
*  Although technically PyTorch supports TPUs, but to get the best performance you have to go to Jaxx and it will solve for a stack.
*  So it becomes quite different operational mode for different business.
*  So this is in a nutshell.
*  Yeah. So speaking about that, as you can see, it's a spectrum.
*  It's a spectrum from most programmable to hyper specialized.
*  And I want to talk a little bit about our matter experience because both of us and actually a large portion of the funding team came from matter.
*  And we all worked on PyTorch extensively over the past five years.
*  So it's very interesting experience there.
*  Of course, as you can see matter like other hyperscalers running on top of CPU, GPU, ASICs.
*  This is the public information, a variety of hardware.
*  And recently they mentioned they deployed more than 600,000 in-house.
*  And what does that mean?
*  Put that in perspective.
*  That's equal to the power needed for 600,000 average American households.
*  That's roughly twice the size of San Francisco.
*  A huge power consumption.
*  But matter didn't get there overnight.
*  It took us more than five years to go from basic machine learning on CPU to complex deep learning on GPU and ASICs.
*  So there are a lot of interesting lessons learned because we work on software stack.
*  So the first lesson learned is a good product cannot compromise and need to be opinionated about what's a part of philosophy and what's the target audience.
*  So matter when we start to work on diving to AI infrastructure, we had at least three different AI frameworks.
*  That's in 2018.
*  We'll have Coffee2 for mobile, Onyx for server production.
*  So our charter is to unify them into one and cover both server, mobile, research and production.
*  It's called PyTorch One.
*  This feels like a mission impossible at the moment because it has so many different goals.
*  So we merged all these teams together, but there's no consensus how to build this one framework.
*  So we came up with a idealistic zipper approach.
*  And the project was actually literally called Zipper.
*  Taking the PyTorch front end, which is very easy, simple to use and zip it with Coffee2 backend, which is highly performant.
*  It failed miserably because these two frameworks were never designed to work together.
*  The integration overhead was more than writing a new framework from scratch.
*  So we ended up ditch that plan and we kept the PyTorch front end and rewrote this backend into Torch script.
*  And that's an interpreter to execute PyTorch efficiently.
*  So notice that the design decision, the product choice we made is to hold the line for ease of use,
*  hold the line for ease of AI innovation for developers built on PyTorch.
*  And then we take all the complexity of building the backend.
*  So that is the design decision.
*  However, Torch script for PyTorch One.O, it requires the user, the developers to annotate which part of PyTorch code is scripted.
*  That's not a very good UX because people need to know how to annotate.
*  So two years ago, we also started Torch compile to fully automate the process.
*  People don't need to annotate at all.
*  So that's called PyTorch Two.O.
*  We left before the project fully shipped, but I'm thrilled to see that there's great progress made from the PyTorch team.
*  So another interesting takeaway we had in that process is we thought it should be easy to bring PyTorch to the platform.
*  To bring PyTorch to production.
*  We thought the process is just swap the libraries because both PyTorch and Cafe Two and Onyx, they're just library, they're not services.
*  Swap those libraries in the service.
*  However, that's a wrong assumption.
*  A framework or library innovation requires a completely new infrastructure service to build to support it.
*  We end up having to build new data loaders, new data transformer, transformation layer for training for PyTorch.
*  We need to build a new training loop for PyTorch.
*  We need to build new distributed inference data for PyTorch.
*  So after five years, we rolled the whole entire PyTorch platform from one up.
*  It was serving more than 50 trillion inference per day across 50 data centers.
*  So as you can see, this journey took us five years, but we start fireworks.
*  We want to reduce.
*  We want to shrink this five years journey into five weeks or even just five days for current broader set of developers in the platform.
*  We have built better tested large scale AI systems.
*  So we're confident that we can all innovate the incumbents and significantly shorten time to market for everyone out there want to build disruptive applications and products on top of JNN.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  The Brave Search API brings affordable developer access to the Brave Search index, an independent index of the web with over 20 billion web pages.
*  So what makes the Brave Search index stand out?
*  One, it's entirely independent and built from scratch.
*  That means no big tech biases or extortionate prices.
*  Two, it's built on real page visits from actual humans collected anonymously, of course, which filters out tons of junk data.
*  And three, the index is refreshed with tens of millions of pages daily.
*  So it always has accurate up to date information.
*  The Brave Search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference, all while remaining affordable with developer first pricing.
*  Integrating the Brave Search API into your workflow translates to more ethical data sourcing and more human representative data sets.
*  Try the Brave Search API for free for up to 2000 queries per month at brave.com slash API.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work, customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it, and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  If I try to summarize that and make the translation from the meta experience to the fireworks product direction, it seems like the key principles are never compromise on the product, user experience above all, the user's hate to wait.
*  I certainly know that from personal experience.
*  And there's an echo of that at the developer layer too.
*  Developers hate complexity and don't want to have to deal with all this mess.
*  So internal focus on the end user experience above all focus on the developer experience.
*  Second, simplify everything, bring all the complexity in-house, abstract away from all the different kinds of hardware.
*  And it sounds like the place that you want to carve out for yourselves with fireworks is a sort of layer that sits between the developers and all the different hardware providers so that folks can easily develop their applications and not really have to worry about what hardware they're running on, the relative strengths and weaknesses of all that.
*  What bottlenecks they're going to hit at all these different, depending on all the different stacks.
*  Tell me if that's right.
*  First of all, and then I'm very curious to get into a little bit more detail on maybe what some of those bottlenecks are.
*  I'm like pretty rudimentary in my GPU knowledge, but I'm learning.
*  And the audience will be pretty varied in terms of how much command they have of this stuff.
*  First of all, do I have that general story and kind of market position and vision, right?
*  Yeah.
*  So it's mostly right.
*  A little bit more nuance is what is getting the way of the fast iteration loop.
*  Here we are talking about current set of application product developers.
*  They haven't jumped onto AI yet, and they have a slew of AI tools they have to learn and pick and choose different models for their use cases.
*  And also try to optimize for latency and try to justify business impacts to low TCO.
*  All of those are on their plate right now.
*  And our goal is to take away those concerns, let them focus on where they should be focusing on is application and product development.
*  And we give them proper tools and higher level abstraction.
*  So they get low latency, low TCO, high quality, extremely easily.
*  Of course, it sounds really nice and we can dive a lot deeper into how we get there.
*  But at the high level, I will break it into two buckets.
*  One is low latency, low TCO.
*  That's a bucket we should dive deeper into that's driven by our high system optimization, performance optimization.
*  The other bucket is quality.
*  And we have to talk about quality because at the end we think our competition are not other inference provider.
*  Our real competition is actually open AI and the topic.
*  So solving and addressing people's quality issue is very high priority of our company goals.
*  Yeah. Okay. Cool.
*  Those are both really interesting.
*  Let's maybe start the quality one because that's probably the more intuitive one.
*  And I was noticing in trying the product and I always do go in and try products on in my preparation for these conversations.
*  I would say the experience is super easy to get started.
*  Just create an account.
*  Next thing you know, you're in a playground.
*  You can choose from all these models.
*  You've got what you call serverless models, which is literally just a very similar experience to what you get with open AI and anthropic where you're making an API call.
*  You're purely paying for tokens.
*  And that's all super simple.
*  You can test stuff out, try all the different models in the playground and then hit the give me the code button and it pops up the code and you can go copy that code and drop it into your application.
*  So all that is probably reasonably familiar to folks in our audience.
*  They've done that kind of thing, at least with an open AI or an anthropic, if not another inference provider quality, though, is a tough challenge, right?
*  Because with some notable exceptions that are starting to crack into the top 10, certainly still the very best models are proprietary to the open eyes and anthropics and Google DeepMinds of the world.
*  And notably to the price is also starting to get pretty low from those guys.
*  The haiku for manthropic is like a really interesting point of comparison.
*  The price that you guys have for the small tier of models up to 16 billion parameters, which is to hear how that cutoff was selected.
*  But up to that 16 billion threshold is 20 cents per million tokens, which is crazy to think not that long ago.
*  It was six cents per thousand tokens from open AI with the original GPT-3.
*  So we've gone from six cents per thousand to 20 per million for better models than the original GPT-3 in just two years.
*  I always like to stand back and just marvel at how fast that cost has come down.
*  But the leaders are not too far behind right there with haiku and thropic is at 25 cents per million, at least on input.
*  They charge a little more for the output.
*  But with the long context, presumably a lot of the time it is pretty input heavy workload there.
*  So, yeah, let's talk about quality.
*  How do you win in a world of haiku?
*  I would assume that's like the number one direct competitor for those smallest models.
*  Curious to hear how you're thinking about the quality challenge.
*  Yeah, definitely.
*  So between closed source vendor and open source vendor, who is going to win?
*  It's clear that we are currently in a very intense race between open source and closed source models.
*  This week is an interesting week.
*  Mistral team just dropped a new MOE model with eight experts of 22 billion parameters.
*  And we just enabled it.
*  It matters with open source Lama 3 in a few weeks.
*  And Google has been continuing to open source newer gamma models.
*  And Q1 and eModels found that Chinese institutions are getting better and better.
*  Also, at the same time, OpenAI and Antarctic keep improving their model quality, including at a smaller model size scale.
*  So I think all these models in the same size bucket will converge in quality eventually.
*  The reason is for smaller models, because of the size, it has the upper bound on how much knowledge it can absorb.
*  And it determines capability.
*  And as we are all also converge on how much data we can train a model.
*  So just inevitable over time, whether open source or closed source, the model quality will be similar to each other.
*  If that's true, and I will argue open source models have a much stronger ecosystem potential because it has a lot more active people engagement.
*  Developers are engaging in tuning over those models and then they open source them.
*  And this keeps going.
*  It has compounding effects.
*  So more and more people can build on top of each other's work.
*  This is how I'm thinking.
*  So that's why fireworks fundamentally build on top of those open source ecosystem.
*  We also just launched our fine tuning service.
*  It's relatively new.
*  So in terms of revenue, it's not dominating any of other product features, but it's one of our fast growing product feature.
*  With that said, I will still say right now we are not there yet.
*  All open source, closed source models, small models are converging right now.
*  The open source model is unique.
*  Fine tuning and the challenge of fine tuning is it's a much longer development process than prompt engineering.
*  And we fully acknowledge that.
*  And that's why we as a company, we want to solve those problems to make fine tuning much faster, easier and actionable.
*  Because once you see the result, hey, what is not working is actionable.
*  And also we will by and large automate a lot of this pain in fine tuning away.
*  So our developers will have much simpler experience as close to prompt engineering as possible.
*  So that's one aspect.
*  The other aspect is eventually open AI and Anthopic, their goal, including meta automation, their goal is to get to AGI.
*  Right.
*  What is AGI?
*  Basically building a system that's smarter than human.
*  It means this system can solve very complex problems, hundreds of them at the same time.
*  But if we look at the problems developers and enterprises, they are solving.
*  They don't solve hundreds of very complex logical reasoning problems at the same time.
*  They probably have a handful of very specific problems.
*  For example, they want to solve classification problem from intent routing based on intent route to different agents to categorize product catalog nicely to re-ranking, retrieve results, get top K of the best answers, or to do structured data extraction from images, like extract information from receipts, from medical bills, from insurance policies to paraphrasing emails.
*  For better sales follow up or for better marketing lead generation.
*  And the list can go very long.
*  But as you can see, every single example as I mentioned here, they're very specific.
*  So that's created an interesting opportunity for us, especially for smaller open source models.
*  Think about model training as a process of aligning the model to optimize for set of objectives.
*  So this is very important framing because what the model is good at is being decided at the beginning of the training process.
*  How you form the training data set.
*  What is a proportion of what kind of training data set you mix together is basically a product opinion you put in what is the capability of this end model.
*  So no model today is going to be good at solving all kind of problem.
*  You have to pick and choose. So if I set the objective at the beginning.
*  So that's a general framing.
*  But you can also think about it's much easier to align model to solve a specific problem very well instead of as a model to solve hundreds of problems.
*  Very well solving narrow down the objective to one problem.
*  It's a much easier alignment process.
*  So that's why in practice all the practical problem I've seen today is amenable to smaller models because the problems are very narrow and well defined.
*  And we have seen a lot of success using fine tuning to solve those problems.
*  And second, almost every single enterprise we talk with, they have data.
*  They have data to align a model better and sometimes not just on power, even better than GPT-4.
*  So based on those observations, we are pretty bullish on the direction of continue down to make the feedback loop of quality between fine tuning, inference, data collection, cleansing.
*  This feedback loop is very efficient for our users.
*  And again, we will try to automate as much as possible in this process.
*  OK, cool. I have a number of follow ups there as well.
*  So just speaking to my own experience briefly, the general notion that fine tuning is that seems like a really good answer to how do we compete with Haiku?
*  Because I would agree that and in fact, at Waymark, my company, we use a fine tuned GPT-3.5 currently to power our core script writing task.
*  You know, the number one most important AI function in the product, we could use GPT-4.
*  It's not really like a budget thing for us.
*  We have a pretty high value use case.
*  So our strategy is use whatever gives us the best results, not just the best overall user experience, I'd say.
*  And the quality of the output is probably the number one factor there.
*  Latency also is important. As we've discussed, people don't want to wait.
*  And so at the moment, we're on a 3.5 fine tuned model.
*  GPT-4 could probably do the task pretty well and we wouldn't be scared off by the cost, but it is a little bit slow sometimes.
*  And also it's a little bit unwieldy.
*  You're trying to prompt engineer your way of all these different caveats and rules and whatever.
*  And it's hard to represent all that stuff in the prompt.
*  And you could also think, maybe we could use Haiku and maybe we could even put like 10 examples into Haiku.
*  And that could, in theory, get it to do the in context learning.
*  But now we've gone up in order of magnitude in price because we're doing 10 examples at every prompt.
*  Fine tuning, I do think, is a really good answer.
*  And certainly, as you said, companies have data.
*  But even if they don't, a lot of companies would probably be very surprised with how little data it really takes to do a reasonable fine tuning.
*  Our data set is in the three figures, hundreds, but not even thousands of data points.
*  And that works quite well.
*  Actually, we don't have to have a huge thing for a narrow task.
*  If you're trying to maintain generality, then you have a much bigger challenge on your hands.
*  But for this one task of write a script for this business, for this video, hundreds of data points we have found pretty well suffices.
*  That's an excellent point.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Today's podcast is brought to you by Plum.
*  It's 2024. Do you really need to be a staff engineer to understand how your AI feature works?
*  Plum doesn't think so.
*  That's why they've created a no-code AI app builder that non-technical folks can understand at a glance.
*  A drag, drop, and configure visual pipeline for any AI feature you can imagine.
*  Plum gives product teams a place to go from prototype to prod together.
*  Check out useplum.com. That's Plum with a B for early access.
*  Hey, all. Eric Thornburg here.
*  I'm hearing more and more that founders want to get profitable and do more with less, especially with engineering.
*  Listen, I love your 30-year-old ex-fang senior software engineer as much as the next guy, but honestly, I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent.
*  But boy, is it a hassle to do at scale from sourcing to interviewing to on the ground operations and management.
*  That's why I teamed up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high level for over five years to help you access global engineering
*  without the headache.
*  SQUAD, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent so you don't have to.
*  With teams across Asia and South America, we can cover you no matter which time zone you operate in.
*  Their engineers follow your process and use your tools.
*  They work with React, Next.js, or your favorite front-end frameworks.
*  And on the backend, they're experts at Node, Python, Java, and anything under the sun.
*  Full disclosure, it's going to cost more than the random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost.
*  Our engineers are vetted top 1% talent and actually working hard for you every day.
*  Increase your velocity without amping up burn.
*  Head to choose squad.com and mention Turpentine to skip the wait list.
*  So tell me about that fine-tuning product and also maybe get into some of the bottlenecks.
*  I looked at the documentation.
*  I didn't actually do a fine-tuning myself, but maybe I'll put that on my to-do list.
*  But it is very similar to the OpenAI product where you can set up your sort of chat records and their JSONL lines and you upload a bunch of JSONL lines and run it.
*  You build that by token.
*  Is it a good idea to do that?
*  Is it accurate to say that it's basically a kind of at the spec level same thing as the OpenAI experience?
*  Yeah, this is a great way to summarize it because we are one of the product design philosophies to be open at compatible because open has a lot of draw for the initial set of developers to try out ideas.
*  And the benefit of being open at compatible from fine-tuning to inference is it's really easy to migrate.
*  So even if our developer don't start from us, but once they get to stage, they need more interesting fine-tuning that doesn't provide and they need low latency and low TCO for the open.
*  And they can move to us.
*  So you're absolutely right.
*  The API will feel very familiar.
*  But on top of that, we're adding also new APIs that doesn't exist in openness.
*  That's also our unique advantage.
*  But coming back to fine-tuning.
*  Yeah, so here we started offer a special fine-tuning for open at compatible.
*  So we started offering a special fine-tuning for open at compatible.
*  So we started offering a special fine-tuning called PATH, performance-efficient fine-tuning actually found a long time ago.
*  So we started offering a special fine-tuning called PATH, performance-efficient fine-tuning actually found a long time ago.
*  The most popular technique in that bucket is called LoRa.
*  LoRa stands for low rank adaptation.
*  So the idea is you freeze the pre-trained model weights and inject trainable rank decomposition matrices into each layer of transformer architecture.
*  And the end result is greatly reduce the number of trainable parameters for downstream tasks.
*  So usually, fine-tuning, you can think of it as short training.
*  So you need to go forward, backwards and do all this stuff.
*  With LoRa, then your base model is only forward.
*  And then your additional adapter, you go through the full training steps.
*  So that's how it saves compute and be very efficient.
*  And also, you just mentioned, actually, you figure out many people are this consistent feedback.
*  You don't need a lot of training samples or tuning samples, typically like around 1000.
*  In your example, just hundreds of them will be sufficient.
*  A compound with very efficient LoRa fine-tuning, that means your feedback loop is going to be really fast.
*  And that makes the whole fine-tuning process even more appealing, alternative.
*  So let me spend a little bit of time explaining what LoRa means.
*  So under the hood, it leverages a concept again called rank decomposition.
*  And rank decomposition basically allows us to represent a high dimensional matrix with a product of two lower dimensional matrices.
*  So if the pre-chained weight matrix, let's say of dimension n by k, and then it can be represented with a product of two matrices,
*  let's call it n by r for the first one.
*  And the second one is r by k.
*  So if we do a multiplication across these two matrices, you will still get n by k.
*  So that's a high level idea.
*  And let's make the saving more concrete.
*  n is 2000, k is 5000, and r is 1 for extreme case.
*  Just make the point here.
*  So the total of parameters in the original matrix is 2000 by 5000.
*  That's 10 million.
*  And then if we decompose into lower rank, then the first matrix is 2000 by 1 is 2000, and second is 1 by 5000 is 5000.
*  So the total of parameters across these two lower rank lower dimensional matrices is 2000 plus 5000 is 7000.
*  So 7 is a significant lower number of parameters than 10 million.
*  That's the original matrix.
*  So this is more than 1000 times reduction.
*  That's the idea behind why using LoRa to do fine tuning is so much faster.
*  It's not just for a faster fine tuning.
*  At inference, we can also do something very interesting.
*  So we actually have a many customer come to us.
*  They need to deploy many LoRa adapters against the same base model.
*  So the naive way to deploy those LoRa adapter is you merge it with the base model,
*  and then you deploy this 100.
*  If they have 100 LoRa adapters, you have to deploy models.
*  And all these 100 models sit in memory.
*  We are one of the first to deploy many LoRa by sharing the same base model.
*  You can imagine it looks like a tree.
*  There's a trunk that's the base model, and each LoRa adapter is hanging on the trunk.
*  So by doing this sharing, we can save a lot of cost in production for inference,
*  because for 100 LoRa adapters, originally without the saving, you have to deploy 100 times,
*  and then you just need to deploy the one base model that's dominating the cost.
*  So by that, you save 100 times of cost.
*  We kind of use LoRa pretty extensively across both fine tuning and inference,
*  and that significantly increases the velocity of our iteration.
*  If you haven't used it, try that.
*  I strongly encourage you to try our fine tuning service.
*  So, yeah, let's just flesh that out a little bit more.
*  For people, you tell me if I'm going wrong anywhere.
*  The high level situation is you want to have a model deployed that you can get inference from quickly.
*  If you have all your computers turned off, you have the cold start problem of,
*  okay, I got to boot up a Docker container and load this stuff in,
*  and then these like billions of parameters take time to move in.
*  So typically most services are going to try to have some mechanism of not making you wait for a full cold start.
*  So instead what you have when something is deployed is you have a GPU sitting there
*  with the model loaded into the high bandwidth memory, which is to say the second tier memory.
*  I've gone into this a bit on a previous episode where I dug into the Mamba architecture,
*  but basically on your GPUs, you've got your many computation cores.
*  There is the SRAM that is the like highest or let's say the lowest latency closest to the computation core RAM, but it's small.
*  You can't fit the whole model in there.
*  So you have to have this second tier RAM, the high bandwidth memory where the actual billions and billions of parameters of the model sit.
*  And then when you're actually doing inference there,
*  you're paging in parameters from high bandwidth memory into the SRAM for the actual computation, paging them in and out to do stuff.
*  And what you're saying with the Laura, like the many Laura's configuration is that you could,
*  the naive approach as you described it would be to say, okay, I'm going to have a hundred different servers.
*  Each one will have its base model and its Laura and the Laura is whatever, one to three percent or something as many parameters.
*  Again, depending on the setup and exactly how you do it.
*  So you could have a hundred of those each with the base model and the Laura, or you could have your base model and a bunch of Laura's all sitting in high bandwidth memory on a single GPU.
*  And then you just have to manage the paging in or keeping track of which Laura we're using, for which use case, that kind of stuff gets a little bit more complicated.
*  But it allows you to save on having to set up all these servers and have them waiting there.
*  What's the next level of sophistication in terms of the analysis there?
*  That could be like, what are the bottlenecks?
*  What are the tradeoffs that you're facing?
*  Tell me, what do I need to know next to get smarter beyond that base level description?
*  Yeah, so we did a lot of very complicated inference stack optimization to bring down latency.
*  As we have discussed in this episode, our hyper focus on latency, but also while we're hyper focused on very low latency, we also hold the latency bar.
*  We can pump up throughput to very high.
*  And that is a result of low TCO.
*  I will pass it to Dimitry to talk about all the tradeoffs and nuances we have put into the inference optimization stack.
*  So I want to hear you take a step back and try to go over some very basic steps of how to build your own GNI inference service and what are the key points you should pay attention to.
*  Because we have right now a huge information overload.
*  There's so much information.
*  Oh, this attention information is the best.
*  This MAMP architecture is the next big thing.
*  Or we need to run a chart model differently and there's so many different techniques.
*  But the question still remains, what are the actual techniques which really do matter?
*  So that's what I want to focus on these important points here.
*  So, okay, now let's say we want to build the GNI inference.
*  GNI inference. And right now let's focus maybe on one or two cases.
*  One is text generation and another is image generation.
*  Luckily, the very welcome development is that the new model from stability for the image generation is based on the transformer architecture.
*  So the old architecture based on the ResNet is gone.
*  And with that, all the convolutions are not as important anymore.
*  So all we have to worry about is the transformer now, which to some extent is great, but it has its own challenges.
*  Now, what does matter for transformer?
*  So the transformer, I would say there are only two operations which matter.
*  One is the most ubiquitous matrix multiplication.
*  And that's all the only I work with GNI or not.
*  Metmul is the most important one.
*  And the second most important one is, is of course, attention.
*  And attention is a bit special kind of metmul.
*  I would say it's back to back batched metmul.
*  And optimizing it is quite critical.
*  Okay. So now let's say you optimize these two operations.
*  But guess what?
*  There are different flavors that you need to have these operations.
*  These flavors are coming from the text generation workload.
*  Because text generation is a bit special.
*  There is input tokens and output tokens.
*  And processing them is vastly different.
*  The processing of input tokens is mostly compute bound.
*  And generating tokens is mostly memory bandwidth bound.
*  Now you have to have flavors of these two operations.
*  So there are two operations.
*  One is Flaps Optimized, Compute Optimized.
*  And the second is Memory Bandwidth Optimized to speed up this page loading of model weights from this HPM to the SRAM and then to registers.
*  So that's what you need to implement.
*  Now how to implement.
*  So let's take NVIDIA stack for example.
*  Can I just interject for one second?
*  Sure. I understand.
*  And it's clear to the audience also that the two...
*  We're all within inference here, right?
*  But the kind of two forms of latency that matter are time to first token and then speed of token generation from there.
*  And these are essentially two different phases of the process.
*  Because, and here's where I'm learning from you and putting two and two together in real time.
*  You said that the input tokens, aka the processing that happens for time to first token, is going to be compute bound.
*  And I understand that to be because in that process we're doing all the attention, all the MLPs for all the tokens.
*  But we can do that in such a way where we don't have to page in and out the parameters for each token.
*  We can process all the tokens with those parameters, page new parameters in, process all the tokens with those parameters.
*  And so that's why it's compute bound, right?
*  Because we're not paging in and out as much on a per token basis versus then when that's done and we get into token by token generation.
*  Now we need all the parameters in and out for every single token. Is that right?
*  So it's actually much simpler than that.
*  So the thing that if you look at typical use cases is they have, I would say roughly 10 to 1 ratio of input to output.
*  So now when you have your input and the input also typically like 1000 and more tokens goes to 10,000.
*  Practically, it's very common to see this kind of workload.
*  Now that's for the input for the generation when you run the generation.
*  First of all, you generate one token at a time, unless you do some speculating generation, which is separate, but it's mostly one token at a time.
*  And of course, yes, you want to also batch multiple generations together.
*  But there is also a limit there because your big prompt length, you need to allocate a lot of memory to host your intermediate activations.
*  OK, so practically what we see is that the batch size for the generation is around, I would say it goes from 16 to 200.
*  And the batch size for prefill can go to tens of thousands.
*  So that's why here you see this, what, or even more, two orders of magnitude difference.
*  And that's why here the compute versus memory bound thing comes in.
*  So for the prefill, you have so many tokens to process.
*  So your bottleneck is actually a metmole, so your bottleneck fluffs on the computer, on the GPU.
*  For the generation, you don't have that many.
*  And your bottleneck, but in both situations, you need to load the weights from HBA all the way to your registry.
*  You do it in both situations, but just the bottleneck on the generation is this loading.
*  It's not the flops. So it's quite simple, actually.
*  OK, I'm not fully sure I understood the distinction between what I was trying to say and what you said.
*  The big idea, as I understood it, was that when you do the input tokens, like to create an attention matrix, for example,
*  you have to do every token, right, and all the attention heads throughout the thing.
*  And so there's a lot of compute there.
*  And so just on a relative basis, there's more compute relative to the moving of parameters in and out.
*  Whereas in the generation side, now you're generating one at a time.
*  There's not really a way to get around the fact you have to run the whole transformer, right, to generate one token.
*  So you do have to run the Fortress model.
*  But the fundamental thing here is that you use fundamental optimization, which is called key v caching.
*  So in this case, nutshell, it is, as you mentioned, for the initial stage, all tokens have to attend to all previous tokens.
*  So it's basically quadratic divided by two.
*  So that's the generation. You need to do the same.
*  But for the previous tokens, you can cache this attention.
*  You don't have to run it again and again and again.
*  This is the KV cache.
*  Yeah, exactly. Results into only the token you're trying to generate attending to the prior ones.
*  So this is, as you see, is much cheaper because it doesn't have this quadratic nature to it in your nature.
*  Yeah. How big does the KV cache get and does it have to come out of the SRAM and go on to the high bandwidth memory?
*  Or does it just stay in the SRAM the whole time?
*  Yeah, so it gets really big. Right.
*  And it varies because of multiple factors.
*  What is the ratio of the Q heads to KV heads?
*  So it's one of the MQA paper popularized this and now all the big models, they have this.
*  So they reduce the amount of KV heads, usually an order of around four to eight, sometimes even more.
*  But eight is very common there.
*  So that's one thing. Another thing, you can shut the model.
*  Now you're reducing it as well.
*  So what we see when we're getting models, QV cache is not typically big of a problem.
*  But in the end of the day, you have to keep it in the HPE for fast access.
*  In some cases, you can actually put in CPU memory and it's going to be permissible.
*  But that introduces a lot of complexities as well.
*  But most typical case, you keep it in HPE.
*  OK, cool. So you were just about to say when I interjected.
*  OK, so let's do that on Nvidia.
*  Yeah, so going through the how do you implement these metamuls and the tensions very efficiently.
*  So Nvidia stack has a lot of APIs and they go from very low level to very high level.
*  And let's start the other direction.
*  So from the high level, Nvidia has now this ready service TLC LLM.
*  So it's based on Triton for the service.
*  It's already ready to go.
*  But it's easy to get started, although it's not as easy as some open source offering.
*  But compared to the rest, it's much easier.
*  But it's the most rigid as always.
*  So if you want to change anything in C++ code, basically good luck.
*  And then when you go down the stack, you have enough flexibility from this setup.
*  You can go and take a step down and you can try to write your own user or the customized metamul using, for example, QBlas library or QDNN.
*  These are pre compiled versions.
*  There's a configs you can tweak, but can fundamentally change them.
*  Then you want to take even step down.
*  You want to have even more flexibility.
*  Now we're looking at the Cutlass library and with the new sub library, which is called Qt.
*  It's pretty Qt, I would say.
*  Much better than the older API.
*  This is very programmable.
*  Way more programmable.
*  It's basically C++ code library.
*  You can perform a lot of customizations there.
*  But even if that is not enough, you can program yourself in C++.
*  Even sometimes if that is not enough, then you can go all the way to the hardware instructions.
*  And you can program in PTFS.
*  So all these options are possible.
*  It's interesting how GPU programming evolved.
*  So it all started with the programming CUDA cores.
*  And if you look at GPU, that's what it used to be.
*  So you had CPU core, which is very programmable, but not as parallelizable.
*  Now we're going to the GPU and GPU has these CUDA cores.
*  It's also programmable, not as CPU.
*  They are fast.
*  Now the time passes by and that is also not enough.
*  Because as I mentioned, we're optimizing really for metamuls and this attention, which is also sort of metamul.
*  So how can we do that?
*  Now we need to do the next best thing is embed ASIC into your GPU.
*  And that's where the tensor cores come in.
*  That's basically ASIC embedded in GPU.
*  But guess what?
*  It complicates the programming big time.
*  And especially on the newest hardware on the H, the tensor cores are asynchronously programmable from the CUDA cores.
*  Now you have two levels of asyncrosity.
*  You code the CPU to launch CUDA kernels and then from CUDA you'll also asynchronously launch tensor core kernel.
*  So this becomes really complicated.
*  And what we see as a result of it, I see practically very few good kernels, which are geared towards H100.
*  V100 and A100, they had a lot of good CUDA kernels geared towards them.
*  People wrote it and enjoyed GPU programming.
*  Comes Hopper with the async programming nature.
*  And the amount of those public code just drops crazily.
*  And there is a very good explanation to it because the program becomes even more complicated.
*  So now the question is how do we solve this problem?
*  One good step is welcome development is Triton from OpenAI.
*  So actually it's a different compiler.
*  I would say that C++ was a good choice probably back in the day when Nvidia chose it for CUDA.
*  But now it's really getting in the way.
*  In some cases, it's much easier to program in assembly for CUDA than in C++ to be honest.
*  Because of that, we see a lot of experimentation and this Triton is a very neat idea.
*  And so there you literally program in method and there is a lot of magic happening behind these things.
*  Of course, there is never free lunch.
*  So we basically introduce some kind of structure to your GPU programming and it splits it in different levels.
*  So first is like a very simple layer where you program just in Python.
*  Then it translates in so-called MLIR, intermediate representation.
*  And then even that one is a low level MLIR, which is closer to hardware and then gets translated to PTF.
*  So they go to the lowest level right away.
*  The nice thing about this is this structure.
*  Because of this very complex GPU architecture, we talked about this structure actually makes it much easier to understand the existing new kernels
*  and long term maintenance is much better.
*  Because if you compare it to the C++ implementations based on CUDA to Triton, those are really hard to understand.
*  There are thousands, thousands lines of code.
*  This provides a very nice clean separation.
*  But again, no free lunch.
*  And if you hope that, oh, I'm just going to write a CUDA kernel in Triton and just write Python and it's going to be super fast.
*  I'm most likely, unless you're doing a point wise, probably not.
*  You have to still look into what is getting generated, what instructions are used in GPUs.
*  Are they pipeline? Are they not? What tweaks I need to do?
*  And so forth. You have to still look in the output in the address.
*  There is no way around it to get to achieve the cutting edge performance.
*  But the nice thing is that it has this compiler because I don't really want to write assembly, right?
*  Because I need to keep track of all the registers and there's like 255 registers.
*  And it's just that code is unreadable, right?
*  So here by introducing this structure, the hope is, and it does work in many cases, although not a silver bullet.
*  This structure actually makes the code much, much more readable and maintainable and you can still achieve state of the art performance.
*  In fact, the Yemet-Mullen attention implementations, although they are not as flexible as you can write yourself,
*  they achieve close to state of the art performance, which is very nice proof of this concept.
*  OK, so let me try a basic summary and then ask a couple of basic questions.
*  There's a lot of layers between electrons moving around at the very lowest level to Python level scripting,
*  or now we can even say prompting GPT-4 to write me the Python to do the things that I want it to do.
*  So I certainly would expect most of the audience is pretty familiar with the fact that the higher level at which you're working,
*  the more you sort of are at the mercy of all the other layers to determine what your ultimate performance is going to be.
*  I have lived a pretty privileged life where most of the things I've done have been fine at the Python layer,
*  and I've only rarely had to think too much about intensive optimization.
*  So that much, I think, is fairly intuitive. Like you go lower level to do more optimization.
*  What is not super intuitive to me is like what is happening that is causing the need for lots of ongoing optimization today?
*  One might naively think, hey, if it's all transformers,
*  there's presumably only so much optimization that would need to be done across these handful of operations within the transformer.
*  And yet it sounds like that's not really the case.
*  So what are the things that are driving the need for continual optimization?
*  Or why isn't just like a finite set of problems that have already all been solved by the community?
*  Good question. Yeah. I would say number one reason is a new hardware and new hardware trying to get more optimal.
*  And it's not just getting better with existing precision.
*  So they used to be we do everything in a single precision float 32 bit.
*  And now it's shifted to a few years ago, we're doing half precision.
*  So we have a new standard for 16 for inference, 16 for training.
*  I would say kind of a new standard.
*  So it's a new precision, go to new precision.
*  But guess what? That is not also good enough.
*  And we need to have an MD.
*  They need to have new step functions.
*  And they what they're doing, they're lowering the precision.
*  So now I will go to precision in inference and to some extent for training is FPA.
*  So that's what we use for a single parameter.
*  And we also do computing.
*  Then we look at the B100.
*  Guess what I want to use?
*  Of course, they go to four bits and look at the recent papers.
*  And one of the best papers which I like is so called 1.5 bit.
*  It's really called one bit, it's not one bit.
*  But fundamentally, the theory is that to train LLM, you just need 0, 1, minus 1.
*  So basically go left, go right or stay put.
*  So this is like a fundamental property.
*  And if you can have that, you can train the model.
*  And it looks like this is enough.
*  You can basically replace the larger parameters model with the smaller parameters.
*  Of course, you have to retrain.
*  This is a crazy reduction precision.
*  But it looks like these models perform on par with the half or full precision models.
*  So this is a very welcome development.
*  You will see even more hardware optimizations.
*  Because if you do this 0, 1, minus 1, guess what?
*  You don't need multiplication.
*  It's all addition now.
*  You'll see even more optimizations from media and AMD in coming years.
*  Once we train bigger models, like one, three billion models trained for this.
*  Once you train bigger models, this position will become even more critical.
*  So now these new precisions, they require very different instructions.
*  And as you see, like here, the ratio of the generation of GPU is really optimized for this specific ratio of computing and memory back.
*  So here, when the ratio changes, they change the nature of the APIs.
*  And you need to basically code from scratch, to be honest, for the GPU generation.
*  So all the APIs, they work, but it's much slower than it could have been.
*  A good example could be, I would say, a flash attention implementation.
*  Flash attention 2 was called for A14, for 16 precision.
*  And then you run H100, you have just half of what you can get.
*  It's the same kernel, but it just uses older operations, older instructions from the peer, while the HAPR instructions are different.
*  So this is like why fundamentally it's happening and we still have a lot of work ahead of it.
*  But for a few years ahead, until we reach 3, once we reach these 3 bits, let's see what's next.
*  But there's still a long way to get there.
*  Yeah, that 3-bit paper is, or the 1.58-bit paper is super interesting.
*  I will add to that. Dimitri just mentioned, hey, hardware keeps evolving.
*  So not just Nvidia hardware keeps moving forward and the basic instruction set keeps changing.
*  But also there's other lines of product. There's MD, there's Intel, there's customistics and so on.
*  So they're very broad. And we want to simplify that for our user.
*  But also if we look at upper stack, so we are looking down.
*  If we look up at the application level, so we mentioned latency, you mentioned time to first token.
*  So sometimes latency also means time to the first 30 tokens because they are voice streaming out and they have to get the 30 tokens before they can streaming.
*  Or they care about the end-to-end latency.
*  So latency also means different things.
*  And people always want to get a spectrum of latency cost tradeoff.
*  They want to see a curve and they want to pick a point in that curve best for their business.
*  And then on top of that, the input output ratio is different per application.
*  We see a lot of rag usage where it pushed the input to output ratio to be very high.
*  It can be 10 to 1 or even much higher.
*  Or sometimes people just generate one token for classification.
*  Or sometimes they are generally a lot like they're in generating code.
*  So the ratio keeps changing and the best deployment to find depends on what kind of latency you care, which dot in this latency cost curve.
*  What is your input output ratio? What are generating?
*  What kind of is your input? Your contest window length?
*  It all matters.
*  It's very complicated to optimize upwards towards where your application looks like.
*  Does it have repetitive prompts, for example, as another application vertical down to ever moving hardware landscape?
*  That is a complexity.
*  All application product developers as they are doing things, fun stuff themselves or in enterprises, they are all facing this challenge.
*  So that's where we come in and we say, you don't worry about it.
*  We handle it all for you.
*  So you just focus on your product application development.
*  So I just want to double click back to what is our roles in this complex ecosystem.
*  Yeah, it's funny that you mentioned the curve and picking the point on that curve.
*  I'm putting together a little talk for business leaders and developing a top 10 or whatever things to know for business leaders.
*  One of my tips for them is to learn to think in Pareto curves.
*  And this is something that I see at literally every level of the stack, including like just false positives, false negatives.
*  Truly every level seems to have this.
*  So do you envision a future of your product experience being literally just showing people these curves?
*  And like, should I expect to see a number of Pareto curves?
*  Can pick like, OK, for this application, I want absolute minimum time to first token.
*  I'll take the highest cost for this one.
*  I'll take the happy medium for this one.
*  I want the lowest cost.
*  It's a background process or whatever.
*  So it's OK to wait.
*  Is that the kind of experience, the kind of choice that you want to expose ultimately to developers?
*  So I would draw an analogy here.
*  So 20, 25 years ago, database is a new domain and database management systems or no start to come into pictures.
*  Actually, it's very interesting analogy.
*  Now I'm thinking about it on the fly.
*  So database queries has strict patterns.
*  It's called SQL.
*  You have your select clause.
*  You have your where clause.
*  Goodbye.
*  Doing navigation.
*  So this is a very clear pattern.
*  If you think about that, Jenny, I the models has very clear pattern to you have your operator layers.
*  It's more or less stable right now.
*  Although the pattern is simple, but depends on how many columns you have, which column you're going to put a filter on, which column you're going to do aggregation, which color you can do group by.
*  There are all different ways to optimize your query.
*  And at early days, none of these database management systems are smart.
*  That's why it created a whole new entire career called DBA.
*  So basically all database has knobs for human to tune to try to optimize things.
*  And those people make a lot of money because once they optimize, it's a much better experience.
*  It save a lot of money to it's very similar to what we just talked about latency and TCO.
*  But over time, all these database management becomes smarter and smarter because they all have a layer called optimizer.
*  Those optimizer observe the workload and they start to create.
*  Oh, you're doing a lot of future on this particular column.
*  So I'm going to create index.
*  I'm going to partition those columns based on your future criteria.
*  So it's much better search, much faster search.
*  You can skip a lot of things.
*  You have to do sequential scanning and so on.
*  So there then the optimizer becomes smarter and you don't need to hire DBAs at all.
*  It's fully automated.
*  So as long as you observe the workload, you have the workload defined.
*  It's tuned itself, tuned towards the best outcome.
*  So that's our vision.
*  Today we have multiple configurations based on what you tell us, your workload pattern, what you care about, we deploy for you, which is really good.
*  But over time, we want to automate ourselves away from that process.
*  Basically, we learn from what you are running and the system becomes smarter and smarter.
*  It can become lower latency or time.
*  It can be higher quality over time.
*  So that's what we aspire to build.
*  So these options in the product line today would be in the dedicated deployments product.
*  Can you run through some of the...
*  I scanned these documents, but I wouldn't say I conceived of it in the way that you're describing it now.
*  So what are some of the choices that I get to make today, depending on what my application needs are and how does that evolve in the short and medium term?
*  For example, if you look at our product offering, we have three tiers.
*  The developer tier, the business tier, the enterprise tier.
*  So the business tier is more like serve less, pay as you go.
*  And enterprise tier, usually they have clear workload definition and they know where the latency cost curve where they want to be because they have budget.
*  They also have product requirements and they know their workload, like in terms of input, how much rag they're using and how much generation and so on.
*  And then we come in and pick a perfect spot for them.
*  And then we deploy a specific configuration towards our workload.
*  But over time, this can be more and more automated.
*  And because their workload can evolve, they don't always have to get us in the loop.
*  And our system are just self adjusting towards ever changing workload.
*  So that's how the direction we're heading towards.
*  So could you give me a little bit more intuition for let's say I'm an enterprise customer and I have three applications.
*  I have one that's user facing and it's going to generate tokens for a voice app.
*  And those first 30 tokens, as you said, are super critical to get fast because I want to have conversational fluency.
*  So that's one.
*  And the other thing is like a background job where I'm just like, give it to me as cheap as I can.
*  And then there's maybe a chat bot one in the middle.
*  I don't want to pay top dollar for that, but I don't want it to be slow.
*  How does that trickle down into what you are actually deploying for those three different scenarios?
*  So usually enterprise, they have many applications and they usually the distribution of traffic is always skewed.
*  They're heavy hitters. They're very high volume and they're long tails.
*  Each doesn't have high volume, but they add up.
*  So we recommend they basically think about long tail as one bucket of deployment and we give them one configuration.
*  And we have to optimize for the heavy hitters.
*  Each of the heavy hitters, as I said, they care about different kind of latency and those heavy hitters probably are coming from their product team.
*  Usually we also work with ML infra team coming from the product team and they have a certain part of budget.
*  So then we work together to figure out, hey, which dot you want to pick in this curve when it comes to quality.
*  Then the prompt length coming to picture, right?
*  How much instruction tuning you put there, whether you fine tune, take away the instruction prompt,
*  or you put a lot of rag information as a context to constrain the model to do less hallucination.
*  So all these kind of product context start to come into picture.
*  And then we have different kind of deployment to have optimized for very long context window processing versus they do a lot of generation.
*  So those are also different configurations.
*  Give some concrete example where you have to have different deployments for specific use cases.
*  So let's say you really want to get a very low time to first token, the prompt is long.
*  And let's say your model is small, smallish, meaning that like say 7 billion parameters, you don't have to shard it really to put it in GPUs.
*  But the thing is that it's still not fast enough to run on single GPU because the prompt is so long.
*  So now for this specific use case, you want to shard it.
*  But there is a cost for shard.
*  So there are fundamentally three sharding techniques.
*  One is to shard your model weights.
*  Another one is to shard the activation of the input.
*  The third one is to shard modeling pieces that is called pipeline parallelism.
*  So the last one doesn't really help you with the latencies.
*  It just helps when the model is too big.
*  The case when you shard model weights, also called model parallelism, aka tensor parallelism.
*  This helps also with the model size and does help with the latencies.
*  Although there is a cost for sharding.
*  So basically your throughput overall declines.
*  And the first one, the input sharding, usually it doesn't help you with the model size.
*  And it's pretty cheap, but there's a caveat to attention.
*  So you need to take care of attention because you attempt to add a token.
*  So now you have to have a bit more complexity in your setup.
*  So the bottom line here is that for the prefill, for example, the most common sharding right now is the tensor parallelism.
*  If you choose it, you don't want to always shard.
*  You really want to don't shard as much as possible up to the point where you have to.
*  Because there is a cost.
*  Because your throughput will be tanking the more you shard.
*  But sometimes you have to shard because you cannot meet the latency budget.
*  So this is a fundamental thing.
*  And I don't think this problem goes away anytime soon.
*  Yeah, OK.
*  I think, again, everybody will be conceptually familiar with the idea that there is a like latency throughput tradeoff.
*  That seems to be a very recurring pattern.
*  But if I understand what you're saying correctly here, it is that if you have a really long prompt, even if you have a small model that can fit onto one GPU, you may want to split across GPUs.
*  I'm not quite clear on the nature of the splitting.
*  Are you splitting like layer wise?
*  Like you'd have early layers on one and then later layers on another?
*  So every layer you split.
*  It's more complicated, but it's very natural because it goes to Megatron sharding.
*  When you shard to metamuls, you do one columnized and another roll-wise and minimize the amount.
*  Because in the end, once you do this, you need to reshuffle, do all the reviews.
*  So you want to minimize that.
*  And this Megatron style sharding helps you.
*  Often, you're splitting actually the weights across GPUs and then you need to overuse the activations.
*  Can you give us a little bit better intuition for that?
*  Because that's something that is not super clear to me.
*  And I suspect a lot of people are not going to be very clear on it either.
*  I've seen examples of this in my study of the Mamba and Mamba related things.
*  Recently, I've been trying to get a better handle on this.
*  And one thing that's surprising or counterintuitive is that there are ways to take advantage of basically the associative property,
*  where you can do these quick counterintuitive algorithms even for just adding up numbers that kind of look pretty weird,
*  but end up being faster, especially because it allows for this kind of parallelism.
*  Am I on the right track with that?
*  Yes. So here it applies not necessarily.
*  This sharding is like, I would say, model architecture independent.
*  So these are the input data parallelism, tensor parallelism, and pipeline parallelism.
*  They've been there before even Gen.E.I. kicked in.
*  So they're kind of fundamental to machine learning.
*  But then which one you want to apply totally depends on the architecture, because one architecture is much better.
*  For example, if you don't have a sequential nature, using pipeline parallelism is actually no goal.
*  It's not going to save anything because you cannot image up the model.
*  And it used to be a model like that.
*  All transform models tend to have layers, so it's much better.
*  But something like if you look back on the image, older image model based on ResNet,
*  they have same connections, it's becoming harder to do pipeline parallelism.
*  And then the tensor parallelism actually conceptually is harder to understand.
*  And the data input parallelism is easier because you just split data, and data is independent.
*  So you could just duplicate the models with the inputs, right?
*  And so you make all the processes and then you join them in there. That is easy.
*  The model parallelism and tensor parallelism, which we actually do use right now,
*  are hardest to understand because once the weights start interacting with each other,
*  you need to make sure your math is correct.
*  Because you kind of just shard across if you need to, for example, two values, if you need to add them in there.
*  If you want to shard them, but you have to still do the addition.
*  If you need to multiply, you still have to do the multiplication.
*  So when you do that, you need to probably gather them on one rank or another rank or send them across them
*  and then split these operations across the ranks.
*  Of course, sending across GPUs is way more expensive than just sending from single GPU to the registers.
*  It will make it worse, even more. So it becomes quite complicated.
*  But these are the kind of compromises you have to go through.
*  So basically, the idea of this, you need to make sure that your math is still correct once you do the sharding.
*  So this is the idea of this and there are different techniques.
*  And basically, not every operation can be easily displayed this way.
*  So you need to look at specific operations, specific matrix multiplication, how you can split.
*  Yeah, so if you want to research about this, yes, Megatron is a good starting point.
*  It has fundamental descriptions how you do the math move sharding.
*  Yeah, OK, cool. I'll check that out. That's a good pointer.
*  Let me just try to summarize the three kinds and make sure I at least have the conceptual framework right.
*  Simplest one is data parallelism. That is just make multiple instantiations of the model.
*  You can split the data across them. That's essentially like a load balancing setup.
*  The next level up, which maybe is the most complicated, is actually splitting the weights.
*  This is the kind of thing that you would do because you have a super long prompt, for example,
*  and you want to have a fast time to first token.
*  So you need to have even more parallelism of the computation.
*  And it can be worth it.
*  But it comes at this cost of now you've got GPU to GPU communication, plus the complexity of what the hell am I doing across all these different now that I'm splitting weights like, OK, that's a lot to keep track of.
*  And then the third one is the pipeline.
*  And that is where you actually split early layers from middle layers, late layers, whatever.
*  And you're feeding through multiple things in a pipeline in a sequential way.
*  Cool. That's awesome. Lots to learn.
*  I've been doing this around the clock, I feel like, for a few years now and still a target rich environment for new things to learn.
*  Yeah, and they can combine them in many different ways and go to really complicated setups.
*  Oh, yes. Yeah, independent dimensions as well.
*  OK, so we've covered a lot of ground.
*  One other question I wanted to ask about is with all this complexity of everything we've talked about, the one thing that was surprising to me is that you are also training your own models.
*  You have your own branded fireworks function calling models.
*  And especially given your earlier comment that you think at least the small models are converging, how does that fit into the overall strategy?
*  Like, why bother training your own models as opposed to just focusing on the insane complexity of the inference stack and letting that convergence happen independently of your efforts?
*  That's a great question. And one of the biggest, like the north star of the product we're building is not just serving individual models.
*  So we want to be the inference stack for knowledge extraction.
*  And when we talk about knowledge, we can first look at the knowledge provided by large language models is very capable.
*  Now they can answer many questions.
*  It surprises us. But at the end, all large language models has limited knowledge.
*  Why? The knowledge is limited by its training data. Its training is limited in terms of time range.
*  It doesn't have the most latest information and it doesn't have the information.
*  People cannot crawl for Internet, those public information.
*  So there are just limits to the corpus of information people can call directly from.
*  And many of those knowledge also live outside of large language models because there are foundation models.
*  They generate images, generate videos, generate audios.
*  They also do information extraction for images.
*  So I want to create a framework to think about the knowledge distribution is beyond just large language model.
*  And even for given large language model, it's limited.
*  And there are other modalities that carry a lot of information.
*  Beyond that, there are a lot of knowledge is hidden behind APIs that we cannot extract from.
*  And we use a very extensively day to day.
*  For example, we do search. So there's Google search, there's weather API, there's stock extraction API, there's map API.
*  For personal productivity, there are APIs for docs, for spreadsheets, for calendars, and so on and so forth.
*  So APIs are everywhere. Within enterprise, one enterprise internally can have hundreds of API surface areas too.
*  There are a lot of key value stores, document stores, production logs, PubSub systems, internal search.
*  So API itself contains a large corpus of knowledge.
*  So think about function calling. What is function calling?
*  So our file function, the model we build ourselves, is serving the function calling area.
*  And function calling is the layer to tie knowledge together behind all different modalities of foundation models and APIs together.
*  So to us, strategically, this is a critical layer for us to build the best inference tier for knowledge.
*  And with that, you can build a lot of fun applications. For example, you can build a personal admin to knock down into everyone on the planet that can sort out tedious work.
*  This application can learn what you like over time and can preemptively finish work before you ask and put out the reminders or even suggest things ahead of time.
*  I wish I could have a personal admin like that.
*  But those kind of new applications have to depend on tools and ways to extract knowledge across the board.
*  From foundation models and from APIs. That's the fundamental reason why we build our own function calling model.
*  We have released two versions, open weights, so everyone can use it. You can download from Huggingface.
*  We are currently working on our third version that's going to come out soon and will have a great quality bomb. So stay tuned.
*  Cool. I can look forward to that. I know we're just about at the limit of our time together today.
*  You guys have been very generous with your time and knowledge. Is there anything that we haven't managed to touch on yet that you want to make sure you mentioned?
*  I think we touch on a lot. Yeah, I think you have one question about SSM.
*  Yeah, that's a hobby horse of mine. Is that on your customer's radar? Is it on your radar? Is it on your roadmap?
*  So actually, we haven't heard too much about the requirements for our customers. I think it's a very cool technology.
*  So of course, when we talk about SSM, it's in the context of Mamba. The main barrier to practical adoption is mainly quality in my mind compared with transformer models.
*  So we haven't seen a pure Mamba SSM based model emerge as highly competitive in quality to Mistral, Cloud, GBT 3.5 or 4 yet.
*  I think AI21 Labs just open source and Jamba. It's a hybrid of SSM and transformer models.
*  But the real quality benchmark is one thing. Real quality in practice is another thing.
*  So real quality using practical use cases yet to be verified.
*  So that's why I think we haven't seen huge demand there. And I guess people are more cautious.
*  It's hard to say what will be the technical challenge. I think Dimitri was pretty confident we supported in no time.
*  But again, coming back to quality, it's a little bit hard to assess.
*  So those kind of architecture Mamba and SSM is really good for long context by removing the quadratic nature of transformer.
*  But for long context, it's hard to assess the quality.
*  Needling this haystack is the most commonly used benchmark, but it's not very comprehensive.
*  I don't think as an industry we have standardized the benchmark for measuring long context quality yet.
*  But this is another area the whole industry needs to move forward.
*  This benchmark still shows that there is room to go for Mamba architecture to meet the current transformer based models.
*  Yeah, my money's on the hybrids for what it's worth.
*  There's been some really interesting kind of very fine grain studies of the comparative strengths and weaknesses.
*  And there will be, I'm sure, many more developments.
*  So we are doing a quick bonus recording, 10 minutes or whatever, on some exciting company developments.
*  This goes to show how fast everything is moving in AI.
*  I think it's only been seven days since we recorded.
*  And I noticed that you mentioned the new image generation model from Stability on our first call.
*  But I didn't know at that time that Fireworks has been in partnership talks
*  and now has announced a partnership with Stability AI to be the exclusive inference provider of Stable Diffusion 3.
*  That's pretty awesome. I'm sure that is a position that a lot of inference providers would love to have.
*  And I am just very curious to hear more about how that came to be and what the competition was like,
*  what sort of work you had to do to make it happen, anything you can share about the nature of the partnership.
*  But for starters, congratulations.
*  Thank you. Yeah, we've been locating Hangbys for a while now.
*  And overall, the partnership makes total sense because if you look at the company level,
*  Stability has a lot of very good researchers who train very good models.
*  If you look at this historically, they've been very successful monetizing that compared to OpenIre.
*  And on the other hand, Fireworks, we have very good production-minded engineers who are also very good at model performance.
*  We talked about the length during our previous conversation.
*  We can bring these models, which are trained by those amazing researchers, to production in no time and run them very cheaply.
*  So that's the high level, while the partnership makes sense.
*  I can talk a little bit more about optimization strategies, what we implore for the image models and how they are different from the text models.
*  And I would say similar at the same time.
*  So one exciting development about the image model is that with the new architecture of Stability Fusion 3,
*  folks move to the transformer based architecture, and that changes a lot of things.
*  Because if you look at the performance profile before, it was mostly like that.
*  And the best was convolution.
*  There's nothing common with the test models, but now it's all transformer based.
*  So we were able to apply a lot of optimizations, which we learned of our running, posting in the text models on these image models.
*  So that actually provided us quite a bit of boost.
*  For example, we applied most optimal kernels, applying different sharding strategies.
*  Yet, at the same time, the image models are still different.
*  They don't have this generation phase.
*  I would say they are running in the constant pre-fill phase, so to speak.
*  And there is no only running big batch sizes, because the batch size wide is big enough to situate GPUs.
*  But there are still a lot of these commonalities because of the transformer architecture.
*  So we're excited about that.
*  Yeah, that's cool.
*  I think folks will probably be fairly familiar with multimodal language models that accept images as input.
*  So in that context, there's a translation rate, depending on the size of your image, to the number of tokens that sort of counts as.
*  And broadly speaking, again, people will know that you tend to break the image down into patches and feed it in that way.
*  And then in most of these multimodal models gets mapped to a language latent space and then was used to inform your generation.
*  This is obviously quite a different situation.
*  So can you give us a little bit more about how it works?
*  Are we generating one image patch at a time?
*  And how should we think about familiar concepts from the transformer, like the vocabulary size or the attention window?
*  How do those concepts map onto this image generation use case?
*  Yes, for the image generation, the best analogy here is to map the pre-fill part of the next generation to the image generation.
*  So those map pretty nicely.
*  The biggest difference there that on the next generation, the input is variable, right?
*  For instance, on the image generation, yes, we will run through encoder.
*  But then once you run through those tokenizers and encoders, that input actually to the transformer layer, this is the heaviest by far, is fixed.
*  So this side is fixed, which actually makes, I would say, optimizing a bit more straightforward.
*  The new 7.3.3 architecture for the whole of the project is quite different, right?
*  But in the same time, the heaviest part by far is the transformer layer now.
*  So that's what our focus has been.
*  And all we were learning is from the text models about the shot, and they still apply to this transformer.
*  But they still apply to this transformer.
*  It's a very long sequential model, and basically all these techniques do apply.
*  So what is a token output?
*  I assume it's like a square that consists of a certain number of pixels, but I haven't studied this in depth.
*  Yeah, I would say that concept is still the same across the diffusion models.
*  It didn't change with the introduction of the transformer architecture.
*  Yes, basically in the image generation, you have to map these pixels essentially to the floating point values.
*  And so there is basically two different modes of how you process the input.
*  For example, there is an X-driven image generation.
*  So there you have to organize the text, right?
*  And then get transformed into a M-band, and they all map the input to the image generation.
*  But I would say the input is quite different because what you say, you generate this noise because it's a diffusion process, right?
*  So that's what the fundamental difference is.
*  So you basically generate this noise.
*  It's literally a randomized noise generation.
*  And then you run into these diffusion steps one by one, and you try to reverse the diffusion process, and you're enhancing this image with each step.
*  So that's what's happening.
*  And then you run and you convert this output of the transformer to the actual pixels.
*  Yeah, let me try to state it back to you.
*  You start with noise.
*  You're running then multiple forward passes where each forward pass constitutes one denoising step.
*  And you have how many denoising steps on the way to a full image?
*  It depends. So for this stable diffusion, three, you can choose, but the fourth one, you run on 50 steps.
*  But for the turbo model, it's quite a bit different architecture.
*  And there, actually, you run around four steps.
*  So it's very, very few.
*  ImageBot is worse, but it's smaller.
*  The turbo model really orients itself.
*  Speed is the number one factor.
*  And for the stable diffusion, three, the quality is the number one factor.
*  Gotcha. And in each forward pass, unlike a language model where you're autoregressing and you are holding all the current tokens fixed and adding one to the end,
*  here you are starting with a bunch of patches and all of those patches get denoised.
*  So your input is n patches and your output is n patches all denoised.
*  And you do that 50 times in a row until you get to the refined final image.
*  Yeah, but this stays constant.
*  So that's very different from the text model.
*  So it stays constant.
*  Yeah. How many patches or is it patches and tokens basically equivalent, right?
*  Yeah, you can say that.
*  And they have different settings on the different model sizes.
*  So again, that's not like how's the thing that changes.
*  Gotcha. OK, cool.
*  So how did this it sounds like something that was maybe driven by the stability leadership team saying, hey, we're good at one part of this, but we're not exactly set up to do the other part.
*  Let's go looking for a partner.
*  Do they come to you directly and say, hey, we think fireworks is the company for us or whatever you can share is cool with me.
*  If I'm inferring reading between the lines correctly, it sounds like they identified you and this was not like a tournament that you participated in, but more of a they knew who they wanted to go with, it sounds like, which is obviously.
*  Yes, it was a many factors which were in play.
*  And again, like from the company's short-term standpoint, our knowledge and leadership with the performance during models, plus the writing, timing, production reliably.
*  So those were two of the most important factors.
*  And yeah, so if you ask people who know fireworks, mostly people say number one is for the speed and starting those two factors are played the key role.
*  Gotcha. Cool.
*  I tried it this morning.
*  It was very simple to get started because I just saw the news of the partnership.
*  So I went to fireworks directly to try to find the model in the playground wherever.
*  And then I realized, oh, it's actually still presented as part of the stability API.
*  So I ended up on the stability docks and got the code there and made a little notebook and started making calls.
*  Is there anything that you can tell about how it works behind the scenes?
*  It seems like I'm still hitting their domain, right?
*  So there's sort of a middle layer and then they're routing over to you.
*  Is there anything interesting in the way that part of the technical setup is constructed?
*  The main reason for this kind of setup is that Stability is a company quite worried about people misusing their models when they want to sanitize the input.
*  And that is also, I would say, quite relevance related to work.
*  So they train models to do that.
*  So in a sense, they can control that process of the input sanitization.
*  So that's one of the reasons we need to route this way.
*  Yeah.
*  Plus for image generation, you can say, oh, it's just some latency is and we are actually working on reducing them.
*  But for image generation, typically, I would say quality is one of the main things.
*  Plus the cost of running models.
*  So that's why this routing is actually works out pretty well in this situation.
*  Cool. That's interesting.
*  Any more detail or interesting aspects of the optimization strategy that you'd like to share?
*  Yeah, basically to repeat what I just said, I emphasize that we're very excited about the proliferation of transformer architecture.
*  And next thing we want to try to work on is a low precision quantization for image models.
*  We are still right now in a P16 composition.
*  But the next thing, one of the next things to mostly to reduce cost of running these models will be looking at the lower basilica compared to the text models, which are the most performing ones in the VA.
*  So we're not doing that for image models yet.
*  So that's one of the areas of study.
*  Interestingly, I need to just directly apply the techniques we learned from text models on the image model because it has quality implications.
*  So you need to do some extra work to make sure the quality is progressing.
*  So that is quite a bit different.
*  So for image, if you think about it, it's different from that.
*  As for text generating, it's one issue, the right book and next book.
*  It doesn't really matter what other tokens were really in play.
*  For text, you're producing the image.
*  So any kind of glitches on the image become invisible.
*  So those are kind of main differences.
*  And if you go on a lower level, is that if you look at the quantization techniques, is that on the image versus text models, the text models, you really want to incorporate the high spikes on activations, for example, which is quite more powerful for digit quantization.
*  And you really want to incorporate them because they do affect the next token choice.
*  The center of the quality choice is the most important thing.
*  Also, the image models, those high activation are not as important.
*  So you can actually cut them and the image quality is not as effective.
*  So it's more decisional of every activation is as aggregate more important.
*  So that's like a kind of high level intuition on the quantization techniques.
*  Yeah, that's quite interesting.
*  It's another way to say that basically, sort of mental model that I have for the language models is that they have obviously very messy, noisy kind of overlapping.
*  But nevertheless, some sort of internal circuits that a given forward pass kind of slots into such that you have these, as you said, high activation points in the network that seem to be doing most of the work beyond a certain layer.
*  Whereas here it's like all to all the whole way through because you need every ultimately.
*  Yeah, every next of cost exactly.
*  Yeah, we'll definitely be announcing more things going forward.
*  So watch out for the new announcements and we also be adjusting based on the back we're receiving from our audience.
*  So, yeah, some more things to come.
*  Guys, I know you got to go.
*  This has been a great conversation.
*  Thank you for being part of the cognitive revolution.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine.co or you can DM me on the social media platform of your choice.
