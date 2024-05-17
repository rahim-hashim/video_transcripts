---
Date Generated: April 02, 2024
Transcription Model: whisper medium 20231117
Length: 4910s
Video Keywords: []
Video Views: 968
Video Rating: None
---

# Synthetic Data with Alex Watson, Founder of Gretel AI
**Cognitive Revolution "How AI Changes Everything":** [November 14, 2023](https://www.youtube.com/watch?v=uX8RgKJXjdQ)
*  Your data is messy, it has gaps in it.
*  I can't create new additional examples,
*  it's too expensive or there's no way to go back to it.
*  We really focused our efforts on,
*  first and foremost, helping you build better data.
*  That's been the guiding light,
*  that's what we're really aiming for.
*  No LLM today can generate
*  a 100,000 or a million row dataset.
*  The first purpose of the agent was
*  interpreting that user query that's coming in,
*  and then figuring out how to divide it up into
*  a set of smaller problems that the LLM
*  can work on one problem at a time.
*  The promise of a really lightweight model,
*  really fast model,
*  shows the power that you can have of taking
*  a domain-specific dataset you have or task,
*  and doing something meaningful without having to
*  do something at the GPT-4 scale.
*  Hello and welcome to the Cognitive Revolution,
*  where we interview visionary researchers,
*  entrepreneurs, and builders working on
*  the frontier of artificial intelligence.
*  Each week, we'll explore their revolutionary ideas,
*  and together, we'll build a picture of how
*  AI technology will transform work,
*  life, and society in the coming years.
*  I'm Nathan Labenz, joined by my co-host, Eric Thornburg.
*  Hello, and welcome back to the Cognitive Revolution.
*  Today, my guest is Alex Watson,
*  founder and chief product officer at Gretel AI,
*  the synthetic data platform for developers.
*  Synthetic data is a fascinating topic.
*  Since the early days of deep learning,
*  it's been well-known that training computer vision models
*  on a mix of original and programmatically altered and
*  degraded images ultimately improves model performance.
*  It seems that learning the concepts through the noise
*  boosts robustness to the random unseen oddities
*  that models inevitably encounter in the wild.
*  More recently, dozens, maybe even hundreds of papers,
*  have explored how LLM-generated data
*  can be used to improve training sets and ultimately
*  model performance on a wide range of problems.
*  Yet at the same time, some research results and many
*  observers of the evolution of the internet in general
*  have cast doubt on just how much synthetic data
*  the system can absorb before models begin to lose touch
*  with their real-world origins or otherwise degrade.
*  With these questions in mind, I reached out to Alex,
*  who's been building a business on synthetic tabular data
*  generation since 2020, and who proved to be
*  an amazing guide to this domain.
*  While synthetic data might sound like a niche topic,
*  I think this conversation will be of general interest.
*  We started with a discussion of why we need synthetic data,
*  how Gretel has trained specialist models to maintain
*  realism while also preserving privacy in creating it,
*  and how we can be confident that we can trust this data
*  for analysis, testing, and yes, AI model training.
*  Along the way, we also explored the trade-offs
*  between statistical realism and social manners.
*  The impact of LLMs on Gretel's business
*  and the new pre-trained tabular LLM
*  that they've recently introduced to help create
*  synthetic data on a zero-shot basis for a wide range
*  of data types and scenarios.
*  We even took a detour into AI regulation in the wake
*  of the recent Biden White House executive order
*  and the UK AI Safety Summit.
*  This episode is a great example of why I love
*  making this show.
*  I learned a ton in the preparation and had a lot of fun
*  with the conversation, and I think you will too.
*  If so, I always appreciate it when listeners share the show
*  with their friends.
*  And of course, we invite your feedback via our email
*  at tcr at turpentine.co or via your favorite social network.
*  For now, I hope you enjoy this conversation
*  with Alex Watson of synthetic data company, Gretel AI.
*  Alex Watson, welcome to the Cognitive Revolution.
*  Appreciate it, thanks Nathan, excited to be here.
*  Yeah, this is gonna be great.
*  So you are the founder and now chief product officer
*  at this company, Gretel AI.
*  I love to hear how you come up with that name by the way.
*  What you guys do is synthetic data.
*  And I'm just so interested to learn so much more about it.
*  It's been really kind of eye opening to explore the product
*  a little bit.
*  You do some of the best live product demos
*  that I've seen your recent 12 minute YouTube short,
*  I thought was like really good.
*  I appreciate that, thanks.
*  I think there's gonna be a ton of fun.
*  So tell me where Gretel come from,
*  give me just a quick backstory.
*  And then let's talk about like,
*  why do we need synthetic data?
*  The original vision for Gretel was around a better way
*  to make data that we can't make accessible, accessible.
*  And it's evolved quite a bit,
*  like synthetic data has so much more kind of capabilities
*  and promises that we've discovered over the past
*  about three years of running our business.
*  But it was a reference to that,
*  like the digital breadcrumbs that we leave behind.
*  And really an effort from our company
*  with using synthetic data to make enabled data sharing
*  at a scale that hasn't been possible before.
*  Imagine hospitals sharing medical records,
*  research institutions, financial companies sharing data
*  in a way that doesn't compromise consumer privacy.
*  And that's really where we started.
*  So you'll see that those like,
*  as we kind of go through the technology we build
*  and talk about differentially private training
*  and things like that,
*  you'll see some of that come through in our product.
*  We've expanded that vision and that scope quite a bit,
*  but we really started around privacy
*  and around the idea of protecting individual privacy,
*  but enabling learning and data sharing at scale.
*  So the big two value drivers today,
*  obviously you kind of are starting,
*  the founding premise is privacy.
*  And now there's this kind of massive takeoff in AI
*  and so many people training stuff and trying to figure it out.
*  And so the other big use case that we're seeing
*  is improving the data that people are feeding
*  into their training processes.
*  So tell us a little bit about that one as well.
*  Yeah, maybe I'll maybe start with the history
*  of how it happened.
*  It actually happened like incredibly early in our company.
*  So for a brief history, prior to Gretel,
*  I was a co-founder of a startup, security startup
*  called Harvest AI.
*  We built products that help customers like scan
*  and detect important data in the cloud.
*  We ended up getting acquired by AWS in 2016.
*  We're going out for a series A raise
*  and got approached around launching that service
*  as an AWS service.
*  So I was a GM there for about four years for Amazon Macie,
*  which people used to scan AWS cloud for important data.
*  And saw that even the biggest, most cloud data
*  incredible data companies struggled
*  with enabling internal access to data.
*  So Pinterest of the world, Airbnb of the world
*  and things like that.
*  So you saw what a problem this was at scale.
*  And also the power of when you can make data accessible,
*  like AWS, we had at the time 500 person compliance team
*  that could work wonders for making data accessible.
*  So we've started out with that privacy thing.
*  And our first open source example, we released in 2020,
*  right, actually, I think about a week
*  before the pandemic hit.
*  And open source ability to essentially
*  we used a language model.
*  This is 2020.
*  So we weren't using transformers at the time.
*  We were using an LSTM where we had started to partner
*  with the Google TensorFlow team around technology called
*  DPSGD, which is enables you to train models
*  with differential privacy.
*  So you can make sure they won't memorize secrets.
*  But one of the early features that we had
*  was the ability just like we all do today
*  to prompt the machine learning model
*  and ask it to create something new.
*  So our first real experiment was saying,
*  can a language model like an LSTM,
*  instead of learning a language and text,
*  can it learn to recreate the distributions
*  inside of a data set?
*  So we really started focusing on tabular data around 2020.
*  And that can be mixed numeric, categorical, text, data,
*  anything in between.
*  And then we had the ability to prompt the model
*  where you could give it a subset of those features, right?
*  Given a zip code and a ethnicity and a date
*  to generate the rest of this record for me.
*  Very early in our journey.
*  I think the first time we had this was working
*  with some researchers at UCI,
*  so University of California Irvine.
*  And they were working with a rare disease data set
*  that was highly imbalanced, right?
*  So you have like thousands of patients,
*  but the only people inside that data set
*  that had the really rare disease were the tens to twenties.
*  So the question was,
*  can we address some of the representation bias here,
*  first of all?
*  So like essentially boost that minority class.
*  And if we do that,
*  can we improve the detection for this disease?
*  So essentially the idea is using synthetic data
*  to create additional kind of labeled examples
*  when they weren't able to go back
*  and recreate their experiment or their collection.
*  And can that data set be used
*  to improve downstream machine learning training?
*  So the idea is it introduces new examples
*  of learning the training data
*  and that'll help the machine learning model.
*  And we had a lot of success there.
*  And since that point,
*  I think we've seen more and more focus
*  and fast forwarding to today
*  and kind of happy to talk about where kind of
*  grow the list today and what we're seeing today,
*  but I'd say it's about 50-50.
*  One corner we have as a value driver,
*  safe sharing of synthetic data
*  where we can create data that has up to mathematically
*  provable privacy guarantees.
*  And the other area where we're saying,
*  hey, how do we improve on machine learning data sets?
*  And this can be tabular data for fraud detection,
*  for ad recommendation systems.
*  It can even be text data.
*  And there's such cool kind of research coming out recently
*  to support that where essentially using an LLM
*  to create additional like diverse examples,
*  like it was mentioned in the Microsoft 105 paper.
*  Yeah, there's a lot of connections here.
*  I mean, right off the bat,
*  I'm just thinking curriculum learning.
*  That's such a huge theme in my mind these days,
*  the ability to get smarter in terms of what data you feed
*  into even the pre-training stage
*  and enhancing, filtering, enhancing, curating, boosting,
*  so many different manipulations there.
*  But this one is probably one of the most
*  intuitively obvious where,
*  especially you think like rare diseases,
*  it's just not in there that much.
*  And that makes it hard for the gradient descent
*  to reinforce, to reward the learning of it.
*  So boost it up a little bit and next thing you know,
*  you're getting better performance.
*  I mean, so many opportunities like that.
*  And that's kind of what was the light bulbs
*  that were going off in my mind as just,
*  application builder today too.
*  I was like, boy, I see just so many quick patches
*  in my future of rare cases that I wanna handle better.
*  So I think that's super interesting.
*  Just going back to the Amazon thing as well for a second.
*  So basically this is,
*  cause I do love to kind of also contrast recent history,
*  approaches, you're scanning for important data.
*  Does that mean you're like,
*  I imagine the sort of five years ago version of that
*  was just a whole Swiss army knife
*  of different explicit techniques,
*  like regular expressions and like classifier,
*  kind of a handful of classifiers.
*  What did that thing look like?
*  And now today also I'm kind of like,
*  maybe I'd use Claude instant,
*  and kind of clean out a lot of that old code.
*  What do you think, is that a reasonable intuition?
*  Yeah, that's one of the reasons I am so immensely grateful
*  for the LLM technologies and transformers that are out,
*  is that there is a light at the tunnel
*  for people doing traditional NLP and NER
*  of a better, more general way to do it.
*  So really excited about that, but you're exactly right.
*  So going back to Macy,
*  they use a combination of traditional
*  like named identity recognition technologies,
*  as well as you were saying,
*  regular expressions and things like that
*  to help identify any type of personal data
*  that might exist in the cloud and label it
*  so you knew where it was.
*  And it would really take a look at it and say,
*  is this exposed to the internet?
*  Is this shared to outside organizations
*  and things like that?
*  And kind of give you the visibility
*  that you needed across your organization.
*  The real goal was to enable developers to make decisions
*  about what tools to use and use the best available tools,
*  but also get the enterprise visibility necessary
*  for that to happen.
*  I think the big challenges we faced doing this
*  in Amazon scale was we went from a startup
*  that had a couple of amazing customers
*  to the first week that we launched Macy,
*  we had 6,000 customers.
*  And we were doing named identity recognition
*  at up to petabyte scale.
*  So, so much time focused on how you make that
*  even traditional ML technologies kind of work at the scale.
*  Part of the reason I'm so excited about technologies today
*  is just the amount of specialization that was required
*  or tuning anytime your data characteristics changed
*  that were required.
*  And now it's really as much as all of us probably get annoyed
*  with the need to prompt tune and do things like that,
*  the promise of an LLM that can understand
*  your kind of natural language question
*  and make that change for you automatically
*  is really, really cool.
*  It's certainly a game changer in so many different respects.
*  Coming back to the present and the synthetic data,
*  as it's kind of unfolding today,
*  there are a number of use cases that you guys highlight
*  in your product and your demos.
*  I'd love to hear you kind of talk through a few more
*  beyond the boosting of the underrepresented set.
*  One that jumped back to me
*  and I think really highlights the challenge is insights.
*  The idea that, and I can just imagine,
*  I've done a lot of data analysis in my time,
*  and it's like, okay, I certainly hear why
*  at the corporate level, you don't want to be passing around
*  the crown jewel data set.
*  Did some work with Rocket Mortgage, for example,
*  and the care with which they maintain
*  their customer data, access to all that stuff.
*  It's a serious, serious effort,
*  so you can't just be passing stuff around like crazy.
*  That makes total sense, but then when you say,
*  okay, well, and super creative concept,
*  instead of having to deal with all that,
*  we'll just make fake stuff.
*  And use that instead.
*  But insights, I was like, okay, boy, insights.
*  I'm gonna need some real theory to start to trust
*  that you can make fake data that is enough like whatever,
*  and that's obviously something that probably most people
*  are gonna struggle to wrap their heads around.
*  Well, how do you kind of define that, prove that, whatever,
*  such that I can actually do my sort of pivot tables on this
*  and trust that what I'm getting is making any sense?
*  I've been thinking about that a lot,
*  and I've got some guesses, but I'm really interested
*  to hear more about the kind of,
*  the provability of how this stuff works.
*  Yeah, our approach, and I think the one that seems
*  to be gathering a fair amount of steam
*  in synthetic data world is to train a model,
*  and of course, we're like minimizing the loss function
*  as we're training it and doing the best we can,
*  but that doesn't tell you how that model's gonna capture
*  the real world distributions that you care about
*  and the ability to replay it.
*  So for us, regardless of the modality, if it's text,
*  if it's tabular, if it's time series,
*  it really starts with having the model kind of master
*  the ability to recreate data matching the same distribution
*  as the real world data was trained on.
*  And if you can have confidence in that,
*  you can start to alter the distribution
*  for whatever your task is.
*  So how we do that, we train the model at each iteration,
*  and really at the end, we sample a bunch of data
*  from the model, about a one-to-one equivalent
*  of the real world data, and then we essentially throw
*  from a statistical perspective,
*  throw the kitchen sink at it.
*  We have two ways of measuring,
*  one I would say is meant to be as objective as possible,
*  and the other is meant to be kind of task specific.
*  So we have something called our synthetic quality score,
*  what it's doing, it's easy to walk through
*  from a tabular perspective, we actually have similar scores
*  for text and time series as well,
*  but we sample a bunch of data from the model,
*  we look at pairwise correlations,
*  and that creates part of a composite score.
*  We look at the per field distribution,
*  we even do like PCA distributions for each field,
*  and then do a distance metric between the real world data
*  and the synthetic data.
*  And the idea is to give you a one through 100 score
*  that you can look at and you can reason about
*  and say, if this is above 80, we expect it to work well
*  for the types of machine learning use cases
*  that most people use synthetic data for,
*  if it's below that, maybe that works for your use case,
*  maybe your use case is just testing or something like that,
*  but as you were saying earlier,
*  you don't wanna create pivot tables on that.
*  So really we start with trying to give you
*  that sense of confidence.
*  We've added in the ability and really just after seeing
*  a lot of customers do this to automatically test
*  a downstream task for your data as well.
*  So after the model's done training,
*  we can run aggression or a classification task
*  or things like that automatically within our platform,
*  we have a lot of customers that use like Vertex
*  or SageMaker or things like that to run this as well.
*  So we just built it into the product,
*  so not everyone had to write code,
*  but I think a mixture of that somewhat completely objective,
*  not task specific score that is a good general indicator.
*  And then also that like understanding of your task,
*  like what you wanna do with the data
*  and making sure it conforms to those expectations
*  feels like the way to get that sense of confidence you need.
*  Hey, we'll continue our interview in a moment
*  after a word from our sponsors.
*  Real quick, what's the easiest choice you can make?
*  Taking the window instead of the middle seat,
*  outsourcing business tasks that you absolutely hate.
*  What about selling with Shopify?
*  Shopify is the global commerce platform
*  that helps you sell at every stage of your business.
*  Shopify powers 10% of all e-commerce in the US
*  and Shopify is the global force behind
*  Allbirds, Rothy's and Brooklyn and millions
*  of other entrepreneurs of every size across 175 countries.
*  Whether you're selling security systems
*  or marketing memory modules,
*  Shopify helps you sell everywhere
*  from their all-in-one e-commerce platform
*  to their in-person POS system.
*  Wherever and whatever you're selling,
*  Shopify has got you covered.
*  I've used it in the past at the companies I've founded
*  and when we launch merch here at Turpentine,
*  Shopify will be our go-to.
*  Shopify helps turn browsers into buyers
*  with the internet's best converting checkout
*  up to 36% better compared to other
*  leading commerce platforms.
*  And Shopify helps you sell more with less effort
*  thanks to Shopify Magic, your AI powered all-star.
*  With Shopify Magic, whip up captivating content
*  that converts from blog posts to product descriptions.
*  Generate instant FAQ answers.
*  Pick the perfect email send time.
*  Plus, Shopify Magic is free for every Shopify seller.
*  Businesses that grow, grow with Shopify.
*  Sign up for a $1 per month trial period
*  at Shopify.com slash Cognitive.
*  Go to Shopify.com slash Cognitive now
*  to grow your business no matter what stage you're in.
*  Shopify.com slash Cognitive.
*  Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
*  Yeah, interesting.
*  So could we unpack the kind of loss function
*  a little bit more?
*  Cause I'm kind of wondering about the relationship.
*  That's all pretty quantitative stuff, right?
*  It's a code base, ultimately, a sort of test suite
*  that you can execute on any data set that comes through
*  and sort of say, we're gonna characterize what you gave us
*  and then we're gonna characterize what we generated
*  and kind of show you that that hopefully lines up
*  distribution wise.
*  On the generation side, and it's important to probably
*  keep in mind for folks, cause we're also used to
*  one token at a time language models.
*  I'm very much thinking of your latest kind of
*  tab LLM that you demoed,
*  it might be worth kind of distinguishing too
*  between that latest thing and the sort of set of more
*  purpose specific models that you have.
*  But I'm kind of imagining for the new big one,
*  it seems like there is a really natural
*  and kind of an insightful thing here maybe for people
*  where there's like a decoupling of the prediction,
*  which is the distribution and then like sampling
*  from that distribution.
*  I think this is something that people maybe don't
*  conceptualize super rigorously, but like the task
*  that you have sort of helps me, I think at least
*  crystallize it a little bit.
*  So like most people have a general sense, right?
*  At the end of the language model,
*  you're putting a prediction onto every token.
*  And then you can, with your temperature setting,
*  this is the experience that people are most familiar with
*  if they're an AI engineer or whatever,
*  you can turn that temperature down to zero
*  and you can get like the most likely token
*  or you can turn that temperature up
*  and you can randomly select from those
*  probability distributions.
*  But in the kind of practical experience of it,
*  we really only see one token and in the training also,
*  there is like a ground truth text document,
*  that is kind of firing one on the actual token
*  and like zero on all the other tokens, right?
*  So it strikes me that your situation
*  is a bit different here where you can potentially
*  define the target as the distribution
*  and just like directly optimize and form the distribution
*  of the predictions to the distribution
*  that you've like characterized from the data.
*  And then the sampling from that becomes like,
*  you can kind of understand it in,
*  I mean, it's the same fundamental thing,
*  but the difference between that one token being right
*  and the, we want to generate the actual distribution
*  seems like something that was really helpful for me
*  to wrap my head around over the last couple of days.
*  That's probably a byproduct of starting
*  working with tabular data,
*  where that rather than looking at it
*  at a row being generated at time,
*  we were using a variety of models when we started.
*  We started with LSTM, we used GANs,
*  we used diffusion models and now as you mentioned
*  with our tabular LM model, we use transformers.
*  A byproduct of how we kind of built our product
*  is we end up looking at the row levels.
*  So every time a row of data is generated,
*  then we examine everything.
*  Similar if you're generating a sequence
*  of new LLM instructions, for example, right?
*  Rather than looking at the per token,
*  what we're gonna look at is the per line
*  or per record distribution.
*  So essentially we let the model generate everything.
*  The first step during training is we're sampling
*  and we're looking at it,
*  but also when you're using the model for inference.
*  So when you're asking the model for data to come out,
*  there is the risk that the model is gonna hallucinate
*  or invent something new that no one wants to have happen.
*  So we have a secondary level of validation.
*  We call them, not very creative, we call them validators,
*  but essentially what it's doing is it's looking
*  at all the outputs in the model
*  and asking how different it is versus the original data
*  that it was dropped that trained on.
*  And you have the ability to filter out things
*  that are too far outside of the distribution.
*  And the idea there with the tabular data
*  was to make sure that we didn't invent anybody's age
*  that was 135 inside of a dataset,
*  but it works really well for text data as well.
*  Just when the model kind of goes off on a rant
*  or invent something that's way outside
*  of what it should be working with,
*  you have the ability to filter that type of data out
*  and helps you have more confidence in a generative model
*  that it's gonna give a usable response.
*  Another kind of cool thing is that
*  with so much of the focus for synthetic data
*  really being on creating machine learning training sets,
*  you can't have someone kind of looking at every record
*  in a row and saying, yes, this is fine,
*  this isn't, this is fine, right?
*  So we've really focused on making sure
*  when we generate data at a thousand or a hundred thousand
*  records or even a million records
*  that you have confidence those records
*  are kind of match your expectation.
*  So I think that's another really kind of neat thing
*  that I see happening too.
*  Go back six months ago and there were so many questions
*  about I wanna use this model,
*  this LLM for summarizing content on Reddit
*  or things like that, right?
*  And the risk was that it would summarize something
*  that was off-base and would be an inaccurate summarization.
*  And I think technology is like what we built
*  for tech scoring.
*  There's been a few open source metrics
*  have been released recently,
*  really help you quickly check and reason
*  about a generative model's output
*  in a way that would allow you to serve the results
*  to customers without having to have necessarily
*  like a human look at it.
*  So a nice kind of quick AI check on data
*  makes these models like so much more usable.
*  How do you do the pre-training?
*  And how kind of big of a foundation model is this?
*  Again, I'm so fascinated with the tab LLM.
*  I'm kind of imagining that like you've gone out
*  and just assembled every public data set you can
*  and in a sense kind of taught a statistical world model
*  to this thing.
*  So it's supposed to have kind of all the right priors
*  basically, right?
*  How do you go about creating and kind of validating
*  that strong baseline?
*  Yeah, so for some background,
*  we are about to release for listeners here,
*  we're about to release a model.
*  We're calling it tab LLM or tabular LLM.
*  What it is is a agent planning and execution architecture
*  built to help people work with tabular data
*  using natural language queries.
*  And really at the core of that is both the agent
*  that is making a decision about whether to use an LLM
*  to generate data or whether to use one of our tools
*  to write code to generate data to serve your response.
*  What we're referring to here is the actual LLM model
*  that we have fine tuned on data sets
*  from across the internet.
*  So it's one of the first examples that you'll see
*  of an LLM that's meant to work with tabular data.
*  Tabular data can be text, time series, numerical,
*  categorical, any combination of those.
*  The approach we took, and I think this will be
*  a constant revolution from us,
*  the initial approach that we took
*  was exactly like you mentioned, Nathan.
*  It was crawl the internet, specifically crawl GitHub,
*  find any accessible data sets there,
*  Kaggle, things like that,
*  anything with an open source license.
*  One area we were particularly lucky with was,
*  I was noticing a lot of times like machine learning papers
*  will reference data sets actually in the README.
*  So there's really great data linked inside READMEs there
*  and we could pull down the license
*  and really kind of understand if it was usable or not.
*  But the idea was to train a LLM
*  that would be used for a data generation task
*  on what good data looks like.
*  And something interesting is that while we all kind of feel
*  that LLMs today are trained, it's mostly accurate,
*  on almost all of the content that are on the internet
*  if you're working with an OpenAI model
*  or a Palm or even a Lama model.
*  But these models really aren't trained largely yet
*  on tabular data.
*  And tabular data also introduces
*  some kind of interesting challenges
*  in the sense that when you look at the context window
*  that are available to LLMs today,
*  which is on a great LLM, let's say like 16,000, 16K tokens,
*  it doesn't translate into a lot of rows
*  in a typical tabular data set, right?
*  So 16,000 tokens, assuming 50 tokens per row
*  is gonna give you about like 350 rows.
*  So I think most of us at Grassley work with data sets
*  much bigger than that.
*  So one of the things that we noticed
*  as we started working with LLMs
*  and asking them to generate tabular data,
*  the power of asking an LLM to generate tabular data
*  is one, they are just by a byproduct of how they work,
*  really good with time series type data.
*  There's been some cool research about that recently.
*  Second, it allows you to apply like a global level
*  of knowledge to your data set.
*  So one thing I think that's really resonated
*  with our users on the platform is realizing
*  that your data set is awesome.
*  Everybody's data set is unique and really cool,
*  but it's also like in some way limited, right?
*  You don't have enough data.
*  You never have enough of the examples,
*  anything you were mentioning,
*  kind of the long tail of data that you deal with
*  and finding a more systematic way to work with it.
*  So the idea of applying a model that is seeing
*  most of the data sets on the internet to that problem
*  and saying, can you help me create some new
*  kind of meaningful variations in the data
*  to help a downstream model generalize is really powerful.
*  So that's where we started.
*  In the initial model, we haven't done
*  for the tablet limb model, we haven't done anything
*  like super clever with how to encode
*  or model numeric distributions.
*  Rather, we just treat everything as text
*  and it goes through there.
*  As I mentioned earlier, our first approach
*  was crawl the internet and train it on everything.
*  And I think very similar to other like research
*  and academic work we see right now,
*  I think a more curated, highly diverse set
*  of high quality examples is the way to go.
*  So we're seeing our team really kind of work on that.
*  And some of the opportunities here is that,
*  even the GBT fours of the world,
*  when they've seen tabular data sets,
*  it's usually a table on Wikipedia or something like that.
*  So it's a couple hundred rows at most.
*  They just haven't, the LLMs have not learned
*  that it's important sometimes that the relationships
*  across the data set might be thousands of rows
*  or hundreds of thousands of rows.
*  So that's a real kind of neat application
*  we're looking at right now is what if we train LLMs
*  on a much larger context length and much more data,
*  how good of a job they do learning the like the kind
*  of subtle insights and distributions of the data
*  that will help improve ML generation
*  when you're using that model.
*  Yeah, I bet quite a bit.
*  I'd love to hear a little bit more
*  about the agent kind of structure
*  because I'm imagining kind of, you said, okay,
*  you generate one row at a time.
*  For one thing, like the order really kind of matters there.
*  I wonder if you have a sort of systematic approach
*  to kind of reordering fields
*  because there's been some interesting research lately
*  that like, A implies B does not imply
*  that B implies A from the language models perspective.
*  And then I guess like there's sort of a kind
*  of sequential probabilistic evaluation
*  where you'd be saying, okay, if I'm,
*  once kind of at least some amount of pre-training
*  has been done, if I were to give you like the zip code
*  as the first field, then you would expect to see
*  like reasonable demographics back just based
*  on that zip code.
*  But then you'd sort of have, depending on the first variable
*  that you predicted, you would have like a very different
*  sort of conditional distribution for subsequent,
*  in all sorts of varying ways correlated variables.
*  So you're kind of doing like a little Markov almost process
*  randomly down the like Plinko board of possibility.
*  And then going back and evaluating each token
*  for its kind of conditional accuracy, right?
*  Or conditional like real representation.
*  Is that conceptually right?
*  Hey, we'll continue our interview in a moment
*  after a word from our sponsors.
*  AI might be the most important new computer technology ever.
*  It's storming every industry and literally billions
*  of dollars are being invested.
*  So buckle up.
*  The problem is that AI needs a lot of speed
*  and processing power.
*  So how do you compete without costs spiraling
*  out of control?
*  It's time to upgrade to the next generation of the cloud.
*  Oracle Cloud Infrastructure or OCI.
*  OCI is a single platform for your infrastructure,
*  database, application development and AI needs.
*  OCI has four to eight times the bandwidth of other clouds
*  offers one consistent price instead
*  of variable regional pricing.
*  And of course, nobody does data better than Oracle.
*  So now you can train your AI models at twice the speed
*  and less than half the cost of other clouds.
*  If you want to do more and spend less like Uber,
*  eight by eight and Databricks Mosaic,
*  take a free test drive of OCI at oracle.com slash cognitive.
*  That's oracle.com slash cognitive,
*  oracle.com slash cognitive.
*  If you're a startup founder or executive running
*  a growing business, you know that as you scale,
*  your systems break down and the cracks start to show.
*  If this resonates with you,
*  there are three numbers you need to know, 36,025 and one.
*  36,000, that's the number of businesses
*  which have upgraded to NetSuite by Oracle.
*  NetSuite is the number one cloud financial system
*  that can streamline accounting, financial management,
*  inventory, HR and more.
*  25, NetSuite turns 25 this year.
*  That's 25 years of helping businesses do more with less,
*  close their books in days, not weeks and drive down costs.
*  One, because your business is one of a kind,
*  so you get a customized solution for all your KPIs
*  in one efficient system with one source of truth.
*  Manage risk, get reliable forecasts and improve margins,
*  everything you need all in one place.
*  Right now, download NetSuite's popular KPI checklist
*  to give you consistently excellent performance,
*  absolutely free at netsuite.com slash cognitive.
*  That's netsuite.com slash cognitive
*  to get your own KPI checklist, netsuite.com slash cognitive.
*  One small modification I would make to that
*  is that we have found the more data you sample
*  from a transformer LLM based model for top of the data
*  up to the level that the LLM is capable of working with.
*  So let me give an example there, I'll start there first.
*  Let's say you're working with Lama2
*  or you're working with OpenAI
*  as a 16K context window model, right?
*  It might be capable of generating all that data,
*  but if it's never learned that more than a couple thousand
*  tokens are relevant to a data set,
*  you're gonna start to lose some efficiency
*  as it generates more and more data.
*  So what we do is we sample from our model
*  and our trained model up to as many tokens
*  as we can at a time, and then we evaluate it row by row.
*  And the purpose of the agent is realizing
*  that with current LLM technologies,
*  there's a couple purposes of the agent,
*  but the first one, the most obvious one is that,
*  no LLM today can generate a hundred thousand
*  or a million row data set,
*  or can go in and edit your data set,
*  which is a really popular use case for us right now, right?
*  If I want to add new fields,
*  if I wanna summarize product reviews,
*  if I even wanna just search for anomalies across my data,
*  we've gotta be able to process data way bigger
*  than what an LLM can handle in a single batch.
*  So the first purpose of the agent
*  really is to take a complex user query, for example,
*  create a demo data set with a spike in sales activity
*  in November, I want a million rows,
*  or if you're editing data,
*  convert this unit from Celsius to Fahrenheit
*  across my entire data warehouse or things like that.
*  The agent's first goal is interpreting that user query
*  that's coming in, and then figuring out how to divide it up
*  into a set of smaller problems
*  that the LLM can work on one problem at a time.
*  So a good analogy there would be if you asked,
*  in the NLP world, if you asked GPT-4 to write a book for you,
*  you would probably get a really short book
*  and you want a novel that's got several hundred pages.
*  If you were able to divide that up,
*  take that problem, what someone's asking for,
*  and divide it up into smaller problems,
*  like write a paragraph or a chapter at a time,
*  you could see how an agent
*  planning execute a base architecture that would say,
*  okay, first step, I need to write an introduction.
*  Next step, I've got to have character growth
*  and start to work on the character arc.
*  And finally, I need the conclusion and things like that,
*  and it can divide those up into smaller problems.
*  That's the approach we're taking with the data set,
*  either editing or data set creation,
*  where we've got something that is breaking it down
*  to a step-by-step problem that a smaller,
*  in this case, our data generation LLM can work with
*  and start generating data to high quality data
*  for that particular window.
*  So is that like a, it's more of kind of an instruct type
*  model that is creating kind of code as policy outputs,
*  and then a dedicated actual data point generation model
*  that is kind of receiving those commands
*  and doing the cell by cell.
*  Exactly.
*  That allows you to put language models into, right?
*  I mean, I saw one of the demos was like,
*  reviews of the product,
*  and obviously that's a pretty different situation
*  from the tabular data.
*  I assume that's kind of a little more random somehow,
*  or like, it seems like it would be kind of less,
*  harder to give a representativeness guarantee
*  on like customer reviews.
*  We've got some research, which I'll link over to you
*  on how we assess the quality of the text
*  based on what you're looking for.
*  But so often data sets are mixed.
*  Like imagine HR data where you've got doctor's notes
*  mixed with initial observations
*  from patients as they come in.
*  So I think that happens quite a bit.
*  So we try to learn across all of them.
*  And one of the kind of interesting things
*  is that you don't necessarily want your LLM
*  to do everything.
*  And that's maybe the other part
*  of the agent planning based architecture.
*  If you were asking for an incrementing ID
*  or a Fahrenheit conversion,
*  we've got a neat example where we're doing like a,
*  maybe a high school kind of like physics level problem.
*  The LLM will approximate,
*  but you don't want it to actually approximate your answers.
*  You want the real answer.
*  So the other part of, I think,
*  making synthetic data using this type of LLM work at scale
*  is having the LLM just recognize which areas are best
*  to calculate or compute
*  and doing that for you automatically.
*  I think we all see that a little bit.
*  If you're experimenting with GBT4 or chat GBT
*  and you ask it to help you work on a data set,
*  sometimes it'll give you a data set back.
*  Sometimes it will give you back code
*  that you could use to solve a problem.
*  And really that's the type of stuff
*  that we are trying to streamline.
*  We're essentially applying the agent to realize
*  when something should be a Fahrenheit
*  to Celsius conversion, right?
*  Just multiply by 0.6 and you get the right answer.
*  You don't have to have an L and figure that out.
*  So the first step is look at that user query, figure out,
*  given the available tools that I have,
*  can I solve this problem with code?
*  If so, execute that code, get that into the data set
*  so you have high confidence in the answer.
*  But for other things that require that kind of like
*  level of knowledge or intuition that an LM would have,
*  summarize this review as positive or negative,
*  things like that that require you to look across fields
*  and understand natural language text
*  and then we use the LM to fill in that data.
*  It comes together very nicely, I think in the product demo.
*  I'm definitely excited to spend a little more time with it.
*  I do think it'll be really helpful.
*  And it's probably a good idea also
*  to just kind of contrast this as you started to do
*  trying to use GPT-4 or certainly any of the RLHF models,
*  I think you have just like very fundamental problems here.
*  And that's kind of where, even for a project like mine.
*  So where I'm thinking of applying this immediately is,
*  we have the script writing model and its job is to write
*  a video script for a given user who comes to us,
*  often naively and we kind of grab some content
*  off their website or whatever and figure out who they are.
*  So it's extremely, extremely diverse.
*  And you might say like extremely sparse, right?
*  We have like a healthy usage, but we're not that big.
*  It's a big world out there.
*  So especially internationally now, different languages,
*  just kind of all sorts of long tail stuff
*  that we have not previously put into our data set,
*  but can at any time kind of come our way.
*  And then I think like, okay, if I wanna do some patching
*  of my fine tuned 3.5, which is my kind of currently,
*  the state of the art best thing that can best nail our task,
*  then like one is probably not quite enough to get it
*  to really learn the pattern I want it to learn.
*  Five to 10 in my like broader mix of a few hundred samples
*  probably is, but I kind of wanna create something,
*  first of all, especially if it's an unfamiliar area,
*  it's like very hard to even know what to do, right?
*  You show some examples where it's like France,
*  and I'm like, oh God, I didn't even know the fucking,
*  excuse my language, excuse my French.
*  I didn't even know the like structure
*  of the postal system in France,
*  let alone how to like make semi realistic examples
*  that I would want to throw into 3.5 fine tuning.
*  So if I'm like making this up totally on my own,
*  just seem destined for underperformance
*  for just kind of garbage in problems.
*  And then, if I ask GPT-4, I'm just like,
*  it's gonna be so RLHF to mode collapse
*  on things like this so often that,
*  just like it answers 42 or whatever,
*  or 97 like way too many percentage of the time
*  when you ask for random number,
*  here I just like don't trust it at all
*  for that sort of kind of representativeness.
*  And I think over there, I would readily agree that like,
*  yeah, you should not use it for that.
*  Obviously it's been trained for a very different purpose.
*  So that to me is exciting,
*  I think gives you guys a real different like position
*  in the market that is so distinct
*  from the kind of mainline AI assistance.
*  I think that's pretty cool.
*  The flip side of RLHF, which I think is so interesting,
*  we've done some initial work that we published
*  on using RLHF to reduce the models kind of propensity
*  to talk about stuff that it shouldn't like initially.
*  So particularly like don't return PII and data
*  in course the model, which is a big enterprise use case.
*  But I think what you talked about also is like,
*  sometimes you want that, sometimes you need it.
*  We have customers, for example, that are generating,
*  no joke here, they're generating spear phishing emails
*  to test their own spear phishing detection system.
*  So there are times that you need to go against
*  what the model has been trained to do.
*  And another interesting piece that came into mind
*  when you're talking about RLHF.
*  So I think like the enterprise use cases
*  are a little different than consumer,
*  where in some cases like you need the ability
*  to turn off some of the guardrails
*  because you need to create a level of diversity
*  or talk about things that a RLHF model
*  probably just doesn't wanna talk about.
*  Big use case for us, I'll give you another example,
*  would be healthcare companies, right?
*  That are looking to create synthetic versions
*  of patient medical records.
*  And a lot of models when you're trying
*  to augment your examples,
*  will just refuse to do it
*  because they think you're talking about
*  something that could be potentially harmful
*  that's really being used for a good use case.
*  So I think there is definitely a case for times
*  where you wanna take off some of the guardrails
*  or the set of expectations that organizations might have
*  are just much different than what,
*  or teams, developers might have are much different
*  than what a consumer might have
*  if they're using chat GPT or something like that.
*  One that I think is so cool that really,
*  you really start to notice with tabular data.
*  Big application and it's the most basic thing
*  that we would see with synthetic data,
*  but people always start generating that mock data set
*  they've had to generate for a demo
*  or for their UI or something like that.
*  And inside that data set, you're gonna have names,
*  you're gonna have addresses and things like that.
*  And genders, things like that,
*  protected class type stuff.
*  And what you'll notice is the models have a tendency
*  to return like one type of data.
*  So you've got names that seem very consistent,
*  you have probably represented the training set,
*  demographics that are across the United States
*  or things like that.
*  One cool application of RLHF that we've done
*  and we've been experimenting with
*  is actually training the model to be more diverse
*  in the results that it gives back.
*  So if I ask for a set of demographics
*  for a particular zip code or city or things like that,
*  having the model want to return a more diverse
*  and kind of aligned set of demographics,
*  then I think then what a model might do off the shelf
*  is pretty powerful,
*  but you want the ability to be able to control that.
*  Sometimes you want real data,
*  sometimes you want ethically aligned data,
*  those are both really important.
*  I think the irony of the whole thing is RLHF
*  can be really good for both of them.
*  It's just like what direction, it's a tool, right?
*  And it's kind of what direction you point the algorithm
*  and the loss function at solving.
*  This goes back to my kind of decoupling
*  of the distribution prediction and then the sampling from it.
*  It seems like you could achieve that largely
*  with just temperature.
*  Like if you said, we're gonna make our,
*  under the core model and its logits or percentage weights,
*  outputs as true to real world data as we can,
*  then you could slide your temperature slider from zero
*  and be like, at zero, you get the modal prediction
*  and at one or whatever, you get the sort of normal,
*  representative, the real world distribution.
*  And then at two, you get like the minorities
*  overrepresented on any and all dimensions version.
*  But it seems like you're approaching that in a different way.
*  So is what I'm saying like not workable for some reason?
*  And why is there more complexity?
*  Even a temperature distribution when you're editing it
*  is going to, when you turn it up relatively high
*  and you start to get into even kind of crazy data
*  for a really imbalanced data set,
*  even then the temperature isn't gonna introduce something
*  that is like 1% of data very often,
*  or at least to the level that you're wanting it to.
*  So this is a technique we can use
*  to kind of force that to happen.
*  This kind of reinforcement learning is really a tool
*  for saying, we really want you to be,
*  to create a more diverse representative data set.
*  This is like the stock photography thing
*  where it's like, we're gonna be intentional about this,
*  but to do that, you have to apply even more
*  than a standard technique.
*  I love their engineering blog at Pinterest
*  and they had a really neat example
*  on how the search results.
*  For example, if you're searching for pictures
*  of wedding rings, would bring back a picture of wedding ring
*  with like very diverse skin colors or things like that,
*  which I think is a nice feature to have.
*  Once again, you don't always want that.
*  Often what I found particularly in the machine learning
*  or the kind of the tabular data space
*  is that the classes are incredibly imbalanced.
*  Then give you another example, even for things at scale,
*  so we work with a major social media company.
*  They were impacted just like everybody else
*  by the kind of changes to the ad,
*  third party ad tracking and things like that.
*  So really, they're trying to make the best possible use
*  out of their data that they have.
*  And when you look at the ad recommendation problem,
*  it's massively imbalanced.
*  For every thousand people that you present an ad to,
*  maybe one or two click.
*  Hopefully better than that,
*  but often that's I think the kind of case
*  that you're looking for.
*  So you're trying to make the absolute most out of that data,
*  but that data represents 0.01.
*  In that range, I'm making these numbers up,
*  but it's meant to be illustrative of the data.
*  So you need the ability to tell the model,
*  this is really important.
*  I wanna learn from these particular features,
*  this very kind of imbalanced class,
*  and then generate meaningful new variations
*  to improve detection with this.
*  And so that's where I'm coming from
*  for the different very strong techniques
*  outside of like altering temperature,
*  where you want very explicit control over the model output
*  to make sure it meets your expectation,
*  because you've got a task at hand.
*  Well, control over models is definitely
*  something we should all be striving for.
*  So in all aspects of AI,
*  definitely in the big picture kind of worries about,
*  are we gonna keep this whole AI technology wave
*  under control in any number of ways?
*  I think your situation here
*  is one of the more compelling things I've ever heard also
*  for the need for kind of the raw model,
*  that has the more accurate world model,
*  even if it is sometimes not so pretty to look at.
*  So I wonder how you,
*  and I'm not like super bent out of shape about these issues,
*  but I guess a lot of times I kind of view
*  the model developer's ability to control things
*  as kind of a canary in the coal mine.
*  Like if they can't prevent it from like being offensive today,
*  are they gonna prevent it from falling,
*  build a bioweapon command?
*  Tomorrow is kind of the most
*  credibly alarming scenario, I think.
*  But this is definitely,
*  I certainly see your point about like,
*  hey, we wanna have all these different dimensions
*  of control and we've got,
*  even just to build stuff to test our detection systems,
*  we gotta have data that's gonna set off alarms, right?
*  So that is all super interesting.
*  I wonder what role does like
*  kind of conventional AI ethics have in the company,
*  given all these use cases that you wanna enable?
*  Have a very optimistic view of AI,
*  and I think a lot of times I view synthetic data as a tool
*  that could be used to improve like the alignment
*  or the ethics by someone that wanted to do it.
*  I think to your point,
*  it could also be used to do stuff that's harmful, right?
*  So I think that's a real question that we're gonna be,
*  kind of wrestling with as a community
*  over the next couple of years.
*  I'm a big fan of having the alignment checks
*  and the warning flags everywhere,
*  but to the extent possible,
*  giving people control over what the model does.
*  And generally speaking,
*  I'm curious to hear your opinion on this one as well too.
*  I think I'm more of a fan of the open model
*  where it can be kind of adapted
*  for whatever particular use case that you might have,
*  versus moving to a more kind of closed space
*  where a very small group of very powerful companies
*  have control over what the models can and can't return.
*  So there is no perfect answer there,
*  but I would say like,
*  I wanna believe that people wanna do the right thing.
*  AI is advancing so incredibly fast that,
*  from what we're seeing,
*  I think that, for example,
*  the White House executive order that came out this week,
*  is it is a sign that people are paying attention
*  to the right things.
*  I'm also, maybe this is a byproduct
*  of being one of the smaller companies out there.
*  We've got about 65 people at Grotto right now.
*  I'm curious to see how regulation will kind of play
*  into this world,
*  where smaller companies that are innovating
*  may not have a hundred people on a regulatory
*  or compliance team to help work on this yet.
*  So love the direction.
*  I think something really important that we do
*  as we kind of move forward is thinking about
*  enabling competition and things like that,
*  and enabling innovation,
*  while protecting people's privacy,
*  while protecting the use of AI across our ecosystem.
*  Yeah, no simple answers on all that.
*  And the 100 plus page order,
*  that seems to mostly be ordering another 10,000 plus pages
*  of reports is certainly reflective of that.
*  I mean, I also thought it was a pretty good first step.
*  And at the highest level,
*  I've been kind of saying a lot lately that,
*  as someone who does take kind of big picture AI risks
*  pretty seriously,
*  it's hard for me to imagine a much better situation
*  for the kind of overall game board to be in today
*  than the one we actually have.
*  At a minimum, we can say all the people at the big companies
*  that are developing the most powerful systems
*  are like pretty serious minded.
*  And the most kind of rogue one is meta.
*  And they're still like,
*  more responsible than you could easily imagine people being
*  if they were just like,
*  didn't care or thought the whole thing was totally ridiculous.
*  So I think that's all pretty good start.
*  I like the flop thing pretty well.
*  I mean, I'm imagining that you're like,
*  you had said 500 billion tokens, right?
*  As the pre-training base.
*  So I mean, if my Intel is correct,
*  GPT-4 is 10 trillion tokens.
*  So kind of 20 times as many tokens,
*  however many more parameters,
*  it feels like you probably have three orders of magnitude
*  between kind of what your compute budget was for this
*  and where even just the reporting threshold would kick in.
*  So it seems like you have plenty of room to run
*  as a small company before you would hit
*  any onerous regulation.
*  And that's one of the neat things is,
*  I think that we don't have to
*  and we're not trying to compete with GPT-4
*  to create a tidal data model at that scale.
*  I think that the promise of,
*  for other people that are building
*  AI powered applications right now,
*  the promise of a really lightweight model,
*  really fast model, at Microsoft's textbooks,
*  all you need paper using like a 1 billion parameter model
*  that is super fast on inference,
*  super low on training costs,
*  trained on a relatively diverse but small set of examples,
*  like shows the power that you can have
*  of taking a domain specific data set you have or task
*  and then doing something meaningful
*  without having to do something at the GPT-4 scale.
*  So personally, like so, you know,
*  excited about that because I think it's gonna enable
*  innovation from the, you know, life sciences companies,
*  from FinTech companies, you know, you name it,
*  AI video content creation companies, things like that,
*  that can create small, efficient, fast models
*  that do something really cool and really unique
*  that the big models haven't, you know,
*  so personally excited about that.
*  And then the combination of those two,
*  like still leverage that big model where you need it,
*  is, you know, like we use it for the intent parsing,
*  really understanding what type of query a user wants.
*  Then we use our small model for speed.
*  I'm excited about that because I think it enables
*  people to experiment without needing, as you were saying,
*  like, you know, to train on, you know,
*  10 trillion tokens or something like just so big
*  that it becomes a barrier to entry.
*  Yeah, I think if we give it a little time,
*  you know, there are some really positive natural trends
*  because, and there, you know, there are some ways
*  where kind of everybody's interests can be aligned.
*  I'm, you know, generally speaking,
*  the systems that worry me the most
*  are the super general ones.
*  Things that are designed and, you know, engineered
*  for kind of narrow purpose seem inherently just, you know,
*  a lot easier to keep under control because like,
*  you know, Alpha Fold may be, you know, a world changer,
*  but, you know, up until at least this week, you know,
*  I think it does a couple things now,
*  but it previously did, you know, kind of one main thing
*  and that's, you know, predictive protein structure
*  and you got to fit that into a broader system.
*  You know, lots of awesome examples like that.
*  You know, Alpha Go can play Go better than any human,
*  but that's all it does.
*  So I think that's all really good.
*  And, you know, there is kind of a vision
*  for long-term AI safety that's kind of like the ecology
*  of small models that I think Eric Drexler was, you know,
*  has a manuscript on this.
*  He calls comprehensive AI services
*  that is like a good early articulation of it.
*  Kind of pretty prescient actually,
*  given, you know, it's like five years old, I think already.
*  And his idea is just that
*  let's have narrow superhuman AI in everything.
*  And then we don't necessarily need, you know,
*  superhuman general AI,
*  which might be hard for us to control.
*  But right now we're just like still figuring out
*  all these techniques and how to make things work
*  and like what the curriculum is supposed to be
*  and what the learning dynamics are.
*  And the one thing that kind of is working,
*  you know, without question,
*  I mean, a lot of things are working without question,
*  but, you know, it's so tempting in the meantime to be like,
*  well, why don't we go, you know,
*  what happens at 10 to the 27, 10 to the 28, 10 to the 29?
*  And there I'm like, you know,
*  I actually would like to see us be a little bit more cautious
*  before we, you know, just race through like
*  how many more orders of magnitude.
*  Cause I have no idea, you know,
*  really what comes out the other end of, you know,
*  10 to the 30 at this point, you know, all bets feel off.
*  Does that feel safe to you?
*  I mean, if somebody were to come today and be like,
*  hey, great news, everybody.
*  You know, all my H100s just warmed up
*  and we're going 10 to the 30 right now.
*  You know, we'll see in a hundred days
*  with my 50,000 H100 cluster, it should take, you know,
*  a hundred or probably a little more than that
*  to go 10 to the 30, but you know, whatever.
*  I don't think there's any way
*  to stop someone from doing that.
*  Well, you are working at like small city size
*  electricity consumption at that point.
*  So I mean, that is the kind of thing
*  that the state can currently intervene on.
*  There may be algorithmic breakthroughs in the future
*  that make, you know, that sort of impossible to,
*  you know, to stop, but.
*  Well, getting a little bit meta here,
*  maybe just kind of talking a little bit of theory.
*  It feels like these advances we made
*  have really been kind of like modeling
*  how the human brain works.
*  And that's neural networks, right?
*  At a go and at some point nature stopped saying
*  we should have a bigger and bigger brain
*  and started to say, we're gonna start like having parts
*  of your brain that are specialized for certain things.
*  So that's where like, I don't think there's anything
*  we can do to stop someone from training
*  something on every, you know, token that can be found
*  across the entire internet.
*  But I actually think this idea of
*  there is a quantity of smart enough
*  where for general reasoning, you've got good stuff there.
*  And then it's still like the task specific,
*  the code generation, you know, LLMs
*  or the synthetic data generation LLMs
*  or, you know, generation for Alpha Fold,
*  like what they're doing like that,
*  like a task specific model that is really great
*  at what it does as a tool that's available to the others
*  that both, I think kind of helps us reason a little bit
*  about more what's going on in a way we couldn't do
*  if the model got bigger.
*  But I also kind of believe is actually probably a smarter
*  and more efficient way to build out that AGI.
*  So I would see like the, you know,
*  personally see the future as hopefully, you know,
*  cause I like the idea of the auditability
*  and the understandability of these small kind of expert
*  models of a world where you've got a lot of models
*  that are trained on small amounts of domain specific,
*  really special data and then orchestrated by a larger,
*  you know, smart enough LLM without creating
*  the Uber intelligence that no one understands how it works.
*  Curious how you've thought about this as well.
*  Yeah, I think largely similarly with maybe just a little more
*  tinge of fear in my, you know, in my affect, but yeah,
*  you know, safety and narrowness, again,
*  I think is super important.
*  It would be, I see a case, you know, I guess to,
*  if I were to, you know, try to summarize the case there,
*  it would be like beyond a certain point,
*  scaling isn't necessarily economical anymore
*  because you're good enough, you know,
*  to do a good job at tasks.
*  And, you know, that's kind of what needs to exist.
*  There I do, now I kind of want to revise
*  maybe my earlier statement on like being, you know,
*  pumped about the state of the game board.
*  Cause I do think we look at some of the leading developers
*  and it's like, there isn't a, in some of them, you know,
*  one maybe in particular, there is a sort of
*  borderline ideological, you know,
*  sense that like we're going to keep scaling
*  and we're going to make something like,
*  that's like the most powerful thing we can make, you know,
*  and we're going to try to do it safely,
*  but like we are going to make the most powerful thing
*  we can make, seems to be kind of a prevailing notion.
*  And I'm like, that is the part that doesn't seem super wise
*  to me and it does seem like the kind of thing
*  that the state can do at least something
*  to control for a while.
*  So I would, I would again,
*  like to see a little caution there,
*  but I'm, it's funny.
*  I just did an episode today with my friend,
*  the CEO of Lindy and we were kind of running down
*  all the places and ways in which we are both EAC,
*  which are many, you know,
*  and then there's like just this one little corner of the,
*  you know, the world where we're like, yeah, maybe
*  let's not rush to 10 to the 30, you know,
*  not knowing what kind of alien pops out
*  the other end of that.
*  But I think this is, you know,
*  I really appreciate your perspective.
*  It is, it is so interesting.
*  You have just such a, such a different kind of angle
*  on so many of these kinds of core fundamentals.
*  I'd love to hear how that plays out for you
*  in terms of your sense of understanding
*  on the part of the language models.
*  You know, you've got the stochastic paradigm, obviously.
*  You've got the reasoning engine, characterization.
*  What do you make of that?
*  You know, as somebody who's kind of focused much more
*  on the representativeness side of the challenge.
*  Our number one focus as we've built out our service is,
*  and I think it's helped keep us kind of grounded
*  is helping data scientists, developers
*  with the problems they have with data today.
*  Your data is messy.
*  It has gaps in it.
*  I can't create new additional examples.
*  It's too expensive or there's no way to go back to it.
*  So we really focused our efforts on first and foremost,
*  like helping you build better data.
*  That better data is either more accurate
*  or it's more private than the existing data.
*  That's been the kind of the guiding light.
*  That's what we're really aiming for out of the gate
*  and learning as we go.
*  One of the areas we're about to release
*  a very early version of our service
*  and to see and really learn from users
*  for what they're able to share and feedback with us
*  for how they use it and use that to guide development.
*  So instead of starting making a set of assumptions
*  that prove it to be incorrect,
*  I think one of the areas that we've been successful
*  as a startup is like getting code out there really fast,
*  getting examples out there people can iterate with,
*  asking for feedback and iterating on that feedback.
*  So I'm super curious to see where this use of generative AI
*  for working with our big focus here
*  is working with tabular or mixed modality,
*  tabular text and time series data goes.
*  We'll use that to drive our own investments
*  on how much time do we spend working on a better agent,
*  for example, so a better agent tooling.
*  If you wanted to create a time series
*  or something like that at the scale of a million rows,
*  like how do you take in our knowledge
*  around building time series that works
*  and then combine it with the other technologies.
*  And where we see it being successful,
*  that's where we're gonna double down.
*  One of the areas I feel is so kind of neat
*  and de-risking in this space right now
*  is there are so many potential tools
*  you can bring to the problem,
*  whether it's retrieval augmented generation,
*  so bringing in example data sets
*  into the element memory just to help it,
*  whether it's kind of the React or the agent approaches
*  for breaking things down into smaller problems
*  and the element training itself.
*  So we've got a bunch of different dials
*  we can use to solve the problem.
*  We're hoping to learn from how people use the service
*  and see which areas we really need to double down on.
*  But I'm psyched for that.
*  I think in the sense that I really don't,
*  I have some ideas on where it's gonna go,
*  but I don't really know where things are gonna go.
*  But this, think about tabular data as a resource
*  and how much of the data we work with every day
*  is like organizations is in some sort of tabular format.
*  It's pretty unique space to be in.
*  I'd say most organizations, like 80, 85% of data
*  in some levels in some sort of structured,
*  semi-structured format.
*  So being able to work with that and leverage it
*  is a kind of a niche, but really cool space
*  to be playing in right now.
*  And to your point earlier,
*  I'm sure it'll be just about our time
*  until we've got competition from the other open AIs
*  of the world, the anthropics of the world
*  and things like that.
*  But right now, we've got a great set of users
*  we've been building on it.
*  And I think this kind of combined approach
*  across advancing LLMs to the point we need them to do
*  without trying to build the Uber LLM.
*  And then also combining other cool technologies
*  that are happening in our space to solve a problem
*  is working out pretty well.
*  Yeah, it kind of strikes me that there's maybe another
*  Pareto curve between these two modalities.
*  I'm trying to find a synthesis
*  for the stochastic pair reasoning engine debate.
*  And in your architecture, I'm sort of seeing maybe
*  they can be both.
*  You very much are training the core LLM here
*  that generates the data to be like a stochastic pair
*  in a sort of highly principled way.
*  But nevertheless, you want that randomness, right?
*  That's kind of a big part of the value driver.
*  And then you also need this planner
*  that has to be much more reliable.
*  And probably a lot of the models we use today
*  are kind of at some sort of outer part of the curve
*  on the production possibility frontier.
*  But maybe there's like a bifurcation that happens there too,
*  where you're really pioneering the sort of
*  high integrity stochastic pair side.
*  And then other people are really pushing
*  the reasoning side.
*  That's such an interesting idea.
*  And it kind of mimics, we went to a conference.
*  There's a major health organization called HL7
*  and they have a FHIR, it's called FHIR.
*  It's the most popular medical data record format
*  in existence today.
*  And they ran a whole conference on synthetic data.
*  And the feedback we heard at that conference
*  was the exact opposite of probably every customer
*  conversation I've ever had, but it was so interesting.
*  In the synthetic data world for healthcare,
*  there's a few projects, there's an open source project
*  called from MITRE called Cynthia
*  that allows you to generate medical format record data
*  that you can use for testing systems and things like that
*  in the healthcare space.
*  It's been under development for like four or five years,
*  purely statistical based approach.
*  And what they called out was that for many of the use cases
*  that they want, particularly around AI or machine learning,
*  that data from Cynthia is just too clean.
*  And I had never heard in my entire professional career
*  up until this point, but what they were saying is like,
*  you do want a little bit of that variability.
*  You want that slight variation that stochasticity
*  that gets introduced, but you don't want crazy, right?
*  So it really is about kind of finding that balance,
*  like just enough within the scope that you need.
*  And then also thinking about it at scale, right?
*  And you can't evaluate these things one at a time.
*  You need to be able to reason about 50,000 examples
*  you create for an LLM training set or a million examples
*  you create to boost a ad recommendation data set,
*  something like that.
*  So you really have to think about it at scale.
*  And that's just been starting with tabular data
*  where it's so easy to look at it and say,
*  this is right or this is wrong.
*  I think is maybe had us thinking about this as a company
*  a little bit earlier than the rest of the industry
*  that is now like, wow, we can generate really amazing texts
*  or images for the community training machine learning
*  pipeline, but how do we know that all thousand images
*  that I created are kind of meet my expectations?
*  So I personally really liked this idea of letting an LLM
*  be an LLM, like let a machine learning neural network
*  generate whatever it wants to,
*  but then examine the outputs at each step
*  and build some controls.
*  And if it goes too far off the reservation
*  and turn the temperature up too high,
*  something doesn't make sense anymore through real world data.
*  You can detect it and kind of filter it out.
*  That kind of recalls how in a lot of like image tasks,
*  there's kind of training on systematic corruptions
*  of the image as well.
*  Like you wanna make your stuff robust,
*  you add a little noise here and you kind of distort this way
*  and change aspect ratio.
*  And if it can work across all those different things,
*  then you're gonna be much better off
*  in a real world situation.
*  And there's kind of a similar problem, I'm sure,
*  for a lot of like medical things where stuff is whatever,
*  anything from illegible to incomplete to contradictory
*  to I just saw a funny story about like a person
*  who had the same name and birthdate
*  in the same hospital as another person
*  and like spent their whole life trying to be
*  disambiguated and like struggles.
*  So yeah, I mean, it's just so many
*  kind of crazy things out there.
*  I know we don't have too much time left
*  and I've really enjoyed kind of the digressions
*  in this conversation.
*  I did wanna ask a little bit more about
*  how you go about kind of training
*  for privacy protection specifically.
*  We've talked a lot about how you train for representation
*  and super representation, but I understand
*  there's like probably a whole different technique
*  for just making sure that like you don't spit out
*  somebody's real email address or whatever.
*  That is interesting.
*  When I find to, one of the experiment I ran,
*  maybe can help me understand this a little bit better.
*  This has been a topic of discussion lately too,
*  is I ran an experiment on OpenAI fine tuning
*  with a bunch of my writing,
*  and kind of my resume, my data, whatever.
*  And I was like, and I need to do it again with 3.5.
*  This is a little while ago,
*  but it was the 002 generation of fine tuning,
*  which they never launched publicly,
*  but I had like an opportunity to test a version of it.
*  And anyway, it kind of like sort of moved in my direction.
*  It did not know who I was though.
*  It was, I was like trying to turn up the epochs a bunch
*  and it's still like never learned
*  that it was supposed to answer as like,
*  I am Nathan Levens.
*  It was like Nathan something else sometimes,
*  and it was kind of vaguely similar to me,
*  but definitely not like memorizing those facts.
*  So I'm very confused about kind of memorization in general.
*  Jeremy Howard recently had a thing
*  where it's like the LLMs can memorize from one example.
*  It definitely hasn't been my experience.
*  So maybe for kind of background,
*  like what do you observe about this sort of LLM memorization?
*  In my case, I was trying to get us to do it.
*  You're trying to prevent it, but what is happening there?
*  And then, what's the technique that you're using
*  to really make sure that it's not happening
*  for your product?
*  Where we started was training language models
*  from random weights on a data set from a customer, right?
*  In that sense, the model learns from the data that it sees,
*  and it has a very high propensity
*  to memorize and replace secrets in data.
*  There was a great paper that came out,
*  and this is like towards the beginning of our company in 2020,
*  came out from Cal Berkeley called
*  the Secret Share Paper.
*  Don Song's team and several others kind of working on it.
*  And what they were highlighting was that,
*  Kevin training a language model on a data,
*  like how quickly it starts to memorize,
*  even rare occurrences in the data
*  and the chance it'll play it back.
*  When you're training, it's an interesting example you gave
*  where you're training GPT 3.5,
*  fine tuning it on an example,
*  because I haven't seen kind of written up
*  exactly how their fine tuning works,
*  and if it's actually updating all middle weights,
*  or if it's using a path to base approach
*  or something like that, just adapting the model on top of it.
*  But it gets a little harder to detect
*  when you have this massive pre-trained corpus
*  and you're making very small changes
*  to only percentage of the model weights, for example,
*  across the entire model, but it still happens.
*  One of the really areas that we see,
*  customers doing a lot is fine tuning a model
*  and then just running a series of tests,
*  like we call them canaries,
*  but essentially trying to get a model
*  to auto complete a credit card number or things like that.
*  Here's what I've seen work,
*  starting with the removal of PII or personal data.
*  So first thing, you can use an LM to do it,
*  you can use any art to do it, whatever you want to.
*  The first step is really kind of removing the data
*  you never wanna have show up inside of your model.
*  The second risk, and this is really the risk
*  that trips people out, particularly like when you're working
*  with patient medical data or things like that,
*  is that some combination of attributes,
*  really easy to imagine in a tabular example, right?
*  You might get rid of a name, but you have a height
*  and you've got a zip code and you've got some sort of disease
*  or something like that.
*  And just that combination of attributes
*  can very quickly become identifying.
*  So none of them identify by themselves,
*  put a few attributes together,
*  and you have a real problem from privacy perspective.
*  Same thing with text, the types of styles
*  that people have for writing and things like that,
*  as well as the data that you're training it on,
*  that combination of attributes can become identifying.
*  I suspect that the open-air approach,
*  as you trained on more and more data,
*  would become more likely to start to have things like that,
*  where the combination of attributes, writing styles,
*  anything like that can become identifying.
*  The answer to that across both tabular and text
*  is actually the same type of approach works.
*  There's an approach called differential privacy.
*  Everyone's heard of it.
*  No one really seems to really know how it works
*  and always try to find a simpler and simpler way to do it
*  and to describe it.
*  What differential privacy does
*  is it inserts a quantitative level of noise into your data.
*  And so when you're training machine learning model,
*  if you're training an LLM in this case,
*  you're training with differentially private tuning,
*  for example, it's inserting noise into the optimizer
*  and clipping gradients on the way out.
*  And what that's making sure is that
*  some rare combination of words inside of your data,
*  like, hey, my name's Alex, I'm six feet,
*  I live in, you know, whatever, Southern California,
*  something like that,
*  doesn't become memorized and replayed by the model.
*  So essentially you can guarantee
*  either a training set example, right?
*  So per example or per entity inside of the data,
*  it could be a set of examples about an individual user.
*  You can guarantee that none of the tokens
*  inside of that data set will be replayed
*  directly by the model.
*  And that's so important when you are training
*  on compliance control data.
*  So we've got how many different customers we have going on
*  with different like healthcare organizations
*  that are trying to train on doctors' notes
*  or, you know, customer support records
*  or things like that where you need to make sure
*  the model does not memorize a customer name or replay it
*  or a combination of attributes there.
*  So things like differential privacy give you a tool
*  that you can say, it's no longer that I think
*  the model didn't memorize it
*  and I haven't been able to extract it.
*  You can actually say like with a level of confidence
*  that given the way we look at individual training example
*  or record, I can guarantee you that the model
*  will not be able to replay that
*  or will not have memorized to be able to replay that example.
*  So in the tabular world,
*  this has really opened the doors up for us.
*  We've got a couple of national level healthcare organizations
*  that have been able to get approvals
*  to share data between hospitals
*  by training not just on de-identified data,
*  so not just removing names from patient medical records,
*  but in this case, creating a synthetic version
*  of those patient medical records
*  where you know that the model did not memorize
*  my combination of zip code and height and gender
*  or things like that that could become identifying.
*  With those kind of like actual mathematical guarantees,
*  it becomes possible.
*  So super excited about differentially private fine tuning,
*  particularly in the LLM space.
*  When you look at small companies that are trying to train
*  those models on their demand specific data,
*  but they hit compliance or privacy issues,
*  it gives you a tool that it's not just a best guess
*  or we think that it's gonna be fine.
*  You can actually convince yourself
*  that the model is not gonna return something that it shouldn't.
*  As you do the training, you've taken the gradients
*  and you're working your way through back propagation.
*  You are literally adding a noise factor
*  to the updates to the weights.
*  For each subsequent token generation.
*  And that basically allows you to say,
*  we've kind of essentially blurred the picture in aggregate.
*  This is probably, I guess, like a trade off there
*  where you probably can, the model converges more slowly,
*  I guess, almost by definition, but without learning the stuff.
*  Yeah, that's such an interesting thing
*  because research has been coming out recently.
*  We had a conference where we ran on synthetic data
*  and we had some folks from Google come in
*  and talk about some of the research they're doing.
*  And that's exactly right when you're introducing
*  a level of noise into the data,
*  it requires more training time
*  to get down to the same level of accuracy.
*  One of the things that's really interesting
*  with this approach is that,
*  and this increases compute requirements,
*  but there's a theory that by really increasing
*  the batch size, bigger and bigger and bigger
*  that you're sending into the model at any given point.
*  So it's gonna increase your computational complexity here,
*  but you can use differentially private techniques
*  with increasing larger batch sizes
*  and approach the same level of accuracy as real world data.
*  So in this sense, you're kind of getting privacy
*  without a real hit on utility of the data,
*  but essentially by more compute budget and more data,
*  it becomes possible to reach the same level of accuracy
*  that you would if you just trained on the data itself,
*  which is pretty exciting.
*  So that's pretty new.
*  From what we've seen using Gradle today,
*  you're going to have a utility hit
*  using a differential privacy, especially on small data sets.
*  It makes a lot more sense when you get into a data set
*  where you've got 100,000 or more examples.
*  Essentially that level of noise it has to introduce
*  to blur out somebody of a particular zip code
*  is a lot lower.
*  That's why you've seen differential privacy, for example,
*  the US Census Bureau uses it.
*  Google and Apple use it on the next keyword prediction
*  or emoji prediction when you're typing a text.
*  At that scale, then differential privacy
*  really starts to work.
*  But I am personally really excited about this.
*  Like public, you know, LLM's trained on public data.
*  You're fine tuning it on a private data set
*  and you're introducing differential privacy as you do that.
*  Large batch sizes, plus like being able
*  to interleave public examples
*  will help a model converge really quickly.
*  And I think in a lot of cases,
*  we got into the weeds there a little bit,
*  but it is like the key to unlocking AI
*  for regulated industries that are gonna have
*  to convince a regulator that there's no way
*  that this patient who is part of this data set,
*  their identity is gonna be compromised, right?
*  Like, I always love this term,
*  like you want the model to learn about a disease,
*  but not about a patient.
*  This is a really great technique to make sure
*  that you have that separation.
*  That's cool.
*  It's really, I've learned a lot by going down this rabbit hole.
*  So always excited for a journey into the weeds.
*  One last thing I wanted to just get your take
*  on a little bit is there's obviously a ton
*  of activity going on in synthetic data, right?
*  And I would kind of flag Anthropics constitutional AI
*  as kind of interesting version of this,
*  where they're constantly iterating on this HHH basis
*  to make things more helpful and honest and harmless.
*  And then, and so that seems to work,
*  like it's caused really good.
*  So that's great.
*  And then you see the, I think you even mentioned earlier
*  the synthetic textbooks project out of Microsoft,
*  which also seems to be like a great proof point
*  for the value of synthetic data.
*  Then you see these kinds of weird stories
*  like self-consuming generative models go mad,
*  which I think most people,
*  if they listen to this show, they probably at least saw that
*  blur whenever it came out not too long ago.
*  And there they sort of say,
*  if you do this like generation after generation,
*  things get weird.
*  Do you think there's anything inherently
*  about synthetic data that is kind of a long-term problem?
*  Or do you think that this is all just these kinds
*  of weirdnesses are just reflections of, you know,
*  not having figured out some of the details yet?
*  I'm pretty strongly in the not in the details category.
*  I could have, I could have guessed that.
*  I've also heard another like kind of a story
*  that I've heard as well as like, well, if, you know,
*  GPT-4 and Anthropic and other LLMs are like creating
*  so much content on the internet,
*  is the next cycle of LLMs, you know,
*  gonna have a regression because it's just operating on,
*  you know, data that's already created
*  from previous generation LLMs?
*  I think that's an interesting question.
*  We're gonna see how that kind of plays out over time,
*  but I would newly posit that in a lot of cases,
*  LLMs for where we are today can generate
*  and often do generate, which is why we do it,
*  like a higher quality version of the data that was fed
*  than what it originally started with.
*  I think so many people use this today.
*  We use Grammarly to improve our text.
*  Sometimes we run an email through an LLM
*  and kind of ask it to help us make some improvements
*  or things like that.
*  So I think the signal inside of there,
*  and that's kind of what came out of that,
*  textbooks are all you need paper,
*  is a very promising thing.
*  I don't think this is fully understood yet,
*  but the idea that synthetic data can be kind of a cleaner,
*  more diverse version of, you know,
*  the limited data you might be starting with
*  is a really powerful idea
*  that I think we're gonna see from.
*  So I'm optimistic that these models,
*  and I would say that maybe the MAT example
*  is just an example of an opportunity to configure things
*  or kind of work with them better,
*  that we aren't moving towards some sort of mode collapse
*  or anything like that with synthetic data,
*  feeding synthetic data,
*  as long as the data that we're generating is high quality
*  and ideally improving on the data that you have,
*  then I think we'll be in a good spot.
*  That's gonna be playing out.
*  So I'm really curious to see how that works out.
*  Yeah, the dynamics certainly of the future of the internet
*  and, you know, a changing mix of content being published there
*  is definitely gonna be another
*  just fascinating society scale story.
*  So anything else that you wanted to touch on
*  that we didn't get to?
*  No, I think it's been an awesome conversation.
*  I was just kind of laughing about the last topic
*  and, you know, as long as like every LM generation
*  doesn't start with, you know, I'm a helpful AI assistant,
*  like, how can I help you or let me explain this for you?
*  The things that we see coming out of LM's all the time,
*  I think that we'll be moving in the right direction.
*  So definitely enjoyed the conversation today
*  and thanks for inviting me on.
*  Alex Watson, founder and chief product officer at Griddle AI,
*  thank you for being part of the cognitive revolution.
*  It is both energizing and enlightening
*  to hear why people listen
*  and learn what they value about the show.
*  So please don't hesitate to reach out via email
*  at tcr at turpentine.co or you can DM me
*  on the social media platform of your choice.
*  Omniki uses generative AI to enable you to launch
*  hundreds of thousands of ad iterations that actually work
*  customized across all platforms with a click of a button.
*  I believe in Omniki so much that I invested in it
*  and I recommend you use it too.
*  Use Cogrev to get a 10% discount.
