---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 3686s
Video Keywords: []
Video Views: 385
Video Rating: None
---

# GPUMaxing with Dr. Ronen Dar of Run:ai
**Cognitive Revolution "How AI Changes Everything":** [July 25, 2023](https://www.youtube.com/watch?v=RvD1R7iceS0)
*  Then we saw how difficult it is to train models on a lot of GPUs,
*  going distributed computing. So our goal, still our goal, was to simplify us,
*  to simplify the way data scientists can train big models.
*  Right now, you have these open source models. You can train them on your data.
*  You don't need tens of thousands of GPUs to do that, right?
*  Open source line up is free for research and commercial users.
*  That's really, really exciting.
*  Hello, and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas, and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Thornburg.
*  Hello, and welcome back to the Cognitive Revolution.
*  Today, I'm joined by Dr. Ronen Dar, CTO and co-founder of RunAI,
*  an Israel-based company that helps enterprises train and deploy AI models
*  by optimizing their GPU usage.
*  With companies around the world racing to adopt next generation AI systems,
*  we first discuss RunAI's technology and what differentiates it from other solutions in the
*  market, before then getting Ronen's perspective on today's market for AI chips, from the ongoing
*  shortage, which he expects to go on for a while, at least, to the process and best practices by
*  which companies secure their compute capacity, to the relative prices across major providers,
*  the prospects for chip makers other than Nvidia to meet the soaring demand,
*  the geopolitics of chip production, including the view from Israel on the US-China rivalry,
*  and finally, the prospects for so-called compute governance to effectively control the pace of AI
*  development, whether in China or anywhere else around the world.
*  As I mentioned on our July 4th episode, one goal we have for the second half of the year is to speak
*  to more researchers, builders, and entrepreneurs who are working on AI outside of the United States.
*  And this conversation with Ronen, who combines deep technical expertise with a global strategic
*  outlook, was a great first step in that direction.
*  If you have any other suggestions, please do let us know. You can always email us at
*  tcr at turpentine dot co or DM me on Twitter, or should I say x dot com, where I am at LeBenz.
*  Finally, for now, I encourage everyone who hasn't already to circle back to my AI scouting report,
*  which is posted exclusively on our YouTube channel. It really is the best way that I know
*  to get up to speed on the fundamentals of AI progress and the most important recent
*  development trends. And it's been gratifying to see that the YouTube audience seems to agree.
*  With that, I hope you enjoyed this enlightening conversation about the physical substrate
*  powering the AIs of the future with Dr. Ronen Dar of Run AI.
*  Ronen Dar of Run AI, welcome to the cognitive revolution.
*  Hey, Dan, good to be here.
*  So I'm excited to talk to you about all things AI workloads, data, and technology.
*  GPUs, orchestrating them and kind of the future of where we're going as really a global AI user base
*  and market over the next year or two. For context, you are the CTO and co-founder of this company
*  based in Israel, Run AI. So for starters, tell us about the company and what sort of AI workloads
*  you're orchestrating for folks. So we run AI. As you said, we're based in Tel Aviv, Israel,
*  but we have people all around the world. We have offices in New York as well and all
*  California as well. And as you said, I'm not from California. And so I spend a lot of my time here
*  in the U.S. And okay, so we run AI and we started in early 2018. We're starting to run since then.
*  So we're an AI infrastructure software company and we help companies to train and deploy AI models
*  We're doing a lot of stuff orchestrating AI workloads, orchestrating GPUs. And I think
*  we're bringing in a lot of technology very close to the GPU level and to the cloud.
*  We edit more, over latest works, we have technologies to optimize the usage of GPUs
*  and optimizing workloads, updating the orchestration, scheduling in the cloud
*  and environments. And we're bringing a lot of tools for development teams to easily deploy
*  training models. And we're working on big enterprises right now. The robot solution is
*  quite horizontal. So we're working with big enterprises in the game industry with Sony's
*  mobile customers. We're working with the finance industry, VNO and Benon's fast. We're working with
*  research institutes, MIT, U.K., and it will delay a history on top of run. And we're on, you will see
*  this exciting things that are happening in our space. We see it for the last six, seven years.
*  And magic stuff happening right now. So it's really fun to be the place that we are right now.
*  Maybe give us a little bit more of the history because it's funny, you know, it's only been five
*  years, right, since you founded the company, but obviously a lot has changed. The types of models
*  that were available to run and the kind of scale of training runs that people were attempting in
*  2018 is obviously, you know, much smaller than what we have today. So what was kind of the,
*  you know, the market that you anticipated going after that inspired you to get involved in
*  starting a company? And then how has that, you know, how has the actual market as it's shaped up
*  deviated from your expectations? Yeah, that's a great question. So in fact,
*  right, we started in 2018. And when we started, it was all about computer vision application,
*  right? That's actually the big breakthrough in the industry for machine learning and big
*  learning happened around 2012, 2013 with the ImageNet competition and researchers from
*  Toronto University training AlexNet and doing this big breakthrough in how machine learning
*  models, deep learning models can get inside phone images and videos. And back then, AlexNet was
*  trained on two GPUs. That was the big breakthrough back then in 2012. Two GPUs, right, to train the
*  state of the art models from scratch. And then we saw an interesting trend of people training
*  bigger models, more methods using more data and using more GPUs. And so a few years later,
*  2015 ResNet came out and ResNet was already trained on hundreds of GPUs. And so we saw this
*  trend of computer vision models being scared from a few GPUs to train the state of the art
*  models to hundreds of GPUs. So 100x increase in the requirements to train state of the art
*  models back there. So we started running it back then and we saw how difficult it is to train
*  models on a lot of GPUs going distributed computing. So our goal, still our goal, was to
*  simplify it, to simplify the way data scientists can train big models and just to allow them to
*  train huge models very easily, just one click on their own distributed computing. So we started
*  with that and then we saw that there are huge problems on distributed training but around also
*  how GPUs are being utilized, how GPUs are being distributed and how MLTs are gaining access to GPUs.
*  So we saw a lot of efficiency there, a lot of complexities. I'm just getting access to GPUs
*  and we solved those problems as well. We bought, as I said before, we built a lot of technology
*  around that aspect of just gaining access to GPUs and using that efficiently. And I think we saw in
*  2017-2018 with dual, grateful, natural-value processing. So we saw again the same trend
*  that we saw in computer vision. People train state of the art models, NLP models,
*  9-inch models. In 2018 on hundreds of GPUs, so I think GPT-1 was changed, I think around
*  hundreds, using our hundreds of models. They stayed GPT-4, just according to rumors, right now
*  GPT-4 is closed source. So according to rumors, GPT-4 was trained on more than 20,000 GPUs.
*  So in four, five years time frame, we went from training state of the art models on hundreds of
*  GPUs to tens of thousands of GPUs. So another 100 in case that they're computing it, means
*  we'll train the state of the art models. Models become bigger, more data, more GPUs. So we see this trend
*  once again and we see now a lot of companies are seeing what can be done, which in their TDI and
*  language model. And they are actually to bring those capabilities into their organizations.
*  For sure, AI is going to transform industries and people see that and I think people need to take
*  action and bring AI into their organizations, how their businesses, how their industries are
*  going to be transformed by AI and work on that. So we are helping our customers to do that. Now
*  it's about enlarging language models, about generating the language models, how to train them.
*  Other people are still training computer vision models and models that are much smaller than those
*  language models. Those models we stage overlapping with those models as well.
*  So where do you play in the overall stack or architecture of all this kind of stuff? And I
*  mean that maybe in a couple of different ways. Conceptually, there is obviously a significant
*  divide between training and inference. And then also there is vertical integration. You partner
*  with NVIDIA. I wasn't quite able to figure out, are your customers primarily managing their own
*  physical computing resources and you are a software layer that complements that? Or do you have
*  deployments across all the major public clouds? Describe how far the tentacles reach.
*  So we turn around our platform wherever the customers want their GPUs to run. So we have
*  customers who run our platform on crevices. We support Nelangap solutions. We have a lot of
*  different customers. We have a lot of customers in the cloud and managing
*  small clusters of GPUs with tons of GPUs. We have customers running thousands of GPUs in just
*  one cluster managing all AWS. We also have customers in Agile and Google. So we have
*  this whole so-called hybrid solution. So with RunIR you can get just one platform with which you can
*  run workloads on crevices in the cloud, in any cloud. And it's all the same interface
*  with the same tools. And so in the stack we're running with Kubernetes, with Cloud Edits. So we
*  can run on any Kubernetes label. It can be either Kubernetes, we can run on any managed Kubernetes
*  solution of the cloud providers with Reddit or on-shift. And then users, a lot of things they can
*  use our tools to train their models or deploy their models. I think first it's more training
*  and inference. And we're really taking an integral approach. So we can integrate with any
*  actual with any tool that runs on Kubernetes. So we're working with a lot of tools in the ML
*  ecosystem, experiment tracking tools, add to the block flow registration tools. So being open,
*  I think it's really important because the field moves so fast and new tools are being created every
*  day. So that was one of our ways to operate. We want to be as open as possible.
*  A lot of that sounds, we just had another episode with a couple of guests from Mosaic ML.
*  And I've made a couple of jokes about the cognitive revolution bump that obviously led them to a good
*  outcome very shortly thereafter. I don't want to get overly bogged down in comparing one company
*  against another, but how would you compare and contrast the business that you've built versus
*  how you kind of see Mosaic? Is it just the sort of thing where the industry is growing so fast that
*  you guys don't even worry about competition? Or do you see that there are kind of head to heads
*  and you have meaningfully different positioning in the market? So Mosaic, first of all, they started
*  after us. They started two and a half years ago and we started five years ago. Mosaic has a clear
*  focus on generative AI and large-scale which is more general than that. But I think that the
*  main thing is that we came and we built our platform very much from the bottom up. So we
*  came from the GPU itself on the hardware itself and we saw the issues and problems we utilize on
*  GPUs. So we really, when we built our platform with many artists, they were the software
*  style, the transfer of GPUs and we started with patients of those software libraries.
*  Mosaic is a great platform. It's a great platform for you to start with. It's a great platform for
*  you to start with. It's a great platform for you to start with. It's a great platform for you to
*  start with. It's a great platform for you to start with. It's a great platform for you to start with.
*  It's a great platform for you to start with. It's a great platform for you to start with. It's a great
*  platform for you to start with. It's a great platform for you to start with. It's a great platform
*  for you to start with. It's a great platform for you to start with. It's a great platform for you to
*  start with. It's a great platform for you to start with. It's a great platform for you to start with.
*  More than 36,000 companies have already upgraded to NetSuite, gaining visibility and control over
*  their financials, inventory, HR, e-commerce, and more. If you've been checking out NetSuite already,
*  then you know this deal is unprecedented. No interest, no payments. So take advantage of the
*  special financing offer with our promo code at netsuite.com slash cognitive. Netsuite.com slash
*  cognitive to get the visibility and control your business needs to weather any storm. That is
*  netsuite.com slash cognitive. Omniki uses generative AI to enable you to launch hundreds of
*  thousands of ad iterations that actually work customized across all platforms with a click of
*  a button. I believe in Omniki so much that I invested in it and I recommend you use it too.
*  Use Cogrev to get a 10% discount. And we built two main components, I think. So one of the
*  components, you know, I'm a CEO of Bratman Technology. So we built it. One thing that we built is GP
*  optimization. So we need what we call like the API or the virtualization,
*  CUDA virtualization. So we sit at the CUDA level and we intercept CUDA calls and we control access
*  to GPUs. And we do that enabling better access to GPUs. So with that layer, workloads can share
*  a single GPU. So we have this feature called GPU fractionalization. So we can fractionalize one GPU
*  and can be shared. And we know how to swap memory between CPU and GPU. So people can all provision
*  GPUs to run video models or more models on the same GPU. So essentially we bring a lot of
*  capabilities into utilizing GPUs much better. The second component is more scheduling and orchestration.
*  So we saw that Kubernetes is the state of the art infrastructure and management frame today with
*  cloud. But Kubernetes was built for running microservices on commodity CPUs. Whereas
*  AI workloads are totally different. AI workloads are built in Texas. There are ongoing GPUs. There's
*  a lot of experimentation in terms of how data scientists and machine engineers are handling
*  their workloads. And we saw that there are a lot of scheduling capabilities missing on Kubernetes
*  that are actually available in other states. Other states like high performance computing,
*  server HPC, for scheduling capabilities on the Hadoop ecosystem. YARN scheduler is an amazing
*  scheduler that was built 10 years ago. We got a lot of scheduling capabilities that were really
*  needed for running Spark workloads. So we brought two concepts on those workloads, on HPC and YARN.
*  And we brought them into the Kubernetes world. So we're bringing a lot of batch scheduling
*  capabilities, ability to preempt workloads, to queue workloads and do gap scheduling. So a lot of
*  scheduling. And at the end, what it allows teams to do, it allows them to first of all get a guaranteed
*  quota, a way to get access to their GPUs. But they are not limited to that guaranteed quota. They can
*  always go further and use more GPUs and run more workloads if there are available GPUs in their
*  clusters. If there are idle GPUs, we allow other people in the organization to use those GPUs.
*  So essentially, those scheduling capabilities are bringing again a lot of efficiency into GPU clusters
*  and much more availability of GPUs. So suddenly, MFT becomes much easier to get access to more
*  GPUs very easily on the net. So interesting that efficiency of GPUs are being utilized.
*  And we're increasing the availability of GPUs. And the availability of GPUs is a failure.
*  And so I think that is really unique for us. The fact that we bring a lot of efficiency and a lot of
*  increasing the availability of GPUs. I don't think that anyone else in the world is doing that.
*  So bringing that, we are also doing a lot of simplicity. So we're helping MFTs to easily
*  train their models and easily deploy their models. So investing heavily, we invested heavily,
*  still investing in chronic tools and ways to abstract the complexity of all three,
*  just running workloads and just training models and deploying them. So I think with penalties,
*  without the right solution, without the right platform, they will spend like 90% of their time
*  on each of such, on setting up libraries, setting up drives, setting up a lot of stuff.
*  And so then to scale out or scale out the experiment is really difficult. They are running
*  just one experiment and they want to run it instead of one GPU on another GPU. The extent of GPU
*  starts to be really difficult. Or if they want to run a lot of experiments in parallel, so scaling
*  out those experiments is also really difficult. So we bring a lot of tools to allow researchers
*  and AI practitioners to iterate, run, scale out, scale up and experiment very easily. So for us,
*  I think it's about simplicity and about bringing a lot of efficiency and efficiency. I think no
*  one else provides the value that we bring. We have had a series that had 4x, and even more than that,
*  it treats the GPU utilization, increase GPU availability. And so together with the simplicity,
*  I think we're bringing a unique hopefully to enterprises on the world.
*  Yeah. Okay. Cool. That's very helpful. And it is certainly in the context of the
*  shortage that, and I want to kind of turn in a second toward just kind of the macro
*  context that's driving all of the concern and focus on utilization. These things are
*  not cheap by default and they're getting bid up at the current moment. So that puts you in a position
*  to be even more valuable. Am I understanding correctly that this sort of assumes a dedicated
*  capacity? Because when you say it could be more efficient, that could mean if you're buying
*  on-demand access that you buy less. But as you talked about it, it sounded more like there's
*  an assumption of certain, either physical infrastructure that a client has, or at least
*  some sort of contractual commitment that now they have a certain amount of capacity.
*  Let's make the most of it and not have our data scientists waiting around when they could be
*  getting to work. So that's another good question. So for what we see, big enterprises,
*  video organizations, they usually secure access to GPUs. So just getting access to GPUs, to other
*  GPUs, that can be really difficult. If you go to your AWS account manager and you ask them to
*  increase the limit of your GPU instances, you can try and do that. And if you want to increase
*  your limit to going from GPUs to other GPUs, that's a big deal. You get a lot of questions
*  while trying to do that. So I think just securing access to GPUs and having them available for you,
*  that's a big problem. So it makes enterprises right now buy and reserve those GPUs. So we see
*  a lot of enterprises using reserve and instances of GPUs, huge clusters of GPUs. That's for
*  enterprises, that's what we see. So reserve is something that is being done when it comes to
*  GPUs. Now, when it comes to smaller companies, and for them, on-demand access to GPUs is totally
*  relative. Many startups won't want to do a big investment upfront and buy GPUs. So many of them
*  using on-demand, or maybe it's a combination of reserve and on-demand. But then in that case,
*  we have also a lot of startup companies work with us and our customers. In that aspect, what we get
*  is clusters that are elastic. So those clusters, Unicore or Shreem, maybe there are multiple
*  clusters in different regions. And just deciding on where to run the workload on each region,
*  and how to get to five different GPUs in the right regions around the workload, that should be a
*  challenge. So we're helping also customers just to get access to clusters that might be in
*  different regions, and they might be dynamic clusters, but you can skip that. So for sure,
*  it's about reserve and about on-demand instances as well. Yeah. So let's talk a little bit more
*  about access and the nature of the market. And I don't have a lot of experience in this for
*  context. And I imagine most of our listeners don't, right? Unless you're one of a small
*  pocket of people at a company that's going to make this kind of capital investment or commitment,
*  you're probably like me and you are mostly paying the hourly rate for GPUs as you go.
*  And that's worked fine for me. I haven't done anything at huge, huge scale, but obviously the
*  biggest companies in the world are kind of waking up to the fact that there is this shortage. Maybe
*  for starters, can you just tell me how do you understand the shortage? How bad is the shortage?
*  Are we now in a period of eternal GPU shortage until further notice? And what do people actually
*  go through to buy? In Googling this, it's not super, or using even perplexity to search for
*  information about this. It's not super obvious. You can go get one here on eBay and then there's
*  an H100 on Amazon in a random spot, but it's not really obvious how the big buyers
*  interact with Nvidia in the first place to even get bulk orders. So maybe you could demystify some
*  of that for us a little bit. First of all, I think the GPU shortage relevant to whoever buys GPUs,
*  you know, for their on premises environment, right? Or for companies, people trying to get
*  access to the high end, the most advanced, the newest GPUs in the cloud. So also getting access
*  to those newest GPUs that can be challenging in the large GPUs. I think what we have seen in the
*  last six months is that the demand to GPUs has been chased amazingly fast. It grew in a way that
*  Nvidia didn't dissipate. OpenAI came out with CharedGPT and they showed the entire world what
*  can be done with the other things in generative AI, right? And a lot of companies, including
*  Microsoft and all the cloud providers, and including Elon Musk, his new company,
*  he went and bought 10,000 GPUs just a few months after CharedGPT went out. So a lot of competition
*  and all the cloud providers went to buy more GPUs on Nvidia. So that created a big jump in the demand
*  for GPUs. With hardware, compared to software, it's much more difficult and much more complex
*  to supply their demand when you have unexpected changes in the demand. So that was happening.
*  And for Nvidia, they need to change the way and the pace of which they manufacture those GPUs.
*  So we're speaking about real machines that are actually manufactured with GPUs. To manufacture
*  more GPUs, you need more machines. And that takes time to set up those machines and let them operate.
*  So supplying that demand and bridging on that gap between the demand and the supply,
*  it comes to hardware, that takes some time. And I'm sure Nvidia are working on it. And I'm sure
*  they are tracing the pace in which they manufacture their GPUs. I think the GPU shortage
*  will go away with time. I don't know how much time it will take your shortage to go away.
*  But a lot of companies are still now waiting for their GPUs, for the GPUs that they're
*  waiting for. So H1 output is the newest GPU that people can buy. And others are waiting.
*  So that's the GPU shortage. I think it's really interesting because what we see,
*  we spoke about the trend of using more and more compute to train air models. I think for the first
*  time we're seeing also a huge increase in the demand for GPU power for inference
*  for running those models in production. So LNMs, generative AI models, are so huge that usually
*  they don't fit into the memory of one GPU. So if you want to run state-of-the-art models with
*  hundreds of billions of parameters, typically you want a few GPUs, about four GPUs, eight GPUs,
*  maybe more than that. But I think now we're seeing that CanX creates the computer requirements for
*  inference work. And that's significant for every company that is actually providing
*  models like OpenAI and like Github with their copiles. So Microsoft between OpenAI and Github
*  with their copiles, they need to manage a lot of GPUs. So for inference, for sure,
*  that contributed to the demand for GPUs was very significant. And I think what we're seeing
*  is that the pace in which AI application and AI innovation is happening is much faster than the
*  pace in which GPU or the hardware is being moved forward with speed progress. The next two modes,
*  though, in that already the next other issues as well, but AI, the AI space, AI innovation moves
*  at an exceptionally fast pace, much faster than the capabilities of new hardware. So when that
*  happens, you're getting more and more demand for the demand for hardware. And then you're getting
*  these problems of demand goes too fast, the supply doesn't able to catch up. And so I think that
*  it's my prediction is that this is not the last time that we see GPU shortage. I don't know when
*  will happen the next GPU shortage. I think it will happen again. But now it's like a temporary thing,
*  it will be closed. But I think that it will happen again GPU shortage. It has major consequences.
*  Yeah, I think it has major consequences on the industry or how companies are operating,
*  on the cost of AI. So a lot of interesting aspects to that.
*  So how does it actually work today if you want to go by, start your own little cluster, right?
*  If you are, let's say you're in, I'm not sure what a relevant threshold would be. Obviously,
*  as you said, leading clusters now getting into the tens of thousands inflection, AI just made this
*  headline with a huge raise, I believe within video as a backer. And a lot of that's going to
*  get plowed right back into the chips. So I mean, at the highest level, there's clearly some like
*  strategic deal making going on where, you know, Nvidia is kind of investing in the people that
*  it's going to be then willing to ship the most chips to. But how does it go if I just want like
*  100 H100s or 1000? Do I contract directly with Nvidia? Is there like a secondary market that
*  tends to kind of, you know, are there like futures contracts that people sort of trade in and then
*  ultimately, because pricing seems fairly dynamic, right? Like I'm seeing headlines that are like
*  H100s now cost $40,000. Presumably, that's not, you know, Nvidia changing the, you know,
*  I couldn't even find a price on their website. So like, yeah, how does that actually work in
*  practice to go through this buying process? There are a few decisions that one needs to make.
*  One of the first decisions is around where to invest. Like, is to invest in
*  on-premise environment and just buy GPUs and then operate those GPUs by yourself.
*  Or whether to go with a cloud solution. And what I'm saying, buying GPUs and operating
*  an on-premise environment, that is certainly on-premise environment. It can be also a
*  co-location or someone is managing your GPUs and some co-location. But still, it's not managed by
*  a cloud provider, it's managed by the co-location provider. So co-location or various resources
*  that's working. Cloud is another deciding there are some trade-off costs and there are these
*  few, you know, interesting trade-off. But that's the first decision. So if you go and you
*  choose going for cloud, then you need to choose the cloud provider. You can actually choose
*  multiple cloud providers. It's not necessarily asked to be AWS, Google or Azure. Right now we
*  have amazing security cloud providers, modern cloud providers like Lambda Labs and that call me.
*  We're working with both of them and both of them have amazing GPUs on the end that provide
*  access to GPUs. So you can go with that as well. So that's one thing. On-premises, that's a totally
*  different story. Then you need to decide from who to buy the GPU. It can be for a video
*  representative or it can be for one status. It's another story. And then it's about choosing the
*  right GPU type. Whether you want to go to the highest and the newest GPUs, Gage 100. Are you
*  saying, okay, I'm good enough with a secure access to the A100? That would be good enough for me and
*  the cost will be reasonable. So I think there are some trade-offs around that. There are some
*  trade-offs not just relating to GPUs. There are some trade-offs relating to storage. Where are you
*  storing your data? How performant is it? And questions around networking. If you're running
*  a small scale experiment, so maybe networking is not that important for you, especially in 3D maps
*  or even NVIDIA. Those are interconnects that are connected between two years. So maybe those are
*  not that important for you. But if you do train your models on multiple GPUs or multiple machines,
*  then networking becomes really crucial for your performance. And you need to get some decisions
*  there as well. So those decisions combine cost, performance, needs of users. So we're seeing
*  customers doing just building huge on-premises environment and still securing access to GPUs in
*  the cloud. And we see customers doing just cloud security access to GPUs in different clouds.
*  But the world right now, I think, is the cloud, the cloud. It is the optionality. It's actually
*  the third solution. Because you don't want to just lock yourself to one cloud provider. So we're seeing
*  enterprises choosing more than two providers on-premises cloud solutions.
*  Prices today, in A100, what I saw on Amazon was like $7,000. And H100, I'm seeing $40,000
*  in headlines. But I'm feeling like that is probably more a reseller price, not like what
*  people are mostly paying. Could you give us general guidance on what these things actually cost in the
*  market today? If it's cloud prices, then they are all available. Cloud providers
*  publishing the prices. So it's A100 can cost, while machine can cost between $20 to $40 an hour.
*  So that's really expensive. H100 will be more expensive. They are still not available on AWS.
*  I think they are available on Azure, for example. H100 are available on smaller cloud providers.
*  We already offer H100. So you need to pay a lot for the newest
*  GPUs. They will be more performant. So it's important to understand that it's not just about
*  the absolute cost of the GPUs. It's also about the performance. Because if your GPU costs two times
*  more, but your workloads are only four times faster on those GPUs. So yeah, it's actually
*  the best solution for you, right? It's both cheaper and faster. So H100 is, according to
*  the GDF benchmark, much better, much lower performance compared to A100 and previous GPUs.
*  Usually GPUs become more and more performant, right? The actual numbers around the performance
*  increase are really dependent on the workloads themselves. But they also come up with higher costs.
*  Now when it comes to long-term services, if you go to NVIDIA and buy a GPU, state-of-the-art
*  DGX machines, then you can pay hundreds of thousands of dollars for one machine. It would be, though,
*  high-end performance for a GPU machine. But you pay hundreds of thousands of dollars.
*  One quick follow-up on the on-demand pricing. Because when I was researching for this, I found
*  Lambda Labs seemed to have the lowest A100 price that I was able to find online. It was just over
*  a dollar. I think it's a $1.10 an hour. And they quote AWS prices at being $4 an hour.
*  Were you maybe citing something different there? Or is that accurate in your understanding?
*  Okay. So I said between $30 to $40 an hour for a whole GPU machine with eight A100 GPUs.
*  Eight packs of that, so that's AWS, right? Yeah. So that's one of the advantages of Lambda.
*  Lambda Labs, they offer very significant, significant $3 prices. That's one of their
*  advantages for sure. How do you see it? How is that sustainable? I understand there being a big
*  delta between making an upfront investment in an on-premise physical hardware, even if you're
*  co-locating it, whatever, versus the flexibility of the cloud. But it's surprising to me that there
*  would be a 4x difference, especially in the presence of companies like yours that are
*  multi-cloud and help you kind of optimize and shift around. How do you understand that 4x
*  difference in on-demand pricing? That's an amazing question. I don't know. I really don't know.
*  Full HD, I agree. It's a lot. It's a big difference. You can just get a spot. But I think
*  it's an interesting question to ask Lambda Labs. Yeah, their H100 pricing is
*  $2 an hour, basically. So they're selling the H100, renting the H100 at still half, though,
*  of the AWS A100 price, which is definitely pretty confusing. Okay. Well, yeah, I'll continue to try
*  to figure that one out. So let's maybe move to... I don't know if this will be kind of in scope or
*  out of scope for your business, because if I understand the technology, as you've described
*  you're at the CUDA layer, which is the NVIDIA proprietary software layer, which I would say
*  many people, from what I understand, and I haven't explored other alternatives, but from what I
*  understand, that is often said to be one of the huge value drivers is that the software
*  actually works. And then you're kind of injecting another layer into that strategic advantage that
*  NVIDIA has and even adding more functionality. But I was kind of also curious, like, what other
*  chips are relevant today or what kind of other chip efforts are relevant today? Obviously,
*  NVIDIA has got huge demand and the stock price reflects that and people are waiting for their
*  things. Do you guys see yourselves trying to partner with other chip makers? And whether you
*  do or don't, I'd love to get your take on kind of what other chip makers are going to be relevant
*  over the next few years as AI just continues to presumably scale and scale and scale.
*  As you said, we're sitting in different layers of the software stack. So we're sitting in the
*  CUDA layer and we're sitting at the Kubernetes layer. We're sitting on top of the Kubernetes layer,
*  we're sitting on the two of them that are running. So we're sitting in different layers and we're
*  working very closely with our hardware players and we're working very closely with Kubernetes
*  providers and Kubernetes, like, Rebro and all child providers. And I think that market for AI
*  chips is really interesting. There are a few players, as I see. So in NVIDIA, of course,
*  people say that NVIDIA has 87% of the market. That's a big number. The players in the market,
*  as I see, first of all, they are child providers. So AWS and Google, they own their chips and both of
*  them are building and working on those chips in Israel. So Israel engineers are amazing.
*  They are really good with hardware and they are really good with software as well. And so
*  I'm using and we're getting out plenty of AI chips here in Israel. I think that as well,
*  NVIDIA is also the best in Israel. They bought Metanux or they're really talking.
*  That's all fabless design, right? There's no actual, are there fabs going in as well?
*  Or I'm understanding this to be the design layer. No, that's fabless. That's really interesting.
*  Intel becomes like so much better now. Intel always had their own fabs for their own usage.
*  And now they're going to the region where they offer their fabs to others. But that's another
*  interesting topic. But in terms of the AI chips, all of those players, they are fabless. AWS,
*  they have already chips for training, chips for reference, also doing their cloud. Google is
*  already for several years, I think more than five years already. Their GPUs is also doing that cloud.
*  There are players like AMD and Intel. So AMD is a strong competitor because their GPUs are used
*  in a significant way in the gaming industry. So they are strong there and their GPUs are really
*  good. Their technology is really good. So they are a strong competitor, which is starting to see more
*  and more usage. We have customers running workloads on IoT. And Intel is also investing. Intel is also
*  investing in Azure with those chips. And there are startups, like there are startups, a few of them,
*  that are also also their own chips on one. And that's interesting. And as you said, I think
*  Nvidia is controlling the market. It controls the market because of their software stack and a lot
*  of because of the software ecosystem. So it starts with a cool development, but it goes much
*  beyond that. So with VR, it's investing a lot. Therefore, it's just getting out a lot of software
*  libraries, software frameworks, software tools in the AI ecosystem just to enable AI to enable
*  more and more workloads to run on GPUs. But as I said, it's really easy to run workloads today on
*  GPUs, on the VDS GPUs. Sometimes it's more difficult to run them on other chips, but I think with time
*  it will become more and more easier. So that's the ecosystem. And I think also in video,
*  really, Nvidia is a great company. The GPUs and the technology that they are really really advanced
*  and they are hopefully what the market will need in two years, three years time. So they are already
*  offered right now. So they came out recently with the great Salker 3. So that's a new 3.
*  And they got really interesting technology there. And they are also getting big GPUs with a lot of
*  memory. They are really seeing what the market needs. And I think right now the market needs
*  to run huge models with a lot of memory. Memory becomes at the bottom. And they have this offering
*  already out. And that we go to support those big models. I think it really is a great company.
*  And as time will go, we'll see a second player. It will be really interesting to see who will be
*  that second player. So it sounds like AMD you probably put in the second position
*  right now in terms of at least being a proper rival to Nvidia. We've got the Amazon,
*  the Google TPUs. Microsoft has recently announced that they're designing their own
*  chip too. I don't know if I said meta yet, but they've had their own chip and have one of the
*  biggest clusters in the world as well. What about other companies like Samsung didn't come up there?
*  Tesla? Do you see those two as potentially big timers? Maybe, maybe. And Tesla,
*  you forgot to mention Qualcomm as well. So Qualcomm is also a player that we don't want to
*  underestimate. And then let's see, like Qualcomm and Samsung, they have their own offering. They
*  might have an interesting offering with custom inference and running inference and running
*  models at the edge. That's a market that will continue to grow. And there are opportunities
*  for sure for players that are traditionally good in those markets like Qualcomm,
*  Nvidia and Samsung selling their edge and devices. But you know, the AI market is really different
*  than previous markets. First of all, because software is really important. It's not just
*  hardware. And this is why hardware and software must have the software at the start on top of it.
*  It's like security car made that. And also the space is more so fast. So you know that
*  other manufacturers need to go faster as well. They need to provide more innovation in the faster
*  pace. So in this AI space, I think it's any different than compared to previous markets that
*  we saw. Are there any other kind of smaller or specialist companies that you would suggest to
*  keep an eye on? Like one that comes to mind for me, because we had CEO Andrew Feldman on as a guest
*  with Cerebris Systems and they've made, as I'm sure you're aware, the biggest ever chip,
*  very different approach, obviously. Do you see them or other kind of smaller,
*  what had been more niche chip companies being able to grow in a significant way?
*  Yeah, Cerebris, they have an amazing offering actually. I haven't tried it.
*  Yeah. But it's really unique and it's really differentiated. And you know, let's see,
*  let's see, maybe they might have a little opportunity. I think the AI chip market is
*  going to be huge and even small players will get huge revenues. So this market is going to be huge
*  with no doubts. And so there are opportunities there with no doubts. How about just the rest of
*  the world? What do you think is kind of the state of or the outlook maybe for Chinese companies,
*  any European companies? I mean, they kind of want to get your take at a higher level as well on just
*  the geopolitics of all of this. Everybody's kind of waking up to the fact that this is
*  somewhat of a strategic resource. I mean, it's maybe not quite oil, but it's increasingly,
*  I think, kind of thought of as the next oil. Do you think countries like China or
*  trading blocks like Europe can develop their own champions that can enter this top tier over the
*  next few years? Or is that just, they're just too far behind and it's just still impossible?
*  Listen, they had a great question. And a couple of years ago, people spoke about all the innovation
*  coming out from China. People spoke about all the research and all the academic papers coming out
*  from China. And people said, what's going on with the US? The US is behind. That was the story two,
*  three years ago. The US is behind China. And see what happened. I think what happened in the last
*  six months or one year, that was amazing. It really showed the strength of the city combating
*  all the innovation and the technology coming from California with the opening eye coming out
*  with the charities. I think the US really showed the strength in the last six to one year. So
*  it showed, you know, that it's moved so fast. I think China now is behind. The girl political
*  issues, right? That's a really interesting topic of different angles, right? On where the chief
*  angle without this people happening, right? It's really interesting chips are strategic, not just
*  to come to countries. And we're seeing this chip war with China. Really interesting stuff around AI.
*  I think there is an ace right now. There is an ace in the Western world, but there is an ace
*  with China as well. And it's amazing thing that it's just starting. Things are moving fast, so,
*  so rapidly. You could see, for example, on OpenAI with their charity. A few months ago,
*  I heard that everyone spoke about how good charity is compared to others, right? That
*  it's much, much better than anything else in the market. And I think now I'm starting to hear that,
*  you know, I know a model provided for that very good models makes it even better than
*  the technology gaps are being closed. Right now, my analysis is that China is behind the US. But
*  but you know, I don't know how fast that gap would be closed. I guess it will be closed.
*  Things are moving so fast. Right now in the airspace, what would happen?
*  You have six months.
*  Yeah, no, unfortunately, I totally agree. It's my guys always say my crystal ball gets real
*  foggy after about six months. Yeah, I'm with you on that for sure. Obviously, I have a US based
*  perspective. I guess I'd love to kind of hear do you think and you spend time here and also in
*  Israel. I'm interested in like, is there a difference in worldview around AI dynamics?
*  You know, here, I think we honestly have a sort of, in my view, counterproductive framing of AI
*  as this, you know, new front in the contest or rivalry between the US and China. And I'm not
*  really comfortable with the idea that we are creating these sort of seemingly, you know,
*  pretty severe escalations along the lines of trying to cut China off from leading edge chips.
*  To me, that seems like it really increases the risk of other kinds of conflict. Because,
*  you know, for example, if they can't buy any of the chips from Taiwan, you know, then maybe that
*  makes the cost of disrupting the production in Taiwan much easier for them to bear.
*  Maybe I'm simpleton on that. But how would you describe the kind of, you know, watching from
*  maybe not a neutral country, but certainly a country that's, you know, far from both of the,
*  you know, the two would be hegemonic rivals? How does the rest of the world see this US China dynamic?
*  I think, from my perspective, the geopolitical issues are really escalating in the last, you know,
*  10 years. Right? The things that are being estimated, it's China and the US. Israel is a
*  very small country, and we have a lot of political issues and a lot of challenges with our neighbors
*  as well. Right? So we also really always in a need to protect ourselves against our
*  other countries that are threatening us, you might say. So I think that for us, Israel, we used
*  to be at this state of mind that, you know, that there is danger, that there are countries that are
*  not, are aiming against us. Right? And so, yeah, it's a big question. It's a huge question. I
*  think, like, I don't like to see things escalating geopolitically. It seems to have gone in that
*  direction, right? But I'm optimistic in my nature. So I always hope that things will become better.
*  It's obviously impossible to characterize Israeli opinion briefly. I know there's a lot of
*  disagreement and contention on everything, but you could either speak for yourself or try to
*  characterize it however you would. But do you see, do Israelis see the view from this kind of middle
*  part of the world? Does China look like an adversary from there? You know, I mean, obviously,
*  there's a lot of kind of local dynamics with neighboring countries, which are much more
*  historically rooted. But like, does China look like an adversary from Israel?
*  From our perspective, Iran is the adversary. Iran is the number one adversary for Israel.
*  And from our perspective, Iran is playing with China from there on the Syrian side,
*  from our perspective. I think that's one of the strengths of Israel and partnership with Israel,
*  the US. From our perspective, Iran is the number one adversary.
*  That perspective, I think the Israeli people really see eye to eye with the American people.
*  They don't like to see things escalating, but they also know that they see the danger.
*  And so I think for several decades already, collaboration between Israel and
*  Iran is around those topics. But as I said, I'm optimistic. I'm always hoping for the best.
*  AI, for sure, if we're going back to the way it was, AI for sure had an impact on that.
*  Because now with the Israelis, the Israelis countries are being armed with AI technology,
*  and they are going to change their defense space. But now that's going to charge for
*  defense space. So for AI, chips are really important. So chips are strategic.
*  AI is strategic for countries. And we will see, I think, their political state changes
*  in the next decades. That's because of AI. Do you see that this sort of supply control
*  is likely to be viable for kind of controlling who can do what with AI? I mean, that could be
*  in the context of China, right? We could say there's these export controls and they can only buy
*  H800s instead of H100s. And then I wonder, is that really going to work? Or is there going to be
*  some way to get around that, either by post-manufacturing even, or maybe just
*  very clever software work that could circumvent some of these imposed restrictions? And then I
*  also think about that in the context of the just AI safety dialogue and discourse in general,
*  people are very kind of hopeful. And I'm not sure how realistic these hopes are that maybe we could
*  have a sort of know your customer regime for GPUs and you can only buy so many before you got to
*  have a license or a permit to do whatever. Do you feel like this is a sort of controllable enough
*  resource that it's ultimately going to be fruitful to try to
*  control the development of AI through controls on hardware?
*  That's a great point, right? People are thinking about regulating AI. And so coming from the compute
*  angle, that can be an interesting angle, just controlling access to your compute. So that's
*  what we are right now with the chip war between the US and China, right? They are just controlling
*  the access to their newest GPUs. So China is not allowed to get access to the newest GPUs
*  according to the US regulations, right? So now people are speaking about AI safety and about
*  the progress of AI regulating how AI is being used. And so can that be controlled with compute?
*  I don't know. I don't know. Because right now to train, if you go, I'll become a little bit
*  technical, but if you train huge models and you try to get to state-of-the-art models, then you
*  need a lot of compute. Right now you have this open source model. You can train them on your data.
*  You don't need tens of thousands of GPUs to do that, right? Just yesterday, Meta, which I love,
*  allowed Meta to do right now. The open source LANA 2, right? Open source LANA 2 is free for
*  for research and commercial users, if they say. So that's really, really exciting. And now we
*  have those very capable models, open source, and people can take data on that and find those models
*  we've done, using that data. They don't need a lot of compute. So then controlling the access to
*  compute becomes a must-get event, I guess. So it's interesting to ask. You know, regulating AI,
*  I don't think it's an easy question. It's really complex.
*  That's probably a good note for us to leave it on. I know that, you know, regardless of how all this
*  develops, and there is tremendous uncertainty, you and the team at Run AI will be helping people get
*  the absolute most out of their investment in GPUs. So Dr. Ronan Dhar, thank you for being part of
*  the Cogrev revolution. Thank you, Nat. I'm back. It was great fun. Thanks.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work, customized across all platforms with a click of a button. I believe in Omniki
*  so much that I invested in it, and I recommend you use it too. Use Cogrev to get a 10% discount.
