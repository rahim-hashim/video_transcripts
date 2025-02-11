---
Date Generated: October 13, 2024
Transcription Model: whisper medium 20231117
Length: 3285s
Video Keywords: []
Video Views: 472
Video Rating: None
Video Description: Nathan and co-host Stephen Parker delve into the world of AI video generation with Anastasis Germanidis, Co-Founder and CTO of Runway. This episode of The Cognitive Revolution explores the cutting-edge technology behind Runway's Gen 3 models and their impact on the creative industry. From emergent properties in scaled-up models to the democratization of video creation, join us for an illuminating discussion on the future of AI-generated content and its potential to reshape entertainment and culture.

Check out Runway here: https://runwayml.com

Apply to join over 400 Founders and Execs in the Turpentine Network: https://www.turpentinenetwork.co/

SPONSORS:
Notion: Notion offers powerful workflow and automation templates, perfect for streamlining processes and laying the groundwork for AI-driven automation. With Notion AI, you can search across thousands of documents from various platforms, generating highly relevant analysis and content tailored just for you - try it for free at https://notion.com/cognitiverevolution

Weights & Biases RAG++: Advanced training for building production-ready RAG applications. Learn from experts to overcome LLM challenges, evaluate systematically, and integrate advanced features. Includes free Cohere credits. Visit https://wandb.me/cr to start the RAG++ course today.

Omneky: Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Oracle: Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

RECOMMENDED PODCAST:
This Won't Last - Eavesdrop on Keith Rabois, Kevin Ryan, Logan Bartlett, and Zach Weinberg's monthly backchannel ft their hottest takes on the future of tech, business, and venture capital.
Spotify: https://open.spotify.com/show/2HwSNeVLL1MXy0RjFPyOSz

CHAPTERS:
(00:00:00) About the Show
(00:00:22) About the Episode
(00:03:05) Introduction and AI for Creative Work
(00:03:39) Video Generation as World Modeling
(00:05:52) Emergent Properties in Scaled Models
(00:08:44) Importance of Architecture vs Data
(00:10:57) Multimodal Models
(00:15:52) Sponsors: Notion | Weights & Biases RAG++
(00:18:37) Video Understanding and AGI
(00:25:03) AI Agents for Video Creation
(00:27:30) Runway's culture of shipping
(00:29:20) Balancing Research Publication and Strategy
(00:33:19) Sponsors: Omneky | Oracle
(00:34:40) Features Variety Release Cycle
(00:36:54) Power Users
(00:38:56) Interactive Video
(00:40:40) Scaling Challenges
(00:42:21) Future of Creativity
(00:45:24) Competing with Giants
(00:47:39) Model Divergence
(00:49:28) Disclosure vs. Strategy
(00:51:19) Runway ML's API
(00:54:23) Outro

SOCIAL LINKS:
Website: https://www.cognitiverevolution.ai
Twitter (Podcast): https://x.com/cogrev_podcast
Twitter (Nathan): https://x.com/labenz
LinkedIn: https://www.linkedin.com/in/nathanlabenz/
Youtube: https://www.youtube.com/@CognitiveRevolutionPodcast
Apple: https://podcasts.apple.com/de/podcast/the-cognitive-revolution-ai-builders-researchers-and/id1669813431
Spotify: https://open.spotify.com/show/6yHyok3M3BjqzR0VB5MSyk
---

