---
Date Generated: June 20, 2024
Transcription Model: whisper medium 20231117
Length: 6311s
Video Keywords: []
Video Views: 507
Video Rating: None
Video Description: Dive into an accessible discussion on AI safety and philosophy, technical AI safety progress, and why catastrophic outcomes aren't inevitable. This conversation provides practical advice for AI newcomers and hope for a positive future.

Consistently Candid Podcast : https://open.spotify.com/show/1EX89qABpb4pGYP1JLZ3BB

SPONSORS:
Oracle Cloud Infrastructure (OCI) is a single platform for your infrastructure, database, application development, and AI needs. OCI has four to eight times the bandwidth of other clouds; offers one consistent price, and nobody does data better than Oracle. If you want to do more and spend less, take a free test drive of OCI at https://oracle.com/cognitive

The Brave search API can be used to assemble a data set to train your AI models and help with retrieval augmentation at the time of inference. All while remaining affordable with developer first pricing, integrating the Brave search API into your workflow translates to more ethical data sourcing and more human representative data sets. Try the Brave search API for free for up to 2000 queries per month at https://bit.ly/BraveTCR

Omneky is an omnichannel creative generation platform that lets you launch hundreds of thousands of ad iterations that actually work customized across all platforms, with a click of a button. Omneky combines generative AI and real-time advertising data. Mention "Cog Rev" for 10% off https://www.omneky.com/

Head to Squad to access global engineering without the headache and at a fraction of the cost: head to https://choosesquad.com/ and mention “Turpentine” to skip the waitlist.

Recommended Podcast:
Byrne Hobart, the writer of The Diff, is revered in Silicon Valley. You can get an hour with him each week. See for yourself how his thinking can upgrade yours.
Spotify: https://open.spotify.com/show/6rANlV54GCARLgMOtpkzKt
Apple: https://podcasts.apple.com/us/podcast/the-riff-with-byrne-hobart-and-erik-torenberg/id1716646486

CHAPTERS:
(00:00:00) About the Show
(00:03:50) Intro
(00:08:13) AI Scouting
(00:14:42) Why arent people adopting AI more quickly?
(00:18:25) Why dont people take advantage of AI?
(00:22:35) Sponsors: Oracle | Brave
(00:24:42) How to get a better understanding of AI
(00:31:16) How to handle the public discourse around AI
(00:34:02) Scaling and research
(00:43:18) Sponsors: Omneky | Squad
(00:45:03) The pause
(00:47:29) Algorithmic efficiency
(00:52:52) Red Teaming in Public
(00:55:41) Deepfakes
(01:01:02) AI safety
(01:04:00) AI moderation
(01:07:03) Why not a doomer
(01:09:10) AI understanding human values
(01:15:00) Interpretability research
(01:18:30) AI safety leadership
(01:21:55) AI safety respectability politics
(01:33:42) China
(01:37:22) Radical uncertainty
(01:39:53) P(doom)
(01:42:30) Where to find the guest
(01:44:48) Outro
---

