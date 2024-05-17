---
Date Generated: April 03, 2024
Transcription Model: whisper medium 20231117
Length: 3669s
Video Keywords: []
Video Views: 550
Video Rating: None
---

# How Hugging Face raised $235M
**Cognitive Revolution "How AI Changes Everything":** [August 31, 2023](https://www.youtube.com/watch?v=XWdV5P3SraE)
*  ML is the next programming in general.
*  It's so massive and the people that do it are so important.
*  Owning that platform becomes like a strategic priority.
*  Again, you look back at the list of investors here and Google and Amazon,
*  given that they don't own GitHub and they want to compete with Microsoft in everything.
*  I can see how an exit to one of those companies would be supernatural.
*  Hello and welcome to the Cognitive Revolution,
*  where we interview visionary researchers, entrepreneurs and builders
*  working on the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas
*  and together we'll build a picture of how AI technology will transform work,
*  life and society in the coming years.
*  I'm Nathan Labenz joined by my co-host, Eric Torenberg.
*  Hello and welcome back to the Cognitive Revolution.
*  Today, Eric and I are talking about Hugging Face,
*  which just announced a major Series D fundraise at a $4.5 billion valuation
*  from a long list of major strategic corporate investors,
*  including Google, Amazon and Nvidia.
*  I had been watching for this story to drop any time
*  because going back to the first half of July,
*  I had received a flurry of expert network call requests to discuss Hugging Face.
*  So in this episode, we'll cover everything that I told the investors.
*  Hugging Face is a fascinating company.
*  Started in 2016 as a chat bot company more akin to Replica
*  than the Hugging Face we know today.
*  The company has gradually become both the leading online hub
*  where people share and discover all sorts of AI models, data sets and demos,
*  and also a leading champion that the open source AI community counts on
*  to advocate for equal open access to AI tools in the halls of power,
*  such as the United States Senate.
*  I find Hugging Face and this deal in particular to be extremely interesting
*  because while the Hugging Face team is absolutely stacked with incredible experts,
*  and I've interacted with many of them,
*  and the value that the Hugging Face platform brings to the community is unmistakable,
*  I think it's still currently much less clear
*  that the company will be able to build a business
*  that supports such a high valuation over time.
*  While the company is a clear leader in AI model discovery,
*  it's currently just one of many options in the fiercely competitive compute market.
*  And while demand for compute is growing so fast
*  that it's likely to support growth for all players for a while to come,
*  I do see reasons to believe that the company's commitment to open source everything
*  could make it quite difficult to sustain moats and margins in the future.
*  We'll get into all that in more detail,
*  but zooming out from Hugging Face for a minute,
*  you might have noticed that we've recently been doing more analysis episodes
*  with just Eric and me discussing important news and developments in AI.
*  I love doing interviews for this show and personally learn a ton from the process,
*  but our audience data, imperfect as it is,
*  suggests that you all might be getting as much or maybe even more value
*  from this sort of analytical content.
*  Our goal is not to cover all the news and probably never will be to cover all the news,
*  but instead to contextualize key developments with in-depth analysis
*  that I'm not seeing well represented online.
*  As always, we value your feedback
*  and I'd particularly love to know if you'd like to hear more of these analytical episodes
*  or if you still prefer the interviews.
*  To borrow a meme, we're in the podcast arena trying stuff.
*  Some will work, some won't, but we're always learning.
*  So let us know how we're doing.
*  Leave a review on Apple Podcasts or Spotify,
*  leave us a comment on YouTube,
*  or contact us directly via email at tcr at turpentine.co
*  or by DMing me on the social media platform of your choice.
*  Now, here's an in-depth discussion on Hugging Face
*  and the unique role it plays in today's AI ecosystem.
*  Nathan, we're here today to talk about Hugging Face
*  and their most recent announcements and analyze the company a little bit.
*  Why don't you give maybe a little bit of overview on the company
*  and the product and then we'll get into it.
*  Cool. Yeah, happy to. I think this will be a fun one.
*  So context for this is Hugging Face just announced a big Series D fundraise,
*  $235 million.
*  That is now more than half of all the capital that's raised to date,
*  which is just under 400 million total raised.
*  And investors, some notable ones,
*  including Google, Amazon, NVIDIA, Intel, AMD, Qualcomm, IBM, Salesforce,
*  and Sound Ventures with a valuation of 4.5.
*  billion dollars, which is up 2x over the last year since the last round
*  and notably now valuation over a hundred times the company's annualized revenue.
*  But I think they're doing something like about 30 million a year in revenue,
*  which would put this at like a 150x.
*  Anyway, it's north of a hundred.
*  So pretty heady valuations for a company like Hugging Face
*  and it was without, you know, disclosing too much.
*  I've signed up for a bunch of expert network type mailing lists
*  and about a month ago, there were a flurry of, you know,
*  I don't even know, you know, what companies, you know, were scheduling these calls,
*  but definitely all of a sudden everybody across networks was interested in talking about Hugging Face.
*  So I think this is a really interesting one.
*  You know, there's obviously been a ton of debate about where the value is in the stack,
*  you know, which companies have positions that are going to prove defensible.
*  You know, is it about infrastructure?
*  Is it about bleeding edge algorithms?
*  And, you know, this one is a kind of a unique one because more,
*  and this is why I really wanted to talk to you more about it too,
*  is this one is more about community than maybe almost any other
*  AI startup that's got a high flying valuation right now.
*  And it's definitely, I think pretty interesting to kind of compare its value,
*  you know, and we can get into more detail on it's like product line too
*  and the role that it plays in the ecosystem.
*  But it's interesting to compare its value to something like a runway,
*  which is raised it over a billion dollars,
*  but is much more focused on models or somebody like Mosaic,
*  which was acquired obviously as we've talked about on a couple of episodes
*  for North of a billion dollars, much more focused on software scaffolding
*  to help you perform your own model training as well as an inference product.
*  I think what's really interesting about this one is product head to head,
*  you know, point for point, feature for feature, and certainly like revenue
*  probably as well doesn't seem obvious to me that hugging face is like killing it.
*  But what is special about it is this kind of place that it occupies.
*  That's at the center of so much activity in the broader ecosystem.
*  Let's get into that.
*  But first, can you give a little bit of overview or a deeper review
*  on kind of its product line?
*  Yeah, it's interesting.
*  So the hugging face is very, has a lot of surface area, put it that way.
*  I first started to pay attention to it as, you know, just a way of finding new cool stuff.
*  Early 2022, as I was looking at very actively for Waymark for what's the best model to caption an image?
*  What's the best model to pick an image that corresponds to a certain bit of text?
*  This stuff was just starting to work at that time.
*  And over and over and over again, it seemed like the demos, you know,
*  were starting to pop up on hugging face.
*  Like that was just kind of the place I kept noticing everybody was posting their,
*  you know, demo experiences to that has only really accelerated.
*  But I'd say that's been true now for the, you know, 18 plus months.
*  From there, I got engaged with them as and I don't even know if they still offer this program,
*  but it's definitely something new where I learned a lot from it in multiple respects.
*  I believe at the time it was called the expert acceleration program.
*  The basic offering there was, okay, you, you know, have a lot of questions.
*  We have a great team of experts that kind of is expert in everything.
*  And we will help you, you know, figure out what the best models are.
*  You can kind of ask us a certain number of questions each month.
*  And so for me, as like a one person AI R&D department, I was like, I could really use that.
*  You know, there's definitely some times when I have questions about feasibility,
*  you know, could I fine tune this or that?
*  Like, how does this work?
*  What is the, you know, what is the state of the art?
*  And that's one thing I've always kind of going back to hugging face, you know, with my feedback.
*  I'm like more curation, I think is something that they're going to have to continue to develop
*  because basically right now it all starts for them with an open source library, which is transformers.
*  They now have a diffusers library as well.
*  But they created just a canonical open source library.
*  And then they created this concept of the model hub on top of that library.
*  And it's basically all the models that can run on this open source execution code becoming,
*  I wouldn't say the standard, but a standard as kind of an underlying library.
*  And then increasingly playing for the standard of like the place where you would post your models to
*  and then elaborating on that has kind of created this over time,
*  this like very diffuse web experience where there's sort of pages, you know,
*  there's a whole section now where it's like all the papers are mostly trying to play,
*  you know, kind of publishing platform in a way, vis-a-vis, I mean, post archive, of course,
*  but, you know, they're like mirroring all the papers on the hub and they actually have the weights.
*  You know, when people, you know, open source, you can download and if it's built with their software,
*  then you can like easily spin it up into a little demo environment.
*  This is what they called the inference API for a long time, just kind of a real simple,
*  hey, you can, you know, if a model is here, we can load it up for you.
*  You can ping it a few times.
*  Then they have the spaces, which is where the demos come in.
*  And they've acquired a company called Gradio about a year ago that makes it easy to do these demos.
*  And so, you know, they host those as well.
*  And if you, you know, buy like a pro account, you know, you can get bigger servers.
*  It's a little bit repel like in that sense where you have like your own little coding environment
*  that you can kind of create the demo, you know, on top of the model because the model itself often,
*  you know, needs a wrapper of what are the inputs, what are the outputs, how's that all going to look?
*  And so, you know, they're kind of building this community first approach.
*  This is where people come to share.
*  This is where people, you know, show off their demos.
*  This is where people can, you know, fork and recombine models.
*  There's a whole data sets are published as well.
*  It's all organized across all these different tasks.
*  So if you want to go look at, you know, what's the show me everything that captions images versus,
*  you know, show me everything that is text to speech versus show me everything that is speech transcription.
*  You know, you can kind of see all these different lenses on everything that is going on in AI.
*  And this is all kind of been built, you know, I think the company and the product in some ways kind of reflect each other.
*  You know, it's a remote first company with people kind of spread all over, you know, very broad set of expertise.
*  And, you know, all these kind of experiences have kind of been built up over time as well.
*  The team is really strong, right?
*  So you can with all that stuff going on and with all the kind of different ways you end up getting linked to hugging face.
*  I was like, I know there's a lot going on here.
*  I feel like I want to, you know, make sure I'm making the most of this platform.
*  Even if that just means being able to clearly figure out what is the state of the art that has been open sourced at any given time.
*  And for that, it was worth it to me to become a customer of the expert acceleration program.
*  And from that, I really learned.
*  Yeah, they do have a really awesome team that has a super diverse set of, you know, different backgrounds and expertise.
*  They actually were very useful to me, especially in those kind of early AI obsessive days where I was like, you know, and when I was initially most focused on just making a product work well, you know, building an app.
*  I'm like, I need the best image capture that I can get.
*  Fast forward to the end of this research question and tell me what the answer is.
*  You know, can you can you help me with that?
*  Now, it's not always super easy, right?
*  There's a lot of, as we've covered in many different ways, a lot of surface area.
*  It's a lot of trade offs, a lot of, you know, depends exactly on your use case.
*  So it's not always to say that they could provide definitive answers, but I did come away from that engagement.
*  Super impressed with the team and feeling like, yeah, there's a lot of expertise here and you can kind of see why they are a center of activity.
*  And I think they're still honestly kind of figuring out like, how do they actually turn this into a business?
*  You know, there's so much activity, but this ratio, you know, of the 4.5 billion to the 30 some whatever million in revenue is super high.
*  And it does, I think, reflect that there's a lot more latent value than they have been able to monetize so far.
*  As I understand it now, it seems like the biggest way that I think they're looking to monetize is by access to compute, right?
*  They want to kind of say, we've got all these different things, whether it's, you know, models hosted or data sets that you can run training on or, you know,
*  increasingly more and more different things.
*  What do they all have in common?
*  They need compute to run.
*  And so in addition to the way that you find all this stuff will also be the way that you run all this stuff.
*  And that's where products like the inference endpoints come in.
*  And some of these numbers, too, the download numbers on these are kind of amazing.
*  Sometimes you look at, you know, just a random model where the actual weights, you know, have been trained and now uploaded and open sourced on the platform.
*  And how many people are downloading these things?
*  And some of them just, you know, right now browsing around the website, 35,000 downloads for some, you know, particular fine tuning of Code Llama 34B.
*  I mean, you know, that's pretty niche in some respects, and it has 35,000 downloads in like the last week.
*  So there really is a lot of people coming here to discover stuff.
*  And then they want to just take that next step to say, okay, now you want to just serve that in an application, you know, click a couple buttons here and we will, you know, handle everything from there.
*  And again, the fact that most of these models have been built on their software library allows them to spin that up relatively easily, but it's still kind of a jungle, you know, and I think they're very much still working on figuring out exactly how to make that awesome for people.
*  You know, one of the complexities, of course, is like, there are literally, you know, thousands, if not tens, there are tens of thousands of models.
*  I don't know how many are really actively used these days, probably hundreds that are like doing any significant inference endpoint work, but still, you know, that's a lot, right?
*  And it's very hard to optimize across all those different possibilities and, you know, all the different workloads that customers bring to the table and so on.
*  So it is very interesting because it is, it is one where community drives so much.
*  The promise is there, the, you know, the product set is definitely still in the kind of phase of maturing, but that has not, you know, stop them from raising a handsome amount of money.
*  Yeah, that's a great overview.
*  Hey, we'll continue our interview in a moment after a word from our sponsors.
*  If you're a startup founder or executive running a growing business, you know that as you scale your systems break down and the cracks start to show.
*  If this resonates with you, there are three numbers you need to know.
*  Thirty six thousand, twenty five and one.
*  Thirty six thousand.
*  That's the number of businesses which have upgraded to NetSuite by Oracle.
*  NetSuite is the number one cloud financial system, streamline accounting, financial management, inventory, HR and more.
*  Twenty five.
*  NetSuite turns twenty five this year.
*  That's twenty five years of helping businesses do more with less, close their books in days, not weeks and drive down costs.
*  One because your business is one of a kind.
*  So you get a customized solution for all your KPIs in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts and improve margins.
*  Everything you need all in one place.
*  Right now download NetSuite's popular KPI checklist designed to give you consistently excellent performance absolutely free at NetSuite.com slash cognitive.
*  That's NetSuite.com slash cognitive to get your own KPI checklist.
*  NetSuite.com slash cognitive.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it to use cog rev to get a 10% discount.
*  Let's get into communities for a bit because communities on their own, they're not defensible.
*  Like if you look at Dig, remember Dig, Dig, you know, pre-Reddit, Dig was one of the most valuable communities on the internet, the front page of the internet where so many people went to see what was happening.
*  And then the challenge with communities is sometimes what makes them special is their exclusiveness.
*  I.e. it's for a certain kind of person and it's not for another kind of person.
*  And what often happens is as communities scale, you sometimes have negative network effects where the bigger the community gets, the less special it gets.
*  Think of any sort of nightclub or party or any sort of group of people.
*  Clubhouse.
*  Exactly.
*  Where there's a special vibe to it.
*  As soon as everybody comes in the party, it's no longer as fun of a party anymore.
*  Now different communities get at that at different ways.
*  The bigger it is, you have to be getting some like utility to the community.
*  Like people always ask me like how big should we make our community?
*  And I would say basically like it depends on the goal of the community, but often like every additional member should be making the community stronger.
*  And so it's less about size and it's more about solving that specific question or the community goal stronger.
*  And often if the goal of the community is like the relationship between its members, smaller is typically better.
*  But if the goal of the community is to aggregate some sort of data or insight, the more can be better.
*  But just to close the dig example, there was a bit of a rebellion among its users and people were mad about something.
*  And then they just switched to Reddit almost overnight and Reddit became the new dig and Reddit has, you know, become, you know, been a massive company ever since.
*  And what that just showed is that community on its own is very difficult.
*  In order to make communities defensible, you have to get the community to do something on the website.
*  That it would be hard to get them to switch, right?
*  Like, you know, on LinkedIn, for example, you have all your connections.
*  You've built up that connections over years.
*  You have your identity.
*  You have all these recommendations.
*  You have these references.
*  People could hate LinkedIn, but there's not going to be a rebellion onto a new platform because the social cost and the coordination cost is just way too high.
*  With dig, it's just Reddit.
*  You just create a username.
*  That's it.
*  That's all you do on the site.
*  You have your posts.
*  I don't mean to downplay it, but with social networks like LinkedIn, you know, Facebook, we'll get into GitHub in a second.
*  You've created state on the website.
*  You've aggregate, you've input data.
*  You've created connections such that the switching cost and coordination cost is too high to leave.
*  And that's why people say LinkedIn is this incredible business.
*  Everyone's trying to disrupt LinkedIn.
*  They can't, you know, be trying for 15 years.
*  They can't and people don't even like LinkedIn.
*  The users don't even like it.
*  They're like, I hate this website.
*  And yet they're on it every day and they can't leave it because and so that's an example of of a company that started as a community, but built defensibility via sort of creating, you know, places to own identity and connections.
*  And I've been on both sides of that.
*  I mean, I was at think of things like product time and hacker news.
*  It's not just the possibility.
*  You also have to create a way for value to be to be exchanged.
*  What LinkedIn does is it not only brings people back every day, you know, you get information on LinkedIn that you can't really get anywhere else.
*  You know, people's detailed professional history, what people think about each other, you know, who's viewing your profile that that's that's pretty valuable.
*  And and, you know, ability to get in touch with people.
*  Ultimately, what GitHub does is it and maybe this is we would get a hugging face.
*  Is it not just is a community of engineers?
*  It's a community.
*  Basically, vertical LinkedIn for engineers in terms of people aren't just coming back.
*  They're inputting all this valuable data that makes the website valuable, even independent of people coming back every day.
*  That is something that sites like Hacker News or Product Hunt have not done.
*  Like Hacker News and Product Hunt have to reinvent the wheel every single day, kind of like DIG.
*  Now they've maybe done a better job on community or branding where people aren't throwing rebellion on them.
*  And there's there's some moat like people are coming back every day, but these are not big businesses.
*  They're not venture scale businesses because they haven't really figured out.
*  They haven't created a ton of identity or state on the site itself.
*  And every day it's kind of a rat race to create this value, but there's no compounding value.
*  Like the way to do that.
*  And we tried this and they're actually trying it right now.
*  God bless them.
*  Like Product Hunt could have turned into like a G2, which for people don't know it's almost like a Yelp for products.
*  Like it would have just been not what's great today, but like almost wire cut.
*  Like here's a review of products historically in a way that would have people coming back to look at not just that today, but but historical.
*  And so I think that's the big challenge.
*  If you're a community business is one, what can you use the community as a wedge to create?
*  What data set can they create that will make the website valuable independent of people coming back right away?
*  Because that will also make it difficult for those people to leave.
*  So what do you think that could be for Hug and Case or any reactions to that analysis?
*  It is still an odd mix, you know, it's like it's not obvious that discovery and inference naturally go together.
*  If the model is basically this and I think this is kind of, you know, the core thesis right now seems to be pretty apparent.
*  All the demos are going to be on here and you're going to find the models on here that power those demos and you're going to spin up your own on our infrastructure.
*  And then, you know, it'll be convenient and you'll pay us for that.
*  I will make a margin over, you know, the cloud providers that they use and just based on, you know, the investors here, Google, Amazon, NVIDIA, Intel, AMD, Qualcomm, AMB, IBM, Salesforce, Sound Ventures.
*  I mean, you know, obviously a lot of cloud infrastructure there.
*  So, you know, they've got the right partners and they can presumably make some margin.
*  But like that product has this thing on its own, you know, it has to be excellent because it's not that hard to take that model because again, the Hug and Case premise is
*  that the model itself is open and you can just download it and you can go do your own thing.
*  You know, you could take that direct to Amazon.
*  You could take it direct to Google Cloud, you know, notably not on there is Microsoft.
*  You could take it to Microsoft as well.
*  All these demos are also open source.
*  You know, the sort of code sharing on Hugging Face is very much like, I mean, it's basically the same thing as Git itself, except that they lean more into providing
*  a running environment.
*  When you go to GitHub, you look at a repository, you know, this is starting to change with like code spaces where you can say, okay, I want to not just look at this
*  code, but run this code in a way that's, you know, not going to take me a ton of setup on my local computer or, you know, whatever else to actually get started.
*  They're making progress on that.
*  But I was at Hugging Face is definitely ahead in that, you know, the demo is there.
*  You can kind of run it.
*  You can fork it into your own, you know, running environments a little bit more replete-like in that respect.
*  But the competition is like pretty fierce from all these different angles because the code is open source.
*  The model is open source.
*  If I think that their inference endpoint is too expensive, you know, I may love the community.
*  I may love coming here and prototyping stuff.
*  I may be willing to pay my, I think it's $9 a month or whatever for the pro account, you know, that gets me the like slightly souped up demo environment so I can do my prototyping more
*  effectively.
*  But if that inference product isn't awesome unto itself, then I'm going to make that decision pretty independently.
*  I think in most cases, certainly like with Wimart, we talked about this a little bit in the last analysis episode too, where, you know, what makes the
*  OpenAI 3.5 fine tuning so awesome in addition to the fact that the model is great and it's easy to use and the fine tuning is like quick and cheap, which, you know, fine tuning in general is
*  getting pretty quick and cheap.
*  But it's basically infinitely scalable and immediately available as soon as you do it.
*  So, you know, if I do a fine tuning and want to make a hundred calls to it immediately and then never call it again, like they allow me to do that, you know, it's so easy.
*  The inference endpoint in the Huggins face case right now is not as mature as that.
*  It does not scale up.
*  You know, they do have auto scaling, but it's a little rougher.
*  It's just not as mature.
*  You kind of have to have one thing running all the time and, you know, then you can go turn it off, but it's not so like, you know, immediately turn on, immediately available, just totally priced and structured to your, you know, amazing convenience like the OpenAI one is.
*  And so if there are things that I don't like about that, or I just don't like the margin that they're taking, you know, if I'm really hitting some scale and it's like, you know, it's time to actually look for cost savings, then I think the
*  lock-in that the community creates to the inference product is actually very small.
*  You know, it's more of like a lead gen type function for an inference product.
*  But if you're a sophisticated app developer, there's really nothing preventing you from, you know, taking all that stuff and going somewhere else.
*  And I think there's also some interesting challenges that they're likely to face too, that you alluded to with the dig example.
*  Which is that they've kind of developed a community that you can't characterize the Huckingface community is huge, right?
*  I mean, it is a big community.
*  They've really closely tied the company's identity to open source and open source, you know, kind of being an inherent good.
*  It honestly is kind of ideological at times, like the company's positioning is kind of ideological.
*  The community that is most excited about it is kind of ideological.
*  It's definitely in opposition to more AI safety hawk type people who are like, you know, open sourcing this stuff is not necessarily a good idea for now.
*  I mean, typically those people, in fairness to them, are not so worried about the current generation of models being open source, but just the general pattern of making stuff, releasing it before we even know what it does, you know, especially as we continue to scale stuff up.
*  Does seem like there's going to be some real unexpected consequences from that.
*  The Huckingface discourse doesn't allow for a ton of recognition of that because their whole kind of thing is like access, you know, a sort of egalitarianism.
*  You know, it goes so far as to reflect in a leaderboard product that they have.
*  And again, this goes back to like, I tell them like curation is a big part of your value to me.
*  I want to hear what you think about curation too, because that also seems like a tough business to, you know, certainly to create lock into like the high dollar products with the leaderboard that they have.
*  They have an open LM leaderboard.
*  And, you know, it's not like it's like.
*  Fair enough, you know, you call it the open language model leaderboard, but it's not useful to me because they don't show the best models.
*  Like you literally go to the Huckingface language model leaderboard.
*  GPT-4 is not there and 3.5 is not there.
*  Nothing from Anthropic is there.
*  I think Lama is basically there even though Lama wasn't, you know, fully commercially whatever initially.
*  I think they kind of round that into inclusion.
*  But it's like if you want to make a leaderboard that shows me what the best models are or, you know, how the best open source models compared to the truly best models.
*  You got to show me how good the, you know, the actual best commercial models are and, you know, the reality that they are beating the open source models is like not one that, you know, again, sophisticated customers are going to fail to realize.
*  So at times it feels like there is a sort of ideological kind of nature to some aspects of the company and some potential at least I wouldn't say this, you know, exists, but certainly the potential for a certain kind of audience capture.
*  Where, you know, if they ever want to make certain moves to like you could imagine they might say, well, we're going to train our own models and they won't be open source and we'll serve those.
*  I think they're going to have a very hard time, right?
*  Making those kinds of deals.
*  There's any number of licensing deals they could do where, you know, folks might publish models on their platform and then, you know, have some sort of rev share depending on how much it gets used more in very early days.
*  I think of business model development here, but the fact that there's such a hard commitment to open source so early, you know, does make in my mind for kind of a hard strategic dynamic in some cases, because people are used to, you know, just.
*  Everything I'm talking face is supposed to be open and free.
*  That's the model, you know, increasingly that's the data sets.
*  It's definitely the demo code that runs it, you know, and all that freedom is awesome.
*  In the end, like the inference product, you know, still has to just earn its keep.
*  It doesn't get that much.
*  I don't think of an advantage for all those, you know, nice public goods that hugging face creates.
*  If you don't win head to head, you know that lead gen is not worth potentially that much.
*  Curation is interesting, right?
*  Because product hunt curated the best products every single day and that's a journalist do and it turns out that's just not a massive business.
*  It's important.
*  It's a size, you know, it's a business, but it's not a massive, you know, business.
*  It's not a repeat.
*  It's something that you have to start over every day and the value there just isn't that high.
*  It's not like their core business problems around, you know, what's the hot thing today in a way that they can easily monetize product on.
*  Now with something like G2 or there are other sort of companies where they're basically reviews of enterprise products.
*  These are decisions that have a big spend to them and all people who are building companies have to use these products and they have to determine which are the best one.
*  And they go to a site that like G2 that helps them determine that there's something that's something they're willing to pay for.
*  And that's an enterprise version, but a consumer version is something in a different way.
*  Glassdoor where people have to determine, you know, which companies to work for and Glassdoor is a review site of companies told from the employee perspective, not just how they're doing, but what it's like to work there, etc.
*  Another example, consumer example, obviously is Yelp, right?
*  People, you know, we need to decide where to get dinner tonight and Yelp helps us, you know, determine that and that not just for restaurants, but for all different types of services.
*  And so what's cool about those examples is that you don't have to start over every day in the same way that you do with like hacker news or product hunt.
*  So there's some compounding value to that.
*  But then also they have real spend to them, especially the enterprise version.
*  It's also, it's not, it's not that you want them to be evergreen forever.
*  There's no turnover.
*  If there is high turnover and high spend, that's also valuable because you need to continuously get new, new reviews.
*  The thing I would ask, how do you face is like, okay, is there a firm of your creation that has a high spend to it that has some turnover but isn't like reset every single day that you can add compounding?
*  You can get compounding value from from continuing to have reviews and and and and thus people willing to to pay or businesses willing to pay hugging face in some capacity.
*  Yeah, certainly the change, you know, is happening fast enough that like you do need to keep the content fresh.
*  You know, I don't know if that works for or against the kind of staying power of the business because there's always something more to discover.
*  On the other hand, if it ever stops becoming the place where these were, you know, the where the best kind of discovery happens, you know, for a month, like the prior content on their ages pretty quickly.
*  And, you know, nobody's really at this point concerned.
*  I mean, it's as many models as they have on there, right?
*  And it's again, probably in the tens of thousands, if not hundreds of thousands, maybe of raw models that have been uploaded.
*  Any of those that are more than, you know, eight months old at this point, anything before, you know, chat GPT like who cares, right?
*  It's all kind of dated.
*  So that'll that'll continue to happen.
*  Presumably, they have to I think maintain that kind of focal status above all else or like everything else seems to be pretty quickly at risk.
*  The analogy to some of these other business you're describing is tough because then for one thing, none of those are like super huge businesses, right?
*  I don't think any of G2, Yelp and what's the Yelp's market cap right now?
*  It's got to be lower than hugging faces, right?
*  You know, it's basically an advertising model at the end of the day, right?
*  Because you go here and there's like all this credible content, then it kind of creates promotional opportunity alongside that content.
*  And, you know, that's not the hugging face model as it stands today, right?
*  I don't know what the analogy would be.
*  If you took like G2, it would be like almost as if, you know, it was just reviews of only open source, you know, software projects for whatever.
*  And then at the end of the thing, you can either like host it on their site or you could go, you know, download it and run it on your own server.
*  I mean, that would be very certainly very analogous.
*  I don't know that there's the like space to monetize hugging face in that way or the like scale because there's definitely always room for some advertising, no doubt.
*  But let's just dream big here.
*  Like if hugging face is a $50 billion company someday, like why could it be like what is sort of the biggest version of what hugging face could turn into?
*  You know, GitHub for AI is kind of the elevator pitched by analogy for hugging face.
*  And obviously GitHub was worth a lot of money.
*  And I think, you know, I don't get the sense that Microsoft regrets buying it at all.
*  So they've done well there.
*  I think it would be I would guess that the ratio of the GitHub acquisition price to its revenue was also like extremely high because at least the things that I have usually paid for and I think that most developers pay for on GitHub is like a handful of dollars a month.
*  And the main thing it allows you to do is like keep your code private.
*  You know, you can use GitHub for free.
*  You got to publish all the code.
*  You want to have your private stuff.
*  You got to pay a few bucks.
*  Hugging face, you know, has a similar thing.
*  That's like the nine bucks and you can kind of, you know, have your private spaces and a little bit more horsepower behind your public demos or whatever.
*  So, so far so good.
*  You know, what is Microsoft really valuing in that?
*  I think they're above all just valuing.
*  They have, you know, hooks into tens of millions of, you know, developers around the world in some way, shape or form.
*  And we know that that's like a very valuable profile.
*  And, you know, hopefully we can sell out more stuff to them later.
*  And, you know, you're starting to see that product.
*  See develop with code spaces and with copilot and, you know, presumably it will continue to mature, but they honestly didn't really need ROI.
*  Right.
*  It's a little bit more of like a defensive arguably position from them where they're just like, you know, we're two trillion dollar company.
*  Let's go pick this thing up and we'll make sure that we continue to be like super focal and almost, you know, inescapable, unavoidable from a developer standpoint.
*  Hugging face could maybe pull off a similar thing.
*  I think, you know, if it were to sell for $20 billion in, you know, two years, it would seem or in three years or whatever.
*  It would seem like the most likely scenario would still be that the revenue is like very much kind of trailing the value.
*  And it would be just a broader sense that like, hey, ML is the next programming in general.
*  It's so massive and the people that do it are so important.
*  And, you know, increasingly like so many decisions are made at that level that owning that platform becomes like a strategic priority for somebody.
*  Right. I mean, again, you look back at the list of investors here and Google and Amazon.
*  You know, right off the bat are kind of like, yeah, I can see why given that they don't own GitHub and they want to compete with Microsoft in everything.
*  I can see how an exit to one of those companies would be supernatural where they would say, you know, we don't really care how many people you're charging nine bucks a month.
*  And we don't even really care if your inference product is like truly top notch.
*  We want a community layer to our, you know, mega stack.
*  And that's kind of that.
*  If you're buying in at this valuation, I find it hard to see a different story aside from that right now.
*  I mean, I guess the other candidates would be like, they go like replet and just.
*  And by replet, I just mean world class execution, you know, project after project.
*  And like I can face does well on stuff, but it's not quite that, you know, sort of thing.
*  Right. With the community nature of it all comes a lot more messiness.
*  And, you know, they don't have the same kind of like super clear, super visionary product vision as much.
*  They're more like, oh my God, we have all this activity.
*  We have all this sharing. We have all this discovery.
*  We have all this, you know, energy.
*  What do these people need?
*  You know, then we can kind of figure out how we back into offering them something.
*  It doesn't seem like they're going to take a huge bite out of inference in the same way that I think like a replet
*  because it's so different and because it works so well, seems like it's a lot closer to taking a real bite out of just like cloud in general
*  compared to what I've seen from Hugging Face.
*  And I love the vision, by the way, of the inference endpoints.
*  I'm actually on, you know, full disclosure.
*  I've, as I've been being a customer of the company, I have no, you know, financial stake or formal relationship whatsoever.
*  But I did participate in the inference endpoint beta.
*  And I do love the vision from a customer standpoint of being able to say, I always tell them the task page is where I think you guys should really make your front door.
*  You know, because I, if I have a task, if I'm that far along, then you can show me the best options to solve that task.
*  You know, a task would be, again, image captioning, text to speech, transcription from speech to text, whatever.
*  They have probably 20 different tasks for which they have, you know, kind of something like a leaderboard.
*  And the leaderboard doesn't even need to be against a benchmark.
*  You know, you know, a good leaderboard these days would have like a number of data sets that all these things are benchmarked against
*  and you could see relative performance quantitatively.
*  They don't necessarily have that for all of those.
*  They don't need to have it for all of them.
*  They can get by to a significant degree with the likes and the number of downloads and you know, just the kind of community commentary can be pretty clarifying.
*  So I do love the idea of just going to a task page, looking at the first, you know, five things being like, okay, here's the five coolest demos that are out there to solve this problem for me right now.
*  Let me go mess with each one.
*  They're all kind of running.
*  They're ready to go.
*  Now I can, I mean, because this is a huge contrast to what came before, right?
*  I mean, to give the credit where it's due, the alternative to a hugging face demo, and I'm old enough to remember, I mean, open source has made incredible progress into the ML community in terms of just what the norms are.
*  If you go back a few years, pretty normal would be like we publish a paper, we share our results.
*  We maybe publish a data set.
*  We maybe give you like a little script that you could use.
*  It was more of kind of a reproducibility notion.
*  Like the reason they were publishing code out of a lot of academic environments was like, we want you to be able to kind of reproduce our results.
*  And therefore, you know, by putting that out there, so you in theory can like we demonstrate that we actually did the work and that, you know, the model can actually perform what we say it's going to perform.
*  But very few of those things were ever intended to be like broadly used, you know, more than a couple of years ago.
*  So it was often through this kind of we're giving you the tools to reproduce and like validate that our work is real lens, not like we're trying to set you up to actually go use it, you know, in a real practical setting somewhere.
*  So that has changed dramatically.
*  Code is now very common.
*  You know, actual trained models is increasingly very common.
*  You know, people on kind of hugging face part of Twitter, you know, are kind of like weights or didn't happen, you know, and even demos.
*  Now, especially again, they acquired this company, Gradyo, which makes the demo creation process really easy.
*  So it is incredible how much again, just in the last 18 months, it has gone from.
*  Okay, here's an interesting paper.
*  They're not like refusing, you know, to allow me to reproduce it.
*  They're not like keeping secrets, but the way that they've made it available to me is hard to evaluate.
*  Hard to just hard to get over the hump to even see like, is this something that could work for me and whatever, you know, context I'm working in with the demos on?
*  Hugging face like that is so much easier.
*  So you can, you know, you can fast forward instead of, you know, might have taken you a week before to be like, okay, paper code.
*  I have to maybe retrain the model.
*  I got to figure out how to do this.
*  Like what libraries is it used?
*  Oh my God, blah, blah, blah, blah.
*  All just to get to the point where you could be like, yeah, they did it all in their academic setting, but I have some real world inputs.
*  Does it work for me or not?
*  A lot of times it doesn't necessarily.
*  So that's a lot to put in.
*  Hugging face today, you can get that down to two hours.
*  You can, you know, go to the task page, try the demos, run a little script, try a handful of things against a handful of different demos.
*  See if anything's really compelling.
*  And then, you know, pretty quickly move over to your inference API as well.
*  And that is like super smooth.
*  And definitely great value to the community.
*  Again, then the question just becomes like, if I go through all that and I'm really hitting scale, you know, what lock in is there to keep me by from hugging face?
*  It either has to be the best on a pure performance value basis, kind of independent of all that discovery.
*  Or, you know, it's pretty easy for me to switch.
*  So yeah, I don't know the curation.
*  Like it is super valuable, but how do you, it seems hard to capture that value, you know, and then you can imagine that they could have a sort of more marketplace type of thing.
*  Again, think about a G2.
*  It's like people can pay to advertise there because they're offering proprietary stuff and, you know, they can get an ROI back.
*  Nobody's really going to advertise their like fully open source model.
*  So at some point they may, you know, if they wanted to go a route where they might say, you know, we want to help you discover both open source and commercial stuff.
*  And we want to monetize the commercial stuff.
*  That would make a lot of sense to me in some ways.
*  I think it honestly would be more valuable to users.
*  It'd be more valuable to me if hugging face would put the commercial models on their LM leaderboard and like kind of do that across the board for all the different tasks.
*  I may care depending on the circumstance, right?
*  But I'm definitely open to commercial things that are not open source.
*  I'm interested in open source as well.
*  Commercial has a certain appeal because I can generally assume that like they're going to handle more problems for me.
*  Hugging face tries to bridge that themselves by saying like, we'll handle a lot of the problems for you of doing the open source stuff.
*  But I want the complete set, you know, it seems like to me the curation value right now is a little bit undermined by certain commitments
*  and kind of expectations around commitment to open source where as an app developer, you know, I just want clarity.
*  I want the full menu of all the models, how well they perform, you know, ideally what they cost, what the rate limits are going to look like.
*  You know, if I want that whole thing and by kind of pretending that a certain amount of it doesn't exist in the way that they present stuff, that's definitely less value than I could be getting.
*  So it's interesting to me that it feels like certain strategies, I don't know that they're closed off, but it feels like they would have a hard time pushing back against the community.
*  And there's again, there's going to be fierce competition from every direction, right?
*  If they take one misstep, GitHub is right there to say, you know what, guess what?
*  We got a live demo thing and you know, who has plenty of disk space for all those models?
*  And honestly, they might even be able to just mirror it directly.
*  I mean, some of this stuff is the legal regime on all of this is very much uncertain, but you know, going back to a LinkedIn, right?
*  There's been some court rulings that like you can scrape LinkedIn and you know, it's not illegal for you to do so.
*  This information is kind of out there and you know, again, there's some fine points around that.
*  But basically, you can scrape LinkedIn.
*  Something similar might be the case with Hugging Face where I'd be like, you can download all the models from Hugging Face.
*  They can't really prevent you from doing that.
*  And you know, if all of a sudden GitHub mirrors all of Hugging Face and has a compelling thing and also has commercial models that are kind of on that menu,
*  I could see, you know, I could see some ways that it could become pretty uncomfortable for them to try to keep everybody happy.
*  You know, how do we keep that open source ethos, but also have the full thing and you know, a lot of stakeholders.
*  It's not easy to manage such a diverse, you know, many-sided marketplace as they're kind of trying to develop.
*  I want to return to something you mentioned, which is your articulation of the Replet strategy because yeah,
*  some people believe that, you know, Replet is also way ahead of their revenue and that they will, you know,
*  eventually sell to Google or one of these major players at a really nice markup.
*  But I'm curious what you think the path is for them to be an independent, massive company.
*  Like what could that look like?
*  Just continued world-class execution at everything, you know, I mean, it's that which is not easy.
*  I wouldn't put that strategy forward for anyone who hadn't already demonstrated strong ability to actually make that work
*  because that's like, you know, I couldn't really go recommend that to Hugging Face.
*  You know, you know, what you guys need to do is just be the absolute best in all of your product execution always tough,
*  you know, and tough for Replet probably to sustain as well.
*  But I at least in using that product, I do feel like it is on the right track.
*  How high can they go up in terms of like real scale?
*  And I'm trying to suppose that some pretty impressive little demos and tests over the last couple of days just around auto scaling,
*  like his own personal website.
*  What happens if I send a quarter million requests at this Replet hosted site all at the same time?
*  You know, does it get overloaded?
*  Can it handle it?
*  I mean, obviously, I'm sure there's some limit, you know, that he hasn't where he may have hit a limit and didn't share that number.
*  But at some pretty impressive numbers, he's shown stuff that works like amazingly well.
*  People in the comments are just like, dude, that is sick.
*  You know, that level of execution, is it sustainable?
*  I mean, it's again, it's going to be hard to sustain, but they do make things so easy that.
*  I think where they can really crush it is in the sort of long tail of apps.
*  I doubt that they get to the point where, you know, major engineering projects that are like.
*  High scale, certainly that already exist would migrate to Replet.
*  What I think they can do is create something that is the best way to create,
*  which I think they're already right there at the top, you know, with something like cursor and copilot.
*  They have rivals, but they're right there at the top of like the best, easiest way to create.
*  Then they're also like the easiest way to just turn that into a live app by just kind of hitting publish, like amazing.
*  How much business they can retain as those like bazillions of small apps grow and mature.
*  Is probably the biggest question for how big that business can really grow.
*  Because if you get started on a platform and you don't have any pain points, you know, and the markup isn't that huge,
*  you're probably not switching from the platform, especially if it would like take a lot of work to switch into something else.
*  That's not, you know, nearly as user friendly.
*  So how far up that curve can they go where they're still like, hey, I'm not hitting any problems.
*  Cost seems, you know, pretty reasonable.
*  And I'm just happy to keep growing with Replet.
*  I would say that's going to be the key question.
*  They have this deployments product set that looks super promising for that and seems like it's, you know,
*  already probably pretty well there for kind of small to medium sized apps.
*  What will be really interesting to see is like.
*  If people start to and it will surely start to happen where.
*  What happens if you start to scale to millions of users on Replet?
*  Are they ready for that?
*  Is the cost profile such that they can keep you as a customer?
*  If so, you know, sky's the limit for them.
*  If they can't handle that, you know, then that puts a cap on how big the business can get,
*  I would think, and that's probably the number one thing that I imagine that they're trying to figure out how to do.
*  They've got the community.
*  They've got people building small stuff all the time.
*  You know, can they get people to build more ambitious stuff and can they keep those things as they really hit tipping points
*  into millions of users?
*  You know, I think they'll be in great shape.
*  Yeah, they also have a whole other thing too, which is like the dynamic.
*  I mean, that's that's conventional analysis.
*  Then the next kind of mind blowing analysis with Replet is they're working on the AI developer.
*  You know, again, it's a much more integrated product than anything you'll see from Hugging Face.
*  Hugging Face is not going to give you, you know, a single copilot like experience,
*  you know, for all of their community.
*  I don't see that on the horizon at all.
*  I would literally be shocked if all of a sudden that drops.
*  They have like some of this stuff, you know, where it's like talk to Hugging Face.
*  It will help you like figure out what the right models are for your use case.
*  But it's again, it's just so diffuse.
*  It's so kind of, you know, everything's changing all the time.
*  They don't have the like same focus on stuff like that.
*  It's all kind of more again, like like we talked about with Llama 2 last time, right?
*  They train it. They get to some publish point.
*  They release it, but they didn't really beat it up like iteratively over and over and over again.
*  That's kind of the vibe that, you know, even though like most kind of meta
*  conceptually interesting projects from Hugging Face seem to look like so far.
*  Whereas with Replet, you know, they're just absolutely lasered in on.
*  We want to make an AI developer.
*  We want it to be able to do stuff for you.
*  We want to be able to do more.
*  You know, we're going to chip away at that.
*  You're going to have this actual pair of programmer for you.
*  Then they've got this whole vision of around like a dynamic economy.
*  They've got the bounties.
*  You know, the bounties can be potentially served in some cases
*  by their AI developers in the future.
*  So there's a whole kind of I think they are set up to try to execute an economy on platform
*  in a way that Hugging Face is really not right now.
*  They have this kind of users can pay users to do stuff.
*  Users can pay AIs to do stuff.
*  Users could pay humans, which, you know, sub delegate to AIs to do stuff.
*  They have, you know, visions of AIs delegating to AIs to do stuff,
*  which is where it really starts to get crazy.
*  But it is all kind of coherent with this idea of we want to be the easiest way for you to build
*  and deploy stuff and, you know, we'll make whatever kind of dynamism
*  or commercial model underneath that is needed to support it.
*  They're not, you know, as ideological about any, you know, certain commitments.
*  And I think that does help them drive toward that execution.
*  Not to say that's all it takes.
*  Obviously, it takes a lot to execute at a super high level.
*  But that's at least one thing that I see kind of getting in the way for Hugging Face
*  that is not not there for a rep as much.
*  Another interesting story to they Hugging Face has been a while,
*  but they had a bloom, an open science project where they created like 175 billion parameter models
*  kind of, you know, analogous to GPT-3.
*  In some ways, it seemed like the point was to prove that an open source community could do this
*  and do it in an open way.
*  And they did.
*  But again, it doesn't really work that well, you know, even at the time,
*  it was like not nearly as good as GPT-3 and it was kind of like, hmm,
*  what is it that has been missing from this process?
*  It was like we brought a lot of people together.
*  We assembled a huge data set.
*  We like agreed on a bunch of decisions.
*  Honestly, pretty phenomenal achievement in terms of just like demonstrating that you can even pull off,
*  you know, a project like that by kind of an open consensus.
*  So like super cool, but didn't really pack the, you know,
*  the ultimate punch that its rivals did at the time.
*  And so mostly like it's kind of a footnote of like they did this thing.
*  It was interesting how they did it, but they didn't really prioritize performance,
*  you know, and they didn't really iterate.
*  And so it kind of became like an artifact that doesn't really have a lot of usage today,
*  you know, in contrast when Replets doing their own code models,
*  they're fine-tuning those models on their own data set, you know,
*  exactly how their platform is used.
*  And it's just a lot more integrated tightly kind of coupled,
*  which I think drives the performance, you know, that I'm talking about.
*  I thought this was a great overview in terms of like really assess,
*  you know, what makes hugging face interesting and what are some of the key questions and risks,
*  you know, looking forward in terms of as it tries to grow into its valuation
*  or perhaps more likely, you know, find the right buyer at the right price
*  if it's less likely it'll be an independent company.
*  Yeah, it'll be fascinating to find out.
*  I think just looking back at our perplexity Q&A thread
*  that we used to help collect some of the facts for this and some of the comparables.
*  I think it is interesting also to contrast against companies that have,
*  you know, also generated a lot of buzz.
*  So something like a runway, something like a character,
*  you know, these are products that people are wowed by.
*  My teammates at Weymark are creating the Frost 2
*  with whatever the latest model is from Runway and they rave about it.
*  You know, it allows them to do super cool stuff that they couldn't do previously.
*  Like we just couldn't make a film like this with the resources that we have
*  without this frontier model.
*  Similarly with character, I mean, people just love the experience.
*  They love going there.
*  The, you know, the creativity of all these different things that you can spin up.
*  Like it's an awesome very novel thing.
*  And, you know, it definitely has a certain kind of product market fit.
*  Those companies, you know, whatever they're valued at a billion ish or something.
*  I do think their position is in some ways even harder to defend
*  than the hugging face position.
*  If I was purely interested in financial return, I think I would,
*  you know, for all the difficulties that we've covered,
*  I think I would bet more on hugging face because it does have the community
*  and that is, you know, undeniably super valuable and discovery is valuable
*  and being, you know, a trusted source for curation is valuable.
*  In contrast, you know, a runway and a character,
*  you have to bet that they continue to be at the frontier of models right now
*  because that's the thing, you know, and what happens
*  if somebody comes out tomorrow with a strictly better model
*  that, you know, just does a better job of generating video clips
*  than Runway's latest model, you could see a dramatic drop in usage.
*  You know, if something really is strictly better,
*  the switching costs are almost zero.
*  You look back at what was the state of the art in image generation a year ago.
*  Well, we just passed the one year anniversary
*  of the original stable diffusion being released open source.
*  And so that was, you know, pretty much it at the time.
*  It was like Dali and it was that and obviously we've had an insane flourishing
*  of all sorts of different things since then.
*  But like nobody's really using that original stable diffusion.
*  It's been through like 10 generations since then and it's we've had like multiple handoffs,
*  you know, of kind of leapfrogs of oh look, you know, Dali, you know,
*  there's another Dali version that's improved and Adobe, you know,
*  Firefly is a thing and mid-journey continues to do a phenomenal job on their model,
*  you know, and has proven that they can maintain their position on the frontier.
*  But again, for all these companies, you know, the switching costs are extremely low.
*  The stickiness is extremely low and the sort of month,
*  maybe not the minute, but like the month that Adobe comes out with a
*  strictly better thing versus the runway is so easy to switch.
*  All the runway customers are already Adobe customers.
*  They all already have Adobe licenses.
*  So credit card is depending on what the business model is.
*  They might just start to get it for free as part of their existing purchase.
*  Maybe it becomes an add-on. But like again, the credit card is already on file.
*  So sticking this there is like super low.
*  I think in general this, you know, this whole discussion does kind of reflect that.
*  It's still not really that obvious like where in the AI stack like massive value is going to accrue
*  and you know, the sort of gravity of the incumbents, the infrastructure owners,
*  the ones that the hugging faces and the runways are built on, you know,
*  it seems like those end up capturing a lot of value here.
*  And it's got to be a stressful job right now to be like the model team at runway, right?
*  You're like, man, we've had a couple hits in a row and we've run that up to a billion dollar plus valuation
*  and like global, you know, minor fame certainly in the AI world global fame.
*  But that other competitor could drop anytime.
*  What's our timeline to get our next one out?
*  You know, what how do we how does it go if we get leapfrogged even for a little while?
*  You know, that's a tough position to defend.
*  And so, yeah, I would the relative valuation in hugging faces favor.
*  I don't think it's like crazy by any means.
*  It's just that, you know, even in their position where they do have so much going for them as,
*  you know, a real hub to use their word, you know, it is it still does seem like a very difficult hand to play strategically.
*  Totally. That's well put. Let's let's wrap on that.
*  It's great episode, Nathan. And until next time.
*  All right, cool. Thanks, Eric. It was a pleasure.
*  It is both energizing and enlightening to hear why people listen and learn what they value about the show.
*  So please don't hesitate to reach out via email at tcr at turpentine dot co.
*  Or you can DM me on the social media platform of your choice.
*  Omniki uses generative AI to enable you to launch hundreds of thousands of ad iterations that actually work customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it and I recommend you use it to use Cogrev to get a 10 percent discount.