# Runway's Video Revolution Empowering Creators with General World Models, with CTO Anastasis
**Cognitive Revolution:** [October 09, 2024](https://www.youtube.com/watch?v=tCZd5f7yiDk)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today I'm excited to share my conversation with Anastasis Germanidis,
*  CTO of Runway ML, a company that's become synonymous with AI video footage generation,
*  and which with their latest Gen 3 models continues to lead the video generation market.
*  Joining me as co-host for this episode is my good friend Stephen Parker,
*  creative director at Waymark and co-creator of the AI-generated film The Frost,
*  which we've covered in a previous episode.
*  As a power user of a great many generative art tools, including Runway, Stephen brings
*  an extremely valuable perspective to this conversation.
*  I came away from this discussion really super impressed with Anastasis. We threw a lot at him,
*  and he gave very nuanced, thoughtful answers on a wide range of topics,
*  including video generation models as world modelers and the potential role of video
*  understanding on the path to AGI. Emergent properties that Anastasis and the Runway team
*  have observed as they've scaled up their models, including surprisingly accurate liquid simulations
*  and improvements in 3D consistency, Runway's product development philosophy and culture of
*  rapid iteration, including how they think about shipping upgraded models even if they might
*  disrupt existing user workflows, and of course, the challenge of scaling to meet explosive demand.
*  We also touch on the creative possibilities unlocked by these tools, from pre-production
*  storyboarding to generating footage for use in final productions, the importance of data quality
*  over architectural complexity, the potential for the next generation of models to incorporate
*  audio, the intriguing possibilities of interactive AI generated environments,
*  how all this technology might shape the future of entertainment and culture more broadly,
*  and even how Anastasis thinks about competing in a game of scale with tech giants who have
*  functionally unlimited resources. In Runway's innovations, we can clearly see signs of things
*  to come. Democratizing access to high-quality video creation means more stories from a wider
*  range of voices, but also potentially major economic disruption for the iconic American film
*  and television industry. As always, the pace of change is relentless. Since we recorded this
*  episode, Runway has indeed launched API access, and we at Weymark are super excited to be among
*  the first wave of customers to try it out. If you're finding value in the show, we would love it if
*  you take a moment to share it with friends or leave us a review on Apple Podcasts or Spotify.
*  And of course, we welcome your feedback via our website, cognitiverevolution.ai,
*  or by DMing me on your favorite social network. Now, I hope you enjoy this illuminating discussion
*  about the technology behind and the impact to come from AI video generation with Anastasis
*  Germanitis, CTO of Runway ML. Anastasis Germanitis, CTO of Runway ML. Welcome to the Cognitive
*  Revolution. Great to be here. I'm excited for this conversation and also excited to have my
*  teammate and friend, Stephen Parker, creative director at Weymark along for this episode.
*  We're going to get into generative AI for creative work, and he is an expert in that with a film that
*  we've covered in a previous episode, The Frost, now traveling the globe and making its debut in
*  Singapore. I will be the least knowledgeable about what is going on here today, but excited to have
*  this conversation. I thought we would start with a big picture discussion of video generation as
*  world modeling and as a step on the perhaps critical path to AGI. I'd love to hear your
*  perspective on the case that video generation really is something that we have to have on the
*  way to an AGI destination. Humans are visual beings. Being in the physical world is a fundamental
*  aspect of being human, and you can formulate so many tasks humans do in the modality of video.
*  World models is, as those models basically learn through video data, large volumes of the video
*  data. They gain powerful representations of the 3D world. They gain representations about a wide
*  range of human activities of different tasks that you can perform in the world. That knowledge can
*  be leveraged to generate video, which is where we came from, but also for a variety of different
*  other tasks. Video models will kind of power huge applications in robotics to build representations
*  of the world. One framework I like to use is that every representation of the world, whether it's
*  video, whether it's language, whether it's another representation, is ultimately a proxy for reality.
*  But video itself has much less inductive biases than text, specifically the text that language
*  models are trained on. Text captures a much smaller subset of everything that humans care about compared
*  to video. So that's in a nutshell kind of the case for why video generation can lead to broadly
*  useful general intelligence and how we're thinking about it. So lots of impact there. A couple just
*  follow-ups in different directions. One might say, is video enough? If you're to take that argument,
*  could you say maybe we need actual 3D point grid representations of the world? Is it a matter of
*  just video being abundant relative to an even richer modality that makes it the natural place
*  to work from? Or do you think that video is in some way a threshold that means it can do
*  similar things as if you had a full 3D model? So what we found is that you can essentially learn
*  3D. You can gain 3D knowledge simply from the 2D footage. Models like Gen 3 have remarkable
*  3D consistency. And like if you're generating a camera moving in a specific direction,
*  essentially you'll see things in the environment remaining consistent as you expect from a 3D
*  point of view. We think 2D representations are sufficient to capture 3D knowledge. 3D data is
*  really hard to find at scale. And that's why generally research in 3D computer vision has not
*  advanced as much as it has advanced in the 2D domain. So those are the two main arguments.
*  There is the abundance of video data and the fact that you can derive 3D representations from 2D
*  data that makes video a good candidate for learning those broadly useful representations.
*  3D When you mentioned object consistency, that definitely reminded me of OpenAI's statements that
*  the things like object permanence and the sort of intuitive physics that seem to get better
*  with scale, I believe their phrase for describing this was, these are purely products of scale.
*  I wonder what you would say have been the most interesting emergent properties or behaviors that
*  you have seen as you have scaled up? Like what has jumped out and surprised you that you didn't
*  necessarily engineer into the system but nevertheless observed?
*  That statement definitely aligns with what we've seen as well. If you compare,
*  we released Gen 2 more than a year ago. We released Gen 3 recently. If you compare the outputs from
*  the Gen 2 model to the outputs of Gen 3, there is a large step up in capabilities and a lot of that
*  can be attributed to compute. There's a lot of other things that we did differently as we were
*  building Gen 3. We've seen a lot of interesting emerging capabilities of Gen 3. Some interesting
*  things on the world modeling side are the ability to simulate liquid simulation being surprisingly
*  more accurate than you'd expect for a model that has no prior knowledge of how the liquid should
*  behave. There are specific prompts that we tried to understand those scalability like the interaction
*  between a boiling pot where you throw out water on the boiling pot. Those kinds of interactions
*  reveal some really surprising physics knowledge embedded into the model and that's all completely
*  learned from data learned from scale. There's no specific inductive priors that we introduced the
*  model to make it follow the laws of physics. There is a lot more room to further improve those things.
*  The model doesn't fully follow the laws of gravity perfectly. Even generating something
*  like a bouncing ball can be challenging. I don't think the problem is fully solved.
*  If you see the delta between Gen 2 and Gen 3 and you extrapolate from there, I don't see a fundamental
*  reason why that additional physics knowledge and the more precise understanding of the world is not
*  going to emerge. How much do you think the architecture matters? Different companies have
*  given different amounts of windows into their architectures. Do you think that the different
*  big efforts to build these sorts of models will converge and ultimately have a similar architecture
*  that is found to work the best or do you think there is room in the space of possible models to
*  see divergence of different strengths and weaknesses? There's definitely more algorithmic
*  improvements to be made. I don't think our collective exploration is a field of possible
*  architectures. It has reached the conclusion. Of course, there is a lot more convergence to
*  transformers and components and it's a very small set of architectures across modalities.
*  At the same time, I do think there's been traditionally much more focus on architecture
*  compared to data, objectives, tasks in the field of machine learning. If you look at the most recent
*  computer vision conference and take a survey of all the papers, you'll see there is probably a
*  disproportionate focus on architectures than on other aspects of training those models.
*  Data is really important. Specifically, the tasks that you're teaching the model
*  through data is something that there's probably less published work on as much as architecture.
*  Have you studied CANs at all? That's the Kolmogorov Arnold network that's out of Tegmark's
*  group at MIT. Ziming Liu is the first author. The reason I bring it up is they've created a way to
*  learn activation functions and now they've also created a way to initialize these networks with
*  specific activation functions that can encode a whole range of useful physics operators into
*  a network. It seems to me an extremely promising neuro-symbolic approach. If you've seen that,
*  great. If not, I wonder if you have any thoughts on embedding into future architectures things that
*  would be obvious calculations that one might want to actually run simulated physics. Obviously,
*  you said gravity is not perfect. If you could build in a parabola operator into the network,
*  presumably that would help with getting these fine points dialed in a little bit more.
*  Any thoughts on that? I'm not very familiar with the paper, but I think something that very often
*  happens with a lot of new architectures that supposedly perform common architectures. We saw
*  myriads of different alternative forms of linear attention. At some point, that was a big focus of
*  the field, just figuring out if there is a more efficient mechanism of attention. Very often,
*  the way those are presented in literature can lead to wrong conclusions. One very common thing is
*  comparing the performance of two models with the same number of iterations, but not taking into
*  account that those models might have different amount of compute per forward pass. There's all
*  those different things that end up confusing the overall conclusion for my paper. It's really hard.
*  There's a lot of people working on improved architectures, and generally, it's very rare
*  that you find something that outperforms the current architectures. I think there's definitely
*  room to improve on what we have, but generally, it's good to start from a place of-
*  Don't be too excited on the first paper. Yeah. I would say not infusing too many
*  inductive biases or prior knowledge into the models, and instead, choosing data carefully
*  or choosing the whole training regime carefully. I think it's a much more scalable approach,
*  or at least that's what we found. It sounds like you're saying,
*  almost I hear echoes of Ilya, the models just want to learn. Don't think too much about the
*  architecture, easy to overcomplicate it. What really seems to matter is data quality, scale,
*  and letting them do their thing and facilitating that more so than trying to engineer it into them.
*  I wonder if you have a take on another recent paper I'm obsessed with, the platonic representation
*  hypothesis, which seems to suggest that width scale models are gradually converging in terms
*  of the way they represent concepts internally. I guess I'd be interested in your take on that.
*  How do you think about that as it may or may not have implications for the strength of multimodal
*  models? I wonder if that pushes you to think, maybe we should do more of the video. What are
*  we missing that textbooks or long math proofs might be bringing to the overall data set if we're
*  primarily just focused on a video training corpus? Yeah, I'm a big fan of that paper,
*  and I was alluding to it earlier on. Basically, the main idea is as you scale models with
*  different modalities, they converge into similar representations, and that's argued in a few
*  different ways. One very interesting argument is that as you scale models, they arrive at simpler
*  solutions to problems. I'm not necessarily suggesting that video needs to be the only
*  modality that you train on. I'm saying it's a more general modality than text. You can imagine
*  models that are trained on many different modalities, and each modality maybe has
*  specific aspect of reality it captures in the more compact, useful tokens. I'm not opposed to
*  the idea that you can train on different modalities that have different strengths
*  rather than training just on video or just on text, but I think the focus on text as the modality that
*  we look at the general intelligence may be misplaced. A lot of what we're trying to argue
*  from the runway research perspective is that video tokens are really useful and reveal so much
*  of the world that's not actually captured text corpora and the main argument, but I do think
*  ultimately as we're getting closer to more general intelligence systems, they will need to be able to
*  utilize these modalities. Can we dig in on that for a second? I was thinking that mixed modality is
*  really a huge thing for you guys coming up soon, I would imagine. There's sight and sound in video
*  right as crucial components and the idea of a mixed token training regime seems like a fascinating
*  prospect for the future. How do you guys think about including sound as you go about this?
*  Yeah, it's definitely something that we're going to do at some point. I think our focus has been
*  really making sure we can get the visual quality and visual generation to be as good as possible.
*  I think we haven't saturated the improvement there that right now it's beneficial for us to focus on
*  just visual modality. I do think eventually generating both frames and sound associated
*  with those frames is definitely the next step, but there is just so much more to do on getting
*  video generation quality to be better and many interesting problems to solve along the way.
*  That's our primary focus, but eventually you want to generate both. I agree.
*  Hey, we'll continue our interview in a moment after word from our sponsors.
*  As a Cognitive Revolution listener, you're obviously interested in cutting edge AI technology.
*  And with that in mind, I'm proud to say that this episode is brought to you in part by Notion.
*  Notion has been a clear leader in high value applications of generative AI since the wave
*  began. Earlier this year, we had Notion AI engineer Linus Lee on the podcast. The quality of his
*  insights showcase the caliber of talent that Notion employs. And that inside look at how
*  Notion builds with AI is still extremely valuable. Given my personal focus on AI automation recently,
*  I specifically wanted to highlight Notion's library of workflow and automation templates.
*  If you're looking to streamline your processes and lay the foundation for future AI driven
*  automation, these templates are an excellent starting point. And even if you're not ready
*  for full automation, you'll benefit immediately from Notion AI. Notion's latest all in one AI
*  implementation that searches through thousands of documents, regardless of whether they live
*  in Notion or on some other platform like Slack or Google Docs, to deeply understand the context of
*  your work and generate highly relevant analysis and content just for you. Notion is used by more
*  than half of Fortune 500 companies, helping teams reduce emails, meetings and time spent searching
*  for information. Want to try it? Head to Notion.com slash Cognitive Revolution. You can start for free
*  and using our link supports the show. So join me in giving Notion AI a shot today at Notion.com
*  slash Cognitive Revolution. As a developer, the journey from concept to production ready,
*  large language model apps is fraught with challenges, dealing with unpredictable language
*  model outputs, hallucinations and ballooning API costs can all be blockers to shipping your next
*  AI powered feature. That's where advanced RAG comes in. With the new RAG plus plus course from
*  Weights and Biases, you can overcome these hurdles and build reliable production ready RAG applications.
*  Go beyond proof of concept and learn how to evaluate systematically, use hybrid search
*  correctly and give your RAG system access to tool calling. Based on 21 months of running a customer
*  support bot in production, industry experts at Weights and Biases, Cohere and Weaviate show you
*  how to get to a deployment grade RAG application. This offer includes free credits from Cohere to
*  get you started. Make real progress on your large language model development and visit
*  WNB.me slash CR to get started with their RAG plus plus course today. That's WNB.me slash CR
*  to get started with their RAG plus plus course today.
*  Do you think of yourselves as an AGI lab at this point? I wasn't quite clear on
*  where's the case that this is going to be important and we are going to go do that.
*  I wonder, I also imagine too there must be some interesting tensions between when I think about
*  all the stuff that people are generating with runway today, so much of it is fantastical,
*  impossible, magical. There's seemingly a notable divergence between what I would
*  train on and what I would want to empower people to do if I was trying to allow them to make films
*  to entertain people versus if I was trying to maximize my universal physics simulation abilities.
*  That seems maybe fundamental. Is there a sort of magical realism token that gets put into
*  the mix at some point to distinguish between when the rules of physics are supposed to apply
*  and not? I also wonder if this has any relation to why OpenAI hasn't launched their thing hardly
*  at all to date because maybe they're thinking we don't really care about making films. We just
*  want to simulate the world. They can maybe afford to do that with the resources they have. Are you
*  an AGI lab? Do you feel a tension between realism and surrealism? Any other speculations would be
*  most welcome. Yeah, we're not an AGI lab. I think the definition of AGI has been very unclear to me.
*  Define it for yourself if you want to declare yourself an AGI lab.
*  But I think there's a lot of other terms that are more useful to us. I think a lot of how we
*  see ourselves is augmenting human intelligence and augmenting creativity versus trying to build
*  agents that are generally intelligent. I also think if we take Turing tests as the criterion for AGI,
*  we can trace discussions in AGI back to the Turing test. And that's such a noisy test to
*  determine intelligence, like whether someone will perceive a system to be intelligent or not.
*  So I do think something more useful than achieving AGI is building more capable simulators of the
*  world and being able to simulate different aspects of reality. I don't necessarily think of it as one
*  milestone where we sufficiently simulate the reality. Reality has an infinite amount of
*  complexity and detail at different levels of abstraction. Something I don't like with AGI
*  as a goal is that it kind of enforces a break point where once you get there, you've achieved
*  AGI. For me, it's a much more continual progress narrative. So a big focus for us is really
*  extending human capabilities. The other part that I find trouble with the AGI concept and discussion
*  is the way I think about humans and human capabilities is directly tied to technology.
*  With every new technology, every new system that we build, we're extending what it means to be human.
*  Suggesting that there is a moment of parity where we've achieved parity with human intelligence,
*  for me, doesn't quite make sense if human intelligence also changes over time with
*  technology. So broadly, my thoughts on the AGI topic. Your second question of whether building
*  those world simulators is compatible with the creative use case we're focusing on,
*  I don't think it's incompatible. My argument for that is that as the models get better,
*  essentially they're learning a data distribution and as the data increases in scale,
*  they're increasingly approximating reality. In some ways, as the models increase in capabilities,
*  they learn a wide variety of tasks and you can combine those tasks in novel ways to create
*  things that are out of distribution technically. As the models improve, the way they can go out of
*  distribution becomes more interesting. So in a way, the better those models become, the better they
*  also become at creating novel combinations of things. You can see that with a lot of AI images
*  and videos, they're combining concepts in ways that have not been combined before. That comes from
*  really learning those individual concepts well from data. So the better those models become,
*  the better they become, essentially hallucinating, which in our case, it's a useful property to have.
*  We want the models to be grounded in some capacity in terms of understanding language well, then user
*  intent as you're creating with those models. But we also want them to be imaginative and arrive at
*  novel combinations of concepts and create videos that do not seem similar to any videos I created
*  before. You can see that with a lot of the outputs from Gen 3, you can generate moving through
*  an environment and opening a door to a completely different environment. And the model is able to
*  reason on how to create those very unlikely outputs just because it has really learned
*  the constituents parts of what you're trying to generate really well, and is able to combine them
*  in novel ways to create the final output. Have you done interpretability on your models? In the
*  large language model space, of course, there's been a lot of interpretability. There's been
*  sparse auto encoders coming online recently that show distinct concepts that are operative at any
*  given point in time. I was joking a minute ago when I said, is there a magical realism token? But
*  it strikes me now that perhaps not a magical realism token at the input level, but a magical
*  realism learned concept somewhere in the 80% through the model range actually might be
*  quite likely. Have you had a chance to go that far, apply any of these interpretability
*  techniques to what you've created? It's an area I'm very interested in. We haven't done as much
*  work on that area, but it's something that we're investing more efforts on. I think it's really
*  interesting to understand what the concepts are for those models, and it becomes even more
*  interesting in the visual domain because from a controllability perspective, it's powerful to
*  detect magical realism token. Now you can activate it and ensure that your generations will have
*  the qualities that you want. I think it's a super interesting area. We don't have too much to share
*  on that yet. I can imagine the Golden Gate experience where the Golden Gate bridge shows
*  up in every teacup no matter what the prompt was. I mean, again, if all these things are converging,
*  it stands to reason that probably is not too far off into the future. You said, we're not trying
*  to create agents. How long does the video clip need to be before there is an implicit agent
*  in the little people that are being simulated? It seems like a 10 second window, you maybe can
*  get by with stochastic parotry. It can be imitations of other things that it's seen,
*  but if you intend to extend the length of what can be generated into longer and longer scenes,
*  it seems like at some point there is likely to be a little agent type ephemera arising in the process
*  of just predicting what the character is going to do next. Does that seem too far out for you to
*  entertain at this point, or do you actually think there could be little proto-ephemeral agents
*  hanging out in the models? If I understand what you're saying correctly, you're saying,
*  let's say you generate an egocentric video, essentially a day in the life of someone.
*  As you generate a long enough video, you'll see the person taking different actions in the world.
*  In order to predict those actions correctly, you essentially need some implicit model of
*  reasoning capability to decide what actions to take or how to respond in the world.
*  I think that's very plausible. As a small scale, increasing capabilities, that definitely, I think,
*  could be the case. I think what's interesting from our perspective is if you can continually
*  provide user input in that generation and you can control it in different ways to either create
*  an interesting output or if you can, going into more on the interactive media side of things,
*  it's one of the most interesting applications looking to the future of video generation,
*  is creating interactive experiences and seeing those models as new rendering engines or game
*  engines. Those are the things that we're more focused on, but I can imagine those reasoning
*  capabilities would emerge at sufficient scale because it's problems that you need to solve to
*  effectively simulate that kind of long duration of videos. I think it's really interesting.
*  You can file this under yet another reason that I continue to find it more and more plausible that
*  we ourselves are living in a simulation. Thank you for going on this journey into the world
*  modeling possibility space with me in the first half. I think it's probably a good time to switch
*  gears and let Stephen take more of the lead, talk about the actual product and how it's being used
*  and the augmentation and philosophy of art. There's a rich set of things to unpack there too.
*  Thank you for agreeing to do this. I'm an avid user of Runway and former New York startup person
*  myself. I think at the beginning, just to wrap as a fan for a minute, maybe you can talk about the
*  culture of shipping that you guys have built. You're obviously quite prolific out in the world these
*  days and shipping changes all over the place. Where does that come from? How do you think about
*  that? How important is that to everybody back at the office? It's very important and it's something
*  that we paid a lot of attention to from the very beginning when it was the three of us.
*  At that point, it was almost an existential thing. If we didn't keep shipping, nobody would care about
*  us and we needed to keep reminding the world that we exist. These days, the technology is moving so
*  fast that it's really important for us that the community that use our tools, our users, are able
*  to follow along with the progress of the technology. We always felt that by continuously deploying
*  newer models, newer techniques, newer tools, it reduces that lag in terms of our perception.
*  I do think shipping continuously is really part of the DNA of Runway. It also builds really great
*  momentum internally. If you continuously are seeing the things that you create being used in all sorts
*  of interesting ways that you can expect by the creatives and the artists using the platform.
*  That momentum has sustained us and it's something that people that work inside Runway have as one
*  of their favorite aspects of being at Runway. It's the ability to see research being translated
*  into amazing forms, amazing artworks really quickly within the span of weeks or months,
*  depending on the specific tool. Listeners might not be aware, as well as some users,
*  I would imagine that you guys actually have a whole wealth of tools, right? You've got stuff for
*  color, reskinning with other styles. There are quite a few video tools inside of Runway, some of
*  which happened before you guys even created the now more famous GenVideo tools. How do you think
*  about keeping up with all of that older tech or tools hanging out in the system, especially now
*  that you guys have gotten super popular with the video generation? Just in terms of priorities and
*  what people want from you, I can imagine we're just sort of trucking along shipping for a while
*  and then one day you have these incredible GenVideo models that everybody wants to use. How do you
*  balance and react to that? The first point is that we were interested in generative models from
*  the very beginning. It's just that the results and the quality of those models was not quite there
*  to build tools that people could use in production or in other use cases. So in the first years of
*  Runway, we had parallel efforts, one on the research side and then the other one is more
*  the product and tool side. And we kept, we tried to improve image generation models,
*  video generation models. At that point, those two parallel paths intersected were like, this is good,
*  it's not perfect, but it's good enough that you can build some really useful tools around those
*  models. Generative models were an interest of ours from the very beginning. When we started in 2019,
*  video generation was not quite usable. The second part is a framework I like to use in terms of the
*  outcomes of those tools versus necessarily tools themselves. Whether you use generative models or
*  more traditional computer vision to achieve those outcomes is less important than achieving
*  those outcomes. One example is one of the most popular tools in the pre-generative era was our
*  green screen tool, which was essentially an interactive segmentation tool. So you can
*  select a specific object or subject in a video and separate it from the background. That's a
*  fundamental aspect in the way video editing and VFX work has been done for a long time,
*  but it's not clear to me that it's going to be a fundamental aspect of video editing. If we look
*  into the future, you can achieve the same goals, which could be that you want to apply an effect on
*  that specific part of the video, maybe just the background or essentially compositing is part of
*  the pipeline. And it's not the final thing you want to do. It's more something that you need to do to
*  get to your goal. And if you can do that final thing without the intermediate step of compositing,
*  then that's a much better workflow. And that's what I think the generative models will enable.
*  Right now, I think we're nowhere quite where we need to be in terms of the ability of those
*  models to understand intention, but I don't see any technical reason why it's not going to happen.
*  And so you can imagine all those editing operations that we had a collection of different tools
*  to perform, you can now do with a single tool or a single interface. So that's how I'm thinking
*  about it. The generative models will eventually be able to handle a lot of those tasks that you need
*  that individual computer vision based tools to achieve. Yeah. When I first saw, I think it was
*  Gen 1, I imagined it was like a pipeline assembly from smaller tools potentially leading up to the
*  output video at the end. Maybe that's not how it works at all. How much of those early tools helped
*  you guys develop this later stuff? Or are these gen models really like living on their own in
*  isolation, their own sort of unique training? So the way to build those models is quite different
*  than the way we were building the tools before. But the early tools really helped us gain a lot
*  of knowledge about what was important in video editing, what people really cared about. And that
*  knowledge definitely transferred to the kind of gen model tooling. I see them as one kind of
*  continuous discovery process towards where we are now. But the way to build those models,
*  they're much more complicated pipeline to get to Gen 3 versus the model powered green screen.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it, and I recommend you use it to use cog rev to get a 10% discount.
*  AI might be the most important new computer technology ever. It's storming every industry
*  and literally billions of dollars are being invested. So buckle up. The problem is that AI
*  needs a lot of speed and processing power. So how do you compete without costs spiraling out of
*  control? It's time to upgrade to the next generation of the cloud, Oracle Cloud Infrastructure, or OCI.
*  OCI is a single platform for your infrastructure, database, application development, and AI needs.
*  OCI has four to eight times the bandwidth of other clouds, offers one consistent price instead of
*  variable regional pricing, and of course, nobody does data better than Oracle. So now you can train
*  your AI models at twice the speed and less than half the cost of other clouds. If you want to do
*  more and spend less like Uber, 8x8, and Databricks Mosaic, take a free test drive of OCI at oracle.com.
*  That's oracle.com slash cognitive, oracle.com slash cognitive.
*  Turning a little bit to features, there are obviously these gen models that people take
*  advantage of inside product. They're surrounded by a range of features, right? Those features might
*  be things like camera zoom in, camera zoom out, pan left and right, things that force instruction
*  in the model. And then as later models come out, those features aren't always there, but there
*  might be more adaptability in the text prompt itself, right? I have more luck as a user saying
*  zoom out from here or pan right just in the text as opposed to a hard tool. How do you think about
*  the release cycle? We have a new model. It doesn't do all aspect ratios yet. It won't respond to all
*  the tools yet, but it's better in all these other ways. We want to go ahead and release it. The
*  world seems to be okay with that cycle now, but I can imagine a future where users are like,
*  I want the next version, but I also want the full set of tools that I had along with it before.
*  How do you guys think about adapting to that and rationalizing through that process?
*  The first thing is something you alluded to is that there is such a big advancement from each
*  model iteration right now that not necessarily all the tools and toggles and sliders that were part
*  of the previous model will be relevant for the next model. So I don't think we're at a point where
*  if the new model was better on the kind of more marginal incremental ways from the older model,
*  I think there's a stronger case that we need to make sure that everything that was part of the
*  previous model is now part of the new tooling. But right now, it's such a big kind of delta of
*  improvement in quality, consistency, and so forth that it makes sense to... It's useful today even
*  if it doesn't have every single controllability aspect of the older model. And having to wait
*  for that would probably make a disservice to our users who want to get advantage of all the
*  capabilities of the newer model. So it's not as big of a consideration to reach priority at the same
*  time if an older aspect of controllability or feature of a model is still useful for the
*  newer model, we want to be able to provide it. And we're working towards adding a lot more
*  capabilities to Gen 3 than even the totality of features of Gen 2.
*  Got it. That's maybe a good segue to the power users of the product. I can imagine they're
*  myriad, but who are some of the strongest representatives? Video means a lot of things
*  to different people. It can mean stock, it can mean film, it can mean commercials, it can mean
*  games. Who's the loudest voice in the room right now? So we have a wide range of customers and
*  users. So from smaller studios, larger agencies and film studios that are using the platform to
*  a wide range of kind of individual creators. I think it's very interesting kind of new emerging
*  kind of genre and culture that's emerging around AI video that we really want to support.
*  And we do that both within the tool, but also with the AI film festival, we do 48 hour film
*  competitions. We really want to support and grow that group of creators embracing AI tools and
*  methods. I think that's only going to grow really fast. That stuff is super cool, by the way. It's
*  like a hack weekend for creators. I think a lot of people really enjoy that. And we have the
*  next one coming up soon, in the coming days. We've had over, I think the latest count was
*  something around 1,800 teams that sign up to participate. Really excited about this new group
*  of creators that are embracing those tools. There's a lot of interest from the enterprise side as well.
*  As I mentioned, film studios are using Runway in different parts of the workflow. We have
*  ad agencies that are using Runway in different ways. You can use it in different parts of the
*  production process. It's really useful in pre-production for storyboarding, for getting
*  to the 80% version of your final campaign or film. And we see a lot of usage for that. Even if the
*  output is not fully usable in the production, it's still really useful to really give,
*  communicate internally, like what does the final result look like. But with Gen 3, we actually saw
*  a lot of the outputs being used in production as well. Again, a lot of limitations to being able to
*  fully generate every shot of a film with a model like Gen 3. But you can generate B-roll footage,
*  you can generate parts of the final result. Can I ask you for hot takes on a couple of recent topics?
*  Game engine, the Doom player. Have you seen the paper and video for that?
*  I have. The first time we've seen interactivity along with the video.
*  Really interesting work. We're really excited about this direction of building interactive engines
*  using generative models. I think what's especially interesting with them is the ability to generalize.
*  You can essentially create a video game from scratch from a prompt. That's the direction
*  I think is really interesting, being able to navigate worlds that you're creating as you're
*  navigating. One aspect of this paper, which I'm less excited about, is that it's essentially
*  trained on a single video game. If you take the size, the Doom video game is probably a few
*  megabytes. The diffusion model was trained based on frames from that video game, what is an order
*  of gigabytes. And so from an efficiency point of view, I don't think it makes much sense that you
*  would use a diffusion model to generate scenes from that game, especially if you don't have that
*  aspect of generalization, which I think is, to me, is the most interesting part of this, the ability
*  to. If you could create variants of Doom that follow your prompt, that would be super cool.
*  But if you're just generating the same footage from the same game, it just becomes a less
*  efficient game engine. Overall, really excited about the direction, but I'm not sure this is
*  the best proof point for it. There was a paper that I found really exciting recently called Genie,
*  I don't know if you've seen it, but essentially you can generate arbitrary platform games and
*  control them. And it's also a video generation model, but I think there's something really
*  compelling there, which is it can generalize to new environments as well. That's the direction
*  most excited about. Maybe the last thing for me is just more on that culture of shipping, but
*  on the culture of scale. What has it been like for you guys to go from small startup to a demand that
*  I can't even imagine dealing with in terms of the product? I mean, people want more and more
*  from you, right? They want faster gens, they want more gens, and you have to figure out how to make
*  it all work. What's that like? Yeah, it's been really exciting. I think the thing that we've
*  emphasized from the very beginning and a big part of our culture beyond shipping is learning fast,
*  learning new aspects of building tools, building technology that the team might have zero prior
*  experience in. And I think that's been the most exciting thing about building Runway is that
*  it's almost been a different company every year. The things that were important to get right every
*  year are different. The ability to scale model training, to build a model like gen three is
*  something that we didn't have a lot of prior experience in. We had to learn a lot of things
*  as we were working on it to get that to work. That aspect is really exciting. We try not to
*  scale too fast from a kind of people perspective. We're still a fairly small company considering our
*  stage in the market. And that's very intentional. I think we try to be always smaller than we need
*  to be, essentially. And another aspect that I think is really important to scale effectively
*  for us has been that all leadership, all management is very technical. Getting the details with the
*  tools and models that we're building is the most important thing that can only be accomplished if
*  the leadership is hands-on and really is one of the people working on the technology.
*  Cool. One question I've been pondering as I've listened to this last exchange is,
*  you've given a few glimpses of your vision for the creative future in terms of in-record experiences.
*  Another big question that looms large over all this is, is this something that ultimately is a
*  total leveler or is it something that still is best wielded by the real pros? The reason I definitely
*  wanted to have Stephen here is that he has made films for years and has made all kinds of creative
*  stuff for years. Whereas I, in first grade, knew that I was not going to be an artist. That was the
*  first thing I knew I wouldn't be. And that difference is maybe, I would say the gap is
*  probably somewhat closed. In general, the research on who benefits from AI and how much seems to show
*  that the low skilled often can be brought up. The very skilled, at least when it comes to language
*  models, don't necessarily get too far ahead or the very best coders don't necessarily solve problems
*  they couldn't previously solve. Creative might be quite different. I mean, I can go in there and
*  make something and it can be cool. I'm still not on Stephen's level, but he is maybe on the level
*  of the Hollywood studio, which is another kind of leveling. So where does this all end up? Are we
*  headed for a world where anybody can conjure up their own feature films? Do we still have specialists?
*  If so, what is the nature of that specialization as the tools mature?
*  I want to take a starting point to something you mentioned of the pros not benefiting from
*  language models or cogen models. I think pros definitely benefit a lot from things like
*  Copilot or Carousel more recently, being able to give you context to know instructions, like
*  how to formulate kind of a project. And you can leverage those models to really expand
*  and speed up your workflow. Maybe you'll be able to implement it on your own and you wouldn't need
*  those models necessarily, but having those models speeds up the choices you can make.
*  I think it's the same with creative projects. Like taste and vision is as important with those
*  models as it is with more traditional filmmaking workflows. That's not going to go away. There's
*  always going to be people that create things on a different level of quality or vision than others.
*  It will help people who might not have prior experience express themselves through filmmaking
*  or making videos. I don't think that gap is going to necessarily close. I think what those tools
*  allow you to do is turn your ideas into a final output much quicker than before. They allow you
*  to make a larger amount of choices in a shorter period of time. The choices you make along the way
*  are really what defines the final output and the knowledge and the kind of insight to make those
*  choices really matters. We're seeing that some people invest a ton of time and effort into
*  becoming great at using those models and that effort pays off. In the kind of zoomed out strategic
*  analysis, it's take a lot of your comments boiled down to scale really matters. That seems pretty
*  clear. How do you compete long term with the trillion dollar companies that have billions
*  and billions to burn to scale up? Is there a time coming like the word from Anthropic, for example,
*  allegedly from their leaked memo was that they think in 25, 26, the leaders may get so far ahead
*  that nobody else can really catch up to them because they'll have the best models and the
*  best models will be useful to train the next models. They'll generate all the revenue.
*  From that position, will you have the chance to do the $10 billion training run and beyond?
*  Do you see similar dynamics happening in the creative gen space? If so, does that mean you're
*  just going to have to raise millions of dollars over the coming years or is there any other way
*  that you can see that playing out? I think you need to spend a larger amount of resources and
*  the barrier to entry becomes much higher very quickly. We need to keep up with and make sure
*  that we stay ahead and make the investments and compute in order to train those larger models.
*  At the same time, scale matters, but it also matters what kind of framework you're trying
*  to scale and what's the task that you're trying to teach them all to perform. I do think there is
*  maybe less focus on that as there should be. I see a lot of companies that are trying to
*  scale the exact same thing, which is a very specific paradigm in LLMs to really achieve
*  certain numbers in the same benchmarks. I think it's important to apply a lot of compute to train
*  models, but compute is not the only thing. It's really what are you training those models to do?
*  What are the tasks that you're focusing on? There is a lot more to do there that might give you
*  the right insights on that front and save you a lot more resources.
*  That's probably how I'm thinking about it. I don't think scaling is the thing that improves
*  models performance, but what you're improving the performance on really matters. That's something
*  we have some unique insights on and a unique perspective on that's not shared by the rest of
*  the industry. I heard something recently from a team member at one of the big three language
*  model companies that surprised me a bit. Basically, the person said, we expect divergence of models
*  over the next generation or two. I've had this kind of paranoia on the language model side,
*  especially with platonic representation. If there's generally this sort of convergence,
*  then we might end up in a very high stakes situation where one new model comes out. It's
*  essentially the same as the last one, but just a bit better. Everybody switches to it. It can
*  create a winner-take-all dynamic, and that could be potentially quite an unstable situation.
*  Then this person said, we think we're going to go in a certain direction, and the other guys are
*  going a little more this direction, and the other ones are going this other direction,
*  and these models will have different strengths, and people will probably use all of them. They'll
*  be more intentional about which model they use for which case. Is that basically the same sketch you
*  are outlining on the creative side? Do you think you'll be distinctive in what you offer? I wasn't
*  sure if it was that or if it was more just, we think we have insights that will save us on the
*  compute budget. I hope that's the case, that what you're saying is true, that there is going to be
*  more diversity of different models because I do think we're not collectively as a field exploring
*  all the different kinds of models that you can scale. I think we're focusing on a very narrow
*  set of tasks that we want them to get good at. Back to your question, I think it's a mix of both,
*  even at the same task. You can find some insights that will give you large algorithm improvements,
*  but it's more about what you want your final model to perform, what tasks you want to perform,
*  essentially. Being very specific on that really pays off, even at scale. How do you think about
*  the tension that exists between private company interests and novel architecture versus
*  disclosure at a paper level, just for the world at large, given that AI is such a big ball of
*  mystery to so many people? What is that like for you guys and how do you think about that?
*  Yeah, so I think it's important to publish findings and making sure that the collective
*  understanding of available techniques, there is not too much difference between the general
*  research knowledge versus the knowledge within individual companies. But there needs to be a
*  balance because of how quickly the field is moving, how competitive the competitive situation between
*  different companies. You can't necessarily publish every single aspect of what you're doing.
*  I think you need to, for strategic reasons, maintain some level of specific insights and
*  things that you found work really well for some period of time. There is a balance to be found
*  of what you can reveal publicly to help uplift the whole field and insights that help maintain
*  some company lead. So maybe there's a statute of limitations or something
*  similar to copyright on our AI future. I mean, knowledge gets diffused eventually. People move
*  between different companies. Not kind of things in sufficient time become kind of known. And I
*  would say for us, a big motivation and the focus of the team is building tools that empower artists
*  and creators. So that's ultimately how a lot of folks on the team see us, where the biggest
*  satisfaction and reward comes from. It's been less of a focus of getting to things that might feel
*  might have novelty as published research versus things that deliver really great tools.
*  I want to ask one very specific, somewhat selfish question, but I do think it is something that a
*  lot of people are probably wondering. And that is, when do we get an API? How do we integrate this
*  into our apps? Waymark specifically, because we serve small businesses, image to video is
*  the number one use case. Every generative tool we've tried for small business, we're always like,
*  even if it looks sweet, they don't feel like it's going to represent them in a way where when
*  customers come to the business, they're going to feel like this was the business they saw on TV.
*  So image to video is the specific subtask that we are most interested in. There's probably also
*  a lot of appetite out there for vertical because so many of the images that we take are and so much
*  of the video we watch is vertical. So give us a quick rundown of that and specifically, how do we
*  get off the API wait list? So we have done some initial work on the API side. We have a few
*  customers that are using our API. Canva is maybe the one we've announced, but there is more in
*  that pipeline. I think our main consideration is getting it right. We want to make sure that we
*  have that API available in a form that makes sense for folks to integrate with. But it's something
*  that it's in the near future and we want to make it more broadly available. I think we can build
*  all the possible tools around those models. You might have specific use case that makes sense for
*  your users. We want to give access to those models in other ways and that's something we're
*  actively working on. All right. Expect a follow up by email from me on that. Time is short. If you
*  have any comments on image to video, I feel like that has proven hard for almost everyone.
*  I'm curious if you have any insight into why. In general, when I do a text prompt, I feel like the
*  coherence and overall quality is typically better, not just on Runway Build. Pretty much all of the
*  products that offer either text to video or image to video, I feel like I get a video that as a
*  standalone asset is more coherent overall better when I do the text prompt versus when I do an
*  image prompt. Interesting. Yeah. We've seen different folks buy more value in one or the other.
*  I think image to video in some cases is a much easier task and in some cases a much more difficult
*  task. It's an easier task in that the model doesn't have to imagine the semantics of the scene,
*  like the overall composition, and you can just focus on the motion. It's a more difficult task
*  because it needs to respond to a wide range of possible inputs that it might not natively perform
*  well with. That's the reason why in some cases I think it can perform better depending on use case
*  from text to video. In some cases, it might not generate as coherent motion and so forth.
*  Cool. Any final thoughts? No. Really great discussion. I think I really enjoyed both
*  sections of the conversation. Cool. Well, we appreciate you taking the time to do it.
*  Fascinating perspective from you and really got a lot from it. For now, I will say Anastasios
*  Germanidis, CTO of Runway ML, thank you for being part of the cognitive revolution.
*  Thank you. It is both energizing and enlightening to hear why people listen and learn what they
*  value about the show. Please don't hesitate to reach out via email at tcr at turpentine.co
*  or you can DM me on the social media platform of your choice.