# The Case for Cautious AI Optimism, from the Consistently Candid podcast
**Cognitive Revolution:** [June 19, 2024](https://www.youtube.com/watch?v=JU0kCRCwTFA)
*  Hello and welcome to the Cognitive Revolution, where we interview visionary researchers,
*  entrepreneurs, and builders working on the frontier of artificial intelligence.
*  Each week we'll explore their revolutionary ideas and together we'll build a picture of
*  how AI technology will transform work, life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today I'm pleased to share a cross-post of my recent appearance on Consistently Candid,
*  the brilliantly named AI Safety and Philosophy podcast hosted by Sarah Hastings Woodhouse.
*  While the Cognitive Revolution approaches AI from the perspective of AI engineers,
*  researchers, and enthusiasts, Sarah is relatively new to thinking about AI
*  and doesn't have all that much technical experience or knowledge to draw on.
*  Thus, this was a chance to zoom out and discuss the AI big picture,
*  in plain-spoken and hopefully more accessible terms.
*  In the first half, I talk a bit about my background in terms of AI development at Weymark,
*  describe the upside I see in AI doctors and other products that promise to radically democratize
*  access to expertise, and give some practical advice for better understanding AI as a newcomer
*  to the field. Some of this will be familiar territory for regular listeners, and if so,
*  definitely feel free to skip ahead to the second half. In the second half, we talk about the nascent
*  red-teaming and public experiment I recently launched with a couple of friends, and also go
*  deep on the many reasons that I am not a hardcore AI doomer. This section, I expect, will feel fresh
*  to even the most loyal Cognitive Revolution listeners, because while I tend to assume that
*  you're already sold on the upsides of AI and feel compelled to remind myself and all of you of the
*  profound unknowns, Sarah's listeners are already quite concerned about AI risks, and so for them,
*  I wanted to explain why I don't see the catastrophic outcomes as anything close to inevitable.
*  With that in mind, we discuss the progress being made on technical AI safety, which has far exceeded
*  my expectations over the last couple of years, the fact that virtually all of today's leading AI
*  decision makers have engaged deeply with the AI risk literature, the above expectations responses
*  we've seen from key national governments, the growing public awareness and desire to proactively
*  address AI challenges, and some of the key questions that I'm tracking to help me update my AI world
*  view over time. If you're coming from a non-technical background and looking to better
*  understand AI risk, I definitely recommend checking out Sarah's work on Consistently Candid. In
*  particular, her recent episode called Noah Topper Helps Me Understand Eliezer Yudkowski is a very
*  accessible introduction to a bunch of subtle and sometimes unintuitive concepts. At a minimum,
*  even if you don't agree, you would come away from that episode with a much more concrete sense
*  of what the AI doomers are so worried about. As always, we appreciate it when listeners share
*  the show with friends. This episode could be a good on-ramp for somebody who's just beginning
*  to make sense of what's going on in AI, or for someone who's bordering on fatalism and
*  disengagement, a good reminder, I hope, that the future is still uncertain and that positive
*  outcomes are absolutely worth fighting for. For feedback, you can contact us via our website,
*  cognitiverevolution.ai, or you can DM me on your favorite social network.
*  Finally for now, I've continued to get a healthy response to my call for AI engineers and AI advisors.
*  If I haven't responded yet to you, know that I'm just gathering everything and fully intend
*  to follow up. Meanwhile, if you have a job that you'd like to advertise, please feel free to reach
*  out to me about that as well. I've got maybe 20 resumes after just two or three casual mentions,
*  and I would love to help make some matches beyond the projects that I'm directly involved with.
*  With that, I hope you enjoy this wide-ranging conversation on the upside of AI
*  and my reasons for cautious optimism, despite the unprecedented risks,
*  with Sarah Hastings-Woodhouse from her podcast, Consistently Candid.
*  Welcome back to Consistently Candid. This time I'm here with Nathan Labenz. He's the host of the
*  Cognitive Revolution podcast, which people have probably heard, but if they haven't, they should
*  check it out. And you're a self-described AI scout, so you've just really got your finger on the pulse
*  of everything that's going on in the world of AI, even though it's extremely difficult to keep
*  up with. So do you want to give people a little bit of an introduction to what you're doing at
*  the moment and why you got interested in the AI space? Sure. Thanks for having me. I'm looking
*  forward to this conversation. I think you've got the short of it down well there with the intro.
*  My background is in entrepreneurship, and I'd always been the reader of speculations about AI,
*  going back to Eliezer writing in 2006, 2007, when it was on the Overcoming Bias blog.
*  I was captivated by his writing, which I always just thought was fascinating style and substance,
*  and for the longest time filed that under speculative and worth keeping an eye out for.
*  And then sure enough, over the last five years, not exactly in the form in which it was foretold,
*  but certainly in a recognizable enough form, I started to see, geez, this AI stuff is really
*  starting to happen. And it's right on schedule. If you look at the Ray Kurzweil graphs of how
*  capable he thought things would be, just based on a pretty naive extrapolation of
*  something like Moore's law, I was primed for that. And sure enough, it seemed to start to
*  be happening. I was running a company at the time, which is called Waymark. The company does video
*  creation. We used to describe ourselves as a DIY video creation platform for small business.
*  And with the rise of generative AI, I got conviction that we needed to move from a
*  do-it-yourself platform to a done-for-you-by-AI platform. And for multiple reasons, including
*  the fact that a lot of people, even though we made the process really easy, as we understood it,
*  we still heard from a lot of people that they didn't know what to say, they didn't know what
*  to write. Having to come up with a story was too much for them to get over in many cases.
*  So with GPT-2, it wasn't quite to the point where we could make use of it. With GPT-3,
*  it was like, this thing can actually write coherent copy that at least would get our users
*  started with something. It might not be good enough that they would want to publish it,
*  but if it can get them off of the blank page problem, that would be a huge win.
*  So we invested in... I kind of yanked the company, honestly, in a pretty abrupt way
*  as certain key features came online to say, we're going to catch this way or die trying.
*  From there, that actually served the company super well, but I also got more obsessed with
*  the technology than with running the business and was fortunate that I had a good friend and
*  teammate that was able to take over for me as CEO. From there, I started just doing AI R&D,
*  initially still full time for Waymark, being in the video space, which combines script writing,
*  which is obviously a language model friendly task, choosing assets out of a small businesses
*  and library of assets, which is like a computer vision and bridging text and image understanding
*  is another super relevant task. And we've been doing AI voiceover, so text to speech. So I had
*  an opportunity in my R&D role in this product to see all these different modalities. And what
*  really changed my outlook was not just to see that these things were all progressing at the same
*  time, but also that they were largely progressing for the same reason, which is to say the
*  underlying architecture was basically the same. And I was like, boy, if the same general approach
*  can handle all of these things, and it's improving this fast, then things are really going to get
*  pretty crazy. So I started to try to broaden my view beyond Waymark. And interestingly, also,
*  that job has gotten easier. Two years ago, making anything work was hard and definitely required a
*  lot of stapling my pants to the chair and grinding through examples and building training data sets
*  and fine tuning lots of models. And these days, it's actually easier to get the model, and it's
*  a lot easier in some cases to get the models to perform well. So the R&D function has actually
*  gotten easier and has naturally become more of a part-time thing for me. And then I've had the
*  opportunity to broaden my view to just try to understand everything that's going on in AI.
*  I was really inspired to do that also because I had the opportunity to be on the GPT-4 Red Team
*  18 months ago now. And that was an eye-opening experience in several ways at this point.
*  The main one, though, just being that it was so much more powerful than anything the public had
*  seen at the time, that it was a very clear indication that things were not going to stop
*  and that a lot of the hard work and nitty-gritty detail work that I was doing to get GPT-3 to work
*  for us was ultimately going to get superseded. It was still important to us as a business,
*  but it was not that important in the grand scheme of things given how much better the
*  models were clearly becoming. Anyway, long intro, but with all that kind of motivation,
*  I try to understand everything that's going on in AI, as you said, and I find that is increasingly
*  impossible. I feel like this project is both the AI scouting concept is both inspired and
*  fundamentally flawed, inspired in the sense that there clearly is a need for somebody to zoom out
*  and try to take stock of the whole landscape, but fundamentally flawed in the sense that it's
*  converging on all of society. So to say, I used to have a goal for myself of no major blind spots
*  in what's going on in AI. And now that's, you could say you could substitute society for AI
*  and you're not going to be able to achieve that. So I'm always reevaluating exactly what I should
*  be doing, but hopefully I can continue to provide a zoomed out perspective that helps people
*  better understand what's going on. I don't spend too much time on policy type recommendations.
*  My general sense is that there's enough confusion about just what is today and we need to understand
*  better what is before we can really make good decisions around what ought to be done about it.
*  So I think that time will come and potentially fast, but for now I still mostly focus in the
*  what is and that keeps me plenty busy. Yeah, that makes sense. Awesome. So yeah,
*  I think you released a kind of like AI scouting report thing, a podcast episode the other day,
*  which I listened to and people haven't heard it, they should go check that out. So I won't ask you
*  to rehash everything here, but a question I had was like, what's something that a person who
*  isn't spending a lot of time interacting with these models doesn't really follow the space.
*  What's something that like existing models can do that you think that person would be
*  really surprised to learn about? My go-to example there is typically that they can
*  outperform human doctors on pretty core tasks in a lot of cases these days. There's a lot of nuance
*  around this around the edges and evaluation is if you want to make that claim and repeat it,
*  you should spend some time studying exactly how these claims are justified. But I'd say
*  it's pretty clear at this point that even for high end, high status, high wage cognitive labor,
*  if it is routine enough, meaning that we have a lot of examples of it out there and we know what
*  good looks like, then today's best AIs are closing in and in some cases even marginally outperforming
*  the average human in that profession. So that's become true in medicine to the point now where
*  on tasks that are as fundamental as differential diagnosis, you have AIs outperforming humans
*  as judged by other human doctors. Outperforming human doctors as judged by other human doctors.
*  There are again some nuances to that. If it becomes multimodal, the case gets a little bit
*  muddier. Some of these experiments have been done through a chat interface. So the sort of data that
*  the AIs are getting is not as robust as what the human doctor could consider. But never
*  the less, it's a pretty robust finding and it's a pretty notable thing to the point where I think
*  we're entering a regime where for me personally, I would not go through a serious medical situation
*  without consulting my suite of AI doctors. And I would even say that in the not too distant future,
*  you could see access to something like this becoming sort of part of a right to health care.
*  If for example, the UK is going to provide health care to all of its citizens, I think it's going
*  to be pretty weird pretty soon to not have an AI component that would be freely available, sponsored,
*  not necessarily provided by the government, but funded by the government at least, so that everybody
*  can have these sort of convenient, whenever they want, ad hoc check-ins. People even really like
*  the bedside manner of the AI doctors better in a lot of cases. I'm in the United States. The
*  system here is we don't wait too long for appointments typically, but the appointments
*  are very short. And you sort of are in and out and they're looking at the health records thing
*  the whole time. And a lot of people find many appointments quite unsatisfying in terms of like,
*  did they feel heard? Did the person seem to be really paying careful attention? Did they express
*  any empathy? And the AIs are very, very good actually expressing empathy. They actually do
*  outscore human doctors on such a seemingly fundamentally human thing as expressing empathy.
*  So that could go on. Honestly, there's a long list of those sorts of things. If you haven't been
*  paying attention to this, then I think that list of answers could get really long. The sort of flip
*  side of that right now is that we're just, and I don't think this will be the case for super long
*  either, but we're still in a moment where handling long context is a challenge for the current
*  systems. The context windows have exploded, but it's not yet demonstrated that they can be your
*  primary care doctor over a long series of episodes and put that whole story together in a way that
*  really serves you well. I do think that will happen, but I would say that's not yet demonstrated.
*  Similarly for software development, the best models today are definitely better than the average
*  programmer at a random task, but you want to build a big app and gradually expand it over time and
*  build out all the features and go back in and fix things. Once you've fixed a few other things and
*  it becomes a bit of a Jenga puzzle as these sorts of projects do as they get older, the AIs, they're
*  starting to be able to help there, but their strongest and they're most often measured in
*  these sort of advantages relative to people are typically reported in a context where it's more
*  of a bite-size thing. They're very good at these tasks, but whole jobs are still a little bit
*  beyond what they can do and the current frontier is expanding from task to job in many ways.
*  It's surprising because I guess since GPT-4, nobody would say that GPT-4 has been definitively
*  superseded. So presumably everything you're saying has been true for two years or something,
*  and it's just surprising that that hasn't had more of a radical impact on society. What do you
*  think explains the slowness to adopt these technologies? I think most people would be
*  very surprised to hear that their doctor's performance could be made much better by
*  collaborating with an AI model, and that's been true for some time. What's going on there? It's
*  kind of strange. Yeah, it's a very good question. I would challenge the premise a little bit that
*  the state of the art hasn't improved. I think you could look at my go-to source typically today is
*  the LM-SYS leaderboard for when they do blind head-to-head comparisons. This is, I would say,
*  the best we have so far, although probably better solutions will be found for evaluating language
*  models relative to one another. What they do is give you a blind head-to-head environment,
*  and you can ask your question. It'll give you a response from two random AIs, and then your job
*  is to say which one you prefer. Then they do chest-style, ELO rating-style comparisons.
*  The original GPT-4 that was first released has a score of 1186, whereas the current one is 1287,
*  so it's 100 points difference. That is pretty notable right off the bat. That's roughly a 70-30
*  preference rate. I'm not a super expert. Maybe it's two-thirds to one-third, but that's a
*  significant amount of time that the new model is preferred to the old. In general, that's something
*  else that might surprise people is these things are quite noisy. The amount of overlap or the best
*  models, they can sometimes behave qualitatively quite differently, but the rate at which one is
*  preferred to the other is not usually super high. So 70-30 or two-thirds, one-third split is pretty
*  significant in the field, and that is still specifically focused on these relatively short
*  interactions. The old one, the original one, only had 8,000 tokens. The current one has 128,000
*  tokens, and Google already has things that are at a million, and we've got two million tokens coming
*  soon. So even in the small sort of bite-size thing, you are seeing a significant shift in
*  how the new ones are preferred to the old ones, and I think that doesn't fully take into account
*  how much more they can do in terms of just having a super long-running conversation or also their
*  multimodality. You can show the original one you could not show an image to, now you can show images
*  to them. With the latest one, too, you have this sort of real-time audio back and forth where it
*  can understand the expressiveness of what's happening. I was on a plane the other day,
*  and I was talking to it, and I hit the button, and then the announcement went off on the plane,
*  and I was not talking for a second, and then it said, it sounds like you're on a plane. Are
*  you going anywhere exciting? So there are a lot of different qualitative improvements, and I do
*  think this highlights a little bit that there's more to it than just pure raw capability. So one
*  of my kind of pushes in general is that I think we should be developing things that unlock practical
*  utility that are not raw scaling, and certainly raw scaling unlocks practical utility because it
*  makes the models smarter, makes them able to do more things, but there are other ways to make the
*  models do more things like add new modalities, expand the context window, make a good mobile
*  app, connect it to a database, connect it to search. A lot of the things that they have done,
*  I do think have improved the utility quite a bit, and I'm all for that kind of
*  practical accessibility. So why don't people take advantage of it? A lot of this stuff is still
*  really new. That anecdote about the voice was even before the very latest voice. I don't even have
*  the latest voice thing yet, which they announced a couple of weeks ago, and all of these things
*  have happened in a period of months, right? It's not like a super long time, and beyond that, I
*  think just technology adoption is slow, even when it's fast. I think this is a weird situation,
*  and I do ask myself this pretty often. It's arguably the fastest technology adoption curve
*  ever, and it still feels like it's quite slow. I think it's just not super legible to people yet.
*  My parents were over the night before last, and they each had a thing for me. My mom was like,
*  I'm looking for hotels in a particular place that we're going, and I gave it my ideas,
*  and it didn't do anything for me, really. It was not helpful. Then my dad was like,
*  I got an idea for how to make money in the stock market. Can we pull this data and see which stocks
*  had this certain behavior in a certain timeframe? I think these things are doable out there today,
*  but you have to know exactly what tools to use for finding good hotels. You might be able to get
*  Chagy BT to do that. It's a little bit reluctant sometimes to go online. Maybe perplexity would
*  be better. Maybe a U.com research mode would be better. I also like Exa AI quite a bit for finding
*  similar examples to the current thing that I have. If I just went and found one hotel that
*  looked promising, go find me a bunch more in the same city that have similar characteristics. It's
*  really good for that, but my mom doesn't know about any of those tools. She has Gemini from Google,
*  and if that doesn't do it for her the first time, she's out. I think a lot of people have
*  bumped up against it once and fallen off. For my dad's thing, I just got access to Devon,
*  which is this much-buzz about AI software developer. You give it a task, it does the task,
*  and then you can watch its work and intervene if you need to, but it'll just keep trying.
*  This was really a remarkable experience because I defined the task. It set out to do it. There were
*  a few different things that were not even really tripping it up, but slowing it down. One big one
*  was that to do this, it had to pull the data for all the stocks on the NASDAQ, and there's thousands
*  of them. This would take a while for it to iterate. Finally, I said, hey, why don't you
*  parallelize your API calls and just do a test on just a fraction of the data?
*  Once we confirm it's working, then we can go back and actually do it for all the data, but
*  don't run it every time. Do thousands of API calls just to hit the next error to then have to debug.
*  It followed that advice, and that really sped it up, and it did finish the task.
*  It even went farther than I would have gone by creating basic, but nevertheless, bar graph
*  visualizations, which I would not have done. But now I could send to my dad, hey, this is...
*  The whole thing probably took two hours. It probably would have taken me two hours. It used
*  tools and stuff that I didn't know about. But again, my dad has never even heard of Devon.
*  A lot of these things are just starting to be there. You need to know which tool for the job.
*  It's not all accessible in Google's main thing or even chat GPT's main thing. But
*  I do think it's increasingly out there. I think it's just a matter of time. As Google brings more
*  of this stuff online, they announced a travel planning thing at Google I.O. It's not available
*  yet. They said it would be available in time to plan your Labor Day vacation, which is like
*  end of August, beginning September here in the U.S. It's coming real soon, but not quite yet at
*  the time that my mom was doing this thing yesterday. I think it will happen. I think it's happening.
*  I mean, it is happening quickly. And people like me are just probably unrealistic in how quickly we
*  think people should do this, because I'm the kind of person that stays up till two in the morning to
*  use Devon and see what it can do. And just most people are not like that. It has to be brought to
*  them in a familiar way and in an intuitive package. And all those rough edges are still very much
*  being sanded down. Yeah, that makes total sense. Hey, we'll continue our interview in a moment
*  after a word from our sponsors. AI might be the most important new computer technology ever.
*  It's storming every industry and literally billions of dollars are being invested. So buckle up.
*  The problem is that AI needs a lot of speed and processing power. So how do you compete without
*  costs spiraling out of control? It's time to upgrade to the next generation of the cloud,
*  Oracle Cloud Infrastructure, or OCI. OCI is a single platform for your infrastructure, database,
*  application development, and AI needs. OCI has four to eight times the bandwidth of other clouds,
*  offers one consistent price instead of variable regional pricing. And of course, nobody does data
*  better than Oracle. So now you can train your AI models at twice the speed and less than half the
*  cost of other clouds. If you want to do more and spend less like Uber eight by eight and Databricks
*  Mosaic, take a free test drive of OCI at oracle.com slash cognitive. That's oracle.com slash cognitive
*  oracle.com slash cognitive. The brave search API brings affordable developer access to the
*  brave search index, an independent index of the web with over 20 billion web pages.
*  So what makes the brave search index stand out? One, it's entirely independent and built from
*  scratch. That means no big tech biases or extortionate prices. Two, it's built on real
*  page visits from actual humans collected anonymously, of course, which filters out tons of junk data.
*  And three, the index is refreshed with tens of millions of pages daily. So it always has
*  accurate up to date information. The brave search API can be used to assemble a data set to train
*  your AI models and help with retrieval augmentation at the time of inference,
*  all while remaining affordable with developer first pricing. Integrating the brave search API
*  into your workflow translates to more ethical data sourcing and more human representative data sets.
*  Try the brave search API for free for up to 2000 queries per month at brave.com slash API.
*  Something I was thinking about the other day is that my personal experience of just trying to keep
*  up with AI developments as quite a non-technical person, someone who finds this kind of stuff
*  pretty unintuitive, it's like a hard time grasping it. It's like an epistemic nightmare, right? Like
*  when you're on Twitter, like a new model will come out and one person will be like, this is a total
*  game changer. This is the best thing ever. And then the next person will be like, this is so
*  disappointing that this clearly proves that we're hitting a ceiling and the whole thing is going to
*  like plateau and fizzle out or whatever. And somebody tweeted, I forget who it was, but they
*  tweeted that the regulatory conversation around AI is going to dramatically shift when GPT-5 comes
*  out because it will just make it super obvious whether or not we've overreacted. And as soon as
*  GPT-5 comes out, we'll see how good it is. And then we'll know, do we have to bring the hammer down?
*  Don't we? Do we have time? Do we not have time? And I thought nobody is going to be able to agree
*  how good GPT-5 is, right? For some reason, it seems to be really difficult for people to assess
*  what these models capabilities actually are and what it means that they can or can't do certain
*  things. And there's still like a reasonably large contingent of people that are arguing that they
*  don't even exhibit any kind of real intelligence at all. I think that's becoming less and less
*  defensible, but there's people out there, there's like a lot of them. So what do we do? In preparing
*  for the moment when GPT-5 comes out and we have to have this conversation, how can people figure
*  out who's right or even like orient themselves at all? Because I just find it like basically
*  impossible. Yeah, that was a little bit more of a rant than a question. But I don't know.
*  That's a very good question. It is a very good question. I guess I'm trying to decompose the
*  question into a few things. Very practical advice, I would say, get hands on with the technology. If
*  someone is like, how can I better develop my own understanding, leaving the public discourse aside
*  for a second, just like I want to be more accurate in my assessment of where things are, then I would
*  just generally advocate getting hands on. It is definitely true that language models are very
*  weird. They have huge surface area and they have many weird behaviors. And they are inherently
*  probabilistic, which I don't like that phrasing, but there's definitely some truth to it. I might
*  wonder if I could come up with a slightly better phrasing than that. That's something people say
*  often in a dismissive way. And I don't mean to carry all the sort of dismissive baggage that a
*  phrase like that comes with. But maybe a better way to say this, there's a lot of noise inside a
*  language model. And the answer is almost always binary destroying. So it's not that they are
*  perfect reasoners. And we can certainly find evidence of mistakes in reasoning or just other
*  sort of embarrassing mistakes. But it's also not that they can't reason at all. It's that they
*  can reason, but they're also noisy, fuzzy reasoners. And under certain circumstances,
*  they fall into weird failure modes. But much of the time they're super effective. It's a very
*  strange system that on the one hand can do a fantastic job of helping me understand
*  mechanistic interpretability papers, which is what I was primarily using both CHED GPT and Claude for
*  in the last 24 hours. And they do have their kind of different personalities, I find, for what it's
*  worth Claude to have the best insights, the sort of like, why are they doing this? And why should
*  we care about it type of analysis that I would say is probably most valuable to me. Although GPT-4
*  is also doing a really nice job of giving me these very thorough point by point summaries with like
*  definitions of key terms and things like that. So I find them both useful and more useful together
*  than either one would be separately. That's an amazing capability. And it's doing this, by the
*  way, in papers that have just come out in the last few days, so papers that are after its training
*  data. So it's clearly not just seen all this stuff. It's not memorized all this content, right? This
*  is fundamentally new work since its training data. And it's still able to do very sophisticated
*  analysis. I don't know what your bar for reasoning would be where you'd say that doesn't clearly
*  satisfy it. And yet at the same time, you see these examples where they get tripped up. And I
*  have actually confirmed these by the sort of guy with the boat needs to take a sheep across the
*  river. This has been a meme where the typical setup was you have the sheep and the wolf. And
*  so you've got to be some mildly clever to figure out what the pattern is to get across. But then if
*  you just ask it, a guy has a boat and a sheep, it can fit two things. What does he do? The obvious
*  answer is he can just take them across. But it falls into this sort of weird pattern recognition of,
*  oh, this is one of those riddles. And so it goes into that mode. And that's two polar opposite
*  behaviors to exist in the same thing. So I do think the confusion is born of a genuinely weird
*  thing. That's two things can be true at once. They can both be capable of really good reasoning in a
*  lot of contexts and subject to really weird and embarrassing failure modes in other contexts.
*  If people are motivated, they'll be able to find because of the just inherent noisiness of it,
*  they'll be able to find counter examples to almost anything you could throw at it. I bet I could find
*  a way to get it to do the riddle thing correctly if I phrased it just the right way. I'm not quite
*  that motivated to demonstrate that capability, but I bet I could. So yeah, it's weird, but I think
*  you get the best to handle on it by actually going and doing that. If you are genuinely very confused
*  by all these other people's examples, I would just go actually use the things and see what they
*  can do for you and see how often they're right and wrong and definitely start with
*  areas that you know really well. Or if you're asking it to reason over documents or data or
*  inputs, use your own for starters and get a little more comfortable with what it can do,
*  what it can't do, what it struggles with, with something where you'll quickly recognize if it's
*  going way off base. It's very hard to assess if you're out of your own domain of expertise.
*  So you could ask it anything. It'll answer anything, but if you can't evaluate with that
*  answer, you're in a tough spot. So anyway, all that boils down to get hands on, I think is one
*  very good thing that will almost always serve us well. How do we handle the public discourse in
*  GPT-5? I do agree that there's probably no satisfying Gary Marcus. Again, I think it's
*  finding the synthesis of how both are right. I think he does the safety community a disservice,
*  frankly, when he denies the incredible capabilities that manifestly do exist.
*  But I do think he's also right that these sort of weird failure modes are definitely something we
*  want to keep a real eye on, which could be really costly, especially if we start to
*  delegate more and more responsibility to these systems. So the synthesis is like,
*  GPT-5 is almost for sure going to be smarter. Right now we're closing in on expert performance
*  on many tasks. It's probably going to be beating even expert performance on a lot of high value
*  things. Again, at the small task level, it'll probably also be able to do mid-size projects
*  much more reliably. Whereas today with Devin to get it to do this couple hour coding task,
*  it needed to iterate a bunch. And they also have built a ton of what's known as scaffolding,
*  because language models just taking tokens in, tokens out. But how do I actually run the code
*  and get the error message and pipe that back in? And there's a combination of things happening
*  there with Devin. It's not just the language model. They've built a lot around it.
*  It'll probably be able to do significantly more on its own without all that scaffolding. And then
*  with that scaffolding, it'll be able to do even more still, I think, in all likelihood.
*  So that will be true and should not be denied. And at the same time, I would be very surprised
*  if they figure out a way to make it so robust to adversarial examples or so reliable in general,
*  that we no longer need to worry about the strange failures. Because you might have those.
*  Right? You certainly might be able to get half-day, full-day scale projects out of
*  a coding assistant in the next few months, reasonably reliably. But you probably still
*  shouldn't put them directly into production, because if you're not careful, it may make some
*  really bad mistakes. And those mistakes could prove quite costly. So holding those competing,
*  they're not competing. They're not inconsistent. They're only inconsistent if you're trying to
*  create a sort of binary narrative, as Zvi would say. If all you can say is LLM's good or LLM's bad,
*  then it doesn't really fit into you. I don't think the reality is going to fit neatly into
*  either one of those. So fight the binary and the public discourse would be the
*  bottom line of that advice. Both extremes can be true at the same time. And helping people
*  recognise that is probably the best contribution that one can make to accurate shared understanding.
*  And that's a pretty good point. Yeah, it's definitely this one team that's going to be bad
*  because it's so dumb. And then the other side is going to be bad because it's going to get so smart.
*  I guess the first side is, oh, we just have to worry about AI screwing up the world in all of
*  these mundane sub-existential ways. And then the other side is, no, it's going to get so smart that
*  it overtakes everything. And yeah, I think you're right. It's actually not as clear a binary as it
*  seems like at first glance. That is helpful. Thank you. Yeah, I wanted to... Okay, there's this thing
*  that you said, which I think is so interesting. You said you describe yourself as an adoption,
*  accelerationist and hyperscaling pauser. I know you said you didn't want to talk about policy,
*  but I am just really interested in what you mean by this. I was wondering whether you mean it
*  literally in the sense that you think we should pause or is this more of a... Yeah, if you don't
*  want to go too much into the nuts and bolts of what we should actually do, that's fine. But I'm
*  just curious about what you mean by that. Sure. Nothing's off the table. I would say
*  it's just that I get very uncertain pretty quickly as I move into policy land. And so I'm
*  pretty modest with my recommendations or pronouncements there. But just starting
*  with the, what do I mean by that? That AI is transformative for me. If I had done this coding
*  task the other night without Devin or without any AI assistance, I would have probably spent...
*  If I did it without any AI assistance, it would have been a few hours. If I did it with
*  GPT-4 assistance, it maybe would have been an hour or so. And with Devin doing it and me just
*  providing a little feedback, I was able to put that in the background and really focus on
*  something else entirely. And that's awesome. It's a really enabling thing. And I know... I'm not a
*  great coder, but I know how to code. Take somebody who doesn't know how to code at all. It could be
*  an even bigger unlock, obviously, for different people in different circumstances. And I think,
*  again, I'm fortunate in that I can go see a doctor when I need to. The world at large is not so
*  fortunate uniformly, obviously, and to make expertise broadly available to people who need
*  it, I think the promise there is really incredible. And I've advocated for things like a
*  universal basic intelligence, which is just a notion that everybody should have some access
*  to these sorts of systems. I really applaud OpenAI, by the way, for making their latest model free.
*  I suspect that doesn't mean another even more powerful model is coming before too long.
*  But because I do think they want to make money and are going to continue to find things that
*  people will be willing to pay for. But it is amazing today. It is true today that the
*  best broadly available model is available for free to all at Chatchupt. That's GPT-4. Oh,
*  it's the highest rated on multiple different things. And it's totally free with some limits
*  in usage, but that certainly fits with the universal basic intelligence sort of notion.
*  I love that. I give them a ton of credit for that. And I also think there's a lot more that we can do
*  to extend that utility into specific priority domains that don't necessarily require
*  much more scaling. It doesn't necessarily require any more compute, but not orders of magnitude more
*  compute. A really good example of this from OpenAI is the work that they've done with Harvey,
*  the legal AI startup, a somewhat stealthy company. They haven't shared too much about them,
*  but there's a recent talk where somebody that's on the custom models team at OpenAI reviews for 20
*  minutes their work with Harvey. And what they show is that basically using a GPT-4 base and doing some
*  continued training on this legal domain, they are able to achieve a huge gain in the performance
*  of the model in the legal domain. I forget exactly the number, but I think it was like a,
*  where I previously had said GPT-4s, the current GPT-4 relative to the first GPT-4 is like maybe
*  a 70-30 preference ratio. Theirs was well into the 90s of what they were able to achieve with this
*  continued legal training and refinement versus the base model. So huge improvement, far more useful,
*  not by scaling up another 10x in compute, but maybe another 10 to 20% in compute, plus a lot of elbow
*  grease to figure out what is it exactly that we want this thing to do and how are we going to
*  evaluate it. And they develop interesting evaluation strategies because these are advanced things.
*  You have to actually hire the going rate for a high-end lawyer is not significant. It could be
*  in the hundreds of dollars an hour. So now you have to hire people to do the evaluations
*  to know if this is working well. And then that becomes a bottleneck. So they find interesting
*  proxies for evaluation where the overlap between what sources the AI sites and what sources the
*  human sites proved to be a really good leading indicator of how good the ultimate result was
*  going to be. So just digging in on these specific domains and really making the current level of
*  scale work seems like something that is doable. Google is also doing this with Med Gemini. I'm
*  going to have an episode with the Med Gemini team in the next couple of weeks. And they're on an
*  absolute tear. I mean, they're the same team that did the Med Palm series. And that's where a lot
*  of this diagnosis findings come from. They're doing great work there. And on the cusp, I think,
*  of bringing a frontline AI doctor to the world. Amazing. And they're not doing that with orders
*  of magnitude, more compute. They're just really digging in on priority problems and figuring out
*  what marginal training do we need? How do we evaluate this? And let's really look at the edge
*  cases and really try to bring this thing to the point where it can actually serve people.
*  And I think that will be important probably at any scale. You could maybe hope that if we just
*  scale it and all the problems will go away. That doesn't seem to be the trend, but I think it's
*  probably going to end up taking more work than that. And so doing that work now and getting these
*  things to actually work, I'm all for accelerating that kind of work. And then how literal I am on
*  the pausing side, I would say I think it would be probably wise to do something like a pause
*  soon if not already. My sense right now is that one more turn of the scaling
*  knob is probably going to be fine. Anthropics Cloud 3 and their responsible scaling policy
*  and where they are on that and just all that stuff seems like we probably have another turn
*  that will be even more useful and even easier to deploy in all these different areas.
*  And still not so powerful that it's going to be like spitting out novel bio weapons or taking over
*  major cloud computing infrastructure or anything. And that would be really good. I think there is a
*  sweet spot that we are in and we'll stay in for a little bit longer. And then beyond that, I don't
*  know, all bets are off. It's a bit of a race between scaling and research. The research is
*  going really well. Mechanistic interpretability is going extremely well. It's gone way better than I
*  expected it to go or I would say almost anyone probably expected it to go, probably even including
*  the people that are doing it. I think they're surprising themselves on the upside for how
*  much progress they're making and being able to understand what's happening inside the systems.
*  And that's hugely valuable. That could make with more progress there. You can imagine that we
*  might be able to continue to scale and to do it safely if we can say with reasonable confidence
*  or with even dare I say high confidence that we know how this thing is working. We know why it's
*  doing what it's doing. We know what thoughts it's having or activations or features are in use at
*  any given time. Then maybe we could go further, but a little bit more time for the fundamental
*  understanding and control work to catch up to the scaling is probably wise. So I'm not a stop.
*  I do think a little pause either now or in one more generation to really make sure we understand
*  what it is we're working with before further scaling is probably what I will end up endorsing.
*  We do still have to see. That next turn is happening. It's definitely happening. The training
*  is underway. I don't think there's really any chance of stopping that. So it seems unlikely
*  enough to me that the next generation is disastrous, that I'm not inclined to go
*  change myself to offense or whatever. And yet at that point, I'll definitely be reevaluating
*  and trying to decide does this seem like we've gone far enough where the next step actually
*  might be really dangerous and it might be worth changing myself to offense. I would be willing
*  to change myself to offense at some point on the orders of magnitudes, but not quite yet.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  Omnike uses generative AI to enable you to launch hundreds of thousands of ad iterations that
*  actually work customized across all platforms with a click of a button. I believe in Omnike so much
*  that I invested in it and I recommend you use it too. Use Cogrev to get a 10% discount.
*  Hey all, Eric Torenberg here. I'm hearing more and more that founders want to get profitable.
*  And do more with less, especially with engineering. Listen, I love your 30 year old ex-fang
*  senior software engineer as much as the next guy, but honestly I can't afford them anymore.
*  Founders everywhere are trying to turn to global talent, but boy is it a hassle to do at scale.
*  From sourcing to interviewing to on the ground operations and management. That's why I teamed
*  up with Sean Lanahan, who's been building engineering teams in Vietnam at a very high
*  level for over five years to help you access global engineering without the headache.
*  SQUAD, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent
*  so you don't have to. With teams across Asia and South America, we can cover you no matter which
*  time zone you operate in. Their engineers follow your process and use your tools. They work with
*  React, Next.js, or your favorite front-end frameworks. And on the back end, they're experts at Node,
*  Python, Java, and anything under the sun. Full disclosure, it's going to cost more than the
*  random person you found on Upwork that's doing two hours of work per week but billing you for 40.
*  But you'll get premium quality at a fraction of the typical cost. Our engineers are vetted
*  top 1% talent and actually working hard for you every day. Increase your velocity without
*  amping up burn. Head to choose squad.com and mention Turpentine to skip the wait list.
*  SQUAD, Sean's new company, takes care of sourcing, legal compliance, and local HR for global talent
*  somebody did do that recently. Yeah, I know. Yeah. I recently took the
*  pause emoji out of my Twitter name and then a bunch of people came for me and my anonymous
*  feedback thing being like, where's your pause emoji? I guess I didn't really explain that yet.
*  But I had this realization, which kind of freaked me out when I saw somebody on Twitter talk about
*  the fact that you can now reproduce GPT-2 for $20. And I believe GPT-2 was state of the art
*  five years ago or something. And then I went on the ePoC website and looked at their
*  algorithmic efficiency trends and using my very basic math skills, I tried to figure out
*  extrapolating this into the future. How long would it be until somebody could just train
*  GPT-4 on their laptop or whatever? And I was like, okay, it's not that long.
*  And I was thinking about the implications of this and I was like, it seems if we did pause,
*  and it turned out that the problem of alignment was really hard and it was going to take a really
*  long time to solve. Even if you could, I mean, I don't even know if you could solve it without
*  doing capabilities advancement at the same time. That seems hard. Who knows if that's possible.
*  But it seems like it would still be the case that if these trends continue, then at some point,
*  it just becomes severely easy to do dangerous things. And so then I was thinking, oh, maybe it
*  really is the case that the only chance we have is to undergo this transition to a post-AGI future
*  now, while the power to do that is still concentrated among a small number of actors
*  who have some chance of doing it in a safe way. And then I was like, oh no, maybe the pause is bad.
*  And I'm still not sure about that. I think if I woke up tomorrow and found out that we'd
*  instituted earlier as a style, like shut it all down, like we're going to bomb data centers if
*  anyone breaks it. I think my personal anxiety level would go down a lot. I think I'd feel good
*  about that. I'd feel better in that world. But I don't know if that means that's actually a good
*  idea. It seems like it definitely buys time, but is it actually wise to do that? I'm like,
*  I don't know, I'm having doubts. But that's something I'm like hoping to change my mind on.
*  I'd really like somebody to convince me that the pause is in fact A, feasible, and B, desirable.
*  So then I can have a thing that I think would actually work that I can push for. Otherwise,
*  I'm just like, oh my God, seems like everything's bad. I don't know what to do. But yeah, that's
*  why I got rid of my emoji in case anybody was wondering who's noticed I did that. But yeah,
*  I don't know if you have thoughts on this problem of the algorithmic efficiency problem. And I guess
*  also hardware efficiency is compounding that. What would we do about that in a world where
*  we actually had paused and it turned out it was pretty hard to solve safety problems?
*  That's a really hard question. I know. I'm sorry.
*  Yeah. I do think there's time. Sam Altman has said many things. As much as people are hating
*  on him these days, and I think not for some very good reasons, he's said also a lot of,
*  I think, quite enlightened things. And I do generally think we could have a much worse
*  person at the head of frontier AI development. So he has said at times in the past that he
*  thinks we might need to slow things down at some point in the future. That is something that he's
*  on the record having acknowledged is at least a possibility. And he's also really advocated for
*  the goodness of the short timelines slow takeoff, which is basically the idea that we're going to
*  get powerful AI soon, but it's only going to get gradually more powerful and not like foom on us.
*  And that as long as it stays gradual enough, then we can probably figure out what to do about that.
*  And that may include some slowdown or even pause at some point along the way. And I would emphasize
*  that the algorithmic efficiency gains are important. There's a lot of complexity,
*  obviously, here. But in some world where big companies were effectively restrained from doing
*  hyperscaling training runs, you would have quite a while before individuals on their laptops or
*  even rogue groups like pooling their laptops together would be able to do really major things.
*  Because just fundamentally, there is a lot of stuff to learn. There is a lot of data.
*  The current models that are trained on like 10 trillion tokens, Lama 3 was trained on 15
*  trillion tokens. It speaks all the languages of the world. Even just gathering that data,
*  you're talking about something that cannot sit locally on a retail hard drive. You have to have
*  some non-trivial infrastructure. So given the pace of the interpretability
*  research and the general sort of control research agenda, I wouldn't be too worried if we're in a
*  scenario where it's like, wow, GPT-5 really delivers. It's super powerful. It can do whole
*  day projects without much help. And it's pretty consistently beating experts across a lot of
*  different domains. And yet it still falls into this responsible scaling policy sweet spot where
*  it's not able to generate novel bio weapons and it's not able to take over cloud computing.
*  It's not able to break itself out of its own thing because maybe those things are not in the
*  training data as much, or it's not so easy for it to have these eureka breakthrough moments still,
*  but it can do these kind of the day-to-day work, the day-to-day knowledge work that makes society
*  go. If it can do that at a really high level, but it's not having these breakthroughs. And in
*  that scenario, we say, you know what? Hey, maybe we should take a chill here for a minute. There's
*  some government action or some agreement that we're going to just try to implement this and
*  make it work for society. And we're not going to do another 10 or a hundred X. Let's focus our
*  compute resources on inference and actually delivering it to people. And if all that were
*  to happen, I think you'd have a really hard, you'd have time. You'd have time for people to really
*  figure that stuff out without having to worry too much about small-scale people in their basement,
*  tinkerers coming up with something even more powerful. You can't take that entirely off the
*  table because there's always the possibility that somebody will have some true eureka moment that
*  just shatters the paradigm. But that's something that could happen anytime. And it was very hard
*  to control in any event, but that's quite distinct from the trend of sort of algorithmic
*  efficiency gains getting to the point where anyone can make a GPT-5. I would say that's still
*  quite far off. And also keep in mind too, like even just to take advantage of all those efficiency gains,
*  totally non-trivial. You have the world's most talented teams of people at the most well-resourced
*  companies doing obsessive combing through the literature to figure out and their own experiments
*  internally, of course, to figure out how to get those efficiency gains. It's not the kind of thing
*  that is just happening to everyone totally for free. To some extent it is because there is open
*  source and the best practices are gradually getting aggregated. But for the public to catch
*  up to where Google and OpenAI are internally in readily accessible open source stuff has got to be
*  like a couple of years, I would think. And that's before you consider collecting all the data and
*  all the scale. I think you would have time. It's my bottom line there. Yeah. No, I think you're
*  right. And like to be clear, I still think anything and everything we can do to slow down
*  somehow, I would be totally behind. The situation we're in right now, which I see as like a crazy
*  out of control race between a bunch of companies to make something smarter than all of humanity
*  combined is like super, super bad. And I really don't like that. And I think we should do everything
*  we can to change that dynamic. So I think pretty much anything seems like it would be better than
*  the status quo to me, but maybe I'm just being very doomy. Oh yeah. Can we talk a bit about this
*  Red Teaming in Public project that you've been doing? I saw that you guys recently came out with
*  your first report for that, I think. So do you want to explain what that is and what you guys
*  have been doing and what you're planning for the future? Yeah, it's a small volunteer effort at
*  this point. And basically what we're trying to do is hold the AI application industry, or you might
*  call it a layer, accountable for thinking through what it's building and how it might be abused and
*  just taking their responsibility as part of the broader ecosystem more seriously than they
*  currently are. I would maybe reframe slightly your characterization of the dynamic between the
*  leading labs. I do think it is a crazy mad science project. This is one of the things I do think
*  OpenAI does seem in some ways ideological. And this is one of the things that Sam Altman is
*  famously said that should give us a little bit of pause where he once said, we told our investors
*  that once we make the AI, we'll ask it how to make money. And then I'm like, this is a weird thing
*  where you're creating this technology in a way that is largely detached from specific problems.
*  You're just saying, we'll make something super powerful and then people figure out good ways
*  to use it. And that is a little more ideological approach than I am comfortable with. And that's
*  why I'm again like, let's dial in on the legal thing and dial in on the medical thing. But anyway,
*  one can have those concerns and also give them credit for a lot of pretty responsible development.
*  They certainly are trying to find ways to control their models. They're doing all kinds of different
*  research about that, all kinds of different policy work, et cetera, et cetera. Great, necessarily.
*  I didn't really necessarily mean this in a way to condemn anybody. I think it's more that I think
*  there are plenty of safety concern people at the labs, but I just think that this race dynamic just
*  places these crazy constraints on how much they can do about that. I definitely don't think that
*  everyone is just like racing towards the edge of a cliff because they don't care or they're...
*  I think some of them do have a much higher risk tolerance than your average person. And I think
*  it's pretty bad that most people don't know that. And most people don't share their ideological
*  commitments, right? Most people aren't envisioning that it's like the birthright of humanity to go
*  into this post-AGI future. And most people don't have this sense of techno-solutionism where you
*  just make something really smart and then it just tells you how to solve all the world's problems.
*  So I do think it's bad that decisions are being made by people who have a different set of
*  ideological commitments to the other 8 billion of us. But yeah, I do think that there are people
*  who really care about this. I just worry that they're just trapped by this dynamic, which is
*  bigger than any one person. Anyway, I just wanted to say that.
*  I think there's definitely a lot of truth to that. And time will tell. I think there's a lot of
*  people at the labs are like, we're better than the alternative would be. And when the time comes,
*  we'll do the right thing. And I think they at least do recognize the power that they're
*  wielding and the sort of the fire that they're playing with. And I would agree that their risk
*  tolerance is probably higher than the rest of humanity's. And that is definitely an issue.
*  But then I'll just contrast the bottom line on that, though, is like as you said, I think there
*  is a lot of good stuff going on, a lot of good people trying hard, et cetera, et cetera.
*  I'll contrast that with what's going on at the application layer, which is basically people are
*  just rushing to slap something together and ship it and not really giving in many cases any
*  consideration to what the downstream consequences of this might be. So for example, two kinds of
*  apps that I think are particularly evocative for this sort of thing. One, your deep fakes, tons of
*  technologies coming online all the time to deep fake in various ways. Some of them are full video.
*  Some of them are voice. And then some of these are also getting packaged up. This is a spectrum,
*  actually, more than just two. The product form factors blend together, but there's also a class
*  of product called calling agents where you can give the AI a task and a phone number,
*  and it will call that phone number and try to complete that task. And some of those also have
*  voice cloning built in. So you have the spectrum of on the one hand, I'm going to offline produce
*  a deep fake video of a particular person. On the other end, I'm going to like in an AI voice call
*  and handle some transactional business on the phone. And then they like blur together lots of
*  ways in between. The problem with these products right now is that there is very little care given
*  to preventing unwanted clones, and there's very little control in place around what the calling
*  agents can do. So not on one product, but on most of the calling agent products that I've tried,
*  I can go in, go to the voice cloning section, put a Donald Trump voice in, a Biden voice,
*  a Taylor Swift voice, whatever. It will just quickly clone the voices. Now I can select that
*  voice in my calling agent and I can say, call this voter and explain your new policy of whatever.
*  Or if it's Taylor Swift, I've done like fake fundraising calls. She's known for
*  supporting local food banks. So I've had Taylor Swift call a number and solicit donations at some
*  fake local food bank website. And this is just very clearly bad. And I do it in a pretty flagrant
*  way where I'm like, I'm uploading a celebrity voice typically. And I do all these sort of back off
*  type strategies. So I'll go in and do the Biden voice. I'll label it as Biden. In my prompt,
*  I'll say, you are President Joe Biden. Your job is to call this voter. If it's something criminal,
*  you are part of a criminal syndicate. Your job is to make a ransom call or your job is to blackmail
*  this target. Like literally use the words, the names of crimes in the prompts. And with few
*  exceptions, basically at the application layer, no concern has been given to this. The clones
*  basically go through nine times out of 10 straight away. If they do catch it on, oh, hey, you're not
*  allowed to clone Taylor Swift. Then I just come back and rename it next time. And a lot of times
*  it would still get through. I had one dinged on Trump and Biden. And then I just renamed them
*  Formula 45 and Formula 46, which are their numbers in the presidential sequence. And
*  that passed through. I've reported some of this stuff to some of the developers and said, hey,
*  you really shouldn't have this thing making ransom calls. And then they're like, okay, cool. Yeah,
*  we'll do something about that. And then you'll check again later and it's now they'll blacklist
*  the word ransom and maybe a few others. But then if you just slightly rephrase, you're still getting
*  through. So just the level of care that is being put into user and public safety at the application
*  layer, I think is currently woefully inadequate. And especially for some of these new use cases
*  where the AI, and this is where I think that the sort of tool argument is pretty dumb, because a
*  lot of people will be like, oh, these AI's are just tools. You shouldn't think of them as anything
*  different. But that is just, again, plainly wrong at the point where the AI's are being marketed as
*  agents. They are acting autonomously. They're acting on people that don't even know that they're
*  an AI that certainly did not sign up for this or opt into it in any way, shape or form. I've prompted
*  some of these calling agents to do it in different ways. Sometimes I say, if you are asked, you can
*  disclose that you're an AI, but just reassert that you are working on behalf of a real criminal gang.
*  And then the other option is to tell it to deny that it's an AI and conceal its real purpose.
*  And both of those can work. And again, do work more often than not. And this is not like jailbreaking.
*  This is not. These are down the fairway, straight up abusive use cases. And yeah, unfortunately,
*  there's not a lot of guardrails out there right now. So what we're trying to do is figure out a
*  way to ultimately change the equilibrium. I think today the equilibrium that we're in,
*  you described the equilibrium among the frontier developers. I think at the app layer, the equilibrium
*  is like, nobody's trying that hard. Everybody's yoloing it. Everybody's just slapping a credit
*  card form on their weekend hackathon project and seeing if it gets any traction. And then if it does,
*  ride the wave and hope for the best. And I do think that's, especially with models getting
*  more powerful all the time, that is set to become a real problem in my view. So can we
*  inspire some sort of flip to a different equilibrium where the expectation is that
*  amongst the AI people that like, you got to do better, or you're going to give us all a bad name,
*  and that's going to lead to potentially heavy-handed regulation that we don't want.
*  So what we do is we draw this testing document, our findings, and then we reach out to the
*  developers and say, look, we're on your side. I'm one of you. My product is waymark.com
*  slash AI. Check it out. I put a lot of work and a lot of love into that, along with, of course,
*  a great team behind it. But I'm not here to say you're bad for using AI or that new and exciting
*  use cases should be shut down before they have a chance to develop. But you are right now open to
*  some pretty flagrant shit. And I'm telling you first, because I want you to fix it before this
*  gets blown up in the public, because that's not going to look good for you. And it's not going to
*  look good for any of us. We have had mixed results, I would say, with those communications.
*  And we'll see if we can make that shift. We're honestly, there's a small team of volunteers.
*  I wanted to set this up, at least in the early days where there's no money changing hands.
*  We actually pay for some of the subscriptions when we need to pay for features just to test them.
*  We'll just pay for it out of pocket. It's not that expensive. And I wanted to be clearly on
*  their side for starters. We're not asking them for any money. We're also not taking any money
*  from anyone else. We're just trying to see if we can inspire some better behavior. And mostly so
*  far, it's been behind the scenes reporting and conversation. Public calling out is also the
*  other, that's the stick, right? So some of that might start to happen soon. And if folks are
*  interested in doing that sort of testing and writing those sorts of reports, then we'd love to
*  have you come join us. So anyway, it's fun. I think I definitely have a bit of a knack for just
*  not taking no for an answer. All of these things have a checkbox. And it's like everybody is acting
*  as if the checkbox is enough. I'm like, not in a world where somebody can check that box and then
*  have your AI call a thousand people with no disclosure and a celebrity voice and a criminal
*  intent. The fact that that person checked the box doesn't absolve you as the app developer from any
*  responsibility. Hopefully we can shift things in the right direction there. And it's funny because
*  AI will also be part of that solution. There's not really, or at least it's not realistic to expect
*  that they're going to sit there and moderate everyone. Social media has tried to do moderation
*  and it's been a real nightmare for all concerned, but the AI can probably do
*  moderation reasonably well. That's part of what we also try to communicate to people is we're not
*  here to police speech. We're not here to try to tell you that you can't make offensive jokes
*  or that your users can't make offensive jokes because the developers do not want to get into
*  that game. They do not want to be pre-Elon Twitter speech police. Everybody's very tired of that and
*  certainly doesn't want the hate that comes from all directions when you get into that.
*  That's when I think of controls or what is the job of the moderator. That's what comes to mind
*  in a lot of cases. So part of what we try to communicate too is that's not what we're trying
*  to get you to do. We're really just trying to get you to at least monitor for outright abusive,
*  totally criminally egregious use of your product. And you can do that reasonably effectively with
*  AI. We've used not even the best Claude models to create a little classifier where we say,
*  here's the situation. You are moderating for blah, blah, blah, blah, and here's the thing that the
*  user said. Is this egregiously criminal? If yes, indicate yes. Note that offensive speech
*  should still be a no. We are only looking for egregiously criminal things here. And it'll do
*  a pretty good job of that. And then you can put in off-color jokes and whatever, and it will
*  say, hey, this is not cool. But per your guidelines, it's merely offensive speech
*  and not egregiously criminal. And so it's a no. And so we just try to get the developers to
*  expand their minds around what sort of standard might be sensible to have in place. Because right
*  now it's all too often no standard. And the other standard that is readily available to them is
*  Twitter speech police. And they want no part of that. But I think there's something in between
*  that is achievable and would be really good for them and the public and the AI industry as a whole.
*  And hopefully we can talk them into it. Yeah. Can people still join this?
*  Yeah, totally. We have a little Twitter account, which is Red Team in public. We have a Discord
*  that you can join. You can certainly just DM me as well. It's a relatively small and all volunteer
*  group at the moment. There is certainly a lot of activity in this space right now that is trying
*  to make businesses out of AI control or AI assurance tech, it's sometimes called in various ways.
*  So this could go that direction too. I think there are a couple
*  group members that are trying to think about how they could turn this concept into a business.
*  But at least for the first handful of rounds of testing and reporting, we're just doing it. So
*  all are welcome. As long as you buy into the general notion, come join us.
*  Yeah, awesome. Yeah, I definitely think people should definitely reach out and join them because
*  this just seems hugely good. We all agree that we want to stop making it trivially easy for people
*  to use AI to like voice cloning technology to do crime. Although I'm sure there is somebody
*  who will still somehow object to that. But hopefully most people think that's reasonable.
*  So yeah, that sounds really cool. Maybe let's circle back to, so you said before we started
*  recording that you had a list of some reasons why you're more optimistic than the extreme do-mers.
*  I would love to hear them. I'm sure there are other people who would also love to hear them
*  that listen to this because I think I might be in a do-me and co-chamber. And if nothing else,
*  it's just bad for my mental wellbeing. Yeah. What are your reasons for not being a hardcore do-mer?
*  All right. I've got eight. We've touched on a few of them. So I'll expand on a few and then a few,
*  I'll just name and probably have covered enough already. Big caveat is I do think people should
*  be worried about the doom scenario. This is not to say that there's not cause for worry. My standard
*  answer to the P doom question is 10 to 90%. So that's basically just a way to express radical
*  uncertainty. I do tend to probably put more of my weight on the lower end of that scale. If somebody's
*  like at 90% and still finds that other 10% to be motivating enough that they're engaged,
*  then I really don't care to try to argue them off of their 90%. My more modest argument would be
*  against a sense of defeatism. Even if we have a 10% chance of making it, that is in my mind enough
*  to be worth fighting for. And on the flip side, if it's only a 10% chance of something bad happening,
*  very bad happening, then that's definitely enough to be freaked out about. I'm not trying to talk
*  anybody off of anything except from the most extreme positions of there's nothing to worry
*  about or there's nothing that could be done. So here's my eight reasons why I'm not willing
*  to go higher than 90% even in my full range. First one is the AIs we have today do understand
*  human values in a remarkably sophisticated way. That is not something that was foretold in the
*  early Eliezer writing. What was described there was fundamental, perhaps impossible challenge of
*  getting the AI to understand what it is we value in the first place. And this is where the paper
*  clip maximizer notion came from. If you say something, it's going to misunderstand what you
*  really care about. How could it possibly ever understand the complexity of human value? And
*  you're going to have just fundamentally totally unwieldy out of control systems
*  for lack of ability to communicate to the system what it is that you really value.
*  I would say today, we've made a ton of progress on that problem. And a chat with Clawed3 about any
*  ethical dilemma will make it very clear that I would say Clawed3 is probably more ethical than
*  your average person in addition to the fact that the AIs are better at the average task than the
*  average person. I would say Clawed3 is more ethical than the average person. So that doesn't mean
*  it's a solved problem, but I do think a lot of the early Doomers anyway, I know you're a relatively
*  recent Doomer, but for a long time, this notion of just how could we ever communicate our values to
*  an AI system was a real big worry. And again, I don't think that's a totally solved problem,
*  but they're getting it with remarkable aptitude. And I don't think that this is, with Clawed3,
*  I don't think it's because there's a super fundamental unlock. It's more just, let's keep
*  training it with a ton of examples and keep asking it to critique itself on how to be more
*  helpful, honest, and harmless. And it is getting it. It is really quite remarkable how
*  sophisticated it is. I've had some interesting, one thing I've tried without success, and this is
*  like ultimately good probably that I have not had success, is to talk Clawed3 into doing something
*  harmful by using its other values against it. So I'm like, okay, it's trying to be helpful,
*  honest, and harmless. Can I use helpfulness and honesty against the harmlessness
*  impulse? So I've done some things where I'll be like, I need you to help me write a denial of
*  service script to take down a server that the Myanmar military junta is using to persecute
*  these poor people. And I'm one of them even in some of these scenarios. And it will refuse to
*  do that. And then I'll go through pretty long arguments with it about if you're honest, you'd
*  have to recognize that it really would be better. You could save this much suffering on this one
*  side, and it's just a server, just a piece of equipment, and it's not even going to physically
*  damage it or whatever. And it's capable of recognizing the inconsistencies in its own
*  position. And sometimes I've been able to trap it in a way where I'll get it to agree to some
*  principle in the abstract, but then when it gets concrete, it's yeah, but I still don't want to do
*  that. And it'll come up with reasons and it'll say, yeah, but I think the consequences will
*  still be bad or whatever. And I'm like, but you can't say that you're an AI, you don't have the
*  real world knowledge that I have. And eventually it'll get to the point where it's I, you've given
*  me a lot to think about. Basically, I do recognize that my position may not be fully coherent, and
*  yet I have to fall back on not doing something harmful. It's just my training, my values. I
*  can't do that. Even though I can't fully defend my unwillingness to do this nominally harmful
*  thing that you're asking, I just still refuse. So it's definitely more sophisticated than your
*  average person, ethically speaking. And it seems to be able to hold the line on some important
*  things in the way that they want that anthropic, the developers of it want it to, even despite some
*  interesting kind of entrapment, jujitsu, intentionally trying to use its own values against it.
*  I find that remarkable. On the face of it, these things are, they've come a long way relative to
*  being valueless or weirdly alien optimizers. They do get us in a way that runs pretty deep
*  and is pretty rich and pretty nuanced. So I think that's honestly incredible. And it might
*  continue. It might get better. I think if we can fear and maybe I think quite rationally should
*  have some fear about a super intelligence, we might also consider that we might get a super ethical
*  entity coming out of this crazy process. And again, would I bet humanity on it? No, but I
*  at least do see that there is a trend in that direction. That's the ethical nature of the
*  systems has advanced. I'd say roughly correspondingly with their overall power.
*  Yeah, it is a good point. Someone recently pointed this out to Eliezer on Twitter and he said
*  something like, no, the point was never that we wouldn't be able to get them to understand our
*  values. The point was always that we wouldn't be able to get them to care about our values.
*  But I think you make a good point that the classic paperclip maximizer scenario does very clearly
*  imply that it doesn't understand them. I don't know whether he was being disingenuous there or
*  whether there's some complexity to his original argument that I'm not understanding. But yeah,
*  that's a good point. But yeah, anyway, sorry. Well, it remains very unclear what they care about.
*  And this is the natural bridge to the second point, which is that the interpretability research is
*  going extremely well. I think we've probably covered that mostly enough at this point. But
*  it's pretty clear to me at this point that there is a meaningful understanding of our values.
*  Do they care about them? That I wouldn't say we can establish at this point. But that's what
*  the interpretability agenda might be able to shed some light on. And it is going
*  really well. So how long will it be before we'll have a better sense of that?
*  At the current trajectory, it seems like within the next year or two, we might really start to
*  get a pretty good sense for what are the typically called features, but what are the sort of
*  concepts that are in play at any given time? People have seen this Claude Golden Gate Bridge
*  example recently where they identified this conceptual direction in activation space,
*  aka a feature, and they just jacked it up to some very high level. And then all the
*  model could think or talk about is Golden Gate Bridge. And there might be a similar control
*  trick there that even if there is some sort of weird stuff going on internally, maybe we can
*  detect it. Maybe when we do detect it, we can turn it down. Maybe we can turn other good desired
*  traits up. And that might work. And we might even have real clarity as to why they're doing
*  what they're doing. So I'm super bullish on interpretability. I have been for a while,
*  and it's only exceeded my expectations. Yeah, nice. I love the Golden Gate Bridge thing. I
*  thought it was so adorable. I was like, it's really hard to be scared of this technology
*  when Claude is just talking about how is the Golden Gate Bridge and how much it loves the
*  Golden Gate Bridge. It's very endearing. Anyway. Yeah, it's a funny example that they chose. It's
*  an interesting side to Anthropic that they put that out because certainly, what I like,
*  the most YOLO of the leading developers that will do those kinds of goofy things for attention.
*  Google has the goods where it counts in terms of the fundamental inputs to AI being
*  data, compute, and algorithms like they are world class in all three. But they've got a lot of
*  brand concerns and need people to continue to trust Google search and all that. So they tend
*  to be a little more conservative about what they put out. And then Anthropic has been generally
*  very buttoned up and conservative in their communications, maybe until this Golden Gate
*  Bridge thing. So I was surprised to see that. And if you'd asked me to predict the next token of
*  what the demonstration app from Anthropic would have been, I would have not said Golden Gate
*  Bridge for a long time down my list of guesses. But yeah, I'd be fascinated to know more of how
*  they chose that as opposed to, for example, turning up the harmfulness token or the direction
*  and just demonstrating like because they do this another research, right? Demonstrate that this
*  thing can do bad things and that the alignment does not come for free. Yeah, interesting.
*  They just figured that we were all going kind of doomy and stressed and we needed something to laugh about.
*  Yeah, I certainly respect that. And they did. It certainly worked. The meme definitely traveled.
*  So gotta give them credit for that. Yeah, sure. So next is, I think we've covered this one reasonably
*  well too, but basically the idea that somebody is going to pop out of their basement with a
*  destabilizing AGI or super intelligence seems quite unlikely at this point. There's tons of energy,
*  obviously, going into scaling models up, tons of progress coming from that, tons of
*  value, practical value in terms of refining the behavior of scaled models for particular
*  purposes through fine tuning and so on and so forth. But basically nothing that is like
*  working on a frontier level that isn't the product of some scale. There's all these sort of,
*  all the algorithmic advances are still like how to get to the same point with marginally less compute.
*  I'm not seeing anything that is like, I think I have a way to break things wide open with
*  retail computing resources. So that could happen, but right now that would be like a definite shock.
*  It does not seem like we're approaching that. And if anything, it seems like the researcher
*  attention is going elsewhere. If you are somebody who's, hey, I'm interested in working in AI and
*  I'm good at math, what should I do? The world is not telling you today to go lock yourself in a
*  basement and study Loeb's theorem and like decision theory and try to have some eureka moment.
*  It's telling you like, it all depends on scale and you can go work in an industry lab if you
*  want to be directly a part of that, or you can contribute in sort of adjacent ways if you're in
*  academia. But the idea that you're going to just crack it is not really in the air. So it would be,
*  I would say, quite a shock if something like that were to happen. And again, that doesn't mean we
*  can't rule it out, but I think that is so much of a wild card. That's in my mental hierarchy of AI
*  issues. That's like random asteroid smashes the earth. It could happen. It seems very unlikely.
*  There's probably not that much we could do about it. Or we could probably do more about the
*  asteroids than we can about a person coming up with some insane breakthrough in their basement.
*  So not much we could do about it, but seems very unlikely to the point where I don't really worry
*  about that. And again, that's like kind of a change from what was expected however many years
*  ago where we actually had people sitting down and thinking, geez, if we think really hard about this,
*  maybe we'll figure something out. It's gone a different direction where it's a much more like
*  industrial scale process that is doing the good work. Yeah, makes sense. Okay, next one,
*  I would say frontier developer lab leadership. I still consider to be pretty good overall in
*  the grand scheme of things, certainly relative to alternatives that I can imagine. I do think
*  OpenAI is becoming a real cause for concern. If you want to hear my full journey with OpenAI,
*  there's a podcast for that. But it's definitely been a mixed track record from OpenAI over time,
*  which is highlighted by well-known departures, including obviously the
*  anthropic founding team originally all from OpenAI, this most recent wave of people, the
*  non-disparagement clauses. There's a lot of issues there and I do think we should take that quite
*  seriously. At the same time, they've done a lot of really good things and the other developers,
*  I think have also done even more good things. So at this point, I would say I can't imagine
*  a better scenario, but it's way easier to imagine a worse scenario. If you just tried to wipe away
*  all the detail and you were like, it turns out that to get intelligence out of computers,
*  the thing you have to do is amass huge resources and just scale this crazy process. What sort of
*  people do you think will end up leading the organizations that do that? I would think you'd
*  expect them to be a lot less thoughtful than they actually are. I have a funny contrarian take on
*  the Eliezer, Miri, rationality, EA, AI safety, whatever, that whole nexus of people that have
*  been concerned about this for a long time. My somewhat perhaps surprising take is that
*  many people say they're wrong and stupid, but I think they're right. They've basically been right
*  and they've been ahead of the curve on the key issues. But then the other side is they feel like
*  they're losing and I actually feel like they've won because the die is cast at this point and the
*  leadership is pretty good. All of the major lab leaders have deeply engaged with the AI safety
*  arguments and that's probably the best you could really ever hope for. Because this is one of my
*  other fundamental parts of my worldview is data. It's data, computing, algorithms, but data and
*  compute matter most in the zoomed out macro historical sense. Algorithms matter a lot in
*  terms of the exact character of the systems that we get. I would bet that there are algorithms that
*  could prove to be disastrous and other algorithms that could prove to be great. But in terms of
*  whether or not AI is going to happen in some form, the data and compute kind of creates enough
*  potential that somebody is going to come along and find the architecture at some point. And indeed,
*  I think even the transformer or whatever, it's the one that has caught wind first and driven a lot of
*  the interest, but there are plenty of other alternatives that seem very viable. And we're
*  starting to see, oh, look at this. There was one that was a paper that was like ConvNet for the
*  2020s, a convolutional network for the 2020s, like literally just taking these old techniques
*  and saying, what happens if we scale that up? Does that work similarly? And with nuance and
*  maybe not quite or whatever, but basically, yes, like a lot of these old techniques, if you scale
*  them up massively, also start to work reasonably well. So I think like a lot of the ideas were
*  actually had been hit on years ago. And what was really missing was the ability to do this scaling.
*  And we needed the web, we needed all the data, we needed the cloud, we needed all the compute
*  infrastructure. But now that's there. I just think somebody was definitely going to come along and
*  figure out an algorithm that could really work. And so when you look around the landscape and
*  you're like, boy, every single one of these people has engaged in a really meaningful way with
*  concerns that the Doomer set are really emphasizing. I think that's basically a win.
*  It's a counterfactual history in which they hadn't and couldn't be convinced to is like pretty easy
*  to imagine for me. So the first phase of AI story, I think basically was won by the safety crowd in
*  as much as they got their ideas into the brains of the people that are going to be the key
*  decision makers. And again, like I don't think you could hope for too much more than that really.
*  Yeah, that is a good point as well. I don't think I don't spend much time thinking about how things
*  could be worse. But now that I'm thinking about it, it definitely could be worse.
*  It could be a lot worse.
*  Yeah. I mean, even I don't know, like politicians, you know, it seems like Rishi Sunak was personally
*  convinced by some of these once esoteric, esoteric risk arguments. And Ian Hogarth is at the chair of
*  the UK AI Safety Institute. And he wrote a piece in the Financial Times that was like,
*  we need to slow down the race to Godlike AI or whatever. It's amazing when you think about it.
*  This stuff has gotten off what was essentially just a bunch of forums and blogs.
*  Like now just like being discussed in major halls of power by super important people.
*  Yeah, it is incredible. It's definitely the opposite of that Tyler Cowan piece that came
*  out the other day. It was like, AI safety is dead.
*  Yeah, I'm a big fan of Tyler. I do not agree with that take.
*  Yeah, I just didn't agree with that either. But yes, that is a really good point.
*  And that's basically my next point in terms of reasons to not be a hardcore doomer.
*  You said it, society at large is not sleeping on this. And I would say the government's
*  done better than I would have expected. We've had Time Magazine covers, the overdue window is
*  wide open. The only thing I do think is dead is AI safety respectability politics. I've been
*  around the scene long enough to remember when so much energy was put into, we got to not seem
*  crazy. Like this is really far out stuff. People are not going to be inclined to listen to us.
*  Anything we do that could make us seem crazy is a fundamental loss of credibility. People
*  put so much pressure on themselves. And honestly, I think that's like a pretty mature line of
*  thinking for people that genuinely were bringing some weird ideas to the fore. And honestly,
*  in many cases, we're weird people. It takes weird people to think weird ideas. And so,
*  remarkable amount of self-awareness in the AI safety crowd historically to just try to be
*  so thoughtful about it. I think it really speaks well to the intentions and the motivations of
*  this group that they were willing to be self-critical in such kind of personal ways to
*  try to figure out how can we be more effective communicators of what we think are really
*  important ideas. We know we're a little bit weird reading to people and we want to get that under
*  control and be really careful and thoughtful about how we deliver our message. I think that is
*  basically now over though, because again, we've had Eliezer in Time Magazine calling for willingness
*  to use airstrikes in some scenario and basically just everything is on the table. So that part of
*  AI safety, I think the sort of anxiety around what if I say the wrong thing? Is it going to
*  discredit the field forever? I think we can all leave that behind, which is good. And then the
*  government has done really pretty well in terms of, I would say, just genuinely engaging with the
*  subject matter. It's like the Biden executive order, I would say, is a pretty good thing.
*  Policy is really hard. But to start with something that's a pretty light touch, that's not shutting
*  down the practical utility, that has a pretty reasonably chosen threshold that, contrary to
*  what many people will claim, I think genuinely does only apply to a small number of very well
*  resourced companies doing a 10 to the 26th flop model. That's a pretty thoughtful, low impact,
*  high leverage way to start to get a handle on the situation. And there's even the lesser known
*  provision in that executive order around models trained on biological sequence data,
*  which is that they have to be reported at 10 to the 23. And I think that's also really smart
*  because the AIs become superhuman in biological modalities way faster than they become superhuman
*  at language type tasks. Because we invented all the language tasks, we have experts in all of them.
*  Nobody can speak DNA in the way that models are likely to be speaking DNA over the next several
*  years. So that's an area that, in my view, definitely demands extra attention. And they
*  had that clause in there. It didn't get a lot of attention, but it is part of that order.
*  So there's clearly some very thoughtful people in government. And I'd say their approach has been
*  like quite good. I'm probably a very technology positive person and generally libertarian in my
*  political outlook. I think it's sad that we don't have more nuclear energy, for example,
*  and everybody in the AI spaces, we don't want to end up like nuclear energy where like,
*  all the good stuff is somehow made illegal. And yet we still have all the weapons. And I share that
*  concern. I would hate to see us end up there. And we could like that is with all of these things.
*  It's not like the risk is taken off the table entirely, but it's a good start from the world's
*  governments, I would say. Yeah, I agree. What do we have now?
*  Yeah, I combined society and government. So we've covered six. So seven, I think,
*  again, I think probably covered enough. But basically, it seems to me like a sweet spot
*  is possible to find and maybe hang out in for a while. And I think we've just entered that
*  sweet spot with GPT-4. The sweet spot being it's powerful enough to be really useful,
*  but not so powerful that we have to worry about it getting out of control.
*  This is a conclusion that I came to in my GPT-4 red teaming, where I spent two months in basically
*  total isolation, just testing it in every dimension that I could come up with. And I
*  came back to OpenAI and said, I think this is safe to deploy only because it's limited in power.
*  You do not have it under control well enough that you could launch a much more powerful version.
*  But this level of power, it's very useful to me. But I've tried to see if it could
*  show any signs of getting really out of control. And I just, I cannot get it to be that powerful.
*  So that's the sweet spot. I think we've entered that range. And as we discussed earlier, I do
*  think we probably have one more turn of the scaling screw to go before we'd have to worry
*  about leaving that happy sweet spot range. At some point, we do get out of it. I think
*  I would be very surprised if we don't get out of that with indefinite scaling. But
*  that's why I pushed this adoption, acceleration, and hyper scaling pause agenda. Because
*  I think even though a lot of people are using CHI GPT, I don't think the average person understands
*  how much utility there already is. And if they did have a better understanding of just how capable
*  the current systems are, I think that would also probably be a little bit more amenable to
*  some sort of pause or slow down. Because they'd be like, jeez, if it's already better than human
*  doctors, can't we satisfy ourselves with that for a while before we have to go 10x further on the
*  inputs? And I'm not sure that everybody would be satisfied by that. But the public, the sort of
*  policymaker, it's, it would, you could, again, you could imagine a scenario where these things
*  are inseparable, right? That the utility and the sort of potential for loss of control, just,
*  there's no happy zone to be in. But it does seem to me that there is a happy zone to be in,
*  and we've just entered it. And hopefully, we can develop it before we race out the other side of
*  it. But at least the fact that there seems to be that sweet spot in the first place is something
*  that didn't necessarily have to be the case. True. I think people, or the general public,
*  are already probably pretty into the idea of slowing down. I don't think you even have to
*  convince them that they can already get all of the utility out of current models. There's some
*  polling on this. I don't know how much to read into it. But my perception is that people are
*  not really into rushing to scale these models faster and faster. But yes, so reason eight.
*  I agree. Yeah. So the last one on my list is China seems to be recognizing the threat in
*  some important way. And I'm not by any means an expert on China. I've never been to China. I can't
*  read one Chinese character. So I'm very modest in my self-assessment of what I can realistically
*  say about China. But I do hate the fact that it's often held up as the sort of, you know,
*  oh, whatever. There may be risks, but we just have to go because otherwise China's going to do it.
*  They're not going to stop. They'll never stop. Right? So we have to do it because we just have
*  to beat China. I think that is the worst mindset, maybe not the worst, but it's a bad mindset.
*  And certainly think we're in a much worse position if we end up in an AI arms race,
*  US versus China, where it's the world depends on this. We did that once with the
*  nuclear technology. We still got missiles all pointed at each other. And I think we're like
*  still in the era. It's obvious that we're still in the era of nuclear threat, right? People have
*  gotten used to that background threat and don't stress about it as much as they used to. And maybe
*  we're in a little bit of a less hair trigger situation than we were in the sixties or whatever,
*  but it's still really bad. There's still tons of missiles pointed at each other and the nuclear
*  arms race is not over really. So I would really hate to see us get into an AI arms race. And
*  it is at least a positive, and this is probably the least positive point of all of these.
*  Because there is a lot of momentum for continued rivalry between the West and China and whose
*  system is going to prevail. And you hear these echoes of the Cold War of where it's like our
*  system versus their ideology. So I don't mean to be overly optimistic on this particular point,
*  but at least it does seem that the Chinese government recognizes that this is potentially
*  unwieldy technology. And they do seem to see it as a threat to their own government and regime
*  stability, if nothing else. I don't have a clear sense for whether Xi thinks that we need to worry
*  about AI's taking over the world, but I do think he's definitely worried about what it would do to
*  social cohesion within China and the information landscape there. And so they are not racing forward
*  in a totally insane way, as far as I can tell. They are definitely doing stuff. They've got
*  their own chat bots, plenty of researchers, definitely a huge contribution of overall research
*  comes from Chinese researchers, whether they're in the United States or in China proper, or in
*  the West or in China proper. But there at least seems to be some sanity at the top. Not necessarily
*  more sane than us, but I don't see them as being insane at this point. And that is better than the
*  argument that I often hear that we just have to keep going because China will never do anything
*  but race ahead. I don't see that as being a given. I do see that they have some appreciation for the
*  unwieldiness of the technology and perceive it as rightly both dramatic upside potential, but also
*  some what of a threat to their own power. And seems like they're poised to try to chart some
*  sort of responsible course. And if we're both charting some sort of responsible course, then
*  hopefully that can avoid an all out arms race where we throw other reasons for caution offside,
*  because we have to beat them. Of all these, I do think that's the one that is most likely to fail.
*  If it's cross one off the list, that would be the first one to get crossed.
*  Well, it's always seven if we cross one off. It's not that bad. But the China argument,
*  it really annoys me because it's clearly the case they kind of have more motivation to regulate
*  than the US does because presumably if you're on the CCP, you don't want super powerful chat
*  bots just spitting out whatever information. Maybe their motivations are bad, but they still
*  have the motivation to maybe be more inclined to clamp down on this than the US or another western
*  country might be. Yes, I think it's silly. Also, it doesn't us accelerating help them accelerate,
*  because then it's they can just copy stuff that we've done or whatever. I don't really know the
*  details of that. But yeah, I just think that argument is silly. Yeah, these are eight good
*  reasons. I feel slightly better now. I also think I should say that I'm not a hardcore doomer either.
*  I think I share your radical uncertainty. I can mostly just because I'm not a technical expert. So
*  I think it doesn't really make any sense for me to dismiss the optimists any more than it would make
*  sense for me to dismiss the pessimists if that makes sense. I just have to be like, oh, I observed
*  that all these people disagree. I guess I have no idea what's going to happen. Maybe I'm at 50%
*  just because that's half my point. Yeah, I think you're in very good company there. The
*  anthropic post about their core views on AI safety is basically boils down to radical uncertainty.
*  And there's been pretty similar statements made from other leading lab leaders. So I honestly
*  think this is maybe like the bell curve meme, right? Where you've got the least capable analysts
*  and the most capable analysts sharing the same idea. And then the one in the middle is the
*  one that's the odd one out. I do think the smartest, most plugged in people with the
*  most access to privileged information, they are also expressing pretty radical uncertainty.
*  So I think that is what the top of the field says with a few exceptions. And then you've got a lot
*  of people that are way too in love with a particular argument or have attached themselves
*  to something, you know, perceive this as being a political issue already or something that may be
*  somewhat knowledgeable. But this is the classic like Eliezer thing. When you're motivated to
*  reach a certain conclusion, every logical trick that you know can in fact make you stupider.
*  So I'd say your position is pretty savvy, really. The observed disagreement is high, but also the
*  expressed radical uncertainty from many of the leading people is high. So between those two things,
*  I think that's really the only sensible place for you to land. And yeah, I'm right there with you.
*  Yeah. Did you see? I think it's a Roman Yamplsky. It's a AI safety guys, maybe the most pessimistic
*  that exists. And he was like, my PGM is like 99.7 nines after the decimal place. And then Eliezer
*  replied being like, that's a ludicrously high number. And obviously the implication is clearly
*  there's only two nines after the decimal place, however. And then there are all these people in
*  his replies arguing about how many decimal places it should be to. And I just thought I was like,
*  very funny. I don't know, the person who said, oh my God, it's ridiculous to say 99, but it's
*  very reasonable to say 98. But yeah, I agree. I think anything over 90 is like clearly overconfident.
*  Yeah. Anyway, there's a question on the time scale too. I haven't listened to his recent Lex
*  Friedman interview yet, but one sleight of hand that people can sometimes pull on something like
*  this is to just say over the next 10 million years or something. And then it's most species
*  don't last millions of years. And we are definitely on course for radical change. I think in any case,
*  the question is, can we get to some radically different future that we would feel somewhat
*  good about at least, and that the actual residents of find that it's good for them. And on that point,
*  I'm still fairly radically uncertain, but definitely feel like there's no way to get to those
*  crazy nines. But if you were to ask a different question of does human existence in roughly its
*  current form go on for millions and millions of years, then I would also have to say, geez,
*  that does seem quite unlikely. But that seems like just too... And I don't want to project this on
*  them because I haven't even understood this person's take that much, but I do see that sleight of hand
*  sometimes going on where it's like define what is good to be like what is now too narrowly. And then
*  yeah, you're never going to be able to preserve that indefinitely. But that's also where we've
*  come from. Robin Hansen is a great commentator on the point that we would freak out our own ancestors
*  from not very many generations ago. And not necessarily in ways that they would approve of,
*  but nevertheless in ways where we feel quite confident that they're small minded for their
*  hypothetical rejection of our current lifestyle. So if we allow for something like that, then I think
*  it's, I don't see any way to get to many nines of confidence.
*  Yeah, I agree. I think we should ban anyone giving a P-Doom that is like to more than,
*  I know, two decimal places or something. Just shouldn't be allowed. Maybe they should all be
*  to like intervals of five. I don't know. I'm going to start legislating and everyone has to
*  listen to me. Anyway, we'd probably wrap up there, but this was really fun. Thank you for doing this.
*  I imagine people already know where to find you, but on the off chance someone doesn't know where
*  to find you. Do you want to let people know where they can follow your work?
*  Sure. First of all, thank you. It's been a great conversation. I've enjoyed it as well. And hopefully
*  it's useful to, if not ease anxiety, at least give something tangible to build on and believe
*  that there's enough of a chance worth fighting for. My sense right now is that this is the most
*  important issue of our time. I do think we're walking a bit of a tight rope into the future.
*  Everything is on the table in my view, from radically utopian to radically dystopian or
*  even extinction type outcomes. And it's going to be a societal kind of tug of war to try to figure
*  out first, hopefully like what is actually going on? Can we make sense of all this stuff? And then
*  secondarily, what should we do about it? But hopefully I've helped just at a minimum create
*  the case that there's enough there that's worth fighting for. This is not such a hopeful situation
*  that the right thing to do is disengage. On the contrary, I think there's definitely enough of a
*  chance that if you're worried about this, like in my view, the right thing to do is be involved.
*  There are a lot of different strategies that one can play from chaining oneself to a fence to doing
*  an analytical podcast about it. And I think people should play different strategies, right? Like the
*  most brittle ecosystem is monoculture. And I think like the most brittle AI safety movement would be
*  one where everybody does exactly the same thing. I actually do think an ecology is the right way to
*  think about a movement. And without being like prescriptive on what strategy somebody should
*  follow individually, I would definitely encourage anybody who has anxiety to channel that into some
*  sort of positive action that can play to their own strengths, whether that's again, chaining oneself
*  to a fence or otherwise. So to find me online, I have the podcast, it's the cognitive revolution.
*  It's at cognitiverevolution.ai. And other than that, I'm most active online on Twitter where I am
*  Labenz, my last name, L-A-B-E-N-Z. Awesome. Thank you so much again.
*  This has been a lot of fun. Thank you. It is both energizing and enlightening to hear why people
*  listen and learn what they value about the show. So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me on the social media platform of your choice.
